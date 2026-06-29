**Resources**

[[]][Home](https://url/to/homepage)

[[]][Package information](https://packages.gentoo.org/packages/app-i18n/ibus-libpinyin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/SoftwareTitleOnTheWikipedia "wikipedia:SoftwareTitleOnTheWikipedia")

[[]][GitHub](https://github.com/Project/SoftwarePackage)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/ibus-libpinyin)

[[[app-i18n/ibus-libpinyin]](https://packages.gentoo.org/packages/app-i18n/ibus-libpinyin)[]] is a Chinese input engine on [IBus](https://wiki.gentoo.org/wiki/IBus "IBus"). It is similar to, and a viable alternative for [Fcitx](https://wiki.gentoo.org/wiki/Fcitx "Fcitx") and [[[app-i18n/fcitx-libpinyin]](https://packages.gentoo.org/packages/app-i18n/fcitx-libpinyin)[]]. It is a modern replacement for the original (outdated) [[[app-i18n/ibus-pinyin]](https://packages.gentoo.org/packages/app-i18n/ibus-pinyin)[]].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)

## [Installation]

### [USE flags]

### [USE flags for] [app-i18n/ibus-libpinyin](https://packages.gentoo.org/packages/app-i18n/ibus-libpinyin) [[]] [Intelligent Pinyin and Bopomofo input methods based on LibPinyin for IBus]

  --------------------------------------------------------- ------------------------------------------
  [`boost`](https://packages.gentoo.org/useflags/boost)     Compile against dev-libs/boost libraries
  [`lua`](https://packages.gentoo.org/useflags/lua)         Enable Lua scripting support
  [`opencc`](https://packages.gentoo.org/useflags/opencc)   Enable support for app-i18n/opencc
  --------------------------------------------------------- ------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-19 16:08] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-i18n/ibus-libpinyin`

If a chinese compatible font is not already installed:

`root `[`#`]`emerge --ask media-fonts/arphicfonts`

### [Additional software]

This will work alongside other [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") input types (e.g. for Japanese input [[[app-i18n/ibus-anthy]](https://packages.gentoo.org/packages/app-i18n/ibus-anthy)[]]).

## [Configuration]

Open up the ibus setup dialogue:

`user `[`$`]`ibus-setup`

Check the \'Next Input Method key\' and change if desired. Then switch to \'Input Method\' tab and add \'Chinese -\> Intelligent Pinyin\'. This adds \'Chinese - Intelligent Pinyin\' to the list of input methods that ibus will cycle through when pressing the \'Input Method Key\'. Select \'Chinese - Intelligent Pinyin\' on the list and click \'Preferences\' to set options as desired.

For [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") (and the Chinese input) to run automatically on next login, configure as per configuration section for [IBus](https://wiki.gentoo.org/wiki/IBus "IBus").

## [Usage]

Press the ibus \'special key\' (as configured above - by default it is super+Space) and select \'Intelligent Pinyin\'. Then type in pinyin to get the Chinese character (type \'nihao\' and if 你好 appears as 1. press space to accept).

### [Invocation]

To manually start ([IBus](https://wiki.gentoo.org/wiki/IBus "IBus")) for a user, for example:

`user `[`$`]`ibus-daemon -d -x`

See [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") wiki for more info.

## [Troubleshooting]

In xterm shows weird glyphs instead of Chinese characters, but it works OK in other software (e.g. browser), launch xterm with settings that can cope with double spaced characters, e.g.:

`user `[`$`]`xterm -rv -en UTF-8 -fs 10 -fa 'AR PL UMing CN:style=Regular,Regular'`