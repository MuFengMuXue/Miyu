# MSI P14

Also known as Prestige 14 or A10RB/A10SC/A10RAS
{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU (Intel) || ||
|-
| GPU (nvidia) || ||
|-
| Webcam ||  ||
|-
| IR Camera || ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|}

## Installation
Secure Boot needs to be disabled at first startup, but it can be configured later. This laptop supports keys reset to factory and custom keys install.

This laptop has advanced UEFI settings if desired.

## Power management
Recommended TLP settings:

Undervolting is quite recommended on this laptop, and it needs to use the  package. Depending on the processor, it can reach up to -150mV, but -100mV should work on any configuration.
Note that the laptop tends to go unstable on battery when undervolted, so enabling the undervolt only on AC could be a good solution.

## Thermals
Fan control can be tuned by https://github.com/YoyPa/isw. Configuration entry for P14 is missing, and needs to be added manually (PR: https://github.com/YoyPa/isw/pull/97):

These settings will be reset on plug/unplugging power source, it can be solved by a dirty hack:
{{hc|1=/etc/udev/rules.d/isw.rules|2=
SUBSYSTEM=="power_supply", ATTR{online}=="0", RUN+="/usr/sbin/systemctl restart isw@E14C2IMS.service"
SUBSYSTEM=="power_supply", ATTR{online}=="1", RUN+="/usr/sbin/systemctl restart isw@E14C2IMS.service"
}}
and reload udev rules:
 $ udevadm control --reload-rules

## Passive cooling
Some users could be interested in Passive cooling mode. It is quiet and energy efficient.
This notebook works well in passive cooling mode. To enable it, you need to completely disable turbo mode and tuning fan settings.

TLP settings to disable turbo boost:

ISW settings:

With these settings, the fan will start only when the discrete GPU is in use.
