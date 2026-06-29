## Contents

-   [[1] [Synopsis]](#Synopsis)
-   [[2] [Environment]](#Environment)
-   [[3] [Analysis]](#Analysis)
-   [[4] [Resolution]](#Resolution)
-   [[5] [See also]](#See_also)

## [Synopsis]

When updating a system or installing a new program users may run into \"blockers\". Blockers in Gentoo ebuilds simply mean that two packages cannot be installed at the same time on the same system.

## [Environment]

When upgrading, these are usually packages that have been superseded by other packages. And this is unfortunately common with names for libraries that are too generic. For example, libnw could be either [[[dev-games/libnw]](https://packages.gentoo.org/packages/dev-games/libnw)[]] or [[[sci-biology/newick-utils]](https://packages.gentoo.org/packages/sci-biology/newick-utils)[]].

## [Analysis]

    [blocks B      ] app-mobilephone/obex-data-server ("app-mobilephone/obex-data-server" is blocking app-mobilephone/obexd-0.43-r1)
    [blocks B      ] app-mobilephone/obexd[server] ("app-mobilephone/obexd[server]" is blocking app-mobilephone/obex-data-server-0.4.5)

     * Error: The above package list contains packages which cannot be
     * installed at the same time on the same system.

      (app-mobilephone/obex-data-server-0.4.5::gentoo, ebuild scheduled for merge) pulled in by
        >=app-mobilephone/obex-data-server-0.4.5 required by (gnome-base/gvfs-1.10.1::gentoo, ebuild scheduled for merge)

      (app-mobilephone/obexd-0.43-r1::gentoo, ebuild scheduled for merge) pulled in by
        app-mobilephone/obexd required by (net-wireless/gnome-bluetooth-3.2.1::gentoo, ebuild scheduled for merge)

## [Resolution]

    app-mobilephone/obexd[server]

Removing the blocker in this case is as simple as removing the `server` USE flag from wherever it is referenced ([make.conf], [package.use], or some other location).

Resolutions will not always be this simple. Be diligent in reading Portage output to determine how to resolve blockers.

## [See also]

-   [USE flags section](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE "Handbook:AMD64/Working/USE") in the AMD64 Gentoo Handbook