# Lm sensors

lm_sensors (Linux monitoring sensors) is a free and open-source application that provides tools and drivers for monitoring temperatures, voltage, and fans. This document explains how to install, configure, and use lm_sensors.

## Installation
Install the  package.

## Configuration
## Auto-detection
Use sensors-detect as root to detect and generate a list of kernel modules:

 # sensors-detect

It will ask to probe for various hardware. The "safe" answers are the defaults, so just hitting  to all the questions will generally not cause any problems. This will create the  configuration file which is used by  to automatically load kernel modules on boot.

When the detection is finished, a summary of the probes is presented.

Example:

## Adding DIMM temperature sensors
To find the temperature sensors of DIMMs, install the  package. Once installed, load the  kernel module.

 # modprobe i2c_dev

To show all the columns, use i2cdetect as root:

Otherwise, its output will appear as follows:

 i2c-2	unknown    	SMBus PIIX4 adapter port 2 at 0b00	N/A
 i2c-2	unknown    	SMBus PIIX4 adapter port 1 at 0b20	N/A
 i2c-0	unknown    	SMBus PIIX4 adapter port 0 at 0b00	N/A

In the following example, RAM sticks are connected to the bus . The i2cdetect command will show the devices that are connected to the bus. The  argument uses the  smbus. Check other buses if needed.

RAM SPD's (serial presence detect) start from address  and RAM temperature sensors start from  at same bus. In this example, there are 2 DIMMs available. The address  and  are the DIMMs temperature sensors.

To read the temperatures of RAM sticks, we need the  kernel module loaded. You need to tell the module which addresses to use. This process consists of writing the  and  to . For example:

 # modprobe jc42
 # echo jc42 0x18 > /sys/bus/i2c/devices/i2c-0/new_device
 # echo jc42 0x19 > /sys/bus/i2c/devices/i2c-0/new_device

After that your ram sticks temperature will be visible:

## Reading SPD values from memory modules (optional)
To read the SPD timing values from memory modules, install the  package. Once installed, load the  or  (deprecated) kernel module.

 # modprobe at24

Finally, view memory information with .

Here is partial output from one machine:

## Usage
Example running :

## Graphical front-ends
There are a variety of front-ends for sensors data.

*
*
*
*

For specific Desktop environments:

*
*
*
*
*
*

## sensord
There is an optional daemon called sensord (included with the  package) which can log data to a round robin database (rrd) and later visualize graphically.  See the  man page for details.

## Tips and tricks
## Adjusting values
In some cases, the data displayed might be incorrect or users may wish to rename the output. Use cases include:

* Incorrect temperature values due to a wrong offset (i.e. temps are reported 20 °C higher than actual).
* Users wish to rename the output of some sensors.
* The cores might be displayed in an incorrect order.

All of the above (and more) can be adjusted by overriding the package provided settings in  by creating  wherein any number of tweaks will override the default values.  It is recommended to rename 'foo' to the motherboard brand and model but this naming nomenclature is optional.

Custom configuration files for a number of motherboards can be found in the configs directory of the lm_sensors package and be used as templates.

To apply configuration, run  with  flag.
 # sensors -s

## Adjusting temperature offsets
This is a real example on a Zotac ION-ITX-A-U motherboard.  The coretemp values are off by 20 °C (too high) and are adjusted down to Intel specs.

Run  with the  switch to see what options are available for each physical chip (raw mode). If some of the raw labels you are presented seem not to be configurable, look at the  directory tree. Each device mentioned there has a  file, which can be used to match the device it is referring to. And then try the labels referred to by that directory.

Create the following file overriding the default values:

Now invoking  shows the adjust values:

## Renaming labels
This is a real example on an Asus A7M266.  The user wishes more verbose names for the temperature labels  and :

Create the following file to override the default values:

Now invoking  shows the adjust values:

## Renumbering cores for multi-CPU systems
This is a real example on an HP Z600 workstation with dual Xeons.  The actual numbering of physical cores is incorrect: numbered 0, 1, 9, 10 which is repeated into the second CPU.  Most users expect the core temperatures to report out in sequential order, i.e. 0,1,2,3,4,5,6,7.

Again, run  with the  switch to see what options are available for each physical chip:

Create the following file overriding the default values:

Now invoking  shows the adjust values:

## Automatic lm_sensors deployment
Users wishing to deploy lm_sensors on multiple machines can use the following to accept the defaults to all questions:

 # sensors-detect --auto

## S.M.A.R.T. drive temperature
Since kernel 5.6the  module will report SATA/SAS temperature through hwmon, but  does not automatically detect this so the module must be manually loaded.

 # modprobe drivetemp

You should now see entries similar to this in your  output:

You can now load the module at boot. Alternatively, manually add it to the  line of . Do note it will not be added automatically when  will be allowed to write this file again.

## Persistent device names
Many pieces of software expect sensor devices to stay put in , but more often than not, they don't on systems with more than 1-2 devices providing a hwmon interface. Software should probably parse the  or use lmsensors libraries, but more often than not, they sadly don't. Some software (example: Monitorix or certain modules of it, namely amdgpu) expect persistent names somewhere else.

Hence, the following kind of udev rules might be useful. Not all software can use them (for example, KDE system monitor - which sadly, makes these software almost useless on many systems). For many cases, simply matching the hwmon subsystem and a suitable name in the udev rule should be enough - but not always! See Udev page for more information on writing rules.

One can not rename or symlink under  hieraerchy. A  statement will also not work. Hence, we need to use the  statement (note, the symlink does not need to be under  as in this example - there is no standard nor a good place for them).

{{hc|/etc/udev/rules.d/99-persistent-hwmon-names.rules|2=
# my motherboard sensor chip:
ACTION=="add", SUBSYSTEM=="hwmon", ATTRS{name}=="nct6687", RUN+="/bin/sh -c 'ln -s /sys$devpath /dev/nct6678'"
# a USB device providing sensors:
ACTION=="add", SUBSYSTEM=="hwmon", ATTRS{name}=="corsaircpro", RUN+="/bin/sh -c 'ln -s /sys$devpath /dev/corsaircpro'"
# my GPU:
ACTION=="add", SUBSYSTEM=="hwmon", ATTRS{vendor}=="0x1002", ATTRS{device}=="0x73bf", RUN+="/bin/sh -c 'ln -s /sys$devpath /dev/rx6900xt'"
}}

## Troubleshooting
## K10Temp module
Some K10 processors have issues with their temperature sensor. See the [https://docs.kernel.org/hwmon/k10temp.html#description k10temp documentation for more information.

On affected machines the module will report "unreliable CPU thermal sensor; monitoring disabled". To force monitoring anyway, you can run the following:

 # rmmod k10temp
 # modprobe k10temp force=1

Confirm that the sensor is in fact valid and reliable. If it is, can edit  and add:

 options k10temp force=1

This will allow the module to load at boot.

## Asus B450M-A/A320M-K/A320M-K-BR and Biostar B650EGTQ motherboards
These motherboards use a IT8655E (Asus) and IT8625E (Biostar) chip, which is not supported by the it87 kernel driver, as of April 2025 However, it is supported by the upstream version of the kernel driver [https://github.com/frankcrawford/it87/blob/master/it87.c#L22. The DKMS variant is contained in . The driver has to be used with a matching .

## Asus B450/X399/X470 motherboards with AM4 Socket
Some recent Asus motherboards use a ITE IT8665E chip, accessing the temperature, fan and voltage sensors may require the  module. It is part of the mainline kernel since 5.17: load the  kernel module which uses the UEFI interface and may require a BIOS update on some boards Alternatively, the  module reads the values from the chip directly, install  and load the  kernel module.

## Biostar B650 motherboards with AM5 Socket
## ASUS H97/Z97/Z170/Z370i/X570/B550/B650-PLUS/X670 motherboards
With some recent ASUS motherboards, fan and voltage sensor access may require the  kernel module to be loaded.

You may also need to add the following kernel parameter:

 acpi_enforce_resources=lax

See https://bugzilla.kernel.org/show_bug.cgi?id=204807 for more information.

## Asrock Deskmini H470
The STX board of the Deskmini H470 uses a NCT6683 chip, for accessing the temperature, fan and voltage sensors the loading of  module is required.

For proper values of the  module have a module config file created:

## Gigabyte B250/Z370/B450M/B560M/B660M/Z690/B550 motherboards
Some Gigabyte motherboards use the ITE IT8686E, ITE8689 (for B560 and B660M) or ITE8689E (for Z690 and B550) chip, which is not supported by the it87 kernel driver, as of May 2019 [https://docs.kernel.org/hwmon/it87.html. However, it is supported by the upstream version of the kernel driver The DKMS variant is contained in . As with #ASUS H97/Z97/Z170/Z370i/X570/B550/B650-PLUS/X670 motherboards, a kernel parameter is required before attempting to install the module:

 acpi_enforce_resources=lax

Furthermore, supply the id of the chip when loading the module as follows:

 # modprobe it87 force_id=0x8686

or

 # modprobe it87 force_id=0x8689  # for B560
 # modprobe it87 force_id=0x8628  # for Z690 and B550

Or you can load the module during boot process by creating the following two files:

For Z690 and B550:

For others:

Once the module is loaded you can use the sensors tool to probe the chip.
Now you can also use fancontrol to control the speed step of your case fan.

Optionally installation of  may allow greater fine tuning of the motherboard's cooling system. However, it does disable the default k10temp module.

## Gigabyte GA-J1900N-D3V
This motherboard uses the ITE IT8620E chip (useful also to read voltages, mainboard temp, fan speed) and it is supported by the  kernel module.[https://docs.kernel.org/hwmon/it87.html

You can load the module at runtime with modprobe:

 $ modprobe it87 force_id=0x8728

Or you can load the modules during boot process by creating the following two files:

Once the module is loaded you can use the sensors tool to probe the chip.

Now you can also use fancontrol to control the speedsteps of your case fan.

## MSI MAG B650 / X870 TOMAHAWK WIFI / Z890 TOMAHAWK WIFI (MS-7D75/MS-7E32) / MAG B550 MORTAR WIFI (MS-7C94)
These motherboards use a Nuvoton NCT6687-R chip for fan, voltage and temperature readings. You need the kernel module  to access those values.

Once installed you can load the module:

 # modprobe nct6687

And then check the output of sensors:

 $ sensors

## Module parameters
The module supports several kernel module parameters:

* force (bool, default: false) - Enable support for unknown vendors
* manual (bool, default: false) - Enable manual voltage input configuration via external sensors file
* fan_config (default|msi_alt1, default: default) - Changes fan configuration for RPM & PWM registers. Automatically enabled for supported boards. Manual configuration only needed for unsupported boards
* msi_fan_brute_force (bool, default: false) - For MSI boards with : Writes PWM values to all 7 fan curve control points. May help if standard PWM writes don't work. Affects only system fans, not CPU/pump fans. Requires blacklisting  module

## msi_fan_brute_force
If you there are no RPM values, or the fan stops at 60% (MSI boards with msi_alt1 support), start by blacklisting the conflicting driver:

Enable brute-force mode:

Ensure the needed module loads at boot:

Verify  does not contain  in , then reboot to apply the previous changes.

## Asrock B650M Pro RS / B850M Pro RS / B850M Steel Legend WiFi / X870 Pro RS
These motherboards use the Nuvoton NCT6796D-S for fan, voltage and temperature readings. This exact variant of the chip has a different ID and therefore is not detected without a module config file:

## Asrock B650M PG Lightning
This motherboard uses the Nuvoton NCT6796D-S for fan, voltage and temperature readings. This exact variant of the chip has a different ID and therefore is not detected without a module config file:

## Laptop screen issues after running sensors-detect
This is caused by lm-sensors messing with the Vcom values of the screen while probing for sensors. It has been discussed and solved at the forums already: https://bbs.archlinux.org/viewtopic.php?id=193048. However, make sure to read through the thread carefully before running any of the suggested commands.

## Asrock X870 Steel Legend WiFi / B650I Lightning WiFi / B650 LiveMixer
These motherboards use a newer Nuvoton NCT6686D for fan, voltage and temperature readings. The [https://docs.kernel.org/hwmon/nct6683.html nct6683 driver documentation states that the driver will only instantiate with Intel CPUs. AMD CPUs require setting  to .

## Asrock B650E Taichi Lite
This motherboard uses a Nuvoton NCT6686D in addition to a NCT6796S for fan, voltage and temperature readings. AMD CPUs require setting  to .

## Asrock B850I Lightning
This motherboard uses a Nuvoton NCT6686D for fan, voltage and temperature readings. The nct6687d module  can be used here.
