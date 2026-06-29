This page contains [[changes](https://wiki.gentoo.org/index.php?title=Mdev&oldid=1400000&diff=1423129)] which are not marked for translation.

Other languages:

-   [English]
-   [italiano](https://wiki.gentoo.org/wiki/Mdev/it "Mdev (85% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Mdev/hu "mdev (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Mdev/ru "mdev (43% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Mdev/zh-cn "Mdev (7% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Mdev/ja "mdev (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Mdev/ko "mdev/ko (80% translated)")

This article documents how to replace udev in Linux with mdev, thus allowing a separate [/usr] partition, without an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). The author uses Gentoo Linux with IceWM as the window manager. The instructions here should be, with some small adjustments, applicable to other distributions.

**mdev** is a udev replacement from [Busybox](https://wiki.gentoo.org/wiki/Busybox "Busybox"), it populates and updates [/dev] ([official docs](https://git.busybox.net/busybox/plain/docs/mdev.txt)). Replacing [eudev](https://wiki.gentoo.org/wiki/Eudev "Eudev") or [udev](https://wiki.gentoo.org/wiki/Udev "Udev") is non-trivial, and is probably most adapted to embedded systems.

## Contents

-   [[1] [Will mdev work on my system?]](#Will_mdev_work_on_my_system.3F)
    -   [[1.1] [Sanity check]](#Sanity_check)
-   [[2] [Replacing udev with mdev]](#Replacing_udev_with_mdev)
    -   [[2.1] [Setting up the kernel for devtmpfs]](#Setting_up_the_kernel_for_devtmpfs)
    -   [[2.2] [Emerging busybox]](#Emerging_busybox)
    -   [[2.3] [Mounting devpts]](#Mounting_devpts)
    -   [[2.4] [Replace the udev service]](#Replace_the_udev_service)
    -   [[2.5] [Reboot]](#Reboot)
    -   [[2.6] [Cleanup]](#Cleanup)
-   [[3] [Setting up a USB printer running under CUPS]](#Setting_up_a_USB_printer_running_under_CUPS)
    -   [[3.1] [Make \'find\' available at early boot-time]](#Make_.27find.27_available_at_early_boot-time)
    -   [[3.2] [Rebuild the kernel]](#Rebuild_the_kernel)
    -   [[3.3] [Configure the new kernel into the bootloader and reboot into it]](#Configure_the_new_kernel_into_the_bootloader_and_reboot_into_it)
    -   [[3.4] [Verify the presence of the new device nodes]](#Verify_the_presence_of_the_new_device_nodes)
    -   [[3.5] [Configure the printer in CUPS]](#Configure_the_printer_in_CUPS)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Linux modules missing at boot sequence]](#Linux_modules_missing_at_boot_sequence)
-   [[5] [Miscellaneous]](#Miscellaneous)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [][Will mdev work on my system?]

The [mdev] application is definitely suitable as long as the system does not use a full-fledged desktop environment. Note that a desktop environment is not required to run AbiWord, Firefox, GIMP, Gnumeric, etc. However, KOffice applications like KMail seem to pull in most of KDE as a dependency. In general, when using KDE or GNOME, [mdev] is not suitable. Also using [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") might be troublesome.

It will work very well when using the default Gentoo profiles:

-   *default/linux/x86/13.0*
-   *default/linux/amd64/13.0*

List the currently used profile by using following command:

`user `[`$`]`eselect profile list`

    Current /etc/portage/make.profile symlink:
      default/linux/amd64/13.0

** Note**\
Recent versions of evdev (as provided through [[[x11-drivers/xf86-input-evdev]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-evdev)[]]) and [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]] require udev. They will not build without it.

There is one more sanity check that Gentoo users can run to check for udev dependency.

### [Sanity check]

Get a general overview which packages might depend on udev. The output could look similar to the one shown below:

`user `[`$`]`equery d udev`

     * These packages depend on udev:
    media-libs/mesa-9.0.1 (gbm ? virtual/udev)
    sys-apps/hwids-20130329 (udev ? >=virtual/udev-197-r1)
    sys-apps/util-linux-2.22.2 (udev ? virtual/udev)
    virtual/dev-manager-0 (virtual/udev)
    x11-base/xorg-server-1.13.4 (udev ? >=virtual/udev-150)
    x11-drivers/xf86-video-intel-2.20.13 (udev ? virtual/udev)
    x11-libs/cairo-1.10.2-r3 (drm ? >=virtual/udev-136)

Add the following line to the [/etc/portage/package.mask] or [/etc/portage/package.mask/mdev] file (which can be created if it does not exist yet):

[FILE] **`/etc/portage/package.mask/mdev`Mask away udev**

    sys-fs/udev

Disable the `udev` USE flag globally in [/etc/portage/make.conf]:

`root `[`#`]`euse -D udev`

Rebuild all packages with the new `-udev` USE flag:

`root `[`#`]`emerge -uDNvp @world`

If the only error that comes up is that Portage is not able to re-install udev as required by [[[virtual/dev-manager]](https://packages.gentoo.org/packages/virtual/dev-manager)[]], proceed to the next stage. Otherwise, [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] might be an hard dependency of one or more packages installed on the system.

## [Replacing udev with mdev]

** Warning**\
This is a critical step which might result in a non-bootable Linux system. Only proceed if the above approach has not revealed any additional udev dependencies.

### [Setting up the kernel for devtmpfs]

Set up the kernel to support and automount a devtmpfs [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") at [/dev]:

[KERNEL] **Enabling devtmpfs**

    Device Drivers --->
        Generic Driver Options --->
            [*] Maintain a devtmpfs filesystem to mount at /dev
            [*] Automount devtmpfs at /dev, after the kernel mounted the rootfs

Once the changes have been made, rebuild the kernel. Do **NOT** reboot yet.

### [Emerging busybox]

Make sure that the `mdev` USE flag is set for [[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]]. The `static` USE flag is probably also a good idea. In the [/etc/portage/package.use] or [/etc/portage/package.use/mdev] file, add the following line:

[FILE] **`/etc/portage/package.use/mdev`**

    sys-apps/busybox static mdev

Now, (re)install busybox:

`root `[`#`]`emerge --ask --oneshot busybox`

### [Mounting devpts]

The devpts filesystem exhibits non-standard behavior. It does not automount, at bootup, or with [mount -a]. An explicit [mount devpts] command is required. The standard solution for udev-based systems is to run [rc-update add udev-mount sysinit] as root, and have the udev-mount script do the mounting at startup. An mdev-based system will probably not have udev installed. An alternative way to do this at bootup is to include the command [mount devpts] in a shell script in [/etc/local.d/]. In this example, the file will be named [/etc/local.d/000.start].

Another side-effect of not using udev-mount is that [/dev/shm] is only writable by root. The command [chmod 1777 /dev/shm] is required to restore the standard behavior. This command will also be run from the script at startup.

[FILE] **`/etc/local.d/000.start`Mount of devpts at bootup and change /dev/shm permissions**

    #!/bin/bash
    mount devpts
    chmod 1777 /dev/shm

** Note**\
Scripts used in [/etc/local.d/]

-   must be executable
-   must have the extension \".start\" in order to run at startup
-   must have the extension \".stop\" in order to run at shutdown

### [Replace the udev service]

Remove udev from the services list and replace it with mdev:

`root `[`#`]`rc-update del udev sysinit `

`root `[`#`]`rc-update add mdev sysinit `

### [Reboot]

Reboot to the new kernel. The system should now be running using mdev.

### [Cleanup]

Remove udev from the system:

`root `[`#`]`emerge --ask --depclean --verbose sys-fs/udev sys-fs/eudev`

In the [/etc/portage/package.mask] file (or a file in this directory), add [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] and [[[sys-fs/eudev]](https://packages.gentoo.org/packages/sys-fs/eudev)[]].

This now results in a completely udev-free machine.

## [Setting up a USB printer running under CUPS]

### [][Make \'find\' available at early boot-time]

`root `[`#`]`cd /bin `

`root `[`#`]`ln -s /bin/busybox find `

### [Rebuild the kernel]

For libusb (and hence CUPS) to see the USB ports, set `CONFIG_USB_DEVICE_CLASS=y` and `CONFIG_USB_DEVICEFS=y` in the kernel configuration. Also enable `CONFIG_USB_PRINTER=y`, despite the injunction in the cups-1.5.2 ebuild to disable it. When using [make menuconfig], these items are found here:

[KERNEL] **Enabling generation of USB devices at boot time**

    Device Drivers --->
        [*] Support for Host-side USB
          [*] USB device filesystem [DEPRECATED]
          [*] USB device class-devices [DEPRECATED]
        [*] USB Printer support

** Note**\
Don\'t worry about the deprecation warnings.

### [Configure the new kernel into the bootloader and reboot into it]

### [Verify the presence of the new device nodes]

A hierarchy of device nodes should be present under [/dev/bus/usb/]. When switching on the printer, a node for it should occur at [/dev/lp0]. [lsusb] should run successfully, and this should display the printer\'s details.

### [Configure the printer in CUPS]

Configure CUPS in the [usual way](https://wiki.gentoo.org/wiki/Printing "Printing"). CUPS should find the printer, and will give it a URI like [parallel:/dev/lp0].

## [Troubleshooting]

### [Linux modules missing at boot sequence]

If Linux modules are required and not loaded on boot after migration, execute one or more of the following solutions:

-   Add Linux modules to `*.conf` files in [/etc/modules-load.d/]

<!-- -->

-   Compile modules into the Linux kernel, without the need of loading them on demand.

<!-- -->

-   Write a custom module loader:

[FILE] **`/sbin/hotplug`**

    #!/bin/sh
    test -n "$MODALIAS" && modprobe "$MODALIAS";
    exec /sbin/mdev

Install it as the hotplug handler instead of mdev. Note that the earlier this gets executed, the better. Consider naming this script [/sbin/hotplug], since that is the default value of [/proc/sys/kernel/hotplug] (or change the default value in the kernel configuration).

## [Miscellaneous]

** Note**\
This set of instructions was originally written by Walter Dnes and hosted at his personal website. It was imported to the Gentoo wiki with some editing by [Michael Mol](https://wiki.gentoo.org/index.php?title=User:Short_Circuit&action=edit&redlink=1 "User:Short Circuit (page does not exist)") per discussion on the gentoo-user mailing list.

-   mdev unlike udev does not support auto-modules loading. Create files ending with `.conf` in [/etc/modules-load.d/] and put all the modules there that should be loaded (nvidia, wl, etc.) one per line. Customize options via files ending with `.conf` in [/etc/modprobe.d] (see [man 5 modprobe.d] for syntax). It might be necessary to move the module configuration to this location.

<!-- -->

-   [mdev -s] does not create [/dev/mapper] nodes. Either manually create them or use [dmsetup mknodes] from lvm2. It is a good idea to add it after [mdev -s] in the init script.

<!-- -->

-   Use mouse and keyboard drivers for xorg inputs. Evdev needs udev to be built. Mousedrv (for the mouse driver) may conflict with the synaptic driver when both are loaded.

<!-- -->

-   The Kernel configuration option `CONFIG_INPUT_EVDEV` not only provides the keyboard and mouse as input device events, it will provide lid and button events to acpid as well.

## [See also]

-   [Mdev/Automount USB‎](https://wiki.gentoo.org/wiki/Mdev/Automount_USB "Mdev/Automount USB") --- describes how to implement automounting of USB devices on a machine using mdev as the device manager.

## [External resources]

-   [mdev like a boss](https://github.com/slashbeast/mdev-like-a-boss) project.