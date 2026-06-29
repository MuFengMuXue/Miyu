This page contains [[changes](https://wiki.gentoo.org/index.php?title=Kernel/Configuration&oldid=1419586&diff=1423921#Configuration_tools)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Kernel/Configuration/de "Kernel/Konfiguration (47% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Kernel/Configuration/es "Núcleo/Configuración (47% translated)")
-   [français](https://wiki.gentoo.org/wiki/Kernel/Configuration/fr "Noyau/Configuration (41% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Kernel/Configuration/it "Kernel/Configurazione (1% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Kernel/Configuration/hu "Kernel/Beállítás (47% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Kernel/Configuration/pl "Kernel/Configuration/pl (1% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Kernel/Configuration/ru "Ядро/Конфигурация (65% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Kernel/Configuration/zh-cn "内核/配置 (34% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Kernel/Configuration/ja "カーネル/コンフィギュレーション (95% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Kernel/Configuration/ko "Kernel/Configuration/ko (35% translated)")

This article describes the manual configuration and setup of the [Linux kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel").

An alternative to manual configuration that uses \'safe defaults\' to build a generic kernel are the [distribution kernels](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel").

## Contents

-   [[1] [Set symlink]](#Set_symlink)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Tools]](#Tools)
    -   [[2.2] [Usage]](#Usage)
    -   [[2.3] [Driver selection]](#Driver_selection)
    -   [[2.4] [Search modules]](#Search_modules)
    -   [[2.5] [Enabling Gentoo Linux common settings]](#Enabling_Gentoo_Linux_common_settings)
    -   [[2.6] [Kbuild]](#Kbuild)
-   [[3] [Build]](#Build)
-   [[4] [Setup]](#Setup)
-   [[5] [Bootloader]](#Bootloader)
-   [[6] [Comparing current kernel configuration with default configuration]](#Comparing_current_kernel_configuration_with_default_configuration)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Set symlink]

The [/usr/src/linux] symlink should always point to the kernel sources that is currently being used. This can be done in one of three ways:

1\. Install the kernel sources with the `symlink` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") active. This will make the [/usr/src/linux] point to the newly installed kernel sources. If necessary, it can still be modified later with the following two methods:

2\. Setting the symlink with the [eselect] tool:

`root `[`#`]`eselect kernel list`

    Available kernel symlink targets:
    [1] linux-6.12.63-gentoo *
    [2] linux-6.12.58-gentoo

This outputs the available kernel sources. The asterisk indicates the chosen sources. To change the kernel sources, e.g. to the second entry, do:

`root `[`#`]`eselect kernel set 2`

3\. Setting the symlink manually:

`root `[`#`]`ln -sf /usr/src/linux-6.12.63-gentoo /usr/src/linux `

`root `[`#`]`ls -l /usr/src/linux `

    lrwxrwxrwx 1 root root 11 Aug 29 22:10 /usr/src/linux -> /usr/src/linux-6.12.63-gentoo

## [Configuration]

### [Tools]

The kernel offers several user facing tools with which to configure itself. The following table is an excerpt of commonly used commands for configuration. See [the upstream documentation](https://docs.kernel.org/admin-guide/README.html#configuring-the-kernel) for the full list.

  ------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Command                                                                                                            Description
  [make config]           Text based configuration. The options are prompted one after another. All options need to be answered, and out-of-order access to former options is not possible.
  [make menuconfig]       An ncurses-based pseudo-graphical menu (only text input). Navigate through the menu to modify the desired options.
  [make defconfig]        Generates a new config with default from the ARCH supplied defconfig file. Use this option to get back the default configuration file that came with the sources.
  [make nconfig]          Pseudo-graphical menu based on ncurses. Requires [[[sys-libs/ncurses]](https://packages.gentoo.org/packages/sys-libs/ncurses)[]] to be installed.
  [make xconfig]          Graphical menu using Qt5. Requires [[[dev-qt/qtwidgets]](https://packages.gentoo.org/packages/dev-qt/qtwidgets)[]] to be installed.
  [make gconfig]          Graphical menu using GTK. Requires [[[x11-libs/gtk+]](https://packages.gentoo.org/packages/x11-libs/gtk+)[]], [[[dev-libs/glib]](https://packages.gentoo.org/packages/dev-libs/glib)[]], and [[[gnome-base/libglade]](https://packages.gentoo.org/packages/gnome-base/libglade)[]] to be installed.
  [make oldconfig]        Review changes between kernel versions and update to create a new [.config] for the kernel.
  [make olddefconfig]     Generates a new configuration with default values from the ARCH supplied defconfig file while, at the same time, maintaining all the previous options set in the [.config] file found at [/usr/src/linux/.config]. This is a fast and safe method for upgrading a config file that has all the configuration options it needs for hardware support while at the same time gaining bug fixes and security patches.
  [make localmodconfig]   Creates a config based on the current config and the currently loaded modules, as viewable via the [lsmod] command.
  [make allyesconfig]     Enables all configuration options in the kernel. It will set *all* kernel options to `*`. Make sure a backup of the current kernel configuration is acquired before using this option!
  [make allmodconfig]     Enables all modules in kernel. Note that this operation will consume quite a bit of disk space.
  ------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are also several scripts to create miscellaneous default configurations. These can make deeper configuration more time efficient. Run the following command for a full list of make targets:

`root `[`#`]`make help`

The remainder of this article will describe configuration using the [make menuconfig] tool, but the procedure is similar for the other kernel build tools.

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make menuconfig`

### [Usage]

In the shown menu the blue bar indicates the cursor position. The [↑] and [↓] arrow keys change cursor position. The [←] and [→] arrow keys traverse the menu bar in the bottom and define what happens when the [Enter] key is pressed. For the menu bar below, **Select** switches to a sub menu for the menu entries ending with **\-\--\>** while **Exit** exits a sub menu. As an alternative, the [Esc] key can be pressed twice to exit the sub menu, dialog or the entire application.

Pressing an associated letter key [A]-[Z] will move the position of the cursor lines that have characters in bold. The [Y], [M], [N] keys are excluded from navigation in this way; they are sanctified for other purposes. If a line begins with a Y, M, or N, the next character will be bold and capable of being jumped to. For example, relative to the cursor\'s current position, if the next line reads \"N**e**twork Device Support \-\--\>\" pressing the [E] key will move the cursor to that line.

The following symbols can appear in front of the lines in the menus:

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Symbol(s)                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `[ ], [*]`                        | Options in square brackets can be activated or deactivated. The asterisk marks the menu entry as activated. The value can be changed with the [space] key. It is also possible to press [Y] key (**Y**es) to activate or [N] key (**N**o) to deactivate the selected entry. |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                   | If the option is activated, the selected feature/driver will be built into the kernel and will always be available at boot time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `< >, <M>, <*>`                   | Options in angle brackets can be activated or deactivated, but also activated as module (indicated by a *M*). The values can be modified by pressing [Y]/[N] keys as before or by pressing the [M] key to activate the feature/driver as a module.                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                   | See the [Kernel Modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules") article for differentiation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `, `                        | Options in curly brackets can be activated or activated as module but not be deactivated. This happens because another feature/driver is dependent on this feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-M-, -*-`                        | Options between hyphens are activated in the shown way by another feature/driver. There is no choice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Furthermore some menu entries have a tag at the end:

  ------------------ ------------------------------------------------------------------
  Tag                Description
  `(NEW)`            This driver is new in the kernel and is maybe not stable enough.
  `(EXPERIMENTAL)`   This driver is experimental and most likely not stable enough.
  `(DEPRECATED)`     This driver is deprecated and not needed for most systems.
  `(OBSOLETE)`       This driver is obsolete and should not be activated.
  ------------------ ------------------------------------------------------------------

Most options have a description, which see by pressing the [H] key or choosing **Help** in the menu bar.

### [Driver selection]

See the [hardware detection](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") article and the articles in the [hardware category](https://wiki.gentoo.org/wiki/Category:Hardware "Category:Hardware").

### [Search modules]

Within `make menuconfig`, use the [/] key to search modules and config options by name.

As shown below, the search result will show numbers in front of the matches. Pressing [1] in the example below would make [make menuconfig] jump straight to the option *Bluetooth device drivers* in the menu structure.

[KERNEL] **Example output after searching for HCIBTUSB**

    Symbol: BT_HCIBTUSB [=m]
    Type  : tristate
    Prompt: HCI USB driver
      Location:
        -> Networking support (NET [=y])
          -> Bluetooth subsystem support (BT [=y])
    (1)     -> Bluetooth device drivers
      Defined at drivers/bluetooth/Kconfig:5
      Depends on: NET [=y] && BT [=y] && USB [=m]

### [Enabling Gentoo Linux common settings]

There is a kernel configuration option called `CONFIG_GENTOO_LINUX` only present in [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] and other [Kernel Project](https://wiki.gentoo.org/wiki/Project:Kernel "Project:Kernel") maintained kernels. It does nothing on its own, but sets various required configuration options for typical installations.

This setting automatically selects `tmpfs` and `devtmpfs` support, which are needed for handling [/dev] on Gentoo Linux, but might be expanded in the future to enable other mandatory settings for a Gentoo Linux system. For more information, read the help information available through the kernel configuration system as described earlier in this guide.

### [Kbuild]

** Warning**\
Be very careful of changing environment variables as it may break the kernel in unexpected ways. **DO NOT MIX** GNU binutils and LLVM binutils!!! For example [make CC=gcc LD=ld.lld AR=llvm-ar] will not work because LLVM\'s ar and ld is not compatible with GCC.

The [**K**ernel **build**](https://www.kernel.org/doc/html/latest/kbuild/index.html) system can be used to change how Kernel builds in a more advanced way than [make \*config], similar to [GNU Make](https://www.gnu.org/software/make/manual/html_node/index.html). Kbuild also support [Environment Variables](https://www.kernel.org/doc/html/latest/kbuild/kbuild.html) like `LLVM=1`. For example, the kernel will be build with LLVM and with aggressive optimization flags:

`root `[`#`]`make LLVM=1 KCFLAGS="-O3 -march=native -pipe"`

** Note**\
Additional variables are explained in [Clang/LLVM](https://wiki.gentoo.org/wiki/Kernel/Optimization#Clang.2FLLVM "Kernel/Optimization").

## [Build]

After configuration has been accomplished successfully, compile the kernel:

`root `[`#`]`make -j$(nproc) `

**-j\$(nproc)** tells make to use all available CPU cores to speed up compiling.

## [Setup]

If drivers are activated as modules, they must be installed:

`root `[`#`]`make modules_install`

The modules will be copied to a sub directory of [/lib/modules] by default, but can be changed using the [`MODLIB`](https://www.kernel.org/doc/html/latest/kbuild/kbuild.html#modlib) environment variable.

** Note**\
If you have enabled the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] to automate initramfs generation during [make install], it is recommended to run

`root `[`#`]`emerge --ask @module-rebuild`

before installing the kernel. This ensures that all external kernel modules (e.g., *NVIDIA*, *ZFS*) are rebuilt and included in the initramfs, preventing potential boot issues or missing functionality. Otherwise (if the flag isn\'t set), you can rebuild external modules later, but before regenerating the initramfs (e.g., using [dracut \--force]). This ensures that the updated modules are included in the initramfs.

To install the actual kernel:

`root `[`#`]`make install`

This command executes [/sbin/installkernel], which is part of the [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] package. See the [installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") page for more details on how it can be configured.

## [Bootloader]

Change the system\'s [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") configuration to load the kernel at system boot.

When the bootloader step has been finished, restart the system with the new kernel.

## [Comparing current kernel configuration with default configuration]

Use the following procedure to get an overview of the kernel configuration settings that deviate from the default. Keep in mind that the modification of one configuration setting may alter additional configuration settings.

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`cp -p .config ../.config.working `

`root `[`#`]`make defconfig `

`root `[`#`]`mv .config ../.config.default `

`root `[`#`]`cp -p ../.config.working .config `

`root `[`#`]`cd .. `

`root `[`#`]`/usr/src/linux/scripts/diffconfig .config.working .config.default > .config.diff `

The search function in [make menuconfig] can be used to look up the symbols and their interpretations. When you\'re done, clean up:

`root `[`#`]`cd /usr/src/ `

`root `[`#`]`rm .config.working .config.default .config.diff `

## [See also]

-   [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") --- a central part of the Gentoo [operating system (OS)](https://en.wikipedia.org/wiki/operating_system "wikipedia:operating system")
-   [Kernel/Gentoo Kernel Configuration Guide](https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide "Kernel/Gentoo Kernel Configuration Guide") --- aims to introduce the concepts of **manual kernel configuration** and details some of the most common configuration pitfalls.
-   [Project:Distribution Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") --- maintains sys-kernel/\*-kernel packages.

## [External resources]

-   [Building the kernel as root can be harmful](https://forums.gentoo.org/viewtopic-t-1064076.html)
-   [Modprobed-db](https://github.com/graysky2/modprobed-db) - logs every module that is modprobed to be used to make a custom config