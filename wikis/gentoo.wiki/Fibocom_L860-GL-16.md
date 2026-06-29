[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Fibocom_L860-GL-16&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Fibocom L860-GL-16 is a M.2 PCIe Wireless Wide Area Network (WWAN) module, which shipped with Lenovo devices.

## Contents

-   [[1] [Preface]](#Preface)
-   [[2] [Is my modem FCC locked?]](#Is_my_modem_FCC_locked.3F)
-   [[3] [Update process]](#Update_process)
    -   [[3.1] [Prepare environment]](#Prepare_environment)
        -   [[3.1.1] [Downloading]](#Downloading)
        -   [[3.1.2] [Unpacking]](#Unpacking)
        -   [[3.1.3] [Flashing]](#Flashing)
-   [[4] [Unlocking]](#Unlocking)
-   [[5] [Kernel configuration]](#Kernel_configuration)
-   [[6] [ModemManager Support]](#ModemManager_Support)

## [Preface]

Lenovo and Government care about people around world and make two things for that:

-   Whitelist WWAN modules in BIOS (be aware, modules from one laptop generation van be forbidden on another one, I found that between L14 Gen3 and L14 Gen4 for example)
-   Apply FCC locking

That means - you can not just plug your equipment into the laptop and go. You should unlock it before using. I did try to use unlocking tool, shipped from Lenovo, but it did not work properly. Of course you can try by yourself and update this wiki page, if you\'re successful.

Before continuing, I strongly recommended to update your modem to the last available firmware version (it was 18601.5001.00.01.17.30_GC). Assuming that you have only one modem at index 0, you can identify the firmware version with

`root `[`#`]`mmcli -m 0`

## [][Is my modem FCC locked?]

Example of a modem, that is already unlocked:

`root `[`#`]`echo 'AT+CFUN?' | socat - /dev/wwan0at1,crnl`

    +CFUN: 4,0

    OK

Example of a modem, that is still locked:

`root `[`#`]`echo 'AT+CFUN?' | socat - /dev/wwan0at1,crnl`

    ERROR

Read more at [https://modemmanager.org/docs/modemmanager/fcc-unlock/](https://modemmanager.org/docs/modemmanager/fcc-unlock/)

## [Update process]

Before start you should have any WWAN card to USB adapter, because updater software supports only USB connection. You can find it on Amazon and Ebay. Plug your modem to this adapter and check for ttyACM in /dev directory and dmesg output after plugging USB.

### [Prepare environment]

All procedure will be followed in /tmp/t directory, you can adjust it for you own solution.

#### [Downloading]

-   DEB file from [Intel Platform Flash Tool Lite](https://github.com/projectceladon/tools)
-   Last firmware for your Laptop from Lenovo [L14 Gen 4 WWAN for example](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-l-series-laptops/thinkpad-l14-gen-4-type-21h5-21h6/downloads/driver-list/component?name=Networking%3A%20Wireless%20WAN&id=49B19606-BEF8-41DD-BE7F-95B570C212C8)

#### [Unpacking]

Unpack and place downloadTool from intel

`root `[`#`]`cd /tmp/t`

`root `[`#`]`ar x platformflashtoollite_5.8.9.0_linux_x86_64.deb`

`root `[`#`]`tar -xvf data.tar.gz`

`root `[`#`]`cp ./opt/intel/platformflashtoollite/bin/downloadTool /usr/local/bin/`

`root `[`#`]`cp ./opt/intel/platformflashtoollite/lib/libDownloadTool.so /usr/local/lib64/`

Unpack firmware from Lenovo

`root `[`#`]`innoextract nyafg03w.exe`

`root `[`#`]`cp 'code$GetExtractPath$/FwUpdateDriver/M2_7560_NAND.flz' .`

`root `[`#`]`rm -rf 'code$GetExtractPath$/'`

`root `[`#`]`unzip M2_7560_NAND.flz`

`root `[`#`]`unzip L860_Secureboot.zip`

#### [Flashing]

Before flashing you should unplug your device and run downloadTool with some magic arguments

`root `[`#`]`downloadTool -v 4 -c 1 --library /usr/local/lib64/libDownloadTool.so PSI_flash/18601.5001.00.01.17.30/18601.5001.00.01.17.30_PSI_FLASH_86511CF8.fls Devicepack/18601.5001.00.01.17.30/LENOVO_cust.5003.14_signed.fls 18601.5001.00.01.17.30_Secureboot.fls row_cust.001.012_signed.fls`

Be aware with 18601.5001.00.01.17.30_PSI_FLASH_86511CF8.fls firmware part. There are a lot of PSI files in the bundle and you should choose the right one for your own equipment. If you choose the wrong one, the notebook will tell you YOUR DEVICE IS NOT WHITELISTED when you plug it into the M.2 slot.

When downloadTool asks about powercycle of your device - just plug it to USB and all should be fine (or not) After flashing you can try to place your device to Laptop. If you got whitelist error - try another one PSI file.

\

## [Unlocking]

Lenovo ships some fcc unlock tool for Ubuntu, but this solution did not work in my own case. I found some workaround in the Internet, but it\'s no silver bullet. Use it at your own risk.

Checkout and build the third party fcc unlocking tool for modem [here](https://github.com/xmm7360/xmm7360-usb-modeswitch/tree/master/fcc_unlock). The process is very simple

`root `[`#`]`cd /tmp/t`

`root `[`#`]`rm -rf *`

`root `[`#`]`git clone `[`https://github.com/xmm7360/xmm7360-usb-modeswitch`](https://github.com/xmm7360/xmm7360-usb-modeswitch)

`root `[`#`]`cd xmm7360-usb-modeswitch/fcc_unlock`

`root `[`#`]`touch sha-256.h`

`root `[`#`]`make`

`root `[`#`]`cp fcc_unlcok /usr/local/bin/`

** Note**\
The Fibocom L860-GL-16 is actually Intel Corporation **XMM7560** LTE Advanced Pro Modem. Above repository is named after XMM7**3**60 though.

At the present moment you can try to unlock your modem (command can fail, just run it again and again and again, it\'ll successful or your modem completely hungs you should reboot your Laptop):

`root `[`#`]`./fcc_unlock`

    lock mode: 2 state: 0
    lock challenge present: 1 challenge: fc71aea3
    resp: a3 ae 71 fc 3d f8 c7 19
     00 00 00 00 00 00 00 00
    success
    successss
    switch states: hw 1, sw 1

After that I wrote some wrapper for unlocking:

[FILE] **`/usr/local/fcc_unlock_wrapper`**

    #!/bin/bash

    OUTPUT="/dev/wwan0at0,crnl"

    /usr/local/bin/fcc_unlock

    sleep 5

    echo 'at@nvm:fix_cat_fcclock.fcclock_mode?' | socat - $
    echo 'at@nvm:fix_cat_fcclock.fcclock_mode=0' | socat - $
    echo 'at@store_nvm(fix_cat_fcclock)' | socat - $
    echo 'AT+CFUN?' | socat - $
    echo 'AT+CFUN=1,0' | socat - $

If unlocking process will be successful you should restart ModemManager and after few seconds your device appeared in unlocked state:

`root `[`#`]`mmcli -m 0`

      ----------------------------------
      General  |                   path: /org/freedesktop/ModemManager1/Modem/0
               |              device id: a2cac38a8c491eefac5507b04f17c590dd6a717d
      ----------------------------------
      Hardware |           manufacturer: generic
               |                  model: MBIM [8086:7560]
               |      firmware revision: 18601.5001.00.01.17.30_GC
               |           h/w revision: V1.3
               |              supported: gsm-umts, lte
               |                current: gsm-umts, lte
               |           equipment id: XXXXXXXXXXXXXXX
      ----------------------------------
      System   |                 device: /sys/devices/pci0000:00/0000:00:02.5/0000:05:00.0
               |                drivers: iosm
               |                 plugin: generic
               |           primary port: wwan0mbim0
               |                  ports: wwan0 (net), wwan0at0 (at), wwan0at1 (at), wwan0mbim0 (mbim)
      ----------------------------------
      Status   |         unlock retries: sim-pin (3)
               |                  state: registered
               |            power state: on
               |            access tech: lte
               |         signal quality: 29% (recent)
      ----------------------------------
      Modes    |              supported: allowed: 3g, 4g; preferred: none
               |                current: allowed: 3g, 4g; preferred: none
      ----------------------------------
      IP       |              supported: ipv4, ipv6, ipv4v6
      ----------------------------------
      3GPP     |                   imei: XXXXXXXXXXXXXXX
               |          enabled locks: fixed-dialing
               |            operator id: 24802
               |          operator name: Elisa EE
               |           registration: home
      ----------------------------------
      3GPP EPS |   ue mode of operation: csps-2
               |    initial bearer path: /org/freedesktop/ModemManager1/Bearer/0
               | initial bearer ip type: ipv4v6
      ----------------------------------
      SIM      |       primary sim path: /org/freedesktop/ModemManager1/SIM/0
               |         sim slot paths: slot 1: /org/freedesktop/ModemManager1/SIM/0 (active)
               |                         slot 2: /org/freedesktop/ModemManager1/SIM/1

## [Kernel configuration]

In my own case modem uses iosm driver

`root `[`#`]`lspci -vv`

    05:00.0 Wireless controller [0d40]: Intel Corporation XMM7560 LTE Advanced Pro Modem (rev 01)
            Subsystem: Device 1cf8:8651
            Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
            Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
            Latency: 0, Cache Line Size: 32 bytes
            Interrupt: pin A routed to IRQ 57
            IOMMU group: 14
            Region 0: Memory at fd500000 (64-bit, non-prefetchable) [size=4K]
            Region 2: Memory at fd501000 (64-bit, non-prefetchable) [size=256]
            Capabilities: [40] Power Management version 3
                    Flags: PMEClk- DSI- D1- D2- AuxCurrent=375mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
                    Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
            Capabilities: [50] MSI: Enable+ Count=1/4 Maskable- 64bit+
                    Address: 00000000fee03000  Data: 0022
            Capabilities: [70] Express (v2) Endpoint, MSI 00
                    DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s unlimited, L1 unlimited
                            ExtTag- AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 75W
                    DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                            RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop-
                            MaxPayload 256 bytes, MaxReadReq 128 bytes
                    DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr+ TransPend-
                    LnkCap: Port #0, Speed 5GT/s, Width x1, ASPM L1, Exit Latency L1 <1us
                            ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                    LnkCtl: ASPM L1 Enabled; RCB 64 bytes, Disabled- CommClk+
                            ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                    LnkSta: Speed 5GT/s, Width x1
                            TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                    DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                             10BitTagComp- 10BitTagReq- OBFF Not Supported, ExtFmt- EETLPPrefix-
                             EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                             FRS- TPHComp- ExtTPHComp-
                             AtomicOpsCap: 32bit- 64bit- 128bitCAS-
                    DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR+ 10BitTagReq- OBFF Disabled,
                             AtomicOpsCtl: ReqEn-
                    LnkCap2: Supported Link Speeds: 2.5-5GT/s, Crosslink- Retimer- 2Retimers- DRS-
                    LnkCtl2: Target Link Speed: 5GT/s, EnterCompliance- SpeedDis-
                             Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                             Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
                    LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                             EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                             Retimer- 2Retimers- CrosslinkRes: unsupported
            Capabilities: [100 v2] Advanced Error Reporting
                    UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                    CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
                    CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
                    AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                            MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
                    HeaderLog: 00000000 00000000 00000000 00000000
            Capabilities: [148 v1] Latency Tolerance Reporting
                    Max snoop latency: 1048576ns
                    Max no snoop latency: 1048576ns
            Capabilities: [150 v1] L1 PM Substates
                    L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                              PortCommonModeRestoreTime=10us PortTPowerOnTime=10us
                    L1SubCtl1: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+
                               T_CommonMode=0us LTR1.2_Threshold=166912ns
                    L1SubCtl2: T_PwrOn=150us
            Capabilities: [d00 v1] Vendor Specific Information: ID=0024 Rev=1 Len=0a0 <?>
            Kernel driver in use: iosm

\

## [ModemManager Support]

Merge request for XMM 7**3**60 in Modem Manager [https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/merge_requests/1200](https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/merge_requests/1200)

Merge request for XMM 7560 FCC unlocking script [https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/merge_requests/1141](https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/merge_requests/1141)