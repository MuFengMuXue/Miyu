This page contains [[changes](https://wiki.gentoo.org/index.php?title=Fontconfig&oldid=1244952&diff=1421229)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Fontconfig/de "Fontconfig (1% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Fontconfig/es "Fontconfig (98% translated)")
-   [français](https://wiki.gentoo.org/wiki/Fontconfig/fr "Fontconfig (71% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Fontconfig/hu "Fontconfig (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Fontconfig/pl "Fontconfig/pl (4% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Fontconfig/ru "Fontconfig (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Fontconfig/zh-cn "Fontconfig (54% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Fontconfig/ja "Fontconfig (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Fontconfig/ko "Fontconfig/ko (68% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Fontconfig "wikipedia:Fontconfig")

[[]][Home](http://www.freedesktop.org/wiki/Software/fontconfig/)

[Fontconfig] ([[[media-libs/fontconfig]](https://packages.gentoo.org/packages/media-libs/fontconfig)[]]) is intended to provide uniform font selection and configuration amongst all GUI applications. Although it is common for a [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") to provide its own font overrides and configuration utilities, [Fontconfig] is still the underlying system.

Refer to the [Fonts](https://wiki.gentoo.org/wiki/Fonts "Fonts") page for more general information about using fonts on Gentoo, and to the [Fonts/Background](https://wiki.gentoo.org/wiki/Fonts/Background "Fonts/Background") page for background information about font-related concepts, terminology and systems.

## Contents

-   [[1] [Installing]](#Installing)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Generic]](#Generic)
    -   [[2.2] [Gentoo specific]](#Gentoo_specific)
        -   [[2.2.1] [Listing available files]](#Listing_available_files)
        -   [[2.2.2] [Enabling a file]](#Enabling_a_file)
        -   [[2.2.3] [Disabling a file]](#Disabling_a_file)
    -   [[2.3] [Custom system wide configuration]](#Custom_system_wide_configuration)
    -   [[2.4] [Per-user configuration]](#Per-user_configuration)
    -   [[2.5] [Checking configuration]](#Checking_configuration)
    -   [[2.6] [Anti-aliasing, hinting, and sub-pixel rendering]](#Anti-aliasing.2C_hinting.2C_and_sub-pixel_rendering)
        -   [[2.6.1] [Forcing hinting]](#Forcing_hinting)
        -   [[2.6.2] [Using sub-pixel rendering]](#Using_sub-pixel_rendering)
        -   [[2.6.3] [Regarding autohinter]](#Regarding_autohinter)
-   [[3] [Querying installed fonts]](#Querying_installed_fonts)
-   [[4] [Installing fonts not packaged in Gentoo]](#Installing_fonts_not_packaged_in_Gentoo)
    -   [[4.1] [For your account]](#For_your_account)
    -   [[4.2] [System Wide]](#System_Wide)
-   [[5] [Picking fonts]](#Picking_fonts)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installing]

When [Fontconfig] is needed, it will almost certainly be installed already. If not, make sure to set up the graphical subsystem (i.e., [X](https://wiki.gentoo.org/wiki/X "X") or [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland")) and [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") properly.

### [USE flags]

### [USE flags for] [media-libs/fontconfig](https://packages.gentoo.org/packages/media-libs/fontconfig) [[]] [A library for configuring and customizing font access]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`nls`](https://packages.gentoo.org/useflags/nls)     Add Native Language Support (using gettext - GNU locale utilities)
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Configuration]

** Note**\
Changes to [Fontconfig] files will reflect only in applications started after the change!

### [Generic]

[Fontconfig] uses XML files in the [/etc/fonts/] directory to generate its internal configuration. By default it parses [/etc/fonts/fonts.conf] (users should not edit this file!) which sets some sane defaults and usually contains code to also parse [/etc/fonts/conf.d/] content. In addition there is the [/etc/fonts/conf.avail/] directory that contains various possible configuration files that each cover some aspect of [Fontconfig]. It\'s customary to symlink necessary files to [/etc/fonts/conf.d/]. These files are executed in order they are named; for this reason their names start with a two digit number with the first digit (tens) indicating what the file affects (called the class).

### [Gentoo specific]

Gentoo ships an [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect") module ([eselect fontconfig]) that does exactly what was described in generic way - it manages symlinks of files in [/etc/fonts/conf.avail/] by adding or removing them from the [/etc/fonts/conf.d/] directory. For obvious reasons changing system wide configuration requires appropriate permissions.

The following subsections explain how to deal with the [fontconfig] eselect module.

#### [Listing available files]

The [list] command shows the available [Fontconfig] files, and marks the enabled ones with an asterisk (`*`).

`root `[`#`]`eselect fontconfig list `

    Available fontconfig .conf files (* is enabled):
      [1]   10-autohint.conf *
      [2]   10-no-sub-pixel.conf
      [3]   10-sub-pixel-bgr.conf
      [4]   10-sub-pixel-rgb.conf
      [5]   10-sub-pixel-vbgr.conf
      [6]   10-sub-pixel-vrgb.conf
      [7]   10-unhinted.conf
      [8]   11-lcdfilter-default.conf
      [9]   11-lcdfilter-legacy.conf
      ...

** Warning**\
Different systems have different files in [fonts.avail] so the output *will* be different. Never blindly use a list number from another source (such as blog posts or wiki articles).

#### [Enabling a file]

Files can be enabled either by filename or by the number in brackets. These two do the same thing:

`root `[`#`]`eselect fontconfig enable 10-sub-pixel-rgb.conf `

`root `[`#`]`eselect fontconfig enable 4 `

#### [Disabling a file]

Files can be disabled likewise:

`root `[`#`]`eselect fontconfig disable 10-sub-pixel-rgb.conf `

`root `[`#`]`eselect fontconfig disable 4 `

### [[] Custom system wide configuration]

To create a custom, system-wide [fontconfig] file, enable [51-local.conf] and create [/etc/fonts/local.conf] (this is an XML file).

[FILE] **`/etc/fonts/local.conf`Example file that sets preferred font fallback order for sans-serif font**

    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
    <fontconfig>
      <alias>
        <family>sans-serif</family>

          <family>Ubuntu</family>
          <family>TakaoPGothic</family>
          <family>Droid Sans</family>
        </prefer>
        <default><family>DejaVu Sans</family></default>
      </alias>
    </fontconfig>

To be clear, this says that when it comes to sans-serif fonts, we *prefer* using Ubuntu, TakaoPGothic, and Droid Sans fonts (in that order) over DejaVu Sans (which can be used as a *default* choice only when necessary). Obviously, different choices can be made here.

### [Per-user configuration]

To create per-user [Fontconfig] files, enable [50-user.conf] (which might be enabled by default), and have the end users use the [\~/.config/fontconfig/fonts.conf] file. This file has the same XML format as [local.conf].

** Note**\
This is one way how a desktop environment might try to affect font rendering. It might be prudent to disable this to be sure that what\'s being shown is actually system wide configuration when customizing it. Disabling it also makes font rendering more uniform across user accounts.

** Note**\
The previously used [\~/.fonts.conf] is now deprecated in favor of the `$XDG_CONFIG_HOME` based location. This variable by defaults points to [\~/.config].

### [Checking configuration]

Check the default font replacement, for example for Arial, by typing:

`user `[`$`]`fc-match Arial`

### [][Anti-aliasing, hinting, and sub-pixel rendering]

Rendering aspects can be tuned as well. In the following sections the *Anti-aliasing*, *Hinting* and *Sub-pixel rendering* features are tuned.

  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Feature               Description
  Anti-aliasing         is enabled by default and makes fonts less blocky.
  Hinting               is an attempt to cope with the low pixel count per unit of area of current displays. Correct hinting makes characters more crisp but since font metrics aren\'t changed (and arguably should not change) affects how overall the rendered text looks like.
  Sub-pixel rendering   uses the fact that LCD matrix has three primaries to effectively triple the resolution of text but can make characters appear not entirely black. To combat that [lcdfilter] is to be used with sub-pixel rendering (available for newer [Fontconfig]) but it can blur the characters too much. In the end this entirely depends on person how they like their text.
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [Forcing hinting]

The default [Fontconfig] behavior regarding hinting is rather undocumented, but it can be made deterministically sub-optimal by making a system wide default.

1.  [First enable [/etc/fonts/local.conf]](https://wiki.gentoo.org/wiki/Fontconfig#Custom_system_wide_configuration "Fontconfig")
2.  Edit the [local.conf] file to include full hinting by default

This [local.conf] snippet enables full hinting:

[FILE] **`/etc/fonts/local.conf`Setting hinting to full**

    <match target="font">
      <edit mode="assign" name="hintstyle">
        <const>hintfull</const>
      </edit>
    </match>

** Note**\
Most fonts look best with full hinting but others need slight or more rarely some other hinting option. Some fonts for one reason or another will always be ugly.

#### [Using sub-pixel rendering]

It\'s important to determine the sub-pixel layout of the LCD matrix. It\'s usually RGB ([10-sub-pixel-rgb.conf]) but the only way to be sure is to either consult display specification or use this [sub-pixel layout test](http://www.lagom.nl/lcd-test/subpixel.php) to determine it.

Once determined, enable the appropriate [10-sub-pixel-*\<matrix type\>*.conf] file.

`root `[`#`]`eselect fontconfig enable 10-sub-pixel-rgb.conf`

It\'s strongly advised that [lcdfilter], if available, is used with sub-pixel rendering. It comes in different varieties but the default ([11-lcdfilter-default.conf]) should be appropriate for all common fonts.

`root `[`#`]`eselect fontconfig enable 11-lcdfilter-default.conf`

Some graphical toolkits ignore the fontconfig sub-pixel rendering settings and might require additional setup. For example, [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") requires setting the `gtk-xft-rgba` option:

[FILE] **`~/.config/gtk-3.0/settings.ini`Enable sub-pixel rendering with rgb layout**

    [Settings]
    gtk-xft-rgba = rgb

#### [Regarding autohinter]

Autohinter attempts to do automatic hinting disregarding any existing hinting information. Until recently it was the default because TrueType2 was covered by patents but now that they have expired there\'s very little reason to use it. From technical point of view it does better than broken or no hinting information but it will be strongly sub-optimal for fonts with good hinting information. Generally system fonts are of the second kind so autohinter should not be used.

** Warning**\
Autohinter is not compatible with sub-pixel rendering, do not use the two together!

## [Querying installed fonts]

[Fontconfig] provides the [fc-\*] suite of programs to provide information about the fonts it\'s aware of.

To list all fonts known to [Fontconfig], use [[[fc-list(1)]](https://man.archlinux.org/man/fc-list.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`user `[`$`]`fc-list`

    /usr/share/fonts/noto/NotoSansArabic-SemiCondensedExtraBold.ttf: Noto Sans Arabic,Noto Sans Arabic SemCond ExtBd:style=SemiCondensed ExtraBold,Regular
    /usr/share/fonts/noto/NotoSerifDevanagari-CondensedBold.ttf: Noto Serif Devanagari Condensed:style=Bold
    /usr/share/fonts/urw-fonts/URWGothic-DemiOblique.ttf: URW Gothic:style=Demi Oblique
    [...]

If a particular font is known to be installed in one of the paths configured for use by [Fontconfig], but doesn\'t appear in the output of [[[fc-list(1)]](https://man.archlinux.org/man/fc-list.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], it might be that the [Fontconfig] cache needs to be refreshed, which can be done by running [[[fc-cache(1)]](https://man.archlinux.org/man/fc-cache.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`user `[`$`]`fc-cache -fv`

To retrieve information about a specific font, use [[[fc-query(1)]](https://man.archlinux.org/man/fc-query.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`user `[`$`]`fc-query /usr/share/fonts/urw-fonts/URWGothic-DemiOblique.ttf`

    Pattern has 25 elts (size 32)
        family: "URW Gothic"(s)
        familylang: "en"(s)
        style: "Demi Oblique"(s)
        stylelang: "en"(s)
        fullname: "URW Gothic Demi Oblique"(s)
        fullnamelang: "en"(s)
        slant: 110(i)(s)
        weight: 200(f)(s)
        width: 100(f)(s)
        foundry: "URW "(s)
        file: "/usr/share/fonts/urw-fonts/URWGothic-DemiOblique.ttf"(s)
        index: 0(i)(s)
        outline: True(s)
        scalable: True(s)
        charset:
        0000: 00000000 ffffffff ffffffff 7fffffff 00000000 ffffffff ffffffff ffffffff
        0001: ffffffff ffffffff ffffffff ffffffff 00040000 00000000 00000000 fc000000
        0002: 0f000000 00000000 00000000 00000000 00000000 00000000 3f0002c0 00000000
        0003: 00000000 00000000 00000000 00000000 ffffd7f0 fffffffb 00627fff 00000000
        0004: ffffffff ffffffff ffffffff 003c000c 3fcf0000 0fcfcc0f 03009801 0000c30c
        001e: 00000000 00000000 00000000 00000000 0000003f 00000000 00000000 000c0000
        0020: 7fb80004 560d0047 00000010 83f10000 00000000 00009098 20000000 00000000
        0021: 514e8020 00e0e145 78000000 00000000 03ff0000 00200100 003f0050 00000000
        0022: e6aeabed 00b04fa9 00000120 00000c37 03e000fc 0800003c 00000000 00000000
        0023: 00010004 00000603 00000000 00000000 00000000 00000000 00000000 00000000
        0025: 11111005 10101010 ffff0000 0001ffff 000f1111 96241c03 03008cd8 00000040
        0026: 00000000 1c000000 00000005 00000c69 00000000 00000000 00000000 00000000
        0030: 0c000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
        00ef: 00000000 00000000 00000000 00000000 00000000 80000000 ffffffff fc001fff
        00fb: 0000001f 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    (s)
        lang: aa|af|av|ay|ba|be|bg|bi|br|bs|bua|ca|ce|ch|co|cs|cy|da|de|el|en|eo|es|et|eu|fi|fj|fo|fr|fur|fy|gd|gl|gv|ho|hr|hu|ia|id|ie|ik|io|is|it|kaa|ki|kk|kl|kum|ky|la|lb|lez|lt|lv|mg|mh|mk|mo|mt|nb|nds|nl|nn|no|nr|nso|ny|oc|om|os|pl|pt|rm|ro|ru|se|sel|sh|sk|sl|sma|smj|smn|so|sq|sr|ss|st|sv|sw|tg|tk|tl|tn|tr|ts|tt|tyv|uk|uz|vo|vot|wa|wen|wo|xh|yap|zu|an|crh|csb|fil|hsb|ht|jv|kj|ku-tr|kwm|lg|li|mn-mn|ms|na|ng|pap-an|pap-aw|rn|rw|sc|sg|sn|su|za(s)
        fontversion: 65536(i)(s)
        fontformat: "TrueType"(s)
        decorative: False(s)
        postscriptname: "URWGothic-DemiOblique"(s)
        color: False(s)
        symbol: False(s)
        variable: False(s)
        fonthashint: True(s)
        order: 0(i)(s)

Each of the listed properties, such as `lang` and `fontformat`, is called an [element].

To search for fonts that best match specified elements, use [[[fc-match(1)]](https://man.archlinux.org/man/fc-match.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`user `[`$`]`fc-match -s 'sans:lang=de' | head -n5`

    LiberationSans-Regular.ttf: "Liberation Sans" "Regular"
    NotoSans-Regular.ttf: "Noto Sans" "Regular"
    NotoSans-Italic.ttf: "Noto Sans" "Italic"
    DejaVuSans.ttf: "DejaVu Sans" "Book"
    DejaVuSans-Bold.ttf: "DejaVu Sans" "Bold"

The `-s` option is used to return all possible matches, ranked by quality of match; the pipe to [[[head(1)]](https://man.archlinux.org/man/head.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] returns the top five results. Without the `-s` option, only the best match is returned.

To list all serif OTF fonts known to [Fontconfig], pass `CFF` ([Compact Font Format](https://en.wikipedia.org/wiki/Compact_Font_Format "wikipedia:Compact Font Format")) as the argument to the `fontformat` element:

`user `[`$`]`fc-match -s 'serif:fontformat=CFF'`

    AccanthisADFStd-Regular.otf: "Accanthis ADF Std" "Regular"
    AurelisADFNo2Std-Regular.otf: "Aurelis ADF No2 Std" "Regular"
    latinmodern-math.otf: "Latin Modern Math" "Regular"
    [...]

## [Installing fonts not packaged in Gentoo]

### [For your account]

By default, [Fontconfig] includes [\$/.local/share/fonts/] in its search path for fonts.^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^. Font files (e.g. OTF and TTF files) can be directly added to that directory; after doing so, run [[[fc-cache(1)]](https://man.archlinux.org/man/fc-cache.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] to make [Fontconfig] pick them up. Refer to the [XDG directories](https://wiki.gentoo.org/wiki/XDG_directories "XDG directories") page for further information about the `XDG_DATA_HOME` variable.

### [System Wide]

System administrators (those with root privileges) can copy fonts into the system\'s [/usr/local/share/fonts] directory. This will make fonts available to any user on the system.

`root `[`#`]`cp /home/larry/Downloads/Inconsolata.otf /usr/local/share/fonts`

If fontconfig isn\'t already set up to look up in [/usr/local/share/fonts], add the following file.

[FILE] **`/etc/conf.avail/00-additionals-directories.conf`Enabling system-wide locally installed fonts**

    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">
    <fontconfig>
      <dir>/usr/local/share/fonts</dir>
    </fontconfig>

And enable the file with the following command:

`root `[`#`]`eselect fontconfig enable 00-additionals-directories.conf`

## [Picking fonts]

Choosing the right font can be trickier than deciding on the right hinting type. For one reason or another, some fonts will never be perfect --- but it\'s certainly possible to make them look better than, say, the Windows 7 default font configuration.

** Note**\
Many fonts don\'t provide glyphs for every assigned Unicode codepoint, due to the size of Unicode. If a font doesn\'t provide a glyph for a given codepoint, the character might be represented by a substitute character (such as a rectangle containing the hexadecimal value of the code point), or by a glyph from a different font (the \"fallback font\"), depending on the application.

Here are some recommendations regarding well known fonts in Gentoo:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Font family                                                                                                                                                                                                                                                                                                                                                                                                        Pros                                                                                                                                                                                                                                                                                                                                                                                                                      Cons

  Liberation\                                                                                                                                                                                                                                                                                                                                                                                                        [Red Hat\'s](https://en.wikipedia.org/wiki/Red_Hat "wikipedia:Red Hat") fonts, which are metric-compatible with MS TrueType [corefonts](https://en.wikipedia.org/wiki/Corefonts "wikipedia:Corefonts"), have a decent, modern look. This is the [Gentoo Fonts team](https://wiki.gentoo.org/wiki/Project:Fonts "Project:Fonts") recommendation for default Latin fonts. Covers about 2,600 code points.   Latin, Greek, Cyrillic, and Hebrew only. A few glyphs may have hinting trouble.
  [[[media-fonts/liberation-fonts]](https://packages.gentoo.org/packages/media-fonts/liberation-fonts)[]]

  Linux Libertine\                                                                                                                                                                                                                                                                                                                                                                                                   Very similar to Liberation, covering about 2,700 code points. Linux Libertine itself is proportional serif only, but the package contains less extensive sans and mono fonts, as well. Can be used as a fallback for some glyphs not in Liberation.                                                                                                                                                                       Latin, Greek, Cyrillic, and Hebrew only. Sans and mono fonts are limited.
  [[[media-fonts/libertine]](https://packages.gentoo.org/packages/media-fonts/libertine)[]]

  Noto\                                                                                                                                                                                                                                                                                                                                                                                                              Google\'s font family that aims to support all the world\'s languages (so, well over 60,000 code points). It goes well with Liberation or Droid. Adobe\'s Source Han Sans fonts are included for [CJK](https://en.wikipedia.org/wiki/CJK "wikipedia:CJK"). Recommended as a fallback for many glyphs not covered by Liberation.                                                                                   Big download.
  [[[media-fonts/noto]](https://packages.gentoo.org/packages/media-fonts/noto)[]]

  DejaVu\                                                                                                                                                                                                                                                                                                                                                                                                            Many styles and covers a lot of code points (about 6,100 for sans).                                                                                                                                                                                                                                                                                                                                                       Exceptionally wide --- even condensed is wider than same-height monospace. Overall second to [Verdana](https://en.wikipedia.org/wiki/Verdana "wikipedia:Verdana") (an MS font) in width. Sans-serif font is only average.
  [[[media-fonts/dejavu]](https://packages.gentoo.org/packages/media-fonts/dejavu)[]]

  Droid\                                                                                                                                                                                                                                                                                                                                                                                                             Covers a lot of code points and scripts.                                                                                                                                                                                                                                                                                                                                                                                  Very dry, wide yet thin glyphs. Clearly designed with handheld devices and their small screens in mind.
  [[[media-fonts/droid]](https://packages.gentoo.org/packages/media-fonts/droid)[]]

  Gentium Plus\                                                                                                                                                                                                                                                                                                                                                                                                      Fairly distinctive; might appeal to people who like narrow fonts.                                                                                                                                                                                                                                                                                                                                                         Serif only. As with other [SIL](https://en.wikipedia.org/wiki/SIL_International "wikipedia:SIL International") fonts, the hinting is questionable.
  [[[media-fonts/sil-gentium]](https://packages.gentoo.org/packages/media-fonts/sil-gentium)[]]

  Ubuntu\                                                                                                                                                                                                                                                                                                                                                                                                            Used in [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu_(operating_system) "wikipedia:Ubuntu (operating system)") (obviously). A distinctive font family with a style which might not appeal to everyone. Overall looks good and covers a fair number of code points.                                                                                                                                               Only the sans-serif font is truly polished; narrow and monospaced versions are unfinished. No known serif font that would accompany it well.
  [[[media-fonts/ubuntu-font-family]](https://packages.gentoo.org/packages/media-fonts/ubuntu-font-family)[]]

  URW\                                                                                                                                                                                                                                                                                                                                                                                                               Metric compatible with popular Adobe fonts (among others?).                                                                                                                                                                                                                                                                                                                                                               Seem to require slight hinting.
  [[[media-fonts/urw-fonts]](https://packages.gentoo.org/packages/media-fonts/urw-fonts)[]]

  MS TrueType corefonts\                                                                                                                                                                                                                                                                                                                                                                                             Includes most fonts used in documents and on the web.                                                                                                                                                                                                                                                                                                                                                                     MS does not distribute them nowadays, so the available fonts are from many years ago and do not reflect their current state (not to mention the state of the art). Obviously, lacks fonts introduced more recently. Require full hinting.
  [[[media-fonts/corefonts]](https://packages.gentoo.org/packages/media-fonts/corefonts)[]]

  Unifont\                                                                                                                                                                                                                                                                                                                                                                                                           Covers a lot of code points.                                                                                                                                                                                                                                                                                                                                                                                              In addition to being *ugly as sin*, it also fails some basic requirements to be considered a typeface. Is it sans-serif? Is it serif? *Please never use this.*
  [[[media-fonts/unifont]](https://packages.gentoo.org/packages/media-fonts/unifont)[]]
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

## [External resources]

-   In-depth articles from Arch Linux wiki on:
    -   [Font configuration](https://wiki.archlinux.org/index.php/Font_configuration)
    -   [Infinality](https://wiki.archlinux.org/index.php/Infinality)
-   [Official [Fontconfig] documentation for users](http://freedesktop.org/software/fontconfig/fontconfig-user.html)
-   [Wikipedia article on font hinting](https://en.wikipedia.org/wiki/Hinting "wikipedia:Hinting")

## [References]

1.  [[[↑](#cite_ref-1)] [[Function `FcConfigXdgDataHome` in [fccfg.c]. Accessed on 2024-03-16.](https://gitlab.freedesktop.org/fontconfig/fontconfig/-/blob/main/src/fccfg.c?ref_type=heads#L2562)]]
2.  [[[↑](#cite_ref-2)] [[Function `FcStrSet` in [fcxml.c]. Accessed on 2024-03-16.](https://gitlab.freedesktop.org/fontconfig/fontconfig/-/blob/main/src/fcxml.c?ref_type=heads#L1292)]]