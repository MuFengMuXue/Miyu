# RuneScape

From Wikipedia:
:RuneScape is a fantasy massively multiplayer online role-playing game (MMORPG) developed and published by Jagex, released in January 2001. RuneScape was originally a browser game built with the Java programming language; it was largely replaced by a standalone C++ client in 2016. The game has had over 300 million accounts created and was recognised by the Guinness World Records as the largest and most-updated free MMORPG.
From Wikipedia:
:Old School RuneScape is a separate incarnation of RuneScape released on 22 February 2013, based on a copy of the game from August 2007. Old School RuneScape receives regular content updates, which must be voted on by its players before they can be added to the game.

## Installation
The installation alternatives offer different features to make a choice on, and may use different dependencies.

## Jagex Launcher
The Jagex Launcher offers installation and shortcuts to each game client Executable and does not Linux support on release.

## Unofficial client
jagex-launcher-linux is a repository that "contains community projects to install the Jagex Launcher and use Jagex Accounts in Linux" as recommended by Jagex Support.

Bolt is a third-party launcher. Install with the  package or with Flatpak as  from Flathub.

## RuneScape
## Official client
Install the official RuneScape NXT client with the  package. The official client can also be installed with Flatpak as  from Flathub.

## Old School RuneScape (OSRS)
## RuneLite
RuneLite is an open-source alternative to other third-party Old School RuneScape clients. It is available on the AUR: .

To enable the GPU feature within RuneLite, ensure you meet the requirements and have updated to the latest version of .

## OSRS-Launcher
osrs-launcher is a repackaging of the mac version of the official Old School RuneScape launcher. It is available for installation from the AUR, .

## Steam
It is worth mentioning that RuneScape and OSRS are individually available on Steam, which offers its own Compatibility layer Proton. Steam is a separate program, and not recommended if unfamiliar. The Steam releases predate the official #Jagex Launcher release by around three years, and lack support for Jagex Account features such as multiple characters.

## Troubleshooting
## Audio issues
The Java client (jagexappletviewer.jar) requires  to be installed for sound to work properly. Otherwise there will be no in-game sound or other applications will not be able to play audio due to the client claiming direct access to  devices. For more details, see PulseAudio#ALSA.

## SSL errors
If you receive an error like this (with RuneLite or otherwise):

 javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake_failure

This error may be due to Java's new TLSv1.3 implementation. Try adding  to your client's launch options.
For example:

 $ java -Djdk.tls.client.protocols=TLSv1.2 -jar RuneLite.jar
