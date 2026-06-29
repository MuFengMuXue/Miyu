#  snap-refresh-control interface

The `snap-refresh-control` interface allows extended control, via [snapctl](https://snapcraft.io/docs/using-snapctl), of refreshes targeting the snap.

**This interface and the full set of features it requires to function are currently under development.**

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

`snap-refresh-control` is a marker interface  (with no associated AppArmor or Seccomp rules).

Currently it allows connected snaps to execute `snapctl refresh --proceed` to unblock pending refreshes outside of the context of the `gate-auto-refresh` hook. This interface should be used with caution.

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_refresh_control_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_refresh_control.go
