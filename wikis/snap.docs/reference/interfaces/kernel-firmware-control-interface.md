#  kernel-firmware-control interface

The ` kernel-firmware-control` interface permits the setting of a custom  [kernel firmware search path](https://www.kernel.org/doc/html/v4.18/driver-api/firmware/fw_search_path.html), and is typically used with [the remoteproc interface](https://snapcraft.io/docs/reference/interfaces/remoteproc-interface/) to upload microcontroller firmware.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

Requires snapd version _2.62+_.

### Code examples

The test code can be found in the snapd repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_firmware_control_test.go>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_firmware_control.go>
