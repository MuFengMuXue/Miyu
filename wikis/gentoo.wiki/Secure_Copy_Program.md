*Not to be confused with [SCAP](https://wiki.gentoo.org/wiki/SCAP "SCAP").*

**Resources**

[[]][Home](http://www.openssh.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Secure_copy "wikipedia:Secure copy")

**SCP** (**S**ecure **C**opy **P**rogram) is an interactive file transfer program, similar to the [copy] command, that copies files over an encrypted SSH transport. It uses many features of [SSH](https://wiki.gentoo.org/wiki/SSH "SSH"), such as public key authentication and compression.^[\[1\]](#cite_note-1)^

** Note**\
The [OpenSSH 8.0 release notes](https://www.openssh.com/txt/release-8.0), from 2019, state \"*The scp protocol is outdated, inflexible and not readily fixed. We recommend the use of more modern protocols like sftp and rsync for file transfer instead.*\". The [OpenSSH 8.8 release notes](https://www.openssh.com/txt/release-8.8), from 2021, state \"*A near-future release of OpenSSH will switch scp(1) from using the* legacy scp/rcp protocol to using SFTP by default.*\".*

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage examples]](#Usage_examples)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

The [scp] command is part of the [[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]] package, and deployments of Gentoo Linux should already have OpenSSH installed, as the package is part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"). The presence and proper functioning of OpenSSH can be checked by running the [scp] command, which should output a usage statement:

`user `[`$`]`scp`

    usage: scp [-346ABCpqrTv] [-c cipher] [-F ssh_config] [-i identity_file]
                [-J destination] [-l limit] [-o ssh_option] [-P port]
                [-S program] source ... target

If no usage statement is printed, OpenSSH may be corrupt, or not installed. Try re-installation by following the [Installation section from the SSH article](https://wiki.gentoo.org/wiki/SSH#Installation "SSH").

## [Configuration]

For configuration see [the configuration section in the SSH article](https://wiki.gentoo.org/wiki/SSH#Configuration "SSH").

## [Usage examples]

Copy a file from a remote computer locally:

`user `[`$`]`scp user@somecomputer:/path/file /path/file`

Where

-   \'user\' is a username on the remote computer. This defaults to the username on the local computer
-   \'somecomputer\' is the hostname or the IP address of the remote computer

\
Copy a local file to a remote computer:

`user `[`$`]`scp /path/file user@somecomputer:/path/file`

## [See also]

-   [SFTP](https://wiki.gentoo.org/wiki/SFTP "SFTP") --- an interactive file transfer program, similar to [FTP](https://wiki.gentoo.org/wiki/FTP "FTP"), which performs all operations over an encrypted [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") transport.
-   [SSHFS](https://wiki.gentoo.org/wiki/SSHFS "SSHFS") --- a secure shell client used to mount remote filesystems to local machines.
-   [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") --- the ubiquitous tool for logging into and working on remote machines securely.
-   [Rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") --- a powerful file sync program capable of efficient file transfers and directory synchronization.
-   [CurlFtpFS](https://wiki.gentoo.org/wiki/CurlFtpFS "CurlFtpFS") --- allows for [mounting](https://wiki.gentoo.org/wiki/Mount "Mount") an FTP folder as a regular directory to the local directory tree.

## [External resources]

-   The SCP man page locally ([man scp]) or online at [openbsd.org](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/scp.1?query=scp&sec=1)

## [References]

1.  [[[↑](#cite_ref-1)] [[http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/scp.1?query=scp&sec=1](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/scp.1?query=scp&sec=1)]]