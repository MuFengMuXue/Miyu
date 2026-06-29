`FETCHCOMMAND` is a variable that defines the command used for fetching package sources from the Internet. It can be set in the [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] configuration file.

## Contents

-   [[1] [Syntax]](#Syntax)
-   [[2] [Variants]](#Variants)
-   [[3] [Speeding up downloads with Wget2]](#Speeding_up_downloads_with_Wget2)
-   [[4] [Speeding up downloads with aria2]](#Speeding_up_downloads_with_aria2)
    -   [[4.1] [Install]](#Install)
-   [[5] [See also]](#See_also)

## [Syntax]

The following placeholders can be used:

  -------------------------- ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------- ----------
  Placeholder                Meaning                                         Example                                                                                                                                   Required
  `\$`   Location of your local source file repository   [/var/cache/distfiles]                                 Yes
  `\$`      Destination file name                           [example-1.0.tar.xz]                                   Yes
  `\$`       Download URL                                    [https://example.com/download/example-1.0.tar.xz](https://example.com/download/example-1.0.tar.xz)        Yes
  `\$`   Space separated list of file digests            [blake2b:\<hexdigest\> sha512:\<hexdigest\>]
  -------------------------- ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------- ----------

## [Variants]

Specific variants of `FETCHCOMMAND` supported by Portage^[\[1\]](#cite_note-1)^ are listed below:

  ---------------------------------- -------------------------------------------------- --------------------------------------------------------------------------------------------
  Placeholder                        Meaning                                            Example
  `FETCHCOMMAND`          Used for HTTP/HTTPS/FTP downloads                  `FETCHCOMMAND="wget -t 3 -T 60 --passive-ftp -O \"\$/\$\" \"\$\""`
  `RESUMECOMMAND`         Used to resume a HTTP/HTTPS/FTP download           `RESUMECOMMAND="wget -c -t 3 -T 60 --passive-ftp -O \"\$/\$\" \"\$\""`
  `FETCHCOMMAND_FTP`      A more specific variant used exclusively for FTP
  `RESUMECOMMAND_FTP`     A more specific variant used exclusively for FTP
  `FETCHCOMMAND_RSYNC`    Used for downloading from an rsync mirror          `FETCHCOMMAND_RSYNC="rsync -LtvP \"\$\" \"\$/\$\""`
  `RESUMECOMMAND_RSYNC`   As above
  `FETCHCOMMAND_SSH`      Used for downloading over SSH
  `RESUMECOMMAND_SSH`     As above
  `FETCHCOMMAND_SFTP`     Used for downloading from a SFTP mirror
  ---------------------------------- -------------------------------------------------- --------------------------------------------------------------------------------------------

## [Speeding up downloads with Wget2]

[[[net-misc/wget2]](https://packages.gentoo.org/packages/net-misc/wget2)[]] is the successor to GNU Wget.

In many cases Wget2 downloads much faster than Wget1.x due to HTTP2, HTTP compression, parallel connections and use of If-Modified-Since HTTP header.^[\[2\]](#cite_note-2)^

Add the following line to your [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] file:

[FILE] **`/etc/portage/make.conf`**

    FETCHCOMMAND="wget2 -v --metalink=off --progress=none -t 3 -T 60 -O \"\$/\$\" \"\$\""
    RESUMECOMMAND="wget2 -v --metalink=off --progress=none -c -t 3 -T 60 -O \"\$/\$\" \"\$\""
    # Wget2 has no support for FTP
    FETCHCOMMAND_FTP="wget -t 3 -T 60 --passive-ftp -O \"\$/\$\" \"\$\""
    RESUMECOMMAND_FTP="wget -c -t 3 -T 60 --passive-ftp -O \"\$/\$\" \"\$\""

## [Speeding up downloads with aria2]

[fetchcommandwrapper] combines download tool [[[net-misc/aria2]](https://packages.gentoo.org/packages/net-misc/aria2)[]] with variable [`GENTOO_MIRRORS`](https://wiki.gentoo.org/wiki/GENTOO_MIRRORS "GENTOO MIRRORS") to speed up distfile downloads of Portage by downloading from multiple mirrors at the same time.

### [Install]

`root `[`#`]`emerge --ask app-portage/fetchcommandwrapper`

Then add the following line to your [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] file:

[FILE] **`/etc/portage/make.conf`**

    source /usr/share/fetchcommandwrapper/make.conf

## [See also]

-   [`GENTOO_MIRRORS`](https://wiki.gentoo.org/wiki/GENTOO_MIRRORS "GENTOO MIRRORS")
-   [`RESUMECOMMAND`](https://wiki.gentoo.org/index.php?title=RESUMECOMMAND&action=edit&redlink=1 "RESUMECOMMAND (page does not exist)")

1.  [[[↑](#cite_ref-1)] [[https://github.com/gentoo/portage/blob/master/cnf/make.globals#L62](https://github.com/gentoo/portage/blob/master/cnf/make.globals#L62)]]
2.  [[[↑](#cite_ref-2)] [[https://gitlab.com/gnuwget/wget2#gnu-wget2\-\--introduction](https://gitlab.com/gnuwget/wget2#gnu-wget2---introduction)]]