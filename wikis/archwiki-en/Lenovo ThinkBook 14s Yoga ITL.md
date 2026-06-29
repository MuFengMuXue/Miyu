# Lenovo ThinkBook 14s Yoga ITL

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Touchscreen || ||
|-
| Smart Pen (Wacom) || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Thunderbolt 4 ||  ||
|-
| rowspan=3 | Fingerprint reader ||  ||
|-
|  ||
|-
|  ||
|-
| TPM || ||
|}

## Installation
Use  or  to enter UEFI/BIOS setup utility. You must disable Secure Boot to be able to boot from the installation media.

## Secure Boot
See Secure Boot for general setup.

## Fingerprint reader
The fingerprint reader is built-in on the button and does not require pressing the button itself.

 requires a proprietary driver which can be obtained here .

 works out of the box and doesn't require a proprietary driver.

 is currently in the works of reverse engineering.The fingerprint reader doesn't work well with the default fprint because the sensor works by touching the sensor, not swiping the finger over the reader, hence it requires . It is very precise: fprint only saves five finger samples which are not enough for different finger placements.

## Screen rotation
Install  for automatic screen rotation to work.

## Power and Performance management
To tweak CPU power and performance preferences, see Dell XPS 13 2-in-1 (9365)#Reduce throttling as Lenovo's and Dell's Intel CPUs use the same interfaces.

To set the Battery Conservation Mode, see Laptop/Lenovo#Battery conservation mode

Desktop Environment specific tools can be found over the internet to set everything up with GUI.

Fan control readings do not work yet and managed by the BIOS by default.

Offline USB charging can be turned on(1) or off(0) with:

 # echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/usb_charging

## Platform profiles
ACPI platform profiles can be managed manually via  at  or automatically via  or power-profiles-daemon. Available profiles can be viewed with .

## HuC firmware
To enable HuC firmware loading for offloading media decoding functionality, see Intel graphics#Enable GuC / HuC firmware loading.

## Lenovo integrated pen and touchscreen (Wacom)
See Graphics tablet for general installation procedure.

## In late userspace
 does not have a tablet definition for the  device ID yet[https://github.com/linuxwacom/wacom-hid-descriptors/issues/333.

It is possible to add your own definition instead so other programs such as  can recognize and configure the tablet:

## In early userspace
Loading drivers for input devices early provides a possibility to use programs such as  for unlocking disks with the GUI.

Required drivers to load into initramfs are:

 evdev hid_multitouch i2c_hid_acpi intel_lpss_pci intel-lpss uhid uinput mac_hid i2c_smbus i2c_i801 hid_multitouch i2c_hid_acpi usbhid wacom ideapad_laptop lenovo_ymc think_lmi hid_generic mousedev

## Function keys
Since the release of Linux 6.5, the  driver has been updated to support extra hotkeys found on this laptop.https://lwn.net/Articles/942879/

To control  programmatically:

 # echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/fn_lock

To control keyboard backlight (from 0 to 2) :

 # echo 0 > /sys/class/leds/platform::kbd_backlight/brightness

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Enables Fn lock
|-
|  ||  ||  || ,
|-
|  ||  ||  || ,
|-
|  ||  ||  || ,
|-
|  ||  ||  || ,
|-
|  ||  ||  || ,
|-
|  ||  ||  || ,
|-
|  ||  ||  || , Switch display devices
|-
|  ||  ||  || , Airplane Mode Toggle
|-
|  ||  ||  || , Lenovo Service Hotkey
|-
|  ||  ||  || ,  Answer a call
|-
|  ||  ||  || , Hang up or reject a call
|-
|  ||  ||  || ,
|-
|  ||  ||  || , On Windows: Starts Lenovo Vantage.
|-
|  ||  ||  ||  On Windows: Starts the "Snipping" Tool app
|-
|  ||  ||  || Cycles states of keyboard backlight
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
|   ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|   ||  ||  ||
|}

# The key is visible to  or  and similar tools.
# The physical key has a symbol on it, which describes its function
