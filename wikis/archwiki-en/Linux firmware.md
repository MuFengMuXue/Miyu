# Linux firmware

Linux firmware is a collection of firmware binary blobs distributed alongside the kernel, necessary for partial or full functionality of certain hardware devices. These binary blobs were never permitted to include in a GPL'd work, but have been permitted to redistribute under separate cover.

Typical kinds of hardware requiring firmware:

* GPUs,
* Wired network adapters,
* Wireless network adapters,
* Bluetooth controllers,
* Sound cards—professional audio or onboard audio.

## Installation
Install the  meta package to pull all commonly used firmware. This is the recommended way for most users. To save some space you could opt into installing firmware only for individual hardware vendors your system uses.

Primary packages pulled by :

*  — AMD Radeon GPUs,
*  — Qualcomm Atheros Wi-Fi and Bluetooth adapters,
*  — Broadcom and Cypress network adapters,
*  — Cirrus Logic audio devices,
*  — Intel audio devices, Bluetooth adapters, GPUs, network adapters, NPUs, webcams and other various devices,
*  — MediaTek and Ralink network adapters,
*  — NVIDIA GPUs and SoCs,
*  — unsorted various devices,
*  — ATI Radeon GPUs,
*  — Realtek network and Bluetooth adapters.

Optional packages:

*  — Cavium LiquidIO server adapters,
*  — Marvell network adapters,
*  — Mellanox Spectrum switches,
*  — Netronome Flow Processors,
*  — Qualcomm SoCs,
*  — QLogic networked devices.

Third-party packages:

*  — loader programs in  and hotplug firmware loader, see ALSA#Firmware,
*  — gt68xx-based scanners,
*  — FX2 logic analyzers,
*  — Sound Open Firmware.

## Tips and tricks
## Detecting loaded firmware
Sometimes you want to know what firmware is loaded by your system, for debugging or to pick firmware packages to install. That could be achieved using dynamic debug:

* Add  to the kernel parameters.
:
* List loaded firmware after modifying the kernel parameters:
