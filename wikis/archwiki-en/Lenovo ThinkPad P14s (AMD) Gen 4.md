# Lenovo ThinkPad P14s (AMD) Gen 4

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Ethernet ||  ||
|-
| Audio ||  ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Webcam ||  ||
|-
| TPM || ||
|-
| Fingerprint reader ||  ||
|-
| Smartcard reader ||  ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo ThinkPad P14s (AMD) Gen 4 laptop. With recent enough kernel the device works almost out of the box.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Firmware
This model is fully compatible with fwupd.

 detects the System Firmware, UEFI BIOS, webcam, fingerprint sensor, CPU/GPU, TPM and the NVMe controller.

## CPU
Since kernel 6.5, the AMD P-State EPP driver with "Active" profile is applied by default, no changes should be needed.

In case you are getting GPU resets (black screen), check Lenovo ThinkPad T14s (AMD) Gen 3#CPU.

## Touchpad
To disable sleep wake-up from touchpad see Lenovo ThinkPad T14s (AMD) Gen 3#Disable wakeup from sleep on touchpad activity.

## Touchscreen
The variation of this model with product code/name  is equipped with InfoVision display with touchscreen capability and it works out of the box.

The respective touchscreen input can be found as I2C device .

See Touchscreen for other information.

## Speakers
Speakers work out of the box. However, they will not have the same sound quality as on Windows due to the missing Dolby Atmos Convolver. The quality can be improved by using EasyEffects with a convolver effect (and possibly others) - see here for an example preset for this laptop.

## Wi-Fi
Starting with kernel v6.10, remaining bugs with the ath11k firmware were fixed.

However, these patches were found to cause issues with suspend, and were reverted in v6.10.10 as well as v6.11.

The patches were merged again starting with v6.16.

See Lenovo ThinkPad T14s (AMD) Gen 3#Network / Wi-Fi for a fix that unloads the  module before sleep and loads it again after resume.

Previously, specific ath11k firmware versions caused suspend during lid close to immediately wake from sleep.

There seems to be another issue where after some suspend/wakeup cycles the Wi-Fi card gets into a weird state where it drops almost all outgoing transmissions. This results in authentication timing out and network speeds being unusable. See Lenovo_ThinkPad_T14_(AMD)_Gen_4#Unreliable/High_latency for a fix.

## Smartcard reader
Tested using FIDO2 applet on J3180. Follow the instructions from smartcards.

## Fingerprint reader
Works as expected. Follow fprintd

## Power management
## S3 sleep / s2idle
S3 () sleep is not supported by this CPU anymore. However, s2idle works out of the box and causes no problems with sleep / hibernation.

The sleep power consumption with s2idle (or  S0//) can vary as it depends on the running OS and how well it can put peripherals into sleep mode.

## Hibernate
Works fine. If you face Wi-Fi issues after hibernation see #Wi-Fi.

## Battery thresholds
Battery charge thresholds can be correctly set with TLP or within KDE / GNOME power management.

## AMD P-State EPP
If you are using , please note that the current stable release of it do not fully support AMD P-State EPP. You can switch to TLP version 1.6 or newer that supports AMP P-State features, or fix this using an udev rule + script to apply different AMD P-State EPP states depending on whether the laptop is running on battery or charger.

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

# Radeon AMDGPU DPM switching does not seem to be supported.
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

# Radeon AMDGPU DPM switching does not seem to be supported.
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

## Microphone
## Reported as unplugged
If the internal mic is recognized by ALSA, but the recorded input is silent, please see: https://bbs.archlinux.org/viewtopic.php?pid=2162297#p2162297

## LED
If the Mic LED seems to stay always on see: Lenovo ThinkPad T14 (AMD) Gen 3#Mute Mic LED always on.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
! Note
|-
|  ||  ||  ||  || Can be swapped with left Ctrl in BIOS
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
|  ||  ||  ||  ||
|-
|  ||  ||  || Change keyboard backlight level ||
|}

# The key is visible to xev or  and similar tools.
# The physical key has a symbol on it, which describes its function.
