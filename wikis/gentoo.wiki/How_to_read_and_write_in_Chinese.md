\
This guide aims at explaining how to read and write in Chinese on a non-Chinese system. Please feel free to amend it based on personal knowledge or experience.

## Contents

-   [[1] [Requirements]](#Requirements)
    -   [[1.1] [Chinese fonts]](#Chinese_fonts)
    -   [[1.2] [Input method]](#Input_method)
    -   [[1.3] [IME]](#IME)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Chinese fonts]](#Chinese_fonts_2)
    -   [[2.2] [Input tools]](#Input_tools)
        -   [[2.2.1] [fcitx-rime]](#fcitx-rime)
        -   [[2.2.2] [Launching the fcitx daemon at login time]](#Launching_the_fcitx_daemon_at_login_time)
        -   [[2.2.3] [Configuring]](#Configuring)
    -   [[2.3] [Latex]](#Latex)
        -   [[2.3.1] [CJK and xetex support]](#CJK_and_xetex_support)
        -   [[2.3.2] [Editor configuration]](#Editor_configuration)
-   [[3] [See also]](#See_also)

## [Requirements]

In order to support Chinese language and characters, a number of required tools, libraries and capabilities need to be installed on the system.

### [Chinese fonts]

Most non-Chinese systems have no Chinese fonts installed. Whenever a user tries to enter Chinese characters from the keyboard, they will only see small rectangle boxes in place of the characters on the screen.

### [Input method]

To read and write in Chinese, the first thing that is needed is a way to enter Chinese characters with the keyboard. This is done via a piece of software usually called an *input method*. At the moment, for the Chinese language, there are 3 kinds of common methods; phonetic, shape-based and a hybrid from both, see [Chinese input methods for computers (Wikipedia)](https://en.wikipedia.org/wiki/Chinese_input_methods_for_computers "wikipedia:Chinese input methods for computers"). The most common ones are *wubi* and *pinyin*.

\

** Note**\
It is not the purpose of this guide to describe in detail how the \"pinyin\" or \"wubi\" input methods work. Please refer to the documentation of these software components or [\"other sources\"](https://en.wikipedia.org/wiki/Chinese_input_methods_for_computers "wikipedia:Chinese input methods for computers")

### [IME]

On top of this users also need a way to switch from the input method normally used for the primary language to the one needed for the Chinese language. This functionality is provided by another piece of software called an IME (Input Method Editor) such as [[[app-i18n/ibus]](https://packages.gentoo.org/packages/app-i18n/ibus)[]], [[[app-i18n/scim]](https://packages.gentoo.org/packages/app-i18n/scim)[]] or [[[app-i18n/fcitx]](https://packages.gentoo.org/packages/app-i18n/fcitx)[]]. fcitx sunpinyin working, table not yet ibus not confirmed yet scim not confirmed yet

Once installed, this allows users to switch from one language\'s input method to the Chinese input method using a key combination or using the mouse to select a relevant icon in the icon tray.

## [Installation]

### [Chinese fonts]

Install the [noto-cjk](https://packages.gentoo.org/packages/media-fonts/noto-cjk) package.

`root `[`#`]`emerge --ask media-fonts/noto-cjk`

Then, list the available font configs with

`root `[`#`]`eselect fontconfig list `

Enable the noto-cjk font configuration with

`root `[`#`]`eselect fontconfig enable 70-noto-cjk.conf `

\
Additionally, the following packages are also available:

-   [[[media-fonts/font-isas-misc]](https://packages.gentoo.org/packages/media-fonts/font-isas-misc)[]]
-   [[[media-fonts/arphicfonts]](https://packages.gentoo.org/packages/media-fonts/arphicfonts)[]]
-   [[[media-fonts/opendesktop-fonts]](https://packages.gentoo.org/packages/media-fonts/opendesktop-fonts)[]]
-   [[[media-fonts/wqy-zenhei]](https://packages.gentoo.org/packages/media-fonts/wqy-zenhei)[]]
-   [[[media-fonts/zh-kcfonts]](https://packages.gentoo.org/packages/media-fonts/zh-kcfonts)[]]

### [Input tools]

It is recommended to use *fcitx* instead of *scim* or *ibus*.

To install fcitx, install [[[app-i18n/fcitx]](https://packages.gentoo.org/packages/app-i18n/fcitx)[]]:

`root `[`#`]`emerge --ask fcitx`

#### [fcitx-rime]

fcitx-rime is provided through the [[[app-i18n/fcitx-rime]](https://packages.gentoo.org/packages/app-i18n/fcitx-rime)[]]package. Note: the fcitx-rime package is mainly a traditional Chinese input engine.

** Note**\
*pinyin* has no steep learning curve.

\

#### [Launching the fcitx daemon at login time]

Add these lines to the [\~/.xprofile] file and log out/log in again.

[FILE] **`~/.xprofile`**

    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS=@im=fcitx
    export SDL_IM_MODULE=fcitx
    export GLFW_IM_MODULE=fcitx
    export INPUT_MODULE=fcitx

This will allow the fcitx daemon to start at login time.

#### [Configuring]

To configure the fcitx Input Method Editor, use the following [[[app-i18n/fcitx-configtool]](https://packages.gentoo.org/packages/app-i18n/fcitx-configtool)[]] package for graphical configuration.

### [Latex]

Here are some additional requirements to write Latex files in Chinese.

#### [CJK and xetex support]

In order to write Chinese chunks in Latex files, add support for CJK languages and for [xetex](https://en.wikipedia.org/wiki/XeTeX "wikipedia:XeTeX") in Texlive.

This can be accomplished by adding or modifying the following lines in [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/latex`Enabling cjk and xetex support**

    app-text/texlive cjk xetex
    app-text/texlive-core cjk xetex

Then reinstall the packages:

`root `[`#`]`emerge --ask --newuse app-text/texlive app-text/texlive-core`

Here is a working short LaTeX sample:

[FILE] **`chinese.tex`**

    \documentclass
    \usepackage
    \usepackage

    \begin

    \begin
    \section
    \textcolor
    \\
    你好世界。
    \\
    But I can also write with latin characters
    \end

    \end

** Note**\
In the `\begin` command in the example above, the third argument defines the font.

#### [Editor configuration]

To compile and visualize the output of the sample above Texmaker or Texstudio editor needs to be configured properly.

Open Texmaker, and go to [Options] -\> [Configure Texmaker]. Under the [Commands] tab change the following:

-   At the LaTeX line, change \"latex\" with \"platex\".
-   At the Dvipdfm line, change \"divipdfm\" with \"dvipdfmx\".

Through the [Fast compile] tab, choose \"Latex + Dvipdfm + View PDF\".

Finally go to the [Editor] tab, choose UTF8 encoding and deselect [On the fly] on the dictionary line.

## [See also]

-   [Fcitx](https://wiki.gentoo.org/wiki/Fcitx "Fcitx") --- an input method framework with support for many languages and scripts.
-   [TeX Live](https://wiki.gentoo.org/wiki/TeX_Live "TeX Live") --- a complete [TeX](https://en.wikipedia.org/wiki/TeX "wikipedia:TeX") distribution with several programs to create professional documents.
-   [How to read and write in Japanese](https://wiki.gentoo.org/wiki/How_to_read_and_write_in_Japanese "How to read and write in Japanese") --- how to read and write in Japanese on a non-Japanese system.
-   [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") --- an open source input framework for Linux and Unix.