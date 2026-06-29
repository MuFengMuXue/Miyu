Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/de "NVIDIA/nvidia-drivers (13% translated)")
-   [English]
-   [Nederlands](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/nl "NVidia/nvidia-drivers (14% translated)")
-   [español](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/es "NVIDIA/nvidia-drivers (25% translated)")
-   [français](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/fr "Pilotes NVidia  NVidia/nvidia-drivers (27% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/it "NVidia/drivers-nvidia (27% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/hu "NVIDIA/nvidia-drivers (76% translated)")
-   [русский](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/ru "NVIDIA/nvidia-drivers (73% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/zh-cn "NVIDIA/nvidia-drivers (26% translated)")
-   [中文（简体）‎](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/zh-hans "NVIDIA/nvidia-drivers (0% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/ja "NVIDIA/nvidia-drivers (37% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers/ko "NVIDIA/nvidia-drivers (21% translated)")

[[]][Home](https://www.nvidia.com/download/index.aspx)

[[]][Package information](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)

The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package contains the *proprietary* graphics driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.

This proprietary driver contains some wrapper functions that will compile against the Linux kernel and a binary blob that does the heavy lifting for talking to the card. The driver consists of two parts: a kernel module and an X11 driver. Both parts are included in a single package. Due to the way the drivers are packaged, it is necessary to make some choices *before* installing the drivers.

The package contains the latest drivers from NVIDIA with support for most NVIDIA graphic cards, with several versions available depending on the age of the card. It uses an [eclass](https://wiki.gentoo.org/wiki/Eclass "Eclass") to detect what kind of card the system is running so that it installs the proper version.

** Note**\
It is recommended (and good practice) to check the corresponding documentation provided by NVIDIA for the version of the system\'s installed driver, as that information may be more up-to-date and prevalent for more use cases. If any issues arise, README documentation may come of a great help. The official README documentation for all NVIDIA\'s drivers can also be found [online](https://download.nvidia.com/XFree86/Linux-x86_64/).

## Contents

-   [[1] [USE flags]](#USE_flags)
-   [[2] [Hardware compatibility]](#Hardware_compatibility)
    -   [[2.1] [Legacy hardware]](#Legacy_hardware)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Enabling global NVIDIA support]](#Enabling_global_NVIDIA_support)
    -   [[3.2] [Closed source kernel modules]](#Closed_source_kernel_modules)
    -   [[3.3] [Distribution Kernel]](#Distribution_Kernel)
    -   [[3.4] [Manually Compiled Kernel]](#Manually_Compiled_Kernel)
        -   [[3.4.1] [Kernel configuration]](#Kernel_configuration)
    -   [[3.5] [Installing the driver]](#Installing_the_driver)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Permissions]](#Permissions)
    -   [[4.2] [Optional: Kernel module signing]](#Optional:_Kernel_module_signing)
    -   [[4.3] [nvidia-persistenced]](#nvidia-persistenced)
    -   [[4.4] [PCI-Express Runtime D3 (RTD3) Power Management]](#PCI-Express_Runtime_D3_.28RTD3.29_Power_Management)
        -   [[4.4.1] [Setup]](#Setup)
    -   [[4.5] [Using the NVIDIA settings tool]](#Using_the_NVIDIA_settings_tool)
-   [[5] [Usage]](#Usage)
    -   [[5.1] [Testing the card]](#Testing_the_card)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Random freezes]](#Random_freezes)
    -   [[6.2] [Driver fails to initialize when MSI interrupts are enabled]](#Driver_fails_to_initialize_when_MSI_interrupts_are_enabled)
    -   [[6.3] [Getting 2D acceleration to work on machines with 4GB memory or more]](#Getting_2D_acceleration_to_work_on_machines_with_4GB_memory_or_more)
    -   [[6.4] [Failed to initialize DMA on Ryzen]](#Failed_to_initialize_DMA_on_Ryzen)
    -   [[6.5] [\"no such device\" appears when trying to load the kernel module]](#.22no_such_device.22_appears_when_trying_to_load_the_kernel_module)
    -   [[6.6] [Direct rendering is not enabled]](#Direct_rendering_is_not_enabled)
    -   [[6.7] [X11: Failed to acquire modesetting permission]](#X11:_Failed_to_acquire_modesetting_permission)
    -   [[6.8] [Video playback stuttering or slow]](#Video_playback_stuttering_or_slow)
    -   [[6.9] [No HDMI Output/Video/Sound]](#No_HDMI_Output.2FVideo.2FSound)
    -   [[6.10] [No vertical synchronization (no VSync, tearing) in OpenGL applications]](#No_vertical_synchronization_.28no_VSync.2C_tearing.29_in_OpenGL_applications)
    -   [[6.11] [udevd using 100% of the CPU, X server failed to start]](#udevd_using_100.25_of_the_CPU.2C_X_server_failed_to_start)
    -   [[6.12] [Distorted white lines during early boot]](#Distorted_white_lines_during_early_boot)
    -   [[6.13] [ERROR: Kernel configuration is invalid.]](#ERROR:_Kernel_configuration_is_invalid.)
    -   [[6.14] [Plymouth can\'t find nvidia-uvm module]](#Plymouth_can.27t_find_nvidia-uvm_module)
    -   [[6.15] [Wayland: Characters being deleted when typing]](#Wayland:_Characters_being_deleted_when_typing)
    -   [[6.16] [API mismatch]](#API_mismatch)
-   [[7] [Expert configuration]](#Expert_configuration)
    -   [[7.1] [Documentation]](#Documentation)
    -   [[7.2] [Kernel module parameters]](#Kernel_module_parameters)
    -   [[7.3] [Advanced X configuration]](#Advanced_X_configuration)
-   [[8] [See also]](#See_also)
-   [[9] [References]](#References)

## [[] USE flags]

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

## [Hardware compatibility]

The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package supports a range of NVIDIA cards. Multiple versions are available for installation, depending on the card(s) that the system has. See [Feature support list](https://wiki.gentoo.org/wiki/NVIDIA#Feature_support "NVIDIA") and the official NVIDIA documentation, [What\'s a legacy driver?](https://www.nvidia.com/object/IO_32667.html), to find out what version of nvidia-drivers should be used.

### [Legacy hardware]

If the card has been identified as a legacy card (470 or lower) then it is highly recommended to either replace the hardware or switch to the [nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") driver, as the official driver is no longer receiving security updates.

It is still possible to use the unsupported driver, if the user accepts the risks and lack of support by Nvidia and Gentoo:

[FILE] **`/etc/portage/package.unmask/nvidia`Unmask 470 drivers**

    ~x11-drivers/nvidia-drivers-470.256.02

\

[FILE] **`/etc/portage/package.mask/nvidia`Masking drivers with version higher than 470**

    >x11-drivers/nvidia-drivers-471

** Note**\
Change the values to the 390 variants if that driver is the one required.

## [Installation]

** Important**\
When using out-of-tree modules it is usually recommended to stick to LTS (stable in Gentoo) kernels, as the fast release cycle can sometimes break the drivers. It should be noted that Nvidia are usually pretty fast at fixing this, so users rarely notice.

### [Enabling global NVIDIA support]

Use of NVIDIA drivers is controlled by `nvidia` [`VIDEO_CARDS`](https://wiki.gentoo.org/wiki/VIDEO_CARDS "VIDEO CARDS") `USE_EXPAND` variable.

Most NVIDIA GPUs have hardware encoding/decoding. [Here](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new) is the support matrix. GeForce 8 series and later GPUs have [VDPAU](https://wiki.gentoo.org/wiki/VDPAU "VDPAU") superseding legacy XvMCNVIDIA support. Some ebuilds, like [[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]] and [[[media-video/obs-studio]](https://packages.gentoo.org/packages/media-video/obs-studio)[]], have [[[vdpau]](https://packages.gentoo.org/useflags/vdpau)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[nvenc]](https://packages.gentoo.org/useflags/nvenc)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags to enable NVIDIA hardware encoding/decoding.

[FILE] **`/etc/portage/package.use/nvidia`Nvidia USE example**

    */* VIDEO_CARDS: -* nvidia
    */* nvidia vdpau nvenc

### [Closed source kernel modules]

The open source driver only works on Turing GPUs and newer (i.e. GTX 1650 and newer). The [[[kernel-open]](https://packages.gentoo.org/useflags/kernel-open)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag will need to be disabled on older cards.

[FILE] **`/etc/portage/package.use/nvidia`**

    x11-drivers/nvidia-drivers -kernel-open

### [Distribution Kernel]

When using a distribution kernel ([[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] or [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]]), building driver support is as simple as adding the following to [/etc/portage/package.use/00-dist-kernel]:

[FILE] **`/etc/portage/package.use/dist-kernel`/etc/portage/package.use/dist-kernel example**

    */* dist-kernel

This will trigger the Nvidia driver to automatically rebuild on every kernel update. Restarting is recommended after doing a kernel update.

** Tip**\
If using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") as a [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader"), enabling USE-flag [[[dbus]](https://packages.gentoo.org/useflags/dbus)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] for it will also trigger GRUB to update the boot.

### [Manually Compiled Kernel]

As mentioned above, the NVIDIA kernel driver installs and runs against the current kernel. It builds as a module, so the kernel must support the loading of kernel modules (see below).

The kernel module ([nvidia.ko]) consists of a proprietary part (commonly known as the \"binary blob\") which drives the graphics chip(s), and an open source part (the \"glue\") which at runtime acts as intermediary between the proprietary part and the kernel. These all need to work nicely together as otherwise the user might be faced with data loss (through kernel panics, X servers crashing with unsaved data in X applications) and even hardware failure (overheating and other power management related issues should spring to mind).

#### [Kernel configuration]

The [Handbook section on manual kernels](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel#Option_2_-_Assisted_manual_process "Handbook:AMD64/Installation/Kernel") enables all the required kernel modules by default. If this isn\'t the case then the [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package will provide a list of modules which need to be enabled or disabled. For more information on manually adding, see [Gentoo kernel configuration guide](https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide "Kernel/Gentoo Kernel Configuration Guide").

At most, check see that the nouveau module is not built-in.

[KERNEL] **Disable support for the nouveau driver (`CONFIG_DRM_NOUVEAU`)**

    Device Drivers  --->
       Graphics support  --->
          Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
             < > Nouveau (nVidia) cards

** Tip**\
Setting as a modules (\<M\>) is also fine as the ebuild will set a blacklist so the module will not load.

The **nvidia-drivers** ebuild automatically discovers the kernel version based on the [/usr/src/linux] symlink. Please ensure that this symlink is pointing to the correct sources. Choose the right kernel source using [eselect]. When using [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] version 6.18.10 for instance, the kernel listing might look something like this:

`root `[`#`]`eselect kernel list`

    Available kernel symlink targets:
      [1]   linux-6.18.10-gentoo *
      [2]   linux-6.18.9-gentoo

An asterisk (`*`) denotes the current target of the symbolic link.

If the symlink is not pointing to the correct sources, update the link by selecting the number of the desired kernel sources, as in the example above.

`root `[`#`]`eselect kernel set 1`

### [Installing the driver]

Just install [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package:

`root `[`#`]`emerge --ask x11-drivers/nvidia-drivers`

Finally, run an update to take advantage of the earlier USE flag changes:

`root `[`#`]`emerge -vauDU @world`

## [Configuration]

### [Permissions]

The user(s) needing to access the video card will need to be added to the [video] group:

`root `[`#`]`gpasswd -a larry video`

Note that users will be able to run X without permission to the DRI subsystem, but hardware acceleration will be disabled. For Wayland sessions not setting this may result in a very low FPS.

### [Optional: Kernel module signing]

The information in this section is necessary for systems that implement [signed kernel module support](https://wiki.gentoo.org/wiki/Signed_kernel_module_support "Signed kernel module support"). Otherwise, this section can be skipped.

If secure boot kernel signing is used, then the NVIDIA kernel modules need to be signed before they can be loaded.

For ease of administration, it is better to set the global [USE](https://wiki.gentoo.org/wiki/USE "USE") flag [[[modules-sign]](https://packages.gentoo.org/useflags/modules-sign)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], which will automatically sign all installed kernel modules supplied from packages:

[FILE] **`/etc/portage/package.use/modules-sign`Example of /etc/portage/package.use/modules-sign file**

    */* modules-sign

`root `[`#`]`emerge --ask --newuse x11-drivers/nvidia-drivers`

Alternatively, to manually sign modules, sign the [nvidia], [nvidia-drm], [nvidia-modeset], [nvidia-peermem] and [nvidia-uvm] modules (replace `kernel-version-modules-path` with the actual version of the kernel):

`root `[`#`]`/usr/src/linux/scripts/sign-file sha512 /usr/src/linux/certs/signing_key.pem /usr/src/linux/certs/signing_key.x509 /lib/modules/Kernel-Version-modules-path/video/nvidia.ko `

`root `[`#`]`/usr/src/linux/scripts/sign-file sha512 /usr/src/linux/certs/signing_key.pem /usr/src/linux/certs/signing_key.x509 /lib/modules/Kernel-Version-modules-path/video/nvidia-drm.ko `

`root `[`#`]`/usr/src/linux/scripts/sign-file sha512 /usr/src/linux/certs/signing_key.pem /usr/src/linux/certs/signing_key.x509 /lib/modules/Kernel-Version-modules-path/video/nvidia-modeset.ko `

`root `[`#`]`/usr/src/linux/scripts/sign-file sha512 /usr/src/linux/certs/signing_key.pem /usr/src/linux/certs/signing_key.x509 /lib/modules/Kernel-Version-modules-path/video/nvidia-peermem.ko `

`root `[`#`]`/usr/src/linux/scripts/sign-file sha512 /usr/src/linux/certs/signing_key.pem /usr/src/linux/certs/signing_key.x509 /lib/modules/<kernel-version-modules-path>/video/nvidia-uvm.ko `

Once the modules are signed, the driver will load as expected on boot up.

### [nvidia-persistenced]

NVIDIA packages a daemon called *nvidia-persistenced* to assist in situations where the tearing down of the GPU device state isn\'t desired. Typically, the tearing down of the device state is the intended behavior of the device driver. Still, the latencies incurred by repetitive device initialization can significantly impact performance for some applications.

*nvidia-persistenced* is intended to be run as a daemon from system initialization and is generally designed as a tool for compute-only platforms where the NVIDIA device is not used to display a graphical user interface. Depending on the user\'s system and its uses, it may not be necessary to set `persistenced` USE flag.

Currently, Gentoo does not set the `persistenced` USE flag as default.

### [][PCI-Express Runtime D3 (RTD3) Power Management]

NVIDIA GPUs have many power-saving mechanisms. Some of them will reduce clocks and voltages to different parts of the chip. Sometimes, turning off clocks or power to parts of the chip entirely, without affecting functionality or continuing to function, just at a slower speed.

The NVIDIA Linux driver includes initial experimental support for dynamically managing power to the NVIDIA GPU.

Thus, this feature is available only when the following conditions are satisfied:

-   This feature is supported only on notebooks.
-   This feature requires system hardware as well as ACPI support. The necessary hardware and ACPI support was first added in the Intel Coffeelake chipset series. Hence, this feature is supported from Intel Coffeelake chipset series.
-   This feature requires a Turing or newer GPU (i.e. GTX 1650+).
-   This feature is supported with Linux kernel versions 4.18 and newer. With older kernel versions, it may not work as intended.
-   This feature is supported when Linux kernel defines `CONFIG_PM=y`. Typically, if the system supports S3 (suspend-to-RAM), then `CONFIG_PM` would be defined.

#### [Setup]

To enable this feature, then it is recommended to follow the \'Automated Setup\' section in Chapter 22 of the official NVIDIA README documentation, which is outlined below.

Create a file named [80-nvidia-pm.rules] in [/etc/udev/rules.d/] directory with the following contents:

[FILE] **`/etc/udev/rules.d/80-nvidia-pm.rules`**

    # Enable runtime PM for NVIDIA VGA/3D controller devices on driver bind
    ACTION=="bind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030000", TEST=="power/control", ATTR="auto"
    ACTION=="bind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030200", TEST=="power/control", ATTR="auto"

    # Disable runtime PM for NVIDIA VGA/3D controller devices on driver unbind
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030000", TEST=="power/control", ATTR="on"
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030200", TEST=="power/control", ATTR="on"

The following file needs be added to [/etc/modprobe.d/] file to seamlessly enable this feature.

[FILE] **`/etc/modprobe.d/nvidia-pm.conf`**

    # Enable RTD3
    options nvidia NVreg_DynamicPowerManagement=0x02

More information and other configuration options are documented in Chapter 22 of NVIDIA\'s README documentation.

### [Using the NVIDIA settings tool]

NVIDIA also provides a settings tool. This tool allows the user to monitor and change graphical settings without restarting the X server and is available through Portage as part of [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] with the `tools` USE flag set.

## [Usage]

### [[] Testing the card]

To test the NVIDIA card, start X and run [glxinfo], which is part of the [[[x11-apps/mesa-progs]](https://packages.gentoo.org/packages/x11-apps/mesa-progs)[]] package. It should say that direct rendering is activated:

`user `[`$`]`glxinfo | grep direct`

    direct rendering: Yes

To monitor the FPS, run [glxgears].

## [Troubleshooting]

For an overview of the currently open bugs reported against the [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package, take a look at the [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=nvidia-drivers&order=bug_id%20DESC)[]].

### [Random freezes]

Freezes can occur for various reasons. Check that:

-   All power saving options turned off in the system firmware setup.
-   Only the original (from installation) driver options card defined in the [/etc/modprobe.d/nvidia.conf] file.

### [Driver fails to initialize when MSI interrupts are enabled]

The Linux NVIDIA driver uses Message Signaled Interrupts (MSI) by default. This provides compatibility and scalability benefits, mainly due to the avoidance of IRQ sharing. Some systems have been seen to have problems supporting MSI, while working fine with virtual wire interrupts. These problems manifest as an inability to start X with the NVIDIA driver, or CUDA initialization failures.

MSI interrupts can be disabled via the NVIDIA kernel module parameter `NVreg_EnableMSI=0`. This can be set on the command line when loading the module, or more appropriately via the distribution\'s kernel module configuration files (such as those under [/etc/modprobe.d/]).

For instance:

[FILE] **`/etc/modprobe.d/nvidia.conf`Setting nvidia NVreg_EnableMSI**

    # Nvidia drivers support
    alias char-major-195 nvidia
    alias /dev/nvidiactl char-major-195

    # To tweak the driver the following options can be used, note that
    # you should be careful, as it could cause instability!! For more
    # options see /usr/share/doc/nvidia-drivers-337.19/README
    #
    # !!! SECURITY WARNING !!!
    # DO NOT MODIFY OR REMOVE THE DEVICE FILE RELATED OPTIONS UNLESS YOU KNOW
    # WHAT YOU ARE DOING.
    # ONLY ADD TRUSTED USERS TO THE VIDEO GROUP, THESE USERS MAY BE ABLE TO CRASH,
    # COMPROMISE, OR IRREPARABLY DAMAGE THE MACHINE.
    options nvidia NVreg_DeviceFileMode=0660 NVreg_DeviceFileUID=0 NVreg_DeviceFileGID=27 NVreg_ModifyDeviceFiles=1 NVreg_EnableMSI=0

### [Getting 2D acceleration to work on machines with 4GB memory or more]

When NVIDIA 2D acceleration is giving problems, then it is likely that the system is unable to set up a write-combining range with MTRR. To verify, check the contents of [/proc/mtrr]:

`root `[`#`]`cat /proc/mtrr`

Every line should contain `write-back` or `write-combining`. When a line shows up with `uncachable` in it then it is necessary to change a BIOS setting to fix this.

Reboot and enter the BIOS, then find the MTRR settings (probably under \"CPU Settings\"). Change the setting from `continuous` to `discrete` and boot back into Linux. There is now no `uncachable` entry anymore and 2D acceleration now works without any glitches.

Alternatively, it might be necessary to enable MTRR cleanup support (CONFIG_MTRR_SANITIZER=Y) in the Linux kernel:

[KERNEL] **Enable MTRR cleanup support**

    Processor type and features  --->
       [*]   MTRR (Memory Type Range Register) support
       [*]   MTRR cleanup support
       (0)     MTRR cleanup enable value (0-1)
       (1)     MTRR cleanup spare reg num (0-7)

### [Failed to initialize DMA on Ryzen]

Disable AMD Secure Memory Encryption^[\[1\]](#cite_note-1)^:

[KERNEL] **Disable AMD Secure Memory Encryption (SME) support**

    Processor type and features  --->
       [ ]   AMD Secure Memory Encryption (SME) support

### [][\"no such device\" appears when trying to load the kernel module]

This is usually caused by one of the following issues:

1.  The system does not have a NVIDIA card at all. Check [lspci] output to confirm that the system has a NVIDIA graphics card installed and detected.
2.  The currently installed version of [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] does not support the installed graphics card model. Check the README file in /usr/share/nvidia-drivers-\*/ for a list of supported devices, or use the driver search at [http://www.geforce.com/drivers](http://www.geforce.com/drivers).
3.  Another kernel driver has control of the hardware. Check [lspci -k] to see if another driver like \"nouveau\" or \"efifb\" is bound to the graphics card. If so, disable or blacklist this driver.

### [Direct rendering is not enabled]

If direct rendering does not work, it may be because the kernel has Direct Rendering Manager enabled, which conflicts with the driver. See the direct rendering status by following instructions in the section [Testing the card](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers#Testing_the_card "NVIDIA/nvidia-drivers").

First, disable Direct Rendering Manager (`CONFIG_DRM`) in the kernel :

[KERNEL] **Disabling Direct Rendering Manager**

    Device drivers --->
        Graphics support --->
            < > Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)

Next, rebuild [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] since the driver may have built against the kernel DRM symbols. It should fix the problem.

### [X11: Failed to acquire modesetting permission]

[FILE] **`/var/log/Xorg.0.log`**

    [...] (EE) NVIDIA(GPU-0): Failed to acquire modesetting permission.
    [...] (EE) NVIDIA(0): Failing initialization of X screen

Ensure that the [nvidia_drm] module is loaded and initialized during boot (`dmesg -k | grep nvidia-drm`) and verify that kernel modesetting is enabled for the driver with `cat /sys/module/nvidia_drm/parameters/modeset`; if this command returns \"N\" then modesetting may need to be explicitly enabled with the [kernel parameter](https://www.kernel.org/doc/html/v4.14/admin-guide/kernel-parameters.html) `nvidia_drm.modeset=1`. If X11 still fails, specifying the PCI bus of the graphics card may resolve the issue.

Get the PCI bus ID of the graphics card:

`root `[`#`]`lspci -k`

    ...
    0X:0Y.Z VGA compatible controller: NVIDIA Corporation GP104 [GeForce GTX 1080]
            Subsystem: [...]
            Kernel driver in use: nvidia
            Kernel modules: nvidia_drm, nvidia
    ...

Edit the X11 configuration file (`nvidia-xconfig` or `nvidia-settings` may be run prior to this step to generate a suitable configuration):

[FILE] **`/etc/X11/xorg.conf`Adding \'BusID\' to \'Section \"Device\"\'**

    Section "Device"
        Identifier     "Device0"
        BusID      "PCI:X:Y:Z"
        Driver         "nvidia"
        VendorName     "NVIDIA Corporation"
        BoardName      "NVIDIA GeForce GTX 1080"
    EndSection

### [Video playback stuttering or slow]

Lately there seems to be some breaking with playback of some types of video with the NVIDIA binary drivers, causing slow video playback or significant stuttering. This problem seems to be occurring within the Intel CPU Idle replacement instead of the common ACPI CPU idling method for certain CPU\'s.

Disable the Intel CPU idling method using `intel_idle.max_cstate=0` on the kernel command line boot method, which should cause the kernel to automatically fall back to the normal or older ACPI CPU idling method. Also, disabling the NVIDIA Powermizer feature, or setting Powermizer to maximum performance within [nvidia-settings] has been said to help. Although the Intel CPU idling method recently was introduced as the default CPU idling method for i5 and i7 CPUs (versus using ACPI CPU idling) is the root cause here. This idling method significantly solves the problem, however some minimal stuttering or slow video is encountered if deinterlacing was enabled; this is when the video is likely already deinterlaced (ie. alias [mplayer-nodeint] with something similar to [}}] as a work around.)

If using GRUB as the bootloader, add this kernel parameter to [/etc/default/grub] like so:

[FILE] **`/etc/default/grub`Adding intel_idle.max_cstate kernel parameter in GRUB**

    GRUB_CMDLINE_LINUX_DEFAULT="intel_idle.max_cstate=0"

Don\'t forget to run [grub-mkconfig -o /boot/grub/grub.cfg] after making the change, so that the new configuration is generated (see [the GRUB article](https://wiki.gentoo.org/wiki/GRUB#Main_configuration_file "GRUB") for further details).

After rebooting, verify that the change is active:

`user `[`$`]`cat /sys/module/intel_idle/parameters/max_cstate`

    0

### [][No HDMI Output/Video/Sound]

This problem tended to occur whenever the HDMI hub device turned-off for a period of time, or the computer was started with an HDMI hub device turned off.

First, find the PCI device ID, using [lspci].

When this problem occurs, substitute the PCI ID within the following command for rescanning the PCI bus:

`root `[`#`]`echo on > /sys/bus/pci/devices/0000\:06\:00.0/power/control`

This avoides disable runtime power management for PCI function 0, placing this PCI bus always on.

See: [https://download.nvidia.com/XFree86/Linux-x86_64/435.17/README/dynamicpowermanagement.html](https://download.nvidia.com/XFree86/Linux-x86_64/435.17/README/dynamicpowermanagement.html)

### [][No vertical synchronization (no VSync, tearing) in OpenGL applications]

Adding the following option to the screen section prevents tearing on GTX 660, 660 Ti, and probably some other GPUs ([reference](https://devtalk.nvidia.com/default/topic/543305/linux/screen-video-tearing-gtx6xx-7xx-kepler-9xx-maxwell-in-almost-all-applications-including-desktop/post/3958593/)):

[FILE] **`/etc/X11/xorg.conf`**

    Section "Screen"
         . . .
        Option         "metamodes" "nvidia-auto-select +0+0 "
         . . .
    EndSection

### [][udevd using 100% of the CPU, X server failed to start]

Workaround available in [[[bug #670340 comment #8]](https://bugs.gentoo.org/show_bug.cgi?id=670340#c8)[]]

### [Distorted white lines during early boot]

If nothing but a black screen with distorted white lines appears right after the kernel and initramfs is loaded, try disabling `CONFIG_SYSFB_SIMPLEFB` and all framebuffer device drivers except `CONFIG_FB_EFI`.

### [ERROR: Kernel configuration is invalid.]

When building nvidia-drivers, a message could appear like:

`root `[`#`]`emerge x11-drivers/nvidia-drivers`

    ...
    * Preparing nvidia module
    make -j8 HOSTCC=x86_64-pc-linux-gnu-gcc 'LDFLAGS=-m elf_x86_64' NV_VERBOSE=1 IGNORE_CC_MISMATCH=yes SYSSRC=/usr/src/linux SYSOUT=/usr/src/linux modules
    make[1]: Entering directory '/usr/src/linux-5.15.23-gentoo'
    test -e include/generated/autoconf.h -a -e include/config/auto.conf || (        \
    echo >&2;                            \
    echo >&2 "  ERROR: Kernel configuration is invalid.";        \
    echo >&2 "         include/generated/autoconf.h or include/config/auto.conf are missing.";\
    echo >&2 "         Run 'make oldconfig && make prepare' on kernel src to fix it.";   \
    echo >&2 ;                          \
    /bin/false)

This is not an error but the code logic that checks for this error. Therefore, the kernel configuration is in fact not invalid.

### [][Plymouth can\'t find `nvidia-uvm` module]

When using [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), it may be worth considering adding the following configuration to [/etc/modprobe.d] to ensure that `nvidia-uvm` is loaded as a soft dependency of the `nvidia` module. This helps prevent an error that happens when the configuration file is added to the initrd but not the `nvidia-uvm` module; causing an error on [Plymouth](https://wiki.gentoo.org/wiki/Plymouth "Plymouth") about not being able to find the `nvidia-uvm` module.

**This may not be required unless specifically using [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut"), [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), and observe the error produced by [Plymouth](https://wiki.gentoo.org/wiki/Plymouth "Plymouth") (not finding `nvidia-uvm`) in the logs.**

[FILE] **`/etc/modprobe.d/nvidia-uvm.conf`Make nvidia-uvm a soft dependency of the nvidia module (on systemd)**

    # Make a soft dependency for nvidia-uvm as adding the module loading to
    # /usr/lib/modules-load.d/nvidia-uvm.conf for systemd consumption, makes the
    # configuration file to be added to the initrd but not the module, throwing an
    # error on plymouth about not being able to find the module.
    # Ref: /usr/lib/dracut/modules.d/00systemd/module-setup.sh

    # Even adding the module is not the correct thing, as we don't want it to be
    # included in the initrd, so use this configuration file to specify the
    # dependency.

    softdep nvidia post: nvidia-uvm

### [Wayland: Characters being deleted when typing]

**Symptoms:** Strange keyboard behavior while typing, characters being redrawn and deleted.

**Affected:** XWayland applications.

**Reported at :** [https://gitlab.freedesktop.org/xorg/xserver/-/issues/1317](https://gitlab.freedesktop.org/xorg/xserver/-/issues/1317)

**Workaround:**

[FILE] **`/etc/environment`Disabling glamor**

    XWAYLAND_NO_GLAMOR=1

Note that this will increase resource usage.

-   Notice: Disabling glamor causes Wine/Proton games to run slower, and there are reports of Steam not starting.

### [API mismatch]

**Symptoms:** API mismatch can cause launching GPU accelerated applications to fail. It can also cause external displays which are connected via a discrete NVIDIA graphics card to be detected, but not be enabled or activated (the screen will show up in [xrandr], but will refuse to display output - the display will stay in low power mode).

**Detection:** This problem can be detected using a few different methods:

1\. Compare the currently loaded kernel module version with the currently available userspace management utilities.

Kernel module check:

`user `[`$`]`modinfo nvidia | grep version | head -n 1`

    version:        515.65.01

Userspace utility version:

`user `[`$`]`nvidia-settings --version | grep version`

    nvidia-settings:  version 520.56.06

Observe in the previous command output there is a difference in the patch versions: 515.65.01 vs 515.65.06.

2\. Something like the following message will be written to the [dmesg] log:

`user `[`$`]`dmesg`

    [  337.995427] NVRM: API mismatch: the client has the version 520.56.06, but
                   NVRM: this kernel module has the version 515.65.01.  Please
                   NVRM: make sure that this kernel module and all NVIDIA driver
                   NVRM: components have the same version.
    [  339.048386] [drm:nv_drm_dumb_map_offset [nvidia_drm]] *ERROR* [nvidia-drm] [GPU ID 0x00000100] Failed to lookup gem object for mapping: 0x00000006
    [  339.048400] [drm:nv_drm_dumb_map_offset [nvidia_drm]] *ERROR* [nvidia-drm] [GPU ID 0x00000100] Failed to lookup gem object for mapping: 0x00000007

3\. The post-install ebuild log output also includes logic to detect for the API mismatch and instructions for the solution:

`root `[`#`]`emerge @module-rebuild`

    >>> Installing (1 of 1) x11-drivers/nvidia-drivers-520.56.06::gentoo
     * >>> SetUID: [chmod go-r] /usr/bin/nvidia-modprobe ...                                                                             [ ok ]
     * Removing x11-drivers/nvidia-drivers-520.56.06 from moduledb.
     * Updating module dependencies for 6.0.5-gentoo-x86_64 ...                                                                          [ ok ]
     * Adding module to moduledb.
     * Currently loaded NVIDIA modules do not match the newly installed
     * libraries and may prevent launching GPU-accelerated applications.
     * The easiest way to fix this is usually to reboot

**Cause:** API mismatch occurs when the nvidia kernel modules are of a different version than the userspace utilities. This can happen if a full system reboot is not performed after a [nvidia-drivers] package update.

**Solution:** The simplest solution is to perform a full system reboot.

## [Expert configuration]

### [Documentation]

The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package also comes with comprehensive documentation. This is installed into [/usr/share/doc] and can be viewed with the following command:

`user `[`$`]`less /usr/share/doc/nvidia-drivers-*/README.bz2`

### [Kernel module parameters]

The `nvidia` kernel module accepts a number of parameters (options) which can be used to tweak the behavior of the driver. Most of these are mentioned in the documentation. To add or change the values of these parameters, edit the file [/etc/modprobe.d/nvidia.conf]. Remember to run [update-modules] after modifying this file, and bear in mind to reload the `nvidia` module before the new settings take effect.

** Warning**\
Pay close attention to this section as these kernel options can enable features that the hardware may or may not support. These options are not forgiving, so be careful with the parameters. Do not make any changes without validating and double-checking that the change is needed.

  ------------------------------------------- ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Attribute                                   Default       Description
  `NVreg_DeviceFileUID`                       `0`           Modify the user ID for the device file. The default value sets it to the [root] user. Setting this to another user ID will make the driver module create the device file with access available to that user ID.
  `NVreg_DeviceFileGID`                       `27`          Modify the Group ID for the device file. The default value sets it to the [video] group.
  `NVreg_DeviceFileMode`                      Undefined     Set the permissions for the device file. A value of 0660 grants the owner and group-owner read-write access while other users cannot access the device file.
  `NVreg_ModifyDeviceFiles`                   `1`           Instruct the driver to enable or disable dynamic device file management.
  `NVreg_EnablePCIeGen3`                      `0`           Enable PCIe Gen 3.x support. If the system supports this 8GT high speed bus then enable it with this module option flag. When this is enabled but the system does not support Gen 3.0, the behavior of the system can become irratic and unstable. Some have even reported damage to hardware enabling this when it is not properly supported. By default the Nvidia driver is set to use PCIe Gen 2.x for compatibility reasons.
  `NVreg_UsePageAttributeTable`               `0`           This is one of the latest and newest additions to the Nvidia driver modules option. It allows the driver to take full advantage of the PAT technology - a newer way of allocating memory, replacing the older Memory Type Range Register (MTRR) method. The PAT method creates a partition type table at a specific address mapped inside the register and utilizes the memory architecture and instruction set more efficiently and faster. If the computer supports PAT and the feature is enabled in the kernel then this flag can be enabled. Without PAT support, users may experience unstable performance and even crashes if this is enabled. So be careful with these options.
  `NVreg_EnableVia4x`                         `0`           Enable AGP 4x mode in the the NVIDIA driver on Via-chipset-powered systems. Some of these hardware configurations would not work properly in AGP 4x mode when others would. The default leaves it at AGP 2x mode.
  `NVreg_EnableALiAGP`                        `0`           On ALi1541 and ALi1647 chipsets, AGP support is by default disabled by the NVIDIA drivers. The value specifies the speed factor to use, so the values 1, 2, 4 and 8 represent AGP 1x, 2x, 4x and 8x respectively. NVIDIA does not recommend changing the value as it may lead to unstable systems.
  `NVreg_ReqAGPRate`                          Unspecified   Forces the AGP mode on the driver. For instance, a value of 1 means AGP 1x, while a value of 4 means AGP 4x.
  `NVreg_NvAGP`                                             Changes the AGP Gart mode setting. Possible values are: `0` (Disable), `1` (Enable using NVIDIAs internal AGP-Gart), `2` (Enable using the Linux kernel AGP-Gart) and `3` (Enable and use any available, but try th NVIDIA internal one first).
  `NVreg_EnableAGPSBA`                        `0`           Disables (`0`) or enables (`1`) AGP Side Banding. For stability reasons, the setting is by default disabled, but the setting can be enabled for testing and debugging purposes. This is not supported by NVIDIA though.
  `NVreg_EnableAGPFW`                         `0`           Enables AGP Fast-Writes when set to `1`. Depending on the system\'s chipset this may cause stability issues if enabled.
  `NVreg_Mobile`                              `0`           Through this setting, users can force the EDID information for particular systems. This workaround is provided for mobile GPU\'s where EDID information is either non-functional or disabled. Potential values are `0` (Auto detection of the correct setting), `1` (Dell notebooks), `2` (non-Compaq Toshiba laptops), `3` (All other notebooks/laptops), `4` (Compaq Toshiba laptops) or `5` (Gateway machines).
  `NVreg_RemapLimit`                          `60`          Maximum amount of system memory remapping. It specifies the amount of memory that the driver will be allowed to remap through the IOMMU/SWIOTLB on a 64-bit system. Only use it if the IOMMU or SMIOTLB is larger than 64mb. NVIDIA recommends to subtract 4mb from the total amount of memory to use. For instance, the default value is `60` which is in fact 64mb. To set it to 128mb, set the value to `124`.
  `NVreg_UpdateMemoryTypes`                   `0`           Tweak the use of page table attributes. Possible values are: `0` (Nvidias logic mechanism), `1` (Enable the use of changed page table attributes) and `2` (Disable the use of page table attributes).
  `NVreg_InitializeSystemMemoryAllocations`   `1`           Tell the NVIDIA driver to clear system memory allocations prior to using it for the GPUs. Disabling can give a slight performance boost but at the cost of increased security risks. By default the driver will wipe the allocated by zeroing out its content.
  `NVreg_UseVBios`                            `1`           Enable or disable the use of the video BIOS int10 code. Set to `0` to disable.
  `NVreg_RMEdgeIntrCheck`                     Unspecified   Enable or disable checking for edge-triggered interrupts.
  `NVreg_EnableMSI`                           `1`           Enable or disable PCIe-MSI capabilities. Enable this to use MSI interrupts instead of wired interrupts.
  `NVreg_MapRegistersEarly`                   `0`           If set to `1`, allow the driver to map the memory locations early when the system is probing the hardware instead of the default option of doing this when loaded by [modprobe] or during [startx]. This is a debugging feature.
  `NVreg_RegisterForACPIEvents`               `1`           Enable the driver to register with the ACPI of the system to receive ACPI events. This can be disabled (`0`) when issues occur with ACPI or while debugging an issue.
  `NVreg_EnableGpuFirmware`                   Varies        Enable or disable use of GSP firmware. Turing and later GPUs include a GPU System Processor (GSP) which can be used to offload GPU initialization and management tasks. When using GSP firmware, the driver will not yet correctly support display-related features or power management related features. These features will be added to GSP firmware in future driver releases.
  ------------------------------------------- ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Edit the [/etc/modprobe.d/nvidia.conf] file, and afterwards update the module information:

`root `[`#`]`update-modules`

Unload the `nvidia` module\...

`root `[`#`]`modprobe -r nvidia`

\...and load it once again:

`root `[`#`]`modprobe nvidia`

### [Advanced X configuration]

The GLX layer also has a plethora of options which can be configured. These control the configuration of TV out, dual displays, monitor frequency detection, etc. Again, all of the available options are detailed in the documentation.

To use any of these options, list them in the relevant Device section of the X config file (usually [/etc/X11/xorg.conf.d/nvidia.conf]). For example, to disable the splash logo:

[FILE] **`/etc/X11/xorg.conf.d/nvidia.conf`Disable the splash logo**

    Section "Device"
      Identifier "nVidia Inc. GeForce2"
      Driver     "nvidia"
      Option     "NoLogo" "true"
      VideoRam   65536
    EndSection

## [See also]

-   [Nouveau & nvidia-drivers switching](https://wiki.gentoo.org/wiki/Nouveau_%26_nvidia-drivers_switching "Nouveau & nvidia-drivers switching") --- describes how to switch between [NVIDIA\'s binary driver] and the open source [nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") driver.
-   [NVIDIA/Optimus](https://wiki.gentoo.org/wiki/NVIDIA/Optimus "NVIDIA/Optimus") --- a proprietary technology that seamlessly switches between two GPUs.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://devtalk.nvidia.com/default/topic/1039297/linux/unable-to-start-x-failed-to-initialize-dma-/](https://devtalk.nvidia.com/default/topic/1039297/linux/unable-to-start-x-failed-to-initialize-dma-/)]]

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **[Sven Vermeulen (SwifT)](https://wiki.gentoo.org/wiki/User:SwifT "User:SwifT") , M Curtis Napier, and Chris Gianelloni**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*