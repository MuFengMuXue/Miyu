Other languages:

[English] • ‎[русский](//wiki.manjaro.org/index.php?title=Sync_dynamic_IP_with_openDNS_service_via_ddclient/ru "Синхронизация динамического IP с сервисом openDNS через ddclient (100% translated)")

## Contents

-   [[1] [Requirements - Account on openDNS]](#Requirements_-_Account_on_openDNS)
-   [[2] [Setup openDNS in system settings]](#Setup_openDNS_in_system_settings)
-   [[3] [Setup openDNS in ddclient]](#Setup_openDNS_in_ddclient)
-   [[4] [See Also]](#See_Also)

\

[![Open-dns-logo.png](/images/9/9a/Open-dns-logo.png)](//wiki.manjaro.org/index.php?title=File:Open-dns-logo.png)

## [Requirements - Account on openDNS]

Service ddclient for sync dynamic IP need account in OpenDNS. You need:

-   Create an account on [openDNS](https://store.opendns.com/get/home-free) and login to [OpenDNS Dashboard](https://dashboard.opendns.com/). Create a new Network in the settings.
-   Login on [DNS-O-Matic Site](https://www.dnsomatic.com/account/) using e-mail and password from OpenDNS.
-   Add new Service. From list select OpenDNS. Click button **Update account info** for sync OpenDNS Dashboard settings with DNS-O-Matic.

\

## [Setup openDNS in system settings]

Set DNS addresses in resolv.conf file:

[user \$ ][ sudo nano /etc/resolv.conf.head [COPY TO CLIPBOARD]]

\

with code:\
`nameserver 208.67.222.222`\
`nameserver 208.67.220.220`\

\

**Note**

------------------------------------------------------------------------

If Your ISP provide IPv6 support, add these DNS IPv6 addresses entries in next lines in the */etc/resolv.conf.head* file:

IPv6 DNS server addresses are:\
`nameserver 2620:119:35::35`\
`nameserver 2620:119:53::53`

Does not provide any level of filtering:\
`nameserver 2620:0:ccc::2`\
`nameserver 2620:0:ccd::2`

## [Setup openDNS in ddclient]

**#1** Install ddclient and ddclient dispatcher for NetworkManager:

[user \$ ][ pamac build networkmanager-dispatcher-ddclient [COPY TO CLIPBOARD]]

\

**#2** Create backup a *ddclient.conf* file:

[user \$ ][ sudo cp /etc/ddclient/ddclient.conf /etc/ddclient/ddclient.conf.skel [COPY TO CLIPBOARD]]

\

**#3** Open *ddclient.conf* file in text editor.

[user \$ ][ sudo nano /etc/ddclient/ddclient.conf [COPY TO CLIPBOARD]]

\

**#4** Delete current content, paste in:\

**Note**

------------------------------------------------------------------------

**REMEMBER** - replace values **email_address**, **password** with correct values.

------------------------------------------------------------------------

` daemon=1800`\
`syslog=yes`\
`pid=/var/run/ddclient.pid`\
`ssl=yes`\
`use=web, web=myip.dnsomatic.com`\
`server=updates.dnsomatic.com`\
`protocol=dyndns2`\
`login=`**`email_address`**\
`password=`**`password`**\
`all.dnsomatic.com`\

------------------------------------------------------------------------

\
Save changes in a file.

**#5** Run command to enable NetworkManager-dispatcher.service:

[user \$ ][ sudo systemctl enable NetworkManager-dispatcher.service [COPY TO CLIPBOARD]]

\

**#6** Logout and login.

**#7** Visit site: [openDNS Dashboard](https://dashboard.opendns.com/) to check sync status.

# [See Also]

-   [openDNS Homepage](http://opendns.com)
-   [DNS-O-Matic](https://www.dnsomatic.com/)
-   [Does OpenDNS Support IPv6?](https://support.opendns.com/hc/en-us/articles/227986667-Does-OpenDNS-Support-IPv6-)
-   [Wikipedia Article](https://en.wikipedia.org/wiki/OpenDNS)
-   The wiki page on [networking](//wiki.manjaro.org/index.php?title=Networking "Networking")
-   [Arch Wiki: resolv.conf](https://wiki.archlinux.org/index.php/resolv.conf)