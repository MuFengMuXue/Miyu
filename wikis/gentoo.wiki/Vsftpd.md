**Resources**

[[]][Home](https://security.appspot.com/vsftpd.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/vsftpd "wikipedia:vsftpd")

**vsftpd** (**V**ery **S**ecure **FTP** **D**aemon) is an FTP server for UNIX-like systems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Anonymous read access]](#Anonymous_read_access)
    -   [[2.2] [Anonymous read/write access]](#Anonymous_read.2Fwrite_access)
-   [[3] [Service]](#Service)
    -   [[3.1] [OpenRC]](#OpenRC)
    -   [[3.2] [systemd]](#systemd)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [seccomp filter sanboxing]](#seccomp_filter_sanboxing)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-ftp/vsftpd](https://packages.gentoo.org/packages/net-ftp/vsftpd) [[]] [Very Secure FTP Daemon]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`pam`](https://packages.gentoo.org/useflags/pam)                 Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                 Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`tcpd`](https://packages.gentoo.org/useflags/tcpd)               Add support for TCP wrappers
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 02:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-ftp/vsftpd`

## [Configuration]

#### [Anonymous read access]

[FILE] **`/etc/vsftpd.conf`**

    listen=YES
    local_enable=NO
    anonymous_enable=YES
    write_enable=NO
    anon_root=/home/ftp

#### [][Anonymous read/write access]

`root `[`#`]`chown ftp /home/ftp`

[FILE] **`/etc/vsftpd.conf`**

    listen=YES
    local_enable=NO
    anonymous_enable=YES
    anon_upload_enable=YES
    write_enable=YES
    anon_mkdir_write_enable=YES
    anon_root=/home/ftp

** Important**\
Allowing anonymous public read/write access is considered a high security risk.

## [Service]

### [OpenRC]

`root `[`#`]`rc-update add vsftpd default `

`root `[`#`]`/etc/init.d/vsftpd start `

### [systemd]

`root `[`#`]`systemctl enable vsftpd `

`root `[`#`]`systemctl start vsftpd `

## [Troubleshooting]

### [seccomp filter sanboxing]

Following error might show using ftp clients with vsftpd 3.0.x version:

    500 OOPS: priv_sock_get_cmd

This is caused by [seccomp filter sanboxing](https://en.wikipedia.org/wiki/Seccomp "wikipedia:Seccomp"), and enabled by default on **[amd64]**. To workaround this issue, disable seccomp filter sanboxing:

[FILE] **`/etc/vsftpd/vsftpd.conf`**

    seccomp_sandbox=NO

For further information, refer to Red Hat [bug #845980](https://bugzilla.redhat.com/show_bug.cgi?id=845980).

## [See also]

-   [Security_Handbook/Securing_services#Vsftpd](https://wiki.gentoo.org/wiki/Security_Handbook/Securing_services#Vsftpd "Security Handbook/Securing services")