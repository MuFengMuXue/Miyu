**Resources**

[[]][Home](http://www.gigabyte.com/products/product-page.aspx?pid=5052)

## [Hardware]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor DRAM Controller (rev 06)
        Subsystem: CLEVO/KAPOK Computer Device 3501
    00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor PCI Express x16 Controller (rev 06)
        Kernel driver in use: pcieport
    00:02.0 VGA compatible controller: Intel Corporation 4th Gen Core Processor Integrated Graphics Controller (rev 06)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel driver in use: i915
    00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller (rev 06)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    00:14.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB xHCI (rev 05)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    00:16.0 Communication controller: Intel Corporation 8 Series/C220 Series Chipset Family MEI Controller #1 (rev 04)
        Subsystem: CLEVO/KAPOK Computer Device 3501
    00:1a.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #2 (rev 05)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel driver in use: ehci-pci
        Kernel modules: ehci_pci
    00:1b.0 Audio device: Intel Corporation 8 Series/C220 Series Chipset High Definition Audio Controller (rev 05)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    00:1c.0 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #1 (rev d5)
        Kernel driver in use: pcieport
    00:1c.2 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #3 (rev d5)
        Kernel driver in use: pcieport
    00:1c.3 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #4 (rev d5)
        Kernel driver in use: pcieport
    00:1d.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #1 (rev 05)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel driver in use: ehci-pci
        Kernel modules: ehci_pci
    00:1f.0 ISA bridge: Intel Corporation HM87 Express LPC Controller (rev 05)
        Subsystem: CLEVO/KAPOK Computer Device 3501
    00:1f.2 SATA controller: Intel Corporation 8 Series/C220 Series Chipset Family 6-port SATA Controller 1 [AHCI mode] (rev 05)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel driver in use: ahci
        Kernel modules: ahci
    00:1f.3 SMBus: Intel Corporation 8 Series/C220 Series Chipset Family SMBus Controller (rev 05)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel modules: i2c_i801
    01:00.0 3D controller: NVIDIA Corporation GM107M [GeForce GTX 860M] (rev a2)
        Subsystem: CLEVO/KAPOK Computer Device 3501
    03:00.0 Network controller: Realtek Semiconductor Co., Ltd. RTL8723BE PCIe Wireless Network Adapter
        Subsystem: Realtek Semiconductor Co., Ltd. Device b729
        Kernel driver in use: rtl8723be
        Kernel modules: rtl8723be
    04:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. Device 5287 (rev 01)
        Subsystem: CLEVO/KAPOK Computer Device 3501
    04:00.1 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 12)
        Subsystem: CLEVO/KAPOK Computer Device 3501
        Kernel driver in use: r8169
        Kernel modules: r8169

## [Kernel configuration]

[KERNEL] **Enabling evdev in the kernel**

    Device Drivers --->
      Input device support --->
      <*>  Event interface

[KERNEL] **Configuring framebuffers**

    Device Drivers --->
      Graphics support --->
        Support for frame buffer devices --->
        ## (Disable all drivers, including VGA, Intel, nVidia, and ATI)

        ## (Further down, enable basic console support. KMS uses this.)
        Console display driver support --->
          <*>  Framebuffer Console Support

[KERNEL] **Intel settings**

    Device Drivers --->
      Graphics support --->
        /dev/agpgart (AGP Support) --->
        <*>  Intel 440LX/BX/GX, I8xx and E7x05 chipset support
        Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
        <*>  Intel 8xx/9xx/G3x/G4x/HD Graphics
        [*]    Enable modesetting on intel by default

[CODE] **to add in make.conf**

    ## (For mouse, keyboard, and Synaptics touchpad support)
    INPUT_DEVICES="evdev synaptics"
    VIDEO_CARDS="intel"

[KERNEL]

    -*- Networking support  --->
      ---Networking support
        [*] Wireless  --->
            <M>   cfg80211 - wireless configuration API
            [ ]     nl80211 testmode command
            [ ]     enable developer warnings
            [ ]     cfg80211 regulatory debugging
            [*]     enable powersave by default
            [*]     cfg80211 wireless extensions compatibility
            <M>   Generic IEEE 802.11 Networking Stack (mac80211)
                  Default rate control algorithm (Minstrel)  --->
                      (x) Minstrel
            [ ]   Enable mac80211 mesh networking (pre-802.11s) support
            -*-   Enable LED triggers
            [ ]   Trace all mac80211 debug messages
            [ ]   Select mac80211 debugging features  ----

[KERNEL]

    Device Drivers  --->
        [*] Network device support  --->
            [*] Wireless LAN  --->
                Select the driver for your Wifi network device, e.g.:
                <M> Realteck rtlwifi family of devices --->
                   <M> Realteck RTL8723BE PCIe Wireless Network Adapter
                   [*] Debugging output for rtlwifi driver family

External firmware is required for the wireless card:

`root `[`#`]`emerge --ask linux-firmware`