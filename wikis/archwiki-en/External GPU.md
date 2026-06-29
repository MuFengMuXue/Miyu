# External GPU

On computers equipped with Thunderbolt 3+ or USB4, it is possible to attach a desktop-grade external graphics card (eGPU) using a GPU enclosure. eGPU.io is a good resource with buyer's guide and a community forum. While some manual configuration (shown below) is needed for most modes of operation, Linux support for eGPUs is generally good.

## Installation
## Thunderbolt
The eGPU enclosure Thunderbolt device may need to be authorized first after plugging in (based on your BIOS/UEFI Firmware configuration). Follow Thunderbolt#User device authorization. If successful, the external graphics card should show up in :

Depending on your computer, its firmware and enclosure firmware, Thunderbolt will limit host  eGPU bandwidth to some extent due to the number of PCIe lanes and OPI Mode:

You may need to make your system hotplug aware by adding the following kernel parameters:

 pcie_ports=native pci=assign-busses,hpbussize=0x33,realloc,hpmmiosize=128M,hpmmioprefsize=16G

This tells the kernel that your PCIe is hot-pluggable, which is required for Thunderbolt.

You may also need to add a modprobe rule to ensure the driver loads after thunderbolt, if your thunderbolt GPU is using the same drivers as your internal GPU (whether discrete or integrated)

The below example is for . Create:

Substitute  for the driver of your choice if you are not using an AMD GPU.

You may also need to tell mkinitcpio to load the thunderbolt driver before executing any hooks by modifying the  line in :

 MODULES=(thunderbolt)

after that, regenerate the initramfs and reboot.

This ensures that the amdgpu driver loads only after the thunderbolt driver has initialized the subsystem and has made the external GPU also available, allowing it to properly initialize both GPUs.

## Drivers
A driver compatible with your GPU model should be installed:

* AMDGPU
* NVIDIA proprietary NVIDIA drivers
* Nouveau open-source NVIDIA drivers

If installed successfully,  should show that a driver has been associated with your card:

## AMDGPU
Note that the AMDGPU driver (with either Thunderbolt or USB4) might in some cases set the wrong pcie_gen_cap option and fall back to PCIe gen 1.1 speed, with possibly serious performance issues.
In this case the proper value can be set as module option (see Kernel module#Using modprobe.d) or even passed as kernel parameters:

This will set PCIe gen 3 speed. A full list of options can be found in amd_pcie.h.

## NVIDIA
For NVIDIA eGPUs on some systems you may need to early load the thunderbolt kernel module to ensure it is loaded before .

* If you use mkinitcpio initramfs, follow mkinitcpio#MODULES to add modules.
* If you use Booster, follow Booster#Early module loading.
* If you use dracut, follow dracut#Early kernel module loading.

## Compute-only workloads
Right after completing installation steps, compute-only workloads like General-purpose computing on graphics processing units#CUDA that do not need to display anything should work without any extra configuration. The nvidia-smi utility (provided by the  package) should work with the proprietary NVIDIA driver. Proprietary NVENC/NVDEC should work (without OpenGL interop).

This use-case should also support full hotplug. Hot-unplug should be also possible (probably depending on drivers used). On NVIDIA, active  is expected to prevent clean hot-unplug.

## Xorg
Multiple setups combining internal (iGPU) and external (eGPU) cards are possible, each with own advantages and disadvantages.

## Xorg rendered on eGPU, PRIME display offload to iGPU
* Most programs that make use of GPU run out-of-the-box on eGPU: /, /, / (including OpenGL interop).
* Xorg only starts with the eGPU plugged in.
* Monitors attached to eGPU work out-of-the-box, PRIME display offload can be used for monitors attached to iGPU (i.e. internal laptop screen).

Main article is PRIME#Reverse PRIME. Also documented in NVIDIA driver docs Chapter 34. Offloading Graphics Display with RandR 1.4.

Use Xorg configuration snippet like this one:

To validate this setup, use , which should display

To output to internal laptop screen and/or other monitors attached to iGPU, RandR 1.4 PRIME display offload can be used, using names from above  output:

You may want to run this command before a display manager shows login prompt or before desktop environment starts, see xrandr#Configuration and xinit.

Vulkan may enumerate GPUs independently of Xorg, so in order to run for example  in this setup, one may need to pass  option. Alternatively, a layer to reorder GPUs during enumeration can be activated with the same effect:  or equivalently .

## Xorg rendered on iGPU, PRIME render offload to eGPU
* Programs are rendered on iGPU by default, but PRIME render offload can be used to render them on eGPU.
* Xorg starts even with eGPU disconnected, but render/display offload will not work until it is restarted.
* Monitors attached to iGPU (i.e. internal laptop screen) work out-of-the-box, PRIME display offload can be used for monitors attached to eGPU.

Main article is PRIME#PRIME GPU offloading. Also documented in NVIDIA driver docs Chapter 35. PRIME Render Offload.

With many discrete GPU drivers, this mode should be the default without any manual Xorg configuration. If that does not work, or if you use proprietary NVIDIA drivers, use the following:

To validate this setup, use , which should display

To render  on the eGPU, PRIME render offload can be used:

* for proprietary NVIDIA drivers:
* for proprietary NVIDIA drivers (convenience wrapper):
* for open-source drivers:

To output to monitors connected to eGPU, RandR 1.4 PRIME display offload can be again used:

 $ xrandr --setprovideroutputsource NVIDIA-G0 modesetting && xrandr --auto

NVIDIA drivers 460.27.04+ implement an optimization for a special case of combined render and display offloads:

: Added support for “Reverse PRIME Bypass”, an optimization that bypasses the bandwidth overhead of PRIME Render Offload and PRIME Display Offload in conditions where a render offload application is fullscreen, unredirected, and visible only on a given NVIDIA-driven PRIME Display Offload output. Use of the optimization is reported in the X log when verbose logging is enabled in the X server.

## Separate Xorg instance for eGPU
Main article is nvidia-xrun#External GPU setup.

## Known issues with eGPUs on Xorg
* hotplug is not supported with most discrete GPU Xorg drivers: the eGPU needs to be plugged in when Xorg starts. Logging out and in again should suffice to restart Xorg.
* hot-unplug is not supported at all: doing so leads to system instability or outright freezes (as acknowledged in the NVIDIA documentation).

## Wayland
Wayland support for eGPUs (or multiple GPUs in general) is much less tested, but should work with even less manual configuration.

Note that there need to be explicit GPU hotplug support by the Wayland compositor, but most already have some level of support:

* KDE's kwin: https://invent.kde.org/plasma/kwin/-/merge_requests/811
* GNOME's Mutter: https://gitlab.gnome.org/GNOME/mutter/-/issues/17, https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1562
* wlroots: https://gitlab.freedesktop.org/wlroots/wlroots/-/issues/1278

For open-source drivers, DRI offloading works fine:

 $ DRI_PRIME=1 some_program

Some projects, such as all-ways-egpu, are trying to provide more efficient methods for GPU selection under Wayland.

## Hotplugging NVIDIA eGPU
It is possible to hotplug eGPU when using Wayland, and use PRIME feature. NVIDIA already has great implementation of PRIME for dGPUs, and it is working same way for eGPU.

First you need to make sure that no program uses NVIDIA modules. EGL programs tend to use 1MB dGPU memory per program, even if they run on iGPU, and it can be seen in . To avoid this, add  as environment variable. Best place for that is .

Then you unload NVIDIA modules:

 # rmmod nvidia_uvm
 # rmmod nvidia_drm
 # rmmod nvidia_modeset
 # rmmod nvidia

When NVIDIA modules is no longer loaded, you can connect external GPU. When GPU is initialized, load NVIDIA modules again with  command or . Naming depends on source of modules, either it is drivers from NVIDIA website or from package manager. In some cases (for example, for GIGABYTE AORUS GAMING BOX) eGPU does not work with proprietary modules, so you might need to load open-source ones: .

When modules successfully loaded, prime feature will work, but since we set  variable to use MESA, we need to add  before starting program. Full string will look like:

 __GLX_VENDOR_LIBRARY_NAME=nvidia __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/10_nvidia.json %command%

For GNOME users, you might need to patch  to include  into list of environment variables. This will allow programs to run on eGPU naturally with right click and "Launch using Dedicated Graphics Card". But this is beyond scope of this article.

## Hotplugging NVIDIA eGPU and temporarily disabling NVIDIA dGPU
In case you have iGPU, NVIDIA dGPU and want to connect NVIDIA eGPU, you will encounter a conflict, where graphics renders only on dGPU, no matter what you do. To solve this, you need to temporarily disable dGPU, so NVIDIA driver will not notice it. Best way to do that is to override its driver.

First, you need to unload NVIDIA driver:

 # rmmod nvidia_uvm
 # rmmod nvidia_drm
 # rmmod nvidia_modeset
 # rmmod nvidia

Then, you need to override dGPU driver with  utility. In this example, 0000:01:00.0 is address of dGPU. It can be found with  utility.

 # driverctl --nosave set-override 0000:01:00.0 vfio-pci

It is important to use  parameter, to prevent driverctl to override driver on boot. It is useful in case something goes wrong, simple reboot cleans everything.

When dGPU is disabled, you can load kernel modules with  and then check if  shows 1 or 2 GPUs.

Bringing dGPU back is tricky, because it is unintuitive. First, unload NVIDIA modules, unplug eGPU and then run this series of commands:

 # modprobe nvidia-current
 # driverctl --nosave unset-override 0000:01:00.0
 # modprobe nvidia-current
 # driverctl --nosave unset-override 0000:01:00.0
 # modprobe nvidia-current-modeset
 # modprobe nvidia-current-drm

It is strange that we need to run first 2 commands twice, but otherwise it will not bring back dGPU. Command will error once, but it is not critical.
