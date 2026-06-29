# Lenovo ThinkPad T480s

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) || ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| TrackPoint || ||  |-
| Touchpad || ||  [https://bugzilla.kernel.org/show_bug.cgi?id=219352
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Mobile broadband || ||
|-
| Bluetooth ||  ||
|-
| Smartcard reader ||  ||
|-
|SD card reader ||  ||
|-
| PrivacyGuard || ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo T480s laptop. For the most part things work out-of-the-box, but some features may need to be configured manually.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Powersaving
Without special configuration and with default firmware settings, power usage is a bit high (around 7,5W in idle). There are a few knobs to improve battery life:

* Set "Thunderbolt BIOS Assist Mode" to "Enabled" in the EFI firmware interface. This seems to reduce number of idle wakeups.
** However, kernel versions since 4.19+ should support it natively (and some power consumption improvements is reported if this is switched to "Disabled" [https://forums.lenovo.com/t5/Other-Linux-Discussions/Thunderbolt-Software-and-Firmware-updates-and-Linux/m-p/4552148?page=7#4631439.
* Disable unused peripherals under "Security" -> "I/O port access" in the firmware. This especially applies to the SD/MMC-cardreader, which seems to drain some power even when idle

As of Kernel 4.15, DisplayPort PSR (Panel self refresh) is disabled by default and broken when forcibly enabled (system hangs after a few seconds, display lag). 4.17-rc1 seems to improve a lot in this regard, but PSR still sometimes causes the screen to freeze for a few seconds.

## SD card reader
According to various reports the SD card reader drains several watts of power. If you do not want to disable it in bios because you use it semi-regularly, you can turn it off by unbinding its driver using this command:

 # echo 2-3 > /sys/bus/usb/drivers/usb/unbind

You can then turn the reader back on by running:

 # echo 2-3 > /sys/bus/usb/drivers/usb/bind

## Fingerprint reader
The fingerprint sensor is not supported by libfprint.

There is a project python-validity based on open-fprintd, see Install  and enroll your fingerprint:

 $ fprintd-enroll

Refer to Fprint#Configuration for configuration.

You may experience an issue where the fingerprint reader does not work after the laptop wakes up from suspension. To fix this, try enabling the  and  systemd services [https://github.com/Tomcat-42/python-validity#fingerprint-not-working-after-waking-up-from-suspend. If the issue is still present, create a unit file as follows, then enable it If this solves the issue, you may disable  and  again.

## PrivacyGuard
The PrivacyGuard feature is referred to as [https://docs.kernel.org/admin-guide/laptops/thinkpad-acpi.html#lcd-shadow-control LCD Shadow and was introduced in Linux 5.4.To enable or turn on the LCD shadow:

 # echo 1 > /proc/acpi/ibm/lcdshadow

Conversely, use  to disable it:

 # echo 0 > /proc/acpi/ibm/lcdshadow

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
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
|  || 3 ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Controls the keyboard backlight
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
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# This key has a keyboard symbol on it. According to Lenovo, it should open the keyboard settings page [https://support.lenovo.com/us/en/solutions/vid500090-thinkpad-function-keys-fn-key-with-f1-to-f12-keys-overview, which it does on Windows 10. It does generate an event on Wayland, but not on X.

## Troubleshooting
## Thermal throttling
There are reported throttling issues for Lenovo T480/T480s/X1C6 notebooks.This script forces the CPU package power limit (PL1/2) to 44 W (29 W on battery) and the temperature trip point to 95 'C (85 'C on battery) by overriding default values in MSR and MCHBAR every 5 seconds (30 on battery) to block the Embedded Controller from resetting these values to default.

Install the  package and enable the .[https://github.com/erpalma/throttled

It is recommended to also undervolt the CPU (Undervolting CPU#intel-undervolt). Most Kaby Lake R chips are able to easily undervolt to -100mV or more, which significantly helps to keep the device from thermal throttling. Throttled also provides undervolting capabilities and will overwrite the undervolt settings applied by intel-undervolt when it updates settings if both services are enabled.

## Fix freezes/hangs on QT applications (with Intel driver)
See Intel graphics#AccelMethod.
