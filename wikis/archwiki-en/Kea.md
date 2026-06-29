# Kea

Kea DHCP is the current Dynamic Host Configuration Protocol server of the Internet Systems Consortium (ISC).

## Installation
Install the  package. For additional documentation install .

Optional dependencies are:

*  for Kerberos support
*  as database backend
*  as database backend
*  to use Kea Shell

## Configuration
The configuration files are located under . The content of the configuration files uses JSON structures. For special configurations that are not yet included in the following examples, please refer to the Kea documentation.

## IPv4 DHCP
To use DHCP for IPv4, the configuration file  must be adapted and the service  must be activated and started.

Make sure to assign a static IP address to the interface on which Kea is listen on.

## Example single subnet configuration
Assumptions for the example:

* The net is
* DNS server has the IP
* Gateway has the IP
* Static IP of the DHCP server network interface  is
* Kea should provide IPs from  to

A minimal configuration file  could look like:

{{hc|/etc/kea/kea-dhcp4.conf|
{
    "Dhcp4": {
        "interfaces-config": {
            "interfaces": [ "eth0/192.168.0.253" ],
            "dhcp-socket-type": "raw"
        },

        "subnet4": [
            {
                "id": 1,
                "subnet": "192.168.0.0/24",
                "pools": [ { "pool": "192.168.0.100 - 192.168.0.199" } ],
                "option-data": [
                    {
                        "name": "routers",
                        "data": "192.168.0.254"
                    },
                    {
                        "name": "domain-name-servers",
                        "data": "192.168.0.1"
                    }
                ]
            }
        ]
    }
}
}}

## Example multiple subnet configuration
Assumptions for the example:

* The networks are:
** Network 1:  (is a standard physical network)
** Network 2:  (is a virtual VLAN network)
* DNS servers are:
** Network 1 hosts it's own DNS server at IP:
** Network 2 uses upstream Google DNS:  &
* Gateways are:
** Network 1:
** Network 2:
* Static IP of the DHCP servers are:
** Network 1: network interface  is
** Network 2: network interface  is
* Kea should provide IPs:
** Network 1: from  to
** Network 2: from  to
* You have a couple of static IPs defined:
** Network 1: Has two special phones with static leases  &&
* You want to enable maximum debug logging for IPv4 in order to troubleshoot any problems with IP reservation

A more complex configuration file  could look like:

{{hc|/etc/kea/kea-dhcp4.conf|
{
    "Dhcp4": {
        "interfaces-config": {
            "interfaces": [ "eth0/192.168.0.253", "eth0.100/192.168.1.253" ],
            "dhcp-socket-type": "raw"
        },
        "loggers": [
          {
            "name": "kea-dhcp4",
            "severity": "DEBUG",
            "debuglevel": 99,
            "output_options": [
              {
                "output": "stdout"
              }
            ]
          }
        ],
        "subnet4": [
            {
                "id": 1,
                "subnet": "192.168.0.0/24",
                "interface": "eth0",
                "pools": [ { "pool": "192.168.0.100 - 192.168.0.199" } ],
                "option-data": [
                    {
                        "name": "routers",
                        "data": "192.168.0.254"
                    },
                    {
                        "name": "domain-name-servers",
                        "data": "192.168.0.1"
                    }
                ],
                "reservations": [
                {
                    "hostname": "phone1",
                    "hw-address": "1a:1b:1c:1d:1e:1f",
                    "ip-address": "192.168.0.10"
                },
                {
                    "hostname": "phone2",
                    "client-id": "01:11:22:33:44:55:66",
                    "ip-address": "192.168.0.11"
                }
            ]
            },
            {
                "id": 2,
                "subnet": "192.168.1.0/24",
                "interface": "eth0.100",
                "pools": [ { "pool": "192.168.1.2 - 192.168.1.252" } ],
                "option-data": [
                    {
                        "name": "routers",
                        "data": "192.168.1.254"
                    },
                    {
                        "name": "domain-name-servers",
                        "data": "8.8.8.8, 8.8.4.4"
                    }
                ]
            }
        ]
    }
}
}}

## Usage
Kea includes four systemd unit files:

{| class="wikitable"
! Unit file
! Manual page
! Description
|-
| kea-dhcp4.service
|
| The DHCPv4 daemon
|-
| kea-dhcp6.service
|
| The DHCPv6 daemon
|-
| kea-dhcp-ddns.service
|
| The DNS update daemon
|-
| kea-ctrl-agent.service
|
| Exposing a REST interface for managing Kea servers
|}

The configuration file for DHCPv4 can be checked for errors by running the command:

 # kea-dhcp4 -t /etc/kea/kea-dhcp4.conf

If everything looks good, then you can enable/start .
