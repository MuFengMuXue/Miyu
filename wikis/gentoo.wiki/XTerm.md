[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=XTerm&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://invisible-island.net/xterm/)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/xterm)

[[]][Official documentation](https://invisible-island.net/xterm/xterm.faq.html)

**XTerm** is a graphical [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") for X11. XTerm is a fast and featureful emulator that predates X11, but is still actively developed.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)

## [Installation]

### [USE flags]

### [USE flags for] [x11-terms/xterm](https://packages.gentoo.org/packages/x11-terms/xterm) [[]] [Terminal Emulator for X Windows]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------
  [`+openpty`](https://packages.gentoo.org/useflags/+openpty)       Use openpty() in preference to posix_openpt()
  [`Xaw3d`](https://packages.gentoo.org/useflags/Xaw3d)             Add support for the 3d athena widget set
  [`sixel`](https://packages.gentoo.org/useflags/sixel)             Enable sixel graphics support
  [`toolbar`](https://packages.gentoo.org/useflags/toolbar)         Enable the xterm toolbar to be built
  [`truetype`](https://packages.gentoo.org/useflags/truetype)       Add support for FreeType and/or FreeType2 fonts
  [`unicode`](https://packages.gentoo.org/useflags/unicode)         Add support for Unicode
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)       Add support for querying multi-monitor screen geometry through the Xinerama API
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-02 23:20] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask x11-terms/xterm`

## [Usage]

### [Invocation]

XTerm will generally be launched from an on-screen menu, or keyboard shortcut, in a user\'s graphical environment.

XTerm may, if needed, be launched from a shell under X11.

`user `[`$`]`xterm -help `

    XTerm(367) usage:
        xterm [-options ...] [-e command args]

    where options include:
        -/+132                       turn on/off 80/132 column switching
        -C                           intercept console messages
        -Sccn                        slave mode on "ttycc", file descriptor "n"
        -T string                    title name for window
        -/+ah                        turn on/off always highlight
        -/+ai                        turn off/on active icon
        -/+aw                        turn on/off auto wraparound
        -b number                    internal border in pixels
        -baudrate rate               set line-speed (default 38400)
        -/+bc                        turn on/off text cursor blinking
        -bcf milliseconds            time text cursor is off when blinking
        -bcn milliseconds            time text cursor is on when blinking
        -bd color                    border color
        -/+bdc                       turn off/on display of bold as color
        -bg color                    background color
        -bw number                   border width in pixels
        -/+cb                        turn on/off cut-to-beginning-of-line inhibit
        -cc classrange               specify additional character classes
        -/+cjk_width                 turn on/off legacy CJK width convention
        -class string                class string (XTerm)
        -/+cm                        turn off/on ANSI color mode
        -/+cn                        turn on/off cut newline inhibit
        -cr color                    text cursor color
        -/+cu                        turn on/off curses emulation
        -/+dc                        turn off/on dynamic color selection
        -display displayname         X server to contact
        -e command args ...          command to execute
        -fa pattern                  FreeType font-selection pattern
        -fb fontname                 bold text font
        -/+fbb                       turn on/off normal/bold font comparison inhibit
        -/+fbx                       turn off/on linedrawing characters
        -fc fontmenu                 start with named fontmenu choice
        -fd pattern                  FreeType Doublesize font-selection pattern
        -fg color                    foreground color
        -fi fontname                 icon font for active icon
        -fn fontname                 normal text font
        -fs size                     FreeType font-size
        -/+fullscreen                turn on/off fullscreen on startup
        -fw fontname                 doublewidth text font
        -fwb fontname                doublewidth bold text font
        -fx fontname                 XIM fontset
        %geom                        Tek window geometry
        #geom                        icon window geometry
        -geometry geom               size (in characters) and position
        -help                        print out this message
        -/+hm                        turn on/off selection-color override
        -/+hold                      turn on/off logic that retains window after exit
        -iconic                      start iconic
        -/+ie                        turn on/off initialization of 'erase' from pty
        -/+im                        use insert mode for TERMCAP
        -into windowId               use the window id given to -into as the parent window rather than the default root window
        -/+itc                       turn off/on display of italic as color
        -/+j                         turn on/off jump scroll
        -/+k8                        turn on/off C1-printable classification
        -kt keyboardtype             set keyboard type: tcap sun vt220
        -/+l                         turn on/off logging
        -/+lc                        turn on/off locale mode using luit
        -lcc path                    filename of locale converter (/usr/bin/luit)
        -leftbar                     force scrollbar left
        -lf filename                 logging filename (use '-' for standard out)
        -/+ls                        turn on/off login shell
        -/+maximized                 turn on/off maximize on startup
        -/+mb                        turn on/off margin bell
        -mc milliseconds             multiclick time in milliseconds
        -/+mesg                      forbid/allow messages
        -/+mk_width                  turn on/off simple width convention
        -ms color                    pointer color
        -n string                    icon name for window
        -name string                 client instance, icon, and title strings
        -nb number                   margin bell in characters from right end
        -/+nul                       turn off/on display of underlining
        -/+pc                        turn on/off PC-style bold colors
        -pf fontname                 cursor font for text area pointer
        -/+pob                       turn on/off pop on bell
        -report-charclass            report "charClass" after initialization
        -report-colors               report colors as they are allocated
        -report-fonts                report fonts as loaded to stdout
        -report-icons                report title/icon updates
        -report-xres                 report X resources for VT100 widget
        -rightbar                    force scrollbar right (default left)
        -/+rv                        turn on/off reverse video
        -/+rvc                       turn off/on display of reverse as color
        -/+rw                        turn on/off reverse wraparound
        -/+s                         turn on/off multiscroll
        -/+samename                  turn on/off the no-flicker option for title and icon name
        -/+sb                        turn on/off scrollbar
        -selbg color                 selection background color
        -selfg color                 selection foreground color
        -/+sf                        turn on/off Sun Function Key escape codes
        -sh number                   scale line-height values by the given number
        -/+si                        turn on/off scroll-on-tty-output inhibit
        -/+sk                        turn on/off scroll-on-keypress
        -sl number                   number of scrolled lines to save
        -/+sm                        turn on/off the session-management support
        -/+sp                        turn on/off Sun/PC Function/Keypad mapping
        -/+t                         turn on/off Tek emulation window
        -ti termid                   terminal identifier
        -title string                title string
        -tm string                   terminal mode keywords and characters
        -tn name                     TERM environment variable name
        -/+u8                        turn on/off UTF-8 mode (implies wide-characters)
        -/+uc                        turn on/off underline cursor
        -/+ulc                       turn off/on display of underline as color
        -/+ulit                      turn off/on display of underline as italics
        -/+ut                        turn on/off utmp support
        -/+vb                        turn on/off visual bell
        -version                     print the version number
        -/+wc                        turn on/off wide-character mode
        -/+wf                        turn on/off wait for map before command exec
        -xrm resourcestring          additional resource specifications
        -ziconbeep percent           beep and flag icon of window having hidden output

    Fonts should be fixed width and, if both normal and bold are specified, should
    have the same size.  If only a normal font is specified, it will be used for
    both normal and bold text (by doing overstriking).  The -e option, if given,
    must appear at the end of the command line, otherwise the user's default shell
    will be started.  Options that start with a plus sign (+) restore the default.