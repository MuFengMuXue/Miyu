# HyperX Cloud Alpha Wireless

The HyperX Cloud Alpha Wireless is a wireless gaming headset from HyperX (HP, Inc). While the headset functions as a standard USB audio device on Linux, the companion features (battery monitoring, sleep timer, mic monitor, voice prompts) require additional software as the official HyperX NGENUITY application is Windows-only.

## Features
The following features are available on Linux through the  package:

{| class="wikitable"
! Feature !! Status
|-
| Audio playback/recording ||
|-
| Battery monitoring ||
|-
| Sleep timer (10/20/30 min) ||
|-
| Mic monitor (sidetone) on/off ||
|-
| Voice prompts on/off ||
|-
| Mic mute status ||
|-
| Mic connect/disconnect ||
|-
| Charging status ||
|-
| System tray icon ||
|-
| Settings persistence ||
|-
| Equalizer / DTS surround ||
|-
| Sidetone volume level ||
|}

## Installation
Install  from the AUR.

Alternatively, build from source:

 $ git clone https://github.com/WaffleThief123/HyerpxAlpha-Linux
 $ cd HyerpxAlpha-Linux
 $ cmake -S . -B build
 $ cmake --build build
 $ ./install.sh

## Dependencies
*  - GUI framework
*  - USB HID communication
*  - udev support

## Configuration
## udev rules
The package installs a udev rule to  that grants access to the headset's HID interface without root privileges:

 SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03f0", ATTRS{idProduct}=="098d", MODE="0666"
 SUBSYSTEM=="usb", ATTRS{idVendor}=="03f0", ATTRS{idProduct}=="098d", MODE="0666"

After installing, unplug and replug the headset's USB dongle for the rules to take effect.

## Settings file
Settings are stored in  (defaults to ). The file is a simple key-value format:

 sleep_timer=2
 voice_prompts=1
 mic_monitor=1

Settings are saved automatically when changed in the GUI and restored when the headset reconnects.

## Usage
Launch the application:

 $ Hyperx

Launch minimized to the system tray:

 $ Hyperx --systray

Enable HID packet debug logging:

 $ Hyperx --debug

Flags can be combined:

 $ Hyperx --systray --debug

## Autostart
The package installs a desktop entry to . To start the tray app automatically at login, copy it to your autostart directory:

 $ cp /usr/share/applications/hyperx-alpha.desktop ~/.config/autostart/

## System tray
The  option requires legacy system tray support. This is available natively in KDE, Xfce, and LXQt. For GNOME, install a tray extension such as .

## HID protocol
The headset communicates via USB HID using vendor ID  and product ID . All commands use 31-byte packets prefixed with .

{| class="wikitable"
! Byte!! Byte[3 !! Direction !! Description
|-
|  ||  || Receive || Connection state (disconnect/connect)
|-
|  || || Send/Receive || Microphone state query
|-
|  ||  || Receive || Sleep timer state (10/20/30 min)
|-
|  ||  || Receive || Voice prompts state (off/on)
|-
|  ||  || Receive || Battery percentage (0-100)
|-
|  ||  || Receive || Ping / charging status
|-
|  ||  || Send || Mic monitor off/on
|-
|  ||  || Send || Set sleep timer
|-
|  ||  || Send || Voice prompts off/on
|-
|  ||  || Receive || Mic disconnected/connected (physical)
|-
|  ||  || Receive || Mic monitor off/on confirmation
|-
|  ||  || Receive || Mic unmuted/muted (physical button)
|-
|  ||  || Receive || Power off/on
|}

Use  to log raw HID packets to stdout for further protocol analysis.

## Equalizer
The equalizer and DTS Headphone:X spatial audio features in HyperX NGENUITY are implemented entirely in the Windows audio driver. They are not HID commands sent to the headset and cannot be replicated through this application.

For equalizer functionality on Linux, use a PipeWire or PulseAudio equalizer plugin:

*  - GUI equalizer for PipeWire
*  - for PulseAudio setups

## Troubleshooting
## Device not found
Verify the dongle is detected:

 $ lsusb | grep 03f0:098d

If it appears but the application cannot access it, check that the udev rules are installed and the dongle was replugged after installation.

## Settings not applying on reconnect
The application delays settings restoration by 2 seconds after the headset powers on to allow the firmware to finish initializing. If settings still do not apply, power cycle the headset and wait for it to fully reconnect.

## System tray icon not appearing
Ensure your desktop environment supports legacy system tray icons. See #System tray.
