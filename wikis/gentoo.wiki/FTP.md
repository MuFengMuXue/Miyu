**Resources**

[[]][Home](https://wiki.linuxfoundation.org/networking/netkit)

[[]][Package information](https://packages.gentoo.org/packages/net-ftp/ftp)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FTP "wikipedia:FTP")

[[]][Man page](http://man7.org/linux/man-pages/man1/ftp.1.html)

[[]][[alt.comp.apps.ftp](news:alt.comp.apps.ftp) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.comp.apps.ftp))]

[[]][r/ftp](https://reddit.com/r/ftp)

**File Transfer Protocol (FTP)** is an legacy protocol for transferring files between computers. Because FTP traffic is not encrypted in transit and can easily be spoofed, it is considered insecure in modern networked computing. It has therefore been displaced by secure alternatives such as [sftp](https://wiki.gentoo.org/wiki/Sftp "Sftp"), and [scp](https://wiki.gentoo.org/wiki/Scp "Scp") for most use-cases. It is occasionally still used in a retrocomputing context or as a means to update firmware on embedded devices along side alternatives such as [TFTP](https://wiki.gentoo.org/index.php?title=TFTP&action=edit&redlink=1 "TFTP (page does not exist)").

While the FTP protocol itself is insecure, as native support for TLS over FTP is relatively rare among FTP servers, it is technically possible to encrypt the traffic by using a TLS wrapper such as [[[net-misc/stunnel]](https://packages.gentoo.org/packages/net-misc/stunnel)[]]. Such a configuration known as FTPS.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Alternative FTP Clients]](#Alternative_FTP_Clients)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [Firewall Configuration for FTP]](#Firewall_Configuration_for_FTP)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External Resources]](#External_Resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-ftp/ftp](https://packages.gentoo.org/packages/net-ftp/ftp) [[]] [Standard Linux FTP client]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)           Add support for IP version 6
  [`readline`](https://packages.gentoo.org/useflags/readline)   Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`ssl`](https://packages.gentoo.org/useflags/ssl)             Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-30 14:23] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Historically, the standard Linux FTP client has been [[[net-ftp/ftp]](https://packages.gentoo.org/packages/net-ftp/ftp)[]]. There is an SSL USE flag for the package but SSL support remains incomplete. Installing it is is simple enough:

`root `[`#`]`emerge --ask net-ftp/ftp`

### [Alternative FTP Clients]

  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------
  Name                        Package                                                                                                                                                                                                                                                                                                                                                                     Description
  Graphical FTP Clients
  filezilla                   [[[net-ftp/filezilla]](https://packages.gentoo.org/packages/net-ftp/filezilla)[]]   A graphical FTP client with lots of useful features and an intuitive file manager style interface.
  Console-based FTP Clients
  cmdftp                      [[[net-ftp/cmdftp]](https://packages.gentoo.org/packages/net-ftp/cmdftp)[]]            A light weight, yet robust command line FTP client with shell-like functionality.
  gftp                        [[[net-ftp/gftp]](https://packages.gentoo.org/packages/net-ftp/gftp)[]]                  A free multithreaded file transfer client.
  lftp                        [[[net-ftp/lftp]](https://packages.gentoo.org/packages/net-ftp/lftp)[]]                  A sophisticated file transfer program with support for FTP, SFTP, HTTP, HTTPS, and Torrent protocols.
  tnftp                       [[[net-ftp/tnftp]](https://packages.gentoo.org/packages/net-ftp/tnftp)[]]               NetBSD\'s native feature rich FTP client.
  yafc                        [[[net-ftp/yafc]](https://packages.gentoo.org/packages/net-ftp/yafc)[]]                  A console-based FTP client with advanced features.
  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------

## [Configuration]

The [.netrc] file is used to configure FTP auto-login behavior. The \"default\" token in the [.netrc] file matches any machine name except for explicitly specified machine tokens. There can be only one \"default\" token, and it should be placed after all machine tokens. It is commonly used in the following format:

[FILE] **`~/.netrc`Default .netrc Syntax**

    default login anonymous password user@site

This configuration allows the user to automatically log in as an anonymous FTP user to machines not specified in the [.netrc] file. The auto-login behavior can be disabled by using the \"-n\" flag.

The following tokens are used in the [.netrc] file:

**login name** Identifies a user on the remote machine. If this token is present, the auto-login process will initiate a login using the specified name.

**password string** Provides a password for the auto-login process. If this token is present, the specified string will be supplied when the remote server requires a password during the login process. Note that if this token is present in the [.netrc] file for any user other than \"anonymous\", the auto-login process will be aborted if the [.netrc] file is readable by anyone besides the user.

**account string** Supplies an additional account password. If this token is present, the auto-login process will supply the specified string when the remote server requires an additional account password. Alternatively, the auto-login process will initiate an ACCT command if no password is specified.

**macdef name** Defines a macro. This token functions similarly to the \"ftp macdef\" command. A macro is defined with the specified name, and its contents start from the next line in the [.netrc] file and continue until a null line (consecutive new-line characters) is encountered. If a macro named \"init\" is defined, it is automatically executed as the last step in the auto-login process.

### [Service]

Historically, the default FTP daemon for Linux was [ftpd]. Currently, Gentoo supports three different FTP daemons:

-   [[[net-ftp/proftpd]](https://packages.gentoo.org/packages/net-ftp/proftpd)[]]
-   [[[net-ftp/vsftpd]](https://packages.gentoo.org/packages/net-ftp/vsftpd)[]]
-   [[[net-ftp/pure-ftpd]](https://packages.gentoo.org/packages/net-ftp/pure-ftpd)[]]

#### [Firewall Configuration for FTP]

The following firewall rules are typical of an FTP server providing FTP in the clear:

[CODE] **FTP server firewall rules**

    # Allow clear text FTP in Active Mode
    iptables -A INPUT -p tcp -m multiport --dports 20,21 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp -m multiport --dports 20,21 -m conntrack --ctstate ESTABLISHED -j ACCEPT

    # The following additional rules are required to support Passive Mode FTP.
    iptables -A INPUT  -p tcp -m tcp --sport 1024: --dport 1024: -m conntrack --ctstate ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp -m tcp --sport 1024: --dport 1024: -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

The following firewall rules are more typical of an FTP server providing FTP over TLS:

[CODE] **FTPS server firewall rules**

    # Allow FTPS (FTP over TLS) in Active Mode
    iptables -A INPUT -p tcp -m multiport --dports 989,990 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp -m multiport --dports 989,990 -m conntrack --ctstate ESTABLISHED -j ACCEPT

    # The following additional rules are required to support Passive Mode FTPS.
    iptables -A INPUT  -p tcp -m tcp --sport 1024: --dport 1024: -m conntrack --ctstate ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp -m tcp --sport 1024: --dport 1024: -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

## [Usage]

### [Invocation]

`user `[`$`]`ftp`

    ftp> help
    Commands may be abbreviated.  Commands are:

    !       dir     mdelete     qc      site
    $       disconnect  mdir        sendport    size
    account     exit        mget        put     status
    append      form        mkdir       pwd     struct
    ascii       get     mls     quit        system
    bell        glob        mode        quote       sunique
    binary      hash        modtime     recv        tenex
    bye     help        mput        reget       tick
    case        idle        newer       rstatus     trace
    cd      image       nmap        rhelp       type
    cdup        ipany       nlist       rename      user
    chmod       ipv4        ntrans      reset       umask
    close       ipv6        open        restart     verbose
    cr      lcd     prompt      rmdir       ?
    delete      ls      passive     runique
    debug       macdef      proxy       send

Basic usage of the [ftp] client is simple enough. Downloading a file works like this:

`user `[`$`]`ftp gentoo.org`

    ftp> get <desired_file>
    ftp> exit

The file will be deposited in the current working (local) directory.

Uploading a file works similarly:

`user `[`$`]`ftp gentoo.org`

    ftp> cd <remote_directory>
    ftp> send <local_path_and_filename>
    ftp> exit

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-ftp/ftp`

## [See also]

-   [SFTP](https://wiki.gentoo.org/wiki/SFTP "SFTP") --- an interactive file transfer program, similar to [FTP], which performs all operations over an encrypted [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") transport.
-   [TFTP](https://wiki.gentoo.org/index.php?title=TFTP&action=edit&redlink=1 "TFTP (page does not exist)")

## [External Resources]

-   [Active FTP vs. Passive FTP, a Definitive Explanation](https://slacksite.com/other/ftp.html)