# Laptop Mode Tools

Laptop Mode Tools is a laptop power saving package for Linux systems. It is the primary way to enable the Laptop Mode feature of the Linux kernel, which lets your hard drive spin down. In addition, it allows you to tweak a number of other power-related settings using a simple configuration file.

Combined with acpid and CPU frequency scaling, LMT provides most users with a complete notebook power management suite.

## Installation
Install the  package.

## Configuration
Configuration is handled through:

*  - primary configuration file.
*  - dozens of feature-specific "modules".

Each module can be explicitly , , or set to  by changing the  argument of any file in .  LMT will attempt to enable any modules where  is set to  if  is set in .  There are two exceptions to the above rule:  and  use an  variable instead of .

To quickly check which modules are enabled, disabled or auto, run:

 $ grep -r '^\(CONTROL\ENABLE\)_' /etc/laptop-mode/conf.d

Finally, enable .

## Hard disks
For this you need to have hdparm and/or sdparm installed. See Hdparm.

Spinning down the hard drive through  values saves power and makes everything a lot more quiet. LMT can also establish  values. The maximum hard drive power saving is 1 and the minimum is 254. For example, set this value to 254 when on AC and 20 when on battery. If you find that normal activity hangs often while waiting for the disk to spin up, it might be a good idea to set it to a higher value (e.g. 128) which will make it spin down less often.  and  values are configured in .

With the  variable (default on), laptop-mode-tools automatically remounts your partitions, appending  in the mount options. This keeps the journaling program jbd2 from accessing your disk every few seconds, instead the disk journal gets updated every 10 minutes.

## Solid state drives
From the official, upstream FAQ:

Question: I have a solid-state disk (SSD) in my machine. Should I enable any of the disk-related parts of laptop-mode-tools, or are they irrelevant?

Answer: They may be relevant, because (a) laptop mode will reduce the number of writes, which improves the lifetime of an SSD, and (b) laptop mode makes writes bursty, which enables power saving mechanisms like ALPM to kick in. However, your mileage may vary depending on the specific hardware involved. For some hardware, you will get no gain at all, for some the gain may be substantial.

## CPU frequency
For this you need to have a CPU frequency driver installed. See CPU frequency scaling.

 # cpufreq.conf
 # ThinkPad T40/T42/T60 Example
 #
 CONTROL_CPU_FREQUENCY=1
 BATT_CPU_MAXFREQ=fastest
 BATT_CPU_MINFREQ=slowest
 BATT_CPU_GOVERNOR=ondemand
 BATT_CPU_IGNORE_NICE_LOAD=1
 LM_AC_CPU_MAXFREQ=fastest
 LM_AC_CPU_MINFREQ=slowest
 LM_AC_CPU_GOVERNOR=ondemand
 LM_AC_CPU_IGNORE_NICE_LOAD=1
 NOLM_AC_CPU_MAXFREQ=fastest
 NOLM_AC_CPU_MINFREQ=slowest
 NOLM_AC_CPU_GOVERNOR=ondemand
 NOLM_AC_CPU_IGNORE_NICE_LOAD=0
 CONTROL_CPU_THROTTLING=0

## Device and bus
## Intel SATA
Enable the Intel SATA AHCI controller Aggressive Link Power Management feature to set the disk link into a very low power mode in the absence of disk IO.

 # intel-sata-powermgmt.conf
 # ThinkPad T40/T42/T60 Example
 #
 DEBUG=0
 CONTROL_INTEL_SATA_POWER=1
 BATT_ACTIVATE_SATA_POWER=1
 LM_AC_ACTIVATE_SATA_POWER=1
 NOLM_AC_ACTIVATE_SATA_POWER=0

## USB autosuspend
 # runtime-pm.conf
 # ThinkPad T40/T42/T60 Example
 #
 DEBUG=0
 CONTROL_RUNTIME_AUTOSUSPEND=1
 BATT_SUSPEND_RUNTIME=1
 LM_AC_SUSPEND_RUNTIME=1
 NOLM_AC_SUSPEND_RUNTIME=1
 AUTOSUSPEND_TIMEOUT=2

## Display and graphics
## LCD brightness
Available brightness values for certain laptops can be obtained by running following command:

 $ cat /proc/acpi/video/VID/LCD/brightness

## ThinkPad T40/T42
For ThinkPad T40/T42 notebooks, minimum and maximum brightness values can be obtained by running:

 $ cat /sys/class/backlight/acpi_video0/brightness
 $ cat /sys/class/backlight/acpi_video0/max_brightness

 # lcd-brightness.conf
 # ThinkPad T40/T42 Example
 #
 DEBUG=0
 CONTROL_BRIGHTNESS=1
 BATT_BRIGHTNESS_COMMAND="echo 0"
 LM_AC_BRIGHTNESS_COMMAND="echo 7"
 NOLM_AC_BRIGHTNESS_COMMAND="echo 7"
 BRIGHTNESS_OUTPUT="/sys/class/backlight/thinkpad_screen/brightness"

## ThinkPad T60
For ThinkPad T60 notebooks, minimum and maximum brightness values can be obtained by running:

 $ cat /sys/class/backlight/thinkpad_screen/max_brightness
 $ cat /sys/class/backlight/thinkpad_screen/brightness

 # lcd-brightness.conf
 # ThinkPad T60 Example
 #
 DEBUG=0
 CONTROL_BRIGHTNESS=1
 BATT_BRIGHTNESS_COMMAND="echo 0"
 LM_AC_BRIGHTNESS_COMMAND="echo 7"
 NOLM_AC_BRIGHTNESS_COMMAND="echo 7"
 BRIGHTNESS_OUTPUT="/sys/class/backlight/acpi_video0/brightness"

## Asus Laptops
## LCD
For most (probably all) Asus ROG & TUF notebooks with Intel CPUs, a maximum brightness value can be obtained by running:

 # cat /sys/class/backlight/intel_backlight/max_brightness

 # lcd-brightness.conf
 # Asus TUF Dash F15 2022 Example
 #
 DEBUG=0
 CONTROL_BRIGHTNESS=1
 BATT_BRIGHTNESS_COMMAND="echo 32000"
 LM_AC_BRIGHTNESS_COMMAND="echo 96000"
 NOLM_AC_BRIGHTNESS_COMMAND="echo 96000"
 BRIGHTNESS_OUTPUT="/sys/class/backlight/intel_backlight/brightness"

## Keyboard backlight
Asus notebooks talk to the kernel though an Asus specific module and as such standard keyboard brightness commands will not work. A maximum brightness levels can be obtained by running:

 # cat /sys/class/leds/asus::kbd_backlight/max_brightness

 # kbd-backlight.conf
 # Asus TUF Dash F15 2022 Example
 #
 DEBUG=0
 CONTROL_BRIGHTNESS=1
 BATT_BRIGHTNESS_COMMAND="echo 1"
 LM_AC_BRIGHTNESS_COMMAND="echo 3"
 NOLM_AC_BRIGHTNESS_COMMAND="echo 3"
 BRIGHTNESS_OUTPUT="/sys/class/leds/asus::kbd_backlight/max_brightness"

## Terminal blanking
 # terminal-blanking.conf
 # ThinkPad T40/T42/T60 Example
 #
 DEBUG=0
 CONTROL_TERMINAL=1
 TERMINALS="/dev/tty1"
 BATT_TERMINAL_BLANK_MINUTES=1
 BATT_TERMINAL_POWERDOWN_MINUTES=2
 LM_AC_TERMINAL_BLANK_MINUTES=10
 LM_AC_TERMINAL_POWERDOWN_MINUTES=10
 NOLM_AC_TERMINAL_BLANK_MINUTES=10
 NOLM_AC_TERMINAL_POWERDOWN_MINUTES=10

## Networking
## Ethernet
 # ethernet.conf
 # ThinkPad T40/T42/T60 Example
 #
 DEBUG=0
 CONTROL_ETHERNET=1
 LM_AC_THROTTLE_ETHERNET=0
 NOLM_AC_THROTTLE_ETHERNET=0
 DISABLE_WAKEUP_ON_LAN=1
 DISABLE_ETHERNET_ON_BATTERY=1
 ETHERNET_DEVICES="eth0"

## Wireless LAN
Wireless interface power management settings are hardware-dependent, and thus a bit trickier to configure. Depending on the wireless chipset, the settings are managed in one of the following three files:
# for a generic method of saving power (using "iwconfig wlan0 power on/off"). This applies to most chipsets (that is, anything but Intel chipsets listed below).
# for Intel chipsets driven by the old ipw driver. This apply to IPW3945, IPW2200 and IPW2100. It currently (as of LMT 1.55-1) uses iwpriv for IPW3945, and a combination of iwconfig and iwpriv settings for IPW2100 and IPW220. See  for details. (note that the ipw3945 is not used anymore, see below)
# for Intel chipsets driven by modules iwl4965, iwl3945 and iwlagn (this latter supports chipsets 4965, 5100, 5300, 5350, 5150, 1000, and 6000)
Note that activating the three of them should not be much of a problem, since LMT detects the module used by the interface and acts accordingly.

The supported modules for each configuration file, indicated above, are taken directly from LMT. However, this seems to be a bit out-of-date, since the current 2.6.34 kernel does not provide the ipw3945 and iwl4965 modules anymore (3945 chipset uses iwl3945 instead, and 4965 uses the generic module iwlagn). This is only brought here for information, as this does not (or should not) affect the way LMT works.

There is a known issue with some chipsets running with the iwlagn module (namely, the 5300 chipset, and maybe others). On those chipsets, the following settings of :

 IWL_AC_POWER
 IWL_BATT_POWER

are ignored, because the  file does not exist. Instead, the standard method (with ) is automatically used.

## Audio
## AC97
 # ac97-powersave.conf
 # ThinkPad T40/T42/T60 Example
 #
 DEBUG=0
 CONTROL_AC97_POWER=1

## Intel HDA
 # intel-hda-powersave.conf
 # ThinkPad T40/T42/T60 Example
 #
 DEBUG=0
 CONTROL_INTEL_HDA_POWER=1
 BATT_INTEL_HDA_POWERSAVE=1
 LM_AC_INTEL_HDA_POWERSAVE=1
 NOLM_AC_INTEL_HDA_POWERSAVE=0
 INTEL_HDA_DEVICE_TIMEOUT=10
 INTEL_HDA_DEVICE_CONTROLLER=0

## Troubleshooting
## Laptop-mode-tools is not picking up events
Install  and enable .

If that does not help, go through the laptop-mode configuration files and make sure that the service you want to enable is set to 1. Many services (including cpufreq control) are by default set to "auto", which may not enable them.

Issues with bluetooth not working when booting up with battery are fixed with disabling runtime-pm.

## USB Mouse sleeping after 5 seconds when on battery
First find the ID of your device (it should look like ):

 $ lsusb

Put this value into the  variable in , for example:

Multiple IDs can be seperated with spaces.

## Issues with NVIDIA driver
## KDE shows black screen
When laptop mode is enabled, KDE fails to start. The reason is that the default KDE display manager (SDDM) starts before the NVIDIA driver. To prevent this from happening you need to remove the  kernel parameter.

## Slower Boot after enabling laptop-mode.service
As described before, laptop-mode-tools affects the NVIDIA driver. Adding the  kernel parameter reduces boot time dramatically.
