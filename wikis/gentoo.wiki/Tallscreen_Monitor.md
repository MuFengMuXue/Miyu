Do vertically scrolling texts and images look lame on your widescreen monitor? Then rotate it!

## [Frame buffer or modesetting rotation]

Support for framebuffer rotation must be enabled in the kernel (this is not required for rotation using Xorg).

[KERNEL] **Tallscreen related kernel modifications**

    Device Drivers  --->
        Graphics support  --->
            Console display driver support  --->
                [*] Framebuffer Console Rotation

The `fbcon` kernel boot option is used to rotate the kernel frame buffer at boot time.

[FILE] **`/usr/src/linux/Documentation/fb/fbcon.txt`**

    fbcon=rotate:<n>

           This option changes the orientation angle of the console display. The
           value 'n' accepts the following:

                 0 - normal orientation (0 degree)
                 1 - clockwise orientation (90 degrees)
                 2 - upside down orientation (180 degrees)
                 3 - counterclockwise orientation (270 degrees)

If you wish to rotate your display to the right and are using GRUB-0, append the option `fbcon=rotate:1` to the `kernel` lines in [/boot/grub/grub.cfg]

To perform the same rotation with GRUB2, append `fbcon=rotate:1` to the `GRUB_CMDLINE_LINUX` variable in [/etc/default/grub] and execute the [grub-mkconfig] command:

`root `[`#`]`grub-mkconfig -o /boot/grub2/grub.cfg`

The screen should be reoriented on the next boot, assuming the kernel has been compiled with rotation support.

## [Xorg rotation]

[xrandr] ([[[x11-apps/xrandr]](https://packages.gentoo.org/packages/x11-apps/xrandr)[]]) can rotate Xorg output at runtime, but the best practice is to rotate the display when Xorg is initialized and before anything is rendered.

First determine the name of you display output by running [xrandr] while Xorg is active. Look for a line like *HDMI1 connected\...*.

Then add a `Rotate` option to the monitor section of [40-monitor.conf] configuration file:

[FILE] **`/etc/X11/xorg.conf.d/40-monitor.conf`Tallscreen related Xorg modifications**

    Section "Monitor"
        # This identifier would be the same as the name
        # of the connector printed by xrander.
        Identifier  "VGA1"
        Option      "Rotate"  "right"

        Option  "PreferredMode"   "1920x1080"
        # A line such as this ^ may be necesary if you
        # are not getting your prefered resolution.
        # These numbers need not be reversed with tallscreen orientation.
    EndSection

Xorg should now rotate the screen at X startup.

The author of this article uses tallscreen monitors whenever possible, but also uses a tiling window manager. Results may vary with other desktop environments.