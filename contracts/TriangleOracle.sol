
pragma solidity 0.6.11;
import "./Ownable.sol";
import "./Interfaces/IERC2362.sol";

contract TriangleOracle is Ownable, IERC2362 {    

    // 32 + 16 + 16 = 64 bytes
    // default 1e+18 
    struct PriceOracle {
        int256 price;              // 16 bytes
        uint256 timestamp;
        uint256 status;           // 16 bytes
    }
    PriceOracle latestPrice;

    event PutLatestTokenPrice(int256 price, uint256 timestamp, uint256 status);

    function putPrice(bytes32 _id, int256 price, uint256 timestamp) public onlyOwner {
        
        uint256 _status = 200;
        latestPrice = PriceOracle ({
            price: price,
            timestamp: timestamp,
            status: _status
        });

        emit PutLatestTokenPrice(price,timestamp, _status);

    }

    function valueFor(bytes32 _id) external view override returns(int256,uint256,uint256) {
        return (latestPrice.price, latestPrice.timestamp, latestPrice.status);
    }

}


