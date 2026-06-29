# Lenovo Yoga 9 14ITL5

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Touchscreen || ||
|-
| Stylus || ||
|-
| Video ||  ||
|-
| Webcam (Chicony) ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Accelerometer ||  ||
|-
| Tablet mode trigger || ||
|-
| Fingerprint reader ||  ||
|}

## Installation
Use  to enter BIOS. You must disable Secure Boot to be able to boot from the installation media. UEFI boot mode (OS Optimized Defaults) is working fine and can be used.

## Firmware
Support for firmware updates through fwupd is supported. But Lenovo so far only provides firmware updates for devices where Linux is officially supported (Thinkpad/ThinkCentre series). As this is not a device of these series, do not expect firmware updates through fwupd.

Firmware updates through fwupd are supported (but unavailable) for the following components:

* System firmware (Lenovo)
* UEFI (Lenovo)
* NVM Express Solid State Drive (Sandisk)

## Suspend
Suspending to system sleep state S3 is not available on the Intel 11th gen mobile CPUs found in this laptop Forcibly suspending the device to S3 leads to it locking up. If this happens, you can restore your device to working order via a hard reset. To hard reset the Yoga 9, press the power button for at least 15 seconds.

More recent Linux kernels will instead detect and use system sleep state S0ix automatically. Depending on your specific hardware configuration you may experience fast battery drain when using S0ix. The likely cause is a bug in the firmware of the SSD (WDC PC SN730 SDBPNTY-1T00-1101, Firmware (fwupd): 11170001) that keeps it in the D0 state (fully on state). This keeps part of the platform in an inefficient S0ix state with some PCIe busses running on full power. To verify whether this bug impacts your specific setup, use the [https://github.com/intel/S0ixSelftestTool S0ixSelftestTool. Discussion around this bug and potential solutions can be found in Talk:Lenovo Yoga 9 14ITL5.

If you wish to eliminate battery drain, but still want to benefit from the fast wakeup times of S0ix, consider using Suspend then Hibernate (Power management/Suspend and hibernate#Hibernation). You can configure your machine to hibernate after sleeping in S0ix for a specific duration of time by configuring the lid close action to  and tuning .

## Accelerometer
You must use  instead of  for the accelerometer to work. It is important to note, that the trigger for tablet mode does currently not work. At least within KDE you can enable automatic screen rotation only globally.

## Audio
This laptop requires Sound Open Firmware in order for the soundcard to work.

## Thermals
It is recommended to enable  in the BIOS settings. Enabling this option improves the thermal properties of the system tremendously. Without it, thermald will not throttle the system before it is near its critical temperature. You may want to select the appropriate cooling strategy in the BIOS (intelligent/performance/power saving).

## Power management
Tools like tp_smapi or tpacpi-bat do not work with this device.

To set the Battery Conservation Mode see Laptop/Lenovo#Battery conservation mode.

## Wireless devices
Rfkill reports two additional devices (, ). Blocking or unblocking these devices has no effect. Instead use the devices:

*  for Wireless LAN
*  for Bluetooth

## Function keys
Fn lock only locks for  to . The  and the  buttons still require the use of  even with Fn lock enabled.

The keys  and  only function with .

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Toggles Fn lock
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
| "Star" with 'S' || 4 ||  ||
|-
| "Star" with 'S' (long pressed) || 4 ||  ||
|-
| "Dashed circle" with "scissor" || 4 ||  ||
|-
|  ||  ||  || Cycles states of keyboard backlight
|-
|  ||  ||  ||  (in xev )
|-
|  ||  ||  ||  (in xev )
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd-logind handles this by default.
# Only with

## Tablet Mode
Installing  will generate the necessary events to trigger tablet mode.
