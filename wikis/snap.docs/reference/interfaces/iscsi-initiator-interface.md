#  iscsi-initiator interface

The `iscsi-initiator` interface allows snaps to act as iSCSI initiators, enabling them to discover, connect to, and manage iSCSI targets for block storage access.

The interface loads kernel modules required for iSCSI operations including iscsi_tcp for transport and target_core_mod for LIO functionality.

See [Interface management](https://snapcraft.io/docs/how-to-guides/manage-snaps/connect-interfaces/) and [Supported interfaces](https://snapcraft.io/docs/reference/interfaces/) for further details on how interfaces are used.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/iscsi_initiator_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/iscsi_initiator.go
