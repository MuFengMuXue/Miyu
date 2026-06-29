**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/WiMAX "wikipedia:WiMAX")

The **WiMAX** (**Worldwide Interoperability for Microwave Access**) system provides users mobile broadband Internet using the 2G and 3G networks. This article explains the setup of WiMAX USB dongles.

## Contents

-   [[1] [Supported hardware]](#Supported_hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Prerequisites]](#Prerequisites)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [USB_ModeSwitch]](#USB_ModeSwitch)
-   [[3] [Configuration]](#Configuration)

## [Supported hardware]

This workflow is tested on the following hardware:

  ----------------- ---------------------------------------- ----------------- -----------------
  Manufacturer      Model                                    USB IDs           Works?

  Alcatel           One Touch X220L                          1bbb:f000\        Yes
                                                             1bbb:0017

  Intel             Intel Corporation WiMAX/WiFi Link 5150   8086:423d         Yes
  ----------------- ---------------------------------------- ----------------- -----------------

** Note**\
Please update this if you have tested it on other hardware.

## [Installation]

### [Prerequisites]

Set [PPP](https://wiki.gentoo.org/wiki/PPP "PPP") first.

### [Kernel]

You need to activate the following kernel options:

[KERNEL]

    Networking support --->
        [*] WiMAX Wireless Broadband support
    Device drivers --->
        [*] Network device support
            WiMMAX broadband devices --->
                <*> Intel Wireless WiMAX Connection 2400 over USB
            USB Network adapters --->
                <*> Option USB High Speed Mobile Devices

### [USB_ModeSwitch]

Most USB WiMAX dongles have a double mode. See the [USB_ModeSwitch](https://wiki.gentoo.org/wiki/USB_ModeSwitch "USB ModeSwitch") article for more information and instructions.

## [Configuration]

-   [Network management](https://wiki.gentoo.org/wiki/Network_management "Network management")