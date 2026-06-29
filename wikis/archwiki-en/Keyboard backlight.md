# Keyboard backlight

There are two general categories of keyboard backlight brightness level control on laptops, depending on the specific hardware:

* The backlight is fully handled by the laptop firmware and the operating system sees nothing happening (e.g. HP EliteBook 745 G4#Function keys),
* The keybind has to be handled by the operating system, with two sub-categories:
** The firmware is not involved at all and the raw key sequences is left for the operating system to handle (e.g. what Toshiba Portege Z30-A#Keyboard backlight control describes)
** The keybind sends a specific  keysym (like what is described in ASUS ROG STRIX G17 (2022)#Function keys).

This can be tested by installing either xev (from ) or  then pressing the backlight control hotkeys:

* If you see an  keysym, for example , then you fall into the "handled by the operating system via keysym" category.
* If you see a raw key sequence, for example , then you fall into the "handled by the operating system via raw sequence" category.
* If you see nothing at all then you fall into the "handled by firmware" category.

Which category your laptop falls into will impact which method you use to control the backlight.

A pure firmware controlled hotkey should always work and requires no configuration for daily usage. This scenario will complicate scripting as no event is exposed to build upon.

In contrast, either operating system–controlled scenario allows for easier scripting at the detriment of lacking backlight control outside of a running operating system.

## Controlling the backlight
Even when the brightness is controlled by firmware, you can adjust the level programmatically. There are a variety ways to manage the brightness level and different helper tools to accomplish this, such as  or .

## sysfs
The  pseudo-file system exposes an interface to the keyboard backlight. The current brightness level can be obtained by reading  where  can is replaced depending on the manufacturer, e.g.  for Lenovo (ThinkPads),  for ASUS or  for Dell. For example to get the maximum brightness level:

 $ cat /sys/class/leds/vendor::kbd_backlight/max_brightness

To set the brightness to 1:

 # echo 1 > /sys/class/leds/vendor::kbd_backlight/brightness

When using brightnessctl you can get a list of available brightness controls with , then to show the kbd backlight information:

 $ brightnessctl --device=vendor::kbd_backlight' info

This will show the absolute and relative current value and the maximum absolute value. To set a different value:

 $ brightnessctl --device=vendor::kbd_backlight' set 1

You can use script to toggle keyboard backlight every call, for example

## xset
Some keyboard manufacturers are not recognized by  or , but you can use  to control its lights if you are running Xorg.

The first parameter  turns on the led, and  turns it off, the  parameters accepts integers for 1 to 32 (each number corresponds to a led in you system, keyboards seem to generally be number 3), or 'on' and 'off' (on will turn ALL lights on, and off will turn ALL lights off).

To turn on the lights:

 $ xset led NUMBER

To turn off the lights:

 $ xset -led NUMBER

## D-Bus
You can control your computer keyboard backlight via the D-Bus interface. The benefits of using it are that no modification to device files is required and it is vendor agnostic.

The following is an example implementation in Python, requiring  and  to be installed. You can then map your keyboard shortcuts to run  and  to increase and decrease your keyboard backlight level by  amounts.

## Troubleshooting
## Restore after sleep
On some laptops (e.g. Dell XPS 15) the backlight is always off after sleep. In order to restore the previous brightness level you can use the following service.
