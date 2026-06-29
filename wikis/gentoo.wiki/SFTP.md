**Resources**

[[]][Home](http://www.openssh.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Secure_file_transfer_program "wikipedia:Secure file transfer program")

**SFTP** (**S**ecure **F**ile **T**ransfer **P**rogram) is an interactive file transfer program, similar to [FTP](https://wiki.gentoo.org/wiki/FTP "FTP"), which performs all operations over an encrypted [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") transport. It uses many features of SSH, such as public key authentication and compression.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Installation]

The [sftp] command is part of the [[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]] package, and deployments of Gentoo Linux should already have OpenSSH installed, as the package is part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"). The presence and proper functioning of OpenSSH can be checked by running the [sftp] command, which should output a usage statement:

`user `[`$`]`sftp`

    usage: sftp [-46AaCfNpqrv] [-B buffer_size] [-b batchfile] [-c cipher]
              [-D sftp_server_path] [-F ssh_config] [-i identity_file]
              [-J destination] [-l limit] [-o ssh_option] [-P port]
              [-R num_requests] [-S program] [-s subsystem | sftp_server]
              destination

If no usage statement is printed, OpenSSH may be corrupt, or not installed. Try re-installation by following the [Installation section from the SSH article](https://wiki.gentoo.org/wiki/SSH#Installation "SSH").

## [Configuration]

For having tab completion the [`libedit`](https://packages.gentoo.org/useflags/libedit) USE flag needs to be enabled.^[\[2\]](#cite_note-2)^ For further configuration see [the configuration section in the SSH article](https://wiki.gentoo.org/wiki/SSH#Configuration "SSH").

## [See also]

-   [CurlFtpFS](https://wiki.gentoo.org/wiki/CurlFtpFS "CurlFtpFS") --- allows for [mounting](https://wiki.gentoo.org/wiki/Mount "Mount") an FTP folder as a regular directory to the local directory tree.
-   [SCP](https://wiki.gentoo.org/wiki/SCP "SCP") --- an interactive file transfer program, similar to the [copy] command, that copies files over an encrypted SSH transport.
-   [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") --- the ubiquitous tool for logging into and working on remote machines securely.
-   [SSHFS](https://wiki.gentoo.org/wiki/SSHFS "SSHFS") --- a secure shell client used to mount remote filesystems to local machines.

## [External resources]

-   The official sftp man page locally via [man sftp] or online at [openbsd.org](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/sftp.1?query=sftp&sec=1)

## [References]

1.  [[[↑](#cite_ref-1)] [[http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/sftp.1?query=sftp&sec=1](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/sftp.1?query=sftp&sec=1)]]
2.  [[[↑](#cite_ref-2)] [[Gentoo Forums :: View topic - (SOLVED) sftp autocompletion](https://forums.gentoo.org/viewtopic.php?p=7828294#7828294), [Welcome -- Gentoo Linux](https://gentoo.org/), October 15th, 2015. Retrieved on October 15th, 2015.]]