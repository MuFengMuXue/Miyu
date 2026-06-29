**Resources**

[[]][Home](https://freedesktop.org/wiki/Software/libinput/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)#libinput "wikipedia:Wayland (display server protocol)")

[[]][Package information (libinput)](https://packages.gentoo.org/packages/dev-libs/libinput)

[[]][Package information (xf86-input-libinput)](https://packages.gentoo.org/packages/x11-drivers/xf86-input-libinput)

[[]][Official documentation](https://wayland.freedesktop.org/libinput/doc/latest/)

[[]][Bugs (upstream)](https://bugs.freedesktop.org/buglist.cgi?component=libinput&product=Wayland&resolution=---)

[[]][GitWeb](https://cgit.freedesktop.org/wayland/libinput)

**libinput** is an input device driver for [Wayland compositors](https://wiki.gentoo.org/wiki/Wayland_Desktop_Landscape#Compositors "Wayland Desktop Landscape") and [X.org](https://wiki.gentoo.org/wiki/Xorg "Xorg") window system. It is Gentoo Linux\'s default input device driver.

libinput provides device detection, device handling, input device event processing and abstraction to minimize the amount of custom input code compositors need to provide the common set of functionality that users expect.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [libinput-gestures for touchpad gestures]](#libinput-gestures_for_touchpad_gestures)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Xorg]](#Xorg)
        -   [[2.1.1] [Selecting libinput]](#Selecting_libinput)
        -   [[2.1.2] [Touchpad disable middle button]](#Touchpad_disable_middle_button)
        -   [[2.1.3] [Touchpad tap-to-click]](#Touchpad_tap-to-click)
        -   [[2.1.4] [Touchpad natural scrolling]](#Touchpad_natural_scrolling)
        -   [[2.1.5] [Pointer acceleration]](#Pointer_acceleration)
-   [[3] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Removing another input driver from INPUT_DEVICES does not prevent Xorg from loading it]](#Removing_another_input_driver_from_INPUT_DEVICES_does_not_prevent_Xorg_from_loading_it)
    -   [[4.2] [Gnome overriding touchpad settings after system upgrade]](#Gnome_overriding_touchpad_settings_after_system_upgrade)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [Kernel]

Support for Event interface (`CONFIG_INPUT_EVDEV`) needs to be enabled in the kernel:

[KERNEL] **Enabling Event interface in the kernel**

    Device Drivers --->
      Input device support --->
      <*>  Event interface

### [USE flags]

### [USE flags for] [dev-libs/libinput](https://packages.gentoo.org/packages/dev-libs/libinput) [[]] [Library to handle input devices in Wayland]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`lua`](https://packages.gentoo.org/useflags/lua)     Enable Lua scripting support
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 04:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Additional software]

#### [libinput-gestures for touchpad gestures]

In order to enable actions gestures on the touchpad using the libinput driver, install the [[[x11-misc/libinput-gestures]](https://packages.gentoo.org/packages/x11-misc/libinput-gestures)[]] package. First unmask the package:

[FILE] **`/etc/portage/package.accept_keywords/libinput-gestures`Unmasking unstable ebuilds**

    x11-misc/libinput-gestures ~amd64

Then merge the package:

`root `[`#`]`emerge --ask x11-misc/libinput-gestures`

Add user to the input group so devices can be read directly (replace \"larry\" with appropriate user name):

`root `[`#`]`usermod -a -G input larry`

Then follow the **Configuration** section on the [official project page.](https://github.com/bulletmark/libinput-gestures)

## [Configuration]

### [Xorg]

Some packages are aware of the [[[libinput]](https://packages.gentoo.org/useflags/libinput)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"). It should already [be set as the default input device driver](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=d3ac878318dd96a88190a13b5ac7572ec0c56380) by the make.defaults file.

To check if it is presently activated, run:

`user `[`$`]`portageq envvar INPUT_DEVICES`

If not, add it to the [/etc/portage/package.use/00input] variable:

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

After the update the packages [[[dev-libs/libinput]](https://packages.gentoo.org/packages/dev-libs/libinput)[]] and [[[x11-drivers/xf86-input-libinput]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-libinput)[]] should be installed.

By default, when libinput is the *only* available input driver for Xorg, no additional configuration is needed. Simply (re)start the graphical environment for the changes to take effect.

If *multiple* input drivers are available on the system ([[[x11-drivers/xf86-input-evdev]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-evdev)[]] and [[[x11-drivers/xf86-input-synaptics]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-synaptics)[]] for example), then additional configuration is required.

#### [Selecting libinput]

When multiple drivers are available on the system, Xorg must be instructed to use libinput before trying to use other input drivers. This can be simply performed by symlinking the [40-libinput.conf] file into the [/etc/X11/xorg.conf.d/] directory:

`root `[`#`]`ln -s /usr/share/X11/xorg.conf.d/40-libinput.conf /etc/X11/xorg.conf.d/`

If the [40-libinput.conf] will be edited, it is better to copy the file to the configuration directory:

`root `[`#`]`cp /usr/share/X11/xorg.conf.d/40-libinput.conf /etc/X11/xorg.conf.d/`

Xorg gives priority to the files in the [/etc/X11/xorg.conf.d/] directory.

(Re)start the graphical environment for the changes to take effect.

#### [Touchpad disable middle button]

Some laptops come with a middle button on their touchpad, which may be inconvenient and sometimes problematic for some users as it is often misclicked in place of the right or left button. It is possible to remove or remap that button by creating the following file:

[FILE] **`/etc/X11/xorg.conf.d/50-disable-middle-button.conf`**

    Section "InputClass"
        Identifier "Disable Middle Button"
        MatchIsTouchpad "on"
        Option "ButtonMapping" "1 0 3"
    EndSection

This way the button will be rendered useless. Alternatively, it can be remapped to left click by replacing \"1 0 3\" with \"1 1 3\" or right click with \"1 3 3\".

#### [Touchpad tap-to-click]

Many users will desire the native \'tap-to-click\" behavior for laptops with modern touchpads. Add the following Option lines to Xorg\'s libinput configuration section:

[FILE] **`/etc/X11/xorg.conf.d/40-libinput.conf`Adding tap-to-click**

    Section "InputClass"
         Identifier "libinput touchpad catchall"
         MatchIsTouchpad "on"
         MatchDevicePath "/dev/input/event*"
         Option "Tapping" "True"
         Option "TappingDrag" "True"
         Driver "libinput"
    EndSection

#### [Touchpad natural scrolling]

Natural scrolling (swipe up on touchpad - content goes up and scrollbar goes down) can be achieved by adding the following options to the [/etc/X11/xorg.conf.d/40-libinput.conf] file:

[FILE] **`/etc/X11/xorg.conf.d/40-libinput.conf`Adding natural scrolling**

    Section "InputClass"
         Identifier "libinput touchpad catchall"
         MatchIsTouchpad "on"
         MatchDevicePath "/dev/input/event*"
         Option "NaturalScrolling" "True"
         Driver "libinput"
    EndSection

Of course, multiple options can be combined without needing to create a new **Section** each time.

#### [Pointer acceleration]

A permanent reduction of pointer acceleration:

[FILE] **`/etc/X11/xorg.conf.d/40-libinput.conf`Setting acceleration to 90%**

    Section "InputClass"
            Identifier "libinput pointer catchall"
            MatchIsPointer "on"
            Driver "libinput"
            Option "TransformationMatrix" "0.90 0 0 0 0.90 0 0 0 1"
    EndSection

It is also possible to disable the acceleration completely:

[FILE] **`/etc/X11/xorg.conf.d/50-touchpad.conf`Disabling acceleration on touchpad**

    Section "InputClass"
            Identifier "Thinkpad TouchPad"
            # See the result of 'xinput list'
            MatchProduct "SynPS/2 Synaptics TouchPad"
            Driver "libinput"
            Option "AccelProfile" "flat"
    EndSection

For more information, refer to the [[[xorg.conf(5)]](https://man.archlinux.org/man/xorg.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.

The corresponding real-time test can be done using [xinput]. For example, for a Logitech G300s mouse :

`user `[`$`]`xinput list`

    Virtual core pointer                        id=2    [master pointer  (3)]
        ↳ Logitech G300s Optical Gaming Mouse       id=10   [slave  pointer  (2)]

`user `[`$`]`xinput list-props 10`

    Device 'Logitech G300s Optical Gaming Mouse':
        Coordinate Transformation Matrix (155): 1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000

`user `[`$`]`xinput set-prop 10 155 0.90 0 0 0 0.90 0 0 0 1`

## [Invocation]

To list the available input devices:

`root `[`#`]`libinput list-devices`

For detailed information, refer to the [[[libinput-list-devices(1)]](https://man.archlinux.org/man/libinput-list-devices.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.

`root `[`#`]`libinput debug-events`

Further invocations need [[[dev-python/python-libevdev]](https://packages.gentoo.org/packages/dev-python/python-libevdev)[]] installed:^[\[2\]](#cite_note-2)^

`user `[`$`]`libinput replay`

    Error: No module named 'libevdev'
    One or more python modules are missing. Please install those modules and re-run this tool.

For more details, refer to the [[[libinput-replay(1)]](https://man.archlinux.org/man/libinput-replay.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.

`user `[`$`]`libinput measure`

    Usage: libinput measure [--help] <feature> [/dev/input/event0]

For more details, refer to the [[[libinput-measure(1)]](https://man.archlinux.org/man/libinput-measure.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.

## [Troubleshooting]

### [Removing another input driver from INPUT_DEVICES does not prevent Xorg from loading it]

This issue can occur in a variety of situations, but it is most prominent when migrating from evdev to libinput.

Be sure the [[[x11-drivers/xf86-input-evdev]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-evdev)[]] package is no longer installed on the system. If [/usr/share/X11/xorg.conf.d/10-evdev.conf] exists then Xorg will still reference it.

Verify the evdev driver is no longer referenced anywhere by Portage (check [make.conf] and [package.use]), then depclean the system:

`root `[`#`]`emerge --ask --depclean`

### [Gnome overriding touchpad settings after system upgrade]

As per [this stack exchange post](https://unix.stackexchange.com/a/433827/93914), recent versions (\> 3.30.2 confirmed) of gnome override trackpad/touchpad options in X.org configuration. This can for instance cause right-click to stop working. These settings are not visible in the usual settings menu - you need to use gnome-tweak-tool and look under \'Keyboard & Mouse\' to change default behavior.

## [See also]

-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [Wacom](https://wiki.gentoo.org/wiki/Wacom "Wacom") --- provides instructions for enabling touchscreen support for [Wacom](https://www.wacom.com/) devices such as laptops, tablets, and ultrabooks, and the like.
-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").

## [External resources]

-   [\"This is the libinput API reference\"](https://wayland.freedesktop.org/libinput/doc/latest/api/)
-   [Gentoo forums discussion on libinput](https://forums.gentoo.org/viewtopic-t-1048230.html)
-   [Arch Linux wiki article on libinput](https://wiki.archlinux.org/index.php/Libinput)
-   [profiles: Switch default INPUT_DEVICES to libinput on Linux.](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=d3ac878318dd96a88190a13b5ac7572ec0c56380)
-   [[[libinput(1)]](https://man.archlinux.org/man/libinput.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[libinput(4)]](https://man.archlinux.org/man/libinput.4.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]

## [References]

1.  [[[↑](#cite_ref-1)] [[https://freedesktop.org/wiki/Software/libinput/](https://freedesktop.org/wiki/Software/libinput/)]]
2.  [[[↑](#cite_ref-2)] [[[[bug #703800]](https://bugs.gentoo.org/show_bug.cgi?id=703800)[]]]]