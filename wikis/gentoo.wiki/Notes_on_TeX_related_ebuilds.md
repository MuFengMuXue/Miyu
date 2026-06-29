## Contents

-   [[1] [Dependencies]](#Dependencies)
    -   [[1.1] [Run time dependencies for packages like TeX editors and GUIs]](#Run_time_dependencies_for_packages_like_TeX_editors_and_GUIs)
    -   [[1.2] [Run time dependencies for packages with specific TeX dependencies]](#Run_time_dependencies_for_packages_with_specific_TeX_dependencies)
    -   [[1.3] [Build time dependencies for packages like PDF manuals]](#Build_time_dependencies_for_packages_like_PDF_manuals)
-   [[2] [Migrate SRC_URI from CTAN to TexLive (draft)]](#Migrate_SRC_URI_from_CTAN_to_TexLive_.28draft.29)
-   [[3] [VARTEXFONTS]](#VARTEXFONTS)
-   [[4] [Notes to be written]](#Notes_to_be_written)

### [Dependencies]

We have two virtual ebuilds in the tree which consumers of tex/latex should depend on (see also [[[bug #195894]](https://bugs.gentoo.org/show_bug.cgi?id=195894)[]]).

1.  [[[virtual/latex-base]](https://packages.gentoo.org/packages/virtual/latex-base)[]] (required in most cases)
2.  [[[virtual/tex-base]](https://packages.gentoo.org/packages/virtual/tex-base)[]]

#### [Run time dependencies for packages like TeX editors and GUIs]

If a package requires (La)TeX at runtime, but we do not know what the user wants to do with it exactly, it should depend on [[[app-text/texlive]](https://packages.gentoo.org/packages/app-text/texlive)[]].

Examples: [[[app-office/texstudio]](https://packages.gentoo.org/packages/app-office/texstudio)[]].

[FILE] **`examples/a-tex-gui*.ebuild`**

    RDEPEND="app-text/texlive"

#### [Run time dependencies for packages with specific TeX dependencies]

If a package requires specific TeX packages at runtime, like in a music score editor, which renders a score with LaTeX, it should depend on [[[virtual/latex-base]](https://packages.gentoo.org/packages/virtual/latex-base)[]] plus the specific packages.

Examples: [[[media-sound/lilypond]](https://packages.gentoo.org/packages/media-sound/lilypond)[]]. TODO: FILEBOX

#### [Build time dependencies for packages like PDF manuals]

If a package requires TeX only at build time, it should depend on [[[virtual/latex-base]](https://packages.gentoo.org/packages/virtual/latex-base)[]] and if required also depend on specific tex packages.

Examples: [[[app-doc/kicad-doc]](https://packages.gentoo.org/packages/app-doc/kicad-doc)[]] and [[[media-gfx/inkscape]](https://packages.gentoo.org/packages/media-gfx/inkscape)[]].

[FILE] **`media-gfx/inkscape*.ebuild`**

    RDEPEND="
        latex? (
            virtual/latex-base
            media-gfx/pstoedit[plotutils]
            app-text/dvipsk
        )
    "

### [][Migrate SRC_URI from CTAN to TexLive (draft)]

It is a common problem for our ebuilds that the CTAN server provides

1.  only the latest version of a package
2.  this package sometimes has no version information in the filename (the new version overwrites the old version)

The Gentoo mirror was misused as primary source as workaround for many TeX ebuilds.

[FILE] **`example.ebuild`**

    ..
    SRC_URI="mirror://gentoo/$.zip"
    ..

Sometimes the developer webspace was used, which is much cleaner but not ideal too.

We should migrate to the texlive ftp server [ftp://tug.org/historic/systems/texlive/](ftp://tug.org/historic/systems/texlive/)

[FILE] **`example.ebuild`**

    ftp://tug.org/historic/systems/texlive/2015/tlnet-final/archive/acronym.tar.xz
    ftp://tug.org/historic/systems/texlive/2016/tlnet-final/archive/acronym.tar.xz
    ftp://tug.org/historic/systems/texlive/2017/tlnet-final/archive/acronym.tar.xz

Enables us to create a generic SRC_URI

[FILE] **`example.ebuild`**

    SRC_URI="ftp://tug.org/historic/systems/texlive/$/tlnet-final/archive/$.tar.xz"

### [VARTEXFONTS]

[kpathsea] sets the path for font cache generation to (???) which is outside of the sandbox.

Setting [VARTEXFONTS=\$/fonts] prevents sandbox violations. See also the Tracker [[[bug #223077]](https://bugs.gentoo.org/show_bug.cgi?id=223077)[]]

### [Notes to be written]

-   Procedure how to test a latex ebuild