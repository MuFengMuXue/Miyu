# Framework Laptop 16

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||   ||
|-
| Keyboard Module - ANSI || ||
|-
| Keyboard Module - ISO || ||
|-
| Numpad Module || ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Bluetooth ||  ||
|-
| Accelerometer ||  ||
|-
| TPM || ||
|-
| Ambient light sensor || ||
|}

This article covers the installation and configuration of Arch Linux on a Framework 16 Laptop.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Installation
Follow the installation guide up to and including the creation of an installation medium. Plug the install media into any of the expansion ports, and press the power button.

The first boot after assembly can take up to 30 seconds to perform memory training, but if it takes longer (up to a few minutes), refer to #Problems booting.

If you get the error , refer to #Disabling Secure Boot.

Continue from the second step of Installation guide#Boot the live environment until the end, then read through the rest of this article to setup framework specific hardware.

## Problems booting
The first boot after assembly can take up to 30 seconds to perform memory training, but if it takes longer (up to a few minutes) the LEDs next to the expansion modules should flash an error code. The first part of the code (Diagnosis) can be decoded using Framework's documentation, and the second part (POST Code) can be decoded using a list of codes.

## Disabling Secure Boot
If you get the error , you may need to disable secure boot.

# Unplug the install media.
# Press the power button to power off.
# After a few seconds press it again to power back on.
# Press  to clear the error.
# Select Administer Secure Boot, change Enforce Secure Boot to Disabled.
# Re-insert your install media.
# Press  (You may have to press ) then  to save changes.

## Hardware
Framework is intended to be a configurable and upgradeable laptop. The lists below is not intended to be an exhaustive list of all the hardware sold with the framework, but rather a list of tested components.

## Wi-Fi
You will be limited to 802.11n (Wi-Fi 4) and 2.4GHz bands if you do not configure the regulatory domain.

There have been reports of Wi-Fi stability and throughput improvements when using iwd on the 13 inch AMD model, either directly or as the NetworkManager backend. It is unclear if these issues persist on the 16 inch model, which uses the exact same Wi-Fi card.

## Display
The Framework Laptop 16 has an IPS display manufactured by BOE (BOE NE160QDM-NZ6) with a native resolution of 2560 x 1600, 165Hz variable refresh rate and FreeSync support. The panel is uncalibrated from factory, giving a suboptimal default sRGB coverage. It is thus recommended to apply an ICC profile to have better color reproduction. Framework 16 ICC color profile: https://www.notebookcheck.net/uploads/tx_nbc2/BOE_CQ_______NE160QDM_NZ6.icm

## Ambient light sensor
## Hardware
The hardware should work out of the box, you can check by reading directly from the device:

Regardless of Desktop Environment, you'll need to install  and restart your session. As a test, run  and check the output for a message similar to:

## Desktop environment integration
GNOME: No further action required other than [https://help.gnome.org/gnome-help/power-autobrightness.html enabling it.

Plasma: Follow the instructions under the ambient light section of the KDE page.

Other: If you do not use Plasma or GNOME but still want automatic brightness control, check out .

## Audio
## Linux audio compatibility
The speakers do not sound very well out of the box.
To improve that just enable the linux audio compatibility in the bios.

## Easy Effects
To further improve the sound you may use Easy Effects PipeWire#EasyEffects with custom profiles.

First install  and the needed dependencies  and .
Then just follow the installation instructions on the GitHub page.

There are some good profiles available:

* Framework 16 profile by amesb just put it in

* Framework 13 profile by cab404 is made for Framework 13 but also works quite well on the Framework 16. Just follow the instructions in the repository.

## Low volume on Audio Expansion Card
The volume of the sound of devices attached to the Audio Expansion Card can be very low. This is particularly noticeable with headphones. In this case you might want to try increasing the volume in  (available in the  package).

Open , press F6 to select a sound card and select the one labeled . You should now see a single slider labeled , increase it to 100%.

## No sound from speakers
After following the general recommendations and installing the PipeWire sound server and WirePlumber session manager, you may experience no sound coming from the speakers. If you get sound from wired headphones (via the audio jack expansion card) and/or Bluetooth headphones, it may be that pipewire selects the wrong device profile by default.

You can check the current profile using , under the "Configuration"-tab, check the "Ryzen HD Audio controller" (this name may not be the same for all Framework 16 models, but it should be correct on the Ryzen AI 300 series). If the active profile is something like:

 HiFi (Headphones, Mic1, Mic2)

The wrong profile is selected (the Headphones is the giveaway), look for a profile (under the  section) that says . For example:

 HiFi (Mic1, Mic2, Speaker)

Change to this profile, then try playing some audio, to test that this is the issue.

Make the change permanent by creating a drop-in configuration file for WirePlumber:

{{hc|/etc/wireplumber/wireplumber.conf.d/20-set-speaker-profile-as-default.conf|monitor.alsa.rules  [
  {
    matches  [
      {
        "device.name"  ""
      }
    ]
    actions  {
      update-props  {
        "device.profile"  "HiFi (Mic1, Mic2, Speaker)"
      }
    }
  }
]}}

You can find the  with:

 pactl list cards | grep -e "device.product.name" -e "device.name" -e "device.description"

You should find the "Ryzen HD Audio Controller" in that output and use the value for  in the config file.

## Keyboard backlight
The Framework Laptop 16 keyboard and input modules use QMK-based firmware for backlight control. As a result, the keyboard and numpad backlights are not exposed as a standard  device by default.

This means desktop environment tools such as KDE PowerDevil, GNOME settings, and utilities like  will not detect or control the keyboard backlight out of the box.

A userspace bridge is available that exposes the keyboard backlight via  and integrates with UPower, enabling normal desktop backlight controls and unified keyboard/numpad brightness control without kernel patches or firmware changes.

*

## Sensors
Framework has a fork of lm-sensors on their Github To use their mappings, copy [https://github.com/FrameworkComputer/lm-sensors/blob/framework/configs/Framework/Framework16-AMD.conf configs/Framework/Framework16-AMD.conf from the framework branch into .

This seems to be a work in progress, so it is probably worth checking back up on it occasionally and see if any updates have been pushed.

## Fan control
As of 2024-03-17 the software fw-fanctrl can work with the framework 13 and 16 AMD versions.
Just install  and set your desired config in .

## Prevent waking up in backpack
Due to a firmware misconfiguration, the Framework 16 will wake up when its screen flexes onto the keyboard while carried in a backpack: this has been fixed upstream in firmware version 0.31 for keyboard modules and 0.0.4.2 for BIOS.

## Suspend
On AMD at the moment of writing only s2idle is supported. If the battery drain is too high you can test your setup with  using:

The tool tests and reports about your devices sleep and gives you hints on what might be causing battery drain.

See also: [https://community.frame.work/t/responded-missing-deep-suspend-to-ram-sleep-state-on-amd-7040-laptop/41544/5 Missing “deep” (Suspend-to-Ram) sleep state on AMD 7040 laptop.
