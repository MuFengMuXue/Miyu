# I2P

I2P is an anonymizing network, offering a simple layer that identity-sensitive applications can use to securely communicate. All data is wrapped with several layers of encryption, and the network is both distributed and dynamic, with no trusted parties. Many applications are available that interface with I2P, including mail, peer-peer, IRC chat, and others.

Two implementations of I2P are as follows:

* I2P — Written in Java. First development. Most interactive and user-friendly web user interface and features, has a built-in client of email (SusiMail) and torrent (I2PSnark).
* i2pd — Alternative development. Does not require Java, is written in C++, consumes less memory and CPU.

More, less stable, clients are listed on the i2p website == I2P (Java suite) ==

## Installation
The standard I2P suite is available with the  and  packages. Both require a Java Runtime Environment. A recent Sun/Oracle Java or OpenJDK version with "mixed mode" support is recommended, "interpreted mode" could result in performance degradation, check with "java -version".

The I2P homepage also provides a [https://i2p.net/en/download#unix pre-compiled binary which includes command line (headless) option and can be installed in the user's home directory. Such an installation will auto update through the i2p network with signed zip packages directly from the i2p developers.

## Usage
Start/enable  in case of . For the pre-compiled binary, run  in a terminal and see the available options.

Open your browser of choice and visit the I2P welcome page at   for the suite (see the FAQ).
From here you can navigate to I2Ps configuration and statistics pages, and links to Eepsites.
Also, be aware that eepsites are unavailable until the daemon has bootstrapped to the network, which can take several minutes.
In order to visit eepsites configure your browser to use the local proxy:

 HTTP  127.0.0.1 4444

## Eepsite
To make an eepsite, follow the I2P instructions, but keep in mind that the home directory will apply to the i2p user whose home directory is  as shown in the AUR i2p.install file.

## i2pd (C++ Alternative)
## Installation
Install the  package for the daemon written in C++ which may suit hardware with limited resources or  for the development version.

## Usage
Start/enable .

The configuration is made in .
Open your browser of choice and visit the I2P welcome page at
In order to visit eepsites configure your browser to use the local proxy:

 HTTP  127.0.0.1 4444
 SOCKS 127.0.0.1 4447

i2pd has no built-in email client, filesharing or webserver for Eepsite. See the How-To / Tutorials in upstream documentation for more details, also for chat servers, XMPP / Jabber or RetroShare.

## Eepsite
Tools required to register your site on http://reg.i2p/add and/or http://stats.i2p/i2p/addkey.html are included in , see the readme for usage documentation.

## Troubleshooting
## Firefox: wrong redirect to a search engine
After entering an i2p page, e.g. "zzz.i2p" Firefox will try to redirect wrongly to duckduckgo.com or www.google.com.
Since most i2p does not provide https, enter your address always explicit with the http protocol prefix, e.g. http://zzz.i2p/

Alternatively, navigate to about:config and create a new boolean config variable named  and set its value to .
