**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

\

**Resources**

[[]][Home](https://www.shrubbery.net/tac_plus/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/TACACS%2B "wikipedia:TACACS+")

*TACACS+ ebuild has been removed from portage Removal on 2024-02-06. See Bug #918536.*

From the [TACACS+ article](https://en.wikipedia.org/wiki/TACACS%2B "wikipedia:TACACS+") at Wikipedia, the free encyclopedia:

In computer networking, TACACS+ (*Terminal Access Controller Access-Control System Plus*) is a AAA protocol which provides access control for user Authentication for routers, network access servers and other networked computing devices via one or more centralized servers. TACACS+ provides separate authentication, authorization and accounting services.

TACACS+ is a protocol for AAA services (Authentication, Authorization, Accounting) similar to RADIUS. A system that provides logins to users is often called a NAS (Network Access Server), not to be confused with NAS - (Network Attached Storage). A NAS can be a *client* to an *AAA server*, such as a RADIUS, LDAP, or TACACS daemon. The client must use the authentication protocol appropriate for the server. A Linux system may act as an authentication client when when logging in a user. Based on the PAM configuration, the Linux system can use a RADIUS, LDAP, or TACACS server or may perform purely local authentication. To use TACACS, the Linux (or other) client must have IP access to a **TACACS server**, which is usually a separate physical server that provides authentication services to many clients. This page describes how to configure a Linux system to act as a TACACS server using the **tac plus** software package. It is often useful to have a TACACS server to support authentication for proprietary systems on your network, such as Cisco routers, that implement TACACS clients. With such a server, you can add or delete a new router administrator on all of your routers at the same time in one place. If some of your Linux systems are acting as network elements that should be accessed only by your network administrators, you may choose to configure these systems to also use your TACACS server for AAA.

## Contents

-   [[1] [About]](#About)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Authentication with passwd file]](#Authentication_with_passwd_file)
    -   [[3.2] [Authentication with PAM]](#Authentication_with_PAM)
    -   [[3.3] [Authentication to tac_plus.conf]](#Authentication_to_tac_plus.conf)
-   [[4] [Network equipment configuration]](#Network_equipment_configuration)
-   [[5] [Final configuration steps]](#Final_configuration_steps)
-   [[6] [Troubleshooting]](#Troubleshooting)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [About]

This document describes how to configure and use the most recent version of tac_plus provided by [Shrubbery Networks](https://www.shrubbery.net/tac_plus/).

This installation howto uses tac_plus-4.0.4.27a as reference. General configuration and troubleshooting tips should also apply to older tac_plus versions available in the portage.

## [Installation]

### [USE flags]

Cannot load package information. Is the atom *net-nds/tac_plus* correct?

### [Emerge]

Be sure to review and set USE flags accordingly before emerging the package:

`root `[`#`]`emerge --ask net-nds/tac_plus`

## [Configuration]

Shrubbery tac_plus is lacking a good documentation. General configuration is split up in 3 main sections:

-   ACL (Access Lists)
-   group
-   users

** Important**\
The sequence ACL, groups, users in the file [/etc/tac_plus/tac_plus.conf] is important.

Further configuration tips at [tac_plus FAQ](https://www.shrubbery.net/tac_plus/FAQ)

Ways to configure user authentication with tac_plus:

-   Authentication to local passwd file [/etc/passwd]
-   Authentication to LDAP server with **PAM**
-   Authentication to password configured in [/etc/tac_plus/tac_plus.conf]

### [Authentication with passwd file]

User authentication to local passwd file [/etc/passwd] example:

[FILE] **`/etc/tac_plus/tac_plus.conf`**

    key = 123-my_tacacs_key

    group = netadmin
    }

    user = larry

### [Authentication with PAM]

User authentication with **PAM** example:

[FILE] **`/etc/tac_plus/tac_plus.conf`**

    key = 123-my_tacacs_key

    group = netadmin
    }

    user = larry

** Note**\
Recent tac_plus versions support user authentication with LDAP. Group membership has to be defined in tac_plus.conf configuration file.

### [Authentication to tac_plus.conf]

User authentication to password configured in [/etc/tac_plus/tac_plus.conf] example:

[FILE] **`/etc/tac_plus/tac_plus.conf`**

    key = 123-my_tacacs_key

    group = netadmin
    }

    user = larry

tac_plus uses the crypt() library in the underlying operating system and asks it to hash a given password against the hash in *tac_plus.conf*.

As such, one can transparently put any hash value you like in tac_plus.conf as long as glibc crypt() supports it. On Linux systems these days with *\>=glibc-2.7*

-   Blowfish
-   SHA-512
-   SHA-256
-   MD5

are supported. To show supported encryption methodes on the tac_plus server use following command:

`user `[`$`]`man 3 crypt`

** Important**\
There is almost no reason left anymore to use DES hashes in tac_plus.conf [http://www.shrubbery.net/pipermail/tac_plus/2011-December/001033.html](http://www.shrubbery.net/pipermail/tac_plus/2011-December/001033.html)

Password hash generation can be done using following tools:

-   Blowfish

`user `[`$`]`htpasswd -bnBC 13 "" Secret-Password | tr -d ':\n'`

-   SHA512

`user `[`$`]`mkpasswd -m SHA-512`

-   SHA256

`user `[`$`]`mkpasswd -m SHA-256`

-   MD5

`user `[`$`]`openssl passwd -1`

## [Network equipment configuration]

A variety of systems implements the client side of the TACACS+ protocol. The following platforms implemented TACACS+ protocol communication:

-   Cisco (CatOS, IOS, IOS-XE, IOS-XR, NX-OS)
-   Juniper (ScreenOS, JUNOS)
-   Huawei (VRP)
-   HP (ComWare, ArubaOS, AOS-CX)
-   OneAccess
-   Linux-based systems (via PAM)

Most operating systems and vendors have TACACS+ client implementation, or other AAA protocol like RADIUS or Diameter.

Basic AAA (Authentication, Authorization, Accounting) configuration on a Cisco IOS component:

-   Substitute *tacacs-server host* with IP address of the tac_plus server
-   For *key* choose the key which is configured in [/etc/tac_plus/tac_plus.conf]

<!-- -->

    !
    aaa new-model
    aaa authentication login default group tacacs+ local
    aaa authentication enable default group tacacs+
    aaa authorization exec default group tacacs+ local
    !
    tacacs-server host 192.0.2.10 key 123-my_tacacs_key
    !
    line con 0
     login authentication default
    !
    line vty 0 15
     login authentication default
    !

## [Final configuration steps]

Start tac_plus daemon:

`root `[`#`]`/etc/init.d/tac_plus start`

Add tac_plus to the default runlevel:

`root `[`#`]`rc-update add tac_plus default`

Verify tac_plus is running:

`root `[`#`]`ps -ef |grep tac_plus `

    root      8123     1  0 21:29 ?        00:00:00 /usr/bin/tac_plus -C /etc/tac_plus/tac_plus.conf

## [Troubleshooting]

Verifying the interfaces and ports on which tac_plus is listening:

`root `[`#`]`netstat -tulpen | grep tac_plus `

    tcp        0      0 0.0.0.0:49              0.0.0.0:*               LISTEN      0          27930913   8455/tac_plus

Looking for configuration errors if daemon fails to start:

`root `[`#`]`tail -f /var/log/messages `

    2011-04-09T21:26:28.847493+02:00 server tac_plus[7749]: Reading config
    2011-04-09T21:26:28.847605+02:00 server tac_plus[7749]: Error Unrecognised keyword default for user on line 51
    2011-04-09T21:26:28.851096+02:00 server /etc/init.d/tac_plus[7738]: ERROR: tac_plus failed to start

Tacacs communication between tacacs-server and a network component. Example output of a a successful user session:

Run tcpdump on the local tacacs-server:

`root `[`#`]`tcpdump -i eth0 tcp port 49 `

    22:53:01.692185 IP switch.11384 > server.tacacs: S 2173305858:2173305858(0) win 4128 <mss 1460>
    22:53:01.692221 IP server.tacacs > switch.11384: S 4283961231:4283961231(0) ack 2173305859 win 5840 <mss 1460>
    22:53:01.693690 IP switch.11384 > server.tacacs: . ack 1 win 4128
    22:53:01.793233 IP switch.11384 > server.tacacs: P 1:43(42) ack 1 win 4128
    22:53:01.793282 IP server.tacacs > switch.11384: . ack 43 win 5840
    22:53:01.808601 IP server.tacacs > switch.11384: P 1:29(28) ack 43 win 5840
    22:53:01.993368 IP switch.11384 > server.tacacs: P 43:68(25) ack 29 win 4100
    22:53:02.002160 IP server.tacacs > switch.11384: P 29:47(18) ack 68 win 5840
    22:53:02.002187 IP server.tacacs > switch.11384: F 47:47(0) ack 68 win 5840
    22:53:02.004152 IP switch.11384 > server.tacacs: . ack 48 win 4082
    22:53:02.096209 IP switch.11384 > server.tacacs: FP 68:68(0) ack 48 win 4082
    22:53:02.096231 IP server.tacacs > switch.11384: . ack 69 win 5840
    22:53:02.123615 IP switch.11385 > server.tacacs: S 4146347262:4146347262(0) win 4128 <mss 1460>
    22:53:02.123641 IP server.tacacs > switch.11385: S 4294861878:4294861878(0) ack 4146347263 win 5840 <mss 1460>
    22:53:02.127410 IP switch.11385 > server.tacacs: . ack 1 win 4128
    22:53:02.229706 IP switch.11385 > server.tacacs: P 1:62(61) ack 1 win 4128
    22:53:02.229751 IP server.tacacs > switch.11385: . ack 62 win 5840
    22:53:02.229890 IP server.tacacs > switch.11385: P 1:52(51) ack 62 win 5840
    22:53:02.229923 IP server.tacacs > switch.11385: F 52:52(0) ack 62 win 5840
    22:53:02.232297 IP switch.11385 > server.tacacs: . ack 53 win 4077
    22:53:02.330097 IP switch.11385 > server.tacacs: FP 62:62(0) ack 53 win 4077
    22:53:02.330118 IP server.tacacs > switch.11385: . ack 63 win 5840

To get debug ouput from tac_plus run tac_plus from shell with following command:

`root `[`#`]`tac_plus -C /etc/tac_plus/tac_plus.conf -L -p 49 -d128 -g`

for used command line options in this command read the tac_plus manual:

`user `[`$`]`man tac_plus`

## [See also]

-   [FreeRADIUS](https://wiki.gentoo.org/wiki/FreeRADIUS "FreeRADIUS") --- implementation of the Remote Authentication Dial-In User Service (RADIUS) protocol

## [External resources]

-   [tac_plus FAQ](https://www.shrubbery.net/tac_plus/FAQ)
-   [RFC 8907 - The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html)
-   [Wikipedia:AAA\_(computer_security)](https://en.wikipedia.org/wiki/AAA_(computer_security) "wikipedia:AAA (computer security)")
-   [https://www.shrubbery.net/pipermail/tac_plus/2011-December/001033.html](https://www.shrubbery.net/pipermail/tac_plus/2011-December/001033.html)
-   [https://man7.org/linux/man-pages/man3/crypt.3.html](https://man7.org/linux/man-pages/man3/crypt.3.html)
-   [FreeRADIUS - TACACS+ Virtual Server Setup](https://www.freeradius.org/documentation/freeradius-server/4.0.0/reference/raddb/sites-available/tacacs.html)