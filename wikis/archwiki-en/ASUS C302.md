# ASUS C302

The Asus C302 (also known as Asus C302C and Asus C302CA) is a Chromebook, which can have Linux installed. Here are some pointers on the smooth running of Arch Linux.

## Installation
Add  to your kernel parameters.

 is from BBS#228604, to prevent the following error from appearing in the output of dmesg:

 i915 *ERROR* CPU pipe A FIFO underrun

The CPU is an Intel Core M3, so install .

## Kernel Modules
In e.g.

 # Needed for the nau8825 kernel sound modules to initialize
 blacklist snd_hda_intel

 options tpm_tis interrupts=0

Note: this does not seem necessary (anymore?), audio also works with  and , as described under #Sound.

## Screen
The screen is 12.5 inches diagonally. At 1920x1080 resolution, this is 176 DPI, which is HiDPI.

In ~/.xinitrc, to set the screen dimensions (measured in millimetres):

 xrandr --fbmm 277x156

## Vsync
For proper vsync (including e.g. fullscreen Youtube in Firefox) in XFCE, install , and enable XFCE's compositor.

Proper vsync also requires , rather than modesetting.

In /etc/X11/xorg.conf.d/20-intel.conf

 Section "Device"
     Identifier "Intel Graphics"
     Driver "intel"
 EndSection

## Screen Flipping
To use the laptop in tent mode, the following script will flip both the screen and touch input:

{{bc|
#!/bin/dash

set_normal() {
	r="normal"
	ctm="1 0 0 0 1 0 0 0 1"

}

set_upside_down() {
	r="inverted"
	ctm="-1 0 1 0 -1 1 0 0 1"
}

line=$(xrandr | grep '^eDP.* connected ')
screen=$(printf "%s" "$line" | cut -d" " -f1)

if $(printf "%s" "$line" | grep -q ' inverted (normal') ; then
	set_normal
else
	set_upside_down
fi

xrandr --output "$screen" --rotate "$r"
xinput set-prop "Elan Touchscreen" "Coordinate Transformation Matrix" $ctm

}}

## Keyboard
To use the top row of Chromebook keys as useful keys in xorg, use e.g.:

In ~/.Xmodmap

 keycode   9 = Escape NoSymbol Escape
 keycode  22 = BackSpace BackSpace BackSpace BackSpace Delete NoSymbol Delete
 keycode  37 = Control_L NoSymbol Control_L
 keycode  50 = Shift_L NoSymbol Shift_L
 keycode  66 = Caps_Lock NoSymbol Caps_Lock
 keycode  67 = Home F1 Home F1 F1 F1 XF86Switch_VT_1
 keycode  68 = End F2 End F2 F2 F2 XF86Switch_VT_2
 keycode  69 = Prior F3 Prior F3 F3 F3 XF86Switch_VT_3
 keycode  70 = Next F4 Next F4 F4 F4 XF86Switch_VT_4
 keycode  71 = Delete F5 Delete F5 F5 F5 XF86Switch_VT_5
 keycode  72 = XF86MonBrightnessDown F6 XF86MonBrightnessDown F6 F6 F6 XF86Switch_VT_6
 keycode  73 = XF86MonBrightnessUp F7 XF86MonBrightnessUp F7 F7 F7 XF86Switch_VT_7
 keycode  74 = XF86AudioMute F8 XF86AudioMute F8 F8 F8 XF86Switch_VT_8
 keycode  75 = XF86AudioLowerVolume F9 XF86AudioLowerVolume F9 F9 F9 XF86Switch_VT_9
 keycode  76 = XF86AudioRaiseVolume F10 XF86AudioRaiseVolume F10 F10 F10 XF86Switch_VT_10
 keycode 111 = Up Up Up Up Prior Prior
 keycode 112 = Prior NoSymbol Prior
 keycode 113 = Left Left Left Left Home Home
 keycode 114 = Right Right Right Right End End
 keycode 115 = End NoSymbol End
 keycode 116 = Down Down Down Down Next Next
 keycode 117 = Next NoSymbol Next
 keycode 118 = Insert NoSymbol Insert
 keycode 119 = Delete NoSymbol Delete
 keycode 124 = XF86PowerOff NoSymbol XF86PowerOff
 keycode 167 = XF86Forward NoSymbol XF86Forward
 keycode 182 = XF86Close NoSymbol XF86Close
 keycode 191 = XF86ScreenSaver NoSymbol XF86ScreenSaver

(This list can be pruned.)

~/.Xmodmap will be loaded by /etc/X11/xinit/xinitrc, which effectively runs:

 xmodmap ~/.Xmodmap

## Keyboard Backlight
To be able to change the keyboard backlight brightness as a normal user, run as root:

 b="/sys/devices/platform/GOOG0002:00/leds/chromeos::kbd_backlight/brightness"
 chgrp users "$b" &&
 chmod 660 "$b" &&
 echo 6 > "$b"

It is a value between 0 (off) and 100 (full brightness). The default on ChromeOS is 25. 6 is a reasonable lower value.

ChromeOS is able to disable the keyboard backlight, when the keyboard is not being used - that functionality does not appear to be available in the Linux kernel, but can be replicated in a simple script, with the aid of , e.g.:

{{bc|
#!/bin/dash

set_keyboard_backlight() {
	printf "%s" "$1" > "/sys/devices/platform/GOOG0002:00/leds/chromeos::kbd_backlight/brightness"
	b="$1"
}

b=0

while true ; do
	pgrep ^Xorg > /dev/null || exit 0

	seconds_to_sleep=10
	idle_millis=$(xprintidle)
	if [ "$idle_millis" -gt 10000 ] ; then
		nb=0
		seconds_to_sleep=5
	else
		nb=25
		seconds_to_sleep=15
	fi

	if [ "$nb" -ne "$b" ] ; then
		set_keyboard_backlight "$nb"
	fi

	echo "nb=$nb, sleeping for $seconds_to_sleep"
	sleep "$seconds_to_sleep"
done

}}

## Touchpad
As of  1.12.0-2, the touchpad works nicely with all of:

* Tapping:
** 1-finger tap = "left" button
** 2-finger tap = "right" button
** 3-finger tap = "middle" button

* Clickpad (clicking the lower portion of the touchpad):
** Left side = "left" button
** Right side = "right" button
** Middle = "middle" button

## Mouse
Due to the limited amount of USB ports, a Bluetooth mouse is a good option. The Logitech M590 mouse works great.

Run "bluetoothctl power on &" at startup, e.g. in ~/.xinitrc

In e.g. /etc/X11/xorg.conf.d/99-mouse.conf

 Section "InputClass"
     Identifier "Logitech M590"
     MatchIsPointer "on"
     MatchDevicePath "/dev/input/event*"
     Driver "libinput"
     Option "AccelProfile" "flat"
 EndSection

Then, the "speed" of the mouse can be set using the XFCE GUI, in "Settings - Mouse", setting the "acceleration" to e.g. 2.0

## Sound
The laptop should be able to play sound via HDMI (untested), built-in speaker, headphone jack, or Bluetooth headsets.

For Bluetooth, follow the standard Bluetooth and Bluetooth headset setup.

Built-in speaker and headphone jacks work with ALSA after installing the  (optional?) and  packages, and then rebooting to ensure the firmware is loaded.

ALSA can also be used as the output sink for the PulseAudio (untested) and PipeWire sound servers.

More information here:

* https://github.com/GalliumOS/galliumos-distro/issues/379
* https://github.com/WeirdTreeThing/chromebook-linux-audio

## Troubleshooting
When succesful,  should show:

 00:1f.3 Multimedia audio controller: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
 	DeviceName: Multimedia audio controller
 	Flags: bus master, fast devsel, latency 64, IRQ 132, IOMMU group 7
 	Memory at 9112c000 (64-bit, non-prefetchable) Memory at 91110000 (64-bit, non-prefetchable) [size=64K
 	Capabilities: Power Management version 3
 	Capabilities: [60 MSI: Enable+ Count=1/1 Maskable- 64bit+
 	Kernel driver in use: snd_soc_avs
 	Kernel modules: snd_soc_avs, snd_hda_intel

And  shows:

 **** List of PLAYBACK Hardware Devices ****
 card 0: HDMI HDMI, device 0: HDMI1 (*) Subdevices: 1/1
   Subdevice #0: subdevice #0
 card 0: HDMI [AVS HDMI, device 1: HDMI2 (*) Subdevices: 1/1
   Subdevice #0: subdevice #0
 card 0: HDMI [AVS HDMI, device 2: HDMI3 (*) Subdevices: 1/1
   Subdevice #0: subdevice #0
 card 1: MAX98357A [AVS I2S MAX98357A, device 0: Built-in Speakers (*) Subdevices: 1/1
   Subdevice #0: subdevice #0
 card 4: NAU8825 [AVS I2S NAU8825, device 0: Headset (*) Subdevices: 1/1
   Subdevice #0: subdevice #0

Here, MAX98357A is the built-in speaker and NAU8825 is the headphone audio port.

Verify playback works, e.g. with:

 aplay -D default:CARD=MAX98357A -i example.wav

## ALSA
To set audio to a sensible level, run in ~/.xinitrc:

 amixer -q -c0 sset Headphone 70% &

## PulseAudio
To prevent audio "clicks", comment out "load-module module-suspend-on-idle" in /etc/pulse/default.pa and /etc/pulse/system.pa

## Coil Whine
There is occasional [https://www.notebookcheck.net/FAQ-Coil-Whine.225152.0.html coil whine, which can be greatly reduced by running:

 printf "1" > /sys/devices/system/cpu/intel_pstate/no_turbo
