# Lenovo ThinkPad P50

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Smart card reader ||  ||
|-
| Color sensor ||  ||
|}

The Lenovo P50 is a quad core Intel Skylake Laptop.

## Hardware
## External video
External video using the Mini DisplayPort seems to work most reliably when the BIOS is configured to use only the discrete graphics card. To use Xorg with this configuration, install NVIDIA drivers and create a minimal X configuration.

## Keyboard function keys
The F key secondary functions accessed via the Fn key can be remapped to other outputs via their keymap IDs listed in the table below.

{| class="wikitable archwiki-table-laptop"
! F key !! XFree86 ID !! EV key code !! X HEX code !! EV key name !! /dev/input/ device !! Device name
|-
| F1 || XF86AudioMute || 113 || 0x1008ff12 || KEY_MUTE ||  || AT Translated Set 2 keyboard
|-
| F2 || XF86AudioLowerVolume || 114 || 0x1008ff11 || KEY_VOLUMEDOWN ||  || AT Translated Set 2 keyboard
|-
| F3 || XF86AudioRaiseVolume || 115 || 0x1008ff13 || KEY_VOLUMEUP ||  || AT Translated Set 2 keyboard
|-
| F4 || XF86AudioMicMute || 248 || 0x1008ffb2 || KEY_MICMUTE ||  || ThinkPad Extra Buttons
|-
| F5 || XF86MonBrightnessDown || 224 || 0x1008ff03 || KEY_BRIGHTNESSDOWN ||  || Video Bus
|-
| F6 || XF86MonBrightnessUp || 225 || 0x1008ff02 || KEY_BRIGHTNESSUP ||  || Video Bus
|-
| F7 || XF86Display || 227 || 0x1008ff59 || KEY_SWITCHVIDEOMODE ||  || ThinkPad Extra Buttons
|-
| F8 || XF86WLAN1 || 238 || 0x1008ff95 || KEY_WLAN ||  || ThinkPad Extra Buttons
|-
| F9 || XF86Tools || 171 || 0x1008ff81 || KEY_CONFIG ||  || ThinkPad Extra Buttons
|-
| F10 || XF86Search || 217 || 0x1008ff1b || KEY_SEARCH ||  || ThinkPad Extra Buttons
|-
| F11 || XF86LaunchA || 120 || 0x1008ff4a || KEY_SCALE ||  || ThinkPad Extra Buttons
|-
| F12 || XF86Explorer || 144 || 0x1008ff5d || KEY_FILE ||  || ThinkPad Extra Buttons
|}

1 Mapping XF86WLAN or its other codes to another function still acts as a WiFi toggle in several desktop environments.

## Troubleshooting
## Sluggish graphics performance with HD Graphics 530 (Skylake GT2)
When running on a 4K monitor using only the embedded Intel graphics, graphics performance may feel sluggish.
This is true for both the built-in monitor (if yours is equipped with a 4K monitor), or an external 4K monitor.
This might be improved in the UEFI BIOS by increasing the amount of RAM the Intel graphics adapter should take from the DRAM from 256MB to the maximum 512MB.
If battery life is not of primary concern, enabling the Nvidia GPU provides a much smoother experience.

## High CPU chromium bug
Chromium takes too long to even display the "new tab" page with the small previews and uses 100% CPU on all cores for several seconds if 5-6 new tabs get open simultaneously when using the Intel Graphics.
This might be due to some hardware acceleration bug maybe related to: Intel graphics#Corruption or unresponsiveness in Chromium and Firefox but has not been tested yet.
But it is simply enough to deactivate hardware acceleration in the chromium settings GUI. Another workaround that seems to work with keeping hardware acceleration enabled is activating the flag

 --ignore-gpu-blacklist

by creating the file ".config/chromium-flag" and adding the flag.

## High fan speed on low CPU load
Even with just low CPU load and only a browser open the fan keeps to switch on and speed up to full power. This behaviour can be at least reduced a bit by only using Intel Graphics and completely powering down the NVIDIA optimus card that uses the same cooling system Power down discrete GPU. This seems due to a low temperature trigger value for the nvidia chip fan.

## Touchpad active even if disabled in BIOS
The touchpad may be enabled in Linux even if it is disabled in the BIOS. To disable it, run

 $ xinput set-prop "SynPS/2 Synaptics TouchPad" "Device Enabled" 0

in an appropriate startup file (e.g., ). To check the device name to use, run

 $ xinput list

## Prevent tap clicking while typing
The touchpad is very sensitive so it often happens that while typing the cursor is moved from unwanted clicks.
Best solution is to deactivate tap click for the touchpad and use the hardware buttons.

This can be done either in the settings of your graphical desktop environment (Gnome3 works after installing libinput drivers) or directly from the shell temporarily with:

 $ synclient TapButton1=0

This change can be made permanent by changing the Xorg configuration.

## Video compression artifacts in VLC
When running on the Nvidia dGPU, if you see compression artifacts when playing videos in VLC, go to Tools -> Preferences -> Input / Codecs and set "Hardware-accelerated decoding" to "Disable".

## Fingerprint reader
See Lenovo ThinkPad T460p#Fingerprint reader; the P50 and T460p share the same fingerprint reader.

## Headsets not working with PulseAudio
Try to boot with headsets plugged in. PulseAudio is innocent.

## Wi-Fi failing to come up (Intel 8260)
On a clean install with kernel 4.8.10 I was unable to bring up the wireless interface. It showed up in 'ip link' and 'iw dev' and was clear of blocks (confirmed via 'rfkill list'). Step 1 is to make sure that it is not soft blocked with rfkill via the 'rfkill list' command. If it is blocked you can use the "F8" Wi-Fi toggle key to ensure that it is not been disabled via that switch.

More importantly: I was unable to get it working intially. I eventually started downgrading the available firmware for this unit by simply moving specific iwlwifi firmware out of /lib/firmware until I identified the working firmware packages.

At the time of this note, the available iwlwifi-8000C-XX.ucode files include version 13, 16, 21 and 22. 22 seems to be the culprit here. 21 and 16 both worked for me. I left all files in place and moved firmware v. 22 to /root/lib/firmware for safe keeping. A reboot (or modprobe -r iwlwifi / modprobe iwlwifi) and the card was working.

## External monitor cannot be detected on Hybrid Graphics in X11
This guide works, if you want to use nvidia driver. If you are using nouveau driver look at this thread.
Wayland-based compositors such as Sway do not appear to exhibit this problem, and work well using either nouveau (Nvidia) or embedded Intel graphics.
