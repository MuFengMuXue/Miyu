[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dell_XPS_17&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

The page talks about specifics of the Gentoo installation on this machine and targets on saving time for the reader on configuring these machines.

The Dell XPS at the time of writing is (2021/22) considered to be powerful workstation. Unfortunately Dell did not put much effort on making this machine friendly to Linux, therefore there are few issues with hardware user will face, which is addressed in this article.

Author bought this laptop in hope of migrating from Macbook Pro. But unfortunately price tag of dell is much higher that the apple and you have to put a lot of effort to get things to more or less ok state, therefore if you thinking of transition like this, think twice before selecting this machine. Also, forget about privacy/security - ime is by default is on on this machine and kernel have support for it :).

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Kernel]](#Kernel)
-   [[3] [DE]](#DE)
-   [[4] [Cheat sheet]](#Cheat_sheet)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Bluetooth \-- pending]](#Bluetooth_--_pending)
    -   [[5.2] [WiFi \-- fixed]](#WiFi_--_fixed)
    -   [[5.3] [Sound \-- fixed]](#Sound_--_fixed)

## [Hardware]

See below \`lspci\` output \-\-- use it as comparison against your machine. Here is also link also into the web page with greater and useful details:

[https://linux-hardware.org/?probe=597fae9cb6](https://linux-hardware.org/?probe=597fae9cb6)

     1z1-xps179710:/usr/src/linux # lspci  -k
     200:00.0 Host bridge: Intel Corporation 11th Gen Core Processor Host Bridge/DRAM Registers (rev 05)
     3        Subsystem: Dell Device 0a5d
     400:01.0 PCI bridge: Intel Corporation 11th Gen Core Processor PCIe Controller #1 (rev 05)
     5        Kernel driver in use: pcieport
     600:01.1 PCI bridge: Intel Corporation Device 9a05 (rev 05)
     7        Kernel driver in use: pcieport
     800:02.0 VGA compatible controller: Intel Corporation TigerLake-H GT1 [UHD Graphics] (rev 01)
     9        DeviceName: Onboard - Video
    10        Subsystem: Dell Device 0a5d
    11        Kernel driver in use: i915
    12        Kernel modules: i915
    1300:04.0 Signal processing controller: Intel Corporation TigerLake-LP Dynamic Tuning Processor Participant (rev 05)
    14        Subsystem: Dell Device 0a5d
    15        Kernel driver in use: proc_thermal
    16        Kernel modules: processor_thermal_device_pci_legacy
    1700:07.0 PCI bridge: Intel Corporation Tiger Lake-H Thunderbolt 4 PCI Express Root Port #0 (rev 05)
    18        Kernel driver in use: pcieport
    1900:07.1 PCI bridge: Intel Corporation Tiger Lake-H Thunderbolt 4 PCI Express Root Port #1 (rev 05)
    20        Kernel driver in use: pcieport
    2100:07.2 PCI bridge: Intel Corporation Tiger Lake-H Thunderbolt 4 PCI Express Root Port #2 (rev 05)
    22        Kernel driver in use: pcieport
    2300:07.3 PCI bridge: Intel Corporation Tiger Lake-H Thunderbolt 4 PCI Express Root Port #3 (rev 05)
    24        Kernel driver in use: pcieport
    2500:08.0 System peripheral: Intel Corporation GNA Scoring Accelerator module (rev 05)
    26        Subsystem: Dell Device 0a5d
    2700:0a.0 Signal processing controller: Intel Corporation Tigerlake Telemetry Aggregator Driver (rev 01)
    28        Subsystem: Dell Device 0a5d
    29        Kernel driver in use: intel-pmt
    30        Kernel modules: intel_pmt
    3100:0d.0 USB controller: Intel Corporation Tiger Lake-H Thunderbolt 4 USB Controller (rev 05)
    32        Subsystem: Dell Device 0a5d
    33        Kernel driver in use: xhci_hcd
    34        Kernel modules: xhci_pci
    3500:0d.2 USB controller: Intel Corporation Tiger Lake-H Thunderbolt 4 NHI #0 (rev 05)
    36        Subsystem: Dell Device 0a5d
    37        Kernel driver in use: thunderbolt
    38        Kernel modules: thunderbolt
    3900:0d.3 USB controller: Intel Corporation Tiger Lake-H Thunderbolt 4 NHI #1 (rev 05)
    40        Subsystem: Dell Device 0a5d
    41        Kernel driver in use: thunderbolt
    42        Kernel modules: thunderbolt
    4300:12.0 Serial controller: Intel Corporation Device 43fc (rev 11)
    44        Subsystem: Dell Device 0a5d
    45        Kernel driver in use: intel_ish_ipc
    46        Kernel modules: intel_ish_ipc
    4700:14.0 USB controller: Intel Corporation Tiger Lake-H USB 3.2 Gen 2x1 xHCI Host Controller (rev 11)
    48        Subsystem: Dell Device 0a5d
    49        Kernel driver in use: xhci_hcd
    50        Kernel modules: xhci_pci
    5100:14.2 RAM memory: Intel Corporation Tiger Lake-H Shared SRAM (rev 11)
    52        Subsystem: Dell Device 0a5d
    5300:14.3 Network controller: Intel Corporation Tiger Lake PCH CNVi WiFi (rev 11)
    54        Subsystem: Rivet Networks Device 1651
    55        Kernel driver in use: iwlwifi
    56        Kernel modules: iwlwifi, wl
    5700:15.0 Serial bus controller: Intel Corporation Tiger Lake-H Serial IO I2C Controller #0 (rev 11)
    58        Subsystem: Dell Device 0a5d
    59        Kernel driver in use: intel-lpss
    60        Kernel modules: intel_lpss_pci
    6100:15.1 Serial bus controller: Intel Corporation Device 43e9 (rev 11)
    62        Subsystem: Dell Device 0a5d
    63        Kernel driver in use: intel-lpss
    64        Kernel modules: intel_lpss_pci
    6500:16.0 Communication controller: Intel Corporation Tiger Lake-H Management Engine Interface (rev 11)
    66        Subsystem: Dell Device 0a5d
    67        Kernel driver in use: mei_me
    68        Kernel modules: mei_me
    6900:1c.0 PCI bridge: Intel Corporation Device 43be (rev 11)
    70        Kernel driver in use: pcieport
    7100:1f.0 ISA bridge: Intel Corporation Device 4389 (rev 11)
    72        Subsystem: Dell Device 0a5d
    7300:1f.3 Multimedia audio controller: Intel Corporation Tiger Lake-H HD Audio Controller (rev 11)
    74        Subsystem: Dell Device 0a5d
    75        Kernel driver in use: sof-audio-pci-intel-tgl
    76        Kernel modules: snd_hda_intel, snd_sof_pci_intel_tgl
    7700:1f.4 SMBus: Intel Corporation Tiger Lake-H SMBus Controller (rev 11)
    78        Subsystem: Dell Device 0a5d
    79        Kernel driver in use: i801_smbus
    80        Kernel modules: i2c_i801
    8100:1f.5 Serial bus controller: Intel Corporation Tiger Lake-H SPI Controller (rev 11)
    82        Subsystem: Dell Device 0a5d
    8301:00.0 3D controller: NVIDIA Corporation GA107M [GeForce RTX 3050 Mobile] (rev a1)
    84        Subsystem: Dell Device 0a5d
    85        Kernel modules: nouveau
    8602:00.0 Non-Volatile memory controller: Micron Technology Inc Device 5405
    87        Subsystem: Micron Technology Inc Device 0100
    88        Kernel driver in use: nvme
    89        Kernel modules: nvme
    90ab:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5260 PCI Express Card Reader (rev 01)
    91        Subsystem: Dell Device 0a5d
    92        Kernel driver in use: rtsx_pci
    93        Kernel modules: rtsx_pci

Another important thing to keep in mind - hardware and kernel is one part, in order to get the modern chips/hardware working you have to get the firmware for those chips. Having correctly configured kernel does not guarantees that you will have working hardware, i.e. bluetooth, wifi was slightly problematic to get working in this particular machine.

## [Kernel]

Please read the Gentoo wiki for the kernel, just for you to understand common things. This article addresses kernel configuration slightly differently. As you likely know configuring kernel is pretty tedious process. There are few shortcuts like using genkernel to get pretty huge kernel, however, if you are interested in configuring things on your own and have smaller/faster kernel, keep reading.

It is assumed that you booted live-cd, let\'s use loaded by your livecd modules:

    1# set to Y on current/livecd loaded modules
    2make localyesconfig

from now on many pain like WiFi etc should be resolved by setting it in the local \`.config\` from the livecd you booted. Another very helpful step would be to use ubuntu or any other distro live-cd/usb to get the kernel settings. For instance, Ubuntu have pretty good hardware detection/drivers DB, including some proprietary. You can use this advantage of the Ubuntu USB stick to get things done quickly, keep in mind though that the kernel version likely will mismatch and you will not have 100% mach on livecd and your kernel - the kernel itself evolves, so things change. Get your USB stick with ubuntu live cd and boot. Save \`lsmod\` output from your booted usb into a file

    1lsmod > ubuntu-livecd-lsmod

\

Now boot from your Gentoo USB stick or if you completed installation and need to fix/re-configure kernel

    make LSMOD=suselsmod LMC_KEEP="drivers/usb:drivers/gpu:fs" localmodconfig | sort -u
    # where `suselsmod` is suse installation kernel config, could be grabbed
    # from ubuntu as well

    # https://www.kernel.org/doc/html/latest/admin-guide/README.html?highlight=localmodconfig
    # make LSMOD=livecd-lsmod LMC_KEEP="drivers/usb:drivers/gpu:fs" localmodconfig

    # build kernel - don't use machine for few minutes
    make -j128 && make modules_install

    # install into the /boot
    make install

## [DE]

KDE will be used in this installation, steps below describes few details not covered by existing documentation. At the bottom of the article see the cheat sheet with shortened script of installation steps.

## [Cheat sheet]

[CODE] **cheatsheet**

    wiki does not allows me enter the content & save

## [Troubleshooting]

Start any troubleshooting by looking at logs:

`root `[`#`]`dmesg`

do not grep, but just read all the logs messages, you will not miss context, and can make a list of items to fix

### [Bluetooth \-- pending]

\`5.15.23\` kernel had issues loading firmware for bluetooth - the device was listed by \`rfkill\` however wasn\'t working as expected due to firmware loading issue.

### [WiFi \-- fixed]

See kernel settings

### [Sound \-- fixed]

Make sure you installed \`emerge sys-firmware/sof-firmware\` \-- there is firmware required for this sound chip to work.

\"Multimedia audio controller: Intel Corporation Tiger Lake-H HD Audio Controller\" needs codecs SND_SOC_RT1308_SDW, SND_SOC_RT711_SDW, SND_SOC_RT711_SDCA_SDW SND_SOC_RT715_SDW, and SND_SOC_RT715_SDCA_SDW in kernel config

Also requires SND_SOC_INTEL_SOUNDWIRE_SOF_MACH driver.