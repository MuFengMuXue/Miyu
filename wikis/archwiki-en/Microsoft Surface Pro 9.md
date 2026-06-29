# Microsoft Surface Pro 9

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Touchscreen || ||
|-
| Digitizer Pen ||  ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| rowspan=2 | Thunderbolt 4 ||  ||
|-
|  ||
|-
| TPM || ||
|}

This page aims to document specific information on getting Arch Linux working on the Microsoft Surface Pro 9 tablet with Intel Processor.

## Installation
Hold  key on the tablet to enter UEFI setup utility. Disable Secure Boot, enable booting from the external USB devices, then boot from the installation media.

Since the Linux kernel does not ship required drivers to use the detachable keyboard, touchscreen and stylus, you have two options to control the operating system:

* Plug in a USB keyboard into a free USB port and continue the installation process as usual.
* Remaster the Archiso and include drivers and kernel from the linux-surface project.

## Secure Boot
It is possible to set the tablet to use only user-provided keys in UEFI setup utility, but the default options allow only either using MS keys, or MS + 3rd Party CA, or disabling the Secure Boot.

The procedure of setting up the secure boot is as follows:

*Disable Secure Boot
*Follow Secure Boot for general setup until the key enrollment.
*Make sure that enrolling keys is the last action you would do with the Secure Boot before shutting down the machine. In other words, for example, either  (only 3rd Party CA only), or  (MS + 3rd Party CA) commands must be entered before shutting down.
*Shutdown the tablet. Do not reboot, do not reboot into the UEFI firmware setup directly.
*Turn the tablet back on and hold "Volume Down" key.
*Navigate to the "Security" section in the menu. If it says that it needs the reboot to access the settings, select the "Reboot to UEFI" option on the same page.
*After the reboot, navigate to the "Security" section again. Verify that the Secure Boot is enabled automatically. If the text says "Secure Boot is Enabled with custom key configuration", then it means that UEFI enabled the hidden option to use only third-party CAs and keys automatically. Never select any other option there if you want to keep using your own keys.
*Reboot to the operating system and verify that the Secure Boot is enabled. E.g.  should tell that the Secure Boot is enabled.
