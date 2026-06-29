# Cardano

Cardano is an open-source blockchain platform based on proof-of-stake. Its flagship cryptocurrency is Ada.

## Running a node
Install  or , which will also install  which can then be started.

By default, the logging is quite verbose. If you would like to tune that down, find the appropriate configuration file (likely  under  and make changes like:

 "TracingVerbosity": "MinimalVerbosity",
 "minSeverity": "Warning",

## Using a wallet
There are several wallets that support Ada. Not mentioned on the site is the CLI tool, .

## cardano-wallet
Install either  or . The latter will also install a systemd service, so you can start  (after also starting the node).

Again, the default logging is quite verbose, and also the wallet will simply stay in memory by default. If you wish to tune down the logging, and write the wallet to disk, edit the systemd service file:
