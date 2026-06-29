# ASUS ROG GA401I

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || PS/2 ||
|-
| Keyboard || PS/2 ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| GPU (AMD) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Speakers ||  ||
|-
| Fingerprint reader ||  ||
|-
| AniMe matrix1 ||  ||
|}

This page contains instructions and tips for configuring Arch Linux on the ASUS Zephyrus G14 and ASUS ROG Studio Pro 14, including models such as:
* GA401I*
* PX401I*
* GA401Q*

# Some models such as the GA401QH do not feature the AniMe matrix

## Accessibility
## BIOS
The BIOS menu is graphical and is intended to be used with a mouse. All entries however can be accessed from the keyboard, and should be easy to OCR.

The official manual states to press  to enter the BIOS while the computer is booting. Neither the manual nor the POST screen not state what button opens the boot options menu, but it can be accessed by pressing

Within the BIOS menu, you can use the arrow keys (///), as well as  to move the cursor, the / key to activate or save things,  to open the boot device menu,  to save changes,  to reset BIOS settings to default,  to switch BIOS modes to and from EZ mode or Advanced mode, and  to exit the BIOS without saving.

EZ mode shows the current BIOS version, your laptop's CPU, RAM, GPU, and Serial Number, display, occupied USB ports, internal storage device, CPU fan speed and CPU tempreture, current battery percentage, BIOS passwords, boot priority, and asset tag.

Advanced mode is split into many pages and is intended to be for more advanced users. You can use the left and right arrow keys to navigate between pages. The right side of the screen lists hotkeys for the menu:
* Main shows your laptop's BIOS information, CPU and RAM, serial number, and current time.
* Advanced allows for toggling power management, CPU virtualization, enter BIOS flashing, UEFI network stack and legacy USB support.
* Boot allows you to change boot device order and whether to enable or disable Fast Boot
* Security allows setting a BIOS password, toggling Secure Boot and for disabling Wi-Fi, Bluetooth, and the fingerprint scanner.
* Save & Edit allows you to quickly save or discard your BIOS changes and leave the bios, or boot off a device using the Boot Override setting.

## LEDs
There is no diagnostic LED on the motherboard. The official technical documentation does not discuss whether the motherboard beeps when there is an issue, nor does it say what such beeps could mean.

There are three status LEDs on the center front of the bottom half of the laptop. The left LED is for power, the center LED is for the battery, and the right LED is for SSD activity. The battery LED has four states:
* Solid White: The laptop is plugged in and the battery power is between 95% and 100%.
* Solid Orange: The laptop is plugged in and the battery power is less than 95%.
* Blinking Orange: The laptop is running on battery and the batter power is less than 10%
* No light: The laptop is running on battery and the batter power is between 10% and 100%.

More information can be found in the official technical documentation.

## Firmware
## ASUS Linux
The ASUS Linux stack provides users of this laptop with a great many ASUS specific functions, to name a few:

*Battery Charge Limit
*Multiplexer (GPU) Controls
*Panel Overdrive
*AniMe matrix and keyboard backlight controls
*Fan curve editing
*Much more.

It is highly recommended to install these tools for the optimal experience on these laptops.

## High battery usage/low runtime on battery
The G14 can be tweaked to have far better battery live and performance on Windows A few optimizations can be taken to reach a similar battery live on Arch (you can monitor your current power usage using  - note that only the reported battery discharge seems to be fully accurate).

## NVIDIA driver optimization
When using the official NVIDIA driver, the power usage can be reduced by putting the following line in :

 options nvidia "NVreg_DynamicPowerManagement=0x02"

This has also shown to reduce fan noise and overall heat.

## Disabling turbo boost
While not necessarily saving power, some user prefer to disable turbo boost for smoother power delivery and less heat. To temporarily disable boost, execute the following:

 # echo 0 > /sys/devices/system/cpu/cpufreq/boost

Or use the power profiles from asusctl to handle this automatically.

## General Tips
To maximize the battery life, follow the general tips at power management.

## Function Keys
{| class="wikitable"
! Key
! Visible?1
! Marked?2
! Effect
|-
| colspan="4" | Function keys
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Does nothing ( in xev)
|-
|  ||  ||  || Does nothing ( in xev)
|-
|  ||  ||  || Opens Screen capture tool ( in xev)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Change external display options ( in xev)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
| colspan="4" | Arrow keys
|-
|  ||  ||  || Opens context menu ()
|-
|  ||  ||  || Page Up
|-
|  ||  ||  || Page Down
|-
|  ||  ||  || Home
|-
|  ||  ||  || End
|-
|  ||  ||  || Toggles the Windows/Super key
|-
| colspan="4" | Top keys
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

## Troubleshooting
## Using external display through the USB-C port
While the dedicated HDMI port works out of the box, the display output through the USB-C port does not appear to be connected to the integrated graphics controller. Using an external display through this port requires to switch to the dedicated NVIDIA graphics card. See asusctl for more details.

## Volume adjustment
When using built-in speakers, volume adjustment will not work for PulseAudio. Download this [https://fars.ee/YkSC patch and apply it:

 # patch -p1 -d /usr/share/alsa-card-profile/mixer/paths/ -i /path/to/patch

Then restart the  user unit.

## Pacman hook
To apply the patch automatically after a  upgrade, you can use a pacman hook:
