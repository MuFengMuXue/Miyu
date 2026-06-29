[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Firewalls&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Firewalls "Firewalls (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Firewalls/tr "Güvenlik duvarları (21% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Firewalls/fr "Pare-feux (26% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Firewalls/ru "Брандмауэры (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Firewalls/fa "دیوارهای آتش (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Firewalls/zh-cn "防火墙 (23% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [UFW]](#UFW)
    -   [[2.1] [Installing UFW]](#Installing_UFW)
    -   [[2.2] [Adding Rules]](#Adding_Rules)
    -   [[2.3] [UFW and Applications]](#UFW_and_Applications)
    -   [[2.4] [Removing Rules]](#Removing_Rules)
    -   [[2.5] [GUFW]](#GUFW)
-   [[3] [iptables]](#iptables)
-   [[4] [See Also]](#See_Also)

# [Overview]

Running a local firewall is almost always a good practice. Even when you are behind a network firewall, a local firewall protects you from threats on the inside of your network.

# [UFW]

UFW stands for Uncomplicated FireWall, and is a program for managing a netfilter firewall. It provides a command line interface and aims to be uncomplicated and easy to use. UFW is far simpler than iptables and a good place to start unless you have very specialized needs.

## [Installing UFW]

You can install the `ufw` package using you favorite package manager or the command:

[user \$ ][ pamac install ufw [COPY TO CLIPBOARD]]

\

Once UFW is installed you need to start and enable it using the commands:

[user \$ ][ sudo systemctl enable ufw.service [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo ufw enable [COPY TO CLIPBOARD]]

\

\

**Warning**

------------------------------------------------------------------------

Don\'t enable both iptables.service and ufw.service

## [Adding Rules]

To view the current configuration you can use the command `ufw status`. Here is what it looks like in a new install:

\

[\$] [sudo ufw status verbose]\

    Status: active
    Logging: on (low)
    Default: deny (incoming), allow (outgoing), disabled (routed)
    New profiles: skip

\
This indicates that it will block all incoming traffic and allow all outgoing traffic. This is a good starting point for most desktop systems. However, often we will want to allow some incoming traffic. This can be done with the command `ufw allow`. For example, if we want to allow incoming ssh traffic so we can connect to the machine from other machines on the network we could use the command:

[user \$ ][ sudo ufw allow ssh [COPY TO CLIPBOARD]]

\

If we wanted to also tcp connections to a local webserver on a non-standard https port, 8443. We could use the command:

[user \$ ][ sudo ufw allow in 8443/tcp [COPY TO CLIPBOARD]]

\

\

\

**Tip**

------------------------------------------------------------------------

When you don\'t specify \"in\" or \"out\", \"in\" is assumed

## [UFW and Applications]

You may notice a difference in the above two commands. When we built the rules for ssh we used the name and for https we used the port number, 8443. This is because UFW has a small database of applications it knows the ports for. You can see the list with the command:

[user \$ ][ sudo ufw app list [COPY TO CLIPBOARD]]

\

For applications on the list you can add them by name. If you want to review the configuration for one of the applications, you can use the command `ufw app info`. For example, to the configuration for ssh:

\

[\$] [sudo ufw app info SSH]\

    Profile: SSH
    Title: SSH server
    Description: SSH server

    Port:
      22/tcp

\

\

**Tip**

------------------------------------------------------------------------

When using ufw app the commands are case sensitive but when adding rules they are not

Some additional preconfigured applications can be added by installing the package `ufw-extras` with your favorite package manager or the command:

[user \$ ][ pamac install ufw-extras [COPY TO CLIPBOARD]]

\

## [Removing Rules]

Rules can be removed with the `ufw delete` command. For example, to delete our 8443 rules we could use the command:

[user \$ ][ sudo ufw delete allow 8443/tcp [COPY TO CLIPBOARD]]

\

You can also delete them by number. This is easier if you have a numbered list which you can see with the command:

\

[\$] [sudo ufw status numbered]\

    Status: active
    To                         Action      From
         --                         ------      ----
    [ 1] 22                         ALLOW IN    Anywhere
    [ 2] 22 (v6)                    ALLOW IN    Anywhere (v6)

\
Now if we wanted to stop allowing ssh on ipv6 we could use the command:

[user \$ ][ sudo ufw delete 2 [COPY TO CLIPBOARD]]

\

## [GUFW]

[![Gufw.jpg](/images/d/d1/Gufw.jpg)](//wiki.manjaro.org/index.php?title=File:Gufw.jpg)

[](//wiki.manjaro.org/index.php?title=File:Gufw.jpg "Enlarge")

Prefer to use GUI applications and still want to manage your firewall? No problem. GUFW is a GTK front-end for UFW that aims to make managing a Linux firewall as accessible and easy as possible. It features pre-sets for common ports and p2p applications.

If it is not installed already gufw can be installed from the repos:

[user \$ ][ pamac install gufw [COPY TO CLIPBOARD]]

\

It will now be available in the menu as **Firewall Configuration** or by running `gufw` directly.

# [iptables]

iptables is included as part of the Linux kernel. iptables is significantly more complicated than using a tool like UFW. As a result, a full tutorial on iptables is beyond the scope of this wiki. Using iptables on Manjaro should be the same for every distribution of Linux so there is plenty of available documentation. Some of this is linked [below](//wiki.manjaro.org/index.php?title=Firewalls#See_Also "Firewalls"). Here are some basics to get you started.

To enable loading rules on startup you can use the command:

[user \$ ][ sudo systemctl enable iptables.service [COPY TO CLIPBOARD]]

\

This will load the rules from the file `/etc/iptables/iptables.rules`.

To display the currently loaded rules:

[user \$ ][ sudo iptables -L [COPY TO CLIPBOARD]]

\

To save the current rules to a file

[user \$ ][ sudo sh -c \"iptables-save \> /etc/iptables/iptables.rules\" [ /etc/iptables/iptables.rules\" \" aria-disabled=\"false\"\>COPY TO CLIPBOARD]]

\

To load the rules from a file

[user \$ ][ sudo sh -c \"iptables-restore \> /etc/iptables/iptables.rules\" [ /etc/iptables/iptables.rules\" \" aria-disabled=\"false\"\>COPY TO CLIPBOARD]]

\

To allow ssh connections

[user \$ ][ sudo iptables -A INPUT -p tcp \--dport 22 -m conntrack \--ctstate NEW,ESTABLISHED -j ACCEPT [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo iptables -A OUTPUT -p tcp \--sport 22 -m conntrack \--ctstate ESTABLISHED -j ACCEPT [COPY TO CLIPBOARD]]

\

# [See Also]

-   The Arch Wiki on [UFW](https://wiki.archlinux.org/index.php/Ufw)
-   The [UFW website](https://help.ubuntu.com/community/UFW)
-   The [GUFW website](http://gufw.org/)
-   The [iptables man page](https://linux.die.net/man/8/iptables)
-   The Arch Wiki on [iptables](https://wiki.archlinux.org/index.php/iptables)
-   The Debian Wiki on [iptables](https://wiki.debian.org/iptables)