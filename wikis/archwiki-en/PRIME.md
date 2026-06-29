# PRIME

PRIME is a technology used to manage hybrid graphics found on recent desktops and laptops (Optimus for NVIDIA, AMD Dynamic Switchable Graphics for Radeon). PRIME GPU offloading and Reverse PRIME are an attempt to support muxless hybrid graphics in the Linux kernel.

## PRIME GPU offloading
We want to render applications on the more powerful card and send the result to the card which has display connected.

The command  can be used to make a render offload provider send its output to the sink provider (the provider which has a display connected). The provider and sink identifiers can be numeric (0x7d, 0x56) or a case-sensitive name (Intel, radeon).

Example:

 $ xrandr --setprovideroffloadsink radeon Intel

You may also use provider index instead of provider name:

 $ xrandr --setprovideroffloadsink 1 0

## For open source drivers—PRIME
To use your discrete card for the applications who need it the most (for example games, 3D modellers...), prepend the  environment variable:

Other applications will still use the less power-hungry integrated card. These settings are lost once the X server restarts, you may want to make a script and auto-run it at the startup of your desktop environment (alternatively, put it in ). This may reduce your battery life and increase heat though.

See Gentoo:AMDGPU#Identifying which graphics card is in use for more information.

For  to work on Vulkan applications  needs to be installed, as well as  for 32 bit applications.

## Note about Windows games
When running Windows DirectX games under Wine or Proton, you need to instruct DXVK directly using the environment variable:

 DXVK_FILTER_DEVICE_NAME="preferred card name"

Get the card name from ; DXVK uses substring match.

## PRIME render offload
NVIDIA driver since version 435.17 supports this method. The modesetting,  (450.57), and  (455.38) are officially supported as iGPU drivers.

To run a program on the NVIDIA card you can use the  script provided by :

 $ prime-run glxinfo | grep "OpenGL renderer"
 $ prime-run vulkaninfo

## PCI-Express Runtime D3 (RTD3) Power Management
## Open-source drivers
Kernel PCI power management turns off the GPU when not used with PRIME offloading or reverse PRIME.
This feature is supported by modesetting, , ,  drivers.

The following command can be used to check current power state of each GPU:
 $ cat /sys/class/drm/card*/device/power_state

## NVIDIA
For Turing generation cards with Intel Coffee Lake or above CPUs as well as some Ryzen CPUs like the 5800H, it is possible to fully [https://us.download.nvidia.com/XFree86/Linux-x86_64/575.64.05/README/dynamicpowermanagement.html power down the GPU when not in use.

The following udev rules are needed, as recommended by NVIDIA:

{{hc|/etc/udev/rules.d/80-nvidia-pm.rules|2=
# Enable runtime PM for NVIDIA VGA/3D controller devices on driver bind
ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="auto"
ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="auto"

# Disable runtime PM for NVIDIA VGA/3D controller devices on driver unbind
ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="on"
ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="on"
}}

Some users also reported that the following additional lines are necessary too:

{{hc|/etc/udev/rules.d/80-nvidia-pm.rules|2=
# Enable runtime PM for NVIDIA VGA/3D controller devices on adding device
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="auto"
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="auto"
}}

Also, add the following module parameters:

Alternatively, you can install  which provides these two configuration files.

After you setup the udev rules and the module parameter either manually or using the AUR package, you will need to restart your Laptop.

To check if the NVIDIA GPU is turned off you can use this command:

 $ cat /sys/bus/pci/devices/0000:01:00.0/power/runtime_status

You will see either  or , if  is displayed, the GPU is turned off. Now the power draw will be 0 Watts, making the battery last longer.

In some cases, such as the NVIDIA RTX A1000, none of the options above might be listed and instead the result will be . This alone does not mean that the GPU is in the  state. In this case you can check the state using this command:

 $ cat /sys/bus/pci/devices/0000:01:00.0/power/runtime_suspended_time

While the GPU is in  state, the counter will be incrementing every time you run the command. When the GPU's state becomes  it will stop incrementing.

If you notice that the  is not incrementing, you can check your D3 Status with this command.

 $ cat /proc/driver/nvidia/gpus/0000:01:00.0/power

If it says , you may need to follow the steps in this forum post to disable. One user noted disabling the  only works on the closed source driver, not on .

To check what uses the GPU, you can use the following command:

 # lsof +c0 /dev/nvidia*

Unlike nvidia-smi, it reports every process using the device, and it doesn't wake up the GPU.

We also need to enable  to avoid the kernel tearing down the device state whenever the NVIDIA device resources are no longer in use. ==== Configure applications to render using GPU ====

Even without enabling Dynamic Power Management, offload rendering of applications is required [https://web.archive.org/web/20211203072304/https://jeansenvaars.wordpress.com/2021/12/02/endeavouros-hybrid-gpu-benchmarks/.

To run an application offloaded to the NVIDIA GPU with Dynamic Power Management enabled, add the following environment variables: __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia command

When using on a Steam game, the launcher command line can be set to:

 __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia %command%

## Desktop environment integration
Install  and enable .

The GNOME, KDE Plasma, Cinnamon, COSMIC and Budgie desktop environments will respect the  property in the desktop entry, and automatically launch apps on the specified GPU.

Alternatively, on GNOME, Cinnamon, and COSMIC, you can launch applications with GPU by right-clicking on the icon and choosing Launch using Discrete Graphics Card (GNOME), Run with dedicated GPU (Cinnamon), and Run with (GPU name) (COSMIC), respectively.

## Troubleshooting
If you have  installed, you should remove it because it blacklists the  driver which is required to load the NVIDIA driver by X server for offloading.

## PRIME synchronization
When using PRIME, the primary GPU renders the screen content / applications, and passes it to the secondary GPU for display. Quoting [https://forums.developer.nvidia.com/t/prime-and-prime-synchronization/44423 an NVIDIA thread, "Traditional vsync can synchronize the rendering of the application with the copy into system memory, but there needs to be an additional mechanism to synchronize the copy into system memory with the iGPU’s display engine. Such a mechanism would have to involve communication between the dGPU’s and the iGPU’s drivers, unlike traditional vsync."

This synchronization is achieved using PRIME sync. To check if PRIME synchronization is enabled for your display, check the output of .

To enable it run:

 $ xrandr --output  --set "PRIME Synchronization" 1

## Reverse PRIME
If the second GPU has outputs that are not accessible by the primary GPU, you can use Reverse PRIME to make use of them. This will involve using the primary GPU to render the images, and then pass them off to the second GPU.

It may work out of the box, however if not, please go through the following steps.

## Configuration
First, identify integrated GPU BusID

In the above example Intel card has  which translates to .

Set up your  as follows and adjust BusID.

Secondary GPUs will be automatically set up as output-sinks and offload-sources thanks to If that doesn't happen, or you'd like to configure it yourself, run  to set the provider as output for the source. For example:

 $ xrandr --listproviders
 Providers: number : 2
 Provider 0: id: 0x48 cap: 0xf, Source Output, Sink Output, Source Offload, Sink Offload crtcs: 4 outputs: 6 associated providers: 1 name:modesetting
 Provider 1: id: 0x257 cap: 0x2, Sink Output crtcs: 4 outputs: 5 associated providers: 1 name:NVIDIA-G0
 $ xrandr --setprovideroutputsource NVIDIA-G0 modesetting

When this is done, the discrete card's outputs should be available in xrandr, and you could do something like:

 $ xrandr --output HDMI-1 --auto --above LVDS1

to configure both internal as well as external displays.

## Known issues
If after reboot you only have one provider, it might be because when Xorg starts, the  module is not loaded yet. You need to enable early module loading. See NVIDIA#Early loading for details.

## Troubleshooting
## XRandR specifies only 1 output provider
Delete/move /etc/X11/xorg.conf file and any other files relating to GPUs in /etc/X11/xorg.conf.d/. Restart the X server after this change.

If the video driver is blacklisted in  or , load the module and restart X. This may be the case if you use the bbswitch module for NVIDIA GPUs.

Another possible problem is that Xorg might try to automatically assign monitors to your second GPU. Check the logs:

To solve this add the ServerLayout section with inactive device to your xorg.conf:

## When an application is rendered with the discrete card, it only renders a black screen
In some cases PRIME needs a composite manager to properly work. If your window manager does not handle compositing, you can use a compositor on top of it.

If you use Xfce, you can go to Menu > Settings > Window Manager Tweaks > Compositor and enable compositing, then try again your application.

## Black screen with GL-based compositors
Currently there are issues with GL-based compositors and PRIME offloading. While Xrender-based compositors (xcompmgr, xfwm, compton's default backend, cairo-compmgr, and a few others) will work without issue, GL-based compositors (Mutter/muffin, Compiz, compton with GLX backend, Kwin's OpenGL backend, etc) will initially show a black screen, as if there was no compositor running. While you can force an image to appear by resizing the offloaded window, this is not a practical solution as it will not work for things such as full screen Wine applications. This means that desktop environments such as GNOME3 and Cinnamon have issues with using PRIME offloading.

Additionally if you are using an Intel IGP you might be able to fix the GL Compositing issue by running the IGP as UXA instead of SNA, however this may cause issues with the offloading process (ie,  may not list the discrete GPU).

For details see [https://bugs.freedesktop.org/show_bug.cgi?id=69101 FDO Bug #69101.

One other way to approach this issue is by enabling DRI3 in the Intel driver. See the below issue for a sample configuration.

## GNOME
You may find that disabling fullscreen undirect allows PRIME offloading to work correctly for full-screen applications.

## Kernel crash/oops when using PRIME and switching windows/workspaces
Using DRI3 WITH a configuration file for the integrated card seems to fix this issue.

To enable DRI3, you need to create a configuration for the integrated card adding the DRI3 option:

 Section "Device"
     Identifier "Intel Graphics"
     Driver "intel"
     Option "DRI" "3"
 EndSection

After this you can use  WITHOUT having to run  as DRI3 will take care of the offloading.

## Glitches/Ghosting synchronization problem on second monitor when using reverse PRIME
This problem can affect users when not using a composite manager, such as with i3. If you experience this problem under Gnome, then a possible fix is to set some environment variables in  [https://bbs.archlinux.org/viewtopic.php?id=177925

 CLUTTER_PAINT=disable-clipped-redraws:disable-culling
 CLUTTER_VBLANK=True

## Error "radeon: Failed to allocate virtual address for buffer:" when launching GL application
This error is given when the power management in the kernel driver is running.
You can overcome this error by appending  to the kernel parameters in the boot loader.

## Constant hangs/freezes with Vulkan applications/games using VSync with closed-source drivers and reverse PRIME
Some Vulkan applications (particularly ones using VK_PRESENT_MODE_FIFO_KHR and/or VK_PRESENT_MODE_FIFO_RELAXED_KHR, including Windows games ran with DXVK) will cause the GPU to lockup constantly (~5-10 seconds freezed, ~1 second working fine)when ran on a system using reverse PRIME.

A GPU lockup will render any input unusable (this includes switching TTYs and using SysRq functions).

There is no known fix for this NVIDIA bug, but a few workarounds exist:
* Turning Vsync off (not possible for some applications)
* Turning PRIME Synchronization[https://devtalk.nvidia.com/default/topic/957814/linux/prime-and-prime-synchronization/ off (will introduce screen tearing):
 xrandr --output HDMI-0 --set "PRIME Synchronization" 0 #replace HDMI-0 with your xrandr output ID

You can verify if your configuration is affected by the issue simply by running  from the  package.

## Some programs have a delay when opening under Wayland
If you have RTD3 working (from #NVIDIA), when using Wayland you will experience some delay when some programs open.
Depending on the application, this can be caused by two sources: Vulkan, or OpenGL, but the mechanism causing the delay is the same.
Both will have to determine which device to defer to. This decision is made based on configuration files.
For OpenGL, the configurations are located in , while for Vulkan they are located in .
The actual delay itself is caused by the determination of a candidate requiring iteration over all potential rendering configurations.
Even if the preferred configuration appears before the other (i.e. has a lower number, igpu before external), it will still iterate through all available options.
While trying the configuration for the sleeping (external) GPU, it is woken up (which it takes ~1 second or more) before deferring to open the program, wasting time and battery life.
This is an NVIDIA driver problem. More details here.

One solution is to make sure the dedicated GPU is not started is to make sure it is not iterated.
This can be done by explicitly setting the configurations as environment variables. These can be passed either directly when running a program, or set globally (for example in your  file). Do note that setting it globally requires you to un-set this variable (or set it to the nvidia files respectively) when deliberately trying to run a program with the external GPU.

## Error when running Wine games with DXVK
When using PRIME offload, encountering the  is a known problem. The only known workaround is to start X session entirely on NVIDIA GPU. A user friendly way to switching between NVIDIA only and PRIME offload method is the optimus-manager utility or write some automation scripts yourself.

## Vulkan/OpenGL applications segfault on Wayland
 requires Kernel modesetting. If you are using a Wayland compositor and unable to start applications on the dGPU without having to force them to run under Xwayland, make sure modesetting is enabled.

This means removing  from Kernel parameters if present.
