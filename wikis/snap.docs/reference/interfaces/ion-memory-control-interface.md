#  ion-memory-control interface

The `ion-memory-control` interface allows access to the Android ION memory allocator, a Linux kernel feature for managing one or more memory pools.

This interface is primarily intended to be used with [Ubuntu Core](https://snapcraft.io/docs/reference/glossary/).

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

The device is expected in the following location:
-  `/dev/ion`

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/ion_memory_control_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/ion_memory_control.go
