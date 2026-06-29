#  vcio interface

The `vcio` interface permits input and output access to a Raspberry Pi's _VideoCore_ multimedia processor, typically used to improve graphics performance and to accelerate the encoding or decoding of media codecs.

This interface is primarily intended to be used with [Ubuntu Core](https://snapcraft.io/docs/reference/glossary/).

## Developer details

**Auto-connect**: no

A Raspberry Pi permits its GPU to be programmed from userspace via the `/dev/vcio`
 device, access to which this interface enables.

### Code examples

The Kodi-Raspberry Pi standalone [snap](https://snapcraft.io/kodi-pi-standalone) uses the _vcio_ interface, as configured in its snapcraft.yaml: https://github.com/ogra1/kodi-pi-standalone/blob/master/snap/snapcraft.yaml

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/vcio_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/vcio.go
