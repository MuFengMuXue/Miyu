# Xiaomi RedmiBook Pro 16 2025

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Touchpad ||  ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| Fingerprint reader ||  ||
|-
| Audio ||  ||
|-
| Ambient light sensor || ||
|-
| NPU ||  ||
|}

The Xiaomi RedmiBook Pro 16 (2025) features a 16" screen, Intel Core Ultra 5 225H or Ultra 7 255H processor, and integrated Intel Arc 130T / 140T GPU.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Installation
When installing Arch Linux on this device, Wi-Fi functionality may require the  package.

To disable Secure Boot, a UEFI password has to be set first.

## Accessibility
The firmware interface is set to Chinese by default.
To change the firmware language to English, navigate through the menus by pressing:  (to access the Settings tab), , ,  (to enter language settings), ,  (to select English).

## Firmware
fwupd supports updating the system firmware, NVMe SSD, and webcam on this device.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || Enable Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Mute Microphone
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Xiao AI
|-
|  ||  ||  || Project
|-
|  ||  ||  || Settings
|-
|  ||  ||  || Toggle Keyboard Backlight
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

## Charge Limit
The device supports setting a charge limit by making some ACPI calls (extracted from the Xiaomi PC Manager software). Provided the  package is installed, the following script makes this easily accessible under Linux as well:

{{hc|set_charge_limit.sh|#!/bin/bash

acpi_call() {
    local command"$1"
    local hex_value"$2"

    local acpi_string"\\_SB.PC00.WMID.WMAA 0x0 0x1 { \
0x00 $command 0x00 0x10 0x02 0x00 $hex_value 0x00 \
0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 }"

    echo "$acpi_string"  tee /proc/acpi/call
}

set_charge_limit() {
    local limit_hex
    case "$1" in
        40) limit_hex"0x08" ;;
        50) limit_hex"0x07" ;;
        60) limit_hex"0x06" ;;
        70) limit_hex"0x05" ;;
        80) limit_hex"0x01" ;;
        *) echo "Invalid limit. Valid options: 40, 50, 60, 70, 80"; exit 1 ;;
    esac

    echo "Setting $1% limit"
    acpi_call "0xfb" "$limit_hex"

    echo "Enabling charge limit"
    acpi_call "0xfa" "0x00"

    echo "Enabling charge limit (second call)"
    acpi_call "0xfa" "0x00"
}

disable_charge_limit() {
    echo "Disabling charge limit"
    acpi_call "0xfb" "0x00"

    echo "Disabling charge limit (second call)"
    acpi_call "0xfb" "0x00"
}

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 "
    echo "  limit: 40, 50, 60, 70, or 80"
    echo "  disable: turns off charge limiting"
    exit 1
fi

if [ "$1"  "disable" ]; then
    disable_charge_limit
else
    set_charge_limit "$1"
fi}}

The script needs to be run on every reboot. You can automate this by using systemd. An example unit to set the charge limit to 70% may look like this:
