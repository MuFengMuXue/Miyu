**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Loadable_kernel_module "wikipedia:Loadable kernel module")

**Kernel modules** are object files that contain code to extend the [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") of an operating system. Kernel modules are used to add support for new [hardware](https://wiki.gentoo.org/wiki/Category:Hardware "Category:Hardware") and/or [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem"), or for adding system calls. Modules can be built into the kernel or compiled as loadable kernel modules.

Most modern Gentoo installations will use a device manager, such as [udev](https://wiki.gentoo.org/wiki/Udev "Udev"), to automatically load and manage kernel modules, thus module loading will often need no particular configuration.

Gentoo installs, except from [Gentoo Prefix](https://wiki.gentoo.org/wiki/Project:Prefix "Project:Prefix"), have the [[[virtual/dev-manager]](https://packages.gentoo.org/packages/virtual/dev-manager)[]] virtual package in the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), which often resolves to [[[virtual/udev]](https://packages.gentoo.org/packages/virtual/udev)[]] by default. virtual/udev has an \"any of many\" dependency on [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]], and [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]] (for non-systemd systems).

## Contents

-   [[1] [About loadable kernel modules]](#About_loadable_kernel_modules)
-   [[2] [Managing kernel modules]](#Managing_kernel_modules)
    -   [[2.1] [View running modules]](#View_running_modules)
    -   [[2.2] [List available modules]](#List_available_modules)
    -   [[2.3] [Load specific modules during boot]](#Load_specific_modules_during_boot)
    -   [[2.4] [Blacklist modules]](#Blacklist_modules)
    -   [[2.5] [Manual loading]](#Manual_loading)
-   [[3] [Installing a kernel module]](#Installing_a_kernel_module)
    -   [[3.1] [Making a kernel module accessible]](#Making_a_kernel_module_accessible)
        -   [[3.1.1] [Making a module from kernel configuration]](#Making_a_module_from_kernel_configuration)
    -   [[3.2] [Recompiling the kernel for a new module]](#Recompiling_the_kernel_for_a_new_module)
-   [[4] [Going completely \"module-less\"]](#Going_completely_.22module-less.22)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Kernel modules fail to automatically load]](#Kernel_modules_fail_to_automatically_load)
    -   [[5.2] [Disable Module Loading at Boot]](#Disable_Module_Loading_at_Boot)
-   [[6] [See also]](#See_also)

## [About loadable kernel modules]

Many loadable kernel modules (LKMs) may also be compiled \"in-kernel\". See [configuring a kernel](https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide#Built-in_vs_modular "Kernel/Gentoo Kernel Configuration Guide") on how to select either built-in and LKM options.

Using LKMs can result in a smaller kernel memory footprint, by not having unneeded modules loaded: modules can be loaded on demand by [udev](https://wiki.gentoo.org/wiki/Udev "Udev") (for example DVB drivers for a DVB stick). Compile-in-kernel code will not be able to be reloaded while the kernel is running, but LKMs can sometimes be used to solve certain issues, by unloading and reloading them.

Using a module rather than building code into the kernel also permits the setting of module-specific parameters, through the [/etc/modprobe.d] file - see [man modprobe.d].

Modules needed early in the boot process may require an update of the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") after a kernel update or recompilation (e.g. filesystem drivers for filesystems used for boot). Some LKMs may incur a slight performance penalty over built-in code, due to the addition of an API layer and slightly more memory usage.

Beware of file system module *X* located on a partition formatted with *X* (unbootable system at worst).

## [Managing kernel modules]

### [View running modules]

To list currently loaded modules, run [lsmod].

To see all modules built into the currently running kernel:

`root `[`#`]`cat /lib/modules/$(uname -r)/modules.builtin`

### [List available modules]

To see all the modules available to be loaded:

`root `[`#`]`find /lib/modules/$(uname -r) -type f -name '*.ko*'`

### [Load specific modules during boot]

Occasionally, modules other than those automatically loaded are desired. Loadable modules can be defined in [.conf] files in the [/etc/modules-load.d/] directory in order to load them during the init portion of the system boot process. Both OpenRC and systemd will look in this path. Each module is listed one per-line. For example:

[FILE] **`/etc/modules-load.d/networking.conf`**

    tun
    e1000e
    brcmfmac

### [Blacklist modules]

To prevent a module from loading, add it by name to a file in [/etc/modprobe.d/] and precede each module name with the `blacklist` keyword:

[FILE] **`/etc/modprobe.d/blacklist.conf`**

    blacklist uhci_hcd
    blacklist nvidia

Note that this does not prevent the [root] user from manually loading the module, it only prevents the module from autoloading at boot. To ensure the module can never be loaded, instead use:

[FILE] **`/etc/modprobe.d/blacklist.conf`**

    install uhci_hcd /bin/false
    install nvidia /bin/false

More information on module blacklisting via [/etc/modprobe.d/] can be found by reading the modprobe.d(5) man page:

`user `[`$`]`man 5 modprobe.d`

Alternatively, kernel modules can be blacklisted from the secondary [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") (see [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), [systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot"), etc.) via parameters passed to the kernel from the kernel command-line. For example, to blacklist the [evbug.ko], [nvidiafb.ko], and [nvidia.ko] kernel modules using command-line parameters:

    module_blacklist=evbug,nvidiafb,nvidia

More details on backlisting via kernel command-line parameters can be found in the [upstream kernel documentation](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html) (search for *module_blacklist*).

### [Manual loading]

A module can be loaded or unloaded manually by the [modprobe] command. For example, to unload the `nvidia` module and load the `nouveau` module, run:

`root `[`#`]`modprobe -r nvidia `

`root `[`#`]`modprobe nouveau `

See [man modprobe].

## [Installing a kernel module]

This section pertains to the installation of a part of a kernel as a module. For example, if one requires a driver to be installed as a module, it may be of use to follow some of the instructions following.

### [Making a kernel module accessible]

** Tip**\
It is possible to filter for certain keywords by piping the find command into a grep command. An example can be [find /lib/modules/\$(uname -r) -type f -name \'\*.ko\*\' ] to find sound kernel driver modules, etc.

A kernel module must first be present and accessible before it is installed. Sometimes, a kernel module is already present and accessible, but sometimes it isn\'t. To check for such a condition, run the following and search for the desired kernel module:

`root `[`#`]`find /lib/modules/$(uname -r) -type f -name '*.ko*'`

#### [Making a module from kernel configuration]

If the desired kernel module isn\'t present, it may be built-in to the kernel. Find the configuration in [/usr/src/linux/.config], and set it to `m` instead of `y` like so.

[FILE] **`/usr/src/linux/.config`Setting a configuration in a kernel to be a module**

    # Replace SETTING in CONFIG_SETTING with the real setting desired to be set as a module
    CONFIG_SETTING=m

### [Recompiling the kernel for a new module]

Once a kernel configuration has been set to a module, or a new module has been installed, it is necessary to recompile the kernel and install the modules as well in order to make the new kernel module accessible and ready to be added to the list of running drivers with [modprobe]. Run the following commands to recompile the kernel and install its modules.

** Tip**\
It is an optional, but recommended addition to run [mount /dev/sda1 /boot] before commencing with the kernel recompilation. Consider it if the results have not worked without it, and retry later.

Move the working directory to [/usr/src/linux] with [cd /usr/linux], with the [/linux] directory being the directory of the system\'s kernel.

`root `[`#`]`make`

`root `[`#`]`make modules_install`

`root `[`#`]`make install`

Once the kernel has been successfully recompiled, reboot the system, and load the kernel module as per the instructions found earlier in this article.

## [][Going completely \"module-less\"]

** Important**\
This is an advanced topic and not recommended for general use. Modules, in general, make certain drivers easier to load. Also, it is possible to reload a misbehaving driver without reboot by removing and reloading the driver module.

If, for some reason, there is a desire to have a completely module-less system, disable loadable module support in the kernel configuration (making sure to build-in any required drivers/features, of course). Setting `CONFIG_MODULES=n` will disable loadable module support:

[KERNEL] **Disable loadable module support (`CONFIG_MODULES`)**

    [ ] Enable loadable module support  ----

With a module-less kernel, it is possible to dispense the userspace programs that manage loadable modules (e.g. [lsmod], [modprobe], etc). To do this, remove `kmod` support from packages that use it, and also remove the [[[sys-apps/kmod]](https://packages.gentoo.org/packages/sys-apps/kmod)[]] package. Because [[[sys-apps/kmod]](https://packages.gentoo.org/packages/sys-apps/kmod)[]] is part of the system set, it must first be removed from the set before it can be unmerged.

First, add `-kmod` to the system\'s USE flags in [/etc/portage/make.conf].

Next, rebuild installed packages without kmod support:

`root `[`#`]`emerge --ask --deep --newuse --update --verbose @world`

Follow any special instructions given by rebuilt packages (for example, if udev was rebuilt, then restart it according to the instructions in the [emerge] output).

Now add `-*sys-apps/kmod` to [/etc/portage/profile/packages] (create the [profile] directory and [packages] file if they don\'t exist). This removes the [[[sys-apps/kmod]](https://packages.gentoo.org/packages/sys-apps/kmod)[]] package from the system set.

Then unmerge the [[[sys-apps/kmod]](https://packages.gentoo.org/packages/sys-apps/kmod)[]] package:

`root `[`#`]`emerge -ac`

If the above command doesn\'t remove kmod, then some package still depends on it even with the `-kmod` USE flag set. Run [emerge -pvc sys-apps/kmod] to find out which package still depends on kmod.

If a kernel was installed with modules, then also remove the [/lib/modules/\<kernel-version\>] directory. Since the kernel was built without any loadable modules, there won\'t be anything useful in there anymore.

When using a [[genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel")] generated initramfs, it may be necessary to add `nomodules` to the kernel command line in the system\'s bootloader (e.g. GRUB) configuration so that the initramfs does not waste any time looking for modules to load.

## [Troubleshooting]

### [Kernel modules fail to automatically load]

Ensure that *CONFIG_MODPROBE_PATH* points to the correct location for the *modprobe* binary:

[KERNEL] **CONFIG_MODPROBE_PATH**

    CONFIG_MODPROBE_PATH="/sbin/modprobe"

### [Disable Module Loading at Boot]

In some rare cases it may be necessary to temporarily disable module loading entirely. This is not generally recommended as a way to solve module issues; if any modules are required from initramfs to boot, they will not be loaded. But, this may be useful in cases where only one kernel is available, and that kernel was rebuilt without re-installing its modules. It is best to have backup kernels to handles this case, but if no backups exist, module loading can be temporarily disabled with the following kernel command-line parameter:

    nomodule

\

## [See also]

-   [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") --- a central part of the Gentoo [operating system (OS)](https://en.wikipedia.org/wiki/operating_system "wikipedia:operating system")
-   [Signed kernel module support](https://wiki.gentoo.org/wiki/Signed_kernel_module_support "Signed kernel module support") --- allows further hardening of the system by disallowing unsigned kernel modules, or kernel modules signed with the wrong key, to be loaded.