# Extensions / Libxt Osf

The osf module does passive operating system fingerprinting. This module compares some data (Window Size, MSS, options and their order, TTL, DF, and others) from packets with the SYN bit set.

\[**!**\] **--genre** *string*
Match an operating system genre by using a passive fingerprinting.

**--ttl** *level*
Do additional TTL checks on the packet to determine the operating system. *level* can be one of the following values:

**0**
True IP address and fingerprint TTL comparison. This generally works for LANs.

**1**
Check if the IP header's TTL is less than the fingerprint one. Works for globally-routable addresses.

**2**
Do not compare the TTL at all.

**--log** *level*
Log determined genres into dmesg even if they do not match the desired one. *level* can be one of the following values:

**0**
Log all matched or unknown signatures

**1**
Log only the first one

**2**
Log all known matched signatures

You may find something like this in syslog:

Windows \[2000:SP3:Windows XP Pro SP1, 2000 SP3\]: 11.22.33.55:4024 -\> 11.22.33.44:139 hops=3 Linux \[2.5-2.6:\] : 1.2.3.4:42624 -\> 1.2.3.5:22 hops=4

OS fingerprints are loadable using the **nfnl_osf** program. To load fingerprints from a file, use:

**nfnl_osf -f /usr/share/xtables/pf.os**

To remove them again,

**nfnl_osf -f /usr/share/xtables/pf.os -d**

The fingerprint database can be downloaded from http://www.openbsd.org/cgi-bin/cvsweb/src/etc/pf.os .
