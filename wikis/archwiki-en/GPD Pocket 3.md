# GPD Pocket 3

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (1195G7) ||  ||
|-
| GPU (N6000) ||  ||
|-
| Wireless (1195G7) ||  ||
|-
| Wireless (N6000) ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth (1195G7) ||  ||
|-
| Bluetooth (N6000) ||  ||
|-
| Audio (1195G7) ||  ||
|-
| Audio (N6000) ||  ||
|-
| Display || ||
|-
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Touchscreen ||  ||
|-
| Digitizer ||  ||
|-
| Thunderbolt (1195G7) ||  ||
|-
| Fingerprint Sensor || ||
|}

This page provides information for the GPD Pocket 3.

## Specifications
There are two models differentiated by processor, memory speed and capacity, storage capacity, Thunderbolt support, and wireless network hardware.

## 1195G7
* Display: 8" 1920x1200
* CPU: Intel Core i7-1195G7
* RAM: 16GB LPDDR4x 3733
* Storage: 1TB PCIe M.2 NVMe SSD (BIWIN NQ200)
* Network: 2.5GbE, Intel AX210 802.11ax (2.4/5/6Ghz), BT 5.2
* Thunderbolt 4 supported (1 port)

## N6000
* Display: 8" 1920x1200
* CPU: Intel Pentium Silver N6000
* RAM: 8GB LPDDR4x 2933
* Storage: 512GB PCIe M.2 NVMe SSD
* Network: 2.5GbE, Intel AX200 802.11ax (2.4/5Ghz), BT 5.0
* Thunderbolt not supported

## Firmware
 is not supported on this device. GPD provides firmware updates via Windows executables.

See https://gpd.hk/gpdpocket3firmware for the files and Windows PE for instructions on how to make a bootable Windows environment to apply the updates.

## Audio
## 1195G7
Using  (legacy) instead of  enables sound on the 1195G7 model.

## N6000
The N6000 model utilizes ESSX8326 sound hardware and drivers are provided by . Since kernel version 6.1 sound works with some caveats (occasional popping, volume resets on reboot) although internal microphone does not work at all. Make sure above fix for 1195G7 is not applied. There is a bug report on the sof project GitHub requesting help specifically for the Pocket 3. The es8xxx series sound devices have a history of problems with Linux and there is a general lack of interest in solving them.

## Display
The Pocket 3's display is designed for portrait devices and is rotated by 90 degrees counter-clockwise by default. This can be solved as explained in Tablet PC#Screen rotation.

## Backlight
Control is provided by installing . Keyboard shortcuts can be configured with xbindkeys.

## Screen Tearing
Due to the display being designed for portrait devices, the device experiences vertical screen tearing.

This can be solved by ensuring  is installed and following the instructions in Intel graphics#Tearing.

## Touchscreen and Digitizer
Install .

The touchscreen and digitizer matrix are in portrait mode and have to be rotated 90 degrees clockwise.
Furthermore, the stylus pen behaves oddly under libinput, so we can force the wacom driver and get reasonable usability.
This can be corrected for all touch and pen interfaces at once with the following configuration for X:

See https://github.com/defencore/gpd-pocket-3-linux

For Wayland rule should be placed in udev system:

{{hc|/etc/udev/rules.d/99-touchscreen.conf|2=
ACTION=="addchange", KERNEL=="eventATTRS{name}=="GXTP7380:00 27C6:0113", ENV{LIBINPUT_CALIBRATION_MATRIX}="0 1 0 -1 0 1"
}}

## Automatic Rotation
xrandr and xinput rotation can be automated with
[https://github.com/akissu/2in1screen/tree/master 2in1screen.

With Wayland there are multiple options depending on compositor:

* on Sway automation can be set up using iio-sway;
* on Hyprland automation can be set up using iio-hyprland.

## Webcam
The Alcor Micro Corp. webcam is a USB 2.0 device with a maximum resolution of 1600x1200 at 30fps. It does not support any 16:10 resolutions to match the screen aspect ratio.

## Fingerprint Sensor
The FocalTech FTE3600 is an SPI fingerprint reading device. Install the  and  packages.

See fprint for configuration.

## Function keys
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
|  ||  ||  || Fan control3
|-
|  ||  ||  || Enables/disables keyboard backlight4
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# toggles between low and high speed, firmware controlled, not configurable
# toggles between on and off, firmware controlled, not configurable

## Thunderbolt
Thunderbolt works out of the box on the 1195G7 model (not available on the N6000 model). See Thunderbolt for general information and External GPU for enhanced graphics via an external GPU enclosure.

## Additional Features
## BIOS Reset
The small hole on the rear of the device between the hinge and the module slot contains a BIOS factory reset button.

## Optional Mounting
The left and right side of the device each have a 2.5mm threaded hole by the hinge. This hole can be used as physical mount for customization.

## Optional KVM Module
Video capture functions as a standard v4l device and can be opened with software such as OBS or via command line with FFmpeg.

When a USB cable is plugged from the module into another computer, the Pocket 3's keyboard, touchpad, and mouse buttons will switch to functioning as input for the connected machine without drivers or configuration.
