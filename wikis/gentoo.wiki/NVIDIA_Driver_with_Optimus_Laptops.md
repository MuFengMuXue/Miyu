**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](https://developer.nvidia.com/optimus)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Nvidia_Optimus "wikipedia:Nvidia Optimus")

** See also**\
PRIME GPU Rendering is a preferred solution by many users and should be looked at for support before trying Optimus. More information can be found at [Hybrid_graphics](https://wiki.gentoo.org/wiki/Hybrid_graphics "Hybrid graphics")

**NVIDIA Optimus** is a proprietary technology that seamlessly switches between two GPUs. It is typically used on systems that have an integrated [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") GPU and a discrete [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") GPU. The main benefit of using NVIDIA Optimus is to extend battery life by providing maximum GPU performance only when needed.

For an open source implementation of NVIDIA Optimus, see [Bumblebee](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Kernel modules]](#Kernel_modules)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [Systemd]](#Systemd)
    -   [[2.2] [xorg.conf]](#xorg.conf)
        -   [[2.2.1] [How to find BusID]](#How_to_find_BusID)
        -   [[2.2.2] [Automatic Xorg.conf Configuration]](#Automatic_Xorg.conf_Configuration)
    -   [[2.3] [Using a specific monitor via EDID]](#Using_a_specific_monitor_via_EDID)
        -   [[2.3.1] [Saving the monitor\'s EDID]](#Saving_the_monitor.27s_EDID)
        -   [[2.3.2] [Example xorg.conf for EDID]](#Example_xorg.conf_for_EDID)
    -   [[2.4] [Before starting X]](#Before_starting_X)
    -   [[2.5] [Display manager configuration]](#Display_manager_configuration)
        -   [[2.5.1] [Qingy]](#Qingy)
            -   [[2.5.1.1] [For menu option (A) KDE-4]](#For_menu_option_.28A.29_KDE-4)
            -   [[2.5.1.2] [For menu option (B) your .xsession]](#For_menu_option_.28B.29_your_.xsession)
            -   [[2.5.1.3] [Qingy DirectFB]](#Qingy_DirectFB)
        -   [[2.5.2] [The Console Display Manager (CDM)]](#The_Console_Display_Manager_.28CDM.29)
        -   [[2.5.3] [Simple Desktop Display Manager (SDDM)]](#Simple_Desktop_Display_Manager_.28SDDM.29)
        -   [[2.5.4] [Mint Desktop Manager (MDM)]](#Mint_Desktop_Manager_.28MDM.29)
        -   [[2.5.5] [X Display Manager (XDM)]](#X_Display_Manager_.28XDM.29)
        -   [[2.5.6] [LXDE Display Manager (LXDM)]](#LXDE_Display_Manager_.28LXDM.29)
        -   [[2.5.7] [Gnome Display Manager (GDM)]](#Gnome_Display_Manager_.28GDM.29)
        -   [[2.5.8] [LightDM]](#LightDM)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Specific models]](#Specific_models)
    -   [[3.2] [D-Bus]](#D-Bus)
    -   [[3.3] [Xorg]](#Xorg)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

Since NVIDIA Optimus will be using the integrated Intel graphics for modesetting, the following kernel options will need to be enabled:

[KERNEL] **Linux kernel 4.3.3+**

    Device Drivers  --->
       Graphics Support  --->
          Direct Rendering Manager (Xfree86 4.1.0 and higher DRI support)   --->
             [*]   Enable legacy fbdev support for your modesetting driver
          <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
             [*]   Enable preliminary support for prerelease Intel hardware by default

** Warning**\
This option has been removed in Kernels above 4.10.

** Important**\
In the case that something should go wrong, it is recommended to have live media to assist in reverting any changes. Having a [Gentoo Minimal Install CD](http://get.gentoo.org/) or a [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") around work nicely for this purpose. If you choose to proceed without having a \"just in case\" alternative boot method **proceed with extreme caution!**

** Note**\
At the time this article was written version 343.36 of [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] was the most recent (stable) version of the driver in the Portage tree, therefore examples that reference a specific version will presume version 343.36 is being used. When a newer version of the driver is released, or if an older version is selected, simply substitute 343.36 for the desired version.

### [USE flags]

### [USE flags for] [x11-drivers/nvidia-drivers](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers) [[]] [NVIDIA Accelerated Graphics Driver]

  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                               Add support for X11
  [`+modules`](https://packages.gentoo.org/useflags/+modules)                   Build the kernel modules
  [`+static-libs`](https://packages.gentoo.org/useflags/+static-libs)           Install the XNVCtrl static library for accessing sensors and other features
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                       Allow symbol stripping to be performed by the ebuild for special files
  [`+tools`](https://packages.gentoo.org/useflags/+tools)                       Install additional tools such as nvidia-settings
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Enable subslot rebuilds on Distribution Kernel upgrades
  [`kernel-open`](https://packages.gentoo.org/useflags/kernel-open)             Use the open source variant of the drivers (only works for Turing/Ampere or newer GPUs, aka GTX 1650+ \-- recommended with \>=560.xx drivers if usable and is \*required\* for 50xx Blackwell or newer GPUs \-- always-enabled regardless of USE in \>=595.xx)
  [`modules-compress`](https://packages.gentoo.org/useflags/modules-compress)   Install compressed kernel modules (if kernel config enables module compression)
  [`modules-sign`](https://packages.gentoo.org/useflags/modules-sign)           Cryptographically sign installed kernel modules (requires CONFIG_MODULE_SIG=y in the kernel)
  [`persistenced`](https://packages.gentoo.org/useflags/persistenced)           Install the persistence daemon for keeping devices state when unused (e.g. for headless)
  [`powerd`](https://packages.gentoo.org/useflags/powerd)                       Install the NVIDIA dynamic boost support daemon (only useful with specific laptops, ignore if unsure)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                     Enable dev-libs/wayland backend
  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-23 00:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Installing NVIDIA drivers is easy, run the following:

`root `[`#`]`emerge --ask x11-drivers/nvidia-drivers`

** Note**\
Since xorg 1.18 if the intel screen is always disabled enable `glamor` USE flag on xorg-server

Also, Make sure [Xrandr](https://wiki.gentoo.org/wiki/Xrandr "Xrandr") is installed, as it is needed later in the setup (it is always pulled in automatically). If not, emerge it as well:

`root `[`#`]`emerge --ask x11-apps/xrandr`

## [Configuration]

Configuring a system to use NVIDIA\'s proprietary driver is not easy as the installation. There are several configuration files that will need to be modified in order for a system to work properly.

### [Kernel modules]

If the user has chosen to not use built-in modules, then the init system should load the necessary modules on system boot. If [/proc/config.gz] (or [/boot/config-\*-gentoo]) is available, this can verified by running the following command:

`user `[`$`]`zgrep "CONFIG_MODULES=" /proc/config.gz`

CONFIG_MODULES=y

If the output returns `CONFIG_MODULES` set to `N`, then the kernel will need recompiled with support to load modules. Information about that can be found over here. After module loading support has been added, return to this article and continue reading.

Create a new file called [nvidia.conf] in the [/etc/modules-load.d] directory. It should contain the NVIDIA module name:

[FILE] **`/etc/modules-load.d/nvidia.conf`**

    nvidia

#### [OpenRC]

Verify the modules init script has been added to the boot runlevel (it should be by default, but double check):

`root `[`#`]`rc-update add modules boot`

The output should look like:

    * rc-update: modules already installed in runlevel `boot'; skipping

#### [Systemd]

Check the status of the systemd-modules-load.service to verify things are running smoothly. If issues arise this service unit will be the place to check:

`root `[`#`]`systemctl start systemd-modules-load.service`

### [xorg.conf]

The best way to set the system\'s [xorg.conf] correctly would be to read the documentation NVIDIA has provided. The documentation can be found in a couple of locations. To save time, consider reading only the pages on Optimus and XRandR, as they are vital to correct configuration. If the driver has already been emerged (done in the installation step above), the documentation can be found locally at [/usr/share/doc/nvidia-drivers-\*/README.bz2].

Example: Use the [less] command to read the local documentation:

`user `[`$`]`less /usr/share/doc/nvidia-drivers-*/README.bz2`

It is also possible to read the documentation at NVIDIA\'s website by following these (external) links:

[http://us.download.nvidia.com/XFree86/Linux-x86_64/343.36/README/optimus.html](http://us.download.nvidia.com/XFree86/Linux-x86_64/343.36/README/optimus.html)

[http://us.download.nvidia.com/XFree86/Linux-x86_64/343.36/README/randr14.html](http://us.download.nvidia.com/XFree86/Linux-x86_64/343.36/README/randr14.html)

Replace 343.36 with your version of nvidia-drivers e.g. 390.42 to get the most suitable configuration.

For a quick example here on the wiki, view [this xorg.conf file](https://wiki.gentoo.org/wiki/NVIDIA/Optimus/xorg.conf "NVIDIA/Optimus/xorg.conf").

** Warning**\
The xorg.conf is an example here and since the configuration might change in any version of nvidia-drivers you had better consult the NVIDIA document noted above.

[How to find the busid](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers#Xorg_says_it_can.27t_find_any_screens "NVIDIA/nvidia-drivers")

#### [How to find BusID]

Invoke [lspci] the BusID is at the beginning of each device:

    01:00.0 3D controller: NVIDIA Corporation GK104M [GeForce GTX 870M] (rev a1)

Where `01:00.0` is BusID.

#### [Automatic Xorg.conf Configuration]

The driver comes with an automatic tool to create an appropriate Xorg.conf for using Optimus. If you have a custom xorg.conf, it is prudent to create a backup just in case (although the tool makes a backup of its own).

`root `[`#`]`nvidia-xconfig --prime`

### [Using a specific monitor via EDID]

It is probably best to first try a simple configuration first like described in the NVIDIA driver manual:

[http://us.download.nvidia.com/XFree86/Linux-x86_64/346.22/README/randr14.html](http://us.download.nvidia.com/XFree86/Linux-x86_64/346.22/README/randr14.html)

#### [][Saving the monitor\'s EDID]

** Important**\
Ensure the currently running kernel has `CONFIG_I2C_CHARDEV` enabled and the resulting i2c-dev module loaded or compiled monolithically for [read-edid] to work.

Some laptops/notebooks may benefit from saving the EDID screen information to a file so it can be passed to the Intel modesetting driver. The EDID information can be saved using the [read-edid] utility.

`root `[`#`]`emerge --ask x11-misc/read-edid`

`root `[`#`]`mkdir -p /lib/firmware/edid`

`root `[`#`]`get-edid > /lib/firmware/edid/1920x1080_Clevo_W670SR.bin`

The EDID information is provided to the Intel GPU (Graphics Processing Unit) by specifying its location in the kernel boot parameter:

`drm_kms_helper.edid_firmware=edid/1920x1080_clevo_W670SR.bin`

If the GRUB2 bootloader is being used, this can be configured in the file [/etc/default/grub]

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="drm_kms_helper.edid_firmware=edid/1920x1080_clevo_W670SR.bin"
    GRUB_GFXMODE=1920x1080

Note: If using Sabayon Linux, the kernel boot parameters should be specified in the [/etc/default/sabayon-grub] file instead of [/etc/default/grub] file.

#### [Example xorg.conf for EDID]

See [EDID xorg.conf Example](https://wiki.gentoo.org/wiki/NVIDIA/Optimus/EDID_Xorg.conf_Example "NVIDIA/Optimus/EDID Xorg.conf Example") to view an example [xorg.conf] using an EDID for a specific monitor.

### [Before starting X]

Per NVIDIA\'s [instructions](http://us.download.nvidia.com/XFree86/Linux-x86/346.22/README/randr14.html), the following commands are required before starting X:

[CODE] **XRandR commands:**

    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto

This is to say any Display Manager that starts X-Windows then asks the user to log in ***will*** result in a black screen unless the above [xrandr] commands are run *before* asking the user to log in.

** Warning**\
The [xrandr] commands must be added to the system\'s X session start up scripts (such as [\~/.xinitrc]) in order for the X display to start using modesetting. Failure to do so will result in a black screen.

NOTE: If you get a black screen with no back-lighting from the previous steps, creating .xsessionrc and placing the xinitrc commands in there COULD fix it.

Use the [xrandr] command to find the appropriate graphics device:

`root `[`#`]`xrandr --listproviders`

### [Display manager configuration]

The following shows a list of where to add the required xrandr commands, sorted by desktop.

** Warning**\
If you are sure you have done every step accordingly and still you get a black screen, chances are that the display manager your are using might have problems. Switch to another display manager like [[[x11-misc/lightdm]](https://packages.gentoo.org/packages/x11-misc/lightdm)[]].

#### [Qingy]

##### [][For menu option (A) KDE-4]

Add the [xrandr] commands to the end of the [/etc/X11/Sessions/KDE-4] file:

[FILE] **`/etc/X11/Sessions/KDE-4`KDE-4\'s X session file**

    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto

##### [][For menu option (B) your .xsession]

Add the [xrandr] commands to the end of the [\~/.xsession] file.

##### [Qingy DirectFB]

In the [/etc/directfbrc] configuration file. It is necessary to set the `busid` variable to the BusID of the Intel graphics card as reported by the [lspci] command:

`root `[`#`]`lspci | grep VGA`

00:02.0 VGA compatible controller: Intel Corporation 4th Gen Core Processor Integrated Graphics Controller (rev 06)

For example, if [lspci] says the Intel graphics card is on BusID 00:02.0, then add the following line to [/etc/directfbrc]

[FILE] **`/etc/directfbrc`**

    busid=0:02:0

#### [][The Console Display Manager (CDM)]

Add the **[xrandr]** commands to [\~/.xinitrc] file:

#### [][Simple Desktop Display Manager (SDDM)]

First, edit the sddm configuration to have it look for the commands:

[FILE] **`/etc/sddm.conf`**

    [X11]
    DisplayCommand=/etc/sddm/scripts/Xsetup

Next create the directory [/etc/sddm/scripts]

`root `[`#`]`mkdir -p /etc/sddm/scripts`

.

Then, Add the [xrandr] commands to the [/etc/sddm/scripts/Xsetup] file

[FILE] **`/etc/sddm/scripts/Xsetup`**

    #!/bin/sh
    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto

Finally set execute permissions on the file [/etc/sddm/scripts/Xsetup].

`root `[`#`]`chmod a+x /etc/sddm/scripts/Xsetup`

#### [][Mint Desktop Manager (MDM)]

Add the [xrandr] commands to the [/etc/X11/mdm/Init/Default] file:

#### [][X Display Manager (XDM)]

[]  As of **2020-07-28**, the information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=NVIDIA/Optimus&action=edit).

Add the [xrandr] commands to the [/usr/lib/X11/xdm/Xsetup_0] file and protect them like described above.

**NOTE:** if the system is a 32-bit system, add the commands to the [/usr/lib64/X11/xdm/Xsetup_0] file.

If using a 64-bit system, edit the [/etc/X11/xdm/xdm-config] configuration file and change the following line to point to the [Xsetup_0] file created above:

[FILE] **`/etc/X11/xdm/xdm-config`X Display Manager Example**

    DisplayManager._0.setup: /usr/lib/X11/xdm/Xsetup_0

#### [][LXDE Display Manager (LXDM)]

Add the following lines to [/etc/lxdm/LoginReady]:

[FILE] **`/etc/lxdm/LoginReady`LXDE Display Manager Example**

    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto

#### [][Gnome Display Manager (GDM)]

Create two .desktop files:

[FILE] **`/etc/xdg/autostart/optimus.desktop & /usr/share/gdm/greeter/autostart/optimus.desktop`Desktop Entries**

    [Desktop Entry]
    Type=Application
    Name=Optimus
    Exec=sh -c "xrandr --setprovideroutputsource modesetting NVIDIA-0; xrandr --auto"
    NoDisplay=true
    X-GNOME-Autostart-Phase=DisplayServer

Make sure that GDM uses X as default backend (this does only affect [[[gnome-base/gdm]](https://packages.gentoo.org/packages/gnome-base/gdm)[]]. [[[gnome-base/gnome-shell]](https://packages.gentoo.org/packages/gnome-base/gnome-shell)[]] will still use wayland when USE=\"wayland\" is enabled):

[FILE] **`/etc/gdm/custom.conf`custom.conf**

    # GDM configuration storage

    [daemon]
    # Uncoment the line below to force the login screen to use Xorg
    WaylandEnable=false

    [security]

    [xdmcp]

    [chooser]

    [debug]
    # Uncomment the line below to turn on debugging
    #Enable=true

#### [LightDM]

Prepare a script in [/usr/local/bin/]:

[FILE] **`/usr/local/bin/prepare-optimus.sh`**

    #!/bin/bash
    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto
    # Run the rest of the arguments.
    # -
    $($@)

Make it executable and update [lightdm.conf] with the location of that script:

[FILE] **`/etc/lightdm/lightdm.conf`**

    [Seat:*]
    # display-setup-script = Script to run when starting a greeter session (runs as root)
    display-setup-script=/usr/local/bin/prepare-optimus.sh

## [Troubleshooting]

Since there are many files to configure and because the NVIDIA\'s proprietary support for Optimus in Linux is buggy, it is rather easy to create a faulty Optimus configuration. It is possible something was typed incorrectly, or a certain configuration was not compatible with the hardware being used. Whatever the case, a broken configuration means that debugging is required.

To debug, carefully read the logs from [dmesg] ([/var/log/dmesg]) and Xorg ([/var/log/Xorg.0.log]) with a favorite text editor; they are the best indicators to find issues. If something irregular is discovered, make changes to the respective configuration files. Other areas to inspect for debugging include any of the configuration files that were modified through the course of this article (the kernel\'s }, kernel boot parameters passed at [/etc/default/grub], the Xorg\'s [/etc/X11/xorg.conf] file, etc.). Continue checking the files as necessary then reboot the system and try again. Many attempts may be required in order to obtain a working configuration! It is not exciting process; time *could* be spent on something more interesting, but if debugging is required in order to get Optimus working then it needs to happen.

** Note**\
In a shell to quickly find warnings and errors: `grep -E 'WW|EE' /var/log/Xorg.0.log`

** Note**\
When viewing [/var/log/Xorg.0.log] using a text editor such as [[[app-editors/vim]](https://packages.gentoo.org/packages/app-editors/vim)[]], search for `(WW)` or `(EE)` to quickly find warnings and errors. This will speed up debugging time considerably.

To aid in distinguishing between important and unimportant messages in [/var/log/dmesg] and [/var/log/Xorg.0.log] files, working examples have been provided at these sub-articles:

### [Specific models]

-   [Lenovo Thinkpad W530](https://wiki.gentoo.org/wiki/Lenovo_Thinkpad_W530 "Lenovo Thinkpad W530") - In short, for all the screens to work, set the configuration to discrete mode in the motherboard firmware.

### [D-Bus]

-   [Troubleshooting D-Bus](https://wiki.gentoo.org/wiki/NVIDIA/Optimus/Debugging_D-Bus "NVIDIA/Optimus/Debugging D-Bus")

### [Xorg]

-   [Troubleshooting Xorg](https://wiki.gentoo.org/wiki/NVIDIA/Optimus/Debugging_Xorg "NVIDIA/Optimus/Debugging Xorg")

\
In case Xorg fails immediately after boot but works fine when launched later, it might be due to a race condition in which the Intel driver doesn\'t load in time and Xorg complains that there is no /dev/dri/card0. In that case you should load the Intel driver to the initramfs:

[FILE] **`/etc/dracut.conf.d/nvidiaoptimus.conf`**

    force_drivers+=" i915 "

Regenerate the initramfs image:

`root `[`#`]`dracut --force`

## [See also]

-   [Nouveau & nvidia-drivers switching](https://wiki.gentoo.org/wiki/Nouveau_%26_nvidia-drivers_switching "Nouveau & nvidia-drivers switching") --- describes how to switch between [NVIDIA\'s binary driver](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") and the open source [nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") driver.
-   [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") --- The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package contains the *proprietary* graphics driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.

## [External resources]

-   [Official NVIDIA website](https://www.nvidia.com)