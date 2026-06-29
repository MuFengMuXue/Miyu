# ASUS Linux

ASUS Linux is a suite of tools designed to improve the performance and functionality of ASUS laptops when running Linux. It comes in 2 main parts, asusctl and supergfxctl, the former interacts with the  and the  kernel modules to control BIOS level features and the latter is used to control the dedicated GPU in dual GPU systems.

The project is maintained by Luke Jones and is hosted on GitLab.

Asus Linux is a founding member of the Open Gaming Collective. Their Discord server is now the server for the OGC.

## Software
ASUS Linux provides many packages, please see subsections below.

There is a custom repository which contains prebuilt binaries available: Unofficial user repositories#g14, provided by Luke Jones.

This repository is the officially recommended way of installing the asus-linux utilities by the asus-linux developers, it was created and is being maintained by them.

See the Arch Guide and FAQ for instructions on utilities and common fixes.

## asusctl
 is a CLI utility for ASUS ROG & TUF laptop, to name some of the important features it gives users control over:

* Integrated GPU MUX Control
* Keyboard RGB Lighting Profile (but limited compared to the Windows AURA/Armoury Crate)
* Fan Curves
* Battery Charge Limit
* Panel Overdrive
* AniMe Matrix Screens

For usage instructions see asusctl.

## rog-control-center
 is a GUI frontend for asusctl and supergfxctl.

## Custom kernel
The ASUS Linux project maintains a set of kernel patches specific to ASUS mobile devices and packages them into a kernel. ''Typically using the custom kernel is not required''. However, on very recent laptop models, some hardware features may not function correctly without it.

## GPU
For NVidia GPUs, see PRIME, NVIDIA, and NVIDIA/Tips and tricks.

Graphics switching is preferably done with PRIME#Desktop environment integration as it is upstream recommendation.

## supergfxctl
 is a CLI utility for managing GPU switching functionality on ASUS hybrid laptops, particularly dedicated GPU MUX control.

For usage instructions see supergfxctl.

## nvidia-laptop-power-cfg
nvidia-laptop-power-cfg is a set of udev rules and modprobe configs designed to make it easier for NVidia GPU owners to easily configure their device with their respective proprietary drivers.

It is intended for Ampere architecture (RTX 2000) or later devices, but can be configured for Turing architecture (GTX 1000) cards also with the following changes after installation of the package:

{{hc|/usr/lib/udev/rules.d/80-nvidia-pm.rules |# Remove NVIDIA USB xHCI Host Controller devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c0330", ATTR{remove}="1"

# Remove NVIDIA USB Type-C UCSI devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c8000", ATTR{remove}="1"

# Remove NVIDIA Audio devices, if present
#ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x040300", ATTR{remove}="1"

# Enable runtime PM for NVIDIA VGA/3D controller devices on driver bind
ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="auto"
ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="auto"

# Disable runtime PM for NVIDIA VGA/3D controller devices on driver unbind
ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="on"
ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="on" }}
