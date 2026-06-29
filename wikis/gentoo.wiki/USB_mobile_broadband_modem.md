**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mobile_broadband_modem "wikipedia:Mobile broadband modem")

USB data cards, surf sticks, etc. are [USB](https://wiki.gentoo.org/wiki/USB "USB") modems to connect to UMTS (or EDGE or GSM) mobile cellular networks.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [USB_ModeSwitch]](#USB_ModeSwitch)
-   [[2] [Configuration]](#Configuration)
-   [[3] [See also]](#See_also)
    -   [[3.1] [USB 3G modem Manual configuration]](#USB_3G_modem_Manual_configuration)
-   [[4] [Configuration]](#Configuration_2)

## [Installation]

### [Prerequisites]

Set [USB](https://wiki.gentoo.org/wiki/USB "USB") and [PPP](https://wiki.gentoo.org/wiki/PPP "PPP") first.

### [Kernel]

Most device are supported by the **option** driver. You need to activate the following kernel options:

[KERNEL]

    Device drivers --->
        [*] USB support  --->
            <*>   USB Serial Converter support  --->
                  <*>   USB driver for GSM and CDMA modems

### [USB_ModeSwitch]

Most USB WiMAX dongles have a double mode. See the [USB_ModeSwitch](https://wiki.gentoo.org/wiki/USB_ModeSwitch "USB ModeSwitch") article for more information and instructions.

## [Configuration]

-   [Network management](https://wiki.gentoo.org/wiki/Network_management "Network management")

## [See also]

-   [Gnokii](https://wiki.gentoo.org/wiki/Gnokii "Gnokii") - Suite of programs for communicating with mobile phones

\

### [USB 3G modem Manual configuration]

There is a case, when the system can not detect the modem, but even when detects, the network manager can not establish connection. Then it needs additional configuration to make it working. To realize this, we need to install some software:

    wvdial
    ppp
    usb_modeswitch

## [Configuration]

for first we need to switch USB modem to work only as a modem and not as a modem+storage etc. For this case, we install usb_modeswitch

`user `[`$`]`lsusb `

and see that modem is attached to a USB and see it\'s ID. This could be like this:

** Tip**\
Bus 002 Device 006: ID 19d2:2000 ZTE WCDMA

19d2 - device 2000 - mode Then, check /dev and see that there is nothing yet named as ttyUSBx

`user `[`$`]` ls /dev `

after that, main problem is to find correct data for Your modem. Here we have some: [http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?t=383](http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?t=383) and here is a link from there to download a list of modem\'s data: [http://www.draisberghof.de/usb_modeswitch/#intro](http://www.draisberghof.de/usb_modeswitch/#intro) There You can find Your modem\'s config and copy that data info into usb_switch.conf. In this case, we took 19d2:2000 file and placed all data into usb_switch.conf

`root `[`#`]`nano /etc/usb_switch.conf `

fter that, we need to run command

`root `[`#`]`nano usb_modeswitch -Wc /etc/usb_modeswitch.conf `

This will change usb-modem into modem only mode, so then we will see in /dev directory some devices named as ttyUSB0, ttyUSB1 etc - those are what we need. Now we see that ttyUSB0, ttyUSB1 etc devices are detected:

`user `[`$`]` ls /dev `

same time, modem mode is different:

** Tip**\
Bus 002 Device 009: ID 19d2:0042 ZTE WCDMA

Means - mode has changed. Now it is modem only device: 19d:2000 become 19d2:0042. Then install wvdial

`root `[`#`]` emerge --ask wvdial `

the we run command wvdialconf to make preliminary config file. Wvdial will detect device and make preliminary setup:

`root `[`#`]` wvdialconf `

After that we open that config file and add there additional data and edit also some data it added there before. What was added by \"wvdialconf\"

`root `[`#`]` nano /etc/wvdial.conf `

    [Dialer Defaults]
    Init1 = ATZ
    Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
    Modem Type = USB Modem
    ISDN = 0
    Modem = /dev/ttyUSB2
    Baud = 9600

where

    Modem = /dev/ttyUSBx

is the device which one is Your modem. This can be different: ttyUSB1, ttyUSB0 etc - just place Your one. Now we edit wvdial.conf and place our modem specific data. Here we used MF637A ZTE modem which is conencting to Orange, so all data is that modem and provider specific. Our modem is detected as ttyUSB2 device.

`root `[`#`]` nano -w /etc/wvdial.conf `

and add next data

    [Dialer Defaults]
    Init1 = ATZ
    Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
    Modem Type = USB Modem
    ISDN = 0
    Modem = /dev/ttyUSB2
    Baud = 57600

now add dialing data. Orange provides next: calling number: \*99#, ATP = \<internet.orange\>.

    [Dialer orange3g]
    Phone = *99#
    New PPD = yes
    Username = foo
    Password = foo
    Stupid Mode = 1
    Init3 = AT+CGDCONT=1,"ip","internet.orange"

\"foo\" means - no. Username = foo, means - no user-name needs to enter. If You must enter PIN code, place this code inside also:

    [Dialer mypin]
    Init4 = AT+CPIN=1234

where 1234 - replace by Your PIN code.

To make a conenction, we use next command

`root `[`#`]` wvdial orange3g `

where \<orange3g\> is coming from

    [Dialer orange3g]

and You can replace it by anything You need to name that connection. Probably, modem can not connect at first attempts, so repeat command until it connects. During connection You will see in terminal the negotiation between modem and base station of GSM provider.

How to integrate this with NetworkManager to make automated connections? Would better to add later by other users. I do not know how to do it.