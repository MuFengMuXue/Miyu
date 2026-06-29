## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Kernel drivers]](#Kernel_drivers)
-   [[3] [Software]](#Software)
-   [[4] [Drivers]](#Drivers)
-   [[5] [Firmware]](#Firmware)
-   [[6] [Settings via AT commands]](#Settings_via_AT_commands)
    -   [[6.1] [Set correct model PRI part number and revision after firmware flashing]](#Set_correct_model_PRI_part_number_and_revision_after_firmware_flashing)
    -   [[6.2] [Change password]](#Change_password)
-   [[7] [Internet connection]](#Internet_connection)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Firmware update not working]](#Firmware_update_not_working)
    -   [[8.2] [ModemManager crashes when attempting to connect]](#ModemManager_crashes_when_attempting_to_connect)
    -   [[8.3] [Device not working on USB 3.x port]](#Device_not_working_on_USB_3.x_port)
-   [[9] [External resources]](#External_resources)

## [Hardware]

The Sierra EM7455 is a PCIe M.2 4G LTE modem module, found in several notebooks. It can be used with an external USB adapter as a mobile broadband modem with any system. To the time of writing (Mar 2024) such a module costs only about 15 Euro on ebay and enables high-speed mobile internet, faster than most 4G USB-dongles on the market. This article focusses on the use as external modem, for the built in version also see here: [Dell_Latitude_7390#WWAN](https://wiki.gentoo.org/wiki/Dell_Latitude_7390#WWAN "Dell Latitude 7390").

## [Kernel drivers]

To make it work, the following kernel drivers (as of linux-4.9) need to be activated:

-   **PPP (point-to-point protocol) support** (` CONFIG_PPP `)
-   **PPP support for sync tty ports** (` CONFIG_PPP__SYNC_TTY `)
-   **USB Modem (CDC ACM) support** (` CONFIG_USB_ACM `)
-   **USB Wireless Device Management support** (` CONFIG_USB_WDM `)
-   **USB MBIM support** (` CONFIG_USB_NET_CDC_MBIM `)

For **rfkill**, the **Dell Laptop Extras** (` CONFIG_DELL_LAPTOP `) option might need to be enabled as well.

## [Software]

Install:

`root `[`#`]`emerge --ask net-libs/libmbim`

`root `[`#`]`emerge --ask net-libs/libqmi`

For serial communication using AT-commands:

`root `[`#`]`emerge --ask net-dialup/minicom`

## [Drivers]

The device needs qcserial module to create /dev/ttyUSB0, /dev/ttyUSB1 and /dev/ttyUSB2 for serial connection. It further needs cdc-mbim module to create /dev/cdc-wdm0 for qmi connection.

Generic version:

`user `[`$`]`lsusb -vt`

    ...
        |__ Port 012: Dev 012, If 0, Class=Vendor Specific Class, Driver=qcserial, 480M
            ID 1199:9071 Sierra Wireless, Inc. AirPrime MC7455 3G/4G LTE Modem
        |__ Port 012: Dev 012, If 2, Class=Vendor Specific Class, Driver=qcserial, 480M
            ID 1199:9071 Sierra Wireless, Inc. AirPrime MC7455 3G/4G LTE Modem
        |__ Port 012: Dev 012, If 3, Class=Vendor Specific Class, Driver=qcserial, 480M
            ID 1199:9071 Sierra Wireless, Inc. AirPrime MC7455 3G/4G LTE Modem
        |__ Port 012: Dev 012, If 12, Class=Communications, Driver=cdc_mbim, 480M
            ID 1199:9071 Sierra Wireless, Inc. AirPrime MC7455 3G/4G LTE Modem
        |__ Port 012: Dev 012, If 13, Class=CDC Data, Driver=cdc_mbim, 480M
            ID 1199:9071 Sierra Wireless, Inc. AirPrime MC7455 3G/4G LTE Modem
    ...

Branded version:

`user `[`$`]`lsusb`

    Bus 002 Device 003: ID 413c:818e Dell Computer Corp.
    ...

## [Firmware]

Download new firmware from manufacturer: [sierra website](https://source.sierrawireless.com/resources/airprime/minicard/74xx/em_mc74xx-approved-fw-packages/#sthash.Z1RNfqTe.dpbs). To flash the firmware:

`root `[`#`]`qmi-firmware-update -w /dev/cdc-wdm0 -u SWI9X30C_02.33.03.00.cwe SWI9X30C_02.33.03.00_GENERIC_002.072_000.nvu --device-open-mbim`

Make sure no other program is sending AT commands to the device meanwhile, e.g disable NetworkManager, ModemManager etc. The branding is removed when using a generic firmware.

## [Settings via AT commands]

The modem can be configured using AT commands: To send AT commands, quit any services communicating with the modem (e.g. ModemManager) and run

`root `[`#`]`minicom -b 9600 -D /dev/ttyUSB2`

then type the commands as described in the [AT command reference](https://source.sierrawireless.com/resources/airprime/minicard/74xx/4117727-airprime-em74xx-mc74xx-at-command-reference/). These can for example be used to restore factory defaults or change the branding. Just type a command and hit enter.

[CODE] **Serial console (e.g minicom)**

    ATE
    ATI

### [Set correct model PRI part number and revision after firmware flashing]

To find out part and revision number, in the directory with the firmware files, run:

`user `[`$`]`qmi-firmware-update -z SWI*.nvu`

Find the version line, looks something like this:

\[cwe 0\] version: 9999999\_**9904609**\_SWI9X30C_02.33.03.00_00_GENERIC\_**002.072**\_001

The module part number to set are the second 7 digits, the revision number are the 6 digits at the end (ignoring the last 3). Set with AT-command:

[CODE] **Serial console (e.g minicom)**

    AT!PRIID="9904609","002.072","Generic-Laptop"
    AT!RESET

### [Change password]

Sensible commands are protected by a password of up to 15 digits. Supported characters: '0'--'9', 'A'--'Z', 'a'--'z', special characters (e.g. "!#\$%&'()\*+,-./:\<\>=?@" Double quotes (") are not allowed. You can change it like this:

[CODE] **Serial console (e.g minicom)**

    AT!ENTERCND="A710"
    AT!SETCND="superpassword"
    AT!RESET

## [Internet connection]

**Important**: (Re-) Emerge NetworkManager with modemmanager USE-flag enabled and ModemManager with mbim and qmi USE-flags enabled. It will not work without these flags.

Add user to the dialout group:

`root `[`#`]`usermod -aG dialout Larry`

Find the modem number (ModemManager cli):

`user `[`$`]`mmcli -L`

Check the modem (assume number 0):

`user `[`$`]`mmcli -m 0`

If that works, use NetworkManager (NetworkManager cli): Find device, look for TYPE \'gsm\':

`root `[`#`]`nmcli device status`

Add connection with the device name you found:

`root `[`#`]`nmcli c add type gsm ifname `*`device`*` con-name `*`my-connection`*` apn internet.your-provider.com user Larry password 123`

apn, username and password can be found on the website of you service provider, if they are not correct, it will not work. Set connection up:

`root `[`#`]`nmcli c up `*`my-connection`*

That\'s it. Internet connection should work and autoconnect when the modem is plugged in.

\

## [Troubleshooting]

### [Firmware update not working]

In one terminal run minicom to send AT commands via serial:

`root `[`#`]`minicom -D /dev/ttyUSB2`

Enable advanced commands and reboot to \'boot and hold\' mode:

[CODE] **Serial console (e.g minicom)**

    AT!ENTERCND="A710"
    AT!BOOTHOLD

Immediatly run from a second terminal:

`root `[`#`]`qmi-firmware-update -t /dev/ttyUSB3 -U SWI9X30C_02.33.03.00.cwe SWI9X30C_02.33.03.00_GENERIC_002.072_001.nvu `

### [ModemManager crashes when attempting to connect]

Make sure you have built modemmanager with qmi and mbim USE-flags enabled.

### [Device not working on USB 3.x port]

Force USB 2.0 (doesn\'t slow down):

[CODE] **Serial console (e.g minicom)**

    AT!USBSPEED=0
    AT!RESET

\

## [External resources]

-   [https://www.dd-wrt.com/wiki/index.php/Mobile_Broadband#Dell](https://www.dd-wrt.com/wiki/index.php/Mobile_Broadband#Dell)
-   [https://forums.gentoo.org/viewtopic-t-1068188.html](https://forums.gentoo.org/viewtopic-t-1068188.html)
-   [https://linux-hardware.org/index.php?id=usb:413c-818e](https://linux-hardware.org/index.php?id=usb:413c-818e)
-   [https://github.com/danielewood/sierra-wireless-modems](https://github.com/danielewood/sierra-wireless-modems)
-   [https://source.sierrawireless.com/devices/em-series/em7455/](https://source.sierrawireless.com/devices/em-series/em7455/)