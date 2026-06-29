# Btcpayserver

BTCPayServer is an open source payment processor for crypto currencies licensed under the MIT license. While Bitcoin is supported natively, other crypto currencies are supported via extensions. The software is written in C# and is accessed over the web browser. The core idea of the project is to give merchants full control over payments without a middleman.

## Installation
Install the package .

## Configuration
## Bitcoin
BTCPayServer communicates with the Bitcoin node via RPC. For this, those values need to be set. Edit  and set  and . Moreover, a whitelist must be defined with .

## Optional configuration
Usage of the lightning network is optional. Information on the lightning connection string can be found here. Decide for one lightning implementation.

## LND
Execute  as a private key needs to be generated. Then, execute  and create your needed wallet or restore an existing one. Edit  and add the following settings.

## Usage
Start/enable

## Lightning
## Core Lightning
{{ic|lightningd --bitcoin-rpcpassword "${bitcoin_rpc_password}" --bitcoin-rpcuser "${USER}" --log-level info --network bitcoin --rpc-file "${XDG_STATE_HOME}"/lightning/lightning-rpc}}

## LND
{{ic|lnd --bitcoin.active --bitcoin.mainnet --bitcoin.node bitcoind --bitcoind.rpcpass "${bitcoin_rpc_password}" --bitcoind.rpcuser "${USER}" --bitcoind.zmqpubrawblock tcp://127.0.0.1:28332 --bitcoind.zmqpubrawtx tcp://127.0.0.1:28333 --externalip localhost}}

## NBXplorer
{{ic|1=nbxplorer --btcrpcpassword "${bitcoin_rpc_password}" --btcrpcuser "${USER}" -d "${XDG_DATA_HOME}"/nbxplorer/ --postgres "User ID=\"${USER}\";Password=\"${postgresql_password}\";Host=localhost;Port=5432;Database=nbxplorer;"}}

## BTCPayServer
When running no lightning node, just skip the option .

## With Core Lightning
{{ic|1=btcpayserver --btclightning type=clightning;unix://"${XDG_STATE_HOME}"/lightning/lightning-rpc -d "${XDG_DATA_HOME}"/btcpayserver/ --explorerpostgres "User ID=\"${USER}\";Password=\"${postgresql_password}\";Host=localhost;Port=5432;Database=nbxplorer;\" --sqlitefile btcpayserver.db}}

## With LND
{{ic|1=btcpayserver --btclightning type=lnd-rest;server=https://127.0.0.1:8080/;macaroonfilepath=/home/"${USER}"/.lnd/data/chain/bitcoin/mainnet/admin.macaroon;certthumbprint="$(openssl x509 -noout -fingerprint -sha256 -in ~/.lnd/tls.cert  sed -e "s/.*=//;s/://g")" -d "${XDG_DATA_HOME}\"/btcpayserver/ --explorerpostgres "UserID=\"${USER}\";Password=${postgresql_password};Host=localhost;Port=5432;Database=nbxplorer;\" --sqlitefile btcpayserver.db}}
