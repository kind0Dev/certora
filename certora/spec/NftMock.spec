/*
* VErification of NftMock
*/
methods {
    function totalSupply() external returns uint256 envfree;
    function mint() external;
    function balanceOf(address) external returns uint256 envfree; 
}

// invariant totalSupplyIsNotNegative()
//     totalSupply() >= 0;

rule minting_mints_one_nft() {
    // Arrange
    env e;
    address minter;
    require e.msg.value == 0;
    require e.msg.sender == minter;
    mathint balanceBefore = balanceOf(minter);

    // Act
    currentContract.mint(e);

    // Asserts
    assert to_mathint(balanceOf(minter)) == balanceBefore + 1, "can only mint 1 nft";



}
// rule sanity{
//     satisfy true;
// }