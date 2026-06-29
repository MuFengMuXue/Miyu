# GPD Pocket

Notes for the GPD Pocket.

## Specs
* Display: 7inch IPS 1920x1200
* CPU: Intel Atom X7-Z8750
* RAM: 8GB LPDDR3-1600
* Storage: 128GB eMMC SSD (non-replaceable)
* Battery: 7000mAh
* WiFi: Broadcom 4356 802.11ac
* Bluetooth: Broadcom 2045
* Audio: Realtek ALC5645
* Ports: 1 x USB 3 type A, 1 x MicroHDMI, 1 x USB 3 type C, 1 x 3.5mm Headphone Jack

## Configuration
## Manual
## Backlight and KMS
Change  to match the following:

This will enable backlight control, and fix a black screen on resume from suspend.

## Screen rotation
Thanks to a kernel patch, the linux kernel should automatically hint screen rotation for the GPD pocket. If it does not, or if you do not use a desktop manager, follow instructions below.

## Wayland
## Screen rotation
To rotate the touchscreen, create:

{{hc|/etc/udev/rules.d/99-goodix-touch.rules|2=
ACTION=="addchange", KERNEL=="eventATTRS{name}=="Goodix Capacitive TouchScreen", ENV{LIBINPUT_CALIBRATION_MATRIX}="0 1 0 -1 0 1"
}}

## Right Click Emulation
Unlike Xorg, under which right click emulation can be enabled by the standard Xorg configuration files, under Wayland, such configuration is supposed to be exposed by the compositor, and unfortunately, some compositors (e.g. GNOME Wayland) do not expose these configurations properly. However, the regarding functionality is still available in . Since these compositors normally load ,  can be used to hook into  and force apply these configurations.

A sample implementation of this approach is available [https://github.com/PeterCxy/scroll-emulation here.

## Xorg
## Screen rotation
Create  to rotate the monitor:

## Gnome and GDM
Edit  (this file might not be present by default):

This sets the correct rotation () and a scale factor of 2 (). For fractional scaling, see HiDPI#GNOME.

For GDM, copy the above  to  to set the correct rotation.

## KDE
In System Settings > Display and Monitor, change Orientation to 90° Clockwise, and Scale Display to a comfortable size.

## Right Click Emulation
Create  to scroll while holding right click:

## SDDM
To change the DPI to be readable, append the following lines to :

## Touchscreen Gestures
Install , then edit the following line in :

Create the following file:
{{hc|/etc/X11/xinit/xinitrc.d/01_touchegg|2=
#!/bin/sh

# starts touchegg application
PREFIX="$HOME/.config/touchegg/.run"
mkdir -p "$PREFIX"
PIDFILE="$PREFIX/touchegg.$USER$DISPLAY.pid"
LOCK="$PREFIX/touchegg.$USER$DISPLAY.lock"

start_touchegg() {
        (
                flock -n 9  exit 1
                touchegg 2>/dev/null >/dev/null &
                PID=$!
                echo "$!" >"$PIDFILE"
                wait $PID
        ) 9>"$LOCK"
}

start_touchegg &
}}

And make it executable.

## Fan
With the latest kernel, your fan should work out of the box.

 # modprobe -r gpd-pocket-fan
 # modprobe gpd-pocket-fan temp_limits=40000,40001,40002

Once this has been completed, you should hear your fan start up at 40c. If you hear a clicking sound, power off the device, remove the back panel and very gently push the fan around a few times. Then re-attach the panel and power on the device, running the above commands again once logged in. It seems to be an issue with some devices that the fan cannot start properly when it has not been powered on in a while.

Once you have completed these steps and the fan is working properly, you should then either reboot or reload the fan kernel module in order to return the temperature limits to default:

 # modprobe -r gpd-pocket-fan
 # modprobe gpd-pocket-fan

## Power Saving
Install  and then edit following lines in :

## Audio
PulseAudio needs to be installed for the sound card.

Append the following lines into :

Turn off realtime scheduling by editing :

## Charge control
It is possible to control the charge current, charge end voltage and a few more settings.

See this reddit post for more information and an example script.

## Known Issues
## Wifi not seeing channels 12/13/14
As of May 2021 with current kernel and firmware versions, the Broadcom 4356 adapter no longer accesses networks on channels beyond the globally-allowed 1-11 range. Setting the regulatory domain with  does not fix this; apparently, the kernel driver does not support this. Instead, edit  and change  to your country (e.g.  enables channels 12/13 but not 14) and reboot (hint found in an older mailing list message).
