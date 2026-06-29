**Resources**

[[]][Home](http://www.freedesktop.org/wiki/Software/Plymouth/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Plymouth_(software) "wikipedia:Plymouth (software)")

[[]][GitWeb](https://gitlab.freedesktop.org/plymouth/plymouth)

**Plymouth** is a [bootsplash](https://en.wikipedia.org/wiki/bootsplash "wikipedia:bootsplash") used to show splash screens during system boot and shutdown.

Plymouth provides flicker-free animated boot splashes with support for progress bars, solar flares, and other nifty things. In addition to [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), it has full [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") support.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Bootup logo]](#Bootup_logo)
        -   [[1.1.2] [KMS for Intel cards]](#KMS_for_Intel_cards)
        -   [[1.1.3] [KMS for Nvidia cards (Nouveau drivers)]](#KMS_for_Nvidia_cards_.28Nouveau_drivers.29)
        -   [[1.1.4] [KMS for Nvidia cards (official drivers)]](#KMS_for_Nvidia_cards_.28official_drivers.29)
        -   [[1.1.5] [KMS for Radeon cards]](#KMS_for_Radeon_cards)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Building Initramfs]](#Building_Initramfs)
    -   [[3.1] [Initramfs Generators]](#Initramfs_Generators)
        -   [[3.1.1] [Dracut]](#Dracut)
    -   [[3.2] [Manual initramfs creation]](#Manual_initramfs_creation)
    -   [[3.3] [Init systems]](#Init_systems)
        -   [[3.3.1] [systemd]](#systemd)
        -   [[3.3.2] [OpenRC]](#OpenRC)
-   [[4] [Bootloaders]](#Bootloaders)
    -   [[4.1] [GRUB]](#GRUB)
-   [[5] [Themes]](#Themes)
    -   [[5.1] [Usage]](#Usage)
-   [[6] [Tips]](#Tips)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installation]

### [Kernel]

Specific kernel options must be altered in order to get Plymouth working properly. If you use a distribution kernel, you can continue to [installing Plymouth](#USE_flags).

#### [Bootup logo]

It is *highly* advised to **disable** the Linux bootup logo. On some systems having the bootup logo displayed seems to cause problems.

[KERNEL] **This example shows the correct way to disable the bootup logo:**

    Device Drivers --->
       Graphics Support --->
          [ ] Bootup logo  --->

** Important**\
Be sure to enable kernel modesetting (KMS) for the system\'s respective graphics card.

#### [KMS for Intel cards]

[KERNEL] **Intel onboard GPUs set to use modesetting:**

    Device Drivers --->
       Graphics Support --->
          <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
             <*>   Intel 8xx/9xx/G3x/G4x/HD Graphics
             [*]     Enable modesetting on intel by default

** Important**\
If this is the user\'s first time modifying settings for on-board Intel GPUs the [Intel article](https://wiki.gentoo.org/wiki/Intel "Intel") should be referenced for additional configuration.

#### [][KMS for Nvidia cards (Nouveau drivers)]

[KERNEL] **NVIDIAGPU set to use Nouveau:**

    Device Drivers  --->
        Graphics support  --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
                <*> Nouveau (nVidia) cards

** Important**\
If this is the user\'s first time changing settings for the NVIDIA graphics card using the nouveau driver be sure to reference the [nouveau article](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") for additional information.

#### [][KMS for Nvidia cards (official drivers)]

To use the official Nvidia drivers see the wiki\'s [official Nvidia-drivers article](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers").

** Note**\
So far the results of using official Nvidia-drivers are untested with Plymouth.

#### [KMS for Radeon cards]

[KERNEL] **Radeon GPU set to use modesetting:**

    Device Drivers --->
       [*] Staging drivers  --->
          [*]     Enable modesetting on radeon by default

** Important**\
If this is the user\'s first time setting up a Radeon graphics card be sure to reference the [radeon article](https://wiki.gentoo.org/wiki/Radeon "Radeon") for further information.

### [USE flags]

### [USE flags for] [sys-boot/plymouth](https://packages.gentoo.org/packages/sys-boot/plymouth) [[]] [Graphical boot animation (splash) and logger]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+drm`](https://packages.gentoo.org/useflags/+drm)                 Provides abstraction to the DRM drivers (intel, nouveau and vmwgfx at this moment)
  [`+gtk`](https://packages.gentoo.org/useflags/+gtk)                 Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`+pango`](https://packages.gentoo.org/useflags/+pango)             Adds support for printing text on splash screen and text prompts, e.g. for password
  [`+split-usr`](https://packages.gentoo.org/useflags/+split-usr)     Enable this if /bin and /usr/bin are separate directories
  [`+udev`](https://packages.gentoo.org/useflags/+udev)               Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`freetype`](https://packages.gentoo.org/useflags/freetype)         Build with freetype support (if enabled, used for encryption prompts)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-26 18:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

The [[[sys-boot/plymouth]](https://packages.gentoo.org/packages/sys-boot/plymouth)[]] package can be installed by running:

`root `[`#`]`emerge --ask sys-boot/plymouth`

## [Configuration]

[/etc/plymouth/plymouthd.conf] - the sole configuration file for Plymouth. It can be left untouched. Selecting theme is described in [further section](#Themes).

## [Building Initramfs]

Bootsplashes are loaded by [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") so they need to be included in it.

### [Initramfs Generators]

#### [Dracut]

[Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") ([[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]]) is an alternative initramfs generator created by the Fedora development team. Fun fact: Plymouth and Dracut are both cities in Massachusetts. Though this is speculation, the creators of these programs might have taken this into consideration.

Dracut should enable Plymouth automatically if it is installed. See the [Dracut installation instructions](https://wiki.gentoo.org/wiki/Dracut#Installation "Dracut").

** Note**\
Some themes such as [[[kde-plasma/breeze-plymouth]](https://packages.gentoo.org/packages/kde-plasma/breeze-plymouth)[]] require certain files to be included in the initramfs such as label plugins and fonts. These currently have to be added manually using `install_items`^[\[1\]](#cite_note-1)^. See [this section on the Dracut page](https://wiki.gentoo.org/wiki/Dracut#Customizing_the_image "Dracut") for customizing the image, and the [example mkinitcpio hook](https://gitlab.com/pwyde/monochrome-plymouth/blob/master/hooks/breeze-plymouth) for which files to add.^[\[2\]](#cite_note-2)^

### [Manual initramfs creation]

When creating a manual initramfs, for example using [Custom Initramfs](https://wiki.gentoo.org/wiki/Custom_Initramfs "Custom Initramfs"), it is possible to bundle Plymouth.

First, disable `udev` USE flag for Plymouth (it will not display anything until udev is properly initialized). Otherwise udev will need to be added to the initramfs as well.

`root `[`#`]`echo "sys-boot/plymouth -udev" >> /etc/portage/package.use`

`root `[`#`]`emerge --ask sys-boot/plymouth`

Then, populate the initramfs with the plymouth files and theme. While it may be done manually, the better way is utilizing [/usr/libexec/plymouth/plymouth-populate-initrd]. It will deliver all the binaries, config and themes needed (only the theme that is enabled, so do not forget to re-execute when changing theme).

The script will copy all the files to selected directory.

Add this code snippet to the initramfs generation script, just before the initramfs packing:

[FILE] **`/path/to/the/generator.sh`Initramfs generation script**

    ....

    # populate plymouth if available
    if [ -x /usr/libexec/plymouth/plymouth-populate-initrd ]
    then
            /usr/libexec/plymouth/plymouth-populate-initrd -t $INITRAM_DIR
    fi

    ....

Finally, update the actual init script in initramfs:

[FILE] **`/path/to/init`Example init file**

    ....

    # Plymouth needs /dev/pts mounted
    mount -t devtmpfs none /dev
    mkdir /dev/pts
    mount -t devpts /dev/pts /dev/pts

    ....

    # early in the process start plymouthd and show splash
    if [[ -x /usr/sbin/plymouthd -a -x /usr/bin/plymouth ]]
    then
            mkdir -p /run/plymouth
            /usr/sbin/plymouthd --attach-to-session --pid-file /run/plymouth/pid --mode=boot
            /usr/bin/plymouth show-splash
    fi

    ....

### [Init systems]

#### [systemd]

Plymouth automatically registers itself with systemd to show splash screens during shutdown and restart. No additional configuration is required.

#### [OpenRC]

There is a plugin for Plymouth that extends a single line version of OpenRC\'s status to the framebuffer. It can be installed via:

`root `[`#`]`emerge --ask sys-boot/plymouth-openrc-plugin`

No additional configuration for the plugin is necessary, it should be operational next time Plymouth is run. To remove this functionality simply uninstall the plugin.

Additionally, make sure that the RC is non-interactive. Edit the [/etc/rc.conf] file:

[FILE] **`/etc/rc.conf`RC configuration for Plymouth example**

    rc_interactive="NO"

## [Bootloaders]

### [GRUB]

When using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), an update to GRUB\'s configuration file must be made in order to enable the splash screen during early boot. Append the options `quiet splash` to the `GRUB_CMDLINE_LINUX_DEFAULT` variable. It may be desirable to adjust the resolution in the `GRUB_GFXMODE` variable to match the desired resolution for the monitor, and set `GRUB_GFXPAYLOAD_LINUX` to \"keep\" in order to preserve the graphics mode during the entire boot.

This all can be performed by modifying the [/etc/default/grub] configuration file:

[FILE] **`/etc/default/grub`Configuring GRUB for Plymouth**

    GRUB_CMDLINE_LINUX_DEFAULT='quiet splash'
    GRUB_GFXMODE=1366x768x24
    GRUB_GFXPAYLOAD_LINUX=keep

## [Themes]

After emerging Plymouth, a number of themes will be pulled in automatically, however more Plymouth themes can be downloaded from the web and installed manually. Extract the downloaded themes to the Plymouth theme directory: [/usr/share/plymouth/themes]

Make sure each new theme is contained in its own folder (just like the default themes that are installed) or they will not be detected by Plymouth.

Once the themes have been extracted, verify successful extraction by requesting Plymouth generate a list of all available themes. Do this using the [plymouth-set-default-theme] command:

`root `[`#`]`plymouth-set-default-theme --list`

To get a preview of the individual themes the following command can be used. Running plymouth from within X can stay on top, preventing the usage of the desktop, hence the killall command after five seconds. It will set a theme, start plymouthd and show the theme, wait five seconds and then kill plymouthd to again allow access to the X session:

`root `[`#`]`plymouth-set-default-theme solar; plymouthd; plymouth --show-splash; sleep 5; killall plymouthd`

Assuming the solar theme is desired as the system\'s theme, run:

`root `[`#`]`plymouth-set-default-theme solar`

** Note**\
The solar theme will be used for the rest of the examples in this article. Simply replace `solar` anywhere it appears with one of the other themes listed when using the [plymouth-set-default-theme] command, to set a different theme.

It is possible to create themes for Plymouth. See the [Theme creation article](https://wiki.gentoo.org/wiki/Plymouth/Theme_creation "Plymouth/Theme creation") for more information.

There is also a [Theming guide](https://wiki.gentoo.org/wiki/User:DerpDays/Plymouth/Theming "User:DerpDays/Plymouth/Theming") which provides a detailed introduction into creating themes.

### [Usage]

Regenerate the initramfs using the [dracut] command:

`root `[`#`]`dracut --force`

As long as the configuration has been performed properly, this will pack the selected Plymouth theme into the initramfs.

Finally, regenerate GRUB config to use the initramfs and apply the [GRUB graphical settings](#GRUB):

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

** Note**\
For Plymouth to work as intended, the proper GRUB video modules must also be loaded. Generally the correct video modules are loaded by default on Gentoo, so inserting additional ones is not usually needed. If frame buffer or video problems are being experienced with GRUB, be sure to investigate missing modules as a possible culprit.

## [Tips]

According to the README file distributed with Plymouth, boot messages are dumped to [/var/log/boot.log] after the root filesystem has been mounted read-write.

## [External resources]

-   [Plymouth on gentoo](https://anderse.wordpress.com/2009/11/05/plymouth-on-gentoo/) - Anders Evenrud\'s Blog (old)
-   [Red Hat 7\'s Plymouth documentation](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Desktop_Migration_and_Administration_Guide/plymouth.html) - Describes how to create a theme using the two-step plugin.
-   [Theming guide](https://wiki.gentoo.org/wiki/User:DerpDays/Plymouth/Theming "User:DerpDays/Plymouth/Theming") for creating themes using the script plugin.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/dracutdevs/dracut/issues/996](https://github.com/dracutdevs/dracut/issues/996)]]
2.  [[[↑](#cite_ref-2)] [[https://aur.archlinux.org/packages/breeze-plymouth#comment-682741](https://aur.archlinux.org/packages/breeze-plymouth#comment-682741)]]