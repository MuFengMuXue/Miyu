## Name

systemd-network-generator.service, systemd-network-generator — Generate network configuration from the kernel command line

## Synopsis

`systemd-network-generator.service`

`/usr/lib/systemd/systemd-network-generator`

## Description

`systemd-network-generator.service` is a system service that translates `ip=` and related settings on the kernel command line (see below) into systemd.network(5), systemd.netdev(5), and systemd.link(5) configuration files understood by systemd-networkd.service(8) and systemd-udevd.service(8).

Files are generated in `/run/systemd/network/`.

Note: despite the name, this generator executes as a normal systemd service and is *not* an implementation of the systemd.generator(7) concept.

## Kernel command line options

This tool understands the following options:

`ip=`, `nameserver=`, `rd.route=`, `rd.peerdns=`  
Translated into systemd.network(5) files.

In addition to the parameters dracut.cmdline(7) defines the `ip=` option accepts the special value "`link-local`". If selected, the network interfaces will be configured for link-local addressing (IPv4LL, IPv6LL) only, DHCP or IPv6RA will not be enabled.

Added in version 245.

`ifname=`, `net.ifname_policy=`  
Translated into systemd.link(5) files.

Added in version 245.

`vlan=`, `bond=`, `bridge=`, `bootdev=`  
Translated into systemd.netdev(5) files.

Added in version 245.

See dracut.cmdline(7) and systemd-udevd.service(8) for option syntax and details.

## Credentials

**systemd-network-generator** supports the service credentials logic as implemented by `ImportCredential=`/`LoadCredential=`/`SetCredential=` (see systemd.exec(5) for details). The following credentials are used when passed in:

`network.conf.*`, `network.link.*`, `network.netdev.*`, `network.network.*`  
These credentials should contain valid networkd.conf(5), systemd.link(5), systemd.netdev(5), systemd.network(5) configuration data. From each matching credential a separate file is created. Example: a passed credential `network.link.50-foobar` will be copied into a configuration file `50-foobar.link`.

Note that the resulting files are created world-readable, it is hence recommended to not include secrets in these credentials, but to supply them via separate credentials directly to systemd-networkd.service(8).

Added in version 256.

Note that by default the systemd-networkd.service(8) service is set up to inherit the these credentials from the service manager.

## See Also

systemd(1), systemd-networkd.service(8), dracut(8)
