/**
 * Use this file to configure your truffle project. It's seeded with some
 * common settings for different networks and features like migrations,
 * compilation and testing. Uncomment the ones you need or modify
 * them to suit your project as necessary.
 *
 * More information about configuration can be found at:
 *
 * trufflesuite.com/docs/advanced/configuration
 *
 * To deploy via Infura you'll need a wallet provider (like @truffle/hdwallet-provider)
 * to sign your transactions before they're sent to a remote public node. Infura accounts
 * are available for free at: infura.io/register.
 *
 * You'll also need a mnemonic - the twelve word phrase the wallet uses to generate
 * public/private key pairs. If you're publishing your code to GitHub make sure you load this
 * phrase from a file you've .gitignored so it doesn't accidentally become public.
 *
 */

// const HDWalletProvider = require('@truffle/hdwallet-provider');
// const infuraKey = "fj4jll3k.....";
//
// const fs = require('fs');
// const mnemonic = fs.readFileSync(".secret").toString().trim();

module.exports = {
  /**
   * Networks define how you connect to your ethereum client and let you set the
   * defaults web3 uses to send transactions. If you don't specify one truffle
   * will spin up a development blockchain for you on port 9545 when you
   * run `develop` or `test`. You can ask a truffle command to use a specific
   * network from the command line, e.g
   *
   * $ truffle test --network <network-name>
   */

  networks: {
    mainnet: {
      host: 'test.confluxrpc.com',     // Conflux provides public RPC services for testnet
      port: 80,
      network_id: 1,       // Conflux testnet networkId is 1
      privateKeys: ['0B6A7A4CF9C143421D948E6E33C7C84BF6882E39F8B2EE56FD29303E659E4F3B']  //  Adding the account private key used for sending transactions

    },
    testnet: {
      host: 'test.confluxrpc.com',     // Conflux provides public RPC services for testnet
      port: 80,
      network_id: 1,       // Conflux testnet networkId is 1
      privateKeys: ['0B6A7A4CF9C143421D948E6E33C7C84BF6882E39F8B2EE56FD29303E659E4F3B']  //  Adding the account private key used for sending transactions
    },
    localhost: {
      host: 'localhost',     // Conflux provides public RPC services for testnet
      port: 8545,
      network_id: 31337,       // Conflux testnet networkId is 1
      privateKeys: ['0B6A7A4CF9C143421D948E6E33C7C84BF6882E39F8B2EE56FD29303E659E4F3B']  //  Adding the account private key used for sending transactions
    },
    localhost_junior: {
      host: 'localhost',     // Conflux provides public RPC services for testnet
      port: 12537,
      network_id: 999,       // Conflux testnet networkId is 1
      privateKeys: ['3cc9a51625d7c4592382dcd2741c91f3076ca64ad7efffc210bb7c57056c98bc']  //  Adding the account private key used for sending transactions
    }
  },
  // Set default mocha options here, use special reporters etc.
  mocha: {
    // timeout: 100000
  },

  // Configure your compilers
  compilers: {
    solc: {
      version: "0.6.11",    // Fetch exact version from solc-bin (default: truffle's version)
      docker: true,        // Use "0.5.1" you've installed locally with docker (default: false)
      settings: {          // See the solidity docs for advice about optimization and evmVersion
       optimizer: {
         enabled: false,
         runs: 200
       },
       evmVersion: "byzantium"
      }
    }
  },

  // Truffle DB is currently disabled by default; to enable it, change enabled: false to enabled: true
  //
  // Note: if you migrated your contracts prior to enabling this field in your Truffle project and want
  // those previously migrated contracts available in the .db directory, you will need to run the following:
  // $ truffle migrate --reset --compile-all

  db: {
    enabled: false
  }
};
