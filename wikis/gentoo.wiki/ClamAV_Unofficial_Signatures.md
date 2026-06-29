There are two good approaches to using unofficial signatures on Gentoo (and elsewhere). The first is to use [[[app-antivirus/fangfrisch]](https://packages.gentoo.org/packages/app-antivirus/fangfrisch)[]], and the second is to use freshclam itself. The eXtremeSHOK clamav-unofficial-sigs script is **not** a secure option.

## [Using freshclam]

Freshclam now supports https URLs, so if your unofficial signatures are available direct from an http(s) URL, then adding them to freshclam is easy. For example,

[CODE] **/etc/freshclam.conf**

    # These HTTP mirrors aren't quite official, but I've asked about them
    # on the sanesecurity mailing list and someone offered them to the public.
    DatabaseCustomURL https://mirror.rollernet.us/sanesecurity/badmacro.ndb
    DatabaseCustomURL https://mirror.rollernet.us/sanesecurity/blurl.ndb
    DatabaseCustomURL https://mirror.rollernet.us/sanesecurity/junk.ndb
    DatabaseCustomURL https://mirror.rollernet.us/sanesecurity/jurlbl.ndb
    DatabaseCustomURL https://mirror.rollernet.us/sanesecurity/jurlbla.ndb
    DatabaseCustomURL https://mirror.rollernet.us/sanesecurity/lott.ndb

There are only a few downsides to using freshclam:

1.  Freshclam can\'t rename the downloaded file, so if the source file is incorrectly named, freshclam will fail to validate it (because clamav won\'t know how to read it).
2.  Freshclam only supports http(s), so you\'re out of luck if your database is only served over rsync.
3.  There\'s currently [a bug in freshclam](https://bugzilla.clamav.net/show_bug.cgi?id=12522) that causes it to validate malformed databases, which will crash clamav. So if there\'s a chance that you\'ll download a bad database, freshclam may not be the best choice (until that bug is fixed).