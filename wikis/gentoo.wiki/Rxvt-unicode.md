This page contains [[changes](https://wiki.gentoo.org/index.php?title=Rxvt-unicode&diff=1338919)] which are not marked for translation.

**Resources**

[[]][Home](http://software.schmorp.de/pkg/rxvt-unicode.html)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/rxvt-unicode)

[[]][GitHub mirror](https://github.com/exg/rxvt-unicode)

[[]][urxvt(1)](https://linux.die.net/man/1/urxvt)

[[]][Official documentation](http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod)

[[]][[#rxvt-unicode](ircs://irc.libera.chat/#rxvt-unicode)] ([[webchat](https://web.libera.chat/#rxvt-unicode)])

** Important**\
The rxvt-unicode FAQ [states](http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod#I_use_Gentoo_and_I_have_a_problem): \"Problems appearing on Gentoo systems will usually simply be ignored unless they can be reproduced on non-Gentoo systems.\"

**rxvt-unicode**, also known simply as [urxvt], is a fast and lightweight [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") with [Xft](https://en.wikipedia.org/wiki/Xft "wikipedia:Xft") and [Unicode](https://en.wikipedia.org/wiki/Unicode "wikipedia:Unicode") support.

Many Gentoo users enjoy using [urxvt] inside the [i3](https://wiki.gentoo.org/wiki/I3 "I3") and [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") window managers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Daemon]](#Daemon)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Font]](#Font)
    -   [[3.2] [Scrollbar]](#Scrollbar)
    -   [[3.3] [Scrollback]](#Scrollback)
    -   [[3.4] [Printing]](#Printing)
    -   [[3.5] [Copy/Paste]](#Copy.2FPaste)
    -   [[3.6] [URL handling/Perl extensions]](#URL_handling.2FPerl_extensions)
    -   [[3.7] [Icons]](#Icons)
        -   [[3.7.1] [Menu icon]](#Menu_icon)
        -   [[3.7.2] [Application icon]](#Application_icon)
    -   [[3.8] [Color theme]](#Color_theme)
    -   [[3.9] [Using urxvt with Powerline fonts]](#Using_urxvt_with_Powerline_fonts)
    -   [[3.10] [Changing font size on the fly]](#Changing_font_size_on_the_fly)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Changes in \~/.Xresources are not applied]](#Changes_in_.7E.2F.Xresources_are_not_applied)
    -   [[4.2] [Reporting bugs]](#Reporting_bugs)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [[] Installation]

### [[] USE flags]

### [USE flags for] [x11-terms/rxvt-unicode](https://packages.gentoo.org/packages/x11-terms/rxvt-unicode) [[]] [rxvt clone with xft and unicode support]

  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+font-styles`](https://packages.gentoo.org/useflags/+font-styles)                   Enable support for bold and italic fonts
  [`+mousewheel`](https://packages.gentoo.org/useflags/+mousewheel)                     Enable scrolling via mouse wheel or buttons 4 and 5
  [`24-bit-color`](https://packages.gentoo.org/useflags/24-bit-color)                   Enable 24-bit color support. Note that this feature is unofficial, may cause visual glitches due to the fact there is no termcap/terminfo definition for rxvt-unicode-24bit yet so it is necessary to use the one for 256 colours, visibly increases memory usage, and might slow urxvt down dramatically when more than six fonts are in use in a terminal instance.
  [`256-color`](https://packages.gentoo.org/useflags/256-color)                         Enable 256 color support
  [`blink`](https://packages.gentoo.org/useflags/blink)                                 Enable blinking text
  [`fading-colors`](https://packages.gentoo.org/useflags/fading-colors)                 Enable colors fading when off focus
  [`gdk-pixbuf`](https://packages.gentoo.org/useflags/gdk-pixbuf)                       Enable transparency support using x11-libs/gdk-pixbuf
  [`iso14755`](https://packages.gentoo.org/useflags/iso14755)                           Enable ISO-14755 support
  [`perl`](https://packages.gentoo.org/useflags/perl)                                   Enable perl script support. You can still disable this at runtime with -pe \"\"
  [`startup-notification`](https://packages.gentoo.org/useflags/startup-notification)   Enable application startup event feedback mechanism
  [`unicode3`](https://packages.gentoo.org/useflags/unicode3)                           Use 21 instead of 16 bits to represent unicode characters
  [`wide-glyphs`](https://packages.gentoo.org/useflags/wide-glyphs)                     Enable support for wide glyphs, required for certain symbol/icon fonts to display correctly. Note that this feature is \*unofficial\* and has been observed to cause stability issues for some users.
  [`xft`](https://packages.gentoo.org/useflags/xft)                                     Build with support for XFT font renderer (x11-libs/libXft)
  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-20 01:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

Install [[[x11-terms/rxvt-unicode]](https://packages.gentoo.org/packages/x11-terms/rxvt-unicode)[]]:

`root `[`#`]`emerge --ask rxvt-unicode`

## [[] Daemon]

It is possible to operate [urxvt] as a daemon, which will lead to lower resource usage and quicker startup for new terminals. It is a good idea to start the daemon at the beginning of the X session.

The following command will start the daemon and fork it into the background.

`user `[`$`]`urxvtd --quiet --opendisplay --fork`

After this, new clients can be opened on the single daemon process, rather than spawning new processes for each terminal. To do this, simply run [urxvtc] in place of the usual [urxvt] command. Keep in mind that if for any reason the daemon is terminated, any subsequent [urxvtc] calls as well all client instances will be closed.

Environment variable can be used to specify different location for the daemon [\~/.urxvt/urxvtd-hostname] listening socket.

[CODE] **The socket location as environment variable**

    export RXVT_SOCKET='/tmp/urxvt-socket'

## [[] Configuration]

Configuration for [urxvt] is done mainly through the [X resources](https://wiki.gentoo.org/wiki/X_resources "X resources") system, though command line equivalents are also available in most cases. A full list of these options can be found in the [urxvt] [manpage](https://linux.die.net/man/1/urxvt). To configure all [urxvt] options in a different file and including this file in .Xresources my be advisable. For example:

[FILE] **`~/.Xresources`**

    ...
    #include ".config/urxvt"
    ...

Some common configuration options are listed below.

** Note**\
It is recommended to become familiar with the [X resources](https://wiki.gentoo.org/wiki/X_resources "X resources") syntax before editing the configuration.

### [[] Font]

[urxvt]\'s [font](https://wiki.gentoo.org/wiki/Fonts "Fonts") can be configured using either [XLFD](https://en.wikipedia.org/wiki/X_logical_font_description "wikipedia:X logical font description") notation or, provided the package was compiled with the [[[xft]](https://packages.gentoo.org/useflags/xft)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), [Xft](https://en.wikipedia.org/wiki/Xft "wikipedia:Xft") fonts.

[FILE] **`~/.Xresources`**

    ! Using XLFD (created via e.g. xfontsel)
    URxvt*font:           -misc-fixed-medium-r-semicondensed-*-12-90-100-*-c-60-iso8859-1
    ! Using Xft
    URxvt*font:           xft:Inconsolata:size=8

Fonts can be modified while [urxvt] is running by assigning actions to keys:

[FILE] **`~/.Xresources`**

    ! Bind C-p to use unifont and show 'halfwidth left corner bracket', U+FF62,｢
    URxvt.keysym.C-p:   command:\033]710;xft:Unifont:pixelsize=20\007
    ! Bind C--, C-0(=) and C-+ to activate small, medium, and big font size resp.
    URxvt.keysym.C-minus:   command:\033]710;xft:Liberation Mono:pixelsize=12\007
    URxvt.keysym.C-0:   command:\033]710;xft:DejaVu Sans Mono:pixelsize=16\007
    URxvt.keysym.C-plus:    command:\033]710;xft:Liberation Mono:pixelsize=20\007

** Note**\
In some fonts, depending on the font size, [Unicode](https://en.wikipedia.org/wiki/Unicode "wikipedia:Unicode") may not work properly.

Rendering settings can be tweaked for Xft fonts as well. Note that this is not specific to [urxvt].

[FILE] **`~/.Xresources`**

    Xft.dpi:        96
    Xft.antialias:  true
    Xft.rgba:       rgb
    Xft.hinting:    true
    Xft.hintstyle:  hintslight
    Xft.autohint:   false
    Xft.lcdfilter:  lcddefault

### [[] Scrollbar]

The look of the scrollbar can be changed, or it can be removed entirely.

[FILE] **`~/.Xresources`**

    URxvt.scrollBar: false
    URxvt.scrollBar_right: false
    URxvt.scrollBar_floating: false
    URxvt.scrollstyle: rxvt

### [[] Scrollback]

The size of the scrollback buffer can be increased with:

[FILE] **`~/.Xresources`**

    URxvt*saveLines: 16384

### [[] Printing]

By default, [urxvt] will print out a screen dump, via [lpr], when [PrntScrn] is pressed. Using [Ctrl]+[PrintScrn] or [Shift]-[PrintScrn] will include the terminal\'s scroll back in the printout as well. This behavior can be changed, or disabled entirely, based on personal preference and need.

[FILE] **`~/.Xresources`**

    ! The string will be interpreted as if typed into the shell as-is.
    ! In this example, printing will be disabled altogether.
    URxvt.print-pipe: "cat > /dev/null"

### [][[] Copy/Paste]

By default, [urxvt] will copy selected text to the `PRIMARY` clipboard, and paste it when middle click is pressed.

To use the `CLIPBOARD` clipboard, use [Ctrl]+[Alt]+[C] to copy, and [Ctrl]+[Alt]+[V] to paste.

** Note**\
Right click can be used to adjust the size of the selection.

### [][[] URL handling/Perl extensions]

The default [urxvt] [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") extensions can be used for copy and paste actions as well for URL handling capabilities. In order to use Perl extensions in [urxvt], the package must have been compiled with [[[perl]](https://packages.gentoo.org/useflags/perl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]. The [[[x11-misc/urxvt-perls]](https://packages.gentoo.org/packages/x11-misc/urxvt-perls)[]] package provides the **keyboard-select** extension not included by default. The package sources code can be found in muennich\'s [GitHub repository](https://github.com/muennich/urxvt-perls) or an [ebuild](https://github.com/tokiclover/bar-overlay/tree/master/dev-perl/perl-URxvt) for example. It is possible to get other Perl [extensions](https://github.com/search?l=Perl&q=urxvt&type=Repositories&utf8=%E2%9C%93).

Here is an example of a [\~/.Xresources]. The following lines could also be added to [\~/.Xdefaults], though [\~/.Xresources] is preferred.

[FILE] **`~/.Xresources`**

    !-*- Perl extensions -*-
    URxvt.perl-ext-common: default,selection-to-clipboard,pasta,matcher,keyboard-select
    URxvt.keysym.M-u:     perl:url-select:select_next
    URxvt.url-launcher:   /usr/bin/firefox
    URxvt.underlineURLs:  True
    URxvt.matcher.button: 1
    URxvt.keysym.M-Escape:perl:keyboard-select:activate
    URxvt.keysym.Control-Shift-V:     perl:pasta:paste
    ! The following configuration will automatically update the CLIPBOARD when the PRIMARY selection changes
    ! This is deprecated since Control-Alt-C/V has been implemented since 9.20
    URxvt.clipboard.autocopy: true

The default selection-to-clipboard extension will put the selected text into the clipboard automatically. To add pasting functionality we have to create a simple extension:

[FILE] **`/usr/lib64/urxvt/perl/pasta`**

    #! /usr/bin/env perl -w
    # Author:   Aaron Caffrey
    # Website:  https://github.com/wifiextender/urxvt-pasta
    # License:  GPLv3

    # Usage: put the following lines in your .Xdefaults/.Xresources:
    # URxvt.perl-ext-common           : selection-to-clipboard,pasta
    # URxvt.keysym.Control-Shift-V    : perl:pasta:paste

    use strict;

    sub on_user_command
      ()
    }

** Note**\
Some urxvt-perls have been deprecated because of improved urxvt functionality [https://github.com/xyb3rt/urxvt-perls/blob/master/deprecated/README.md](https://github.com/xyb3rt/urxvt-perls/blob/master/deprecated/README.md)

### [[] Icons]

#### [[] Menu icon]

This adds menu entry and menu icon for [urxvt]. If [urxvt] doesn\'t have a [.desktop] file, create one.

[FILE] **`/usr/share/applications/urxvt.desktop`**

    [Desktop Entry]
    Name=Urxvt
    Comment=Terminal emulator
    TryExec=urxvt
    Exec=urxvt
    Icon=utilities-terminal
    Type=Application
    Categories=GTK;TerminalEmulator;System;
    # This assumes the 'startup-notification' USE flag being enabled
    StartupNotify=true

#### [[] Application icon]

For setting application icon [[[x11-terms/rxvt-unicode]](https://packages.gentoo.org/packages/x11-terms/rxvt-unicode)[]] has to be compiled with [[[pixbuf]](https://packages.gentoo.org/useflags/pixbuf)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")].

[FILE] **`~/.Xresources`**

    URxvt.iconFile:    /usr/share/icons/hicolor/scalable/apps/Terminal.svg

### [[] Color theme]

The main [urxvt]\'s color palette is defined by `background`, `foreground` and `color`**`n`** resources. It is also possible to set color of other elements (e.g. cursor or text underline). For more information consult the [urxvt] [manpage](https://linux.die.net/man/1/urxvt).

[FILE] **`~/.Xresources`**

    *background: #0f0f0f
    *foreground: #c8c8c8

    !black
    *color0:  #251f1f
    *color8:  #5e5e5e
    !red
    *color1:  #eb4509
    *color9:  #eb4509
    !green
    *color2:  #94e76b
    *color10: #95e76b
    !yellow
    *color3:  #ffac18
    *color11: #ffac18
    !blue
    *color4:  #46aede
    *color12: #46aede
    !magenta
    *color5:  #e32c57
    *color13: #e32c57
    !cyan
    *color6:  #d6dbac
    *color14: #d6dbac
    !white
    *color7:  #efefef
    *color15: #efefef

[FILE] **`~/.Xresources`Tango colors**

    ! black
    *color0:  #2E3436
    *color8:  #555753
    ! red
    *color1:  #a40000
    *color9:  #EF2929
    ! green
    *color2:  #4E9A06
    *color10: #8AE234
    ! yellow
    *color3:  #C4A000
    *color11: #FCE94F
    ! blue
    *color4:  #3465A4
    *color12: #729FCF
    ! purple
    *color5:  #75507B
    *color13: #AD7FA8
    ! orange (replaces cyan)
    *color6:  #ce5c00
    *color14: #fcaf3e
    ! white
    *color7:  #babdb9
    *color15: #EEEEEC

[FILE] **`~/.Xresources`Linux colors**

    ! Colors
    URxvt*background: #000000
    URxvt*foreground: #B2B2B2
    ! black
    URxvt*color0:  #000000
    URxvt*color8:  #686868
    ! red
    URxvt*color1:  #B21818
    URxvt*color9:  #FF5454
    ! green
    URxvt*color2:  #18B218
    URxvt*color10: #54FF54
    ! yellow
    URxvt*color3:  #B26818
    URxvt*color11: #FFFF54
    ! blue
    URxvt*color4:  #1818B2
    URxvt*color12: #5454FF
    ! purple
    URxvt*color5:  #B218B2
    URxvt*color13: #FF54FF
    ! cyan
    URxvt*color6:  #18B2B2
    URxvt*color14: #54FFFF
    ! white
    URxvt*color7:  #B2B2B2
    URxvt*color15: #FFFFFF

### [[] Using urxvt with Powerline fonts]

As of v9.30 the default [urxvt] configuration does not support icon-oriented fonts, such as [Powerline](https://github.com/powerline/powerline) or [Nerd Fonts](https://www.nerdfonts.com/). Therefore the icon symbols fail to display correctly unless the `unicode3` USE flag is set.

Rendering of a common Powerline symbol (solid triangle separator) can be tested as:

`user `[`$`]`echo -e '\xEE\x82\xB0'`

Using the standard fonts and enabling [[[media-fonts/powerline-symbols]](https://packages.gentoo.org/packages/media-fonts/powerline-symbols)[]] fallback via [Fontconfig](https://wiki.gentoo.org/wiki/Fontconfig "Fontconfig") does not seem to work for [urxvt]^[\[1\]](#cite_note-1)^. This forces installing one of the Powerline [patched fonts](https://powerline.readthedocs.io/en/latest/installation/linux.html#patched-font-installation) (bearing the ` for Powerline` suffix).

See also [rxvt-unicode and the Powerline symbols](http://lists.schmorp.de/pipermail/rxvt-unicode/2016q1/002204.html) thread on the [urxvt] mailing list.

### [[] Changing font size on the fly]

To be able to use font size changing within running terminal session, first verify [urxvt] has been build with [[[perl]](https://packages.gentoo.org/useflags/perl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")].

Install the [[[x11-misc/urxvt-font-size]](https://packages.gentoo.org/packages/x11-misc/urxvt-font-size)[]] package:

`root `[`#`]`emerge --ask x11-misc/urxvt-font-size`

Open the [\~/.Xresources] file for editing and replace the entry:

[FILE] **`~/.Xresources`**

    !-*- Perl extensions -*-
    URxvt.perl-ext-common: default,selection-to-clipboard,pasta,matcher,keyboard-select
    ...

With following entry, or just add the `font-size` to the end of the listed extensions:

[FILE] **`~/.Xresources`**

    !-*- Perl extensions -*-
    URxvt.perl-ext-common: default,selection-to-clipboard,pasta,matcher,keyboard-select,font-size
    ...

Configure a keyboard key combination to increase or decrease the font size, add following entries:

[FILE] **`~/.Xresources`**

    ...
    ! Ctrl + Up / Down arrow
    URxvt.keysym.C-Up:           font-size:increase
    URxvt.keysym.C-Down:         font-size:decrease
    ! Ctrl + plus / minus keys on keypad
    URxvt.keysym.C-KP_Add:       font-size:increase
    URxvt.keysym.C-KP_Subtract:  font-size:decrease
    URxvt.keysym.C-S-Up:         font-size:incglobal
    URxvt.keysym.C-S-Down:       font-size:decglobal
    URxvt.keysym.C-equal:        font-size:reset
    URxvt.keysym.C-KP_0:         font-size:reset
    URxvt.keysym.C-slash:        font-size:show
    ...

To increase the font size press [Ctrl]+[+], to decrease the font size press [Ctrl]+[-]. To reset to the default font size press [Ctrl]+[0].

## [[] Troubleshooting]

### [][[] Changes in \~/.Xresources are not applied]

1\. Check for syntax errors in [\~/.Xresources] based on [X resources](https://wiki.gentoo.org/wiki/X_resources "X resources") article.

2\. If you\'re using \~/.xinitrc add `[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources` to \~/.xinitrc and reboot.

3\. Invoking \`xrdb -merge -I\$HOME \~/.Xresources\`might also resolve the issue.

### [[] Reporting bugs]

** Note**\
This \'Reporting bugs\' section is satire.

This section describes the instructions for reporting and fixing [urxvt] bugs.

1.  Install Arch GNU/Linux.
    1.  Test on Arch to see if the bug persists.
        1.  If the bug does not persist, then contact the ebuild maintainer [Jeroen Roovers (jer)](https://wiki.gentoo.org/wiki/User:JeR "User:JeR") . The ebuild maintainer may be able to make a fix.
2.  Contact upstream developer. Be sure to note testing was performed on Gentoo Linux as Gentoo GNU/Linux or you will be ignored and possibly yelled at.
3.  When all else fails, contact the maintainer [Jeroen Roovers (jer)](https://wiki.gentoo.org/wiki/User:JeR "User:JeR") and fix it this way.

These instructions are based on official upstream [instructions from the developer](http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod#I_use_Gentoo_and_I_have_a_problem).

## [[] See also]

-   [X resources](https://wiki.gentoo.org/wiki/X_resources "X resources") --- configuration options for X applications
-   [Fonts](https://wiki.gentoo.org/wiki/Fonts "Fonts") --- home page for information about using fonts on Gentoo

## [[] External resources]

-   [Terminal Color Scheme Designer](https://terminal.sexy)

## [[] References]

1.  [[[↑](#cite_ref-1)] [[Request for feedback: Patched fonts may be unnecessary for many users #60](https://github.com/powerline/powerline/issues/60#issuecomment-12620932), GitHub. Retrieved on March 12, 2022 ]]