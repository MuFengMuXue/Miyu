# Lenovo ThinkPad T520

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| rowspan="3" | WLAN (Intel) ||  ||
|-
|  ||
|-
|  ||
|-
| WLAN (Realtek) ||  ||
|-
| WWAN ||  ||
|-
| rowspan="2" | GPU (Intel) ||  ||
|-
|  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Touchpad || ||
|-
| Trackpoint || ||
|-
| Keyboard || ||
|-
| Fingerprint reader ||  ||
|-
| Smart card reader ||  ||
|-
| rowspan="2" | SD card reader ||  ||
|-
|  ||
|-
| Audio ||  ||
|}

The larger 15-inch variant of the Lenovo ThinkPad T420.

## Accessibility
The appearance of the ThinkPad Setup program (i.e., the tool used to configure UEFI BIOS settings) is simple and uses contrasting colours, so it may work well with OCR software. A legend of keyboard navigation shortcuts is also clearly listed on the bottom of the screen.

The user guide has a section under Chapter 8, "Advanced configuration", titled "ThinkPad Setup" that highlights the steps need to configure the UEFI BIOS settings. Relevant keyboard shortcuts (including those needed to trigger certain features on device startup) are also mentioned throughout:

{| class="wikitable"
! Key !! Effect
|-
|  || Interrupt normal startup and bring up the Startup menu
|-
|  || Start the ThinkPad Setup program
|-
|  || Bring up the Boot Menu window
|}

## Firmware
fwupd does not support this device yet.

## Graphics
## Selecting the graphics device
(This section only applies if your laptop also comes with the NVIDIA graphics card.)

Selecting a graphics device can be done by entering the ThinkPad Setup program and selecting one of the following options from Config > Display > Graphics Device:

* Integrated Graphics
* Discrete Graphics
* NVIDIA Graphics

See Intel graphics, NVIDIA, and NVIDIA Optimus or Bumblebee for more details.

## Screen freeze in Discrete Graphics mode
In Discrete Graphics mode, GRUB's framebuffer can freeze the screen before the login prompt appears. Disabling the framebuffer resolves this issue.

## Touchpad
libinput does not support horizontal edge scrolling on the T520's touchpad.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
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
|  ||  || ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles the ThinkLight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || None
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
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
