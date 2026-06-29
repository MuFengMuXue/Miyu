This guide is for Huawei Mobile Broadband E367 HSPA+ USB Rotator. This method should also work for many other huawei 3G adapters (E175 & E353 & E363 for example?).

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Install]](#Install)
-   [[3] [Configure]](#Configure)
-   [[4] [Run]](#Run)
-   [[5] [Connecting]](#Connecting)
-   [[6] [net-misc/netifrc config]](#net-misc.2Fnetifrc_config)
    -   [[6.1] [MTN South Africa]](#MTN_South_Africa)
-   [[7] [app-mobilephone/gnokii]](#app-mobilephone.2Fgnokii)
-   [[8] [gsm-ussd]](#gsm-ussd)

## [Kernel]

usbserial needs to be built to your kernel or as a module:

`root `[`#`]`modprobe usbserial`

## [Install]

`root `[`#`]`emerge --ask sys-apps/usb_modeswitch`

## [Configure]

Add the following to the bottom of the config file.

[FILE] **`/etc/usb_modeswitch.conf`**

    # Huawei E367
    DefaultVendor=0x12d1
    DefaultProduct=0x1446

    TargetVendor=0x12d1
    TargetProductList="1001,1406,140b,140c,1412,141b,14ac,1506"

    CheckSuccess=20

    MessageEndpoint=0x01
    MessageContent="55534243123456780000000000000011062000000100000000000000000000"

## [Run]

`root `[`#`]`usb_modeswitch -c /etc/usb_modeswitch.conf`

    Looking for default devices ...
       found matching product ID
       adding device
     Found device in default mode, class or configuration (1)
    Accessing device 002 on bus 002 ...
    Getting the current device configuration ...
     OK, got current device configuration (1)
    Using first interface: 0x00
    Using endpoints 0x01 (out) and 0x81 (in)
    Inquiring device details; driver will be detached ...
    Looking for active driver ...
     No driver found. Either detached before or never attached

    SCSI inquiry data (for identification)
    -------------------------
      Vendor String: HUAWEI
       Model String: Mass Storage
    Revision String: 2.31
    -------------------------

    USB description data (for identification)
    -------------------------
    Manufacturer: Huawei Technologies
         Product: HUAWEI Mobile
      Serial No.: not provided
    -------------------------
    Setting up communication with interface 0
    Using endpoint 0x01 for message sending ...
    Trying to send message 1 to endpoint 0x01 ...
     OK, message successfully sent
    Resetting response endpoint 0x81
    Resetting message endpoint 0x01
     Device is gone, skipping any further commands

    Checking for mode switch (max. 20 times, once per second) ...
     (For a better success check provide target IDs or class)
     Original device vanished after switching

    Mode switch most likely succeeded. Bye.

The modem shows up a different output in lsusb after running usb_modeswitch.

Before running usb_modeswitch :

`root `[`#`]`lsusb`

Bus 001 Device 005: ID 12d1:1446 Huawei Technologies Co., Ltd. E1552/E1800 (HSPA modem)

After running usb_modeswitch :

`root `[`#`]`lsusb`

Bus 002 Device 003: ID 12d1:1506 Huawei Technologies Co., Ltd. E398 LTE/UMTS/GSM Modem/Networkcard

## [Connecting]

Now you should have three device nodes:

`root `[`#`]`ls /dev/ttyUSB*`

/dev/ttyUSB0 /dev/ttyUSB1 /dev/ttyUSB2

The modem should be [/dev/ttyUSB2]. You can now connect to internet using wvdial or [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager").

## [][net-misc/netifrc config]

### [MTN South Africa]

This is for mtn.co.za. APN is `internet`.

`user `[`$`]`ls -l /dev/serial/by-id/usb-HUAWEI_HUAWEI_Mobile-if??-port0`

    lrwxrwxrwx 1 root root 13 Mar  1 13:20 /dev/serial/by-id/usb-HUAWEI_HUAWEI_Mobile-if00-port0 -> ../../ttyUSB0
    lrwxrwxrwx 1 root root 13 Mar  1 13:20 /dev/serial/by-id/usb-HUAWEI_HUAWEI_Mobile-if02-port0 -> ../../ttyUSB1
    lrwxrwxrwx 1 root root 13 Mar  1 13:20 /dev/serial/by-id/usb-HUAWEI_HUAWEI_Mobile-if03-port0 -> ../../ttyUSB2

`user `[`$`]`gnokii --config /etc/gnokiirc-huawei_e367 --getnetworkinfo`

    GNOKII Version 0.6.29
    Network      : MTN / Mobile Telephone Networks (South Africa)
    Network code : 655 10
    LAC          : 0000 (0)
    Cell id      : 00000000 (0)

[FILE] **`/etc/init.d/net`**

    ## /dev/serial/by-id/usb-HUAWEI_HUAWEI_Mobile-if??-port0
    dns_servers_ppp1="8.8.8.8 8.8.4.4"
    config_ppp1="ppp"
    link_ppp1="/dev/serial/by-id/usb-HUAWEI_HUAWEI_Mobile-if00-port0"
    username_ppp1="guest"
    password_ppp1=""
    pppd_ppp1="lock noipdefault defaultroute defaultmetric 10000 noauth 460800"
    phone_number_ppp1="*99#"
    chat_ppp1="
       'ABORT' 'BUSY'
       'ABORT' 'ERROR'
       'ABORT' 'NO ANSWER'
       'ABORT' 'NO CARRIER'
       'ABORT' 'NO DIALTONE'
       'ABORT' 'Invalid Login'
       'ABORT' 'Login incorrect'
       'TIMEOUT' '10'
       '' 'ATZ'
       'OK' 'AT+CPIN?'
       'READY-AT+CPIN=1234\r\n\d\d\d\d\d-OK' 'ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0'
       'OK' 'AT+CGDCONT=1,\\\"IP\\\",\\\"internet\\\"'
       'OK' 'ATDT\T'
       'CONNECT' ''
       '~--' ''
    "

## [][app-mobilephone/gnokii]

[FILE] **`gnokiirc-huawei_e367`**

    [global]
    model = AT
    port = /dev/ttyUSB2
    connection = serial
    use_locking = yes
    #serial_baudrate = 460800
    serial_baudrate = 19200

`user `[`$`]`gnokii --config /etc/gnokiirc-huawei_e367 --identify`

    GNOKII Version 0.6.29
    IMEI         : 356793040724668
    Manufacturer : huawei
    Model        : E353
    Product name : E353
    Revision     : 21.137.01.00.864

\

[FILE] **`gsms`**

    #!/bin/bash

    device="huawei_e367"
    config_file=~/etc/gnokiirc-$
    gnokii="gnokii --config $"
    pin=1234
    output_file=~/gnokii-$-getsms

    # Check if phone is PIN locked
    if $ --getsecuritycodestatus

## [gsm-ussd]

[gsm-ussd site](http://linux.zum-quadrat.de/downloads/)

-   `*123*888#` is for MTN South Africa and it returns your MSISDN.

`user `[`$`]`gsm-ussd --no-cleartext -m /dev/ttyUSB2 '*123*888#'`

    Yello! Your MSISDN is 2783XXXXXXX

-   `*141*1#` is for MTN South Africa and it returns your balance.

`user `[`$`]`gsm-ussd --no-cleartext -m /dev/ttyUSB2 '*141*1#'`

    You have RXXXX.XX airtime, XXXX SMS and XXXX.XX MB of data. For detailed balances dial *141*1#.