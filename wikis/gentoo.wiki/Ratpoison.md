**Resources**

[[]][Home](https://nongnu.org/ratpoison/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ratpoison "wikipedia:Ratpoison")

[[]][GitWeb](https://git.savannah.gnu.org/cgit/ratpoison.git)

**ratpoison** is a tiling [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") modeled after [`screen`](https://wiki.gentoo.org/wiki/Screen "Screen"). The main philosophy behind ratpoison is to manage window without using a mouse (what its name reflects). Written in C, it is extremely lightweight and fast.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Starting]](#Starting)
    -   [[2.2] [Startup file]](#Startup_file)
-   [[3] [Usage]](#Usage)
-   [[4] [Tips]](#Tips)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [x11-wm/ratpoison](https://packages.gentoo.org/packages/x11-wm/ratpoison) [[]] [window manager without mouse dependency]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+history`](https://packages.gentoo.org/useflags/+history)   Use sys-libs/readline for history handling
  [`+xft`](https://packages.gentoo.org/useflags/+xft)           Build with support for XFT font renderer (x11-libs/libXft)
  [`+xrandr`](https://packages.gentoo.org/useflags/+xrandr)     Enable support for XRandR
  [`debug`](https://packages.gentoo.org/useflags/debug)         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`emacs`](https://packages.gentoo.org/useflags/emacs)         Add support for GNU Emacs
  [`sloppy`](https://packages.gentoo.org/useflags/sloppy)       Install sloppy, a focus-follows-mouse implementation for ratpoison
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[x11-wm/ratpoison]](https://packages.gentoo.org/packages/x11-wm/ratpoison)[]]:

`root `[`#`]`emerge --ask x11-wm/ratpoison`

## [Configuration]

### [Starting]

Edit [\~/.xinitrc] in the user\'s home directory by adding the following line:

[FILE] **`~/.xinitrc`**

    exec /usr/bin/ratpoison

### [Startup file]

Being a simple window manager, ratpoison does not need much out-of-the-box configuration. Customizable settings can be adjusted to each user\'s needs by editing ratpoison\'s start up file.

On start up ratpoison runs commands found in the [\~/.ratpoisonrc] file. This file contains key bindings and programs that need to be run with ratpoison. Here is an example of a [\~/.ratpoisonrc] file:

[FILE] **`~/.ratpoisonrc`**

    # Add key bindings:
    bind c exec /usr/bin/urxvt
    bind e exec /usr/bin/urxvt -e /usr/bin/emacs
    bind m exec /usr/bin/urxvt -bg black -fg white -e /usr/bin/mitmproxy
    bind f exec /usr/bin/firefox

    # What programs should be ran on start up?
    exec /usr/bin/numlockx

    # Initiate here the number of desired workspaces:
    exec /usr/bin/rpws init 6 -k

## [Usage]

Since ratpoison is modeled after `screen`, users accustomed to `screen` will easily manage to use it. Each command begins with a [Ctrl]-[t] (abbreviated C-t from now on), and is followed by one other keystroke. The simplest way to get to know the commands is to press C-t ? This will open a help window containing the most common key bindings.

Most commonly used keys:

  ----------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Keystroke   Description
  C-t C-c     Execute xterm
  C-t !       Spawn a shell executing shell command, usually an application, such as C-t ! firefox [Enter]
  C-t k       Close the current window
  C-t b       Banish the rat cursor to the lower right corner of the screen. The next step would be to unplug the rat from the computer altogether.
  C-t C-t     Switch to the window that was last accessed but is not currently visible
  C-t s       Split the current frame into upper frame and a lower frame. By default, split in halves.
  C-t S       Split the current frame into left frame and a right frame.
  C-t r       Resize the current frame interactively by pressing [Up] and [Down] keys. Hit [Enter] when finished.
  C-t R       Remove the current frame and extend some frames around to fill the remaining gap.
  C-t :quit   Run before exiting ratpoison
  C-t a       Output current data and time
  C-t C-g     Do nothing and that successfully
  ----------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

** Note**\
All windows are maximized to the full screen size.

## [Tips]

By default, ratpoison only has one workspace. Add the following line to the [\~/.ratpoisonrc] file in order to create six workspaces:

[FILE] **`~/.ratpoisonrc`**

    exec /usr/bin/rpws init 6 -k

Switch between workspaces with [Alt]+[F1], [Alt]+[F2], etc.

## [See also]

-   [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox") --- a highly configurable stacking [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11") with extensive standards support.
-   [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE") - The Lightweight X11 Desktop Environment built off Openbox and a smart collection of lightweight applications.
-   [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") --- a lightweight [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") built to be fast, good looking, and user friendly.