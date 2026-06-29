# Steam Deck

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| microSD card reader ||  ||
|-
| Wi-Fi (LCD/Jupiter) ||  || rowspan=2
|-
| Wi-Fi (OLED/Galileo) ||
|-
| GPU (LCD/Jupiter) ||  || rowspan=2
|-
| GPU (OLED/Galileo) ||
|-
| Audio ||  ||
|-
| Bluetooth (LCD/Jupiter) ||  || rowspan=2
|-
| Bluetooth (OLED/Galileo) ||
|-
| Touchscreen ||  ||
|-
| Steam Deck controls ||  ||
|}

The Steam Deck is a gaming-focused handheld PC from Valve. Since it is completely unlocked and by design has full Linux driver compatibility, it can easily be used as an all-purpose handheld PC with Arch Linux.

## Accessibility
The firmware has white text on black background, which should be fine with OCR. Blind users may still want to request the help of a sighted person to change firmware settings or selecting a boot device.

Navigation can be done with a keyboard and mouse, or the physical buttons ( and ,,,) and tactile screen of the device.

There is a single LED at the top of the device, but it does not provide diagnostic codes.

## Installation
You can install Arch Linux from the SteamOS "Desktop Mode", although this way of installing is more involved than using a USB flash installation medium through the microSD card slot or the USB-C port.

If you choose to use an Arch Linux installation medium, hold down  and press the  buttons to boot on it when starting up the deck.

## Firmware
Updating the firmware works with fwupd.

For the LCD models, firmware F7A0131 is the first to enable support for the  CPU frequency scaling driver.

## Shortcuts
* Hold down  and press the  button to access the UEFI settings,
* Hold down  and press the  button to access the UEFI boot menu (called "Boot Manager" in Valve's documentation),
* Hold down  ("Three Dots" button under the right touchpad) and press the  button to access Valve's boot loader menu,
* Hold down  ("Three Dots" button under the right touchpad) to reset the UEFI settings to their defaults (keep the two buttons other than  held after the first blink of the LED: the LED will blink during the operation and stop once done, then release the buttons).
* With the Deck turned off and plugged into the charger, hold down  ("Three Dots" button under the right touchpad) for 10 seconds, and then unplug the Deck to enter Battery Storage Mode. On LCD models the LED will then flash 3 times, on OLED models the LED will blink blue twice. Battery Storage mode also be entered from the UEFI through Setup Utility > Power Menu.

## Audio
The LCD model's built-in audio works out of the box since kernel version 6.1.

The OLED model's built-in audio requires compatible firmware, kernel and ALSA UCM rules in order to work:

* The following firmware files need to be present in the system. They can be compiled from upstream source, or copied from the steamdeck-dsp package published in Valve's jupiter repository.
:
* Neptune kernel (from the jupiter repository) version 6.1.52 or newer works.
*  1.2.11 or newer needs to be installed. Then, rules for  need to be added, such as by copying  from steamdeck-dsp.
You may want to use the Bazzite kernel instead for audio support on the OLED model.
https://github.com/hhd-dev/kernel-bazzite

For troubleshooting, see ALSA and PipeWire. If ALSA can't access the built-in audio, check the kernel and audio firmware (see ALSA#Firmware and ALSA#Driver configuration). If ALSA works but PipeWire doesn't, check the UCM rules.

## PipeWire
Some applications, notably Wine, cause audio crackling on the OLED Deck's built-in speakers. When using pipewire-pulse, this can be fixed by increasing the minimum quantum size in :

 default.clock.min-quantum = 256

256 is the lowest value that has been observed to work well with wine. Higher, safer values of 512 or 1024 can also be used.

## Bluetooth
A small Bluetooth quirk can be encountered on OLED models: a kernel bug prevents suspending if Bluetooth was turned off since boot. This means turning Bluetooth off requires a reboot.

## Controller
The built-in game controller works out of the box, but is in lizard mode by default. In this mode, the touchpads act as a mouse, and some buttons as keys, while other buttons do nothing. One of the following methods can be used to remap the controller for gaming.

## Raw
On some kernel-firmware-game combinations, the Steam Deck's controller will detect that a game is trying to use it, and switch from lizard mode to emulating a simple Xbox-compatible controller until the game is exited. While this precludes use of touchpads, gyros, and extra buttons that a basic Xbox controller would not have, it requires no configuration and may be preferred over more involved methods for some games.

## sc-controller
You can use  as an alternative to Steam Input.

If the C0rn3j fork listed above gives you trouble with the right touchpad only working as a joystick mouse, or with the right joystick refusing to work in game, try the kozec beta branch.

This is useful if you wish to use complex profiles without using Steam, for non-Steam games, or as a fix for games that send double inputs.

You can use this while using Steam, just ensure the profile you wish to use is selected before launching a game. If you want to go back to the Steam driver, disable sc-controller from its GUI using the green "burger" button on the top left: if Steam is already open it will automatically switch.

## Steam Input
Steam Input can detect and remap the Deck's controls, complete with complex tools such as gyros and capacitive thumbsticks. If Steam is being used to run games, using it to also handle controller mapping may be desirable.

Even if Steam is not being used to run games, it can still serve a dedicated controller remapper – it will create a virtual Xbox-compatible controller under  that respects the mapping configured in the Steam client and can be used by any application. If Steam's role is limited to remapping controls, it can optionally be set to permanent offline mode, and in case of the Flatpak version, most permissions can be revoked.

## OpenSD
Available via , OpenSD is a highly-configurable userspace driver for the Steam Deck. It aims to be lightweight, very fast and provide a way to fully utilize the hardware. Configuration is done through text files and it provides a great user's manual.

## Display
## Orientation
On Wayland, the display and touchscreen work correctly in all orientations, without any tweaks. Depending on the model, the orientation may default to portrait but can be changed as normal in a desktop environment's settings.

On Xorg, a manual orientation fix may be needed depending on the display manager used. If the screen defaults to portrait, it can be rotated using xrandr.

 $ xrandr --output eDP-1 --rotate right

The touchscreen can then be mapped to the proper orientation using xinput.

 $ xinput --map-to-output 'pointer:FTS3528:00 2808:1015' eDP

To have this persist on reboots, create an autostart script.

## Refresh rates
The Steam Deck's display supports a wide range of refresh rates, but display managers will not auto-detect most of them.

On LCD models, only 60Hz is auto-detected, but 50Hz works well when force-enabled via KMS:

 video=eDP-1:800x1280M@50

On OLED models with the Samsung display, 90Hz and 60Hz are auto-detected.

## Brightness
If your monitor is unusually dimmed while booting, give priority to the vendor ACPI driver with a kernel parameter:

 acpi_backlight=vendor

## Gamut
The OLED models are billed as HDR-capable and have a much wider gamut than sRGB, but this causes sRGB-targeting content, including most games, to appear greatly oversaturated.

Fortunately, the display's EDID exposes fairly accurate color information, which can be used to good effect even without any calibration hardware.

GNOME and KDE will automatically generate an ICC profile based on the EDID, which can be used with various desktop applications.

To set up the same color correction for games, run  GUI on the Deck, tell it to generate its own ICC profile from EDID (this is recommended over re-using the profile generated by GNOME since that uses a newer version of the ICC format), then convert that profile to a LUT via DisplayCAL's 3D LUT Maker. This LUT can then be injected into games via .

The above was observed to give excellent results on the Samsung OLED. An even better method would be to tell AMDGPU to load the LUT into its color management pipeline, but while technical capability to do this is being adopted into mainline, documentation is scarce.

## Fan controls
The Steam Deck's fan control can be enhanced by a daemon provided in Valve's jupiter repository, but are fully functional without it.

If you are using a mainline kernel, you need patches from Valve's kernel to expose the corresponding ACPI functionality, for example by installing the user-adapted  ACPI platform driver in DKMS form.

## Battery limiting
If you leave your Steam Deck docked or with the charger plugged in, then it is worth to set a charging limit to a value below 100% to improve the battery life. Either valve's neptune kernel or mainline kernel with kernel patch from valve applied is needed (Example: using ). Then, limiting battery charge level can be achieved by writing the target limit in  where  is  directory containing  file with  written on it. Example for setting charge limit to 80 percents:

 $ echo 80 | sudo tee $(grep -l "steamdeck_hwmon" /sys/class/hwmon/hwmon*/name | sed "s/name$/max_battery_charge_level/")

This can also be set persistently with a udev rule:
{{hc|/etc/udev/rules.d/99-battery.rules|2=
ACTION=="addchange", SUBSYSTEM=="hwmon", ATTR{name}=="steamdeck_hwmon", ATTR{max_battery_charge_level}="80"
}}

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
|  || 3 ||  ||
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
|  "Three dots" ||  ||  ||
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
# systemd-logind handles this by default.

## Mimic SteamOS behavior
## Auto-login
To set your system to automatically login without password:

# Setup automatic login to virtual console.
# Add your desktop environment's startup command to your login shell script.

## Big Picture Networking
To enable Steam Big Picture networking support, you must use NetworkManager.

## Steam client integration
You can launch steam with the  launch option to enable fullscreen UI elements such as login and client updates.

## On-screen keyboard
See KDE#Plasma Mobile, GNOME on-screen keyboard or List of applications/Utilities#On-screen keyboards for information on how to set up an on-screen keyboard.

Steam's on-screen keyboard also fully works, but Wayland will by design prevent it from interacting with other applications' windows. The  library can be injected into Steam to effectively remove this boundary, but this weakens the security inherently offered by Wayland.
