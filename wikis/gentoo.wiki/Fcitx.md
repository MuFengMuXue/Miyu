Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Fcitx/de "Fcitx/de (2% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Fcitx/hu "Fcitx (42% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Fcitx/zh-cn "Fcitx (42% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Fcitx/ja "Fcitx (75% translated)")

**Resources**

[[]][Home](http://fcitx-im.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Fcitx "wikipedia:Fcitx")

[[]][GitHub](https://github.com/fcitx/fcitx/)

**Fcitx** (**F**lexible **C**ontext-aware **I**nput **T**ool with e**X**tension support) \[ˈfaɪtɪks\] is an input method framework with support for many languages and scripts.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Using Fcitx]](#Using_Fcitx)
-   [[3] [Configuration]](#Configuration)
-   [[4] [Specific language support]](#Specific_language_support)
    -   [[4.1] [Chinese]](#Chinese)
        -   [[4.1.1] [Bopomofo]](#Bopomofo)
        -   [[4.1.2] [Cangjie & Boshiamy]](#Cangjie_.26_Boshiamy)
    -   [[4.2] [Japanese]](#Japanese)
    -   [[4.3] [Korean]](#Korean)
    -   [[4.4] [Vietnamese]](#Vietnamese)
-   [[5] [TroubleShooting]](#TroubleShooting)
    -   [[5.1] [Advanced features in some schemas of fcitx-rime doesn\'t work]](#Advanced_features_in_some_schemas_of_fcitx-rime_doesn.27t_work)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-i18n/fcitx](https://packages.gentoo.org/packages/app-i18n/fcitx) [[]] [Fcitx 5 is a generic input method framework]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                     Add support for X11
  [`+autostart`](https://packages.gentoo.org/useflags/+autostart)     Enable XDG-compatible autostart of Fcitx
  [`+emoji`](https://packages.gentoo.org/useflags/+emoji)             Enable emoji loading for CLDR
  [`+enchant`](https://packages.gentoo.org/useflags/+enchant)         Enable Enchant backend (using app-text/enchant) for spelling hinting
  [`+keyboard`](https://packages.gentoo.org/useflags/+keyboard)       Enable key event translation with XKB and build keyboard engine
  [`+server`](https://packages.gentoo.org/useflags/+server)           Build a fcitx as server, disable this option if you want to use fcitx as an embedded library
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`presage`](https://packages.gentoo.org/useflags/presage)           Enable presage for word predication (not stable)
  [`system-yoga`](https://packages.gentoo.org/useflags/system-yoga)   Use the system-wide dev-libs/yogainstead of bundled.
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)           Enable dev-libs/wayland backend
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-17 16:56] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
It is strongly recommended to add the `gtk2`, `gtk3` or `gtk4` [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") when applications are installed that make use of these toolkits.

### [Emerge]

`root `[`#`]`emerge --ask app-i18n/fcitx`

## [Using Fcitx]

To use Fcitx under X, the appropriate input method environment variables must be set in the startup files. In addition to `XMODIFIERS="@im=fcitx"`, `GTK_IM_MODULE` and `QT_IM_MODULE` must be set for [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") and [Qt](https://wiki.gentoo.org/wiki/Qt "Qt") applications, respectively.

To enable native input method support for [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") applications, install [[[app-i18n/fcitx-gtk]](https://packages.gentoo.org/packages/app-i18n/fcitx-gtk)[]] and set `GTK_IM_MODULE=fcitx`. To enable native input method support for [Qt](https://wiki.gentoo.org/wiki/Qt "Qt") applications, install [[[app-i18n/fcitx-qt]](https://packages.gentoo.org/packages/app-i18n/fcitx-qt)[]] and set `QT_IM_MODULE=fcitx`. In most cases, both modules should be installed and both variables set.

When using login managers such as [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM") to start the X server, add the following to the [\~/.xprofile] file.

[FILE] **`~/.xprofile`**

    export XMODIFIERS="@im=fcitx"
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx

When starting X manually with the [startx] command or [SLiM](https://wiki.gentoo.org/wiki/SLiM "SLiM"), add the following to the [\~/.xinitrc] file.

[FILE] **`~/.xinitrc`**

    export XMODIFIERS="@im=fcitx"
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    pgrep -x fcitx5 > /dev/null || fcitx5 -d &

For KDE users, if these environment variables are not getting loaded either from [\~/.xprofile] or [\~/.xinitrc], try adding them to a Plasma startup script, such as [\~/.config/plasma-workspace/env/fcitx.sh].

Fcitx relies on the Dbus service to run. If it is a systemd init system, no additional configuration is generally required. Otherwise, you need to manually configure the operation of dbus. For details, refer to the [Dbus](https://wiki.gentoo.org/wiki/Dbus "Dbus") entry.

** Warning**\
When desiring to use Fcitx in X, the system [locale](https://wiki.gentoo.org/wiki/Localization "Localization") **cannot** be *C* or *POSIX*.

** Tip**\
To use fctix in Wayland, check the official documentation: [Using_Fcitx_5_on_Wayland](https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland).

## [Configuration]

Edit Fcitx\'s configuration file at [\~/.config/fcitx5/config].

Configure Fcitx using graphical tools, install [[[app-i18n/fcitx-configtool]](https://packages.gentoo.org/packages/app-i18n/fcitx-configtool)[]]. For KDE settings integration, enable [[[kcm]](https://packages.gentoo.org/useflags/kcm)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag.

## [Specific language support]

### [Chinese]

Fcitx itself has built-in pinyin support. Install [[[app-i18n/fcitx-chinese-addons]](https://packages.gentoo.org/packages/app-i18n/fcitx-chinese-addons)[]] to provide multiple table-based input methods such as WuBi and Ziranma.

Install [[[app-i18n/fcitx-chinese-addons]](https://packages.gentoo.org/packages/app-i18n/fcitx-chinese-addons)[]] with flag [[[cloudpinyin]](https://packages.gentoo.org/useflags/cloudpinyin)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] enabled to have better results in the candidate words list.

The built-in pinyin use a simple algorithm, and there are other pinyin input methods using other algorithms. Install [[[app-i18n/fcitx-rime]](https://packages.gentoo.org/packages/app-i18n/fcitx-rime)[]] to use them.

#### [Bopomofo]

Install [[[app-i18n/fcitx-chewing]](https://packages.gentoo.org/packages/app-i18n/fcitx-chewing)[]]:

`root `[`#`]`emerge --ask app-i18n/fcitx-chewing`

#### [][Cangjie & Boshiamy]

Install [[[app-i18n/fcitx-table-extra]](https://packages.gentoo.org/packages/app-i18n/fcitx-table-extra)[]]:

`root `[`#`]`emerge --ask app-i18n/fcitx-table-extra`

### [Japanese]

** Note**\
See also: [How to read and write in Japanese](https://wiki.gentoo.org/wiki/How_to_read_and_write_in_Japanese "How to read and write in Japanese") --- how to read and write in Japanese on a non-Japanese system.

Install [[[app-i18n/fcitx-anthy]](https://packages.gentoo.org/packages/app-i18n/fcitx-anthy)[]]:

`root `[`#`]`emerge --ask app-i18n/fcitx-anthy`

### [Korean]

Install [[[app-i18n/fcitx-hangul]](https://packages.gentoo.org/packages/app-i18n/fcitx-hangul)[]]:

`root `[`#`]`emerge --ask app-i18n/fcitx-hangul`

### [Vietnamese]

Install [[[app-i18n/fcitx-unikey]](https://packages.gentoo.org/packages/app-i18n/fcitx-unikey)[]]:

`root `[`#`]`emerge --ask app-i18n/fcitx-unikey`

## [TroubleShooting]

### [][Advanced features in some schemas of [fcitx-rime] doesn\'t work]

Some third-party [fcitx-rime] schemas use [Lua](https://wiki.gentoo.org/wiki/Lua "Lua") to accomplish some advanced features. This could be identified by reading the corresponding schema definition files and the presence of Lua scripts in [rime] configuration path.

The configuration path of [rime] is located at `~/.local/share/fcitx5/rime` by default.

For these features to function properly, [[[app-i18n/fcitx-lua]](https://packages.gentoo.org/packages/app-i18n/fcitx-lua)[]] and [[[app-i18n/librime-lua]](https://packages.gentoo.org/packages/app-i18n/librime-lua)[]] have to be installed using matching `LUA_SINGLE_TARGET` USE flags.

After the installation of these packages, restart [fcitx] and redeploy [rime].

** Tip**\
[rime] will automatically redeploy after touching its configuration files; alternatively, there is a \"redeploy\" option in the right-click menu of fcitx icon.

## [See also]

-   [Dbus](https://wiki.gentoo.org/wiki/Dbus "Dbus") --- an interprocess communication (IPC) system for software applications.
-   [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") --- an open source input framework for Linux and Unix.

## [External resources]

-   [https://fcitx-im.org/wiki/Setup_Fcitx_5](https://fcitx-im.org/wiki/Setup_Fcitx_5)