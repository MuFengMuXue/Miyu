# Lenovo ThinkPad T14s (AMD) Gen 3

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Mobile broadband ||  ||
|-
| Bluetooth ||  ||
|-
| Smartcard reader ||  ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo Thinkpad T14s (AMD) Gen 3 laptop. Almost everything seems to work pretty much out the box.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Firmware
Updating the firmware using the fwupd utility works as long as all the relevant options are enabled in the BIOS (Enable Windows Update UEFI Update).

Updating the BIOS firmware also fixes some error that produces the following output from linux:

 Error: Corrected error, no action required.
 Error: CPU:0 (19:44:1) MC15_STATUS0xdc204000000c011b
 [Hardware Error: Error Addr: 0x00000001faa88180
 Error: IPID: 0x0000009600050f00, Syndrome: 0x000001ff0a240700
 ...

## Touchpad
The touchpad works fine on Wayland.

However, some people have an occasional freeze of 3-4 seconds on Xorg.

## Disable wakeup from sleep on touchpad activity
Use the following to disable wake-up events caused by the touchpad. Note that this only applies to the touchpad itself and the integrated buttons for left/right click at its bottom, not the 3 buttons at its top or any other input.

{{hc|/etc/udev/rules.d/99-disable-touchpad-wakeup.rules|2=
KERNEL=="i2c-SYNA8018:00", SUBSYSTEM=="i2c", ATTR{power/wakeup}="disabled"
}}

## Speakers
Speakers work out of the box. How ever, they won't have the same sound quality as on Windows due to the missing Dolby Atmos Convolver.

To enable Dolby Atmos Convolver install EasyEffects, go to Effects > Add Convolver > Import Impulse

You can download the "Movie" and "Music" preset here:

https://files.bestmail.ws/Arch/T14s_G3_AMD/T14S_G3_Music_Movies.irs

They were created on the T14s G3 AMD with Windows 10.

## Display
You can download a calibrated color profile for the 400nits IPS panel.

Some users reported crashes / issue of the display, especially after hibernate/suspend: a fix is to disable panel self refresh by adding  to the kernel parameters.

For full multi display support across USB-C, see DisplayLink#USB 3.0 DL-6xxx, DL-5xxx, DL-41xx, DL-3xxx Devices.

## Network / Wi-Fi
There was a known bug in the  module that could block the resume process, freeze the graphics interface and cause loss of wireless card interface. A manual fix is to disable the  module before hibernate and re-enable it after resume. However, this issue shouldn't be present anymore.

If you still face the issue: See Dell XPS 13 (9310)#Wi-Fi for a systemd service to automate this procedure.

This can be automated via sleep hooks - if the module is unloaded before hibernating or suspending it unloads immediately with no delay, and the resume kernel bug does not happen:

You need to enable  and .

Additionally it might be required to also restart .

## Mobile broadband
Works correctly. Follow instruction from Mobile broadband modem especially section FCC unlocking.

## Smartcard reader
Seems to work and read cards. Follow instructions from smartcards.

## Fingerprint reader
Work as expected. Follow fprintd

## Power management
## S3 sleep / s2idle
S3 sleep is not supported. However, s2idle works out of the box and causes no problems with sleep / hibernation.

## Hibernate
Works fine. If you face Wi-Fi issues after hibernation see: Network / Wi-Fi

## Battery thresholds
Battery charge thresholds can be correctly set with TLP, within KDE / GNOME power management or from the command line:

 # echo 75 > /sys/class/power_supply/BAT0/charge_start_threshold
 # echo 80 > /sys/class/power_supply/BAT0/charge_stop_threshold

## AMD P-State EPP
Use  or this udev rule + script to apply different AMD P-State EPP states depending on whether the laptop is running on battery or charger.

{{hc|1=/etc/udev/rules.d/99-battery.rules|2=
SUBSYSTEM=="power_supply", ATTR{online}=="0", RUN+="/usr/local/bin/on_battery.sh"
SUBSYSTEM=="power_supply", ATTR{online}=="1", RUN+="/usr/local/bin/on_ac.sh"
}}

{{hc|1=/usr/local/bin/on_battery.sh|2=
#!/usr/bin/bash

# Change Dirty Writeback Centisecs according to TLP / Powertop
echo '5000' > '/proc/sys/vm/dirty_writeback_centisecs';

# Change AMD Paste EPP energy preference
# Available profiles: performance, balance_performance, balance_power, power
echo 'balance_power'  tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference;

# If required, change cpu scaling governor
# Possible options are: conservative ondemand userspace powersave performance schedutil
#cpupower frequency-set -g powersave;

# Platform Profiles Daemon will do this automatically, based on your settings in KDE / GNOME
# You can how ever, set this manually as well
# Possible profile options are: performance, powersave, low-power
#echo 'powersave' > '/sys/firmware/acpi/platform_profile';

# Radeon AMDGPU DPM switching doesn't seem to be supported.
# Possible options should be: battery, balanced, performance, auto
#echo 'battery' > '/sys/class/drm/card0/device/power_dpm_state';

# Should always be auto (TLP default = auto)
# Possible options are: auto, high, low
#echo 'auto' > '/sys/class/drm/card0/device/power_dpm_force_performance_level';

# Runtime PM for PCI Device to auto
find /sys/bus/pci/devices/*/power -name control -exec sh -c 'echo "auto" > "$1"' _ {} \;
for i in $(find /sys/devices/pci0000\:00/0* -maxdepth 3 -name control); do
    echo auto > $i;
done
}}

{{hc|1=/usr/local/bin/on_ac.sh|2=
#!/usr/bin/bash

# Change Dirty Writeback Centisecs according to TLP / Powertop
echo '500' > '/proc/sys/vm/dirty_writeback_centisecs';

# Change AMD Paste EPP energy preference
# Available profiles: performance, balance_performance, balance_power, power
echo 'balance_performance'  tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference;

# If required, change cpu scaling governor
# Possible options are: conservative ondemand userspace powersave performance schedutil
#cpupower frequency-set -g performance;

# Platform Profiles Daemon will do this automatically, based on your settings in KDE / GNOME
# You can how ever, set this manually as well
# Possible profile options are: performance, powersave, low-power
#echo 'performance' > '/sys/firmware/acpi/platform_profile';

# Radeon AMDGPU DPM switching doesn't seem to be supported.
# Possible options should be: battery, balanced, performance, auto
#echo 'performance' > '/sys/class/drm/card0/device/power_dpm_state';

# Should always be auto (TLP default = auto)
# Possible options are: auto, high, low
#echo 'auto' > '/sys/class/drm/card0/device/power_dpm_force_performance_level';

# Runtime PM for PCI Device to on
find /sys/bus/pci/devices/*/power -name control -exec sh -c 'echo "on" > "$1"' _ {} \;
for i in $(find /sys/devices/pci0000\:00/0* -maxdepth 3 -name control); do
    echo on > $i;
done
}}

Additionally make  and  executable.

## Power Profiles Daemon
The package  is the standard power management service for KDE#Power management and GNOME#Power modes.
It conflicts with TLP and the reasons for that are described here: https://gitlab.freedesktop.org/upower/power-profiles-daemon#why-not

# Install
# Start/enable the  service.

## Microphone LED
Some users reported that the Mic LED is always on.

This doesn't always happen but if you face the issue see: Lenovo ThinkPad T14 (AMD) Gen 3#Mute Mic LED always on.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
! Note
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  || Toggles Fn lock || Has status led
|-
|  ||  ||  ||  || Has status led
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  || Has status led
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  || Marked with airplane mode
|-
|  ||  ||  ||  || Marked with message box
|-
|  ||  ||  ||  || Marked with phone answer call
|-
|  ||  ||  ||  || Marked with phone end call
|-
|  ||  ||  ||  ||

|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  || Change keyboard backlight level ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.

## Troubleshooting
## Laptop cannot suspend/reboot/shutdown
If your laptop cannot suspend, reboot or even shutdown, it might be due to the UEFI Firmware 0.1.40, released on May 5th, 2024.
This firmware has been reported to cause several issues such as (and possibly not limited to):
# Laptop cannot suspend/reboot/shutdown;
# TLP and  services cannot start;
# Regenerating the  is not possible, as the  autodetect hook hangs indefinitely.

All these issues might be related to the malfunctioning of the AMD Sensor Fusion HUB device.
Running  will reveal similar errors:

To solve this issue, blacklist the  kernel module.
Notice that, since you cannot rebuild the , you should first blacklist the
module  from your boot loader, and later make it permanent.
See also here and here.
