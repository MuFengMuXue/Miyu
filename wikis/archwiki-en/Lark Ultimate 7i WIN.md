# Lark Ultimate 7i WIN

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Display || ||
|-
| #Touchscreen || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Camera (front) || ||
|-
| Camera (back) || ||
|-
| Bluetooth || ||
|-
| MicroSD Reader || ||
|-
| Accelerometer || ||
|-
|}
Lark Ultimate 7i WIN is a budget 7" tablet shipping with Windows 8, 8.1 or 10. Android versions are known to exist but were not as popular and less featured than the Windows (WIN) counterparts. There also exist 8", 10" and 11" versions of these tables and versions with 3G modem, featuring different interiors.

Lark Ultimate 7i WIN has Intel Atom Z3735G BayTrail processor with integrated graphics and 1 GB of integrated DDR3L RAM, 16 GB eMMC, 1024 x 600 pixel screen with 10-point touchscreen of unknown resolution and "Windows" button, three hardware buttons (volume up, down and power), basic accelerometer, two cameras (VGA in front, 2 Mpix in the back), microphone, mono speaker, 3.5 mm jack slot, microSD slot, miniHDMI port and one microUSB port (for data and charging). It features InsydeH20 32-bit UEFI BIOS.

## Configuration
## Installation
This tablet uses 32-bit UEFI despite having 64-bit processor.

For installation, you will most likely need some kind of USB hub, as you need to have keyboard and boot media connected. Booting from microSD was not tested. Wireless should work with recent Arch boot media.

## Touchscreen
For touchscreen to work, firmware is needed. For  (recommended) driver, copy mssl1680.fw file that was extracted from Windows drivers to  directory. Then, Calibrating Touchscreen will be needed. Until a better solution is found, this entry can be added at the bottom of  file for relatively usable touchpad:

See https://github.com/onitake/gsl-firmware/tree/master/firmware/lark/ulti7iwin and https://github.com/onitake/gsl-firmware/blob/master/README.md for more info.

## Accelerometer
 lists a BMA250E device. To see how it works, see

 $ cd /sys/bus/i2c/devices/i2c-BMA250E\:00/iio\:device0/
 $ watch cat in_accel_*_raw

## Broken devices
## Camera
According to , there is an INT0310 device (GalaxyCore GC0310 - Front Camera) and OVTI2680 device (OmniVision OV2680 - Back Camera). Both had a short-lived driver implementation as a part of Linux kernels 4.12–4.17 staging  driver https://github.com/torvalds/linux/tree/v4.17/drivers/staging/media/atomisp, which was later removed. OV2680 is implemented as a standalone driver, but it is not enabled on stock Arch kernel.

## Device info
## Devices on i2c bus
{| class="wikitable"
| i2c-10EC5640:00 || snd_soc_rt5640 || Realtek RT5640 - Sound Card
|-
| i2c-BMA250E:00 || bmc150_accel_* || Bosch BMC150 - Accelerometer
|-
| i2c-INT0310:00 || gc0310 || GalaxyCore GC0310 - Front Camera
|-
| i2c-INT33F4:00 || intel_soc_pmic_i2c || Intel I2C Interface
|-
| i2c-MSSL1680:00 || silead || GSL1680 - Silead touchescreen
|-
| i2c-OVTI2680:00 || ov2680 || OmniVision OV2680 - Back Camera
|}
