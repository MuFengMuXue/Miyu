# Lenovo ThinkPad T14/T14s (Intel) Gen 3

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| TrackPoint || ||
|-
| GPU (Intel) ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth || ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
| Mobile broadband || ||
|-
| Fingerprint reader ||  ||
|-
| Smartcard Reader || ||
|}

The Lenovo ThinkPad T14/T14s (Intel) Gen 3 was introduced in 2022. It features a 14" screen, 12th-gen Intel Core processors, and integrated Intel Iris Xe graphics.

To ensure you have this version, install the package  and run:

For a general overview of laptop-related articles and recommendations, see Laptop.

## Intel Turbo Boost
Check that Intel® Turbo Boost Technology 2.0 is enabled using

 $ cat /sys/devices/system/cpu/intel_pstate/no_turbo

An output of 1 means it is not enabled, so you will have to reset your BIOS to defaults. After doing that, running the command again should print 0.
You should be able to see your CPU boosting way higher.

## Firmware
With fwupd you can update System Firmware (UEFI). The version available in  is more recent (1.15) than in the BIOS update ISO (1.14).

There are some devices that supports updating, but currently have no available updates in  or  repositories. Probably updates can be extractes from Windows updaters.
They are:
* ELAN0676:00 04F3:3195 - this is a trackpoint
* Fingerprint Sensor
* Integrated RGB Camera - there are downloadable windows updaters (Azurewave 1SF54AA: 2252 / Bison BNK919KSE: 5711 / LuxVisions 0SF108N3: 0004 and LuxVisions 1BF208N3: 1024 / Bison BNK5U6VE8: 6717)
* Intel Management Engine - there is downloadable windows updater (16.1.25.1932 as of 2023.08.15)
* UEFI Device Firmware - 12 entries with such name. Probably for nfc, smartcard reader, etc.

Some updates are available out of the box:

* UEFI revocation list (dbx)
* Battery
* Samsung NVMe SSD

And if you enable , you can also update:
* Embedded Controller

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
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
|  ||  ||  || Unknown
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggle keyboard backlight3
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# Works out of the box, but it can be controlled by software.

## Mobile broadband
See NetworkManager#Mobile broadband support.

## Audio
This laptop requires Sound Open Firmware for the internal sound card to work. Install .

Audio quality might still be muffled or lower quality than expected. The lower sound quality is due to the missing Dolby Atmos Convolver.

The quality difference is massive, converting the speakers from sounding tinny and cheap to something actually enjoyable.

You can download the "Movie", "Music", and "Dynamic" presets here: https://stuff.kurz.pw/arch/P14s_G4/Speakers/. They were created on a P14s G4 AMD (identical to T14) with Windows 11.

To enable Dolby Atmos Convolver, install EasyEffects and open it. On the left side of the UI, go to Effects > Add Effect > Convolver.

Then on the right side of the UI go to Impulses <, select Import Impulse and select one of the  files you downloaded. You can then activate them from the Impulses < popover.
