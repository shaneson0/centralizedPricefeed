// SPDX-License-Identifier: MIT
pragma solidity 0.6.11;

import "./Dependencies/SafeMath.sol";
import "./Interfaces/IERC2362.sol";
import "./Interfaces/IPriceFeed.sol";
import "./Dependencies/Initializable.sol";
import "./Dependencies/CheckContract.sol";

contract PriceFeed is CheckContract, IPriceFeed, Initializable {
    using SafeMath for uint256;

    uint constant public TARGET_DIGITS = 18;

    // CFX/USDT assertID
    bytes32 constant public assetID = bytes32(0x65784185a07d3add5e7a99a6ddd4477e3c8caad717bac3ba3c3361d99a978c29);

    struct WitnetResponse {
        int256 value;
        uint256 _timestamp;
        uint256 status;
    }

    IERC2362 public witnet;
    uint public lastGoodPrice;

    event LastGoodPriceUpdated(uint _lastGoodPrice);

    // --- Dependency setters ---

    function initialize(address _IWitnetCFXUSDTAddress) public initializer {
        checkContract(_IWitnetCFXUSDTAddress);
        witnet = IERC2362(_IWitnetCFXUSDTAddress);
        WitnetResponse memory witnetResponse = _getCurrentWitnetResponse(assetID);
        _storePrice(witnetResponse);
    }

    function getPrice() external view returns (uint) {
        return lastGoodPrice;
    }

    function fetchPrice() external override returns (uint) {
        WitnetResponse memory witnetResponse = _getCurrentWitnetResponse(assetID);
        _storePrice(witnetResponse);
        return lastGoodPrice;
    }

    function _getCurrentWitnetResponse(bytes32 _assetID) internal view returns(WitnetResponse memory response) {
        try witnet.valueFor(_assetID) returns (
            int256 value,
            uint256 _timestamp,
            uint256 status
        ) {
            response.value = value;
            response._timestamp = _timestamp;
            response.status = status;
        } catch {
            // If call to Chainlink aggregator reverts, return a zero response with success = false
            return response;
        }
    }

    function _storePrice(WitnetResponse memory witnetResponse) internal {
        require(witnetResponse.status == 200, "witnet Response is not 200. response error.");
        uint goodPrice = _scaleWitnetPriceByDigits(uint(witnetResponse.value), 6);
        if (goodPrice != lastGoodPrice) {
            lastGoodPrice = goodPrice;
            emit LastGoodPriceUpdated(lastGoodPrice);
        }
    }

    function _scaleWitnetPriceByDigits(uint _price, uint _answerDigits) internal pure returns (uint) {
        /*
        * Convert the price returned by the Chainlink oracle to an 18-digit decimal for use by Liquity.
        * At date of Liquity launch, Chainlink uses an 8-digit price, but we also handle the possibility of
        * future changes.
        *
        */
        uint price;
        if (_answerDigits >= TARGET_DIGITS) {
            // Scale the returned price value down to Liquity's target precision
            price = _price.div(10 ** (_answerDigits - TARGET_DIGITS));
        }
        else if (_answerDigits < TARGET_DIGITS) {
            // Scale the returned price value up to Liquity's target precision
            price = _price.mul(10 ** (TARGET_DIGITS - _answerDigits));
        }
        return price;
    }

}

