#  xilinx-dma interface

The `xilinx-dma` interface allows access to [Xilinx](https://en.wikipedia.org/wiki/Xilinx) DMA IP from a connected [PCIe card](https://github.com/Xilinx/dma_ip_drivers/) on a device typically running [Ubuntu Core](https://snapcraft.io/docs/glossary#heading--ubuntu-core).

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/xilinx_dma_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/xilinx_dma.go
