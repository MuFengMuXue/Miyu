#  sd-control interface

The `sd-control` interface allows for the management and control of SD cards on certain devices using the DualSD driver.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

The main DualSD device node (`/dev/DualSD`) is used to control certain aspects of SD cards on the system.

Requires snapd version _2.51.3+_.

### Code examples

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/sd_control.go>
