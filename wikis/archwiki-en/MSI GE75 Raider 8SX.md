# MSI GE75 Raider 8SX

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard ||  ||
|-
| GPU (Intel) ||  ||
|-
| RTX 2080 || ||
|-
| RTX 2070 || ||
|-
| RTX 2060 ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

MSI GE75 Raider 8SX refers to the following laptop models:

* MSI GE75 Raider 8SG
* MSI GE75 Raider 8SF
* MSI GE75 Raider 8SE

The only apparent difference between the models is the dedicated Nvidia GPU.

## CPU
Like with many laptop models, these models seem to be designed to run your CPU at a steamy 90+°C when under load. The thermals are already better than on Windows out of the gate on Arch Linux, thermals (and therefore performance) can and should be further improved by undervolting via the intel-undervolt utility, you do this at your own risk.

Disabling CPU vulnerability mitigations can also improve performance significantly for this machine, like with undervolting you do this at your own risk.

## Video
## Integrated graphics
The iGPU works without problems, has Intel GVT-g support too.

## 8SG (Nvidia RTX 2080)
Untested (Should work fine on proprietary nvidia driver)

## 8SF (Nvidia RTX 2070)
Untested (Should work fine on proprietary nvidia driver)

## 8SE (Nvidia RTX 2060)
Although the dedicated graphics seem to be working perfectly with PRIME, there are a few odd issues that might occur on the 8SE.

* Performance issues of various kinds when the display refresh rate is misconfigured (correct refresh rate is 144hz)
* Hard system (GPU Driver Crash?) freeze when running some games with VSync disabled (Tested in Subnautica and No Man's Sky) and in some games for unknown reasons (War Thunder); It also happens when recording long videos with ffmpeg using nvenc (5 min+). This issue can be solved by not using PRIME offloading (e.g. use the dGPU as your main graphics card for X, for instance through )
* *RESOLVED* When using mpv with its vulkan renderer, you may experience major issues when resizing the window. Setting  and  fixes the issue. See git issue for mpv.
* Prime-sync seems not to work when following common instructions to enable it/check if it is enabled, although functionally the card is fine when used with prime, when using the dgpu to run x (with nvidia-xurn or optimus manager) instead of the iGPU, there will be a very high amount of tearing.

The crashing and mpv issues could be regressions, most likely in the nvidia drivers, they were not present in early 2019.

It is uncertain if these issues are bound to the model or if they are faults in the specific device tested on. Overall, all issues are something that is easy to workaround (ensure refresh rate is correctly configured for the display in X, make sure to keep vsync on in video games, use the suggested settings for mpv and use prime normally when you want to use the GPU).

## Audio
This series has some audio issues on Linux.

## Known issues
* Sound from headphones is tied to the volume of the speaker channel which gets muted whenever headphones are plugged in. Headphones will be almost entirely muted. Run  to temporarily fix. The issue can be resolved with the driver options mentioned below.
* Laptop Speakers sound pretty bad by default, can be resolved with driver options below.
* Crackling/popping noises/artifacts in audio occur frequently at start & end of audio streams, barely noticable in speakers but very noticable in headphones. No known solution, although increasing buffer size can sometimes reduce it.c
* Crackling in Pipewire (besides just at start & end of streams), solutions in the relevant section below.

## Driver options
There are two driver options that are known to positively impact this model.

The below setting improves the sound from the laptop speakers (presumably by enabling the LFEs), and the issue with headphones being muted when plugged in.

The below setting fixes the muted headphones on plugin but does not affect the laptop speakers.

## PulseAudio
Default settings are fine, so long as one of the above driver options is used.

## PipeWire
Some applications may cause crackling if not allowed to run sound at their preferred sample rate, this issue can be solved by setting:

A lot of crackling issues can also be solved by increasing the audio buffer size/adding latency.

Increase the buffer size to 1024 and reduce the ALSA period size:

Alternatively, if you prefer not to set a global buffer size, you can instead configure pipewire-pulse applications to have a larger buffer:

To set latency on a per application basis use environment variables  (pipewire-pulse) or  (everything else):
 PULSE_LATENCY_MSEC=X    # Replace X with a number (integer)
 PIPEWIRE_LATENCY=1024/48000 # 21ms, does not work for pipewire-pulse!

When using  environment variable, always check in  and see the QUANT and RATE values, actual latency is QUANT/RATE=LATENCY (in seconds).

It is recommended to either target a quantum of 1024 or 2048 when trying to fix crackling (when 1024 quantum is not enough to prevent crackling, 2048 often is).

No setting to eliminate crackling at the start & end of audio streams has been found, but setting quantum to 2048 for the problematic applications often helps.

## TouchPad
Has some scrolling & palm detection issues, but otherwise works fine. It is recommended to disable tap-to-click functionality due to the palm detect issues.

Refer to below keyboard section if you want to be able to use the toggle touchpad button (FN+F3).

Gestures not tested.

## Keyboard
## RGB Backlighting
RGB Backlighting can be configured via the  utility. If a lighting profile has been configured on Windows prior to booting Linux, the keyboard will remember it.

## Function keys
{| class="wikitable"
|-
! Key
! Detected
! Labeled
! Working
! Effect
|-
|  ||  ||  || || Keyboard Backlighting Increase
|-
|  ||  ||  ||  || Keyboard Backlighting Decrease
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  || P1 (Turbo Mode)
|-
|  ||  ||  ||  || Eco Mode/
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  || Transmission (Gaming Mode)
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  || Airplane Mode
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|}

The Airplane Mode, WLan and Bluetooth buttons will only work if you, add  to your kernel parameters.

The ,  and  keys all get detected with keysyms, but they are all either unassigned or wrongly assigned. To make these keys usable, you need to add this to your :

Understandably, the Turbo and Eco mode buttons do not do anything on Linux since we do not have the Dragon Center software required for those buttons to do anything. You can however now use sxhkd, xbindkeys or your window manager to bind those keys to whatever custom function you want.

There is a remaining issue however where when  is pressed,  are also pressed, this issue is also present on Windows (probably a hardware flaw). This issue sometimes seems to interfere with the buttons functionality. For instance default keybinds for  will not work due to the forced modifiers. Even if you do change the keybind in your DE by going to the appropriate shortcut and hitting  to register it, it is not actually guaranteed to work (in KDE for instance you may get a popup that says the touchpad is on/off, but the touchpad is never actually toggled)

In the end to be able to toggle your touchpad you may need to bind it to a custom script.
