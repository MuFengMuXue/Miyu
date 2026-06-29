# Fujitsu Lifebook U9311

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Trackpoint || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|}

## Firmware
fwupd does not support this device.

## Intel Wi-Fi 6 AX200
For models with the Intel AX200 wireless adapter, the interface can engage in power saving when running on battery which increases network latency.

To avoid this issue, you can disable power saving by following the instructions in Power management#Network interfaces.

## Suspend
All Tiger Lake/Alder Lake Fujitsu laptops face a long-standing BIOS bug related to Intel graphics since 2021, still unfixed as of Sep 2025.

Symptoms include i915 driver errors in kernel log, waking up to a black screen or flickering screen from s2idle, and working HDMI output and everything else despite black screen, as this bug only affects the internal eDP connection to the display panel.

There are multiple reports online, such as on ArchBBS and Ubuntu Launchpad, [https://gitlab.freedesktop.org/drm/i915/kernel/-/issues/3455.

## Affected models
This list is incomplete:

* U9311 and its variants.
* U9312 and its variants.
* E5411 and its variants.

## ACPI patch
This solution was developed on FreeDesktop. Extract and decompile the SSDT table. For this model, the code is found in SSDT4.

 # cat /sys/firmware/acpi/tables/SSDT4 > SSDT4.aml
 $ iasl -d SSDT4.aml

Apply the required changes.

{{hc|fujitsu-vdd.patch|2=
--- SSDT4.dsl.orig	2024-07-29 18:33:14.782373152 +0200
+++ SSDT4.dsl	2024-07-29 18:38:33.021477685 +0200
@@ -18,7 +18,7 @@
  *     Compiler ID      "INTL"
  *     Compiler Version 0x20160422 (538313762)
  */
-DefinitionBlock ("", "SSDT", 2, "INTEL ", "IgfxSsdt", 0x00003000)
+DefinitionBlock ("", "SSDT", 2, "INTEL ", "IgfxSsdt", 0x00003001)
 {
     External (_SB_.PC00, DeviceObj)
     External (_SB_.PC00.GFX0, DeviceObj)
@@ -115,11 +115,6 @@
         {
             If ((PDRD () == Zero))
             {
-                If ((VDDE == One))
-                {
-                    VDDE = Zero
-                    Sleep (0x01F4)
-                }
             }

             NDID = 0x02
@@ -2479,11 +2474,6 @@
             {
                 If ((PDRD () == Zero))
                 {
-                    If ((VDDE == One))
-                    {
-                        VDDE = Zero
-                        Sleep (0x01F4)
-                    }
                 }
             }
}}

Recompile

 $ iasl -sa SSDT4.dsl.

Load the file by one of the methods described in DSDT#Using modified code.
