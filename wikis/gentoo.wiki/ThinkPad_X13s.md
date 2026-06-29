[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x13s-type-21bx-21by)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X13s_Gen_1/ThinkPad_X13s_Gen_1_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X13s_Gen_1?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x13s_gen1_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x13s_gen1_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

The **Lenovo ThinkPad X13s** is an ARM64 based laptop with good support under Linux and Gentoo. Most features work flawlessly with a few still being under active development. For details on the support of each feature check [this page](https://github.com/jhovold/linux/wiki/X13s).

This laptop isn\'t the fastest ever, but performs well and gets 12-16 hours of battery life under normal use conditions.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Requirements and constraints]](#Requirements_and_constraints)
    -   [[2.2] [Options to Modify the Boot Menu]](#Options_to_Modify_the_Boot_Menu)
    -   [[2.3] [Web Resources]](#Web_Resources)
    -   [[2.4] [Kernel]](#Kernel)
    -   [[2.5] [initrd]](#initrd)
        -   [[2.5.1] [Dracut]](#Dracut)
        -   [[2.5.2] [Genkernel]](#Genkernel)
    -   [[2.6] [Bootloader]](#Bootloader)
    -   [[2.7] [User-space]](#User-space)
-   [[3] [Post-install]](#Post-install)
    -   [[3.1] [Audio]](#Audio)
    -   [[3.2] [Video Acceleration]](#Video_Acceleration)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [f0 respawning]](#f0_respawning)
    -   [[4.2] [Clock loses time on reboot]](#Clock_loses_time_on_reboot)
    -   [[4.3] [MAC Address changes on reboot]](#MAC_Address_changes_on_reboot)
-   [[5] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  ----------- ------------------------------------- ------------- ------------------------ ------------------ ---------------- -------
  Device      Make/model                            Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU         Qualcomm Snapdragon 8cx Gen 3         Works         N/A                      N/A                6.7.3
  iGPU        Qualcomm Adreno™ 690 GPU              Works         N/A                      N/A                6.7.3
  SSD         Micron Technology Inc 2450 NVMe SSD   Works         1344:5411                nvme               6.7.3
  Sound       N/A                                   Works         N/A                      N/A                6.7.3
  Wi-Fi       Qualcomm Wi-Fi® 6E WCN6855            Works         17cb:1103                ath11k_pci         6.7.3
  Bluetooth   Qualcomm Wi-Fi® 6E WCN6855            Works         17cb:1103                N/A                6.7.3
  Webcam      N/A                                   Not tested    N/A                      N/A                N/A
  ----------- ------------------------------------- ------------- ------------------------ ------------------ ---------------- -------

### [Detailed information]

`root `[`#`]`lscpu`

    Architecture:           aarch64
      CPU op-mode(s):       32-bit, 64-bit
      Byte Order:           Little Endian
    CPU(s):                 8
      On-line CPU(s) list:  0-7
    Vendor ID:              ARM
      Model name:           Cortex-A78C
        Model:              0
        Thread(s) per core: 1
        Core(s) per socket: 4
        Socket(s):          1
        Stepping:           r0p0
        CPU(s) scaling MHz: 100%
        CPU max MHz:        2438.3999
        CPU min MHz:        300.0000
        BogoMIPS:           38.40
        Flags:              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp uscat ilrcpc flagm
      Model name:           Cortex-X1C
        Model:              0
        Thread(s) per core: 1
        Core(s) per socket: 4
        Socket(s):          1
        Stepping:           r0p0
        CPU(s) scaling MHz: 28%
        CPU max MHz:        2995.2000
        CPU min MHz:        825.6000
        BogoMIPS:           38.40
        Flags:              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp uscat ilrcpc flagm
    NUMA:
      NUMA node(s):         1
      NUMA node0 CPU(s):    0-7
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

    0002:00:00.0 PCI bridge [0604]: Qualcomm Technologies, Inc SC8280XP PCI Express Root Port [17cb:010e]
            Kernel driver in use: pcieport
    0002:01:00.0 Non-Volatile memory controller [0108]: Micron Technology Inc 2450 NVMe SSD [HendrixV] (DRAM-less) [1344:5411] (rev 01)
            Subsystem: Micron Technology Inc 2450 NVMe SSD [HendrixV] (DRAM-less) [1344:0100]
            Kernel driver in use: nvme
    0004:00:00.0 PCI bridge [0604]: Qualcomm Technologies, Inc SC8280XP PCI Express Root Port [17cb:010e]
            Kernel driver in use: pcieport
    0006:00:00.0 PCI bridge [0604]: Qualcomm Technologies, Inc SC8280XP PCI Express Root Port [17cb:010e]
            Kernel driver in use: pcieport
    0006:01:00.0 Network controller [0280]: Qualcomm Technologies, Inc QCNFA765 Wireless Network Adapter [17cb:1103] (rev 01)
            Subsystem: Qualcomm Technologies, Inc QCNFA765 Wireless Network Adapter [17cb:0108]
            Kernel driver in use: ath11k_pci
            Kernel modules: ath11k_pci

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 06cb:00fc Synaptics, Inc.
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`root `[`#`]`lsusb -vt`

    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/4p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 004: Dev 002, If 0, Class=Vendor Specific Class, Driver=[none], 12M
            ID 06cb:00fc Synaptics, Inc.
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/2p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 005.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 006.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub

## [Installation]

Installing Gentoo on the **ThinkPad X13s** is very similar to how one installs Gentoo on just about any EFI-based laptop. The main parts that need special attention are the GPU and the kernel/dtb (plus firmware blobs).

##### [Requirements and constraints]

Due to the \"freshness\" of all the x13s kernel and devicetree bits, the install path starts with building a kernel and creating a bootable USB stick for this device. This can either be done natively (on another arm64 device) or using a cross-compiler and qemu. Either of these methods will also require some additional hardware, either a USB-C flash drive or a small USB-C dock/hub with type-A USB ports (a USB-C ethernet adapter can also be very helpful).

Although the walk-through document uses windows boot manager, the preferred tool is [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr").

The Gentoo arm64 USB image does not seem to successfully boot, but there is a [custom Arch boot image](https://github.com/ironrobin/archiso-x13s) that does and it has all the tools necessary to install Gentoo on it.

NOTE: For now it is necessary to cross(or native) build the initial kernel for the device (and the boot stick!!) using the WIP branches listed below in order to have the proper thermal throttling.

##### [Options to Modify the Boot Menu]

How to get the Gentoo grub install to boot by default? There are several options:

-   the walkthrough below uses the debian installer to get the grub shell, to run an EFI shell, and then use the bcfg command
-   instead, add an EFI shell to your boot stick and/or internal SSD (use the EDK2 link below and follow debian wakthrough)
-   if efi runtime is working, use [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") as mentioned above
-   install [refind](https://wiki.gentoo.org/wiki/Refind "Refind")

Note recent version of the UEFI BIOS should have a UI to edit the order of boot menu entries, but new entries cannot be created that way.

##### [Web Resources]

The [install walk-through](https://docs.google.com/document/d/1WuxE-42ZeOkKAft5FuUk6C2fonkQ8sqNZ56ZmZ49hGI/mobilebasic#heading=h.d1689esafsky) for the hacked debian installer .iso can be a helpful resource. Other related repositories and readme files may also be of interest:

-   [https://github.com/jhovold/linux/wiki/X13s](https://github.com/jhovold/linux/wiki/X13s)
-   [https://github.com/steev/thinkpad-x13s](https://github.com/steev/thinkpad-x13s)
-   [https://github.com/ironrobin/x13s-alarm](https://github.com/ironrobin/x13s-alarm)
-   [https://fedoraproject.org/wiki/Thinkpad_X13s](https://fedoraproject.org/wiki/Thinkpad_X13s)
-   [https://github.com/aarch64-laptops/build](https://github.com/aarch64-laptops/build)
-   [https://github.com/VCTLabs/alsa-ucm-conf](https://github.com/VCTLabs/alsa-ucm-conf)
-   [https://github.com/tianocore/edk2/releases/download/edk2-stable201911/ShellBinPkg.zip](https://github.com/tianocore/edk2/releases/download/edk2-stable201911/ShellBinPkg.zip)

### [Kernel]

Since kernel patches are still in the patch queue/review process, the working patch set is on several branches in [this repo](https://github.com/steev/linux/branches) but be sure and check for the latest branch version(s). Use one of the configs in the kernel source to start; a good choice is laptop_defconfig.

Multiple kernel branch versions are (relatively) current/available depending on needs/level of risk tolerance:

-   lenovo-x13s-linux-6.5.y
-   lenovo-x13s-linux-6.6.y
-   lenovo-x13s-linux-6.7.y

It is recommended to clone with a depth of 1 initially; the default (manual) kernel install paths work fine (see example in grub.cfg snippet).

`root `[`#`]`cd /usr/src`

`root `[`#`]`git clone --depth 1 `[`https://github.com/steev/linux.git`](https://github.com/steev/linux.git)` -b lenovo-x13s-linux-6.7.y`

`root `[`#`]`cd linux`

`root `[`#`]`make -j9 laptop_defconfig all modules_install install dtbs_install`

### [initrd]

When generating an initrd make sure the following kernel modules are included and loaded early, to ensure the display output is working.

The list below was scraped from one of the install docs. Depending on which tools are used to generate the initrd, all or some of those might be included automatically. Note that dracut does not really provide an easy way to include an arbitrary set of firmware blobs; if the dracut initramfs doesn\'t work with the chosen kernel, then see below (or use [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") instead).

#### [Dracut]

When using [dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") to build the initrd, add a configuration file that looks like this:

[FILE] **`/etc/dracut.conf.d/20_thinkpad-x13s.conf`**

    force_drivers+=" nvme phy_qcom_qmp_pcie pcie_qcom i2c_hid_of i2c_qcom_geni leds_qcom_lpg pwm_bl qrtr pmic_glink_altmode gpio_sbu_mux phy_qcom_qmp_combo panel-edp msm phy_qcom_edp "

With nothing else in the above config, a minimal but working initramfs of approx. 12 MBs can be generated via the following:

`root `[`#`]`dracut --kver 6.6.2 -m "kernel-modules rootfs-block base"`

Note the version shown above is just an example, and the argument is only required if building for a non-running kernel.

To make a somewhat larger initramfs with dracut and use the same set of firmware sub-directories used in the genkernel example requires some manual work to create an \"overlay\" tree, which can then be used by the one-time-only \--include argument with the following config file, e.g.,

`root `[`#`]`dracut --kver 6.7.3+ --include initrd-fw-tree / --force `

[FILE] **`/etc/dracut.conf.d/20_thinkpad-x13s.conf`**

    force_drivers+=" nvme phy_qcom_qmp_pcie pcie_qcom i2c_hid_of i2c_qcom_geni leds_qcom_lpg pwm_bl qrtr pmic_glink_altmode gpio_sbu_mux phy_qcom_qmp_combo panel-edp msm phy_qcom_edp "

    dracutmodules+=" kernel-modules rootfs-block udev-rules base fs-lib shutdown "

Note that in the above command, the included path `initrd-fw-tree` is a local firmware directory tree (relative to the root dir) with a small subset of firmware directories and their respective contents. Create the overlay tree first using something like the following:

`root `[`#`]`cd /lib/firmware/`

`root `[`#`]`mkdir -p ~/initrd-fw-tree/lib/firmware/qcom`

`root `[`#`]`cp -a ./ ~/initrd-fw-tree/lib/firmware/`

`root `[`#`]`cp -a qcom/sc8280xp ~/initrd-fw-tree/lib/firmware/qcom/`

#### [Genkernel]

The primary requirements for a working initramfs (meaning one that activates the peripherals) are a handful of modules and firmware blobs. Most of the config options are up to the user, however, the required bits are shown below:

[FILE] **`/etc/genkernel.conf`**

    # Add in early microcode support: this sets the kernel options for early microcode loading
    # Possible values: empty/"no", "all", "intel", "amd"
    MICROCODE=""
    ...
    FIRMWARE="yes"
    ...
    # Specify a comma-separated list of firmware files or directories to include,
    # relative to FIRMWARE_DIR (if FIRMWARE option above is set to YES
    # and ALLFIRMWARE is set to NO).
    FIRMWARE_FILES="qcom/sc8280xp,qca,ath10k,ath11k,ath6k,RTL8192E,regulatory.db"
    ...
    #AMODULES_group="module-to-include another-module"
    AMODULES_nvme="nvme phy_qcom_qmp_pcie pcie_qcom i2c_hid_of i2c_qcom_geni leds_qcom_lpg pwm_bl qrtr pmic_glink_altmode gpio_sbu_mux phy_qcom_qmp_combo panel-edp msm phy_qcom_edp"

Note that using `ALLFIRMWARE=yes` does work, however the generated initramfs is over 60 MBs compressed. The \"base\" config shown above should result in an initramfs file about half as big. Refer to the [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") page for more info. The following command should work to generate just the initramfs file:

`root `[`#`]`genkernel initramfs`

### [Bootloader]

No u-boot here, just EFI BIOS firmware and any of the usual EFI bootloaders, ie, Grub works with both install modes, as well as an EFI stub kernel. Either of these methods requires both an initramfs and the devicetree blob passed to the kernel (note: install grub with efi support and [devicetree patches](https://github.com/VCTLabs/embedded-overlay) otherwise grub will not add devicetree to the config so it must be added manually instead).

Certain kernel parameters are required to get the system to boot and run optimally. These can be added to the default grub config as shown below.

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX="efi=noruntime pd_ignore_unused clk_ignore_unused arm64.nopauth"

-   pd_ignore_usused - keeps some power domains from being erroneously turned off
-   clk_ignore_unused - keeps some clocks from being erroneously turned off, this keeps the display from turning off immediately after boot
-   for pre-6.7 kernels, include `pcie_aspm.policy=powersupersave` to enable PCIe ASPM
-   for 6.7.0 or later kernels, `efi=noruntime` can be removed if the Linux boot option is enabled in the bios

If using the grub devicetree patches, then also add the following:

[FILE] **`/etc/default/grub`**

    GRUB_DEFAULT_DTB="qcom/sc8280xp-lenovo-thinkpad-x13s.dtb"

After adding these be sure to run the following command in order to have them added to the grub config:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

After installing a new kernel and running grub-mkconfig, if not using the patched grub from the overlay, remember to add the following line to each boot stanza in grub.cfg, using the local version, path, etc, keeping in mind that the file root will be the same as where the kernel and initramfs are stored:

[FILE] **`/boot/grub/grub.cfg`**

    devicetree  /boot/dtbs/6.3.0-rc2-x13s-r0/qcom/sc8280xp-lenovo-thinkpad-x13s.dtb

### [User-space]

The user-space configuration consists mainly of firmware blobs (not yet in linux-firmware) and some Qualcomm-specific user-space daemons borrowed from Android. The latest a690 GPU support should be in the current mesa package(s).

-   [Alarm x13s repo](https://github.com/ironrobin/x13s-alarm/tree/trunk/x13s-firmware) - WLAN/BT, GPU, Audio firmware (sys-firmware/x13s-firmware)
    -   reinstall `linux-firmware` without the USE=savedconfig if done previously for this machine
    -   use the latest non-live ebuild versions for both x13s-firmware and linux-firmware (\>=linux-firmware-20231211 and \>=x13s-firmware-20231030-r1)
-   [qrtr](https://github.com/andersson/qrtr) - namespace daemon for net/qrtr in the Linux kernel (sys-power/qrtr-1.1)
-   [pd-mapper](https://github.com/andersson/pd-mapper) - Qualcomm Protection Domain mapper daemon (sys-power/pd-mapper-1.0)
    -   install and configure the firmware and `sys-power/pd-mapper` as shown below
-   [audio config](https://github.com/alsa-project/alsa-ucm-conf) - ALSA UCM configuration files (media-libs/alsa-ucm-conf). The current working version is 9999 from the overlay below or master branch from upstream

In-progress ebuilds for the above can be found in the [embedded overlay](https://github.com/VCTLabs/embedded-overlay). Be sure to install and activate the overlay *before* installing an actual desktop, eg, Gnome or XFCE. Manually installing `sys-firmware/x13s-firmware` and `sys-power/pd-mapper` along with one of the big desktops should pull in all the required bits.

To configure bluetooth and the Qualcomm user-space bits:

`root `[`#`]`emerge linux-firmware x13s-firmware -v --ask `

`root `[`#`]`emerge sys-power/pd-mapper -v --ask `

Edit /etc/conf.d/bdaddr and change the last 3 octets

`root `[`#`]`rc-update del bluetooth `

`root `[`#`]`rc-update add bdaddr `

`root `[`#`]`rc-update add pd-mapper `

`root `[`#`]`openrc `

## [Post-install]

These devices are generally \"new\" enough to need BIOS firmware updates, which can be obtained from the Lenovo support page. If the device no longer has the vendor-installed OS, follow the steps here to [create a bootable USB stick](https://gitlab.com/TheOneWithTheBraid/x13s-firmware-update) for updating the BIOS firmware. Selecting the USB disk from the (BIOS) Boot Menu will automatically launch the EFI firmware installer.

Possibly some configuration nits may also need to be addressed; feel free to add your own here.

### [Audio]

In order to get audio working install PipeWire with PulseAudio emulation

1.  Install [[[media-video/pipewire]](https://packages.gentoo.org/packages/media-video/pipewire)[]] with **pipewire-alsa** and **sound-server** USE flags enabled
2.  Install [[[media-video/wireplumber]](https://packages.gentoo.org/packages/media-video/wireplumber)[]]
3.  Install [[[media-sound/pulseaudio]](https://packages.gentoo.org/packages/media-sound/pulseaudio)[]] with **-daemon** USE flag disabled
4.  Globally enable the **pulseaudio** USE flag in make.conf so that applications will use the PulseAudio API to talk to PipeWire
5.  Add your user to the pipewire group

`root `[`#`]`usermod -aG pipewire larry`

If running a minimalist desktop that does not take advantage of autostart files, add the gentoo-pipewire-launcher command to the .xinitrc file:

`user `[`$`]`nohup gentoo-pipewire-launcher restart &`

There are some audio glitches when using Firefox with PipeWire on the x13s. To fix these, either switch to PulseAudio or decrease the max-quantum as a workaround:

`user `[`$`]`pw-metadata -n settings 0 clock.max-quantum 1024`

### [Video Acceleration]

Working video acceleration requires the **qcvss8280.mbn** firmware blob. Due to legal issues this is not yet included in the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] packgae. Either copy it from the windows partition or download it from Lenovo\'s website. It\'s in [the GPU driver package](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x13s-type-21bx-21by/downloads/driver-list/component?name=Graphics%20Processing%20Units%20%28GPU%29%20and%20Server-AI%20Accelerators). The file can be extracted after unpacking with innoextract:

`user `[`$`]`innoextract n3hdr19w.exe`

1.  Place the **qcvss8280.mbn** file in the /lib/firmware/qcom/sc8280xp/LENOVO/21BX/ directory.
2.  Enable VIDEO_CARDS=\"freedreno\"
3.  Enable USE=\"vulkan zink\"
4.  Recompile everything necessary
5.  Add your user to the **video** group

[FILE] **`/etc/portage/make.conf`**

    USE="vulkan zink"
    VIDEO_CARDS="freedreno"

`root `[`#`]`emerge -uDavN @world`

`root `[`#`]`usermod -aG video larry`

This should make video acceleration work and allow a few hours extra battery life.

## [Troubleshooting]

### [f0 respawning]

With a default arm64 system, error messages like this may appear both on the default `TTY` and in the system log:

    Id "f0" respawning too fast: disabled for 5 minutes

To get rid of those, edit the `inittab` at [/etc/inittab] and remove or comment out the last line, that looks something like this:

[FILE] **`/etc/inittab`**

    # Architecture specific features
    f0:12345:respawn:/sbin/agetty 9600 ttyAMA0 vt100

Then, restart the system.

### [Clock loses time on reboot]

The default configuration may not assume a builtin RTC with a battery, so check the following config and go ahead and treat this device like a real laptop (NTP use is completely optional).

[FILE] **`/etc/conf.d/hwclock`**

    clock_hctosys="YES"
    clock_systohc="YES"

### [MAC Address changes on reboot]

For some reason the MAC address of the wireless card changes every time the system is rebooted. This can be frustrating if using Static DHCP or MAC FIltering on the local network. In order to fix this, add a udev rule to set the MAC address. Simply fill in the X\'s with the desired MAC address:

[FILE] **`/etc/udev/rules.d/99-wifi-mac.rules`**

    ACTION=="add", SUBSYSTEM=="net", KERNELS=="0006:01:00.0", RUN+="/bin/ip link set dev $name address XX:XX:XX:XX:XX:XX"

## [External resources]

-   [https://github.com/jhovold/linux/wiki/X13s](https://github.com/jhovold/linux/wiki/X13s)
-   [https://www.notebookcheck.net/Lenovo-ThinkPad-X13s-G1-Laptop-review-Introducing-the-Qualcomm-Snapdragon-8cx-Gen-3.665008.0.html](https://www.notebookcheck.net/Lenovo-ThinkPad-X13s-G1-Laptop-review-Introducing-the-Qualcomm-Snapdragon-8cx-Gen-3.665008.0.html)