# Network configuration/Wireless

The main article on network configuration is Network configuration.

Configuring wireless is a two-part process; the first part is to identify and ensure the correct driver for your wireless device is installed (they are available on the installation media, but often have to be installed explicitly), and to configure the interface. The second is choosing a method of managing wireless connections. This article covers both parts, and provides additional links to wireless management tools.

The #iw section describes how to manually manage your wireless network interface / your wireless LANs using . The Network configuration#Network managers section describes several programs that can be used to automatically manage your wireless interface, some of which include a GUI and all of which include support for network profiles (useful when frequently switching wireless networks, like with laptops).

## Device driver
The default Arch Linux kernel is modular, meaning many of the drivers for machine hardware reside on the hard drive and are available as modules. At boot, udev takes an inventory of your hardware and loads appropriate modules (drivers) for your corresponding hardware, which will in turn allow creation of a network interface.

Some wireless chipsets also require firmware, in addition to a corresponding driver. Many firmware images are provided by the  package; however, proprietary firmware images are not included and have to be installed separately. This is described in #Installing driver/firmware.

## Check the driver status
To check if the driver for your card has been loaded, check the output of the  or  command, depending on if the card is connected by PCIe or USB. You should see that some kernel driver is in use, for example:

Also check the output of the  command to see if a wireless interface was created; usually the naming of the wireless network interfaces starts with the letters "wl", e.g.  or . Then bring the interface up with:

 # ip link set interface up

For example, assuming the interface is , this is .

Check kernel messages for firmware being loaded:

If there is no relevant output, check the messages for the full output for the module you identified earlier ( in this example) to identify the relevant message or further issues:

If the kernel module is successfully loaded and the interface is up, you can skip the next section.

## Installing driver/firmware
Check the following lists to discover if your card is supported:

* See the table of existing Linux wireless drivers and follow to the specific driver's page, which contains a list of supported devices. There is also a List of Wi-Fi Device IDs in Linux.
* The Ubuntu Wiki has a good list of wireless cards and whether or not they are supported either in the Linux kernel or by a user-space driver (includes driver name).
* Linux Wireless Support and The Linux Questions' Hardware Compatibility List (HCL) also have a good database of kernel-friendly hardware.

Note that some vendors ship products that may contain different chip sets, even if the product identifier is the same. Only the USB ID (for USB devices) or PCI ID (for PCIe devices) is authoritative.

If your wireless card is listed above, follow the #Troubleshooting drivers and firmware subsection of this page, which contains information about installing drivers and firmware of some specific wireless cards. Then check the driver status again.

If your wireless card is not listed above, it is likely supported only under Windows (some Broadcom, 3com, etc). For these, you can try to use ndiswrapper.

## Utilities
Just like other network interfaces, the wireless ones are controlled with ip from the  package.

Managing a wireless connection can be accomplished using network manager which will use wpa_supplicant or iwd for wireless authentication, or using wpa_supplicant or iwd directly. For lower level configuring, or if you are using a legacy driver or a legacy authentication method, there are  and the deprecated .

## iw and wireless_tools comparison
{| class="wikitable"
! Software !! Package !! WEXT2 !! nl80211 !! WEP !! WPA/WPA2/WPA3 !! Archiso
|-
| iw ||  ||  ||  ||  ||  ||
|-
| wireless_tools1 ||  ||  ||  ||  ||  ||
|}

# Deprecated.
# Note that some ancient drivers only support WEXT.

The table below gives an overview of comparable commands for iw and wireless_tools. See Replacing iwconfig with iw for more examples.

{| class="wikitable"
! iw command
! wireless_tools command
! Description
|-
| iw dev wlan0 link
| iwconfig wlan0
| Getting link status.
|-
| iw dev wlan0 scan
| iwlist wlan0 scan
| Scanning for available access points.
|-
| iw dev wlan0 set type ibss
| iwconfig wlan0 mode ad-hoc
| Setting the operation mode to ad-hoc.
|-
| iw dev wlan0 connect your_essid
| iwconfig wlan0 essid your_essid
| Connecting to open network.
|-
| iw dev wlan0 connect your_essid 2432
| iwconfig wlan0 essid your_essid freq 2432M
| Connecting to open network specifying channel.
|-
| rowspan="2" | iw dev wlan0 connect your_essid key 0:your_key
| iwconfig wlan0 essid your_essid key your_key
| Connecting to WEP encrypted network using hexadecimal key.
|-
| iwconfig wlan0 essid your_essid key s:your_key
| Connecting to WEP encrypted network using ASCII key.
|-
| iw dev wlan0 set power_save on
| iwconfig wlan0 power on
| Enabling power save.
|}

## iw
Examples in this section assume that your wireless device interface is  and that you are connecting to  Wi-Fi access point. Replace both accordingly.

## Get the name of the interface
To get the name of your wireless interface, do:

 $ iw dev

The name of the interface will be output after the word "Interface". For example, it is commonly .

## Get the status of the interface
To check link status, use the following command.

 $ iw dev interface link

You can get statistic information, such as the amount of tx/rx bytes, signal strength etc., with the following command:

 $ iw dev interface station dump

## Activate the interface
Some cards require that the kernel interface be activated before you can use iw or wireless_tools:

 # ip link set interface up

To verify that the interface is up, inspect the output of the following command:

The  in  is what indicates the interface is up, not the later .

## Discover access points
To see what access points are available:

 # iw dev interface scan | less

The important points to check:
* SSID: the name of the network.
* Signal: is reported in a wireless power ratio in dBm (e.g. from -100 to 0). The closer the negative value gets to zero, the better the signal. Observing the reported power on a good quality link and a bad one should give an idea about the individual range.
* Security: it is not reported directly, check the line starting with . If there is , for example , then the network is protected somehow.
** If you see an  information block, then the network is protected by Robust Security Network protocol, also known as WPA2.
** If you see an  information block, then the network is protected by Wi-Fi Protected Access protocol.
** In the  and  blocks, you may find the following information:
*** Group cipher: value in TKIP, CCMP, both, others.
*** Pairwise ciphers: value in TKIP, CCMP, both, others. Not necessarily the same value than Group cipher.
*** Authentication suites: value in PSK, 802.1x, others. For home router, you will usually find PSK (i.e. passphrase). In universities, you are more likely to find 802.1x suite which requires login and password. Then you will need to know which key management is in use (e.g. EAP), and what encapsulation it uses (e.g. PEAP). See #WPA2 Enterprise and Wikipedia:Authentication protocol for details.
** If you see neither  nor  blocks but there is , then WEP is used.

## Set operating mode
You might need to set the proper operating mode of the wireless card. More specifically, if you are going to connect an ad-hoc network, you need to set the operating mode to :

 # iw dev interface set type ibss

## Connect to an access point
Depending on the encryption, you need to associate your wireless device with the access point to use and pass the encryption key:

* No encryption
* WEP
** using a hexadecimal or ASCII key (the format is distinguished automatically, because a WEP key has a fixed length):
** using a hexadecimal or ASCII key, specifying the third set up key as default (keys are counted from zero, four are possible):
* Other
** iw can only handle WEP. To connect using other encryption schemes, see the section on #Authentication below.

Regardless of the method used, you can check if you have associated successfully:

 # iw dev interface link

## Authentication
There are mainly two options for Wi-Fi authentication on Linux: wpa_supplicant and iwd.

## WPA2 Personal
WPA2 Personal, a.k.a. WPA2-PSK, is a mode of Wi-Fi Protected Access.

You can authenticate to WPA2 Personal networks using wpa_supplicant or iwd, or connect using a network manager. If you only authenticated to the network, then to have a fully functional connection, you will still need to assign the IP address(es) and routes either manually or using a DHCP client.

## WPA2 Enterprise
WPA2 Enterprise is a mode of Wi-Fi Protected Access. It provides better security and key management than WPA2 Personal, and supports other enterprise-type functionality, such as VLANs and NAP. However, it requires an authentication server, called RADIUS server, to handle the authentication of users. This is in contrast to Personal mode which does not require anything beyond the wireless router or access points (APs), and uses a single passphrase or password for all users.

The Enterprise mode enables users to log onto the Wi-Fi network with a username and password and/or a digital certificate. Since each user has a dynamic and unique encryption key, it also helps to prevent user-to-user snooping on the wireless network, and improves encryption strength.

This section describes the configuration of network clients to connect to a wireless access point with WPA2 Enterprise mode. See Software access point#RADIUS for information on setting up an access point itself.

For a comparison of protocols, see the following table.

## MS-CHAPv2
WPA2-Enterprise wireless networks demanding MSCHAPv2 type-2 authentication with PEAP sometimes require  in addition to the stock  package. netctl seems to work out of the box without ppp-mppe, however. In either case, usage of MSCHAPv2 is discouraged as it is highly vulnerable, although using another method is usually not an option.

## eduroam
eduroam is an international roaming service for users in research, higher education and further education, based on WPA2 Enterprise.

## Manual/automatic setup
* wpa_supplicant can be configured directly by its configuration file or using its CLI/GUI front ends and used in combination with a DHCP client. See the examples in  for configuring the connection details.
* iwd#WPA Enterprise
* NetworkManager can create WPA2 Enterprise profiles with nmcli, nmtui or the graphical front ends.
* ConnMan needs a separate configuration file before connecting to the network. See  and ConnMan#Connecting to eduroam (802.1X) for details.
* netctl supports wpa_supplicant configuration through blocks included with . See  for details.
:
:

## WPA3 Personal
WPA3 Personal, a.k.a. WPA3-SAE, is a mode of Wi-Fi Protected Access.

Both wpa_supplicant and iwd support WPA3 Personal.

## WPA3 Enterprise
WPA3 Enterprise is a mode of Wi-Fi Protected Access.

wpa_supplicant (since version 2:2.10-8) supports WPA3 Enterprise. See .

## Tips and tricks
## Respecting the regulatory domain
The regulatory domain, or "regdomain", is used to reconfigure wireless drivers to make sure that wireless hardware usage complies with local laws set by the FCC, ETSI and other organizations. Regdomains use ISO 3166-1 alpha-2 country codes. For example, the regdomain of the United States would be "US", China would be "CN", etc.

Regdomains affect the availability of wireless channels. In the 2.4GHz band, the allowed channels are 1-11 for the US, 1-14 for Japan, and 1-13 for most of the rest of the world. In the 5GHz band, the rules for allowed channels are much more complex. In either case, consult this list of WLAN channels for more detailed information.

Regdomains also affect the limit on the effective isotropic radiated power (EIRP) from wireless devices. This is derived from transmit power/"tx power", and is measured in dBm/mBm (1dBm=100mBm) or mW (log scale). In the 2.4GHz band, the maximum is 30dBm in the US and Canada, 20dBm in most of Europe, and 20dBm-30dBm for the rest of the world. In the 5GHz band, maximums are usually lower. Consult the wireless-regdb for more detailed information (EIRP dBm values are in the second set of brackets for each line).

Misconfiguring the regdomain can be useful - for example, by allowing use of an unused channel when other channels are crowded, or by allowing an increase in tx power to widen transmitter range. However, this is not recommended as it could break local laws and cause interference with other radio devices.

The kernel loads the database directly when  is installed. (If it is not installed, the kernel should log something like  into the journal during boot.) For direct loading, the kernel should, for security's sake, be configured with  set to yes to allow for cryptographic verification of the database. This is true of the stock Arch kernel, but if you are using an alternate kernel, or compiling your own, you should verify this. More information is available at this guide.

To configure the regdomain, install  and reboot, then edit  and uncomment the appropriate domain.

The current regdomain can be temporarily set to the United States with:

 # iw reg set US

And queried with:

 $ iw reg get

However, setting the regdomain may not alter your settings. Some devices have a regdomain set in firmware/EEPROM, which dictates the limits of the device, meaning that setting regdomain in software can only increase restrictions, not decrease them. For example, a CN device could be set in software to the US regdomain, but because CN has an EIRP maximum of 20dBm, the device will not be able to transmit at the US maximum of 30dBm.

For example, to see if the regdomain is being set in firmware for an Atheros device:

 # journalctl -kg ath:

For other chipsets, it may help to search for "EEPROM", "regdomain", or simply the name of the device driver.

To see if your regdomain change has been successful, and to query the number of available channels and their allowed transmit power:

 $ iw list | grep -A 15 Frequencies:

wpa_supplicant can also use a regdomain in the  line of .

It is also possible to configure the cfg80211 kernel module to use a specific regdomain by adding, for example,  as module options. The module option is inherited from the old regulatory implementation and in modern kernels act as a userspace regulatory hint as if it came through  through utilities like  and .

## Rfkill caveat
Many laptops have a hardware button (or switch) to turn off the wireless card; however, the card can also be blocked by the kernel. This can be handled by . To show the current status:

If the card is hard-blocked, use the hardware button (switch) to unblock it. If the card is not hard-blocked but soft-blocked, use the following command:

 # rfkill unblock wlan

Hardware buttons to toggle wireless cards are handled by a vendor specific kernel module. Frequently, these are WMI modules. Particularly for very new hardware models, it happens that the model is not fully supported in the latest stable kernel yet. In this case, it often helps to search the kernel bug tracker for information and report the model to the maintainer of the respective vendor kernel module, if it has not happened already.

See also === Power saving ===

See Power saving#Network interfaces.

## Troubleshooting
This section contains general troubleshooting tips, not strictly related to problems with drivers or firmware. For such topics, see next section #Troubleshooting drivers and firmware.

## Temporary internet access
If you have problematic hardware and need internet access to, for example, download some software or get help in forums, you can make use of Android's built-in feature for internet sharing via USB cable. See Android tethering#USB tethering for more information.

## Observing logs
A good first measure to troubleshoot is to analyze the system's logfiles first. In order not to manually parse through them all, it can help to open a second terminal/console window and watch the kernels messages with

 # dmesg -w

while performing the action, e.g. the wireless association attempt.

When using a tool for network management, the same can be done for systemd with

 # journalctl -f

Frequently, a wireless error is accompanied by a deauthentication with a particular reason code, for example:

 wlan0: deauthenticating from XX:XX:XX:XX:XX:XX by local choice (reason=3)

Looking up [http://www.aboutcher.co.uk/2012/07/linux-wifi-deauthenticated-reason-codes/ the reason code might give a first hint. Maybe it also helps you to look at the control message flowchart, the journal messages will follow it.

The individual tools used in this article further provide options for more detailed debugging output, which can be used in a second step of the analysis, if required.

## Failed to get IP address
* If you can get an IP address for a wired interface and not for a wireless interface, try disabling the wireless card's power saving features (specify  instead of ).

* If you get a timeout error due to a waiting for carrier problem, then you might have to set the channel mode to  for the specific device:

 # iwconfig wlan0 channel auto

Before changing the channel to auto, make sure your wireless interface is down. After it has successfully changed it, you can bring the interface up again and continue from there.

## Valid IP address but cannot resolve host
If you are on a public wireless network that may have a captive portal, make sure to query an HTTP page (not an HTTPS page) from your web browser, as some captive portals only redirect HTTP.
If this is not the issue, check if you can resolve domain names, it may be necessary to use the DNS server advertised via DHCP.

## Setting RTS and fragmentation thresholds
Wireless hardware disables RTS and fragmentation by default. These are two different methods of increasing throughput at the expense of bandwidth (i.e. reliability at the expense of speed). These are useful in environments with wireless noise or many adjacent access points, which may create interference leading to timeouts or failing connections.

Packet fragmentation improves throughput by splitting up packets with size exceeding the fragmentation threshold. The maximum value (2346) effectively disables fragmentation since no packet can exceed it. The minimum value (256) maximizes throughput, but may carry a significant bandwidth cost.

 # iw phy0 set frag 512

RTS improves throughput by performing a handshake with the access point before transmitting packets with size exceeding the RTS threshold. The maximum threshold (2347) effectively disables RTS since no packet can exceed it. The minimum threshold (0) enables RTS for all packets, which is probably excessive for most situations.

 # iw phy0 set rts 500

## Random disconnections
## Cause #1
If your journal says  and you lose your Wi-Fi connection, it is likely that you have a bit too aggressive power-saving on your Wi-Fi card. Try disabling the wireless card's power saving features (specify  instead of ).

If your card does not support enabling/disabling power save mode, check the BIOS for power management options. Disabling PCI-Express power management in the BIOS of a Lenovo W520 resolved this issue.

## Cause #2
If you are experiencing frequent disconnections and your journal shows messages such as

try changing the channel bandwidth to  through your router's settings page.

## Cause #3
On some laptop models with hardware rfkill switches (e.g., Thinkpad X200 series), due to wear or bad design, the switch (or its connection to the mainboard) might become loose over time resulting in seemingly random hardblocks/disconnects when you accidentally touch the switch or move the laptop.
There is no software solution to this, unless your switch is electrical and the BIOS offers the option to disable the switch.
If your switch is mechanical (and most are), there are lots of possible solutions, most of which aim to disable the switch: Soldering the contact point on the mainboard or Wi-Fi card, gluing or blocking the switch, using a screw nut to tighten the switch or removing it altogether.

## Cause #4
Another cause for frequent disconnects or a complete failure to connect may also be a sub-standard router, incomplete settings of the router, interference by other wireless devices or low quality signal.

To troubleshoot, first try to connect to the router with no authentication and by getting closer to it. If it does not work, reboot the router and try with another device first.

If that works, enable WPA/WPA2 again but choose fixed and/or limited router settings. For example:
* If the router is considerably older than the wireless device you use for the client, test if it works with setting the router to one wireless mode.
* Disable mixed-mode authentication (e.g. only WPA2 with AES, or TKIP if the router is old).
* Try a fixed/free channel rather than "auto" channel (maybe the router next door is old and interfering).
* Disable WPS.
* Change the router's 5 GHz channel(s) to a non-DFS (Dynamic Frequency Selection) channel. Connections on such channels may be dropped or suddenly switched due to interference from nearby weather radar.
* Try setting your client to 2.4 GHz only instead of letting it choose what it thinks is best between 5 GHz and 2.4 GHz (the later has a lower throughput but will provide a more stable connection over longer distances).
* Disable  channel bandwidth (lower throughput but less likely collisions) with .
* If the router has quality of service settings, check completeness of settings (e.g. Wi-Fi Multimedia (WMM) is part of optional QoS flow control. An erroneous router firmware may advertise its existence although the setting is not enabled).

## Cause #5
On some wireless network adapters (e.g. Qualcomm Atheros AR9485), random disconnects can happen with a DMA error:

A possible workaround is to disable the Intel IOMMU driver (DMA), adding  to the kernel parameters ==== Cause #6 ====

If you are using a device with  and  for wireless connectivity, and your Wi-Fi card appears to disappear when on battery power (perhaps after a reboot or resuming from suspend), this can be fixed by configuring power saving settings in iwlmvm.

Create the file  if it does not exist already, then add the following line to it:

A  of 1 sets iwlmvm to "Always Active." Available options are:

{| class="wikitable"
! Value !! Description
|-
| 1 || Always Active
|-
| 2 || Balanced
|-
| 3 || Low-power
|}

This fix was discovered at [https://forums.debian.net/viewtopic.php?t=121696#p576208.

## Cause #7
If your device undergoes long periods of inactivity (e.g. a file server), the disconnection may be due to power saving, which will block incoming traffic and prevent connections. Try disabling power saving for the interface:

 # iw dev interface set power_save off

You can create a udev rule to do this on boot, see Power management#Network interfaces.

## Cause #8
If you notice occasional interruptions when connected to a mesh network (e.g., Wi-Fi 6) and notice a message such as:

You are experiencing roaming issues. Depending on your mean of connection and the issue at hand, one could:

* Lock the BSSID (the  show above) in NetworkManager if roaming is not desired (see NetworkManager#Regular network disconnects, latency and lost packets (Wi-Fi)).
* Adjust the  setting in Wpa_supplicant#Roaming

## Wi-Fi networks invisible because of incorrect regulatory domain
If the computer's Wi-Fi channels do not match those of the user's country, some in-range Wi-Fi networks might be invisible because they use wireless channels that are not allowed by default. The solution is to configure the regulatory domain correctly; see #Respecting the regulatory domain.

## Troubleshooting drivers and firmware
This section covers methods and procedures for installing kernel modules and firmware for specific chipsets, that differ from generic method.

See Kernel modules for general information on operations with modules.

## Ralink/MediaTek
Some chipsets require additional firmware:

## rt2x00
Unified driver for Ralink chipsets (it replaces , , , etc). This driver has been in the Linux kernel since 2.6.24, you only need to load the right module for the chip: , , ,  or  which will autoload the respective  modules too.

A list of devices supported by the modules is available at the project's homepage.

; Additional notes
* Since kernel 3.0, rt2x00 includes also these drivers: , .
* Since kernel 3.0, the staging drivers  and  are replaced by the mainline drivers  and  * Some devices have a wide range of options that can be configured with . These are documented in the [https://web.archive.org/web/20111105120212/http://web.ralinktech.com:80/ralink/Home/Support/Linux.html source tarballs available from Ralink.

## rt3090
For devices which use the rt3090 chipset, it should be possible to use the  driver; however, it does not work with this chipset very well (e.g. sometimes it is not possible to use higher rate than 2Mb/s).

## rt3290
The rt3290 chipset is recognised by the kernel  module. However, some users experience problems and reverting to a patched Ralink driver seems to be beneficial in these cases.

## rt3573
New chipset as of 2012. It may require proprietary drivers from Ralink. Different manufacturers use it; see the Belkin N750 DB wireless usb adapter forums thread.

## mt7612u
New chipset as of 2014, released under their new commercial name MediaTek. It is an AC1200 or AC1300 chipset. Manufacturer provides drivers for Linux on their support page. As of kernel 5.5 it should be supported by the included  driver.

DFS channels are currently not supported in 5 GHz AP mode.

## mt7921 / mt7922
There are some high latency problems with these MediaTek chipsets. To fix this, the only solution is to disable ASPM:

This configuration file will take effect on next reboot or after reloading the module with modprobe:

 # modprobe -r mt7921e && modprobe mt7921e

These are also sometimes branded as AMD RZ608 (mt7921) and RZ616 (mt7922).

## Realtek
See for a list of Realtek chipsets and specifications.

## rtl8192cu
The driver is now in the kernel, but many users have reported being unable to make a connection although scanning for networks does work.

 includes many patches; try this if it does not work fine with the driver in kernel.

## rtl8723ae/rtl8723be
The  and  modules are included in the mainline Linux kernel.

Some users may encounter errors with powersave on this card. This is shown with occasional disconnects that are not recognized by high level network managers (netctl, NetworkManager). This error can be confirmed by running  as root or  as root and looking for output related to powersave and the / module. If you have this issue, use the  kernel module parameter which should prevent the Wi-Fi card from automatically sleeping and halting connection.

If you have poor signal, perhaps your device has only one physical antenna connected, and antenna autoselection is broken. You can force the choice of antenna with  or  kernel option. [https://bbs.archlinux.org/viewtopic.php?id=208472

## rtl88xxau
Realtek chipsets rtl8811au, rtl8812au, rtl8814au and rtl8821au designed for various USB adapters ranging from AC600 to AC1900. Several packages provide various kernel drivers, these require DKMS (the  package and the kernel headers installed):

{| class="wikitable"
! Chipset || Package || Notes
|-
| rtl88xxyy ||  || A backport of the Realtek Wifi 5 drivers from the wireless-next repo. Supports:
*PCIe: RTL8723DE, RTL8814AE, RTL8821CE, RTL8822BE, RTL8822CE
*SDIO: RTL8723CS, RTL8723DS, RTL8821CS, RTL8822BS, RTL8822CS
*USB : RTL8723DU, RTL8811AU, RTL8811CU, RTL8812AU, RTL8812BU, RTL8812CU, RTL8814AU, RTL8821AU, RTL8821CU, RTL8822BU, RTL8822CU
|-
| rtl8812au ||  || (probably deprecated) Alternative official Realtek driver version for rtl8812au only.
|-
| rtl8811au, rtl8821au ||  || (probably deprecated) Alternative driver version for rtl8821au.
|-
| rtl8814au ||  || (probably deprecated) Possibly works for rtl8813au too.
|}

## rtl8811cu/rtl8821cu
 provides a kernel module for the Realtek 8811cu and 8821cu chipset.

This requires DKMS, so make sure you have your proper kernel headers installed.

If no wireless interface shows up even though the  module is loaded, you may need to manually specify the  kernel module parameter Try e.g. , other values might also work.

## rtl8821ce
 provides a kernel module for the Realtek 8821ce chipset found in the Asus X543UA.

This requires DKMS, so make sure you have your proper kernel headers installed.

## rtl8822bu
 provides a kernel module for the Realtek 8822bu chipset found in the Edimax EW7822ULC USB3, Asus AC53 Nano USB 802.11ac and TP-Link Archer T3U adapter.

This requires DKMS, so make sure you have your proper kernel headers installed.

## rtl8xxxu
Issues with the  mainline kernel module may be solved by compiling a third-party module for the specific chipset. The source code can be found in [https://github.com/lwfinger?tab=repositories GitHub repositories.

Some drivers may be already prepared in the AUR, e.g. , , ,  .

## RTW88
RWT88 kernel module is included in all officially supported Arch Linux kernels. The number of supported devices grew over time, currently it supports most RTW88 chip devices if configured and compiled to do so.

As of Linux 6.10.3, the driver supports: 882BE (possibly), 8703B, 8723CS, 8723D, 8723DE, 8723DS, 8723DU, 8723X, 8821C, 8821CE, 8821CS, 8821CU, 8822B, 8822BE, 8822BS, 8822BU, 8822C, 8822CE, 8822CS, 8822CU.

To get more up-to-date list, Ctrl+F  's config or check out wireless-next upstream.

Make sure that wireless-regdom is configured. Otherwise, you will be able to see all Wi-Fi networks, but will not be able to connect. Out-of-tree driver  can connect without such configuration, so it's important to set regulatory domain when switching from it.

Here is how those symptoms look in dmesg:

And in iwd log:

## RTW89
The RTW89 kernel module has been merged into the upstream kernel and provides support for newer Realtek wireless chipsets.

This driver supports: 8852AE, 8851BE, 8852BE, and 8852CE.

On some computers, you may experience unstable connections. It seems like a common issue on late models from HP and Lenovo.
Try disabling ASPM-related features using the config below.

See also:
* https://github.com/lwfinger/rtw89#option-configuration
* https://github.com/lwfinger/rtw89/issues/275#issuecomment-1784155449

## Atheros
There are different drivers for devices with Atheros chipset:

*  is a driver which replaces the obsolete  driver. Currently a better choice for some chipsets, but not all chipsets are supported (see below).
*  is intended for newer Atheros chipsets. All of the chips with 802.11n capabilities are supported.
*  is a Linux driver for Qualcomm Wi-Fi 7 (IEEE 802.11be) devices. ath12k uses mac80211.

There are some other drivers for some Atheros devices. See Linux Wireless documentation for details.

## ath5k
External resources:

* https://wireless.docs.kernel.org/en/latest/en/users/drivers/ath5k.html
* Debian:ath5k

If you find web pages randomly loading very slow, or if the device is unable to lease an IP address, try to switch from hardware to software encryption by loading the  module with  option. See Kernel modules#Setting module options for details.

Some laptops may have problems with their wireless LED indicator flickering red and blue. To solve this problem, do:

 # echo none > /sys/class/leds/ath5k-phy0::tx/trigger
 # echo none > /sys/class/leds/ath5k-phy0::rx/trigger

For alternatives, see this bug report.

## ath9k
External resources:
* https://wireless.wiki.kernel.org/en/users/drivers/ath9k
* Debian:ath9k

As of Linux 3.15.1, some users have been experiencing a decrease in bandwidth. In some cases, this can fixed by setting the  kernel module parameter for the  module.

## Power saving
Although Linux Wireless says that dynamic power saving is enabled for Atheros ath9k single-chips newer than AR9280, for some devices (e.g. AR9285),  might still report that power saving is disabled. In this case, enable it manually.

On some devices (e.g. AR9285), enabling the power saving might result in the following error:

The solution is to set the  kernel module parameter for the  module.

## Intel
## iwlegacy
iwlegacy is the wireless driver for Intel's 3945 and 4965 wireless chips. The firmware is included in the  package.

udev should load the driver automatically, otherwise load  or  manually. See Kernel modules for details.

If you have problems connecting to networks in general (e.g. random failures with your card on bootup or your link quality is very poor), try to disable 802.11n:

## iwlwifi
iwlwifi is the wireless driver for Intel's current wireless chips, such as 5100AGN, 5300AGN, and 5350AGN. See the full list of supported devices.

If you have problems connecting to networks in general or your link quality is very poor, try to disable 802.11n, and perhaps also enable software encryption:

If you have a problem with slow uplink speed you may try disabling power saving for your wireless adapter.

If you have an 802.11ax (Wi-Fi 6) access point and have problems detecting the beacons or an unreliable connection, review Intel Article 54799.

## Bluetooth coexistence
If you have difficulty connecting a bluetooth headset and maintaining good downlink speed, try disabling Bluetooth coexistence:

## Firmware issues
Make sure your firmware is fully updated before trying anything else.

You may have some issue where the driver outputs stack traces & errors, which can cause some stuttering.

Alternatively, you may simply experience miscellaneous issues (e.g. connection issues on 5GHz, random disconnections, no connection on resume).

To confirm it is the cause of the issues, downgrade the package .

If confirmed, move the buggy firmware files so that an older version is loaded (to be able to have an up to date  since it is not only providing firmware updates for your Intel Wi-Fi card):

 # for i in {64..73} ; do mv /usr/lib/firmware/iwlwifi-ty-a0-gf-a0-$i.ucode.xz /usr/lib/firmware/iwlwifi-ty-a0-gf-a0-$i.ucode.xz.bak ; done

To avoid having to repeat these steps manually after each update, use the NoExtract and NoUpgrade arrays in  with a wildcard to block their installation.

## Adapter not detected after booting from Windows
If the Wi-Fi adapter is not getting detected after finishing a session in Windows, this might be due to Windows' Fast Startup feature which is enabled by default. Try disabling Fast Startup. The iwlwifi kernel driver wiki has an entry for this.

## Disabling LED blink
The default settings on the module are to have the LED blink on activity. Some people find this extremely annoying. To have the LED on solid when Wi-Fi is active, you can use the systemd-tmpfiles:

Run  for the change to take effect, or reboot.

To see all the possible trigger values for this LED:

 # cat /sys/class/leds/phy0-led/trigger

## Aicsemi
## AIC8800/8801/8800DC/8800DW/8800FC
The  package should be used with these devices. These drivers are out of the mainline Linux kernel and require DKMS.

## AIC8800D80
For this chip variant,  package should be used instead of the one mentioned above.

## Broadcom
See Broadcom wireless.

## Other drivers/devices
## Tenda w322u
Treat this Tenda card as an  device. See #rt2x00.

## orinoco
This should be a part of the kernel package and be installed already.

Some Orinoco chipsets are Hermes II. You can use the  driver instead of  and gain WPA support. To use the driver, blacklist  first.

## prism54
The driver  is included in kernel, but you have to download the appropriate firmware for your card from this site and install it into the  directory.

## zd1211rw
zd1211rw is a driver for the ZyDAS ZD1211 802.11b/g USB WLAN chipset, and it is included in recent versions of the Linux kernel. See for a list of supported devices. You only need to install the firmware for the device, provided by the  package.

## hostap_cs
[https://hostap.epitest.fi/ Host AP is a Linux driver for wireless LAN cards based on Intersil's Prism2/2.5/3 chipset. The driver is included in Linux kernel.

## ndiswrapper
Ndiswrapper is a wrapper script that allows you to use some Windows drivers in Linux. You will need the .inf and .sys files from your Windows driver.

Follow these steps to configure ndiswrapper.

# Install .
# Install the driver to :
# List all installed drivers for ndiswrapper:
# Let ndiswrapper write its configuration in :

The ndiswrapper install is almost finished; you can load the module at boot.

Test that ndiswrapper will load now:

 # modprobe ndiswrapper

See Network configuration#Listing network interfaces for more assurance the wireless interface now exists.

If you have problems, some help is available at:
ndiswrapper howto and ndiswrapper FAQ.
