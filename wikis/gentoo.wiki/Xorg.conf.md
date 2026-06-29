The [xorg.conf] file is the main configuration file for the [X server](https://wiki.gentoo.org/wiki/X_server "X server").

** Note**\
Manually creating [xorg.conf] should be seen as a last resort option. It is typically desirable to run the X server without any special configuration. If you still can\'t get a working configuration, then read on.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [xorg.conf and xorg.conf.d]](#xorg.conf_and_xorg.conf.d)
    -   [[1.2] [Syntax]](#Syntax)
    -   [[1.3] [Sections]](#Sections)
        -   [[1.3.1] [ServerFlags]](#ServerFlags)
        -   [[1.3.2] [InputClass]](#InputClass)
        -   [[1.3.3] [Device]](#Device)
        -   [[1.3.4] [Monitor]](#Monitor)
    -   [[1.4] [Hot-swapping input devices]](#Hot-swapping_input_devices)
-   [[2] [See also]](#See_also)

## [Configuration]

### [xorg.conf and xorg.conf.d]

The X server read the settings from the files in [/etc/X11/xorg.conf.d/] directory (recommended) or the legacy [/etc/X11/xorg.conf] file. In the [/etc/X11/xorg.conf.d/] directory, each file is given a unique name and ends in [.conf]. If the filenames start with a number, then the X server will read the files in numeric order. [10-evdev.conf] will be read before [20-synaptics.conf], and so on. You don\'t have to give them numbers, but it may help you organize them.

The settings in [/etc/X11/xorg.conf] take precedence over the files in [/etc/X11/xorg.conf.d/], which take precedence over the files in [/usr/share/X11/xorg.conf.d/], which take precedence over the built-in X server configuration.

[[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]] provides example configurations in [/usr/share/doc/xorg-server-\*/xorg.conf.example.bz2]. You can use these to create your own configuration files in [/etc/X11/xorg.conf.d/].

### [Syntax]

The configuration is composed of a number of sections. The most common ones include:

-   [ServerFlags](#ServerFlags): Common X server settings
-   [InputClass](#InputClass): Settings for input devices
-   [Device](#Device): Settings for graphics cards
-   [Monitor](#Monitor): Settings for displays
-   Screen: Settings for \"graphics card / display\"-combinations
-   ServerLayout: Settings for \"screen / input devices\"-combinations

Lines starting with a hash (**\#**) are comments and are ignored by the X server. Each other line in a section define a value to an option. The value can be of the following types:

-   *INTEGER*: an integer number in decimal, hex or octal, e.g. 1, 2, 3, etc.
-   *REAL*: a floating point number, e.g. 1.2
-   *STRING*: a string enclosed in double quote marks (\"), e.g. \"Hello world!\"

Most options and values are case-insensitive. Superfluous white spaces are ignored.

The special option named *Option* accepts also the additional types:

-   *BOOLEAN*: a boolean value, e.g. **on**, **true**, **1** or **yes**; **off**, **false**, **0** or **no**.
-   *FREQUENCY*: in **Hz**, **k**, **kHz**, **M** or **MHz**

Note also that the *Option* values must be enclosed in double quote marks (\").

### [Sections]

#### [ServerFlags]

An example *ServerFlags* section looks like this:

[FILE] **`/etc/X11/xorg.conf`**

    Section "ServerFlags"
       Option "OffTime" "5"
       ...
    EndSection

All entries are optional.

The most common options are:

  ----------------------------------------- --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Option                                    Default   Description
  *Option \"AutoAddDevices\" \"BOOLEAN\"*   *true*    Enables or disables the automatic detection of input devices using [udev](https://wiki.gentoo.org/wiki/Udev "Udev").
  *Option \"AutoAddGPU\" \"BOOLEAN\"*       *true*    If disabled then no GPU devices will be added from the udev backend.
  *Option \"AutoBindGPU\" \"BOOLEAN\"*      *true*    If enabled then secondary GPUs will be automatically set up as output-sinks and offload-sources. Making e.g. laptop outputs connected only to the secondary GPU directly available for use (without needing to run `xrandr --setprovideroutputsource`).
  *Option \"OffTime\" \"INTEGER\"*          *10*      Turns off the monitor after the given time (in minutes) of inactivity.
  ----------------------------------------- --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more information see the [xorg.conf] [man page](https://wiki.gentoo.org/wiki/Man_page "Man page").

#### [InputClass]

Create for each input device class (keyboard, mouse, etc.) a *InputClass* section. An example *InputClass* section looks like this:

[FILE] **`/etc/X11/xorg.conf`**

    Section "InputClass"
       Identifier   "My Keyboard"
       MatchIsKeyboard "True"
       ...
    EndSection

*Identifier* is mandatory, everything else is optional.

Without specify a matching condition a *InputClass* section applies to all input devices. Add a matching condition to apply settings only to input devices of the target class or to a single device. The most common conditions are:

  ---------------------------------- -------------------------------------------------
  Condition                          Description
  *MatchIsKeyboard \"BOOLEAN\"*      Match only keyboards
  *MatchIsPointer \"BOOLEAN\"*       Match only mice
  *MatchIsJoystick \"BOOLEAN\"*      Match only joysticks
  *MatchIsTablet \"BOOLEAN\"*        Match only tablets
  *MatchIsTouchpad \"BOOLEAN\"*      Match only touchpads
  *MatchIsTouchscreen \"BOOLEAN\"*   Match only touchscreens
  *MatchProduct \"STRING\"*          Match only devices with the given product name.
  *MatchVendor \"STRING\"*           Match only devices with the given vendor name.
  ---------------------------------- -------------------------------------------------

The most common options are:

  ------------------------------------ --------- -------------------------------------------------------------------------------------------------------------------------------------------------
  Option                               Default   Description
  *Identifier \"STRING\"*              none      Specify an unique name
  *Driver \"STRING\"*                  none      Specify the input device driver, see the [input device articles](https://wiki.gentoo.org/wiki/Category:Input_devices "Category:Input devices").
  *Option \"Ignore\" \"BOOLEAN\"*      *false*   Disable the input device (useful for e.g. sensors)
  *Option \"XkbLayout\" \"STRING\"*    *en*      Specify a keyboard layout.
  *Option \"XkbVariant\" \"STRING\"*             Specify a keyboard layout variant
  *Option \"XkbOptions\" \"STRING\"*             Specify keyboard layout options
  ------------------------------------ --------- -------------------------------------------------------------------------------------------------------------------------------------------------

For more information see the [xorg.conf] [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") and the man pages of your input device drivers.

#### [Device]

Create for each graphics card a *Device* section. An example *Device* section looks like this:

[FILE] **`/etc/X11/xorg.conf`**

    Section "Device"
       Identifier   "My Graphics Card"
       Driver       "intel"
       ...
    EndSection

*Identifier* and *Driver* is mandatory, everything else is optional.

The most common options are:

  ---------------------------------------- ----------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Option                                   Default                 Description
  *Identifier \"STRING\"*                  none                    Specify an unique name
  *Driver \"STRING\"*                      none                    Specify the graphics driver, see the [graphics drivers articles](https://wiki.gentoo.org/wiki/Category:Video_cards "Category:Video cards").
  *BusID \"STRING\"*                       none                    For multiple graphics cards specify the BusID in the form *PCI:bus:device:function* provided by **scanpci**.
  *Option \"Accel\" \"STRING\"*            driver/card dependent   Specify a 2D acceleration system
  *Option \"Monitor-OUTPUT\" \"STRING\"*   none                    Force bind a *Monitor* section to this device. *OUTPUT* is a connector name, see [xrandr](https://wiki.gentoo.org/wiki/Xrandr "Xrandr"), and *STRING* is the chosen identifier of the *Monitor* section.
  ---------------------------------------- ----------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more information see the [xorg.conf] [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") and the man pages of your graphics drivers.

#### [Monitor]

Create for each monitor a *Monitor* section. An example *Monitor* section looks like this:

[FILE] **`/etc/X11/xorg.conf`**

    Section "Monitor"
       Identifier   "My Monitor"
       ...
    EndSection

*Identifier* is mandatory, everything else is optional.

The most common options are:

  --------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
  Option                                  Default                                                                                                                               Description
  *Identifier \"STRING\"*                 none                                                                                                                                  Specify an unique name
  *DisplaySize INTEGER INTEGER*           [EDID](https://en.wikipedia.org/wiki/Extended_display_identification_data "wikipedia:Extended display identification data")   Specify the physical width and height (in millimeters) of the monitor. It will be used to calculate the DPI.
  *Modeline \"STRING\" \...*              [EDID](https://en.wikipedia.org/wiki/Extended_display_identification_data "wikipedia:Extended display identification data")   Specify a new [mode](https://en.wikipedia.org/wiki/XFree86_Modeline "wikipedia:XFree86 Modeline") entry.
  *Option \"Enable\" \"BOOLEAN\"*         *true*                                                                                                                                Enables or disables the monitor by default.
  *Option \"PreferredMode\" \"STRING\"*   none                                                                                                                                  Specify the default mode.
  --------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------

For more information see the [xorg.conf] [man page](https://wiki.gentoo.org/wiki/Man_page "Man page").

### [Hot-swapping input devices]

For input devices override the configuration of [xorg.conf] by using the [xinput] command:

`user `[`$`]`xinput list`

    ⎡ Virtual core pointer                      id=2    [master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
    ⎜   ↳ Synaptics TM3127-001                      id=11   [slave  pointer  (2)]
    ⎣ Virtual core keyboard                     id=3    [master keyboard (2)]
        ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
    ...

`user `[`$`]`xinput --list-props 11 # One of the above id number `

    Device 'Synaptics TM3127-001':
            Device Enabled (146):   1
            Coordinate Transformation Matrix (148): 1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000
            libinput Tapping Enabled (311): 1
            libinput Tapping Enabled Default (312): 0
        ...

To change \"Tapping Enabled\" to 0 (i.e. false), run:

`user `[`$`]`xinput --set-prop --type=int 11 311 0 `

## [See also]

-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients