# MSI GT72-6QE

## BIOS
Ensure that you have the latest BIOS and EC firmware from MSI's website. Once you have updated, disable C-States and Secure Boot in the BIOS.

## Installation
This notebook has a physical hardware button to switch between the Intel and discrete (Nvidia 980m) GPU. Before installing Arch, boot into Windows and use the button to switch to the Intel display adapter. Also #Networking in Linux might not work out of the box, so you may need to use a USB networking dongle or prepare your own.

Now you can follow the installation guide as usual. Remember to install the NVIDIA driver as well (Nouveau might not work). After installing, boot back into Windows and use the button to switch the display adapter back to the NVIDIA GPU.

## Troubleshooting
## Frequent Kernel Panics
By default, the linux kernel may have issues with the Intel Skylake architecture of this notebook resulting in frequent kernel panics. To resolve this issue, you may need to disable KMS and the high resolution clock by adding the following kernel parameters:
