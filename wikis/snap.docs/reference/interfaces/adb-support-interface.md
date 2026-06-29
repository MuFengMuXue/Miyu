#  adb-support interface

`adb-support` allows a snap to operating the Android Debug Bridge service, providing privileged access to an Android device.

## Example

[guiscrcpy](https://snapcraft.io/guiscrcpy) uses _adb-support_ to help share an Android screen on a Linux desktop.

## Developer details

**Auto-connect**: no

Requires snapd version _2.36+_.

### Code examples

The adb-support interface is used in the _guiscrcpy_ snap: <https://github.com/srevinsaju/guiscrcpy/blob/master/snap/snapcraft.yaml>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/adb_support.go>
