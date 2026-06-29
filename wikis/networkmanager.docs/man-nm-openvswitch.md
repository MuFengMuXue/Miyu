# Man / Nm Openvswitch

NetworkManager Open vSwitch support

nm-openvswitch

7

NetworkManager

Open vSwitch support overview

nm-openvswitch

overview of NetworkManager Open vSwitch support

# Overview

NetworkManager includes basic Open vSwitch support, good enough to be capable of setting up simple Open vSwitch configurations. It is not extensive and does not expose all functionality of Open vSwitch provides. For large or complicated deployments users are advised to use native tools shipped with Open vSwitch. This document seeks to provide overview of functionality currently provided by NetworkManager, its capabilities and limitations.

First and foremost: NetworkManager applies the configuration by modifying the OVSDB directly. Its configuration model follows the OVSDB database model closely and it does not provide the level of abstraction `ovs-vsctl` provides.

In practical terms it means the following:

- NetworkManager only ever talks to a single OVSDB instance via an UNIX domain socket.

- The configuration is made up of Bridges, Ports and Interfaces. Interfaces are always attached to Ports, and Ports are always attached to Bridges.

- NetworkManager only creates Bridges, Ports and Interfaces you ask it to. Unlike `ovs-vsctl`, it doesn't create the local interface nor its port automatically.

- You can't attach Interface directly to a Bridge. You always need a Port, even if it has just one interface.

- There are no VLANs. The VLAN tagging is enabled by setting a [ovs-port.tag](#nm-settings.property.ovs-port.tag) property on a Port.

- There are no bonds either. The bonding is enabled by enslaving multiple Interfaces to a Port and configured by setting properties on a port.

## Bridges

Bridges are represented by connections of ovs-bridge [type](#nm-settings.property.connection.type). Due to the limitations of OVSDB, "empty" Bridges (with no Ports) can't exist. NetworkManager inserts the records for Bridges into OVSDB when a Port is attached.

Known limitation: when the last NetworkManager's owned port is removed, the bridge is removed too, even if there are other externally attached ports.

## Ports

Ports are represented by connections of ovs-port [type](#nm-settings.property.connection.type). Due to the limitations of OVSDB, "empty" Ports (with no Interfaces) can't exist. Ports can also be configured to do VLAN tagging or Bonding. NetworkManager inserts the records for Ports into OVSDB when an Interface is attached. Ports must be attached to a Bridge.

Known limitation: when the last NetworkManager's owned interface is removed, the port is removed too, even if there are other externally attached interfaces.

## Interfaces

Interfaces are represented by a connections attached to a Port. The system interfaces (that have a corresponding Linux link) have a respective [connection.type](#nm-settings.property.connection.type) of the link (e.g. "wired", "bond", "dummy", etc.). Other interfaces ("internal" or "patch" interfaces) are of ovs-interface type. The OVSDB entries are inserted upon attachment to a Port.

# Examples

    $ nmcli conn add type ovs-bridge conn.interface bridge0
    Connection 'ovs-bridge-bridge0' (d10fc64d-1d48-4394-a1b8-e1aea72f27d5) successfully added.
    $ nmcli conn add type ovs-port conn.interface port0 controller bridge0
    Connection 'ovs-port-port0' (5ae22bae-bba4-4815-9ade-7e635633e1f0) successfully added.
    $ nmcli conn add type ovs-interface port-type ovs-port conn.interface iface0 \
      controller port0 ipv4.method manual ipv4.address 192.0.2.1/24
    Connection 'ovs-interface-iface0' (3640d2a1-a2fd-4718-92f1-cffadb5b6cdc) successfully added.

As said above, you need to create a Port even for a single interface. Also, before you add the Interface, the Bridge and Port devices appear active, but are not configured in OVSDB yet. You can inspect the results with `ovs-vsctl show`.

    $ nmcli conn add type ovs-port conn.interface port1 controller bridge0
    Connection 'ovs-port-port1' (67d041eb-8e7b-4458-afee-a1d07c9c4552) successfully added.
    $ nmcli conn add type ethernet conn.interface eth0 controller port1
    Connection 'ovs-slave-eth0' (d459c45c-cf78-4c1c-b4b7-505e71379624) successfully added.

Again, you need a port.

    $ nmcli conn add type ovs-port conn.interface port2 controller bridge0 ovs-port.tag 120
    Connection 'ovs-port-port2' (3994c093-4ef7-4549-a4fd-627b831c3cb8) successfully added.
    $ nmcli conn add type ethernet conn.interface eth1 controller port2
    Connection 'ovs-slave-eth1' (099be06e-71ad-484d-8d5a-fcadc5f207f5) successfully added.

It's just a port with a tag.

    $ nmcli conn add type ovs-port conn.interface bond0 controller bridge0
    Connection 'ovs-port-bond0' (d154ebf9-e999-4e1b-a084-a3de53d25d8a) successfully added.
    $ nmcli conn add type ethernet conn.interface eth2 controller bond0
    Connection 'ovs-slave-eth2' (475ac1bf-30b2-4534-a877-27f33f58b082) successfully added.
    $ nmcli conn add type ethernet conn.interface eth3 controller bond0
    Connection 'ovs-slave-eth3' (8dedeecb-ed12-482b-b77a-24a4fb835136) successfully added.

It's just a Port with multiple interfaces. See nm-settings-nmcli manual for Bonding options you can use with "nmcli c add" or "nmcli c modify". You could even set a VLAN tag on the same Port to do VLAN tagging and bonding at the same time.

# Bugs

- Not all Open vSwitch capabilities are supported.

- Open vSwitch devices don't expose many useful properties on D-Bus.

Probably many more.

# See Also

[RFC 7047: The Open vSwitch Database Management Protocol](https://www.rfc-editor.org/rfc/rfc7047.txt), `ovs-vsctl(8)`, `ovs-vswitchd.conf.db(5)`, [`nm-settings-nmcli(5)`](#nm-settings-nmcli), [`nmcli(1)`](#nmcli)
