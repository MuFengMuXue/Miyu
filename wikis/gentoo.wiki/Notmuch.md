[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Notmuch&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://notmuchmail.org/)

[[]][GitWeb](https://gitweb.gentoo.org/proj/https://git.notmuchmail.org/git/notmuch)

[[]][Official documentation](https://notmuchmail.org/doc/latest/)

[[]][Package information](https://packages.gentoo.org/packages/net-mail/notmuch)

Notmuch is a threaded email indexer that assists users with tagging messages and sorting mail.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [See also]](#See_also)

## [Installation]

** Important**\
Notmuch itself is not an IMAP or POP client, users will need to utilize a separate utility to account for this. One such example of an IMAP client is [isync](https://wiki.gentoo.org/wiki/Isync "Isync").

### [Emerge]

`root `[`#`]`emerge --ask net-mail/notmuch`

## [Configuration]

** Note**\
For full configuration documentation, refer to the [manpage](https://notmuchmail.org/manpages/notmuch-config-1/).

A simple `.notmuch-config` file might look like the following:

[FILE] **`/home/larry/.notmuch-config`**

    [database]
    path=/home/larry/.mail

    [user]
    name=Larry
    primary_email=larry@gentoo.org
    other_email=larry@example.com

    [new]
    tags=unread;inbox;sent;
    ignore=.uidvalidity;.mbsyncstate;

    [search]
    exclude_tags=deleted;spam;

    [maildir]
    synchronize_flags=true

    [crypto]
    gpg_path=gpg

## [See also]

-   [aerc](https://wiki.gentoo.org/wiki/Aerc "Aerc") --- a lightweight, command-line [mail user agent](https://en.wikipedia.org/wiki/mail_user_agent "wikipedia:mail user agent") (MUA) written in the [Go](https://wiki.gentoo.org/wiki/Go "Go") programming language.
-   [neomutt](https://wiki.gentoo.org/wiki/Neomutt "Neomutt") --- command-line mail client forked from [[mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")].