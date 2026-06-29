# HP ProBook 4530s

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (AMD) || ||
|-
| Bluetooth || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Webcam || ||
|-
| Card reader || ||
|-
| Touchpad || ||
|}

## Fan throttling
The fan can be controlled (throttled) in software, otherwise it never shuts off, even if the BIOS option "Fan always on while on AC power" is disabled. There are two programs supporting the 4530s:

* NoteBook FanControl. NBFC have pre-made profile for HP ProBook 4530s.
* probook_ec.pl script daemonized in Python and in Ruby

## Intel CPU microcode
See Microcode page.

## Network
Both the wired and wireless network cards (with the exception of the ralink RT3592 and RT3590) works out-of-the-box. The Atheros card requires the ath9k module, and the Realtek Ethernet card requires the r8169 module. More information can be found at Wireless network configuration#ath9k

## WLAN BIOS whitelist workaround (experimental)
HP BIOS allows only certain WLAN cards (whitelisting) to be used. This can be worked around by adding the following as the first GRUB command in every OS entry:

 write_dword 0xFED1F418 0x1F501FEB

You can read more on engineering this hack here. It is confirmed to work on the 4330s, 4530s and 4730s, but consider it experimental.

## Bluetooth
Sending/receiving files and switching Bluetooth on/off works. The ath3k module is required.

## hciconfig -a
## Graphics
Intel HD Graphics 3000 is supported by the open-source  driver. Dual-head with HDMI works. If using hybrid graphics in conjunction with AMD, open-source ATI driver should be used for GPU card (proprietary driver is not available, see Graphics processing unit#AMD (ex-ATI)). For dynamic switching can be used PRIME technology. ATI driver should be installed along with xf86-video-intel to support hybrid (Intel) GPU.

## Brightness
Controlling screen brightness with the keystrokes  and  works in Gnome 3, KDE and MATE and has not been tested in other desktop environments.

## Touchpad
Touchpad function works with  package. Disabling touchpad using the top-left corner double tap works with  and  () packages.

## Miscellaneous hardware
## Card reader
SD cards tested and working. With 3.4.7 kernel, Memory Stick card works as intended.

## Function keys
Module hp-wmi is likely to be required for the keys to work. In Gnome 3 and MATE every  key works.  key requires gnome-power-manager installed.
Keys above numeric keypad are also recognized. The  key has a XF86HomePage symbol (opens home page),  key has NoSymbol and switch fly mode in Gnome 3 (has not been tested in other desktop environments).

## Camera
Works with  module.

## HP DriveGuard
Works with  package.

## Power
Module acpi-cpufreq and at least one of CPU governors (cpufreq_ondemand, cpufreq_conservative, etc.) are required. More information on CPU frequency scaling.

## Suspend and hibernation
Both suspend and hibernation work with pm-utils and kernel backend.

## Sensors
 shows one acpitz-virtual device with 4 working temperature readings and coretemp-isa device which has one sensor for each CPU core.
It does not show any info about fans RPMs.
