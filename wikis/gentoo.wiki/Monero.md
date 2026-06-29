**Resources**

[[]][Home](https://www.getmonero.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Monero "wikipedia:Monero")

[[]][Blog](https://www.getmonero.org/blog)

[[]][[#monero](ircs://irc.libera.chat/#monero)] ([[webchat](https://web.libera.chat/#monero)])

**Monero** is a privacy and security-focused cryptocurrency originating from the 2013 CryptoNote protocol.^[\[1\]](#cite_note-1)^ It uses a combination of ring signatures^[\[2\]](#cite_note-2)^ and zero-knowledge proofs to implement \"Ring Confidential Transactions\" (RingCT)^[\[3\]](#cite_note-3)^ intended to obfuscate the sender, receiver, and amount of a transaction.^[\[4\]](#cite_note-4)^

As these privacy features prevent the use of Bitcoin\'s [SPV (Simplified-Payment-Verification)](https://en.bitcoin.it/wiki/Scalability#Simplified_payment_verification), it is necessary to distribute the software in two separate programs: the wallet and the node. The **Wallet** (Client) software has control over funds and is the minimum needed to make a private transaction and accept payments. The wallet connects to a **Node** (Server) that may run on the same computer or on another computer over the network. The Node connects to the peer-to-peer network, stores and relays transactions, and works together with with other computers on the network to come to a consensus about the order in which they occur.

** Note**\
In general *Wallet* is used to refer both to the client software and the `.keys` file. They are both needed to interact with Nodes.

Cryptocurrencies like Bitcoin use [Proof-of-Work](https://en.wikipedia.org/wiki/Proof_of_work "wikipedia:Proof of work") to make it difficult for an attacker to reverse the order of transactions (which would allow the attacker to [spend funds more than once](https://en.wikipedia.org/wiki/Double-spending "wikipedia:Double-spending")). Unlike Bitcoin, Monero uses a Proof-of-Work system which is designed to mitigate the effectiveness of specialized hardware (ASICs) as opposed to general-purpose CPUs^[\[5\]](#cite_note-5)^. Because of this, it becomes necessary to distribute **Mining Software** for everyday users that may wish to secure the network with their own hardware. This article discusses methods for mitigating [cryptojacking](https://en.wikipedia.org/wiki/Cryptojacking "wikipedia:Cryptojacking") attacks.

** Note**\
Most packages listed here are still on the [GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") overlay. See [this page](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users") for information on how to use GURU.

## Contents

-   [[1] [Wallet Software]](#Wallet_Software)
    -   [[1.1] [Official]](#Official)
        -   [[1.1.1] [Monero CLI]](#Monero_CLI)
        -   [[1.1.2] [Monero GUI]](#Monero_GUI)
    -   [[1.2] [Third party]](#Third_party)
        -   [[1.2.1] [Feather]](#Feather)
-   [[2] [Node software]](#Node_software)
    -   [[2.1] [monerod]](#monerod)
        -   [[2.1.1] [Installation]](#Installation)
        -   [[2.1.2] [Configuration]](#Configuration)
        -   [[2.1.3] [Service]](#Service)
    -   [[2.2] [Cuprate]](#Cuprate)
-   [[3] [Mining Software]](#Mining_Software)
    -   [[3.1] [XMRig]](#XMRig)
        -   [[3.1.1] [Installation]](#Installation_2)
        -   [[3.1.2] [Usage]](#Usage)
        -   [[3.1.3] [Optimization]](#Optimization)
    -   [[3.2] [P2Pool]](#P2Pool)
        -   [[3.2.1] [Installation]](#Installation_3)
        -   [[3.2.2] [Usage]](#Usage_2)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [monerod can\'t sync]](#monerod_can.27t_sync)
-   [[5] [Cryptojacking Prevention]](#Cryptojacking_Prevention)
-   [[6] [Libraries]](#Libraries)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Wallet Software]

### [Official]

The Monero Core team develops the official wallet in CLI & GUI variants. More information about them can be found on the [project\'s download page](https://www.getmonero.org/downloads/).

#### [Monero CLI]

** Note**\
Currently still on GURU

The command-line wallet can be installed by emerging `net-p2p/monero[wallet-cli]`.

It can be summoned with:

`user `[`$`]`monero-wallet-cli`

#### [Monero GUI]

** Note**\
Currently still on GURU, as a binary package

The Graphical wallet is available as a binary package:

`root `[`#`]`emerge --ask net-p2p/monero-gui-bin`

.

The wallet has a Simple and an Advanced mode. Using the former might be a good idea if you are just starting.

### [Third party]

#### [Feather]

** Note**\
Currently still on GURU

[Feather Wallet](https://featherwallet.org/) is a lightweight and simple Qt5/Qt6 implementation of the monero wallet.

[![](/images/thumb/a/a0/Feather_wallet.png/300px-Feather_wallet.png)](https://wiki.gentoo.org/wiki/File:Feather_wallet.png)

[](https://wiki.gentoo.org/wiki/File:Feather_wallet.png "Enlarge")

Feather Wallet appearance

`root `[`#`]`emerge --ask net-p2p/feather`

By default, it\'s configured to connect to a remote node over the internet (and to onion sites if the [tor daemon](https://wiki.gentoo.org/wiki/Tor "Tor") is running).

To connect feather wallet to a local node instead, select File\>Settings\>Network\>Node\>Add custom node(s) and add 127.0.0.1:18081 to the custom nodes list.

## [Node software]

### [monerod]

** Note**\
Currently still on GURU

monerod is the only \"official\" node implementation.

#### [Installation]

`root `[`#`]`emerge --ask net-p2p/monero`

#### [Configuration]

Because monero\'s blockchain (the list of transactions, also called the \"ledger\") can take up quite a lot of space (about 164 GB as of 2025^[\[6\]](#cite_note-6)^) The two most important configuration settings are the directory in which it is stored ([/var/lib/monero] by default), and whether or not it should be \"pruned\". Pruning is an option that reduces storage usage by about 60%, storing an incomplete but usable copy of the blockchain^[\[7\]](#cite_note-7)^. Below is an example configuration file at [/etc/monero/monerod.conf] that changes both of these options:

[FILE] **`/etc/monero/monerod.conf`Setting blockchain directory and pruning**

    data-dir=/your/monero/directory/
    log-file=/your/monero/directory/monero.log
    prune-blockchain=1

See [monerod options](https://docs.getmonero.org/interacting/monerod-reference/) and [monerod.conf](https://docs.getmonero.org/interacting/monero-config-file/) for a more complete list of configuration options

#### [Service]

To start immediately:

`root `[`#`]`rc-service monerod start`

To start the monerod service on system boot, add it to the default runlevel:

`root `[`#`]`rc-update add monerod default`

To get monerod\'s current status:

`user `[`$`]`monerod status`

### [Cuprate]

[Cuprate](https://github.com/Cuprate/cuprate) is an alternate implementation of the monero server software with a focus on performance and security. Its development is intended to improve node diversity and resilience of the Monero network as whole against implementation vulnerabilities (side-channel attacks). It is currently under development and requires a nightly build of rust to compile.

You can still compile it yourself out-of-tree by cloning the [the repo](https://github.com/Cuprate/cuprate) and running `cargo build` if you use a rustup-installed nightly toolchain in your home directory as described in [Rust#Rustup](https://wiki.gentoo.org/wiki/Rust#Rustup "Rust").

## [Mining Software]

To incentivize users to secure the network with Proof-of-Work, 0.6 XMR is randomly rewarded every 2 minutes to a successful miner^[\[8\]](#cite_note-8)^. The average expected return can be calculated by multiplying the [expected hashrate](https://xmrig.com/benchmark), dividing by the total network hashrate, then subtracting the total cost of electricity consumed. See the [monero mining calculator](https://www.monero.how/monero-mining-calculator). Generally speaking, Monero mining is not profitable without access to relatively modern CPUs and cheap electricity, or use of computers for indoor heating. GPU mining is also possible, but it is far less profitable compared to other cryptocurrencies.

While monerod does support mining by itself, it\'s recommended to use a faster mining implementation instead of monerod\'s built-in mining.

### [XMRig]

XMRig is the largest fast implementation of Monero mining. This gentoo package respects the `opencl` USE flag for AMD GPUs, however the use of Nvidia GPUs through CUDA requires a [separate plugin](https://github.com/xmrig/xmrig-cuda).

#### [Installation]

### [USE flags for] [net-misc/xmrig](https://packages.gentoo.org/packages/net-misc/xmrig) [[]] [RandomX, CryptoNight, KawPow, AstroBWT, and Argon2 CPU/GPU miner]

  --------------------------------------------------------- --------------------------------------------------------------------------------------
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)       Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`donate`](https://packages.gentoo.org/useflags/donate)   Set the default donation level to 1% instead of 0
  [`hwloc`](https://packages.gentoo.org/useflags/hwloc)     Use sys-apps/hwloc for CPU affinity support
  [`opencl`](https://packages.gentoo.org/useflags/opencl)   Enable OpenCL support (computation on GPU)
  --------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-29 02:10] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

`root `[`#`]`emerge --ask net-misc/xmrig`

#### [Usage]

If a monero node is running, (localhost on port 18081), solo mining is as simple as

`user `[`$`]`xmrig -u YOUR_MONERO_ADDRESS `

Another option is pool mining, which eliminates the need to run a monero node, and may offer more regular payouts at the cost of increased centralization and fees. Configuration depends on the pool, but usually looks something like:

`user `[`$`]`xmrig -o your-mining-pool.com:port -u YOUR_MONERO_ADDRESS `

#### [Optimization]

Disabling \"hardware prefetchers\" has been shown to increase mining performance by about 30%. This can be done by using the wrmsr command as shown in [/usr/bin/randomx_boost.sh]. XMRig automatically runs this script when run as root.

Enabling \"1GB huge pages\" also yields a slight performance improvement on linux systems, at the cost of using more memory. This is done through the [/usr/bin/enable_1gb_pages.sh] script.

See also the [RandomX Optimization Guide](https://xmrig.com/docs/miner/randomx-optimization-guide)

### [P2Pool]

** Note**\
Currently still on GURU

P2Pool is a decentralized method of spreading out mining rewards into regular payouts, similar to a regular mining pool but with lower fees. The P2Pool software connects to a monero node and exposes a pool that miners such as XMRig can connect to.

#### [Installation]

`root `[`#`]`emerge --ask net-p2p/p2pool`

#### [Usage]

p2pool can be started in the current directory by running

`user `[`$`]`p2pool --host MONERO_NODE_ADDRESS --wallet YOUR_PRIMARY_ADDRESS`

Where `MONERO_NODE_ADDRESS` is the address of the monero node (for example, 127.0.0.1 for a monero node that runs on the same computer), and `YOUR_PRIMARY_ADDRESS` is a monero primary address (begins with a \"4\" as opposed to a secondary address that begins with an \"8\") that will receive the mining reward. Once the P2Pool software finishes connecting to the network, one can start mining with XMRig as if it\'s a normal pool. By default, this is exposed on port 3333:

`user `[`$`]`xmrig -o 127.0.0.1:3333`

There are currently two different networks: p2pool and p2pool-mini. If a computer has a lower hashrate, it may be better to connect to the p2pool-mini network instead by passing the \--mini flag to p2pool:

`user `[`$`]`p2pool --mini --host MONERO_NODE_ADDRESS --wallet YOUR_PRIMARY_ADDRESS`

See also [P2Pool FAQ](https://p2pool.io/#faq)

## [Troubleshooting]

### [][monerod can\'t sync]

Sometimes monerod can get stuck if the computer is forcibly shutdown (for example, electrical outage or running out of battery). This can usually be fixed with [monerod \--db-salvage].

## [Cryptojacking Prevention]

Cryptojacking is the act of hijacking a computer to mine cryptocurrency against the owner\'s will. Because of the CPU-bound nature of Monero\'s Proof-of-Work system (RandomX), it\'s easier for a hacker to capitalize on a victim\'s computing power relative to the rest of the network. However, RandomX also has some features designed to mitigate cryptojacking.

It is often speculated that a large portion of Monero\'s hashrate is a result of cryptojacked \"IoT\" devices (appliances such as cameras, toasters, etc. that contain computers which are unnecessarily connected to the internet). It is important to consider RandomX\'s [Memory-hardness](https://en.wikipedia.org/wiki/Memory-hard_function "wikipedia:Memory-hard function") on low-end devices, which prevents it from running at all on computers with less than 256 MiB of memory, and massively decreases mining efficiency on devices with less than 2080 MiB.

Cryptojacking can often be used to extract additional money from a hacked VPS service at great cost to the client. One feature of RandomX is that efficient miners will necessarily leave a detectable trace in the state of CPU registers. [\"RandomX Sniffer\"](https://github.com/tevador/randomx-sniffer) is a proof-of-concept tool that can be used to detect cryptojacking malware. In theory, VPS providers could use this method to warn clients or prevent cryptojacking though the use of [Virtual Machine Introspection](https://en.wikipedia.org/wiki/Virtual_machine_introspection "wikipedia:Virtual machine introspection"). If the client has a firewall installed, then they can also just monitor outbound connections to common Monero pools or to the P2Pool network.

Lastly, a common another attack vector is web mining (sometimes referred to as \"Drive-by Mining\"), which involves the insertion of mining scripts into webpages, taking advantage of the computers that access the web page. Web miners are particularly inefficient because of the decrease in branch prediction speeds and the lack of directed rounding support for floating point operations in JavaScript and WebAssembly. As such, web mining is typically orders of magnitude less efficient than mining natively. When hosting a web service, pay attention to securing the website against [cross-site scripting attacks](https://en.wikipedia.org/wiki/Cross-site_scripting "wikipedia:Cross-site scripting"). As a user there is not much that can be done to avoid web mining besides installing an ad-blocker or disabling JavaScript altogether. Some browsers like [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") have default settings to block common crypto mining scripts. It\'s also important to consider [Web extensions](https://blog.chromium.org/2018/04/protecting-users-from-extension-cryptojacking.html) as another vector for web mining.

## [Libraries]

[Monero-rs](https://github.com/monero-rs/monero-rs) is a similar monero library for the Rust programming language.

[MoneroPy](https://github.com/bigreddmachine/moneropy) is a demonstration of some programming concepts in monero. See also [MiniNero](https://github.com/monero-project/mininero) and the [Zero to Monero](https://www.getmonero.org/library/Zero-to-Monero-2-0-0.pdf) tutorial.

## [External resources]

-   N. Alsalami and B. Zhang, [SoK: A Systematic Study of Anonymity in Cryptocurrencies](https://ieeexplore.ieee.org/document/8937681), 2019 IEEE Conference on Dependable and Secure Computing (DSC), Hangzhou, China, 2019, pp. 1-9, doi: 10.1109/DSC47296.2019.8937681.
-   RandomX proof-of-work (PoW) algorithm --- [https://github.com/tevador/randomx](https://github.com/tevador/randomx)
-   Shen Noether, [Ring Signature Confidential Transactions for Monero](https://eprint.iacr.org/2015/1098), 2015 Cryptology ePrint Archive, Paper 2015/1098.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://web.archive.org/web/20201028121818/https://cryptonote.org/whitepaper.pdf](https://web.archive.org/web/20201028121818/https://cryptonote.org/whitepaper.pdf)]]
2.  [[[↑](#cite_ref-2)] [[https://www.getmonero.org/resources/moneropedia/ringsignatures.html](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)]]
3.  [[[↑](#cite_ref-3)] [[https://www.getmonero.org/resources/moneropedia/ringCT.html](https://www.getmonero.org/resources/moneropedia/ringCT.html)]]
4.  [[[↑](#cite_ref-4)] [[https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf)]]
5.  [[[↑](#cite_ref-5)] [[https://github.com/tevador/RandomX/blob/master/doc/design.md](https://github.com/tevador/RandomX/blob/master/doc/design.md)]]
6.  [[[↑](#cite_ref-6)] [[https://localmonero.co/blocks/stats/blockchain-growth](https://localmonero.co/blocks/stats/blockchain-growth)]]
7.  [[[↑](#cite_ref-7)] [[https://www.getmonero.org/resources/moneropedia/pruning.html](https://www.getmonero.org/resources/moneropedia/pruning.html)]]
8.  [[[↑](#cite_ref-8)] [[https://localmonero.co/knowledge/monero-tail-emission](https://localmonero.co/knowledge/monero-tail-emission)]]