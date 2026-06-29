**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Virtualization "wikipedia:Virtualization")

**Virtualization** is the concept and technique that permits running software in an environment separate from a computer operating system.

This article deals with [system virtual machines](https://en.wikipedia.org/wiki/System_virtual_machine "wikipedia:System virtual machine") and [OS-level virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization "wikipedia:OS-level virtualization") rather than [process virtual machines](https://en.wikipedia.org/wiki/Virtual_machine#Process_virtual_machines "wikipedia:Virtual machine") such as the [Java virtual machine](https://en.wikipedia.org/wiki/Java_virtual_machine "wikipedia:Java virtual machine") or the [.NET Common Language Runtime](https://en.wikipedia.org/wiki/Common_Language_Runtime "wikipedia:Common Language Runtime").

The operating system actually running on the hardware is referred to as the *host*. On this host resides a [hypervisor](https://en.wikipedia.org/wiki/Hypervisor "wikipedia:Hypervisor") (aka *virtual machine manager*), which runs [virtual machines](https://en.wikipedia.org/wiki/virtual_machine "wikipedia:virtual machine") containing *guest* software.

## Contents

-   [[1] [Hardware feature]](#Hardware_feature)
    -   [[1.1] [System firmware]](#System_firmware)
    -   [[1.2] [Kernel support]](#Kernel_support)
        -   [[1.2.1] [AMD CPUs]](#AMD_CPUs)
        -   [[1.2.2] [Intel CPUs]](#Intel_CPUs)
-   [[2] [Available software]](#Available_software)
    -   [[2.1] [Hypervisors]](#Hypervisors)
    -   [[2.2] [Containers]](#Containers)
        -   [[2.2.1] [Orchestration]](#Orchestration)
            -   [[2.2.1.1] [Libvirt]](#Libvirt)
    -   [[2.3] [GUIs]](#GUIs)
    -   [[2.4] [Guest facilities]](#Guest_facilities)
    -   [[2.5] [Utilities]](#Utilities)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Hardware feature]

Most modern computer architectures include support for virtualization at the hardware level.

For the **[AMD64]** and **[x86]** computer architectures, hardware virtualization is supported via [AMD\'s AMD-V (svm)](https://en.wikipedia.org/wiki/X86_virtualization#AMD_virtualization_.28AMD-V.29 "wikipedia:X86 virtualization") or [Intel\'s Vt-x (vmx)](https://en.wikipedia.org/wiki/X86_virtualization#Intel-VT-x "wikipedia:X86 virtualization") virtualization extensions. The virtualization extensions must be supported by the processor *and* enabled in the system\'s firmware (typically the motherboard\'s firmware menu) in order to be accessible by guest operating system(s).

### [System firmware]

Accessing the appropriate menu for enabling virtualization support in the system firmware is beyond the scope of this article. Each manufacture has a sightly different navigation and title for the setting. Generally, there is a toggle for \"Virtualization\" under the CPU settings of the motherboard firmware.

Once enabled at the firmware level, validate support is available in the kernel.

### [Kernel support]

#### [AMD CPUs]

To inspect hardware for virtualization support issue the following command:

`user `[`$`]`grep --color -E "svm" /proc/cpuinfo`

The running kernel supports hardware virtualization when \"svm\" is visible in the output.

#### [Intel CPUs]

Hardware virtualization support for [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") based systems can be tested by running the following command:

`user `[`$`]`grep --color -E "vmx" /proc/cpuinfo`

The running kernel supports hardware virtualization when \"vmx\" is visible in the output.

## [Available software]

### [Hypervisors]

  ----------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                  Package                                                                                                                                                                                                                                                                                                                                                                                          Description
  [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU")                                                      [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]]                     **Q**uick **EMU**lator, a generic, open source, hardware emulator and virtualization suite.
  [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox")                                    [[[app-emulation/virtualbox]](https://packages.gentoo.org/packages/app-emulation/virtualbox)[]]   Cross-platform virtualization software that allows users to run guest operating systems inside a host operating system.
  [Xen](https://wiki.gentoo.org/wiki/Xen "Xen")                                                         [[[app-emulation/xen]](https://packages.gentoo.org/packages/app-emulation/xen)[]]                        Native, bare-metal, hypervisor that allows multiple distinct virtual machines (referred to as domains) to share a single physical machine.
  [Bhyve (FreeBSD)](https://bhyve.org/)                                 paravirtualization^[\[1\]](#cite_note-1)^                                                                                                                                                                                                                                                                                                                                                        bhyve, the \"BSD hypervisor\" is a hypervisor/virtual machine manager available on FreeBSD, macOS, and Illumos.
  [User-Mode Linux (UML)](https://avdv.github.io/libvirt/drvuml.html)   paravirtualization^[\[2\]](#cite_note-2)^                                                                                                                                                                                                                                                                                                                                                        The UML driver for libvirt allows use and management of paravirtualized guests built for User Mode Linux. UML is a software-assist, Type-2 virtualization. Incorporated into mainstream Linux repository in 2016
  ----------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Containers]

[Containers](https://en.wikipedia.org/wiki/OS-level_virtualization "wikipedia:OS-level virtualization") provide isolated user space instances.

  -------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                                                         Package                                                                                                                                                                                                                                                                                                                                                                                                                           Description
  Buildah                                                                                                                                      [[[app-containers/buildah]](https://packages.gentoo.org/packages/app-containers/buildah)[]]                                          Tool that facilitates building OCI images.
  [Docker](https://wiki.gentoo.org/wiki/Docker "Docker")                                                                                       [[[app-containers/docker]](https://packages.gentoo.org/packages/app-containers/docker)[]]                                             Container virtualization environment which can establish development or runtime environments without modifying the environment of the base operating system.
  [LXC](https://wiki.gentoo.org/wiki/LXC "LXC") (Linux Containers)                                                                             [[[app-containers/lxc]](https://packages.gentoo.org/packages/app-containers/lxc)[]]                                                      Virtualization system making use of the cgroups feature of the Linux kernel.
  [LXD](https://wiki.gentoo.org/wiki/LXD "LXD")                                                                                                [[[app-containers/lxd]](https://packages.gentoo.org/packages/app-containers/lxd)[]]                                                      Next generation system container manager.
  [Podman](https://wiki.gentoo.org/wiki/Podman "Podman")                                                                                       [[[app-containers/podman]](https://packages.gentoo.org/packages/app-containers/podman)[]]                                             Daemonless container engine for developing, managing, and running [OCI Containers](https://opencontainers.org/) on linux.
  [containerd]                                      [[[app-containers/containerd]](https://packages.gentoo.org/packages/app-containers/containerd)[]]                                 container runtime (daemon) that handles pulling, storing, and running images; default CRI in Kubernetes. Powers most modern setups (e.g., under Docker/Podman); lightweight and secure for edge/AI workloads. OCI-compliant.
  [nerdctl]                                         [[[app-containers/nerdctl]](https://packages.gentoo.org/packages/app-containers/nerdctl)[]]                                          CLI tool for running OCI containers via [containerd] using Docker-compatible syntax. Podman alternative for containerd users; daemonless, rootless, and integrates with Kubernetes. Gaining traction in homelabs (r/homelab).
  [systemd-nspawn](https://wiki.gentoo.org/wiki/Systemd/systemd-nspawn "Systemd/systemd-nspawn")^[\[3\]](#cite_note-3)[\[4\]](#cite_note-4)^
  Systemd nspawn.                                                                                                                              [[[sys-apps/gentoo-systemd-integration]](https://packages.gentoo.org/packages/sys-apps/gentoo-systemd-integration)[]]   Latest newcomer, not fully tested as of 3/2025.
  Skopeo                                                                                                                                       [[[app-containers/skopeo]](https://packages.gentoo.org/packages/app-containers/skopeo)[]]                                             Tool for copying, inspecting, and signing OCI/Docker images between registries and storage. Essential for multi-registry workflows; pairs with Buildah/Podman.
  -------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [Orchestration]

[Container orchestration](https://en.wikipedia.org/wiki/Orchestration_(computing) "wikipedia:Orchestration (computing)") concerns the details of managing multiple Linux containers and virtual machines (VMs).

This management layer spins up and spins down individual containers and VMs.

Examples of orchestration managers are [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt"), [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") and Mesos, although others exist. There is also container orchestration where K8/docker swarm and related software compete for similar management functions.

Name

Package

Description

Kubernetes (K8s)

[[[app-emulation/kubernetes]](https://packages.gentoo.org/packages/app-emulation/kubernetes)[]]

Automating deployment, scaling, and operations of application containers across clusters of hosts.

Portainer

[[[app-containers/portainer]](https://packages.gentoo.org/packages/app-containers/portainer)[]]

Web-based GUI for managing Docker, Kubernetes, LXC, and Podman environments. Simplifies ops for non-CLI users; top-rated for homelabs and small teams. Multi-environment dashboard, RBAC, stack deployment (Compose/YAML).

OpenShift

[[[app-emulation/openshift]](https://packages.gentoo.org/packages/app-emulation/openshift)[]]

Enterprise Kubernetes platform from Red Hat, with built-in CI/CD and security. Popular for hybrid cloud/enterprise Linux (RHEL/Fedora); extends K8s with developer tools. Source-to-image builds, SELinux integration, auto-vuln scanning.

\

##### [Libvirt]

The widest coverage of and most common orchestration is [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt").

Libvirt handle the following virtualization engines: BHyve, [LXC](https://wiki.gentoo.org/wiki/LXC "LXC"), [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU"), QEMU/[KVM](https://wiki.gentoo.org/wiki/KVM "KVM"), [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox"), [OpenVZ](https://wiki.gentoo.org/wiki/OpenVZ "OpenVZ") (Virtuozzo), [VMware](https://wiki.gentoo.org/wiki/VMware "VMware") ESX, and [Xen](https://wiki.gentoo.org/wiki/Xen "Xen").

For storage support, Libvirt handles Virtio directory sharing, Direct block device access, gluster, [iSCSI](https://wiki.gentoo.org/wiki/ISCSI "ISCSI")/SCSI, [LVM](https://wiki.gentoo.org/wiki/LVM "LVM"), multi-path devices, netfs, RADOS/[Ceph](https://wiki.gentoo.org/wiki/Ceph "Ceph"), and Sheepdog.

For network drivers, Libvirt handles nearly all network types.

### [GUIs]

  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------
  Name                                                                       Package                                                                                                                                                                                                                                                                                                                                                                                                Description
  [GNOME Boxes](https://wiki.gentoo.org/wiki/Boxes "Boxes")                  [[[gnome-extra/gnome-boxes]](https://packages.gentoo.org/packages/gnome-extra/gnome-boxes)[]]            Simple GNOME application to access remote or virtual systems.
  [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager")   [[[app-emulation/virt-manager]](https://packages.gentoo.org/packages/app-emulation/virt-manager)[]]   Graphical tool for administering virtual machines.
  [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox")         [[[app-emulation/virtualbox]](https://packages.gentoo.org/packages/app-emulation/virtualbox)[]]         A GUI is included by default with VirtualBox. The `headless` USE flag is can be enabled to remove GUI support.
  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------

### [Guest facilities]

Guest facilities are packages that are installed and configured inside the guest domain (VM) that enables better interactions with its VM manager on the host platform. Such extra functionality may entail power-switch handling, graphic card passthrough, battery-level, or keyboard handling.

** Note**\
While guest facilities deals with Linux-centric guest OS, there are some tools that are specific to the host\'s (non-Linux) operating system.

The following packages are for Gentoo **guests** running *inside* virtual machines. See [Category:QEMU Guests](https://wiki.gentoo.org/wiki/Category:QEMU_Guests "Category:QEMU Guests") for tools helping to run other operating systems inside virtual machines.

  -------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------- ---------------------
  Name                                                                 Package                                                                                                                                                                                                                                                                                                                                                                                                                                          Description                                                                                 Host O/S
  [ACPI](https://wiki.gentoo.org/wiki/ACPI "ACPI")                     [[[sys-power/acpid]](https://packages.gentoo.org/packages/sys-power/acpid)[]]                                                                              for proper shutdown handling by [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt")   Linux
  [USB](https://wiki.gentoo.org/wiki/USB "USB")                        [[[net-misc/spice-gtk]](https://packages.gentoo.org/packages/net-misc/spice-gtk)[]]                                                                     USB redirection                                                                             Linux
  [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox")   [[[app-emulation/virtualbox-guest-additions]](https://packages.gentoo.org/packages/app-emulation/virtualbox-guest-additions)[]]   VirtualBox Guest Additions                                                                  Windows/Linux/macOS
  [VMware](https://wiki.gentoo.org/wiki/VMware "VMware")               [[[app-emulation/open-vm-tools]](https://packages.gentoo.org/packages/app-emulation/open-vm-tools)[]]                                          VMware, Inc. sells a variety of closed-source hypervisors.                                  Windows/Linux/macOS
  -------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------- ---------------------

### [Utilities]

  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name         Package                                                                                                                                                                                                                                                                                                                                                                                          Description
  libguestfs   [[[app-emulation/libguestfs]](https://packages.gentoo.org/packages/app-emulation/libguestfs)[]]   Tools for accessing and modifying VM disk images. Provides [guestfish], [guestmount], [virt-cat], [virt-copy-\*], etc.
  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [See also]

-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.
-   [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") --- a virtualization management toolkit
-   [Embedded Handbook/General/Compiling with QEMU user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_QEMU_user_chroot "Embedded Handbook/General/Compiling with QEMU user chroot") --- how to use [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") to chroot into a system that targets a different architecture (e.g. **[aarch64]**) than the one being used (e.g. **[amd64]**).
-   [Comparison of virtual machines](https://wiki.gentoo.org/wiki/Comparison_of_virtual_machines "Comparison of virtual machines") --- compares the features of several platform virtual machines.
-   [Recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"))

## [References]

1.  [[[↑](#cite_ref-1)] [[https://en.wikipedia.org/wiki/Paravirtualization](https://en.wikipedia.org/wiki/Paravirtualization)]]
2.  [[[↑](#cite_ref-2)] [[https://en.wikipedia.org/wiki/Paravirtualization](https://en.wikipedia.org/wiki/Paravirtualization)]]
3.  [[[↑](#cite_ref-3)] [[https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html](https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html)]]
4.  [[[↑](#cite_ref-4)] [[https://en.wikipedia.org/wiki/OS-level_virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization)]]