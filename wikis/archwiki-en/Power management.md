# Power management

Power management is a feature that turns off the power or switches system components to a low-power state when inactive.

In Arch Linux, power management consists of two main parts:

# Configuration of the Linux kernel, which interacts with the hardware:
#* Kernel parameters
#* Kernel modules
#* udev rules
# Configuration of userspace tools, which interact with the kernel and react to its events. Many userspace tools also allow modification of kernel configuration in a "user-friendly" way. See #Userspace tools for the options.

## Userspace tools
These tools allow you to change a lot of settings without the need to edit config files by hand. Only run one of these tools to avoid possible conflicts as they all work more or less similarly. Have a look at the power management category to get an overview on what power management options exist in Arch Linux.

These are the more popular scripts and tools designed to help power saving:

## Console
*
*
*
*
*
*
*
*
*
*

## Graphical
*
*
*
*
*
*
*
*
*
*
*

## ACPI events
systemd handles some power-related ACPI events, whose actions can be configured in  or  — see . On systems with no dedicated power manager, this may replace the acpid daemon which is usually used to react to these ACPI events.

The specified action for each event can be one of , , , , , , , ,  or . In case of hibernation and suspension, they must be properly set up. If an event is not configured, systemd will use a default action.

{| class="wikitable sortable"
!Event handler
!Description
!Default action
|-
|
|Triggered when the power key/button is pressed.
|
|-
|
|Triggered when the power key/button is held
|
|-
|
|Triggered when the reboot key/button is pressed
|
|-
|
|Triggered when the Reboot key/button is held
|
|-
|
|Triggered when the suspend key/button is pressed.
|
|-
|
|Triggered when the suspend key/button is held
|
|-
|
|Triggered when the hibernate key/button is pressed.
|
|-
|
|Triggered when the hibernate key/button is held
|
|-
|
|Triggered when the lid is closed, except in the cases below.
|
|-
|
|Triggered when the lid is closed if the system is inserted in a docking station, or more than one display is connected.
|
|-
|
|Triggered when the lid is closed if the system is connected to external power.
|action set for
|}

To apply changes, reload .

## Power managers
Some desktop environments include power managers which inhibit (temporarily turn off) some or all of the systemd ACPI settings. If such a power manager is running, then the actions for ACPI events can be configured in the power manager alone. Changes to  or  need be made only if you wish to configure behaviour for a particular event that is not inhibited by the power manager.

Note that if the power manager does not inhibit systemd for the appropriate events you can end up with a situation where systemd suspends your system and then when the system is woken up the other power manager suspends it again. The power managers of GNOME, MATE, Plasma and Xfce issue the necessary inhibited commands. If the inhibited commands are not being issued, such as when using acpid or others to handle ACPI events, set the  options to . See also .

## xss-lock
 subscribes to the systemd-events , , , and  with appropriate actions (run locker and wait for user to unlock or kill locker). xss-lock also reacts to DPMS events and runs or kills the locker in response.

Autostarting the following for example:

 $ xss-lock -- i3lock -n -i background_image.png &

## Power saving
This section is a reference for creating custom scripts and power saving settings such as by udev rules. Make sure that the settings are not managed by some other utility to avoid conflicts.

Almost all of the features listed here are worth using whether or not the computer is on AC or battery power. Most have negligible performance impact and are just not enabled by default because of commonly broken hardware/drivers. Reducing power usage means reducing heat, which can even lead to higher performance on a modern Intel or AMD CPU, thanks to dynamic overclocking.

## Print power settings
This script prints power settings and a variety of other properties for USB and PCI devices.  Note that root permissions are needed to see all settings.

{{bc|1=
#!/bin/bash

for i in $(find /sys/devices/ -name "bMaxPower")
do
	busdir=${i%/*}
	busnum=$(/dev/null)
	do
		v=$(cat $ff 2>/dev/nulltr -d "\n")
		 ${#v} -gt 0  && echo -e " ${ff##*/}=$v";
		v=;
	done  sort -g;
done;

printf "\n\n\n+++ %s\n" "Kernel Modules"
for mod in $(lspci -k  sed -n '/in use:/s,^.*: ,,p'  sort -u)
do
	echo "+ $mod";
	systool -v -m $mod 2> /dev/null  sed -n "/Parameters:/,/^$/p";
done
}}

## Processors with Intel Hardware P-state support
The available energy preferences of an Intel Hardware P-state (HWP) supported processor are , , , , .

This can be validated by running

 $ cat /sys/devices/system/cpu/cpufreq/policy*/energy_performance_available_preferences

To conserve more energy, you can edit the configuration by creating the following file:

See the  man page for more details on energy-performance policy in Intel processors. Also see  and  man pages for temporary files/directories details.

## Audio
Whether power saving is turned on by default depends on a given driver, e.g. it is on for HD Audio. Identify the module in use, then run

 $ modinfo --field=parm module_name | column --separator=':' --table --table-columns-limit=2

and look for a kernel module parameter (like ) that adjusts or disables power-saving feature.

## Backlight
See Backlight.

## Bluetooth
To disable Bluetooth completely, blacklist the  and  modules.

Alternatively, create the following udev rules:

{{hc|/etc/udev/rules.d/50-bluetooth.rules|2=
# disable bluetooth
SUBSYSTEM=="rfkill", ATTR{type}=="bluetooth", ATTR{state}="0"
}}

To turn off Bluetooth only temporarily, use :

 # rfkill block bluetooth

## Web camera
If you will not use integrated web camera then blacklist the  module.

## Kernel parameters
This section uses configurations in , which is "a drop-in directory for kernel sysctl parameters."  See The New Configuration Files and more specifically  for more information.

## Disabling NMI watchdog
The NMI watchdog is a debugging feature to catch hardware hangs that cause a kernel panic. On some systems it can generate a lot of interrupts, causing a noticeable increase in power usage. To list these interrupts per CPU core since last boot, you can use:

To turn the hardlockup detector off, use:

or add  to the kernel command line.

Alternatively add  to the kernel command line to disable both hard and soft lockup detectors. See ==== Writeback Time ====

Increasing the virtual memory dirty writeback time helps to aggregate disk I/O together, thus reducing spanned disk writes, and increasing power saving. To set the value to 60 seconds (default is 5 seconds):

To do the same for journal commits on supported filesystems (e.g. ext4, btrfs...), use  as an option in fstab.

Note that this value is modified as a side effect of the Laptop Mode setting below. See also sysctl#Virtual memory for other parameters affecting I/O performance and power saving.

## Network interfaces
Wake-on-LAN can be a useful feature, but if you are not making use of it then it is simply draining extra power waiting for a magic packet while in suspend. You can adapt the Wake-on-LAN#udev rule to disable the feature for all ethernet interfaces. To enable powersaving with  on all wireless interfaces:

The name of the configuration file is important. With the use of persistent device names in systemd, the above network rule, named lexicographically after , is applied after the device is renamed with a persistent name e.g.  renamed . Be aware that the  command is executed after all rules have been processed and must anyway use the persistent name, available in  for the matched device.

## Intel wireless cards (iwlwifi)
Additional power saving functions of Intel wireless cards with  driver can be enabled by passing the correct parameters to the kernel module. Making them persistent can be achieved by adding the lines below to the  file:

 options iwlwifi power_save=1

This option will probably increase your median latency:

 options iwlwifi uapsd_disable=0

On kernels  /sys/module/pcie_aspm/parameters/policy

To configure a specific ASPM state to enable upon system boot (using  as an example), add  as a kernel parameter.

## PCI Runtime Power Management
{{hc|/etc/udev/rules.d/pci_pm.rules|2=
SUBSYSTEM=="pci", ATTR{power/control}="auto"
SUBSYSTEM=="ata_port", KERNEL=="ata*", ATTR{device/power/control}="auto"
}}

The rule above powers down unused devices.

Some devices will not wake up again. To allow runtime power management only for devices that are known to work, use simple matching against vendor and device IDs (use  to get these values):

{{hc|/etc/udev/rules.d/pci_pm.rules|2=
# whitelist for pci autosuspend
SUBSYSTEM=="pci", ATTR{vendor}=="0x1234", ATTR{device}=="0x1234", ATTR{power/control}="auto"
}}

Alternatively, to blacklist devices that are not working with PCI runtime power management and enable it for all other devices:

{{hc|/etc/udev/rules.d/pci_pm.rules|2=
# blacklist for pci runtime power management
SUBSYSTEM=="pci", ATTR{vendor}=="0x1234", ATTR{device}=="0x1234", ATTR{power/control}="on", GOTO="pci_pm_end"

SUBSYSTEM=="pci", ATTR{power/control}="auto"
LABEL="pci_pm_end"
}}

## USB autosuspend
The Linux kernel can automatically suspend USB devices when they are not in use. This can sometimes save quite a bit of power, however some USB devices are not compatible with USB power saving and start to misbehave (common for USB mice/keyboards). udev rules based on whitelist or blacklist filtering can help to mitigate the problem.

The example is enabling autosuspend for all USB devices except for keyboards and mice:

{{hc|/etc/udev/rules.d/50-usb_power_save.rules|2=
ACTION=="add", SUBSYSTEM=="usb", ATTR{product}!="*Mouse", ATTR{product}!="*Keyboard", TEST=="power/control", ATTR{power/control}="auto"
}}

To allow autosuspend only for devices that are known to work, use simple matching against vendor and product IDs (use lsusb to get these values):

{{hc|/etc/udev/rules.d/50-usb_power_save.rules|2=
# whitelist for usb autosuspend
ACTION=="add", SUBSYSTEM=="usb", TEST=="power/control", ATTR{idVendor}=="05c6", ATTR{idProduct}=="9205", ATTR{power/control}="auto"
}}

Alternatively, to blacklist devices that are not working with USB autosuspend and enable it for all other devices:

{{hc|/etc/udev/rules.d/50-usb_power_save.rules|2=
# blacklist for usb autosuspend
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="05c6", ATTR{idProduct}=="9205", GOTO="power_usb_rules_end"

ACTION=="add", SUBSYSTEM=="usb", TEST=="power/control", ATTR{power/control}="auto"
LABEL="power_usb_rules_end"
}}

The default autosuspend idle delay time is controlled by the  parameter of the  built-in kernel module. To set the delay to 5 seconds instead of the default 2 seconds, add the following kernel parameter for your boot loader.

 usbcore.autosuspend=5

Similarly to , the delay time can be fine-tuned per device by setting the  attribute. This means, alternatively, autosuspend can be disabled by setting  to -1 (i.e., never autosuspend):

{{hc|/etc/udev/rules.d/50-usb_power_save.rules|2=
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="05c6", ATTR{idProduct}=="9205", ATTR{power/autosuspend}="-1"
}}

See the [https://docs.kernel.org/driver-api/usb/power-management.html Linux kernel documentation for more information on USB power management.

## SATA Active Link Power Management
The current setting can be read from or written to  as follows:

 $ grep . /sys/class/scsi_host/host*/link_power_management_policy
 $ echo "med_power_with_dipm" >/sys/class/scsi_host/hostN/link_power_management_policy

{| class="wikitable"
|+ Available ALPM settings
! Setting
! Description
! Power saving
|-
| max_performance
| current default
| None
|-
| medium_power
| -
| ~1.0 Watts
|-
| med_power_with_dipm
| recommended setting1
| ~1.5 Watts
|-
| min_power
| WARNING: possible data loss2
| ~1.5 Watts
|}

# Since Linux 4.15 there is a setting called  that matches the behaviour of Windows IRST driver settings and should not cause data loss with recent SSDs or HDDs. The power saving can be significant, ranging from 1.0 to 1.5 Watts (when idle). It has become the default setting for Intel based laptops in Linux 4.16 In Linux 6.11 it became the default setting [https://www.phoronix.com/news/SATA-Link-Power-Linux-6.11.
#

You can configure  settings persistently by adding a udev rules file, for example:

{{hc|/etc/udev/rules.d/hd_power_save.rules|2=
ACTION=="add", SUBSYSTEM=="scsi_host", KERNEL=="host*", ATTR{link_power_management_policy}="med_power_with_dipm"
}}

## Hard disk drive
See hdparm#Power management configuration for drive parameters that can be set.

Power saving is not effective when too many programs are frequently writing to the disk. Tracking all programs, and how and when they write to disk is the way to limit disk usage. Use  to see which programs use the disk frequently. See Improving performance#Storage devices for other tips.

Small adjustments such as setting the noatime option can also help. If enough RAM is available, consider disabling or limiting swappiness as it has the possibility to limit a good number of disk writes.

For Seagate drives with PowerChoice technology, tricks setting APM via hdparm will not work due to the EPC (Extended Power Conditions) feature. Rather than setting APM, you can install   and fully disable EPC like so (replace X with actual drive letter):

 # openSeaChest_PowerControl --scan
 # openSeaChest_PowerControl -d /dev/sdX -i
 # openSeaChest_PowerControl -d /dev/sdX --showEPCSettings
 # openSeaChest_PowerControl -d /dev/sdX --EPCfeature disable
 # openSeaChest_PowerControl -d /dev/sdX --showEPCSettings

Last invocation will give the following summary:

 ==========================================================================================
  openSeaChest_PowerControl - openSeaChest drive utilities - NVMe Enabled
  Copyright (c) 2014-2023 Seagate Technology LLC and/or its Affiliates, All Rights Reserved
  openSeaChest_PowerControl Version: 3.3.1-4_1_1 X86_64
  Build Date: Jul  4 2023
  Today: Tue Jul  4 17:49:36 2023        User: root
 ==========================================================================================

 /dev/sdX - ST1000NM0008-2F2100 - ZFA19JG2 - SN02 - ATA

 ===EPC Settings===
         * = timer is enabled
         C column = Changeable
         S column = Savable
         All times are in 100 milliseconds

 Name       Current Timer Default Timer Saved Timer   Recovery Time C S
 Idle A      0            *10           *10           1             Y Y
 Idle B      0            *1200         *1200         3             Y Y
 Idle C      0             6000          6000         16            Y Y
 Standby Z   0             9000          9000         46            Y Y

Zeroes in the first column confirm that parking and spindown were disabled successfully

## Tools and scripts
## Using a script and a udev rule
Since systemd users can suspend and hibernate through  or  and handle acpi events with , it might be interesting to remove pm-utils and acpid. There is just one thing systemd cannot do (as of systemd-204): power management depending on whether the system is running on AC or battery. To fill this gap, you can create a single udev rule that runs a script when the AC adapter is plugged and unplugged:

{{hc|/etc/udev/rules.d/powersave.rules|2=
SUBSYSTEM=="power_supply", ATTR{online}=="0", RUN+="/path/to/your/script true"
SUBSYSTEM=="power_supply", ATTR{online}=="1", RUN+="/path/to/your/script false"
}}

Examples of powersave scripts:

* ftw, package:
* powersave
* throttlectl, from

The above udev rule should work as expected, but if your power settings are not updated after a suspend or hibernate cycle, you should add a script in  with the following contents:

Do not forget to make it executable!

## Allow users to shutdown
## Button and lid events
The suspend, poweroff and hibernate button presses and lid close events are handled by logind as described in #ACPI events.

## Using systemd-logind
If you are using , users with non-remote session can issue power-related commands as long as the session is not broken.

To check if your session is active:

 $ loginctl show-session $XDG_SESSION_ID --property=Active

The user can then use systemctl commands in the command line, or add them to menus:

 $ systemctl poweroff
 $ systemctl reboot

Other commands can be used as well, including  and . See the System Commands section in .

## Using sudo
Install , and configure it to give the user root privileges. The user will then be able to use the  commands (e.g. , ,  and ). See the System Commands section in

## Users without root privileges
If users should only be allowed to use shutdown commands, but not have other privileges, create the following drop-in file using the  command as root. Substitute user for your username and hostname for the machine's hostname.

Now your user can shutdown with , and reboot with . Users wishing to power down a system can also use . Use the  tag only if you do not want to be prompted for your password.
