import { ethers } from "ethers";

const mnemonic = ethers.Mnemonic.fromEntropy(ethers.randomBytes(32));
const wallet = ethers.Wallet.fromPhrase(mnemonic.phrase);

console.log("wallet.address:", wallet.address);
console.log("wallet.mnemonic.phrase:", wallet.mnemonic.phrase);
console.log("wallet.privateKey:", wallet.privateKey);
