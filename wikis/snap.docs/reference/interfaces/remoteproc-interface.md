#  remoteproc interface

The `remoteproc` interface enables developers to interact with the [Remote Processor Framework](https://docs.kernel.org/staging/remoteproc.html) of the Linux kernel, typically allowing them to upload firmware to a SoC embedded microcontroller.

Modern ARM-based silicon contain have additional Cortex M4 or M7 based microcontrollers within the SoC.

This interface allows a snap to load a firmware to such microcontrollers via a snap, and permits the microcontroller to be started and stopped.

Requires snapd version _2.62+_.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)** : no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)** : yes

### Code examples

The test code can be found in the snapd repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/remoteproc_test.go>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/remoteproc.go>
