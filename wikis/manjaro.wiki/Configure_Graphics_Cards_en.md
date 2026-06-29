[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Configure+Graphics+Cards&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Configure_Graphics_Cards "Configure Graphics Cards (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Configure_Graphics_Cards/tr "Grafik Kartlarını Yapılandırma (1% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Configure_Graphics_Cards/es "Configurar Tarjetas Gráficas (6% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Configure_Graphics_Cards/ru "Настройка видеокарт (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Configure_Graphics_Cards/zh-cn "配置显卡 (28% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Automated Identification and Installation]](#Automated_Identification_and_Installation)
-   [[3] [Manual Identification and Installation]](#Manual_Identification_and_Installation)
    -   [[3.1] [Identifying Available Drivers]](#Identifying_Available_Drivers)
    -   [[3.2] [Installing a Driver]](#Installing_a_Driver)
    -   [[3.3] [Force Reinstall a Driver]](#Force_Reinstall_a_Driver)
-   [[4] [Removing an Installed Driver]](#Removing_an_Installed_Driver)
    -   [[4.1] [Identifying Installed Drivers]](#Identifying_Installed_Drivers)
    -   [[4.2] [Removing Installed Drivers]](#Removing_Installed_Drivers)
-   [[5] [Checking configuration]](#Checking_configuration)
-   [[6] [Dual GPU]](#Dual_GPU)
    -   [[6.1] [PRIME GPU offloading]](#PRIME_GPU_offloading)
-   [[7] [NVIDIA Proprietary (non-free) drivers]](#NVIDIA_Proprietary_.28non-free.29_drivers)
    -   [[7.1] [Nvidia Optimus]](#Nvidia_Optimus)
    -   [[7.2] [Configure The Resolution/Refresh Rate]](#Configure_The_Resolution.2FRefresh_Rate)
    -   [[7.3] [Configure X Screen settings (OpenGL Settings, Antialiasing, X Server XVideo)]](#Configure_X_Screen_settings_.28OpenGL_Settings.2C_Antialiasing.2C_X_Server_XVideo.29)
    -   [[7.4] [Nvidia settings for special cases]](#Nvidia_settings_for_special_cases)
    -   [[7.5] [nvidia-prime]](#nvidia-prime)
    -   [[7.6] [Bumblebee]](#Bumblebee)
-   [[8] [See also]](#See_also)
-   [[9] [Easier way]](#Easier_way)
-   [[10] [How to check the driver]](#How_to_check_the_driver)
    -   [[10.1] [Checking vulkan support]](#Checking_vulkan_support)

# [Overview]

**Note**

------------------------------------------------------------------------

The mhwd command is still *under development*, and at present is only able to install drivers for graphics cards connected internally via pci.

Where installing the full version of Manjaro (i.e. complete with a pre-installed desktop environment, codecs, and software applications), the mhwd command will be automatically run by the GUI and CLI installer to automatically detect your graphics card and install the most appropriate driver for it. **Whether free or proprietary drivers are installed will depend on your initial choice of using free or nonfree graphics drivers to boot up**. Otherwise, it will be necessary to run the mhwd command manually as part of the post-installation process for the minimalistic **NET-Edition** of Manjaro.

**For Beginners, it is recommended to use \"Hardware Detection\" in [Manjaro Settings Manager](//wiki.manjaro.org/index.php?title=Manjaro_Settings_Manager "Manjaro Settings Manager") to change or install new graphics drivers.**\
For intermediate and advanced users, it is also possible to use the mhwd command to install, re-install, and remove installed graphics drivers at any time, as illustrated below.

# [Automated Identification and Installation]

This is the recommended method for the detection and installation of graphics drivers. The syntax for the automated installation method is:

[user \$ ][ sudo mhwd -a \[pci or usb connection\] \[free or nonfree drivers\] 0300 [COPY TO CLIPBOARD]]

\

A breakdown of the command used for the automated method is as follows:

-   **-a**: Automatically detect and install the appropriate driver
-   **\[pci or usb\]**: Install the appropriate driver for devices connected internally via pci, or externally via usb (again, mhwd currently only supports pci connections at this stage in its development)
-   **\[free or nonfree\]**: Install either free drivers (e.g. provided by the Linux community), or nonfree drivers (e.g. provided by hardware manufacturers)
-   **0300**: Identify that a driver is to be installed for a graphics card (0300 is the ID for graphics cards. As the mhwd command develops, new ids will be used for other hardware devices).

\
For example, the following command would result in the automatic detection and installation of the best available **proprietary driver** for a pci-connected graphics card:

[user \$ ][ sudo mhwd -a pci nonfree 0300 [COPY TO CLIPBOARD]]

\

\
Otherwise, the following command would result in the automatic detection and installation of the best available **free driver** for a pci-connected graphics card:

[user \$ ][ sudo mhwd -a pci free 0300 [COPY TO CLIPBOARD]]

\

# [Manual Identification and Installation]

Taking a do-it-yourself approach is itself relatively easy and straightforward using the mhwd command. This should be undertaken in two stages:

**1.** Identify the appropriate driver to be installed, and then

**2.** Install the driver

\

\

**Tip**

------------------------------------------------------------------------

Just ensure that you have identified and are indeed about to install the correct driver for your particular graphics card!

\

## [Identifying Available Drivers]

Prior to manually installing a graphics driver, it will be necessary to identify what drivers are available for your system. To list the appropriate drivers available, the basic syntax is:

[user \$ ][ mhwd -l \[optional: detailed view\] \[optional: \--pci or \--usb connection\] [COPY TO CLIPBOARD]]

\

Using this command without the additional options will list basic information for all the available drivers for devices connected to your system. **All drivers graphics card drivers will have the prefix (video-) in their name**. The basic information provided for all listed drivers will be:

-   Name
-   Version
-   Free or proprietary, and
-   PCI or USB connection

\
A more detailed list of installed drivers can be obtained by entering:

[user \$ ][ mhwd -l -d [COPY TO CLIPBOARD]]

\

A detailed list will provide the following information:

-   Name
-   Version
-   PCI or USB connection
-   Description
-   Priority
-   Free or proprietary
-   Dependencies
-   Conflicts
-   Class ID (e.g. \'0300\' for graphics card drivers), and
-   Vendor ID

\
In addition, using the *\--pci* filter in the following example will list detailed information for only the drivers available for devices (e.g. graphics cards) using an internal PCI connection:

[user \$ ][ mhwd -l -d \--pci [COPY TO CLIPBOARD]]

\

## [Installing a Driver]

To install a driver for a graphics card, the syntax is:

[user \$ ][ sudo mhwd -i pci \[name of driver\] [COPY TO CLIPBOARD]]

\

\
A breakdown of the command used to manually install a driver is as follows:

-   **-i**: Install a driver
-   **\[pci\]**: Install a driver for a device connected internally via pci (e.g. graphics cards)
-   **\[name of driver\]**: The name of the driver to be installed

For example, to install the proprietary nvidia graphics card driver, the following command would be used:

[user \$ ][ sudo mhwd -i pci video-nvidia [COPY TO CLIPBOARD]]

\

## [Force Reinstall a Driver]

**Warning**

------------------------------------------------------------------------

use this command with care!

To force the re-installation of an existing driver without removing it first, the syntax is:

[user \$ ][ sudo mhwd -f -i pci \[name of driver\] [COPY TO CLIPBOARD]]

\

For example, to force the re-installation of a previously installed nvidia graphics card driver, the following command would be used:

[user \$ ][ sudo mhwd -f -i pci video-nvidia [COPY TO CLIPBOARD]]

\

# [Removing an Installed Driver]

On occasion it may be necessary to remove an installed graphics card driver. Similarly to manually installing a graphics card driver, two steps should be undertaken for removal:

**1.** Identify the installed driver

**2.** Remove the identified driver

After all, it would be somewhat difficult to remove an installed driver if you don\'t know what it\'s called!

\

## [Identifying Installed Drivers]

To identify and list Manjaro\'s installed drivers - including the graphics driver to be removed, the syntax is:

[user \$ ][ mhwd -li \[optional: detailed view\] \[optional: pci or usb devices only\] [COPY TO CLIPBOARD]]

\

Using this command without the additional options will list the basic information of all the drivers currently installed on your system. **Once again, all drivers for graphics cards will have the prefix (video-) in their name**. As with listing drivers available for your system, the *-d* option used in the following command will list detailed information:

[user \$ ][ mhwd -li -d [COPY TO CLIPBOARD]]

\

This information may prove useful to determine any otherwise unforeseen consequences or problems upon removing a driver. And again, it is also possible to filter your list of installed drivers by whether they are used on hardware connected via pci or usb. In this instance, a detailed list will be generated only for installed drivers used on hardware with a PCI connection:

[user \$ ][ mhwd -li -d \--pci [COPY TO CLIPBOARD]]

\

One other way of reporting drivers installed andin use is using the `inxi` tool.

[user \$ ][ inxi -G [COPY TO CLIPBOARD]]

\

\

**Note**

------------------------------------------------------------------------

The mhwd profile \'video-linux\' corresponds to the latest opensource driver availablefor your hardware.

**Note**

------------------------------------------------------------------------

The mhwd profile \'video-vesa\' is a generic fallback driver which should not be used in the vast majority of cases.

## [Removing Installed Drivers]

**Warning**

------------------------------------------------------------------------

use this command with care!

To remove an installed driver, the syntax is:

[user \$ ][ sudo mhwd -r \[pci or usb\] \[name of driver\] [COPY TO CLIPBOARD]]

\

For example, to remove the installed driver for a nvidia graphics card (connected internally via pci), the following command would be used:

[user \$ ][ sudo mhwd -r pci video-nvidia [COPY TO CLIPBOARD]]

\

# [Checking configuration]

You can check configuration with:

[user \$ ][ sudo mhwd-gpu \--check [COPY TO CLIPBOARD]]

\

[user \$ ][ mhwd-gpu \--status [COPY TO CLIPBOARD]]

\

And if needed fix issues with:

[user \$ ][ sudo mhwd-gpu \--setmod [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo mhwd-gpu \--setxorg \[PATH\] [COPY TO CLIPBOARD]]

\

Make sure the path to xorg config file is valid.

Note about ati, xorg file and login artifacts or kicad: if you get artifacts upon logging in or if kicad rendering and zooming is slow, try adding \[Option \"EXAPixmaps\" \"off\"\] in the \"Device\" section of xorg config file. See [here.](https://wiki.archlinux.org/title/ATI#Performance_and/or_artifacts_issues_when_using_EXA)

# [Dual GPU]

## [PRIME GPU offloading]

If your hardware includes more than one GPU card you can make use of PRIME offloading. PRIME is a technology used to manage hybrid graphics found on recent desktops and laptops (Optimus for NVIDIA, AMD Dynamic Switchable Graphics for Radeon). PRIME detects both cards and automatically selects Intel card by default; using the more powerful discrete graphics card, when called, for more demanding applications.

In Manjaro this will automatically be available for hybrid graphics systems using intel/modesetting for the integrated card and free drivers (AMDGPU or Nouveau) for the dGPU.

You may choose to run a program with a specific GPU, prepending the application\'s command with *DRI_PRIME=x*, where *x* is the card priority number.

For example, to run an application using the second card prepend the application command with **DRI_PRIME=1**

[user \$ ][ DRI_PRIME=1 glxspheres64 [COPY TO CLIPBOARD]]

\

To use the 1st card (usually when the CPU has an embedded GPU, this is used)

[user \$ ][ DRI_PRIME=0 glxspheres64 [COPY TO CLIPBOARD]]

\

If you want to always run some application with the discrete gpu, you may copy that application\'s .desktop file to `~/.local/share/applications/` and edit the \"Exec\" property

[user \$ ][ Exec=DRI_PRIME=1 inkscape [COPY TO CLIPBOARD]]

\

Some applications (usually games like steam) may have an embedded option to specify the command line, where it is preferred to use this way.

For example, in Steam, select a game - that you want to run using your discrete Nvidia card - from the Library page of the Steam client, right-click, and select Properties. Click the SET LAUNCH OPTIONS\... button and specify for the command line options followed by the default launch hook %command%.

    DRI_PRIME=1 %command%

To use the dGPU by default see **[Reverse Prime](https://wiki.archlinux.org/index.php/PRIME#Reverse_PRIME)**

# [][NVIDIA Proprietary (non-free) drivers]

If you have a Nvidia card, you have the option to use the proprietary (closed source = non-free) drivers instead of the open source (free) nouveau driver.

For Legacy/older nvidia cards, Manjaro maintains older drivers for compatibility. In these cases the driver name is different, instead of nvidia it is nvidia-390xx or nvidia340xx, whether in nvidia-only or bumblebee mhwd driver configuration.

When you install the non-free driver, mhwd includes a Nvidia utility \"Nvidia Settings Utility\" that can help you configure several settings. You can find this utility in your GUI Applications Menu or start it from a terminal

[user \$ ][ sudo nvidia-settings [COPY TO CLIPBOARD]]

\

If you are using bumblebee, the nvidia utility needs a special command

[user \$ ][ sudo optirun -b none nvidia-settings -c :8 [COPY TO CLIPBOARD]]

\

## [Nvidia Optimus]

For Optimus laptops or dual GPU hardware with intel and nvidia GPUs, you have three options to utilize the card driver usage at your preference or your hardware capabilities.

**[PRIME](#nvidia-prime) (mhwd default)**

**[Bumblebee](#Bumblebee)**

When you install Manjaro with the non-free option selected from Grub menu, or when you use automatic driver installation, PRIME or bumblebee is installed by default, depending on support for your GPU, PRIME being preferred. In these cases, the mhwd driver is named \"video-hybrid-intel-nvidia-\*\*\*xx-prime\" or \"video-hybrid-intel-nvidia-\*\*\*xx-bumblebee\".

## [][Configure The Resolution/Refresh Rate]

**Warning**

------------------------------------------------------------------------

The method provided does not currently work for the Cinnamon Edition. As soon as a solution is found, then this article will be updated.

\
**1.** Start nvidia-settings utility

**2.** Change resolution and refresh rate in \'X Server Display Configuration\' tab.

**3.** Hit the \'Save to X Configuration File\' button and save to **/etc/X11/mhwd.d/nvidia.conf**

**4.** Now start your terminal and enter the following command to complete the process:

[user \$ ][ sudo mhwd-gpu \--setmod nvidia \--setxorg /etc/X11/mhwd.d/nvidia.conf [COPY TO CLIPBOARD]]

\

## [][Configure X Screen settings (OpenGL Settings, Antialiasing, X Server XVideo)]

**1.** Start nvidia-settings utility

**2.** Change settings in X Server XVideo Settings, OpenGL and Antialiasing, in the \'X Screen\' tab.

**3.** Click on \'nvidia-settings configuration\' tab and click on the \'Save Current Configuration\' button.

**4.** Save the .nvidia-settings-rc to the default location specified (**/home/\[your account name\]**)

**5.** Edit the .xinitrc file with your preferred text editor. For example, if you use gedit, run this in your terminal:

[user \$ ][ gedit \~/.xinitrc [COPY TO CLIPBOARD]]

\

**6.** Once opened, add the following line into the configuration file, before the last line that starts with \'exec\':

    nvidia-settings --load-config-only
    exec $(get_session "$1")

**7.** Save and exit.

## [Nvidia settings for special cases]

In case your monitor is not entering powersave mode (DPMS), try adding \`Option \"HardDPMS\" \"true\"\` in your Xorg monitor section. For example:

      Section "Monitor"
        # HorizSync source: edid, VertRefresh source: edid
        Identifier     "Monitor0"
        VendorName     "Unknown"
        ModelName      "BenQ ZOWIE XL LCD"
        HorizSync       30.0 - 160.0
        VertRefresh     56.0 - 144.0
        Option         "DPMS"
        Option         "HardDPMS" "true"
      EndSection

\
After forum [issue](https://forum.manjaro.org/t/display-does-not-go-to-powersave/84004/5)

\

## [nvidia-prime]

Manjaro also offers an easy way to use PRIME with proprietary Nvidia drivers.\
Simply select and install an \'nvidia-prime\' profile through MSM or mhwd (such as *video-hybrid-intel-nvidia-440xx-prime*) and ensure the package *nvidia-prime* is installed.

Then to use the discrete Nvidia card it works the same as [PRIME offloading](#PRIME_GPU_offloading) above but uses a different command. Prepend the application command with **prime-run**. For example:

[user \$ ][ prime-run glxspheres64 [COPY TO CLIPBOARD]]

\

## [Bumblebee]

Bumblebee configuration is mainly developed to help minimize laptop battery consumption, since Nvidia usually consumes significant power, while Intel cards are more power efficient. So, bumblebee detects both cards and automatically selects Intel card by default and can use the Nvidia for more demanding applications. For an application to use the Nvidia card, prepend the application command with optirun or primusrun. For example:

[user \$ ][ optirun glxspheres64 [COPY TO CLIPBOARD]]

\

[user \$ ][ primusrun inkscape [COPY TO CLIPBOARD]]

\

If you want to specifically run some application with the nvidia driver, you may edit that application\'s .desktop file \"Exec\" property, or run it in terminal like this

     Exec=primusrun chromium

Some applications (usually games like steam) may have an embedded option to specify the command line, where it is preferred to use this way.

For example, in Steam, select a game - that you want to run using your discrete Nvidia card - from the Library page of the Steam client, right-click, and select Properties. Click the SET LAUNCH OPTIONS\... button and specify for the command line options followed by the default launch hook %command%.

    primusrun %command%

\

# [See also]

-   [Manjaro Hardware Detection Overview](//wiki.manjaro.org/index.php?title=Manjaro_Hardware_Detection_Overview "Manjaro Hardware Detection Overview")

\

# [Easier way]

You may use a GUI version of mhwd in [Manjaro Settings Manager#Hardware Detection](//wiki.manjaro.org/index.php?title=Manjaro_Settings_Manager#Hardware_Detection "Manjaro Settings Manager")

With this tool you can:

\- install graphic driver

\- switch graphic driver

[https://www.youtube.com/watch?v=UAFGukpEIJw](https://www.youtube.com/watch?v=UAFGukpEIJw)

\

# [How to check the driver]

[user \$ ][ glxinfo \| grep OpenGL [COPY TO CLIPBOARD]]

\

Example output command:

**Nvidia driver** ( proprietary driver )

\

[\$] [glxinfo \| grep OpenGL]\

OpenGL vendor string: NVIDIA Corporation\
OpenGL renderer string: GeForce GTX 660/PCIe/SSE2\
OpenGL core profile version string: 4.3.0 NVIDIA 331.49\
OpenGL core profile shading language version string: 4.30 NVIDIA via Cg compiler\
OpenGL core profile context flags: (none)\
OpenGL core profile profile mask: core profile\
OpenGL core profile extensions:\
OpenGL version string: 4.4.0 NVIDIA 331.49\
OpenGL shading language version string: 4.40 NVIDIA via Cg compiler\
OpenGL context flags: (none)\
OpenGL profile mask: (none)\
OpenGL extensions:

\
**Nouveau** , **Gallium** from **Mesa** ( open source driver )

\

[\$] [glxinfo \| grep OpenGL]\

OpenGL vendor string: nouveau\
OpenGL renderer string: Gallium 0.4 on NVE6\
OpenGL core profile version string: 3.1 (Core Profile) Mesa 9.2.5\
OpenGL core profile shading language version string: 1.40\
OpenGL core profile context flags: (none)\
OpenGL core profile extensions:\
OpenGL version string: 3.0 Mesa 9.2.5\
OpenGL shading language version string: 1.30\
OpenGL context flags: (none)\
OpenGL extensions:

\
**Intel** driver from **Mesa** ( open driver )

\

[\$] [glxinfo \| grep OpenGL]\

OpenGL vendor string: Intel Open Source Technology Center\
OpenGL renderer string: Mesa DRI Intel(R) Ivybridge Desktop\
OpenGL core profile version string: 3.3 (Core Profile) Mesa 11.0.6\
OpenGL core profile shading language version string: 3.30\
OpenGL core profile context flags: (none)\
OpenGL core profile profile mask: core profile\
OpenGL core profile extensions:\
OpenGL version string: 3.0 Mesa 11.0.6\
OpenGL shading language version string: 1.30\
OpenGL context flags: (none)\
OpenGL extensions:\
OpenGL ES profile version string: OpenGL ES 3.0 Mesa 11.0.6\
OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.00\
OpenGL ES profile extensions:

\

#### [Checking vulkan support]

OpenGL is a graphics API specification and it has been superseded by the Vulkan api. To check support for Vulkan applications, you can install vulkan-tools and run

\

[\$] [vkcube]\

Selected GPU 0: NVIDIA GeForce RTX 3050 Laptop GPU, type: DiscreteGpu

\
With integrated GPU you can select the GPU:

\

[\$] [vkcube \--gpu_number 0]\

Selected GPU 0: NVIDIA GeForce RTX 3050 Laptop GPU, type: DiscreteGpu

\

[\$] [vkcube \--gpu_number 1]\

Selected GPU 1: AMD Radeon Graphics (RADV RENOIR), type: IntegratedGpu

\$