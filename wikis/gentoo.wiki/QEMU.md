This page contains [[changes](https://wiki.gentoo.org/index.php?title=QEMU&oldid=1421005&diff=1437392)] which are not marked for translation.

Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/QEMU/fr "QEMU (51% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/QEMU/hu "QEMU (25% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/QEMU/zh-cn "QEMU (22% translated)")

\

**Resources**

[[]][Home](https://www.qemu.org/docs/master/index.html)

[[]][Official documentation](https://www.qemu.org/docs/master/index.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/QEMU "wikipedia:QEMU")

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/qemu)

[[]][GitLab](https://gitlab.com/qemu-project/qemu)

[[]][Official project wiki](https://wiki.qemu.org/Main_Page)

[[]][Bugs (upstream)](https://gitlab.com/groups/qemu-project/-/issues)

[[]][Blog](https://www.qemu.org/blog/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/qemu)

**QEMU** (**Q**uick **EMU**lator) is a generic, open-source hardware emulator and virtualization suite.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [BIOS and UEFI firmware]](#BIOS_and_UEFI_firmware)
    -   [[2.2] [Kernel]](#Kernel)
        -   [[2.2.1] [Physical CPU processor support - Host]](#Physical_CPU_processor_support_-_Host)
        -   [[2.2.2] [Processor Support]](#Processor_Support)
        -   [[2.2.3] [Handling kernel config at CLI]](#Handling_kernel_config_at_CLI)
        -   [[2.2.4] [Networking]](#Networking)
        -   [[2.2.5] [Intel VT-g (integrated graphics adapter virtualization)]](#Intel_VT-g_.28integrated_graphics_adapter_virtualization.29)
    -   [[2.3] [USE flags]](#USE_flags)
        -   [[2.3.1] [USE_EXPAND]](#USE_EXPAND)
    -   [[2.4] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
    -   [[3.2] [Files]](#Files)
        -   [[3.2.1] [Single File]](#Single_File)
        -   [[3.2.2] [Image File]](#Image_File)
    -   [[3.3] [Additional software]](#Additional_software)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)
    -   [[4.2] [Permissions]](#Permissions)
    -   [[4.3] [Creation of a disk image]](#Creation_of_a_disk_image)
    -   [[4.4] [Preparation of a bootable disk image from scratch]](#Preparation_of_a_bootable_disk_image_from_scratch)
    -   [[4.5] [CPU selection]](#CPU_selection)
    -   [[4.6] [Starting QEMU]](#Starting_QEMU)
    -   [[4.7] [Connecting to the virtual machine via VNC]](#Connecting_to_the_virtual_machine_via_VNC)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [qemu-system-x86_64: CPU model \'host\' requires KVM or HVF]](#qemu-system-x86_64:_CPU_model_.27host.27_requires_KVM_or_HVF)
    -   [[5.2] [kvm: already loaded the other module]](#kvm:_already_loaded_the_other_module)
    -   [[5.3] [Creating TUN/TAP device - No such file or directory]](#Creating_TUN.2FTAP_device_-_No_such_file_or_directory)
    -   [[5.4] [Configuration does not support video model \'qxl\']](#Configuration_does_not_support_video_model_.27qxl.27)
    -   [[5.5] [QEMU has kvm support on some guest CPU architectures]](#QEMU_has_kvm_support_on_some_guest_CPU_architectures)
    -   [[5.6] [Invalid context errors on SELinux systems]](#Invalid_context_errors_on_SELinux_systems)
    -   [[5.7] [lto1: internal compiler error: original not compressed with zstd]](#lto1:_internal_compiler_error:_original_not_compressed_with_zstd)
    -   [[5.8] [Windows guests fail to provision, boot or Blue Screen of Death (BSOD) on startup]](#Windows_guests_fail_to_provision.2C_boot_or_Blue_Screen_of_Death_.28BSOD.29_on_startup)
    -   [[5.9] [Guest system breaks sound]](#Guest_system_breaks_sound)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Unmerge]](#Unmerge)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Introduction]

QEMU is a *hardware emulator and virtualization tool*, which runs on a *host OS platforms*. Inside a virtual machine, QEMU can emulate *multiple operating systems*; it can also emulate *embedded systems*.

QEMU supports *32+ kinds of CPUs*. It emulates *nearly all* the opcodes of these CPUs.

QEMU has several plugins: [Accelerator] is one of them. This plugin allows execution directly by the host CPU. When using an [accelerator], QEMU executes CPU instructions the *fastest*.

QEMU is a [Type-2 hypervisor](https://en.wikipedia.org/wiki/Hypervisor#Classification "wikipedia:Hypervisor"), which runs within user namespace and performs virtual hardware emulation.

-   QEMU can be paired with [KVM](https://wiki.gentoo.org/wiki/KVM "KVM") to run VMs at *near-native speed*. This is accomplished by using hardware extensions such as: Intel VT-x or AMD-V.
-   It can then emulate user-level processes, which allow applications, compiled for one architecture, to run on a different one.
-   There are multiple operating modes: user-mode emulation, system emulation, KVM hosting and Xen hosting.
-   QEMU can save and restore the state of virtual machines of all its running programs.
-   QEMU virtual machines can interface with many types of physical host hardware, such as, but not limited to, CD-ROM drives, USB devices, audio interfaces, hard disks and network cards.
-   Virtual disk image defaults to the qcow2 format. This format only uses as much host disk space as the guest OS grows to use. Using the snapshot method, the guest OS can revert back to its desired state in time.
-   It does *not depend* on graphical output methods on the host system, instead, making use of an integrated VNC server to access the screen of the guest OS.
-   QEMU on a host CPU can execute multiple virtual CPUs *in parallel*.

QEMU has support for several accelerator plug-ins:

  ------------- ----------------------------- ------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Virtualizer   Accelerator                   Virtualization type       Description                                                                                                                                                                                                                                                                                                                                                      Gentoo package name
  qemu          tcg                           full/software emulation   QEMU\'s own Tiny Code Generator. This is the default. More frequently denoted as qemu and not qemu/tcg so often.                                                                                                                                                                                                                                                 [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]]
  qemu          hvf                           paravirtualization        Apple\'s Hypervisor framework based on Intel VT.
  qemu          whpx^[\[1\]](#cite_note-1)^   hybrid                    Microsoft\'s Windows Hypervisor Platform based on Intel VT or AMD-V.
  qemu          kvm                           paravirtualization        Linux Type-1 Hypervisor. This is the common choice for hosts using **[amd64]**, **[arm64]**, or **[mips]**^[\[2\]](#cite_note-2)^. Supports Microsoft Windows.   [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]]
  qemu          haxm^[\[3\]](#cite_note-3)^   paravirtualization        Intel VT, by Intel Corporation.
  ------------- ----------------------------- ------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

QEMU, if used in conjunction with an accelerator, becomes a Type-1 hypervisor, which runs in Kernel namespace. This allows a user namespace program access to the hardware virtualization features of various processors. Such an accelerator can be [KVM](https://wiki.gentoo.org/wiki/KVM "KVM") (**K**ernel-based **V**irtual **M**achine) or [Xen](https://wiki.gentoo.org/wiki/Xen "Xen").

If *no accelerator* is used, QEMU will run entirely in user namespace, using its *built-in* binary translator TCG (Tiny Code Generator). Using QEMU without an accelerator is *relatively inefficient and slow*.

** Note**\
This article typically uses KVM as the accelerator of choice, due to its GPL licensing and availability. Without KVM, nearly all commands described here, will still work (unless KVM-specific).

The following sub-articles provide detailed instructions on QEMU configurations and options:

-   [QEMU/Bridge with Wifi Routing](https://wiki.gentoo.org/wiki/QEMU/Bridge_with_Wifi_Routing "QEMU/Bridge with Wifi Routing")
-   [QEMU/KVM IPv6 Support](https://wiki.gentoo.org/wiki/QEMU/KVM_IPv6_Support "QEMU/KVM IPv6 Support") --- describes IPv6 support in QEMU/KVM.
-   [QEMU/Linux guest](https://wiki.gentoo.org/wiki/QEMU/Linux_guest "QEMU/Linux guest") --- describes the setup of a Gentoo Linux guest in [QEMU] using Gentoo bootable media.
-   [Virtiofs](https://wiki.gentoo.org/wiki/Virtiofs "Virtiofs") --- a shared file system that lets virtual machines access a directory tree on the host
-   [QEMU/Options](https://wiki.gentoo.org/wiki/QEMU/Options "QEMU/Options") --- describes some of the options useful for configuring [QEMU] virtual machines.
-   [QEMU/OS2WarpV3 guest](https://wiki.gentoo.org/wiki/QEMU/OS2WarpV3_guest "QEMU/OS2WarpV3 guest")
-   [QEMU/Windows guest](https://wiki.gentoo.org/wiki/QEMU/Windows_guest "QEMU/Windows guest") --- setup of a Windows guest using [QEMU]

## [Installation]

### [BIOS and UEFI firmware]

In order to utilize KVM, either Vt-x (`vmx`) or AMD-V (`svm`) must be supported by the processor. Vt-x or AMD-V are Intel\'s and AMD\'s respective technologies for permitting multiple operating systems to concurrently execute operations on the processors.

To inspect hardware for virtualization support, issue the following command:

`user `[`$`]`grep --color --extended-regexp "vmx|svm" "/proc/cpuinfo"`

** Important**\
For a period, manufacturers were shipping with virtualization **turned off** by default in the system\'s firmware. Toggling this feature in the firmware may require **full removal of power** from the system to take effect.

If KVM support is available, there should be a `kvm` device listed at [/dev/kvm]. This will take effect *after* the system has booted to a KVM-enabled kernel.

### [Kernel]

Described below are the basic requirements for KVM kernel configuration for the host OS. A more complete and up-to-date list can be found at the [KVM Tuning Kernel](http://www.linux-kvm.org/page/Tuning_Kernel) page.

** Note**\
Different guest (virtualized) OS may require additional kernel options. These are covered in the corresponding [Usage](https://wiki.gentoo.org/wiki/QEMU#Usage "QEMU") section.

[KERNEL] **Enable high resolution timer support (`CONFIG_HIGH_RES_TIMERS`)**

    General setup  --->
        Timers subsystem  --->
            <*>   High Resolution Timer Support

** Note**\
This includes support for ARM64 processors.

#### [Physical CPU processor support - Host]

If KVM support is not available, insert `CONFIG_KVM=y` into the [/usr/src/linux/.config] and rebuild/reinstall the kernel (and its initramfs image). Come back here after the host is rebooted.

[KERNEL] **Enable KVM Support (`CONFIG_KVM`)**

    [*] Virtualization  --->
        <*>   Kernel-based Virtual Machine (KVM) support

** Note**\
This includes support for ARM64 processors.

#### [Processor Support]

[KERNEL] **Enable KVM support for Intel processors (`CONFIG_KVM_INTEL`)**

    [*] Virtualization  --->
        <M>   KVM for Intel processors support

[KERNEL] **Enable KVM support for AMD processors (`CONFIG_KVM_AMD`)**

    [*] Virtualization  --->
        <M>   KVM for AMD processors support

** Warning**\
If *both* **KVM support for Intel processors** *and* **KVM support for AMD processors** are set to be built into the kernel (`*`), an error message will be returned by [kprint] at early boot. Since the system can only have one processor type: Intel *or* AMD. Enabling *one* or *both* options as *modules* (`M`) will solve this issue.

#### [Handling kernel config at CLI]

To set the various kernel configuration settings from the command lines, the [linux/scripts/kconfig/merge_config.sh] shall be used here:

**Mandatory kernel configuration options to set**:

[FILE] **`/usr/src/kernel-kconfig-qemu-host.config`**

    CONFIG_VIRTUALIZATION=y
    CONFIG_KVM=y
    CONFIG_KVM_INTEL=y
    CONFIG_KVM_AMD=y

`root `[`#`]`cd "/usr/src/linux" `

`root `[`#`]`"./scripts/kconfig/merge_config.sh" ".config" "/usr/src/kernel-kconfig-qemu-host.config" `

*Useful* kernel configuration options to use:

[FILE] **`/usr/src/kernel-kconfig-qemu-host-optional.config`**

    CONFIG_VHOST_NET=y
    CONFIG_HIGH_RES_TIMERS=y
    CONFIG_HPET=y
    CONFIG_COMPACTION=y
    CONFIG_MIGRATION=y
    CONFIG_KSM=y
    CONFIG_SYSFS=y
    CONFIG_PROC_FS=y
    CONFIG_TRANSPARENT_HUGEPAGE=y
    CONFIG_CGROUPS=y
    CONFIG_KVM_HYPERV=y

`root `[`#`]`"./scripts/kconfig/merge_config.sh" ".config" "/usr/src/kernel-kconfig-qemu-host-optional.config" `

** Important**\
Recent Windows guests (at least Windows 10 22H2 and up) are **required** to set `CONFIG_KVM_HYPERV` (as per the optional configuration above). If this is **not** selected, VMs will fail to provision (or boot) with errors like: `Failed to set MSR` and `` Assertion `ret == cpu->kvm_msr_buf->nmsrs' failed ``.

#### [Networking]

Accelerated networking, **required** for `vhost-net` USE flag (recommend):

[KERNEL] **vhost-net kernel 5.7 and later (`CONFIG_VHOST_NET`)**

    Device Drivers  --->
        [*] VHOST drivers  --->
            <*> Host kernel accelerator for virtio net

[KERNEL] **Optional advanced networking support (`CONFIG_NET_CORE`, `CONFIG_TUN`)**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Network core driver support
                <*> Universal TUN/TAP device driver support

Needed for 802.1d Ethernet bridging:

[KERNEL] **Enabling 802.1d Ethernet Bridging support (`CONFIG_IPV6`, `CONFIG_BRIDGE`)**

    [*] Networking support  --->
            Networking options  --->
                <*> The IPv6 protocol
                <*> 802.1d Ethernet Bridging

#### [][Intel VT-g (integrated graphics adapter virtualization)]

Mediated device passthrough for Intel GPUs (Broadwell to Comet Lake)^[\[4\]](#cite_note-4)^

[KERNEL] **Intel VT-g (`CONFIG_VFIO_MDEV`, `CONFIG_DRM_I915_GVT`, `CONFIG_DRM_I915_GVT_KVMGT`)**

    Device Drivers  --->
            <*> VFIO Non-Privileged userspace driver framework
                <*> Mediated device driver framework
            Graphics Support  --->
                <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
                    [*] Enable Intel GVT-g graphics virtualization host support
                <*> Enable KVM host support Intel GVT-g graphics virtualization

### [USE flags]

Some packages are aware of the [[[qemu]](https://packages.gentoo.org/useflags/qemu)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

Review the possible USE flags for QEMU:

### [USE flags for] [app-emulation/qemu](https://packages.gentoo.org/packages/app-emulation/qemu) [[]] [QEMU + Kernel-based Virtual Machine userland tools]

  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+aio`](https://packages.gentoo.org/useflags/+aio)                                 Enables support for Linux\'s Async IO
  [`+curl`](https://packages.gentoo.org/useflags/+curl)                               Support ISOs / -cdrom directives via HTTP or HTTPS.
  [`+doc`](https://packages.gentoo.org/useflags/+doc)                                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`+fdt`](https://packages.gentoo.org/useflags/+fdt)                                 Enables firmware device tree support
  [`+filecaps`](https://packages.gentoo.org/useflags/+filecaps)                       Use Linux file capabilities to control privilege rather than set\*id (this is orthogonal to USE=caps which uses capabilities at runtime e.g. libcap)
  [`+gnutls`](https://packages.gentoo.org/useflags/+gnutls)                           Enable TLS support for the VNC console server. For 1.4 and newer this also enables WebSocket support. For 2.0 through 2.3 also enables disk quorum support.
  [`+jpeg`](https://packages.gentoo.org/useflags/+jpeg)                               Enable jpeg image support for the VNC console server
  [`+oss`](https://packages.gentoo.org/useflags/+oss)                                 Add support for OSS (Open Sound System)
  [`+pin-upstream-blobs`](https://packages.gentoo.org/useflags/+pin-upstream-blobs)   Pin the versions of BIOS firmware to the version included in the upstream release. This is needed to sanely support migration/suspend/resume/snapshotting/etc\... of instances. When the blobs are different, random corruption/bugs/crashes/etc\... may be observed.
  [`+png`](https://packages.gentoo.org/useflags/+png)                                 Enable png image support for the VNC console server
  [`+seccomp`](https://packages.gentoo.org/useflags/+seccomp)                         Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`+slirp`](https://packages.gentoo.org/useflags/+slirp)                             Enable TCP/IP in hypervisor via net-libs/libslirp
  [`+vhost-net`](https://packages.gentoo.org/useflags/+vhost-net)                     Enable accelerated networking using vhost-net, see https://www.linux-kvm.org/page/VhostNet
  [`+vnc`](https://packages.gentoo.org/useflags/+vnc)                                 Enable VNC (remote desktop viewer) support
  [`X`](https://packages.gentoo.org/useflags/X)                                       Add support for X11
  [`accessibility`](https://packages.gentoo.org/useflags/accessibility)               Adds support for braille displays using brltty
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                                 Enable alsa output for sound emulation
  [`bpf`](https://packages.gentoo.org/useflags/bpf)                                   Enable eBPF support for RSS implementation.
  [`bzip2`](https://packages.gentoo.org/useflags/bzip2)                               Enable bzip2 compression support
  [`capstone`](https://packages.gentoo.org/useflags/capstone)                         Enable disassembly support with dev-libs/capstone
  [`debug`](https://packages.gentoo.org/useflags/debug)                               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`fuse`](https://packages.gentoo.org/useflags/fuse)                                 Enables FUSE block device export
  [`glusterfs`](https://packages.gentoo.org/useflags/glusterfs)                       Enables GlusterFS cluster fileystem via sys-cluster/glusterfs
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                                   Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`infiniband`](https://packages.gentoo.org/useflags/infiniband)                     Enable Infiniband RDMA transport support
  [`io-uring`](https://packages.gentoo.org/useflags/io-uring)                         Enable the use of io_uring for efficient asynchronous IO and system requests
  [`iscsi`](https://packages.gentoo.org/useflags/iscsi)                               Enable direct iSCSI support via net-libs/libiscsi instead of indirectly via the Linux block layer that sys-block/open-iscsi does.
  [`jack`](https://packages.gentoo.org/useflags/jack)                                 Add support for the JACK Audio Connection Kit
  [`jemalloc`](https://packages.gentoo.org/useflags/jemalloc)                         Use dev-libs/jemalloc for memory management
  [`keyutils`](https://packages.gentoo.org/useflags/keyutils)                         Support Linux keyrings via sys-apps/keyutils
  [`lzo`](https://packages.gentoo.org/useflags/lzo)                                   Enable support for lzo compression
  [`multipath`](https://packages.gentoo.org/useflags/multipath)                       Enable multipath persistent reservation passthrough via sys-fs/multipath-tools.
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)                           Enable the ncurses-based console
  [`nfs`](https://packages.gentoo.org/useflags/nfs)                                   Enable NFS support
  [`nls`](https://packages.gentoo.org/useflags/nls)                                   Add Native Language Support (using gettext - GNU locale utilities)
  [`numa`](https://packages.gentoo.org/useflags/numa)                                 Enable NUMA support
  [`opengl`](https://packages.gentoo.org/useflags/opengl)                             Add support for OpenGL (3D graphics)
  [`pam`](https://packages.gentoo.org/useflags/pam)                                   Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`passt`](https://packages.gentoo.org/useflags/passt)                               Enable TCP/IP in hypervisor via net-misc/passt
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)                         Enable pipewire output for sound emulation
  [`plugins`](https://packages.gentoo.org/useflags/plugins)                           Enable qemu plugin API via shared library loading.
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)                     Enable pulseaudio output for sound emulation
  [`python`](https://packages.gentoo.org/useflags/python)                             Add optional support/bindings for the Python language
  [`rbd`](https://packages.gentoo.org/useflags/rbd)                                   Enable rados block device backend support, see https://docs.ceph.com/en/mimic/rbd/qemu-rbd/
  [`sasl`](https://packages.gentoo.org/useflags/sasl)                                 Add support for the Simple Authentication and Security Layer
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                                   Enable the SDL-based console
  [`sdl-image`](https://packages.gentoo.org/useflags/sdl-image)                       SDL Image support for icons
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`smartcard`](https://packages.gentoo.org/useflags/smartcard)                       Enable smartcard support
  [`snappy`](https://packages.gentoo.org/useflags/snappy)                             Enable support for Snappy compression (as implemented in app-arch/snappy)
  [`spice`](https://packages.gentoo.org/useflags/spice)                               Enable Spice protocol support via app-emulation/spice
  [`ssh`](https://packages.gentoo.org/useflags/ssh)                                   Enable SSH based block device support via net-libs/libssh2
  [`static-user`](https://packages.gentoo.org/useflags/static-user)                   Build the User targets as static binaries
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)                       Enable SystemTap/DTrace tracing
  [`test`](https://packages.gentoo.org/useflags/test)                                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`udev`](https://packages.gentoo.org/useflags/udev)                                 Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`usb`](https://packages.gentoo.org/useflags/usb)                                   Enable USB passthrough via dev-libs/libusb
  [`usbredir`](https://packages.gentoo.org/useflags/usbredir)                         Use sys-apps/usbredir to redirect USB devices to another machine over TCP
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)                         Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`vde`](https://packages.gentoo.org/useflags/vde)                                   Enable VDE-based networking
  [`virgl`](https://packages.gentoo.org/useflags/virgl)                               Enable experimental Virgil 3d (virtual software GPU)
  [`virtfs`](https://packages.gentoo.org/useflags/virtfs)                             Enable VirtFS via virtio-9p-pci / fsdev. See https://wiki.qemu.org/Documentation/9psetup
  [`vte`](https://packages.gentoo.org/useflags/vte)                                   Enable terminal support (x11-libs/vte) in the GTK+ interface
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                           Enable dev-libs/wayland backend
  [`xattr`](https://packages.gentoo.org/useflags/xattr)                               Add support for getting and setting POSIX extended attributes, through sys-apps/attr. Requisite for the virtfs backend.
  [`xdp`](https://packages.gentoo.org/useflags/xdp)                                   Enable support for XDP through net-libs/xdp-tools
  [`xen`](https://packages.gentoo.org/useflags/xen)                                   Enables support for Xen backends
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                                 Enable support for ZSTD compression
  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-17 11:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
More than one USE flag ([[[gtk]](https://packages.gentoo.org/useflags/gtk)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], [[[ncurses]](https://packages.gentoo.org/useflags/ncurses)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], [[[sdl]](https://packages.gentoo.org/useflags/sdl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], or [[[spice]](https://packages.gentoo.org/useflags/spice)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]) can be enabled for graphical output. If graphics are desired, it is generally recommended to enable more than one graphical USE flag.

** Note**\
If [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager") is going to be used, be sure to enable the [[[usbredir]](https://packages.gentoo.org/useflags/usbredir)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[spice]](https://packages.gentoo.org/useflags/spice)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags on the qemu package for correct operation.

#### [USE_EXPAND]

Additional ebuild configuration are provided as the *USE_EXPAND* variables `QEMU_USER_TARGETS` and `QEMU_SOFTMMU_TARGETS`. See [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]] for a list of all the available targets (there are many; most are very obscure and may be ignored; leaving these variables at their default values *will disable almost everything*, which is probably just fine for most users).

For each target specified, a `qemu` executable will be built. A `softmmu` target is the standard qemu use-case of emulating an entire system (like [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox") or VMWare, but with optional support for emulating CPU hardware along with peripherals). `user` targets execute user-mode code only; the (somewhat ambitious) purpose of these targets, is to \"magically\" allow importing user namespace Linux ELF binaries from a different architecture into the native system (like multilib, without the need for a software stack or CPU capable of running it).

In order to enable `QEMU_USER_TARGETS` and `QEMU_SOFTMMU_TARGETS`, use [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")]:

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu QEMU_SOFTMMU_TARGETS: arm x86_64 sparc QEMU_USER_TARGETS: x86_64

### [Emerge]

After reviewing and adding any desired USE flags, emerge [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]]:

`root `[`#`]`emerge --ask app-emulation/qemu`

## [Configuration]

The following sub-articles provide detailed instructions on QEMU configurations and options:

-   [QEMU/Options](https://wiki.gentoo.org/wiki/QEMU/Options "QEMU/Options") --- describes some of the options useful for configuring [QEMU] virtual machines.
-   [QEMU/Linux guest](https://wiki.gentoo.org/wiki/QEMU/Linux_guest "QEMU/Linux guest") --- describes the setup of a Gentoo Linux guest in [QEMU] using Gentoo bootable media.
-   [QEMU/Windows guest](https://wiki.gentoo.org/wiki/QEMU/Windows_guest "QEMU/Windows guest") --- setup of a Windows guest using [QEMU]
-   [QEMU/OS2WarpV3 guest](https://wiki.gentoo.org/wiki/QEMU/OS2WarpV3_guest "QEMU/OS2WarpV3 guest")

### [Environment variables]

  ------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  name                            description
  `G_MESSAGES_DEBUG`   Enables debug messages for components using GLib\'s logging system. If set to `all`, it outputs to [stderr]. Other options are `all`, `QEMU`, `libvirt`, `gtk`, and `pulse`. Use comma to separate multiple option.
  `LISTEN_FDS`         Number of file descriptors passed. Used with QEMU activated by [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").
  `LISTEN_PID`         PID of the receiving process (usually set to the current PID). Used with QEMU activated by [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").
  `QEMU_AUDIO_DRV`     Specifies the audio backend driver to use (options are `alsa`, `pa`, `oss`, `none`).
  `XDG_RUNTIME_DIR`    Specifies where user-specific runtime files and sockets should be stored (e.g., /run/user/UID/). Commonly used by [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"), [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"), or [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager").
  ------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Files]

Files that QEMU uses.

#### [Single File]

-   [/etc/libvirt/qemu.conf] - QEMU configuration file.
-   [/etc/libvirt/qemu-lockd.conf] - QEMU lock files
-   [/etc/libvirt/qemu-sanlock.conf] - QEMU SAN lock
-   [/etc/libvirt/qemu/\<domain-name\>.xml] - Domain XML setting for a virtual machine or container.
-   [/etc/libvirt/qemu/autostart/\<domain-name\>.xml] - Autostart this domain (virtual machine or container).
-   [/etc/libvirt/qemu/networks/\<network-name\>.xml] - Network XML setting file for a network connection
-   [/etc/libvirt/qemu/networks/autostart/\<network-name\>.xml] - Autostart this network connection.
-   [/var/lib/libvirt/qemu/channel/target/\<domain-name\>/\<socket-file\>] - UNIX socket file for Libvertd daemon API
-   [/var/cache/libvirt/qemu/capabilities/\<hash-value\>.xml] - Host OS capabilities in XML format
-   [/var/lib/libvirt/qemu/checkpoint/]
-   [/var/lib/libvirt/qemu/\<domain-9-XXXX\>/] - holds UNIX sockets and AES keys for this domain.
-   [/var/lib/libvirt/qemu/dump/]
-   [/var/lib/libvirt/qemu/nvram/]
-   [/var/lib/libvirt/qemu/ram/]
-   [/var/lib/libvirt/qemu/save/] - holding directory of hibernation images
-   [/var/lib/libvirt/qemu/snapshot/] - holding directory of snapshots
-   [/var/run/libvirt/qemu] - various UNIX socket and PID files for the [libvirtd] daemon.

#### [Image File]

QEMU supports the following disk image formats:

-   QEMU copy-on-write ([.qcow2], [.qed], [.qcow], [.cow])
-   VirtualBox Virtual Disk Image ([.vdi])
-   CD/DVD (ISO-9660) images ([.iso])
-   Raw images ([.img]), that guest OS can control
-   VFAT-16
-   VMware Virtual Machine Disk ([.vmdk])
-   Virtual PC Virtual Hard Disk ([.vhd])
-   Parallels disk image ([.hdd], [.hds]) -- **Read-only**
-   Apple macos Universal Disk Image Format ([.dmg]) -- **Read-only**
-   Bochs -- **Read-only**
-   Linux cloop -- **Read-only**

### [Additional software]

To connect to the SPICE server of QEMU, a GUI client like [[[net-misc/spice-gtk]](https://packages.gentoo.org/packages/net-misc/spice-gtk)[]] is required.

## [Usage]

QEMU can be used with GUI front-ends or via the command line. There are multiple user-friendly front ends to QEMU: See [Front-ends](https://wiki.gentoo.org/wiki/QEMU/Front-ends "QEMU/Front-ends").

### [Invocation]

QEMU supports around 34 different CPU architectures. To find the desired architecture, one can list them like so:

`user `[`$`]`ls "/usr/bin/qemu-system-"*`

    /usr/bin/qemu-system-aarch64       /usr/bin/qemu-system-mips      /usr/bin/qemu-system-rx
    /usr/bin/qemu-system-alpha         /usr/bin/qemu-system-mips64    /usr/bin/qemu-system-s390x
    /usr/bin/qemu-system-arm           /usr/bin/qemu-system-mips64el  /usr/bin/qemu-system-sh4
    /usr/bin/qemu-system-avr           /usr/bin/qemu-system-mipsel    /usr/bin/qemu-system-sh4eb
    /usr/bin/qemu-system-cris          /usr/bin/qemu-system-nios2     /usr/bin/qemu-system-sparc
    /usr/bin/qemu-system-hppa          /usr/bin/qemu-system-or1k      /usr/bin/qemu-system-sparc64
    /usr/bin/qemu-system-i386          /usr/bin/qemu-system-ppc       /usr/bin/qemu-system-tricore
    /usr/bin/qemu-system-loongarch64   /usr/bin/qemu-system-ppc64     /usr/bin/qemu-system-x86_64
    /usr/bin/qemu-system-m68k          /usr/bin/qemu-system-ppc64le   /usr/bin/qemu-system-x86_64-microvm
    /usr/bin/qemu-system-microblaze    /usr/bin/qemu-system-riscv32   /usr/bin/qemu-system-xtensa
    /usr/bin/qemu-system-microblazeel  /usr/bin/qemu-system-riscv64   /usr/bin/qemu-system-xtensaeb

### [Permissions]

In order to run a KVM-accelerated virtual machine without root privileges, one can add normal users to the [kvm] group:

`root `[`#`]`gpasswd -a larry kvm`

### [Creation of a disk image]

To create a raw disk image with 4 GiB size:

`user `[`$`]`qemu-img create -f raw "/home/larry/qemu/my-systems-disk-image.img" 4G`

    Formatting 'my-systems-disk-image.img', fmt=raw size=4294967296

`user `[`$`]`ls -lh`

    total 4
    -rw-r--r-- 1 larry larry 4.0G Apr 12 11:23 my-systems-disk-image.img

To create a raw disk image with copy-on-write disabled:

`user `[`$`]`qemu-img create -f raw "/home/larry/qemu/my-systems-disk-image.img" -o nocow=on 4G`

    Formatting 'my-systems-disk-image.img', fmt=raw size=4294967296 nocow=on

`user `[`$`]`ls -lh`

    total 4
    -rw-r--r-- 1 larry larry 4.0G Apr 12 11:23 my-systems-disk-image.img

The option [nocow] is also a file attribute, which can be determined via the command [lsattr]^[\[5\]](#cite_note-5)^.

The following will create a qcow2 disk image (useful, if the host filesystem does not support sparse files):

`user `[`$`]`qemu-img create -f qcow2 "/home/larry/qemu/my-systems-disk-image.qcow2" 4G`

    Formatting 'my-systems-disk-image.qcow2', fmt=qcow2 cluster_size=65536 extended_l2=off compression_type=zlib size=4294967296 lazy_refcounts=off refcount_bits=16

`user `[`$`]`ls -l`

    total 196K
    -rw-r--r-- 1 larry larry 193K Apr 12 11:30 my-systems-disk-image.qcow2

### [Preparation of a bootable disk image from scratch]

A system can be copied onto a disk image, when not using a CD-ROM installation medium.

By default, [qemu] uses a [bios-firmware] to boot the system.

The disk can be prepared with a msdos disk label and a gap between the end of the 512-byte-MBR (Master Boot Record) and the start of the first partition. The gap is needed for boot loaders like [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), which place boot-code within this gap.

The following example uses the raw disk image, which was created [above](https://wiki.gentoo.org/wiki/QEMU#Creation_of_a_disk_image "QEMU").

A raw disk image can be prepared by attaching it as a loop device:

`root `[`#`]`losetup --find --partscan --show "/home/larry/qemu/my-systems-disk-image.img"`

    /dev/loop0

-   The parameter `--find` finds the first unused loop device.
-   The parameter `--partscan` forces the Linux kernel to scan the partition table on the newly created loop device, where the **default sector size of 512 bytes** is assumed.
-   The parameter `--show` displays the name of the assigned loop device, if the parameter `--find` is used.

Attached loop devices can be listed with the following command:

`root `[`#`]`losetup --list`

    NAME       SIZELIMIT OFFSET AUTOCLEAR RO BACK-FILE                                  DIO LOG-SEC
    /dev/loop0         0      0         0  0 /home/larry/qemu/my-systems-disk-image.img   0     512

Then, the loop device can be formatted like a normal disk.

Print the partition table:

`root `[`#`]`parted "/dev/loop0" "unit mib print"`

    Error: /dev/loop0: unrecognised disk label
    Model: Loopback device (loopback)
    Disk /dev/loop0: 4096MiB
    Sector size (logical/physical): 512B/512B
    Partition Table: unknown
    Disk Flags:

Create a new partition table (msdos disk label):

** Warning**\
Make absolutely sure to select the correct loop device, since this may **overwrite an existing partition table**; resulting in **data loss**, if the **overwritten partition table** cannot be recovered.

`root `[`#`]`parted "/dev/loop0" "mklabel msdos"`

    Information: You may need to update /etc/fstab.

The returned information can be ignored, since an entry in the configuration file [/etc/fstab] is not needed.

[parted] now indicates, that the partition table}} is [msdos]:

`root `[`#`]`parted "/dev/loop0" "unit mib print"`

    Model: Loopback device (loopback)
    Disk /dev/loop0: 4096MiB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos
    Disk Flags:

    Number  Start  End  Size  Type  File system  Flags

Create an [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") partition with an offset of 2 MiB:

`root `[`#`]`parted "/dev/loop0" "mkpart primary ext4 2MiB -1"`

The parameter `-1` represents the last sector of the partition.

The first partition has been successfully created:

`root `[`#`]`parted "/dev/loop0" "unit mib print"`

    Model: Loopback device (loopback)
    Disk /dev/loop0: 4096MiB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos
    Disk Flags:

    Number  Start    End      Size     Type     File system  Flags
     1      2.00MiB  4095MiB  4093MiB  primary

This will also attach a new loop device at [/dev/loop0p1]:

`root `[`#`]`ls -l "/dev/loop0"*`

    brw-rw---- 1 root disk   7, 0 Apr 12 12:33 /dev/loop0
    brw-rw---- 1 root disk 259, 0 Apr 12 12:33 /dev/loop0p1

Set the boot flag:

`root `[`#`]`parted "/dev/loop0" set 1 boot on`

All partition flags can be found in the column \"Flags\":

`root `[`#`]`parted "/dev/loop0" "unit mib print"`

    Model: Loopback device (loopback)
    Disk /dev/loop0: 4096MiB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos
    Disk Flags:

    Number  Start    End      Size     Type     File system  Flags
     1      2.00MiB  4095MiB  4093MiB  primary               boot

Create the ext4 filesystem, which was declared via [parted] earlier:

`root `[`#`]`mkfs.ext4 "/dev/loop0p1"`

    mke2fs 1.47.2 (1-Jan-2025)
    Discarding device blocks: done
    Creating filesystem with 1047808 4k blocks and 262144 inodes
    Filesystem UUID: 0e344af7-6f7b-4d27-8238-89d46a5920d6
    Superblock backups stored on blocks:
            32768, 98304, 163840, 229376, 294912, 819200, 884736

    Allocating group tables: done
    Writing inode tables: done
    Creating journal (16384 blocks): done
    Writing superblocks and filesystem accounting information: done

Mount it at [/mnt]:

`root `[`#`]`mount /dev/loop0p1 /mnt`

`root `[`#`]`df --human-readable --print-type "/mnt/"`

    Filesystem     Type  Size  Used Avail Use% Mounted on
    /dev/loop0p1   ext4  3.9G   24K  3.7G   1% /mnt

Create the directories [/mnt/boot/grub], which will be used by GRUB later:

`root `[`#`]`mkdir --parents --verbose "/mnt/boot/grub"`

    mkdir: created directory '/mnt/boot'
    mkdir: created directory '/mnt/boot/grub'

Install GRUB boot loader on the loop device and advice it to install its files to [/mnt/boot/grub/]:

`root `[`#`]`grub-install --target="i386-pc" --boot-directory="/mnt/boot/" "/dev/loop0"`

`root `[`#`]`tree -F "/mnt/boot/grub/"`

    /mnt/boot/grub/
    ├── fonts/
    │   └── unicode.pf2
    ├── grubenv
    ├── i386-pc/
    │   ├── acpi.mod
    │   ├── adler32.mod
    │   ├── affs.mod
    │   ├── afs.mod
    │   ├── afsplitter.mod
    │   ├── ahci.mod
    │   ├── all_video.mod
    │   ├── aout.mod
    │   ├── archelp.mod
    │   ├── ata.mod
    [...]

Unmount the filesystem and detach the loop device:

`root `[`#`]`umount "/mnt/" `

`root `[`#`]`losetup --detach "/dev/loop0" `

If the loop device is still busy - for example, processes are still accessing [/mnt/] - no error will be returned. This can be verified and solved with the following commands:

`root `[`#`]`losetup --list`

    NAME       SIZELIMIT OFFSET AUTOCLEAR RO BACK-FILE                                  DIO LOG-SEC
    /dev/loop0         0      0         0  0 /home/larry/qemu/my-systems-disk-image.img   0     512

`root `[`#`]`lsof | grep "/mnt"`

    sleep     31813                       root cwd       DIR              259,0      4096              131074 /mnt/boot/grub

`root `[`#`]`kill -SIGTERM 31813`

This is sufficient to boot into a grub2 boot prompt. This is can be used as the basis for a bootable system.

### [CPU selection]

QEMU CPU selections have additional support for accelerators, like [kvm] (**K**ernel **V**irtual **M**achine), [tcg] (**T**iny **C**ode **G**enerator) or [Xen].

The accelerator can usually only *accelerate* the features, which are available on the host CPU. So the selection of the CPU affects the performance.

To get a list of CPUs, one can use the parameters `-cpu help`.

To show available accelerators, one can use the parameters `-accel help`.

### [Starting QEMU]

The following explains, how to start a virtual machine with the same feature set as the host CPU, a raw disk image and 2 GB of RAM.

By default, a VNC server starts **without password protection** and listens on the loop interface. QEMU is advised to listen on a local UNIX socket with the following command:

`user `[`$`]`qemu-system-x86_64 -vnc "unix:/run/user/$(id --user)/qemu-vnc.sock" -enable-kvm -cpu host -drive "file=/home/larry/qemu/my-systems-disk-image.img,format=raw" -m 2G`

** Warning**\
**Set the file permissions of [/run/user/\$(id \--user)/qemu-vnc.sock] appropriately**, in order to protect the VNC server from unauthorized access! If the virtual machine is started with the parameter `-vnc :0`, it will listen on port 5900 **on all interfaces without password protection!** The parameter `:0` represents the first display of the host machine, which may be mistaken as a port number!

** Note**\
A CD-ROM installation or boot medium can be added via the parameter `-cdrom`. For example: `-cdrom filename.iso`

### [Connecting to the virtual machine via VNC]

In order to connect to the VNC server, any VNC viewer can be used, for example the [vncviewer], provided by [[[net-misc/tigervnc]](https://packages.gentoo.org/packages/net-misc/tigervnc)[]], can be used:

`user `[`$`]`vncviewer "/run/user/$(id --user)/qemu-vnc.sock"`

    TigerVNC viewer v1.15.0
    Built on: 2025-05-13 12:30
    Copyright (C) 1999-2025 TigerVNC team and many others (see README.rst)
    See https://www.tigervnc.org for information on TigerVNC.

    Tue May 13 14:44:36 2025
     DecodeManager: Detected 4 CPU core(s)
     DecodeManager: Creating 4 decoder thread(s)
     CConn:       Connected to socket /run/user/1000/qemu-vnc.sock
     CConnection: Server supports RFB protocol version 3.8
     CConnection: Using RFB protocol version 3.8
     CConnection: Choosing security type None(1)
     CConn:       Using pixel format depth 24 (32bpp) little-endian rgb888
     CConn:       SetDesktopSize failed: 3

This will open a separate window, where one gets greeted with a GRUB shell, which was installed via `grub-install` [earlier](https://wiki.gentoo.org/wiki/QEMU#Preparation_of_a_bootable_disk_image_from_scratch "QEMU"):

[![Qemu minimal vm with grub2.png](/images/thumb/7/77/Qemu_minimal_vm_with_grub2.png/500px-Qemu_minimal_vm_with_grub2.png)](https://wiki.gentoo.org/wiki/File:Qemu_minimal_vm_with_grub2.png)

## [Troubleshooting]

### [][qemu-system-x86_64: CPU model \'host\' requires KVM or HVF]

When trying to start a virtual machine, using the parameter `-cpu host`, one may encounter the following error:

[CODE] **CPU model \'host\' requires KVM or HVF**

    qemu-system-x86_64: CPU model 'host' requires KVM or HVF

In order to fix this, use the parameter `-enable-kvm`, which will enable [KVM full virtualization support]:

`user `[`$`]`qemu-system-x86_64 -cpu host -enable-kvm [...]`

### [kvm: already loaded the other module]

Sometimes, during the early boot splash, the following error message may be seen:

[CODE] **kvm: already loaded the other module**

    kvm: already loaded the other module.

This indicates, that both, the Intel and the AMD kernel virtual machine settings, have been enabled in the kernel. To fix this, enable it as a *module* or disable either the Intel *or* AMD KVM option specific to the system\'s processor in the kernel configuration as described [above](https://wiki.gentoo.org/wiki/QEMU#Configuration "QEMU").

### [][Creating TUN/TAP device - No such file or directory]

Sometimes, this error can occur, if TUN/TAP support cannot be found in the kernel. To solve this, try loading the [tun] kernel module:

`root `[`#`]`modprobe tun`

If this works, add `tun` to a file in [/etc/modules-load.d/], so the kernel module will be loaded on every boot of the host system:

[FILE] **`/etc/modules-load.d/qemu-modules.conf`**

    tun

### [][Configuration does not support video model \'qxl\']

This is usually the case, if QEMU is built without the `spice` USE flag. To resolve this issue, try to build QEMU [with the correct USE flag](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:AMD64/Working/USE").

First add `spice` to via a [package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use") file:

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu spice

Then recompile the QEMU:

`root `[`#`]`emerge --ask --changed-use app-emulation/qemu`

### [QEMU has kvm support on some guest CPU architectures]

KVM only works for the same CPU architecture. An ARM64 host **cannot** handle x86_64 instructions.

### [Invalid context errors on SELinux systems]

By default, [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") generates a random SELinux MCS label for the QEMU process, when it is started. If the loaded [SELinux](https://wiki.gentoo.org/wiki/SELinux "SELinux") policy does not support MCS categories, the resulting security context will be invalid:

[CODE] **SELinux error from virt-manager**

    Error starting domain: unable to set socket security context 'system_u:system_r:svirt_t:s0:c123,c456': Invalid argument

[CODE] **SELinux error from the kernel**

    kernel: SELinux:  Context system_u:object_r:svirt_image_t:s0:c123,c456 is not valid (left unmapped).

The solution is, either to *switch* to one of the policy types, which supports MCS categories or *manually set* the virtual machine\'s security labels, without MCS categories:

[CODE] **Libvirt domain XML with manually specified seclabel fields**

    <domain type="kvm">
      <name>fedora</name>
      ...
      <devices>
        <disk type="file" device="disk">
          <driver name="qemu" type="qcow2"/>
          <source file="/var/lib/libvirt/images/fedora.qcow2">
            <seclabel model='selinux' relabel='yes'>
              <label>system_u:object_r:svirt_image_t</label>
            </seclabel>
          </source>
          <target dev="vda" bus="virtio"/>
          <address type="pci" domain="0x0000" bus="0x04" slot="0x00" function="0x0"/>
        </disk>
      ...
      <seclabel type='static' model='selinux' relabel='yes'>
        <label>system_u:system_r:svirt_t</label>
      </seclabel>
    </domain>

### [lto1: internal compiler error: original not compressed with zstd]

This is caused by a mismatch of [GCC](https://wiki.gentoo.org/wiki/GCC "GCC"), where qemu is compiled against [[[sys-libs/zlib]](https://packages.gentoo.org/packages/sys-libs/zlib)[]] and [[[dev-libs/glib]](https://packages.gentoo.org/packages/dev-libs/glib)[]]. This can be fixed, by *recompiling* both libraries, *before* recompiling [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]] again:

`root `[`#`]`emerge --ask --oneshot sys-libs/zlib dev-libs/glib`

`root `[`#`]`emerge --ask --oneshot app-emulation/qemu`

### [][Windows guests fail to provision, boot or Blue Screen of Death (BSOD) on startup]

For *optimal performance*, it is recommended, that modern Windows guests (at least Windows 10 22H2 and up) run under a kernel with `CONFIG_KVM_HYPERV` enabled. If this Kernel driver is **not** enabled, VMs will fail to provision, to boot or run into a Blue Screen.

Later versions of Windows, if running as virtual machines, sometimes attempt to access hardware registers - specifically MSRs (**M**odel **S**pecific **R**egisters) - that are not actually defined for the emulated processor within the virtual environment. This is often, due to how Windows interacts with hardware, a driver trying to be overly clever or even bugs within the operating system itself. While these MSR accesses might be valid on physical processors, the virtualized environment presented by KVM may not support them.

KVM\'s default behavior is to attempt to emulate these MSR accesses, but when encountering an undefined register, it reports an *invalid instruction error* to the virtual Windows instance. This error is often fatal, resulting in a Blue Screen and *halting* the virtual machine.

** Tip**\
`unhandled rdmsr` or `unhandled wrmsr` messages in the system logs of the host indicate attempts to access undefined [MSRs]. Failures may also be more obvious, like `failed to set MSR` and `` Assertion `ret == cpu->kvm_msr_buf->nmsrs' failed `` from `qemu-system-*`.

An alternative is passing the kernel parameter `kvm.ignore_msrs=1` on the kernel command line or as a parameter to the kvm module:

** Warning**\
This parameter should only be set, if there are still undefined MSRs. If there *are* any, then it is probably a bug, which needs to be reported to the software vendor or [KVM/QEMU maintainers].

[FILE] **`/etc/modprobe.d/kvm.conf`**

    options kvm ignore_msrs=1

The `ignore_msrs` parameter instructs KVM to ignore any attempts by the virtual Windows machine to access these undefined MSRs. Instead of generating an error and causing a Blue Screen, KVM silently bypasses the problematic instruction. This allows Windows to continue running, albeit potentially with some minor performance implications or masked underlying issues.

** Note**\
While the parameter `ignore_msrs` can be a quick fix for a decent amount of Blue Screens related to MSR accesses, it is likely, that this can be addressed properly, by *enabling* the appropriate kernel parameter, as documented above.

### [Guest system breaks sound]

Attempting sound playback may output either choppy sound or none at all. A possible fix is to use these parameters^[\[6\]](#cite_note-6)^:

`user `[`$`]`qemu-system-x86_64 -audiodev pa,id=Sound -device intel-hda -device hda-output,audiodev=Sound [...]`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-emulation/qemu`

** Note**\
There may be image files left behind after the removal of the QEMU package.

## [See also]

-   [qemu-img](https://wiki.gentoo.org/wiki/Qemu-img "Qemu-img") --- a QEMU disk image utility
-   [Comparison of virtual machines](https://wiki.gentoo.org/wiki/Comparison_of_virtual_machines "Comparison of virtual machines") --- compares the features of several platform virtual machines.
-   [Fast Virtio VM](https://wiki.gentoo.org/wiki/Fast_Virtio_VM "Fast Virtio VM") --- explains a way to build a blazing fast Gentoo VM under [KVM] using Virtio and mdev.
-   [GPU passthrough with virt-manager, QEMU, and KVM](https://wiki.gentoo.org/wiki/GPU_passthrough_with_virt-manager,_QEMU,_and_KVM "GPU passthrough with virt-manager, QEMU, and KVM") --- directly present an internal PCI GPU as-is for direct use by a virtual machine
-   [QEMU with Open vSwitch network](https://wiki.gentoo.org/wiki/QEMU_with_Open_vSwitch_network "QEMU with Open vSwitch network")
-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.
-   [QEMU/Front-ends](https://wiki.gentoo.org/wiki/QEMU/Front-ends "QEMU/Front-ends") --- facilitate VM management and use
-   [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") --- a virtualization management toolkit
-   [Libvirt/QEMU_networking](https://wiki.gentoo.org/wiki/Libvirt/QEMU_networking "Libvirt/QEMU networking") --- details the setup of Gentoo networking by [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") for use by guest containers and [QEMU]-based virtual machines.
-   [Libvirt/QEMU_guest](https://wiki.gentoo.org/wiki/Libvirt/QEMU_guest "Libvirt/QEMU guest") --- creation of a guest domain (virtual machine, VM), running inside a QEMU hypervisor, using tools found in [[[libvirt]](https://packages.gentoo.org/packages/libvirt)[]] package.
-   [Virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager") --- lightweight GUI application designed for managing virtual machines and containers via the [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") API.
-   [Virt-manager/QEMU_guest](https://wiki.gentoo.org/wiki/Virt-manager/QEMU_guest "Virt-manager/QEMU guest") --- creation of a guest virtual machine (VM) running inside a QEMU hypervisor using just the [virt-manager] GUI tool.
-   [QEMU/Linux guest](https://wiki.gentoo.org/wiki/QEMU/Linux_guest "QEMU/Linux guest") --- describes the setup of a Gentoo Linux guest in [QEMU] using Gentoo bootable media.
-   [QEMU/Bridge with Wifi Routing](https://wiki.gentoo.org/wiki/QEMU/Bridge_with_Wifi_Routing "QEMU/Bridge with Wifi Routing")
-   [Category:QEMU Guests](https://wiki.gentoo.org/wiki/Category:QEMU_Guests "Category:QEMU Guests")
-   [Remote_desktop](https://wiki.gentoo.org/wiki/Remote_desktop "Remote desktop") --- a guide to **[remote desktop](https://en.wikipedia.org/wiki/Remote_desktop_software "wikipedia:Remote desktop software")** software on Gentoo

## [External resources]

-   [https://www.linux-kvm.org/page/KvmOnGentoo](https://www.linux-kvm.org/page/KvmOnGentoo) - The Gentoo article on the KVM wiki
-   [https://wiki.qemu.org/Main_Page](https://wiki.qemu.org/Main_Page) - The Official QEMU wiki

## [[] References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/RceNinja/notes/blob/master/notes/build_qemu_with_enabled_hyper-v_acceleration\_(whpx)\_on_windows.md](https://github.com/RceNinja/notes/blob/master/notes/build_qemu_with_enabled_hyper-v_acceleration_(whpx)_on_windows.md)]]
2.  [[[↑](#cite_ref-2)] [[QEMU / KVM CPU model configuration](https://www.qemu.org/docs/master/system/qemu-cpu-models.html)]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/intel/haxm](https://github.com/intel/haxm)]]
4.  [[[↑](#cite_ref-4)] [[https://forums.gentoo.org/viewtopic-p-8157704.html](https://forums.gentoo.org/viewtopic-p-8157704.html)]]
5.  [[[↑](#cite_ref-5)] [[https://www.qemu.org/docs/master/system/qemu-block-drivers.html#cmdoption-qcow2-arg-nocow](https://www.qemu.org/docs/master/system/qemu-block-drivers.html#cmdoption-qcow2-arg-nocow)]]
6.  [[[↑](#cite_ref-6)] [[https://ww2.coastal.edu/mmurphy2/oer/qemu/audio/](https://ww2.coastal.edu/mmurphy2/oer/qemu/audio/)]]