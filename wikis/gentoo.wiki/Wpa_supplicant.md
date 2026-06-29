This page contains [[changes](https://wiki.gentoo.org/index.php?title=Wpa_supplicant&oldid=1428395&diff=1430162)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Wpa_supplicant/hu "wpa_supplicant (91% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Wpa_supplicant/ru "wpa_supplicant (76% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Wpa_supplicant/zh-cn "Wpa supplicant (53% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Wpa_supplicant/ja "wpa_supplicant (97% translated)")

**Resources**

[[]][Home](https://w1.fi/wpa_supplicant/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Wpa_supplicant "wikipedia:Wpa supplicant")

[[]][Package information](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)

[[]][GitWeb](https://w1.fi/cgit/hostap/)

[[]][Bugs (upstream)](http://lists.infradead.org/mailman/listinfo/hostap)

[[]][wpa_supplicant(8)](https://linux.die.net/man/8/wpa_supplicant)

[[]][wpa_supplicant.conf(5)](https://linux.die.net/man/5/wpa_supplicant.conf)

**wpa_supplicant** is an app for [Wi-Fi](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi") authentication (a [\"supplicant\"](https://en.wikipedia.org/wiki/Supplicant_(computer) "wikipedia:Supplicant (computer)") in the technical jargon).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Direct connect]](#Direct_connect)
    -   [[2.1] [Quick Connect]](#Quick_Connect)
    -   [[2.2] [Connection for two interfaces]](#Connection_for_two_interfaces)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
        -   [[3.1.1] [Minimal configuration]](#Minimal_configuration)
        -   [[3.1.2] [Setup for wireless interface]](#Setup_for_wireless_interface)
        -   [[3.1.3] [WPA2 with wpa_supplicant]](#WPA2_with_wpa_supplicant)
        -   [[3.1.4] [Configuration file with dynamic WEP keys]](#Configuration_file_with_dynamic_WEP_keys)
        -   [[3.1.5] [Allows more or less all configuration modes]](#Allows_more_or_less_all_configuration_modes)
        -   [[3.1.6] [Setup wired 802.1X]](#Setup_wired_802.1X)
-   [[4] [Setup the network manager]](#Setup_the_network_manager)
    -   [[4.1] [Setup for dhcpcd as network manager]](#Setup_for_dhcpcd_as_network_manager)
        -   [[4.1.1] [Using OpenRC]](#Using_OpenRC)
        -   [[4.1.2] [Using Systemd]](#Using_Systemd)
    -   [[4.2] [Setup for Netifrc]](#Setup_for_Netifrc)
    -   [[4.3] [Setup for NetworkManager]](#Setup_for_NetworkManager)
-   [[5] [Usage]](#Usage)
    -   [[5.1] [Using wpa_gui]](#Using_wpa_gui)
    -   [[5.2] [Using wpa_cli]](#Using_wpa_cli)
    -   [[5.3] [Editing manually]](#Editing_manually)
        -   [[5.3.1] [Auto-connect to any unsecured network]](#Auto-connect_to_any_unsecured_network)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Name can have spaces postfix]](#Name_can_have_spaces_postfix)
    -   [[6.2] [Check for known bugs]](#Check_for_known_bugs)
    -   [[6.3] [Can\'t see all SSIDs]](#Can.27t_see_all_SSIDs)
    -   [[6.4] [rfkill: WLAN soft blocked]](#rfkill:_WLAN_soft_blocked)
    -   [[6.5] [Configuration for a captive portal]](#Configuration_for_a_captive_portal)
    -   [[6.6] [Run wpa_supplicant in debug mode]](#Run_wpa_supplicant_in_debug_mode)
    -   [[6.7] [Enable logging]](#Enable_logging)
        -   [[6.7.1] [Enable logging for Gentoo net.\* scripts]](#Enable_logging_for_Gentoo_net..2A_scripts)
-   [[7] [References]](#References)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)

## [Installation]

As a precondition, wireless support might need to be activated in the kernel as described in [IEEE 802.11 section](https://wiki.gentoo.org/wiki/Wi-Fi#IEEE_802.11 "Wi-Fi") as well as necessary [wireless device drivers](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi").^[\[1\]](#cite_note-1)^

### [USE flags]

### [USE flags for] [net-wireless/wpa_supplicant](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant) [[]] [IEEE 802.1X/WPA supplicant for secure wireless transfers]

  --------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+ap`](https://packages.gentoo.org/useflags/+ap)                                 Add support for access point mode
  [`+fils`](https://packages.gentoo.org/useflags/+fils)                             Add support for Fast Initial Link Setup (802.11ai)
  [`+mbo`](https://packages.gentoo.org/useflags/+mbo)                               Add support Multiband Operation
  [`+mesh`](https://packages.gentoo.org/useflags/+mesh)                             Add support for mesh mode
  [`broadcom-sta`](https://packages.gentoo.org/useflags/broadcom-sta)               Flag to help users disable features not supported by broadcom-sta driver
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                               Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`eap-sim`](https://packages.gentoo.org/useflags/eap-sim)                         Add support for EAP-SIM authentication algorithm
  [`eapol-test`](https://packages.gentoo.org/useflags/eapol-test)                   Build and install eapol_test binary
  [`gui`](https://packages.gentoo.org/useflags/gui)                                 Enable support for a graphical user interface
  [`macsec`](https://packages.gentoo.org/useflags/macsec)                           Add support for wired macsec
  [`p2p`](https://packages.gentoo.org/useflags/p2p)                                 Add support for Wi-Fi Direct mode
  [`privsep`](https://packages.gentoo.org/useflags/privsep)                         Enable wpa_priv privledge separation binary
  [`readline`](https://packages.gentoo.org/useflags/readline)                       Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`smartcard`](https://packages.gentoo.org/useflags/smartcard)                     Add support for smartcards
  [`tkip`](https://packages.gentoo.org/useflags/tkip)                               Add support for WPA TKIP (deprecated due to security flaws in 2009)
  [`uncommon-eap-types`](https://packages.gentoo.org/useflags/uncommon-eap-types)   Add support for GPSK, SAKE, GPSK_SHA256, IKEV2 and EKE
  [`wep`](https://packages.gentoo.org/useflags/wep)                                 Add support for Wired Equivalent Privacy (deprecated due to security flaws in 2004)
  [`wps`](https://packages.gentoo.org/useflags/wps)                                 Add support for Wi-Fi Protected Setup
  --------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 19:18] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After USE flags have been reviewed, install [[[net-wireless/wpa_supplicant]](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)[]] using Portage\'s [emerge] command:

`root `[`#`]`emerge --ask net-wireless/wpa_supplicant`

## [Direct connect]

### [Quick Connect]

** Warning**\
To not store any clear text password in history, history is disabled. This should be used temporarily to test that it is possible to connect to the access point.

`root `[`#`]`set +o history`

`root `[`#`]`wpa_supplicant -i wlp0s20f3 -c <(wpa_passphrase ssid password) &`

`root `[`#`]`set -o history`

** Note**\
In case the SSID contains whitespace or special characters it needs to be enclosed in double quotes, e.g. \"FRITZ!Box 7530 LA\"

### [Connection for two interfaces]

[wpa_supplicant] can control multiple interfaces (or *radios*) either by running a separate process for each interface, or one process for all interfaces with a list of options on the command line. Each interface is separated with a `-N` argument. The following command would start [wpa_supplicant] for two interfaces:

`user `[`$`]`wpa_supplicant -c wpa1.conf -i wlan0 -D nl80211 -N -c wpa2.conf -i ath0 -D wext`

## [Configuration]

### [Files]

#### [Minimal configuration]

wpa_supplicant includes a tool to quickly write a network block from the command line for pre-shared key (WPA-PSK aka password) networks, [wpa_passphrase].

`root `[`#`]`wpa_passphrase ssid password >> /etc/wpa_supplicant/wpa_supplicant.conf`

** Note**\
When password is stored as hash instead of clear text it is required to add *key_MGMT=WPA-EAP* and *eap=PEAP* to the configuration file that is not generated by default

#### [Setup for wireless interface]

For usage with a single wireless interface only one configuration file will be needed.

[FILE] **`/etc/wpa_supplicant/wpa_supplicant.conf`**

    # Allow users in the 'wheel' group to control wpa_supplicant
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel

    # Make this file writable for wpa_gui / wpa_cli
    update_config=1

To allow unprivileged users to control the connection using [wpa_gui] / [wpa_cli], make sure the users are in the [wheel] [group](https://wiki.gentoo.org/wiki/Knowledge_Base:Adding_a_user_to_a_group "Knowledge Base:Adding a user to a group").

This file does not exist by default; a well documented template configuration file can be copied from [/usr/share/doc/\$/wpa_supplicant.conf.bz2] where the value of the `P` variable is the name and version of the currently emerged wpa_supplicant:

`root `[`#`]`bzcat /usr/share/doc/$/wpa_supplicant.conf.bz2 > /etc/wpa_supplicant/wpa_supplicant.conf`

#### [WPA2 with wpa_supplicant]

Connecting to any wireless access point serving *YourSSID*

[FILE] **`/etc/wpa_supplicant/wpa_supplicant.conf`**

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel
    #ap_scan=0
    #update_config=1

    network=

#### [Configuration file with dynamic WEP keys]

[FILE] **`/etc/wpa_supplicant/wpa_supplicant_wired.conf`**

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel
    network=

#### [Allows more or less all configuration modes]

** Warning**\
The configuration options are used based on what security policy is used in the selected SSID. This is mostly for testing and is not recommended for normal use

[FILE] **`/etc/wpa_supplicant/wpa_supplicant_wired.conf`**

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel
    network=

\

#### [Setup wired 802.1X]

It\'s possible to have wired connections handled via wpa_supplicant, which is useful for networks using 802.1X. Create a separate configuration file containing the wired configuration. Below example use certificates for authentication, check the wpa_supplicant.conf man page for examples of other methods.

** Note**\
This can be used with wired or roboswitch interface (-Dwired or -Droboswitch on command line)

[FILE] **`/etc/wpa_supplicant/wpa_supplicant_wired.conf`**

    ctrl_interface=/var/run/wpa_supplicant
    eapol_version=1
    ap_scan=0
    fast_reauth=1

    network=

Since the configuration file contains sensitive information, [chmod] accordingly.

`root `[`#`]`chmod 600 /etc/wpa_supplicant/wpa_supplicant_wired.conf`

wpa_supplicant needs some extra parameters to apply above configuration to the wired interface (eth0) Note that below wpa_supplicant arguments assumes wpa_supplicant is version \>=2.6-r2 (-M, CONFIG_MATCH_IFACE=y)

[FILE] **`/etc/conf.d/wpa_supplicant`**

    wpa_supplicant_args="-ieth0 -Dwired -c/etc/wpa_supplicant/wpa_supplicant_wired.conf -M -c/etc/wpa_supplicant/wpa_supplicant.conf"

Let wpa_supplicant handle start/stop of the interfaces by removing them from /etc/init.d and enabling the wpa_supplicant daemon

`root `[`#`]`/etc/init.d/net.eth0 stop `

`root `[`#`]`/etc/init.d/net.wlan0 stop `

`root `[`#`]`rm /etc/init.d/net.wlan0 /etc/init.d/net.eth0 `

`root `[`#`]`rc-update add wpa_supplicant `

`root `[`#`]`/etc/init.d/wpa_supplicant start `

Check the status of the wired interface via wpa_cli

Connect directly to the wireless access point from the command line

\

`root `[`#`]`wpa_cli `

    wpa_cli v2.8
    Copyright (c) 2004-2019, Jouni Malinen <j@w1.fi> and contributors

    This software may be distributed under the terms of the BSD license.
    See README for more details.

    Selected interface 'p2p-dev-wlan0'

    Interactive mode

    > interface eth0
    Connected to interface 'eth0.
    > status
    bssid=00:00:00:00:00:00
    freq=0
    ssid=
    id=0
    mode=station
    pairwise_cipher=NONE
    group_cipher=NONE
    key_mgmt=IEEE 802.1X (no WPA)
    wpa_state=COMPLETED
    ip_address=10.10.10.100
    p2p_device_address=bb:bb:bb:bb:bb:bb
    address=aa:aa:aa:aa:aa:aa
    Supplicant PAE state=AUTHENTICATED
    suppPortStatus=Authorized
    EAP state=SUCCESS
    selectedMethod=13 (EAP-TLS)
    eap_tls_version=TLSv1
    EAP TLS cipher=ECDHE-RSA-AES256-SHA
    ...

## [Setup the network manager]

** Important**\
The solutions listed in [Network management](https://wiki.gentoo.org/wiki/Network_management#Comparison_of_network_managers "Network management") typically do not work together. Be sure only one of those services is running at a time. Starting more than one network management service **will lead to unpredictable results**!

Be sure to choose the corresponding setup.

### [Setup for dhcpcd as network manager]

First follow the setup guide for [dhcpcd](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD#Setup "Network management using DHCPCD").

Emerge [wpa_supplicant] (Version \>=2.6-r2 is needed in order to get the [CONFIG_MATCH_IFACE](https://forums.gentoo.org/viewtopic-t-1036958-start-4.html) option [added in April 2017](https://gitweb.gentoo.org/repo/gentoo.git/commit/net-wireless/wpa_supplicant?id=423af2686b225f76bb8ae52221690581a56a9625)):

`root `[`#`]`emerge --ask net-wireless/wpa_supplicant`

#### [Using [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")]

Complete its [conf.d] file with the `-M` option for the wireless network interface:

[FILE] **`/etc/conf.d/wpa_supplicant`**

    wpa_supplicant_args="-B -M -c /etc/wpa_supplicant/wpa_supplicant.conf"

In case authentication for the [wired interface](https://wiki.gentoo.org/wiki/Wpa_supplicant#Setup_wired_802.1X "Wpa supplicant") is needed, this configuration file should look like:

[FILE] **`/etc/conf.d/wpa_supplicant`**

    wpa_supplicant_args="-ieth0 -Dwired -c/etc/wpa_supplicant/wpa_supplicant_wired.conf -B -M -c/etc/wpa_supplicant/wpa_supplicant.conf"

With the configuration done, run it as a service:

`root `[`#`]`rc-update add wpa_supplicant default`

`root `[`#`]`rc-service wpa_supplicant start`

#### [Using [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")]

[Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") allows a simpler per-device setup without needing to create the above [conf.d] files. As explained under *wpa_supplicant* item in the [Native services](https://wiki.gentoo.org/wiki/Systemd#Native_services "Systemd") section, a service symlink such as `wpa_supplicant@wlan0.service` looks for a separate configuration file to manage the device `wlan0` in this case.

To configure a specific device this way, first copy or rename the [/etc/wpa_supplicant/wpa_supplicant.conf] file as [/etc/wpa_supplicant/wpa_supplicant-DEVNAME.conf] where `DEVNAME` should be the name of the device, such as `wlan0`.

Then, navigate to [/etc/systemd/system/multi-user.target.wants] and create the symlink:

`root `[`#`]`ln -s /lib/systemd/system/wpa_supplicant@.service wpa_supplicant@DEVNAME.service`

where `DEVNAME` is *same* device name as in the conf file above.

** Important**\
Note the **@** signs on both arguments in the symlink step.

Test the system:

`root `[`#`]`systemctl daemon-reload `

`root `[`#`]`systemctl start wpa_supplicant@DEVNAME `

`root `[`#`]`systemctl status wpa_supplicant@DEVNAME `

In case the deprecated [WEXT](https://wiki.gentoo.org/wiki/Wifi#WEXT "Wifi") driver is needed, changing the wireless driver can help resolve cases where it associates then immediately disconnects with **reason 3**. Run [wpa_supplicant -h] to see a list of the available drivers that were built at compile-time.

[FILE] **`/etc/conf.d/wpa_supplicant`set the driver to wext**

    wpa_supplicant_args="-D wext"

### [Setup for Netifrc]

To configure [Netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") to use wpa_supplicant:

[FILE] **`/etc/conf.d/net`**

    modules_wlan0="wpa_supplicant"
    config_wlan0="dhcp"

After configuration above it is a good idea to change the permissions to ensure that WiFi passwords can not be viewed in plaintext by anyone using the computer:^[\[2\]](#cite_note-2)^

`root `[`#`]`chmod 600 /etc/wpa_supplicant/wpa_supplicant.conf`

### [Setup for NetworkManager]

[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") configured with wpa_supplicant as WiFi backend is able to use [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") to start wpa_supplicant when needed. Therefore it is recommended to keep the wpa_supplicant service itself stopped at boot time.

## [Usage]

### [Using wpa_gui]

The simplest way to use wpa_supplicant is by using its interface called [wpa_gui]. To enable it, build wpa_supplicant with the `qt5` USE flag enabled.

### [Using wpa_cli]

Wpa_supplicant also has a command-line user interface. Typing [wpa_cli] starts its interactive mode with tab-completion. Typing `help` at this prompt will list the commands available (click \"Expand\" to view the output for the [wpa_cli] command below):

`user `[`$`]`wpa_cli `

    wpa_cli v2.5
     Copyright (c) 2004-2015, Jouni Malinen <j@w1.fi> and contributors

     This software may be distributed under the terms of the BSD license.
     See README for more details.

     Selected interface 'wlan0'

     Interactive mode

     > scan
     OK
     > scan_results
     bssid / frequency / signal level / flags / ssid
     01:23:45:67:89:ab       2437    0       [WPA-PSK-CCMP+TKIP][WPA2-PSK-CCMP+TKIP][ESS]    hotel-free-wifi
     > add_network
     0
     > set_network 0 ssid "hotel-free-wifi"
     OK
     > set_network 0 psk "password"
     OK
     > enable_network 0
     OK
     <3>CTRL-EVENT-SCAN-RESULTS
     <3>WPS-AP-AVAILABLE
     <3>Trying to associate with 01:23:45:67:89:ab (SSID='hotel-free-wifi' freq=2437 MHz)
     <3>Associated with 01:23:45:67:89:ab
     <3>WPA: Key negotiation completed with 01:23:45:67:89:ab [PTK=CCMP GTK=TKIP]
     <3>CTRL-EVENT-CONNECTED - Connection to 01:23:45:67:89:ab completed [id=0 id_str=]
     > save_config
     OK
     > quit

For switching to another Wi-Fi:

`user `[`$`]`wpa_cli `

    wpa_cli v2.5
     Copyright (c) 2004-2015, Jouni Malinen <j@w1.fi> and contributors

     This software may be distributed under the terms of the BSD license.
     See README for more details.
    > list_networks
    network id / ssid / bssid / flags
    0   TAMO    any
    1   ORBI705 any
    2   ORBI    any
    3   Tangerine   any
    4   271 any
    5   POCO X3 Pro any
    6   Orbi Guest  any
    7   hackerspace any
    8   HUAWEI-25 a-2   any
    9   A1-13   any

    > select_network 1

More details on how to connect can be found in the Arch Linux wiki.^[\[3\]](#cite_note-3)^

### [Editing manually]

Of course, the configuration file [/etc/wpa_supplicant/wpa_supplicant.conf] could also be edited manually. However this can be very laborious if the computer needs to connect to many different access points.

Examples can be found in [[[wpa_supplicant.conf(5)]](https://man.archlinux.org/man/wpa_supplicant.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page and [/usr/share/doc/wpa_supplicant-2.4-r3/wpa_supplicant.conf.bz2].

[FILE] **`/etc/wpa_supplicant/wpa_supplicant.conf`**

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel
    ap_scan=1

    network=

#### [Auto-connect to any unsecured network]

[FILE] **`/etc/wpa_supplicant/wpa_supplicant.conf`**

    network=

## [Troubleshooting]

### [Name can have spaces postfix]

See point in the scan but not connecting? Check SSID for spaces: in wpa_cli scan_results select that point - so you will \"see\" the space at the end.

In case it does not work as expected try some of the following and analyze the output.

### [Check for known bugs]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=wpa_supplicant&order=bug_id%20DESC)[]]
-   [Upstream\'s mailing list archive](http://lists.infradead.org/pipermail/hostap/)

### [][Can\'t see all SSIDs]

SSIDs that use deprecated insecure protocols will be unavailable by default, this can sometimes explain why some SSIDs may seem to be \"missing\".

** Warning**\
Enabling insecure options should only be attempted if fully cognizant of the risks.

There is an [insecure workaround](https://wiki.gentoo.org/wiki/Warning_about_insecure_obsolete_network_hardware#Insecure_workaround "Warning about insecure obsolete network hardware") to enable connecting to these insecure networks, though users should be aware of the security implications.

### [rfkill: WLAN soft blocked]

If [rfkill](https://wiki.gentoo.org/wiki/Util-linux#rfkill "Util-linux") is blocking the interface, first find the interface number with:

`user `[`$`]`rfkill list`

    0: ideapad_wlan: Wireless LAN
        Soft blocked: yes
        Hard blocked: no
    1: ideapad_bluetooth: Bluetooth
        Soft blocked: yes
        Hard blocked: no
    2: hci0: Bluetooth
        Soft blocked: yes
        Hard blocked: no
    3: phy0: Wireless LAN
        Soft blocked: yes
        Hard blocked: no

Then the interface can be unblocked with:

`root `[`#`]`rfkill unblock 3`

### [Configuration for a captive portal]

Using a captive portal involves setting the `key_mgmt` parameter for the relevant network to `NONE`:

[FILE] **`/etc/wpa_supplicant/wpa_supplicant.conf`**

    network=

### [Run wpa_supplicant in debug mode]

Be sure to stop any running instance of the supplicant:

`root `[`#`]`killall wpa_supplicant`

Something like the following options can be used for debugging (click \"Expand\" to view the output below):

`root `[`#`]`wpa_supplicant -Dnl80211 -iwlan0 -C/var/run/wpa_supplicant/ -c/etc/wpa_supplicant/wpa_supplicant.conf -dd `

    wpa_supplicant v2.2
    random: Trying to read entropy from /dev/random
    Successfully initialized wpa_supplicant
    Initializing interface 'wlp8s0' conf '/etc/wpa_supplicant/wpa_supplicant.conf' driver 'nl80211' ctrl_interface '/var/run/wpa_supplicant' bridge 'N/A'
    Configuration file '/etc/wpa_supplicant/wpa_supplicant.conf' -> '/etc/wpa_supplicant/wpa_supplicant.conf'
    Reading configuration file '/etc/wpa_supplicant/wpa_supplicant.conf'
    ctrl_interface='DIR=/var/run/wpa_supplicant GROUP=wheel'
    update_config=1
    Line: 6 - start of a new network block

### [Enable logging]

#### [][Enable logging for Gentoo net.\* scripts]

[FILE] **`/etc/conf.d/net`for usage with the setup for Gentoo net.\* scripts**

    modules_wlan0="wpa_supplicant"
    wpa_supplicant_wlan0="-Dnl80211 -d -f /var/log/wpa_supplicant.log"
    config_wlan0="dhcp"

Now, within one terminal issue a [tail] command to monitor output and restart the [net.wlan0] device in another:

`root `[`#`]`tail -f /var/log/wpa_supplicant.log `

`root `[`#`]`/etc/init.d/net.wlan0 restart `

## [References]

1.  [[[↑](#cite_ref-1)] [[[[bug #623014]](https://bugs.gentoo.org/show_bug.cgi?id=623014)[]]]]
2.  [[[↑](#cite_ref-2)] [[[[bug #264000]](https://bugs.gentoo.org/show_bug.cgi?id=264000)[]]]]
3.  [[[↑](#cite_ref-3)] [[https://wiki.archlinux.org/index.php/WPA_supplicant#Connecting_with_wpa_cli](https://wiki.archlinux.org/index.php/WPA_supplicant#Connecting_with_wpa_cli)]]

## [See also]

-   [iwd](https://wiki.gentoo.org/wiki/Iwd "Iwd") --- a wireless daemon intended to replace wpa_supplicant

## [External resources]

-   [wpa_supplicant / hostapd Developers\' documentation for wpa_supplicant and hostapd](https://w1.fi/wpa_supplicant/devel/)
-   [sample config for wpa_supplicant](https://w1.fi/cgit/hostap/plain/wpa_supplicant/wpa_supplicant.conf)
-   [HOWTO: Remote access point with wpa_supplicant](https://forums.gentoo.org/viewtopic-t-1007254.html) (Gentoo Forums)
-   [Extensible Authentication Protocol](https://en.wikipedia.org/wiki/Extensible_Authentication_Protocol "wikipedia:Extensible Authentication Protocol") (Wikipedia)
-   [Extensible Authentication Protocol](https://wiki.freeradius.org/protocol/EAP) (wiki.freeradius.org)
-   [wpa_supplicant upstream just accepted patch to allow interface matching](https://forums.gentoo.org/viewtopic-t-1036958-start-4.html)
-   [https://www.kb.cert.org/vuls/id/CHEU-AQNN3Z](https://www.kb.cert.org/vuls/id/CHEU-AQNN3Z)