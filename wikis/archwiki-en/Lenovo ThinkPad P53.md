# Lenovo ThinkPad P53

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU (Intel) ||  ||
|-
| GPU (Nvidia) ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|}

## Discrete GPU
This model uses PRIME for combining the integrated and the dedicated GPU. As the external graphic ports are wired to the discrete GPU, drivers for the discrete GPU need to be present in order to use them. However, no special X.org configuration should be necessary, as xrandr should the ports automatically. If not, follow the instructions in PRIME#Reverse PRIME.

## GPU passthrough
Both the motherboard and the CPU in this model provide IOMMU and VT-d support, allowing GPU passthrough to virtual machines. However, Kernel DMA Protection needs to be enabled as well in order for VT-d to work:
# In the UEFI settings, go to
# Make sure the following entries are enabled:
#* Kernel DMA Protection
#* Intel Virtualization Technology
#* Intel VT-d Feature

Follow this instructions afterwards. At least for the Quadro T1000 GPU, it was required to follow these troubleshooting steps in order to allow the driver to load:
* PCI passthrough via OVMF#QEMU 4.0: Unable to load graphics drivers/BSOD/Graphics stutter after driver install using Q35
* PCI passthrough via OVMF#"Error 43: Driver failed to load" with mobile (Optimus/max-q) nvidia GPUs
