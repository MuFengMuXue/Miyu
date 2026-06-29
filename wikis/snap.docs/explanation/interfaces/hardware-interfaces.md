# Hardware interfaces

Hardware IO (input/output) interfaces, including the [serial-port](https://snapcraft.io/docs/reference/interfaces/serial-port-interface/), [gpio](https://snapcraft.io/docs/reference/interfaces/gpio-interface/), [gpio-chardev](https://snapcraft.io/docs/reference/interfaces/gpio-chardev-interface/) and [i2c](https://snapcraft.io/docs/reference/interfaces/i2c-interface/) interfaces, are designed to be used on devices running [Ubuntu Core](https://snapcraft.io/docs/reference/glossary/). These interfaces are exposed as _slots_ from a device's [gadget snap](https://snapcraft.io/docs/reference/development/yaml-schemas/the-gadget-snap/) which is used to define and configure a device's system properties.

This approach is more robust because it allows the gadget snap providing the slot to centralise and arbitrate the connection conditions. These conditions include which other snaps, identified by their snap ID, can connect to the slots the gadget offers and, consequently, gain privileged access to the hardware.  For the application snap, usually no change is required other than to declare and use an appropriately-configured plug.

The following are exceptions to the above, and can be used without being declared in the gadget snap:
- [gpio-control interface](https://snapcraft.io/docs/reference/interfaces/gpio-control-interface/)
- [serial-port interface](https://snapcraft.io/docs/reference/interfaces/serial-port-interface/) (experimental support)

See [Supported interfaces](https://snapcraft.io/docs/reference/interfaces/) for a complete list of interfaces.

## Interface considerations

The extent of access an interface has is granted through both _connection permissions_ and the specifics of the _interface connections_ being requested.

1. **Connection permissions**: [auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/) | [privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/) | [super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)

Connection requirements are dependent on which store a developer is using.
     - [Global Snap Store](https://forum.snapcraft.io/t/glossary/14612#heading--snap-store): privileged and super-privileged interfaces require store approval because of the level of trust and permissiveness these interfaces have, which is also why certain interfaces need certain oversight. See [Permission requests](https://snapcraft.io/docs/reference/administration/process-for-aliases-auto-connections-and-tracks/) for further details.
    * [Dedicated Snap Store](https://documentation.ubuntu.com/core/explanation/stores/dedicated-snap-store): trust and permissiveness are now  the responsibility of the store owner, and many privileged interface connections can be self-served and defined within the dedicated snap store and the device context.
1. **Interface connections**: hardware IO interfaces | app-provided interfaces | other interfaces
    * **Hardware IO interfaces**: These require either a [slot](https://snapcraft.io/docs/how-to-guides/manage-snaps/connect-interfaces/) to be defined by a device's _gadget snap_ or an interface with [Hotplug support](https://snapcraft.io/docs/explanation/how-snaps-work/hotplug-support/), in which case the slot appears from the system snap.
      * An unconstrained [auto-connection](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/) cannot be used because there may be _many slots of a given interface_, resulting in ambiguity that requires  an extensive set of store rules to manage and maintain.
      * Each plug should therefore be connected to a slot, for example:
        * green led plug on app => green led slot on gadget
        * red led plug on app => red led slot on gadget
      - This kind of 1-to-1 connections can usually be established via [slot rules in the snap-declaration](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/) for the gadget.
    * **App-provided interfaces**: slots are defined by apps, or occasionally from the gadget snap,
      * May require access, such as from the [content](https://snapcraft.io/docs/reference/interfaces/content-interface/) or [shared-memory](https://snapcraft.io/docs/reference/interfaces/shared-memory-interface/) interfaces.
      * A slot might may be provided by the system snap to cover the case of an equivalent system service, such as [audio-playback](https://snapcraft.io/docs/reference/interfaces/audio-playback-interface/)
      * the slot might be [super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)
    * **Other interfaces**: For more system level access, slots are provided by the system snap.

### Code examples

The [gadget snap](https://github.com/canonical/pi-gadget/tree/20-arm64) definition for the reference [Raspberry Pi Ubuntu Core](https://ubuntu.com/core/docs/install-raspberry-pi) image contains interface definitions for various hardware IO interfaces on the system, including slots for each specific GPIO pin, i2c connections, the Bluetooth serial port, and the generic serial ports:

```yaml
slots:
  bcm-gpio-0:
    interface: gpio
    number: 0
  bcm-gpio-1:
    interface: gpio
    number: 1
  bcm-gpio-2:
    interface: gpio
    number: 2
[...]
  i2c-0:
    interface: i2c
    path: /dev/i2c-0
[...]
  bt-serial:
    interface: serial-port
    path: /dev/ttyAMA0
[...]
  serial0:
    interface: serial-port
    path: /dev/ttyS0
  serial1:
    interface: serial-port
    path: /dev/ttyS1
```

On a Raspberry Pi, the above hardware IO interfaces are accessible to apps from the system snap without requiring any further configuration.
