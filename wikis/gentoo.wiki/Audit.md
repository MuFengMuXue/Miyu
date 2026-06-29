[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Audit&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://people.redhat.com/sgrubb/audit/)

[[]][GitHub](https://github.com/linux-audit/audit-userspace)

The Linux Audit System is designed to make Linux compliant with the requirements from Common Criteria, PCI-DSS, and other security standards by intercepting system calls and serializing audit log entries from privileged user space applications. The framework allows the configured events to be recorded to disk and distributed to plugins in realtime. Each audit event contains the date and time of event, type of event, subject identity, object acted upon, and result (success/fail) of the action if applicable.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Daemon]](#Daemon)

## [Installation]

### [USE flags]

### [USE flags for] [sys-process/audit](https://packages.gentoo.org/packages/sys-process/audit) [[]] [Userspace utilities for storing and processing auditing records]

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
  [`gssapi`](https://packages.gentoo.org/useflags/gssapi)             Enable GSSAPI support
  [`io-uring`](https://packages.gentoo.org/useflags/io-uring)         Enable the use of io_uring for efficient asynchronous IO and system requests
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                 Add LDAP support (Lightweight Directory Access Protocol)
  [`python`](https://packages.gentoo.org/useflags/python)             Add optional support/bindings for the Python language
  [`split-usr`](https://packages.gentoo.org/useflags/split-usr)       Enable behavior to support maintaining /bin, /lib\*, /sbin and /usr/sbin separately from /usr/bin and /usr/lib\*
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 04:10] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-process/audit`

## [Usage]

### [Daemon]

To start the daemon for OpenRC systems, run:

`root `[`#`]`rc-service auditd start`

`root `[`#`]`rc-update add auditd default`

For systemd systems:

`root `[`#`]`systemctl enable --now auditd`