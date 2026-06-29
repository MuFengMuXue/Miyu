** Note**\
The Trident driver may no longer be available in the Gentoo ebuild repository, see [[[bug #606132]](https://bugs.gentoo.org/show_bug.cgi?id=606132)[]]. See [Talk:Trident](https://wiki.gentoo.org/wiki/Talk:Trident "Talk:Trident") for notes on compiling the driver from source.

**trident** is the open source graphics drivers for [Trident](https://en.wikipedia.org/wiki/Trident_Microsystems "wikipedia:Trident Microsystems") graphics cards.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Firmware]](#Firmware)
    -   [[1.3] [Driver]](#Driver)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Permissions]](#Permissions)
    -   [[2.2] [xorg.conf]](#xorg.conf)
    -   [[2.3] [Framebuffer (GRUB or LILO)]](#Framebuffer_.28GRUB_or_LILO.29)
-   [[3] [Documentation]](#Documentation)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

You need to activate the following kernel options:

[KERNEL]

    Processor type and features  --->
        [*] MTRR (Memory Type Range Register) support
    Device Drivers  --->
        Graphics support  --->

            If your card sits in an AGP slot, choose your AGP driver:
            (Note: ALI chipsets are typically bundled with Trident graphics cards in laptops)
            <*> /dev/agpgart (AGP Support)  --->
                <*> ALI chipset support

            <*> Support for frame buffer devices  --->
                [*] Enable firmware EDID
                [*] VESA VGA graphics support
                <*> Trident/CyberXXX/CyberBlade support

### [Firmware]

Unknown IRQ microcode needed for Trident graphics support at this time, since the Kernel driver (tridentfb) should support most functions for Trident cards.

[[[x11-drivers/xf86-video-trident]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-trident)[]] is an old video card and old driver. It has no corresponding KMS (Kernel ModeSetting), at least in recent (3.12.21) kernels. Although in some distros (AFAIK Fedora 21) such drivers were removed, to my experience it works without KMS. At least with =x11-base/xorg-server-1.15.0.

Make sure firmware for your model (check available ones in [/lib/firmware/trident]) is included in kernel:

[KERNEL] **Including trident firmware**

    Device Drivers  --->
        -*- Userspace firmware loading support
        [*] Include in-kernel firmware blobs in kernel binary
            (trident/<YOUR-MODEL>.bin)
            (/lib/firmware) Firmware blobs root directory

Below is a list of the firmware files needed for each family of cards:

No known firmware files are needed for any particular Trident card at this time.

### [Driver]

[FILE] **`/etc/portage/make.conf`Set `VIDEO_CARDS` to trident**

    VIDEO_CARDS="... trident ..."

After setting or altering `VIDEO_CARDS` values remember to update the system using the following command so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [Configuration]

### [Permissions]

If the [`acl`](https://packages.gentoo.org/useflags/acl) USE flag is enabled globally and [`elogind`](https://packages.gentoo.org/useflags/elogind) is being used (default for desktop profiles) permissions to video cards will be handled automatically. It is possible to check the permissions using [getfacl]:

`user `[`$`]`getfacl /dev/dri/card0 | grep larry`

`user:`**`larry`**`:rw-`

A broader solution is to add the user(s) needing access the video card to the [video] group:

`root `[`#`]`gpasswd -a larry video`

Note that users will be able to run X without permission to the DRI subsystem, but hardware acceleration will be disabled.

### [xorg.conf]

The [X server](https://wiki.gentoo.org/wiki/X_server "X server") is designed to work out-of-the-box, with no need to manually edit X.Org\'s configuration files. It should detect and configure devices such as displays, keyboards, and mice.

However, the main configuration file of the X server is the [xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf").

You can force the X server to use desired driver with:

[FILE] **`/etc/X11/xorg.conf.d/trident.conf`Explicit trident driver section**

    Section "Device"
       Identifier  "trident"
       Driver      "trident"
    EndSection

To my experience quoted config don\'t works. Last error message in [Xorg.log] is:

    [   218.176] (II) Loading sub module "xaa"
    [   218.176] (II) LoadModule: "xaa"
    [   218.177] (WW) Warning, couldn't open module xaa
    [   218.178] (II) UnloadModule: "xaa"
    [   218.178] (II) Unloading xaa
    [   218.178] (EE) TRIDENT: Failed to load module "xaa" (module does not exist, 0)

Adding to [trident.conf] the option:

[FILE] **`/etc/X11/xorg.conf.d/trident.conf`**

    Option       "AccelMethod" "EXA"

makes xorg server operable.

### [][Framebuffer (GRUB or LILO)]

[CODE]

    video=tridentfb:1024x768-16@60

## [Documentation]

Full Documentation can be found under [/usr/src/linux/Documentation/fb/tridentfb.txt].

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=xf86-video-trident&order=bug_id%20DESC)[]]
-   [[[Freedesktop.org bugtracker: known bugs]](https://bugs.freedesktop.org/buglist.cgi?quicksearch=xf86-video-trident&order=bug_id%20DESC)[]]

## [External resources]

-   [X.Org Wiki](http://wiki.x.org/wiki/trident)