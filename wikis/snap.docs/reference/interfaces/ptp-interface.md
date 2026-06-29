#  ptp interface

The `ptp` interface allows access to the Precision Time Protocol (PTP) [Hardware Clock subsystem](https://www.kernel.org/doc/Documentation/ptp/ptp.txt) in the Linux kernel, enabling the clock to be synced to sub-100 nanoseconds.

This interface is primarily intended to be used with [Ubuntu Core](https://snapcraft.io/docs/reference/glossary/).

## Developer details

**Auto-connect**: no

See [sysfs-ptp](https://github.com/torvalds/linux/blob/master/Documentation/ABI/testing/sysfs-ptp) for device _sysfs_ location and configuration details.

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/ptp_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/ptp.go
