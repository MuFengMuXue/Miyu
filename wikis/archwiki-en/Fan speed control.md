# Fan speed control

Fan control can bring various benefits to your system, such as quieter working system and power saving by completely stopping fans on low CPU load.

## Fancontrol (lm-sensors)
 is a part of , which can be used to control the speed of CPU/case fans. It is most suitable for desktops and laptops, where fan controls are available via .

Support for newer motherboards may not yet be in the Linux kernel.

## lm-sensors
The first thing to do is to run

 # sensors-detect

This will detect all of the sensors present and they will be used for fancontrol. After that, run the following to check if it detected the sensors correctly:

## Configuration
Once the sensors are properly configured, use  to test and configure fan speed control. Following the guide should create , a customized configuration file. In the guide, the default answers are in parenthesis if you press enter without typing anything. Enter  for yes,  for no.

 # pwmconfig

## Tweaking
Some users may want to manually tweak the configuration file after running  with root privileges, usually to fix something. For manually tweaking the  configuration file, see  for the variable definitions.

Users will probably encounter the hwmon path issues as noted above in #Fancontrol (lm-sensors). See #Device paths have changed in /etc/fancontrol for more information.

## Running Fancontrol
Try to run fancontrol:

 # fancontrol

A properly configured setup will not output errors and will take control of the system fans. Users should hear system fans starting shortly after executing this command. fancontrol can also be run by starting/enabling .

For an unofficial GUI, install .

## Fancontrol stops working after suspend–wake cycles
Unfortunately, fancontrol does not work after suspending. As per the filed bug, you will have to restart fancontrol after suspending. This can be achieved automatically by a systemd hook.

## NBFC
NBFC (NoteBook Fan Control) is a cross-platform fan control solution for notebooks, written in C# and works under Mono runtime. It comes with a powerful configuration system, which allows to adjust it to many different notebook models, including some of the latest ones.

There is another lightweight implementation of NBFC, written in C, named NBFC-Linux. It does not depend on the Mono framework. It can be installed as .

## Installation
NBFC can be installed as . Also start/enable .

## Configuration
NBFC comes with pre-made profiles. You can find them in  directory. When applying them, use the exact profile name without a file extension (e.g.  becomes ).

Check if there is anything NBFC can recommend:

 $ nbfc config -r

If there is at least one model, try to apply this profile and see how fan speeds are being handled. For example:

 $ nbfc config -a "Asus Zenbook UX430UA"

If there are no recommended models, go to NBFC git repository or  and check if there are any similar models available from the same manufacturer. For example, on Asus Zenbook UX430UQ, the configuration Asus Zenbook UX430UA did not work well (fans completelly stopped all the time), but Asus Zenbook UX410UQ worked fantastically.

Run  to see all options. More information about configuration is available at upstream wiki.

## Dell laptops
i8kutils is a daemon to configure fan speed according to CPU temperatures on some Dell Inspiron and Latitude laptops. It uses the  interface provided by the  driver (an alias for ). Results will vary depending on the exact model of laptop.

If fancontrol will not work on your system, use the  kernel module parameter to load .

## Installation
 is the main package to control fan speed. Additionally, you might want to install these:

*  — must be installed to use i8kmon.
*  — must be installed in order to run i8kmon as a background service (using the  option).
*  — must be installed together with  to run as X11 desktop applet.
*  — recommended if your BIOS overrides fan control.

## Configuration
The temperature points at which the fan changes speed can be adjusted in the configuration file . Only three fans speeds are supported (high, low, and off). Look for a section similar to the following:

 set config(0)  {{0 0}  -1  55  -1  55}
 set config(1)  {{1 1}  45  75  45  75}
 set config(2)  {{2 2}  65 128  65 128}

This example starts the fan at low speed when the CPU temperature reaches 55 °C, switching to high speed at 75 °C. The fan will switch back to low speed once the temperature drops to 65 °C, and turns off completely at 45 °C.

## Installation as a service
i8kmon can be started automatically by starting/enabling .

## BIOS overriding fan control
Some newer laptops have BIOS fan control in place which will override the OS level fan control. To test if this the case, run  with verbose mode in a command line, make sure the CPU is idle, then see if the fan is turned off or turned down accordingly.

If the BIOS fan control is in place, you can try using :

To enable BIOS fan control:

 # dell-bios-fan-control 1

To disable BIOS fan control:

 # dell-bios-fan-control 0

BIOS fan control can be automatically disabled by starting/enabling .

## ThinkPad laptops
Some fan control daemons include  and  (recommended).

## Installation
Install . Optionally, but recommended, install . If needed, a GUI is available with . Then have a look at the files:

 # pacman -Ql thinkfan

Note that the thinkfan package installs , which contains the following kernel module parameter:

 options thinkpad_acpi fan_control=1

So fan control is enabled by default, but you may need you to manually regenerate the initramfs.

Now, reload the module with fan control enabled:

 # modprobe -r thinkpad_acpi
 # modprobe thinkpad_acpi fan_control=1
 # cat /proc/acpi/ibm/fan

You should see that the fan level is "auto" by default, but you can echo a level command to the same file to control the fan speed manually:

 # echo level 1 > /proc/acpi/ibm/fan

{| class="wikitable"
|+ Fan Levels
|-
! Level !! Effect
|-
| 0 || off
|-
| 2 || low speed
|-
| 4 || medium speed
|-
| 7 || maximum speed
|-
| auto || default - automatic, the fan RPM is controlled by the BIOS
|-
| full-speed / disengaged || the maximum fan speed; here the controller does not monitor the fan speed
|}

The thinkfan daemon will do this automatically.

"7" is not the same as "disengaged". "7" is the maximum regulated speed (corresponds to "full-speed"). disengaged is the maximum unregulated speed.
See ThinkWiki for more details.

Finally, enable the .

To configure the temperature thresholds, you will need to copy the example configuration file () to , and modify to taste. This file specifies which sensors to read, and which interface to use to control the fan. Some systems have  and  available; on others, you will need to specify something like:

 hwmon: /sys/devices/virtual/thermal/thermal_zone0/temp

to use generic hwmon sensors instead of thinkpad-specific ones.

A configuration example can be found in Gentoo:Fan speed control/thinkfan#Configuration.

## Running
You can test your configuration first by running thinkfan manually (as root):

 # thinkfan -n

and see how it reacts to the load level of whatever other programs you have running.

When you have it configured correctly, start/enable .

## Lenovo Legions laptops
The tool Lenovo Legion Linux allows to change the fan curves that are stored in the embedded controller. It consists of a kernel module that must be compiled and loaded. Currently, there is no package, but it must be compiled and installed from source.

Then the fan curve can be set via the hwmon interface. This can be done with the provided script or the Python GUI.

## ASUS laptops
This topic will cover drivers configuration on ASUS laptops for Fancontrol (lm-sensors).

## Kernel modules
In configuration files, we are going to use full paths to sysfs files (e.g. ). This is because  might change to any other number after reboot. Fancontrol (lm-sensors) is written in Bash, so using these paths in configuration file is completely acceptable. You can find complete  configuration file examples at ASUS N550JV#Fan control.

## asus-nb-wmi
 is a kernel module, which is included in the Linux kernel and is loaded automatically on ASUS laptops. It will only allow to control a single fan and if there is a second fan you will not have any controls over it. Note that blacklisting this module will prevent keyboard backlight to work.

Below are the commands to control it. Check if you have any controls over your fan:

 # echo 255 > /sys/devices/platform/asus-nb-wmi/hwmon/hwmon:print:*/pwm1           # Full fan speed (Value: 255)
 # echo 0 > /sys/devices/platform/asus-nb-wmi/hwmon/hwmon:print:*/pwm1             # Fan is stopped (Value: 0)
 # echo 2 > /sys/devices/platform/asus-nb-wmi/hwmon/hwmon:print:*/pwm1_enable      # Change fan mode to automatic
 # echo 1 > /sys/devices/platform/asus-nb-wmi/hwmon/hwmon:print:*/pwm1_enable      # Change fan mode to manual
 # echo 0 > /sys/devices/platform/asus-nb-wmi/hwmon/hwmon:print:*/pwm1_enable      # Change fan mode to full speed

If you were able to modify fan speed with above commands, then continue with #Generate configuration file with pwmconfig.

## asus_fan
 is a kernel module, which allows to control both fans on some older ASUS laptops. It does not work with the most recent models.

Install the DKMS  kernel module, providing :

 # modprobe asus_fan

Check if you have any control over both fans:

 # echo 255 > /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/pwm1          # Full CPU fan speed (Value: 255)
 # echo 0 > /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/pwm1            # CPU fan is stopped (Value: 0)
 # echo 255 > /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/pwm2          # Full GFX fan speed (Value: 255)
 # echo 0 > /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/pwm2            # GFX fan is stopped (Value: 0)
 # echo 2 > /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/pwm1_enable     # Change CPU fan mode to automatic
 # echo 1 > /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/pwm1_enable     # Change CPU fan mode to manual
 # echo 2 > /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/pwm2_enable     # Change GFX fan mode to automatic
 # echo 1 > /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/pwm2_enable     # Change GFX fan mode to manual
 # cat /sys/devices/platform/asus_fan/hwmon/hwmon:print:*/temp1_input          # Display GFX temperature (will always be 0 when GFX is disabled/unused)

If everything works, you can load the module at boot to automate this step.

## Generate configuration file with pwmconfig
If you get an error  while generating configuration file with , open first console and execute:

 # watch -n 1 "echo 2 > /sys/devices/platform/''kernel_module/hwmon/hwmon:print:*/pwm1'''_enable"

If you use  kernel module and have 2nd fan, in second console:

 # watch -n 1 "echo 2 > /sys/devices/platform/''kernel_module/hwmon/hwmon:print:*/pwm2'''_enable"

And finally, in the third console:

 # pwmconfig

Once you are done and the configuration file is generated, you should stop the first and second consoles. Continue with #Fancontrol (lm-sensors). After the configuration file is generated, you might need to manually replace PWM values with full sysfs paths as they are used in these steps, because hwmon number values might change after reboot.

## Alternative method using EC registers
If the above methods do not work for you, an alternative method is to directly write to certain registers in the embedded controller (EC). Using the EC-Probe tool, you can set the fan mode to one of the three fan speed modes, provided your model offers such feature in Windows.

In ASUS FX504GD model setting the fan speed to one of the three modes uses these register values:

 # ec_probe write 0x5e 0x80 # silent mode
 # ec_probe write 0x5e 0x40 # balance mode
 # ec_probe write 0x5e 0xC0 # performance mode

Here we write to register  that is responsible in setting the fan speed mode.

If these values do not work for you, run the ec-probe tool in monitor mode in Windows and try to identify which register in the EC changes value when switching through fan speed modes.

## Setting thermal throttle policy
Instead of manually controlling fan speed using , it is also possible to set the thermal throttling policy to have a more or less aggressive fan control policy. Possible values are  (default),  (overboost), and  (silent).

 # echo number > /sys/devices/platform/asus-nb-wmi/hwmon/hwmon:print:*/throttle_thermal_policy

## Fan control modes on certain TUF series laptops
On certain ASUS TUF series laptops, performance and fan control modes can be changed using . The current mode can be viewed by running the following command:

 $ cat /sys/devices/platform/asus-nb-wmi/fan_boost_mode

You can view the value changing as you use press . 0 is "Normal Mode", 1 is "Performance Mode", 2 is most likely "Silent Mode".It is also possible to write these values into the  file as root and have the desired effect.

This was tested on the ASUS TUF FX504GE and ASUS TUF FX504GD models and found to be working.

You can use  to get notifications every time the FanSpeed mode gets changed.

## AMDGPU sysfs fan control
AMDGPU kernel driver offers fan control for graphics cards via hwmon in sysfs.

## Manual fan control
To switch to manual fan control from automatic, run
 # echo "1" > /sys/class/drm/card0/device/hwmon/hwmon0/pwm1_enable
Set up fan speed to e.g. 50% (100% are 255 PWM cycles, thus calculate desired fan speed percentage by multiplying its value by 2.55):
 # echo "128" > /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
To reset to automatic fan control, run
 # echo "2" > /sys/class/drm/card0/device/hwmon/hwmon0/pwm1_enable

## Fan curves control
Newer AMD graphical cards such as RDNA3 graphical cards do not support manual fan control due to firmware limitations [https://gitlab.freedesktop.org/drm/amd/-/issues/2764#note_2031564. For these cases AMD provides a fan_curve sysfs api for controlling the fan curves, for more information on it see === amdgpu-fan ===

The  package is an automated fan controller for AMDGPU-enabled video cards written in Python. It uses a "speed-matrix" to match the frequency of the fans with the temperature of the GPU, for example:

Launch the fan control service by starting/enabling .

## amdfand-bin
Then  package is a native alternative to . Launch the fan control service by starting/enabling .

For this tool there are also GUI clients available:  (Xorg) and  (Wayland). Before starting the client you need to enable/start .

## fancurve script
Not just fan controls are offered via hwmon in sysfs, but also GPU temperature reading:

 # cat /sys/class/drm/card0/device/hwmon/hwmon0/temp1_input

This outputs GPU temperature in °C + three zeroes, e.g.  for 33°C.

The bash script [https://github.com/grmat/amdgpu-fancontrol amdgpu-fancontrol by grmat offers a fully automatic fan control by using the described sysfs hwmon functionality. It also allows to comfortably adjust the fancurve's temperature/PWM cycles assignments and a hysteresis by offering abstracted configuration fields at the top of the script.

For safety reasons, the script sets fan control again to auto when shutting down. This may cause spinning up of fans, which can be worked around at cost of security by setting  in the section .

## Setting up fancurve script
To start the script, it is recommend to do so via systemd init system. This way the script's verbose output can be read via journalctl/systemctl status. For this purpose, a .service unit file is already included in the GitHub repository.

It may also be required to restart the script via a root-resume.service after hibernation in order to make it automatically function properly again:

## Others
*  — An alternative to Fancontrol independent of device-paths.
*  — Fan control application for MSI laptops.
*  — Fan configuration for Framework Laptops.
*  — A fan control daemon with GUI for sysfs and  devices.
*  — Simple GUI written in Qt to configure FAN PWM via HWMON interface. You could use it to setup the kernel auto point for every FAN who support it.

## Troubleshooting
## Increase the fan divisor for sensors
If sensors does not output the CPU fan RPM, it may be necessary to change the fan divisor.

The first line of the sensors output is the chipset used by the motherboard for readings of temperatures and voltages.

Create a file in :

Replacing  with name of the chipset and  with the number of the CPU fan to change.

Save the file, and run as root:

 # sensors -s

which will reload the configuration files.

Run  again, and check if there is an RPM readout. If not, increase the divisor to 8, 16, or 32. Your mileage may vary.

## Device paths have changed in /etc/fancontrol
The enumerated hwmon symlinks located in  might vary in order because the kernel modules do not load in a consistent order per boot. Because of this, it may cause fancontrol to not function correctly. The error is "Configuration appears to be outdated, please run pwmconfig again". Upstream bug.

## Solution
In , there are 2 arrays that list all of the modules detected when you execute . These get loaded in by fancontrol. If the file does not exist, run  as root, accepting the defaults. Open (or create) . Get all of the modules listed from the 2 variables in  and place them into the  file, one module per line. Specifying them like this should make a defined order for the modules to load in, which should make the hwmon paths stay where they are and not change orders for every boot. If this does not work, I highly recommend finding another program to control your fans. If you cannot find any, then you could try using the alternative solution below.

## Alternative solution: absolute paths
Using absolute file paths in fancontrol does not work by default, as its helper script  is programmed to only use the hwmon paths to get the files. The way it does this is that it detects whether the hwmon path that is provided in its configuration file  did not change, and uses the variables  and  to determine such change. If your hwmon paths keep changing, this will prevent fancontrol from running no matter what you do. However, one can circumvent this problem. Open , and comment out this part of the script:

 if [ "$DIR" = "/" -a -n "$DEVPATH" ]
 then
    echo "Unneeded DEVPATH with absolute device paths" >&2
    exit 1
 fi
 if ! ValidateDevices "$DEVPATH" "$DEVNAME"
  then
      echo "Configuration appears to be outdated, please run pwmconfig again" >&2
      exit 1
  fi

Commenting this out should effectively ignore the hwmon validation checks. You can also ignore the variables  and  in the configuration file as well. After this, replace all of the hwmon paths in the other variables with its absolute path. To make it easier, rerun  with root privileges to refresh the hwmon devices. The hwmon paths in the configuration file should now point to the correct absolute paths. For each hwmon path, run the following command (where  is the enumeration of the hwmon path):

 $ readlink -f /sys/class/hwmon/hwmonN/device

This will give you the absolute path of the device.

For example, an  file lists  as this:

 FCTEMPS=hwmon2/pwm1=hwmon3/temp1_input

Executing  can, for example, output .  into this directory. If you see a  directory, you have to do this in your fancontrol configuration file to replace the  path. From the previous example:

 # BEFORE
 FCTEMPS=hwmon2/pwm1=hwmon3/temp1_input
 # AFTER
 FCTEMPS=hwmon2/pwm1=/sys/devices/platform/coretemp.0/hwmon/:print:*/temp1_input

Essentially, you must replace the hwmon path with the absolute path, concatenated with  so that bash can catch the random enumerated hwmon name.

If you do not see the  directory, then you do not have to worry about this. This means that the temperature files are in the root of the device directory. Just replace  with the absolute file path. For example:

 # BEFORE
 FCTEMPS=hwmon2/pwm1=hwmon3/temp1_input
 # AFTER
 FCTEMPS=hwmon2/pwm1=/sys/devices/platform/coretemp.0/temp1_input

After replacing all of paths, fancontrol should work fine.
