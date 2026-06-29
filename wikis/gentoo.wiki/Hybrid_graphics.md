[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Hybrid_graphics&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This page details the system management of NVIDIA or AMD switchable graphics and Intel hybrid graphics.

## Contents

-   [[1] [When are hybrid graphics useful?]](#When_are_hybrid_graphics_useful.3F)
-   [[2] [Basic setup]](#Basic_setup)
-   [[3] [AMD CPU with iGPU/Nvidia dGPU]](#AMD_CPU_with_iGPU.2FNvidia_dGPU)
-   [[4] [Nvidia dGPU]](#Nvidia_dGPU)
    -   [[4.1] [Nvidia PRIME]](#Nvidia_PRIME)
        -   [[4.1.1] [PRIME on X server 1.20.7 and newer]](#PRIME_on_X_server_1.20.7_and_newer)
        -   [[4.1.2] [PRIME on older X Server versions]](#PRIME_on_older_X_Server_versions)
        -   [[4.1.3] [Choosing when to use the Nvidia dGPU]](#Choosing_when_to_use_the_Nvidia_dGPU)
    -   [[4.2] [Completely powering down the Nvidia dGPU]](#Completely_powering_down_the_Nvidia_dGPU)
        -   [[4.2.1] [Proprietary driver]](#Proprietary_driver)
            -   [[4.2.1.1] [Dynamic power management]](#Dynamic_power_management)
                -   [[4.2.1.1.1] [Ampere and Newer]](#Ampere_and_Newer)
                -   [[4.2.1.1.2] [Older than Ampere]](#Older_than_Ampere)
            -   [[4.2.1.2] [udev rules]](#udev_rules)
                -   [[4.2.1.2.1] [Kernels 5.5 and newer]](#Kernels_5.5_and_newer)
                -   [[4.2.1.2.2] [Kernels prior to version 5.5]](#Kernels_prior_to_version_5.5)
            -   [[4.2.1.3] [Testing]](#Testing)
            -   [[4.2.1.4] [Points to note]](#Points_to_note)
        -   [[4.2.2] [Open-source nouveau]](#Open-source_nouveau)
-   [[5] [Other options that are available?]](#Other_options_that_are_available.3F)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [][When are hybrid graphics useful?]

-   The display is connected to the iGPU (Integrated Graphics Processing Unit).
-   There is no hardware multiplexer available (and therefore no BIOS/Firmware option to switch to one of the cards).
-   [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") or [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") cards and [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") SOC are the two graphic cards on the device.
-   Maximizing battery life is a priority.

Run:

`user `[`$`]`xrandr --listproviders`

    Providers: number : 2
    Provider 0: id: 0x6e cap: 0xb, Source Output, Sink Output, Sink Offload crtcs: 4 outputs: 5 associated providers: 0 name:Intel
    Provider 1: id: 0x45 cap: 0xf, Source Output, Sink Output, Source Offload, Sink Offload crtcs: 6 outputs: 0 associated providers: 0 name:Unknown
    AMD Radeon GPU @ pci:0000:01:00.0

## [Basic setup]

Make sure the appropriate drivers installed. If the correct drivers are not installed random crashes may occur when turning on external screens, or manual configuration of something like PRIME Render may seem to be the only way to force certain outputs to work when in reality the `amdgpu` and `radeonsi` drivers were not installed.

## [][AMD CPU with iGPU/Nvidia dGPU]

For an AMD CPU with an iGPU, it is important to ensure the following set is present in the [package.use]:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* nvidia amdgpu radeonsi

## [Nvidia dGPU]

The most common configurations will be one of the following:

-   Intel iGPU/Nvidia dGPU
-   AMD iGPU/Nvidia dGPU

When the package [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] is installed, the driver documentation can be found at

[/usr/share/doc/nvidia-drivers-\<driver version\>/html/index.html]

The following will reference pages in that documentation for more information. All of the configuration settings come from the documentation provided by Nvidia.

### [Nvidia PRIME]

*\"PRIME render offload is the ability to have an X screen rendered by one GPU, but choose certain applications within that X screen to be rendered on a different GPU.\"*

This means that the X display server will run on the iGPU and save the use of the dGPU for graphics intensive tasks such as playing games. Fortunately on X server 1.20.7 and newer this should setup automatically.

#### [PRIME on X server 1.20.7 and newer]

*\"On systems with both an integrated GPU and an NVIDIA discrete GPU, the X.Org X server version 1.20.7 and newer will automatically use NVIDIA\'s PRIME render offload\...\"* ^[\[1\]](#cite_note-1)^

On X server 1.20.7 and newer, PRIME should be configured to work by default. The iGPU will offload rendering of specific tasks to the dGPU with very little configuration required.

To check if it is automatically configured:

`user `[`$`]`xrandr --listproviders`

    Providers: number : 2
    Provider 0: id: 0x58 cap: 0xf, Source Output, Sink Output, Source Offload, Sink Offload crtcs: 4 outputs: 6 associated providers: 1 name:AMD Radeon Graphics @ pci:0000:34:00.0
    Provider 1: id: 0x1fc cap: 0x2, Sink Output crtcs: 4 outputs: 1 associated providers: 1 name:NVIDIA-G0

The output should list a NVIDIA-G0 like above.

#### [PRIME on older X Server versions]

*\"NVIDIA\'s PRIME render offload support requires X.Org xserver version 1.20.7 or newer.\"* The X server must be newer than 1.20.7

The [nvidia-xconfig] (provided by the package [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] ) tool has the flag `--prime` which will write a configuration to [/etc/X11/Xorg.conf] that should setup Nvidia PRIME.

`root `[`#`]`nvidia-xconfig --prime`

    Using X configuration file: "/etc/X11/xorg.conf".

    VALIDATION ERROR: Data incomplete in file /etc/X11/xorg.conf.
                      At least one Device section is required.

    X Configuration file set up for PRIME. Please run "xrandr
    --setprovideroutputsource modesetting NVIDIA-0" and "xrandr --auto" to enable.
    See the README for more details.
    Option "AllowEmptyInitialConfiguration" "True" added to Screen "Screen0".
    Backed up file '/etc/X11/xorg.conf' as
    '/etc/X11/xorg.conf.nvidia-xconfig-original'
    Backed up file '/etc/X11/xorg.conf' as '/etc/X11/xorg.conf.backup'
    New X configuration file written to '/etc/X11/xorg.conf'

For more information see: [/usr/share/doc/nvidia-drivers-\<driver version\>/html/primerenderoffload.html]

#### [Choosing when to use the Nvidia dGPU]

To enable all OpenGL and Vulkan apps run on the Nvidia dGPU, add the following to the [/etc/environment] file:

[FILE] **`/etc/environment`Use Nvidia dGPU for Vulkan and OpenGL apps**

    __NV_PRIME_RENDER_OFFLOAD=1
    __GLX_VENDOR_LIBRARY_NAME=nvidia

For more information on the keys available to set, see [/usr/share/doc/nvidia-drivers-\<driver version\>/html/primerenderoffload.html]

To do this on a per application basis, use the program [prime-run] provided by the package [[[x11-misc/prime-run]](https://packages.gentoo.org/packages/x11-misc/prime-run)[]]

Combined with [glxinfo] which is provided by the package [[[x11-apps/mesa-progs]](https://packages.gentoo.org/packages/x11-apps/mesa-progs)[]], the GPU that is being used to render OpenGL applications, in this case it is the dGPU.

`user `[`$`]`prime-run glxinfo | grep "OpenGL renderer string" `

    OpenGL renderer string: NVIDIA GeForce RTX 3050 Ti Laptop GPU/PCIe/SSE2

Or in the terminal preface the command like so (this is what prime-run is doing)

`user `[`$`]`__GLX_VENDOR_LIBRARY_NAME=nvidia glxinfo | grep "OpenGL renderer string" `

    OpenGL renderer string: NVIDIA GeForce RTX 3050 Ti Laptop GPU/PCIe/SSE2

### [Completely powering down the Nvidia dGPU]

It is possible to completely turn off the Nvidia dGPU with minimal adjustments in the settings. For once, some laptops have a BIOS setting which allows to disable the dedicated (or, alternatively, the integrated) graphics card before even the operating system starts. If this option does not exist in the firmware setup, Linux may be configured to disable the dedicated Nvidia card as well.

** Note**\
Some laptops allow to select the primary video card in the firmware setup, without switching either the integrated or dedicated video option completely off. If no Nvidia driver is installed on Linux, i.e. neither nvidia nor nouveau, this firmware option must be set to prefer integrated graphics over the dedicated graphics card and Linux will use *the other* driver for it (mostly either AMD or Intel). For example, on Lenovo Legion 5 laptops this BIOS option is called \"Hybrid Mode\".

#### [Proprietary driver]

Turning the Nvidia card off completely is notably simpler on Ampere cards and newer models, as the default configuration options have this almost completely set up. Nonetheless, it is also feasible to accomplish this on older cards.

To achieve this, the dynamic power management feature must be enabled. Configuring this feature will maximize laptop battery life.

##### [Dynamic power management]

###### [Ampere and Newer]

Ampere and newer Nvidia GPU\'s use the configuration option `NVreg_DynamicPowerManagement=0x03` by default ^[\[2\]](#cite_note-2)^, so no additional settings are necessary in [/etc/modprobe.d/nvidia].

###### [Older than Ampere]

If the Nvidia GPU is older than Ampere then add the following:

[FILE] **`/etc/modprobe.d/nvidia-pm.conf`Enabling dynamic power management**

    options nvidia \
        NVreg_DynamicPowerManagement=0x02 \

Please note that on older hardware the option `0x03` will **disable** dynamic power management!

##### [udev rules]

To completely turn off the dGPU, add a few udev rules:

###### [Kernels 5.5 and newer]

Add the following:

[FILE] **`/lib/udev/rules.d/80-nvidia-pm.rules`Adding udev rules**

    # Enable runtime PM for NVIDIA VGA/3D controller devices on driver bind
    ACTION=="bind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030000", TEST=="power/control", ATTR="auto"
    ACTION=="bind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030200", TEST=="power/control", ATTR="auto"

    # Disable runtime PM for NVIDIA VGA/3D controller devices on driver unbind
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030000", TEST=="power/control", ATTR="on"
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030200", TEST=="power/control", ATTR="on"

^[\[3\]](#cite_note-3)^

###### [Kernels prior to version 5.5]

In addition to the rules added above, add the following:

[FILE] **`/lib/udev/rules.d/80-nvidia-pm.rules`Adding udev rules**

    # Remove NVIDIA USB xHCI Host Controller devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x0c0330", ATTR="1"

    # Remove NVIDIA USB Type-C UCSI devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x0c8000", ATTR="1"

    # Remove NVIDIA Audio devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x040300", ATTR="1"

^[\[4\]](#cite_note-4)^

as per [/usr/share/doc/nvidia-drivers-\<driver version\>/html/dynamicpowermanagement.html]

##### [Testing]

To test if the dGPU is powering down, use the tool [nvidia-smi] which is part of the [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] when compiled with the `tools` USE flag.

`user `[`$`]`nvidia-smi`

    Sun Feb  5 16:49:23 2023
    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 525.85.05    Driver Version: 525.85.05    CUDA Version: 12.0     |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |                               |                      |               MIG M. |
    |===============================+======================+======================|
    |   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0 Off |                  N/A |
    | N/A   46C    P8    N/A /  35W |   1001MiB /  4096MiB |      0%      Default |
    |                               |                      |                  N/A |
    +-------------------------------+----------------------+----------------------+

The N/A / 35W in the example above indicates that the dGPU is turned off.

##### [Points to note]

Here are a few points to note:

-   Executing `nvidia-smi` will turn the dGPU on.
-   Sensor programs that probe for something like the temperature of the dGPU will turn it on.
-   When the dGPU turns on it can cause stuttering.

#### [Open-source nouveau]

This method works when the proprietary nvidia driver has not been installed.

First, blacklist the nouveau module to prevent it from being loaded:

[FILE] **`/etc/modprobe.d/blacklist-nouveau.conf`**

    blacklist nouveau
    options nouveau modeset=0

Alternatively, if the driver has been built-in into the kernel, it can be disabled by the following kernel commandline parameter:

[CODE] **kernel parameter: disable nouveau**

    modprobe.blacklist=nouveau

If the kernel is custom-build, the nouveau driver may also simply be completely omitted.

Then, using a udev rule, the Nvidia graphics card can be completely disabled.

[FILE] **`/etc/udev/rules.d/00-remove-nvidia.rules`**

    # Remove NVIDIA USB xHCI Host Controller devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x0c0330", ATTR="auto", ATTR="1"

    # Remove NVIDIA USB Type-C UCSI devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x0c8000", ATTR="auto", ATTR="1"

    # Remove NVIDIA Audio devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x040300", ATTR="auto", ATTR="1"

    # Remove NVIDIA VGA/3D controller devices
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x03[0-9]*", ATTR="auto", ATTR="1"

After rebooting with those new configuration options in effect, run [lspci \| grep VGA]. If this no longer lists the Nvidia graphics card, it worked.

## [][Other options that are available?]

-   Proprietary [NVIDIA drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers")
    -   with [Bumblebee](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee").
    -   with [PRIME Render Offload](https://download.nvidia.com/XFree86/Linux-x86_64/460.27.04/README/primerenderoffload.html).
-   [Nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") with [PRIME](https://nouveau.freedesktop.org/wiki/Optimus/).

** Note**\
Bumblebee does not work correctly with Nouveau.

-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") with [PRIME](https://github.com/torvalds/linux/blob/master/Documentation/gpu/amdgpu/driver-core.rst#prime-buffer-sharing).

## [See also]

-   [Nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") --- an open source driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.
-   [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") --- The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package contains the *proprietary* graphics driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.
-   [NVIDIA/Bumblebee](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee") --- an open source implementation of [NVIDIA Optimus](https://wiki.gentoo.org/wiki/NVIDIA/Optimus "NVIDIA/Optimus").
-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.

## [External resources]

-   [https://wiki.archlinux.org/title/Hybrid_graphics](https://wiki.archlinux.org/title/Hybrid_graphics) - Arch documentation on hybrid graphics
-   [https://github.com/Bumblebee-Project/bumblebee-gentoo/](https://github.com/Bumblebee-Project/bumblebee-gentoo/) - Bumblebee Overlay
-   [https://wiki.archlinux.org/index.php/PRIME](https://wiki.archlinux.org/index.php/PRIME) - Arch documentation on switchable graphics using either the Nvidia or AMD open source or closed source drivers

## [References]

1.  [[[↑](#cite_ref-1)] [ \'Configure the X Server\' [/usr/share/doc/nvidia-drivers-\<driver version\>/html/primerenderoffload.html] ]]
2.  [[[↑](#cite_ref-2)] [\'Driver Settings\' [/usr/share/doc/nvidia-drivers-\<driver version\>/html/dynamicpowermanagement.html]]]
3.  [[[↑](#cite_ref-3)] [\'Automated Setup\' [/usr/share/doc/nvidia-drivers-\<driver version\>/html/dynamicpowermanagement.html]]]
4.  [[[↑](#cite_ref-4)] [\'Automated Setup\' [/usr/share/doc/nvidia-drivers-\<driver version\>/html/dynamicpowermanagement.html]]]