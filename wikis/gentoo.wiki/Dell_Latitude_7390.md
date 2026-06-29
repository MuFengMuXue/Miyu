\

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
-   [[3] [Device Configuration]](#Device_Configuration)
    -   [[3.1] [Firmware]](#Firmware)
        -   [[3.1.1] [Touchpad]](#Touchpad)
        -   [[3.1.2] [SD card reader]](#SD_card_reader)
        -   [[3.1.3] [Webcam]](#Webcam)
        -   [[3.1.4] [SmartCard Reader]](#SmartCard_Reader)
        -   [[3.1.5] [WWAN]](#WWAN)
            -   [[3.1.5.1] [Firmware Updates]](#Firmware_Updates)
            -   [[3.1.5.2] [Troubleshooting]](#Troubleshooting)
        -   [[3.1.6] [Kernel Config]](#Kernel_Config)
-   [[4] [See also]](#See_also)

## [Hardware]

  ---------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------------ ------------------------------------------------------------------------------------------------ ---------------- -----------------------------------
  Device           Make/model                                                                                                                                                                 Status        Vendor ID / Product ID   Kernel driver(s)                                                                                 Kernel version   Notes
  CPU              [Intel i7-8650U](https://ark.intel.com/content/www/us/en/ark/products/124968/intel-core-i7-8650u-processor-8m-cache-up-to-4-20-ghz.html)   Works         N/A                      N/A                                                                                              5.6.6
  Controller       Intel Sunrise Point-LP Serial IO I2C Controller                                                                                                                            Works                                  mfd_intel_lpss\_                                                                       5.6.6            required for touchpad
  Controller       Intel Sunrise Point-LP Thermal subsystem                                                                                                                                   Works                                  intel_pch_thermal                                                                                5.6.6
  Video            Intel UHD Graphics 620                                                                                                                                                     Works                                  i915; linux-firmware (i915/kbl_dmc_v1_04.bin, i915/kbl_guc_33.0.0.bin, i915/kbl_huc_4.0.0.bin)   5.6.6
  Audio            Intel Device 9d71                                                                                                                                                          Works                                  snd_hda_intel                                                                                    5.6.6
  Ethernet         [Intel I219-LM](https://ark.intel.com/products/82185/Intel-Ethernet-Connection-I219-LM)                                                    Works                                  e1000e                                                                                           5.6.6
  Wireless         Intel Wireless 8265 / 8275                                                                                                                                                 Works                                  [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")                                        5.6.6            linux-firmware wifi-8265-36.ucode
  WWAN             Dell DW5816E (rebadged Sierra Wireless EM7430)                                                                                                                             Works                                  cdc_mbim or qmi_wwan and qcserial                                                                5.6.13
  Touchpad         DLL07A8:01 044E:120B                                                                                                                                                       Works                                  i2c_designware\_                                                                  5.6.6            with alps/synaptics
  Touchscreen      Elan Microelectronics Touchscreen                                                                                                                                          Works         04f3:254f                usb_hid                                                                                          5.6.6
  SD Card reader   Realtek RTS525A PCI Express Card Reader                                                                                                                                    Works                                  mfd_rtsx_pci, mmc_realtek_pci                                                                    5.6.6
  Bluetooth        Intel Bluetooth controller                                                                                                                                                 Works         8087:0a2b                btusb                                                                                            5.6.6
  Webcam           Realtek Integrated Webcam HD                                                                                                                                               Works         0bda:568c                uvcvideo (usb_video_class)                                                                       5.6.6
  Smartcard        Broadcom 5880                                                                                                                                                              Not tested    0a5c:5832                app-crypt/ccid                                                                                   5.6.6
  ---------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------------ ------------------------------------------------------------------------------------------------ ---------------- -----------------------------------

## [Installation]

Installed from Xubuntu booted in EFI mode.

## [Device Configuration]

### [Firmware]

Firmware from the [Linux firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") package will be necessary:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

After emerging linux-firmware, the savedconfig file may be modified and the package re-emerged so that it only installs firmware required for the device. As an example:

[FILE] **`/etc/portage/savedconfig/sys-kernel/linux-firmware-20200421`**

    # Remove files that shall not be installed from this list.
    i915/kbl_dmc_ver1_04.bin
    i915/kbl_guc_33.0.0.bin
    i915/kbl_huc_4.0.0.bin
    intel/ibt-12-16.ddc
    intel/ibt-12-16.sfi
    iwlwifi-8265-36.ucode

In order for this change to take effect, the [savedconfig](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") USE flag must be enabled.

`root `[`#`]`echo 'sys-kernel/linux-firmware savedconfig' > /etc/portage/package.use/linux-firmware`

And re-emerge the package:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

Ensure that the Intel Wireless driver (iwlwifi) is built as a module to so that updated firmware can be found by the driver automatically.

The Intel video driver (i915) should also be built as a module for the reason listed above.

** Note**\
The i915 driver is known to cause freezes in modern (5.3+) kernels. The driver option `intel_idle.max_cstate=1` may need to be set as a kernel command line parameter as a workaround until this is fixed. This option will impact on battery life as it prevents the processor from reaching deeper idle states.

#### [Touchpad]

To enable the i2c touchpad, set the following kernel options.

[KERNEL] **Enable support for touchpad**

    Device Drivers  --->
         I2C support  --->
             I2C Hardware Bus support  --->
                  <*> Synopsys DesignWare Platform
         Multifunction device drivers  --->
                  <*> Intel Low Power Subsystem support in PCI mode
         HID support  --->
             Special HID drivers  --->
                 <*> Alps HID device support
             I2C HID support  --->
                 <*> HID over I2C transport layer

After that, the [Synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics") article can be followed.

** Note**\
Altering the acpi_osi parameter may result in touchpads being not detected and as such, not working.

#### [SD card reader]

[KERNEL] **Enable support for the SD card reader**

    Device Drivers  --->
         Multifunction device drivers  --->
             <*> Realtek PCI-E card reader
         <*> MMC/SD/SDIO card support  --->
             <*>   Realtek PCI-E SD/MMC Card Interface Driver

#### [Webcam]

[KERNEL] **Enable support for the webcam**

    Device Drivers  --->
        <*> Multimedia support  --->
            [*]   Media USB Adapters  --->.
                <*>   USB Video Class (UVC)

And add any users that need access to webcams to the video group to access the device: [/dev/video0].

`root `[`#`]`gpassword -a <user> video`

#### [SmartCard Reader]

The SmartCard reader (BCM5880) is often locked into \"CV\" mode, meaning that it is set to operate only through the Dell ControlVault2 Windows application. To unlock the reader, use the script available [here.](https://github.com/jacekkow/controlvault2-nfc-enable)

To use the reader, the ccid driver needs to be installed:

`root `[`#`]`emerge --ask app-crypt/ccid`

Once both of the above steps have been performed, the SmartCard reader should be visible using the pcsc_scan utility (sys-apps/pcsc-tools).

#### [WWAN]

Modern kernels (5.6.13+, 5.4.41+, [4.19.123+](https://cdn.kernel.org/pub/linux/kernel/v4.x/ChangeLog-4.19.123)) include support for the Dell Wireless 5816e in the cdc_mbim and qmi_wwan ethernet drivers, and the qc_serial interface driver.

To manage the WWAN card using ModemManager several kernel drivers are required:

[KERNEL] **Enable PPP**

    Device Drivers  --->
         Network Device Support  --->
             <M> PPP (point-to-point protocol) support
             <M> PPP support for sync tty ports

The WWAN card can operate in either MBIM or QMI mode, and depending on USB composition will expose the following ports:

  ------------- ------ ------ ------ -----------
  Composition   DM     NMEA   AT     Interface
  6 - QMI       Yes    Yes    Yes    QMI
  8 - MBIM      Yes    Yes    Yes    MBIM
  9 - MBIM      No     No     No     MBIM
  ------------- ------ ------ ------ -----------

AT, NMEA and DM ports are [/dev/ttyUSB] interfaces that are provided by the qcserial driver:

-   The AT port is a Hayes command set (AT command) port, and can be used to control and check the status of the modem.
    -   It is required in addition to the MBIM interface in order to establish a connection using GUI tools (Network Manager).
-   The NMEA port provides GPS NMEA strings, if enabled. The NMEA/GPS output can be enabled/disabled using AT commands.
-   The DM port is a serial diagnostic port.

The USB composition of the DW5816e can be changed using the [swi_setusbcomp.pl](https://git.mork.no/wwan.git/plain/scripts/swi_setusbcomp.pl) script as long as the cdc-wdm0 interface is exposed in either MBIM or QMI mode. This will allow exposure the interface for the desired driver.

Both the cdc_mbim and qmi_wwan drivers will provide the /dev/cdc-wdm0 device.

** Note**\
MBIM and QMI are Ethernet over USB standards with an added signalling channel:

-   MBIM is the NCM (Network Control Model) protocol with an added signalling channel.
-   QMI is the ECM (Ethernet Control Model) protocol with an added signalling channel.

ECM is an earlier standard and has some issues with latency while NCM resolves those issues and is designed for high speed operation. More information is available [here](https://en.wikipedia.org/wiki/Ethernet_over_USB#Protocols "wikipedia:Ethernet over USB").

As MBIM is the more modern standard, it\'s assumed that this is in use going forward, however it\'s entirely possible to substitute libqmi for libmbim if QMI is chosen.

Before proceeding, ensure that the following interfaces exist in /dev:

-   cdc-wdm0 (MBIM/QMI)
-   ttyUSB0 (DM)
-   ttyUSB1 (NMEA)
-   ttyUSB2 (AT)

** Note**\
NetworkManager may need to be stopped and ModemManager killed to communicate with the modem over MBIM - try it if issues are encountered communicating with the device.

To test the modem is working, insert a SIM card, install libmbim and attempt to communicate with the device:

`root `[`#`]`emerge --ask net-libs/libmbim`

`root `[`#`]`mbimcli -p -d /dev/cdc-wdm0 --query-device-caps`

If the modem is working and configured correctly, a response should be received.

mbim-network can then be used to attempt to establish a network connection. If successful, the device should be managed by NetworkManager when the service is restarted. Ensure that the network is disconnected using mbim-network before attempting to manage the device with NetworkManager.

##### [Firmware Updates]

Firmware Updates for the DW5816e are available on the [Sierra Wireless website](https://source.sierrawireless.com/resources/airprime/minicard/74xx/airprime-em_mc74xx-approved-fw-packages/#sthash.q1kO6MBw.dpbs).

The [qmi-firmware-update] utility is used to update the firmware of Sierra Wireless Qualcomm-based devices. The tool supports both MBIM and QMI drivers / interfaces. If the utility is not available, install it:

`root `[`#`]`emerge --ask net-libs/libqmi`

Determine the appropriate firmware version then download it and extract the firmware. There should be two files: a .cwe and a .nvu.

`user `[`$`]`ls`

SWI9X30C_02.33.03.00.cwe SWI9X30C_02.33.03.00_GENERIC_002.072_000.nvu SWI9X30C_02.33.03.00_Generic_002.072_000.zip

If ModemManager is running, it must be killed. If on OpenRC, stop the NetworkManager service first to prevent it from respawning:

`root `[`#`]`rc-service NetworkManager stop`

`root `[`#`]`pidof ModemManager`

4000

`root `[`#`]`kill 4000`

Finally, navigate to the directory containing your firmware files and run [qmi-firmware-update]:

`root `[`#`]`qmi-firmware-update -w /dev/cdc-wdm0 -u SWI9X30C_02.33.03.00.cwe SWI9X30C_02.33.03.00_GENERIC_002.072_000.nvu --device-open-mbim`

** Note**\
This process involves rebooting the WWAN card into QDL mode (aka Download or Boot and Hold mode). In this mode the device reports a different device ID when enumerated (81cb instead of 81cc). This device ID is not currently supported by the qcserial driver causing the firmware update to fail. The qcserial driver will need to be patched and a new kernel built before this process will complete successfully until upstream accepts the patch.

** Note**\
In the event of an unsuccessful firmware update the device may be successfully communicated with, but will be unable to connect to networks using ModemManager. If this is the case, often the device is stuck attempting to restore from low-power mode and failing due to a mismatch between configured and installed firmwares. Running \'qmicli -d /dev/cdc-wdm0 -p \--dms-list-stored-images\' may prove useful for troubleshooting, as may the flags \'\--dms-select-stored-image=, \--dms-get-firmware-preference, \--dms-list-stored-images, and \--dms-get-operating-mode\' - This utility may be used in either MBIM or QMI mode. Successfully completing the firmware update should also resolve this issue if it occurs.

##### [Troubleshooting]

The exposed AT port can be used to send AT commands to the device using minicom to assist with troubleshooting.

`root `[`#`]`emerge --ask net-dialup/minicom`

`root `[`#`]`minicom -D /dev/ttyUSB2`

Within minicom, Ctrl+A then E will enable local echo (display commands as they\'re typed).

Type ATI to get some basic device info - if communications are successful a response similar to the following should be received:

    ATI

    Manufacturer: Sierra Wireless, Incorporated
    Model: EM7430
    Revision: SWI9X30C_02.26.01.00 r7120 CARMD-EV-FRMWR2 2017/09/15 18:38:46
    MEID: 3############8
    IMEI: 3#############4
    IMEI SV: 11
    FSN: LR8##########0
    +GCAP: +CGSM

    OK

An AT command reference can be found [here](https://source.sierrawireless.com/resources/airprime/minicard/74xx/4117727-airprime-em74xx-mc74xx-at-command-reference/#sthash.XWpfbIY3.dpbs) (login required).

** Note**\
Some commands (like AT!UDUSBCOMP) that are listed in the reference do not work. It is possible that these commands require proprietary drivers to modify the USB composition via AT commands. The recommended method for changing USB composition is swi_setusbcomp.pl listed above, anyway.

#### [Kernel Config]

A working example kernel config can be found [here](https://github.com/SeanIT05/Gentoo-DELL-latitude-7390).

## [See also]

-   [Intel](https://wiki.gentoo.org/wiki/Intel "Intel")