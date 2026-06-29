#  classic-support interface

The `classic-support` interface sets special permissions for the [classic snap](https://snapcraft.io/classic), effectively giving device ownership to its connected snaps.

This interface is intended to be used only with [Ubuntu Core](https://snapcraft.io/docs/reference/glossary/).

Requires snapd version _2.23+_.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/classic_support_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/classic_support.go
