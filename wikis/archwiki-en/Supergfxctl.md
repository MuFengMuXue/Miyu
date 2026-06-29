# Supergfxctl

is a useful utility provided by ASUS Linux. It helps with managing GPU switching functionality on hybrid laptops.

While supergfxctl was originally designed with ASUS Optimus laptops in mind, it has since evolved into a standalone tool that functions with any laptops with hybrid graphics.

## Pre-installation
For Optimus laptops make sure that the NVIDIA drivers are installed. Do not install . Remove  and  if they are installed and make sure no residual configs for NVIDIA, Intel and/or any PRIME managers are located in the following locations:

*
*
*

## Initramfs and kernel parameters
If your laptop has a dedicated NVIDIA GPU then you need to set some kernel parameters, see NVIDIA#DRM kernel mode setting for instructions. If your laptop has a dedicated AMD GPU then no extra steps are required.

## Installation
Installation can be done through ASUS Linux's own repository. You can also install the  package. Then, enable .

## Configuration
Settings are stored at . An example configuration file is as follows:

{{hc|supergfxd.conf|2=
{
  "mode": "Hybrid",
  "vfio_enable": false,
  "vfio_save": false,
  "always_reboot": false,
  "no_logind": false,
  "logout_timeout_s": 180,
  "hotplug_type": "None"
}
}}

## Usage
Supergfxctl supports the following modes, ,  and . It has the ability to detect if a mux switch is in use for  mode. There is also an  option that reboots the system with the NVIDIA GPU kernel module disabled.

Using the MUX switch requires that you are running asusctl, for details please see asusctl#Using the MUX switch.

## Show supported modes
The following command is used to display all the modes your laptop supports:

 $ supergfxctl -s

## Get current mode
The following command is used to query the current GPU mode:

 $ supergfxctl -g

## Switch modes
The following command is used to switch the current GPU mode to :

 $ supergfxctl -m Hybrid

## Post launch configuration
## Using supergfxctl for GPU passthrough (VFIO)
VFIO GPU passthrough can be enabled by editing . In this configuration file, it is also recommended to change the  value to , instead of  as is documented upstream.

{{hc|/etc/supergfxd.conf|
{
"vfio_enable": true,
"hotplug_type": "Asus"
}
}}

See the ASUS Linux VFIO guide for details.

## Using supergfxctl and the MUX switch
If the system is in  mode, prime-run from  can be used to run programs on the discrete GPU. This does not break applications while the MUX switch is enabled, so it can be used wherever more graphics performance is needed.

## Using supergfxctl with a Wayland client
Since Wayland supports multiple GPUs simultaneously, users do not need to install supergfxctl unless they want to use VFIO or further limit power consumption.  mode can be switched with asusctl, see asusctl#Using the MUX switch for details.

## Graphical utilities
Users of GNOME & KDE can make use of desktop environment add-ons to control supergfxctl from their desktop. The following is a list of these including links:

{| class="wikitable"
! Name !! Desktop !! Link
|-
| GPU Supergfxctl Switch || Gnome (46+) || https://extensions.gnome.org/extension/7018/gpu-supergfxctl-switch/
|-
| supergfxctl-gex || Gnome || https://extensions.gnome.org/extension/5344/supergfxctl-gex/
|-
| plasma6-applets-supergfxctl || KDE Plasma ||
|-
| rog-control-center || Any ||
|-
|}
