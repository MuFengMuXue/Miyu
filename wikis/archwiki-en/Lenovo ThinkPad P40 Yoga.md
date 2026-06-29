# Lenovo ThinkPad P40 Yoga

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| Touchpad || ||
|-
| Touchscreen ||  ||
|-
| Webcam ||  ||
|-
| Card reader ||  ||
|-
| Fingerprint reader ||  ||
|-
| Bluetooth ||  ||
|-
| Accelerometer || ||
|}

## Configuration
## Automatic rotation
Install . Under GNOME, rotation will happen automatically. Under i3, you can use this script in the background:

{{bc|
#!/bin/sh
# Requires https://github.com/hadess/iio-sensor-proxy

dbus-monitor --system interface=org.freedesktop.DBus.Properties,member=PropertiesChanged,path=/net/hadess/SensorProxy 2> /dev/null |
        sed -n -u -e '/string "AccelerometerOrientation"/ {n ; s/\s*variant\s*string\s*"\(.*\)"/\1/p}' |
        while read -r line ; do
                case $line in
                        right-up )
                                xrandr -o right &> /dev/null
                                ;;
                        left-up )
                                xrandr -o left &> /dev/null
                                ;;
                        bottom-up )
                                xrandr -o inverted &> /dev/null
                                ;;
                        normal | * )
                                xrandr -o normal &> /dev/null
                                ;;
                 esac
        done

}}

In order to have your touchpad, Trackpoint, touchscreen and stylus also change orientation, install xrandr-align and run the following script at startup:
