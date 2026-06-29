# Ethereum

The Ethereum Project provides an open-source, distributed, blockchain-based platform for so-called smart contracts.

## Clients
## Go Ethereum
Go Ethereum, the official Go implementation of the Ethereum protocol, is available as the  package.

Create an account with .

The client can be started with , and it will proceed to download several gigabytes of blockchain data. This will take a very long time. This time can be shortened with

 $ geth --syncmode full --cache=1024

Higher cache values appear to speed up the process morehttps://ethereum.stackexchange.com/questions/603/help-with-very-slow-mist-sync#3805.

Optionally, start the client with  to get a JavaScript console for more meaningful interaction.
This console can then be attached-to from another terminal or remotely with .

To check balances in the console or attach modes, use .

To start CPU mining, use .  This is far less efficient than GPU mining, and ethereum.org does not recommend it.

## GPU Mining with geth
GPU mining with geth has been discontinued.

## Ethereum Wallet
You can install the Ethereum Wallet via the  package.
