This page contains [[changes](https://wiki.gentoo.org/index.php?title=How_to_read_and_write_in_Japanese&oldid=1314948&diff=1411734)] which are not marked for translation.

Other languages:

-   [English]
-   [español de América Latina](https://wiki.gentoo.org/wiki/How_to_read_and_write_in_Japanese/es-419 "Como leer y escribir en Japonés (62% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/How_to_read_and_write_in_Japanese/hu "Hogyan kell írni és olvasni japánul? (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/How_to_read_and_write_in_Japanese/zh-cn "如何读写日语 (14% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/How_to_read_and_write_in_Japanese/ja "日本語を使った読み書きの方法 (92% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/How_to_read_and_write_in_Japanese/ko "How to read and write in Japanese/ko (62% translated)")

This guide aims at explaining how to read and write in Japanese on a non-Japanese system. Please feel free to amend it based on personal knowledge or experience.

## Contents

-   [[1] [Requirements]](#Requirements)
    -   [[1.1] [Japanese fonts]](#Japanese_fonts)
    -   [[1.2] [Japanese Menus and Environment]](#Japanese_Menus_and_Environment)
    -   [[1.3] [Input method]](#Input_method)
    -   [[1.4] [IME]](#IME)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Japanese fonts]](#Japanese_fonts_2)
    -   [[2.2] [Input tools]](#Input_tools)
        -   [[2.2.1] [anthy]](#anthy)
        -   [[2.2.2] [mozc]](#mozc)
        -   [[2.2.3] [Configuring]](#Configuring)
        -   [[2.2.4] [Common USE Flags]](#Common_USE_Flags)
    -   [[2.3] [Latex]](#Latex)
        -   [[2.3.1] [CJK and xetex support]](#CJK_and_xetex_support)
        -   [[2.3.2] [Editor configuration]](#Editor_configuration)
-   [[3] [See also]](#See_also)

## [Requirements]

In order to support Japanese language and characters, a number of required tools, libraries and capabilities need to be installed on the system.

### [Japanese fonts]

Most non-Japanese systems have no Japanese fonts installed. Whenever a user tries to enter Japanese characters from the keyboard, they will only see small rectangle boxes in place of the characters on the screen.

### [Japanese Menus and Environment]

For those interested (perhaps for immersion based learning) in having a Japanese language based environment, in order to change menus and other materials into the Japanese language, change the user\'s profile into LANG=ja_JP.UTF-8 (in the user\'s locale as well as .bash_profile^[\[1\]](#cite_note-1)^)

### [Input method]

To read and write in Japanese, the first thing that is needed is a way to enter Japanese characters with the keyboard. This is done via a piece of software usually called an *input method*. At the moment, for the Japanese language, there are 2 such common methods: *anthy* and *mozc*.

With such a software component typing \"ta\" on the keyboard will input the kana **た** into the word processor. Some simple manipulation that is relevant to the way the input method works, will permit to easily switch from the hiragana **た** to the katakana **タ**.

In a similar way typing \"nihon\" will input **にほん** and an other simple manipulation will permit to turn this to the kanji version of this word, **日本**.

** Note**\
It is not the purpose of this guide to describe in detail how the \"anthy\" or \"mozc\" input methods work. Please refer to the documentation of these software components.

### [IME]

On top of this users also need a way to switch from the input method normally used for the primary language to the one needed for the Japanese language. This functionality is provided by another piece of software called an IME (Input Method Editor) such as [[[app-i18n/ibus]](https://packages.gentoo.org/packages/app-i18n/ibus)[]], [[[app-i18n/scim]](https://packages.gentoo.org/packages/app-i18n/scim)[]] or [[[app-i18n/fcitx]](https://packages.gentoo.org/packages/app-i18n/fcitx)[]].

Once installed, this allows users to switch from one language\'s input method to the Japanese input method using a key combination or using the mouse to select a relevant icon in the icon tray.

## [Installation]

### [Japanese fonts]

As a minimum, install the [[[media-fonts/kochi-substitute]](https://packages.gentoo.org/packages/media-fonts/kochi-substitute)[]] package.

`root `[`#`]`emerge --ask kochi-substitute`

Additionally, the following packages are also available:

-   [[[media-fonts/ja-ipafonts]](https://packages.gentoo.org/packages/media-fonts/ja-ipafonts)[]]
-   [[[media-fonts/vlgothic]](https://packages.gentoo.org/packages/media-fonts/vlgothic)[]]
-   [[[media-fonts/mplus-outline-fonts]](https://packages.gentoo.org/packages/media-fonts/mplus-outline-fonts)[]]
-   [[[media-fonts/monafont]](https://packages.gentoo.org/packages/media-fonts/monafont)[]]
-   [[[media-fonts/noto-cjk]](https://packages.gentoo.org/packages/media-fonts/noto-cjk)[]]
-   [[[media-fonts/ipamonafont]](https://packages.gentoo.org/packages/media-fonts/ipamonafont)[]]
-   [[[media-fonts/sazanami]](https://packages.gentoo.org/packages/media-fonts/sazanami)[]]

** Note**\
Many Japanese fonts display a yen symbol (¥) instead of a backslash (\\). To see backslashes instead, the [[[media-fonts/noto-cjk]](https://packages.gentoo.org/packages/media-fonts/noto-cjk)[]] package can be used.

** Note**\
When multiple fonts are installed, [fc-config] will pick a single font for Monospace, Sans and Serif. Verify which font is used with [fc-match monospace], [fc-match sans] and [fc-match serif] respectively.

### [Input tools]

It is recommended to use [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") instead of [SCIM](https://en.wikipedia.org/wiki/Smart_Common_Input_Method "wikipedia:Smart Common Input Method").

** Warning**\
[Compose key](https://wiki.gentoo.org/wiki/Compose_key "Compose key") will stop working when [ibus engine] is not `xkb:*`.

#### [anthy]

[[[app-i18n/ibus-anthy]](https://packages.gentoo.org/packages/app-i18n/ibus-anthy)[]]

`root `[`#`]`emerge --ask ibus-anthy`

#### [mozc]

[[[app-i18n/mozc\[ibus\]]](https://packages.gentoo.org/packages/app-i18n/mozc)[]]

`root `[`#`]`USE=ibus emerge --ask app-i18n/mozc`

** Note**\
*mozc* has a better reputation than *anthy* though anthy has been proved to be working fine for years now. Among pros for *mozc*, there is the fact that it shows the candidates instantly during typing and has a better learning system in order to present the user the best candidates depending on the user\'s habit and context. It also provides the *ATOK* mechanism to quickly change an hiragana input to katakana (e.g. F7 as default before hitting space) or to other modes.

** Note**\
When trying to use *mozc* some problems might occur. After selecting *mozc* as an input method in the *ibus-preferences* graphical utility, the *mozc* icon in the keyboard icon tray might not be visible. Open the [gnome settings] \--\> [Countries & Languages], remove all Japanese input methods (in this case \"anthy\") and add \"Japanese(Mozc)\".

#### [Configuring]

See [IBus](https://wiki.gentoo.org/wiki/IBus#Configuration "IBus") article on running IBus on login.

`user `[`$`]`ibus-setup`

In the dialog box that appears, click on the \"Input method\" tab and add the \"japanese-anthy\" or \"Japanese - Mozc\" method. Then return to the \"General\" tab and define a key combination as a keyboard shortcut for switching the input method.

The following useful keybindings could be set up for the \"Japanese - Mozc\" method:

[Preferences → General → Keymap → Keymap style → Customize...]

  ---------------- -------------- ----------------------------
  Mode             Key            Command
  Direct input     `` Ctrl ` ``   Set input mode to Hiragana
  Precomposition   `` Ctrl ` ``   Deactivate IME
  ---------------- -------------- ----------------------------

** Warning**\
The user will most likely want to convert the typing to hiragana. In anthy, change the input mode from *Latin* to *Hiragana*.

#### [Common USE Flags]

The following use flags are commonly employed^[\[2\]](#cite_note-2)^:\
**cjk** - Support for Hanzi-inspired characters (containing two bytes, hence the cause of accented a\'s *cum* sans cjk environment)\
**nls** - \'native language support\' - enables other languages in interface,\
**immqt-bc** - For Qt to manage other language inputs\
**immqt** - conflicts with immqt-bc as of Qt3.\
**unicode** - Standard except for cursive hebrew\

### [Latex]

Here are some additional requirements to write Latex files in Japanese.

#### [CJK and xetex support]

In order to write Japanese chunks in Latex files, add support for CJK languages and for [xetex](https://en.wikipedia.org/wiki/XeTeX "wikipedia:XeTeX") in Texlive.

This can be accomplished by adding or modifying the following lines in [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/latex`Enabling cjk and xetex support**

    app-text/texlive cjk xetex
    app-text/texlive-core cjk xetex

Then reinstall the packages:

`root `[`#`]`emerge --ask --newuse app-text/texlive app-text/texlive-core`

Here is a working short LaTeX sample:

[FILE] **`japanese.tex`**

    \documentclass
    \usepackage
    \usepackage

    \begin

    \begin
    \section
    \textcolor
    \\
    私は日本語で書けます。
    \\
    But I can also write with latin characters
    \end

    \end

** Note**\
In the `\begin` command in the example above, the third argument defines the font. Here `` is used for Mincho, but other supported fonts are Gothic (``) and Maru Gothic (``).

#### [Editor configuration]

To compile and visualize the output of the sample above Texmaker or Texstudio editor needs to be configured properly.

Open Texmaker, and go to [Options] -\> [Configure Texmaker]. Under the [Commands] tab change the following:

-   At the LaTeX line, change \"latex\" with \"platex\".
-   At the Dvipdfm line, change \"divipdfm\" with \"dvipdfmx\".

Through the [Fast compile] tab, choose \"Latex + Dvipdfm + View PDF\".

Finally go to the [Editor] tab, choose UTF8 encoding and deselect [On the fly] on the dictionary line.

## [See also]

-   [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") --- an open source input framework for Linux and Unix.
-   [TeX Live](https://wiki.gentoo.org/wiki/TeX_Live "TeX Live") --- a complete [TeX](https://en.wikipedia.org/wiki/TeX "wikipedia:TeX") distribution with several programs to create professional documents.

1.  [[[↑](#cite_ref-1)] [[https://srobb.net/jpninpt.html](https://srobb.net/jpninpt.html)]]
2.  [[[↑](#cite_ref-2)] [[https://forums.gentoo.org/viewtopic-p-1852138.html](https://forums.gentoo.org/viewtopic-p-1852138.html)]]