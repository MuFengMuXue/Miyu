# Lenovo Yoga C940

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard || PS/2 ||
|-
| Touchscreen ||  ||
|-
| Stylus ||  ||
|-
| Video ||  ||
|-
| Webcam (Acer) ||  ||
|-
| Webcam (IMC) ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint Reader ||   ||
|}

## Installation
To access the boot menu and UEFI, use . Disable Secure Boot. UEFI boot works fine.

## Accessibility
The UEFI user interface (both Vanilla and patched − see #Audio) is graphical. An option to switch to a text-based GUI is not provided. However, the options may be selected with the arrow keys and the values changed with  and  keys.

## Function keys
By default, the  key does not need to be pressed to toggle the alternative function of the  keys, and  actually sends the  key signal. This behavior can be reversed in the UEFI.

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
|  ||  ||  ||  (No change, despite the "Refresh" pictogram)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
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
|  ||  ||  || Changes keyboard backlight
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd-logind handles this by default.
# Press and release signals are sent on physical key press, nothing occurs on physical release.

## Video
By default on Xorg, tearing is apparent when playing videos. See Intel graphics#Tearing.

There seems to be issues with Chromium based GPU acceleration, see Intel graphics#Corruption or unresponsiveness in Chromium and Firefox.

## Audio
This laptop is equipped with 2+2 speaker combo: two on the hinge ("front speaker") and two on the bottom (wired on a single "bass" channel).
The latter requires a custom initialization sequence that is not supported on mainline Linux (see bugzilla.kernel.org#205755). Therefore, two options are possible: either use the vanilla configuration and rely only on the front speakers, or flash a beta BIOS an activate the full speaker array.
In both cases, Sound Open Firmware is required in order for the soundcard to work.

## Vanilla configuration
You need to blacklist the  and  modules for the soundcard to correctly work.

## Using a beta BIOS
There exists an unreleased patched BIOS (from Lenovo) that initialize correctly the bass speakers, see comment 59. It is now only available on a mirror, which details the flashing procedure.

If you did not follow the former advice and bricked your device, a procedure exists to emergency flash the BIOS, which can also be used to downgrade it:

* Format a USB key to FAT32
* Copy the desired BIOS on the key (or the one provided in this post, guaranteed to work), and rename it to
* (Force) shut down the computer, and plug it on AC power.
* Insert the USB key
* Boot while maintaining the key  during 10 seconds

The power indicator should blink orange rapidly, and the screen backlight will turn on after 2-3 minutes. Then, a scrambled progress bar will appear and slowly filled. Once completed, the computer will reboot with the desired BIOS restored.

## Thermals
Thermal shutdowns are a problem unless you install  or .

## pstate-frequency
 allows the user to define Turbo Boost behavior and maximum clock frequencies. The user should activate  and  for the setting to persist after suspend or reboot. Configuration files are located in .

Changing the line  to  in  will throttle the maximum clock speed from 3.90 GHz to 2.70 GHz on AC. Moreover, the default plan of pstate-frequency will throttle the CPU to 30 % (around 1.2 GHz; see ) on battery power, removing the issue of thermal shutdowns.

## thermald
A few changes are necessary for  to work as intended:

Add the following thermald config:

You might wish to tweak the target temperature (i.e. 64000) if you are OK with your machine running a bit hotter.

Edit  and remove  and add  to the  line:

 ExecStart=/usr/bin/thermald --systemd --dbus-enable --ignore-default-control

Manual fan control does not work at all.

## Power management
Battery Conservation Mode (charge to max 50%) can be set with:

 # echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004\:00/conservation_mode

where  could vary depending on the model.

If shutdown is not working and the system hangs on "reboot: Shutting down", try adding  to your Kernel parameters.

## Tablet mode
By default, the kernel cannot detect when the device is folded keyboard-down (360 tablet mode),  adds a driver. If the desktop environment supports it (eg. KDE, Gnome, Sway) then the touchpad and keyboard will be disabled when the device is folded by default, and may offer more touch-friendly functionality.

## Fingerprint reader
Fingerprint reader requires a beta custom library based on a reverse-engineered Windows driver, . Once installed, the fingerprint reader must be configured following fprint's procedure.

If you have the goodix reader (), you can use this driver . Note: you will need to flash your device with goodix-fp-dump to use this
