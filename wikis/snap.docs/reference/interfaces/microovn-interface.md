#  microovn interface

The `microovn` interface allows access to the MicroOVN socket, and can only be used by the [MicroOVN](https://snapcraft.io/microovn) snap. MicroOVN is a snap-based distribution of the [Open Virtual Network](https://www.ovn.org/en/).

See the [MicroOVN documentation](https://canonical-microovn.readthedocs-hosted.com/en/latest/) for further details.

---

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

With the MicroOVN snap installed, the socket is located at the following location:
 `/var/snap/microovn/common/state/control.socket`

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/microovn_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/microovn.go
