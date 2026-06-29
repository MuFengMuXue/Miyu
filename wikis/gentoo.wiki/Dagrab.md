Dagrab is a CD ripper, might be faster than others. It can be used as a backend to abcde ([[[media-sound/abcde]](https://packages.gentoo.org/packages/media-sound/abcde)[]]), instead of cdparanoia (or libcdio-paranoia). Standalone use is also possible.

Dagrab is a very old software. As of 2017, most major Linux distributions don\'t provide dagrab. Fortuanetly in Gentoo it\'s still available as [[[media-sound/dagrab]](https://packages.gentoo.org/packages/media-sound/dagrab)[]].

## [History]

In fact, dagrab was forked. The orignal version was initiated by Marcello Urbani, from Feb 1998 to 2000. Its homepage, [http://web.tiscalinet.it/marcellou/dagrab.html](http://web.tiscalinet.it/marcellou/dagrab.html), is available as of 2017.

In Dec 1998 Miroslav Stibor released a forked version. The last release was in 2004. Its [homepage](http://vertigo.fme.vutbr.cz/~stibor/dagrab.html) was there until c. 2011. It can be [viewed](https://web.archive.org/web/*/http://vertigo.fme.vutbr.cz/~stibor/dagrab.html) by Wayback.

Gentoo provides the forked version, the last release 0.513. (The author versionated it as \"S0.513\".)

## [Use with abcde]

If CD ripping is slow with abcde (taking \> 4 min. to rip a CD), use dagrab.

[[[media-sound/abcde]](https://packages.gentoo.org/packages/media-sound/abcde)[]], a command-line CD encoder, relies on cdparanoia (or libcdio-paranoia) as a ripper. On some hardwares, cdparanoia is slow; setting the speed by the option [-S] has no effect.

To use dagrab, emerge abcde \>= 2.7. The configuration file, [/etc/abcde.conf] or [\$HOME/.abcde.conf] should have the following lines:

[CODE]

    CDROMREADERSYNTAX=dagrab
    # "-n 8" is the dagrab's default. For recent drives, 127 is a good try.
    DAGRABOPTS="-n 127"

[DAGRABOPTS] is the options to pass to dagrab. For the details, run [\$ dagrab -h], and see the dagrab\'s FAQ file, found at [/usr/share/doc/dagrab-\<version #\>/FAQ.bz2].

[DAGRABOPTS] is not documented up to abcde-2.8.1, but was fixed in [this upstream commit](https://git.einval.com/cgi-bin/gitweb.cgi?p=abcde.git;a=commit;h=c91ca32ad9ecd236324065bfa075ce388e9c75af).

## [Forum thread]

-   See [this thread](https://forums.gentoo.org/viewtopic-t-1059274.html)