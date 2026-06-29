[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Isync&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://isync.sourceforge.io/)

[[]][GitWeb](https://gitweb.gentoo.org/proj/https://sourceforge.net/p/isync/isync/ci/master/tree/)

[[]][Package information](https://packages.gentoo.org/packages/net-mail/isync)

[[]][Man page](http://man7.org/linux/man-pages/https://isync.sourceforge.io/mbsync.html.html)

isync is a command line application which synchronizes mailboxes; currently Maildir and IMAP4 mailboxes are supported. New messages, message deletions and flag changes can be propagated both ways. isync is suitable for use in IMAP-disconnected mode.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Syncing mailboxes]](#Syncing_mailboxes)
    -   [[3.2] [Emerge]](#Emerge)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-mail/isync](https://packages.gentoo.org/packages/net-mail/isync) [[]] [MailDir mailbox synchronizer]

  --------------------------------------------------------- --------------------------------------------------------------------------------------
  [`berkdb`](https://packages.gentoo.org/useflags/berkdb)   Add support for sys-libs/db (Berkeley DB)
  [`sasl`](https://packages.gentoo.org/useflags/sasl)       Add support for the Simple Authentication and Security Layer
  [`ssl`](https://packages.gentoo.org/useflags/ssl)         Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`zlib`](https://packages.gentoo.org/useflags/zlib)       Add support for zlib compression
  --------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-12 02:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Configuration]

isync utilizes the `.mbsyncrc` file that lives in the home directory. An example of this looks like the following:

[FILE] **`/home/larry/.mbsyncrc`**

    IMAPAccount gentoo
    Host dev.gentoo.org
    Port 143
    User larry@gentoo.org
    Pass "password123"
    TLSType STARTTLS
    AuthMechs LOGIN

    IMAPStore gentoo-remote
    Account gentoo

    MaildirStore gentoo-local
    Path ~/.mail/personal/
    Inbox ~/.mail/personal/INBOX
    SubFolders Verbatim

    Channel gentoo
    Far :gentoo-remote:
    Near :gentoo-local:
    Patterns *
    Patterns INBOX*
    Expunge None
    CopyArrivalDate yes
    Sync All
    SyncState *
    Create Both

## [Usage]

### [Syncing mailboxes]

To sync all mailboxes, run:

`user `[`$`]`mbsync -a`

    Channels: 2    Boxes: 44    Far: +0 *0 #0 -0    Near: +0 *0 #0 -0

### [Emerge]

`root `[`#`]`emerge --ask net-mail/isync`

## [See also]

-   [Notmuch](https://wiki.gentoo.org/wiki/Notmuch "Notmuch")