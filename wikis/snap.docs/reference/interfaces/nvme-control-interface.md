#  nvme-control interface

The `nvme-control` interface allows snaps to manage and access NVMe controllers,alongside namespaces via in-kernel NVMe interfaces (PCI & NVMe-oF).

This interface provides access to enumerate devices, create/delete/attach/detach namespaces, and read device health/ telemetry data.

Access is limited to NVMe management operations through sysfs, nvme-fabrics char device, and controller/namespace device nodes. Raw block I/O remains constrained by device cgroups. The nvme and nvme-tcp kernel modules may auto-load as needed.

For further details on interfaces, see [How to connect interfaces](https://snapcraft.io/docs/explanation/interfaces/all-about-interfaces/).

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/onvme_control_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/nvme_control.go
