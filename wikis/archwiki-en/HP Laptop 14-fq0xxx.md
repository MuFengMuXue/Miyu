# HP Laptop 14-fq0xxx

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam||  || *
|-
| Wi-Fi ||  || *
|-
| GPU ||  ||
|-
| TPM ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|}

The HP 14-fq0xxx is a laptop featuring a 14" LCD Built-in Monitor, 4GB of RAM, 128 GB SATA 3 TLC M.2 SSD, a 640×360 HP Webcam and a AMD Athlon Silver 3050U (2) @ 2.30 GHz with AMD Radeon Vega Series/Radeon Vega Mobile Series Graphics.

## Installation
The wireless network adapter and integrated graphics require .

AMD GPU graphics card; see AMDGPU for Vulkan support and Hardware video acceleration. ( recommended)

The Webcam may require additional configuration or software such as  to work.

## Accessibility
The BIOS setup is a simple, text-based GUI, navigated with a keyboard. It does not expose many options apart from the standard time/date settings, and boot configuration.

To show a list of all available menus, press .

To access the BIOS setup, press ; To display the help menu, press .

To access the boot menu, press .

## Firmware
fwupd does not support this device.

## Battery
The BIOS has a setting for reporting battery state to the OS; is disabled by default, if disabled only percentage will be reported to the OS.

## Secure Boot
Secure Boot works, tested with sbctl.

## Function keys
By default, keys - perform their alternative functions, and  is needed to press , but there is a BIOS option to change this behavior. The following table assumes this setting was disabled.

{| class="wikitable"
|-
! Key !!  Visible?1 !! Marked?2 !! Effect
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
|  || 3 ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd handles this by default, but does not consume it.
