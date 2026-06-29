# Bumblebee

From Bumblebee's FAQ:

:Bumblebee is an effort to make NVIDIA Optimus enabled laptops work in GNU/Linux systems. Such feature involves two graphics cards with two different power consumption profiles plugged in a layered way sharing a single framebuffer.

## Bumblebee: Optimus for Linux
Optimus Technology is a hybrid graphics implementation without a hardware multiplexer. The integrated GPU manages the display while the dedicated GPU manages the most demanding rendering and ships the work to the integrated GPU to be displayed. When the laptop is running on battery supply, the dedicated GPU is turned off to save power and prolong the battery life. It has also been tested successfully with desktop machines with Intel integrated graphics and an NVIDIA dedicated graphics card.

Bumblebee is a software implementation comprising two parts:

* Render programs off-screen on the dedicated video card and display it on the screen using the integrated video card. This bridge is provided by VirtualGL or primus (read further) and connects to a X server started for the discrete video card.
* Disable the dedicated video card when it is not in use (see the #Power management section)

It tries to mimic the Optimus technology behavior; using the dedicated GPU for rendering when needed and power it down when not in use. The present releases only support rendering on-demand, automatically starting a program with the discrete video card based on workload is not implemented.

## Installation
Before installing Bumblebee, check your BIOS and activate Optimus (older laptops call it "switchable graphics") if possible (BIOS does not have to provide this option). If neither "Optimus" or "switchable" is in the BIOS, still make sure both GPUs will be enabled and that the integrated graphics (igfx) is initial display (primary display). The display should be connected to the onboard integrated graphics, not the discrete graphics card. If integrated graphics had previously been disabled and discrete graphics drivers installed, be sure to remove  or the conf file in  related to the discrete graphics card.

Install:

*  - The main package providing the daemon and client programs.
*  - An open-source implementation of the OpenGL specification.
* An appropriate version of the NVIDIA driver, see NVIDIA#Installation.
* Optionally install  - Intel Xorg driver.

For 32-bit application support, enable the multilib repository and install:

*  - A render/display bridge for 32 bit applications.
*  or  (match the version of the regular NVIDIA driver).

In order to use Bumblebee, it is necessary to add your regular user to the  group:

 # gpasswd -a user bumblebee

Also enable . Reboot your system and follow #Usage.

## Usage
## Test
Install  and use  to test if Bumblebee works with your Optimus system:

 $ optirun glxgears -info

If it fails, try the following command (from ):

 $ optirun glxspheres64

If the window with animation shows up, Optimus with Bumblebee is working.

## General usage
 $ optirun application [application-parameters

For example, start Windows applications with Optimus:

 $ optirun wine application.exe

For another example, open NVIDIA Settings panel with Optimus:

 $ optirun -b none nvidia-settings -c :8

For a list of all available options, see .

## Configuration
You can configure the behaviour of Bumblebee to fit your needs. Fine tuning like speed optimization, power management and other stuff can be configured in

## Optimizing speed
One disadvantage of the offscreen rendering methods is performance. The following table gives a raw overview of a Lenovo ThinkPad T480 in an eGPU setup with NVIDIA GTX 1060 6GB and  benchmark (1920x1080, max settings, 8x AA):

{| class="wikitable"
! Command !! Display !! FPS !! Score !! Min FPS !! Max FPS
|-
| optirun unigine-heaven || internal || 20.7 || 521 || 6.9 || 26.6
|-
| primusrun unigine-heaven || internal || 36.9 || 930 || 15.3 || 44.1
|-
| unigine-heaven || internal in Nvidia-xrun || 51.3 || 1293 || 8.4 || 95.6
|-
| unigine-heaven || external in Nvidia-xrun || 56.1 || 1414 || 8.4 || 111.9
|}

## Using VirtualGL as bridge
Bumblebee renders frames for your Optimus NVIDIA card in an invisible X Server with VirtualGL and transports them back to your visible X Server. Frames will be compressed before they are transported - this saves bandwidth and can be used for speed-up optimization of bumblebee:

To use another compression method for a single application:

 $ optirun -c compress-method application

The method of compress will affect performance in the GPU/CPU usage. Compressed methods will mostly load the CPU. However, uncompressed methods will mostly load the GPU.

Compressed methods:

:*
:*
:*

Uncompressed methods:

:*
:*

Here is a performance table tested with ASUS N550JV laptop and benchmark app :

{| class="wikitable"
! Command !! FPS !! Score !! Min FPS !! Max FPS
|-
| optirun unigine-heaven || 25.0 || 630 || 16.4 || 36.1
|-
| optirun -c jpeg unigine-heaven || 24.2 || 610 || 9.5 || 36.8
|-
| optirun -c rgb unigine-heaven || 25.1 || 632 || 16.6 || 35.5
|-
| optirun -c yuv unigine-heaven || 24.9 || 626 || 16.5 || 35.8
|-
| optirun -c proxy unigine-heaven || 25.0 || 629 || 16.0 || 36.1
|-
| optirun -c xv unigine-heaven || 22.9 || 577 || 15.4 || 32.2
|}

To use a standard compression for all applications, set the  to  in :

You can also play with the way VirtualGL reads back the pixels from your graphics card. Setting  environment variable to  should increase the performance. Compare the following:

PBO should be faster:

 VGL_READBACK=pbo optirun glxgears

The default value is sync:

 VGL_READBACK=sync optirun glxgears

## Primusrun
primusrun (from ) is becoming the default choice, because it consumes less power and sometimes provides better performance than /. It may be run separately, but it does not accept options as  does. Setting  as the bridge for  provides more flexibility.

For 32-bit applications support on 64-bit machines, install  (multilib must be enabled).

You can either run it separately:

 $ primusrun glxgears

Or as a bridge for optirun. The default configuration sets  as the bridge. Override that on the command line:

 $ optirun -b primus glxgears

Alternatively, set  in  and you will not have to specify it on the command line.

## Pvkrun
 from the package  is a drop-in replacement for  that enables to run Vulkan-based applications. A quick check can be done with  from .

 $ pvkrun vulkaninfo

## Power management
The goal of the power management feature is to turn off the NVIDIA card when it is not used by Bumblebee any more. If  (for ) or  (for  or custom kernels) is installed, it will be detected automatically when the Bumblebee daemon starts. No additional configuration is necessary. However,  is for Optimus laptops only and will not work on desktop computers. So, Bumblebee power management is not available for desktop computers, and there is no reason to install  on a desktop. (Nevertheless, the other features of Bumblebee do work on some desktop computers.)

To manually turn the card on or off using bbswitch, write into /proc/acpi/bbswitch:

 # echo OFF > /proc/acpi/bbswitch
 # echo ON > /proc/acpi/bbswitch

## Default power state of NVIDIA card using bbswitch
The default behavior of bbswitch is to leave the card power state unchanged.  does disable the card when started, so the following is only necessary if you use bbswitch without bumblebeed.

Set  and  kernel module parameters according to your needs (see bbswitch documentation).

To run bbswitch without bumblebeed on system startup, do not forget to add  to , as explained in Kernel module#systemd.

## Enable NVIDIA card during shutdown
On some laptops, the NVIDIA card may not correctly initialize during boot if the card was powered off when the system was last shutdown. Therefore the Bumblebee daemon will power on the GPU when stopping the daemon (e.g. on shutdown) due to the (default) setting  in . Note that this setting does not influence power state while the daemon is running, so if all  or  programs have exited, the GPU will still be powered off.

When you stop the daemon manually, you might want to keep the card powered off while still powering it on on shutdown. To achieve the latter, add the following systemd service (if using ):

Then enable the  unit.

## Enable NVIDIA card after waking from suspend
The bumblebee daemon may fail to activate the graphics card after suspending. A possible fix involves setting  as the default method for power management:

If the above fix fails, try the following command:

 # echo 1 > /sys/bus/pci/rescan

To rescan the PCI bus automatically after a suspend, create a script as described in Power management/Suspend and hibernate#Hooks in /usr/lib/systemd/system-sleep.

## Multiple monitors
## Outputs wired to the Intel chip
If the port (DisplayPort/HDMI/VGA) is wired to the Intel chip, you can set up multiple monitors with xorg.conf. Set them to use the Intel card, but Bumblebee can still use the NVIDIA card. One example configuration is below for two identical screens with 1080p resolution and using the HDMI out.

You need to probably change the BusID for both the Intel and the NVIDIA card.

The BusID is 0:2:0. Note that lspci outputs hexadecimal values, but Xorg expects decimal values.

## Output wired to the NVIDIA chip
On some notebooks, the digital Video Output (HDMI or DisplayPort) is hardwired to the NVIDIA chip. If you want to use all the displays on such a system simultaneously, the easiest solution is to use intel-virtual-output, a tool provided in the  driver set, as of v2.99. It will allow you to extend the existing X session onto other screens, leveraging virtual outputs to work with the discrete graphics card. Usage is as follows:

If this command alone does not work, you can try running it with optirun to enable the discrete graphics and allow it to detect the outputs accordingly. This is known to be necessary on Lenovo's Legion Y720.

 $ optirun intel-virtual-output

If no target displays are parsed on the commandline, intel-virtual-output will attempt to connect to any local display. The detected displays will be manageable via any desktop display manager such as xrandr or KDE Display. The tool will also start bumblebee (which may be left as default install). See the Bumblebee wiki page for more information.

When run in a terminal, intel-virtual-output will daemonize itself unless the  switch is used. Games can be run on the external screen by first exporting the display , and then running the game with , however, cursor and keyboard are not fully captured. Use  to revert back to standard operation.

If intel-virtual-output does not detect displays, or if a  message is obtained, then create:

which does exist by default, and:

See for further configurations to try. If the laptop screen is stretched and the cursor is misplaced while the external monitor shows only the cursor, try killing any running compositing managers.

If you do not want to use intel-virtual-output, another option is to configure Bumblebee to leave the discrete GPU on and directly configure X to use both the screens, as it will be able to detect them.

As a last resort, you can run 2 X Servers. The first will be using the Intel driver for the notebook's screen. The second will be started through optirun on the NVIDIA card, to show on the external display. Make sure to disable any display/session manager before manually starting your desktop environment with optirun. Then, you can log in the integrated-graphics powered one.

## Disabling screen blanking
You can disable screen blanking when using intel-virtual-output with  by setting the  environment variable appropriately (see DPMS for more info):

 $ DISPLAY=:8 xset -dpms s off

## Multiple NVIDIA graphics cards or NVIDIA Optimus
If you have multiple NVIDIA graphics cards (eg. when using an eGPU with a laptop with another built in NVIDIA graphics card) or NVIDIA Optimus, you need to make a minor edit to . If this change is not made the daemon may default to using the internal NVIDIA card.

First, determine the BusID of the external card:

In this case, the BusID is .

Now edit  and add the following line to :

## Troubleshooting
## [VGL ERROR: Could not open display :8
There is a known problem with some wine applications that fork and kill the parent process without keeping track of it (for example the free to play online game "Runes of Magic").

This is a known problem with VirtualGL. As of bumblebee 3.1, so long as you have it installed, you can use Primus as your render bridge:

 $ optirun -b primus wine windows program.exe

If this does not work, an alternative walkaround for this problem is:

 $ optirun bash
 $ optirun wine windows program.exe

If using NVIDIA drivers a fix for this problem is to edit  and change Option  to .

## Xlib: extension "GLX" missing on display ":0.0"
If you tried to install the NVIDIA driver from NVIDIA website, this is not going to work.

# Uninstall that driver in the similar way:
# Remove the Xorg configuration file generated by NVIDIA:
# (Re)install the correct NVIDIA driver: See #Installation.

## access secondary GPU: No devices detected
In some instances, running  will return:

 [ERRORCannot access secondary GPU - error: (EE) No devices detected.
 [ERRORAborting because fallback start is disabled.

In this case, you will need to move the file  to somewhere else, restart the bumblebeed daemon and it should work. If you do need to change some features for the Intel module, a workaround is to merge  to .

It could be also necessary to comment the driver line in .

If you are using the nouveau driver you could try switching to the NVIDIA driver.

You might need to define the NVIDIA card somewhere (e.g. file ), using the correct  according to  output:

Observe that the format of  output is in HEX, while in xorg it is in decimals. So if the output of  is, for example,  the  should be .

## NVIDIA(0): Failed to assign any connected display devices to X screen 0
If the console output is:

 access secondary GPU - error: [XORG (EE) NVIDIA(0): Failed to assign any connected display devices to X screen 0
 because fallback start is disabled.

If the following line in  does not exist, you can add it to the "Device" section:

 Option "ConnectedMonitor" "DFP"

If it does already exist, you can try changing it to:

 Option "ConnectedMonitor" "CRT"

After that, restart the Bumblebee service to apply these changes.

## Failed to initialize the NVIDIA GPU at PCI:1:0:0 (GPU fallen off the bus / RmInitAdapter failed!)
Add  to the kernel parameters of the boot loader configuration (see also the original [https://bbs.archlinux.org/viewtopic.php?id=169742 BBS post for a configuration example).

## Failed to initialize the NVIDIA GPU at PCI:1:0:0 (Bumblebee daemon reported: error: (EE) NVIDIA(GPU-0))
You might encounter an issue when after resume from sleep,  or  command does not work anymore. there are two ways to fix this issue - reboot your system or execute the following command:

 # echo 1 > /sys/bus/pci/rescan

And try to test if  or  works.

If the above command did not help, try finding your NVIDIA card's bus ID:

For example, above command showed  so we use following commands with this bus ID:

 # echo 1 > /sys/bus/pci/devices/0000:01:00.0/remove
 # echo 1 > /sys/bus/pci/rescan

## Could not load GPU driver
If the console output is:

 [ERRORCannot access secondary GPU - error: Could not load GPU driver

and if you try to load the nvidia module:

This could be because the nvidia driver is out of sync with the Linux kernel, for example if you installed the latest NVIDIA driver and have not updated the kernel in a while. A full system update , followed by a reboot into the updated kernel.

## NOUVEAU(0): failed to set drm interface version
Consider switching to the official NVIDIA driver. As commented [https://github.com/Bumblebee-Project/Bumblebee/issues/438#issuecomment-22005923 upstream, the nouveau driver has some issues with some cards and bumblebee.

## access secondary GPU - error: X did not start properly
Set the  option to  in  (see [https://github.com/Bumblebee-Project/Bumblebee/issues/88 here):

## /dev/dri/card0: failed to set DRM interface version 1.4: Permission denied
This could be worked around by appending following lines in  (see here):

## ERROR: ld.so: object 'libdlfaker.so' from LD_PRELOAD cannot be preloaded: ignored
You probably want to start a 32-bit application with bumblebee on a 64-bit system. See the "For 32-bit..." section in #Installation. If the problem persists or if it is a 64-bit application, try using the primus bridge.

## Fatal IO error 11 (Resource temporarily unavailable) on X server
Change  in  from  to . Your program forks into background and bumblebee do not know anything about it.

## Video tearing
Video tearing is a somewhat common problem on Bumblebee. To fix it, you need to enable vsync. It should be enabled by default on the Intel card, but verify that from Xorg logs. To check whether or not it is enabled for NVIDIA, make sure  is installed and run:

 $ optirun nvidia-settings -c :8

 and  should both be enabled. The Intel card has in general less tearing, so use it for video playback. Especially use VA-API for video decoding (e.g.  and with  parameter).

Refer to Intel graphics#Tearing on how to fix tearing on the Intel card.

If it is still not fixed, try to disable compositing from your desktop environment. Try also disabling triple buffering.

## Bumblebee cannot connect to socket
You might get something like:

 $ optirun glxspheres64

or (for 32 bit):

If you are already in the  group (), you may try removing the socket .

Another reason for this error could be that you have not actually turned on both GPUs in your BIOS, and as a result, the Bumblebee daemon is in fact not running. Check the BIOS settings carefully and be sure Intel graphics (integrated graphics - may be abbreviated in BIOS as something like igfx) has been enabled or set to auto, and that it is the primary GPU. Your display should be connected to the onboard integrated graphics, not the discrete graphics card.

If you mistakenly had the display connected to the discrete graphics card and Intel graphics was disabled, you probably installed Bumblebee after first trying to run NVIDIA alone. In this case, be sure to remove the  or  configuration files. If Xorg is instructed to use NVIDIA in a configuration file, X will fail.

## Running X.org from console after login (rootless X.org)
See Xorg#Rootless Xorg.

## Using Primus causes a segmentation fault
In some instances, using primusrun instead of optirun will result in a segfault. This is caused by an issue in code auto-detecting faster upload method, see .

The workaround is skipping auto-detection by manually setting  environment variable to either 1 or 2, depending on which one is faster on your setup.

 $ PRIMUS_UPLOAD=1 primusrun ...

## Primusrun mouse delay (disable VSYNC)
For ,  is enabled by default and as a result, it could make mouse input delay lag or even slightly decrease performance. Test  with  disabled:

 $ vblank_mode=0 primusrun glxgears

If you are satisfied with the above setting, create an alias (e.g. ).

Performance comparison:

{| class="wikitable"
! VSYNC enabled !! FPS !! Score !! Min FPS !! Max FPS
|-
| FALSE || 31.5 || 793 || 22.3 || 54.8
|-
| TRUE || 31.4 || 792 || 18.7 || 54.2
|}

Tested with ASUS N550JV notebook and benchmark app .

## Primus issues under compositing window managers
Since compositing hurts performance, invoking primus when a compositing WM is active is not recommended.If you need to use primus with compositing and see flickering or bad performance, synchronizing primus' display thread with the application's rendering thread may help:

 $ PRIMUS_SYNC=1 primusrun ...

This makes primus display the previously rendered frame.

## Problems with bumblebee after resuming from standby
In some systems, it can happens that the  module is loaded after resuming from standby.
One possible solution for this is to install the  and  package.

## Optirun does not work, no debug output
Users are reporting that in some cases, even though Bumblebee was installed correctly, running

 $ optirun glxgears -info

gives no output at all, and the glxgears window does not appear. Any programs that need 3d acceleration crashes:

 $ optirun bash
 $ glxgears
 Segmentation fault (core dumped)

Apparently it is a bug of some versions of virtualgl. So a workaround is to use #Primusrun instead.
See [https://bbs.archlinux.org/viewtopic.php?pid=1643609 this forum post for more information.

## Broken power management with kernel 4.8
If you have a newer laptop (BIOS date 2015 or newer), then Linux 4.8 might break bbswitch (bbswitch issue 140) since bbswitch does not support the newer, recommended power management method. As a result, the GPU may fail to power on, fail to power off or worse.

As a workaround, add  to your Kernel parameters.

Alternatively, if you are only interested in power saving (and perhaps use of external monitors), remove bbswitch and rely on Nouveau runtime power-management (which supports the new method).

## Lockup issue (lspci hangs)
See NVIDIA Optimus#Lockup issue (lspci hangs) for an issue that affects new laptops with a GTX 965M (or alike).

## Discrete card always on and acpi warnings
Add  to your Kernel parameters.
See and [https://github.com/Bumblebee-Project/bbswitch/issues/112 for more information.

## Screen 0 deleted because of no matching config section
Modify the configuration as follows:

## Erratic, unpredictable behaviour
If Bumblebee starts/works in a random manner, check that you have set your Network configuration#Local network hostname resolution (details here).

## Discrete card always on and NVIDIA driver cannot be unloaded
Make sure  is disabled and not currently active. It is intended to keep the NVIDIA driver running at all times which prevents the card being turned off.

## Discrete card is silently activated when EGL is requested by some application
If the discrete card is activated by some program (e.g.  with its GPU backend), it might stays on.
The problem might be  which is loading the NVIDIA drivers and activating the card.

To disable this set environment variable  (see [https://github.com/NVIDIA/libglvnd/blob/master/src/EGL/icd_enumeration.md documentation) to only load mesa configuration file:

 __EGL_VENDOR_LIBRARY_FILENAMES="/usr/share/glvnd/egl_vendor.d/50_mesa.json"

 (and its branches) is installing the configuration file at  which has priority and causes libglvnd to load the NVIDIA drivers and enable the card.

The other solution is to avoid installing the configuration file provided by .

## Framerate drops to 1 FPS after a fixed period of time
With the NVIDIA 440.36 driver, the DPMS setting is enabled by default resulting in a timeout after a fixed period of time (e.g. 10 minutes) which causes the frame rate to throttle down to 1 FPS. To work around this, add the following line to the "Device" section in

## Application cannot record screen
Using Bumblebee, applications cannot access the screen to identify and record it. This happens, for example, using  with NVENC activated. To solve this, disable the bridging mode with .
