**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Displaylink#Technology "wikipedia:Displaylink")

**Article status**

[[]]This article has some todo items:\

-   [One X-Server](#One_X-Server)

**DisplayLink** is a technology that enables monitors to work via [USB](https://wiki.gentoo.org/wiki/USB "USB").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [X driver]](#X_driver)
-   [[2] [One X server]](#One_X_server)
-   [[3] [Two X server]](#Two_X_server)
    -   [[3.1] [Software]](#Software)
    -   [[3.2] [xorg.conf.DL]](#xorg.conf.DL)
    -   [[3.3] [.xinitrc2]](#.xinitrc2)
    -   [[3.4] [displaylink.sh]](#displaylink.sh)
-   [[4] [DisplayLink 4-in-1 Adapter]](#DisplayLink_4-in-1_Adapter)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

Activate the following kernel options:

[KERNEL]

    Device Drivers --->
        Graphics support --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
                <*> DisplayLink
            <*> Frame buffer Devices --->
                <*> Displaylink USB Framebuffer support
                <*> Provide legacy /dev/fb* device

After booting into the new kernel the external monitor should show a green background image. That means the kernel module is loaded and the device works, it also creates the device in [/dev/fb0].

** Note**\
If there are other [framebuffer](https://wiki.gentoo.org/wiki/Framebuffer "Framebuffer") devices, it will be [/dev/fb1], \...

### [X driver]

For X11 drivers, [[[x11-drivers/xf86-video-fbdev]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-fbdev)[]]:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* fbdev

After setting or altering `VIDEO_CARDS` values remember to update the system using the following command so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [One X server]

TODO

## [Two X server]

This method is failsafe and should work with any graphics card installed. Start two instances of [X server](https://wiki.gentoo.org/wiki/X_server "X server") for each device and then use a software called [x2x] to move the input devices between them.

-   two independent instances and desktops
-   Input devices follow the mouse pointer

### [Software]

For this method, another input device driver called [[[x11-drivers/xf86-input-void]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-void)[]] is necessary:

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: void

\

`root `[`#`]`emerge --ask --changed-use --deep @world`

Also install [[[x11-misc/x2x]](https://packages.gentoo.org/packages/x11-misc/x2x)[]]:

`root `[`#`]`emerge --ask x11-misc/x2x`

### [xorg.conf.DL]

Configure two independent [xorg.confs](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf") for each device and initialize the desktop using [\~/.xinitrc] scripts.

** Note**\
Checking other xorg.conf files (including files in [/etc/X11/xorg.conf.d/]) may be necessary for any overlap in various names used. See the Discussion page for details.

Create the file [/etc/X11/xorg.conf.DL]:

[FILE] **`/etc/X11/xorg.conf.DL`**

    Section "Device"
        Identifier "DisplayLinkDevice"
        driver "fbdev"
        Option "fbdev" "/dev/fb0"    # You have to use the correct framebuffer device here
    EndSection

    Section "Monitor"
        Identifier "DisplayLinkMonitor"
    EndSection

    Section "Screen"
        Identifier "Default Screen"
        Device "DisplayLinkDevice"
        Monitor "DisplayLinkMonitor"
        SubSection "Display"
            Depth 16         # 24bit works fine but for USB 2.0 a lot of data
            Modes "1280x1024"
        EndSubSection
    EndSection

    Section "ServerLayout"
        Identifier "Server Layout"
        Screen 0 "Default Screen" 0 0
        Option "AllowMouseOpenFail" "True"
        InputDevice "Keyboard0" "CoreKeyboard"
        InputDevice "Mouse0" "CorePointer"
    EndSection

    Section "ServerFlags"
        Option "AllowEmptyInput" "false"
        Option "AutoAddDevices" "false"
        Option "AutoEnableDevices" "false"
    EndSection

    Section "InputDevice"
        Identifier "Keyboard0"
        Driver "void"
    EndSection

    Section "InputDevice"
        Identifier "Mouse0"
        Driver "void"
    EndSection

### [.xinitrc2]

Next, create the [\~/.xinitrc2] for the external display. Create and customize the file to as needed, here is an example:

** Note**\
DPMS is turned off, because I once had trouble to wake up the monitor again.

[FILE] **`~/.xinitrc2`**

    # DPMS stuff
    ## turn on monitor
    xset dpms force on
    ## disable sleep modes etc.
    xset -dpms
    ## disable screensaver
    xset s off

    # turn off beep
    xset -b

    # activate zapping (ctrl+alt+Bksp killall X)
    setxkbmap -option terminate:ctrl_alt_bksp

    # Set the background using feh
    feh --bg-scale /usr/share/slim/themes/capernoited/background.jpg

    # compositoring
    xcompmgr -c -t-5 -l-5 -r4.2 -o.55 &

    # start programs
    wicd-client &
    mrxvt &
    # start the actual window manager
    exec /usr/bin/awesome

### [displaylink.sh]

This is the actual script that starts the second instance of X server. Make it executable and save it somewhere in your home folder, in this example we save it to [\~/.displaylink.sh]:

[FILE] **`~/.displaylink.sh`**

    #!/bin/sh
    xinit ~/.xinitrc2 -- /usr/bin/X :1 -xf86config xorg.conf.DL -novtswitch -sharevts -audit 0 -layout "Screen Layout" vt12 &
    sleep 5
    x2x -west -from :0 -to :1 &

** Note**\
If you call this script to your actual [\~/.xinitrc] (which is executed on every start of X) or add it to [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME"), [KDE](https://wiki.gentoo.org/wiki/KDE "KDE"), etc. autostart, it will automatically initialize the second desktop for you. If the second screen is not attached, it just fails to do so.

** Note**\
If your system has a [/etc/X11/xorg.conf.d/], most likely you will need to start with the above -layout option so the X11 server being started will start properly. See the discussion.

## [DisplayLink 4-in-1 Adapter]

It is a USB 3.0 adapter comes with 4 ports:

-   One USB 3.0 port
-   One Ethernet port
-   One HDMI port
-   One VGA port

The USB 3.0 port should work if you already have USB 3.0 related kernel configured. To get the Ethernet port work, you need to activate the following kernel options：

[KERNEL]

    Device Drivers --->
        <*> Network device support --->
            <*> USB Network Adapters --->
            -M- CDC NCM support
            <M> CDC MBIM support

The Ethernet port will be seen as **usb0** network device.

## [External resources]

-   [libdlo freedesktop.org](http://libdlo.freedesktop.org/wiki/)
-   [Linux Forum displaylink.org](http://displaylink.org/forum/forumdisplay.php?f=29)
-   [Linux plugable.com](http://plugable.com/category/linux/)
-   [Setting up Multiseat plugable.com](http://plugable.com/2009/11/16/setting-up-usb-multiseat-with-displaylink-on-linux-gdm-up-to-2-20/)