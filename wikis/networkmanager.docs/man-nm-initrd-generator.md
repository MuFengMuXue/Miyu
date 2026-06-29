# Man / Nm Initrd Generator

NetworkManager developers

nm-initrd-generator

8

NetworkManager

System Administration

nm-initrd-generator

early boot NetworkManager configuration generator

nm-initrd-generator

OPTIONS

--

CMDLINE

# Description

`nm-initrd-generator` scans the command line for options relevant to network configuration and creates configuration files for an early instance of NetworkManager run from the initial ramdisk during early boot.

# Options

`-c` `--connections-dir` \<path\>
Output connection directory.

`-p` `--persistent-connections-dir` \<path\>
Persistent connection directory. If it exists, rd.neednet will not cause a default connection to be generated in absence of other options.

`-i` `--initrd-data-dir` \<path\>
Output directory for initrd data (e.g. hostname).

`-d` `--sysfs-dir` \<path\>
The sysfs mount point.

`-r` `--run-config-dir` \<path\>
Output directory for config files.

`-s` `--stdout`
Dump connections to standard output. Useful for debugging.

\<CMDLINE\>
The options that appear on the kernel command line. The following options are recognized:

ip

rd.route

bridge

bond

team

vlan

ib.pkey

bootdev

nameserver

net.ifnames

rd.peerdns

rd.iscsi.ibft

rd.nvmf.nonbft

rd.bootif

rd.neednet

rd.ethtool

rd.net.dns

rd.net.dns-backend

rd.net.dns-resolve-mode

rd.net.timeout.dhcp

rd.net.dhcp.client-id

rd.net.dhcp.retry

rd.net.dhcp.vendor-class

rd.net.dhcp.dscp

rd.net.timeout.carrier

rd.znet

rd.znet_ifname

BOOTIF

Please consult the `dracut.cmdline(7)` manual for the documentation of the precise format of the values supported.

# Differences from the network-legacy dracut module

`nm-initrd-generator` generates a set of connections that are then configured by the NetworkManager instance running in the initrd. There are some differences in behavior compared to the network-legacy dracut module:

- When an interface is configured with a static address and a gateway, the network-legacy module waits that the gateway responds to arping requests before proceeding, while NetworkManager doesn't.

- network-legacy configures interfaces one by one in the order in which they are announced by udev. If multiple interfaces specify a hostname (from command line or from DHCP), the one from the last interface activated wins. With NetworkManager, hostnames from command line have higher precedence over ones from DHCP, and the last that appears in the command line wins.

- NetworkManager supports the `ib.pkey`=\<PARENT\>.\<PKEY\> argument to set up an Infiniband partition on IPoIB parent device \<PARENT\> using the specified partition key \<PKEY\>. The partition key must be in hexadecimal notation without leading "0x", for example "ib.pkey=ib0.8004".

- NetworkManager supports the `rd.ethtool`=\<INTERFACE\>:\<AUTONEG\>:\<SPEED\> kernel command line option to set up ethtool NIC configuration parameters \<AUTONEG\> and \<SPEED\>. The \<INTERFACE\> being configured must be specified, and the other parameters are optional and can be left blank. When \<SPEED\> is set, duplex mode is automatically set to 'full'. \<INTERFACE\> accepts string values, \<AUTONEG\> accepts boolean values (true and false / on or off / 0 or 1), and \<SPEED\> accepts positive integer values.

- NetworkManager supports the `rd.net.dns-backend`=\<VALUE\> kernel command line option to configure the DNS processing mode. See the description of the `"dns"` key in the `"main section"` paragraph of [`NetworkManager.conf(5)`](#NetworkManager.conf). For example: `rd.net.dns-backend=systemd-resolved`, `rd.net.dns-backend=dnsconfd`

- NetworkManager supports the `rd.net.dns`=\<SERVER\> kernel command line option to configure a global (non interface-specific) DNS server. The option can be specified multiple time to add more than one server. Each server can be specified as a plain IP or as an URI according to the description in the "global-dns-domains sections" paragraph of [`NetworkManager.conf(5)`](#NetworkManager.conf). For example: `rd.net.dns=2001:db8::1`, `rd.net.dns=dns+tls://192.0.2.0`, `rd.net.dns=dns+tls://[2001:db8::2]:5353#example.org`. In addition, it supports configuring the `"resolve-mode"` key in the global DNS configuration via the `rd.net.dns-resolve-mode` command line option.

- NetworkManager supports the `rd.net.dhcp.dscp`={\<CS0\>\|\<CS4\>\|\<CS6\>} kernel command line option to set a specific DSCP (TOS) value in the IP header of DHCP messages.

- NetworkManager supports the `rd.net.dhcp.client-id`=\<interface\>:\<client-id\> kernel command line option to set a specific DHCPv4 client identifier for the given interface. The client-id can be specified either as a sequence of bytes in hexadecimal format separated by dashes, or as the character '@' followed by a non-empty string. When using the second format, NetworkManager prepends a zero byte to the given string, according to section 9.14 of RFC 2132. See the "ipv4.dhcp-client-id" section of [`nm-settings-nmcli(5)`](#nm-settings-nmcli) for more details. Examples: `rd.net.dhcp.client-id=eth0:01-52-54-00-45-87-42`, `rd.net.dhcp.client-id=enp1s0:@example.com`.

# Exit Status

`nm-initrd-generator` exits with status 0. It ignores unrecognized options and prints an error message if it encounters a malformed option.

# See Also

[`dracut.cmdline(7)`](#dracut.cmdline), [`NetworkManager(8)`](#NetworkManager), [`nm-settings-nmcli(5)`](#nm-settings-nmcli).
