# Dell Inspiron 7375

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Touchscreen ||  ||
|-
| SD card reader ||  ||
|-
| Sensor hub ||  ||
|}

This is an install and configuration guide for the Dell Inspiron 13 7000 Series (Model 7375) laptop, Ryzen 7 2700U with Vega Mobile graphics.

See the Laptop/Dell chart for information on other Dell laptops.

## Installation
## Kernel parameters
System will be unstable without kernel parameters. For  5.4 and newer, use:

 acpi_osi=Linux idle=nomwait

## Power management
## On battery
To improve battery time, use the  governor:

 # cpupower frequency-set -g powersave
 # echo low > /sys/class/drm/card0/device/power_dpm_force_performance_level

For further improvements, see Power saving or TLP.

## Fan Control
Install the  package.

## Disable IPMI
There is no support for IPMI in this laptop. Blacklist  to prevent some warnings while booting.

## Disable Time Throttling STAPM
Is you only want CPU/GPU temperature-based throttling, install  and run:

 # ryzenadj --slow-time=0xffffffff --stapm-time=0xffffffff

Run this command before running high demand tasks. The setting will be disabled after suspension.

## Wireless
See Broadcom.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  || ||  || Toggles Mute
|-
|  || ||  || Volume Down
|-
|  || ||  || Volume Up
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  || Toggles keyboard backlight
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  || Toggles Fn lock
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|-
|  || ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
