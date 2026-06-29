# Lenovo ThinkPad T400

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| rowspan="2" | Ethernet ||  ||
|-
|  ||
|-
| rowspan="2" | WLAN (Intel) ||  ||
|-
|  ||
|-
| WLAN (Realtek) ||  ||
|-
| WWAN (Sierra) ||  ||
|-
| WWAN (Ericsson) ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (ATI) ||  ||
|-
| Touchpad || ||
|-
| Trackpoint || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| Fingerprint reader(STMicroelectronics) ||  ||
|-
| Fingerprint reader(AuthenTec) ||  ||
|-
| CardBus slot ||  ||
|-
| Smart card reader ||  ||
|-
| SD card reader ||  ||
|-
| Memory Stick reader ||  ||
|-
| xD card reader ||  ||
|-
| Audio ||  ||
|}

## Accessibility
The appearance of the BIOS Setup Utility is simple and uses contrasting colours, so it may work well with OCR software. A legend of keyboard navigation shortcuts is also clearly listed at the bottom of the screen.

Keyboard shortcuts needed to trigger certain features on device startup are mentioned throughout the hardware maintenance manual:

{| class="wikitable"
! Key !! Effect
|-
|  || Interrupt normal startup and bring up the Startup menu
|-
|  || Start the BIOS Setup Utility
|-
|  || Bring up the Boot Menu window
|}

## Firmware
fwupd does not support this device yet.

## Graphics
## Selecting the graphics device
(This section only applies if your laptop also comes with the ATI graphics card.)

Both the Intel graphics card and the optional ATI graphics card must be turned on to allow graphics switching by restarting Xorg. Selecting a graphics device can also be done by entering the BIOS Setup Utility and selecting one of the following options from Config > Display > Graphics Device:

* Integrated Graphics
* Discrete Graphics
* Switchable Graphics

See Intel graphics, ATI, and Hybrid graphics for more details.

## Visually corrupted GRUB menu
GRUB's framebuffer may cause the GRUB menu to disappear or appear "corrupted" during the boot process. Fortunately, the menu will still be functional even without visual aid. This issue can be resolved by disabling GRUB's framebuffer.

## Touchpad
Although libinput is recommended over Touchpad Synaptics, the latter driver provides more touchpad scrolling options, namely:

* Horizontal and vertical edge scrolling.
* Horizontal and vertical two-finger scrolling.
* Circular scrolling.

libinput, on the other hand, only supports vertical edge scrolling for this particular touchpad.

## Touchpad Synaptics
Note that two-finger pressure may need to be decreased in order to increase the responsiveness/sensitivity of two-finger scrolling. This can be done by decreasing the default value of  to a value like :

 $ xinput set-prop 'SynPS/2 Synaptics TouchPad' 'Synaptics Two-Finger Pressure' 50

You can experiment with different values to find something that works for you. See  for more input device properties (and configuration options), e.g., selecting the scrolling method. See Touchpad Synaptics#Configuration for making the above change persistent across sessions.

## Mute key
T400 laptops with BIOS versions older than 3.01 (7UET71WW) may need to pass  as a kernel parameter to allow the mute key to function as intended. See https://thinkwiki.org/wiki/Mute_button and the relevant thread on the linux-acpi mailing list for more details.

## Power management
## Fan speed control
See Fan speed control#ThinkPad laptops.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  ||
|-
|  ||  || || Reserved3
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , reserved3
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , reserved3
|-
|  ||  || || Reserved3
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
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# The key is marked as "reserved" in the hardware maintenance manual.
