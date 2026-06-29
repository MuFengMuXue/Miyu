**Resources**

[[]][Hetzner Cloud](https://www.hetzner.com/cloud/)

[[]][FAQ](https://docs.hetzner.com/cloud/servers/faq)

This page describes the installation process of Gentoo Linux on Hetzner Cloud with a shared virtual ARM processor.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Hetzner Cloud Firewall]](#Hetzner_Cloud_Firewall)
    -   [[2.2] [Server IP address]](#Server_IP_address)
    -   [[2.3] [Usage of GPG keys instead of SSH keys]](#Usage_of_GPG_keys_instead_of_SSH_keys)
        -   [[2.3.1] [Client-side actions]](#Client-side_actions)
            -   [[2.3.1.1] [GPG key generation]](#GPG_key_generation)
            -   [[2.3.1.2] [Configuration of gpg-agent]](#Configuration_of_gpg-agent)
    -   [[2.4] [UEFI]](#UEFI)
    -   [[2.5] [Kernel]](#Kernel)
    -   [[2.6] [Scripted Kernel Config]](#Scripted_Kernel_Config)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [SSH]](#SSH)
        -   [[3.1.1] [SSH key]](#SSH_key)
        -   [[3.1.2] [Removal of unnecessary SSH host keys]](#Removal_of_unnecessary_SSH_host_keys)
            -   [[3.1.2.1] [Disabling host key regeneration (OpenRC)]](#Disabling_host_key_regeneration_.28OpenRC.29)
    -   [[3.2] [Network]](#Network)
        -   [[3.2.1] [IPv4 only]](#IPv4_only)
        -   [[3.2.2] [IPv6 only]](#IPv6_only)
        -   [[3.2.3] [IPv4 with IPv6]](#IPv4_with_IPv6)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [f0 respawning]](#f0_respawning)
    -   [[4.2] [jitterentropy initialization failure (unsolved issue)]](#jitterentropy_initialization_failure_.28unsolved_issue.29)
    -   [[4.3] [Losing IPv6 after 20 minutes]](#Losing_IPv6_after_20_minutes)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Hardware]

** Tip**\
It is better to purchase the cheapest machine (2 cores, 4GB of RAM) as clouds can be upgraded but cannot be downgraded (because SSD cannot be scaled down). A checkbox that allows to keep the disk size appears on an attempt to upgrade the machine. If the disk size remains the same, then the downgrade is acceptable. The cheapest model compiles smoothly (`MAKEOPTS="-j2 -l2"`).

### [Standard]

  ---------- ----------------------------------------- -------- ------------------------ -------------------- ---------------- ---------------------------------------------------
  Device     Make/model                                Status   Vendor ID / Product ID   Kernel driver(s)     Kernel version   Notes
  CPU        ARM Neoverse-N1 (QEMU)                    Works    N/A                      N/A                  6.6.13
  GPU        Red Hat, Inc. Virtio 1.0 GPU              Works    1af4:1050                virtio-pci           6.6.13           The kernel parameter `console=tty1` is required.
  SSD        Red Hat, Inc. Virtio 1.0 SCSI             Works    1af4:1048                virtio-pci           6.6.13
  Ethernet   Red Hat, Inc. Virtio 1.0 network device   Works    1af4:1041                virtio-pci           6.6.13           The kernel parameter `net.ifnames=0` is required.
  Keyboard   QEMU USB Keyboard                         Works    0627:0001                hid-generic usbhid   6.6.13
  ---------- ----------------------------------------- -------- ------------------------ -------------------- ---------------- ---------------------------------------------------

### [Detailed information]

`root `[`#`]`lscpu`

    Architecture:           aarch64
      CPU op-mode(s):       32-bit, 64-bit
      Byte Order:           Little Endian
    CPU(s):                 2
      On-line CPU(s) list:  0,1
    Vendor ID:              ARM
      BIOS Vendor ID:       QEMU
      Model name:           Neoverse-N1
        BIOS Model name:    NotSpecified  CPU @ 2.0GHz
        BIOS CPU family:    1
        Model:              1
        Thread(s) per core: 1
        Core(s) per socket: 2
        Socket(s):          1
        Stepping:           r3p1
        BogoMIPS:           50.00
        Flags:              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp ssbs
    NUMA:
      NUMA node(s):         1
      NUMA node0 CPU(s):    0,1
    Vulnerabilities:
      Gather data sampling: Not affected
      Itlb multihit:        Not affected
      L1tf:                 Not affected
      Mds:                  Not affected
      Meltdown:             Not affected
      Mmio stale data:      Not affected
      Retbleed:             Not affected
      Spec rstack overflow: Not affected
      Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:           Mitigation; __user pointer sanitization
      Spectre v2:           Mitigation; CSV2, BHB
      Srbds:                Not affected
      Tsx async abort:      Not affected

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Red Hat, Inc. QEMU PCIe Host bridge [1b36:0008]
        Subsystem: Red Hat, Inc. QEMU PCIe Host bridge [1af4:1100]
    00:01.0 Display controller [0380]: Red Hat, Inc. Virtio 1.0 GPU [1af4:1050] (rev 01)
        Subsystem: Red Hat, Inc. Virtio 1.0 GPU [1af4:1100]
        Kernel driver in use: virtio-pci
        Kernel modules: virtio_pci
    00:02.0 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:02.1 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:02.2 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:02.3 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:02.4 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:02.5 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:02.6 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:02.7 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:03.0 PCI bridge [0604]: Red Hat, Inc. QEMU PCIe Root port [1b36:000c]
        Subsystem: Red Hat, Inc. QEMU PCIe Root port [1b36:0000]
        Kernel driver in use: pcieport
    00:04.0 Serial controller [0700]: Red Hat, Inc. QEMU PCI 16550A Adapter [1b36:0002] (rev 01)
        Subsystem: Red Hat, Inc. QEMU Virtual Machine [1af4:1100]
        Kernel driver in use: serial
    01:00.0 Ethernet controller [0200]: Red Hat, Inc. Virtio 1.0 network device [1af4:1041] (rev 01)
        Subsystem: Red Hat, Inc. Virtio 1.0 network device [1af4:1100]
        Kernel driver in use: virtio-pci
        Kernel modules: virtio_pci
    02:00.0 USB controller [0c03]: Red Hat, Inc. QEMU XHCI Host Controller [1b36:000d] (rev 01)
        Subsystem: Red Hat, Inc. QEMU XHCI Host Controller [1af4:1100]
        Kernel driver in use: xhci_hcd
    03:00.0 Communication controller [0780]: Red Hat, Inc. Virtio 1.0 console [1af4:1043] (rev 01)
        Subsystem: Red Hat, Inc. Virtio 1.0 console [1af4:1100]
        Kernel driver in use: virtio-pci
        Kernel modules: virtio_pci
    04:00.0 Unclassified device [00ff]: Red Hat, Inc. Virtio 1.0 memory balloon [1af4:1045] (rev 01)
        Subsystem: Red Hat, Inc. Virtio 1.0 memory balloon [1af4:1100]
        Kernel driver in use: virtio-pci
        Kernel modules: virtio_pci
    05:00.0 Unclassified device [00ff]: Red Hat, Inc. Virtio 1.0 RNG [1af4:1044] (rev 01)
        Subsystem: Red Hat, Inc. Virtio 1.0 RNG [1af4:1100]
        Kernel driver in use: virtio-pci
        Kernel modules: virtio_pci
    06:00.0 SCSI storage controller [0100]: Red Hat, Inc. Virtio 1.0 SCSI [1af4:1048] (rev 01)
        Subsystem: Red Hat, Inc. Virtio 1.0 SCSI [1af4:1100]
        Kernel driver in use: virtio-pci
        Kernel modules: virtio_pci

`root `[`#`]`lsusb -vt`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 1: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 480M
            ID 0627:0001 Adomax Technology Co., Ltd QEMU Tablet
        |__ Port 2: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 480M
            ID 0627:0001 Adomax Technology Co., Ltd QEMU Tablet

`root `[`#`]`lsmod`

    Module                  Size  Used by
    ipmi_ssif              24576  0
    ipmi_devintf           20480  0
    ipmi_msghandler        49152  2 ipmi_devintf,ipmi_ssif
    sd_mod                 45056  0
    t10_pi                 16384  1 sd_mod
    crc64_rocksoft_generic    16384  1
    sr_mod                 24576  0
    cdrom                  32768  1 sr_mod
    crc64_rocksoft         16384  1 t10_pi
    crc64                  20480  2 crc64_rocksoft,crc64_rocksoft_generic
    sg                     32768  0
    sha2_ce                16384  0
    sha256_arm64           24576  1 sha2_ce
    virtio_scsi            20480  0
    virtio_balloon         20480  0
    virtio_rng             16384  0
    virtio_console         28672  0
    button                 16384  0
    evdev                  20480  2
    binfmt_misc            20480  1
    jc42                   16384  0
    regmap_i2c             16384  1 jc42
    fuse                  106496  1
    dm_mod                106496  0
    configfs               36864  1
    efivarfs               20480  1
    qemu_fw_cfg            16384  0
    ip_tables              24576  0
    x_tables               28672  1 ip_tables
    autofs4                28672  2
    virtio_net             45056  0
    net_failover           20480  1 virtio_net
    failover               16384  1 net_failover
    virtio_pci             24576  0
    virtio_pci_legacy_dev    16384  1 virtio_pci
    virtio_pci_modern_dev    16384  1 virtio_pci
    virtio_mmio            16384  0

`root `[`#`]`dmidecode`

    # dmidecode 3.4
    Getting SMBIOS data from sysfs.
    SMBIOS 3.0.0 present.
    Table at 0x135EC0000.

    Handle 0x0000, DMI type 0, 24 bytes
    BIOS Information
        Vendor: Hetzner
        Version: 20171111
        Release Date: 11/11/2017
        Address: 0xE8000
        Runtime Size: 96 kB
        ROM Size: 64 kB
        Characteristics:
            BIOS characteristics not supported
            Targeted content distribution is supported
            UEFI is supported
            System is a virtual machine
        BIOS Revision: 1.0

    Handle 0x0100, DMI type 1, 27 bytes
    System Information
        Manufacturer: Hetzner
        Product Name: vServer
        Version: 20171111
        Serial Number: 43607703
        UUID: 5316b371-b196-4a2e-9bcd-3488e8f3e8a7
        Wake-up Type: Power Switch
        SKU Number: TM
        Family: Hetzner_vServer

    Handle 0x0200, DMI type 2, 15 bytes
    Base Board Information
        Manufacturer: KVM
        Product Name: KVM Virtual Machine
        Version: virt-6.2
        Serial Number: Not Specified
        Asset Tag: Not Specified
        Features:
            Board is a hosting board
        Location In Chassis: Not Specified
        Chassis Handle: 0x0300
        Type: Motherboard
        Contained Object Handles: 0

    Handle 0x0300, DMI type 3, 22 bytes
    Chassis Information
        Manufacturer: QEMU
        Type: Other
        Lock: Not Present
        Version: NotSpecified
        Serial Number: Not Specified
        Asset Tag: Not Specified
        Boot-up State: Safe
        Power Supply State: Safe
        Thermal State: Safe
        Security Status: Unknown
        OEM Information: 0x00000000
        Height: Unspecified
        Number Of Power Cords: Unspecified
        Contained Elements: 0
        SKU Number: Not Specified

    Handle 0x0400, DMI type 4, 42 bytes
    Processor Information
        Socket Designation: CPU 0
        Type: Central Processor
        Family: Other
        Manufacturer: QEMU
        ID: 00 00 00 00 00 00 00 00
        Version: NotSpecified
        Voltage: Unknown
        External Clock: Unknown
        Max Speed: 2000 MHz
        Current Speed: 2000 MHz
        Status: Populated, Enabled
        Upgrade: Other
        L1 Cache Handle: Not Provided
        L2 Cache Handle: Not Provided
        L3 Cache Handle: Not Provided
        Serial Number: Not Specified
        Asset Tag: Not Specified
        Part Number: Not Specified
        Core Count: 2
        Core Enabled: 2
        Thread Count: 1
        Characteristics: None

    Handle 0x1000, DMI type 16, 23 bytes
    Physical Memory Array
        Location: Other
        Use: System Memory
        Error Correction Type: Multi-bit ECC
        Maximum Capacity: 4000 MB
        Error Information Handle: Not Provided
        Number Of Devices: 1

    Handle 0x1100, DMI type 17, 40 bytes
    Memory Device
        Array Handle: 0x1000
        Error Information Handle: Not Provided
        Total Width: Unknown
        Data Width: Unknown
        Size: 4000 MB
        Form Factor: DIMM
        Set: None
        Locator: DIMM 0
        Bank Locator: Not Specified
        Type: RAM
        Type Detail: Other
        Speed: Unknown
        Manufacturer: QEMU
        Serial Number: Not Specified
        Asset Tag: Not Specified
        Part Number: Not Specified
        Rank: Unknown
        Configured Memory Speed: Unknown
        Minimum Voltage: Unknown
        Maximum Voltage: Unknown
        Configured Voltage: Unknown

    Handle 0x2000, DMI type 32, 11 bytes
    System Boot Information
        Status: No errors detected

    Handle 0xFEFF, DMI type 127, 4 bytes
    End Of Table

## [Installation]

** Note**\
There is an [installation script](https://github.com/m1027/gentoo-utils) for Hetzner Cloud (AMD64, ARM64) provided by [M1027 ](https://wiki.gentoo.org/wiki/User:M1027 "User:M1027"), which might be useful in some circumstances.

Hetzner solutions do not provide the option to boot from a Gentoo installation disk (although it is possible to contact them to add a custom ISO to the menu ^[\[1\]](#cite_note-1)^), but Gentoo can be installed from the [Hetzner Rescue System](https://docs.hetzner.com/robot/dedicated-server/troubleshooting/hetzner-rescue-system/), which is based on Debian, so it doesn\'t matter which distribution is chosen when creating the server. Before creating the server, it would be wise to [configure the firewall](#Hetzner_Cloud_Firewall). Once the firewall is configured, [create an SSH key](https://community.hetzner.com/tutorials/howto-ssh-key) (or [create a GPG key](#Usage_of_GPG_keys_instead_of_SSH_keys)). The created key and firewall should be specified during the [server creation process](https://docs.hetzner.com/cloud/servers/getting-started/creating-a-server/). After creating the server, go to the server menu. Click on the *Rescue* tab and click on the button labeled *Enable rescue & power cycle*. Select the previously created SSH key from the list and click on the button labeled *Enable rescue & power cycle*. The server will reboot into the Rescue System and it will be possible to [connect to it via SSH](https://docs.hetzner.com/cloud/servers/getting-started/connecting-via-private-ip/). The installation process is straightforward, [Handbook:AMD64](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") is usable even for ARM virtual machines. The system should be installed on [/dev/sda] which contains another operating system, so the disk needs to be wiped.

** Note**\
In addition or alternatively to SSH, the [VNC console](https://docs.hetzner.com/cloud/servers/getting-started/vnc-console/) can be used, which is free of charge (not to be confused with the [KVM console](https://docs.hetzner.com/robot/dedicated-server/maintainance/kvm-console/), which is chargeable).

** Tip**\
A [swap file](https://wiki.gentoo.org/wiki/Swap#Swap_files "Swap") can be used instead of a swap partition to save disk space.

### [Hetzner Cloud Firewall]

Hetzner provides a way to configure the [Hetzner Could Firewall](https://docs.hetzner.com/cloud/firewalls/faq/) before server creation. The firewall is free of charge and allows to create a whitelist for incoming traffic, so only allowed IP addresses will be able to connect to the server. This is useful because the server will be protected from attacks until it is ready for public release (or to keep the server completely private). The [official guide](https://docs.hetzner.com/cloud/firewalls/getting-started/creating-a-firewall/) can be used to configure the firewall.

** Important**\
If the cloud is purchased without IPv4 support, IPv6 addresses must be used in the whitelist.

### [Server IP address]

The *Networking* tab shows the IPv6 address as `7777:777:7777:7777::/64`, which is a bit confusing since the IP address to connect to is `7777:777:7777:7777::1` (click on the button with the three dots to the right of the IP address and click *Show Instructions* to see it). Hetzner assigns the first address (`::1`) by default ^[\[2\]](#cite_note-2)^.

### [Usage of GPG keys instead of SSH keys]

It is possible to use [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") to create and store authentication keys.

#### [Client-side actions]

##### [GPG key generation]

Generate a master key as described [here](https://wiki.gentoo.org/wiki/GnuPG#Primary_key "GnuPG") and an authentication key as described [here](https://wiki.gentoo.org/wiki/GnuPG#Add_an_authentication_key "GnuPG"). The articles describe *Ed25519*, but *RSA-4096* is also acceptable. However, moving past *RSA-2048* leads to the inability to use some smartcards and other devices. ^[\[3\]](#cite_note-3)^

To export the public SSH key, execute the following command:

`user `[`$`]`gpg --export-ssh-key KEY_ID`

The key can be treated as a regular SSH key and can be used in Hetzner web forms.

##### [Configuration of gpg-agent]

It is necessary to tell gpg-agent which key to use for SSH. To do so, it is necessary to know the *keygrip* of the authentication key:

`user `[`$`]`gpg --list-keys --with-keygrip`

Once the *keygrip* is known, gpg-agent can be informed (replace *7777777777777777777777777777777777777777* with the *keygrip*):

`user `[`$`]`gpg-connect-agent 'KEYATTR 7777777777777777777777777777777777777777 Use-for-ssh: true' /bye`

gpg-agent will add the corresponding line to [\~/.gnupg/private-keys-v1.d/\<keygrip\>.key], so the above actions need to be performed only once.

Next, it is necessary to tell SSH to use gpg-agent and run it if it is not already running:

[FILE] **`~/.bashrc`**

    export GPG_TTY=`tty`
    export SSH_AUTH_SOCK=`gpgconf --list-dirs agent-ssh-socket`
    gpg-connect-agent /bye 1>&- 2>&-

SSH does not inform gpg-aget which [/dev/pts/\<N\>] to use ^[\[4\]](#cite_note-4)^, so it should be done as below:

[FILE] **`~/.ssh/config`**

    Match host * exec "gpg-connect-agent updatestartuptty /bye"

The configuration will take effect after a reboot or after gpg-agent is safely ^[\[5\]](#cite_note-5)^ terminated:

`user `[`$`]`gpgconf --kill gpg-agent`

### [UEFI]

The cloud uses UEFI with the following entries:

`root `[`#`]`efibootmgr`

    BootCurrent: 0004
    BootOrder: 0004,0005,0006,0007,0003,0001,0000,0002,0008
    Boot0000* UiApp
    Boot0001* UEFI QEMU QEMU CD-ROM
    Boot0002* UEFI Misc Device
    Boot0003* UEFI QEMU QEMU HARDDISK
    Boot0004* UEFI PXEv4 (MAC:96000308A34D)
    Boot0005* UEFI PXEv6 (MAC:96000308A34D)
    Boot0006* UEFI HTTPv4 (MAC:96000308A34D)
    Boot0007* UEFI HTTPv6 (MAC:96000308A34D)
    Boot0008* EFI Internal Shell

If the entries are deleted, they will be recreated after a reboot. The cloud supports the creation of new entries (tested with [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub")).

### [Kernel]

[KERNEL] **Kernel parameters (the root should be modified or deleted depending on the boot method)**

    Boot options  --->
        (root=/dev/sda2 console=tty1 net.ifnames=0) Default kernel command string

[KERNEL] **PCI bus**

    Device Drivers  --->
        [*] PCI support  --->
            --- PCI support
            [*] PCI Express Port Bus support

[KERNEL] **Virtio**

    Device Drivers  --->
        [*] Virtio drivers  --->
            --- Virtio drivers
            [*] PCI driver for virtio devices
            [*] Virtio balloon driver

[KERNEL] **GPU**

    Device Drivers  --->
        Graphics support  --->
            [*] Direct Rendering Manager
            [*] Enable legacy fbdev support for your modesetting driver
            [*] Virtio GPU driver
            [*]   Virtio GPU driver modesetting support

[KERNEL] **SSD**

    Device Drivers  --->
        SCSI device support  --->
            [*] SCSI device support
            [*] SCSI disk support
            [*] SCSI low-level drivers  --->
                --- SCSI low-level drivers
                [*]   virtio-scsi support

[KERNEL] **Ethernet**

    Device Drivers  --->
        [*] Networking support  --->
            --- Network device support
            [*] Network core driver support
            [*]   Virtio network driver

[KERNEL] **Keyboard**

    Device Drivers  --->
        [*] USB support  --->
            --- USB support
            [*]   Support for Host-side USB
            [*]   PCI based USB host interface
            [*]   xHCI HCD (USB 3.0) support

        [*] HID bus support  --->
            --- HID bus support
            -*-   HID bus core support
            [*]     Generic HID driver
            [*]   USB HID support  --->
                      [*] USB HID transport layer

[KERNEL] **RTC (see also [Clock Sync](https://wiki.gentoo.org/wiki/System_time#In-kernel_method "System time"))**

    Device Drivers  --->
        [*] Real Time Clock  --->
            [*] EFI RTC

[KERNEL] **Random Number Generator**

    Device Drivers  --->
        Character devices  --->
            -*- Hardware Random Number Generator Core support  --->
                --- Hardware Random Number Generator Core support
                [*]   VirtIO Random Number Generator support

[KERNEL] **Shutdown button**

    ACPI (Advanced Configuration and Power Interface) Support  --->
        --- ACPI (Advanced Configuration and Power Interface) Support
        [*]   Button

** Note**\
[acpid](https://wiki.gentoo.org/wiki/ACPI "ACPI") needs to be installed and enabled for the shutdown button to work.

### [Scripted Kernel Config]

Since Hetzner Cloud is run on KVM virtual machines, we can take advantage of some default configurations included in the kernel source tree:

    make defconfig
    make kvm_guest.config
    for i in \
        DRM_NOUVEAU \
        DRM_EXYNOS \
        DRM_ROCKCHIP \
        DRM_RCAR_DU \
        DRM_RCAR_DW_HDMI \
        DRM_RCAR_USE_LVDS \
        DRM_RCAR_USE_MIPI_DSI \
        DRM_IMX_DCSS \
        DRM_ETNAVIV \
        DRM_HISI_HIBMC \
        DRM_HISI_KIRIN \
        DRM_MEDIATEK \
        DRM_MSM \
        DRM_MXSFB \
        DRM_MESON \
        DRM_PL111 \
        DRM_TIDSS \
        DRM_LEGACY \
        DRM_SUN4I \
        DRM_TEGRA \
        TEGRA_HOST1X \
        SCSI_UFSHCD \
        FPGA \
        RC_CORE \
        NEW_LEDS \
        CHROME_PLATFORMS \
        SURFACE_PLATFORMS \
        XEN_BLKDEV_FRONTEND \
        LOGO \
        SOUND \
        SLIMBUS \
        SOUNDWIRE \
        MEDIA_SUPPORT \
        MMC \
        BTRFS_FS \
        OVERLAY_FS \
        NFS_FS \
        9P_FS \
        SUSPEND \
        HIBERNATION \
        BLK_DEV_INITRD \
        VIRTUALIZATION \
        WLAN \
        PINCTRL \
        GPIOLIB \
        PWM \
        IPMI_HANDLER \
        CAN \
        BT \
        WIRELESS \
        MD \
        RFKILL \
        NET_9P \
        NFC \
        SPI \
        SPMI \
        HWMON \
        THERMAL \
        IIO \
        USB_NET_DRIVERS \
        XEN_NETDEV_FRONTEND \
        ETHERNET \
        QCOM_IPA \
        REGULATOR \
        STAGING \
        SQUASHFS \
        DEBUG_KERNEL \
        XEN \
        MODULES; do ./scripts/config --disable $i; done
    ./scripts/config --set-str CMDLINE "init=/usr/lib/systemd/systemd root=/dev/sda3 rootwait rootfstype=ext4"
    make -j<n> Image
    mkdir -p /boot/EFI/BOOT
    cp -a /usr/src/linux/arch/arm64/boot/Image /efi/EFI/BOOT/BOOTAA64.EFI

Adapting init and root

## [Configuration]

### [SSH]

** Tip**\
Check the [Security Handbook](https://wiki.gentoo.org/wiki/Security_Handbook/Securing_services#SSH "Security Handbook/Securing services") to properly configure the SSH daemon. In the case of IPv6, `ListenAddress` requires the address to be surrounded by square brackets: `ListenAddress [7777:777:7777:7777::1]:22` (`:22` is an optional port).

** Note**\
In case `ListenAddress` is specified, `rc_need="net.eth0"` must be added to [/etc/conf.d/sshd], otherwise OpenRC will complain about it on boot.

** Important**\
A [system logger](https://wiki.gentoo.org/wiki/Logging "Logging") must be installed to track connection attempts.

#### [SSH key]

Before leaving the Rescue System, the SSH key should be copied to the installed system:

`root `[`#`]`mkdir /mnt/gentoo/root/.ssh`

`root `[`#`]`chmod 700 /mnt/gentoo/root/.ssh`

`root `[`#`]`cp /root/.ssh/authorized_keys /mnt/gentoo/root/.ssh`

`root `[`#`]`chmod 600 /mnt/gentoo/root/.ssh/authorized_keys`

#### [Removal of unnecessary SSH host keys]

Assuming that only *Ed25519* is used, other host keys can be removed:

`root `[`#`]`rm -rf /etc/ssh/ssh_host_ecdsa_key*`

`root `[`#`]`rm -rf /etc/ssh/ssh_host_rsa_key*`

##### [][Disabling host key regeneration (OpenRC)]

To prevent key regeneration, comment out or delete the following line in [/etc/init.d/sshd]:

    $ -A || return 2

Restart the SSH daemon:

`root `[`#`]`rc-service sshd restart`

Check the result from the client machine:

`user `[`$`]`ssh-keyscan <SERVER IP>`

There should only be one host key in the result.

### [Network]

Install [Netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc"):

`root `[`#`]`emerge --ask net-misc/netifrc`

Create the [interface symlink](https://wiki.gentoo.org/wiki/Netifrc#Creating_symlinks "Netifrc"):

`root `[`#`]`ln -s /etc/init.d/net.lo /etc/init.d/net.eth0`

Enable the interface [at boot](https://wiki.gentoo.org/wiki/Netifrc#Enable_at_boot "Netifrc"):

`root `[`#`]`rc-update add net.eth0 default`

#### [IPv4 only]

Replace `XXX.XXX.XXX.XXX` with the real IP. The gateway is provided by Hetzner. ^[\[6\]](#cite_note-6)^ The DNS servers are official servers provided by Hetzner. ^[\[7\]](#cite_note-7)^

[FILE] **`/etc/conf.d/net`**

    config_eth0="XXX.XXX.XXX.XXX/32"
    routes_eth0="172.31.1.1
     default via 172.31.1.1"
    dns_servers_eth0="185.12.64.1 185.12.64.2"

#### [IPv6 only]

** Important**\
Some services (like GitHub ^[\[8\]](#cite_note-8)^) do not support IPv6, and to be able to use such services, it is necessary to use a DNS name server with NAT64 support instead of the official Hetzner name servers. To see a list of such public name servers, see [this link](https://nat64.net/public-providers).

Replace `XXX:XXX:XXX:XXX` with the real IP (found [above](#Server_IP_address)). The gateway is provided by Hetzner. ^[\[9\]](#cite_note-9)^ The DNS servers are official servers provided by Hetzner. ^[\[10\]](#cite_note-10)^

[FILE] **`/etc/conf.d/net`**

    config_eth0="XXXX:XXXX:XXXX:XXXX::1/64"
    routes_eth0="default via fe80::1"
    dns_servers_eth0="2a01:4ff:ff00::add:1 2a01:4ff:ff00::add:2"

#### [IPv4 with IPv6]

The following configuration is a combination of the above configurations.

[FILE] **`/etc/conf.d/net`**

    config_eth0="XXX.XXX.XXX.XXX/32 XXXX:XXXX:XXXX:XXXX::1/64"
    routes_eth0="172.31.1.1
     default via 172.31.1.1
     default via fe80::1"
    dns_servers_eth0="185.12.64.1 185.12.64.2 2a01:4ff:ff00::add:1 2a01:4ff:ff00::add:2"

## [Troubleshooting]

### [f0 respawning]

The following message constantly appears in the VNC console:

    INIT: Id "f0" respawning too fast: disabled for 5 minutes

To get rid of it, follow [these steps](https://wiki.gentoo.org/wiki/MNT_Reform#f0_respawning "MNT Reform").

### [][jitterentropy initialization failure (unsolved issue)]

Sometimes [jitterentropy](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/crypto/jitterentropy.c) initialization fails on boot, but it doesn\'t cause the kernel to panic, just a failure message in the log. Since the error doesn\'t always appear, it\'s most likely a kernel bug. Other ARM machines seem to be affected too. ^[\[11\]](#cite_note-11)^ ^[\[12\]](#cite_note-12)^

`root `[`#`]`dmesg`

    [    0.172340] jitterentropy: Initialization failed with host not compliant with requirements: 9

### [Losing IPv6 after 20 minutes]

If the system keeps losing IPv6 connection after 20 minutes adding following file to the [/etc/syslog.d/00_IPv6.conf] directory might solve the issue.

[FILE] **`/etc/sysctl.d/00_IPv6.conf`Enabling IPv6 privacy extensions**

    net.ipv6.conf.all.forwarding=1
     #net.ipv6.conf.all.accept_ra=2  << Might be over bearing
     net.ipv6.conf.default.forwarding=1
     net.ipv6.conf.enp1s0.accept_ra=2

** Important**\
For IPv6 to work properly ICMPv6 (ping echo) needs to be allowed, this is a mandatory IPv6 setting. Forbidding ICMPv6 will break IPv6 connectivity.

## [See also]

-   [QEMU/Linux guest](https://wiki.gentoo.org/wiki/QEMU/Linux_guest "QEMU/Linux guest")
-   [QEMU/KVM IPv6 Support](https://wiki.gentoo.org/wiki/QEMU/KVM_IPv6_Support "QEMU/KVM IPv6 Support")

## [References]

1.  [[[↑](#cite_ref-1)] [[https://docs.hetzner.com/cloud/servers/faq/#how-can-i-get-a-custom-iso](https://docs.hetzner.com/cloud/servers/faq/#how-can-i-get-a-custom-iso)]]
2.  [[[↑](#cite_ref-2)] [[https://docs.hetzner.com/cloud/servers/faq/#why-can-i-not-connect-to-my-ipv6-only-cloud-server](https://docs.hetzner.com/cloud/servers/faq/#why-can-i-not-connect-to-my-ipv6-only-cloud-server)]]
3.  [[[↑](#cite_ref-3)] [[https://www.gnupg.org/faq/gnupg-faq.html#no_default_of_rsa4096](https://www.gnupg.org/faq/gnupg-faq.html#no_default_of_rsa4096)]]
4.  [[[↑](#cite_ref-4)] [[https://www.gnupg.org/documentation/manuals/gnupg/Common-Problems.html](https://www.gnupg.org/documentation/manuals/gnupg/Common-Problems.html)]]
5.  [[[↑](#cite_ref-5)] [[https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html)]]
6.  [[[↑](#cite_ref-6)] [[https://docs.hetzner.com/cloud/servers/static-configuration/](https://docs.hetzner.com/cloud/servers/static-configuration/)]]
7.  [[[↑](#cite_ref-7)] [[https://docs.hetzner.com/dns-console/dns/general/recursive-name-servers/](https://docs.hetzner.com/dns-console/dns/general/recursive-name-servers/)]]
8.  [[[↑](#cite_ref-8)] [[https://github.com/orgs/community/discussions/10539](https://github.com/orgs/community/discussions/10539)]]
9.  [[[↑](#cite_ref-9)] [[https://docs.hetzner.com/cloud/servers/static-configuration/](https://docs.hetzner.com/cloud/servers/static-configuration/)]]
10. [[[↑](#cite_ref-10)] [[https://docs.hetzner.com/dns-console/dns/general/recursive-name-servers/](https://docs.hetzner.com/dns-console/dns/general/recursive-name-servers/)]]
11. [[[↑](#cite_ref-11)] [[https://patchwork.yoctoproject.org/project/oe-core/patch/20231003122542.764073-1-ross.burton@arm.com/](https://patchwork.yoctoproject.org/project/oe-core/patch/20231003122542.764073-1-ross.burton@arm.com/)]]
12. [[[↑](#cite_ref-12)] [[https://lore.kernel.org/linux-arm-kernel/68c6b70a-8d6c-08b5-46ce-243607479d5c@i2se.com/T/](https://lore.kernel.org/linux-arm-kernel/68c6b70a-8d6c-08b5-46ce-243607479d5c@i2se.com/T/)]]