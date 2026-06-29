Gentoo provides [packages for TeX Live](https://wiki.gentoo.org/wiki/TeX_Live "TeX Live") in the official tree, but they are [very difficult to update](https://wiki.gentoo.org/wiki/Project:TeX/TeX_Live_Bump_Story "Project:TeX/TeX Live Bump Story"). The TeX Live packages in the tree are several months (sometimes a year) behind upstream, while users who install TeX Live manually with the tlmgr manager get updates every day.

This procedure is very similar to other package managers like pip in python or the package managers of GNU R (using cran), and Perl (using cpan).

This page collects user experience and hints about the manual installation

## Contents

-   [[1] [Manual installation]](#Manual_installation)
-   [[2] [Dependencies]](#Dependencies)
-   [[3] [Updates]](#Updates)
-   [[4] [Trouble ahead]](#Trouble_ahead)

## [Manual installation]

Get the latest installer from [https://www.tug.org/texlive/](https://www.tug.org/texlive/) and follow the instructions to install system wide to [/usr/local] as root. To speed up the download process, upstream highly recommends the installation of LWP,^[\[1\]](#cite_note-1)^ which is packaged in the gentoo repositories as [[[dev-perl/libwww-perl]](https://packages.gentoo.org/packages/dev-perl/libwww-perl)[]].

`root `[`#`]`tar -xzf install-tl-unx.tar.gz # deflate the installation tar ball`

The texlive distribution can be installed via a graphical user interface (GUI), a terminal user interface (TUI) or a command-line interface (CLI).

The graphical installer requires [[[dev-lang/tk]](https://packages.gentoo.org/packages/dev-lang/tk)[]]. If [[[dev-lang/tk]](https://packages.gentoo.org/packages/dev-lang/tk)[]] is not installed, [install-tl] will fall back to the TUI-based installer, which will fail silently when starting the installation.

`root `[`#`]`emerge --ask dev-lang/tk`

`root `[`#`]`perl install-tl -gui`

The TUI-based installer does not depend on [[[dev-lang/tk]](https://packages.gentoo.org/packages/dev-lang/tk)[]] and can be run as follows:

`root `[`#`]`perl install-tl`

The CLI-based installer does not depend on [[[dev-lang/tk]](https://packages.gentoo.org/packages/dev-lang/tk)[]] either and can be run as follows:

`root `[`#`]`perl install-tl --no-interaction`

Let the installer create symbolic links for the binaries in [/usr/local/bin/].

## [Dependencies]

The manual TeX Live installation provides many packages, which could be installed via Portage too. To prevent Portage to install [[[app-text/texlive]](https://packages.gentoo.org/packages/app-text/texlive)[]] as dependency, one can add the package names in a .provided file:

[FILE] **[`/etc/portage/profile/package.provided/texlive.provided`](https://wiki.gentoo.org/wiki//etc/portage/profile/package.provided "/etc/portage/profile/package.provided")**

    app-text/texlive-9999
    app-text/texlive-core-9999
    dev-tex/latexdiff-9999
    dev-texlive/texlive-basic-9999
    dev-texlive/texlive-fontsextra-9999
    dev-texlive/texlive-fontsrecommended-9999
    dev-texlive/texlive-fontutils-9999
    dev-texlive/texlive-formatsextra-9999
    dev-texlive/texlive-latex-9999
    dev-texlive/texlive-latexextra-9999
    dev-texlive/texlive-latexrecommended-9999
    dev-texlive/texlive-luatex-9999
    dev-texlive/texlive-mathscience-9999
    dev-texlive/texlive-plaingeneric-9999
    dev-texlive/texlive-pstricks-9999
    dev-texlive/texlive-xetex-9999
    dev-tex/tex4ht-999999999999
    virtual/latex-base-1.0
    virtual/tex-base-9999

9999 tells portage, that we provide already the latest version of the package via tlmgr.

\
package.provided was banned in EAPI 7 for ebuilds, but is still fine and sometimes important for the local system.

## [Updates]

`root `[`#`]`tlmgr update --all`

## [Trouble ahead]

The manual installation of TeX Live bears the chance of other conflicts and bugs than a Portage installed TeX Live. Keep track of all commands regarding the administration of TeX. Using the package manager of the distribution and of a software suite on the same system is always a challenge.

1.  [[[↑](#cite_ref-1)] [[https://www.tug.org/texlive/acquire-netinstall.html#netlwp](https://www.tug.org/texlive/acquire-netinstall.html#netlwp)]]