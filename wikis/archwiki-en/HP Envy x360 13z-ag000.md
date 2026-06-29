# HP Envy x360 13z-ag000

The HP Envy X360 13z-ag000 was released in 2018. It has variable processors/ram and displays, from a Ryzen Mobile 2300U to a 2700U, from 4GB RAM to 16GB RAM, and a 1080p display to a 4K display.

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad || PS/2 ||
|-
| Camera ||  ||
|-
| IR Camera ||  ||
|-
| Card reader ||  ||
|-
| Sensors ||  ||
|}

## Installation
This laptop has Secure Boot enabled by default. To start the installer you need to disable it in the UEFI. Then you can just boot the installer in UEFI mode and just install like a normal UEFI system.

There appears to be an option to use your own Secure Boot keys.

## Battery and power management
4 hour of battery life because of the 4K display.

## Display, video Card
The integrated Vega GPU works with the AMDGPU drivers.  is somewhat necessary for most applications.

## Audio
The Bang & Olufsen top soundbar is disabled by default. You can activate it by using the hdajackretask utility provided by . More information can be found in this thread: https://bugzilla.kernel.org/show_bug.cgi?id=189331.

The exact pinout can be found in this attachment: https://bugzilla.kernel.org/attachment.cgi?id=282109&action=edit.

## Touchscreen and stylus
Kernel 4.19.5 or greater is needed. [https://cdn.kernel.org/pub/linux/kernel/v4.x/ChangeLog-4.19.5

The built in ELAN digitizer does not use the wacom driver by default, but it can be configured to do so. Switching to the wacom driver allows easier configuration of the digitizer and pen through tools like xsetwacom. This can be achieved with the following xorg configuration file:

After a reboot xsetwacom should now correctly register the device.

You can use xinput to probe the different devices and find out what actions get triggered by which buttons. For instance, the "wacom bamboo ink" pen triggers the eraser device while touching the screen while maintaining the second side button pressed.

 $ xinput test $deviceID

The following simple example script will bind rightclick to the eraser device.

 device=$(xsetwacom --list | grep -i "eraser" |  awk '{print $(NF-2)}')
 xsetwacom --set "$device" button 1 3

## Orientation sensor
No IIO sensors are enumerated as of 4.18-rc7, even with all possible IIO modules compiled.  (from ) returns no sensors detected.

## Wireless networking
Using the  kernel parameter seems to prevent the card from dropping offline as much, but also worsens battery life.

## Hard Drive
Built-in NVMe drive works with advertised speed. Blockdevices are located at .
