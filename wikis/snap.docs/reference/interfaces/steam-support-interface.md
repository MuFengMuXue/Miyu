#  steam-support interface

The `steam-support` interface has been developed specifically to help Valve's Steam client configure [pressure-vessel](https://gitlab.steamos.cloud/steamrt/steam-runtime-tools/-/tree/master/pressure-vessel) containers from the [Steam snap](https://snapcraft.io/steam).

Only the Steam snap may establish this interface.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Code examples

The source code for the Steam snap: https://github.com/canonical/steam-snap

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/steam_support_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/steam_support.go
