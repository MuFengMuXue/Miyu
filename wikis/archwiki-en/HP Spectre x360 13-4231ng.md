# HP Spectre x360 13-4231ng

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Video ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad || PS/2 ||
|-
| Touchscreen ||  ||
|-
| Webcam ||  ||
|-
| Card Reader ||  ||
|-
| Fingerprint Reader ||  ||
|}
This article covers hardware specific configuration of this laptop, some minor issues remain after customization. These can be performed after an installation of Arch Linux has been finished and the machine rebooted into it.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Hardware info
## Hardware options
The HP Spectre x360 name has been used for a number of models over the years.  While the overall look & feel of the brick has not changed, some hardware configuration changed a lot.

This model was released in November 2015 to replace the 13-4100.

Specifications:

* Intel i7 Skylake 6560U with Intel Iris 540 graphics (compared to i7 6500 with Intel HD 520 graphics on a 4100)
* OLED touch screen running at 2560x1440 (compared to LED 1920x1080 on a 4100)
* 500 GB M.2 SSD
* 8 GB RAM

This model has now been succeeded by the HP Spectre x360 13-w023dx.

## Installation
Installing Arch is straight forward for everything (disable Secure Boot,  for BIOS,  for boot options) but one thing: you may have to disable a BIOS option called "fast boot". While this option is activated in BIOS the machine may boot into Windows no matter what you select. After you installed Arch, you may activate that option again: no difference in boot performance could be observed with the option activated or deactivated.

## Tweaks
## Brightness / backlight
 exists but is not working as of kernel 4.6 and 4.7rc6. Proposed kernel parameters (such as ) do not remedy the issue. It may be helpful to know that OLED displays by their nature do not have backlight. xrandr offers some neat feature to change brightness of your screen. Depending on your driver (modesetting driver included in Xorg or xf86-video-intel, see Intel graphics) your screen is named eDP-1 or eDP1. Use  to determine the correct name if in doubt. The following statement changes brightness to 50%.

 $ xrandr --output eDP1 --brightness .5

While this may probably work on non-OLED displays as well, it will not reduce power consumption on non-OLED displays at all. Without in-depth tests and measurements done, it seems like lowering brightness from the default 100% to something more regular 50% extends battery life by some hours.

Since the hotkeys are performing updates on  you may use  to enable brightness adjustment using the hotkeys (see Backlight#sysfs modified but no brightness change). The following script does the job:

{{bc|
#!/bin/sh

path=/sys/class/backlight/intel_backlight

luminance() {
    read -r level < "$path"/actual_brightness
    bc <<< "scale=10;$level/$max"
}

read -r max < "$path"/max_brightness
xrandr --output eDP1 --brightness "$(luminance)"

inotifywait -me modify --format '' "$path"/actual_brightness | while read; do
    echo $(luminance)
    xrandr --output eDP1 --brightness "$(luminance)"
done
}}

The script requires package  to actually calculate the brightness factor. If you store the script at  (see Arch filesystem hierarchy), you may use the following file at  to run the script at login to gnome:

While all this fixes brightness issues on the brick quite well, there are still some issues to be solved:

* Chromium and some other programs reset brightness to 100% upon their first start since reboot.
* Hotkeys are not working prior to login.

## Gnome scaling
The screen natively runs at 2560x1440. Gnome by default assumes a scaling factor of 2 since the screen resolution at y-axis is greater than 1200 With this, at first glance all controls are quite over sized. xrandr offers some nice workaround:

 $ xrandr --output eDP1 --scale 1.25x1.25
 $ xrandr --output eDP1 --panning 3200x1800

Those commands should be executed in two steps tho. Gnome does not adjust size for sure each time. Setting those changes in an autostart script after login is not very reliable if some other programs are started at the same time. Even adding some sleep does not improve reliability to an acceptable level. Testing will be continued since this is a perfect resolution.

## Video driver
As mentioned in Intel graphics some people recommend to stay with the modesetting driver included in Xorg. As of Xorg 1.18.2, Mesa before 12.0 the performance of this driver is inacceptable when it comes to simple tasks like web browsing, scrolling documents or anything alike. On this machine installing  improves performance a lot.

## Issue: Airplane mode after login
* Wi-Fi is working. The hotkey for the airplane mode works. Although something strange is going on with the hotkey:
** Booting to console leads to some spam of ^@ for like 10 seconds. After this it suddenly stops and you can log in.
** Booting to GDM makes the hotkey for airplane mode work. Nothing special. You can login immediately.
** Right after login to Gnome the hotkey is spammed and thus airplane mode turned off and on for like 7 seconds. dmesg shows some hard faults caused by Wi-Fi module being unexpectedly unavailable but nothing else suspicious.
** If you wait in GDM for a while, the spam hotkey spam will not happen after login. I.e. the timer is running already while you are in GDM.
* The solution described at [https://askubuntu.com/questions/965595/why-does-airplane-mode-keep-toggling-on-my-hp-laptop-in-ubuntu-18-04 seems to work.
