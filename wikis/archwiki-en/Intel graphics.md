# Intel graphics

Since Intel provides and supports open source drivers, Intel graphics are essentially plug-and-play.

For a comprehensive list of Intel GPU models and corresponding chipsets and CPUs, see Wikipedia:Intel Graphics Technology and Gentoo:Intel#Feature support.

## Installation
* Install one of the following packages, which provide the DRI driver for 3D acceleration.
**  is the up-to-date Mesa package which includes the modern Gallium3D drivers for Gen 3 hardware and later. This is the recommended choice.
**  is the legacy Mesa package which includes the classic (non-Gallium3D) drivers from Gen 2 to Gen 11 hardware. This driver might have better performance or stability for Gen 7 and older hardware, but is unmaintained.
* For 32-bit application support, also install the  or  package from the multilib repository.
* For the DDX driver which provides 2D acceleration in Xorg, use one of the following drivers:
** The modesetting driver included in the  package is the recommended choice for Gen 3 hardware and later. It uses the DRI driver for acceleration via glamor.
** The  package provides the legacy intel DDX driver from Gen 2 to Gen 9 hardware. This package is generally not recommended, see note below.
* For Vulkan support (Broadwell and newer; support for earlier chips is incomplete or missing), install the  package. For 32-bit Vulkan support, install the  package.

Also see Hardware video acceleration.

## Loading
The Intel kernel module should load fine automatically on system boot.

If it does not happen, then:

* Make sure you do not have  as a kernel parameter, since Intel requires kernel mode-setting.
* Also, check that you have not disabled Intel by using any modprobe blacklisting within  or .

## Early KMS
Kernel mode setting (KMS) is supported by the  and  drivers, and is enabled early since mkinitcpio v32, as the  hook is included by default. For other setups, see Kernel mode setting#Early KMS start for instructions on how to enable KMS as soon as possible at the boot process.

## Enable GuC / HuC firmware loading
Starting with Gen 9 (Skylake and onwards), Intel GPUs include a Graphics micro (μ) Controller (GuC) which provides the following functionality:
* Offloading some media decoding functionality from the CPU to the HEVC/H.265 micro (µ) Controller (HuC). Only applicable if using  for hardware video acceleration. Introduced with Gen 9.
* Using the GuC for scheduling, context submission, and power management. Introduced with Alder Lake-P (Mobile), within Gen 12.

To use this functionality, first ensure that  is installed, as it provides the GuC and HuC firmware files.

Next, the GuC firmware must be loaded. With regards to HuC support, some video features (e.g. CBR rate control on SKL low-power encoding mode) require loading the HuC firmware as well The new experimental  driver enables Guc and Huc functionality by default.

For the  driver, GuC functionality is controlled by the  kernel module parameter. Its usage is as follows:

{| class="wikitable"
! enable_guc value !! GuC Submission !! HuC Firmware Loading !! Default for platforms !! Supported on platforms
|-
|0 ||  ||  || Tiger Lake, Rocket Lake, and pre-Gen 12 [https://github.com/torvalds/linux/blob/b3454ce0b2c8a56e760e6baa88ed10278585072b/drivers/gpu/drm/i915/gt/uc/intel_uc.c#L26-L36 || All
|-
|1 ||  ||  ||  || Alder Lake-P (Mobile) and newer
|-
|2 ||  ||  || Alder Lake-S (Desktop) [https://lore.kernel.org/all/87ee6wit2r.fsf@intel.com/T/ || Gen 9 and newer
|-
|3 ||  ||  || Alder Lake-P (Mobile) and newer || Gen 9.5 and newer (better for some)
|}

If GuC submission or HuC firmware loading is not enabled by default for your GPU, you can manually enable it.

Set the  kernel module parameter. For example, with:

Regenerate the initramfs, on next boot you can verify both GuC and HuC are enabled by using dmesg:

If they are not supported by your graphics adapter you will see:

Alternatively, check using:

 # less /sys/kernel/debug/dri/*/gt0/uc/guc_info
 # less /sys/kernel/debug/dri/*/gt0/uc/huc_info

## Xorg configuration
There is generally no need for any configuration to run Xorg.

However, to take advantage of some driver options or if Xorg does not start, you can create an Xorg configuration file.

## With the modesetting driver
If you have installed  but want to load the modesetting driver explicitly instead of letting the DDX driver take priority, for example when trying to compare them:

## With the Intel driver
Create an Xorg configuration file similar to the one below:

Additional options are added by the user on new lines below .
For the full list of options, see the  man page.

## AccelMethod
You may need to indicate  when creating a configuration file, the classical options are ,  (default) and .

If you experience issues with default  (e.g. pixelated graphics, corrupt text, etc.), try using  instead, which can be done by adding the following line to your configuration file:

 Option      "AccelMethod"  "uxa"

See the "AccelMethod" option under .

## Using Intel DDX driver with recent GPUs
For Intel GPUs starting from Gen 8 (Broadwell), the Iris Mesa driver is needed:

 Option      "DRI"  "iris"

## Disabling TearFree, TripleBuffer, SwapbuffersWait
If you use a compositor (the default in modern desktop environment like GNOME, KDE Plasma, Xfce, etc.), then TearFree, TripleBuffer and SwapbuffersWait can usually be disabled to improve performance and decrease power consumption.

 Option      "TearFree"        "false"
 Option      "TripleBuffer"    "false"
 Option      "SwapbuffersWait" "false"

## Module-based options
The  kernel module allows for configuration via module options. Some of the module options impact power saving.

A list of all options along with short descriptions and default values can be generated with the following command:

 $ modinfo -p i915

To check which options are currently enabled, run

 # systool -m i915 -av

You will note that many options default to -1, resulting in per-chip powersaving defaults. It is however possible to configure more aggressive powersaving by using module options.

## Framebuffer compression (enable_fbc)
Framebuffer compression (FBC) is a feature that can reduce power consumption and memory bandwidth during screen refreshes.

The feature will be automatically enabled if supported by the hardware. You can use the command below to verify whether it is enabled:

If the parm is set to , you do not need to do anything. Otherwise, to force-enable FBC, use  as kernel parameter or set in :

## Fastboot
The goal of Intel Fastboot is to preserve the frame-buffer as setup by the BIOS or boot loader to avoid any flickering until Xorg has started.To force enable fastboot on platforms where it is not the default already, set  as kernel parameter or set in :

## Intel GVT-g graphics virtualization support
See Intel GVT-g for details.

## Enable performance support
Starting with Gen 6 (Sandy Bridge and onwards), Intel GPUs provide performance counters used for exposing internal performance data to drivers. The drivers and hardware registers refer to this infrastructure as the Observation Architecture (internally "OA") [https://www.phoronix.com/scan.php?page=news_item&px=Intel-HSW-Observation-Arch, but Intel's documentation also more generally refers to this functionality as providing Observability Performance Counters [https://web.archive.org/web/20230321005143/https://01.org/sites/default/files/documentation/intel-gfx-prm-osrc-skl-vol14-observability.pdf.

By default, only programs running with the CAP_SYS_ADMIN (equivalent to root) or CAP_PERFMON capabilities can utilize the observation architecture [https://github.com/torvalds/linux/blob/b14ffae378aa1db993e62b01392e70d1e585fb23/drivers/gpu/drm/i915/i915_perf.c#L3481-L3484. Most applications will be running without either of these, resulting in the following warning:

 MESA-INTEL: warning: Performance support disabled, consider sysctl dev.i915.perf_stream_paranoid=0

To enable performance support without using the capabilities (or root), set the kernel parameter as described in sysctl.

## Tips and tricks
## Setting scaling mode
This can be useful for some full screen applications:

 $ xrandr --output LVDS1 --set PANEL_FITTING param

where  can be:

* : resolution will be kept exactly as defined, no scaling will be made,
* : scale the resolution so it uses the entire screen or
* : scale the resolution to the maximum possible but keep the aspect ratio.

If it does not work, try:

 $ xrandr --output LVDS1 --set "scaling mode" param

where  is one of ,  or .

## Overriding reported OpenGL version
The  environment variable can be used to override the reported OpenGL version to any application. For example, setting  will report OpenGL 4.5.

## Monitoring
See Hardware video acceleration#Verification.

## Setting brightness and gamma
See Backlight.

## Testing the new experimental Xe driver
To try the (experimental) new Xe driver, you need:

*  6.8 or above
* Tiger Lake integrated graphics and newer, or a discrete graphics card.
* .

Note your PCI ID with:

Then add the following to your Kernel parameters with the appropriate PCI ID:

 ... i915.force_probe=!9a49 xe.force_probe=9a49

Make sure you have an alternate solution to boot in order to revert if necessary.

## Troubleshooting
## Tearing
## With the Intel driver
The SNA acceleration method causes tearing on some machines. To fix this, enable the  option in the  driver by adding the following line to your configuration file:

See the original bug report for more info.

## With the modesetting driver
TearFree support was added to the modesetting driver As the last release for the non-XWayland servers was the 21.1 release in 2021, this patch has not reached a stable release, so you will need  until then.

## Disable Vertical Synchronization (VSYNC)
Useful when:

* Chromium/Chrome has lags and slow performance due to GPU and runs smoothly with --disable-gpu switch
* glxgears test does not show desired performance

The intel-driver uses [https://www.intel.com/content/www/us/en/support/articles/000006930/graphics.html Triple Buffering for vertical synchronization; this allows for full performance and avoids tearing. To turn vertical synchronization off (e.g. for benchmarking) use this  in your home directory:

## DRI3 issues
DRI3 is the default DRI version in . On some systems this can cause issues such as this. To switch back to DRI2 add the following line to your configuration file:

 Option "DRI" "2"

For the  driver, this method of disabling DRI3 does not work.  Instead, one can set the environment variable .

## Missing glyphs in GTK applications
Should you experience missing font glyphs in GTK applications, the following workaround might help. Edit  to add the following line:

See also FreeDesktop bug 88584.

## Corrupted and frozen graphics
If you experience corrupted and/or frozen graphics in some applications (such as random colors filling the application window, extreme unreasonable blurriness, an application failing to update its graphics at all while performing other tasks without lag, etc), try running the application with OpenGL instead of Vulkan. This has occurred on some configurations with Intel Arc GPUs.

## X freeze/crash with intel driver
Some issues with X crashing, GPU hanging, or problems with X freezing, can be fixed by disabling the GPU usage with the  option - add the following lines to your configuration file:

   Option "NoAccel" "True"

Alternatively, try to disable the 3D acceleration only with the  option:

   Option "DRI" "False"

## Adding undetected resolutions
This issue is covered on the Xrandr page.

## Backlight is not adjustable
If after resuming from suspend, the hotkeys for changing the screen brightness do not take effect, check your configuration against the Backlight article.

If the problem persists, try one of the following kernel parameters:

 acpi_osi=Linux
 acpi_osi="!Windows 2012"
 acpi_osi=

Also make sure you are not using fastboot mode ( kernel parameter), it is known for breaking backlight controls.

## Corruption or unresponsiveness in Chromium and Firefox
If you experience corruption, unresponsiveness, lags or slow performance in Chromium and/or Firefox some possible solutions are:

* Set the AccelMethod to "uxa"
* Disable VSYNC
* Enable the TearFree option
* Disable "DRI" and acceleration method (tested on Gen 10):

## Kernel crashing w/kernels 4.0+ on Broadwell/Core-M chips
A few seconds after X/Wayland loads the machine will freeze and journalctl will log a kernel crash referencing the Intel graphics as below:

 Jun 16 17:54:03 hostname kernel: BUG: unable to handle kernel NULL pointer dereference at           (null)
 Jun 16 17:54:03 hostname kernel: IP: (null)
 ...
 Jun 16 17:54:03 hostname kernel: CPU: 0 PID: 733 Comm: gnome-shell Tainted: G     U     O    4.0.5-1-ARCH #1
 ...
 Jun 16 17:54:03 hostname kernel: Call Trace:
 Jun 16 17:54:03 hostname kernel:  [ ? i915_gem_object_sync+0xe7/0x190 Jun 16 17:54:03 hostname kernel:  [ intel_execlists_submission+0x294/0x4c0 Jun 16 17:54:03 hostname kernel:  [ i915_gem_do_execbuffer.isra.12+0xabc/0x1230 Jun 16 17:54:03 hostname kernel:  [ ? i915_gem_object_set_to_cpu_domain+0xa9/0x1f0 Jun 16 17:54:03 hostname kernel:  [ ? __kmalloc+0x2e/0x2a0
 Jun 16 17:54:03 hostname kernel:  i915_gem_execbuffer2+0x141/0x2b0 [i915
 Jun 16 17:54:03 hostname kernel:  drm_ioctl+0x1db/0x640 [drm
 Jun 16 17:54:03 hostname kernel:  ? i915_gem_execbuffer+0x450/0x450 [i915
 Jun 16 17:54:03 hostname kernel:  ? eventfd_ctx_read+0x16b/0x200
 Jun 16 17:54:03 hostname kernel:  [ do_vfs_ioctl+0x2c6/0x4d0
 Jun 16 17:54:03 hostname kernel:  ? __fget+0x72/0xb0
 Jun 16 17:54:03 hostname kernel:  [ SyS_ioctl+0x81/0xa0
 Jun 16 17:54:03 hostname kernel:  system_call_fastpath+0x12/0x17
 Jun 16 17:54:03 hostname kernel: Code:  Bad RIP value.
 Jun 16 17:54:03 hostname kernel: RIP  [           (null)

This can be fixed by disabling execlist support which was changed to default on with kernel 4.0. Add the following kernel parameter:

 i915.enable_execlists=0

This is known to be broken to at least kernel 4.0.5.

## Lag in Windows guests
The video output of a Windows guest in VirtualBox sometimes hangs until the host forces a screen update (e.g. by moving the mouse cursor). Removing the  option fixes this issue.

## Screen flickering
Panel Self Refresh (PSR), a power saving feature used by Intel iGPUs is known to cause flickering in some instances   . A temporary solution is to disable this feature using the kernel parameter  or .

This can solve error messages like .

## OpenGL 2.1 with i915 driver
The classic mesa driver for Gen 3 GPUs included in the  package reports OpenGL 2.0 by default, because the hardware is not fully compatible with OpenGL 2.1.OpenGL 2.1 support can be enabled manually by setting  or  options like:

## KMS Issue: console is limited to small area
One of the low-resolution video ports may be enabled on boot which is causing the terminal to utilize a small area of the screen. To fix, explicitly disable the port with an i915 module setting with  in the kernel command line parameter in the boot loader. See Kernel parameters for more info.

If that does not work, try disabling TV1 or VGA1 instead of SVIDEO-1. Video port names can be listed with xrandr.

## No sound through HDMI on a Haswell CPU
According to a [https://bugzilla.kernel.org/show_bug.cgi?id=60769 Linux kernel issue, sound will not be output through HDMI if . To fix this problem, use the following kernel parameter:

 intel_iommu=on,igfx_off

Or alternatively, disable IOMMU:

 intel_iommu=off

## Crash/freeze on low power Intel CPUs
Low-powered Intel processors and/or laptop processors have a tendency to randomly hang or crash due to the problems with the power management features found in low-power Intel chips. If such a crash happens, you will not see any logs reporting this problem. Adding the following Kernel parameters may help to resolve the problem.

 intel_idle.max_cstate=1 i915.enable_dc=0 ahci.mobile_lpm_policy=1

 fixes a hang on several Lenovo laptops and some Acer notebooks due to problematic SATA controller power management. That workaround is strictly not related to Intel graphics but it does solve related issues. Adding this kernel parameter sets the link power management from firmware default to maximum performance and will also solve hangs when you change display brightness on certain Lenovo machines but increases idle power consumption by 1-1.5 W on modern ultrabooks. For further information, especially about the other states, see the Linux kernel mailing list and Red Hat documentation.

 disables GPU power management. This does solve random hangs on certain Intel systems, notably Goldmount and Kaby Lake Refresh chips. Using this parameter does result in higher power use and shorter battery life on laptops/notebooks.  If this helps, you can try finer-grained DC limitations as documented in .

 limits the processors sleep states, it prevents the processor from going into deep sleep states. That is absolutely not ideal and does result in higher power use and lower battery life. However, it does solve random hangs on many Intel systems. Use this if you have a Intel Baytrail or a Kaby Lake Refresh chip. Intel "Baytrail" chips were known to randomly hang without this kernel parameter due to a hardware flaw, theoretically fixed 2019-04-26.
More information about the max_cstate parameter can be found in the kernel documentation and about the cstates in general on a writeup on GitHub.

If you try adding  in the hope of fixing frequent hangs and that solves the issue you should later remove one by one to see which of them actually helped you solve the issue. Running with cstates and display power management disabled is not advisable if the actual problem is related to SATA power management and  is the one that actually solves it.

Check Linux Reviews for more details.

## Higher C-states prevent wakeup from S3
In case you infrequently wake up to a black screen, but the system otherwise properly resumes with  messages in the journal and limiting  reliably prevents that, you can use Suspend and hibernate#Sleep hooks and  to effectively control the C-state around the suspend cycle with  and  to not permanently run the CPU in the lowest C-state.

## Add support for 165Hz monitor
For some 165Hz monitors, xrandr might not display the 165Hz option, and the fix in #Adding undetected resolutions does not solve this. In this case, see i915-driver-stuck-at-40hz-on-165hz-screen.

{{Note|Other than creating , a mkinitcpio hook should be made:

{{hc|/etc/initcpio/install/edid|
#!/bin/bash

build() {
    add_file /lib/firmware/edid/edid.bin
}

help() {
    cat  vbt

 --- vbt
 +++ modified_vbt
 @@ -22,10 +22,10 @@
  00000150  00 08 00 20 00 08 00 10  00 08 00 02 00 08 00 01  |... ............|
  00000160  00 08 00 00 01 08 00 00  00 04 00 00 00 40 00 00  |.............@..|
  00000170  00 20 00 00 00 10 00 00  00 02 00 00 00 01 00 00  |. ..............|
 -00000180  00 00 01 00 00 02 8b 01  02 04 00 00 27 08 00 06  |............'...|
 -00000190  18 00 00 00 00 00 00 00  00 00 00 00 00 0a 00 00  |................|
 +00000180  00 00 01 00 00 02 8b 01  02 04 00 00 27 08 00 00  |............'...|
 +00000190  00 00 00 00 00 00 00 00  00 00 00 00 00 0a 00 00  |................|
  000001a0  03 00 00 00 c0 00 40 00  20 00 00 00 00 00 00 00  |......@. .......|
 -000001b0  00 00 20 00 80 00 06 18  00 00 00 00 00 00 00 00  |.. .............|
 +000001b0  00 00 20 00 80 00 00 00  00 00 00 00 00 00 00 00  |.. .............|
  000001c0  00 00 00 00 07 00 00 00  00 00 00 c0 00 10 00 20  |............... |
  000001d0  00 00 00 00 00 00 00 00  00 20 00 04 00 d2 60 00  |......... ....`.|
  000001e0  10 10 00 23 21 10 00 00  00 00 00 07 00 00 02 00  |...#!...........|

The modified VBT can then be loaded by copying it to  and including the file in the initramfs. For mkinitcpio, the  field in  can be used:

 FILES=(/lib/firmware/i195/modified_vbt)

regenerate the initramfs, and pass the new table to the i915 as a kernel parameter: .

## Washed out colors
By default some monitors might not be recognized properly by the Intel GPU and have washed out colors because it's not in full-range RGB mode.

## Fix colors for Wayland
 to the  configuration. For example:

## Fix colors for X11/Xorg
 # xrandr --output NAME_OF_YOUR_OUTPUT --set "Broadcast RGB" "Full"

## Unable to run some programs, "bus error" with B580
When getting an error like this when running some programs (eg. vainfo, falkon, mpv...):

 1234 bus error : vaapi

The probable cause could be disabled ReBar (Resizable BAR) in BIOS/UEFI. Some motherboards may allow to enable ReBar only when UEFI mode is active, without legacy support.
