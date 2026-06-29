For modern clients, IPsec IKEv2 MSCHAPv2 is now the preferred VPN solution. It is supported by Windows since Windows 7, Android since 11, macOS since 10.11, iOS since 9. Both full tunnel and split tunnel configurations are possible (Split tunnel may be require additional configuration on the client)

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Assumptions and example settings]](#Assumptions_and_example_settings)
    -   [[1.2] [Before emerging strongSwan]](#Before_emerging_strongSwan)
    -   [[1.3] [Create missing directories]](#Create_missing_directories)
    -   [[1.4] [Copy certificates and keys to the correct place]](#Copy_certificates_and_keys_to_the_correct_place)
-   [[2] [Server configuration 1:Base configuration]](#Server_configuration_1:Base_configuration)
    -   [[2.1] [Configuration File]](#Configuration_File)
-   [[3] [Server configuration 2: Policy based, full-tunnel VPN]](#Server_configuration_2:_Policy_based.2C_full-tunnel_VPN)
    -   [[3.1] [Configuration file]](#Configuration_file_2)
        -   [[3.1.1] [VPN Server is the default gateway]](#VPN_Server_is_the_default_gateway)
        -   [[3.1.2] [VPN Server is the not default gateway]](#VPN_Server_is_the_not_default_gateway)
            -   [[3.1.2.1] [NAT with iptables]](#NAT_with_iptables)
            -   [[3.1.2.2] [NAT with nftables]](#NAT_with_nftables)
-   [[4] [Server configuration 3: XFRM Route based, full-tunnel VPN]](#Server_configuration_3:_XFRM_Route_based.2C_full-tunnel_VPN)
    -   [[4.1] [Configuration File]](#Configuration_File_3)
    -   [[4.2] [Creating interface]](#Creating_interface)
        -   [[4.2.1] [VPN Server is the default gateway]](#VPN_Server_is_the_default_gateway_2)
        -   [[4.2.2] [VPN Server is the not default gateway]](#VPN_Server_is_the_not_default_gateway_2)
            -   [[4.2.2.1] [NAT with iptables]](#NAT_with_iptables_2)
            -   [[4.2.2.2] [NAT with nftables]](#NAT_with_nftables_2)
-   [[5] [Server configuration 4: vti Route based, full-tunnel VPN]](#Server_configuration_4:_vti_Route_based.2C_full-tunnel_VPN)
    -   [[5.1] [Charon configuration]](#Charon_configuration)
    -   [[5.2] [Configuration file]](#Configuration_file_4)
    -   [[5.3] [Interface configuration]](#Interface_configuration)
        -   [[5.3.1] [VPN Server is the default gateway]](#VPN_Server_is_the_default_gateway_3)
        -   [[5.3.2] [VPN Server is the not default gateway]](#VPN_Server_is_the_not_default_gateway_3)
            -   [[5.3.2.1] [NAT with iptables]](#NAT_with_iptables_3)
            -   [[5.3.2.2] [NAT with nftables]](#NAT_with_nftables_3)
-   [[6] [Server configuration 5: Policy based, split-tunnel VPN]](#Server_configuration_5:_Policy_based.2C_split-tunnel_VPN)
    -   [[6.1] [Configuration File]](#Configuration_File_5)
-   [[7] [Server configuration 6: DHCP addressing, policy-based full-tunnel VPN]](#Server_configuration_6:_DHCP_addressing.2C_policy-based_full-tunnel_VPN)
    -   [[7.1] [Plugin configuration]](#Plugin_configuration)
    -   [[7.2] [Server configuration]](#Server_configuration)
        -   [[7.2.1] [VPN Server is the default gateway]](#VPN_Server_is_the_default_gateway_4)
        -   [[7.2.2] [VPN Server is the not default gateway]](#VPN_Server_is_the_not_default_gateway_4)
            -   [[7.2.2.1] [NAT with iptables]](#NAT_with_iptables_4)
            -   [[7.2.2.2] [NAT with nftables]](#NAT_with_nftables_4)
-   [[8] [Server configuration 7: RADIUS authentication/pools, policy based full tunnel]](#Server_configuration_7:_RADIUS_authentication.2Fpools.2C_policy_based_full_tunnel)
    -   [[8.1] [Plugin configuration]](#Plugin_configuration_2)
    -   [[8.2] [Configuration File]](#Configuration_File_6)
-   [[9] [Client configuration notes]](#Client_configuration_notes)
    -   [[9.1] [Windows]](#Windows)
        -   [[9.1.1] [Enabling split tunneling]](#Enabling_split_tunneling)
            -   [[9.1.1.1] [Enable split tunneling via the GUI]](#Enable_split_tunneling_via_the_GUI)
            -   [[9.1.1.2] [Via PowerShell]](#Via_PowerShell)
        -   [[9.1.2] [Making a more secure proposal]](#Making_a_more_secure_proposal)
    -   [[9.2] [MacOS]](#MacOS)
    -   [[9.3] [Android]](#Android)
        -   [[9.3.1] [Android 11]](#Android_11)
    -   [[9.4] [iOS]](#iOS)

## [Introduction]

IPsec IKEv2 MSCHAPv2 is VPN protocol commonly supported now. This guide will not cover setting up DHCP or RADIUS. PKI will also not be covered, but the [[[app-crypt/easy-rsa]](https://packages.gentoo.org/packages/app-crypt/easy-rsa)[]] package can quickly create a PKI suitable for use for a VPN server. Its also possible to create server certificate signed by a real CA like [Let\'s_Encrypt](https://wiki.gentoo.org/wiki/Let%27s_Encrypt "Let's Encrypt"). IPv6 is not covered, even though its a first-class citizen in IPsec IKEv2 MSCHAPv2 - the reason being is for dynamic IP strongSwan would need to support a prefix delegation (PD) client, which it currently does not. In addition, Windows client is different with respect to ipv6 to all other clients.

Client configuration for common client will be covered.

### [Assumptions and example settings]

-   Domain is example.com
-   Server name is vpn.example.com
-   CA file is called [ca.crt]
-   Server cert is [vpn.example.com.crt]
-   Server key is [vpn.example.com.key]
-   IP being server to the clients is 172.21.119.0/24, except 172.21.119.1 (which some configuration need for the server).
-   Linux Kernel at least 5.4
-   USing current stable version of [[[net-vpn/strongSwan]](https://packages.gentoo.org/packages/net-vpn/strongSwan)[]] in Portage

### [Before emerging strongSwan]

The [eap] USE Flag needs to be set on [[[net-vpn/strongSwan]](https://packages.gentoo.org/packages/net-vpn/strongSwan)[]]

### [Create missing directories]

Some of the strongSwan directories are not create by either strongSwan itself or the ebuild currently, so those needs to be created:

`root `[`#`]`( umask 007 ;\ `

    mkdir /etc/swanctl/;\
    mkdir /etc/swanctl/x509;\
    mkdir /etc/ipsec.d;\

mkdir /etc/ipsec.d/; )

### [Copy certificates and keys to the correct place]

`root `[`#`]`cp ca.crt /etc/swanctl/conf.d/x590ca`

`root `[`#`]`cp server.example.com.crt /etc/swanctl/conf.d/x509`

`root `[`#`]`cp server.example.com.key /etc/swanctl/conf.d/private`

## [Server configuration 1:Base configuration]

Each server configuration will have its own section, this is the one the be used as a template for the others. Note that configuration CAN be mixed and matched, and is encouraged.

### [Configuration File]

[FILE] **`/etc/swanctl/conf.d/vpn.example.com.conf`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    }
    secrets
    }
    authorities

Here, an IPsec responder is defined that serves IP from 172.21.119.0/24 block, and a single user named \"avatar\" with the password \"unobtainium\". Multiple pools and usernames can be defined. For a guide to the config file format, see [swanctl.conf](https://wiki.strongswan.org/projects/strongswan/wiki/Swanctlconf)

There are 2 extra lines to required to deal with buggy clients. The [proposals=aes128-aes192-aes256-sha1-sha256-sha384-modp1024,default] is for Windows, which will not negotiate a DH higher than modp1024 without a registry hack (described later). The [send_cert=always] is for the native Android client, which doesn\'t ask for it like other clients but needs it.

## [][Server configuration 2: Policy based, full-tunnel VPN]

### [Configuration file]

[FILE] **`/etc/swanctl/conf.d/vpn.example.com.conf`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    }
    secrets
    }
    authorities

The configuration is pretty much the same as above. If there\'s an internal DNS server, it can be specified in the pools section, this is required for \"split-horizon\" DNS setup.

#### [VPN Server is the default gateway]

No extra action is required. It Just Works.

#### [VPN Server is the not default gateway]

Extra steps are required. The VPN server will be able to send out packets, but the other clients on the network won\'t know how to get them back to VPN server, resulting in one-way traffic. There are several solution, but the easiest to the NAT the clients.

##### [NAT with iptables]

Replace [eth0] with the real outgoing interface

`root `[`#`]`iptables -t nat -A POSTROUTING -s 172.21.119.0/24 -o eth0 -m policy --dir out --pol ipsec -j ACCEPT`

`root `[`#`]`iptables -t nat -A POSTROUTING -s 172.21.119.0/24 -o eth0 -j MASQUERADE`

##### [NAT with nftables]

Replace [eth0] with the real outgoing interface

[FILE] **`ipsec-nat.nft`**

    #!/sbin/nft -f

    table ip ipsec-nat
    }

## [][Server configuration 3: XFRM Route based, full-tunnel VPN]

### [Configuration File]

[FILE] **`/etc/swanctl/conf.d/vpn.example.com.conf`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    }
    secrets
    }
    authorities

The new additions are the [if_id_in=500] and [if_id_out=500]. The value [500] is arbitrary. Any nonzero [u32] is valid.

### [Creating interface]

Note the interface may (and should) be create before strongSwan starts. Note that, as of Feb 2022, neither [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") nor [Netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") ([[[bug #443480]](https://bugs.gentoo.org/show_bug.cgi?id=443480)[]]) support creation of xfrm interfaces, while systemd-networkd does.

To create the interface (replace [eth0] with the real outgoing interface):

`root `[`#`]`ip link add xfrm0 type xfrm dev eth0 if_id 500`

`root `[`#`]`ip addr add 172.21.119.1/24 dev xfrm0`

`root `[`#`]`ip link set xfrm0 up`

[xfrm0] is an arbitrary name. The [if_id] must match the value in [/etc/swanctl/conf.d/vpn.example.com.conf]. Note that 172.21.119.1 was intentionally left out of the client IP pool so the server could claim it. If the server has as static allocation of ipv6 addresses, the interface may be assigned an ipv6 address too.

#### [VPN Server is the default gateway]

No extra action is required. It Just Works.

#### [VPN Server is the not default gateway]

Extra steps are required. The VPN server will be able to send out packets, but the other clients on the network won\'t know how to get them back to VPN server, resulting in one-way traffic. There are several solution, but the easiest to the NAT the clients.

##### [NAT with iptables]

Replace [eth0] with the real outgoing interface (NOT the xfrm interface)

`root `[`#`]`iptables -t nat -A POSTROUTING -s 172.21.119.0/24 -o eth0 -j MASQUERADE`

##### [NAT with nftables]

Replace [eth0] with the real outgoing interface (NOT the xfrm interface)

[FILE] **`ipsec-nat.nft`**

    #!/sbin/nft -f

    table ip ipsec-nat
    }

## [][Server configuration 4: vti Route based, full-tunnel VPN]

### [Charon configuration]

Edit [/etc/strongswan.d/charon.conf] and change [install_routes] to [no]

### [Configuration file]

[FILE] **`/etc/swanctl/conf.d/vpn.example.com`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    }
    secrets
    }
    authorities

### [Interface configuration]

`root `[`#`]`ip tunnel add vti0 loocal 192.168.50.68 remote 0.0.0.0 mode vti key 0x0001`

`root `[`#`]`sysctl -w net.ipv4.conf.vti0.disable_policy=1`

`root `[`#`]`ip addr add 172.21.119.1/24 dev vti0`

`root `[`#`]`ip link set vti0 up`

Substitute [192.168.50.68] with the real outgoing interface.the [key] value must match the [mark_in] and [mark_out] value in the config file.

Note that 172.21.119.1 was intentionally left out of the client IP pool so the server could claim it. For IPv6 users, a separate vti6 interface will be required.

#### [VPN Server is the default gateway]

No extra action is required. It Just Works.

#### [VPN Server is the not default gateway]

Extra steps are required. The VPN server will be able to send out packets, but the other clients on the network won\'t know how to get them back to VPN server, resulting in one-way traffic. There are several solution, but the easiest to the NAT the clients.

##### [NAT with iptables]

Replace [eth0] with the real outgoing interface (NOT the vti interface)

`root `[`#`]`iptables -t nat -A POSTROUTING -s 172.21.119.0/24 -o eth0 -j MASQUERADE`

##### [NAT with nftables]

Replace [eth0] with the real outgoing interface (NOT the vti interface)

[FILE] **`ipsec-nat.nft`**

    #!/sbin/nft -f

    table ip ipsec-nat
    }

## [][Server configuration 5: Policy based, split-tunnel VPN]

### [Configuration File]

[FILE] **`/etc/swanctl/conf.d/vpn.example.com.conf`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    }
    secrets
    }
    authorities

The change this time is in the [local_ts] parameters. This only allows traffic going to 192.168.50.0/24 (an internal network, replace with the real internal network). It up to the client as to what to do with other traffic. Most client (including strongSwan itself) will not send such traffic over the tunnel and let it go over through the appropriate interface.. Windows is the exception, and by default, attempts to send all traffic over the tunnel, unless told not to.

If using split-horizon DNS, add a DNS server to the pool (like the full-tunnel case), but additional care is needed, that the DNS server is in the range of [local_ts] and that it can resolve all addresses including those outside the work, otherwise the client may lose the ability to resolve non-internal sites.

If the a route-based VPN server is desired, see the section about about route-based VPN. IF the server is not the default gateway, see the sections about setting up NAT.

## [][Server configuration 6: DHCP addressing, policy-based full-tunnel VPN]

[[[net-vpn/strongswan]](https://packages.gentoo.org/packages/net-vpn/strongswan)[]] needs to [dhcp] and [farp] flags configured. This plugin only works with DHCPv4.

### [Plugin configuration]

IF the VPN server is not the DHCP server, no additional configuration is required. If the VPN server is the DHCP server, configuration is required if the DHCP daemon does not listen on localhost. See [dhcp plugin](https://wiki.strongswan.org/projects/strongswan/wiki/Dhcpplugin) for the configuration details.

To configure the plugin, edit [/etc/strongswan/charon.d/dhcp].

### [Server configuration]

[FILE] **`/etc/swanctl/conf.d/vpn.example.com.conf`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    secrets
    }
    authorities

The change this time is [pools=dhcp]. This will serve client IP address from the DHCP server. For a split tunnel server, set [local_ts] to the internal network

#### [VPN Server is the default gateway]

No extra action is required. It Just Works.

#### [VPN Server is the not default gateway]

##### [NAT with iptables]

Replace [eth0] with the real outgoing interface. This is mostly the same, with one addition: The server itself should not NAT itself. Replace [192.168.50.68] with the real outgoing interface IP and [192.168.50.0] with the IP pool issued by the DHCP server.

`root `[`#`]`iptables -t nat -A POSTROUTING -s 192.168.50.68 -o eth0 -j ACCEPT`

`root `[`#`]`iptables -t nat -A POSTROUTING -s 192.168.50.0/24 -o eth0 -m policy --dir out --pol ipsec -j ACCEPT`

`root `[`#`]`iptables -t nat -A POSTROUTING -s 192.168.50.0/24 -o eth0 -j MASQUERADE`

##### [NAT with nftables]

Replace [eth0] with the real outgoing interface. This is mostly the same, with one addition: The server itself should not NAT itself. Replace [192.168.50.68] with the real outgoing interface IP and [192.168.50.0] with the IP pool issued by the DHCP server.

[FILE] **`ipsec-nat.nft`**

    #!/sbin/nft -f

    table ip ipsec-nat
    }

## [][Server configuration 7: RADIUS authentication/pools, policy based full tunnel]

### [Plugin configuration]

To configure the plugin, edit [/etc/strongswan/charon.d/eap-radius.conf]. See [EAP-Radius](https://wiki.strongswan.org/projects/strongswan/wiki/EAPRADIUS) for details.

### [Configuration File]

[FILE] **`/etc/swanctl/conf.d/vpn.example.com.conf`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    secrets
    authorities

Here, [auth] on [remote-1] changes to [eap-radius]. The pool and secrets section is empty, as the values will be returned by the RADIUS server. For a split tunnel, adjust [local_ts]. For a route-based VPN, see the above section. If the VPN server is not the default gateway, see the above section on NAT.

Note that many clients perfer EAP-PEAPv0/MSCHAPv2 over EAP-MSCHAPv2, so clients will likely start using the former if its available. EAP-PEAPv0/MSCHAPv2 requires some special OIDs on the RADIUS server certificate.

## [Client configuration notes]

### [Windows]

#### [Enabling split tunneling]

BY default, Windows connects via full tunnel mode even if the server local traffic selector are restricted, dropping extra traffic. To get Windows to split tunnel, there are 2 options

##### [Enable split tunneling via the GUI]

Go to \"Change adapter options\" to show the adapters. Right-click the VPN connection, choose Properties, then Networking, then Internet Protocol Version 4 (TCP/IPv4), then Properties, then Advanced, then uncheck \"Use default gateway on remote network\".

##### [Via PowerShell]

[CODE]

    Set-VPNconnection -name vpn.example.com -SplitTunneling $true

Substitute [vpn.example.com] with the given VPN connection name

#### [Making a more secure proposal]

Windows won\'t offer and IKE proposal better then modp1024, which strongSwan does not include in the default proposal. It is however, possible to windows to aes256-sha1-modp2048 through a registry addition. Create the key `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\Parameters\NegotiateDH2048_AES256` as a **DWORD**. Set it to **1** to allow windows to accept a proposal of aes256-sha1-modp2048. Set it to **2** to force windows disallow lesser proposals.

### [MacOS]

The \"Remote name\" must be the subjectAltName or CN name of the VPN server (usually, it is DNS names). The \"Local Name\" may remain blank.

### [Android]

The native android client ha a few bugs. First, even though the IPSec identifier says (unused), it must actually be populated, but the value is unimportant. Second, even though the IPSec CA certificate is \"optional\", it isn\'t if using a CA (like a internal one) Android does not know about - Android will fail to connect without it.

#### [Android 11]

The native client for Android 11 does not work. See [strongSwan issue \# 3673](https://wiki.strongswan.org/issues/3673). This is an Android bug. not a strongSwan one. Until (if) Google fixes it, use the strongSwan client instead.

### [iOS]

If the VPN server certificate is not signed by an authority known by iOS, the certificate must be downloaded (either via Safari or e-mail attachment) and installed as \"profile\" in Settings. Note a raw .crt file is needed, iOS won\'t install the certificate from a PKCS#12 bundle.