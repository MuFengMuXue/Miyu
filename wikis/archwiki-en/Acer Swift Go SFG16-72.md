# Acer Swift Go SFG16-72

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Fingerprint scanner ||  ||
|}

## Cannot access Firmware Setup issues
Firmware Version: Insyde Corp. V1.14 (Release Date: 08/25/2024)

After installing Linux, you may encounter issues accessing the Firmware Setup. For further information and troubleshooting, please refer to this discussion: https://bbs.archlinux.org/viewtopic.php?pid=2200805

The solution is to delete the entry '\systemd\systemd-bootx64.efi' with efibootmgr. This will restore your access to Firmware Setup (F2).

 $ efibootmgr --delete-bootnum --bootnum 2

## Installation
Enable the "F12 Boot Menu" under the Main section in Firmware Setup. This provides a useful fallback in case you're unable to access the Firmware Setup later.

To disable Secure Boot, set the supervisor password in the UEFI settings. Then you should be able to disable Secure Boot and boot Arch.

After installation, you'll need to re-enable Secure Boot. Then, navigate to the "Select an UEFI file as trusted for executing" option, and locate your boot loader. In my case, it was located at . After selecting the boot loader, you can disable Secure Boot again.

This step is necessary; otherwise, you won't be able to access the firmware setup.

## Audio
Install  to support the audio card.

## Battery health control
Install  and reboot.

Ensure  is loaded:

 $ lsmod | grep acer

Enable health mode:

 $ cat /sys/module/acer_wmi_battery/drivers/wmi:acer-wmi-battery/health_mode

If health_mode returns 0:

 $ echo 1 > /sys/module/acer_wmi_battery/drivers/wmi:acer-wmi-battery/health_mode

This enables battery thresholds until reboot.

Create a systemd service file to ensure battery health mode is set automatically on boot:

Enable the .

## Firmware
 supports only "UEFI dbx". It is possible to manually flash the UEFI firmware update with fwupdtool.

These errors during bootup related to ACPI can safely ignored.
 ACPI BIOS Error (bug): Failure creating named object \_SB.UBTC, AE_ALREADY_EXISTS (20240322/dswload2-326)
 ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20240322/psobject-220)

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
|  ||  ||  ||
|-
|  ||  ||  || Disable TouchPad
|}
# The key is visible to ,  and similar tools.
# The physical key has a symbol on it, which describes its function.
