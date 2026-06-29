# Alienware 15

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (NVIDIA) || ||
|-
| Touchpad || ||
|-
| Camera || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Ethernet || ||
|-
| Card reader || ||
|}

For a general overview of laptop-related articles and recommendations, see Laptop. For the macro keys, see extra keyboard keys

## Networking
Install the supported driver for the QCA6174 802.11ac Wireless Network Adapter.

Download the board.bin file and put it into your firmware library:

 $ wget https://github.com/kvalo/ath10k-firmware/raw/master/QCA6174/hw3.0/2.0/board.bin
 # mkdir -p /lib/firmware/ath10k/QCA6174/hw3.0/
 # mv board.bin /lib/firmware/ath10k/QCA6174/hw3.0/

then download the specific firmware binary and move it into your firmware library:

 $ wget https://github.com/kvalo/ath10k-firmware/raw/master/QCA6174/hw3.0/2.0/firmware-4.bin_WLAN.RM.2.0-00180-QCARMSWPZ-1
 # mv firmware-4.bin_WLAN.RM.2.0-00180-QCARMSWPZ-1 /lib/firmware/ath10k/QCA6174/hw3.0/firmware-4.bin

a reboot is needed to load these files.

## Video
Nvidia & Intel video card configuration: NVIDIA Optimus

## NVIDIA Corporation GM204M GTX 965M
Currently not supported by Bumblebee (Tested on Alienware 15 R2)
Please install only Intel driver via

## NVIDIA Corporation GP104M GTX 1070 Mobile
Make sure the NVIDIA driver is installed, and install  (do not use ).

This configuration supports an external display at high refresh rate, as well as gaming using proton/steam.

Before installing optimus-manager, backup and clear out  and  to avoid user reported freezes when booting.

Optimus manager should generate approximately

Then you can switch GPUs using

 $ optimus-manager --switch nvidia

You can set the default GPU by editing  and setting

 startup_mode=nvidia

You can copy  as a starting point.

## Control of the light colors
* Currently unsupported by pyAlienFx and alienfxhave some diff from previous version.
* Probably supported by [https://github.com/rsm-gh/alienware-kbl alienware-kbl, a software to manage the light colors with a graphical interface, python or bash commands.

## Issues
## Audio
To switch to headphones after plugging them, create:

## Alienware m15 r5 Ryzen Edition
It is possible on this laptop — since it uses Ampere graphics and Optimus — to use hybrid graphics in a power efficient manner. In order to do so, use optimus-manager on "hybrid" settings to generate an Xorg configuration file. To do this, use the following (be sure to use AMDGPU graphics, i.e. ):

You will then have to generate correct udev rules to ensure the dedicated GPU will completely turn off when unused:

{{hc|/lib/udev/rules.d/80-nvidia-pm.rules|2=
# Enable runtime PM for NVIDIA VGA/3D controller devices on driver bind
ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="auto"
ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="auto"
# Disable runtime PM for NVIDIA VGA/3D controller devices on driver unbind
ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="on"
ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control",    ATTR{power/control}="on"
}}

You can confirm this is properly working by rebooting the system and running the following command:

You can then install  and use prime-run to run programs on the dedicated GPU.
