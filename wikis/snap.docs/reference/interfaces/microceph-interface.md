# microceph interface

The `microceph` interface permits access to  the [MicroCeph](https://canonical-microceph.readthedocs-hosted.com/en/reef-stable/) socket, which is used internally by the [microceph](https://snapcraft.io/microceph) snap.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/microceph_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/microceph.go
