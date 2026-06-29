# Lenovo Yoga 7i

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| rowspan="2" | GPU ||  ||
|-
|  ||
|-
| rowspan="2" | Wi-Fi ||  ||
|-
|  ||
|-
| rowspan="2" | Bluetooth ||  ||
|-
|  ||
|-
| rowspan="2" | Audio ||  ||
|-
|  ||
|-
| rowspan="2" | Webcam ||  ||
|-
|  ||
|-
| Keyboard || ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Active pen || ||
|-
| Fingerprint reader ||  ||
|}

This page provides information for the Gen 6 and Gen 7 version of the Intel-equipped Yoga 7 laptops.

Many of these points mentioned here should also be applicable to Gen 8 versions. See Lenovo Yoga 7i Gen 8 (16IRL8) for details on one specific Yoga 7i Gen 8 model.

## Installation
If you see  when you run mkinitcpio, you can safely ignore the message as this laptop does not have a Renesas USB3 controller. See Mkinitcpio#Possibly missing firmware for module XXXX for details.

## Accessibility
The speakers do not work out of the box (see below), so in particular speech-aided installation is not possible.

## Power management
## Control Power Saving Modes
Install  and then enable/start .

Desktop environments will then detect support for it.

## Activating S3 sleep
In order to support "Windows Modern Standby", the BIOS does not advertise S3 sleep (suspend to RAM), as discussed in detail in this forum post.

Follow DSDT#Recompiling it yourself to patch the DSDT table with the following patch:

{{bc|
--- dsdt.dsl
+++ dsdt.dsl
@@ -18,7 +18,7 @@
  *     Compiler ID      "INTL"
  *     Compiler Version 0x20210105 (539033861)
  */
-DefinitionBlock ("", "DSDT", 2, "LENOVO", "CB-01   ", 0x00000002)
+DefinitionBlock ("", "DSDT", 2, "LENOVO", "CB-01   ", 0x00000003)
 {
     External (_GPE.AL6F, MethodObj)    // 0 Arguments
     External (_GPE.P0L6, MethodObj)    // 0 Arguments
@@ -516,7 +516,7 @@

     Name (SS1, Zero)
     Name (SS2, Zero)
-    Name (SS3, Zero)
+    Name (SS3, One)
     Name (SS4, One)
     OperationRegion (GNVS, SystemMemory, 0x45AB8018, 0x0A9B)
     Field (GNVS, AnyAcc, Lock, Preserve)
}}

See Power management/Suspend and hibernate#Changing suspend method for more details on the general context.

## Battery conservation mode
See Laptop/Lenovo#Battery conservation mode.

## Function keys
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
|  ||  ||  || , see below
|-
|  ||  ||  || , see below
|-
|  ||  ||  ||
|-
|  || 3 ||  || , toggles soft-block Wi-Fi and bluetooth
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Opens Lenovo Vantage on Windows, not usable on Linux
|-
|  ||  ||  ||
|-
|  ||  ||  || Change keyboard backlight level
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default

## Brightness keys
The brightness hotkeys only emit signals after resuming from suspend-to-RAM or hibernation, but not after (re)booting. This is because they depend on initialization by an ACPI method which is called when resuming from a sleep state but not on boot.

This should be fixed in kernel 6.2.x: https://bugzilla.kernel.org/show_bug.cgi?id=214899

## Speaker audio
Install all the packages listed by Sound Open Firmware.

If your speakers sound tinny due to ALSA only using the tweeters, use the  kernel module parameter.

On more recent kernels (>=6.11.0 at least), use  instead.

## Tablet PC
Install  to get the accelerometer working and enable support for screen rotation in Destop Environments such as GNOME or KDE.

Check out Tablet PC for more information.

## GNOME Screen Rotation
See Tablet PC#With GNOME 2.

## Fingerprint reader
There is experimental support for the Goodix 55b4 fingerprint reader this laptop ships with. Thanks to the Goodix Fingerprint Discord.

To get it working:

# Install  and
# Follow the instructions at https://github.com/goodix-fp-linux-dev/goodix-fp-dump#how-to-use-it to reflash the firmware of the fingerprint reader
# Start the  service for the first time and enroll fingerprints in your DE or following instructions in fprint

There is a known issue with this experimental driver where sometimes after a long sleep mode period you will need to restart the fprintd service to get it working again.

## Screen flickering
If you see screen flickering or stuttering, follow the instructions at Intel graphics#Screen flickering.
