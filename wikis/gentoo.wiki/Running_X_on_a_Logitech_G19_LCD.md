[The Logitech G19](https://en.wikipedia.org/wiki/Logitech_G19 "wikipedia:Logitech G19") keyboard is a gaming keyboard that has extra keys and a built-in LCD color display. Its display is small and its resolution is rather low (320x240 pixels), but it\'s enough to do a lot of useful and cool things, considering it\'s connected with USB 2.0.

The following instructions describe the installation of the kernel driver and the setup of a secondary X server. While it should be possible to use an existing X server to handle the G19 LCD in addition to standard screen(s), there are advantages on using a separate X server. For example, a user can start/stop/restart the G19 X while your main X is running.

## Contents

-   [[1] [Kernel Preparation]](#Kernel_Preparation)
-   [[2] [Installing the lg4l driver]](#Installing_the_lg4l_driver)
-   [[3] [Installing fbdev]](#Installing_fbdev)
-   [[4] [After rebooting]](#After_rebooting)
-   [[5] [Secondary X server]](#Secondary_X_server)
    -   [[5.1] [xorg.conf.g19]](#xorg.conf.g19)
    -   [[5.2] [.xinitrc2]](#.xinitrc2)
    -   [[5.3] [g19lcd.sh]](#g19lcd.sh)

## [Kernel Preparation]

The official linux kernel does not have support for the G19 yet. However, a working driver is available from github:

`user `[`$`]`git clone `[`https://github.com/CMoH/lg4l.git`](https://github.com/CMoH/lg4l.git)

But before installing it make sure the kernel has CONFIG_FB_DEFERRED_IO set. If it is already set, this part can be skipped.

`user `[`$`]`grep CONFIG_FB_DEFERRED_IO /usr/src/linux/.config`

    CONFIG_FB_DEFERRED_IO}y

There isn\'t a way to directly set this from the kernel menuconfig, but it can be enabling by something that selects it:

[KERNEL]

    Device Drivers --->
        HID Devices (HID_SUPPORT [=y]) --->
           Special HID drivers --->
              <M> PicoLCD (graphic version)

Please note this driver isn\'t really needed, it\'s just a hackish way to select CONFIG_FB_DEFERRED_IO through menuconfig. If a better way is known, please add it here.

Now, compile the new kernel image and install it. Making just the modules isn\'t enough as CONFIG_FB_DEFERRED_IO option changed. Don\'t reboot yet.

## [Installing the lg4l driver]

`user `[`$`]`cd lg4l `

`user `[`$`]`make `

`user `[`$`]`su -c "make install"`

If CONFIG_FB_DEFERRED_IO is not set as described above, there will be an error while compiling. If everything is OK, move on.

## [Installing fbdev]

[[[x11-drivers/xf86-video-fbdev]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-fbdev)[]] is required to run X later:

`root `[`#`]`emerge --ask -uv xf86-video-fbdev`

You may now reboot.

## [After rebooting]

As per the lg4l README:

`root `[`#`]`modprobe hid-g19`

but the device will still be grabbed by the generic driver. Running:

`root `[`#`]`./rebind`

located in the lg4l source tree to put the new module in control of the device (consider automating this).

## [Secondary X server]

The following method is based on the [DisplayLink](https://wiki.gentoo.org/wiki/DisplayLink "DisplayLink") wiki page. In it, it says you need [[[x11-drivers/xf86-input-void]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-void)[]] to make it work but I haven\'t installed it and it all works fine. If it doesn\'t work, follow the instructions on the [DisplayLink](https://wiki.gentoo.org/wiki/DisplayLink "DisplayLink") page.

To switch keyboard/mouse focus to the LCD screen, you will need x2x. Expert users who plan to just open apps in the G19 LCD won\'t need x2x.

`root `[`#`]`emerge --ask -uv x11-misc/x2x`

#### [xorg.conf.g19]

Create this file in /etc/X11/ and name it xorg.conf.g19:

[FILE] **`/etc/X11/xorg.conf.g19`**

    Section "Device"
        Identifier     "g19lcd"
        Driver         "fbdev"
        VendorName     "Logitech"
        BusID          "USB"
        Option         "fbdev" "/dev/fb0"
        Screen         0
    EndSection

    Section "Monitor"
        Identifier     "G19monitor"
        VendorName     "Logitech"
        ModelName      "Logitech G19"
    EndSection

    Section "Screen"
        Identifier     "Screen0"
        Device         "g19lcd"
        Monitor        "G19monitor"
        DefaultDepth   16
        SubSection     "Display"
            Depth      16
            Modes      "320x240"
        EndSubSection
    EndSection

    Section "ServerLayout"
        Identifier     "Layout0"
        Screen      0  "Screen0" 0 0
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

#### [.xinitrc2]

Next create the \~/.initrc2 for the G19 display. Create and customize the file as needed, here is an example:

[FILE] **`~/.xinitrc2`**

    # run profile to set $PATH and other env vars correctly
    . $/.bash_profile

    ## turn on display
    xset dpms force on

    ## disable sleep modes etc.
    xset -dpms

    ## disable screensaver
    xset s off

    ## turn off beep
    xset -b

    xset r rate 250 30

    ## activate zapping (ctrl+alt+Bksp killall X)
    setxkbmap -option terminate:ctrl_alt_bksp

    # run initial programs
    uxterm -ls -geometry 200x62+0+162 -fg white -bg black &
    exec icewm || exec xterm -fg red

Please note the commands there will only affect the G19 display, not the main X.

#### [g19lcd.sh]

This is the actual script that starts the second instance of xorg-server. Make it executable and save it somewhere accessible:

[FILE] **`~/.g19lcd.sh`**

    #!/bin/sh
    xinit ~/.xinitrc2 -- /usr/bin/X :1 -xf86config xorg.conf.g19 -novtswitch -sharevts -audit 0 vt12 &
    sleep 5
    x2x -west -from :0 -to :1 &