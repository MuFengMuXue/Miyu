#  uio interface

`uio` provides access to a specific uio device. This interface is restricted because it provides privileged access to uio hardware.

The slot is intended to be implemented by a gadget snap and is not provided by the core system snap.

**Auto-Connect**: no
**Attributes**:
 * `path` (slot): path to uio device. e.g. `/dev/uio1`

Requires snapd version *2.44+*.

To use the uio device, the snap developer must add `plugs: [ uio ]` to a snap's [snapcraft.yaml](https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/anatomy-of-snapcraft-yaml/). The snap user can then access a specific disk partition with an [interface connection](https://snapcraft.io/docs/explanation/interfaces/all-about-interfaces/).

Use  `snap interface uio` to see which disk partitions are available on the system for snaps to use:

```
$ snap interface uio
name:    uio
summary: allows access to specific uio device
slots:
  - foo:uio1
  - foo:uio2
```

Once connected, the consuming snap can use the device via the path specified by the connected slot.
