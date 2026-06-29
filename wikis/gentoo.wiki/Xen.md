**Resources**

[[]][Home](https://xenproject.org/)

[[]][Blog](https://blog.xenproject.org)

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Xen "Project:Xen")][Project](https://wiki.gentoo.org/wiki/Project:Xen "Project:Xen")

[[]][Wikipedia](https://en.wikipedia.org/wiki/Xen "wikipedia:Xen")

[[]][Official documentation](https://xenproject.org/help/documentation/)

[Xen](https://xenproject.org/about-us/) is a native, or bare-metal, [hypervisor](https://en.wikipedia.org/wiki/Hypervisor "wikipedia:Hypervisor") that allows multiple distinct virtual machines (referred to as domains) to share a single physical machine. As the highest privilege process on the system, Xen is responsible for the distribution of processor and memory resources between guest domains on the host. Other hardware resources such as network interfaces, disks, or direct PCI/USB devices are controlled by a privileged domain known as domain-0 (dom0).

From its inception Xen has focused on the [para-virtualization](https://en.wikipedia.org/wiki/Paravirtualization "wikipedia:Paravirtualization") approach to hypervisor design. As a result, Xen guests or unprivileged domains (domU) are typically aware of the hypervisor and their status as guests. The base system, Domain-0, must have inherent Xen support, however, unmodified domU guests are supported on hardware which implements Intel (VT-x) or AMD (SVM) virtualization technology.

## Contents

-   [[1] [Host configuration (domain-0)]](#Host_configuration_.28domain-0.29)
    -   [[1.1] [Preparation]](#Preparation)
        -   [[1.1.1] [BIOS and UEFI firmware]](#BIOS_and_UEFI_firmware)
        -   [[1.1.2] [Rebuilding the Gentoo installation?]](#Rebuilding_the_Gentoo_installation.3F)
        -   [[1.1.3] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Installation]](#Installation)
        -   [[1.3.1] [Emerge]](#Emerge)
        -   [[1.3.2] [Performance tuning]](#Performance_tuning)
        -   [[1.3.3] [Runlevel]](#Runlevel)
        -   [[1.3.4] [Bootloader]](#Bootloader)
            -   [[1.3.4.1] [Default: GRUB]](#Default:_GRUB)
            -   [[1.3.4.2] [Alternative: LILO]](#Alternative:_LILO)
            -   [[1.3.4.3] [Alternative: UEFI]](#Alternative:_UEFI)
        -   [[1.3.5] [Booting Xen]](#Booting_Xen)
-   [[2] [Creating an unprivileged domain (domU)]](#Creating_an_unprivileged_domain_.28domU.29)
    -   [[2.1] [Building the kernel]](#Building_the_kernel)
    -   [[2.2] [Creating the domain disks]](#Creating_the_domain_disks)
    -   [[2.3] [Configuring a domain]](#Configuring_a_domain)
    -   [[2.4] [Launching the new domain]](#Launching_the_new_domain)
-   [[3] [Networking on domains]](#Networking_on_domains)
    -   [[3.1] [Introduction]](#Introduction)
    -   [[3.2] [Bridged interfaces]](#Bridged_interfaces)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Unable to passthrough USB mouse and keyboard to HVM (Windows 7) domU in Xen 4.7.3]](#Unable_to_passthrough_USB_mouse_and_keyboard_to_HVM_.28Windows_7.29_domU_in_Xen_4.7.3)
    -   [[4.2] [Xen domU hanging with kernel 4.3+]](#Xen_domU_hanging_with_kernel_4.3.2B)
    -   [[4.3] [Xen domU hanging with Xen 4.12+]](#Xen_domU_hanging_with_Xen_4.12.2B)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [][Host configuration (domain-0)]

### [Preparation]

#### [BIOS and UEFI firmware]

While paravirtualized (PV) guests can run on a host without any form of hardware accelerated virtualization extensions this severely restricts the set of available guests and prevents the use of new and exciting modes such as [PVH](https://wiki.xenproject.org/wiki/PVH_(v2)_Domu).

The following command should provide a highlighted row for each processor if the corresponding feature is present:

`user `[`$`]`grep --color -E "vmx|svm" /proc/cpuinfo`

Unfortunately motherboard manufacturers often explicitly disable these virtualization extensions via [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") or UEFI settings. If you don\'t see support listed check your BIOS/UEFI configuration for flags related to virtualization.

#### [][Rebuilding the Gentoo installation?]

A dramatic change that might be necessary on 32-bit systems is to rebuild the entire Gentoo installation with a different `CFLAGS` setting. Guest operating systems running under Xen might otherwise see major performance degradation. If you, however, are planning on checking out Xen rather than installing it for production use and are not terribly fond of rebuilding all programs, you can skip this step. In this case you will notice performance degradation but you will still be able to use Xen.

** Important**\
It is advised that, if you change your `CFLAGS` and build your system with a GCC lower than version 4, you do not have `-Os` set as it has been reported to produce broken code.

Add `-mno-tls-direct-seg-refs` ONLY if you have a 32-bit dom0. You don\'t need this flag if you have a 64-bit dom0.

[FILE] **`/etc/portage/make.conf`CFLAGS change for mno-tls-direct-seg-refs**

    CFLAGS="... -mno-tls-direct-seg-refs"

`root `[`#`]`emerge -e @world`

If you boot your system using an initial ramdisk (initrd) you need to rebuild the initrd as well (which is best done by running all steps you would do when you rebuild your kernel).

#### [Kernel]

Next we\'ll build the Linux kernel with Xen support. This kernel, whose sources are available at [/usr/src/linux] , will be our main running kernel (i.e. the one running domain 0). In the `XEN` section you\'ll find drivers for all kinds of input/output, each driver having a *backend* and *frontend* implementation available. For the domain 0 kernel you need to select the *backend* implementation: these are used by the other domains (who use the *frontend* drivers) to communicate directly with the hardware. However, you should be able to configure the kernel to provide support for both frontend (guest) and backend (host) drivers.

If you\'re wondering about networking: each interface in a domain has a point-to-point link to an interface on domain 0 (called [vifX.Y] where X is the domain number and Y the Yth interface of that domain), so you can configure your network the way you want (bridging, NAT, etc.)

Enable general Xen support:

[KERNEL] **Xen Base**

    Processor type and features  --->
       [*] Linux guest support  --->
          [*]   Enable paravirtualization code
          [*]     Paravirtualization layer for spinlocks
          [*]     Xen guest support
          [*]       Support for running as a PVH guest

Add support for paravirtualized console connections:

[KERNEL] **PV Console**

    Device Drivers  --->
       Character devices  --->
          [*] Xen Hypervisor Console support
          [*]   Xen Hypervisor Multiple Consoles support

Facilitates guest access to block and network devices via dom0:

[KERNEL] **Disk and Network**

    Device Drivers  --->
       [*] Block devices  --->
          <*>   Xen virtual block device support
       [*] Network device support  --->
          <*>   Xen network device frontend driver

In some configurations it can be desirable to provide a guest with direct access to a PCI device. This is known as [Xen PCI Passthrough](https://wiki.xenproject.org/wiki/Xen_PCI_Passthrough):

[KERNEL] **Guest PCI Passthrough**

    Device Drivers  --->
      [*] PCI support  --->
        <*> Xen PCI Frontend

Keyboard, mouse, and display support via dom0 backend:

[KERNEL] **Guest human interface**

    Device Drivers  --->
       Input device support  --->
          [*] Miscellaneous devices  --->
             <*>   Xen virtual keyboard and mouse support
       Graphics support  --->
             Frame buffer Devices  --->
                <*> Xen virtual frame buffer support

Xen dom0 support depends on ACPI; without it dom0 related options will be hidden:

[KERNEL] **ACPI support**

    Power management and ACPI options  --->
       [*] ACPI (Advanced Configuration and Power Interface) Support  --->

Typical network configurations depend on Linux bridge functionality:

[KERNEL] **Linux bridge**

    [*] Networking support --->
       Networking options  --->
             <*> 802.1d Ethernet Bridging
         [*] Network packet filtering framework (Netfilter) --->
                [*] Advanced netfilter configuration
                [*]   Bridged IP/ARP packets filtering

[Fully virtualized (HVM)](https://wiki.xenproject.org/wiki/Xen_Project_Software_Overview#HVM_and_its_variants_.28x86.29) guests depend on Universal TUN/TAP device driver support for their network interfaces. This option is required if you plan to create fully [Emulated Network Devices](https://wiki.xenproject.org/wiki/Xen_Networking#Emulated_Network_Devices) within Dom0/DomU configuration.

[KERNEL] **TUN and TAP virtual network kernel devices**

    [*] Device Drivers  --->
       Network device support --->
          <M> Universal TUN/TAP device driver support

The remaining drivers flesh out memory management, domain-to-domain communication, and communication to Xen via sysfs interfaces:

[KERNEL] **Xen Drivers**

    Device Drivers  --->
       [*] Block devices  --->
             <*>   Xen block-device backend driver
       [*] Network device support --->
             <*>   Xen backend network device
       Xen driver support  --->
             [*] Xen memory balloon driver
             [*]   Scrub pages before returning them to system
             <*> Xen /dev/xen/evtchn device
             [*] Backend driver support
             <*> Xen filesystem
             [*]   Create compatibility mount point /proc/xen
             [*] Create xen entries under /sys/hypervisor
             <*> userspace grant access device driver
             <*> User-space grant reference allocator driver
             <M> Xen PCI-device backend driver
             <*> Xen ACPI processor
             [*] Xen platform mcelog

With all of the above configuration enabled, this kernel image should be able to boot as the dom0 host or as another domU guest. Note that the domU kernel can be slimmed down significantly if desired.

### [USE flags]

The first set of use flags correspond directly to the Xen hypervisor. Of these, ensure that EFI support is selected if you plan to configure EFI boot.

### [USE flags for] [app-emulation/xen](https://packages.gentoo.org/packages/app-emulation/xen) [[]] [The Xen virtual machine monitor]

  ------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+boot-symlinks`](https://packages.gentoo.org/useflags/+boot-symlinks)   Symlink xen.gz variants in /boot, disable on fat filesystems
  [`debug`](https://packages.gentoo.org/useflags/debug)                     Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`flask`](https://packages.gentoo.org/useflags/flask)                     Enable the Flask XSM module from NSA
  [`secureboot`](https://packages.gentoo.org/useflags/secureboot)           Automatically sign efi executables using user specified key
  [`uefi`](https://packages.gentoo.org/useflags/uefi)                       Adds UEFI boot support, requires LDFLAG -melf_x86_64 for amd64
  ------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-22 13:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

In addition to the core hypervisor Xen depends on a set of supporting libraries and management tools.

### [USE flags for] [app-emulation/xen-tools](https://packages.gentoo.org/packages/app-emulation/xen-tools) [[]] [Xen tools including QEMU and xl]

  ------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+hvm`](https://packages.gentoo.org/useflags/+hvm)                             Enable support for hardware based virtualization (VT-x,AMD-v)
  [`+ipxe`](https://packages.gentoo.org/useflags/+ipxe)                           Enable ipxe support
  [`+qemu`](https://packages.gentoo.org/useflags/+qemu)                           Enable IOEMU support via the use of qemu-dm
  [`+qemu-traditional`](https://packages.gentoo.org/useflags/+qemu-traditional)   Build the old qemu traditional device model (useful only if you cannot change to the new device model e.g. Windows VMs)
  [`+rombios`](https://packages.gentoo.org/useflags/+rombios)                     Enable rombios support, needed by ipxe
  [`api`](https://packages.gentoo.org/useflags/api)                               Build the C libxenapi bindings
  [`debug`](https://packages.gentoo.org/useflags/debug)                           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                               Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`lzma`](https://packages.gentoo.org/useflags/lzma)                             Support for LZMA compression algorithm
  [`ocaml`](https://packages.gentoo.org/useflags/ocaml)                           Add support/bindings for the Ocaml language
  [`ovmf`](https://packages.gentoo.org/useflags/ovmf)                             Enable support to boot UEFI guest vm, needed by hvm
  [`pygrub`](https://packages.gentoo.org/useflags/pygrub)                         Install the pygrub boot loader
  [`python`](https://packages.gentoo.org/useflags/python)                         Add optional support/bindings for the Python language
  [`screen`](https://packages.gentoo.org/useflags/screen)                         Enable support for running domain U console in an app-misc/screen session
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                               Add support for Simple Direct Layer (media library)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)               Build static versions of dynamic libraries as well
  [`system-ipxe`](https://packages.gentoo.org/useflags/system-ipxe)               Using sys-firmware/ipxe instead of the bundled one
  [`system-qemu`](https://packages.gentoo.org/useflags/system-qemu)               Using app-emulation/qemu instead of the bundled one
  [`system-seabios`](https://packages.gentoo.org/useflags/system-seabios)         Using sys-firmware/seabios instead of the bundled one
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                       Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                             Enable support for ZSTD compression
  ------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-22 13:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Installation]

#### [Emerge]

Xen will automatically deploy the compiled, boot-able hypervisor in [/boot]. If you have a separate [boot partition](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks#Creating_the_boot_partition "Handbook:AMD64/Installation/Disks") ensure that it is mounted.

`root `[`#`]`mount /boot`

After you have reviewed and updated the relevant USE flags, emerge xen and xen-tools:

`root `[`#`]`emerge --ask app-emulation/xen app-emulation/xen-tools`

Once the installation process completes [/boot/xen.gz] should be present.

#### [Performance tuning]

When configuring a host with a significant amount of memory it is beneficial to fix the allocated to dom0 and disable ballooning functionality. This ensures Xen and the dom0 operating system are able to build working structures based on the memory available at boot-time and have their assumptions hold throughout operation. Additionally, in the event that a large number of guests are created, dom0 is explicitly protected from external memory pressure.

In a GRUB environment the following directive assigns 1 GiB of memory to the dom0 guest:

[FILE] **`/etc/default/grub`GRUB limit dom0 memory**

    GRUB_CMDLINE_XEN_DEFAULT="dom0_mem=1024M,max:1024M"

Ballooning should also be disabled by setting autoballoon to either \"off\" or \"auto\" in [/etc/xen/xl.conf].

Further detail on this topic and other related tuning suggestions can be found on the [Tuning Xen for Performance](https://wiki.xen.org/wiki/Tuning_Xen_for_Performance) article on the Xen wiki.

#### [Runlevel]

In order for your new Xen environment to function correctly a number of daemons must be started. The following table provides a brief overview of each daemon and its function.

  -------------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Init Script    Required   Description
  xencommons     Yes        This daemon ensures all Xen related kernel modules are loaded in a dom0 system. Additionally, in dom0 and domU pv_ops systems it mounts [/proc/xen] as type xenfs.
  xenconsoled    Yes        Manages xl console sessions between dom0 and domU guests.
  xendomains     No         Automatically starts all domU configuration files found in [/etc/xen/auto/].
  xenstored      Yes        Manages both disk and network I/O configuration and operations between the dom0 environment and other domU guests.
  xen-watchdog   ?          Probably kills the dom0 environment or Xen in general if it becomes unresponsive for too long. It looks like this may have been removed
  xenqemudev     ?          Facilitates QEMU based disks for Xen guests. This comment is incomplete.
  -------------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

** Note**\
The xen-watchdog init script currently has not been migrated from sysvinit to the runscript/openRC format.

To add these daemons directly to the default runlevel perform the following:

`root `[`#`]`rc-update add xencommons default `

`root `[`#`]`rc-update add xenconsoled default `

`root `[`#`]`rc-update add xendomains default `

`root `[`#`]`rc-update add xenstored default `

`root `[`#`]`rc-update add xen-watchdog default `

These daemons should only be started when the system boots into Xen. As this may not always be the case, it may be desirable to keep these services out of the default runlevel. One possible alternative is to utilize an alternate default runlevel via the softlevel kernel parameter. The following example, based on [this blog post](https://michaelmk.blogspot.com/2012/05/different-runlevels-in-gentoo.html), creates a new runlevel named xen.

First create the new runlevel:

`root `[`#`]`install -d /etc/runlevels/xen `

Stack the default runlevel onto it:

`root `[`#`]`rc-update -s add default xen`

Then instead of adding the xen daemons to the default runlevel add them to the xen level:

`root `[`#`]`rc-update add xencommons xen `

`root `[`#`]`rc-update add xenconsoled xen `

`root `[`#`]`rc-update add xendomains xen `

`root `[`#`]`rc-update add xenstored xen `

`root `[`#`]`rc-update add xen-watchdog xen `

Once all of these steps have been completed add the following statement to the GRUB default file:

[FILE] **`/etc/default/grub`Setting the softlevel**

    # Replace the default runlevel with "xen"
    GRUB_CMDLINE_LINUX_XEN_REPLACE_DEFAULT="softlevel=xen"

#### [Bootloader]

In order for Xen to be the highest privilege process it must be the initial boot target, however, it must also subsequently boot the dom0 kernel.

##### [Default: GRUB]

[GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") provides auto-configuration scripts through [grub-mkconfig] which will generate the appropriate settings based on the kernel [.config]. If the scripts detect Xen dom0 options they will append Xen hypervisor boot lines to the GRUB menu. Note that for this to function correctly the kernel config file must be located in one of the following directories with a suffix matching the desired kernel:

  --------------- ------------------ -----------------------------------------
  Directory       File Prefix        Example
  /etc/kernels/   kernel-config-\*   /etc/kernels/kernel-config-4.0.5-gentoo
  /boot           config-\*          /boot/config-4.0.5-gentoo
  --------------- ------------------ -----------------------------------------

The example column above assumes a kernel named /boot/kernel-4.0.5-gentoo.

The following variables in [/etc/default/grub] are the most common ones to set to control how GRUB will function:

  ----------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Variable                                              Explanation
  `GRUB_CMDLINE_XEN`                         Extra parameters to be passed on the Xen command line for all Xen menu entries. For instance, to have a timestamped Xen dmesg, users will need to add `GRUB_CMDLINE_XEN="console_timestamps=boot"`.
  `GRUB_CMDLINE_XEN_DEFAULT`                 Parameters to be passed on the Xen command line for non-recovery Xen menu entries.
  `GRUB_CMDLINE_LINUX_XEN_REPLACE_DEFAULT`   Overrides the `GRUB_CMDLINE_LINUX_DEFAULT` variable from the above Linux section for Xen boot lines only. Users may prefer to start a specific softlevel for xen via `GRUB_CMDLINE_LINUX_XEN_REPLACE_DEFAULT="softlevel=xen"`
  ----------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For a more complete list, please refer to the [GRUB configuration variables](https://wiki.gentoo.org/wiki/GRUB/Configuration_variables "GRUB/Configuration variables") sub-page.

Now update the GRUB configuration file in the boot directory.

`root `[`#`]` grub-mkconfig -o /boot/grub/grub.cfg `

GRUB support is also included in [[genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel")] and can be triggered during the build process:

`root `[`#`]`genkernel --oldconfig --menuconfig --install --bootloader=grub --symlink --disklabel --lvm --mdadm --makeopts=-j9 all`

##### [Alternative: LILO]

To make lilo load the kernel, you need to pack the hypervisor, dom0 and initrd images into a single image. This can be achieved with the tool `mbootpack`. You need to decompress all images in order to pass them to `mbootpack`.

`root `[`#`]`mbootpack -o /boot/kernel-4.0.x.y-xen0-pack -m /boot/kernel-4.0.x.y-xen0.decompressed -m /boot/initrd-4.0.x.y-xen0.decompressed /boot/xen.decompressed`

Then you can configure lilo to use the newly created image.

[FILE] **`/etc/lilo.conf`LILO Configuration for Xen**

    image=/boot/kernel-4.0.x.y-xen0-pack
        label=XENGentoo4
        read-only
        root=/dev/sda3
        softlevel=xen

Finally, run the `lilo` binary.

`root `[`#`]`lilo`

##### [Alternative: UEFI]

It is possible to create a Xen [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub") and launch it directly from your machine\'s UEFI boot rom, without needing Grub or Lilo. See the [Xen project\'s EFI page](https://wiki.xenproject.org/wiki/Xen_EFI) for detailed information. [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") has some background information regarding Gentoo, and the handbook\'s Installation/Disks page talks about EFI System partion requirements.

This mode requires the flag [[[uefi]](https://packages.gentoo.org/useflags/uefi)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]. As noted in its description, on the amd64 platform this also requires a special LDFLAG setting. You can place it in your [/etc/portage/make.conf] file, or specify it for just this one merge:

`root `[`#`]`LDFLAGS="-melf_x86_64" emerge --ask app-emulation/xen app-emulation/xen-tools`

The ebuild assumes your [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP) mountpoint is [/boot], and will install the Xen stub files in [/boot/efi/gentoo/xen-VERSION.efi] (or its FAT-equivalent [/boot/EFI/gentoo/xen-VERSION.efi]). That same directory must also contain the [vmlinuz], [initramfs], and [xen.cfg] files. The latter tells the Xen stub which kernel files to load. An example of this is:

[FILE] **`/boot/efi/gentoo/xen.cfg`Xen stub configuration file**

    [global]
    default=gentoo-6.8.0

    [gentoo-6.8.0]
    options=dom0_mem=1536M console=vga vga=text-80x60,keep console_timestamps
    kernel=vmlinuz-6.8.0 root=/dev/mapper/dom0root ro rd.auto=1 console=hvc0 xcons=tty earlyprintk=xen
    ramdisk=initramfs-6.8.0.img

After creating the stub you must tell the boot ROM about it with the [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") command:

`root `[`#`]`efibootmgr -c -L "Xen 4.7.1" -l '\efi\gentoo\xen-4.7.1.efi'`

#### [Booting Xen]

Once you are satisfied with your configuration, reboot the system into Xen. Assuming everything worked correctly Xen should transfer display control to the dom0 environment, which will operate just like the original bare-metal system.

Running [xl list] should result in output similar to the following if Xen is functioning correctly:

`root `[`#`]`xl list `

    Name                                        ID   Mem VCPUs      State   Time(s)
    Domain-0                                     0  1024    24     r-----      22.0

At this point you may want to configure your system to boot into Xen by default. When utilizing GRUB, add the following lines to the GRUB defaults file:

[FILE] **`/etc/default/grub`Enabling Saved Defaults**

    # Default menu entry
    GRUB_DEFAULT="saved"
    GRUB_SAVEDEFAULT="true"

Then, copy the name or ID of the Xen boot config and set it via grub-set-default:

`root `[`#`]`grub-set-default 'Gentoo GNU/Linux, with Xen hypervisor'`

## [][Creating an unprivileged domain (domU)]

### [Building the kernel]

Go to the Xen-powered Linux kernel source and, if necessary, update the configuration. It is wise to keep as many topics as possible similar to the main kernel. Then build the kernel and place the resulting [vmlinuz] file where you want (we assume this is [/mnt/data/xen/kernel] ):

`root `[`#`]`make O=~/build/domU `

`root `[`#`]`cp ~/build/domU/vmlinuz /mnt/data/xen/kernel/kernel-3.5.x.y-xen `

** Note**\
On modern systems (e.g. xen-4.3.2, kernel-3.12) it is possible to use only one kernel for both: dom0 and domU. Just configure all options needed for a guest system in the main kernel. Don\'t forget to copy the modules [/lib/modules/\<your kernel\>] to the guest system.

If you\'d like to trim down the domU kernel the following flags are necessary.

Enable general Xen support:

[KERNEL] **Xen base support**

    Processor type and features  --->
         [*] Linux guest support  --->
              [*]   Enable paravirtualization code
              [*]     Xen guest support
              [*]       Support for running as a PVH guest
              [*]     Paravirtualization layer for spinlocks

Facilitates guest access to block and network devices via dom0:

[KERNEL] **Disk and network**

    Device Drivers  --->
         [*] Block devices  --->
              <*>   Xen virtual block device support
         [*] Network device support  --->
              <*>   Xen network device frontend driver

In some configurations it can be desirable to provide a guest with direct access to a PCI device. This is known as [Xen PCI Passthrough](https://wiki.xenproject.org/wiki/Xen_PCI_Passthrough):

[KERNEL] **Guest PCI passthrough**

    Bus options (PCI etc.)  --->
         [*] Xen PCI Frontend

Keyboard, mouse, and display support via dom0 backend:

[KERNEL] **Guest human interface**

    Device Drivers  --->
         Input device support  --->
              [*]   Miscellaneous devices  --->
                   <*>   Xen virtual keyboard and mouse support
         Graphics support  --->
              Frame buffer Devices  --->
                   <*> Xen virtual frame buffer support

The remaining drivers flesh out memory management, domain-to-domain communication, and communication to Xen via sysfs interfaces:

[KERNEL] **Xen drivers**

    Device Drivers  --->
         Xen driver support  --->
              [*] Xen memory balloon driver
              [*]   Scrub pages before returning them to system
              <*> Xen /dev/xen/evtchn device
              <*> Xen filesystem
              [*]   Create compatibility mount point /proc/xen
              [*] Create xen entries under /sys/hypervisor
              <*> userspace grant access device driver
              <*> User-space grant reference allocator driver
              <*> Xen ACPI processor
              [*] Xen platform mcelog

### [Creating the domain disks]

For best performance, it is best to dedicate a partition (or logical volume) to a domain rather than a file based filesystem. However, if you are going to use Xen primarily for tests using a file based filesystem does have its advantages (especially regarding maintenance).

You can create a file based filesystem using [dd] and [mke2fs] (or any other file system creation tool). For instance, to create a 4 Gbyte ext4 filesystem:

`root `[`#`]`dd if=/dev/zero of=/mnt/data/xen/disks/ext4root.img bs=1M count=4096 `

`root `[`#`]`mkfs.ext4 /mnt/data/xen/disks/ext4root.img `

### [Configuring a domain]

Next we create a Xen configuration file for a domain. You can store these configuration files where you want, for instance at [/mnt/data/xen/configs]. As an example, we create a configuration file for a small Gentoo environment which uses the disk image we created previously:

[FILE] **`/mnt/data/xen/configs/gentoo`**

    kernel = "/mnt/data/xen/kernel/kernel-4.12.5-xen"
    memory = 2048
    vcpus  = 2
    name   = "gentoo"
    disk   = ['file:/mnt/data/xen/disks/ext4root.img,xvda1,w'] # Map the disk image to the virtual /dev/xvda1
    root   = "/dev/xvda1 ro"
    vif    = ['bridge=br0'] # set the bridge name to br0 (see later), otherwise xen will use xenbr0

Syntax of the configuration file is based on Python, but in recent releases of Xen, it is not a Python script. Unknown items are ignored -- you can use that to define custom options for your own tooling.

If you are using a block device (such as an lvm volume or partition) for the disk use \'phy:\' instead of \'file:\' and optionally leave off /dev. For example:

[CODE] **Using a block device**

    (LVM Volume)
    disk = [ 'phy:lvm/xen-guest-root,xvda1,w' ]

    (Physical Partition)
    disk = [ 'phy:sdb6,xvda1,w' ]

    (Any block device)
    disk = [ 'phy:/dev/loop4p2,xvda1,w' ]

You can find example configuration files in [/etc/xen], which is also the default location for domU config files.

### [Launching the new domain]

Now we\'re all set and we can launch the new domain. If the disk image contained an operating system, we could just create and attach the domain using the [xl] command:

`root `[`#`]`xl create /mnt/data/xen/gentoo -c`

The domain would be booted inside the terminal in which you executed the command. However, in our case, the disk image is empty so the domain won\'t boot up in anything useful. To fix this, you can loop-mount the image and install Gentoo as you\'re used to.

If you want to disconnect from the domain, press [Ctrl]+[\]]. You can always reconnect to the domains\' console using [xl console gentoo]. However, there is only one console per domain, so only use it when you can\'t access the domain otherwise (for instance, through SSH).

If you are missing login prompt on the console, make sure you have entries like this in your inittab files on dom0 and domU pointing to [/dev/hvc0]:

[FILE] **`dom0:/etc/inittab`**

    c0:2345:respawn:/sbin/agetty 115200 hvc0 linux

[FILE] **`domU:/etc/inittab`**

    c0:2345:respawn:/sbin/agetty 115200 hvc0 linux

You might also want to log the `root` user of the domU automatically:

[FILE] **`domU:/etc/inittab`**

    c0:2345:respawn:/sbin/agetty -a root 115200 hvc0 linux

To apply the changes in [/etc/inittab] without a reboot issue the following command:

`root `[`#`]`telinit q`

If it still does not work, check the kernel config for `DEVTMPFS` and `DEVTMPFS_MOUNT`. These two values should be enabled in either module or built in format.

[KERNEL] **Setting `DEVTMPFS` and `DEVTMPFS_MOUNT`**

    Device Drivers --->
       Generic Driver Options  --->
          -*- Maintain a devtmpfs filesystem to mount at /dev
          [*]   Automount devtmpfs at /dev, after the kernel mounted the rootfs

## [Networking on domains]

### [Introduction]

Xen works best when using a bridged mode network configuration. This means that your default network interface on the administrative domain becomes a bridge which accepts connections to the virtual domains as well as to the IP address your administrative domain has.

### [Bridged interfaces]

Create a bridge interface by creating a new link to the networking init script as provided by Gentoo:

`root `[`#`]`cd /etc/init.d `

`root `[`#`]`ln -s net.lo net.br0 `

`root `[`#`]`ln -s net.lo net.eth0 `

Next, edit [/etc/conf.d/net] and setup the bridge:

[FILE] **`dom0:/etc/conf.d/net`**

    # eth0 should NOT have an ip configured
    config_eth0="null"

    # configure bridge to replace eth0 on dom0. Make sure the netmask for the bridge includes ip addresses of all your domUs!
    bridge_br0="eth0"
    config_br0="192.168.XX.XX netmask 255.255.0.0 brd 192.168.255.255"
    routes_br0="default via 192.168.XX.XX"
    mac_br0="00:16:3e:5b:XX:XX"

    # bridge options to make interface come up immediately
    bridge_stp_state_br0="0"
    bridge_forward_delay_br0="0"
    bridge_hello_time_br0="1000"

    rc_net_br0_need="net.eth0"
    rc_net_br0_provide="!net"

Alternatively the bridge may request IP information from DHCP.

[FILE] **`dom0:/etc/conf.d/net`**

    # eth0 should NOT have an ip configured
    config_eth0="null"

    config_br0="dhcp"

    # bridge options to make interface come up immediately
    bridge_stp_state_br0="0"
    bridge_forward_delay_br0="0"
    bridge_hello_time_br0="1000"

    rc_net_br0_need="net.eth0"
    rc_net_br0_provide="!net"

[FILE] **`domU:/etc/conf.d/net`**

    config_eth0="192.168.1.200 netmask 255.255.255.0 brd 192.168.1.255"
    # route all traffic through dom0 bridge address
    routes_eth0="default via 192.168.XX.XX"
    # make sure all your domUs have different mac addresses! Set them if needed in xen domU
    # config files in /etc/xen/<domU_name> with "vif = [ "ip=192.68.XX.XX,mac=XX:XX:XX:XX:XX:XX,bridge=br0" ];" !

Finally, install the [[[net-misc/bridge-utils]](https://packages.gentoo.org/packages/net-misc/bridge-utils)[]] package, and make sure the [net.br0] init script is loaded at boot.

`root `[`#`]`emerge --ask net-misc/bridge-utils`

`root `[`#`]`rc-update add net.br0 default`

To start the interface immediately

`root `[`#`]`/etc/init.d/net.br0 start`

If you use bridged networks with real internet IP\'s in hosted environments, it may be necessary to add one or all of the following lines (depending on your environment) in your [/etc/sysctl.conf] file to prevent redirects, that can cause intermittent network interruptions:

[FILE] **`/etc/sysctl.conf`**

    net.ipv4.conf.all.send_redirects=0
    net.ipv4.conf.eth0.send_redirects=0
    net.ipv4.conf.br0.send_redirects=0
    net.ipv4.conf.default.send_redirects=0

To get the changes in [/etc/sysctl.conf] to work, use:

`root `[`#`]`sysctl -p /etc/sysctl.conf`

If encountering poor network performance or if your domU network permanently stops working under heavy load (backup jobs, etc) (from outside it looks like the instance would crash, but deactivating and activating the interface e.g. from the `xl console <domU name>` with `/etc/init.d/net.eth0 stop/start`, restores normal operation), use [ethtool] to improve/prevent it on all interfaces connected to the bridge (don\'t forget the bridge itself):

`root `[`#`]`ethtool --offload <network device> gso off tso off sg off gro off`

** Note**\
You have to do it after each reboot, so use e.g. [/etc/crontab] to make it permanent.

## [Troubleshooting]

### [][Unable to passthrough USB mouse and keyboard to HVM (Windows 7) domU in Xen 4.7.3]

If using the latest stable version of Xen (i.e. app-emulation/xen-4.7.3), you find yourself unable to passthrough an emulated USB device (in other words, you cannot use a mouse and keyboard in a HVM windows guest domU OS), note that QEMU-emulated USB controllers are **not** present in Xen 4.7.3. Observe that the emulated USB controller (a.k.a. usbctrl=\[\"type=devicemodel\"\]) is absent from the Xen 4.7 official documentation.

In order to use a USB keyboard and mouse in a Win7 domU:

-   If your setup is capable of supporting it, consider passing through the entire USB host controller using [PCI Passthrough](https://wiki.xenproject.org/wiki/Xen_PCI_Passthrough). Note that this will likely require some IOMMU/VT-d and will depend on how your motherboard and chipset were designed; or

<!-- -->

-   Unmask Xen 4.8.2 in portage and upgrade to it, following which USB mouse and keyboard passthrough may be achieved with the following changes to domU\'s config file:

Assuming that the Xen configs are located, as above, at [/mnt/data/xen/configs], and that the HVM Windows 7 config file is called \"win7\":

[FILE] **`/mnt/data/xen/configs/win7`**

    #This creates a USB1.1 emulated controller for a dom0 on Xen 4.8.2 (NOT 4.7.3)
    usb = 1
    usbdevice = ['host:XXXX:XXXX','host:XXXX:XXXX'] #Replace with the IDs of your mouse and keyboard, respectively.

You can find the IDs of your mouse and keyboard by issuing the command:

`user `[`$`]`lsusb`

### [][Xen domU hanging with kernel 4.3+]

tl;dr:

[FILE] **`/etc/default/grub`increase gnttab_max_frames**

    GRUB_CMDLINE_XEN="... gnttab_max_frames=256"

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

`root `[`#`]`reboot`

Kernel 4.3 added blk-mq support for xen-blkfront. In some cases (heavy IO/networking/high number of CPU), you may observe domU hangs. Kernel 4.12 added some mitigation, but it still happens from time to time (depends on your workload). In kernels 4.13+ you at least see the following message in the dmesg:

`root `[`#`]`dmesg `

    Jan 10 12:15:19 domU kernel: xen:grant_table: xen/grant-table: max_grant_frames reached cur=32 extra=1 limit=32 gnttab_free_count=0 req_entries=24

As both xen-netfront and xen-blkfront support multi-queue, they would consume a lot of grant table references when there are many paravirtual devices and vcpus assigned to guest. Guest domU might panic or hang due to grant allocation failure when nr_grant_frames in guest has reached its max value.

You can use the xen-diag tool from Xen 4.10 to see if you\'re reaching the limit with your domUs.

`root `[`#`]`xl list `

    Name                                        ID   Mem VCPUs      State   Time(s)
    Domain-0                                     0  4096    24     r-----     895.4
    domU                                         1  4992    24     r-----    2065.5

`root `[`#`]`xen-diag gnttab_query_size 1 `

    domid=1: nr_frames=13, max_nr_frames=32

The default limit for Xen 4.9 is 32, Xen 4.10 increased the limit to 64. You can change it via the xen \"gnttab_max_frames\" command line options. A novell support page recommended to set it to 256.

You can add the xen-diag tool to Xen 4.9: [commit1](https://xenbits.xen.org/gitweb/?p=xen.git;a=patch;h=df36d82e3fc91bee2ff1681fd438c815fa324b6a) [commit2](https://xenbits.xen.org/gitweb/?p=xen.git;a=patch;h=04e0457e1e786a3a33d1854275fd6cd7ba6306f7)

More information: [Gentoo bug](https://bugs.gentoo.org/643208) [Debian bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=880554) [Novell workaround](https://www.novell.com/support/kb/doc.php?id=7018590) [Kernel 4.13 grant table optimization](https://www.mail-archive.com/xen-devel@lists.xen.org/msg116412.html)

\

### [][Xen domU hanging with Xen 4.12+]

tl;dr:

[FILE] **`/etc/default/grub`use credit scheduler**

    GRUB_CMDLINE_XEN="... sched=credit"

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

`root `[`#`]`reboot`

Xen 4.12 switched the default scheduler to Credit 2. Reports has shown that Credit 2 on multi-cpu machines may cause domU stalls on busy machines.

More information: [xen 4.12 changelog](https://xenproject.org/2019/04/02/whats-new-in-xen-4-12/) [xen-users report 1](https://lists.xenproject.org/archives/html/xen-users/2020-01/msg00019.html) [xen-users report 2](https://lists.xenproject.org/archives/html/xen-users/2020-02/msg00018.html) [xen-devel report 3](https://lists.xenproject.org/archives/html/xen-devel/2020-01/msg00361.html)

## [See also]

-   [KVM](https://wiki.gentoo.org/wiki/KVM "KVM") --- a generic, open-source hardware emulator and virtualization suite.
-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.

## [External resources]

-   [Xen Wiki](https://wiki.xen.org/)
-   [virt-manager](https://virt-manager.org/) - A graphical tool for administering virtual machines.
-   [Xen Project Beginners Guide](https://wiki.xenproject.org/wiki/Xen_Project_Beginners_Guide) - Nice introduction although written for Debian.
-   [Xen On Funtoo From Scratch](https://wiki.xenproject.org/wiki/Xen_On_Funtoo_From_Scratch) - An installation guide, somewhat closer to Gentoo.

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: ****\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*