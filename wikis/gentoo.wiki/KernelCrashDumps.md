**Resources**

[[]][Home](http://lse.sourceforge.net/kdump/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Kdump_(Linux) "wikipedia:Kdump (Linux)")

[[]][Official documentation](https://www.kernel.org/doc/Documentation/kdump/kdump.txt)

[[]][GitWeb](https://git.kernel.org/cgit/utils/kernel/kexec/kexec-tools.git/)

This article explains how to capture the kernel crash dumps (also known as **kdumps**). Kdumps are produced by kernel panic or lockup. To be simple, just a single kernel is used both for the ordinary system and recovery. The described method is *almost* distribution independent.

This article is based on [KDump on Gentoo](http://rich0gentoo.wordpress.com/2011/11/11/kdump-on-gentoo/) by [Richard Freeman (rich0)](https://wiki.gentoo.org/wiki/User:Rich0 "User:Rich0") , and the first version is posted by the author.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [local.d script]](#local.d_script)
    -   [[2.2] [Bootloader]](#Bootloader)
-   [[3] [Usage]](#Usage)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Kernel is not loading]](#Kernel_is_not_loading)
    -   [[4.2] [VGA not resetting]](#VGA_not_resetting)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

Activate the following kernel options:

CONFIG_KEXEC, CONFIG_CRASH_DUMP, CONFIG_RELOCATABLE

CONFIG_DEBUG_KERNEL, CONFIG_DEBUG_INFO

CONFIG_PROC_FS, CONFIG_PROC_KCORE, CONFIG_PROC_VMCORE

[KERNEL]

    Processor type and features --->
        [*] kexec system call
        [*] kernel crash dumps
        [*] Build a relocatable kernel
    Kernel hacking  --->
        [*] Kernel debugging
        Compile-time checks and compiler options --->
            [*] Compile the kernel with debug info
    File systems  --->
        Pseudo filesystems  --->
            -*- /proc file system support
            [*]   /proc/kcore support
            [*]   /proc/vmcore support

** Note**\
`CONFIG_PHYSICAL_START` might need to be set greater than 2 MB (`0x200000`) on some motherboards to offset the kernel\'s memory space enough to avoid the BIOS clobber. Try setting `0x1000000` (16 MB) if the above Kernel options are not working as expected.

### [USE flags]

### [USE flags for] [sys-apps/kexec-tools](https://packages.gentoo.org/packages/sys-apps/kexec-tools) [[]] [Load another kernel from the currently executing Linux kernel]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`booke`](https://packages.gentoo.org/useflags/booke)       Include support for Book-E memory management
  [`lzma`](https://packages.gentoo.org/useflags/lzma)         Enables support for LZMA compressed kernel images
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`xen`](https://packages.gentoo.org/useflags/xen)           Enable extended xen support
  [`zlib`](https://packages.gentoo.org/useflags/zlib)         Add support for zlib compression
  [`zstd`](https://packages.gentoo.org/useflags/zstd)         Enable support for ZSTD compression
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-16 16:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Merge:

`root `[`#`]`emerge --ask sys-apps/kexec-tools`

## [Configuration]

### [local.d script]

Create [/etc/local.d/kdump.start] containing:

[FILE] **`/etc/local.d/kdump.start`**

    #!/bin/bash
    kexec -p /[path-to-kernel] --append="root=[root-device] single irqpoll maxcpus=1 reset_devices"

** Note**\
Your system may require core headers in ELF32 or ELF64 format for the kernel to boot. Check the manpage for details.

When using an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"), a reference to it will need passed as a parameter. For example:

[FILE] **`/etc/local.d/kdump.start`**

    #!/bin/bash
    kexec -p /boot/kernel-genkernel-x86_64-3.16.1-gentoo \
          --initrd=/boot/initramfs-genkernel-x86_64-3.16.1-gentoo \
          --append="root=/dev/mapper/lvm-slash single irqpoll maxcpus=1 reset_devices dolvm softlevel=kdump"

Now make this file executable:

`root `[`#`]`chmod u+x /etc/local.d/kdump.start`

Note the kernel has to be readable. A typical Gentoo configuration leaves [/boot] unmounted, so either remove *noauto* from the [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") file or place a copy of the kernel in a place that is mounted during a crash.

### [Bootloader]

Add the `crashkernel=64M nokaslr` argument to the kernel command-line via the bootloader (most likely [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB")) for systems with up to around 12 GB of RAM.

** Note**\
`nokaslr` disables KASLR security feature. You can omit this option, but then you will have to manually load symbols from all kernel sections in [gdb] because kernel location is randomized.

## [Usage]

First, run the above script:

`root `[`#`]`/etc/local.d/kdump.start`

It loads the rescue kernel image which is run after kernel crash.

Whenever a kernel panic or lockup (hard/soft if the kernel is set to detect them) occurs, [kexec] runs the kernel in crash mode, relocated to a reserved area of memory. The rest of RAM will be untouched. When the system boots up log in and copy [/proc/vmcore] to a file - this is the crash dump. Then reboot the system to get back to a normal configuration; the system might not be stable and should not continue to operate in this state.

A kernel panic can be forced on demand by executing the following command (do not forget to save all data, log-out other users, and leave the filesystems in a clean state by the invocation of the [sync] command before doing this):

`root `[`#`]`echo c | tee /proc/sysrq-trigger`

## [Troubleshooting]

### [Kernel is not loading]

If the kernel is not loading when [kexec] is called, check to to see if kernel compression was set to xz (lzma) format.

If xz compression is used the [[[sys-apps/kexec-tools]](https://packages.gentoo.org/packages/sys-apps/kexec-tools)[]] package will need to be re-emerged with the `lzma` USE flag enabled.

### [VGA not resetting]

After loading a kexec crash kernel and after a kernel panic kexec does not appear to load the crash kernel. The output on the display freezes.

This might be caused by the VGA port not being reset. The solution may be to tell kexec to reset the display output on the VGA port. Something like the following could work (the important options being `--reset-vga --console-vga`):

`root `[`#`]`kexec -p /boot/kernel-gentoo --initrd=/boot/initramfs-gentoo --reset-vga --console-vga --command-line="root=/dev/sda3 maxcpus=1 irqpoll"`

## [External resources]

-   [Official RedHat Enterprise Linux 7 Kernel Crash Dump Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Kernel_Crash_Dump_Guide/index.html)
-   [Linux Kernel Crash Book](https://www.dropbox.com/s/ktbz9fy7qbwsyfa/www.dedoimedo.com-crash-book.pdf)