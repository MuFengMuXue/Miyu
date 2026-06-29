# NVIDIA Optimus

NVIDIA Optimus is a technology that allows an integrated GPU and discrete NVIDIA GPU to be built into and accessed by a laptop. As a prerequisite, install the relevant GPU driver for both cards.

## Available methods
There are several methods available:

* #Use integrated graphics only - saves power, because NVIDIA GPU will be completely powered off.
* #Use NVIDIA graphics only - gives more performance than integrated graphics, but drains more battery (which is not welcome for mobile devices). This utilizes the same underlying process as the optimus-manager and nvidia-xrun options, it should be utilized for troubleshooting and verifying general functionality, before opting for one of the more automated approaches.
* Using both (use NVIDIA GPU when needed and keep it powered off to save power):
** #Using PRIME render offload - official method supported by NVIDIA.
** #Using switcheroo-control - Similar to PRIME render offload, but has desktop environment integration, and also works with AMD and Intel GPUs. Allows applications to specify if they prefer the dedicated GPU in their desktop entry file, and lets you manually run any application on the dedicated GPU from the right-click menu.
** #Using optimus-manager - switches graphics with a single command (logout and login required to take effect). Also supports hybrid mode with PRIME render offload. It achieves maximum performance out of NVIDIA GPU and switches it off if not in use. Since the 1.4 release AMD+NVIDIA combination is also supported.
** #Using nvidia-xrun - run separate X session on different TTY with NVIDIA graphics. It achieves maximum performance out of NVIDIA GPU and switches it off if not in use.
** #Using Bumblebee - provides Windows-like functionality by allowing to run selected applications with NVIDIA graphics while using Intel graphics for everything else. Has significant performance issues.
** #Using nouveau - offers poorer performance (compared to the proprietary NVIDIA driver) and may cause issues with sleep and hibernate. Does not work with latest NVIDIA GPUs.
** #Using EnvyControl - Similar to optimus-manager but does not require extensive configuration or having a daemon running in the background as well as having to install a patched version of GDM if you are a GNOME user.
** #Using NVidia-eXec - Similar to Bumblebee, but without the performance impact. It works on both Xorg and Wayland. This package is experimental, and is currently being tested only under GNOME/GDM.
** #Using nvidia-switch - Similar to nvidia-xrun, but not needing to change TTY, the switches will be done by login and logouts in your display manager. This package is being tested on Debian based system, but, like nvidia-xrun, it must work in all Linux systems.

## Use integrated graphics only
If you only care to use a certain GPU without switching, check the options in your system's BIOS. There should be an option to disable one of the cards. Some laptops only allow disabling of the discrete card, or vice-versa, but it is worth checking if you only plan to use just one of the cards.

If your BIOS does not allow to disable Nvidia graphics, you can disable it from the Linux kernel itself. See Hybrid graphics#Fully power down discrete GPU.

## Use CUDA without switching the rendering provider
You can use CUDA without switching rendering to the Nvidia graphics. All you need to do is ensure that the Nvidia card is powered on before starting a CUDA application, see Hybrid graphics#Fully power down discrete GPU for details.

Now when you start a CUDA application, it will automatically load all necessary kernel modules. Before turning off the Nvidia card after using CUDA, the  kernel modules have to be unloaded first:

 # rmmod nvidia_uvm
 # rmmod nvidia

## Use NVIDIA graphics only
The proprietary NVIDIA driver can be configured to be the primary rendering provider. It also has notable screen-tearing issues unless you enable prime sync by enabling NVIDIA#DRM kernel mode setting, see for further information. It does allow use of the discrete GPU and has (as of [https://www.phoronix.com/scan.php?page=article&item=nouveau-410-blob&num=1 January 2017) a marked edge in performance over the nouveau driver.

First, install the NVIDIA driver and . Then, configure  the options of which will be combined with the package provided  to provide compatibility with this setup.

Next, add the following two lines to the beginning of your :

Now reboot to load the drivers, and X should start.

If your display dpi is not correct add the following line:

 xrandr --dpi 96

If you get a black screen when starting X, make sure that there are no ampersands after the two  commands in . If there are ampersands, it seems that the window manager can run before the  commands finish executing, leading to a black screen.

## Display managers
If you are using a display manager then you will need to create or edit a display setup script for your display manager instead of using .

## LightDM
For the LightDM display manager:

Make the script executable.

Now configure lightdm to run the script by editing the  section in :

Now reboot and your display manager should start.

## SDDM
For the SDDM display manager (SDDM is the default DM for KDE):

## GDM
For the GDM display manager create two new .desktop files:

Make sure that GDM use X as default backend.

## Checking 3D
You can check if the NVIDIA graphics are being used by installing  and running

 $ glxinfo | grep NVIDIA

## Further information
For more information, look at NVIDIA's official page on the topic == Use switchable graphics ==

## Using PRIME render offload
This is the official NVIDIA method to support switchable graphics.

See PRIME#PRIME render offload for details.

## Using switcheroo-control
See PRIME#Desktop environment integration.

## Using optimus-manager
See [https://github.com/Askannz/optimus-manager Optimus-manager upstream documentation. It covers both installation and configuration in Arch Linux systems.

## Using nvidia-xrun
See nvidia-xrun.

## Using Bumblebee
See Bumblebee.

## Using nouveau
See PRIME for graphics switching and nouveau for open-source NVIDIA driver.

## Using EnvyControl
See EnvyControl upstream documentation. It covers both installation and usage instructions.

## Using NVidia-eXec
See NVidia-eXec upstream documentation. It covers both installation and usage instructions.

## Using nvidia-switch
See nvidia-switch upstream documentation. It covers both installation and usage instructions.

## Troubleshooting
## Tearing/Broken VSync
Enable DRM kernel mode setting, which will in turn enable the PRIME synchronization and fix the tearing.

You can read the official forum thread for details.

## Failed to initialize the NVIDIA GPU at PCI:1:0:0 (GPU fallen off the bus / RmInitAdapter failed!)
Add  to the kernel parameters. Original topic can be found in and [https://bbs.archlinux.org/viewtopic.php?id=169742.

## Resolution, screen scan wrong. EDID errors in Xorg.log
This is due to the NVIDIA driver not detecting the EDID for the display. You need to manually specify the path to an EDID file or provide the same information in a similar way.

To provide the path to the EDID file edit the Device Section for the NVIDIA card in Xorg.conf, adding these lines and changing parts to reflect your own system:

If Xorg will not start try swapping out all references of CRT to DFB.
 is the identifier for the Intel card to which the display is connected via LVDS. The edid binary is in this directory. If the hardware arrangement is different, the value for CustomEDID might vary but yet this has to be confirmed. The path will start in any case with .

Alternatively you can generate your edid with tools like  and point the driver to this file. Even modelines can be used, but then be sure to change  and .

## Wrong resolution without EDID errors
Using nvidia-xconfig, incorrect information might be generated in  and in particular wrong monitor refresh rates that restrict the possible resolutions. Try commenting out the / lines. If this helps, you can probably also remove everything else not mentioned in this article.

## Lockup issue (lspci hangs)
Symptoms: lspci hangs, system suspend fails, shutdown hangs, optirun hangs.

Applies to: newer laptops with GTX 965M or alike when bbswitch (e.g. via Bumblebee) or nouveau is in use.

When the dGPU power resource is turned on, it may fail to do so and hang in ACPI code (kernel bug 156341).

When using nouveau, disabling runtime power-management stops it from changing the power state, thus avoiding this issue.
To disable runtime power-management, add  to the kernel parameters.

For known model-specific workarounds, see this issue.
In other cases you can try to boot with  or  added to your Kernel parameters. (Consider reporting your laptop to that issue.)

## No screens found on a laptop/NVIDIA Optimus
Check if the output is something similar to:

NVIDIA drivers now offer Optimus support since 319.12 Beta with kernels above and including 3.9.

Another solution is to install the Intel driver to handle the screens, then if you want 3D software you should run them through Bumblebee to tell them to use the NVIDIA card.

## Random freezes "(EE) NVIDIA(GPU-0): WAIT"
Using the proprietary drivers on a setup with an integrated AMD card and with the dedicated NVIDIA card set as the only one in use, users report freezes for up to 10 seconds, with the following errors in the Xorg logs:

 [   219.796 (EE) NVIDIA(GPU-0): WAIT (2, 8, 0x8000, 0x0002e1c4, 0x0002e1cc)
 [   226.796] (EE) NVIDIA(GPU-0): WAIT (1, 8, 0x8000, 0x0002e1c4, 0x0002e1cc)

While this is not root-caused yet, it seems linked to a conflict in how the integrated and dedicated cards interact with Xorg.

The workaround is to use switchable graphics, see PRIME#PRIME render offload for details.

## "No Devices detected" with optimus-manager
There are cases where lspci will show the PCI domain as first output column, making optimus-manager generated files break while trying to map  on multiple laptop models.

If you face a black screen that never ends to load your GUI, GUI partially loading with console artifacts or Xorg crashing with , the workaround and bug reports are available at the upstream GitHub.

## Xorg: external monitor updates only when the mouse is moving
A workaround for the issue is to uninstall the Xorg driver of the iGPU (e.g.  or ) This should work as long as the external monitor port (HDMI/DP/USB-C) is connected directly to the Nvidia dGPU.

## Low power usage (TDP)
Since the 530.41 driver version, cases of cards locked at low power consumption limits appeared (see [https://github.com/NVIDIA/open-gpu-kernel-modules/issues/483 GitHub issue 483). The NVIDIA driver has disabled the ability to manually set the power limit using  command, so many laptops are stuck with low power usage and bad performance.

To workaround this problem (for the Ampere generation or newer), see NVIDIA/Tips and tricks#Dynamic Boost.

## NVIDIA GPU will not turn off or stay deactivated
Some processes may keep your NVIDIA GPU on due to their way of interacting with the GPU. This causes significantly increased power usage, lower battery life, and higher temperatures.

You can check if your GPU is in an active state or suspended by running the following command:

 $ cat /sys/bus/pci/devices/0000\:01\:00.0/power/runtime_status

If the state is , you are probably running a process that keeps your GPU alive.

If you use a thermal monitor that is probing your GPU temperature, it typically calls  to get this temperature, which will wake up your GPU and keep it in an active state.

You can use  to check if a process (such as Xorg) is using the NVIDIA GPU, but this method does not work in all cases. For example, if you have a Ollama server running, it will always keep your GPU on but will not show in  or invoke .

Remember to check the articles related to your specific chosen method for troubleshooting as well.
