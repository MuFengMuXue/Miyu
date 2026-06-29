Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Sshguard/es "Sshguard (46% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Sshguard/it "Sshguard (14% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Sshguard/hu "sshguard (57% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Sshguard/ru "sshguard (62% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Sshguard/ta "sshguard (14% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Sshguard/zh-cn "Sshguard (14% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Sshguard/ja "sshguard (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Sshguard/ko "Sshguard (32% translated)")

**Resources**

[[]][Home](https://www.sshguard.net/)

[[]][Official documentation](https://www.sshguard.net/docs/)

[[]][GitWeb](https://bitbucket.org/sshguard/sshguard/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/sshguard)

[sshguard] is an intrusion prevention system that parses server logs, determines malicious activity, and uses the system firewall to block the IP addresses of malicious connections. sshguard is written in C so it does not tax an interpreter.

## Contents

-   [[1] [How it works]](#How_it_works)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
    -   [[2.2] [Additional software]](#Additional_software)
        -   [[2.2.1] [Logging]](#Logging)
        -   [[2.2.2] [OpenSSH]](#OpenSSH)
        -   [[2.2.3] [Firewall]](#Firewall)
            -   [[2.2.3.1] [nftables]](#nftables)
            -   [[2.2.3.2] [iptables]](#iptables)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [nftables backend]](#nftables_backend)
        -   [[3.1.1] [Verification]](#Verification)
    -   [[3.2] [iptables backend]](#iptables_backend)
        -   [[3.2.1] [Preparing the firewall]](#Preparing_the_firewall)
        -   [[3.2.2] [Verification]](#Verification_2)
    -   [[3.3] [Services]](#Services)
        -   [[3.3.1] [OpenRC]](#OpenRC)
        -   [[3.3.2] [systemd]](#systemd)
    -   [[3.4] [Blacklisting hosts]](#Blacklisting_hosts)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [File \'/var/log/auth.log\' vanished while adding!]](#File_.27.2Fvar.2Flog.2Fauth.log.27_vanished_while_adding.21)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [How it works]

sshguard is a simple daemon that continuously tracks one or more log files. It parses the log events that daemons send out in case of failed login attempts and then blocks any further attempts from those connections by updating the system\'s firewall.

Unlike what the name implies, sshguard does not only parse SSH logs. It also supports many mail systems as well as a few FTP ones. A full listing of supported services can be found on the [sshguard.net website](https://www.sshguard.net).

## [Installation]

### [Emerge]

Install [[[app-admin/sshguard]](https://packages.gentoo.org/packages/app-admin/sshguard)[]]:

`root `[`#`]`emerge --ask app-admin/sshguard`

### [Additional software]

#### [Logging]

Running a local [Logging](https://wiki.gentoo.org/wiki/Logging "Logging") daemon is mandatory to be able to setup and run sshguard.

#### [OpenSSH]

**sshguard** works only with [OpenSSH](https://wiki.gentoo.org/wiki/OpenSSH "OpenSSH").

** Note**\
The [dropbear](https://wiki.gentoo.org/wiki/Dropbear "Dropbear") SSH daemons logs **do not match** anything when used with sshguard. sshguard does not work with dropbear.

** Note**\
OpenSSH version 9.7 released a built-in intrusion prevention mechanism. See [Intrusion prevention section of SSH article](https://wiki.gentoo.org/wiki/SSH#Intrusion_prevention "SSH") for configuration instructions.

#### [Firewall]

Depending on the init system and the desired firewall backend to be used by sshguard, additional software is required to be emerged in order for sshguard to block malicious actors.

More information on various supported backends can be found by reading the [[[sshguard-setup(7)]](https://man.archlinux.org/man/sshguard-setup.7.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] manpage.

##### [nftables]

When nftables are being used as the system firewall:

`root `[`#`]`emerge --ask net-firewall/nftables`

More information about configuring and using nftables can be found on the [nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables") article.

##### [iptables]

When iptables are being used as the system firewall:

`root `[`#`]`emerge --ask net-firewall/iptables`

More information about configuring and using iptables can be found on the [iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") article.

## [Configuration]

### [nftables backend]

Following settings are required before starting sshguard. Set the BACKEND path to use **nftables** and configure the FILES paths [/etc/sshguard.conf].

[FILE] **`/etc/sshguard.conf``BACKEND` and `FILES` mandatory settings**

    #!/bin/sh
    # sshguard.conf -- SSHGuard configuration

    # Options that are uncommented in this example are set to their default
    # values. Options without defaults are commented out.

    #### REQUIRED CONFIGURATION ####
    # Full path to backend executable (required, no default)
    BACKEND="/usr/libexec/sshg-fw-nft-sets"

    # Space-separated list of log files to monitor. (optional, no default)
    FILES="/var/log/auth.log /var/log/messages"
    # ...

Additional sshguard settings are optional, and can be left at the default value now, and be adjusted at a later time.

#### [Verification]

Once the **sshguard** daemon has been started, **nftables** will list the created sshguard ruleset. Use the **nft list ruleset** command to show the current status:

`root `[`#`]`nft list ruleset`

    table ip sshguard
            chain blacklist
    }
    table ip6 sshguard
            chain blacklist
    }

### [iptables backend]

Verify that the appropriate path to the **iptables** backend library is set in [/etc/sshguard.conf]:

[FILE] **`/etc/sshguard.conf``BACKEND` and `FILES` mandatory settings**

    #!/bin/sh
    # sshguard.conf -- SSHGuard configuration

    # Options that are uncommented in this example are set to their default
    # values. Options without defaults are commented out.

    #### REQUIRED CONFIGURATION ####
    # Full path to backend executable (required, no default)
    BACKEND="/usr/libexec/sshg-fw-iptables"

    # Space-separated list of log files to monitor. (optional, no default)
    FILES="/var/log/auth.log /var/log/messages"
    # ...

Additional settings are optional and can be left at the default value for now, or be adjusted at a later time.

#### [Preparing the firewall]

When [sshguard] blocks any malicious users (by blocking their IP addresses), it will use the [sshguard] chain.

Prepare the chain using **iptables** and make sure it is also triggered when new incoming connections are detected:

`root `[`#`]`iptables -N sshguard `

`root `[`#`]`iptables -A INPUT -j sshguard `

#### [Verification]

Once the **sshguard** daemon has been started **iptables** will list the Chain sshguard at the bottom, and a reference in INPUT chain to it. Use following iptables command to verify the status:

`root `[`#`]`iptables -L`

    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination
    sshguard   all  --  anywhere             anywhere

    Chain FORWARD (policy ACCEPT)
    target     prot opt source               destination

    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination

    Chain sshguard (1 references)
    target     prot opt source               destination

### [Services]

#### [OpenRC]

Have sshguard be started by default by adding it to the default runlevel, and then start it:

`root `[`#`]`rc-update add sshguard default `

`root `[`#`]`rc-service sshguard start `

#### [systemd]

Use systemd\'s conventional way to enable it, and then start it:

`root `[`#`]`systemctl enable sshguard `

`root `[`#`]`systemctl restart sshguard `

### [Blacklisting hosts]

With the blacklisting option after a number of abuses the IP address of the attacker or a IP subnet will be blocked permanently. The blacklist will be loaded at each startup and extended with new entries during operation. [sshguard] inserts a new address after it exceeded a threshold of abuses.

Blacklisted addresses are never scheduled to be released (allowed) again.

To enable blacklisting, create an appropriate directory and file:

`root `[`#`]`mkdir -p /var/lib/sshguard `

`root `[`#`]`touch /var/lib/sshguard/blacklist.db `

While defining a blacklist it is important to exclude trusted IP networks and hosts in a whitelist.

To enable whitelisting, create an appropriate directory and file:

`root `[`#`]`mkdir -p /etc/sshguard `

`root `[`#`]`touch /etc/sshguard/whitelist `

The whitelist has to include the loopback interface, and should have at least 1 IP trusted network f.e. 192.0.2.0/24.

[FILE] **`/etc/sshguard/whitelist`Whitelisting trusted networks**

    127.0.0.0/8
    ::1/128
    192.0.2.0/24

** Note**\
The 192.0.2.0/24 entry has to be adjusted to fit the own needs.

Add the `BLACKLIST_FILE` and `WHITELIST_FILE` file to the configuration. Example configuration listed blocks all hosts after the first login attempt. To setup a less agressive blocking policy, adjust the `THRESHOLD` and `BLACKLIST_FILE` integer, and set it to f.e. **10** instead of **2**:

[FILE] **`/etc/sshguard.conf`Configuring sshguard to blacklist abusers**

    BACKEND="/usr/libexec/sshg-fw-nft-sets"
    FILES="/var/log/auth.log"
    #
    THRESHOLD=2
    BLOCK_TIME=120
    DETECTION_TIME=1800
    #
    IPV6_SUBNET=128
    IPV4_SUBNET=32
    #
    # Add following lines
    BLACKLIST_FILE=2:/var/lib/sshguard/blacklist.db
    WHITELIST_FILE=/etc/sshguard/whitelist

Restart the [sshguard] daemon to have the changes take effect. On OpenRC:

`root `[`#`]`rc-service sshguard restart `

Or on systemd:

`root `[`#`]`systemctl restart sshguard `

## [Troubleshooting]

### [][File \'/var/log/auth.log\' vanished while adding!]

When starting up, sshguard reports the following error:

[CODE] **Error message when trying to add a monitor for /var/log/auth.log**

    Sep 23 03:39:11 foo.bar.com sshguard[64933]: File '/var/log/auth.log' vanished while adding!

Such an error (the file path itself can be different) occurs when the target file is not available on the system. Make sure that it is created, or update the sshguard configuration to not add it for monitoring.

On a syslog-ng system with OpenRC, the following addition to [syslog-ng.conf] can suffice:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`creating auth.log file**

    log ;
    log ;

    destination authlog ;
    filter f_auth ;
    filter f_authpriv ;
    log ;

Reload the configuration for the changes to take effect:

`root `[`#`]`rc-service syslog-ng reload`

## [See also]

-   [Fail2ban](https://wiki.gentoo.org/wiki/Fail2ban "Fail2ban") --- a system denying hosts causing multiple authentication errors access to a service.
-   [Iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") --- a program used to configure and manage the kernel\'s netfilter modules.
-   [Nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables") --- the successor to [[iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables")].
-   [OpenSSH](https://wiki.gentoo.org/wiki/OpenSSH "OpenSSH") --- the ubiquitous tool for logging into and working on remote machines securely.

## [External resources]

The [sshguard documentation](http://www.sshguard.net/docs/) provides all the information needed to further tune the application.