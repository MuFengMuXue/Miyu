This article introduces several ways to expose local services to devices on other networks.

## Contents

-   [[1] [Rationale]](#Rationale)
-   [[2] [Available software and articles]](#Available_software_and_articles)
-   [[3] [External resources]](#External_resources)
-   [[4] [References]](#References)

## [[] Rationale]

Each device on the internet has a unique [IPv4](https://en.wikipedia.org/wiki/IPv4 "wikipedia:IPv4") address. Because IPv4 addresses can only address a maximum of about 4.4 billion devices, some internet service providers (ISPs) place [NAT](https://en.wikipedia.org/wiki/NAT "wikipedia:NAT") gateways between their customers\' devices and the internet, in order to hide multiple devices behind one IPv4 address. In some cases, these NAT gateways run firewalls that prevent outside devices from establishing connections with devices on the ISPs\' networks.^[\[1\]](#cite_note-1)^

Before NAT, enabling port forwarding was all that was needed to expose a service to the internet. With NAT, this is no longer a solution.

## [[] Available software and articles]

  ------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                            Package                                                                                                                                                                                                                                                                                                                                                                                       Homepage                                                                           Description
  [Tailscale](https://wiki.gentoo.org/wiki/Tailscale "Tailscale")                 [[[net-vpn/tailscale]](https://packages.gentoo.org/packages/net-vpn/tailscale)[]]                     [https://tailscale.com/](https://tailscale.com/)   A VPN. Offers a free plan with no bandwidth restrictions; no private server needed. Offers fast speeds across all but the most complex network boundaries. Can expose one service per device to the entire internet.
  ZeroTier                                                                        [[[net-misc/zerotier]](https://packages.gentoo.org/packages/net-misc/zerotier)[]]                     [https://zerotier.com/](https://zerotier.com/)     Similar to Tailscale. No option to expose services to the internet.
  [Wireguard](https://wiki.gentoo.org/wiki/Wireguard "Wireguard")   [[[net-vpn/wireguard-tools]](https://packages.gentoo.org/packages/net-vpn/wireguard-tools)[]]   [https://wireguard.com/](https://wireguard.com/)   Self-hosted; a private server is needed. Offers fast speeds, with no traffic flowing through the private server in some cases.
  ------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [[] External resources]

-   [SSH tunneling](https://en.wikipedia.org/wiki/Tunneling_protocol#Secure_Shell_tunneling "wikipedia:Tunneling protocol") --- using a server on the internet to relay encrypted traffic.
-   [How NAT traversal works](https://tailscale.com/blog/how-nat-traversal-works) --- explains different NAT setups and how Tailscale bypasses them.

## [[] References]

1.  [[[↑](#cite_ref-1)] [[Wikipedia:CGNAT](https://en.wikipedia.org/wiki/CGNAT "wikipedia:CGNAT")]]