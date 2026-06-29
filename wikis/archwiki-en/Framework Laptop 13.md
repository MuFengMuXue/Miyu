# Framework Laptop 13

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wi-Fi || ||
|-
| Audio (Intel) ||  ||
|-
| Audio (AMD) ||  ||
|-
| Touchpad || ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Bluetooth || ||
|-
| TPM || ||
|-
| Ambient light sensor || ||
|}

This article covers the installation and configuration of Arch Linux on a Framework Laptop.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Hardware
Framework is intended to be a configurable and upgradeable laptop. The lists below is not intended to be an exhaustive list of all the hardware sold with the framework, but rather a list of tested components.

## Wi-Fi/Bluetooth
{| class="wikitable"
|-
! Device Name !! PCI ID !! Bluetooth USB ID !! Working? !! Bluetooth? || Notes
|-
| AX200 ||  ||  ||  ||  || Pre-production units
|-
| AX201 vPro || || ||  ||  || Professional Edition
|-
| AX201 w/o vPro ||  ||  ||  ||  || Base/Performance Editions
|-
| AX210 vPro ||  || ||  ||  || DIY Edition (Optional)
|-
| AX210 w/o vPro ||  ||  ||  ||  || DIY Edition (Optional)
|-
| AX411 vPro ||  ||  ||  ||  || Not sold by Framework, but works
|-
| BE200 ||  ||  ||  ||  || Not sold by Framework, but works only with intel CPU
|-
| RZ608 / MediaTek MT7921K ||  ||  ||  ||  || Not sold by Framework, known to work
|-
| RZ616 / MediaTek MT7922 ||  ||  ||  ||  || AMD edition
|-
| RZ717 / MediaTek MT7925 ||  ||  ||  ||  || AMD edition
|}

## Wi-Fi performance on AMD edition
You will be limited to 802.11n (Wi-Fi 4) and 2.4GHz bands if you do not configure the regulatory domain.

There have been reports of Wi-Fi stability and throughput improvements when using iwd, either directly or as the NetworkManager backend.

For MT7921/MT7922, Wi-Fi stability can be improved by disabling power saving mode as described in Network configuration/Wireless#mt7921 / mt7922.

For MT7925, network speeds over Wi-Fi are very limited; see this thread.

## Graphics
## Intel / i915
{| class="wikitable"
|-
! Device Name !! PCI ID !! Working?
|-
| TigerLake-LP GT2 Xe Graphics ||  ||
|-
| Alder Lake-P GT2 Xe Graphics ||  ||
|-
| Meteor Lake-P Arc Graphics||  ||
|}

## AMD / amdgpu
{| class="wikitable"
|-
! Device Name !! PCI ID !! Working? !! Notes
|-
| Advanced Micro Devices, Inc. Phoenix1 ||  ||  || Needs BIOS 3.03 or newer
|}

## Expansion cards
{| class="wikitable"
|-
! Card Name !! PCI/USB ID !! Working? !! Notes
|-
| USB-C ||  ||  ||
|-
| USB-A ||  ||  || [https://knowledgebase.frame.work/expansion-card-functionality-on-framework-laptop-13-amd-ryzen-7040-series-SkrVx7gAh Can cause high power drain if placed on the two back slots.
|-
| MicroSD ||  ||  ||
|-
| HDMI ||  ||  || For some series, may not work if placed on the front-left slot.

|-
| DisplayPort ||  ||  || For some series, may not work if placed on the front-left slot.
|-
| Storage 250GB ||  ||  || Can crash your USB controller on the AMD Ryzen AI and UAS. You can revert to usb-storage for that device only with: `options usb-storage quirks=13fe:6500:u`
|-
| Storage 1TB ||  ||  ||
|-
| Ethernet ||  ||  ||
|-
| SD (full-size) ||  ||  || Can cause booting issues if an empty SD-to-MicroSD adapter is inserted at boot time.
|}

## Headset jack
On Intel and AMD motherboards, when powersave activates and deactivates on the sound card, there is a small noisy popping sound or a buzzing sound.

The number of seconds after which, if there is no sound activity, the kernel puts the audio module into powersaving, therefore producing the pop or buzz noise, is stored in .

You can deactivate powersave for the sound card entirely by passing  as a module option to , as described in Advanced Linux Sound Architecture/Troubleshooting#Power saving.

If you are using TLP, you can instead set the  variables in .

Motherboards with an Intel Core 12th Gen and later use a different DAC, the Tempo 92HD95Bwhich can cause popping noises when playing back audio using the PipeWire audio server. This seems to happen because PipeWire incorrectly sets the bit depth for the device to 32-bit, while the card only supports 16, 20 & 24-bit [https://community.frame.work/t/responded-headphone-jack-intermittent-noise/5246/119.

The supported rates can be verified by probing :

The current sample rate can be verified by probing  while playing back audio:

The solution is to force the use of 16-bit samples through WirePlumber, by creating the following config file {{hc|/etc/wireplumber/wireplumber.conf.d/51-fix-crackle.conf|
monitor.alsa.rules  [
  {
    matches  [
      {
        node.name  "alsa_output.pci-0000_00_1f.3.analog-stereo"
      }

    actions  {
      update-props  {
        audio.format  "S16LE",
      }
    }
  }
]
}}

## Speakers
By default, the speakers do not sound very balanced (due to downward firing speakers), so you may want to use an equalizer to fix this. The recommended method is to install EasyEffects and use the official preset found here.

Alternatively, you can use user-created profiles such as this one created by cab404.

## Display
The Framework Laptop 13 can be configured with 2 different displays: a 2256x1504 TFT-LCD display or a 2880x1920 display with rounded corners, both manufactured by BOE. They are uncalibrated from factory, giving a suboptimal default sRGB coverage. It is thus recommended to apply an ICC profile to have better color reproduction. [https://www.notebookcheck.net/Framework-Laptop-13-5-Intel-12th-gen-review-Like-the-Microsoft-Surface-but-actually-repairable.633893.0.html#c8723572

* Intel Framework 13 ICC color profile: https://www.notebookcheck.net/uploads/tx_nbc2/BOE_CQ_______NE135FBM_N41_01.icm
* AMD Framework 13 ICC color profile: https://www.notebookcheck.net/uploads/tx_nbc2/BOE_CQ_______NE135FBM_N41_03.icm

* Intel Core Ultra Framework 13 ICC color profile for the 2.8k display: https://www.notebookcheck.net/uploads/tx_nbc2/BOE0CB4.icm

## HDMI audio output
On Intel 11thGen there is a problem where an HDMI TV or HDMI VideoProjector is recognized as an Audio Output Device but no sound is heard when playing music. The HDMI TV output sound correctly using a fresh installed Windows operating system. For correcting this issue you have to first install the  package, then you have to pass  as a module option to  so it uses the SOF version instead of the legacy one.

## Firmware
## BIOS updates
Updates are generally available as UEFI Shell updates from Framework directly. LVFS support is still in testing for some models.

{| class="wikitable"
|-
! Generation !! Stable !! Beta !! LVFS !! LVFSTesting !! Notes
|-
| Intel 11th Gen || 3.24 || || || 3.17(testing only) ||  There will be no LVFS releases for 3.22+ because because they have an Intel CSME update. An UEFI Shell update method is available.Announcement here: |-
| [https://knowledgebase.frame.work/framework-laptop-bios-and-driver-releases-12th-gen-intel-core-Bkx2kosqq Intel 12th Gen || 3.19 || || 3.19 || || Later batches come with 3.05 "to resolve an in-factory specific issue"Announcement here: [https://community.frame.work/t/framework-laptop-13-12th-gen-intel-core-bios-3-19-release-stable/75567
|-
| Intel 13th Gen || 3.09 || || 3.09 || || Windows updater and EFI Shell packages for 3.05 available.Announcement here: |-
| [https://knowledgebase.frame.work/en_us/framework-laptop-bios-and-driver-releases-intel-core-ultra-series-1-H1nZQdxYR Intel Core Ultra 1 || 3.06 || || 3.06 || || Announcement here: |-
| [https://knowledgebase.frame.work/framework-laptop-bios-and-driver-releases-amd-ryzen-7040-series-r1rXGVL16 AMD Ryzen 7040 || 3.18 || || 3.18 || || If you have a batch 1 or 2 device (of the first original Framework AMD release), make sure you upgrade to at least 3.03 first. It comes preinstalled on batch 3 and later. Newer AMD releases with the new 2.8k display batches should already contain latest BIOS firmware (Framework started counting again from batch 1).Announcement here: |-
| [https://knowledgebase.frame.work/framework-laptop-13-bios-and-driver-releases-amd-ryzen-ai-300-series-r1wqKAs1e AMD Ryzen AI 300 || 3.05 || || 3.05 || || All initial batches should come with 3.03 preinstalled.Announcement here: |}

The BIOS can be updated by EFI shell script placed on a bootable USB flash drive. This firmware update method clears EFI boot loaders registered in NVRAM, so having a recovery disk or alternate method of reinstalling your boot loader(s) handy is recommended. If your boot loader installs itself as the EFI fallback at  (systemd-boot will by default, GRUB will with GRUB#Default/fallback boot path), no recovery disk is necessary, but your boot loader may need to be reinstalled to restore its NVRAM entry.

To check which bios is currently installed without rebooting into the bios itself is possible with:

 # dmidecode -s bios-version

## LVFS
Support for fwupd is readily available through the stable remote, which should be enabled by default. Beta firmware builds can sometimes be found on the testing remote [https://community.frame.work/t/bios-3-09-beta-release/20085#lvfs-update-6, which can be enabled by running:

 $ fwupdmgr enable-remote lvfs-testing

## Fingerprint reader
Framework has published a guide for Intel 13th Gen and AMD to upgrade the firmware to a known working version.

## Secure Boot
One can enroll custom keys into the Framework Laptop without any Option ROM concerns, or use the SHIM approach. See Secure Boot for details.

## Suspend
On Intel boards, adding the kernel parameter  fixes a regression in s2idle, making the keyboard backlight and power button correctly turn off when suspending, as well as decreasing battery drain in suspend to about 1%/hourIf your system fails to wake up from suspend due to the SSD disconnecting, you can try putting  in your kernel parameters. This may also improve battery life in suspend, if your SSD has a bad ACPI implementation. This should only be used on Intel boards, as on AMD it will cause the issue, instead of fixing it.

See Power management/Suspend and hibernate#Changing suspend method if you want to use S3 sleep instead of s2idle.

## Fn key after suspend
Some users on 11th-generation Intel boards report that after resuming from suspend, the Fn key and/or media keys no longer work. The workaround is to blacklist the  module:

## Wakeup triggers
If your Framework wakes up while being transported in a backpack or bag, this is because of [https://community.frame.work/t/firmware-feature-request-disable-keypress-while-the-lid-is-closed/49464 the screen pressing against the keyboard. Deactivating the keyboard Wakeup trigger solves this.

Deactivate until next reboot:

 # echo disabled > /sys/devices/platform/i8042/serio0/power/wakeup

Deactivate starting next reboot:

{{hc|/etc/udev/rules.d/disable-keyboard-wakeup.rules|2=
ACTION=="add", SUBSYSTEM=="serio", DRIVERS=="atkbd", ATTR{power/wakeup}="disabled"
}}

Alternatively to disable both keypresses and touchpad is:

 # echo disabled > /sys/devices/platform/AMDI0010:03/i2c-1/i2c-PIXA3854:00/power/wakeup

Framework provides a script which creates a systemd triger to set it up after reboots. Also see their forum post for more discussions.

## Touchpad
There are reports of the touchpad exhibiting issues (e.g. pointer does not move, two-finger scroll does not work, etc.) after waking from sleep. Disabling PS/2 mouse emulation under Advanced in the BIOS seems to resolve the issues=== Interact with system ===

You can interact with your system using .

On 11th and 12th Gen Intel boards, you can also interact with the embedded controller using .

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || Toggles Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , soft blocks wlan and bluetooth
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Controls the keyboard backlight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.

## Ambient light sensor
Should work out of the box, you can check by reading .

On Plasma (starting from version 6.6) and GNOME, you need to install  and restart the session (or reboot, just in case). Then run  to check if it is working.

If you do not use Plasma or GNOME but still want automatic brightness control, check out .

## Fan speed control
You can force the fan speed to any value between 0 and 100 using this tool: https://gitlab.howett.net/DHowett/ectool ()
 $ ectool --interface=lpc fanduty 1OO
to return to automatic mode use this command:
 $ ectool --interface=lpc autofanctrl

In the meantime: https://lore.kernel.org/chrome-platform/20231005160701.19987-1-dustin@howett.net/ for direct support of the EC chromium driver.

## Battery control
Framework laptops have an [https://community.frame.work/t/exploring-the-embedded-controller/12846 embedded controller responsible for controlling a variety of functions (fans, battery, LEDs...). Settings for this EC can be changed with  until patches are merged into the mainline kernel, or alternatively with the framework_tool binary in . Some of the exposed settings related to battery health care are:

 # ectool chargecontrol idle

 # ectool chargecontrol normal lower upper

chargecontrol can be set to discharge, idle, and normal. Discharge makes the system use the energy from the battery, disabling the charger; normal allows setting lower and upper limits (the battery stays in discharge mode while the battery level is between the upper and lower limits, and starts charging when the level is below the lower limit); and idle allows the system to get all the energy from the charger, essentially leaving the battery unused and avoiding any wear. This is very useful for using the laptop as an always-plugged-in device. Setting lower = upper values automatically sets idle mode after reaching the target value, while using idle keeps the battery in idle mode at the current charge level.

You can check how much current is being withdrawn from or charged into the battery with:

 # cat /sys/class/power_supply/BAT0/current_now

Or under Present current in:

 # ectool battery

Using:

 # ectool fwchargelimit level

seems to do the same as setting the charge limit through BIOS, which tries to maintain the battery level at the set level but is constantly charging and discharging it (no idle mode is used in this mode).

Finally, we can set a limit to the max current allowed for charging, thus enabling slow charging, with:

 # ectool chargecurrentlimit mA

Parameters set via ectool remains active until the laptop is powered off and unplugged for a few (10~) seconds, after which values go back to default.

## Troubleshooting
## Stuttering, flickering and periodic freeze
There are reports of stuttering, flickering and periodic freezes on the laptop. Disabling Panel Self-Refresh (as explained in Intel graphics#Screen flickering) has been reported to work. However it is helpful for battery life, so it should be left on if there are no issues.

This can also happen if you have installed  instead of using modesetting, see the note at Intel graphics#Installation.

## Two/three finger clicks
By default, the touchpad provides middle and right click by clicking on specific regions (bottom middle for middle click and bottom right corner for right click). To switch this two-finger click for right click and three-finger click for middle click, you will need to set the "click method" via libinput. First, find your "Touchpad" device name:

 $ xinput

And then set the click method, where  is the name (or ID) found in the previous step:

 $ xinput set-prop "device" "libinput Click Method Enabled" 0 1

To make this persistent, put it in a startup script. Alternatively, if using X11, one can create a custom Xorg configuration file with the appropriate settings (see libinput#Via Xorg configuration file).

## HiDPI settings
* For the 2256x1504 display using scaling factor 1,5 is suggested.
* For the 2880x1920 (2.8K) display using scaling factor 2 is suggested.

For more details, see HiDPI.

## Lowering fan noise
This applies to the Intel version only. AMD users should use power-profiles-daemon.

The handling of fans can be significantly improved by using the  service. Install the package and then you can Start and Enable the service via the  unit file.

## Changing the brightness of the monitor does not work
See Backlight#xbacklight returns : No outputs have backlight property.

For Alder Lake CPUs a solution for using the backlight keys instead of the light sensor is to deactivate the ambient light sensor.

Reboot is required, the light sensor module will be deactivated and the backlight keys work.

Note that some minimal WMs/compositors, such as sway, do not automatically bind the brightness keys, so if you can adjust the brightness through other means but the fn keys do not work, that is likely to be the issue.

## Bootmanager flashing black screen and not loading operating system
If your Framework laptop loads the boot loader and can recognize the EFI system partition on your flash drive or m.2. drive, but cannot load your boot manager (it only flashes a black screen before returning to the boot loader), you must disable Secure Boot.

# Reboot holding . There is a bug in some versions of the BIOS that prevents the  key on the builtin laptop keyboard from being recognized during reboot or power up. The workaround is to connect an external USB keyboard to the laptop an hold the  key on the external keyboard while rebooting or powering up the laptop. After the laptop has entered the BIOS settings the builtin keyboard can be used and the external one can be disconnected.
# Go to the Security Tab
# Secure boot defaults to ON; disable it
# Save changes and restart

## Intel Wi-Fi 6E AX210 reset / low throughput / "Microcode SW error"
Under high stress, Wi-Fi device restarts and network speeds become abysmally slow or non-responsive until disconnecting and reconnecting to Wi-Fi network.This issue has been observed by owners of other manufacturers' laptops (not just framework). [https://community.intel.com/t5/Wireless/Intel-AX210-Firmware-Reset-under-Load/m-p/1339292/highlight/true#M39083

Disabling IEEE 802.11ax seems to be a suitable workaround for the time being. Intel is aware[https://bugzilla.kernel.org/show_bug.cgi?id=214693#c4 of the issue and there is a patchthat fix slow tx after restart, and another[https://bugzilla.kernel.org/attachment.cgi?id=299841&action=diff that address the SW error.

## Fingerprint reader device disconnected error
When the fingerprint reader has been used to enroll a fingerprint on Windows, and you later attempt to use the reader under Linux without first unenrolling your print from within Windows,  can fail to work. In this situation, upon enrolling with fprintd-enroll, the command will hang, as  has crashed.

The best way to deal with this, if you still have access to Windows, is to boot back in and unenroll your fingerprint from there. If this is not possible, you can try a script posted by someone on the Framework laptop forums.

## Low framerate or stuttering webcam
This issue can occur if the program displaying the webcam feed is using the YUYV 4:2:2 color format. Most GUI camera applications do not allow for configuring this. Some applications that will let you configure this include  and , and they also appear to work with the default configuration.

You can also open the webcam using  with:

 $ vlc v4l2:///dev/video1 --v4l2-chroma MJPG

or  with:

 $ mpv --cache=no --demuxer-lavf-format=video4linux2 --demuxer-lavf-o=video_size=1920x1080,input_format=mjpeg av://v4l2:/dev/video0

## 12th gen Turbo-Boost on battery with tlp
By default the 12th gen will not Turbo-Boost on battery if  is installed. This can configured in tlp's configuration.

## 12th gen brightness and airplane mode keys
On the 12th gen motherboards there is a bug where ALS and the brightness up/down including the airplane mode keys conflict. In order to make the brightness and airplane mode keys work in the detriment of using the ambient light sensor, blacklist the  module.

## Ethernet not working with tlp
By default tlp will power limit the framework ethernet adapter. This can be changed in tlp's configuration where  is the ID of the framework ethernet adapter.

## (AMD) TLP is not advised for power management. PPD is recommended
Framework Laptop 13 AMD Ryzen 7040 Series configurations are advised to use power-profiles-daemon (PPD) instead of TLP, which is actively discouraged for this processor. For further discussion see this Framework community thread.

## (AMD) Washed-out colors when using power-profiles-daemon in power-saver or balanced mode
PPD (from Linux 6.9 and PPD 0.20) makes use of ABM (Ambient Backlight Manager), which impacts display color realism in order to save energy when the device is not charging. For more information on configuring it check this Framework community thread.

To simply prevent PPD from adjusting this setting create a drop-in file with the following lines to it:

## (AMD) Flickering, artifacts and a white screen when a second monitor is connected
Note: This issue should be resolved with the latest BIOS update

When a second monitor is connected (possibly only with higher resolutions or refresh rates, and possibly only in Wayland), an issue can be triggered where graphical artifacts or a white image will appear, sometimes showing the original content in a flicker as screen content changes. This can be resolved by adding  as a kernel parameter.

## (AMD) GPU Lockup during graphical load (system still accessible through ssh)
Note: This issue should be resolved with the latest BIOS update and linux-firmware package.

A number of measures seemed to reduce the chances of this happening, and complete system stability was achieved by combining them. It's possible some or all of these will not be necessary as the kernel and firmware are updated.

* Replacing the  package with  (make sure to check  is newer than  before doing this)
* In the BIOS, set the  to
* Setting  to  or  instead of  (in tlp this can be achieved with  and )

Since the use of TLP with an AMD CPU is not advised, setting the performance level depending on the presence of a power supply can be archived with a simple udev rule and a small script:

{{hc|/etc/udev/rules.d/60-power-dpm-force-performance-level.rules|2=
SUBSYSTEM=="power_supply" ENV{POWER_SUPPLY_TYPE}=="Mains" RUN+="/usr/local/bin/set_dpm_perf_level.sh %E{POWER_SUPPLY_ONLINE}"
}}

## (AMD) Flickering graphical corruption on a single monitor
Providing additional memory to the iGPU appears to fix this problem, as advised by Framework Support in this Community thread. Follow this guide from Framework to enable allocating more iGPU RAM from the BIOS.

## "Boot failed" when booting the Arch installer
When trying to boot the official installer the BIOS might show the error "${device} boot failed". This is because the official installation image does not support Secure Boot () and secure boot is enabled by default. This can be resolved by disabling secure boot from the BIOS menu.

## Additional hardware
## Docking stations
Check the USB-C/Thunderbolt Dock Megathread on the Framework community boards for up to date information on functioning docks.

## External GPU
{| class="wikitable"
|-
! Name !! Model Number !! Interface !! Power Delivery? || eGPU? || Notes
|-
| AKITO Node Pro Thunderbolt 3 ||  || USB-C ||  ||  || Errors with PCIe bus expansion for eGPU, 3.16.5 kernel, 3.07 firmware
|-
| Sonnet ||  || USB-C ||  ||  || Tested in kernel 5.15 and above
|-
| Razer ||  || USB-C ||  ||  || Tested in kernel 5.15 and above
|-
| Mantiz MZ-03 Saturn Pro eGPU V2 ||  || USB-C ||  ||  || EU-edition, Potentially needs intel_iommu=on,Tested in kernel 5.15 and above 3.06 Firmware 3.10 and 12th gen framework
|-
| TREBLEET Mini eGPU Enclosure ||  || USB-C ||  ||  || Tested in kernel 6.8.7 and above.
Times out decrypting LUKS partition when cold booting, works when hot-plugged. Crashes WM when unplugged, kicks to DM login
|-
| ADT-Link UT3G ||  || USB-C ||  ||  || Tested in kernel 6.6.52-1-lts and above.

The eGPU works when plugged and does not crash the system when unplugged.

Bandwidth seems to be limited to PCIe 4 x1 in both Arch and Windows on 12th gen.
|-
|}
