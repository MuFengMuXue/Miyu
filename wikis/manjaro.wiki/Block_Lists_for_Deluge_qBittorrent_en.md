[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Block+Lists+for+Deluge+%26+qBittorrent&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Block_Lists_for_Deluge_%26_qBittorrent "Block Lists for Deluge & qBittorrent (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Block_Lists_for_Deluge_%26_qBittorrent/tr "Deluge ve qBittorrent için Engelleme Listeleri (17% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Block_Lists_for_Deluge_%26_qBittorrent/fr "Listes de blocage pour Deluge & qBittorrent (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Block_Lists_for_Deluge_%26_qBittorrent/ru "Списки блокировки для Deluge и qBittorrent (100% translated)")

## Contents

-   [[1] [Firstly, are Block Lists worth the trouble?]](#Firstly.2C_are_Block_Lists_worth_the_trouble.3F)
-   [[2] [Finding a Block List]](#Finding_a_Block_List)
-   [[3] [Block List installation]](#Block_List_installation)
    -   [[3.1] [The Quick Way]](#The_Quick_Way)
        -   [[3.1.1] [For Deluge]](#For_Deluge)
        -   [[3.1.2] [For qBittorrent]](#For_qBittorrent)
    -   [[3.2] [The Slower Way for Deluge]](#The_Slower_Way_for_Deluge)

## [][Firstly, are Block Lists worth the trouble?]

This is a highly informative article written by a professional in the IT Security industry. Unfortunately, the full article is no longer available. This is a small part of the start of his article, just to get you going:

    IP Block Lists Myths Misconceptions

        Written by Moore

    Table of contents

       IP Block Lists Myths Misconceptions
       Myths and Urban Legends
       Blocklists give 100% protection
       Companies regularly change IP's
       Blocklists block billions of innocent people
       Blocklists put you at greater risk
       Block lists achieve absolutely nothing
       Bust The Myths

    Over the years we have heard all kinds of false and incorrect
    information posted around the net regarding the use of
    blocklists as a unreliable form of protection against a wide
    range of internet based threats.

    This has led to the development of common misconceptions about
    the blocklists among many users.

    Some of this false information may be part of a deliberate
    campaign to discredit the blocklists and their maintainers, or
    an attempt to trick people into lowering their defences by
    convincing people they are either more at risk or wasting their
    time.

    While in some cases the false information has been outright
    fabricated lies intended to do damage, it also seems that a lack
    of technical knowledge mixed with extremely poor research simply
    results in bad and incorrect information being spread with no
    attempt to seek out the actual facts.

    Often you'll see different kinds of insults on discussion forums
    from people who just want to ridicule other p2p users that are
    discussing the use of a blocklist.

Taken from: http://blocklistpro.com/guides/ip-block-lists-myths-misconceptions/all-pages.html (No longer available)

\

## [Finding a Block List]

The most time consuming problem was finding a block list for Deluge to import.

If you want to use a Block list with Deluge, open the Preferences panel, where you will find a Plugins option, a long way down the list on the left hand side; select it, then in the Plugins pane select (tick) the built in Block list plugin.

One source for a block list is the one that eMule uses. It can be found at [http://hostex.de/1316700423](http://hostex.de/1316700423).

The added bonus is that you can use eMule block list in other torrent clients. It has also been tested in qbittorrent.

Another option for a block list can be found at [http://john.bitsurge.net/public/biglist.p2p.gz](http://john.bitsurge.net/public/biglist.p2p.gz).

## [Block List installation]

### [The Quick Way]

#### [For Deluge]

Here is the installation path for the unzipped contents after unzipping the file & calling it *ipfilter.dat* :

    ~/.config/deluge/plugins/ipfilter.dat

\

#### [For qBittorrent]

Here is the installation path for the unzipped contents:

    ~/.config/qBittorrent/ipfilter.dat

\

### [The Slower Way for Deluge]

The Deluge blocklist plugin can be found at [https://dev.deluge-torrent.org/wiki/Plugins/Blocklist](https://dev.deluge-torrent.org/wiki/Plugins/Blocklist).

Which means, whilst still in the Plugins pane of the Deluge Preferences, select the Install Plugin button & then navigate with the file requester to where you have the eMule ipfilter.dat & then type the path to it in the location field (it opens up once you start navigating in the file requester), using the following format:

    file:///home/<username>//ipfilter.dat

After that it may be a good idea to restart Deluge to initialise the block list.