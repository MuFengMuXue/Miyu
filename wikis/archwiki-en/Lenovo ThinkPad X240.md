# Lenovo ThinkPad X240

The Lenovo X240 is a laptop from the Lenovo Ultrabook Series and also is a complete redesign of the X Series. This can be observed especially with devices like the touchpad, which has been changed to be a one-click touchpad instead of having the classic 5 button touchpad. The X240 is a very light device, weighing in at just 2.84 lbs (1.36 kg) and measuring 12.02" x 8.19" x 0.79".

## Tested Configuration
{| class="wikitable sortable"
! Feature !! X240 !! X240 (20AMS4SM00) !! X240 (20ALA0K-WIG) !! X240 (20ALCTO1WW)
|-
| CPU || Intel(R) Core(TM) i7-4600U CPU @ 2.10GHz || Intel(R) Core(TM) i5-4210U CPU @ 2.7GHz || Inter(R) Core(TM) i5-4200U CPU @ 1.6 GHz || Inter(R) Core(TM) i5-4300U CPU @ 1.9 GHz
|-
| Graphics || Intel HD 4400 - Haswell-ULT || Intel HD 4400 - Haswell-ULT || Intel HD 4400 - Haswell-ULT || Intel HD 4400 - Haswell-ULT
|-
| Ram || 8 GB || 8 GB || 4 GB || 4 GB
|-
| Disk || Samsung 5120 SSD || Seagate ST500LM000-SSHD-8GB || WDC WD10JPVX-08JC3T5 || Samsung 840 Evo
|-
| Display || 12.5" IPS FHD (1920x1080) || 12.5" IPS FHD (1920x1080) || 12.5" IPS 1366x768 || 12.5" IPS FHD 1920x1080
|-
| Wireless || Intel Corporation Wireless 7260 || Intel Corporation Wireless 7260 || Intel Corporation Wireless 7260 || Intel Corporation Wireless 7260
|-
| Built-in Battery || 9 Cell || 9 Cell || Not Tested || 3 Cell
|-
| Additional Plugable Battery || 6 Cell 19+ || 6 Cell 19+ || 6 Cell 19+ || 3 Cell
|-
| Backlight Keyboard || Yes || Yes || Yes || -
|-
| ThinkLight || No || No || No || -
|-
| Fingerprint Scanner || Yes || Yes || Yes || Yes
|-
| Bluetooth || Yes || Yes || Yes || Yes
|-
| Camera || Yes || Yes || Yes || Yes
|-
| NFC || No || - || - || -
|}

## System Configuration
## Use analog sound card by default in ALSA
You likely need to change the ALSA default sound card if you want to output sound via line-out by default.

Install the  package, run  and inspect its output:

The card that drives the analog line-out is in this case card #1. Create a global configuration file to make it the default:

Alternatively, the same configuration may be set in .

## Touchpad
The touchpad works out of the box. You will need to install .

Some users may prefer to use the trackpoint over the touchpad. In that case, the touchpad can be disabled via  (will be gone after re-login). See Synaptics for more information and options.

## Battery
Despite they focus on power management under Microsoft Windows, it might be useful to read the following articles from the official documentation:

* Easy ways to extend your battery life - ideapad/Lenovo/ThinkPad laptops
* Display contrast reduced while on battery mode on ThinkPad X220

## TrackPoint
The TrackPoint is usuable out of the box, but the default parameters for speed, sensitivity and inertia yield only insufficient navigation ability given the high-res display. The following udev configuration delivers a snappy experience:

{{hc|$ cat /etc/udev/rules.d/10-trackpoint.rules|

SUBSYSTEM=="serio", DRIVERS=="psmouse", ACTION=="change", ENV{SERIO_TYPE}=="05", ATTR{press_to_select}="1", ATTR{sensitivity}="196", ATTR{speed}="255", ATTR{inertia}="4"

}}

Consult the ThinkWiki for other configuration possibilities such as scrolling.

## Keyboard
The keyboard works out of the box mostly, including the  key and XF86 aliases. For the LED of the  button to work  needs to be appended to the kernel parameters.

Most WMs/DEs handle the special XF86 keys automatically, but you might need to add a configuration yourself. Tools like  (), ,  and  help in this regard.

The button  automatically toggles the (soft) rfkill block state of the wireless device. Keep this in mind when you set it up to connect/disconnect to your wireless network. You can also unblock wlan without using this key: .

The keyboard does not have an LED for . If your WM/DE does not come with an indicator you can use  in the tray.

The indicator LED for  seems to be broken in some way. According to this commit it should work with  but it does not. There is also an older kernel patch available that might or might not help, but probably does not work with a current kernel as is.

## Keyboard Backlight
The default hotkey for the keyboard backlight () is automatically supported by GNOME. In order to set the keyboard brightness from a terminal it is possible to choose between three different levels of brightness using the following commands:

0% brightness:

 # echo 0 > /sys/class/leds/tpacpi::kbd_backlight/brightness

50% brightness:

 # echo 1 > /sys/class/leds/tpacpi::kbd_backlight/brightness

100% brightness:

 # echo 2 > /sys/class/leds/tpacpi::kbd_backlight/brightness

Alternatively, installing the package  allows to do the same thing using a different syntax:

0% brightness:

 # xbacklight -ctrl tpacpi::kbd_backlight -set 0

50% brightness:

 # xbacklight -ctrl tpacpi::kbd_backlight -set 50

100% brightness:

 # xbacklight -ctrl tpacpi::kbd_backlight -set 100

## Fingerprint Reader
The fingerprint reader is a Validity Sensors model (138a:0017) also used on the Thinkpad X1 Carbon and T440. ThinkFinger does NOT support this reader. This fingerprint reader requires libfprint to be build from the current git (https://github.com/ars3niy/fprint_vfs5011.git ). Alternatively, it can also be done going through Fprint, for 20ALA0K-WIG.

## Fingerprint Login
Install the  package to enable the fingerprint login in GNOME.

## Caveats
## Common hardware problems
This page provides a list and links regarding common issues with X240 hardware.

## NFC Reader
Some of the x240 devices have a NFC reader integrated in the touchpad. However it seems that this type of NFC reader is not support for Linux. This post seems to confirm this.

## Grey noise with analog audio when audio is not muted
On some X240 and other TP 4xx models, persisting grey noise is hearable when the audio mixer has not been muted. The issue has been reported to the ALSA developers, but as of now, the issue persists. Affected users are encouraged to report their situation in the linked thread.
