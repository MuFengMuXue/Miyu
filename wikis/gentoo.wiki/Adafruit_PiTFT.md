Adafruit Industries produces whole series of resistive and capacitance touchscreens displays suited for all generations of Raspberry Pi computers^[\[1\]](#cite_note-1)^. Original PiTFT 2.8\" and PiTFT 3.5\" screens fit on Raspberry Pi\'s A and B and overhang slightly over the USB-ports on more modern versions. 2x20 GPIO pins adapted PiTFT Plus 2.8\" and 3.5\" do not have this problem, however, they cannot be used with *classical* A and B models with 2x13 GPIO pins^[\[2\]](#cite_note-2)^. 2.8\" and 3.5\" versions have 320x240 and 480x320 screen resolution, respectively; 2.8\" model features additional GPIO-connected ports, which could be fit e.g. with hardware buttons. The screen resolutions available may be not enough for modern DE, however, the touchscreen can be used for some simple mini monitor with framebuffer console or even X11 output (e.g. conky).

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Hardware and config.txt]](#Hardware_and_config.txt)
-   [[3] [Configuring the kernel]](#Configuring_the_kernel)
-   [[4] [Framebuffer console set-up]](#Framebuffer_console_set-up)
-   [[5] [UDEV configuration]](#UDEV_configuration)
-   [[6] [X11 configuration]](#X11_configuration)
-   [[7] [fbcp]](#fbcp)
-   [[8] [References]](#References)

## [Overview]

Adafruit provides extensive installation instructions via the python [adafruit-pitft.py]^[\[3\]](#cite_note-3)^. It is highly recommended to look through these instructions in case of any questions and further information. These instructions also cover not only 2.8\" and 3.5\" models, but the whole variety of the **other** Adafruit models, such as PiTFT 2.2\", miniPiTFT 1.14\", 1.3\", 1.54\", etc. However, the script adapted for Raspbian/Raspberry Pi OS does not work well under Gentoo. Following instructions are written based on the above mentioned script and this slightly outdated text.^[\[4\]](#cite_note-4)^ and tested on Raspberry Pi B and PiTFT 2.8\" resistive screen. Still these instructions keep certain amount of generality and *should* work with the other models.

Installation consists of the following steps:

1.  Enabling hardware configuration in [/boot/config.txt].
2.  Checking kernel configuration and modules as well as the proper command line options.
3.  Console configuration.
4.  X11 configuration.

## [Hardware and config.txt]

Raspberry Pi kernels and firmware use a Device Tree (DT) and DT overlays to describe and configure the hardware present in the Pi board as well as the external hardware.

The PiTFT screen uses the hardware I2C Pins (SDA & SCL), SPI pins (SCK, MOSI, MISO, CE0) as well as GPIO #25 and #24. Additionally 2.8\" version can use GPIO #18, #21-23 (or #27 instead of #21 on all newer models) for the hardware buttons, and 2.8\" Plus version occupies GPIO #17, #22, #23, #27 for the same purpose instead. All other GPIO contacts remain unused.

The list of the DT for the screens and options for them can be found in [/boot/overlays/README] by searching *Adafruit*. Important options are screen rotation angle `rotate` and frame rate `fps`. Rotation angle `rotate=90` will align the \"horizontal\" axis of the screen along the wide side.

By default Raspberry Pi will start using its HDMI interface for the video output on boot and PiTFT screen will become \"secondary\". To use solely PiTFT screen one should disable HDMI hotplug and set the maximum number of created framebuffers to 1. Additionally the output to PiTFT should be configured to 320x240 and 60Hz (or different supported depending on the screen) via `hdmi_cvt` option.

Last but not least is a choice of used graphics output. Raspberry Pi have in general 3 options: Legacy (default, when no DT overlay is used), \"fake\" and \"real\" KMS (with DTs such as [vc4-fkms-v3d]). Technical differences between those choice are beyond the scope of this instruction, one just should note, that `dtoverlay=vc4-kms-v3d` resulted in booting failure. This may not be the case though for the screens which have DRM support e.g. Adafruit 2.4\" and 3.5\".

Keeping in mind all above the [/boot/config.txt] file should contain following lines in *addition* to the ones present:

[FILE] **`/boot/config.txt`**

    ## --- Adafruit PiTFT configuration ---
    ## enabling required interfaces
    dtparam=i2c_arm=on
    dtparam=spi=on

    ## enabling the PiTFT screen itself
    dtoverlay=pitft28-resistive,rotate=90,fps=60

    ## Choice of the graphical stack: fake KMS
    dtoverlay=vc4-fkms-v3d

    ## configuring HDMI output
    hdmi_force_hotplug=0
    hdmi_group=2
    hdmi_mode=87
    hdmi_cvt=320 240 60 1 0 0 0
    max_framebuffers=1

## [Configuring the kernel]

Raspberry Pi kernel distribution^[\[5\]](#cite_note-5)^ already has necessary module pre-compiled. Alternatively, using default kernel configuration `bcmrpi_defconfig`, `bcm2709_defconfig`, `bcm2711_defconfig` for the appropriate target will select necessary modules. Otherwise check if you have these modules selected. The chip model is also written on the backside of some PiTFTs.

[KERNEL] **Enabling appropriate modules**

    Device Drivers --->
      Graphics support --->
        <M> DRM support for HX8357D display panels
        <M> DRM support for ILI9225 display panels
        <M> DRM support for ILI9341 display panels
        <M> DRM support for Sitronix ST7715R/ST7735R display panels
      Staging drivers --->
        <M>  Support for small TFT LCD display modules --->
            (Choose either all there or just yours)

## [Framebuffer console set-up]

Append `fbcon=map:10 fbcon=font:VGA8x8` to kernel command line either during build time or to the file [/boot/cmdline.txt].

[FILE] **`/boot/config.txt`**

    fbcon=map:10 fbcon=font:VGA8x8

A good idea is to use `consolefont` service to change console font during system boot. Choose console font and size, e.g [[[media-fonts/terminus-font]](https://packages.gentoo.org/packages/media-fonts/terminus-font)[]] 12 pt.

[FILE] **`/etc/conf.d/consolefont`**

    consolefont="ter-v12n"

Add `consolefont` service to the boot sequence:

`root `[`#`]`rc-update add consolefont boot`

When working with the Raspberry Pi remotely, e.g. via ssh, one can check if framebuffer works correctly with [[[media-gfx/fim]](https://packages.gentoo.org/packages/media-gfx/fim)[]] of fbi part of [[[media-gfx/fbida]](https://packages.gentoo.org/packages/media-gfx/fbida)[]] package.

`user `[`$`]`fbi --device /dev/fb0 <yourimage.png>`

or

`user `[`$`]`fim --device /dev/fb0 <yourimage.png>`

where [/dev/fb0] should be changed to e.g. [/dev/fb1] if HDMI is connected.

## [UDEV configuration]

The installation script suggests creating following files, so the link [/dev/input/touchscreen] to [/dev/eventN] of the PiTFT is created. This is required for the touchscreen functionality.

[FILE] **`/etc/udev/rules.d/95-touchmouse.rules`**

    SUBSYSTEM=="input", ATTRS=="touchmouse", ENV=="*event*", SYMLINK+="input/touchscreen"

[FILE] **`/etc/udev/rules.d/95-ftcaptouch.rules`**

    SUBSYSTEM=="input", ATTRS=="EP0110M09", ENV=="*event*", SYMLINK+="input/touchscreen"
    SUBSYSTEM=="input", ATTRS=="generic ft5x06*", ENV=="*event*", SYMLINK+="input/touchscreen"

[FILE] **`/etc/udev/rules.d/95-stmpe.rules"`**

    SUBSYSTEM=="input", ATTRS=="*stmpe*", ENV=="*event*", SYMLINK+="input/touchscreen"

## [X11 configuration]

Following files should be created to configure PiTFT with X11 system. First one ensures that /dev/fbX is attached to X-server with fbdev driver, as it seems not to work automatically.

[FILE] **`/etc/X11/xorg.conf.d/98-PiTFT.conf`**

    Section "Device"
        Identifier "PiTFT"
        Driver "fbdev"
        Option "fbdev" "/dev/fb0" #change fb0 to your framebuffer device!
    #   Option "ShadowFB" "false"
    EndSection

    Section "ServerFlags"
        Option "BlankTime" "0"
        Option "StandbyTime" "0"
        Option "SuspendTime" "0"
        Option "OffTime" "0"
    EndSection

Second file provides the calibration for the PiTFT as a touchscreen.

[FILE] **`/etc/X11/xorg.conf.d/99-calibration.conf`**

    Section "InputClass"
       Identifier      "calibration"
       MatchProduct    "stmpe-ts"
       MatchDevicePath "/dev/input/event0"
    # The following line can found in the installation script for your TFT and rotation.
    # Here it matches PiTFT 2.8" and 90 degrees rotation.
       Option "TransformationMatrix"   "0.014773 -1.132874 1.033662 1.118701 0.009656 -0.065273 0 0 1"
       Option  "SwapAxes"      "1"
    # The following options should allow right click emulation with a long touch on PiTFT.
       Option "EmulateThirdButton" "1"
       Option "EmulateThirdButtonTimeout" "750"
       Option "EmulateThirdButtonMoveThreshold" "30"
    EndSection

## [fbcp]

All configuration above considers mainly setting up a framebuffer display separate from HDMI-connected display. However, the PiTFT is not GPU-accelerated (e.g. DRI2 is not working), so all 3D graphics is drawn by CPU, it is much slower compared to GPU-accelerated. The solution suggested by Adafruit is to copy HDMI output to framebuffer device via framebuffer copy utility (*fbcp*)^[\[6\]](#cite_note-6)^. Unfortunately, this part is currently beyond scope of this article.

## [References]

1.  [[[↑](#cite_ref-1)] [[\[1\]](https://www.adafruit.com/category/804) Some of Adafruit touchscreen products.]]
2.  [[[↑](#cite_ref-2)] [[\[2\]](https://www.adafruit.com/product/1601), [\[3\]](https://www.adafruit.com/product/2298) E.g. compare Adafruit PiTFT 2.8\" and PiTFT Plus 2.8\" screens, respectively.]]
3.  [[[↑](#cite_ref-3)] [[\[4\]](https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/easy-install-2), [\[5\]](https://learn.adafruit.com/adafruit-pitft-3-dot-5-touch-screen-for-raspberry-pi?view=all), [\[6\]](https://github.com/adafruit/Raspberry-Pi-Installer-Scripts) Adafruit PiTFT Easy install instructions and the scripts GitHub repository.]]
4.  [[[↑](#cite_ref-4)] [[\[7\]](https://www.vctlabs.com/posts/2014/Oct/22/pitft_kernel/) VCT labs instructions]]
5.  [[[↑](#cite_ref-5)] [[\[8\]](https://github.com/raspberrypi/firmware) Official Raspberry Pi repository containing pre-compiled binaries of the kernel and modules and more.]]
6.  [[[↑](#cite_ref-6)] [[\[9\]](https://github.com/adafruit/rpi-fbcp) RPI framebuffer copy utility]]