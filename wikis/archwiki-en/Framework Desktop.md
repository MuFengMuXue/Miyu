# Framework Desktop

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| NPU ||  ||
|-
| TPM || ||
|}

This article covers the installation and configuration of Arch Linux on a Framework Desktop.

## Accessibility
The firmware is GUI-based. It supports keyboard navigation as well as mouse navigation. To access firmware settings, press  while the computer is starting. The firmware does not provide an audio cue to indicate that it has entered the settings menu. There are no accessibility-specific options or modes available.

OCR assistive tools can read the text well, but struggle with presenting the UI's layout in a useful way for navigation.

The default text size is a little larger than average. The background color is black, and the selected menu option is highlighted with a strongly contrasting colored box, either bright orange or bright green depending on the menu.

## Disabling Secure Boot
Installing Arch requires disabling Secure Boot. Here is a detailed, keyboard-only description of that procedure:

# Power on the system, or press  to reset if it is already running.
# While the system is starting press  until the settings menu appears. It features a bright orange box in the top left quadrant of the display. If you cannot see the display at all, pressing  for 2 minutes should reliably get you to the settings menu.
# Press  to select the Administer secure boot option. The orange rectangle will move to the lower left quadrant of the display.
# Press  to access secure boot settings.
# The Enforce Secure Boot setting is the second entry in the settings list. Press  then  to select it.
# Press  to select Enabled, or  to select Disabled. The desired value will be selected regardless of the initial state.
# Press  to confirm your choice, or  to cancel without changing the setting.
# Press  then  to save changes and reboot.

## Selecting a boot device
To boot from a USB stick:

# Power on the system, or press  to reset if it is already running.
# While the system is starting press  until the settings menu appears. It features a bright orange box in the top left quadrant of the display. If you cannot see the display at all, pressing  for 2 minutes should reliably get you to the settings menu.
# Press  to select the boot menu. The orange rectangle will move to the upper middle of the display.
# Press  to access the boot menu.
# Select the EFI USB Device (USB) menu entry. It should be near the bottom of the list, below the menu entries for any already installed OSes. Pres  to boot.

## Installation
To avoid the  error, start by disabling Secure Boot as explained above.

Secure Boot settings are separate from other UEFI settings, and are only accessible from a full reboot. Do not go to system settings directly from the boot failure screen without rebooting, there will be no Secure Boot settings in there.

Follow the installation guide up to and including Prepare an installation medium.

Plug the installation media into any of the expansion ports, and press the power button. The first boot after assembly can take up to 30 seconds to perform memory training.

Continue with Installation guide#Set the console keyboard layout and font, then read through the rest of this article to setup Framework specific hardware.

After installation, consider re-enabling Secure Boot instead of leaving it disabled.

## Firmware
fwupd supports updating the UEFI BIOS out of the box. Early access to new updates is available by enabling the LVFS testing remote.

## Wi-Fi
You will be limited to 802.11n (Wi-Fi 4) and 2.4GHz bands (the "world" regulatory domain) if you do not configure the regulatory domain for your country.

## Unified memory
The Framework Desktop's CPU and GPU share the same memory pool. The UEFI allows you to set the minimum amount of memory reserved for the GPU. The  driver can dynamically allocate more than the minimum, up to the maximum configured in the  kernel module.

By default, the guaranteed minimum GPU RAM is 512MiB, and the maximum limit is 64GiB.

To change the minimum video memory reservation:

# Reboot and hit  until the BIOS settings appear.
# Enter the settings menu
# Go into the Advanced > iGPU Memory Configuration submenu
# Select the Custom setting, and enter the amount of reserved video memory you want, from 512MiB up to 3/4 of the total RAM in your system.
# Save the changes and reboot

To change the maximum limit, change the module parameters of the  kernel module. A straightforward way to make a persistent change is with:

The values are a number of 4KiB memory pages. To convert, multiply a value in GiB by 262144. Some common values you might want:

{| class="wikitable"
|-
! GPU memory limit !! pages_limit/page_pool_size
|-
| 16GiB || 4194304
|-
| 32GiB || 8388608
|-
| 64GiB || 16777216
|-
| 96GiB || 25165824
|-
| 112GiB || 29360128
|}

You can set the limit as high as you want, but make sure the rest of your system would be able to run if the GPU tries to allocate the maximum. For a 128GiB system, Framework recommends an upper limit of 112GiB, which guarantees that the rest of the system will always have at least 16GiB.

## CPU frequency scaling
By default, the Framework Desktop uses the  scaling governor in the  profile. This optimizes for low power consumption at the expense of performance.

For a desktop, you probably want to switch to the  profile, as there is no battery to conserve and the SoC is still quite power efficient even in the high performance profile.

See CPU frequency scaling for options to manage the scaling governor configuration.

## Known Issues
BIOS version 3.04 has a known issue where some users report a long delay (1-2+ minutes) in hand-off between GRUB and the kernel on boot. Downgrading to 3.03 fixes this issue. (Related: Framework Forum 3.04 BIOS annoucement thread.)
