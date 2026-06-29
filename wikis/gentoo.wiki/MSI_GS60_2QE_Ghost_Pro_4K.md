\

## Contents

-   [[1] [Laptop Specifics]](#Laptop_Specifics)
    -   [[1.1] [lspci]](#lspci)
    -   [[1.2] [lsusb]](#lsusb)
    -   [[1.3] [lsmod]](#lsmod)
-   [[2] [Hardware Info]](#Hardware_Info)
    -   [[2.1] [Atheros Killer E220x Gigabit Ethernet Controller]](#Atheros_Killer_E220x_Gigabit_Ethernet_Controller)
    -   [[2.2] [Realtek RTS5249 PCI Express Card Reader]](#Realtek_RTS5249_PCI_Express_Card_Reader)
    -   [[2.3] [Bluetooth]](#Bluetooth)
        -   [[2.3.1] [Modify existing btusb.c file]](#Modify_existing_btusb.c_file)
    -   [[2.4] [SteelSeries Programmable Full Color Backlit Keyboard]](#SteelSeries_Programmable_Full_Color_Backlit_Keyboard)

## [Laptop Specifics]

MSI GS60 2QE Ghost Pro 4k - 079

-   Intel® Core™ i7-4710HQ 2.5GHz to 3.5GHz w/ Turbo Boost 6MB Cache
-   Intel® HM87
-   15.6\" WQHD+ 4K IPS 3840x2160 (16:9)
-   GeForce® GTX 970M 6GB GDDR5
-   SteelSeries Programmable Full Color Backlit Keyboard
-   Dynaudio Premium Speakers & Subwoofer
-   16GB DDR3L 1600MHz
-   128GB M.2 SSD x 2 RAID 0 + 1TB HDD (7200RPM)
-   LANKiller™ E2200 Game Networking
-   WLANKiller™ N1525 Wireless-AC with Bluetooth
-   Card ReaderSD (XC/HC)
-   1080p FHD Webcam
-   HDMI 1.4 x 1, mDP x 1
-   Battery Pack 6 Cell
-   Mic-in x 1, Headphone-out x 1
-   15.35\" (L) x 10.47\" (W) x 0.78\" (H)
-   4.2 lbs

\

### [lspci]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor DRAM Controller (rev 06)
    00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor PCI Express x16 Controller (rev 06)
    00:02.0 VGA compatible controller: Intel Corporation 4th Gen Core Processor Integrated Graphics Controller (rev 06)
    00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller (rev 06)
    00:14.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB xHCI (rev 05)
    00:16.0 Communication controller: Intel Corporation 8 Series/C220 Series Chipset Family MEI Controller #1 (rev 04)
    00:1a.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #2 (rev 05)
    00:1b.0 Audio device: Intel Corporation 8 Series/C220 Series Chipset High Definition Audio Controller (rev 05)
    00:1c.0 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #1 (rev d5)
    00:1c.2 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #3 (rev d5)
    00:1c.3 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #4 (rev d5)
    00:1c.4 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #5 (rev d5)
    00:1d.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #1 (rev 05)
    00:1f.0 ISA bridge: Intel Corporation HM87 Express LPC Controller (rev 05)
    00:1f.2 RAID bus controller: Intel Corporation 82801 Mobile SATA Controller [RAID mode] (rev 05)
    00:1f.3 SMBus: Intel Corporation 8 Series/C220 Series Chipset Family SMBus Controller (rev 05)
    01:00.0 3D controller: NVIDIA Corporation GM204M [GeForce GTX 970M] (rev ff)
    03:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5249 PCI Express Card Reader (rev 01)
    04:00.0 Ethernet controller: Qualcomm Atheros Killer E220x Gigabit Ethernet Controller (rev 13)
    05:00.0 Network controller: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter (rev 20)

### [lsusb]

`root `[`#`]`lsusb`

    Bus 002 Device 003: ID 1770:ff00
    Bus 002 Device 002: ID 8087:8000 Intel Corp.
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 004: ID 5986:055c Acer, Inc
    Bus 001 Device 003: ID 0cf3:3004 Atheros Communications, Inc. AR3012 Bluetooth 4.0
    Bus 001 Device 002: ID 8087:8008 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [lsmod]

`root `[`#`]`lsmod`

    mmc_block              25887  2
    rtsx_pci_sdmmc         10079  0
    rtsx_pci_ms             5010  0
    mmc_core               86950  2 mmc_block,rtsx_pci_sdmmc
    memstick                6160  1 rtsx_pci_ms
    rtsx_pci               28841  2 rtsx_pci_ms,rtsx_pci_sdmmc
    mfd_core                3177  1 rtsx_pci
    ccm                     7641  2
    uvcvideo               72059  0
    videobuf2_vmalloc       4648  1 uvcvideo
    videobuf2_memops        1783  1 videobuf2_vmalloc
    videobuf2_core         33987  1 uvcvideo
    v4l2_common             3358  1 videobuf2_core
    videodev              126553  3 uvcvideo,v4l2_common,videobuf2_core
    ath3k                   7837  0
    btusb                  27652  0
    btrtl                   3824  1 btusb
    btbcm                   5170  1 btusb
    btintel                 1313  1 btusb
    bluetooth             315253  5 ath3k,btbcm,btrtl,btusb,btintel
    bbswitch                4528  0
    snd_hda_codec_hdmi     36001  1
    snd_hda_codec_realtek    54779  1
    snd_hda_codec_generic    53728  1 snd_hda_codec_realtek
    x86_pkg_temp_thermal     4519  0
    kvm_intel             146790  0
    ath10k_pci             26573  0
    ath10k_core           172016  1 ath10k_pci
    kvm                   404662  1 kvm_intel
    msi_wmi                 2537  0
    sparse_keymap           2818  1 msi_wmi
    ath                    18475  1 ath10k_core
    joydev                  9207  0
    mac80211              480391  1 ath10k_core
    snd_hda_intel          21359  10
    snd_hda_codec          88562  4 snd_hda_codec_realtek,snd_hda_codec_hdmi,snd_hda_codec_generic,snd_hda_intel
    snd_hwdep               5690  1 snd_hda_codec
    snd_hda_core           36195  5 snd_hda_codec_realtek,snd_hda_codec_hdmi,snd_hda_codec_generic,snd_hda_codec,snd_hda_intel
    cfg80211              426882  3 ath,mac80211,ath10k_core
    snd_pcm                77395  4 snd_hda_codec_hdmi,snd_hda_codec,snd_hda_intel,snd_hda_core
    rfkill                 14015  4 cfg80211,bluetooth
    alx                    27327  0
    mdio                    2951  1 alx
    snd_timer              17993  1 snd_pcm
    snd                    56013  28 snd_hda_codec_realtek,snd_hwdep,snd_timer,snd_hda_codec_hdmi,snd_pcm,snd_hda_codec_generic,snd_hda_codec,snd_hda_intel
    soundcore               4906  1 snd
    xhci_pci                3635  0
    wmi                     7571  1 msi_wmi
    efivarfs                5355  1
    atl1c                  32826  0
    fuse                   74793  1
    usbhid                 35186  0
    xhci_hcd               99925  1 xhci_pci
    ohci_hcd               26846  0
    uhci_hcd               21091  0
    usb_storage            47023  0
    ehci_pci                3695  0
    ehci_hcd               40198  1 ehci_pci
    usbcore               156973  11 ath3k,btusb,uhci_hcd,uvcvideo,usb_storage,ohci_hcd,ehci_hcd,ehci_pci,usbhid,xhci_hcd,xhci_pci
    usb_common              1544  1 usbcore

## [Hardware Info]

### [Atheros Killer E220x Gigabit Ethernet Controller]

[KERNEL] **Ethernet: Atheros Killer E220x Gigabit Ethernet Controller**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Ethernet driver support  --->
                [*] Atheros devices
                    <M> Atheros L1C Gigabit Ethernet support
                    <M> Qualcomm Atheros AR816x/AR817x support

### [Realtek RTS5249 PCI Express Card Reader]

[KERNEL] **Card Reader: Realtek Semiconductor Co., Ltd. RTS5249 PCI Express Card Reader**

    Device Drivers  --->
        Multifunction device drivers  --->
             <M> Realtek PCI-E card reader
        <M> MMC/SD/SDIO card support  --->
             <M> MMC block device driver
             <M> Realtek PCI-E SD/MMC Card Interface Driver
        <M> Sony MemoryStick card support  --->
             <M> Realtek PCI-E Memstick Card Interface Driver

### [Bluetooth]

The Bluetooth doesn\'t work with default kernel configuration. Below changes are needed for the bluetooth to function.

#### [Modify existing btusb.c file]

`root `[`#`]`nano /usr/src/linux/drivers/bluetooth/btusb.c`

[FILE] **`/usr/src/linux/drivers/bluetooth/btusb.c`**

    Find section "static const struct usb_device_id blacklist_table[] = ,

    Remove from /* Atheros 3012 with sflash firmware */

    ,

Rebuild the kernel after the change.

### [SteelSeries Programmable Full Color Backlit Keyboard]

Control the LED colors of the SteelSeries programmable full color backlit keyboard.

`root `[`#`]`emerge -av net-libs/nodejs`

Clone and install the utility:

`user `[`$`]`git clone `[`https://github.com/wearefractal/msi-keyboard.git`](https://github.com/wearefractal/msi-keyboard.git)

`user `[`$`]`cd msi-keyboard`

`user `[`$`]`npm install`

Run the example:

`user `[`$`]`cd examples`

`user `[`$`]`node sample.js`