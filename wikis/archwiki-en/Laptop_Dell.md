# Laptop/Dell

## Software
Dell offers in-house Linux support for a subset of hardware, contributing to the  kernel module (refer to it's documentation hereand providing native Linux utilities to control hardware on supported devices. These utilities include:

*  a suite of programs for controlling hardware. Key programs include:
** : Get and set battery charge configuration
** : Control keyboard backlight illumination and light sensors
** : Set separate screen brightness for battery and mains
** : Get and set service, asset and property tags
** : Get and set thermal modes - usually balanced, cool-bottom, quiet, and performance
** : Get and control the status of radio hardware
*  () enables BIOS configuration from userland. On some devices this is the only method for configuring and persisting custom battery charge behaviour.

ACPI  are natively supported on newer kernels which enables setting thermal modes without Dell specific software.[https://web.git.kernel.org/pub/scm/linux/kernel/git/pdx86/platform-drivers-x86.git/commit/?h=for-next&id=996ad412981024a9bb90991ab195685d37187bbd

Dell also makes firmware updates for some devices available via the Linux Vendor firmware Service (LVFS).

## Accessibility
* The firmware is graphical and has a tightly-packed simple text menu (with expandable categories) on the left, with fairly small text.
* All the settable options are in a large pane on the right, again.
* Apply must be clicked to make any changes.
* The touch screen and the touchpad work in the firmware, and the tabulation and arrow keys also allow cursoring around the different options and buttons.
** The  key alternates between three zones: the menu at the left, the settings pane at the right, and the Apply, Restore Settings, and Exit buttons. The arrow keys must then be used to cursor around the items within each of those zones.
* The firmware contains many radio buttons and checkboxes, but these are only in the right pane.

## Model list
## Alienware
| Alienware M11x || 2012-02-28 ||  ||  ||  ||  ||  ||  || ||
|-
| Alienware M14xR2 || 2013-06-15 ||  ||  ||  ||  ||  ||  || ||
|-
|}

## Inspiron
| Inspiron 13 2-in-1 (5368) || 2016-12-20 ||  ||  ||  ||  ||  ||  || ||
|-
| Inspiron 13 2-in-1 (5378) || 2023-10-14 ||  ||  ||  ||  ||  ||  || ||
|-
| Inspiron 13 (5391) || 2021-03-30 ||  || * ||  ||  ||  ||  ||  || *Needs
|-
| Inspiron 13 (7348) || 2021-05-28 ||  ||  ||  ||  ||  ||  || ||
|-
| Inspiron 13 (7370) || 2017-12 ||  ||  ||  ||  ||  ||  || Fingerprint reader is unsupported.|| *Does not wake up after closing the screen lid. Wireless toggle does not work
|-
| Inspiron 14 (3420) || 2016-09-03 ||  ||  ||  ||  ||  ||  || || Requires
|-
| Inspiron 14 (5425) || 2023-01-18 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Inspiron 14 2-in-1 (7425) || 2022-01-24 ||  ||  ||  ||  || * ||  || || *Fingerprint reader and Bluetooth cause system to hang on wake from sleep, need to add scripts to shutdown on sleep and restart on wake.
|-
| Inspiron 14 Plus (7430) || 2023-03 ||  ||  ||  ||  ||  ||  ||  || HDMI always turn on NVIDIA, but monitor through thunderbolt can work with Intel only. Sound works better with pipewire.
|-
| Inspiron 14 (7490) || 2023-08-28 ||  ||  ||  ||  ||  ||  ||  || Requires AHCI to be manually enabled
|-
| Inspiron 15 (3511) || 2026-01-30 ||  ||  ||  ||  ||  ||  ||  || S3 sleep is not supported
|-
| Inspiron 15 (3521) || 2025-07-06 ||  ||  ||  ||  ||  ||  || ||
|-
| Inspiron 15 (3525) || 2023-08-08 ||  ||  ||  ||  ||  ||  || || *Disabling C6 states fixes closing the lid and suspending
|-
| Inspiron 15 (3593) || 2024-11-09 ||  ||  ||  ||  ||  ||  || ||
|-
| Inspiron 15 (5515) || 2021-07-01 ||  ||  ||  ||  || * ||  || || * Not reliable, needs restarting or running   as root when having issues.
|-
| Inspiron 15R (5521) || 2022-09-26 ||  ||  ||  ||  ||  ||  ||  || Function keys need to be manually assigned.
|-
| Inspiron 15 (5547) || 2016-01-25 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Inspiron 15 (5559) || 2021-07-19 ||  ||  ||  ||  ||   ||  || ||
|-
| Inspiron 15 (5566) || 2020-09-24 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Inspiron 15 (5567) || 2020-04-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Inspiron 15 (5575) || 2019-12-01 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Inspiron 15 (7537)  || 2016-06-01 ||  ||  ||  ||  ||  ||  || colspan=2 | Volume up / down button needs some modifying to work all other buttons work with drivers that come with the kernel. ACPI battery is not detected on bootup and requires you to plug in and out the AC adapter.
|-
| Inspiron 15 (7548)  || 2015-05 ||  ||  ||  ||  ||  ||  ||  || If the kernel panics during bootup replace the 'keyboard'-hook with the specific module.
|-
| Inspiron 15 (7559)  || 2016-08 || * ||  ||  ||  ||  ||  || || *bumblebee with issue
|-
| Inspiron 15 (7566) || 2025-03 ||  || * ||  ||  ||  ||  || || *Subwoofer requires channel remapping via HDAJackRetask.
|-
| Inspiron 15 (7570)  || 2021-10-27 ||  ||  ||  ||  ||  ||  || colspan=2 | USB-C DisplayPort alt-mode tested with a Dell P2721Q monitor. 65W of power, USB hub and Video delivered over USB-C work well. Rare issues with the monitor sometimes losing the video connection when switching users or logging out (on resolution changes). The power and USB keep working though.
|-
| Inspiron 15 (7586) || 2019-07-01 ||  ||  ||  ||  ||  ||  ||  || Fingerprint reader works with proprietary driver.
|-
| Inspiron 15 (7590) || 2020-02 ||  ||  ||  ||  ||  ||  ||  || *See dedicated page
|-
| Inspiron 16 (5620) || 2024-03-15 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Inspiron 16 Plus (7620) || 2022-08-08 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Inspiron 16 2-in-1 (7620) || 2022-12-12 ||  ||  ||  ||  ||  ||  || ||
|-
| Inspiron 15 (5590) || 2026-02-25 ||  ||  ||  ||  ||  ||  || ||
|-
|}

## Latitude
| Latitude D620 || 2007-05-17 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Latitude D630 || 2015-12-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude D820 || 2007-05-17 ||  ||  ||  || ||  ||  || ||
|-
| Latitude D830 || 2007-08-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude 3540 || 2022-06-28 ||  ||  ||  ||  ||  ||  || colspan=2 | Flaky Bluetooth coexistence with Wi-Fi
|-
| Latitude E5400 || 2021-11-11 ||  ||  ||  ||  ||  ||  || Bluetooth LED does not glow. ||
|-
| Latitude 5290 2-in-1 || 2022-05 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Latitude 5490 || 2022-02 ||  || * ||  ||  ||  ||  || Random Screen flicker with i915 *ERROR* CPU pipe A FIFO underrun in kernel logs. Solved with  || *audio mute LED use **[https://bbs.archlinux.org/viewtopic.php?pid=1902231#p1902231 Kernel panic on suspend solved with
|-
| Latitude E5500 || 2016-03-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude E5520 || 2024-01-15 ||  ||  ||  ||  ||  ||  || || Buggy SD card reader
CPU would sometimes get stuck at minimum frequency, fixed with Lenovo ThinkPad T480#CPU stuck at minimum frequency
|-
| Latitude E5430 || 2016-02-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude E5540 || 2016-02-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude E5570 || 2017-02-01 ||  ||  ||  ||  ||  ||  || || BIOS may report incorrect RAM size, OK on UEFI.
|-
| Latitude E5580 || 2018-07-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude E5401 || 2019-10 ||  ||  ||  ||  ||  ||  ||  || Poor thermal design (i7 i7-9850H CPU @ 2.60GHz)
|-
| Latitude E5270 || 2023-10-11 ||  ||  ||  ||  ||  ||  ||
|-
| Latitude E6220 || 2016-02-01 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Latitude E6230 || 2018-12 ||  ||  ||  ||  ||  ||  || RFID reader requires enabling RFID radioTouchpad (alps a10) shaky ||
|-
| Latitude E6410 || 2018-06-01 ||  ||  ||  ||  ||  ||  || Fingerprint Sensor not functioning, no drivers seem to exist || *Suspension on closing the lid not working right
|-
| Latitude E6410 (BIOS A16)|| 2018-08-01 ||  ||  ||  ||  ||  ||  || SD card reader is unreliable. For advanced touchpad functionality see Touchpad Synaptics ||
|-
| Latitude E6420 || 2011-08-19 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Latitude E6430 || 2018-12 ||  ||  ||  ||  ||  ||  || colspan=2 | Touchpad shaky, use  for smartcards and enable NFC/RFID if needed.
|-
| Latitude E6530 || 2014-10-01 || * ||  ||  ||  ||  ||  || || *If Optimus is enabled, output is VGA only, otherwise HDMI works when NVIDIA GPU is disabled in BIOS.
|-
| Latitude E7270 || 2017-01-01 ||  ||  ||  ||  ||  || * || || *After UEFI updateHigh suspend usage with power share port active
|-
| Latitude 7370 || 2026-05-05 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude 7390 ( 2-in-1 )  || 2019-02-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude E7440 || 2019-05-11 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude E7450 || 2016-03-01 ||  ||  ||  ||  ||  ||  || Modem: NoSynaptics touchpad + stick. || *Hibernate does not work
|-
| Latitude E7470 || 2021-01-25 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude 3500 || 2020-10-28 ||  ||  ||  ||  ||  ||  || Fingerprint reader works with proprietary driver. || See linked article for more details
|-
| Latitude 5580 || 2017-11-06 ||  ||  ||  ||  ||  || * || || *Needs BIOS update (with fwupd) to avoid occasional black screen when resuming
|-
| Latitude 5420 || 2023-04-20 ||  ||  ||  ||  ||  ||  || Fingerprint reader works with proprietary  ||
|-
| Latitude 5520 || 2024-03-24 ||  ||  ||  ||  ||  ||  || Fingerprint reader works with proprietary  ||
|-
| Latitude 7280 || 2024-05-07 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Latitude 7420 || 2020-10 ||  ||  ||  ||  ||  || * || || *See: https://github.com/intel/thermal_daemon/issues/341
|-
| Latitude 7430 || 2026-01-30 ||  ||  ||  ||  ||  ||  ||  || S3 sleep is not supportedWhen resuming from hibernation, system freezes a lot unless swap is disabled after resumption
|-
| Latitude 7480 || 2019-11-07 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Latitude 7490 || 2019-05-11 ||  ||  ||  ||  ||  ||  || ||
|-
| Latitude 5511 || 2020-10 ||  ||  ||  ||  ||  ||  || colspan=2 | Fix freezes with
|-
| Latitude 3420 || 2022-02-04 ||  ||  || ||  ||  ||  || ||
|-
| Latitude 7450 || 2025-07-08 ||  ||  ||  ||  ||  ||  || Webcam does not work. Shows up as multiple inpu6 devices|| Fingerprint reader requires .
|-
| Latitude 3310 || 2024-11-05 ||  ||  ||  ||  ||  ||  ||  needs to be run for functionality within the Ethernet port (Ethernet through USB works automatically) ||
|}

## Precision
| Precision M4800 || 2024-08-23 || * ||  ||  ||  || ** || *** || colspan=2 | * may be required to boot.** needed.***power-profiles-daemon required
|-
| Precision M6700 || 2017-01-01 ||  ||  ||  ||  ||  ||  || colspan=2 | Occasional GPU freezes with "GPU has fallen off the bus" errors since kernel 4.14.15-1 and NVIDIA 387.34
|-
| Precision 7710 || 2017-11-01 ||  ||  ||  ||  ||  ||  || colspan=2 | Suspend works without hard drive password. is very slow.kernel≥5.12.9 or nvidia≥465.24.02-5 causes no display to be seen after X launches. DFP-2 shows as disconnected.
|-
| Precision 7760 || 2024-05-06 ||  ||  ||  ||  ||  ||  || colspan=2 | S3 Sleep is disabled in ACPI, can be re-enabled by injecting modified ACPI DSDT via acpi_override. Edit the dsdt.dsl file to remove the if statement for S3 state. However many ACPI errors result from this.
|-
| Precision 7780 || 2024-09-12 ||  ||  ||  ||  ||  ||  || colspan=2 | S3 Sleep is disabled in ACPI; modified ACPI DSDT untested.
|-
| Precision 5510 || 2020-04-01 ||  ||  ||  ||  ||  ||  || colspan=2 | Essentially the same device as the Dell XPS 15 (9550)
|-
| Precision 3530 || 2020-07-01 ||  ||  ||  ||  ||  ||  || colspan=2 | You need to disable early microcode loading. Upgrade Thunderbolt controller to latest firmware from Windows and optionally disable Thunderbolt security within the BIOS (e.g. for TB16 docking station).
|-
| Precision 3531 || 2017-08-27 ||  ||  ||  ||  ||  ||  || || Needs
|-
| Precision 5520 || 2018-02-01 ||  ||  ||  ||  ||  ||  || colspan=2 | Essentially the same device as the Dell XPS 15 (9560)
|-
| Precision 5530 || 2023-02-21 ||  ||  ||  ||  || * ||  || colspan=2 | *Needs occasional driver reloads with . Need to change sleep state as per Dell XPS 15 (9570).
|-
| Precision 5570 || 2022-05-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Precision 5760 || 2023-12-24 ||  ||  ||  ||  ||  ||  || ||
|}

## Pro
| Pro 14 Plus (PB14250) || 2026-03-11 ||  ||  ||  ||  ||  ||  ||   || - Fingerprint needs libfprint-tod (see fprint page)
- *The webcam should work with a custom kernel patch (IPU7)
|}

## Studio
| Studio 1749 || 2013-01-04 ||  || * ||  ||  ||  ||  || || *Add  to
|-
| Studio XPS M1640 || 2009-08 ||  ||  ||  ||  ||  ||  || ||
|-
| Studio 1555 ||  2013-04-30 ||  ||  ||  ||  ||  ||  || ||
|}

## Vostro
| Vostro 1310 || 2009-06-24 ||  ||  ||  ||  ||  ||  || ||
|-
| Vostro 1320 || 2009-12-04 ||  ||  ||  ||  ||  ||  || colspan="2"
|-
| Vostro 1000 || 2011-03-28 ||  ||  ||  ||  ||  ||  || || Add  if resume does not work after suspend
|-
| Vostro 5481 || 2019-11-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Vostro 3360 || 2017-11-21 ||  ||  ||  ||  ||  ||  || ||
|-
| Vostro 3583 || 2019-12-21 ||  ||  ||  ||  ||  ||  || || Reload  after resuming from sleep if Wi-Fi stops working
|-
| Vostro 3530 || 2023-01-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Vostro 3560 || 2020-02-01 ||  ||  ||  ||  ||  ||  || ||
|-
| Vostro 5590 || 2021-01-23 ||  ||  ||  ||  ||  || || ||
|-
| Vostro 7500 || 2020-10-16 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Vostro 7620 || 2022-09-05 ||  ||  ||  ||  ||  ||  || Fingerprint reader requires  ||
|}

## XPS
| XPS L322 || 2013-03 ||  ||  ||  ||  ||  ||  || colspan=2 | ALPS Touchpad recognized only as PS/2 mouse, two-finger scroll, finger tap-to-click, etc... does not work.
|-
| XPS M1330 || 2021-01 ||  ||  ||  ||  ||  || * || || *acpi_cpufreq see: forums
|-
| XPS 13 (9333) || 2016-16-16 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 13 (9310) || 2016-16-16 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 13 (9315) || 2022-11-26 ||  ||  ||  ||  ||  ||  ||  ||
|-
| XPS 13 (9343) || 2016-16-16 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 13 (9350) || 2016-11-16 ||  ||  ||  ||  ||  ||  || || Apply firmware updates
|-
| XPS 13 (9360) || 2016-11-16 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 13 (9370) || 2018-05-29 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 13 (9380) || 2020-06-19 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 13 2-in-1 (9365) || 2017-10-22 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 13 (7390) || 2019-12-21 ||  ||  ||  ||  ||  ||  ||  ||
|-
| XPS 13 (9350) 2024 || 2025-06-10 ||  ||  ||  ||  ||  ||  || IR camera not work || Apply firmware updates
|-
| XPS 13 2-in-1 (7390) || 2019-09-01 ||  ||  ||  ||  ||  ||  ||  || System freezes on boot. See device page for fix.
|-
| XPS 15 || 2016-11-17 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 17 (9700) || 2020-09-18 ||  ||  ||  ||  ||  ||  || ||
|-
| XPS 17 (9710) || 2023-04-23 ||  ||  ||  ||  ||  ||  || || Touchpad input may sometimes feel slow, potential fix is to update the touchpad driver in Windows. See Dell XPS 17 (9710)#Touchpad
|-
| XPS 13 2-in-1 (9310) ||  2021-03-24 ||  ||  ||  ||  ||  ||  || colspan="2" | Fingerprint reader  unsupported, other model needs  or
|}

## G3
| G3 15 3590 || 2020-19-10 ||  ||  ||  ||  ||  ||  || CUDA is not working with Linux 5.9 || Works well with , follow their page on power management.
|}

## G5
| G5 5590-9340 || 2020-08-20 ||  ||  ||  ||  ||  ||  ||  || *drivers might be extracted from Ubuntu image of this laptop
|}

## G7
| G7 7700 || 2022-05-17 ||  ||  ||  ||  ||  ||  ||  || No fine backlight control, no RGB control
|}

## G15
| G15 5511 || 2025-10-18 ||  ||  ||  ||  ||  ||  ||  ||  can be used for lights and fans control
|-
| G15 5515 AMD EDITION || 2022-02-12 ||  ||  ||  ||  ||  ||  || || Touchpad disables randomly on boot, create
|-
| G15 5520 NVIDIA || 2022-08-30 ||  ||  ||  ||  ||  ||  || ||
|-
| G15 5525 || 2023-03-10 ||  || * ||  ||  ||  ||  || ||
|-
| G15 5530 || 2025-08-09 ||  ||  ||  ||  ||  ||  ||   ||  can be used for lights and fans control

|}

## G16
| G16 7630 || 2023-01-03 ||  ||  ||  ||  ||  ||  || ||  works fine for fan control and G-Mode. Screen brightness control works through
|}
