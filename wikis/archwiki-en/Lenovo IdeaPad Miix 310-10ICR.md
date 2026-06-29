# Lenovo IdeaPad Miix 310-10ICR

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Keyboard ||  ||
|-
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Audio || ||
|-
| Wi-Fi ||  ||
|-
| WWAN ||  ||
|-
| Bluetooth || ||
|-
| TF/SIM reader || ||
|-
| TPM ||  ||
|}

## Installation
The boot process might fail due to a CPU lockup. In this case, the  and/or  modules should be blacklisted using the kernel command lineSecure Boot may prevent booting of non-Windows operating systems, as the device is officially [https://pcsupport.lenovo.com/us/en/products/tablets/miix-series/miix-310-10icr/downloads/ds112922-bios-update-for-windows-10-64-bit-miix-310-10icr?category=BIOS%2FUEFI compatible with Windows 10 only.
It can be fully disabled in the BIOS if needed.

## Accessibility
The BIOS mainly uses 3 colors providing a contrasted interface.
One can navigate it using the touchpad, keyboard or the touchscreen.

The support page document the  key used to enter the BIOS.
It even offers an interactive BIOS Simulator, which simulates different BIOS interfaces for certain Lenovo products, but not this particular model.

## Firmware
One source recommends updating the BIOS to the latest version: .
The oldest version:  also works.

fwupd does not support this device yet.

## Cameras
As mentioned above, the modules responsible for the cameras can cause a CPU lockup, preventing the boot process from ever completing.
This can be partially fixed by putting a binary firmware file into With this, blacklisting the modules is not required anymore.

## Wireless
There might not be any Wi-Fi or Bluetooth functionality, as the necessary hardware may neither be detected by ,  nor hw-probe.
As a workaround, one can use USB tethering with a capable phone or an adapter to achieve Wi-Fi or Bluetooth connectivity.

When installing Ubuntu 22.10 alongside Arch, Wi-Fi starts working[https://bbs.archlinux.org/viewtopic.php?pid=1957672#p1957672.
It now uses the  module and is picked up by  as an SDIO device: .

The modem is detected regardless, meaning that, with a SIM card, mobile internet might be possible.

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
|  ||  ||  || Toggles touchpad on or off
|-
|  ||  ||  ||  Toggles soft-block on Bluetooth and Wi-Fi
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
