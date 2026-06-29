This article describes how to enable font anti-aliasing in Emacs using the Xft library.

## Contents

-   [[1] [Enabling anti-aliased fonts for Emacs]](#Enabling_anti-aliased_fonts_for_Emacs)
    -   [[1.1] [Installation and setup]](#Installation_and_setup)
        -   [[1.1.1] [Lucid toolkit]](#Lucid_toolkit)
        -   [[1.1.2] [Motif toolkit]](#Motif_toolkit)
-   [[2] [External resources]](#External_resources)

## [Enabling anti-aliased fonts for Emacs]

### [Installation and setup]

** Note**\
Font anti-aliasing using the Xft library and FreeType fonts is available with Emacs 23 or later.

First, set the appropriate USE flags -- you *must* have the `xft` flag.

`root `[`#`]`echo "app-editors/emacs xft" >> /etc/portage/package.use`

Now it\'s time to install Emacs:

`root `[`#`]`emerge --ask app-editors/emacs`

You can now install some XFT fonts such as [[[media-fonts/dejavu]](https://packages.gentoo.org/packages/media-fonts/dejavu)[]]:

`root `[`#`]`emerge --ask media-fonts/dejavu`

Try starting Emacs with the desired XFT fonts:

`user `[`$`]`emacs --font 'DejaVu Sans Mono-12'`

If you\'re happy with this as your default font, set it in your [[\~/.Xresources]](https://wiki.gentoo.org/wiki/X_resources "X resources"):

`user `[`$`]`echo "Emacs.font: DejaVu Sans Mono-12" >> ~/.Xresources `

`user `[`$`]`xrdb -merge ~/.Xresources `

#### [Lucid toolkit]

When Emacs was built with the Lucid toolkit (i.e. with the `athena` or `Xaw3d` USE flags), the font of the menubar can be set using the following in your [\~/.Xresources]:

[CODE]

    Emacs.pane.menubar.font: DejaVu Sans-12

#### [Motif toolkit]

For Emacs built with the Motif toolkit (i.e. with the `motif` USE flag enabled), anti-aliased fonts can be enabled using the XFT font renderer in Motif. Make sure that [[[x11-libs/motif]](https://packages.gentoo.org/packages/x11-libs/motif)[]] was built with the `xft` flag, and add for example the following to your [\~/.Xresources], in order to set the font globally:

[CODE]

    Emacs.*.renderTable: emacs
    Emacs.*.renderTable.fontType: FONT_IS_XFT
    Emacs.*.renderTable.fontName: DejaVu Sans
    Emacs.*.renderTable.fontSize: 10

More specific control of resources is also possible, e.g., the following will set a bold font for the menubar:

[CODE]

    Emacs.pane.menubar.*.renderTable.fontStyle: bold

Don\'t forget to load the resources:

`user `[`$`]`xrdb -merge ~/.Xresources`

## [External resources]

For more details on Emacs with XFT pretty fonts, see:

-   [XftGnuEmacs](https://www.emacswiki.org/emacs/XftGnuEmacs) on the Emacs wiki

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Thomas Nichols, Ulrich Müller, Christian Faulhammer**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*