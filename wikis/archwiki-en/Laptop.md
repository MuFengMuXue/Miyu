# Laptop

This Laptop main page contains links to articles (sections) needed for configuring a laptop for the best experience. Setting up a laptop is in many ways the same as setting up a desktop. However, there are a few key differences. Arch Linux provides all the tools and programs necessary to take complete control of your laptop. These programs and utilities are highlighted below, with appropriate tips tutorials.

If there are laptop model specific instructions, the respective article is crosslinked in the first column of the vendor subpages. In case the model is not listed in the vendor table, existing instructions of similar models via the Laptops vendor subcategory may help.

## Power management
Power management is very important for anyone who wishes to make good use of their battery capacity. The following tools and programs help to increase battery life and keep your laptop cool and quiet.

## Battery state
Reading battery state can be done in multiple ways. Classical method is some daemon periodically polling battery level using ACPI interface. On some systems, the battery sends events to udev whenever it (dis)charges by 1%, this event can be connected to some action using a udev rule.

Battery can be checked directly from the kernel using:

 $ cat /sys/class/power_supply/BAT0/capacity

 could also have vendor name. For example,  for Wacom stylus pen.

Alternatively, you can use the  abstraction utility:

 $ for BAT_PATH in $(upower -e | grep BAT); do upower -i "$BAT_PATH"; done

## ACPI
Battery state can be read using ACPI utilities from the terminal. ACPI command line utilities are provided via the  package. See ACPI modules for more information.

*  is a battery icon that sits in the system tray.
*  is an udevrule file triggering plug and battery level notifications (multi-x sessions support).
*  is a lightweight battery monitor daemon that uses libnotify to warn of low battery levels.

## Hibernate on low battery level
If your battery sends events to udev whenever it (dis)charges by 1%, you can use this udev rule to automatically hibernate the system when battery level is critical, and thus prevent all unsaved work from being lost. Alternatively,  can also take action when battery level is at a configurable critical level if  is enabled.

## udev
{{hc|/etc/udev/rules.d/99-lowbat.rules|2=
# Suspend the system when battery level drops to 5% or lower
SUBSYSTEM=="power_supply", ATTR{status}=="Discharging", ATTR{capacity}=="RUN+="/usr/bin/systemctl hibernate"
}}

This rule will be repeated whenever the condition is set. As such, when resuming from hibernate when the battery is critical, the computer will hibernate directly. Some laptops do not boot beyond a certain battery level, so the rule could be adjusted accordingly.

If you have more than one battery or if you are using a battery powered peripheral device, the rule could be triggered unexpectedly by another battery discharging; this can be fixed by obtaining another attribute/value pair to add to your udev rule that specifically match the main battery, for example . Such new attribute/value pair can be obtained for example by checking , or by running  and waiting for battery events.

Batteries can jump to a lower value instead of discharging continuously, therefore a udev string matching pattern for all capacities 0 through 5 is used.

To shutdown the system instead of hibernating, use . The  flag can be used to ignore shutdown inhibitors, see . Other rules can be added to perform different actions depending on power supply status and/or capacity.

If your system has no or missing ACPI events, frequently run the following script which uses :

{{bc|1=
#!/bin/sh
acpi -b  awk -F'[,:%' '{print $2, $3}'  {
	read -r status capacity

	if [ "$status" = Discharging -a "$capacity" -lt 5 ]; then
		logger "Critical battery threshold"
		systemctl hibernate
	fi
}
}}

If you have more than one battery or if you are using a battery powered peripheral device, you should modify the second line of the script by adding  to monitor the correct battery like so: {{ic|acpi -b  grep "Battery 0"  awk -F''{print $2, $3}'  {}}. Replace  with your required battery as reported by .

## Testing events
One way to test udev rules is to have them create a file when they are run. For example:

{{hc|/etc/udev/rules.d/98-discharging.rules|2=
SUBSYSTEM=="power_supply", ATTR{status}=="Discharging", RUN+="/usr/bin/touch /home/username/discharging"
}}

This creates a file at  when the laptop charger is unplugged. You can test whether the rule worked by unplugging your laptop and looking for this file. For more advanced udev rule testing, see Udev#Testing rules before loading.

## UPower
Configure UPower, for example:

Enable and start  afterwards.

## Suspend and hibernate
Manually suspending the operating system, either to memory (standby) or to disk (hibernate) sometimes provides the most efficient way to optimize battery life, depending on the usage pattern of the laptop.

See the main article Suspend and hibernate.

## Hard drive spin down problem
Documented [https://bugs.launchpad.net/ubuntu/+source/acpi-support/+bug/59695 here.

To prevent your laptop hard drive from spinning down too often, set less aggressive power management as described in hdparm#Power management configuration. Even the default values may be too aggressive.

## Wakeup triggers
Wakeup sources/events/triggers wake the system from any of the hardware power-saving states. To find and configure these see wakeup triggers.

## Hardware support
## Screen brightness
See Backlight.

## Touchpad
To get your touchpad working properly, see the libinput page. Touchpad Synaptics is the older input driver, which is currently in maintenance mode and is no longer updated.

## Touchpad not detected at all
If a touchpad device is not detected and shown as a device at all, a possible solution might be using one or more of these kernel parameters:

 i8042.noloop i8042.nomux i8042.nopnp i8042.reset

## Elantech
If an Elantech Touchpad is not being detected and the following line appears in your journal:

 elan_i2c 5-0015: 5-0015 supply vcc not found, using dummy regulator

it is related to an issue with the  module trying to use a secondary bus for the touchpad device, and  failing to do so. The fix is to force it to use the primary one. Create the file below and reload the  module or reboot:

If the Touchpad is detected (which can be tested using libinput) but still does not work, it can help to blacklist the elan_i2c kernel, as discussed in === Fingerprint reader ===

See Fingerprint-gui, fprint and ThinkFinger (for ThinkPads).

## Webcam
See Webcam setup.

## Hard disk shock protection
There are several laptops from different vendors featuring shock protection capabilities. As manufacturers have refused to support open source development of the required software components so far, Linux support for shock protection varies considerably between different hardware implementations.

Currently, two projects, named HDAPS and Hpfall, support this kind of protection. HDAPS is for IBM/Lenovo Thinkpads and hpfall for HP/Compaq laptops.

## Hybrid graphics
The laptop manufacturers developed new technologies involving two graphic cards in a single computer, enabling both high performance and power saving usages. These laptops usually use an Intel chip for display by default, so an Intel graphics driver is needed first. Then you can choose methods to utilize the second graphics chip.

## Hardware video acceleration
Use of hardware decoding and encoding can lead to a higher battery life. See Video acceleration.

## Audio mute LED
On laptops using Intel HD Audio, the user may need to manually specify the codec model in order to get the audio mute LED to work. First, check if your laptop uses Intel HD Audio; the following command will produce output if so:

 $ lsmod | grep snd_hda_intel

Next, you will need to find your audio codec model:

 $ grep Codec /proc/asound/card*/codec*

Now you need to find their codec in the [https://docs.kernel.org/sound/hd-audio/models.html list of available model names. If you cannot find a codec for your specific model, you may be able to find one that works through trial and error.

In order to tell the kernel module which model-specific options to load, specify the  kernel module parameter. For example:

To test whether or not this worked, the kernel module must be reloaded. You can do this by rebooting.

If you need to test a large number of codecs, it may be more efficient to avoid rebooting by first bringing the system to a state where no processes are using the kernel module, and then reloading the module with the new parameters. This can be done by logging out of all graphical and console sessions, and stopping the display manager if using one. Upon logging back in at a console, run the following commands:

 # modprobe -r snd_hda_intel
 # modprobe snd_hda_intel model=model_name

The module will now be using the new codec specified in model_name.

## Network time syncing
For a laptop, it may be a good idea to use Chrony as an alternative to NTPd, OpenNTPD or systemd-timesyncd to sync your clock over the network. Chrony is designed to work well even on systems with no permanent network connection (such as laptops), and is capable of much faster time synchronisation than standard ntp. Chrony has several advantages when used in systems running on virtual machines, such as a larger range for frequency correction to help correct quickly drifting clocks, and better response to rapid changes in the clock frequency. It also has a smaller memory footprint and no unnecessary process wakeups, improving power efficiency.

## Writing laptop pages
See Help:Laptop page guidelines if you want to create or modify any laptop page.
