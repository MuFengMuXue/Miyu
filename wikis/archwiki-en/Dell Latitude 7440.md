# Dell Latitude 7440

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam || ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||   ||
|-
| Fingerprint reader ||  ||
|-
| TPM || ||
|-
| Touchscreen || ||
|-
| Fn Keys || ||
|-
| Suspend to RAM || ||
|-
| Suspend to disk || ||
|}

## Installation
As of mid 2023, installation from USB medium is relatively smooth except for the webcam driver, which is currently barely supported and only works through a workaround that is extremely tedious to install. It does work though, see below.

## Graphics
Do not install the  package: it makes things worse, as you can verify using glxgears from the  package.

## Audio
Audio (both speakers and microphone) works out of the box. You might have to unmute the speakers and/or the microphone using e.g. .

## Disks
Disks are recognized in AHCI mode. RAID mode untested.

## Touchpad
Works out of the box, but without some essential gestures (e.g. paste from primary clipboard with three-finger tap). In Xorg, you can use libinput to activate the tap paste, and then create an Xorg configuration file to save the setting across reboots, e.g.:

## Webcam
Works but requires tedious installation of drivers, firmware and other software. To make a long story short, Intel decided to ship IPU6/MIPI webcams including the one on this laptop without first upstreaming drivers into the linux kernel. It then turned out that the camera requires not just a driver, but a whole separate substack because certain operations that are typically performed within the camera silicon are now delegated to the CPU/GPU. Dell ships Ubuntu "certified" laptops with this camera using a workaround that creates a "virtual camera", but the code is scattered across multiple packages, several of which require custom PKGBUILDs. A recipe to get it working as of kernel 6.4.2 is listed here.

Efforts are under way by Intel and the Linux kernel community to support this webcam out of the box, but it might take a year or two (i.e. 2024-2025).

## Fingerprint reader
 is required for the fingerprint reader to be working. The package  needs to be installed as well, as described in Fprint.

## Firmware
Dell provides firmware updates that can be installed automatically using fwupd.

It is possible to install custom Secure Boot root keys in the BIOS and use them for Secure Boot with Linux.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Toggles Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  || 3
|-
|  ||  ||  || 3
|-
|  ||  ||  || 4
|-
|  ||  ||  || Toggle Keyboard Backlight Brightness 0%/50%/100%
|-
|  ||  ||  || 3
|-
|  ||  ||  || 3
|-
|  ||  ||  || It appears to be
|-
|  ||  ||  || None
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
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# Keypress is best handled via ACPI events, e.g. the  package/service.
# Keypress is only recognized via ACPI (e.g.  as . User reports it used to be recognized as  on a fresh installation, but it somehow does not work anymore.

## Accessibility
## BIOS Settings overview
The "BIOS Settings" interface can be reached by pressing  during POST.

The BIOS settings page itself is GUI based. There is a panel taking approximately 20% of the screen on the left, containing various sub-categories of settings. The main panel takes 80% of the screen to the right, and contains the settings associated with each sub-category. The font is relatively large, and toggle switches will appear as light grey if set to 'off', and turn light blue if set to 'on'.

The BIOS can be updated through the "One-Time Boot Menu" (press  during POST).

## BIOS Settings navigation
The "BIOS Settings" interface can be navigated using a keyboard, or mouse - with mouse being the preferred mode. Keyboard navigation keys are as follows:

{| class="wikitable"
|-
! Key
! Effect
|-
|     || Moves to the previous field.
|-
|   || Moves to the next field.
|-
|  || Selects a value in the selected field (if applicable) or follow the link in the field.
|-
|  || Expands or collapses a drop-down list, if applicable.
|-
|    || Moves to the next focus area
|-
|    || Scrolls the currently selected view up.
|-
|    || Scrolls the currently selected view down.
|-
|    || Moves to the previous page until you view the main screen. Pressing Esc in the main screen displays a message that prompts you to save any unsaved changes and restarts the system.
|}

## Diagnostics
Pressing  during POST starts the "One-Time Boot Menu" (if enabled in BIOS). There the diagnostic option can be found, which offers various thorough on-board tests.

If  is held while powering on, the "Display panel built-in self-test" (LCD-BIST) is initiated. The screen will cycle three times through solid colors before powering off again. This can be used to make sure all colors are displayed correctly without distortions and no dead pixels are present.
