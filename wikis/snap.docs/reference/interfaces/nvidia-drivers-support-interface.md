#  nvidia-drivers-support interface

The `nvidia-drivers-support` interface is for internal Ubuntu Core use only and is meant to be used exclusively by kernel snaps.

This interface permits the [nvidia-assemble](https://snapcraft.io/nvidia-assemble) snap to access to NVIDIA char devices, `/dev/nvidiactl` and `/dev/nvidia-uvmfrom`, which it needs to assemble and load the NVIDIA kernel driver.

---

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/nvidia_drivers_support_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/nvidia_drivers_support.go
