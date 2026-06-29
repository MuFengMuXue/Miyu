# Lenovo ThinkPad X1 Carbon

Lenovo ThinkPad X1 Carbon (X1C).
There is also a touch version. Comes without optical drive.
Has UEFI BIOS with BIOS-legacy fallback mode.

## Booting
## Legacy-BIOS
Boot into your BIOS and change the boot mode to Legacy. Then simply follow the normal installation guide.

## Hanging on "HWP enabled" message
This is due to a bug introduced in Linux 4.4. To work around it, add  to your kernel parameters.

## Hardware
Almost everything works out of the box.

## Audio
Sound works out of the box.

## Xbindkeys
For alternative window managers (Fluxbox, etc..), try installing xbindkeys and adding the following to :

 "amixer -c 0 set Master 1dB-"
   XF86AudioLowerVolume
 "amixer -c 0 set Master 1dB+"
   XF86AudioRaiseVolume

## Network
Wired networking works out of the box with the Ethernet to USB adapter. Wireless works out of the box using the  module.

## Touchscreen
Works out of the box. To enable multi-touch, install Touchegg.

## Video
The video card installed is Intel HD Graphics 4000. See intel for more info.

## Brightness control
Default brightness adjustment keys work but need to be pressed multiple times to increase/decrease the screen brightness. Use either the #Xbindkeys_2 or #ACPI methods to fix this.

Some desktop environments may lack granularity while changing brightness. This is due to the DE (e.g. gnome-settings-daemon) along with the internal graphics module changing the brightness when brightness adjustment keys are pressed causing multiple steps per press. To work around this add the kernel parameter .

## Xbindkeys
Install xbindkeys and append the following to :

 "xbacklight -dec 5"
   XF86MonBrightnessDown
 "xbacklight -inc 5"
   XF86MonBrightnessUp

## ACPI
Writing custom ACPI handlers for the brightness adjustment keys seems to have no effect. In order to use them properly you need to add the kernel parameter . See also Backlight#ACPI. Note that the ACPI backlight is disabled by default on Windows 8 hardware with a native backlight. Consider using the #Xbindkeys approach instead.

## Wrong EDID for external display
With certain connectors (e.g. MiniDP to VGA), there is a bug getting EDID for the external screen while booting:
 [ 93.736330] *ERROR* too many retries, giving up
This does not occur if the external screen is connected after booting.

The correct mode can be added per xrandr#Adding undetected resolutions:

## KMS
Enable KMS using the  module and by enabling VT in BIOS.

## Webcam
Works out of the box. Tested with guvcview

## Fingerprint Reader
Works out of the box with Fprint.

For a GUI,  is already patched to work with the X1's newer fingerprint reader. To get the gui's dropdown to recognize your device, you will have to add your user to the  group:

 $ gpasswd -a  plugdev

See fingerprint-gui for more information about config

## WWAN (Mobile broadband)
This model includes a [https://www.thinkwiki.org/wiki/Ericsson_H5321_gw_Mobile_Broadband_Module Ericsson H5321gw adapter that can be used as a mobile broadband adapter and GPS.

The SIM-card must be inserted in the back of the laptop.

Add text to the following file and reboot

Tested OK with NetworkManager with  installed

## GPS
Install  and .
Add this to the following file

{{hc|/etc/udev/rules.d/99-mbm.rules|2=
ATTRS{idVendor}=="0bdb", ATTRS{idProduct}=="1926", ENV{ID_USB_INTERFACE_NUM}=="09", ENV{MBM_CAPABILITY}="gps_nmea"
ATTRS{idVendor}=="0bdb", ATTRS{idProduct}=="1926", ENV{ID_USB_INTERFACE_NUM}=="03", ENV{MBM_CAPABILITY}="gps_ctrl"
}}

Reboot to reload udev rules.

Run

See if there is GPS-output

Run

To test it

Or use e.g.  in AUR.

See this link for more info.

## Keyboard backlight
Works out of the box. Use FN+Space

## Bluetooth
First try to set up Bluetooth normally. If you get kernel error messages:

 kernel: bluetooth hci0: Direct firmware load for brcm/BCM20702A1-0a5c-21e6.hcd failed with error -2
 kernel: Bluetooth: hci0: BCM: Patch brcm/BCM20702A1-0a5c-21e6.hcd not found
You need to manually install the proprietary firmware. The slackware wiki describes one way to do this: https://www.slackwiki.com/Btfirmware-nonfree.

## Mouse/Touchpad
Works out of the box. See TrackPoint for additional details.

## Docking
This model has no docking port.

Video for USB 3 Docking Stations currently is not supported, so you must use a USB Port Replicator with Digital Video (USB 2.0)

This supports:
* USB-devices connected to dock
* Audio
* Microphone
* Ethernet
* Video (see DisplayLink)
