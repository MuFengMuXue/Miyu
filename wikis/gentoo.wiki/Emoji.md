**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Fonts "Project:Fonts")][Project](https://wiki.gentoo.org/wiki/Project:Fonts "Project:Fonts")

[[]][Wikipedia](https://en.wikipedia.org/wiki/Computer_font "wikipedia:Computer font")

This is a home page for information about using fonts on Gentoo.

In general usage, a *font* is typically a file containing one or more variations of a [typeface](https://en.wikipedia.org/wiki/typeface "wikipedia:typeface"). In typographical usage, a *font* is a particular size, weight and style of a typeface.

The best starting point for general information about configuration, use and management of fonts on Gentoo, particularly for software running under X or a Wayland compositor (including [terminal emulators](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator")), is the [Fontconfig](https://wiki.gentoo.org/wiki/Fontconfig "Fontconfig") page.

Additionally:

-   For information about configuring fonts for the [Linux console](https://en.wikipedia.org/wiki/Linux_console "wikipedia:Linux console") specifically (rather than for GUI-based terminal emulators), refer to the [Fonts/Console](https://wiki.gentoo.org/wiki/Fonts/Console "Fonts/Console") page.

<!-- -->

-   For information about software for working with fonts, refer to the [Fonts/Software](https://wiki.gentoo.org/wiki/Fonts/Software "Fonts/Software") page.

<!-- -->

-   For background on font-related concepts, terminology, and systems (e.g. Unicode), refer to the [Fonts/Background](https://wiki.gentoo.org/wiki/Fonts/Background "Fonts/Background") page.

<!-- -->

-   For a high-level introduction to the systems involved in displaying text on Linux, refer to the external article \"[Modern text rendering with Linux: Overview](https://mrandri19.github.io/2019/07/24/modern-text-rendering-linux-overview.html)\".

## Contents

-   [[1] [Font installation]](#Font_installation)
    -   [[1.1] [Manual font installation]](#Manual_font_installation)
        -   [[1.1.1] [Global]](#Global)
        -   [[1.1.2] [Per-user]](#Per-user)
    -   [[1.2] [Font support for specific characters]](#Font_support_for_specific_characters)
        -   [[1.2.1] [Noto]](#Noto)
        -   [[1.2.2] [Symbols]](#Symbols)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Font installation]

A variety of fonts are provided by the `media-fonts` package category. Fonts provided by the `gentoo` repository can be listed by viewing the contents of the [/var/db/repos/gentoo/media-fonts/] directory, or by using [eix](https://wiki.gentoo.org/wiki/Eix "Eix"):

`user `[`$`]`eix -C media-fonts`

[[[media-fonts/fonts-meta]](https://packages.gentoo.org/packages/media-fonts/fonts-meta)[]] is a meta package providing fonts to cover most needs.

[[[media-fonts/corefonts]](https://packages.gentoo.org/packages/media-fonts/corefonts)[]] provides Microsoft\'s TrueType core fonts.

### [Manual font installation]

#### [Global]

System administrators (those with root privileges) can copy fonts into [/usr/local/share/fonts]. This will make fonts available to any user on the system.

`root `[`#`]`cp /home/larry/Downloads/Inconsolata.otf /usr/local/share/fonts`

#### [Per-user]

Users can create a [.local/share/fonts] directory in their home directory. Font files can then be added to that directory, or to a subdirectory of that directory:

`user `[`$`]`mkdir -p ~/.local/share/fonts `

`user `[`$`]`cp ~/Downloads/Inconsolata.otf ~/.local/share/fonts `

To make a newly-installed font available to applications, refresh the Fontconfig cache via [[[fc-cache(1)]](https://man.archlinux.org/man/fc-cache.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`user `[`$`]`fc-cache -fv`

Use an application such as a [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") or an office program to confirm that the font is now available.

** Note**\
Historically, the [\~/.fonts] directory was used to store fonts on a per-user basis.

### [Font support for specific characters]

** Note**\
Refer to the [\"Writing systems\" section of the Fonts/Background page](https://wiki.gentoo.org/wiki/Fonts/Background#Writing_systems "Fonts/Background") for an explanation of the word *glyph* and related terminology.

Gentoo doesn\'t install many fonts by default. If an application needs to display a particular character, but the current font (or, perhaps, any font known to the application) doesn\'t have a glyph for it, the character will be rendered using the *.notdef* character, informally known as *tofu*. Tofu is typically displayed as either:

-   an empty square, ☐;
-   a box with an X in it, ☒;
-   a box with a question mark in it, ⍰;
-   a box containing the Unicode code point in hexadecimal.

To check if any installed font provides a glyph for a particular Unicode code point, use [[[fc-list(1)]](https://man.archlinux.org/man/fc-list.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - provided by the [[[media-libs/fontconfig]](https://packages.gentoo.org/packages/media-libs/fontconfig)[]] package - to list all installed fonts with such a glyph, specifying the code point in hexadecimal:

`user `[`$`]`fc-list ':charset=3088'`

#### [Noto]

Google\'s \"Noto\" typeface family is an attempt to provide a single typeface with glyphs for all assigned Unicode code points, which cover most of the world\'s scripts; the name \"Noto\" is an abbreviation of \"No Tofu\".

On Gentoo, the Noto family is available via the [[[media-fonts/noto]](https://packages.gentoo.org/packages/media-fonts/noto)[]] (including support for Arabic, Bengali, Persian, Tamil, and Thai), [[[media-fonts/noto-cjk]](https://packages.gentoo.org/packages/media-fonts/noto-cjk)[]] (including support for Chinese, Japanese and Korean), and [[[media-fonts/noto-emoji]](https://packages.gentoo.org/packages/media-fonts/noto-emoji)[]] packages.

Once installed, Noto Emoji can be configured for use as a fallback font (used when a glyph does not exist in the selected font) for Emoji by running:

`root `[`#`]`eselect fontconfig enable 75-noto-emoji-fallback.conf`

Note that Web browsers tend to use their own font selection logic; often simply installing the package is sufficient.

#### [Symbols]

One option for a symbol font is Symbola, provided by the [[[media-fonts/ttf-ancient-fonts::guru]](https://gpo.zugaina.org/Overlays/guru/media-fonts/ttf-ancient-fonts)[]] package in the [GURU overlay](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU"). This font has previously been provided by the [[[media-fonts/symbola::guru]](https://gpo.zugaina.org/Overlays/guru/media-fonts/symbola)[]] package, [which is now obsolete](https://gitweb.gentoo.org/repo/proj/guru.git/commit/?id=79239b5207c500a5cd0defd9012345fbe97db3ea).

## [See also]

-   [Fontconfig](https://wiki.gentoo.org/wiki/Fontconfig "Fontconfig") --- intended to provide uniform font selection and configuration amongst all GUI applications.
-   [Fonts/Background](https://wiki.gentoo.org/wiki/Fonts/Background "Fonts/Background") --- a quick and informal introduction to font-related concepts, terminology, and systems, with the aim of facilitating understanding and solving font-related issues
-   [Fonts/Console](https://wiki.gentoo.org/wiki/Fonts/Console "Fonts/Console")
-   [Fonts/Software](https://wiki.gentoo.org/wiki/Fonts/Software "Fonts/Software") --- list of end-user software for working with fonts
-   [Localization/Guide/The_Euro_symbol](https://wiki.gentoo.org/wiki/Localization/Guide/The_Euro_symbol "Localization/Guide/The Euro symbol") --- how to display the Euro symbol (€) for the console and in X.

## [External resources]

-   [Font Library](https://fontlibrary.org/) - Font distribution website that beautifully displays fonts.