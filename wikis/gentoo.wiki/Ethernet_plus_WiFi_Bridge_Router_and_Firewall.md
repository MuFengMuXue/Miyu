Set up your Gentoo Linux box as a 802.11 (WiFi) bridge router, with firewall.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Prerequisites]](#Prerequisites)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Emerge Necessary Packages]](#Emerge_Necessary_Packages)
    -   [[3.2] [Configure Network]](#Configure_Network)
    -   [[3.3] [Configure hostapd]](#Configure_hostapd)
    -   [[3.4] [Configure dnsmasq]](#Configure_dnsmasq)
    -   [[3.5] [Configure shorewall]](#Configure_shorewall)
-   [[4] [Testing]](#Testing)
-   [[5] [Enabling]](#Enabling)

## [Introduction]

If you have a WiFi (802.11) adaptor and two Ethernet adaptors fitted to your Gentoo box, you can configure it as a bridging router and firewall.

** Note**\
You can easily modify the instructions below for various alternative configurations (e.g., no wireless card).\
Furthermore, the Gentoo box doesn\'t have to be a PC - indeed, these instructions were [originally prepared](https://github.com/sakaki-/archlinux-on-b3/wiki/Set-Up-Your-B3-as-a-WiFi-Gateway-Server) for the Excito B3, an ARM-based miniserver.

We\'re going to be aiming for the following set-up (which you can easily adapt to meet your own requirements):

[![Gentoo box used as WiFi / Ethernet Bridge Router and Firewall](/images/4/44/Gentoo_gateway_server.png)](https://wiki.gentoo.org/wiki/File:Gentoo_gateway_server.png "Gentoo box used as WiFi / Ethernet Bridge Router and Firewall")

Specifically:

-   Your Gentoo box (henceforth, **`FW`**) will be connected on a fixed address (we\'ll assume 192.168.1.129) via its wan interface (which we\'re assuming is `enp4s0` here; yours will probably differ) to your external router (ADSL, cable or whatever).
    -   Instructions for connecting via DHCP will also be given.
    -   The external router\'s gateway address will be assumed to be 192.168.1.254.
-   The `FW` will then provide a (firewall secured) internal network, via its WiFi adaptor (here, we\'ve assumed `wlp1s0`) and the lan (here, we\'ve assumed `enp4s1`) interface.
    -   We\'ll bridge these two interfaces together (and use `br0` as the bridge name).
    -   The `FW` will provide DHCP addresses to clients that connect (whether by WiFi or Ethernet) in the range 192.168.50.151-200. Connected clients will be able to browse the web etc.
    -   The `FW` will use Google\'s public DNS on 8.8.8.8, but clients will see 192.168.50.1 as the DNS address.
    -   Instructions for those with no WiFi on their `FW` will also be given.
-   You will be able to run services on your `FW` (for example, ownCloud) and make these available to clients on the lan, and (with port-forwarding in your external router) to users on the internet (wan).

You can, obviously, adapt any of the above specifics to suit your own requirements. The set-up is summarized below:

  --------------- ------------- ---------------- --------------- --------------------------------------------------------
  Firewall Zone   Bridge Name   Interface Name   IP Address      Description
  `net`           `N/A`         `enp4s0`         192.168.1.129   Connection to external internet (via ADSL etc. router)
  `loc`           `br0`         `enp4s1`         192.168.50.1    Ethernet connection for local hosts
                                `wlp1s0`                         WiFi connection for local hosts
  --------------- ------------- ---------------- --------------- --------------------------------------------------------

## [Prerequisites]

This article assumes that:

-   You are using `OpenRC`, not `systemd` (the instructions are easily adapted, however).
-   You are currently logged into your box using `ssh` via its lan Ethernet interface (`enp4s0` in our example).
-   You know the \'persistent device names\' for your Ethernet and WiFi adaptors (we\'ve assumed `enp4s0`, `enp4s1` and `wlp1s0` here; you can find the appropriate names for your system using [ifconfig -a]).
-   You have the necessary kernel settings in place to support these devices.
-   You have the necessary kernel settings in place to support a basic, `netfilter` firewall with NAT, and bridging.
-   Your primary target is IPv4. It is straightforward to extend this guide to support IPv6 also, but this is currently not covered.

## [Installation]

### [Emerge Necessary Packages]

The first step is to install the various packages that are required. We will use:

-   [[[net-firewall/shorewall]](https://packages.gentoo.org/packages/net-firewall/shorewall)[]] as the firewall (front-end),
-   [[[net-dns/dnsmasq]](https://packages.gentoo.org/packages/net-dns/dnsmasq)[]] to provide the DHCP and DNS services on the lan side,
-   [[[net-wireless/hostapd]](https://packages.gentoo.org/packages/net-wireless/hostapd)[]] to manage your WiFi adaptor as an access point,
-   [[[net-misc/bridge-utils]](https://packages.gentoo.org/packages/net-misc/bridge-utils)[]] for tools to let us bridge the ethernet and WiFi interfaces together.
-   [[[sys-apps/haveged]](https://packages.gentoo.org/packages/sys-apps/haveged)[]] to ensure we have sufficient entropy for the WiFi access point cryptography.

Note that we\'ll need the `doc` USE flag for `shorewall` (to ensure that we get the sample configurations), so create the following file first:

[FILE] **`/etc/portage/package.use/shorewall`Ensure shorewall includes sample configs**

    net-firewall/shorewall doc

** Note**\
This assumes that your [/etc/portage/package.use] is a directory; if it is a file, simply append the above line to it.

Now we can `emerge` the packages; issue:

`root `[`#`]`emerge --ask --verbose --noreplace net-firewall/shorewall net-dns/dnsmasq net-wireless/hostapd net-misc/bridge-utils sys-apps/haveged `

Wait for the process to complete before continuing.

** Note**\
If your PC has no WiFi adaptor, you can omit net-wireless/hostapd from the above.

### [Configure Network]

First, check your network adaptor names. Then edit [/etc/conf.d/net] accordingly; the below shows an example for our assumed names (enp4s0, enp4s1, wlp1s0 and br0):

[FILE] **`/etc/conf.d/net`A twin-ethernet, single WiFi adaptor network configuration**

    # setup fixed address for enp4s0 (wan Ethernet port)
    config_enp4s0="192.168.1.129 netmask 255.255.255.0 brd 192.168.1.255"
    routes_enp4s0="default via 192.168.1.254"
    # null setup for enp4s1 (lan Ethernet port)
    # (this will be owned by the bridge, br0)
    config_enp4s1="null"
    # null setup for wlp1s0 (WiFi adaptor)
    # (this will be owned by hostapd)
    config_wlp1s0="null"
    # bridge address (we ignore wifi here, it'll be added by hostapd)
    config_br0="192.168.50.1 netmask 255.255.255.0 brd 192.168.50.255"
    # no default route set for br0, leave forwarding etc. to shorewall
    # add the lan Ethernet port (enp4s1) only to br0
    # hostapd will add the WiFi adaptor (wlp1s0)
    bridge_forward_delay_br0=0
    bridge_hello_time_br0=1000
    bridge_stp_state_br0=0
    bridge_br0="enp4s1"

** Note**\
If you want to use DHCP, rather than a fixed address, on your external router connection, you\'d set config_enp4s0=\"dhcp\" in the above instead, and omit the `routes_enp4s0` specification.\
Note however, that the use of DHCP can make port forwarding less reliable (even if your external router claims to be able to support both together!) so it is recommended to use a fixed address for your wan connection if possible. Most routers will have part of their address space that is not managed by DHCP and can be used for fixed address hosts. In our example, we\'re assuming that the router leases IP addresses in the 192.168.1.151-200 range, and that (otherwise unallocated) addresses outside that range, such as 192.168.1.129, are safe to use. Obviously, you\'ll need to check your router\'s setup to find an appropriate address.

Create a network service for the new bridge interface (`br0`):

`root `[`#`]`pushd /etc/init.d; ln -s net.; popd `

and ensure that the files [/etc/init.d/net.enp4s0], [/etc/init.d/net.enp4s1] and [/etc/init.d/net.wlp1s0] already exist (link them to [/etc/init.d/net.lo], as above, if they do not).

Ensure that, for now, only the wan Ethernet interface is set to come up on boot (we\'ll add the bridge, `br0`, later, once testing is complete):

`root `[`#`]`rc-update del net.enp4s1 default `

`root `[`#`]`rc-update del net.wlp1s0 default `

`root `[`#`]`rc-update del net.br0 default `

`root `[`#`]`rc-update add net.enp4s0 default `

### [Configure `hostapd`]

Next, set up the WiFi adaptor as a [software access point](https://wiki.archlinux.org/index.php/Software_access_point), using `hostapd` (users with no WiFi adaptor should skip this step). Save off the current `hostapd` configuration:

`root `[`#`]`mv /etc/hostapd/hostapd.conf `

then put the following in its place (I\'m going to assume you want an SSID (WiFi network name) of \"gentoowifi\" and a passphrase of \"my passphrase 123\"; obviously, **please don\'t** use these verbatim!):

[FILE] **`/etc/hostapd/hostapd.conf`A basic hostapd configuration, adapt as required**

    ssid=gentoowifi
    # Use one of the following two lines; note, DO NOT quote wpa_passphrase
    wpa_passphrase=my passphrase 123
    #wpa_psk=<generated by "wpa_passphrase <SSID> ">
    interface=wlp1s0
    bridge=br0
    auth_algs=1
    country_code=GB # Unlock channels for your country, here UK
    channel=7       # Channel to use, select as appropriate
    driver=nl80211
    ieee80211d=1
    hw_mode=g
    logger_stdout=-1
    logger_stdout_level=2
    max_num_sta=5
    rsn_pairwise=CCMP
    wpa=2
    # you can set WPA-PSK-SHA256 below, but iPads won't like it if you do
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP CCMP
    rsn_pairwise=CCMP

You can find more details about what these settings mean [here](https://wireless.wiki.kernel.org/en/users/documentation/hostapd) and [here](https://w1.fi/cgit/hostap/plain/hostapd/hostapd.conf).

You\'ll also need to edit the `INTERFACES` line in [/etc/conf.d/hostapd], to specify that the bridge, `br0`, must be started prior to `hostapd`, so:

[FILE] **`/etc/conf.d/hostapd`Ensure br0 started before hostapd**

    # Space separated List of interfaces which needs to be started before
    # hostapd
    INTERFACES="br0"

Leave the rest of the file as-is.

### [Configure `dnsmasq`]

Next, we\'ll configure `dnsmasq`, to ensure that clients connecting to our firewall box on `br0` will be allocated addresses via DHCP. We\'ll also provide DNS services (ultimately, satisfied via Google\'s DNS on 8.8.8.8).

To achieve this, edit [/etc/dnsmasq.conf] so that the following lines are at the end (and make sure all other lines in the file are commented out):

[FILE] **`/etc/dnsmasq.conf`Basic dnsmasq configuration for DNS and DHCP**

    # be a good citizen
    domain-needed
    bogus-priv
    filterwin2k
    # prevent wildcard matching
    listen-address=192.168.50.1
    bind-interfaces
    # disables dnsmasq reading any other files
    # like /etc/resolv.conf for nameservers
    no-resolv
    # here is the explicit nameserver WE will use (Google)
    # (clients will get 192.168.50.1)
    server=8.8.8.8
    # Interface to bind to
    interface=br0
    # Specify starting_range,end_range,lease_time
    dhcp-range=192.168.50.151,192.168.50.200,12h

Adapt as required (see comments in the file itself for explanations of the various options available).

### [Configure `shorewall`]

Next, we will set up the `shorewall` firewall (actually, a convenient interface to `iptables` / `netfilter`). Amongst other things, this will allow hosts on the lan side of **FW** to access the external internet.

Begin by copying across the two-interface configuration files; issue:

`root `[`#`]`cp -v /usr/share/doc/shorewall-$(shorewall version)/Samples/two-interfaces/* /etc/shorewall/ `

`root `[`#`]`bunzip2 -f /etc/shorewall/*.bz2 `

** Note**\
You can look at the \'annotated\' version of these files to get information on options are available. For example, to get more details about [/etc/shorewall/interfaces], look in [/etc/shorewall/interfaces.annotated]. The [shorewall home page](https://shorewall.org/index.html) is also a useful resource.

Next, we\'ll need to edit these baseline files to match our target configuration.

Begin with [/etc/shorewall/interfaces]; ensure that the last part of this file reads as follows:

[FILE] **`/etc/shorewall/interfaces`Basic firewall network interface configuration**

    #ZONE   INTERFACE       OPTIONS
    net     enp4s0          tcpflags,nosmurfs,routefilter,logmartians,sourceroute=0
    loc     br0             dhcp,tcpflags,nosmurfs,routefilter,logmartians

** Note**\
If you are using DHCP from your *external* router to configure the wan port, you\'ll need to add the `dhcp` option to the `net` line above, too.

** Note**\
This file defines two **zones**: the first, `net`, is used to represent the \'outside\' internet, and is mapped to the interface `enp4s0` (the wan Ethernet port in our example, connected to your external router). The second, `loc`, is mapped to the (bridge) interface `br0`, and thereby to the underlying `enp4s1` (lan) and `wlp1s0` (WiFi) interfaces. It is used to represent the \'internal\' network.

** Note**\
Even if you have no WiFi adaptor on your Gentoo firewall box, it is fine to use the bridge interface.

Next, edit the [/etc/shorewall/policy] file, which specifies the default handing for each zone-to-zone traffic category, so the bottom section reads as follows:

[FILE] **`/etc/shorewall/policy`Basic firewall policy configuration**

    #SOURCE         DEST            POLICY          LOG LEVEL       LIMIT:BURST

    $FW             net             ACCEPT
    loc             net             ACCEPT
    net             all             DROP            info
    # THE FOLLOWING POLICY MUST BE LAST
    all             all             REJECT          info

This logs and drops any traffic we don\'t explicitly allow from the `net` zone; allows any oubound connection from `loc` clients and the firewall itself (represented by the variable `$FW`), and rejects all other traffic.

** Note**\
By default, this \'two-interface\' configuration will also allow:

-   Traffic on the localhost interface;
-   \'Return traffic\' for initiated outbound connections;
-   Forwarding (with NAT) of traffic from the `loc` to `net` zones (you don\'t have to enable anything else to allow this).

Next, edit [/etc/shorewall/stoppedrules], to specify what interface (NB, *not* zone) traffic should be allowed when the `shorewall` firewall is in the stopped state.

What to allow here is up to you; if you wanted to leave the firewall essentially open in such a situation (all connections in and out on any interface allowed), modify the lines at the bottom of this file so they read:

[FILE] **`/etc/shorewall/stoppedrules`Basic (permissive) rules for use when shorewall is not running**

    #ACTION         SOURCE          DEST            PROTO   DEST            SOURCE
    #                                                       PORT(S)         PORT(S)
    ACCEPT          br0             -
    ACCEPT          -               br0
    ACCEPT          enp4s0          -
    ACCEPT          -               enp4s0

Next, we need to enable any specific services we want made accessible on the firewall, via the file [/etc/firewall/rules]. This already contains a basic set (allowing `ssh` from the `loc` zone into the firewall host, for example). Add any additional services you require to the bottom of this file. You should at least allow DNS connections from the `loc` zone:

[FILE] **`/etc/shorewall/rules`Allow local zone DNS queries into the firewall host**

    #   Accept DNS connections from local network to the firewall
    #
    DNS(ACCEPT)     loc             $FW

and optionally, allow `ssh` connections from the wan (`net` zone):

[FILE] **`/etc/shorewall/rules`Allow ssh connections from the net zone (optional)**

    #   Accept SSH connections from the net for administration
    #
    SSH(ACCEPT)     net             $FW

Add stanzas for any additional services you wish to expose (such as HTTP, HTTPS etc.), and leave the rest of the file unchanged.

** Note**\
If you are running e.g. a web server, on your firewall host, remember that you need to add rules for *both* the external zone (`net`) *and* the lan zone (`loc`), as appropriate. There is no default access to all services for hosts in `loc` in the given set-up. Remember also to add port forwarding rules for these services on your external router (if they are to be visible on the external internet).

** Note**\
Also, remember that your VirtualHosts (if using the apache web server), and similar, must bind to *both* the firewall host\'s external (`enp4s0`) address (192.168.1.129, in our example) and its bridge (`br0`) address (192.168.50.1, in our example), for the service to be visible both on the external and lan side.

** Note**\
Please also remember, that you\'ll need to use the `br0` interface\'s IP address when `ssh`-ing in to **FW** from the `loc` zone (so e.g., [ssh root@192.168.50.1], for the interface parameters assumed in this tutorial).

By default, the file [/etc/shorewall/masq] refers to the external interface as `eth0`; fix that now:

`root `[`#`]`sed -i 's/eth0/enp4s0/g' /etc/shorewall/masq `

Finally, you need to make a change to [/etc/shorewall/shorewall.conf]. Modify the `STARTUP_ENABLED` line as follows:

[FILE] **`/etc/shorewall/shorewall.conf`Ensure firewall started when shorewall service runs**

    STARTUP_ENABLED=Yes

You may also wish to modify the `DISABLE_IPV6` line as follows (if not using IPv6 services externally; this will *not* block localhost IPv6 traffic however):

[FILE] **`/etc/shorewall/shorewall.conf`Disable non-local IPv6 (optional)**

    DISABLE_IPV6=Yes

Leave the rest of the file as-is.

## [Testing]

Now we can start the various services, to ensure that they work. Issue:

`root `[`#`]`/etc/init.d/haveged start `

`root `[`#`]`/etc/init.d/net.br0 start `

`root `[`#`]`/etc/init.d/hostapd start `

At this point, external clients should be able to see the \"gentoowifi\" WiFi network. However, it will have no DHCP, and nor will connections be able to access the external internet. Let\'s fix that next:

`root `[`#`]`/etc/init.d/dnsmasq start `

`root `[`#`]`/etc/init.d/shorewall start `

Now check that your connected device (e.g. an iPad, or whatever) can browse the web successfully.

** Important**\
You should also check that you can still log in, via `ssh` to **FW**: this is very important - do *not* close your original `ssh` connection until you are happy that you can connect a fresh one, so that you can [/etc/init.d/shorewall stop] if something is wrong.

## [Enabling]

When you are happy that all is working correctly, set the services up to start on boot:

`root `[`#`]`rc-update add haveged default `

`root `[`#`]`rc-update add net.br0 default `

`root `[`#`]`rc-update add hostapd default `

`root `[`#`]`rc-update add dnsmasq default `

`root `[`#`]`rc-update add shorewall default `

Reboot your firewall host, and you should be done!