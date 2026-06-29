**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:GNU_Emacs "Project:GNU Emacs")][Project](https://wiki.gentoo.org/wiki/Project:GNU_Emacs "Project:GNU Emacs")

[[]][Home](https://www.gnu.org/software/emacs/)

[[]][Official documentation](https://www.gnu.org/software/emacs/documentation.html)

[[]][Package information](https://packages.gentoo.org/packages/app-editors/emacs)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_Emacs "wikipedia:GNU Emacs")

[[]][[#emacs](ircs://irc.libera.chat/#emacs)] ([[webchat](https://web.libera.chat/#emacs)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/emacs)

**GNU Emacs** is a powerful, extensible, self-documenting text editor. It is released by the [Free Software Foundation](https://www.fsf.org/) and has been under development since 1985.

In Gentoo, GNU Emacs is maintained by the team of the same name, which can be reached through [gnu-emacs@gentoo.org](mailto:gnu-emacs@gentoo.org). Detailed developer information can be found on the [project page](https://wiki.gentoo.org/wiki/Project:Emacs "Project:Emacs").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
        -   [[1.1.1] [JIT]](#JIT)
        -   [[1.1.2] [PGTK]](#PGTK)
        -   [[1.1.3] [SSL]](#SSL)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Several versions side-by-side]](#Several_versions_side-by-side)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Gentoo packages]](#Gentoo_packages)
    -   [[2.2] [Daemon]](#Daemon)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
        -   [[2.2.3] [Builtin method]](#Builtin_method)
        -   [[2.2.4] [Connect to emacs daemon]](#Connect_to_emacs_daemon)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Exiting Emacs]](#Exiting_Emacs)
    -   [[3.2] [Documentation]](#Documentation)
    -   [[3.3] [Starter Kits]](#Starter_Kits)
    -   [[3.4] [Vim controls]](#Vim_controls)
-   [[4] [Additional elisp packages]](#Additional_elisp_packages)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

** Note**\
Some packages have the [[[emacs]](https://packages.gentoo.org/useflags/emacs)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") set, which usually adds emacs-related functionality.

### [USE flags for] [app-editors/emacs](https://packages.gentoo.org/packages/app-editors/emacs) [[]] [The advanced, extensible, customizable, self-documenting editor]

  ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                                     Add support for X11
  [`+gmp`](https://packages.gentoo.org/useflags/+gmp)                                 Use the GNU multiple precision arithmetic library (dev-libs/gmp) instead of the bundled mini-gmp subset
  [`+inotify`](https://packages.gentoo.org/useflags/+inotify)                         Enable inotify filesystem monitoring support
  [`+threads`](https://packages.gentoo.org/useflags/+threads)                         Add elisp threading support
  [`+xpm`](https://packages.gentoo.org/useflags/+xpm)                                 Add support for XPM graphics format
  [`Xaw3d`](https://packages.gentoo.org/useflags/Xaw3d)                               Add support for the 3d athena widget set
  [`acl`](https://packages.gentoo.org/useflags/acl)                                   Add support for Access Control Lists
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                                 Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`aqua`](https://packages.gentoo.org/useflags/aqua)                                 Include support for the Mac OS X Aqua (Carbon/Cocoa) GUI
  [`athena`](https://packages.gentoo.org/useflags/athena)                             Enable the MIT Athena widget set (x11-libs/libXaw)
  [`cairo`](https://packages.gentoo.org/useflags/cairo)                               Enable support for the cairo graphics library
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                                 Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`dynamic-loading`](https://packages.gentoo.org/useflags/dynamic-loading)           Enable loading of dynamic libraries (modules) at runtime
  [`games`](https://packages.gentoo.org/useflags/games)                               Support shared score files for games
  [`gfile`](https://packages.gentoo.org/useflags/gfile)                               Use gfile (dev-libs/glib) for file notification
  [`gif`](https://packages.gentoo.org/useflags/gif)                                   Add GIF image support
  [`gpm`](https://packages.gentoo.org/useflags/gpm)                                   Add support for sys-libs/gpm (Console-based mouse driver)
  [`gsettings`](https://packages.gentoo.org/useflags/gsettings)                       Use gsettings (dev-libs/glib) to read the system font name
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                                   Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`gui`](https://packages.gentoo.org/useflags/gui)                                   Enable support for a graphical user interface
  [`gzip-el`](https://packages.gentoo.org/useflags/gzip-el)                           Compress bundled Emacs Lisp source
  [`harfbuzz`](https://packages.gentoo.org/useflags/harfbuzz)                         Use media-libs/harfbuzz as text shaping engine
  [`imagemagick`](https://packages.gentoo.org/useflags/imagemagick)                   Use media-gfx/imagemagick for image processing
  [`jit`](https://packages.gentoo.org/useflags/jit)                                   Compile with Emacs Lisp native compiler support via libgccjit
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)                                 Add JPEG image support
  [`json`](https://packages.gentoo.org/useflags/json)                                 Compile with native JSON support using dev-libs/jansson
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)                         Add kerberos support
  [`lcms`](https://packages.gentoo.org/useflags/lcms)                                 Add lcms support (color management engine)
  [`libxml2`](https://packages.gentoo.org/useflags/libxml2)                           Use dev-libs/libxml2 to parse XML instead of the internal Lisp implementations
  [`livecd`](https://packages.gentoo.org/useflags/livecd)                             !!internal use only!! DO NOT SET THIS FLAG YOURSELF!, used during livecd building
  [`m17n-lib`](https://packages.gentoo.org/useflags/m17n-lib)                         Enable m17n-lib support
  [`mailutils`](https://packages.gentoo.org/useflags/mailutils)                       Retrieve e-mail using net-mail/mailutils instead of the internal movemail substitute
  [`motif`](https://packages.gentoo.org/useflags/motif)                               Add support for the Motif toolkit
  [`png`](https://packages.gentoo.org/useflags/png)                                   Add support for libpng (PNG images)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sound`](https://packages.gentoo.org/useflags/sound)                               Enable sound support
  [`source`](https://packages.gentoo.org/useflags/source)                             Install C source files and make them available for find-function
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)                             Add support for sqlite - embedded sql database
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                                   Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`svg`](https://packages.gentoo.org/useflags/svg)                                   Add support for SVG (Scalable Vector Graphics)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`tiff`](https://packages.gentoo.org/useflags/tiff)                                 Add support for the TIFF image format
  [`toolkit-scroll-bars`](https://packages.gentoo.org/useflags/toolkit-scroll-bars)   Use the selected toolkit\'s scrollbars in preference to Emacs\' own scrollbars
  [`tree-sitter`](https://packages.gentoo.org/useflags/tree-sitter)                   Support the dev-libs/tree-sitter parsing library
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)                         Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`webp`](https://packages.gentoo.org/useflags/webp)                                 Add support for the WebP image format
  [`wide-int`](https://packages.gentoo.org/useflags/wide-int)                         Prefer wide Emacs integers (typically 62-bit). This option has an effect only on 32-bit systems, where it increases the maximum buffer size from 0.5 to 2 GiB, at the cost of 10% to 30% Lisp slowdown.
  [`xattr`](https://packages.gentoo.org/useflags/xattr)                               Add support for extended attributes (filesystem-stored metadata)
  [`xft`](https://packages.gentoo.org/useflags/xft)                                   Build with support for XFT font renderer (x11-libs/libXft)
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                                 Add support for zlib compression
  ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-11 22:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

`USE="mailutils"` is encouraged for e-mail features.

For Xorg or Wayland, at least `USE="gui"` is required. After Emacs 29 on Wayland, [[[bug #831154]](https://bugs.gentoo.org/show_bug.cgi?id=831154)[]] recommends `USE="-X gtk"` enabled \"pure GTK mode\".

Toolkit USE flags are mutually exclusive, so enable only one of: `gtk`, `athena`, `motif`, or `aqua`.

-   `USE="aqua"` only applies to [macOS](https://wiki.gentoo.org/wiki/Prefix/Darwin "Prefix/Darwin").
-   `USE="gtk"` is generally good for systems with one display.
-   Multiple displays may `USE="athena Xaw3d"` which resembles gtk very well.
-   An alternative for multiple displays is `USE="motif"`.
-   To use Emacs as a daemon, [[[bug #292471]](https://bugs.gentoo.org/show_bug.cgi?id=292471)[]] recommends `USE="athena Xaw3d -motif -gtk"` or `USE="motif -athena -Xaw3d -gtk"`.

\

#### [JIT]

Emacs can use [gcc](https://wiki.gentoo.org/wiki/C "C") to compile Emacs Lisp code to native binaries (they have `.eln` suffix) which gives a nice performance boost.

To use it, activate the [[[jit]](https://packages.gentoo.org/useflags/jit)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag for [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]] and [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]:

[FILE] **`/etc/portage/package.use`**

    app-editors/emacs jit
    sys-devel/gcc jit

Then complete a world upgrade for these changes to take effect:

`root `[`#`]`emerge --ask --update --changed-use @world`

** Note**\
The Gentoo ebuild compiles the whole emacs distribution Lisp code: [https://www.emacswiki.org/emacs/GccEmacs#h5o-15](https://www.emacswiki.org/emacs/GccEmacs#h5o-15)

** Note**\
Emacs packages do not yet handle JIT by themselves: [[[bug #735148]](https://bugs.gentoo.org/show_bug.cgi?id=735148)[]].

\

#### [PGTK]

Emacs can be built to the use \"pgtk\" (Pure [GTK](https://wiki.gentoo.org/wiki/GTK "GTK")) frontend: Emacs will no longer use [X11](https://wiki.gentoo.org/wiki/X11 "X11") APIs directly, instead it only uses [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") (and [Cairo](https://wiki.gentoo.org/index.php?title=Cairo&action=edit&redlink=1 "Cairo (page does not exist)")), hence (in theory) any platform supported by [GTK](https://wiki.gentoo.org/wiki/GTK "GTK"), such as [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") (without the need for XWayland).

To activate pgtk, disable the [[[X]](https://packages.gentoo.org/useflags/X)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag and enable [[[gui]](https://packages.gentoo.org/useflags/gui)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[gtk]](https://packages.gentoo.org/useflags/gtk)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] for [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]]:

[FILE] **`/etc/portage/package.use`**

    app-editors/emacs gui gtk -X

Then run:

`root `[`#`]`emerge --ask --update --changed-use @world`

This will also get rid of the warning:

    Warning: due to a long standing Gtk+ bug
    http://bugzilla.gnome.org/show_bug.cgi?id=85715
    Emacs might crash when run in daemon mode and the X11 connection is unexpectedly lost.
    Using an Emacs configured with --with-x-toolkit=lucid does not have this problem.

Of course, the underlying Gtk+ problem still exists, and multiple displays cannot be used with pgtk.

#### [SSL]

To use Emacs for ERC or when desiring to download packages from ELPA/MELPA via Emacs, it is wise to compile with the `ssl` USE flag. Emacs will use the program [gnutls-cli] (provided by [[[net-libs/gnutls]](https://packages.gentoo.org/packages/net-libs/gnutls)[]]), but only when it is also compiled with the `tools` USE flag. The `tools` USE flag is not enabled by default.

### [Emerge]

To install Emacs, run:

`root `[`#`]`emerge --ask app-editors/emacs`

### [Several versions side-by-side]

In Gentoo, several Emacs versions can be installed on a system simultaneously. The upstream version already installs elisp and data files into versioned subdirectories. To avoid file collisions between slots, in Gentoo binaries and man pages are suffixed with their corresponding version number, too.

The eselect module from [[[app-eselect/eselect-emacs]](https://packages.gentoo.org/packages/app-eselect/eselect-emacs)[]] can be used to link [/usr/bin/emacs] and its auxiliary programs to the ones belonging to the desired Emacs version. Consult the [eselect user guide](https://wiki.gentoo.org/wiki/Project:Eselect/User_guide "Project:Eselect/User guide") for details on eselect.

## [Configuration]

Emacs can be customized by clicking through the GUI (use [M-x] `customize-group` [RET]).

Emacs can also be configured by using the [\~/.emacs] configuration file, which is written in Emacs Lisp, Emacs\' own Lisp dialect. The [\~/.emacs] file is not automatically created on installation or on first invocation, though the directory [\~/.emacs.d] can be.

### [Gentoo packages]

Gentoo provide many Emacs Lisp packages available for installation:

`root `[`#`]`emerge --search 'app-emacs/*'`

Package are installed to `/usr/share/emacs/site-lisp`. After installation, package\'s paths are added to Emacs `load-path` global variable and *autoloaded*. This behavior may be controlled in `/etc/emacs/site-start.el` Emacs initialization file.

### [Daemon]

#### [OpenRC]

** Tip**\
Customization is available via [/etc/conf.d/emacs] and [/etc/conf.d/emacs.\<user\>]

Gentoo provides OpenRC init scripts for Emacs in the package [[[app-emacs/emacs-daemon]](https://packages.gentoo.org/packages/app-emacs/emacs-daemon)[]]:

`root `[`#`]`emerge --ask app-emacs/emacs-daemon`

First, create a symlink for at least one user in [/etc/init.d]:

`root `[`#`]`ln -s /etc/init.d/emacs /etc/init.d/emacs.myuser`

Then add it to the appropriate runlevel:

`root `[`#`]`rc-update add emacs.myuser default`

Finally, start up the new Emacs service:

`root `[`#`]`/etc/init.d/emacs.myuser start`

Usually, an Emacs server socket will be created for [emacsclient] to connect to. The socket will be created at [/tmp/emacs\<user_id\>/server], e.g. [/tmp/emacs1000/server]. To use [emacsclient] with this socket, use the `-s` / `--socket-name` option, e.g.:

`user `[`$`]`emacsclient --socket-name='/tmp/emacs1000/server'`

\

#### [systemd]

With systemd, simply enable the upstream user unit:

`user `[`$`]`systemctl --user enable --now emacs`

#### [Builtin method]

The user can also start the daemon inside an already running instance of emacs. For that, type [M-x server-start RET] (that is, [Meta], or [Alt], followed by [x server-start], and finally [Enter]).

#### [Connect to emacs daemon]

`user `[`$`]`emacsclient --socket-name=/tmp/emacs$(id -u)/server file`

** Tip**\
If user starts the daemon inside emacs, everything works out-of-the-box. Otherwise, in order to save typing while connecting to the emacs daemon, export `EMACS_SOCKET_NAME` in a user\'s profile file, as in the example above. See [[[bug #794649]](https://bugs.gentoo.org/show_bug.cgi?id=794649)[]]. This method also guarantees that exporting `EDITOR=emacsclient` will work as expected.

## [Usage]

### [Exiting Emacs]

For beginners who don\'t know the key combinations, it may be difficult to exit Emacs. To close Emacs, type [C-x C-c] ([Ctrl]+[x] followed by [Ctrl]+[c]).

### [Documentation]

For a quick-start documentation, type in Emacs: [C-h t] ([Ctrl]+[h] followed by [t]). For further help on how to use Emacs, start `emacs` and type [C-h r] ([Ctrl]+[h] followed by [r]).

-   [A guided tour of Emacs](https://www.gnu.org/software/emacs/tour/)
-   [GNU Emacs manual](https://www.gnu.org/software/emacs/manual/emacs.html)

### [Starter Kits]

Since Emacs supports so many features and additional packages, configuration and customization can become cumbersome, an [*Emacs distribution*](https://www.emacswiki.org/emacs/StarterKits) may help starting out. They aim to provide a \"batteries included\" approach and plug together many features and packages automatically:

-   [Spacemacs](https://wiki.gentoo.org/wiki/Spacemacs "Spacemacs")
-   [Doom Emacs](https://github.com/doomemacs/doomemacs)
-   [Prelude](https://prelude.emacsredux.com)

### [Vim controls]

Contrary to popular belief, many Emacs users prefer to get the best out of [\"both worlds\"](https://en.wikipedia.org/wiki/Editor_war). To do so, [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") and Emacs features can be combined (and used alongside), for example, with [Evil](https://github.com/emacs-evil/evil).

[Spacemacs](https://wiki.gentoo.org/wiki/Spacemacs "Spacemacs") and [Doom](https://github.com/doomemacs/doomemacs) support this out of the box.

## [Additional elisp packages]

Emacs has lots of additional packages written in elisp.

Users have two choices:

1.  If installing packages per-user, [package.el](https://www.emacswiki.org/emacs/ELPA) is recommended. Other methods exist too such as [straight.el](https://github.com/radian-software/straight.el) and [Elpaca](https://github.com/progfolio/elpaca).
2.  If installing packages through the system\'s package manager is preferred, then only [emerge] is needed.

## [See also]

-   [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs") --- a class of powerful, extensible, self-documenting text editors.
-   [Knowledge Base:Edit a configuration file](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file")
-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.
-   [Xft support for GNU Emacs](https://wiki.gentoo.org/wiki/Xft_support_for_GNU_Emacs "Xft support for GNU Emacs") --- describes how to enable font anti-aliasing in Emacs using the Xft library.