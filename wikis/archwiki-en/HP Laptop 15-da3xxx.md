# HP Laptop 15-da3xxx

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
| GPU ||  ||
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| SD-card reader || ||
|-
| Audio ||  ||
|}

The HP Laptop 15-da3xxx (as reported by  under "Product Name",  the exact model can be found by entering the "Serial Number" on HP's laptop support site) features a 39.6 cm (15.6") diagonal HD display and Intel® Core™ i3-1005G1 with integrated graphics (ICL GT1).

## Installation
The Realtek RTL8821CE Wi-Fi card and the Intel iGPU require  to be installed.

During installation, its possible that the keyboard and touchpad will suddenly stop working due to a bug discussed below. Use external keyboard and mouse, or use the fix below.

## Accessibility
The UEFI setup is a simple, text-based interface, navigated with a keyboard. It does not expose many options apart from the standard time/date settings and boot configurations.

To show a list of all available menus, press .

To access the UEFI setup, press .

To access the boot menu, press .

## Power management
The idle battery drain is around 3-4 watts with TLP defaults. Under moderate browser use (10-15 tabs), it can last for up to 4 hours.

## Wi-Fi driver crash when waking from powersave state
The Wi-Fi driver, rtw88, can crash due to failure to wake from powersave state. This can cause sudden degradation in Wi-Fi performance.

The fix is to disable Wi-Fi powersave:

 # iw wlan0 set power_save off

This gets reset after reboot so its necessary to execute this on every boot or disable it in TLP.

## Suspension
The laptop faces a number of issues when waking from suspension. The supported methods are:

Thus, both suspend to RAM and suspend to idle are supported. The issues below have been noticed when using suspend to RAM but might also be present when using suspend to idle.

## Lag after waking
After waking from suspend, there is an input lag for up to 10 seconds. No input is accepted during this time. Fix has not yet been found.

There is also lag in waking from suspend, up to 20 seconds.

## Integrated keyboard and touchpad not working after waking
After waking up, keyboard and mouse will not work. The precise fix for this is not known but the combination of the following kernel flags are known to fix the issue:

 psmouse.synaptics_intertouch=1 i8042.nopnp=1 i8042.reset

Its possible not all of these flags are required so further testing is suggested to pinpoint the exact combination.

## USB connected peripherals stop working after waking
The xHCI host is non responsive after waking up. The following kernel errors are logged:

This causes all USB peripherals to stop working.

The temporary fix is to unbind and rebind the xHCI host (change the ID if different):

 # echo -n "0000:00:14.0" > /sys/bus/pci/drivers/xhci_hcd/bind

 # echo -n "0000:00:14.0" > /sys/bus/pci/drivers/xhci_hcd/unbind

To fix this permanently, use the quirk , using the kernel arg . This has been tested to work.

But if for some reason that does not work, turning off USB Autosuspend might help. Either pass the additional kernel parameter  or configure it in TLP.

## Function keys
By default, keys - perform their alternative functions, and  is needed to press , but there is a UEFI option to change this behavior. The following table assumes the default behavior (i.e., for , need to press , and so on).

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect3
|-
|  ||  ||  || , Shows Help
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , Changes Display Output
|-
|  ||  ||  || No effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# All effects as output by .

## Firmware
fwupd does not support this device.

## Kernel errors
The following ACPI errors are visible on boot:

Additionally, the following warnings are also present:

And when the laptop is shutting down, watchdog fails to stop leading to this (critical) error:

However, these errors have had no noticeable impact on the system.
