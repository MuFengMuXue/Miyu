**Resources**

[[]][Home](http://qingy.sourceforge.net/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/qingy)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/qingy)

**Qingy** (**Q**ingy **I**s **N**ot **G**ett**Y**) is a replacement for getty. Written in C, it uses DirectFB to provide a GUI without the overhead of the X Windows System. It allows the user to log in and start the session of choice (text console, GNOME, KDE, wmaker, etc.).

** Note**\
DirectFB is no longer in available in Portage as per [[[bug #606194]](https://bugs.gentoo.org/show_bug.cgi?id=606194)[]]. All that remains now is a text mode login.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Keypair]](#Keypair)
    -   [[2.2] [inittab]](#inittab)
    -   [[2.3] [Configuration file]](#Configuration_file)
-   [[3] [Display managers]](#Display_managers)
-   [[4] [Starting qingy]](#Starting_qingy)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/qingy](https://packages.gentoo.org/packages/sys-apps/qingy) [[]] [A DirectFB getty replacement]

  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)             Add support for X11
  [`crypt`](https://packages.gentoo.org/useflags/crypt)     Add support for encryption \-- using mcrypt or gpg where applicable
  [`emacs`](https://packages.gentoo.org/useflags/emacs)     Add support for GNU Emacs
  [`gpm`](https://packages.gentoo.org/useflags/gpm)         Add support for sys-libs/gpm (Console-based mouse driver)
  [`pam`](https://packages.gentoo.org/useflags/pam)         Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`static`](https://packages.gentoo.org/useflags/static)   !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-04-23 18:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask qingy`

## [Configuration]

### [Keypair]

qingy requires keypairs to run. To generate keys:

`root `[`#`]`qingy-keygen`

### [inittab]

After successful installation edit the [/etc/inittab] file and replace following section:

[FILE] **`/etc/inittab`**

    ...
    # TERMINALS
    c1:12345:respawn:/sbin/agetty 38400 tty1 linux
    c2:2345:respawn:/sbin/agetty 38400 tty2 linux
    c3:2345:respawn:/sbin/agetty 38400 tty3 linux
    c4:2345:respawn:/sbin/agetty 38400 tty4 linux
    c5:2345:respawn:/sbin/agetty 38400 tty5 linux
    c6:2345:respawn:/sbin/agetty 38400 tty6 linux
    ...

with following entries:

[FILE] **`/etc/inittab`**

    ...
    # TERMINALS
    c1:12345:respawn:/sbin/qingy tty1
    c2:12345:respawn:/sbin/qingy tty2
    c3:12345:respawn:/sbin/qingy tty3
    c4:12345:respawn:/sbin/qingy tty4
    c5:12345:respawn:/sbin/qingy tty5
    c6:12345:respawn:/sbin/agetty 38400 tty6 linux
    ...

** Note**\
Leave the 6-th terminal tty6 assigned to agetty. Pressing [Ctrl]+[Alt]+[F6] will get the agetty spawned terminal, just in case something goes wrong at least one working terminal will be available.

### [Configuration file]

This is default qingy\'s configuration as shipped with Gentoo:

[FILE] **`/etc/qingy/settings`**

    x_sessions = "/etc/X11/Sessions/"
    text_sessions = "/etc/qingy/sessions/"
    temp_files_dir = "/var/lib/misc"

    xinit = "/usr/bin/xinit"
    x_args = "-nolisten tcp -br"

    log_level = error
    log_facilities = console

    x_server_tty = qingy_tty

    pre_gui_script  = "/etc/qingy/pre_GUI.sh"
    post_gui_script = "/etc/qingy/post_GUI.sh"

    themes_dir = "/usr/share/qingy/themes"
    theme = gentoo

    keybindings


## [Display managers]

Remove xdm and display-manager from the default startup level, otherwise they will fight with qingy for screen control at system boot. This sometimes results in nasty results.

`root `[`#`]`rc-update del xdm default`

`root `[`#`]`rc-update del display-manager default`

## [Starting qingy]

Now either reboot the system or use following commands:

`root `[`#`]`init Q `

`root `[`#`]`killall agetty`

After successful authentication qingy will list contents of [/etc/X11/Xsession/] directory:

     Welcome, $, please select a session...
     (a) dwm
     (b) fvwm
     (c) Your .xsession
     (d) Text: Console
     Your choice (just press ENTER for 'Text: Console'):

Different Xsessions can be started in each tty, which works fine. Use the [Ctrl]+[Alt]+[F1] through [F6] key combinations to switch between different X sessions.

## [Troubleshooting]

If qingy hangs making it impossible to login press [Ctrl]+[Alt]+[F6] to get the agetty spawned terminal and login from there.

## [See also]

## [External resources]

-   [http://qingy.sourceforge.net/faq.php#Gentoo%20specific](http://qingy.sourceforge.net/faq.php#Gentoo%20specific)
-   [http://qingy.sourceforge.net/manual.php](http://qingy.sourceforge.net/manual.php)