#  userns interface

The `userns` interface permits a snap to create new user [namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html). This is a system-level interface, and is not designed to be used with higher level snap applications.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

This interface  supports the inclusion of the appropriate AppArmor and seccomp policies to allow user namespaces to be created when this interface is plugged.

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/userns_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/userns.go
