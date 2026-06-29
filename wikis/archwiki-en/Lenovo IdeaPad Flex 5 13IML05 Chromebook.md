# Lenovo IdeaPad Flex 5 13IML05 Chromebook

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| SSD ||  ||
|-
| MicroSD card reader ||||
|-
| Keyboard ||||
|-
| Keyboard backlight ||||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Speakers ||  ||
|-
| Microphone ||||
|-
| 3.5mm jack ||||
|-
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| Stylus ||  ||
|-
| Webcam ||  ||
|}

## Installation
This Chromebook does not support Legacy Boot Mode. Even if you try to invoke it by pressing  on the Developer Mode boot screen, it will show two options without a choice. Therefore it is necessary to flash a custom firmware.

## UEFI firmware flashing
# Disable Firmware Write Protection by booting without battery or using SuzyQable.
# Enable Developer Mode.
# Use MrChromebox's Firmware Utility Script.

## Arch Linux installation
Use  to suppress audit messages that appear every second:
 # auditctl -e0

Follow the Installation guide.

## Lid sensor
As of kernel version 5.19.16 or perhaps earlier, the lid sensor causes the system to wakeup shortly after suspending, regardless of whether the lid is closed.

A workaround is to disable wakeup events from the lid sensor. An example udev rule:

{{hc|/etc/udev/rules.d/lid.rules|2=
# Disable wakeups from lid sensor
ACTION=="add", SUBSYSTEM=="acpi", KERNEL=="PNP0C0D:00", ATTR{power/wakeup}="disabled"
}}

## Sound
Install the following packages:
*  - sound driver
*  - PulseAudio
*  - required to connect ALSA with PulseAudio
*  - acpid is required to make work the 3.5mm jack

Describe the sound card using the ALSA configuration file:

Force PulseAudio to use the devices defined above:

Find and delete or comment out the following block of code to prevent conflicts:

Create the following script to automatically switch sinks with acpid because of the 3.5mm jack:

{{hc|/etc/acpi/headphones_jack.sh|2=
# License: 0BSD

#!/bin/bash

function get_active_pulseaudio_users_ids {
    active_pulseaudio_users_ids=`ps -C pulseaudio -o ruid=`
}

function set_up_environment {
    local user_id="$1"
    export HOME=`getent passwd $user_id  cut -d: -f6`
    export PULSE_RUNTIME_PATH="/var/run/user/$user_id/pulse"
}

function set_sink {
    local user_id="$1"
    local sink_name="$2"
    sudo -u "#$user_id" -E pacmd set-default-sink $sink_name
}

if [ "$2" == "HEADPHONE" ]; then
    get_active_pulseaudio_users_ids

    for user_id in $active_pulseaudio_users_ids; do
        set_up_environment $user_id
        if [ "$3" == "plug" ]; then
            set_sink $user_id "headphones"
        else
            set_sink $user_id "speakers"
        fi
    done
fi
}}

Make the script executable.

Register the script as a listener:

Enable

The sound should work after reboot.

## Touchscreen
As of January 12, 2022, the Linux kernel (5.15.13) uses the wrong module for the touchscreen due to a bug.

Therefore, it is necessary to block it:

The kernel will load the correct module after reboot.
