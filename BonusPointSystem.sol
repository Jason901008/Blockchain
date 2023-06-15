pragma solidity 0.5.17;

contract RewardsCalculator {
    address public Server;
    address public Costomer;
    uint public Bonus;
    uint public TotalRewards;
    // constructor function
    constructor(address costomer) public {
        Server = msg.sender;
        Costomer = costomer;
        TotalRewards = 0;
    }
    // call this function to add miles
    function AddBonus(uint cost) public {
        Bonus = cost;
        ComputeTotalRewards();
    }
    function ComputeTotalRewards() private {
        TotalRewards += Bonus;
    }
}
