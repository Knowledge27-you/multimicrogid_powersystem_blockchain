const { ethers } = require("hardhat");

async function main() {
    const tokenAddress = "0xFC0c18234210241b34cB8Bf8e0Bb9F9F23263424";
    const recipient = "0x541D16f0246Be1f926Ec162A5C7E98dF0089d43f";
    const amount = "10000";

    const EnergyToken = await ethers.getContractFactory("EnergyToken");
    const token = EnergyToken.attach(tokenAddress);
    const mintAmount = ethers.utils.parseUnits(amount, 18);

    const tx = await token.mint(
        recipient,
        mintAmount
    );

    await tx.wait();

    console.log(
        `Minted ${amount} ETK to ${recipient}`
    );

} 

main()
.then(() => process.exit(0))
.catch((error) => {
    console.error(error);
    process.exit(1);
});