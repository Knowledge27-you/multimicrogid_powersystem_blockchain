require("@nomiclabs/hardhat-ethers");
require("solidity-coverage");
require("dotenv").config();

const {SEPOLIA_RPC_URL, METAMASK_PRIVATE_KEY} = process.env;

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
    solidity: "0.8.28",
    networks: {
        sepolia: {
            url: SEPOLIA_RPC_URL,
            accounts: [METAMASK_PRIVATE_KEY]
        }
    }
};