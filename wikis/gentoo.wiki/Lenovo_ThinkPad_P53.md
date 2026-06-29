**Resources**

[[]][Product Information](https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadp/p53/22ws2wpwp53)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-p-series-laptops/thinkpad-p53-type-20qn-20qq)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P53/ThinkPad_P53_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_P53)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/p53_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/p53_user_guide_fedora.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad P series](https://en.wikipedia.org/wiki/ThinkPad_P_series "wikipedia:ThinkPad P series")

Installing Linux to Thinkpads is mostly easy. Even more so, since Lenovo started official support for Linux on a number of systems.^[\[1\]](#cite_note-1)^

The installation using a Gentoo installation media works perfectly as described [in the Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation "Handbook:AMD64/Full/Installation").

Almost all of the P53 hardware is supported in kernel or by installing additional drivers from Portage. Due to the muxed GPU hardware and the decent IOMMU layout of the P53, this laptop is also a good candidate for advanced configurations like GPU passthrough in QEMU.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [System Model Verfication]](#System_Model_Verfication)
    -   [[1.2] [Lenovo ThinkPad P53]](#Lenovo_ThinkPad_P53)
    -   [[1.3] [Accessories]](#Accessories)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [CPU]](#CPU)
    -   [[2.2] [Power]](#Power)
    -   [[2.3] [Hardware monitoring]](#Hardware_monitoring)
    -   [[2.4] [Networking]](#Networking)
    -   [[2.5] [Bluetooth]](#Bluetooth)
    -   [[2.6] [Storage]](#Storage)
    -   [[2.7] [Graphics]](#Graphics)
        -   [[2.7.1] [Intel Firmware]](#Intel_Firmware)
        -   [[2.7.2] [Nvidia Drivers]](#Nvidia_Drivers)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Hardware]

### [System Model Verfication]

`root `[`#`]`dmidecode -s system-version`

    ThinkPad P53

### [Lenovo ThinkPad P53]

  ----------------------- ---------------------------- -------- --------- ------------------ ----------------------
  Device                  Make/model                   Status   Bus ID    Kernel driver(s)   Notes
  CPU                     Intel i7-9750H series        Works    N/A       mcore2             None
  Ethernet                Intel I219-V                 Works    00:1f.6   e1000e             None
  WiFi                    Intel Wi-Fi 6 AX200          Works    52:00.0   iwlwifi            None
  Bluetooth               Intel Wireless Bluetooth     Works    N/A       btusb              None
  Touchpad                SynPS/2 Synaptics TouchPad   Works    N/A       synaptics          None
  SD Card Reader          RTS525A                      Works    54:00.0   rtsx_pci           None
  Integrated Video card   Intel UHD 630                Works    00:02.0   intel i965         None
  Second Video card       NVIDIA Quadro T2000M         Works    01:00.0   N/A                Needs Nvidia drivers
  ----------------------- ---------------------------- -------- --------- ------------------ ----------------------

### [Accessories]

  ----------------- ----------------------------- -------- -------- ------------------ --------------------------------------------------------------
  Device            Make/model                    Status   Bus ID   Kernel driver(s)   Notes
  Docking Station   Thinkpad Thunderbold 3 Dock   Works    N/A      hotplug_pci_acpi   Using LAN over Thunderbold does not work great all the time.
  ----------------- ----------------------------- -------- -------- ------------------ --------------------------------------------------------------

## [Configuration]

### [CPU]

It is recommended to enable the microcode update support as explained in [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode").

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    Processor type and features  --->
      Processor family (Generic-x86-64)
      [*] CPU microcode loading support
      [*]   Intel microcode loading support

### [Power]

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  --->
        <*> AC Adapter
        <*> Battery
        <*> Button
        <*> Video
        <*> Fan
        <*> Dock
    CPU Frequency scaling  --->
        <*> CPU Frequency Transition Statistics
        Default CPUFreq governor (performance)
        <*> 'performance' governor
        <*> 'powersave' governor
        [*] Intel P state control

### [Hardware monitoring]

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    Device Drivers  --->
      [*] X86 Platform Specific Device Drivers  --->
        <*> ThinkPad ACPI Laptop Extras
       Hardware Monitoring Support  --->
        <*> Intel Core/Core2/Atom temperature sensor

### [Networking]

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    Networking support  --->
      <*> Wireless  --->
        <*> cfg80211 - wireless configuration API -->
          <*> cfg80211 - wireless extensions compatability
        <*> Generic IEEE 802.11 Networking Stack (mac80211)
      <*> RF switch subsystem support
    Device Drivers  --->
      [*] Network device support  --->
        [*] Ethernet driver support  --->
          [*] Intel devices
            <*> Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support
          [*] Wireless LAN  --->
            [*] Intel devices
              <M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
              <M> Intel Wireless WiFi DVM Firmware support
              <M> Intel Wireless WiFi MVM Firmware support

### [Bluetooth]

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    Networking support  --->
      Bluetooth subsystem support  --->
        Bluetooth device drivers  --->
          <*> HCI USB driver
    Device Drivers  --->
      Generic Driver Options  --->
        Firmware Loader  --->
          intel/ibt-20-1-3.sfi intel/ibt-20-1-3.ddc

It is recommended to globally enable the `bluetooth` USE Flag in order to make use of this feature it in your system and software.

### [Storage]

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    Device Drivers --->
       NVME Support --->
         <*> NVM Express block device

### [Graphics]

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    Device Drivers  --->
      Graphics support  --->
        [*] Laptop Hybrid Graphics - GPU switching support
        <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
        < > Nouveau (NVIDIA) cards
        <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
      X86 Platform Specific Device Drivers  --->
        <*> WMI
          <M> WMI support for MXM Laptop Graphics
        <*> ThinkPad ACPI Laptop Extras
          [*] Video output control support

#### [Intel Firmware]

You may also want to include the propretary DMC firmware for the GPU.

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    Device Drivers  --->
      Generic Driver Options  --->
        Firmware Loader  --->
          i915/kbl_dmc_ver1_04.bin

#### [Nvidia Drivers]

In order to make use of the more powerful Nvidia card, you\'ll need to install the propretary drivers.

`root `[`#`]`emerge nvidia-drivers`

## [See also]

-   [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") --- The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package contains the *proprietary* graphics driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.
-   [NVIDIA/Optimus](https://wiki.gentoo.org/wiki/NVIDIA/Optimus "NVIDIA/Optimus") --- a proprietary technology that seamlessly switches between two GPUs.
-   [NVIDIA/Bumblebee](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee") --- an open source implementation of [NVIDIA Optimus](https://wiki.gentoo.org/wiki/NVIDIA/Optimus "NVIDIA/Optimus").
-   [Lenovo ThinkPad P50](https://wiki.gentoo.org/wiki/Lenovo_ThinkPad_P50 "Lenovo ThinkPad P50")
-   [Lenovo ThinkPad P52](https://wiki.gentoo.org/wiki/Lenovo_ThinkPad_P52 "Lenovo ThinkPad P52")

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_P53](https://wiki.archlinux.org/title/Lenovo_ThinkPad_P53)

## [References]

1.  [[[↑](#cite_ref-1)] [[Lenovo Launches Linux-Ready ThinkPad and ThinkStation PCs Preinstalled with Ubuntu](https://news.lenovo.com/pressroom/press-releases/lenovo-launches-linux-ready-thinkpad-and-thinkstation-pcs-preinstalled-with-ubuntu/), accessed 12th Sep 2021]]