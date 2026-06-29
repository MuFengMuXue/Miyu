# Lenovo LOQ 15ARP9

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| GPU (NVIDIA) ||  ||
|}

## Installation
Steps from the Installation guide can be followed to install a working copy of Arch Linux.

## Accessibility
The firmware is GUI-based. It supports both keyboard navigation and mouse navigation. To access UEFI settings, repeatedly press  while the computer is starting. There are no audio cues once the menu is open.

Additionally, pressing  will lead the user to an interim menu which serves only for quick access to a very limited set of options. Entering settings proper requires pressing another button.

## Firmware
Firmeware updates through fwupd are supported for the NVME drive, touchpad, CPU, TPM and UEFI.

## Suspend
This laptop only supports S0ix (also known as Modern Standby or s2idle) as the power management mechanism on both Windows and Linux distributions. This can be verified through the file , which only displays one entry:

The option to enable suspend-to-RAM exists, but is hidden behind advanced BIOS settings and leads to an unresponsive kernel on resume.

By default, the device will either fail to suspend or more commonly fail to resume from suspend.

Scenarios include:

* Suspending appears to work. On resume, fans begin spinning, but the screen backlight does not turn on. Userspace is unresponsive.
* Suspending appears to work. On resume, fans begin spinning and a few seconds later the device reboots.
* Suspending appears to work. Resume is impossible, as the device does not react to any input.
* Suspending does not work. The screen may turn off for a second before coming back.

Which scenario occurs is inconsistent and may change seemingly at random as a result of unknown factors.

Achieving functional suspend/resume requires creating a file in  such as  and enabling S0ix support in the NVIDIA driver through the following parameter:

Status of S0ix support can be verified through :

 under  indicates that the driver is configured to suspend under S0ix.

No other workarounds are necessary. In particular, the following should be avoided:

* Passing  on the kernel command line. This does actually bring suspend/resume to a functional state, but it completely disables ASPM and will certainly lead to increased power usage.
* Using NVIDIA parameters such as  or , or any other options related to S0ix. The option recommended above is also the officially recommended method to configure S0ix support in NVIDIA drivers.

Resuming from suspend may still not work despite enabling the GPU drivers' S0ix support. This is likely caused by a #Firmware suspend bug, for which the linked section provides a solution.

This section is based on findings in an Arch Linux Forum thread === Hibernation ===

Hibernation does not work with early KMS. To achieve working hibernation, remove NVIDIA modules from . Read the page on hibernation and make sure your system is correctly configured to resume.

There is a bug in both proprietary and open NVIDIA drivers where suspending fails if the system has previously been resumed from hibernation. Suspending in sequence and hibernating in sequence works, but if you attempt to execute a sequence of hibernate-resume-suspend-resume, the NVIDIA driver crashes and the screen does not come back on.

As of December 8th 2025, the issue is tracked internally by NVIDIA according to communication on the NVIDIA Developer Forum[https://forums.developer.nvidia.com/t/resume-from-suspend-fails-on-system-previously-resumed-from-hibernation/346698.

## Firmware suspend bug
If dual booting, Windows updates may trigger the BIOS to enter a confused state. This may happen only after booting into Linux. In this confused state, suspending will not work correctly on Linux, even if S0ix support is enabled in NVIDIA drivers. This confused state will persist between reboots into different operating systems and attempts to sleep on Windows.

Whether this bug is triggered only by dual booting Windows, only by sharing an EFI partition or happens as a result of some other factor is unknown at this time. Windows will still be able to suspend and resume in this state, although the fans will remain on, indicating that the laptop did not suspend fully.

One way to tell if this issue is the root cause of problems with suspend is if the LEDs around the power button start flashing every time the screen backlight is off. Normally, the power button should only flash if the laptop is suspended. If you observe flashing during moments where the backlight is off but the laptop is not suspended (for example while booting up or logging into a graphical environment), your device is likely affected by this issue.

In order to restore the firmware to a state where suspend works again, first check the firmware version with :

Make sure the BIOS version is PQCN24WW released on June 2nd 2025 or newer. Note that the  field returned by  is in the  format. You may use Lenovo Vantage on Windows or fwupd to update the BIOS.

To eliminate all other possible root causes, ensure a clean slate by removing all configuration related to power management in the Arch Linux installation. In particular, remove any NVIDIA driver parameters other than . Restore kernel parameters to the absolute minimum, for example:

Reboot the device and enter BIOS configuration by repeatedly pressing the  key after the screen turns off and on until you see the main menu. Press More Settings to enter the actual configuration menu.

Navigate to the Exit menu and select the Load Default Settings option, then confirm the dialog that appears. Finally, press F10 and confirm to save and quit. This restores all BIOS settings to factory defaults and is a crucial step, even if you never changed any BIOS setting.

If you have some BIOS settings you want to keep, write them down before loading defaults and restore them on the next boot.

Upon next boot, suspend and resume should work again.

## Advanced BIOS settings
More configuration options exist than presented by default in the proper BIOS configuration menu.

Getting access to these options requires taking the following steps:

* Repeatedly press  during boot to enter the quick access menu.
* Enter the proper BIOS configuration menu.
* Press the key combination  twice.
* Save and exit (this can be done through the  shortcut). The device will reboot.
* Immediately on this next boot repeatedly press  again to enter the quick access menu.
* Enter the proper configuration menu.
* More options should be visible.
* Upon exiting settings in any way, advanced options will once again be hidden.
