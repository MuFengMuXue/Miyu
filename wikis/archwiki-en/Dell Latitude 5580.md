# Dell Latitude 5580

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| SD card reader ||  ||
|-
| WWAN/SIM card || ||
|-
| Camera ||  ||
|-
| Fingerprint reader ||  ||
|-
| Smartcard reader || ||
|-
|}

## NVIDIA GPU
Install NVIDIA and  using pacman

Use this script to run apps using the NVIDIA GPU. I called it /usr/bin/prime, so all I have to do is run 'prime ' or change the shortcut to force the use of the dGPU.

: #!/bin/bash
: __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia __GL_SYNC_TO_VBLANK=0 "$@"

Bumblebee/Optimus was a huge headache and I couldn't seem to get either to work properly, so I gave up and used the above method.

## Fingerprint reader
Allegedly,  is needed to enable the fprint, but I have not been able to get it to work
