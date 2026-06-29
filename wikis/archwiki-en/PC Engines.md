# PC Engines

PC Engines is a Swiss hardware manufacturer for embedded x86 devices.

## apu2c4
This document describes how to install Arch Linux to the SSD via an SD card or USB flash drive.

## Hardware
CPU: AMD Embedded G series GX-412TC, 1 GHz quad Jaguar core with 64 bit

RAM: 4GB DRAM with ECC

Assemble the device with care and read the guide for the cooling system!

## Setup preperations
* You need a serial (RS-232) connection to the APU to control it.
* Add your user to uucp.
* Install  or something similar, see Working with the serial console#Making Connections.
* Download and verify the installation image.

## Boot the system
To see the BIOS use this command:

 $ LANG=C picocom --baud 115200 /dev/ttyUSB0

If your device does not boot from the SD card or USB flash drive, press  during boot to bring up a boot menu.
Then close picocom with

Reconnect to the Archiso GRUB:

 $ LANG=C picocom --baud 38400 /dev/ttyUSB0

Enter CLI mode by pressing , and append the following kernel parameter to the line:

 console=ttyS0,115200

Press .

Now exit picocom and reconnect with the first command again to switch to the higher baud rate of 115200.
Finally wait for about 30 seconds and you will get a colorful boot prompt.

## Install the system
The most comfortable way to install Arch now is to start the ssh server and use the installation guide.

You may need to get a new IP with dhclient and start .

One possible layout of the SSD maybe looking like this:

  /dev/sda1           2048   264191   262144  128M 83 Linux
  /dev/sda2         264192 25430015 25165824   12G 83 Linux
  /dev/sda3       25430016 31277231  5847216  2.8G 82 Linux swap / Solaris

It is a good idea to use a MBR layout with GRUB:

 # grub-install --target=i386-pc /dev/sda
 # grub-mkconfig -o /boot/grub/grub.cfg

If using Syslinux, make sure to provide a  option in the boot menu:

See also Working with the serial console#Configure console access on the target machine.

Remember to remove the SD card or USB flash drive after you finished your setup.

## LED Control
While there are 2 mainline kernel drivers ( and ) that can control the LEDs on various APU models, if you are running mainline PC Engines firmware it is advised to let ACPI handle LED control. In conjunction with the  module,  the APU LEDs can be controlled through the following sysfs entries:

 /sys/class/leds/apu2:green:led1
 /sys/class/leds/apu2:green:led2
 /sys/class/leds/apu2:green:led3

## Module Handling
You will have to manually load . You also want to blacklist both  and .

## Example Configuration
A common use case is to use the APU as a wireless router. In this scenario, one wired NIC () is connected upstream to an ISP and the remaining wired & wireless NICs are bridged () together as the LAN. A typical LED configuration using the netdev trigger might be:

 LED1: power on / power off indicator
 LED2: upstream network (wan0) traffic indicator
 LED3: local network (br0) traffic indicator

To enable this setup:

## Persist Configuration
Systemd automatic module loading and tmpfiles.d can be used to persist this configuration across restarts.

## Firmware
The APUx devices use coreboot firmware, not UEFI. To update the firmware on APU2/3/4/5 devices, use :

Then unplug and replug. If a full reboot is impossible, e.g. because firmware is being updated remotely, workarounds are available. For details, see:

* APUx firmware flashing
* APUx firmware downloads

## Troubleshooting
## BIOS serial console interfering with GRUB serial console
If the GRUB boot screen shows most characters twice, check if the serial console in the BIOS menu is enabled and disable it. See https://forum.ipxe.org/showthread.php?tid=7809 for details.
