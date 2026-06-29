# Acer C720 Chromebook

The Acer C720 Chromebook (and newer Chromebooks in general) features a "legacy boot" mode that makes it easy to boot Linux and other operating systems. The legacy boot mode is provided by the SeaBIOS payload of Coreboot. SeaBIOS behaves like a traditional BIOS that boots into the MBR of a disk, and from there into your BIOS-compatible boot loaders.

## Installation
Go to the Chrome OS devices page, read the Introduction and continue by following the Installation guide.

## Configuration
For information on general Chromebook post installation configuration (hotkeys, power key handling ...) see the Post installation configuration on the Chrome OS devices page.

## Touchpad Configuration
See the libinput article on how to install and setup your touchpad.

## Improving WLAN and BT performance
The C720 comes with Atheros AR9462 WLAN and Bluetooth chip which is supported by the  kernel module, the following kernel module parameters to the  module can help to affect the performance, quality and power consumption of the chip.

Details of possible settings are below.

## Bluetooth coexistence
Both Bluetooth and WiFi can use 2.4 GHz, which can cause interference. You can enable Bluetooth coexistence to improve the performance of the card with the parameter .

## Power saving
You can enable power savings with the option  to reduce power usage, though it has been suggested that enabling it might be related to system freezes and also to dropouts so if you encounter such issues then you might want to make sure it is disabled ().

## Improving signal quality
Enable antenna diversity with the option  to improve the signal quality and boost performance. However, keep in mind that this disables the bluetooth interface and, as such, bluetooth coexistence  must not be loaded at the same time.

## Fixing decrease in bandwidth
If you are experiencing a decrease in bandwidth at seemingly random times try switching from hardware to software wireless encryption as explained in Wireless network configuration#ath9k.

## Suspend
## Fix wakeup from suspend on lid close
When the lid of the C720 is closed, the top of the screen presses against the touchpad, instantly waking the computer from suspend. To disable wakeup by touchpad, create the following file:

To check the current state:

 # grep TPAD /proc/acpi/wakeup

Alternatively, it may be toggled manually by running:

 # echo TPAD > /proc/acpi/wakeup

This method does not persist after a reboot.

## Lots of ehci errors in dmesg after resume
See Chrome OS devices#Fixing suspend.  Additionally, [https://github.com/vonbrownie/linux-post-install/blob/master/config/c720_jessiebook/lib/systemd/system-sleep/ehci-pci.sh, and [https://bugzilla.redhat.com/show_bug.cgi?id=1218734 may be helpful.

One symptom may be that it cannot properly shut down or reboot.

## Locating the Write-Protect Screw
* Remove the bottom panel of the laptop by removing the 12 visible screws and another one underneath the warranty sticker.
* Separate the plastic starting at the back.
* Remove completely the write-protect screw from the motherboard, which is labelled as #7 in this picture.

## Known issues
## System freezes
See power saving section at Improving WLAN and BT performance.

Additionally see SSD#Troubleshooting if the system freezes are associated with hard drive errors in the system's journal.

## Internal microphone not working
If your internal microphone is not working, select "Microphone (unplugged)" as your input source in the PulseAudio Volume Control. Your internal microphone should now work. See also Chrome OS devices#Fixing audio for another possible solution.

## System shutdown on battery
If you are on battery and the system shutdown when you use the keyboard, it is probably a battery switch mulfunction (cover do not press it all time), labbeled #5 in [https://web.archive.org/web/20211201002401/https://www.chromium.org/_/rsrc/1381990807648/chromium-os/developer-information-for-chrome-os-devices/acer-c720-chromebook/c720-chromebook-annotated-innards.png this picture. It is a safety mechanism to prevent the Acer C720 from being powered by the battery while the cover is removed.

You can bypass this switch with a screw inserted in hole #6.
