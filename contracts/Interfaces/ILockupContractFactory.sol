// SPDX-License-Identifier: MIT

pragma solidity 0.6.11;
    
interface ILockupContractFactory {
    
    // --- Events ---

    event LQTYTokenAddressSet(address _lqtyTokenAddress);
    event LockupContractDeployedThroughFactory(
            address _lockupContractAddress, address _beneficiary,
            uint _vestingStartTime, uint _vestingEndTime, address _deployer);

    // --- Functions ---

    function setAddresses(address _lqtyTokenAddress) external;

    function deployLockupContract(address _beneficiary, uint _vestingStartTime, uint _vestingEndTime) external;

    function isRegisteredLockup(address _addr) external view returns (bool);
}
