# Lenovo XiaoXin 15are 2020

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| Video ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| Fingerprint reader ||  ||
|-
|}

The XiaoXin-15ARE 2020 is primarily sold in China, the most similar internationally sold model is the IdeaPad 5 15ARE.

## Firmware setup
You can access the BIOS by pressing  at the Splash screen. The boot menu can also be accessed by pressing .

## F2 and F12 keys do not work
The Windows 20H2 installer (consumer edition, updated Feb 2021) is tested to delete these keys' functionality to reach BIOS settings and Boot menu. It is unclear whether Microsoft intentionally did this or is yet another bug in Windows. You can try return your laptop Lenovo to repair mainboard BIOS information.

It is recommended to update to BIOS version , as in #BIOS update, which fixes this issue.

## Noto Button
You can also use the "Noto Boot Menu" which displays more options like BIOS Setup and Boot Menu. On power on, press the power button while holding  to access it. Note that this is also affected by #F2 and F12 keys do not work, so if the  and  keys do not work, "Noto Boot Menu" cannot either.

## Enter Firmware Setup Utility without F2 and F12 keys
See Unified Extensible Firmware Interface#Enter firmware setup without function keys.

## Firmware
No Fwupd support is present on this device.

## BIOS update
BIOS updates can be found here: 小新-15 2020(AMD平台：ARE版) 驱动列表 under the BIOS section. Only a Windows installer is provided.
Extracting with innoextract (version 1.8 tested) can unpack the downloaded BIOS-E7CN39WW.exe to E7CN39WW.exe, which is the Phoneix's BIOS installer. But this installer cannot be further extracted with innoextract.

It is recommended to update to BIOS version , which will fix  and  keys problem. It also adjusts thermal control so that the fans are more quiet and more efficient. The update will reset UEFI boot order to only contain Windows boot manager; return to Arch Linux after BIOS update by following the steps in Unified Extensible Firmware Interface#Boot back to Arch Linux when stuck with Windows

## Power management
This laptop has 3 modes of system performance mode available: Intelligent Cooling, Extreme Performance and Battery Saving. To toggle it, you need to call some ACPI methods, which require an out-of-tree kernel module. See Lenovo IdeaPad 5 15are05#Power management

## Wi-Fi
Wi-Fi Direct (aka Wi-Fi P2P) support is only present on Windows: in Windows cmd, see .

## Function Keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Enables Fn lock
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
|  ||  ||  || Not an XF86 Key: Switch Monitor
|-
|  ||  ||  ||
|-
|  ||  ||  || Not an XF86 Key: System Settings
|-
|  ||  ||  || Not an XF86 Key: Lock Screen
|-
|  ||  ||  || For MS-Windows: Switch window
|-
|  ||  ||  ||
|-
|  ||  ||  || For MS-Windows: Lenovo Energy Star
|-
|  ||  ||  || For MS-Windows: ScreenShot
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools. Desktop environments and even some window managers may come with a default configuration which swallows all the function keys, since it is handling them by itself. This visiblility column is tested on a minimal window manager Openbox with .
# The physical key has a symbol on it, which describes its function.

## Toggle Fn lock in UEFI/BIOS Setup Utility
Besides , you can also change Fn lock in UEFI/BIOS Setup Utility. In UEFI/BIOS Setup Utility, Configuration > HotKey Mode, change to Disabled to use  for direct  key,  for function key (HotKey), change to Enabled to use  for function key (HotKey),  for direct  key.
