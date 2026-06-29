**Resources**

[[]][Home](https://gitweb.gentoo.org/repo/gentoo.git/tree/eclass)

[[]][Bugs](https://bugs.gentoo.org/buglist.cgi?quicksearch=eclass)

An eclass is a collection of code which can be used by more than one [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild").^[\[1\]](#cite_note-1)^ At the time of writing, all eclasses live in the [eclass/ directory](https://gitweb.gentoo.org/repo/gentoo.git/tree/eclass) of the [Gentoo ebuild repository](https://gitweb.gentoo.org/repo/gentoo.git/tree/).

To use an eclass, it must be *inherited*. This is done via the `inherit` function, which is provided by [ebuild.sh]. The inherit statement must come at the top of the ebuild, before any functions.^[\[2\]](#cite_note-2)^

[FILE] **`autotools-example-9999.ebuild`eclass usage snippet**

    # Copyright 2022 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    EAPI=8

    inherit autotools

    DESCRIPTION="Example ebuild using the autotools eclass"

    # ...

## [External resources]

-   [https://devmanual.gentoo.org/eclass-reference/](https://devmanual.gentoo.org/eclass-reference/)
-   [https://gentoo.org/glep/glep-0033.html](https://gentoo.org/glep/glep-0033.html)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://devmanual.gentoo.org/eclass-writing/](https://devmanual.gentoo.org/eclass-writing/)]]
2.  [[[↑](#cite_ref-2)] [[https://devmanual.gentoo.org/ebuild-writing/using-eclasses/#the-inherit-function](https://devmanual.gentoo.org/ebuild-writing/using-eclasses/#the-inherit-function)]]