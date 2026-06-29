# Lenovo Legion Y7000P2020H

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Backlight || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Webcam || ||
|-
| Bluetooth || ||
|-
| Thunderbolt || ||
|-
| Keyboard || ||
|-
| Touchpad || ||
|-
| TPM || ||
|-
| Fingerprint reader || ||
|-
| SD-card reader || ||
|-
| Speakers || ||
|-
| Microphone || ||
|-
| Ambient light sensor || ||
|}

For a general overview of laptop-related articles and recommendations, see Laptop.

## BIOS
At bootup, the BIOS settings page is entered via the  key.

In the BIOS settings, the model name can be seen in the Main tab, Secure Boot can be disabled from the Security tab and boot mode can optionally be switched between UEFI and legacy.

There is no known option to disable the discrete NVIDIA GPU using the BIOS (only have "Hybride Graphics" and "Discrete Graphics"), there may be one present after unlocking the advanced options.

## Video
## Backlight
## Power Down Nvidia Card
Blacklist nouveau drivers, reboot, and run:

 # echo 'auto' >> /sys/bus/pci/devices/0000:01:00.0/power/control

## Multihead
External displays using the USB-C ports only seem to function using the proprietary NVIDIA driver.

## If you enabled Discrete Graphics mode
If you enaled Discrete Graphics mode in BIOS,you cannot control the backlight via the function keys or in "Battery and Brightness" section in control center. Because the brightness is controlled by .

To recover the functionality of  and , you can change the acpi actions via creating the following files in the this blog and reboot:

Reboot afterwards.

## Power Management
One can change the power mode with the default  key.

Battery conservation mode is available. It will charge the device to 60% when charge falls below 50%, extending the life of the battery. It can be activated by running the following command:

 # echo 1 >/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

You can also install  to change the status conveniently.

## Keyboard
Keyboard is working out of box. There is no RGB settings.

## Function Keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Toggles Fn lock
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
|  ||  ||  || Select video project mode
|-
|  ||  ||  || Airplane Mode
|-
|  ||  ||  || Not Defined
|-
|  ||  ||  || Toggle Touchpad
|-
|  ||  ||  || Not Defined
|-
|  ||  ||  || Not Defined
|-
|  ||  ||  || Not Defined
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}
Lenovo Legion series Laptops uses IdeaPad ACPI and ones in normal configuration can use nearly all of the function keys except for  (Favorite key),  (tab switching key) and  (Calculator key), since ACPI key functions is not defined.== Touchpad ==

Single tap and double finger scrolling work. Multi gestures must be configured, they are detected with .

## Fan Control
Fan control only works with . You can also download the appimage version [https://odintdh.itch.io/extremecooling4linux to use it in GUI, but root permission is required.
