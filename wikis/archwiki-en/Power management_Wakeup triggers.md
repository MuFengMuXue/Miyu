# Power management/Wakeup triggers

Wakeup triggers are event sources that can wake the system from any of the hardware power-saving states. The obvious example is the power or suspend button, the Wake-on-LAN functionality or the lid switch in laptop systems. Wakeup triggers can be controlled through various kernel interfaces listed below. There is no unified interface covering all possible triggers.

## Wakeup trigger interfaces
## /proc/acpi/wakeup
Reading the  file yields list of ACPI-registered wakeup sources with corresponding  IDs where available. Writing an entry from the Device column to the file toggles its state. For example, to disable waking on opening the laptop lid, run:

 # echo "LID" > /proc/acpi/wakeup

## /sys/module/acpi/parameters/ec_no_wakeup
This file represents the value of ACPI kernel module option , which controls passing the wakeup triggers from embedded controller when the system is in the suspend-to-idle () power state On modern laptops embedded controller wakeups can cause excessive battery drain in some cases.

## /sys/devices/
Each  device that supports wakeup contains the file  in a device's  subdirectory. The file contains wakeup trigger's status and can be written to as well. Bus controllers as well as endpoint devices can be capable of waking up the system. For example, to disable wakeups from the first USB controller (bus), run:

 # echo "disabled" > /sys/bus/usb/devices/usb1/power/wakeup

An endpoint device should be able to wake the device if the trigger is enabled regardless of the controller's setting, however this might be hardware-dependent.

Program PowerTOP interfaces with , but it only lists wakeup triggers of networking and USB devices by reading  and  (containing symlinks to ).

## /sys/class/wakeup/*
Almost all wakeup triggers can be found in the  directory, which contains symlinks to all relevant devices. This is useful for finding possible wakeup triggers by going through subdirectories. Some of the triggers can correspond to virtual devices while hardware-related wakeup triggers are the ones that contain at least one of these files:

 /sys/class/wakeup/*/device/physical_node/power/wakeup
 /sys/class/wakeup/*/device/power/wakeup

Some of wakeup triggers in  also provide a link to the cryptic  names where the following file is present:

 /sys/class/wakeup/*/device/path

## Persistent settings
The one-time methods should suffice for setting the  states and  kernel parameter while the event-driven approach with udev is the reliable way to configure the  devices.

## One-time with systemd
The  ACPI kernel module option can be set at boot as described in the article. The standard solution to set the  values at boot are systemd services such as in this troubleshooting case. Another systemd-based manager for  is .

Some systems can override some of the ACPI wakeup triggers upon power state transition(s) in what is more of a bug rather than a feature. If the hardware is overriding triggers at predictable times that can still be solved with appropriately crafted systemd units. The  is a generic target covering all different suspended states that might be helpful in this case, but there is no generic  [https://github.com/systemd/systemd/issues/6364.

This method only works reliably with  devices that are connected all the time.

## Event-driven with udev
Setting the wakeup trigger status with udev rules is an event-driven method that works reliably any time the devices with wakeup triggers are connected. The key is to detect an addition of a new device () in a rule and set the wakeup trigger status with {{ic|1=ATTR{power/wakeup}="disabled"}}. If the hardware is resetting this setting, udev can try to circumvent it by reapplying rules upon every device change (). A device tree with possible parameters for matching a particular device found in  can be obtained with .

A representative common example here would be a Logitech Unifying USB receiver. Its wakeup trigger should be enabled by default and if that is not desired, a solution could be a udev rule, as follows:

{{hc|/etc/udev/rules.d/logitech-unifying.rules|2=
ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", ATTRS{idVendor}=="046d", ATTRS{idProduct}=="c52b", ATTR{power/wakeup}="disabled"
}}

The reverse case to enable the necessary trigger(s) is described in the udev article.

udev triggers so early in the device enumeration that disabling wakeup trigger with the method above causes (some?) disabled triggers to not be listed in . That might be dependent on whether the device was already present at boot and needs further clarification.

## Troubleshooting
## List device and/or bus trees
These auxiliary commands can be helpful when trying to understand all wakeup triggers of a certain system, to aid with udev rule writing or general wakeup source troubleshooting:

 # lshw -businfo -numeric
 # lspci -DPPnn
 # lsusb -tvv

## Last wakeup trigger source
The information on which wakeup source was the reason for the last device wakeup is unfortunately platform-specific. On x86 machines  can be used:

 # dmidecode -t system | grep -P '\tWake-up Type\: '

However for some computers it always reports "Power Switch" regardless of the real cause, e.g. for any of the USB keyboard, laptop keyboard, the power switch and the mouse.

In some cases, the wakeup count information can also be useful to find the last wakeup trigger source:

 # grep -F "" /sys/class/wakeup/*/device/power/wakeup_count

One can then compare the result after a wakeup with the values from before to find the reason for the wakeup.

## Instantaneous wakeup after suspending
## Intel Haswell with LynxPoint(-LP)
For some Intel Haswell systems with the LynxPoint and LynxPoint-LP chipset, instantaneous wakeups after suspending are reported. They are linked to erroneous BIOS ACPI implementations and how the  module interprets it during boot. As a work-around reported affected systems are added to a denylist (named ) by the kernel case-by-case Wakeup may happen, for example, if a USB device is plugged during suspending and ACPI wakeup triggers are enabled. A viable workaround for such a system is to disable the relevant wakeup triggers. An example to disable wakeup through USB is described as follows [https://bbs.archlinux.org/viewtopic.php?pid=1575617.

To view the current configuration:

The relevant devices are ,  and  (for USB 3.0). To toggle their state you have to echo the device name to the file as root:

 # echo EHC1 > /proc/acpi/wakeup
 # echo EHC2 > /proc/acpi/wakeup
 # echo XHC > /proc/acpi/wakeup

This should result in suspension working again. However, this settings are only temporary and need to be set at every boot. To automate this, see systemd-tmpfiles or BBS thread for possible solutions.

## Gigabyte motherboards
## GPP bridge
On some Gigabyte motherboards, the GPP bridge to the NVMe drive may cause premature wakeups from suspend.

Known boards affected:
* B550i AORUS,
* B550 AORUS ELITE V2,
* B550 AORUS ELITE AX V2 (Rev. 1.5),
* B550M DS3H
* B550M AORUS PRO-P
* A520M K V2

Setting the status of  to disabled may fix the issue:

 # echo GPP0 > /proc/acpi/wakeup

This setting is only temporary. Disabling it for all PCIe devices can be made permanent using a udev rule: {{hc|/etc/udev/rules.d/90-gigabyte.rules|2=ACTION=="add", SUBSYSTEM=="pci", DRIVER=="pcieport", ATTR{power/wakeup}="disabled"}}

It's also possible to target the specific device: {{hc|/etc/udev/rules.d/90-gigabyte.rules|2=ACTION=="add", SUBSYSTEM=="pci", KERNEL=="0000:00:01.1", ATTR{power/wakeup}="disabled"}}

The value for  is the  column, without the  prefix, from .

## ACPI _OSI string
For some Gigabyte motherboards, disabling everything in  including  does not prevent an instantaneous wakeup from suspension. If this is the case, your motherboard may have issues with ACPI in Linux.

Known boards affected:

* B850M AORUS ELITE WIFI6E ICE
* B850 GAMING X WIFI6E
* B650 GAMING X AX V2
* B650 AORUS ELITE AX (Rev. 1.0)
* B650M AORUS ELITE AX
* B650 EAGLE AX
* B650i AORUS ULTRA (Rev. 1.0)
* X670E AORUS PRO X
* X670 GAMING X AX V2
* X870E AORUS ELITE WIFI7
* X870 EAGLE WIFI7
* MSI PRO X870E-P WIFI

Apply the following to your kernel parameters:

 acpi_osi="!Windows 2015"

Some boards will also require require the OS name to be set and this will vary by BIOS version. A general  example:

 acpi_os_name="Microsoft Windows"

## ASRock AM5 motherboards
Certain ASRock motherboards for the AM5 platform may instantly wake from sleep also. This is due to the USB xHCI controller.

This can be fixed by disabling wakeup on this device, in line with the Gigabyte instructions above:

 # echo XH00 > /proc/acpi/wakeup

This behaviour has been noticed on the B850M Pro-A WiFi, the B850M Pro RS model (and will presumably also extend to the very similar B850M Pro RS WiFi.)

## MSI AM5 motherboards
Certain MSI motherboards for the AM5 platform may also be affected by the premature wakeups from suspend because of the GPP bridge to the NVME drive.

This can be fixed by disabling wakeup on this device, in line with the Gigabyte instructions above:
 # echo GPP1 > /proc/acpi/wakeup

This behaviour has been noticed on the X870 Tomahawk model.

## Ryzen 7000 Series
For some newer AMD Ryzen 7000 Series systems, instantaneous wakeups after suspending, or wake up from s2idle when plugging in the AC adapter or by closing the lid, may occur. It is due to the redundant IRQ interrupt from the GPIO controller in . The current workaround is to configure the kernel to ignore the interrupt from the problematic GPIO pins. Add the following to your kernel parameters:

 gpiolib_acpi.ignore_interrupt=AMDI0030:00@2,AMDI0030:00@3,...

Multiple GPIO pins can be appended to the ignore list in the format of . However, the corresponding GPIO pins that cause the system to wake up is depended to the device model. You may find the pin number from the  log after enabling debug messages from the system suspend/hibernation infrastructure:

 # echo 1 > /sys/power/pm_debug_messages

Perform a suspend/resume cycle, you may find the following lines in  log.

 kernel: GPIO 3 is active: 0x30047ce0

Usually GPIO 2, 3 and 4 would be the one response to this issue. Then, you may mount the  to  to trace the state of the GPIOs.

Look for the lines in  with data in  and  columns.

 gpio      int|active|trigger|S0i3| S3|S4/S5| Z|wake|pull|  orient|       debounce|reg
 #3         😛|     ↑|   edge|  ⏰| ⏰|     |  |    |    |input  ↑|               |0x54800

Ignore the corresponding GPIO pins in , regenerate the initramfs image, and reboot.

## NVIDIA drivers
Installing NVIDIA proprietary drivers might render suspension and hibernation not possible. In that case the system log might include:

 kernel: NVRM: GPU 0000:01:00.0: PreserveVideoMemoryAllocations module parameter is set. System Power Management attempted without driver procfs suspend interface. Please refer to the 'Configuring Power Management Support' section in the driver README.
 kernel: PM: pci_pm_suspend(): nv_pmops_suspend+0x0/0x20 [nvidia returns -5
 kernel: PM: dpm_run_callback(): pci_pm_suspend+0x0/0x160 returns -5
 kernel: nvidia 0000:01:00.0: PM: failed to suspend async: error -5

See NVIDIA/Tips and tricks#Preserve video memory after suspend.

## nouveau driver
If the nouveau driver is used, the reason for instantaneous wakeups may be a bug in the driver, which sometimes prevents GPU from suspending. A possible workaround is unloading the  kernel module right before going to sleep and loading it back after wakeup. To do this, create the following script:

The first echo line unbinds  from the framebuffer console driver (). Usually it is  as in this example, but it may also be another . See  which one of them is a frame buffer device ==== Logi Bolt receiver ====

The Logitech Bolt receiver is a dongle with a yellow hexagon that has a lightning bolt shape cut out of it. It can cause immediate wakeup after suspending. See Logitech Unifying Receiver#PC wakes immediately from sleep.

## intel_hid kernel module
As is described in [https://bugzilla.kernel.org/show_bug.cgi?id=218634 and https://bbs.archlinux.org/viewtopic.php?pid=2179723#p2179723, the kernel module  prevents suspend to disk and causes wakeup immediately on some Dell laptops. Simple workaround is blacklisting  or unload this module before suspending to disk.
