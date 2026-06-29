This page contains [[changes](https://wiki.gentoo.org/index.php?title=Genkernel&oldid=1408454&diff=1421667)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Genkernel/de "Genkernel (11% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Genkernel/es "Genkernel (34% translated)")
-   [français](https://wiki.gentoo.org/wiki/Genkernel/fr "genkernel/fr (34% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Genkernel/it "Genkernel (4% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Genkernel/hu "Genkernel (71% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Genkernel/pt-br "Genkernel (5% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Genkernel/ru "genkernel (44% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Genkernel/ta "Gen kernel (11% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Genkernel/zh-cn "Genkernel (21% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Genkernel/ja "genkernel (52% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Genkernel/ko "Genkernel/ko (33% translated)")

*Not to be confused with [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit").*

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Genkernel "Project:Genkernel")][Project](https://wiki.gentoo.org/wiki/Project:Genkernel "Project:Genkernel")

[[]][Package information](https://packages.gentoo.org/packages/sys-kernel/genkernel)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Genkernel "wikipedia:Genkernel")

[[]][GitWeb](https://gitweb.gentoo.org/proj/genkernel.git)

[[]][GitHub](https://github.com/gentoo/genkernel)

**Article status**

[[]]This article has some todo items:\

-   Article must be updated for genkernel-4 in general

<!-- -->

-   Add documentation for \--boot-font feature

<!-- -->

-   Add documentation for \--bcache feature

<!-- -->

-   Add documentation for gk.keep feature (including /etc/initramfs.mounts)

** Warning**\
[genkernel] is unmaintained; documentation presented here may be incomplete and may not reflect the current state of Gentoo tooling. Users encountering issues with genkernel will be asked to use another tool. Please see the [Distribution kernel](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel#Distribution_kernels "Handbook:AMD64/Installation/Kernel") section in the Handbook for a supported alternative.

[genkernel] is a tool created by Gentoo used to automate the build process of the [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") and [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). Some of the general features include:

-   Configuring the kernel sources.
-   Building the compressed kernel [bzImage] and copying it to [/boot].
-   Creating an initramfs and copying it to [/boot].
-   Creating symlinks in [/boot].
-   Adding custom content to the initramfs such as encryption related files, boot splash images, extra modules, and more.
-   Configuring the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") to boot the newly created kernel and initramfs.

** Note**\
To use [/efi] instead of [/boot] for newer UEFI systems, see [Changing the boot directory to /efi](#Changing_the_boot_directory_to_.2Fefi).

** Note**\
It is a common misconception that [genkernel] will \"automatically\" generate a *custom* kernel configuration. [genkernel] automates the kernel build process and assembles the initramfs, but does **not** generate a *custom* kernel configuration file. If a kernel configuration is not provided, [genkernel] will use a generic kernel configuration file which will produce a general purpose kernel suitable for daily usage (at the expense of a large modular kernel).

\
Same is true for [genkernel]\'s initramfs: Its primary job is to bring up only the basic stuff needed to mount a (block) device containing the root filesystem so that it can hand off control to real system as soon as possible.

It is **not** [genkernel]\'s goal to load all available modules, to start all available devices, to unlock additional volumes, to start network or do other fancy stuff. So don\'t forget to set up normal boot services so that the real system can finish boot and do all of the things mentioned above.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Options]](#Options)
        -   [[2.1.1] [Options acting on user interactivity]](#Options_acting_on_user_interactivity)
        -   [[2.1.2] [Options acting on the resulting system]](#Options_acting_on_the_resulting_system)
        -   [[2.1.3] [Options acting on the choice of the tools used for building]](#Options_acting_on_the_choice_of_the_tools_used_for_building)
        -   [[2.1.4] [Options acting on the compilation process]](#Options_acting_on_the_compilation_process)
        -   [[2.1.5] [Debugging options]](#Debugging_options)
    -   [[2.2] [Actions]](#Actions)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Starting off]](#Starting_off)
    -   [[3.2] [Changing the boot directory to /efi]](#Changing_the_boot_directory_to_.2Fefi)
    -   [[3.3] [Changing the kernel]](#Changing_the_kernel)
        -   [[3.3.1] [File management]](#File_management)
            -   [[3.3.1.1] [Source files]](#Source_files)
            -   [[3.3.1.2] [Kernel configuration file]](#Kernel_configuration_file)
            -   [[3.3.1.3] [Saving the compiled configuration]](#Saving_the_compiled_configuration)
            -   [[3.3.1.4] [Installing the kernel and initramfs into the /boot directory]](#Installing_the_kernel_and_initramfs_into_the_.2Fboot_directory)
        -   [[3.3.2] [Configuring the bootloader]](#Configuring_the_bootloader)
            -   [[3.3.2.1] [extlinux]](#extlinux)
            -   [[3.3.2.2] [GRUB Legacy]](#GRUB_Legacy)
            -   [[3.3.2.3] [GRUB]](#GRUB)
            -   [[3.3.2.4] [systemd-boot]](#systemd-boot)
        -   [[3.3.3] [Preserving the working files]](#Preserving_the_working_files)
        -   [[3.3.4] [Using previous kernel configuration while changing the sources]](#Using_previous_kernel_configuration_while_changing_the_sources)
        -   [[3.3.5] [Checking that initramfs includes necessary modules/utilities before booting]](#Checking_that_initramfs_includes_necessary_modules.2Futilities_before_booting)
            -   [[3.3.5.1] [Using lsinitrd]](#Using_lsinitrd)
            -   [[3.3.5.2] [Manual extraction]](#Manual_extraction)
    -   [[3.4] [Microcode loading]](#Microcode_loading)
        -   [[3.4.1] [Microcode loading support in kernel]](#Microcode_loading_support_in_kernel)
        -   [[3.4.2] [Embedding microcode updates into initramfs]](#Embedding_microcode_updates_into_initramfs)
    -   [[3.5] [Firmware loading]](#Firmware_loading)
    -   [[3.6] [Remote rescue shell]](#Remote_rescue_shell)
        -   [[3.6.1] [Pre-requirement for SSH daemon support in initramfs]](#Pre-requirement_for_SSH_daemon_support_in_initramfs)
        -   [[3.6.2] [Adding SSH support to initramfs]](#Adding_SSH_support_to_initramfs)
        -   [[3.6.3] [Enabling SSH daemon on boot]](#Enabling_SSH_daemon_on_boot)
        -   [[3.6.4] [Remote unlock]](#Remote_unlock)
            -   [[3.6.4.1] [Manual unlock]](#Manual_unlock)
            -   [[3.6.4.2] [Automatic unlock]](#Automatic_unlock)
    -   [[3.7] [Network booting]](#Network_booting)
        -   [[3.7.1] [From an installation CD]](#From_an_installation_CD)
        -   [[3.7.2] [Building the kernel and initramfs with netboot support]](#Building_the_kernel_and_initramfs_with_netboot_support)
        -   [[3.7.3] [NFS setup]](#NFS_setup)
        -   [[3.7.4] [DHCP setup]](#DHCP_setup)
        -   [[3.7.5] [Netbooting instructions]](#Netbooting_instructions)
        -   [[3.7.6] [Booting a genkernel initramfs]](#Booting_a_genkernel_initramfs)
            -   [[3.7.6.1] [Introduction]](#Introduction)
            -   [[3.7.6.2] [Loading LVM or software-RAID]](#Loading_LVM_or_software-RAID)
            -   [[3.7.6.3] [Booting in single-user mode]](#Booting_in_single-user_mode)
    -   [[3.8] [Cross-compile support]](#Cross-compile_support)
    -   [[3.9] [Initramfs kernel command-line parameters]](#Initramfs_kernel_command-line_parameters)
-   [[4] [FAQ]](#FAQ)
    -   [[4.1] [Can genkernel be used for systemd-based systems?]](#Can_genkernel_be_used_for_systemd-based_systems.3F)
    -   [[4.2] [Genkernel? Dracut?]](#Genkernel.3F_Dracut.3F)
    -   [[4.3] [Can a separate kernel/initramfs be created for tests?]](#Can_a_separate_kernel.2Finitramfs_be_created_for_tests.3F)
    -   [[4.4] [How can external modules (such as xtables-addons, nvidia-drivers\...) be rebuilt for a new kernel?]](#How_can_external_modules_.28such_as_xtables-addons.2C_nvidia-drivers....29_be_rebuilt_for_a_new_kernel.3F)
    -   [[4.5] [How can additional commands be run after building the kernel?]](#How_can_additional_commands_be_run_after_building_the_kernel.3F)
    -   [[4.6] [How can ccache or distcc be used with genkernel?]](#How_can_ccache_or_distcc_be_used_with_genkernel.3F)
    -   [[4.7] [ERROR: compile_kernel(): compile_generic() failed to compile the \"bzImage\" target!]](#ERROR:_compile_kernel.28.29:_compile_generic.28.29_failed_to_compile_the_.22bzImage.22_target.21)
    -   [[4.8] [Is the order of kernel command-line arguments important?]](#Is_the_order_of_kernel_command-line_arguments_important.3F)
    -   [[4.9] [Required kernel option \'CONFIG_MICROCODE_INTEL\' or \'CONFIG_MICROCODE_AMD\' which genkernel tried to set is missing!]](#Required_kernel_option_.27CONFIG_MICROCODE_INTEL.27_or_.27CONFIG_MICROCODE_AMD.27_which_genkernel_tried_to_set_is_missing.21)
    -   [[4.10] [Help! Something isn\'t working!]](#Help.21_Something_isn.27t_working.21)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-kernel/genkernel](https://packages.gentoo.org/packages/sys-kernel/genkernel) [[]] [Gentoo automatic kernel building scripts]

  --------------------------------------------------------------- --------------------------------------------------------------------------------------------------
  [`+firmware`](https://packages.gentoo.org/useflags/+firmware)   Prefer system firmware sys-kernel/linux-firmware over local copy.
  [`ibm`](https://packages.gentoo.org/useflags/ibm)               Add support for IBM ppc64 specific systems
  [`systemd`](https://packages.gentoo.org/useflags/systemd)       Enable use of systemd-specific libraries and features like socket activation or session tracking
  --------------------------------------------------------------- --------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 19:05] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Initiate the installation of genkernel:

`root `[`#`]`emerge --ask sys-kernel/genkernel`

## [Usage]

The general form of genkernel invocation is as follows:

`root `[`#`]`genkernel [options ...] action`

### [Options]

The actual behavior of genkernel depends on a large variety of options, the majority of which can be set/unset in the [/etc/genkernel.conf] file or passed via the [genkernel] command on each invocation. Options passed over the command line take precedence over options defined in [/etc/genkernel.conf]. The configuration file is very well documented, however some of the most commonly used options will be explored in this article. The goal is for the reader to be familiar with common genkernel invocations. For a more complete set of explanations refer to the comments in [/etc/genkernel.conf] itself or to the output of [man genkernel].

** Note**\
Some of the options have a variant that triggers a converse behavior figured as `--[no-]option_name`, and the converse effect is shown in square brackets as in the following example:

[CODE] **Enable or disable a certain option**

    --[no-]menuconfig : Activates [deactivates] ...

Where options have only a negative effect, the `no-`, and its effect, which are not optional in this case, are figured without square brackets.

#### [Options acting on user interactivity]

The configuration options listed below help the user decide how to interact with the configuration process. Users can even choose whether or not the configuration file created in the process should be saved. The following are considered primary configuration options:

`--config=/path/to/genkernel.conf`

<!-- -->

`--kernel-config=/path/to/kernel.config`

<!-- -->

`--[no-]menuconfig`

<!-- -->

`--gconfig`

<!-- -->

`--xconfig`

<!-- -->

`--[no-]save-config`

<!-- -->

`--kernel-append-localversion=-mycfg42`

#### [Options acting on the resulting system]

The configuration options listed here defines which features will or will not be enabled in the resulting kernel and initrd/[initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs").

`--[no-]splash`

<!-- -->

`--splash-res=PreferredResolution`

<!-- -->

`--do-keymap-auto`

<!-- -->

`--keymap`

<!-- -->

`--lvm`

<!-- -->

`--dmraid`

<!-- -->

`--luks`

<!-- -->

`--iscsi`

<!-- -->

`--multipath`

<!-- -->

`--linuxrc=/path/to/the/linuxrc_file`

<!-- -->

`--cachedir=/path/to/alt/dir`

<!-- -->

`--tmpdir=/path/to/new/tempdir`

<!-- -->

`--unionfs`

<!-- -->

`--mountboot`

<!-- -->

`--microcode`

#### [Options acting on the choice of the tools used for building]

The following options are supported by genkernel, and are passed to the relevant applications while the kernel is being assembled. The options affect low level kernel compilation tools.

`--kernel-cc=someCompiler`

<!-- -->

`--kernel-ld=someLinker`

<!-- -->

`--kernel-as=someAssembler`

<!-- -->

`--kernel-make=someMake`

<!-- -->

`--utils-cc=someCompiler`

<!-- -->

`--utils-ld=someLinker`

<!-- -->

`--utils-as=someAssembler`

<!-- -->

`--utils-make=someMake`

<!-- -->

`--makeopts=-jX`

#### [Options acting on the compilation process]

The following options usually take effect during the actual compilation:

`--kerneldir=/path/to/sources/`

<!-- -->

`--kernel-config=/path/to/config-file`
    :::
    ** Tip**\
    Use `--kernel-config=/proc/config.gz` to start building a new kernel based on kernel configuration from currently running kernel.\
    Note: This will only work if current active kernel was built with `CONFIG_IKCONFIG=y` which is normally the case.
    :::

<!-- -->

`--module-prefix=/path/to/prefix-directory/`

<!-- -->

`--[no-]clean`

<!-- -->

`--[no-]mrproper`

<!-- -->

`--oldconfig`

<!-- -->

`--[no-]module-rebuild`

<!-- -->

`--callback="echo hello"`
    :::
    ** Note**\
    Before genkernel-4, this callback was used to trigger rebuild of out-of-tree modules. Since genkernel-4, a dedicated command-line parameter `--module-rebuild` was introduced, see above.
    :::

<!-- -->

`--[no-]install`

<!-- -->

`--no-ramdisk-modules`

<!-- -->

`--all-ramdisk-modules`

<!-- -->

`--genzimage`

#### [Debugging options]

The use of debugging options during the kernel compilation process controls the amount of information reported, as well as the presentation of said data.

`--loglevel=<0|1|2|3|4|5>`
    :::
    ** Note**\
    Genkernel will always log complete output to [/var/log/genkernel.log] by default. `--loglevel` only controls output shown on screen.
    :::

<!-- -->

`--logfile=/path/to/output_file`

<!-- -->

`--[no-]color`

<!-- -->

`--[no-]cleanup`

### [Actions]

The action passed on the command line with the [genkernel \[options ...\] *action*] tells genkernel what action to perform. The following actions are supported:

  -------------------------------------------------------------------------------------------------------- -------------------------------------------------------------
  Action                                                                                                   Description
  [all]         Builds all stages --- the initrd, kernel image and modules.
  [bzImage]     Only builds the kernel image.
  [kernel]      Only builds the kernel image and modules.
  [initramfs]   Only builds the initramfs/ramdisk image.
  [ramdisk]     Only builds the initramfs/ramdisk image.
  -------------------------------------------------------------------------------------------------------- -------------------------------------------------------------

## [Configuration]

### [Starting off]

Although there are several ways to run genkernel, the least-intrusive approach recommended for most users is provided by [genkernel all]. Here, a generic configuration which works well for most systems is used. As was mentioned earlier, this approach is not without drawbacks; most of the modules created are useless to the average user and may increase compile time. Below is an illustration of a more efficient approach, achieved by passing certain options to genkernel as root:

`root `[`#`]`genkernel --luks --no-install --no-clean --menuconfig all`

The above operation causes genkernel to create a kernel capable to open LUKS and LUKS2 encrypted volumes, compile and embed [cryptsetup] into initramfs (`--luks`), both kernel and initramfs will have to be manually installed (`--no-install`). While preparing the kernel source tree, genkernel will refrain from cleaning out any preexisting object files present in the source tree (`--no-clean`). A menu-driven kernel configuration utility will be displayed that allows the user to select which modules will be built for the system (`--menuconfig`).

Replacing `--no-install` with the `--install` option allows genkernel to automatically install the new kernel in the [/boot] directory, and will create symlinks if `--symlink` is specified. Using the `--mountboot` option allows genkernel to mount the [/boot] partition automatically, if necessary.

** Note**\
Don\'t forget that the [/etc/genkernel.conf] file is sourced by the **genkernel** command at startup, and that any option defined there will be applied, except where a command line option takes precedence over it.

### [][[] Changing the boot directory to [/efi]]

It is now recommended to mount the UEFI system boot partition (ESP) under [/efi] instead of [/boot].

By default, the kernel is written to [/boot], which used to be the ESP in certain configurations, but is now on the root partition. Reasons to write the kernel to [/efi] include:

-   Secure Boot expecting a hard coded ESP kernel path
-   Making GRUB2 independent of the root partition for stability or security
-   GRUB2 not supporting the root file-system (bcachefs)
-   Using a grub.cfg not generated by [grub-mkconfig]

\
To point genkernel to [/efi], either add `--bootdir=/efi` to the `genkernel` command or `BOOTDIR="/efi"` to [/etc/genkernel.conf].

[FILE] **`/etc/genkernel.conf`Changing the boot directory to /efi in /etc/genkernel.conf**

    # Set the boot directory, default is /boot
    BOOTDIR="/efi"

### [Changing the kernel]

The first thing that should be done is to allow the triggering of [make menuconfig] in the [/etc/genkernel.conf] file:

[FILE] **`/etc/genkernel.conf`Forcing the use of the configuration menu in /etc/genkernel.conf**

    # Run 'make menuconfig' before compiling this kernel?
    MENUCONFIG="yes"

#### [File management]

While using genkernel, the user has to be aware of some aspects relating to kernel configuration and kernel image files management and the way the kernel sources are handled by the system.

##### [Source files]

After issuing [emerge -u gentoo-sources], a directory is created under [/usr/src/] to store new sources. Normally, the active kernel sources directory is pointed to by the [/usr/src/linux] symlink.

The [/usr/src] directory might look like this:

`user `[`$`]`ls -l /usr/src`

    total 24
    drwxr-xr-x  6 root root 4096 Dec 16 00:56 .
    drwxr-xr-x 12 root root 4096 Dec 15 12:42 ..
    -rw-r--r--  1 root root    0 Mar 19  2015 .keep
    lrwxrwxrwx  1 root root   22 Dec 16 00:56 linux -> linux-5.3.14-gentoo-r1
    drwxr-xr-x 26 root root 4096 Nov 24 03:33 linux-4.19.85-gentoo
    drwxr-xr-x 27 root root 4096 Dec  9 15:10 linux-4.19.88-gentoo
    drwxr-xr-x 27 root root 4096 Dec 16 00:51 linux-4.19.89-gentoo
    drwxr-xr-x 25 root root 4096 Dec 16 00:58 linux-5.3.14-gentoo-r1

The [/usr/src/linux] symlink can be changed in different ways.

-   If the `symlink` USE is set the [/usr/src/linux] symlink is automatically updated to point to the newly emerged sources.

<!-- -->

-   If the `symlink` USE is *not* set, the user can change the destination of the symlink using the [eselect kernel list] followed by the [eselect kernel set] command.

genkernel will *always* (exclusively) use the sources pointed by the [/usr/src/linux] symlink.

##### [Kernel configuration file]

If a kernel compilation has already been run with the active kernel sources, there might be a file inside the [/etc/kernels] directory that contains the kernel configuration that has been applied while creating the last bzImage of the kernel. This file is named, for example [kernel-config-5.3.14-gentoo-r1-x86_64-wifitest2] where `x86_64` might be substituted with the system\'s architecture, `5.3.14-gentoo-r1` might be substituted with the [package/version of the sources used](https://gitweb.gentoo.org/repo/gentoo.git/tree/sys-kernel/gentoo-sources/gentoo-sources-5.3.14-r1.ebuild?id=9557f104aa85b65c7d394c52c5c8d8727a111651), and `wifitest2` with the `LOCALVERSION` appended user value.

It is this [kernel-config-5.3.14-gentoo-r1-x86_64-wifitest2] file that is used as a starting configuration when running  [genkernel \--menuconfig all].

If it is the first time that genkernel is run with the new kernel sources, or if the previous result has not been saved, this file is substituted with a default configuration file that resides at [usr/share/genkernel/arch/x86_64/generated-config] where x86_64 is substituted with the actual architecture.

** Note**\
The path to this default configuration file, may be altered by setting the `DEFAULT_KERNEL_CONFIG` variable in [/etc/genkernel.conf] file

.

##### [Saving the compiled configuration]

If the `--save-config` genkernel option is activated, either from the command line or inside [/etc/genkernel.conf], the compiled kernel configuration is saved (with the name given above) into the [/etc/kernels] directory. At the same time, the configuration is saved in the [.config] file in [/usr/src/linux] directory but this file is not reused on the next [genkernel all] run.

** Warning**\
One has to be aware, that each time genkernel is run, with the `--save-config` genkernel option set, the configuration file in [/etc/kernels] is overridden. Thus, it is highly recommended to copy this file under a new name *before* running genkernel in order to preserve it.

##### [][Installing the kernel and initramfs into the [/boot] directory]

Specifying the `--install` option when invoking genkernel, will ask genkernel to install the kernel image and the initramfs into the [/boot] directory. In order to run `--install` a convenient manner, set the following in the [/etc/genkernel.conf] file:

[FILE] **`/etc/genkernel.conf`Setting up kernel and initramfs auto-saving**

    # Mount BOOTDIR automatically if it isn't mounted
    MOUNTBOOT="yes"

    # Save the new configuration in /etc/kernels upon
    # successful compilation
    SAVE_CONFIG="yes"

    # Make symlinks in BOOTDIR automatically
    SYMLINK="yes"

    # Add new kernel to grub
    # Possible values: empty/"no", "grub", "grub2"
    BOOTLOADER="grub2"

-   The first parameter speaks for itself.

<!-- -->

-   The second parameter tells genkernel to save the compiled kernel configuration into [/etc/kernels].

<!-- -->

-   The last two options tell genkernel to automatically update the grub configuration. In practice, the following happens:
    -   If a previous kernel image with the same name already exist, it is renamed by appending [.old] to its name. A symlink [kernel.old] is automatically created that points to it.
    -   The new kernel takes the place of any kernel with the same name into [/boot]. If it is the first time a kernel is compiled, a symlink kernel is automatically created that points to the new kernel.

After running [genkernel \--menuconfig all], the [/boot] directory might look like this:

`user `[`$`]`ls -al /boot`

    total 69388
    lrwxrwxrwx 1 root root      44 Dec 16 00:58 System.map -> System.map-5.3.14-gentoo-r1-x86_64-wifitest2
    -rw-r--r-- 1 root root 3465443 Dec  9 15:05 System.map-4.19.88-gentoo-x86_64
    -rw-r--r-- 1 root root 3465554 Dec 16 00:45 System.map-4.19.89-gentoo-x86_64
    -rw-r--r-- 1 root root 3645309 Dec 15 16:07 System.map-5.3.14-gentoo-r1-x86_64
    -rw-r--r-- 1 root root 3645309 Dec 15 16:07 System.map-5.3.14-gentoo-r1-x86_64.old
    -rw-r--r-- 1 root root 3645309 Dec 16 00:58 System.map-5.3.14-gentoo-r1-x86_64-wifitest2
    drwxr-xr-x 2 root root    4096 Mar 21  2015 efi
    drwxr-xr-x 6 root root    4096 Dec 16 01:02 grub
    lrwxrwxrwx 1 root root      47 Dec 16 01:02 initramfs -> initramfs-5.3.14-gentoo-r1-x86_64-wifitest2.img
    -rw-r--r-- 1 root root 3631084 Dec  9 15:34 initramfs-4.19.88-gentoo-x86_64.img
    -rw-r--r-- 1 root root 3637148 Dec 16 00:54 initramfs-4.19.89-gentoo-x86_64.img
    -rw-r--r-- 1 root root 3670176 Dec 15 17:41 initramfs-5.3.14-gentoo-r1-x86_64.img
    -rw-r--r-- 1 root root 3669692 Dec 16 01:02 initramfs-5.3.14-gentoo-r1-x86_64-wifitest2.img
    -rw-r--r-- 1 root root  168960 Nov 16 19:10 intel-uc.img
    lrwxrwxrwx 1 root root      41 Dec 16 00:58 kernel -> vmlinuz-5.3.14-gentoo-r1-x86_64-wifitest2
    -rw-r--r-- 1 root root 7509552 Dec  9 15:05 vmlinuz-4.19.88-gentoo-x86_64
    -rw-r--r-- 1 root root 7509552 Dec 16 00:45 vmlinuz-4.19.89-gentoo-x86_64
    -rw-r--r-- 1 root root 7784496 Dec 15 16:07 vmlinuz-5.3.14-gentoo-r1-x86_64
    -rw-r--r-- 1 root root 7784496 Dec 15 16:07 vmlinuz-5.3.14-gentoo-r1-x86_64.old
    -rw-r--r-- 1 root root 7784496 Dec 16 00:58 vmlinuz-5.3.14-gentoo-r1-x86_64-wifitest2

#### [Configuring the bootloader]

##### [extlinux]

TODO

##### [GRUB Legacy]

** Warning**\
The following text is about GRUB Legacy which was removed in Gentoo in February 2019. If at all possible, please [migrate to GRUB2](https://wiki.gentoo.org/wiki/GRUB2_Migration "GRUB2 Migration") as soon as possible.

The symlinks presented above in the bootloader\'s configuration can be used so that, even if the new kernel is not bootable, the user can always boot on the old one.

To allow the kernel and intird provided by genkernel to run correctly, provide a minimum information in bootloader\'s configuration file:

-   Add `root=/dev/sdaN` to the kernel parameters passed to the kernel image, where [/dev/sdaN] points to the root partition (`N` is the number of the partition if a partition exists).
-   If splash is used, add a suitable mode line such as `vga=0x317` to the parameters passed to the kernel and also add `splash=verbose` or `splash=silent` depending on the verboseness required through the boot process.
-   Add the initrd information as required by the bootloader. Consult the [Bootloader Configuration Chapter](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/Bootloader "Handbook:X86/Installation/Bootloader") of the Gentoo Handbook for details on how to make the bootloader initrd-aware.

Here is how the [grub.conf] file might look.

[FILE] **`/boot/grub/grub.conf`An example of grub.conf file**

    # This is a sample grub.conf for use with Genkernel, per the Gentoo handbook
    # http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=1&chap=10#doc_chap2
    # When not using Genkernel, see the handbook.
    # Alternatively, see grub.conf.sample in the GRUB documentation.

    default 0
    timeout 5
    splashimage=(hd1,0)/boot/grub/splash.xpm.gz

    title Gentoo Linux
    root (hd0,6)
    kernel /boot/kernel initrd=/dev/ram0 root=/dev/sda7 rootfstype=ext4
    initrd /boot/initramfs

    title Gentoo Linux old kernel
    root (hd0,6)
    kernel /boot/kernel.old initrd=/dev/ram0 root=/dev/sda7 rootfstype=ext4
    initrd /boot/initramfs.old

##### [GRUB]

TODO

##### [systemd-boot]

TODO

#### [Preserving the working files]

The genkernel application automatically saves new changes to the files. If previous changes are to be preserved, then the following actions need to be taken.

-   The first file to preserve is the kernel configuration file in [/etc/kernels/] If the source has not changed prior to the recompilation of the kernel, the previously used name for this file will be used. So copying the previous configuration file under a different name helps in preserving the information while keeping the file available as a starting point for a new configuration.

<!-- -->

-   The second important thing is to preserve the already bootable kernel and initramfs images. The way to accomplish this depends on the context:

1.  If the last kernel compiled is bootable, running [genkernel] will rename this kernel (and similarly initramfs) image to [vmlinuz-\$KV.old] and create a new [vmlinux-\$KV]. This mean that even if the new kernel is not bootable, users will always be able to boot the old one.
2.  If the last kernel compiled is not bootable and sources haven\'t changed since the user compiled a bootable one, prior to running [genkernel], first delete the new kernel image and remove the [.old] suffix from the last bootable one. Without this, if the newly compiled kernel is not bootable for the second time, the bootable [vmlinuz-\$KV.old] will be kicked out by the renaming of the non bootable [vmlinuz-\$KV], giving the user an unbootable system. Use the same reasoning for initramfs.

** Note**\
Since genkernel-4, it is recommended to create new, independent revisions each with its own kernel image, initramfs and installed modules in [/lib/modules] using [genkernel \--kernel-append-localversion=-my-new-revision all].

#### [Using previous kernel configuration while changing the sources]

The previous configuration can be used through the `MENUCONFIG` variable in [/etc/genkernel.conf] as follows:

[FILE] **`/etc/genkernel.conf`Setting up make menuconfig**

    # Run 'make menuconfig' before compiling this kernel
    MENUCONFIG="yes"

** Note**\
There is no need to manually run [make oldconfig] when using [genkernel], even if the sources are changed. This is because [make menuconfig] will try to load the previous configuration into the menu as much as possible. Nevertheless, *reviewing* each option and new sections carefully is recommended.

#### [][Checking that initramfs includes necessary modules/utilities before booting]

Before booting the system, it might be wise checking that initramfs includes necessary utilities and modules. For example, to utilize remote unlock capabilities for a headless system using [LUKS](https://wiki.gentoo.org/wiki/Dm-crypt_full_disk_encryption "Dm-crypt full disk encryption"), ensure that kernel modules for the network interface card, dropbear, and cryptsetup have been included.

##### [Using lsinitrd]

Since genkernel-4, created initramfs can be processed using the [lsinitrd] command from the [[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]] package:

`user `[`$`]`lsinitrd /boot/initramfs-5.3.14-gentoo-r1-x86_64-wifitest2.img `

    Image: /boot/initramfs-5.3.14-gentoo-r1-x86_64-wifitest2.img: 4,5M
    ========================================================================
    Version: Genkernel 4.0.1 (2019-12-16 00:48:10 UTC)

    Arguments: --boot-font=none --keymap --compress-initramfs --no-microcode-initramfs --ramdisk-modules --busybox --no-btrfs --no-iscsi --no-multipath --no-dmraid --mdadm --lvm --no-unionfs --no-zfs --no-splash --no-strace --no-gpg --luks --no-firmware --firmware-dir=/lib/firmware --ssh --no-e2fsprogs --no-xfsprogs

    dracut modules:
    ========================================================================
    drwxr-xr-x  16 root     root            0  Dec 16 01:49 .
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 bin
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/ash -> busybox
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/[ -> busybox
    -rwxr-xr-x   1 root     root      2351376  Dec 16 01:49 bin/busybox
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/cat -> busybox
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/cut -> busybox
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/echo -> busybox
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/mknod -> busybox
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/mount -> busybox
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/sh -> busybox
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 bin/uname -> busybox
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 dev
    drwxr-xr-x   8 root     root            0  Dec 16 01:49 etc
    -rw-r--r--   1 root     root           24  Dec 16 01:49 etc/build_date
    -rw-r--r--   1 root     root           16  Dec 16 01:49 etc/build_id
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 etc/dropbear
    -rw-------   1 root     root          140  Dec 16 01:49 etc/dropbear/dropbear_ecdsa_host_key
    -rw-------   1 root     root          806  Dec 16 01:49 etc/dropbear/dropbear_rsa_host_key
    prw-r--r--   1 root     root            0  Dec 16 01:49 etc/dropbear/fifo_root
    prw-r--r--   1 root     root            0  Dec 16 01:49 etc/dropbear/fifo_swap
    -rw-r--r--   1 root     root           97  Dec 16 01:49 etc/fstab
    -rw-r--r--   1 root     root           14  Dec 16 01:49 etc/group
    -rw-r--r--   1 root     root         3742  Dec 16 01:49 etc/initrd.defaults
    -rw-r--r--   1 root     root        69232  Dec 16 01:49 etc/initrd.scripts
    -rw-r--r--   1 root     root          441  Dec 16 01:49 etc/ld.so.cache
    -rw-r--r--   1 root     root           78  Dec 16 01:49 etc/ld.so.conf
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 etc/ld.so.conf.d
    -rw-r--r--   1 root     root           81  Dec 16 01:49 etc/ld.so.conf.d/05gcc-x86_64-pc-linux-gnu.conf
    -rw-r--r--   1 root     root         2298  Dec 16 01:49 etc/localtime
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 etc/lvm
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 etc/lvm/cache
    -rw-r--r--   1 root     root        95231  Dec 16 01:49 etc/lvm/lvm.conf
    -rw-r--r--   1 root     root         2882  Dec 16 01:49 etc/mdadm.conf
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 etc/mdev
    -rw-r--r--   1 root     root         1172  Dec 16 01:49 etc/mdev.conf
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 etc/mdev/helpers
    -rwxr-xr-x   1 root     root          666  Dec 16 01:49 etc/mdev/helpers/nvme
    -rwxr-xr-x   1 root     root         1295  Dec 16 01:49 etc/mdev/helpers/storage-device
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 etc/modprobe.d
    -rw-r--r--   1 root     root         1186  Dec 16 01:49 etc/modprobe.d/aliases.conf
    -rw-r--r--   1 root     root          122  Dec 16 01:49 etc/modprobe.d/i386.conf
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 etc/modules
    -rw-r--r--   1 root     root           24  Dec 16 01:49 etc/modules/ataraid
    -rw-r--r--   1 root     root           21  Dec 16 01:49 etc/modules/block
    -rw-r--r--   1 root     root          180  Dec 16 01:49 etc/modules/crypto
    -rw-r--r--   1 root     root           26  Dec 16 01:49 etc/modules/dmraid
    -rw-r--r--   1 root     root           23  Dec 16 01:49 etc/modules/firewire
    -rw-r--r--   1 root     root          123  Dec 16 01:49 etc/modules/fs
    -rw-r--r--   1 root     root           86  Dec 16 01:49 etc/modules/hyperv
    -rw-r--r--   1 root     root           40  Dec 16 01:49 etc/modules/iscsi
    -rw-r--r--   1 root     root          437  Dec 16 01:49 etc/modules/lvm
    -rw-r--r--   1 root     root          194  Dec 16 01:49 etc/modules/mdadm
    -rw-r--r--   1 root     root           75  Dec 16 01:49 etc/modules/multipath
    -rw-r--r--   1 root     root          214  Dec 16 01:49 etc/modules/net
    -rw-r--r--   1 root     root           56  Dec 16 01:49 etc/modules/nvme
    -rw-r--r--   1 root     root          519  Dec 16 01:49 etc/modules/pata
    -rw-r--r--   1 root     root           83  Dec 16 01:49 etc/modules/pcmcia
    -rw-r--r--   1 root     root          158  Dec 16 01:49 etc/modules/sata
    -rw-r--r--   1 root     root          523  Dec 16 01:49 etc/modules/scsi
    -rw-r--r--   1 root     root          350  Dec 16 01:49 etc/modules/usb
    -rw-r--r--   1 root     root          133  Dec 16 01:49 etc/modules/virtio
    -rw-r--r--   1 root     root           15  Dec 16 01:49 etc/modules/waitscan
    -rw-r--r--   1 root     root           47  Dec 16 01:49 etc/passwd
    -rw-r-----   1 root     root           22  Dec 16 01:49 etc/shadow
    -rw-r--r--   1 root     root           25  Dec 16 01:49 etc/shells
    -rwxr-xr-x   1 root     root        32331  Dec 16 01:49 init
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 .initrd
    drwxr-xr-x   6 root     root            0  Dec 16 01:49 lib
    lrwxrwxrwx   1 root     root            3  Dec 16 01:49 lib32 -> lib
    lrwxrwxrwx   1 root     root            3  Dec 16 01:49 lib64 -> lib
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/console
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/dracut
    -rw-r--r--   1 root     root          312  Dec 16 01:49 lib/dracut/build-parameter.txt
    -rw-r--r--   1 root     root           42  Dec 16 01:49 lib/dracut/dracut-gk-version.info
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/keymaps
    lrwxrwxrwx   1 root     root            9  Dec 16 01:49 lib/keymaps/10.map -> croat.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/11.map -> cz.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/12.map -> de.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/13.map -> dk.map
    lrwxrwxrwx   1 root     root           10  Dec 16 01:49 lib/keymaps/14.map -> dvorak.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/15.map -> es.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/16.map -> et.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/17.map -> fi.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/18.map -> fr.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/19.map -> gr.map
    lrwxrwxrwx   1 root     root           10  Dec 16 01:49 lib/keymaps/1.map -> azerty.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/20.map -> hu.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/21.map -> il.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/22.map -> is.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/23.map -> it.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/24.map -> jp.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/25.map -> la.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/26.map -> lt.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/27.map -> mk.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/28.map -> nl.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/29.map -> no.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/2.map -> be.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/30.map -> pl.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/31.map -> pt.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/32.map -> ro.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/33.map -> ru.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/34.map -> se.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/35.map -> sf.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/36.map -> sg.map
    lrwxrwxrwx   1 root     root            8  Dec 16 01:49 lib/keymaps/37.map -> sk-y.map
    lrwxrwxrwx   1 root     root            8  Dec 16 01:49 lib/keymaps/38.map -> sk-z.map
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 lib/keymaps/39.map -> slovene.map
    lrwxrwxrwx   1 root     root            8  Dec 16 01:49 lib/keymaps/3.map -> bepo.map
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 lib/keymaps/40.map -> trf.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/41.map -> ua.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/42.map -> uk.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/43.map -> us.map
    lrwxrwxrwx   1 root     root           10  Dec 16 01:49 lib/keymaps/44.map -> wangbe.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/4.map -> bg.map
    lrwxrwxrwx   1 root     root            8  Dec 16 01:49 lib/keymaps/5.map -> br-a.map
    lrwxrwxrwx   1 root     root            8  Dec 16 01:49 lib/keymaps/6.map -> br-l.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/7.map -> by.map
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 lib/keymaps/8.map -> cf.map
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 lib/keymaps/9.map -> colemak.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/azerty.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/be.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/bepo.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/bg.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/br-a.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/br-l.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/by.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/cf.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/colemak.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/croat.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/cz.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/de.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/dk.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/dvorak.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/es.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/et.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/fi.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/fr.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/gr.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/hu.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/il.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/is.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/it.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/jp.map
    -rw-r--r--   1 root     root          518  Dec 16 01:49 lib/keymaps/keymapList
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/la.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/lt.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/mk.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/nl.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/no.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/pl.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/pt.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/ro.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/ru.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/se.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/sf.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/sg.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/sk-y.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/sk-z.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/slovene.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/trf.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/ua.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/uk.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/us.map
    -rw-r--r--   1 root     root         2823  Dec 16 01:49 lib/keymaps/wangbe.map
    -rwxr-xr-x   1 root     root       169376  Dec 16 01:49 lib/ld-linux-x86-64.so.2
    -rwxr-xr-x   1 root     root      1913648  Dec 16 01:49 lib/libc.so.6
    -rwxr-xr-x   1 root     root        26800  Dec 16 01:49 lib/libnss_dns.so
    lrwxrwxrwx   1 root     root           13  Dec 16 01:49 lib/libnss_dns.so.2 -> libnss_dns.so
    -rwxr-xr-x   1 root     root        51536  Dec 16 01:49 lib/libnss_files.so
    lrwxrwxrwx   1 root     root           15  Dec 16 01:49 lib/libnss_files.so.2 -> libnss_files.so
    -rwxr-xr-x   1 root     root        88736  Dec 16 01:49 lib/libresolv.so.2
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 lib/modules
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2
    drwxr-xr-x   5 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/crypto
    -rw-r--r--   1 root     root         7152  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/crypto/algif_rng.ko
    drwxr-xr-x   6 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/hid
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/hid/usbhid
    -rw-r--r--   1 root     root        66448  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/hid/usbhid/usbhid.ko
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/md
    -rw-r--r--   1 root     root        19024  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/md/dm-log.ko
    -rw-r--r--   1 root     root        27256  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/md/dm-mirror.ko
    -rw-r--r--   1 root     root        49200  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/md/dm-raid.ko
    -rw-r--r--   1 root     root        16536  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/md/dm-region-hash.ko
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/net
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/net/intel
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/net/intel/e1000
    -rw-r--r--   1 root     root        70480  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/net/intel/e1000/e1000.ko
    drwxr-xr-x   6 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/common
    -rw-r--r--   1 root     root         6584  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/common/usb-common.ko
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/core
    -rw-r--r--   1 root     root       308944  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/core/usbcore.ko
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/host
    -rw-r--r--   1 root     root        60416  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/host/ehci-hcd.ko
    -rw-r--r--   1 root     root        10616  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/host/ehci-pci.ko
    -rw-r--r--   1 root     root        46072  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/host/ohci-hcd.ko
    -rw-r--r--   1 root     root        35896  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/host/uhci-hcd.ko
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/storage
    -rw-r--r--   1 root     root       126512  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/drivers/usb/storage/usb-storage.ko
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/fs
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/fs/fat
    -rw-r--r--   1 root     root        95664  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/fs/fat/fat.ko
    -rw-r--r--   1 root     root        16104  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/kernel/fs/fat/msdos.ko
    -rw-r--r--   1 root     root        32434  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.alias
    -rw-r--r--   1 root     root        42356  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.alias.bin
    -rw-r--r--   1 root     root         8132  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.builtin
    -rw-r--r--   1 root     root        11529  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.builtin.bin
    -rw-r--r--   1 root     root        15196  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.dep
    -rw-r--r--   1 root     root        23748  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.dep.bin
    -rw-r--r--   1 root     root            0  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.devname
    -rw-r--r--   1 root     root         8320  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.order
    -rw-r--r--   1 root     root          117  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.softdep
    -rw-r--r--   1 root     root        24707  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.symbols
    -rw-r--r--   1 root     root        29469  Dec 16 01:49 lib/modules/5.3.14-gentoo-r1-x86_64-wifitest2/modules.symbols.bin
    lrwxrwxrwx   1 root     root            4  Dec 16 01:49 linuxrc -> init
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 mnt
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 proc
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 root
    drwx------   2 root     root            0  Dec 16 01:49 root/.ssh
    -rw-------   1 root     root          742  Dec 16 01:49 root/.ssh/authorized_keys
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 run
    -rw-r--r--   1 root     root            0  Dec 16 01:49 run/utmp
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 sbin
    -rwxr-xr-x   1 root     root      1105720  Dec 16 01:49 sbin/blkid
    -rwxr-xr-x   1 root     root      2813384  Dec 16 01:49 sbin/cryptsetup
    lrwxrwxrwx   1 root     root           19  Dec 16 01:49 sbin/dmsetup -> ../usr/sbin/dmsetup
    lrwxrwxrwx   1 root     root           19  Dec 16 01:49 sbin/dmstats -> ../usr/sbin/dmstats
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 sbin/init -> ../init
    lrwxrwxrwx   1 root     root           15  Dec 16 01:49 sbin/lvm -> ../usr/sbin/lvm
    -rwxr-xr-x   1 root     root      1510360  Dec 16 01:49 sbin/mdadm
    -rwxr-xr-x   1 root     root      1267904  Dec 16 01:49 sbin/mdmon
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 sys
    drwxrwxrwt   2 root     root            0  Dec 16 01:49 tmp
    drwxr-xr-x   6 root     root            0  Dec 16 01:49 usr
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 usr/bin
    lrwxrwxrwx   1 root     root           13  Dec 16 01:49 usr/bin/dropbearconvert -> dropbearmulti
    lrwxrwxrwx   1 root     root           13  Dec 16 01:49 usr/bin/dropbearkey -> dropbearmulti
    -rwxr-xr-x   1 root     root      1365144  Dec 16 01:49 usr/bin/dropbearmulti
    -rwxr-xr-x   1 root     root         2881  Dec 16 01:49 usr/bin/login-remote.sh
    lrwxrwxrwx   1 root     root           13  Dec 16 01:49 usr/bin/scp -> dropbearmulti
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 usr/lib
    lrwxrwxrwx   1 root     root            3  Dec 16 01:49 usr/lib32 -> lib
    lrwxrwxrwx   1 root     root            3  Dec 16 01:49 usr/lib64 -> lib
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 usr/sbin
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/cache_check -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/cache_dump -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/cache_metadata_size -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/cache_repair -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/cache_restore -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/cache_writeback -> pdata_tools
    -rwxr-xr-x   1 root     root      1262952  Dec 16 01:49 usr/sbin/dmsetup
    lrwxrwxrwx   1 root     root            7  Dec 16 01:49 usr/sbin/dmstats -> dmsetup
    lrwxrwxrwx   1 root     root           20  Dec 16 01:49 usr/sbin/dropbear -> ../bin/dropbearmulti
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/era_check -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/era_dump -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/era_invalidate -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/era_restore -> pdata_tools
    -rwxr-xr-x   1 root     root      2905416  Dec 16 01:49 usr/sbin/lvm
    -rwxr-xr-x   1 root     root      3061192  Dec 16 01:49 usr/sbin/pdata_tools
    -rwxr-xr-x   1 root     root          609  Dec 16 01:49 usr/sbin/resume-boot
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_check -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_delta -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_dump -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_ls -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_metadata_size -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_repair -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_restore -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_rmap -> pdata_tools
    lrwxrwxrwx   1 root     root           11  Dec 16 01:49 usr/sbin/thin_trim -> pdata_tools
    -rwxr-xr-x   1 root     root         3076  Dec 16 01:49 usr/sbin/unlock-luks
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 usr/share
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 usr/share/udhcpc
    -rwxr-xr-x   1 root     root         1098  Dec 16 01:49 usr/share/udhcpc/default.script
    drwxr-xr-x   3 root     root            0  Dec 16 01:49 var
    drwxr-xr-x   2 root     root            0  Dec 16 01:49 var/log
    -rw-r--r--   1 root     root            0  Dec 16 01:49 var/log/lastlog
    -rw-r--r--   1 root     root            0  Dec 16 01:49 var/log/wtmp
    lrwxrwxrwx   1 root     root            6  Dec 16 01:49 var/run -> ../run
    ========================================================================

The output above shows the [e1000.ko] file for an Intel NIC, the dropbear executable ([usr/bin/dropbearmulti]), and the cryptsetup ([sbin/cryptsetup]) executable have been embedded into the initramfs file.

##### [Manual extraction]

To extract a generated initramfs to inspect its content:

`root `[`#`]`mkdir /tmp/initramfs `

`root `[`#`]`cd /tmp/initramfs `

`root `[`#`]`xzcat /boot/initramfs-5.3.14-gentoo-r1-x86_64-wifitest2.img | cpio -idmv `

`root `[`#`]`ls -l sbin/cryptsetup `

    -rwxr-xr-x   1 root     root      2813384  Dec 16 01:49 sbin/cryptsetup

** Note**\
Manual extraction will be difficult if CPU microcode updates have been embedded into the initramfs.

### [Microcode loading]

For microcode (ucode) updates, kernel must support (early-)microcode loading and microcode updates must be present early at boot. See [Microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") article for more details.

#### [Microcode loading support in kernel]

By default, [genkernel] will enable microcode loading support in kernel for both, AMD and Intel processors. This behavior can be controlled through `MICROCODE` option in [/etc/genkernel.conf] or by using the `--microcode=(no|all|amd|intel)` command-line parameter during invocation.

#### [Embedding microcode updates into initramfs]

To embed microcode (ucode) updates into initramfs, `MICROCODE_INITRAMFS` must be enabled in [/etc/genkernel.conf] or command-line parameter `--microcode-initramfs` must be passed at invocation. This will cause [genkernel] to prepend microcode(s) for selected processor (see `--microcode` option above) to initramfs in case [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]] with the `split-ucode` USE flag for Intel processors and/or [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] for AMD processors is installed.

** Note**\
The technique of embedding microcode updates into the initramfs has been deprecated for modern systems in favor of using bootloaders (like [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]]) which are capable of loading multiple initramfs files. When using GRUB, or another modern bootloader, it is recommended to install [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]] for Intel and [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] for AMD processors, both require the `initramfs` USE flag to be enabled. Let the bootloader load [/boot/amd-uc.img] and/or [/boot/intel-uc.img] in addition to genkernel\'s initramfs. This will enable updating of the CPU microcode independently of kernel/initramfs updates.

### [Firmware loading]

Specific firmware files can be added to genkernel\'s automatically generated initramfs when listed, with relative paths, in the variable `FIRMWARE_FILES` in [/etc/genkernel.conf]. When [[[sys-kernel/genkernel]](https://packages.gentoo.org/packages/sys-kernel/genkernel)[]] is installed with `USE="firmware"` it will prefer firmware files from [/lib/firmware].

[FILE] **`/etc/genkernel.conf`Including firmware in the initramfs**

    # Add firmware(s) to initramfs
    FIRMWARE="yes"

    # Specify directory to pull from
    FIRMWARE_DIR="/lib/firmware"

    # Specify a comma-separated list of firmware files or directories to include,
    # relative to FIRMWARE_DIR.  If empty or unset, the full contents of
    # FIRMWARE_DIR will be included (if FIRMWARE option above is set to YES).
    FIRMWARE_FILES="<comma-separated list of firmware files here>"

In case [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] is installed with `USE="experimental"` and the kernel is configured with `CONFIG_GENTOO_PRINT_FIRMWARE_INFO=y`, the following command gets a comma-separated list of all currently loaded firmware files for the use in the `FIRMWARE_FILES` variable from [/etc/genkernel.conf] as illustrated above (the output is just an example):

`root `[`#`]`dmesg -t | grep '^Loading firmware*' | sed 's/^Loading\sfirmware:\s//' | echo $(cat) | tr ' ' ',' `

    amdgpu/green_sardine_sdma.bin,amdgpu/green_sardine_asd.bin,amdgpu/green_sardine_ta.bin,amdgpu/green_sardine_pfp.bin,amdgpu/green_sardine_me.bin,amdgpu/green_sardine_ce.bin,amdgpu/green_sardine_rlc.bin,amdgpu/green_sardine_mec.bin,amdgpu/green_sardine_dmcub.bin,amdgpu/green_sardine_vcn.bin,regulatory.db,regulatory.db.p7s,rtw89/rtw8852a_fw.bin,rtl_bt/rtl8852au_fw.bin,rtl_bt/rtl8852au_config.bin,rtl_nic/rtl8168h-2.fw

It is also possible to incorporate the firmware into the kernel image directly, but be aware that `CONFIG_EXTRA_FIRMWARE` in the kernel configuration file [.config] (normally found in [/usr/src/linux]) requires a space-separated list (output example):

`root `[`#`]`dmesg -t | grep '^Loading firmware*' | sed 's/^Loading\sfirmware:\s//' | echo $(cat) `

    amdgpu/green_sardine_sdma.bin amdgpu/green_sardine_asd.bin amdgpu/green_sardine_ta.bin amdgpu/green_sardine_pfp.bin amdgpu/green_sardine_me.bin amdgpu/green_sardine_ce.bin amdgpu/green_sardine_rlc.bin amdgpu/green_sardine_mec.bin amdgpu/green_sardine_dmcub.bin amdgpu/green_sardine_vcn.bin regulatory.db regulatory.db.p7s rtw89/rtw8852a_fw.bin rtl_bt/rtl8852au_fw.bin rtl_bt/rtl8852au_config.bin rtl_nic/rtl8168h-2.fw

** Note**\
Such a list will only be complete if the drivers successfully load all the required firmware(s): In case a driver requires more than one firmware file but fails loading the first one, only this will be listed and thereby other required firmware filenames will be missing. A recommended procedure to find all required firmware files is to compile the respective drivers as modules first, `M` in the kernel configuration, and to **not**the modules in initramfs. The modules will be loaded after switching to the real `/` (root) directory, where all firmware files will be available from [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] (and others) under [/lib/firmware]. When a system boots successfully with this method, running the above command will gather a complete list of the required firmware files. The files can be included in the initramfs (or the kernel itself), allowing for the drivers to be compiled directly into the kernel, `*` in the kernel configuration, or to include the drivers as kernel modules in the initramfs as well. In both cases loading the modules will be earlier and it will be successful with the availability of the firmware files in the initramfs, which must be loaded alongside the kernel e.g. using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB").

### [Remote rescue shell]

genkernel can embed the [[[net-misc/dropbear]](https://packages.gentoo.org/packages/net-misc/dropbear)[]] SSH daemon into the initramfs which will allow fixing certain things on boot remotely when initramfs is at least able to load. The most common used feature will be remote unlock capability for LUKS-encrypted root or swap devices or [ZFS](https://wiki.gentoo.org/wiki/ZFS "ZFS") volumes.

#### [Pre-requirement for SSH daemon support in initramfs]

A [authorized_keys] file must exist before genkernel will be invoked. By default, genkernel will look for [/etc/dropbear/authorized_keys]. Command-line argument `--ssh-authorized-keys-file=/path/to/custom/authorized_keys` or genkernel configuration option `SSH_AUTHORIZED_KEYS_FILE` can be used to alter default value.

** Tip**\
Create [/etc/dropbear/authorized_keys] as a symlink to [/root/.ssh/authorized_keys] for example to keep root access and remote rescue shell access in sync!

#### [Adding SSH support to initramfs]

To embed SSH daemon into genkernel\'s initramfs, run [genkernel] with `--ssh` command-line argument or set `SSH="yes"` in genkernel configuration file. Needless to mention that this feature will require working network at boot. The following example will just (re-)build initramfs with SSH daemon embedded:

`root `[`#`]`genkernel --ssh initramfs `

    * Gentoo Linux Genkernel; Version 4.0.1
    * Using genkernel configuration from '/etc/genkernel.conf' ...
    * Running with options: --ssh initramfs

    * Working with Linux kernel 5.3.14-gentoo-r1-x86_64 for x86_64
    * Using kernel config file '/etc/kernels/kernel-config-5.3.14-gentoo-r1-x86_64' ...

    * initramfs: >> Initializing ...
    *         >> Appending devices cpio data ...
    *         >> Appending base_layout cpio data ...
    *         >> Appending auxilary cpio data ...
    *         >> Appending blkid cpio data ...
    *         >> Appending busybox cpio data ...
    *         >> Appending dropbear cpio data ...
    =================================================================
    This initramfs' sshd will use the following host key(s):
    256 MD5:a5:13:09:90:5b:f6:a1:95:49:9f:87:d9:fa:e5:d8:02 (ECDSA)
    256 SHA256:5dxNGEOwH9hvX4+sV4WtzRV/9m8/hrhgnNtTplZf5x8 (ECDSA)
    2048 MD5:1d:e6:cc:ce:c8:96:a0:73:3e:4c:2a:56:ce:b9:10:26 (RSA)
    2048 SHA256:V4WrMKhfVSxSeW3XIbW8dSaAmXiwN6jiMA/geNKLcqA (RSA)
    =================================================================
    *         >> Appending modprobed cpio data ...
    *         >> Appending modules cpio data ...
    *         >> Appending linker cpio data ...
    *         >> Deduping cpio ...
    *         >> Pre-generating initramfs' /etc/ld.so.cache ...
    *         >> Compressing cpio data (.xz) ...
    *
    * You will find the initramfs in '/boot/initramfs-5.3.14-gentoo-r1-x86_64.img'.

    * WARNING... WARNING... WARNING...
    * Additional kernel parameters that *may* be required to boot properly:
    * - Add "dosshd" to start SSH daemon in initramfs

    * Do NOT report kernel bugs as genkernel bugs unless your bug
    * is about the default genkernel configuration...
    *
    * Make sure you have the latest ~arch genkernel before reporting bugs.

** Note**\
By default, genkernel will generate own, dedicated SSH host keys for any missing supported key algorithm for embedded SSH daemon. This will allow to differentiate between real system\'s SSH daemon and initramfs\' SSH daemon. To use host\'s SSH host keys instead or generate new keys at runtime on each boot use `--ssh-host-keys` command-line option and see genkernel\'s man page for more details.

#### [Enabling SSH daemon on boot]

Just adding SSH daemon to initramfs is not enough. Because exposing any network service could be a security risk, this feature **must** be enabled via the kernel command-line argument `dosshd`! See Configure Network for how to configure network in genkernel.

#### [Remote unlock]

There are two possibilities to unlock LUKS-encrypted root and/or swap volume: A manual way, through an SSH connection, run a command and will get prompted for passphrase(s) or an automatic way where user passes passphrase through SSH as command.

** Note**\
This will require a kernel/initramfs generated with `--luks` command-line argument and kernel must be booted with `crypt_root` (and/or `crypt_swap`) kernel command-line argument. ZFS user must generate kernel/initramfs with `--zfs` command-line argument and kernel must be booted with `dozfs` kernel command-line argument.

##### [Manual unlock]

Connect to the remote system through SSH and run the following commands:

`user `[`$`]`ssh root@remote-system-running-genkernel-initramfs-with-dosshd `

    >> Welcome to Genkernel 4.0.1 (2019-12-16 22:34:14 UTC) remote rescue shell!
    >> ...running Linux kernel 5.3.14-gentoo-r1-x86_64

    >> The lockfile '/tmp/remote-rescueshell.lock' was created.
    >> In order to resume boot process, run 'resume-boot'.
    >> Be aware that it will kill your connection which means
    >> you will no longer be able to work in this shell.
    >> To remote unlock LUKS-encrypted root device, run 'unlock-luks root'.

    remote rescueshell ~ # unlock-luks root
    >> Detected real_root as a md device. Setting up the device node ...
    Enter passphrase for /dev/md126:
    >> LUKS device /dev/md126 opened
    remote rescueshell ~ # resume-boot
    >> Resuming boot process ...

** Note**\
In this example, system was booted with just `crypt_root=` set in kernel command-line. In case system was booted with `crypt_swap=` there will be an additional prompt regarding how to unlock swap. ZFS user will get prompted to use `unlock-zfs` command instead.

##### [Automatic unlock]

It\'s basically the same like manual unlock just without the need to manually run [resume-boot]. In case user has both, encrypted root and swap volume, user must unlock swap volume first:

`user `[`$`]`cat /path/to/secret.key/on/local/disk | ssh root@remote-system-running-genkernel-initramfs-with-dosshd post root `

    >> Detected real_root as a md device. Setting up the device node ...
    >> LUKS device /dev/md126 opened
    >> Resuming boot process ...

** Note**\
Automatic unlock is not available for ZFS users.

### [Network booting]

#### [From an installation CD]

The [genkernel] utility can build kernel and initrd images that provide support for network booting, or netbooting. With any luck, users should be able to netboot any recent computer into the environment provided by the Installation CD.

The magic lies in genkernel\'s linuxrc script: it will try to netmount the Installation CD using NFS. From there, the init scripts of the Installation CD can take over, as if the CD was present locally.

#### [Building the kernel and initramfs with netboot support]

To enable support for netbooting, include the following options while configuring the kernel:

** Warning**\
Support for netbooting with genkernel is experimental and may contain bugs.

First, the kernel image must include the drivers for the system\'s Network Interface Cards (NIC). Normally, drivers for such devices will be compiled as modules. However, it is essential (for netbooting) that such drivers are compiled directly into the kernel image and not as modules.

[KERNEL] **Configuring a 3.x.x series kernel to support various NIC drivers**

    Device Drivers --->
       Networking Support --->
          Ethernet (10 or 100Mbit)  --->
             [*] Ethernet (10 or 100Mbit)
             <*>   The driver(s) for each network card

** Note**\
Be sure to select [\<\*\>] and not [\<M\>].

Secondly, it is suggested that *IP: kernel level autoconfiguration* is enabled as well as *IP: DHCP support options*. This avoids an unnecessary layer of complexity since the IP address and the NFS path to the Installation CD can be configured on a DHCP server. Of course, this means the kernel command line will remain constant for any machine --- which is very important for etherbooting.

[KERNEL] **Configuring a 3.x.x series kernel to support DHCP**

    Device Drivers --->
       Networking Support --->
          Networking options
             [*] TCP/IP networking--->
             [*]   IP: kernel level autoconfiguration
             [*]     IP: DHCP support

Tells the kernel to send a DHCP request at bootup.

Additionally, enable [SquashFS](https://wiki.gentoo.org/wiki/SquashFS "SquashFS") because most modern Gentoo Installation CDs require it. Support for SquashFS is not included with the generic kernel source tree. To enable SquashFS, apply the necessary patches to the generic kernel source or install gentoo-sources.

[KERNEL] **Configuring the kernel to support SquashFS**

    File systems--->
       Miscellaneous filesystems --->
          [*] SquashFS 2.X - Squashed file system support

Once the compilation process is completed, create a compressed tarball (tar.gz) that contains the kernel\'s modules. This step is only necessary if the kernel version does not match the kernel image version on the Installation CD.

To create an archive containing all the modules:

`root `[`#`]`cd / `

`root `[`#`]`tar -cf /tmp/modules-X.Y.Z.tar.gz /lib/modules/X.Y.Z/`

Depending on the network boot mechanism, one of the following steps need to be followed:

To create an etherboot image:

`root `[`#`]`emerge --ask net-misc/mknbi`

`root `[`#`]`cd /boot `

`root `[`#`]`mkelf-linux -params="root=/dev/ram0 init=/linuxrc ip=dhcp" kernel... initrd... > etherboot.img`

To create an OpenBoot/SPARC64 TFTP image:

`root `[`#`]`emerge --ask sys-apps/sparc-utils`

`root `[`#`]`cd /boot `

`root `[`#`]`elftoaout kernel... -o kernel.aout `

`root `[`#`]`piggyback64 kernel.aout System.map-... initrd-... `

`root `[`#`]`mv kernel.aout openboot.img`

The [openboot.img] file is the boot image.

Finally, copy this kernel to the TFTP server. The details are architecture-dependent and are beyond the scope of this guide. Please refer to the documentation for the specific platform of interest.

#### [NFS setup]

To setup a NFS share that contains the Installation CD, use the loop device to mount the ISO image and then copy the contents of the CD into the NFS share. As a nice extra, genkernel\'s initrd scripts will extract all tar.gz files located in the [/nfs/livecd/add/] directory. All that needs to be done here is copy the [modules-X.Y.Z.tar.gz] archive to the [/nfs/livecd/add/] directory.

The following assumes that [/nfs/livecd] is an exported NFS share:

`root `[`#`]`mount /tmp/gentoo-livecd.iso /mnt/cdrom -o loop `

`root `[`#`]`cp -p /mnt/cdrom /nfs/livecd `

`root `[`#`]`umount /mnt/cdrom`

Now copy the [modules.tar.gz] file into [/add]:

`root `[`#`]`mkdir /nfs/livecd/add `

`root `[`#`]`cp /tmp/modules-X.Y.Z.tar.gz /nfs/livecd/add`

#### [DHCP setup]

The netboot images will ask the DHCP server on the network for an IP as well as a `root-path` option. Both can be specified per host using a MAC address to identify machines:

[FILE] **`/etc/dhcpd.conf`Sample client dhcpd.conf setup**

    # Here, 192.168.1.2 is the NFS server while 192.168.1.10 will be the IP address of the netbooted machine
    host netbootableMachine

#### [Netbooting instructions]

Netbooting itself is again very platform-specific. The important part is to specify the `ip=dhcp` and `init=/linuxrc` parameters on the kernel command line, as this will bring up the network interface and tell the initrd scripts to mount the Installation CD via NFS. Here are some platform-specific tips.

For etherboot, insert the etherboot disk into the drive and reboot. The kernel command line was specified when the image was constructed.

With Sparc64, press [Stop]+[A] at the boot prompt and then enter:

`ok``boot net ip=dhcp init=/linuxrc`

For PXE, setup pxelinux (part of syslinux), then create a [pxelinux.cfg/default] along the lines of:

[FILE] **`pxelinux.cfg/default`Default entry**

    DEFAULT gentoo
    TIMEOUT 40
    PROMPT 1

    LABEL gentoo
        KERNEL kernel-X.Y.Z
        APPEND initrd=initrd-X.Y.Z root=/dev/ram0 init=/linuxrc ip=dhcp

#### [Booting a genkernel initramfs]

##### [Introduction]

If an initramfs is installed with genkernel, then take a look at the various boot options that can (or should) be defined in the bootloader configuration. The most common ones are added to this guide.

##### [Loading LVM or software-RAID]

If the system uses LVM or software-RAID, the initramfs has to be built using the `--lvm` and `--mdadm` options. Do not forget to enable support during boot as well. This can be done using the dolvm and domdadm options.

[FILE] **`/boot/grub/grub.conf`Enabling LVM and/or MDADM support**

    # Example for GRUB 1.x
    title Gentoo Linux
    root (hd0,0)
    kernel /vmlinuz root=/dev/md3 dolvm domdadm
    initrd /initramfs-genkernel-x86_64-3.4.3

##### [Booting in single-user mode]

If for some reason boot-up fails, rescuing the system by booting in the single-user mode is still possible. This will only load the really necessary services and then drop the user to a rescue (root) shell.

[FILE] **`/boot/grub/grub.conf`Booting in single-user mode**

    # Example for GRUB 1.x
    title Gentoo Linux
    root (hd0,0)
    kernel /vmlinuz root=/dev/md3 init_opts=S
    initrd /initramfs-genkernel-x86_64-3.4.3

### [Cross-compile support]

To build kernel and/or initramfs for a different platform as [genkernel] is being executed on, kernel/initramfs must be cross-compiled.

`root `[`#`]`genkernel --mdadm --no-install --cross-compile=aarch64-linux-gnu all`

The above command causes [genkernel] to create a kernel supporting MD raid and embed [mdadm] into initramfs (`--mdadm`), both kernel and initramfs will have to be manually installed (`--no-install`). The kernel and programs embedded into initramfs will run on arm64 (`--cross-compile=aarch64-linux-gnu`).

`--cross-compile=<target triplet>`

** Tip**\
The recommended way to create a cross-compile environment is using [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]]. See the [how to create a cross-compile environment](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") article for more details.

### [Initramfs kernel command-line parameters]

** Note**\
The following parameter list is just an excerpt. Always check the version relevant [man genkernel].

`root=<...>`

<!-- -->

`cdroot`

<!-- -->

`crypt_root=<...>`
    :::
    ** Note**\
    Will require that at least initramfs was built with `--luks` option set.
    :::

<!-- -->

`crypt_swap=<...>`

<!-- -->

`root_trim=(yes|no)`
    :::
    ** Note**\
    Will require that at least initramfs was built with `--luks` option set and is only useful for flash-based volumes.
    :::

<!-- -->

`ip=<dhcp,addr/cidr>`

<!-- -->

`gk.net.dhcp.retries=<...>`

<!-- -->

`gk.net.iface=<interface,macaddr>`
    A MAC address (00:00:00:00:00:00 format) can be specified instead of an interface name.

<!-- -->

`gk.net.gw=<...>`

<!-- -->

`gk.net.routes=<...>`

<!-- -->

`gk.net.timeout.dad=<...>`

<!-- -->

`gk.net.timeout.deconfiguration=<...>`

<!-- -->

`gk.net.timeout.dhcp=<...>`

<!-- -->

`gk.net.timeout.interface=<...>`

<!-- -->

`gk.prompt.timeout=<...>`
    :::
    ** Note**\
    When dosshd is used, `gk.prompt.timeout` will be set to 30 seconds when not set. This will allow remote user to provide answer through `GK_PROMPT_FILE` which is set to [/tmp/current_prompt] by default.
    :::

<!-- -->

`dosshd`
    :::
    ** Note**\
    Will require that initramfs was built at least with `--ssh` option set.
    :::

<!-- -->

`gk.sshd.port=<...>`

<!-- -->

`gk.sshd.wait=<...>`

<!-- -->

`dolvm`
    :::
    ** Note**\
    Will require that initramfs was built at least with `--lvm` option set.
    :::

<!-- -->

`lvmraid=<...>`

<!-- -->

`domdadm` (Deprecated in Genkernel 4.2.0, udev rules now control MD assembly)
    :::
    ** Note**\
    Will require that initramfs was built at least with `--mdadm` option set.
    :::

<!-- -->

`dozfs[=cache,force]`
    :::
    ** Note**\
    Will require that initramfs was built at least with `--zfs` option set.
    :::

<!-- -->

`gk.log.disabled=<...>`

<!-- -->

`gk.log.keep=<...>`
    :::
    ** Note**\
    The default file [/genkernel-boot.log] on root was chosen because genkernel\'s initramfs will only mount root filesystem by default. To store the log file at [/var/log/genkernel-boot.log], the mount point must be accessible (see [/etc/initramfs.mounts]).
    :::

<!-- -->

`gk.hw.load-all=<...>`

## [FAQ]

### [][Can genkernel be used for systemd-based systems?]

Yes.

### [][Genkernel? Dracut?]

[[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]] in comparison to [[[sys-kernel/genkernel]](https://packages.gentoo.org/packages/sys-kernel/genkernel)[]] is just a generic tool for creating an initramfs. It does not create a kernel like [genkernel] does. I.e. while both, [genkernel] and [dracut] supports booting from LUKS-encrypted root volume, only [genkernel] will ensure that kernel will have all required options set. It\'s also worthwhile to mention that [genkernel] will compile most packages (LVM, cryptsetup, mdadm, sshd\...) used in initramfs on its own whereas [dracut] will copy binaries from host system which can be a problem for some setups. Thus, [genkernel] supports kernel/initramfs creation for another system (cross-compile) unlike [dracut] or [genkernel-next].

### [][Can a separate kernel/initramfs be created for tests?]

`root `[`#`]`genkernel --kernel-config=/proc/config.gz --kernel-append-localversion=-test42 --menuconfig all`

The above command causes [genkernel] to build a new kernel and initramfs (`all`) based on config from current running kernel (`--kernel-config=/proc/config.gz`), invoke menuconfig (`--menuconfig`) allowing user to adjust configuration and will append `-test42` to kernel\'s `LOCALVERSION` variable (`--kernel-append-localversion=-test42`) which will affect naming of kernel image, modules dir and initramfs by default.

### [][How can external modules (such as xtables-addons, nvidia-drivers\...) be rebuilt for a new kernel?]

By default, [genkernel] will call [emerge \@module-rebuild] when building a kernel to ensure that out-of-tree modules installed through the package manager are still present in new/rebuilt kernel. This feature can be toggled via `--[no-]module-rebuild` command-line argument or `MODULEREBUILD` in [/etc/genkernel.conf].

### [][How can additional commands be run after building the kernel?]

[Genkernel] provides a callback for that (before version 4, callback was used to rebuild external modules). See `CMD_CALLBACK` in [/etc/genkernel.conf] for more details.

### [][How can ccache or distcc be used with genkernel?]

Set up [ccache](https://wiki.gentoo.org/wiki/Ccache "Ccache") or [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") the normal way like for [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]]. Set `--kernel-cc` command-line parameter or adjust `KERNEL_CC` in [/etc/genkernel.conf] for the desired tool to use. Do the same for `UTILS_CC` (`--utils-cc`) and `UTILS_CXX` (`--utils-cxx`).

### [][ERROR: compile_kernel(): compile_generic() failed to compile the \"bzImage\" target!]

Check [/var/log/genkernel.log] first. In most cases, a root cause will appear like:

[FILE] **`/var/log/genkernel.log`**

    [...]
      AR      drivers/usb/built-in.a
      AR      drivers/built-in.a
      GEN     .version
      CHK     include/generated/compile.h
      AR      built-in.a
      LD      vmlinux.o
      MODPOST vmlinux.o
    ld: .tmp_vmlinux1: final close failed: No space left on device
    make: *** [Makefile:1032: vmlinux] Error 1

    * ERROR: compile_kernel(): compile_generic() failed to compile the "bzImage" target!
    * Please consult '/var/log/genkernel.log' for more information and any
    * errors that were reported above.
    *
    * Report any genkernel bugs to bugs.gentoo.org and
    * assign your bug to genkernel@gentoo.org. Please include
    * as much information as you can in your bug report; attaching
    * '/var/log/genkernel.log' so that your issue can be dealt with effectively.
    *
    * Please do *not* report kernel compilation failures as genkernel bugs!
    *

    * mount: >> Boot partition state on '/boot' was not changed; Skipping restore boot partition state ...
    >>> Ended on: 2019-12-16 02:30:19 (after 0 days 0 hours 07 minutes 49 seconds)
    </pre>

In other words: The system has run out of disk space (`No space left on device`) during compilation.

To guard against problems like this set `CHECK_FREE_DISK_SPACE_BOOTDIR=50` and `CHECK_FREE_DISK_SPACE_KERNELOUTPUTDIR=4000` in [/etc/genkernel.conf] in which case [genkernel] would fail early with a message like

`root `[`#`]`genkernel --kernel-config=/proc/config.gz all `

    * Gentoo Linux Genkernel; Version 4.0.1
    * Using genkernel configuration from '/etc/genkernel.conf' ...
    * Running with options: --kernel-config=/proc/config.gz all

    * Working with Linux kernel 4.19.89-gentoo-x86_64 for x86_64
    * Using kernel config file '/proc/config.gz' ...
    *
    * Note: The version above is subject to change (depends on config and status of kernel sources).
    * ERROR: 4000 MB free disk space is required in '/usr/src/linux' but only 1026 MB is available!
    [...]

### [][Is the order of kernel command-line arguments important?]

No.

### [][Required kernel option \'CONFIG_MICROCODE_INTEL\' or \'CONFIG_MICROCODE_AMD\' which genkernel tried to set is missing!]

Kernel v6.6 permanently applied the kernel config parameters (see [this commit](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=42a7f6e3ffe06308c1ec43a7dac39a27de101574)). This [was fixed in version 4.3.10](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=791a15028278c7cc1e463aee8b7d0c42d06583db) of [[[sys-kernel/genkernel]](https://packages.gentoo.org/packages/sys-kernel/genkernel)[]].

### [][Help! Something isn\'t working!]

To report a problem, please always provide [/var/log/genkernel.log] (sometimes it maybe necessary to compress that file before sharing or attaching to bugs) which will help developers a lot. Even if the command is run with `--loglevel=1` (default), the logfile will always contain complete output (no need to re-run with logging turned on) which will help developers to understand, reproduce and maybe fix a bug.

## [See also]

-   [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") --- an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") infrastructure and aims to have as little as possible hard-coded into the initramfs.
-   [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") --- a central part of the Gentoo [operating system (OS)](https://en.wikipedia.org/wiki/operating_system "wikipedia:operating system")
-   [Kernel/Configuration](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration")
-   [Project:Distribution Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") --- maintains sys-kernel/\*-kernel packages.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Tim Yamin, Jimi Ayodele, Thomas Seiler, Joshua Saddler (nightmorph), [Sebastian Pipping (sping)](https://wiki.gentoo.org/wiki/User:Sping "User:Sping") , [José Fournier (jaaf)](https://wiki.gentoo.org/wiki/User:Jaaf "User:Jaaf") **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*