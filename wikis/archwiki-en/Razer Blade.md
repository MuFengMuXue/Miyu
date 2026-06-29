# Razer Blade

Razer Blade is Razer's line of gaming laptops. As of 2018, the lineup consists of a 13" model (Razer Blade Stealth), 15" model (Razer Blade), and a 17" model (Razer Blade Pro). It is known to have very limited bios feature and limited Linux stability.

Due to the proprietary SBUI trackpad on the 17" model, it will be extremely difficult to get it to work without extensive USB protocol reversing.

## Installation
Before uninstalling Windows, make sure to update the bios. It is easier to install the Razer drivers with Windows. You can find updates on the support page related to your model.

If you are for some reason unable to boot into Windows to perform the update, there is still a patch that you can apply to your kernel build to get things working. However, this will unlikely be maintained due to the availability of the BIOS patch.

The normal installation process works in general with the exceptions enumerated below.

## Touchpad
Install the  package: this is also the only one that will enable natural scrolling. See libinput for more information on this driver.

Alternatively, if you prefer using the Touchpad Synaptics driver, install the  package.

If you have issues with the touchpad not working after resuming from sleep, restarting the module i2c_hid seems to work.

In the 2013 version, the touchpad works only on Linux 4.0+ without libinput-based X.Org input driver (xf86-input-libinput) thanks to Andrew Duggan's work.

In the 2018 version, the touchpad works with the vanilla kernel with BIOS version 1.05.

In the 2019 version, the touchpad works with the vanilla kernel and BIOS version 1.02.

## Touchscreen
While the touchscreen will provide basic functionality out of the box, it is best to use  to configure multitouch gestures. These include two-finger scrolling, right-click, etc.

## Graphics drivers
The graphics card works OK with the standard Intel drivers which you can install with the  package. See Intel graphics for more information on installation and configuration.

Issues with screen flickering seem to be resolved by changing AccelMethod to uxa as described in the SNA issues section.

If you experience screen tearing while scrolling, add the following line to the configuration above:  and set the "AccelMethod" to "sna" and comment out "uxa".

If you have an Intel Kaby Lake chip Wikipedia:Kaby Lake, and the issue is not fixed with the configuration above, add to  to the kernel parameters.

## Hybrid graphics
If the discrete NVIDIA GPU is switched off before starting Xorg or Wayland, then the system freezes. The only possible solution is to manually disable/enable the discrete card after starting the graphical session. However, there is an ACPI DSDT fix available which fixes this problem. Check the repository and DSDT for more information.

If you experience very poor battery life compared to Windows, even after implementing Powertop, TPL and cpupower-gui recommendations, try reverting back to the nvidia525 drivers instead of the nvidia535 drivers; the 535xx series have a known bug which does not properly power down the dGPU even when the iGPU is set to integrated.

## Keyboard backlight
There are two drivers to control the keyboard backlight:
*
*

## Known issues
## Thunderbolt
While thunderbolt does work (tested thunderbolt 4 on  2021 Razer Blade Stealth 13"), there are many issues that could arise due to the limited capabilities of the bios. For example, the latest kernels will segfault for some thunderbolt drivers (such as those for blackmagic video capture device), and solutions that work on thinkpad, such a turning of Intel VT or other bios features, are not available on the Razer series of laptops.

## Audio
## No Sound
On newer models (such as RZ09-0409x from 2021), Sound Open Firmware is required for the built-in Intel sound card and the headphone jack (aux port) to work.

If the speakers are detected but don't produce any sound try the script verbs until there is a proper kernel fix available.

## Bad Sound from headphone jack
On newer models (such as Blade 14+ 2021), the quality from the headphone jack is very bad/low volume, and is unusable. You can use Bluetooth, the internal speakers, or a USB audio adapter to remedy this.

## Bad sound from speakers
Razer models can require equalization to sound as good as they do in their windows configurations. EasyEffects, Calf, or Carla can be used with parametric equalizers to fix that issue. Equalization can be automatically applied using PipeWire filters, which may be more user friendly than running one of these tools constantly.

In the following example, Freq, Q, and Gain settings are copied directly from saved LSP Parametric Equalizer configuration - equalized on a 2022 Blade 15" Advanced RZ09-421. The mix node dumps 5% of input to account for increases in the mid-range.
It uses wireplumber smart filter features to auto-wire the filter to the correct interface, without touching the default audio sink.
This pipewire config could be placed under .

{{bc|context.modules  [
    { name  libpipewire-module-filter-chain
        args  {
            node.description  "Equalizer Sink"
            media.name        "Equalizer Sink"
            filter.graph  {
                nodes  [
                    {
                        type     builtin
                        name     eq_band_0
                        label    bq_lowpass
                        control  { "Freq"  18000.0 "Q"  0.707 "Gain"  0.0 }
                    }
                    {
                        type     builtin
                        name     eq_band_1
                        label    bq_peaking
                        control  { "Freq"  250.0 "Q"  1.0 "Gain"  4.3 }
                    }
                    {
                        type     builtin
                        name     eq_band_2
                        label    bq_peaking
                        control  { "Freq"  500.0 "Q"  1.698 "Gain"  -4.3 }
                    }
                    {
                        type     builtin
                        name     eq_band_3
                        label    bq_peaking
                        control  { "Freq"  760.612 "Q"  1.0 "Gain"  -8.7 }
                    }
                    {
                        type     builtin
                        name     eq_band_4
                        label    bq_peaking
                        control  { "Freq"  8000.0 "Q"  1.0 "Gain"  -1.2 }
                    }
                    {
                        type     builtin
                        name     eq_band_5
                        label    bq_highshelf
                        control  { "Freq"  5000.0 "Q"  0.707 "Gain"  0.0 }
                    }
                    {
                        name    mix
                        type    builtin
                        label   mixer
                        control  {
                          "Gain 1"  .95
                        }
                    }
                ]
                links  [
                    { output  "mix:Out" input  "eq_band_0:In" }
                    { output  "eq_band_0:Out" input  "eq_band_1:In" }
                    { output  "eq_band_1:Out" input  "eq_band_2:In" }
                    { output  "eq_band_2:Out" input  "eq_band_3:In" }
                    { output  "eq_band_3:Out" input  "eq_band_4:In" }
                    { output  "eq_band_4:Out" input  "eq_band_5:In" }
                ]
                inputs   [ "mix:In 1" ]
                outputs  [  "eq_band_5:Out"  ]
            }
	    audio.channels  2
	    audio.position  [ FL FR ]
        capture.props  {
            node.name    "effect_input.eq6"
            media.class  Audio/Sink
            filter.smart  true
            filter.smart.name  "effect_input.eq6.smart.1"
            filter.smart.target  { node.name  "alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Speaker__sink" }
        }
        playback.props  {
            node.name    "effect_output.eq6"
            node.passive  true
        }

        }
    }
]
}}

Get the  for the  parameter by inspecting the default sink  :

The id for the default output can be found {{ic|wpctl status  grep '\*'  head -n1 |awk '{gsub(/\./, "", $3); printf "%s", $3}'}} or by examining .

Apply the settings by restarting pipewire and wireplumber services

## Left/Right Speaker Signal is Reversed
On the RZ09-421 model left/right speaker sound is swapped.

This can be automatically corrected using a pipewire configuration that follows. The example uses wireplumber smart filter features to auto-wire the filter to the correct interface, without touching the default audio sink. File :

{{bc|
context.modules  [
    { name  libpipewire-module-filter-chain
        args  {
            node.description  "remap-FL-FR-to-FR-FL"
            media.name        "remap-FL-FR-to-FR-FL"
            filter.graph  {
                nodes  [
                    {
                        name    copyIL
                        type    builtin
                        label   copy
                    }
                    {
                        name    copyIR
                        type    builtin
                        label   copy
                    }
                    {
                        name    copyOL
                        type    builtin
                        label   copy
                    }
                    {
                        name    copyOR
                        type    builtin
                        label   copy
                    }
                ]
                links  [
                # we can only tee from nodes, not inputs so we need
                # to copy the inputs and then tee.
                    { output  "copyIL:Out" input  "copyOR:In" }
                    { output  "copyIR:Out" input  "copyOL:In" }
                ]
                inputs   [ "copyIL:In"  "copyIR:In" ]
                outputs  [ "copyOL:Out" "copyOR:Out" ]
            }
            capture.props  {
                node.name          "remap_input.remap-FL-FR-to-FR-FL"
                audio.position     [ FL FR ]
                stream.dont-remix  true
                node.passive       true
                media.class  Audio/Sink
                filter.smart  true
                filter.smart.name  "swapflfr"
                filter.smart.target  { node.name  "alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Speaker__sink" }
            }
            playback.props  {
                node.name          "remap_output.remap-FL-FR-to-FR-FL"
                audio.position     [ FL FR ]
            }
        }
    }
]
}}

Get the  for the  parameter by inspecting the default sink  :

The id for the default output can be found {{ic|wpctl status  grep '\*'  head -n1 |awk '{gsub(/\./, "", $3); printf "%s", $3}'}} or by examining .
This effect can be chained with the equalized described in the previous section by adding a wireplumber filter smart rule to  :

Apply the settings by restarting pipewire and wireplumber services

## Dual Boot
On later 'Kaby Lake' Intel CPU, if you also have a dual-boot with Windows, you might experience some audio issues when booting to Windows and restarting on Linux. The problem is no sound from the speakers and some cracking noises on the headphones—especially when using the touchpad. No official solution has been posted yet, but a quick hack is to completely shut down the computer (so power off, not restart).

## Secure Boot
The bios does not allow changing signing keys. Therefore, it is not possible to setup a full secure boot system on most Razer hardware. Tested on 2021 Razer Blade Stealth 13" but based on forum posts and research, it appears to apply to many other Razer laptops. We tested appending or changing keys using efitools KeyTool.efi or the efi-updatevars tool; neither work.

## Suspend issues
* If the fan is running when executing , the fan will stay running constantly (tested on Razer Blade Stealth 13" 2021).
* Changing the suspend method to  on newer laptops may resolve this issue (tested on Razer Blade 15 2023).

## Touchpad issues
* Touchpad activates when typing. Despite settings in the window manager to ignore touchpad when typing, this still happens often. No easy resolution is available, and one probably needs to disable the right half of the touch pad as nearly every Razer laptop positions the touchpad off-center from the space bar, causing unwanted touches very often from the right side
* The location of the right click is uncomfortable on nearly every Razer laptop. There is no known way with libinput or synaptics drivers to change the x,z division of the mousepad so that it better aligns with hand placement. Currently, one must take their right hand entirely off the keyboard to get to the right mouse button. A workaround can be to turn on left-handed mode (if you are right handed) so that the secondary click is the far left instead of far right.

## Webcam power drain
* The webcam is constantly consuming power regardless of whether it is in use or not as seen in . The recommended methods for disabling the webcam work to disable the webcam but power drain remains constant. Those methods include added  to  and . We observed that the only way to get the power drain to reduce is to first fully load uvcvideo module after system has completely started and then after that unload and unbind.

## SwitchBlade UI not working (2013)
Source

* SwitchBlade UI, the secondary LCD placed next to keyboard found in some models, does not work due to lack of drivers.

## Tips and tricks
## Tweaking
If you are using GNOME, the gnome-tweak-tool can be used to adjust the window and font scaling. A font scale of 1.25 puts the font sizes closer to how they are displayed by default in Windows 10.

If you are using an external monitor that is not HiDPI, you can use xrandr to alter the scaling of the external monitor using the instructions for multiple displays. You may have better results though running GNOME on Wayland. When installed, clicking the gear icon in GDM will allow you to select Gnome On Wayland and will default to that in the future.

## Power management
Configuration option 1 is compatible if you use optimus manager to switch between Intel and NVIDIA drivers.

## Power modes and fan control
Razer-Laptop-Control can be used to switch between balanced, gaming and creator power modes, as well as manually adjust fan RPM for much better gaming performance and cooling. You can install it via  package for the driver and use the  package for the CLI tool.

Note: The original project has been publicly archived, consider using this updated fork instead Razer-Control-Revived it offers a a cli tool and neat GUI interface, somewhat similar to the razer windows desktop application. As of this writing, it's the most recently updated and active project.

Razer-ctl is another fork of the original project, it offers a cli tool and a minimal tray application in contrast to the GUI aproach of the Razer-Control-Revived fork, which some users might prefer.

## Troubleshooting
## 2016 model issues
## Webcam
There is a known issue using high resolutions (more than 360p) on the webcam video driver used by this models. This is well described in this issue #207045 from the Linux Kernel. You can solve it using Arch build system to build your custom kernel and applying this small patch.

Here is how to Patch your kernel.

## 2014 model issues
Source

* touchpad (multitouch, although this may be a kernel bug that has since been fixed)
* keys to increase/decrease screen illumination not working
* keys to increase/decrease keyboard illumination not working

## Possible trackpad solution
Source

 $ git clone https://github.com/aduggan/hid-rmi.git -b rb14 # and then install it
 # depmod -a

Then install the  package.

Feature still not working: pinch to zoom, 3rd mouse button.

## Webcam
Setting the uvcvideo option "quirks=128" appears to let the webcam work at 720p30, thus enabling Google Hangouts support.  works after changing resolution to 720p and relaunching. Multiplying the quirk by a power of 2+ further improves video quality to a point. "quirks=512" seems to work best for one user.

## Keyboard
The  package enables backlight control capabilities (including effects) and macro controls. You may use  or  for a GUI to set the keyboard options.

For more information on OpenRazer, see Razer peripherals#OpenRazer.

## Infinite suspend loop
Add the following kernel parameter:

 button.lid_init_state=open

to fix the suspend-resume-loop after closing the lid the first time after boot.

## Suspend loop
Suspending (Close laptop lid) does not seem to work with a basic installation. The lid state transitions from "open" to "closed" correctly the first time (and the system suspends), but after resuming from suspend by opening the lid, the lid state does not change back to "open". This results in the laptop entering a suspend loop because systemd monitors the lid state, sees that the lid is closed, and suspends the system.

A bug was filed against the kernel ACPI driver in November 2016. It contains a fair amount of documentation on the issue along with a workaround that seems to solve the problem.

To work around the issue, add the following to your kernel parameters:

 button.lid_init_state=open

This will instruct the acpi driver to generate an extra open event when waking from suspend which will keep the system up.

You can check that the setting was acknowledged:

And also view all boot parameters:

## Suspending
Some users are reporting the laptop immediately waking up after suspending. It appears to be XHC (USB 3.0 chip) that is causing the wakeups.

You can fix this by running

 # echo XHC > /proc/acpi/wakeup

This will not persist on a restart though. To run this command on every startup, see systemd#Writing unit files.

## Suspension issues
If you have suspending stall issue, try to add a new file in  with the following contents:

 blacklist i2c_nvidia_gpu

If you have an infinite suspend loop after the first time you close laptop's lid, then try adding  to your kernel parameters.If you have resume issues with suspension, try adding  as a kernel module parameter.

## Screen flickering / distorted / noise on the 2017 Stealth
Add the kernel parameter:

 i915.edp_vswing=2

Other fixes (changing  settings like DRI and AccelMode) do not seem to help.

Alternatively, add the following kernel parameter:

 intel_idle.max_cstate=1

This changes the power options for the kernel. This will increase the power usage as it keeps the processor on all the time. More information can be found at https://gist.github.com/wmealing/2dd2b543c4d3cff6cab7. It may be worth setting max_cstate as high as possible to reduce power usage. Users reports testing from 8 downward and the first one to work was .

## Possible trackpad solution for 2013 version
[https://web.archive.org/web/20140912193000/https://bbs.archlinux.org/viewtopic.php?id=173356&p=2 Source

 $ git clone https://github.com/aduggan/hid-rmi.git -b rb14 # and then install it
 # depmod -a

Then install the  packages.

Feature still not working: pinch to zoom, 3rd mouse button

## pcieport PCIe bus error
You may see the following errors in dmesg:

 kernel: pcieport 0000:00:1c.0: PCIe Bus Error: severity=Corrected, type=Data Link Layer, id=00e0(Transmitter ID)
 kernel: pcieport 0000:00:1c.0:   device error status/mask=00001000/00002000
 kernel: pcieport 0000:00:1c.0:    [12 Replay Timer Timeout

To avoid these log messages, add a kernel parameter:

 pci=noaer

## 2013 version
## What works
Source

* Wireless
* Switchable graphics
* Bluetooth
* Keyboard light (hardware controlled)
* UEFI boot
