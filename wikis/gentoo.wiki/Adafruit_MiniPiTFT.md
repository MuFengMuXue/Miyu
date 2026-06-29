[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Adafruit_MiniPiTFT&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**DRAFT / WIP**

Adafruit MiniPiTFT is a small, 240x135 or 240x240 pixels display with two additional buttons, designed for Raspberry Pi. Adafruit only provides a raspbian installer, so these steps are necessary to work on Gentoo.

This wiki entry has not yet been tested and contains some stuff pulled from the original install script and not yet translated for Gentoo.

This is a starting point for using the Adafruit MiniPiTFT display in python OR as a console.

Original source: [https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi/kernel-module-install](https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi/kernel-module-install)

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Kernel config]](#Kernel_config)
    -   [[1.2] [Software packages]](#Software_packages)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [disabling console blanking]](#disabling_console_blanking)

# [Prerequisites]

## [Kernel config]

correct kernel options should already be set ; in doubt, make sure you have

[KERNEL]

    CONFIG_FB_TFT_ST7789V=m

## [Software packages]

    # emerge dev-vcs/git
    # emerge media-fonts/terminus-font media-fonts/dejavu
    # emerge dev-python/wheel dev-python/numpy
    ## apt-get install python3-pil
    # pip install --user adafruit-python-shell
    # pip install --user click
    # pip install --user adafruit-circuitpython-rgb-display
    # pip install --upgrade --force-reinstall spidev
    ## echo "=media-libs/raspberrypi-userland-9999   **" >> /etc/portage/package.accept_keywords/rpi
    ## emerge media-libs/raspberrypi-userland
    # git clone https://github.com/adafruit/rpi-fbcp.git
    $ cd rpi-fbcp
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make
    # install fbcp /usr/local/bin/fbcp

original script also says:

    # apt-get install -y bc fbi git python3-dev python3-pip python3-smbus python3-spidev evtest libts-bin device-tree-compiler

and

    # dtc --warning no-unit_address_vs_reg -I dts -O dtb -o

at this point you should be able to get something displayed with [https://learn.adafruit.com/pages/17702/elements/3044300/download](https://learn.adafruit.com/pages/17702/elements/3044300/download)

# [Configuration]

it makes no sense to clone [https://github.com/adafruit/Raspberry-Pi-Installer-Scripts.git](https://github.com/adafruit/Raspberry-Pi-Installer-Scripts.git) ; instead :

The console font needs to be changed. For OpenRC:

[FILE] **`/etc/conf.d/consolefont`**

    consolefont="ter-u12n"

note: I have yet to find the 6x12 terminus font if that\'s not it.

add the correct options in [/boot/cmdline.txt]:

[FILE] **`/boot/cmdline.txt`**

    fbcon=map:10 fbcon=font:VGA8x8 BLANK_TIME=0

edit [/boot/config.txt]:

[FILE] **`/boot/config.txt`**

    hdmi_force_hotplug=1
    hdmi_group=2
    hdmi_mode=87
    #dtoverlay=vc4-fkms-v3d
    hdmi_cvt=WIDTH HEIGHT 60 1 0 0 0"
    hdmi_force_hotplug=1  # required for cases when HDMI is not plugged in!
    dtparam=spi=on
    dtparam=i2c1=on
    dtparam=i2c_arm=on

    overscan=0

`root `[`#`]`echo "/usr/local/bin/fbcp \&" > /etc/local.d/rpi-tft `

`root `[`#`]`chmod +x /etc/local.d/rpi-tft`

    [Unit]
    Description=Framebuffer copy utility for PiTFT
    After=network.target

    [Service]
    Type=simple
    ExecStartPre=/bin/sleep 10
    ExecStart=/usr/local/bin/fbcp

    [Install]
    WantedBy=multi-user.target

\

## [disabling console blanking]

TODO unless it was successful above