# ASUS ROG Zephyrus G14 (2022) GA402

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| Webcam ||  ||
|}
This page is applicable to the Asus ROG Zephyrus G14 GA402.

## VFIO
The GPUs being muxed makes this laptop great for PCI Passthrough.

Kernel parameters can be set to bind vfio-pci to the discrete GPU.

 rd.driver.pre=vfio-pci nogpumanager vfio-pci.ids=1002:73ef,1002:ab28

The GPU can then later be unbound from vfio-pci and rebound to AMDGPU later
without disturbing the X11 session.

## Power Management
See Power management, Laptop#Power management, AMDGPU#Power profiles

## Suspend
See Power management/Suspend and hibernate#Changing suspend method.

## Wireless
## Wi-Fi
The MediaTek MT7922 works with the MT7921e driver, but has oddly high ping times (~20ms for a single hop) with high variability (>2ms jitter). So it is functional, but has problems.

Some have recommended switching it out for the more popular and widely supported Intel Wi-Fi cards.

## ASUS Linux
The ASUS Linux stack provides users of this laptop with a great many ASUS specific functions, to name a few:

*Battery Charge Limit,
*Multiplexer (GPU) Controls,
*Panel Overdrive,
*Much more.

It is highly recommended to install these tools for the optimal experience on these laptops.
