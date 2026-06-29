# Laptop/ASUS

See also Wikipedia:Asus.

## ASUS Linux
Advanced power management (Laptop Power Profile selection, battery charge limit and Panel Overdrive) and many other functions from recent laptops need the ASUS Linux stack installed and running.

## Battery charge threshold
Kernel 5.4 brought the ability to set the battery charge threshold for some Asus laptops, by modifying the  variable exposed under By default this value is set to  and reset on every power cycle[https://github.com/torvalds/linux/commit/7973353e92ee1e7ca3b2eb361a4b7cb66c92abee#diff-38095ba4871836b9eeaa6e1904739d398da72cda890e5ef932daec2995579db3R429-R434.

The effect of its change can be demonstrated as follows:

## Include required module in initramfs
To work around cases of configuration failing to apply at boot because the required  kernel module has not yet been loadedconfigure early module loading for it.

## TLP
TLP gained with [https://github.com/linrunner/TLP/releases/tag/1.4.0 version 1.4 the ability to set battery charge thresholds for laptops other than Thinkpads: see upstream documentation and config example.

## bat
Another (more simple) way to force the charging threshold is by using , which provides a   service and an intuitive terminal interface to change the threshold by typing .

## GNOME extension
 is a GNOME extension that "provides a graphical user interface for setting a laptop’s charging limit (charging threshold) within a Gnome environment". It supports ASUS laptops and many other brands. See its official website for details and screenshots.

## udev rule
The battery's  power supply class attribute does not initially exist. It is added to the  directory by the  kernel module. Create a udev rule for  to set the battery's charge threshold:

## Persist after hibernation
While this setting will persist after suspending to RAM, it will be reset when resuming from hibernation. In order to re-execute the service after hibernation, use one of the methods described in Power management/Suspend and hibernate#Sleep hooks.

If creating a script as described in Power management/Suspend and hibernate#Hooks in /usr/lib/systemd/system-sleep, use something similar to:

Do not forget to make the script executable.

## Model list
## Vivobook
| VivoBook 13 Slate OLED T3300 || 2022-08-11 ||  ||  ||  ||  ||  ||  || Fingerprint enrolls but never matches. Cameras do not work. || Set the  kernel module parameter for the  module in order to use eMMC.
|-
| VivoBook M513IA || 2021-09-12 ||  ||  ||  ||  ||  ||  || See #Function key behavior ||
|-
| VivoBook F510UA || 2018-07-01 ||  ||  ||  ||  ||  ||  || || UEFI secure boot key rejected, had to disable in BIOS.
|-
| VivoBook 14 X405UQ-BV240T || 2024-01-21 ||  ||  ||  ||  ||  ||  || || Secure boot is working. Microsoft platform keys can be deleted without any issue.
|-
| VivoBook 14 X442UA-GA139T || 2018-05-01 ||  ||  ||  ||  ||  ||  || || UEFI secure boot does not pass, might need work.
|-
| VivoBook S301LA || 2016-09-01 ||  ||  ||  ||  ||  ||  needed for hotkeys and backlight control. For package power states lower than PC3, see Remarks. || || To reach PC7,  has to be built without certain build options. An easy way to do this is to build  after modifying its  by removing
|-
| VivoBook X512DA || 2019-03-15 ||  ||  ||  ||  ||  ||  || See #Function key behavior || Fan spins unusually fast when started plugged in.
|-
| Vivobook S14 M433 (X421IA) || 2020-07-31 ||  ||  ||  ||  ||  ||  || Fingerprint does not work. See #Function key behavior || See article for more details.
|-
| VivoBook X509DA_D509DA || 2021-06-21 ||  ||  ||  || , with  ||  ||  || Sometimes the touchpad is not recognized, to fix run  and  || Needed an external Wi-Fi/Ethernet adapter (via USB) during archiso (for access to internet), screen brightness is set to lowest when you plug/unplug your power for the first time after boot (now fixed, i think by adding the  module in )
|-
| VivoBook Pro 14 (M3400) || 2021-04-29 ||  ||  ||  ||  ||  ||  || A few keys were strangely mapped (e.g. Screenshot key  mapped to ). || Recovering from DPMS brightness reset to default can be solved by replacing  with .
|-
| Vivobook X450LCP || 2019-11-01 ||  ||  ||  ||  ||  ||  || Touchpad works better with deprecated  driver || Apparently there is no way to control manually the fan. Every time the fan just stops spinning, needing suspending/reboot to fix.
|-
| Vivobook S 14X OLED (M5402) || 2023-01-06 ||  ||  ||  ||  ||  ||  || No OLED safety features, e.g. pixel shift. ||
* Fingerprint reader is unreliable but does work.
* Battery life is significantly worse compared to when running Windows.
|-
| Vivobook X513EAN || 2023-03-26 ||  ||  ||  ||  ||  ||  ||  needed for hotkeys and backlight control. || Keyboard backlighting is handled by hardware and works normally, other function keys register when pressed but will require remapping to function
|-
| ASUS Vivobook 15X (M1503Q) || 2023-03-29 ||  ||  ||  ||  ||  ||  || ||
|-
| Vivobook M1502IA OLED || 2023-05-04 ||  ||  ||  ||  ||  ||  || Mouse/Keyboard do not wake up after long suspend. System does not properly shutdown or reboot. || The majority of the trackpad is left-click. Middle and right-click are only at the bottom edge.
|-
| Vivobook 15 M1502Q || 2026-01-26 ||  ||  ||  ||  ||  ||  || Fingerprint enrolls but never matches ||
|-
| Vivobook 15 M1502YA || 2025-03-22 ||  ||  ||  ||  ||  ||  || || Sound untested without sof-firmware.
|-
| Vivobook GO 15 E1504FA || 2024-01-08 ||  ||  ||  ||  ||  ||  || Easiest method to control the monitor backlight is to use  ||
|-
| Vivobook GO 15 E1504G || 2024-12-25 ||  ||  ||  ||  ||  ||  || The Wi-Fi and Bluetooth device is a MediaTek MT7902 which doesn't have drivers in the Linux kernel nor is supported by MediaTek on Linux||
|-
| Vivobook Pro 15 N6506MJ OLED || 2025-07-08 ||  ||  ||  ||  ||  ||  || || Some wakeup triggers must be disabled to prevent the laptop from waking up immediately upon sleeping.
Use the  and  kernel module parameters along with a power management tool to match the battery life of this device when running Windows.
|-
| Vivobook S 16 M5606KA || 2025-12-17 ||  ||  ||  ||  ||  ||  || Keyboard backlight is always white; only brightness is controllable. No color or pattern control. ||  Self panel refresh causes occasional typing latency and makes sudo prompts almost unusable due to lack of screen updates between keystrokes. Fixed with kernel parameter .
|-
| Vivobook Go 14 E410MA || 2026-01-15 ||  ||  ||  ||  ||  ||  || ||Numberpad needs additional configuration to work.
|}
## Function key behavior
The Function keys default behavior is , , etc… and must be unset by using  to use alternative functions.

## Gaming
| GL552VM-DM-802D || 2017-02-01 ||  ||  ||  ||  ||  ||  || || Needs  to have  keys backlight control,  and  to boot.
|-
| G502VM-FY017T || 2017-02-01 ||  ||  ||  ||  ||  ||  || The screen adjustment need a little workaround ||
|-
| FX502VM || 2017-02-01 ||  ||  ||  ||  ||  ||  || Fn keys does not send ACPI events, except ,, (sound control) ||
|-
| FX504GD || 2019-05-30 ||  ||  ||  ||  ||  ||  || For Fan Speed Control see Fan speed control#Alternative method using EC registers. For touchpad five finger touch of death apply patch pinctl-intel.c patch ||
|-
| FX505DY || 2020-12-01 ||  ||  ||  ||  ||  ||  || || See #Black screen after sleep
|-
| FX505DT || 2021-09-30 ||  ||  ||  ||  ||  ||  || See #Battery charge threshold. Keyboard backlight settings can be controlled via  || See #Black screen after sleep
|-
| G73SW || 2011-08-19 ||  ||  || ||  ||  ||  || ||
|-
| G550JK || 2014-08-01 ||  ||  ||  ||  ||  ||  || || fix background noises while using headphones
|-
| FX 533VE || 2018-02-01 ||  ||  ||  ||  ||  ||  || || See #Nouveau prevents boot.
|-
| FX 504GM || 2019-02-01 ||  ||  ||  ||  ||  ||  || || Did not manage to use the HDMI output (in fact, it is possible, but...), issue posted on the forum. See #Nouveau prevents boot.
|-
| FX 504GE || 2019-06-01 ||  ||  ||  ||  ||  ||  || || See #Elan1200 touchpad.
|-
| GL 503VD || 2019-02-01 ||  ||  ||  ||  ||  ||  || || See #Elan1200 touchpad.See #Nouveau prevents boot.
|-
| FA506IV || 2022-02-02 ||  ||  ||  ||  ||  ||  || Keyboard backlight works but needs faustus with  to change RGB. || Cannot change EFI boot stubs timeout with efibootmgr.
|}

## Republic of Gamers (ROG)
| ROG G55VW || 2012-07-30 ||  ||  ||  ||  ||  ||  || ||
|-
| ROG Strix GL702ZC || 2017-04-01 ||  ||  ||  ||  ||  ||  || Backlight keys are amdgpu, not xbacklight. Fancontrol is ACPI, there are some amdgpu fan control stuff on aur/github. ||
|-
| ROG Zephyrus M || 2023-08-20 ||  ||  ||  ||  ||  ||  || All of the Asus AUR control applications seem to work just fine for controlling keyboard backlight, fans (on/off/auto), and battery thresholds    || The battery is the big disadvantage. On Windows it can last for up to 6h, however. This laptop is definitely not Linux friendly
|-
| ROG Zephyrus M16 GU603Z || 2023-03-08 ||  ||  ||  ||  ||  ||  || All of the Asus AUR control applications seem to work just fine for controlling keyboard backlight, fans, and battery thresholds    || I did not expect the battery life to be great on this laptop, but otherwise it works fine with linux, i.e. gaming is fantastic and the 20 core CPU seems to work great.
|-
| ROG Zephyrus G14 (GA401I) || 2021-05-12 ||  ||  ||  ||  ||  ||  || Some function keys and AniMe LED matrix work with kernel patches and . ||
|-
| ROG Zephyrus G15 (GA502IU)|| 2020-07-08 ||  ||  ||  ||  ||  ||  || Some custom keys do not work. Can control only one fan with  module. ||
|-
| ROG Zephyrus S15 (GX502LWS) || 2020-20-25 ||  ||  ||  ||  ||  ||  || Keyboard colors work using  ||
|-
| ROG Flow X13 (GV301QE) || 2021-07-01 || rowspan="3"  || rowspan="3"  || rowspan="3"  || rowspan="3"  || rowspan="3"  || rowspan="2"  || Accelerometer sensor is not detected (waiting for asus-wmi fix?). Lid-backflip sensor works with  || rowspan="2" | Tablet integration is manual, because the lid-backflip sensor is missing.
|-
| ROG Flow X13 (GV301QH) || 2021-10-09 || Lid-backflip is not detected. Fingerprint sensor is detected when libfprint is fully upgraded, however it always fails to verify.
|-
| ROG Flow X13 (GV301RA) || 2024-10-13 ||  || Accelerometer works, Fingerprint sensor works but verification fails pretty often. ||
|-
| ROG Zephyrus GU501GM || 2021-11-24 ||  ||  ||  ||  ||  ||  || Fan curves cannot be changed though overboost modes work. RGB works with  and all keys work except the mute microphone button || HDMI output is hardwired to the NVIDIA GPU.
|-
| ROG Zephyrus S GX531GS || 2024-04-29 ||  ||  ||  ||  ||  ||  || Fan curves cannot be changed though overboost modes work. RGB works with  and all keys work || HDMI output is hardwired to the NVIDIA GPU.
|-
| ROG Strix G15 G513QY Advantage Edition || 2022-01-16 ||  ||  ||  ||  ||  ||  || Flashing lights during sleep could be disabled with . Support for custom fan curves should land in kernel 5.17 ||
|-
| ROG Strix Scar G15 G533QS || 2022-02-19 ||  ||  ||  ||  ||  ||  || ||
|-
| ROG Strix G15 G513 (G513QR) || 2022-02-21 ||  || * ||  ||  ||  ||  || Sometimes the Wi-Fi card is not recognized after rebooting. The keys for changing profile and muting the mic require workaround (see fix for profile and mic-mute. || *Very noisy (almost useless) internal mic. Headset mic requires hdajackretask: select Realtek ALC825 and override pin  with "Microphone".
|-
| ROG STRIX G732LXS || 2022-11-12 ||  || * ||  ||  ||  ||  || supergfxd works perfectly with balanced settings. Optimus needs NVIDIA only ||
|-
| ROG Zephyrus M16 2023 (GU604V) || 2023-04-26 ||  || * ||  ||  ||  ||  || There is no support for Advanced Optimus as of now. || Tested with secure boot and fast boot disabled.
|-
| ROG STRIX G17 (G713RW) || 2023-07-03 ||  ||  ||  ||  ||  ||  || Awful microphone and also minor Wi-Fi Problems || ASUS Linux works great. RGB control supported.
|-
| ROG STRIX G17 (G713PU) || 2026-05-08 ||  ||  ||  ||  ||  ||  || || Works great. ASUS Linux & PRIME make it better.
|-
| ROG Zephyrus G14 2023 (G402NV) || 2023-07-16 ||  ||  ||  ||  ||  ||  ||
|| In case of suspend-to-ram issue, downgrade UEFI to v310 (see here)
|-
| ROG Zephyrus G14 2023 (G402XV) || 2023-10-24 ||  ||  ||  ||  ||  ||  ||
 works great.
||
* In case of suspend-to-ram issue, downgrade UEFI to v310 (see here)
* Screen flickering issues may occur with certain resolutions and refresh rates in some Linux kernel versions.
|-
| ROG Flow X16 2023 (GV601VI) || 2024-01-24 ||  ||  ||  ||  ||  ||  ||
*  works great, you can toggle the MiniLED mode of the display too
* Tablet PC#Automatic rotation works
||
|-
| ROG Strix G16 2023 (G614JI) || 2024-05-01 ||  ||  ||  ||  ||  ||  || colspan=2 |
* nvidia driver version 550.78+ is required for suspend to work
* Set  for proper display brightness control on dGPU
|-
| ROG Zephyrus G14 2024 (GA403UV) || 2024-06-17 ||  ||  ||  ||  ||  ||  || colspan=2 |  avoids crashes with the standard driver.
|-
| ROG Zephyrus G16 2024 (GU605MI) || 2024-09-01 ||  ||  ||  ||  ||  ||  || || For OLED screen brightness, see Backlight#Color correction.
|-
| ROG Zephyrus G16 2024 (GU605MZ) || 2025-06-23 ||  ||  ||  ||  ||  ||  || need kernel parameters  for screen backlight control in hybrid GPU mode ||
|-
| ROG Zephyrus G14 2025 (GA403WW) || 2025-05-26 ||  ||  ||  ||  ||  ||  || ||
|}

## The Ultimate Force (TUF)
| TUF Dash F15 (FX517ZC/ZR/ZM/ZE) || 2022-07-01 ||  ||  ||  ||  ||  ||  || Keyboard effects not controllable. Most function keys work, Aura and airplane mode keys do not. || Hybrid GPU switching works perfectly using asusctl.
|-
| TUF Gaming F15 (FA507RC/RE/RM/RR/RW) || 2022-12-17 ||  ||  ||  ||  ||  ||  || Keyboard RGB controllable with kernel above 6.1. All function keys work. || Needs  kernel module blacklisted.
|-
| TUF Gaming A15 (FA506NC/IC/IE/IHR/QR/) || 2021-03-15 ||  ||  ||  ||  ||  ||  || colspan=2 |
* Monitor brightness control requires the following kernel parameters:
* Keyboard rgb control requires asusctl (only static effect available)
|-
| TUF Gaming A16 (FA617XS/NS/NSR/XT/NT) || 2025-03-06 ||  ||  ||  ||  ||  ||  || ||
* Suspend-to-RAM is broken in BIOS versions 311-313. The issue is addressed in BIOS version 316 and later.
* For Steam gaming start games with , for gaming and desktop graphic glitch issues see AMDGPU#Tear free rendering
* If you experience green artifacts on eDP display, disable Panel self refresh v1 with the following kernel parameter
|-
| TUF Gaming F15 (FX506HC-HN111W) || 2024-01-21 ||  ||  ||  ||  ||  ||  || || asusctl recommended for keyboard RGB control and hybrid GPU switching
|-
| TUF Gaming A15 (FA507UV) || 2024-10-07 ||  ||  ||  ||  ||  ||  || || Upgrading BIOS from 307 to 309 causes losing control over keyboard's LED, fan speed and charge threshold
|}

## Black screen after sleep
Add  to your kernel command line.

## Laptop not resuming (NVIDIA GPU with no iGPU)
Some laptops with only an NVIDIA GPU and no integrated GPU may fail to resume properly from suspend, especially when the system only supports . To fix that enable S0ix support on NVIDIA Proprietary driver

## Enable S0ix support (NVIDIA proprietary driver)
You can check if S0ix is currently enabled for the NVIDIA GPU by running:

Look for this section:

If it shows:

Then S0ix is not currently active.

To enable S0ix support, ensure you're using NVIDIA driver version 515 or newer. Then, configure the kernel module option:

Create a modprobe configuration file:

Rebuild the initramfs:

Then reboot:

After rebooting, re-check:

Confirm that the line now reads:

This indicates that S0ix is now active.

Additionally, enable NVIDIA suspend/resume services:

These services help properly transition the GPU into and out of low-power states during suspend/resume.

## Nouveau prevents boot
Boot with nouveau disabled: use  on the kernel command line.
Need to edit bumblebee service to boot : https://github.com/Bumblebee-Project/Bumblebee/issues/764#issuecomment-450749984.

## Elan1200 touchpad
Some fixes are needed: see https://bugzilla.redhat.com/show_bug.cgi?id=1543769.

## ZenBook
| UX305FA || 2016-10-01 ||  ||  ||  ||  ||  ||  || Function keys for brightness (/) do not send ACPI events ||
|-
| UX303LN || 2014-10-01 ||  ||  ||  ||  ||  ||  || Touchpad misses gestures, Touchscreen misses multi-touch support || Avoid some power management features due to Kernel Bug 102091.
|-
| UX32A || 2014-03-14 ||  ||  ||  ||  ||  ||  || || See ASUS Zenbook Prime UX31A#Keyboard backlight
|-
| UX32L(N) || 2015-08-29 ||  ||  ||  ||  ||  ||  || Set the kernel parameters  for working backlight keys and backlight restore. || Avoid activating some power management features due to Kernel Bug 102091.
|-
| UX325EA || 2025-03-22 ||  ||  ||  ||  ||  ||  ||  || Button to enable/disable camera, MyASUS, not working. Numpad works with relevant driver.
|-
| UX331UA || 2018-09-05 ||  ||  ||  ||  ||  ||  ||  ||
|-
| UX3404VA || 2024-04-08 ||  ||  ||  ||  ||  ||  || ||
|-
| UX3405MA || 2024-05-17 ||  ||  ||  ||  ||  ||  || ||
|-
| UX480 || 2019-10-23 ||  ||  ||  ||  ||  ||  || ||
|-
| UX430UA || 2017-06-01 ||  ||  ||  ||  ||  ||  || rowspan="3" | PWM Fan control is not available || rowspan="3" | See dedicated page.
|-
| UX390UA || 2018-05-01 ||  ||  ||  ||  ||  ||
|-
| UX534FTC || 2020-04-09 ||  ||  ||  ||  ||  ||
|-
| UM425 || 2021-02-01 ||  ||  ||  ||  ||  ||
|-
| UM3402YA || 2022-09-28 ||  ||  ||  ||  ||  ||  || Fancontroll, fingerprint sensor not working; "deep sleep"/suspend to ram draining power || *internal speakers not working
|-
| UX3402ZA || 2023-01-31 ||  ||  ||  ||  ||  ||  || Fingerprint works but might require some patience when swiping ||
|-
| UX5401ZA || 2023-02-24 ||  ||  ||  ||  ||  ||  || ||
|-
| UX363EA || 2023-07-22 ||  || * ||  ||  ||  ||  || *Audio might require disabling fast boot in UEFI if dual booting and tweaking ALSA volume control || Pipewire + wireplumber confirmed to work on audio/video playback
|-
| UX5304 || 2023-04-21 ||  || * ||  ||  ||  ||  || *Audio might require disabling fast boot in UEFI if dual booting and tweaking ALSA volume control || Internal Speakers do not work
|-
| UX8402Z || 2023-11-10 ||  ||  ||  ||  ||  ||  || ||
|-
| UX6404VV || 2024-01-15 ||  ||  ||  ||  ||  ||  || ||
|-
| UM5606 || 2024-09-09 ||  || * ||  ||  || * || * || *Most issues can be resolved by reading the ASUS Zenbook UM5606 page and installing  &
||
|-
| UX5406(SA) || 2025-04-17 ||  ||  ||  ||  ||  ||  || ||
|-
| UX582 HS i9 11900H || 2025-06-30 ||  ||  ||  ||  ||  ||  || Do not use "Better Blur" in KDE Plasma. With it, the system will be very slow while playing youtube 4k videos.
Regular "Blur" works fine.
||
No sound on the internal speakers or the headphones jack.

Sound works on displays over HDMI or USB-C, and on  bluetooth headphones.
|-
| UM3406KA || 2025-09-21 ||  ||  ||  || * ||  ||  || Face login works well with Howdy || Ensure that  or  are installed, otherwise Wi-Fi will not work (even though the chip is not Broadcom)
|}

## ExpertBook
| B9450 || 2020-04-20 ||  ||  ||  ||  ||  ||  || ||
|-
| B9450CEA || 2021-03-14 ||  || * ||  ||  ||  ||  || ||
|-
| BR1100FKA || 2021-05-28 ||  ||  ||  ||  ||  ||  ||  || Set the  kernel module parameter for the  module in order to use eMMC.
|}

## Eee PC
|-
| T101MT || 2010-08-14 ||  ||  ||  ||  ||  ||  || ||
|-
| 1001P || 2011-09-04 ||  ||  ||  ||  ||  ||  || ||
|-
| 1001PXD || 2025-04-10 ||  || * ||  ||  ||  ||  ||  needed for hotkeys and  module related features (like SHE). || *Add  to
|-
| 1005P || 2013-04-22 ||  ||  ||  ||  ||  ||  || ||
|-
| 1015 series || 2014-05-19 ||  ||  ||  ||  ||  ||  ||  ||
|-
| F201E || 2015-09-19 ||  ||  ||  ||  ||  ||  || ||
|-
| 1201 series || 2017-11-11 ||  ||  ||  ||  ||  ||  || ||
|-
| 1215 series || 2017-12-08 ||  ||  ||  ||  ||  ||  || || Might need
|}

## Other
| W7S || 2007-08-01 ||  ||  ||  ||  ||  ||  || ||
|-
| F5R || 2008-01-16 ||  ||  ||  ||  ||  ||  || colspan=2 | ACPI works with acpi4asus and acpid
|-
| G1 || 2008-11-23 ||  ||  ||  ||  ||  ||  ||
|-
| M51SN || 2008-12-17 ||  ||  ||  ||  ||  ||  || colspan=2 | Add  to
|-
| A7SN || 2008-12-31 ||  ||  ||  ||  ||  ||  ||
|-
| N80Vn-X5 || 2009-02 ||  ||  ||  ||  ||  ||  || colspan=2 | Add  to
|-
| F8SN || 2009-08 ||  ||  ||  ||  ||  ||  ||  ||
|-
| A6km || 2009-08-10 ||  ||  ||  ||  ||  ||  || ||
|-
| L3000D || 2010-02-13 ||  ||  ||  ||  ||  ||  || ||
|-
| N53JN || 2010-11-03 ||  ||  ||  ||  ||  ||  || colspan=2 | suspend works but with problems due to USB3 controller
|-
| N53SV || 2011-06-26 ||  ||  ||  ||  ||  ||  || colspan=2 | See also Ubuntu help
|-
| N82JV || 2011-11-20 ||  ||  ||  ||  ||  ||  || ||
|-
| N56 series || 2014-06-30 ||  ||  ||  ||  ||  ||  ||  ||
|-
| A8Le || 2011-07-31 ||  ||  ||  ||  ||  ||  || ||
|-
| UL30A || 2015-07-03 ||  ||  ||  ||  ||  ||  ||  || Needs . Use  if crashing on boot.
|-
| A53T || 2012-07-21 ||  ||  ||  ||  ||  ||  || ||
|-
| U31SD || 2012-12-30 ||  ||  ||  ||  ||  ||  || ||
|-
| K55VM || 2013-04-01 ||  ||  ||  ||  ||  ||  || ||
|-
| A55VJ || 2013-05-01 ||  ||  ||  ||  ||  ||  || colspan=2 | Use  to prevent jittery touchpad.
|-
| X401A/X401A1 || 2013-05-01 ||  ||  ||  ||  ||  || brightness control needs  and  || ||
|-
| X502CA || 2013-07-01 ||  ||  ||  ||  ||  ||  || || Poor Wi-Fi performance
|-
| S300CA || 2013-08-01 ||  ||  ||  ||  ||  ||  ||  || Use
|-
| Q400A || 2013-10-17 ||  ||  ||  ||  ||  ||  ||  ||
|-
| X401U || 2014-01-05 ||  ||  ||  ||  ||  ||  || ||
|-
| K55N || 2014-11-12 ||  ||  ||  ||  ||  || Overheats and immediately shuts down on modern 3D games. Use thermald to control temp using acpi_cpufreq || colspan=2 | Fix fn brightness keys with . Do not enable early radeon hook to prevent blank screen after hibernation. Fix blank screen on suspend to ram with .
|-
| X53BR/K53BR || 2014-03-30 ||  ||  ||  ||  ||  ||  || || heats up very fast
|-
| X551CA || 2014-03-24 ||  ||  ||  ||  ||  ||  || colspan=2 | Disabling Wi-Fi blocks the card,  does not work. Workaround on Ubuntu forum.
|-
| N550JV || 2014-03-01 ||  || * ||  ||  ||  || ** || colspan=2 | *external speakers pop on sleep/shutdown**battery issues when a powered device is left plugged into the USB charging port.
|-
| X83VB-X2 || 2014-09-01 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Q500A || 2015-02-01 ||  ||  ||  ||  ||  ||  || ||
|-
| S400CA || 2015-02-01 ||  ||  ||  ||  ||  ||  ||  || Use
|-
| U32U || 2015-02-01 ||  ||  ||  || ||  ||  || Needs significant setup. Power management hard to get right. CPU Fan constantly on. || For rfkill issues  may help
|-
| X555L || 2016-05-19 ||  ||  ||  ||  ||  ||  || colspan=2 | Set  for proper display brightness control
|-
| X551MA(V) || 2017-01-31 ||  ||  ||  ||  ||  ||  || colspan=2 | Set  for proper display brightness control
|-
| X553MA || 2015-06-01 ||  ||  ||  ||  ||  ||  || colspan=2 | Set  in BIOS setup to broadcom-wl (causes freezes)
|-
| F550J (aka A550J) || 2015-09-01 ||  ||  ||  ||  ||  ||  ||  recommended for touchpad || Consider disabling standalone graphics card
|-
| N550JX || 2015-12-28 ||  || * ||  ||  ||  ||  || || *external speakers needs Add kernel parameter  to fix  keys
|-
| X552M || 2015-12-01 ||  ||  ||  ||  ||  ||  || Use  for changing backlight with / || broadcom-wl (causes freezes)
|-
| E403SA || 2017-10-29 ||  ||  ||  ||  ||  ||  ||  ||
|-
| F555UA || 2016-08-14 ||  ||  ||  ||  ||  ||  || No two finger scroll, very buggy touchpad || Add  to  to get mic and headphone/mic to work
|-
| K501J || 2016-09-01 ||  ||  ||  ||  ||  ||  || colspan=2 | Touchpad works with , but somewhat uncomfortable. Better with  even if deprecated.
|-
| K501LX || 2017-01-01 ||  ||  ||  ||  ||  ||  ||  || Added  to kernel parameters to make  work correctly.
|-
| R540SA || 2017-03-01 ||  ||  ||  ||  ||  ||  || ||
|-
| N551VW || 2017-06-01 ||  || * ||  ||  ||  ||  || colspan=2 | *Through hdajackretask select Realtek ALC668, check Show unconnected pins then check Override on Pin ID: 0x1a and Internal speaker (LFE), then apply and install the boot override.
|-
| N551ZU || 2022-10-20 ||  ||  ||  ||  ||  ||  || || AMD Enduro supported via PRIME
|-
| N76V || 2019-01-05 ||  ||  ||  ||  ||  ||  || ||
|-
| X451MA || 2021-02-12 ||  ||  ||  ||  ||  ||  || || Install
|-
| K55VD || 2024-04-19 ||  ||  ||  ||  ||  ||  ||
|-
| B9440UA || 2024-01-13 ||  ||  ||  ||  ||  ||  ||  || * Headphone Jack outputs very silent audio requiring output volume to be set to 153% to be audible which then produces distortion.
|}
