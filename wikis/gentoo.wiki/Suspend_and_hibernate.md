This page contains [[changes](https://wiki.gentoo.org/index.php?title=Suspend_and_hibernate&diff=1423212)] which are not marked for translation.

\
This article describes how to suspend or hibernate a Gentoo system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Software]](#Software)
-   [[2] [Available suspend modes]](#Available_suspend_modes)
-   [[3] [Suspend to Idle]](#Suspend_to_Idle)
-   [[4] [Suspend to RAM]](#Suspend_to_RAM)
-   [[5] [Suspend to disk]](#Suspend_to_disk)
    -   [[5.1] [Suspend to disk and reboot afterwards]](#Suspend_to_disk_and_reboot_afterwards)
    -   [[5.2] [Suspend to disk with sys-auth/elogind]](#Suspend_to_disk_with_sys-auth.2Felogind)
    -   [[5.3] [Suspend to disk with swap file]](#Suspend_to_disk_with_swap_file)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Can not resume after suspend]](#Can_not_resume_after_suspend)
        -   [[6.1.1] [Buggy microcode]](#Buggy_microcode)
        -   [[6.1.2] [Dracut configured without resume module]](#Dracut_configured_without_resume_module)
    -   [[6.2] [WiFi stays hard blocked]](#WiFi_stays_hard_blocked)
    -   [[6.3] [Migration from pm-utils to elogind]](#Migration_from_pm-utils_to_elogind)
    -   [[6.4] [High Battery Drain in S2idle]](#High_Battery_Drain_in_S2idle)
    -   [[6.5] [Long delay before suspend]](#Long_delay_before_suspend)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Installation]

### [Kernel]

Make sure support for suspend and hibernation has been activated (`CONFIG_SUSPEND`) and (`CONFIG_HIBERNATION`):

[KERNEL]

    Power management and ACPI options --->
        [*] Suspend to RAM and standby
        [*] Hibernation (aka 'suspend to disk')

** Warning**\
Kernel versions 6.9.0 through 6.9.8 have broken suspend to disk support if there is a resume kernel parameter and any error is found checking and/or reading the suspend data. [Upstream bug 218845](https://bugzilla.kernel.org/show_bug.cgi?id=218845) is tracking the issue and is fixed in kernel 6.9.9.

### [Software]

One of the following packages can be used to control the in-kernel default suspend/hibernate implementation, namely, *[swsusp](https://en.wikipedia.org/wiki/swsusp "wikipedia:swsusp")*.

-   [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]] provides the following commands that can be launched as root or from a user account. Many [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") already require it if [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") is not used instead. Make sure it is [configured properly](https://wiki.gentoo.org/wiki/Elogind "Elogind").
    -   [loginctl suspend]
    -   [loginctl hibernate]
    -   [loginctl hybrid-sleep]
    -   [loginctl suspend-then-hibernate]
-   [[[sys-power/suspend]](https://packages.gentoo.org/packages/sys-power/suspend)[]] provides:
    -   [s2ram]
    -   [s2disk]
    -   [s2both]
-   [[[sys-power/hibernate-script]](https://packages.gentoo.org/packages/sys-power/hibernate-script)[]]

## [Available suspend modes]

To see available suspend modes use

`root `[`#`]`cat /sys/power/state`

    freeze mem disk

for swsusp, default implementation.

Those two file will list at least [ACPI](https://wiki.gentoo.org/wiki/ACPI "ACPI") S2/4 power down methods on modern hardware. New hardware would also support S5 method which is a rough S4 method. ACPI S2 correspond to suspend to ram (*ram* method in swsusp terms and *3* in ToI terms); S4 hibernation to disk (*disk* in swsusp terms and *4* in ToI terms; S5 hibernation to disk (*5* in ToI terms).

Swsusp users can choose between *platform*, meaning ACPI, or *shutdown* methods which can be echo-ed to [/sys/power/disk] sysfs file.

## [Suspend to Idle]

On modern hardware, traditional S3 suspend is being replaced by a set of fine-grained runtime power management capabilities for the S0 sleep state. This is referred to as S0ix by Intel and Modern Standby by Microsoft. To check available standby modes use

`root `[`#`]`cat /sys/power/mem_sleep`

    [s2idle] shallow

For S0ix to work, s2idle must be active.

## [Suspend to RAM]

Preferred commands to suspend are:

`root `[`#`]`s2ram`

or, if using [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]]:

`root `[`#`]`loginctl suspend`

See settings at **/etc/elogind/logind.conf**, in \[Sleep\] section **SuspendMode** must be **deep** if you want to disable fan noise on sleep.

For suspend (to RAM) for [[[sys-power/hibernate-script]](https://packages.gentoo.org/packages/sys-power/hibernate-script)[]] users:

`root `[`#`]`hibernate-ram`

or

`root `[`#`]`hibernate`

to hibernate (to disk).

A more \"raw\" method to directly communicate with the kernel is:

`root `[`#`]`echo mem > /sys/power/state`

** Note**\
This is not a configuration option! Instead it shows all available states and echo-ing one of them into it immediately executes this state.

## [Suspend to disk]

** Warning**\
If you are using [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") initramfs, you may experience [[[bug #156445]](https://bugs.gentoo.org/show_bug.cgi?id=156445)[]] which makes it impossible to resume after suspend-to-disk. There is a number of ways to avoid it, from editing initramfs (e.g. as described [here](https://forums.gentoo.org/viewtopic-p-7461806.html#7461806)) to dropping genkernel completely.

** Important**\
Remember, [swap](https://wiki.gentoo.org/wiki/Swap "Swap") file must contain all memory used by running processes and memory-based [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem"), like [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs") or [zram](https://wiki.gentoo.org/wiki/Zram "Zram"), prior to hibernating. However, unless specifically set, the hibernation image is compressed. Setting hibernation image size to half of the amount of installed RAM is a safe value in *most* cases. One of the cases where this does **not** fully apply is when the system has a high usage of [zswap](https://wiki.gentoo.org/wiki/Zswap "Zswap") which means that memory may already be compressed.

For suspend to disk to operate a swap partition or swap file must exist.

The swap file should be active beforehand and should be echoed on the appropriate file before any attempt to suspend/hibernate.

`root `[`#`]`echo /dev/sda1 > /sys/power/resume`

A more \"raw\" method is to:

`root `[`#`]`echo disk > /sys/power/state`

\

### [Suspend to disk and reboot afterwards]

Let\'s say you just want to save your current session and boot into another OS, it is not necessary to do a regular hibernation including shutdown. It is sufficient to just create the hibernate image (within swap or a swap file) and reboot afterwards:

`root `[`#`]`echo reboot > /sys/power/disk`

`root `[`#`]`echo disk > /sys/power/state`

If this didn\'t work, please check the available options on your system (and [debugging hibernation and suspend](https://docs.kernel.org/power/basic-pm-debugging.html) on kernel.org). When reboot is available, after echo-ing it you will see something like this (the active/chosen option is within brackets):

`root `[`#`]`cat /sys/power/disk`

    platform shutdown [reboot] suspend test_resume

Further information can be found within the documentation on [kernel.org](https://www.kernel.org/doc/Documentation/power/interface.txt) for [/sys/power/disk] resp. [/sys/power/state] sysfs file.

** Important**\
When rebooting the hibernated system again, the chosen option in [/sys/power/disk] is still the same (`reboot`). Change it again if you want to shutdown your system next time using hibernate this way.

** Note**\
Neither KDE/Plasma or loginctl respect the value (`reboot`) in [/sys/power/disk] when hibernating the system and still poweroff. At least on my system.

### [][Suspend to disk with sys-auth/elogind]

First, make sure a swap partition has been set, [grub.cfg] rebuilt and the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") (if any) updated as shown above.

Reboot the system:

`root `[`#`]`loginctl reboot`

Next, try running:

`root `[`#`]`loginctl hibernate`

### [Suspend to disk with swap file]

You can use suspend to disk with a swap file. When you have a functional swap file you need to configure [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") parameters (via [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), etc.).

First find UUID of device where your swap file resides. For example [/dev/sda1].

** Warning**\
When swap file resides in a [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") volume, GRUB must be compiled with LVM support - `device-mapper` USE flag. Otherwise, the system will not wake up and will be cold started.

`root `[`#`]`blkid /dev/sda1`

Find offset of swap file on given partition using the [swap-offset] utility from [[[sys-power/suspend]](https://packages.gentoo.org/packages/sys-power/suspend)[]]:

** Important**\
[Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") filesystem requires to compute the offset of the swap file a different way, see [Arch Linux wiki, Hibernation into a swap file on Btrfs](https://wiki.archlinux.org/title/Power_management/Suspend_and_hibernate#Hibernation_into_swap_file_on_Btrfs).

`root `[`#`]`swap-offset /path/to/swapfile`

After that edit GRUB config and add required parameters to the boot string:

[FILE] **`/etc/default/grub`GRUB defaults**

    GRUB_CMDLINE_LINUX_DEFAULT="resume=UUID=<UUID_of_partition> resume_offset=<offset_of_swapfile>"

Rebuild GRUB config:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

Reboot the system and check used kernel parameters:

`user `[`$`]`cat /proc/cmdline`

It should now be possible to hibernate the system.

## [Troubleshooting]

Classic kernel buffer comes handy:

`user `[`$`]`dmesg`

### [Can not resume after suspend]

#### [Buggy microcode]

Try disabling the security chip setting in BIOS/UEFI and try again. Outdated [microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") can result in dysfunction of resumption from suspension, thus make sure it is updated (eg. [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode") with i915 drivers).

For i915 drivers if the microcode update is ineffective, try disabling `CONFIG_RETPOLINE` at the cost of [Spectre v2 vulnerability](https://en.wikipedia.org/wiki/Spectre_(security_vulnerability) "wikipedia:Spectre (security vulnerability)").

#### [Dracut configured without resume module]

If using [[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]] for the creation of the [initramfs], be sure the [resume] module is included in the image. For example, the configuration file could contain:

[FILE] **`/etc/dracut.conf`**

    add_dracutmodules+=" resume "

### [WiFi stays hard blocked]

Although possibly *unsafe*, tricking the BIOS into believing it being \"Microsoft Windows\" might solve it.

** Important**\
Enabling this feature can cause compatibility issues for I2C/ACPI HID devices (touchpads, etc)

This can be done by adding `acpi_osi=! acpi_osi=Windows` or `acpi_osi=! acpi_osi='Windows 2009'`[(kernel source)](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/drivers/acpi/acpica/utosi.c) to the boot command line options.

For [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]], the options can be appended to `GRUB_CMDLINE_LINUX` in [/etc/default/grub].

### [Migration from pm-utils to elogind]

Copy any suspend/resume and hibernate/thaw hook scripts from the directory [/etc/pm/sleep.d/] to [/lib64/elogind/system-sleep/], and modify them to cater for the new \$1 (\'pre\' or \'post\') and \$2 (\'suspend\', \'hibernate\', or \'hybrid-sleep\'). See also: [Elogind#Suspend.2FHibernate_Resume.2FThaw_hook_scripts](https://wiki.gentoo.org/wiki/Elogind#Suspend.2FHibernate_Resume.2FThaw_hook_scripts "Elogind")

### [High Battery Drain in S2idle]

On many systems, it is necessary to override certain power management defaults to achieve S0ix properly. To test and troubleshoot such problems, Intel\'s [S0ixSelftestTool](https://github.com/intel/S0ixSelftestTool) is recommended.

### [Long delay before suspend]

Systemd versions from v256 and later will attempt to freeze the user session before suspending. If QEMU is running, Systemd might fail to freeze it and time out after 60 seconds before suspending.^[\[1\]](#cite_note-1)^ This can be identified by the \`Failed to freeze unit \'user.slice\'\` message in the output of `journalctl -b`.

To work around this, Systemd\'s freezing can be disabled (without disabling the kernel\'s freezing) by [customizing](https://wiki.gentoo.org/wiki/Systemd#Customizing_unit_files "Systemd") systemd-suspend.service with the following configuration:

[FILE] **`/etc/systemd/system/systemd-suspend.service.d`**

    [Service]
    Environment="SYSTEMD_SLEEP_FREEZE_USER_SESSIONS=false"

## [See also]

-   [Power management/Guide](https://wiki.gentoo.org/wiki/Power_management/Guide "Power management/Guide") --- a guide to setup power management features of a laptop.
-   [Custom Initramfs/Hibernation](https://wiki.gentoo.org/wiki/Custom_Initramfs/Hibernation "Custom Initramfs/Hibernation") --- describes how to enable hibernation with a custom initramfs.

## [External resources]

-   [Suspend and hibernate](https://wiki.archlinux.org/index.php/Power_management/Suspend%20and%20hibernate) on wiki.archlinux.org
-   [Linux kernel documentation - swsusp.txt](https://www.kernel.org/doc/Documentation/power/swsusp.txt), or the usual location of [/usr/src/linux/Documentation/power/swsusp.txt]
-   [Gentoo Forums: Suspend and Hibernate with UEFI](https://forums.gentoo.org/viewtopic-p-8111048.html#8111048)
-   [How to achieve S0ix states in Linux](https://01.org/blogs/qwang59/2018/how-achieve-s0ix-states-linux) details on how to enable and troubleshoot S0ix in Linux

## [References]

1.  [[[↑](#cite_ref-1)] [lucS. [freezes during suspend after 2024-06-13 qemu update - General system / Kernel, boot, graphics & hardware - EndeavourOS](https://forum.endeavouros.com/t/system-freezes-during-suspend-after-2024-06-13-qemu-update/57123/2%7CSystem), July 21, 2024. Retreived on January 13th, 2026]]