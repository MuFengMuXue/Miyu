# MacBookPro9,x

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Microphone ||  ||
|-
| SD-card reader ||  ||
|-
| IR Receiver ||  ||
|-
| Thunderbolt ||  ||
|}

This page covers the following Apple models:

* MacBookPro9,1 15" Mid-2012
* MacBookPro9,2 13" Mid-2012

## Installation
After booting the installation image, Ethernet works, but not Wi-Fi. To fix this, remove the  kernel module and load . This is because the b43 firmware files are not on the installation image.

 # rmmod b43 bcma ssb wl
 # modprobe wl
 # ip link set wlan0 down
 # ip link set wlan0 up

## Wi-Fi
Wi-Fi does not work out of the box. Install  or . See Broadcom wireless. In the past it was reported to be flaky, and fixed with ConnMan.

## SD-card reader
The SD-card reader works, with occasional failures due to a bug. The maximum card speed is 22 MB/s always. In the past it was recommended to use the following kernel parameter, however this seems to have no change in behavior.

 sdhci.debug_quirks2=4

## Function keys
See Apple Keyboard to adjust the function keys.

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|}

## Touchpad
The touchpad works out of the box. In the past, it was recommended to use .

## Using synclient
 is included with the  driver. It is useful for experimenting with settings as they take effect immediately and expire at the end of an X session. Many macOS options can be emulated without any additional software.

Run  to have a look at all the available options. Here are some suggestions which resemble the options found in macOS's System Preferences:

* By default synaptics is configured to use a double-tap drag gesture found on older touchpads - one may argue that this is not necessary on a clickpad.  will turn this off.
* TapButtonX and ClickFingerX sets the mouse button triggered by tapping or clicking with X fingers. set  and  to assign two-finger click to the right mouse button.
* Setting the bottom-right corner click to right mouse button can be done by subtracting about 500 from  and  and plugging the new values into  and . If the last two options are not visible, set .

To make settings permanent, just modify .
