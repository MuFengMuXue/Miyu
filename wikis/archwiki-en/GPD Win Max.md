# GPD Win Max

{| class="wikitable archwiki-table-laptop"
! Hardware !! Bus + ID !! Working !! Bus + ID !! Working !! Bus + ID !! Working
|-
| || colspan="2" | Win Max || colspan="2" | Win Max 2021 || colspan="2" | Win Max 2
|-
| Video ||  ||  ||  ||  ||  ||
|-
| Wireless ||  ||  ||  ||  ||  ||
|-
| Ethernet ||  ||  ||  ||  ||  ||
|-
| Bluetooth ||  ||  ||  ||  ||  ||
|-
| Audio ||  ||  ||  ||  ||  ||
|-
| Camera ||  ||  ||  ||  ||  ||
|-
| Keyboard ||  ||  ||  ||  ||  ||
|-
| Touchpad ||  ||  ||  ||  ||  ||
|-
| Gamepad || ||  || ||  ||  ||
|-
| Touchscreen ||  ||  ||  ||  ||  ||
|-
| Stylus ||  ||  ||  ||  ||  ||
|-
| MicroSD ||  ||  ||  ||  ||  ||
|-
| SD Card || ||  ||  ||  ||  ||
|-
| Fingerprint ||  ||  ||  ||  ||  ||
|-
| IMU ||  ||  ||  ||  ||  ||
|}

## Models
There are several models in the GPD Win Max family, some multiple SKUs.

## GPD Win Max (2020)
* Display: 8" 1280x800
* CPU: Intel Core i5-1037G7
* Graphics: Intel Iris Plus 940
* RAM: 16 GB LPDDR4x 3733
* Storage: 512 GB PCIe M.2 NVMe SSD
* Network: 1 GbE, Intel WiFi 6 AX, BT 5.0
* Thunderbolt 3

## GPD Win Max 2021
* Display: 8" 1280x800
* CPU: Intel Core i7-1195G7 / AMD Ryzen 7 4800U
* Graphics: Intel Iris Xe G7 / AMD Radeon Vega 8
* RAM: 16 GB LPDDR4x 4226
* Storage: 1 TB PCIe M.2 NVMe SSD
* Network: 1 GbE, Intel WiFi 6 AX BT 5.0
* Thunderbolt 4 (Intel)

## GPD Win Max 2 (2022)
* Display: 10.1" 2560x1600
* CPU: Intel Core i7-1260P / AMD Ryzen 7 6800U
* Graphics: Intel Iris Xe / AMD Radeon 680M
* RAM: 16/32 GB LPDDR5 6400
* Storage: 1/2 TB PCIe 4.0 M.2 NVMe SSD
* Network: Intel WiFi 6 AX BT 5.2
* Thunderbolt 4 (Intel) | USB4 (AMD)

## GPD Win Max 2 (2023)
* Display: 10.1" 2560x1600
* CPU: AMD Ryzen 7 7640U / AMD Ryzen 7 7840U
* Graphics: AMD Radeon 680M / AMD Radeon 780M
* RAM: 16/32/64 GB LPDDR5 6400
* Storage: 1/2 TB PCIe 4.0 M.2 NVMe SSD
* Network: Intel WiFi 6 AX210 BT 5.2
* USB4

## Driver
## Fan driver
Here is an experimental driver that expose GPD device's fan to kernel's hwmon subsystem: gpd-fan-driver. It has been packaged on AUR

Warn: This driver has not been fully tested and reviewed. It may cause damage to your device. Use at your own risk.

## Fixes
## GPD Win Max 2020/2021
## Touchscreen
If you are using Xorg, create the file:  to rotate the touchscreen.

## Mute Key
The mute key does not send a release code. To fix it, create a new udev hwdb file under , and configure the key to trigger an automatic release event.

## GPD Win Max 2021
## Screen rotation
This device uses a portrait screen, see Tablet PC#Screen rotation.

## GPD Win Max 2
## Keyboard
BIOS  5.18.9: the keyboard IRQ, as specified in the BIOS, is incompatible with a change made in kernel 5.18.10 targeting AMD 6000 APUs.

Consequently, the keyboard will not work without either patching the kernel or applying a DSDT override.

Kernel patch:

{{hc|kbd_irq.patch|
diff --git a/drivers/acpi/resource.c b/drivers/acpi/resource.c
index 510cdec375c4..c2d494784425 100644
--- a/drivers/acpi/resource.c
+++ b/drivers/acpi/resource.c
@@ -416,16 +416,6 @@ static bool acpi_dev_irq_override(u32 gsi, u8 triggering, u8 polarity,
 {
 	int i;

-#ifdef CONFIG_X86
-	/*
-	 * IRQ override is not needed on modern AMD Zen systems and
-	 * this override breaks active low IRQs on AMD Ryzen 6000 and
-	 * newer systems. Skip it.
-	 */
-	if (boot_cpu_has(X86_FEATURE_ZEN))
-		return false;
-#endif
-
 	for (i = 0; i  DefinitionBlock ("", "DSDT", 2, "ALASKA", "A M I ", 0x0107200a)
7102c7102
                 IRQ (Level, ActiveLow, Exclusive, )
7121c7121
                     IRQ (Level, ActiveLow, Exclusive, )
}}

## IMU (Accelerometer + Gyro)
The IMU (Bosch BMI160) is incorrectly identified in the BIOS.  A DKMS patch may be applied.

Alternatively, a DSDT override may be generated with the correct part number.  The aformentioned keyboard fix and following IMU fix may be combined into a single DSDT override.

DSDT changes:

## GPD Win Max 2 (2023)
## Sleep/ Si0X
With the old BIOS, The GPD Win Max 2 2023 edition might have problems with sleep: It might wake up (instantaneously or after some time). It is now working on https://gitlab.freedesktop.org/drm/amd/-/issues/3073.

It is now fixed in the .38 BIOS.

## IMU (Accelerometer + Gyro)
With the old BIOS, the IMU (Bosch BMI260) is incorrectly identified in the BIOS. It is named  in ACPI table. It is now corrected in the .40 BIOS.

The package  installs the correct kernel driver  and the sensor works with that. (For low level testing, use  from package .)
Kernel modules ,  and  can be blacklisted to stop false autoload if not needed for some external device.

## Known issues
## GPD Win Max 2021 (Intel)
## Deep sleep
Deep sleep is not working and there is no fix.

## GPD Win Max 2
## Fingerprint reader
The fingerprint reader (ChipSailing CS9711 @ USB 5.4) now has a experimental support for libfprint ==== USB autosuspend ====

On BIOS version v1.04, the USB controller may fail to enumerate devices that are newly plugged in after boot. This is due to a bug with USB suspend support and can be worked around by disabling autosuspend with the kernel parameter .

## GPD Win Max 2 (2023)
## Fingerprint reader
The fingerprint reader (ChipSailing CS9711 @ USB 5.4) now has a experimental support for libfprint [https://github.com/ddlsmurf/libfprint-CS9711

## USB4/Thunderbolt eGPU Crashes
Using an eGPU via USB4/Thunderbolt (not OCuLink) may result in PCIe errors causing the desktop environment and/or application using the eGPU to crash. To ignore these errors, try adding the kernel parameter ; this disables PCI Express Advanced Error Reporting which disables reporting and mitigation of PCIe errors but does not actually resolve the errors. The errors, however, do not appear to hinder the functioning of the GPU.

## Notes
## GPD Win Max (2020) kernel requirement
The 2020 variant uses a different location for EDID that is not supported by Linux kernels prior to 5.18.

Linux kernel 5.18 or above is required for the screen to work.

## BIOS updates
 is not supported.

GPD provides BIOS updates via Windows executables in the following locations:

* GPD Win Max: https://gpd.hk/gpdwinmaxfirmware
* GPD Win Max 2021: https://gpd.hk/gpdwinmax2021firmwaredriver
* GPD Win Max 2: https://gpd.hk/gpdwinmax2firmwareanddriver

See Windows PE for instructions on how to make a bootable Windows environment to apply the updates.
