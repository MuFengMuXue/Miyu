[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=WKD&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Web Key Directory (WKD)** is one of mechanisms for distributing [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") keys. WKD works by querying a *.well-known* directory on a domain, extracted from an email address, and obtains the keys from there. It avoids reliance on a centralized keyserver.

## Contents

-   [[1] [Use in Gentoo]](#Use_in_Gentoo)
    -   [[1.1] [Using Web Key Directory on gentoo.org]](#Using_Web_Key_Directory_on_gentoo.org)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Use in Gentoo]

[Gemato](https://wiki.gentoo.org/wiki/Gemato "Gemato"), which is used for repository verification by Portage, uses WKD as one method for refreshing keys safely.

### [Using Web Key Directory on gentoo.org]

The public key from each Gentoo developer can be fetched via the command line:

`user `[`$`]`gpg --auto-key-locate clear,nodefault,wkd --locate-keys [devname]@gentoo.org`

## [See also]

-   [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") --- a free implementation of the OpenPGP standard (RFC 4880).

## [External resources]

-   Test WKD providers online [https://metacode.biz/openpgp/web-key-directory](https://metacode.biz/openpgp/web-key-directory)
-   [https://wiki.gnupg.org/WKD](https://wiki.gnupg.org/WKD)
-   [https://www.gentoo.org/news/2019/07/03/sks-key-poisoning.html](https://www.gentoo.org/news/2019/07/03/sks-key-poisoning.html)
-   Draft of the IETF WKS standard [https://datatracker.ietf.org/doc/html/draft-koch-openpgp-webkey-service-10](https://datatracker.ietf.org/doc/html/draft-koch-openpgp-webkey-service-10)
-   [eix-sync: Refreshing keys via WKD always fails](https://forums.gentoo.org/viewtopic-t-1107842.html)