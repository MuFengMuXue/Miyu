[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ASUS_Zenbook_Pro_UX501VW&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.asus.com/us/Notebooks/ASUS-ZenBook-Pro-UX501VW)

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Xorg]](#Xorg)

## [Installation]

### [Kernel]

[KERNEL] **Linux 4.10 touchpad and touchscreen support**

    Device Drivers --->
     Input device support --->
      [*] Mice --->
       <*> ELAN I2C Touchpad support
        [*] Enable I2C support
        [*] Enable SMbus support
      [*] Touchscreens --->
       <*> USB Touchscreen Driver
        [*] (All devices selected)

     I2C support --->
      [*] I2C support
      I2C Hardware Bus support --->
       <*> (I selected all Intel options)
       <*> Synopsys DesignWare Platform
       <*> Synopsys DesignWare PCI
       [*] Intel Baytrail I2C semaphore support

[KERNEL] **Linux 4.10 wifi support**

    Device Drivers --->
     [*] Network device support --->
      [*] Wireless LAN --->
       [*] Intel devices
        <*/M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
         <*/M> Intel Wireless WiFi MVM Firmware support

## [Configuration]

### [Xorg]

For proper input, video, and high DPI support on the 3840x2160 screen:

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965 nouveau

Create a xorg configuration file to set the monitor size in millimeters (these values were quickly and crudely calculated; you may want to measure your own):

[FILE] **`/etc/X11/xorg.conf.d/90-hidpi.conf`**

    Section "Monitor"
        Identifier  "<default monitor>"
        DisplaySize 342 193
    EndSection

If not using GNOME or some other software which manages Xresources and DPI for you, you will need to specify the DPI:

[FILE] **`~/.Xresources`**

    Xft.dpi: 240

And you will need this line in someplace like [\~/.xinitrc] or [\~/.xsession] (depending on your configuration) in order to apply the Xresources file:

[FILE] **`~/.xinitrc`**

    xrdb -merge ~/.Xresources

Other applications may handle high DPI weirdly. The [Arch wiki page on High DPI](https://wiki.archlinux.org/index.php/HiDPI) has many helpful hints.