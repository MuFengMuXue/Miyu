# ASUS ROG GX650P

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| GPU (AMD) ||  ||
|-
| Speakers ||  ||
|}

## Installation
Press the  key when the ROG logo appears to enter the laptop's UEFI. To boot into the installation medium, disable Secure Boot in the UEFI interface by deleting all related keys after backing up your keys. It is recommended to use a wired network during installation because wireless network connections can be non-trivial to deal with for now (see #Bluetooth and Wi-Fi).

## Bluetooth and Wi-Fi
Both the Bluetooth and Wi-Fi on this device are supported by MediaTek mt7922, which is driven by . As of kernel 6.4.2 in July 2023, two kernel patches and firmware updates are still required. First check your device with:

It is likely that one will lack the line  without further setup since the kernel module is not properly loaded.

Start with a fresh boot, i.e. completely shutdown your device and boot your device; one might encounter an error log similar to this in the journal:

It is recommended to patch to fix device init failed so that Wi-Fi can work. Further, to support Bluetooth, another kernel patch should be applied.

## Speaker
Due to the insufficient amplifier setup (Cirrus Logic CS35L41) on Linux, the sound turned out to be tiny. Follow the guide on asus-linux and add quick with this kernel patch (for 6.4.2) to fix the issue. In general, one might need to

# Dump ACPI table and patch SSDT
# Install and load the SSDT patch with the corresponding boot-loader
# Apply the aforementioned kernel patch

When all the problems have been solved, the log might look like this,

If there is a lack of some line, e.g. the firmware is not successfully loaded, one should check if the kernel patch is patched successfully.

## Recommendations
## ASUS Linux
ASUS Linux is a project that enhances ASUS laptops' user experience with a series of utils, including:

; asusctl: enables platform profile control, GPU mode switch, and BIOS control, etc.
; supergfxctl: enhances GPU mode switch

## Known issues
* mini-led is not enabled if  is used even after this kernel patch, while booting with  in  works well.
* Booting with discrete GPU results in a black second display.
* The refresh rate under KDE with the Xorg backend is significantly low. Wayland is recommended for two screens, with DPI scales of 1.0 and 1.5, correspondingly.
* S0ix mode (see Power management/Suspend and hibernate) is not working.
* After upgrading to BIOS version 306 (released in 2023/07/19), the screen turns white in KDE and flash under Wayland. The solution is to add  to kernel parameters.
