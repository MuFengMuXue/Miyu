# Broadcom wireless

This article details how to install and setup a Broadcom wireless network device.

## History
Broadcom has a noted history with its support for Wi-Fi devices regarding GNU/Linux. For a good portion of its initial history, Broadcom devices were either entirely unsupported or required the user to tinker with the firmware. The limited set of wireless devices that were supported were done so by a reverse-engineered driver. The reverse-engineered  driver was introduced in the 2.6.24 kernel.

In August 2008, Broadcom released the 802.11 Linux STA driver officially supporting Broadcom wireless devices on GNU/Linux. This is a restrictively licensed driver and it does not work with hidden ESSIDs, but Broadcom promised to work towards a more open approach in the future.

In September 2010, Broadcom released a fully open source driver. The brcm80211 driver was introduced in the 2.6.37 kernel and in the 2.6.39 kernel it was sub-divided into the  and  drivers.

The types of available drivers are:

{| class="wikitable"
! Driver      !! Description
|-
| brcm80211   || Kernel driver mainline version
|-
| b43         || Kernel driver reverse-engineered version
|-
| broadcom-wl || Broadcom driver with restricted license
|}

## Driver selection
To know what driver(s) are operable on the computer's Broadcom wireless network device, the device ID and chipset name will need to be detected. Cross-reference them with the driver list of devices supported by the brcm80211 and b43 drivers.

Check if your device is supported by the builtin kernel driver brcm80211 first before resorting to other drivers.

 $ lspci -vnn -d 14e4:

## Installation
## brcm80211
The kernel contains two built-in open-source drivers: brcmfmac for native FullMAC and brcmsmac for mac80211-based SoftMAC. They should be automatically loaded when booting.

Chips supported by the brcm80211 driver can be found in ==== BCM43602 802.11ac Wireless LAN SoC ====

BCM43602 needs the  kernel parameter as tested with PCI Device ID  (see [https://bbs.archlinux.org/viewtopic.php?id=298025&p=2 BBS#298025).

## b43
Two reverse-engineered open-source drivers are built-in to the kernel: b43 and b43legacy. b43 supports most newer Broadcom chipsets, while the b43legacy driver only supports the early BCM4301 and BCM4306 rev.2 chipsets. To avoid erroneous detection of your Wi-Fi cards chipset, blacklist the unused driver.

Both of these drivers require non-free firmware to function. Install , , or  depending on the chipset.

The  should be loaded automatically, but you may need to explicitly load the module at boot.

## broadcom-wl
There are two variants of the restrictively licensed driver:

* the regular variant:
* the DKMS variant:

## Known issues
## Ethernet card is not detected
Broadcom wireless module has a history of conflicting with Broadcom Ethernet module.

Due to conflicts between  (wireless module) and  (Ethernet module),  is now blacklisted as of  6.30.223.271-27See also .

This also affects  as it is built based on .

## Older Broadcom drivers not allowing connections
Broadcom chips BCM4360 or lower  do not support modern security connection methods such as WPA3. WPA2 or alternative security methods are necessary for certain network connections to handshake.

## Troubleshooting
## Setting broadcom-wl in monitor mode
Monitor mode is used to capture 802.11 frames over the air. This can be useful for diagnosing issues on a network or testing the security of your wireless network. Often, monitor mode is required to capture certain frames for wireless penetration testing, but it may be unethical or even illegal to capture frames on any network you do not own, manage or have permission to perform penetration testing against.

To set broadcom-wl in monitor mode you have to set 1 to :

 # echo 1 > /proc/brcm_monitor0

It will create a new network interface called .

To work in monitor mode, use this newly created network interface.

## Device inaccessible after kernel upgrade
Since the 3.3.1 kernel the bcma module was introduced. If using a brcm80211 driver be sure it has not been blacklisted. It should be blackisted if using a b43 driver.

If you are using , uninstall and reinstall it after upgrading your kernel or switch to  package.

## Device with broadcom-wl driver not working/showing
Be sure the correct modules are blacklisted and occasionally it may be necessary to blacklist the brcm80211 drivers if accidentally detected before the wl driver is loaded. Furthermore, update the modules dependencies , verify the wireless interface with , kernel upgrades will require an upgrade of the non-DKMS package.

## Interface is showing but not allowing connections
Append the following kernel parameter:

 b43.allhwsupport=1

## Suppressing console messages
You may continuously get some verbose and annoying messages during the boot, similar to

 phy0: brcms_ops_bss_info_changed: arp filtering: enabled true, count 0 (implement)
 phy0: brcms_ops_bss_info_changed: qos enabled: false (implement)
 phy0: brcms_ops_bss_info_changed: arp filtering: enabled true, count 1 (implement)
 enabled, active

To disable those messages, increase the loglevel of printk messages that get through to the console - see Silent boot#sysctl.

## Device BCM43241 not detected
This device will not display with either  nor ; there is no known solution yet.

## Device BCM43241 EFI Vars
As per [https://wireless.wiki.kernel.org/en/users/drivers/brcm80211 the driver page it may be necessary to copy the efi vars before the driver will operate correctly. However the expected path depends on your system.

Write the efi vars into the referenced location, e.g. on a thinkpad tablet:

 $ cat /sys/firmware/efi/efivars/nvram-74b00bd9-805a-4d61-b51f-43268123d113 > /lib/firmware/brcm/brcmfmac43241b5-sdio.LENOVO-20C1002PUK.txt

## Connection is unstable with some routers
If no other approaches help, install , or use a previous driver version.

## No 5GHz for BCM4360 (14e4:43a0) / BCM43602 (14e4:43ba)  devices
Issue appears to be linked to a channel issue. Changing the wireless channel to a lower channel number (like 40 or, if your router show MHz instead of channel numbers, like 5200 MHz or 5280 MHz) seems to allow connection to 5GHz bands.
If your router has the same SSID for the 2.4GHZ and 5GHZ, this can fix problems with your wireless connection being unstable or very slow.

## Device works intermittently
In some cases (e.g. using BCM4331 and ), Wi-Fi connection works intermittently. One way to fix this is to check if the card is hard-blocked or soft-blocked by kernel, and if it is, unblock it with rfkill.

## SSH freeze for BCM4331 with b43
The  driver has been observed hanging in ssh sessions with BCM4331. Installing  and removing b43 solves it.

## BRCM43430 not found during installation
If you have a brcm43430 connected via SDIO, you are unable to see the device after booting the installation ISO, because in the delivered image is missing a default parameter file for the device: .

To overcome the problem, you have to download brcmfmac43430-sdio.txt on another machine, and copy it on a different pendrive.

After booting the install ISO you need to copy the file to the  directory. Then follow these steps in order to activate it:

* stop
* unload the kernel module:
* load the kernel module:
* start

After that you can start iwctl that now should find your device, and proceed with the installation as usual.

After completing the installation, do not forget to copy the file to the target disk to the same location.

## Slow (1Mbps or less) internet speeds
If you are using the kernel driver along with certain Broadcom laptop Wi-Fi cards, you may experience extremely slow or even unusable internet speeds. This can be fixed by installing #broadcom-wl and rebooting

## brcmfmac suspension crash
Some users report that systems using the  driver (notably the Broadcom 4352 chipset on MacBookPro12,1 and similar hardware) experience Wi-Fi failures after suspending. Symptoms may include:

* Device failing to suspend
* No Wi-Fi networks visible after suspend attempt (or no Wi-Fi networks after resume)
* Wireless interface not functioning
* dmesg logs showing driver errors or timeouts

This appears to be a race condition during suspend, where the driver is not properly unloaded before power state changes occur.

A workaround is unloading the  module before suspend and reload it after resume by systemd service:

## Crashes on older Apple hardware
Older Apple laptops (namely MacBookAir4,1 & MacBookAir4,2) with Broadcom chipsets (notably BCM4353) can experience complete system freezes, especially when the device is under load. This appears to be an issue with PCI MSI support and can be worked around using the  kernel parameter.
