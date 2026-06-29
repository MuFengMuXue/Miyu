# GRAPHICS DRIVERS QUICKSTART - UBUNTU

Some of the newest titles available on Linux with Steam Play require cutting-edge drivers that are not distributed with the latest Ubuntu release. To achieve the highest level of compatibility with Windows game titles, we recommend installing the following drivers:

## NVIDIA

Linux users with NVIDIA graphics cards should install the latest NVIDIA proprietary drivers; 418.49.04 or newer is required. They can be installed directly from Canonical's repository for third-party drivers:

```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt install nvidia-driver-535
```
Note: There are newer driver series available in this ppa and this is an example.

Provide your user password when requested and reboot after the last command completes to ensure the driver has updated correctly.  

Further details about this PPA repository are available here: 
https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa

## AMD/Intel

**VR Users should skip this section and see AMD+VR instead.**

Linux users with AMD or Intel Graphics Technology should install recent versions of Mesa and LLVM through this repository: https://launchpad.net/~kisak/+archive/ubuntu/kisak-mesa

```
sudo add-apt-repository ppa:kisak/kisak-mesa
sudo apt dist-upgrade
sudo apt install mesa-vulkan-drivers mesa-vulkan-drivers:i386
```

On Radeon R9 200/300 series you have to blacklist radeon module and add following parameters to amdgpu:

```
echo "blacklist radeon" | sudo tee --append /etc/modprobe.d/blacklist.conf
echo "options amdgpu si_support=1 cik_support=1" | sudo tee --append /etc/modprobe.d/amdgpu.conf
sudo update-initramfs -u
```

Provide your user password when requested and reboot after the last command completes to ensure the driver has updated correctly.

VR is not currently supported on Intel graphics.

## AMD + VR

For users running VR on AMD, please follow the driver installation instructions
from the SteamVR for Linux GitHub project:
https://github.com/ValveSoftware/SteamVR-for-Linux#amd

# GRAPHICS DRIVERS REQUIREMENTS - GENERAL

## DirectX 9, 10, 11 games:
For best results, use the suggestions on the [DXVK driver support page](https://github.com/doitsujin/dxvk/wiki/Driver-support).

## DirectX 12 games:
For best result please follow suggestions from [vkd3d-proton's README](https://github.com/HansKristian-Work/vkd3d-proton#drivers).

## Enable Vulkan on Radeon R9 200/300 series:
On Radeon R9 200/300 series you have to blacklist radeon module and add following parameters to amdgpu:
```
echo "blacklist radeon" | sudo tee --append /etc/modprobe.d/blacklist.conf
echo "options amdgpu si_support=1 cik_support=1" | sudo tee --append /etc/modprobe.d/amdgpu.conf
sudo update-initramfs -u
```
After that remember to reboot your PC.

# Increasing The Maximum Number Of Memory Map Areas A Process May Have

Some modern games require more than the kernel's default of 65530. Custom kernels and distributions may increase that number. You can check the current value with:

```
sysctl vm.max_map_count
```

You can set a higher value with:

```
sudo sysctl vm.max_map_count=2147483642
```

This is however not persistent and will revert upon a reboot. To make it automatically apply you can create a file `/etc/sysctl.d/99-max-map-count.conf` that contains:

```
vm.max_map_count = 2147483642
```