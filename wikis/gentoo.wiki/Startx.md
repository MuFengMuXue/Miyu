This page contains [[changes](https://wiki.gentoo.org/index.php?title=Xorg/Guide&oldid=1396529&diff=1441377#Using_startx)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Xorg/Guide/de "Xorg/Guide (53% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Xorg/Guide/es "Xorg/Guía (48% translated)")
-   [français](https://wiki.gentoo.org/wiki/Xorg/Guide/fr "Xorg/Guide (41% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Xorg/Guide/hu "Xorg/Útmutató (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Xorg/Guide/pl "Xorg/Guide/pl (0% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Xorg/Guide/sv "Xorg/Guide (57% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Xorg/Guide/ru "Xorg/Руководство (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Xorg/Guide/zh-cn "Xorg/指南 (50% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Xorg/Guide/ja "Xorg/ガイド (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Xorg/Guide/ko "Xorg/Guide/ko (37% translated)")

Xorg is the [X Window server](https://wiki.gentoo.org/wiki/X_server "X server") which allows users to have a graphical environment at their fingertips. This guide explains what Xorg is, how to install it, and the various configuration options.

** See also**\
[Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") and [X server](https://wiki.gentoo.org/wiki/X_server "X server") articles.

## Contents

-   [[1] [What is the X Window server?]](#What_is_the_X_Window_server.3F)
    -   [[1.1] [Graphical vs command-line]](#Graphical_vs_command-line)
    -   [[1.2] [The X.org project]](#The_X.org_project)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Input driver support]](#Input_driver_support)
    -   [[2.2] [Kernel modesetting]](#Kernel_modesetting)
        -   [[2.2.1] [Verify legacy framebuffer drivers have been disabled]](#Verify_legacy_framebuffer_drivers_have_been_disabled)
        -   [[2.2.2] [Intel]](#Intel)
        -   [[2.2.3] [NVIDIA]](#NVIDIA)
        -   [[2.2.4] [AMD/ATI]](#AMD.2FATI)
    -   [[2.3] [USE flags]](#USE_flags)
        -   [[2.3.1] [USE_EXPAND]](#USE_EXPAND)
    -   [[2.4] [Locale]](#Locale)
    -   [[2.5] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [The xorg.conf.d directory]](#The_xorg.conf.d_directory)
    -   [[3.2] [Using startx]](#Using_startx)
    -   [[3.3] [Tweaking X settings]](#Tweaking_X_settings)
        -   [[3.3.1] [Setting the screen resolution]](#Setting_the_screen_resolution)
        -   [[3.3.2] [Multiple monitors]](#Multiple_monitors)
        -   [[3.3.3] [Configuring the keyboard]](#Configuring_the_keyboard)
        -   [[3.3.4] [Finishing up]](#Finishing_up)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
    -   [[5.1] [Creating and editing config files]](#Creating_and_editing_config_files)
    -   [[5.2] [Other resources]](#Other_resources)

## [][What is the X Window server?]

### [Graphical vs command-line]

An average user may be frightened at the thought of having to type in commands at a command-line interface (CLI). Why wouldn\'t they be able to point-and-click their way through the freedom provided by Gentoo (and Linux in general)? Well, of course they can!

Gentoo offers a wide variety of flashy graphical interfaces such as [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager") and [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") which can be installed on top of an existing installation.

One of the biggest surprises users who are new to Linux come across: graphical user interfaces are nothing more than an application (or in some cases a suite of applications) which are run on a system. It is *not* part of the Linux kernel or any other internals of the system. That said, GUIs are powerful tools that unlock the graphical abilities of a workstation.

As standards are important, a standard for drawing and moving windows on a screen, interacting with the user through mouse, keyboard, and other basic, yet important aspects has been created and named the *X Window System*, commonly abbreviated as *X11* or just *X*. It is used on Unix, Linux, and Unix-like operating systems throughout the world.

The application that provides Linux users with the ability to run graphical user interfaces and that uses the X11 standard is Xorg-X11, a fork of the XFree86 project. XFree86 has decided to use a license that might not be compatible with the GPL license; the use of Xorg is therefore recommended. XFree86 packages are no longer provided through the Gentoo repository.

### [The X.org project]

The [X.org](http://www.x.org) project created and maintains a freely redistributable, open-source implementation of the X11 system. It is an open source X11-based desktop infrastructure.

Xorg provides an interface between hardware and the graphical software. Besides that, Xorg is also fully network-aware, allowing to run an application on one system while viewing it on a different one.

## [Installation]

Before installing Xorg, prepare the system for it. First, set up the kernel to support input devices and video cards. Then, prepare [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] so that the right drivers and Xorg packages are built and installed.

### [Input driver support]

Support for Event interface needs to be activated by making a change to the kernel configuration. Read the [Kernel Configuration Guide](https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide "Kernel/Gentoo Kernel Configuration Guide") for information on how to setup the kernel.

[KERNEL] **Enable Event interface in the kernel (`CONFIG_INPUT_EVDEV`)**

    Device Drivers --->
      Input device support --->
        <*>  Event interface

### [Kernel modesetting]

Modern open source video drivers rely on kernel mode setting (KMS). KMS provides an improved graphical boot with less flickering, faster user switching, a built-in framebuffer console, seamless switching from the console to Xorg, and other features.

#### [Verify legacy framebuffer drivers have been disabled]

** Important**\
KMS conflicts with legacy framebuffer drivers, which must remain **disabled** in the kernel configuration.

First prepare the kernel for KMS. This step regardless of which Xorg video driver will be used:

[KERNEL] **Disable legacy framebuffer support and enable basic console FB support**

    Device Drivers --->
       Graphics support --->
          Frame Buffer Devices --->
             <*> Support for frame buffer devices --->
             ## (Disable all drivers, including VGA, Intel, NVIDIA, and ATI, except EFI-based Framebuffer Support, only if you are using UEFI)

          ## (Further down, enable basic console support. KMS uses this.)
          Console display driver support --->
             <*>  Framebuffer Console Support

Next configure the kernel to use the proper KMS driver for the video card. Intel, NVIDIA, and AMD/ATI are the most common cards, so follow code listing for each card below.

#### [Intel]

For Intel cards see the [kernel section of the Intel article](https://wiki.gentoo.org/wiki/Intel#Kernel "Intel").

#### [NVIDIA]

For NVIDIA cards, two driver options are available. For a full open source system, an open source driver entitled [Nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") is suggested. The second option is the closed source [NVIDIA driver](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA"), which is officially supported by NVIDIA. This article recommends the Nouveau driver, however be aware not all functionality for certain cards may be supported using the open source driver.

In addition to the kernel driver, certain cards require closed source firmware to be built-in to the Linux kernel. Depending on the selected driver, readers should visit each respective article to check to see if firmware (from the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] is necessary for their specific card.

[KERNEL] **Open source NVIDIA kernel support (`CONFIG_DRM_NOUVEAU`)**

    Device Drivers --->
       Graphics support --->
          <M/*>  Nouveau (NVIDIA) cards

#### [][AMD/ATI]

For newer AMD/ATI cards ([RadeonHD 2000 and up](https://wiki.gentoo.org/wiki/ATI_FAQ "ATI FAQ")), emerge [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] (the package includes firmware for radeon and amdgpu drivers). Once one of these packages has been installed, make the Radeon driver a module in the kernel or, optionally, configure the kernel as detailed in the [firmware section](https://wiki.gentoo.org/wiki/Radeon#Firmware "Radeon") of the Radeon article or, for newer AMD graphics cards (GCN1.1+), the [firmware section](https://wiki.gentoo.org/wiki/AMDGPU#Firmware "AMDGPU") of the AMDGPU article.

Older cards:

[KERNEL] **AMD/ATI Radeon settings**

    ## (Setup the kernel to use the radeon-ucode firmware, optional if "ATI Radeon" below is M)
    Device Drivers --->
       Generic Driver Options --->
       [*]  Include in-kernel firmware blobs in kernel binary
      ## # ATI card specific, (see Radeon page for details which firmware files to include)
       (radeon/<CARD-MODEL>.bin ...)
      ## # Specify the root directory
       (/lib/firmware/) External firmware blobs to build into the kernel binary

    ## (Enable Radeon KMS support)
    Device Drivers --->
       Graphics support --->
       <M/*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
       <M/*>    ATI Radeon
       [*]      Enable modesetting on radeon by default
       [ ]      Enable userspace modesetting on radeon (DEPRECATED)

Newer cards:

[KERNEL] **AMDGPU settings**

    ## (Setup the kernel to use the amdgpu firmware, optional if "AMD GPU" below is M)
    Device Drivers --->
       Generic Driver Options --->
       [*]  Include in-kernel firmware blobs in kernel binary
      ## # AMD card specific, (see AMDGPU page for details which firmware files to include)
       (amdgpu/<CARD-MODEL>.bin ...)
      ## # Specify the root directory
       (/lib/firmware/) External firmware blobs to build into the kernel binary

    ## (Enable Radeon KMS support)
    Device Drivers --->
       Graphics support --->
       <M/*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
       <M/*> AMD GPU
             [ /*] Enable amdgpu support for SI parts
             [ /*] Enable amdgpu support for CIK parts
             [*]   Enable AMD powerplay component
             ACP (Audio CoProcessor) Configuration  --->
                 [*] Enable AMD Audio CoProcessor IP support (CONFIG_DRM_AMD_ACP)
             Display Engine Configuration  --->
                 [*] AMD DC - Enable new display engine
                 [ /*] DC support for Polaris and older ASICs
                 [ /*] AMD FBC - Enable Frame Buffer Compression
                 [ /*] DCN 1.0 Raven family
       <M/*> HSA kernel driver for AMD GPU devices

** Note**\
On x86/amd64, older Radeon cards (X1900 series and older) do not need extra firmware or any special firmware configuration. Direct Rendering Manager (DRM) and ATI Radeon modesetting driver are the only kernel settings necessary for correct operation.

** Note**\
Linux kernel \>= 3.9 does not have the *Enable modesetting on radeon by default* since it is already implied by default. Do not be alarmed if this option is missing in new kernels.

** Note**\
Linux kernel \>= 4.15 does include *Display Core* (DC) which is required for AMDGPU to work. This newer driver was written for GCN5.0 *Vega* and DCN1.0 *Raven Ridge* (APU), but also adds additional functionality for older Radeon graphics cards starting with GCN1.1 *Southern Islands* and newer. It is planned to make this additional support for older Radeon cards the standard, so do not be alarmed if this option is missing in newer kernels.

Save any changes to the kernel configuration, [rebuild the kernel](https://wiki.gentoo.org/wiki/Kernel/Rebuild "Kernel/Rebuild"), and reboot.

### [USE flags]

Before installing Xorg, some adjustments might be needed to the configuration in [[/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage")].

Portage knows the [[[X]](https://packages.gentoo.org/useflags/X)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") for enabling support for X in other packages (default in all *desktop* [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)")). If using a non-desktop profile, make sure the list of USE flags in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] contains `X` to enable optional X compatibility system wide:

[FILE] **`/etc/portage/make.conf`**

    USE="X"

#### [USE_EXPAND]

There are two [USE_EXPAND](https://wiki.gentoo.org/wiki/USE_EXPAND "USE EXPAND") variables that are particularly important to set before installing Xorg.

[`VIDEO_CARDS`](https://wiki.gentoo.org/wiki/VIDEO_CARDS "VIDEO CARDS") is used to enable support for various video cards. Most users will want to set this variable based on their active hardware configuration. Common values include `nouveau` for NVIDIA cards, `amdgpu radeonsi` for [AMD](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") cards, and `intel` for [Intel](https://wiki.gentoo.org/wiki/Intel#X_drivers "Intel") systems. These enable the well-supported, actively developed open-source drivers for their respective devices. To set `VIDEO_CARDS`, create a file like the one below in [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")]. If [/etc/portage/package.use] does not exist, create it.

[FILE] **`/etc/portage/package.use/00video_cards`VIDEO_CARDS examples**

    ## For a system with an Intel CPU and AMD GPU
    */* VIDEO_CARDS: -* amdgpu radeonsi intel

** Important**\
Prior to kernel 6.19, systems with older AMD video cards (Southern Islands and Sea Islands) may require `radeon` as well. See the [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") article for more details.

** Note**\
It is also possible to use the [proprietary NVIDIA drivers](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") by specifying `nvidia` in `VIDEO_CARDS`. However, configuring and installing the proprietary drivers is beyond the scope of this guide. There is a dedicated [Gentoo Linux NVIDIA guide](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") that details that process.

[`INPUT_DEVICES`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#INPUT_DEVICES "/etc/portage/make.conf") is used to determine which drivers should be built to support various input devices.

[make.defaults] has [Libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") as the default input device driver.

To check what is presently set, run:

`user `[`$`]`portageq envvar INPUT_DEVICES`

The default value of `libinput` is sufficient in many cases. However, there are some input devices, such as Synaptics touchpads on laptops, that need other drivers. If this is the case, `INPUT_DEVICES` can be configured by creating a file like the one below in the [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")] directory.

[FILE] **`/etc/portage/package.use/00input`INPUT_DEVICES example**

    ## (For generic mouse, generic keyboard, Synaptics touchpad, and Wacom drawing tablet support)
    */* INPUT_DEVICES: libinput synaptics wacom

If the suggested settings do not work, emerge the [[[x11-base/xorg-drivers]](https://packages.gentoo.org/packages/x11-base/xorg-drivers)[]] package (see the step below). Check all the options available and choose those which apply to the system. This example is for a system with a keyboard, mouse, Synaptics touchpad, and an AMD Radeon video card.

`root `[`#`]`emerge --pretend --verbose x11-base/xorg-drivers`

    These are the packages that would be merged, in order:

    Calculating dependencies... done!
    [ebuild   R   ] x11-base/xorg-drivers-1.20-r1::gentoo  INPUT_DEVICES="libinput synaptics -elographics -evdev -joystick -keyboard -mouse -vmmouse -void -wacom" VIDEO_CARDS="amdgpu radeonsi -ast -dummy -fbdev (-freedreno) (-geode) -glint -i915 -i965 -intel -mga -nouveau -nv -nvidia (-omap) -qxl -r128 -radeon -siliconmotion (-tegra) (-vc4) -vesa -via -virtualbox -vmware" 0 KiB

The USE flags have the following meaning:

### [USE flags for] [x11-base/xorg-server](https://packages.gentoo.org/packages/x11-base/xorg-server) [[]] [X.Org X servers]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+elogind`](https://packages.gentoo.org/useflags/+elogind)       Use elogind to get control over framebuffer when running as regular user
  [`+udev`](https://packages.gentoo.org/useflags/+udev)             Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`minimal`](https://packages.gentoo.org/useflags/minimal)         Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`suid`](https://packages.gentoo.org/useflags/suid)               Enable setuid root program(s)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`unwind`](https://packages.gentoo.org/useflags/unwind)           Enable libunwind usage for backtraces
  [`xcsecurity`](https://packages.gentoo.org/useflags/xcsecurity)   Build Security extension
  [`xephyr`](https://packages.gentoo.org/useflags/xephyr)           Build the Xephyr server
  [`xnest`](https://packages.gentoo.org/useflags/xnest)             Build the Xnest server
  [`xorg`](https://packages.gentoo.org/useflags/xorg)               Build the Xorg X server (HIGHLY RECOMMENDED)
  [`xvfb`](https://packages.gentoo.org/useflags/xvfb)               Build the Xvfb server
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-30 20:45] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
By default the [[[suid]](https://packages.gentoo.org/useflags/suid)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is disabled, which is fine when, as per recommendation, X runs under a [logind](https://wiki.gentoo.org/wiki/OpenRC#logind "OpenRC") provider like [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind"), or [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"). The [[[suid]](https://packages.gentoo.org/useflags/suid)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag should however be enabled in [/etc/portage/package.use/xorg-server] in case no logind provider is used and X is run under a normal user account, e.g. started with [startx]. Please see also this [repository news article](https://www.gentoo.org/support/news-items/2020-06-24-xorg-server-dropping-default-suid.html). Setting suid would then prevent permission errors on [/dev/tty0], or on *virtual console 7*. For more details see the dedicated [Non root Xorg](https://wiki.gentoo.org/wiki/Non_root_Xorg "Non root Xorg") article.

### [Locale]

x11-libs/libxcb fails to emerge without [UTF-8](https://wiki.gentoo.org/wiki/UTF-8 "UTF-8") ([[[bug #913655]](https://bugs.gentoo.org/show_bug.cgi?id=913655)[]]).

`user `[`$`]`eselect locale list`

    Available targets for the LANG variable:
      [1]   C
      [2]   C.utf8
      [3]   en_US
      [4]   en_US.iso88591 *
      [5]   en_US.utf8
      [6]   POSIX
      [ ]   (free form)

Set the \"utf8\" locale.

`root `[`#`]`eselect locale set 5`

### [Emerge]

After setting all the necessary variables and USE flags Xorg can be installed:

`root `[`#`]`emerge --ask x11-base/xorg-server`

When the installation is finished, some environment variables will need to re-initialized before continuing. Source the profile with this command:

`root `[`#`]`env-update `

`root `[`#`]`source /etc/profile `

## [Configuration]

The [X server](https://wiki.gentoo.org/wiki/X_server "X server") is designed to work out-of-the-box, with no need to manually edit Xorg\'s configuration files. It *should* detect and configure devices such as displays, keyboards, and mice.

Try [using startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide") without editing any configuration files. If Xorg will not start, or there is some other problem, then manual configuration of Xorg might be needed. This is explained in the following section.

To run Xorg with non-root users, as root, either enable a logind provider (see [Non root Xorg](https://wiki.gentoo.org/wiki/Non_root_Xorg "Non root Xorg")) or set the `suid` USE flag (see above note).

** Note**\
If changes have been made to the kernel, do not forget to **restart the system** *before* using [startx] in order to be using the newly built kernel. If the kernel was updated to a newer version in the process this will most likely require the bootloader\'s configuration files to be updated as well.

### [The [xorg.conf.d] directory]

** Important**\
Configuring files in [[xorg.conf.d](https://wiki.gentoo.org/wiki/Xorg.conf#xorg.conf.d.2C_xorg.conf "Xorg.conf")] should be seen as a last resort option. If possible it is desirable to run Xorg without any special configuration.

Most of the configuration files for Xorg are stored in [[/etc/X11/xorg.conf.d/](https://wiki.gentoo.org/wiki/Xorg.conf#xorg.conf.d.2C_xorg.conf "Xorg.conf")]. If that directory does not exist, then create it. Each file is given a unique name and ends in [.conf]. The file names in Xorg\'s configuration directory will be read in alpha numeric order. For example, [10-evdev.conf] will be read before [20-synaptics.conf]; [a-evdev.conf] will be read before [b-synaptics.conf], and so on. The files in this directory are not required to be numbered, but doing so will help to keep them organized. Organization is helpful when debugging faulty configuration files.

** Note**\
Xorg provides example configurations in [/usr/share/doc/xorg-server-\$/xorg.conf.example.bz2]. These can be used to create custom configuration files in [[/etc/X11/xorg.conf.d/](https://wiki.gentoo.org/wiki/Xorg.conf#xorg.conf.d.2C_xorg.conf "Xorg.conf")]. The examples are heavily commented, but if more documentation regarding the syntax is needed, [man xorg.conf] is always available. Other examples can be found in the section [Other resources](https://wiki.gentoo.org/wiki/Xorg/Guide#Other_resources "Xorg/Guide") at the end of this guide.

### [[] Using startx]

Try [startx] to start up the [X server](https://wiki.gentoo.org/wiki/X_server "X server"). [startx] is a script (it\'s installed by [[[x11-apps/xinit]](https://packages.gentoo.org/packages/x11-apps/xinit)[]]) that executes an *X session*; that is, it starts the X server and some graphical applications on top of it. It decides which applications to run using the following logic:

-   If a file named [.xinitrc] exists in the home directory, it will execute the commands listed there.

<!-- -->

-   Otherwise, it will read the value of the `XSESSION` variable from the [/etc/env.d/90xsession] file and execute the relevant session accordingly. Values for `XSESSION` are available in [/etc/X11/Sessions/]. To set a system wide default session run:

`root `[`#`]`echo XSESSION="Xfce4" > /etc/env.d/90xsession`

This will create the [90xsession] file and set the default X session to [Xfce](https://wiki.gentoo.org/wiki/Xfce/Guide "Xfce/Guide"). Remember to run [env-update] after making changes to [90xsession].

`user `[`$`]`startx`

If no window manager has been installed a solid black screen will appear. Since this can also be a sign that something is wrong, the [[[x11-wm/twm]](https://packages.gentoo.org/packages/x11-wm/twm)[]] and [[[x11-terms/xterm]](https://packages.gentoo.org/packages/x11-terms/xterm)[]] packages can be installed only to test X.

Once the programs are installed, run [startx] again. A few [xterm] windows should appear, making it easy to verify the X server is working correctly. Once satisfied with the results, depclean [[[x11-wm/twm]](https://packages.gentoo.org/packages/x11-wm/twm)[]] and [[[x11-terms/xterm]](https://packages.gentoo.org/packages/x11-terms/xterm)[]] if installed in the step above to remove the testing packages. They will not be needed to setup a proper desktop environment.

The session (program to start) could also be given as an argument to [startx]:

`user `[`$`]`startx /usr/bin/startfluxbox`

In addition, to pass X11 server options, by preceding them with a double dash:

`user `[`$`]`startx -- vt7`

### [Tweaking X settings]

#### [Setting the screen resolution]

If the screen resolution looks to be wrong, check two sections in [[xorg.conf.d](https://wiki.gentoo.org/wiki/Xorg.conf#xorg.conf.d.2C_xorg.conf "Xorg.conf")] configuration. First of all, the *Screen* section lists the resolutions that the X server will run at. This section might not list any resolutions at all. If this is the case, Xorg will estimate the resolutions based on the information in the second section, *Monitor*.

Now change the resolution. In the next example from [/etc/X11/xorg.conf.d/40-monitor.conf] we add the `PreferredMode` line so that the X server starts at 1440x900 by default. The `Option` in the `Device` section must match the name of the monitor (`DVI-0`), which can be obtained by running [xrandr]. Install [xrandr] ([emerge xrandr]) just long enough to get this information. The argument after the monitor name (in the `Device` section) must match the `Identifier` in the `Monitor` section.

[FILE] **`/etc/X11/xorg.conf.d/40-monitor.conf`**

    Section "Device"
      Identifier  "RadeonHD 4550"
      Option      "Monitor-DVI-0" "DVI screen"
    EndSection
    Section "Monitor"
      Identifier  "DVI screen"
      Option      "PreferredMode" "1440x900"
    EndSection

Run X ([startx]) to discover it uses the desired resolution.

#### [Multiple monitors]

More than one monitor in can be established in [[/etc/X11/xorg.conf.d/](https://wiki.gentoo.org/wiki/Xorg.conf#xorg.conf.d.2C_xorg.conf "Xorg.conf")]. Give each monitor a unique identifier, then list its physical position, such as \"RightOf\" or \"Above\" another monitor. The following example shows how to configure a DVI and a VGA monitor, with the VGA monitor as the right-hand screen:

[FILE] **`/etc/X11/xorg.conf.d/40-monitor.conf`**

    Section "Device"
      Identifier "RadeonHD 4550"
      Option     "Monitor-DVI-0" "DVI screen"
      Option     "Monitor-VGA-0" "VGA screen"
    EndSection
    Section "Monitor"
      Identifier "DVI screen"
    EndSection
    Section "Monitor"
      Identifier "VGA screen"
      Option     "RightOf" "DVI screen"
    EndSection

#### [Configuring the keyboard]

For methods of switching the keyboard layout see the [Keyboard layout switching](https://wiki.gentoo.org/wiki/Keyboard_layout_switching#X11 "Keyboard layout switching") article.

** Note**\
The rest of this section may not be needed if following the [Keyboard layout switching](https://wiki.gentoo.org/wiki/Keyboard_layout_switching#X11 "Keyboard layout switching") article.

To setup X to use an international keyboard create the appropriate config file in [[/etc/X11/xorg.conf.d/](https://wiki.gentoo.org/wiki/Xorg.conf#xorg.conf.d.2C_xorg.conf "Xorg.conf")]. This example features a Czech keyboard layout:

[FILE] **`/etc/X11/xorg.conf.d/30-keyboard.conf`**

    Section "InputClass"
      Identifier "keyboard-all"
      Driver "evdev"
      MatchProduct "AT Translated Set 2 keyboard"    # apply to devices having this as a substring
      MatchIsKeyboard "true"                         # apply to "keyboard" devices only
      Option "XkbLayout" "us,cz"
      Option "XkbModel" "logitech_g15"
      Option "XkbRules" "xorg"
      Option "XkbOptions" "grp:alt_shift_toggle,grp:switch,grp_led:scroll,compose:rwin,terminate:ctrl_alt_bksp"
      Option "XkbVariant" ",qwerty"
      MatchIsKeyboard "on"
    EndSection

The \"terminate\" command (`terminate:ctrl_alt_bksp`) lets users kill the X session by using the [Ctrl]+[Alt]+[Backspace] key combination. This will, however, make X exit disgracefully \-- something that users might want to avoid. It can be useful when programs have frozen the display entirely, or when configuring and tweaking the Xorg environment. Be careful when killing the desktop with this key combination - most programs really do not like it when they are ended this way. Some, if not all, of the information that has not been written to the disk (information stored in \"open documents\") will be lost.

Because the \"evdev\" driver can handle multiple devices (even non-keyboards), limiting the section to only some devices might be needed for proper working of all the devices. Use the `MatchProduct` directive to specify the device name, consult [man xorg.conf] for more info.

For more information about `XkbModel` and `XkbOptions`, consult [/usr/share/X11/xkb/rules/base.lst] and [man xkeyboard-config].

#### [Finishing up]

Run [startx] and be happy about the result. There should now be a (hopefully) working Xorg! The next step is to install a useful window manager or desktop environment such as [KDE](https://wiki.gentoo.org/wiki/KDE "KDE"), [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME"), or [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce"). Information on installing these desktop environments can be found here on the wiki.

## [See also]

-   [Non root Xorg](https://wiki.gentoo.org/wiki/Non_root_Xorg "Non root Xorg") --- describes how an unprivileged user can run [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") without using suid.
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [X (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/Securing_services#X "Security Handbook/Securing services") - The Security Handbook\'s entry on securing the X server.
-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").
-   [Xorg/Guide] --- explains what Xorg is, how to install it, and the various configuration options.
-   [Xrandr](https://wiki.gentoo.org/wiki/Xrandr "Xrandr") --- [X](https://wiki.gentoo.org/wiki/X "X") protocol extension and its CLI tool [xrandr] are used to manage screen resolutions, rotation and screens with multiply displays in X
-   [X server](https://wiki.gentoo.org/wiki/X_server "X server") --- the main component of the X Window system which abstracts the hardware and provides the foundation for most graphical user interfaces, like [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") or [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), and their applications.

## [External resources]

### [Creating and editing config files]

[man xorg.conf] and [man evdev] provide quick yet complete references about the syntax used by these configuration files. Be sure to have them open on a terminal when editing Xorg configuration files!

Example configurations can be found at [/usr/share/doc/xorg-server-\*/xorg.conf.example.bz2].

There are also many online resources on editing config files in [/etc/X11/]. Only a few are listed here; use a favorite search engine to find more.

### [[] Other resources]

More information about installing and configuring various graphical desktop environments and applications can be found in the [Gentoo desktop resources](https://wiki.gentoo.org/wiki/Category:Desktop "Category:Desktop") section of our documentation.

When upgrading to xorg-server 1.9 or higher, be sure to read the [migration guide](https://wiki.gentoo.org/wiki/X_server/upgrade "X server/upgrade").

X.org provides many [FAQs](http://www.x.org/wiki/FAQ) on their website, in addition to their other documentation.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **[Sven Vermeulen (SwifT)](https://wiki.gentoo.org/wiki/User:SwifT "User:SwifT") , Joshua Saddler(nightmorph)**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*