Network admins may require static, simple and stable IP addresses for both IPv4 and IPv6. The goal of this article is to assign a static custom IPv6 suffix to an interface without additional software while keeping full RA functionality from the router.

When combined with a fix ULA Prefix advertised from the router, IPv6 Addresses can then be simple, organized, static and easily be handled in DNS.

## Contents

-   [[1] [Default kernel IPv6 address creation mechanism]](#Default_kernel_IPv6_address_creation_mechanism)
    -   [[1.1] [Example: default MAC construction]](#Example:_default_MAC_construction)
    -   [[1.2] [Drawbacks on MAC-constructed addresses]](#Drawbacks_on_MAC-constructed_addresses)
-   [[2] [IPv6 tokenized interface identifiers]](#IPv6_tokenized_interface_identifiers)
    -   [[2.1] [Static IPv6 address problems]](#Static_IPv6_address_problems)
    -   [[2.2] [Solution: Tokens]](#Solution:_Tokens)
-   [[3] [Putting it together: On boot]](#Putting_it_together:_On_boot)

## [Default kernel IPv6 address creation mechanism]

In a IPv6 network, addresses are often self-assigned (constructed) by the kernel using both **PREFIX:** information provided by a router (DHCPv6 server) and **:SUFFIX** information extracted from hardware (MAC address). The router mechanism for this functionality is called \"Router Advertisement\" (RA). A machine usually has multiple IPv6 addresses for global, link or network scope. If the IPv6 Prefix can change (for example on a dialup connection), static addresses can not be assigned as easily as on IPv4.

### [Example: default MAC construction]

Take a look at a simple example configuration with IPv6 addresses completely self-constructed with prefix information received by a router. Note that the IPv4 configuration is already static:

[FILE] **`~/etc/conf.d/net`**

    rc_keyword="-stop"
    config_eth0="192.168.0.35/24"
    routes_eth0="default via 192.168.0.2"

when the interface is started, the address configuration could like this:

`root `[`#`]`ip addr show eth0`

    1: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
            link/ether 9a:02:79:45:ce:d2 brd ff:ff:ff:ff:ff:ff
            inet 192.168.0.35/24 brd 192.168.0.255 scope global eth0
               valid_lft forever preferred_lft forever
            inet6 2a02:810a:8240:a2c:9802:79ff:fe45:ced2/64 scope global
            inet6 fd00::9802:79ff:fe45:ced2/64 scope global
            inet6 fe80::9802:79ff:fe45:ced2/64 scope link
               valid_lft forever preferred_lft forever

Note that the Suffix part **9802:79ff:fe45:ced2** is constructed out of the MAC address.

### [Drawbacks on MAC-constructed addresses]

There a couple drawbacks of MAC-constructed addresses, for example

-   complicated to read
-   change when the MAC address changes (hardware, VM setup etc)
-   not associated with their IPv4 counterpart

## [IPv6 tokenized interface identifiers]

### [Static IPv6 address problems]

The word \"static IPv6 addresses\" is a bit misleading. When on dialup, the Prefix may change and so does the global IPv6 address of the interface. If the machine needs access to the internet without an additional router or NAT, it needs a public IPv6 address with the same prefix as the IPv6 gateway.

Within a closed network, for example a LAN, that\'s not important. For DNS and connectivity within a closed network, the Unique Local Address (or ULA) is important. This address can be fully fixed.

Since the Prefix can change, static addresses cannot be assigned for all scopes. When using RA to get IPv6 configured, an additional IPv6 address could be entered in /etc/conf.d/net. Drawback: The kernel still constructs and adds another address using it\'s constructions defaults. And this kernel-auto-created address becomes route default.

### [Solution: Tokens]

An easy solution is called **[IPv6 Tokenized Interface Identifiers](https://tools.ietf.org/id/draft-chown-6man-tokenised-ipv6-identifiers-02.txt)**: tell the kernel which SUFFIX to use for a particular interface.

When combined with a **fixed ULA Prefix (Unique Local Address Prefix) announced from the router**, the Local Address (for example `fd00:`) will stay the same while the Global Address gets updated by the kernel as soon as the router announces a prefix change. And thanks to the token, the Global Address also **keeps it\'s suffix!**

*Unfortunately, IPV6 tokens are not supported by netifrc yet*, which is Gentoo\'s default framework for configuring network when using OpenRC. Further more, tokens can not be configured using sysctl. Tokens can only be set using the ip (or ifconfig) command.

Example: Assign the simple suffix `::35` to interface `eth0`, in order to match the IPv4 counterpart `192.168.0.35`:

`root `[`#`]`ip token set ::35 dev eth0`

Restart the interface, the changes apply:

`root `[`#`]`rc-service net.eth0 restart`

`root `[`#`]`ip addr show eth0`

    1: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
            link/ether 9a:02:79:45:ce:d2 brd ff:ff:ff:ff:ff:ff
            inet 192.168.0.35/24 brd 192.168.0.255 scope global eth0
               valid_lft forever preferred_lft forever
            inet6 2a02:810a:8240:a2c::35/64 scope global
            inet6 fd00::35/64 scope global
            inet6 fe80::9802:79ff:fe45:ced2/64 scope link
               valid_lft forever preferred_lft forever

Notice the new `::35` suffix on all IPV6 addresses, except for the Link Local address `fe80:`. That\'s by design, but can be changed too if desired by changing the address after its creation:

`root `[`#`]`ip addr flush scope link dev eth0 `

`root `[`#`]`ip addr add fe80::35/64 dev eth0`

`root `[`#`]`rc-service net.eth0 restart`

`root `[`#`]`ip addr show eth0`

    1: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
            link/ether 9a:02:79:45:ce:d2 brd ff:ff:ff:ff:ff:ff
            inet 192.168.0.35/24 brd 192.168.0.255 scope global eth0
               valid_lft forever preferred_lft forever
            inet6 2a02:810a:8240:a2c::35/64 scope global
            inet6 fd00::35/64 scope global
            inet6 fe80::35/64 scope link
               valid_lft forever preferred_lft forever

Now all IPv6 addresses on eth0 have the simple suffix of `::35`.

In this example, the Router additionally announces a fixed ULA Prefix (Unique Local Address Prefix) of `fd00:`. The full Unique Local Address (ULA) is now simply `fd00::35` - this address is used for all traffic within the local network (LAN). The global (Public, WAN side) address of this interface is now `2a02:810a:8240:a2c::35`.

`fd00::35` can now be registered in local DNS - it will never change (unless the ULA Prefix would change).

The interface now has fully functional, easy to read and manage IPv6 addresses while **keeping full RA functionality from the router**. This means that the kernel will instantly re-configure the global IPV6 address when for example the Prefix changes.

## [Putting it together: On boot]

Since [netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") does not support tokens yet out of the box, a parameter cannot be added to /etc/conf.d/net for configuration.

A simple workaround is to call an ip command before launching an interface. This can easily be achieved by implementing [hook functions](https://wiki.gentoo.org/wiki/Handbook:X86/Networking/Extending#Standard_function_hooks "Handbook:X86/Networking/Extending") directly in /etc/conf.d/net:

[FILE] **`/etc/conf.d/net`**

    rc_keyword="-stop"
    config_eth0="192.168.0.35/24"
    routes_eth0="default via 192.168.0.1"

    # set IPv6 interface token
    preup()

    # optional: assign the token ::35 address to fe80:
    postup()

** Note**\
The setup listed above will **not work on bridges** due to a design limitation of netifrc: At the point in time when the preup() function is called, the bridge interface does not exist yet.

A workaround for bridges is to only use the postup() function with a slight modification. The drawback: When creating (starting) the bridge, it has more addresses than necessary. But this can be ignored since the auto-generated (non-tokenized old MAC) addresses automatically vanish after their expiration time (\"valid_lft\").

[FILE] **`/etc/conf.d/net`**

    rc_keyword="-stop"
    config_br0="192.168.0.35/24"
    routes_br0="default via 192.168.0.1"

    # set IPv6 interface token
    # and set the IPv6 token to fe80: identifier.
    # filtering interface names in the postup() function using an if statement,
    # multiple interfaces / bridges can be assigned with different settings
    postup() " = "br0" ] ; then
        ip token set ::35 dev br0
        ip addr flush scope link dev br0
        ip addr add fe80::35/64 dev br0
      fi
      if [ "$" = "br1" ] ; then
        # settings for interface br1 go here
      fi
      return 0
    }