# Mechrevo WUJIE14X

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || PS/2 ||
|-
| Keyboard || PS/2 ||
|-
| GPU ||  ||
|-
| Webcam (Infrared) ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

The Mechrevo WUJIE 14X series encompasses several retail models featuring different processors and aesthetics. At least three variations are known to exist:

* Mechrevo WUJIE 14XA: Powered by an AMD Ryzen 7 8845HS processor.
* Mechrevo WUJIE 14XA Blizzard Edition (or 暴风雪, Baofengxue in Chinese): Also powered by an AMD Ryzen 7 8845HS processor.
* Mechrevo WUJIE 14X: Powered by an Intel Core Ultra 7 155H processor.

The former two models share identical hardware specifications, with the only distinction being their colorway. This page primarily focuses on these first two models.

## Installation
## Disable secure boot
Secure Boot is enabled by default. Since the installation medium does not support it, press  repeatedly during startup to access UEFI setup and disable it.

## Ethernet controller
The RJ-45 Ethernet controller requires installation of .

## Accessibility
The UEFI interface is a generic version from AMI (American Megatrends) that can be controlled with either a keyboard or a mouse, which should also make it relatively straightforward for OCR apps to parse.

To switch boot devices, repeatedly press  during startup to display a boot menu. This menu can be navigated using the arrow keys, and a selection can be made with .

This laptop is not equipped with diagnostic LEDs.

## Firmware
fwupd supports updating the UEFI CA (UEFI revocation database).

## BIOS / EC
Official support site (Chinese only) provides BIOS/EC firmware upgrades.

## SSD
The firmware of the pre-installed Crucial SSD can be upgraded. See Solid state drive#Crucial for details.

## Hardware control
On Windows, the pre-installed UWP application, Mechrevo Control Console, is used to control features such as keyboard backlighting, performance/thermal profiles, as well as battery charging speed and limits. Under Arch Linux, various workarounds are available.

## Platform drivers
Because WUJIE14X utilizes a Tuxedo-compatible motherboard, the necessary platform drivers can be acquired by installing either  or  (Recommended).

These packages provide essential drivers for controlling various peripherals, and are also a dependency for some of the tools mentioned below.

## Unified control
TUXEDO Control Center () can be used to manage most hardware features, including the keyboard backlight, fans, battery modes, and performance profiles. For those seeking an all-in-one package, it is the best available alternative to Mechrevo Control Console.

## Fan
tuxedo-rs provides the ability to control cooling fan speeds and configure fan curves.

You can install  to view fan speed and temperature sensor data, and install either  or  (GUI) to set the fan curves.

## Platform profile
Platform Profile, also known as Fn Mode or Thermal Mode, is used to control the system's overall power consumption and thermal performance. On WUJIE14X, the Platform Profile includes three levels: Office / Quiet, Gaming / Balanced, and Turbo / Performance.

Aside from using TUXEDO Control Center, there is currently no other reliable method for switching between the profiles.

## Battery charging mode
The battery control interface is implemented under  by the #Platform drivers.

To view the available charging modes:

 $ cat /sys/devices/platform/tuxedo_keyboard/charging_profile/charging_profiles_available
 high_capacity balanced stationary

To set a charging mode:

 # echo mode > /sys/devices/platform/tuxedo_keyboard/charging_profile/charging_profile

## Keyboard backlight
The keyboard backlight has three brightness levels: off, low, and high. The state can always be cycled using .

At present, no known software interface exists to control the backlight. Consequently, there is no straightforward method to implement features like automatic backlight (de)activation.

## Facial authentication
The infrared camera on this laptop functions correctly. Install Howdy for facial recognition similar to Windows Hello.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  || Lock screen?3
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || 3
|-
|  ||  ||  || 3
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
# These key codes were not directly captured; they are inferred based on XF86keysym.h and . Further testing is required to confirm.

## Troubleshooting
## Wake up immediately from sleeping
After suspending to idle, the laptop might immediately wake up. You can disable certain wake-up signals from the Embedded Controller (EC) by adding the kernel parameter .
