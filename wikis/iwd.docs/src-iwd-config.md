# iwd.config

## Configuration file for wireless daemon

Author
Marcel Holtmann \<<marcel@holtmann.org>\>

Author
Denis Kenzior \<<denkenz@gmail.com>\>

Author
Andrew Zaborowski \<<andrew.zaborowski@intel.com>\>

Author
Tim Kourt \<<tim.a.kourt@linux.intel.com>\>

Author
James Prestwood \<<prestwoj@gmail.com>\>

Copyright
2013-2019 Intel Corporation

Version
iwd

Date
22 September 2019

Manual section
5

Manual group
Linux Connectivity

### SYNOPSIS

Configuration file **main.conf**

### DESCRIPTION

The *main.conf* configuration file configures the system-wide settings for **iwd**. This file lives in the configuration directory specified by the environment variable *\$CONFIGURATION_DIRECTORY*, which is normally provided by **systemd**. In the absence of such an environment variable it defaults to */etc/iwd*. If no *main.conf* is present, then default values are chosen. The presence of *main.conf* is not required.

### FILE FORMAT

See *iwd.network* for details on the file format.

### SETTINGS

The settings are split into several categories. Each category has a group associated with it and described in separate tables below.

#### General Settings

The group `[General]` contains general settings.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>EnableNetworkConfiguration</p></td>
<td><p>Values: true, <strong>false</strong></p>
<p>Enable network configuration.</p>
<p>Setting this option to <em>true</em> enables <strong>iwd</strong> to configure the network interfaces with the IP addresses. There are two types IP addressing supported by <strong>iwd</strong>: static and dynamic. The static IP addresses are configured through the network configuration files. If no static IP configuration has been provided for a network, <strong>iwd</strong> will attempt to obtain the dynamic addresses from the network through the built-in DHCP client.</p>
<p>This also enables network configuration and the DHCP server when in AP mode and the AP profile being activated does not override it.</p>
<p>The network configuration feature is disabled by default. See <code>[Network]</code> settings for additional settings related to network configuration.</p></td>
</tr>
<tr>
<td><p>UseDefaultInterface (<strong>deprecated</strong>)</p></td>
<td><p>Values: true, <strong>false</strong></p>
<p>Do not allow <strong>iwd</strong> to destroy / recreate wireless interfaces at startup, including default interfaces. Enable this behavior if your wireless card driver is buggy or does not allow such an operation, or if you do not want <strong>iwd</strong> to manage netdevs for another reason. For most users with an upstream driver it should be safe to omit/disable this setting.</p>
<p>This setting is deprecated, please use [DriverQuirks].DefaultInterface instead.</p></td>
</tr>
<tr>
<td><p>AddressRandomization</p></td>
<td><p>Values: <strong>disabled</strong>, once, network</p>
<p>If <code>AddressRandomization</code> is set to <code>disabled</code>, the default kernel behavior is used. This means the kernel will assign a mac address from the permanent mac address range provided by the hardware / driver. Thus it is possible for networks to track the user by the mac address which is permanent.</p>
<p>If <code>AddressRandomization</code> is set to <code>once</code>, MAC address is randomized a single time when <strong>iwd</strong> starts or when the hardware is detected for the first time (due to hotplug, etc.)</p>
<p>If <code>AddressRandomization</code> is set to <code>network</code>, the MAC address is randomized on each connection to a network. The MAC is generated based on the SSID and permanent address of the adapter. This allows the same MAC to be generated each time connecting to a given SSID while still hiding the permanent address.</p></td>
</tr>
<tr>
<td><p>AddressRandomizationRange</p></td>
<td><p>Values: <strong>full</strong>, nic</p>
<p>One can control which part of the address is randomized using this setting.</p>
<p>When using <code>AddressRandomizationRange</code> set to <code>nic</code>, only the NIC specific octets (last 3 octets) are randomized. Note that the randomization range is limited to 00:00:01 to 00:00:FE. The permanent mac address of the card is used for the initial 3 octets.</p>
<p>When using <code>AddressRandomizationRange</code> set to <code>full</code>, all 6 octets of the address are randomized. The locally-administered bit will be set.</p></td>
</tr>
<tr>
<td><p>RoamThreshold</p></td>
<td><p>Value: rssi dBm value, from -100 to 1, default: <strong>-70</strong></p>
<p>This value can be used to control how aggressively <strong>iwd</strong> roams when connected to a 2.4GHz access point.</p></td>
</tr>
<tr>
<td><p>RoamThreshold5G</p></td>
<td><p>Value: rssi dBm value, from -100 to 1, default: <strong>-76</strong></p>
<p>This value can be used to control how aggressively <strong>iwd</strong> roams when connected to a 5GHz access point.</p></td>
</tr>
<tr>
<td><p>CriticalRoamThreshold</p></td>
<td><p>Value: rssi dBm value, from -100 to -1, default: <strong>-80</strong></p>
<p>The threshold (for 2.4GHz) at which IWD will roam regardless of the affinity set to the current BSS. If the connected BSS has affinity (set in Station's Affinities list) the roam threshold will be lowed to this value and IWD will not attempt to roam (or roam scan) until either the affinity is cleared, or the signal drops below this threshold.</p></td>
</tr>
<tr>
<td><p>CriticalRoamThreshold5G</p></td>
<td><p>Value: rssi dBm value, from -100 to -1, default: <strong>-82</strong></p>
<p>This has the same effect as <code>CriticalRoamThreshold</code>, but for the 5GHz band.</p></td>
</tr>
<tr>
<td><p>RoamRetryInterval</p></td>
<td><p>Value: unsigned int value in seconds (default: <strong>60</strong>)</p>
<p>Specifies how long <strong>iwd</strong> will wait before attempting to roam again if the last roam attempt failed, or if the signal of the newly connected BSS is still considered weak.</p></td>
</tr>
<tr>
<td><p>ManagementFrameProtection</p></td>
<td><p>Values: 0, <strong>1</strong> or 2</p>
<p>When <code>ManagementFrameProtection</code> is <code>0</code>, MFP is completely turned off, even if the hardware is capable. This setting is not recommended.</p>
<p>When <code>ManagementFrameProtection</code> is <code>1</code>, MFP is enabled if the local hardware and remote AP both support it.</p>
<p>When <code>ManagementFrameProtection</code> is <code>2</code>, MFP is always required. This can prevent successful connection establishment on some hardware or to some networks.</p></td>
</tr>
<tr>
<td><p>ControlPortOverNL80211</p></td>
<td><p>Values: false, <strong>true</strong></p>
<p>Enable/Disable sending EAPoL packets over NL80211. Enabled by default if kernel support is available. Doing so sends all EAPoL traffic over directly to the supplicant process (<strong>iwd</strong>) instead of putting these on the Ethernet device. Since only the supplicant can usually make sense / decrypt these packets, enabling this option can save some CPU cycles on your system and avoids certain long-standing race conditions.</p></td>
</tr>
<tr>
<td><p>DisableANQP</p></td>
<td><p>Values: false, <strong>true</strong></p>
<p>Enable/disable ANQP queries. The way IWD does ANQP queries is dependent on a recent kernel patch (available in Kernel 5.3). If your kernel does not have this functionality this should be disabled (default). Some drivers also do a terrible job of sending public action frames (freezing or crashes) which is another reason why this has been turned off by default. If you want to easily utilize Hotspot 2.0 networks, then setting <code>DisableANQP</code> to <code>false</code> is recommended.</p></td>
</tr>
<tr>
<td><p>DisableOCV</p></td>
<td><p>Value: <strong>false</strong>, true</p>
<p>Disable Operating Channel Validation. Support for this is not advertised by the kernel so if kernels/drivers exist which don't support OCV it can be disabled here.</p></td>
</tr>
<tr>
<td><p>SystemdEncrypt</p>
<p><strong>Warning: This is a highly experimental feature</strong></p></td>
<td><p>Value: Systemd key ID</p>
<p>Enables network profile encryption using a systemd provided secret key. Once enabled all PSK/8021x network profiles will be encrypted automatically. Once the profile is encrypted there is no way of going back using IWD alone. A tool, <strong>iwd-decrypt-profile</strong>, is provided assuming the secret is known which will decrypt a profile. This decrypted profile could manually be set to /var/lib/iwd to 'undo' any profile encryption, but its going to be a manual process.</p>
<p>Setting up systemd to provide the secret is left up to the user as IWD has no way of performing this automatically. The systemd options required are LoadCredentialEncrypted or SetCredentialEncrypted, and the secret identifier should be named whatever SystemdEncrypt is set to.</p></td>
</tr>
<tr>
<td><p>Country</p></td>
<td><p>Value: Country Code (ISO Alpha-2)</p>
<p>Requests the country be set for the system. Note that setting this is simply a <strong>request</strong> to set the country, and does not guarantee the country will be set. For a self-managed wiphy it is never possible to set the country from userspace. For other devices any regulatory domain request is just a 'hint' and ultimately left up to the kernel to set the country.</p></td>
</tr>
<tr>
<td><p>DisablePMKSA</p></td>
<td><p>Value: <strong>false</strong>, true</p>
<p>Disable PMKSA support in IWD</p></td>
</tr>
</tbody>
</table>

#### Network

The group `[Network]` contains network configuration related settings.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>EnableIPv6</p></td>
<td><p>Values: <strong>true</strong>, false</p>
<p>Sets the global default that tells <strong>iwd</strong> whether it should configure IPv6 addresses and routes (either provided via static settings, Router Advertisements or DHCPv6 protocol). This setting is enabled by default. This setting can also be overridden on a per-network basis.</p></td>
</tr>
<tr>
<td><p>NameResolvingService</p></td>
<td><p>Values: resolvconf, <strong>systemd</strong>, none</p>
<p>Configures a DNS resolution method used by the system.</p>
<p>This configuration option must be used in conjunction with <code>EnableNetworkConfiguration</code> and provides the choice of system resolver integration.</p>
<p>If not specified, <code>systemd</code> is used as default.</p>
<p>If <code>none</code> is specified, then DNS and domain name information is ignored.</p></td>
</tr>
<tr>
<td><p>RoutePriorityOffset</p></td>
<td><p>Values: uint32 value (default: <strong>300</strong>)</p>
<p>Configures a route priority offset used by the system to prioritize the default routes. The route with lower priority offset is preferred.</p>
<p>If not specified, <code>300</code> is used as default.</p></td>
</tr>
</tbody>
</table>

#### Blacklist

The group `[Blacklist]` contains settings related to blacklisting of BSSes. If **iwd** determines that a connection to a BSS fails for a reason that indicates the BSS is currently misbehaving or misconfigured (e.g. timeouts, unexpected status/reason codes, etc), then **iwd** will blacklist this BSS and avoid connecting to it for a period of time. These options let the user control how long a misbehaved BSS spends on the blacklist.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>InitialTimeout</p></td>
<td><p>Values: uint64 value in seconds (default: <strong>60</strong>)</p>
<p>The initial time that a BSS spends on the blacklist. Setting this to zero will disable blacklisting functionality in IWD.</p></td>
</tr>
<tr>
<td><p>InitialRoamRequestedTimeout (<strong>deprecated</strong>)</p></td>
<td><p>Values: uint64 value in seconds (default: <strong>30</strong>)</p>
<p>This setting is deprecated, please use [Blacklist].InitialAccessPointBusyTimeout instead.</p></td>
</tr>
<tr>
<td><p>InitialAccessPointBusyTimeout</p></td>
<td><p>Values: uint64 value in seconds (default: <strong>30</strong>)</p>
<p>The initial time that a BSS will be blacklisted after indicating it cannot handle more connections. This is triggered by either a BSS transition management request (telling IWD to roam elsewhere) or by a denied authentication or association with the NOMORE_STAS status code.</p>
<p>Once a BSS is blacklisted in this manor IWD will attempt to avoid it for the configured amount of time.</p></td>
</tr>
<tr>
<td><p>Multiplier</p></td>
<td><p>Values: unsigned int value greater than zero, in seconds (default: <strong>30</strong>)</p>
<p>If the BSS was blacklisted previously and another connection attempt has failed after the initial timeout has expired, then the BSS blacklist time will be extended by a multiple of <em>Multiplier</em> for each unsuccessful attempt up to <em>MaxiumTimeout</em> time in seconds.</p></td>
</tr>
<tr>
<td><p>MaximumTimeout</p></td>
<td><p>Values: uint64 value in seconds (default: <strong>86400</strong>)</p>
<p>Maximum time that a BSS is blacklisted.</p></td>
</tr>
</tbody>
</table>

#### Rank

The group `[Rank]` contains settings related to ranking of networks for autoconnect purposes.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>BandModifier24GHz</p></td>
<td><p>Values: floating point value (default: <strong>1.0</strong>)</p>
<p>Increase or decrease the preference for 2.4GHz access points by increasing or decreasing the value of this modifier.</p>
<p>A value of 0.0 will disable the 2.4GHz band and prevent scanning or connecting on those frequencies.</p></td>
</tr>
<tr>
<td><p>BandModifier5GHz</p></td>
<td><p>Values: floating point value (default: <strong>1.0</strong>)</p>
<p>Increase or decrease the preference for 5GHz access points by increasing or decreasing the value of this modifier. 5GHz networks are already preferred due to their increase throughput / data rate. However, 5GHz networks are highly RSSI sensitive, so it is still possible for IWD to prefer 2.4GHz APs in certain circumstances.</p>
<p>A value of 0.0 will disable the 5GHz band and prevent scanning or connecting on those frequencies.</p></td>
</tr>
<tr>
<td><p>BandModifier6GHz</p></td>
<td><p>Values: floating point value (default: <strong>1.0</strong>)</p>
<p>Increase or decrease the preference for 6GHz access points by increasing or decreasing the value of this modifier. Since 6GHz networks are highly RSSI sensitive, this gives an option to prefer 6GHz APs over 5GHz APs.</p>
<p>A value of 0.0 will disable the 6GHz band and prevent scanning or connecting on those frequencies.</p></td>
</tr>
<tr>
<td><p>HighUtilizationThreshold</p></td>
<td><p>Values: unsigned integer value 0 - 255 (default: <strong>0</strong>, disabled)</p>
<p><strong>Warning: This is an experimental feature</strong></p>
<p>The BSS utilization threshold at which a negative rank factor begins to be applied to the BSS. As the load increases for a BSS the ranking factor decays exponentially, meaning the ranking factor will decrease exponentially. Setting this can have very drastic effects on the BSS rank if its utilization is high, use with care.</p></td>
</tr>
<tr>
<td><p>HighStationCountThreshold</p></td>
<td><p>Values: unsigned integer value 0 - 255 (default: <strong>0</strong>, disabled)</p>
<p><strong>Warning: This is an experimental feature</strong></p>
<p>The BSS station count threshold at which a negative rank factor begins to be applied to the BSS. As the station count increases for a BSS the ranking factor decays exponentially, meaning the ranking factor will decrease exponentially. Setting this can have very drastic effects on the BSS rank if its station count is high, use with care.</p></td>
</tr>
</tbody>
</table>

#### Scan

The group `[Scan]` contains settings related to scanning functionality. No modification from defaults is normally required.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>DisablePeriodicScan</p></td>
<td><p>Values: true, <strong>false</strong></p>
<p>Disable periodic scan. Setting this option to 'true' will prevent <strong>iwd</strong> from issuing the periodic scans for the available networks while disconnected. The behavior of the user-initiated scans isn't affected. The periodic scan is enabled by default.</p></td>
</tr>
<tr>
<td><p>InitialPeriodicScanInterval</p></td>
<td><p>Values: unsigned int value in seconds (default: <strong>10</strong>)</p>
<p>The initial periodic scan interval upon disconnect.</p></td>
</tr>
<tr>
<td><p>MaximumPeriodicScanInterval</p></td>
<td><p>Values: unsigned int value in seconds (default: <strong>300</strong>)</p>
<p>The maximum periodic scan interval.</p></td>
</tr>
<tr>
<td><p>DisableRoamingScan</p></td>
<td><p>Values: true, <strong>false</strong></p>
<p>Disable roaming scan. Setting this option to 'true' will prevent <strong>iwd</strong> from trying to scan when roaming decisions are activated. This can prevent <strong>iwd</strong> from roaming properly, but can be useful for networks operating under extremely low rssi levels where roaming isn't possible.</p></td>
</tr>
</tbody>
</table>

#### IPv4

The group `[IPv4]` contains settings related to IPv4 network configuration.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>APAddressPool</p></td>
<td><p>Values: comma-separated list of prefix-notation IP strings</p>
<p>Defines the space of IPs used for the Access Point-mode subnet addresses and the DHCP server. Defaults to 192.168.0.0/16. The prefix length decides the size of the pool from which an address is selected but the actual subnet size (netmask) is based on the AP profile being activated and defaults to 28 bits. The AP profile's <code>[IPv4].Address</code> setting overrides the global value set here. Setting a too small address space will limit the number of access points that can be running simultaneously on different interfaces.</p></td>
</tr>
</tbody>
</table>

#### DriverQuirks

The group `[DriverQuirks]` contains special flags associated with drivers that are buggy or just don't behave similar enough to the majority of other drivers.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>DefaultInterface</p></td>
<td><p>Values: comma-separated list of drivers or glob matches</p>
<p>If a driver in use matches one in this list IWD will not attempt to remove and re-create the default interface.</p></td>
</tr>
<tr>
<td><p>ForcePae</p></td>
<td><p>Values: comma-separated list of drivers or glob matches</p>
<p>If a driver in use matches one in this list ControlPortOverNL80211 will not be used, and PAE will be used instead. Some drivers do not properly support ControlPortOverNL80211 even though they advertise support for it.</p></td>
</tr>
<tr>
<td><p>PowerSaveDisable</p></td>
<td><p>Values: comma-separated list of drivers or glob matches</p>
<p>If a driver in user matches one in this list power save will be disabled.</p></td>
</tr>
<tr>
<td><p>MulticastRxDisable</p></td>
<td><p>Values: comma-separated list of drivers or glob matches</p>
<p>If a driver in use matches one in this list, multicast RX will be disabled.</p></td>
</tr>
<tr>
<td><p>SaeDisable</p></td>
<td><p>Values: comma-separated list of drivers or glob matches</p>
<p>If a driver in use matches one in this list, SAE/WPA3 will be disabled for connections. This will prevent connections to WPA3-only networks, but will allow for connections to WPA3/WPA2 hybrid networks by utilizing WPA2.</p></td>
</tr>
</tbody>
</table>

### SEE ALSO

iwd(8), iwd.network(5)
