**RTL-SDR** is a driver that enables the use of Realtek RTL2832-series based DVB-T tuners as cheap (\<\$25 USD) Software Defined Radio hardware.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Userspace]](#Userspace)
-   [[2] [Software]](#Software)

## [Installation]

### [Kernel]

RTL-SDR is incompatible with the rtl2832 kernel driver. If the driver has been built as a module it must be blacklisted:

[FILE] **`/etc/modprobe.d/blacklist.conf`**

    blacklist rtl2832

If the rtl2832 driver has been built into the kernel it must either be built as a module and blacklisted (if DVB functionality is desired), or not selected.

[KERNEL] **Disable rtl2832 driver**

    Device Drivers --->
        <*> Multimedia support --->
            [*] Customise DVB Frontends --->
                <> Realtek RTL2832 DVB-T

** Note**\
If DVB functionality is not desired it is safe to disable DVB entirely under Device Drivers \-\--\> Multimedia support

** Note**\
While the RTL-SDR driver is in use it is impossible to use the device as a DVB Tuner

### [Userspace]

Install the [[[net-wireless/rtl-sdr]](https://packages.gentoo.org/packages/net-wireless/rtl-sdr)[]] driver:

`root `[`#`]`emerge --ask net-wireless/rtl-sdr`

Create the sdr group to allow non-root users to access the device:

`root `[`#`]`groupadd sdr`

Add any users that need to access the SDR device to the sdr group:

`root `[`#`]`usermod -aG sdr larry`

** Note**\
If larry is currently logged in, he will have to log off for the group change to take effect.

Use lsusb to confirm the product and vendor IDs of the device:

`user `[`$`]`lsusb`

Bus 002 Device 002: ID 413c:81cc Dell Computer Corp.

     ...

Bus 001 Device 008: ID 0bda:2838 Realtek Semiconductor Corp. RTL2838 DVB-T

Add a udev rule to create the device [/dev/rtl_sdr]:

[FILE] **`/etc/udev/rules.d/20-rtlsdr.rules`**

    SUBSYSTEM=="usb", ATTRS=="0bda", ATTRS=="2838", GROUP="sdr", MODE="0666", SYMLINK+="rtl_sdr"

Reload and trigger your udev rules:

`root `[`#`]`udevadm control --reload-rules`

`root `[`#`]`udevadm trigger`

Plug in the device and ensure that [/dev/rdl_sdr] is created by udev.

`root `[`#`]`ls -la /dev/rtl_sdr`

lrwxrwxrwx 1 root root 15 May 11 13:32 /dev/rtl_sdr -\> bus/usb/001/007

Test the device using rtl_test.

`user `[`$`]`rtl_test`

Found 1 device(s):

     0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM Found Rafael Micro R820T tuner

     ...

User cancel, exiting\...

Samples per million lost (minimum): 0

** Note**\
If root can perform this task but larry cannot, ensure that larry is a member of the sdr group and that he has logged off and back on since he was added to it.

## [Software]

Install a package such as [[[net-wireless/gqrx]](https://packages.gentoo.org/packages/net-wireless/gqrx)[]] to gain a graphical view of the radio spectrum and easily capture tuned frequencies; see [Gqrx](https://wiki.gentoo.org/wiki/Gqrx "Gqrx") for details.

The [rtl_power] utility (installed as part of [[[net-wireless/rtl-sdr]](https://packages.gentoo.org/packages/net-wireless/rtl-sdr)[]]) can be used to scan the spectrum available to the rtl2832 device (\~64 - 1700MHz) for a period of time and output the results to a csv file. This can be converted into a waterfall graph that can be analysed to find interesting signals to investigate.

The example command below will scan from 13MHz to 1750MHz in bins of 200kHz, with a scan interval of 10 seconds for four hours:

`user `[`$`]`rtl_power -f 13M:1750M:200k -i 100 -e 4h ~/sdr_data.csv`

This can be converted to a waterfall using the script available [here](https://github.com/keenerd/rtl-sdr-misc/tree/master/heatmap).