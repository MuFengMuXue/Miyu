#  acrn-support interface

The `acrn` interface  allows access to, and control of, user virtual machines using the [ACRN hypervisor](https://projectacrn.org/).

**This interface is primarily intended to be used with [Ubuntu Core](https://snapcraft.io/docs/reference/glossary/) devices.**

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: no

### Code examples

The following (third-party) repository contains recipes to create snap packages for ACRN: https://github.com/gvancuts/acrn-snap

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/acrn_support_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/acrn_support.go
