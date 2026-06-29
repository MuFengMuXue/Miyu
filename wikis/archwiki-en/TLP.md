# TLP

TLP is a feature-rich command line utility for Linux, saving laptop battery power without the need to delve deeper into technical details.

TLP's default settings are already optimized for battery life and implement Powertop's recommendations out of the box, so additional configuration is not needed. Also, TLP is completely customizable, which means you can get even more power savings or meet your exact requirements.

TLP intentionally excludes some settings from the project, notably Fan speed control and Backlight.

## Installation
Install the  package. Installing the optional dependencies may help provide additional power saving.

Enable/start .

One should also mask the service  and socket  to avoid conflicts and ensure proper operation of TLP's radio device switching options.

## Replace power-profiles-daemon support in Desktop Environments
To be able to use the power profiles interface in power-profiles-daemon used by GNOME and KDE, install .

See TLP FAQ for details.

## Radio Device Wizard (tlp-rdw)
When using the Radio Device Wizard (), it is required to use NetworkManager and enabling .

See TLP settings for details.

## Front end
*  is a GTK user interface for TLP written in Python.
*  is a different GTK interface that works with additional drivers like AMD and NVIDIA.

## ThinkPads only
Controlling the charge thresholds using D-Bus without root privileges is possible using  and its example Qt user interface . Note: threshy is no longer maintained by its developer.

## Before Sandy Bridge (until 2010)
For ThinkPads before model year 2011, the tp_smapi kernel module is required. See tp_smapi#Installation for kernel-specific installation instructions.

## Configuration
The configuration file is located at  and provides a largely optimized power saving by default. For a full explanation of options see: TLP settings.
Instead of editing this file directly, you can also place files in , for example  with the desired changes. If the same parameter is defined in both places, the value set in  takes precedence.

## USB autosuspend
When starting TLP with the default configuration, some USB devices such as audio DACs will be powered down when running on battery due to TLP's autosuspend feature. Some devices such as keyboards and scanners are blacklisted from autosuspend by default.

You may simply want to disable USB autosuspend entirely with the following setting:

Or blacklist specific devices from being auto-suspended. See the TLP documentation on USB devices for details.

## Force balanced (BAL) power profile
When no power supply can be detected, the performance power profile (PRF) will be used on devices like desktops and embedded hardware.

You may want to force the balanced (BAL) or power-saving (SAV) profile when using TLP on these devices to enable more power saving:

(Note: Legacy values AC and BAT continue to work. They are mapped to PRF and BAL, respectively.)

## Bumblebee with NVIDIA driver
If you are running Bumblebee with NVIDIA driver, you need to disable power management for the GPU in TLP in order to make Bumblebee control the power of the GPU.

Depending on the driver(s) that you are using, blacklist one or more of them, preventing TLP from managing their power state:

## PRIME with NVIDIA driver
If you are running PRIME with NVIDIA driver, do not disable power management for the GPU in TLP.
Instead, you may want to enable power management all the time to prevent your laptop from heating by adding the NVIDIA card PCI ID () to the variable :

## PCI(e) runtime power management on AC
Enabling runtime power management for PCI(e) bus devices while on AC may improve power saving on some laptops. This is enabled by default on battery, but not on AC. To enable on AC, set:

## Enable Wi-Fi radio on boot
By default, TLP stops the Wi-Fi radio from automatically powering on. Although definitely power-saving, most users might find this behavior undesirable. To make Wi-Fi start on boot, set the following:

## Command line
TLP provides several command line tools. See TLP commands.

## Troubleshooting
For debugging you can display information about the currently used Mode(AC/BAT) and applied configurations:

 # tlp-stat

See also the upstream troubleshooting guide.

## hci0: link tx timeout
If your bluetooth headphones suddenly stop working and you see this error from dmesg, it may be caused by TLP suspending your device. Add device ID to  in :

 # Disable bluetooth autosuspend
 USB_DENYLIST="8087:0aaa"

Get the device ID for your bluetooth device from . Restart TLP and the  service.
