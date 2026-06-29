# Laptop/Other

## Avell
| A40 LIV
| 2022-04-13
|
|
|
|
|
|
|
| Small annoyances with brightness during reboot.
|-
| A70 MOB RTX 3050/3060
| 2022-09-18
|
|
|
|
|
|
|
| *Performance is severely affected after waking from suspend, solution on the forums.
|-
| Storm 450r / ION A52r (R7-7435HS)
| 2026-02-10
|
|
|
|
|
|
|
|
|-
| Storm 350r / HYB A52r (R7-7435HS)
| 2026-02-10
|
|
|
|
|
|
|
|
|}

## Casper
| Nirvana X600.5700
| 2024-01-24
|
|
|
|
|
|
| Internal keyboard only works with some kernel versions. See BBS#291569
| Add  kernel parameter to fix internal keyboard.
|}

## Chuwi
| Corebook X (2022)
| 2022-06-26
|
|
|
|
|
| , battery undetected
| Camera works
|-
| MiniBook X (2023)
| 2023-09-24
| *
|
|
|
|
|
|
| *Screen rotation needs to be set up to work correctly
|-
| MiniBook X N100 (2023)
| 2023-12-29
|
|
|
|
|
|
| Camera works,
dual accelerometer does not work*
| *Screen rotation needs a workaround, tablet mode is impossible.
|}

## Clevo
| NP50DB || 2020-09-25 ||  ||  ||  ||  ||  ||  || || Keyboard LEDs work with .
|-
| N130BU || 2017-12-27 ||  ||  ||  ||  ||  ||  || Touchpad works with libinput but awkard default config ("Tapping" disabled)
|| Many small annoyances as some functionalities are not working out of the box.
|-
| M350 || 2006-01-05 ||  ||  ||  ||  ||  ||  ||  || Front panel keys does not work
|-
| W150HRM || 2011-08-19 ||  ||  ||  ||  ||  ||  || ||
|-
| W110ER || 2013-04-01 ||  ||  ||  || * || ||  ||  || *Unreliable on some 802.11n networks: workaround by disabling 802.11n with Tested only in BIOS mode, not in UEFI.
|}

## Colorful
| Colorful X15 AT (2023)|| 2023-03-15 ||  ||  ||  ||  || ||  || Keyboard shortcuts and backlight needs  || No manual fan speed control.
|}

## Cube
| KNote i1101 || 2018-01-11 ||  ||  ||  ||  || ||  || Touchscreen needs , Camera does not work || Accelerometer needs  kernel module.
|}

## Eve/Dough
| Eve V (2017) (i7 version) || 2022-08-23 ||  ||  ||  ||  || ||  || Camera does not work || Accelerometer needs
|}

## Fujitsu
| Lifebook WU4/H1
| 2023-06-03
|
|
|
|
|
|
| Fingerprint reader: Yes.
|
|-
| Lifebook U747
| 2023-01-01
|
|
|
|
|
|
| Internal keyboard requires  in the initramfs to be reliably detected at boot.
| *The device does not wake again. Otherwise, the suspend process seems to work.
|-
| Lifebook T902
| 2017-08-01
|
|
|
|
|
|
| Touchscreen drivers needs to be manually removed and re-added after suspend.
| Rotation lock, A and B buttons do nothing.Tablet mode essentially unusable: rotating screen and disabling the keyboard / touchpad automatically does not work.
|-
| Lifebook T904
| 2014
|
|
|
|
|
|
| The fingerprint reader does not appear to be a supported model. If unused, consider disabling physically in the BIOS.
| Update BIOS to version 1.08 to fix fan noise.
|-
| Amilo Se 1520
| 2007
|
| *
|
|
|
|
|
| *SPDIF and external microphone do not work. Internal microphone cannot be disabled and has no volume control.Special buttons on the left side of the keyboard do not work out of the box.
|-
|}

## Suspend issue
The Fujitsu Lifebook U9311 and other Tiger Lake/Alder Lake Fujitsu laptops face a long-standing BIOS bug related to Intel graphics since 2021. See Fujitsu Lifebook U9311#Suspend.

## Gateway
| MX6961 || 2007-05 ||  ||  ||  ||  ||  ||  ||  || Fn keys for brightness and volume are unsupported.
|}

## Gigabyte
| Aero 14k
| 2018-02-07
|
|
|
|
|
|
|
| Reset the BIOS to Windows 7 settings to boot the ArchISO.
Macro keys have to be defined using the windows application.
|-
| P34G v2 aka XMG C404
| 2020-06-27
|
|
|
|
|
|
|
| Touchpad intermittent on boot/reset with XMG firmware, works fine with attempted coreboot port, but could not figure out power management: device runs hot
|-
| Aero 15 Classic XA
| 2021-11-12
| *
|
|
|
|
|
|
| *very low performance with HDMI, use Thunderbolt 3 docking station instead.To use the webcam, enable the webcam option in BIOS manually (from default 'AUTO').Macro keys have to be defined using the windows application.
|-
| Aorus 17 XE4
| 2022-08-18
|
|
|
|
|
|
| colspan="2" | Wake-from-suspend issue needs a workaround, and using NVIDIA's proprietary driver (i.e. not ).Kernel parameters  may also be necessary.
|-
| U4
| 2023-02-12
|
|
|
|
|
|
|
| Update to newest UEFI version to (partially) fix freezes on the GRUB menu when interacting or opening its' terminal. External USB keyboards will not work on the UEFI or grub menu.
Default NVME drive (ESR512GTLG-E6GBTNB4) has a very fragile firmware. If issued any NVME or S.M.A.R.T command, all filesystems fail to mount. The only known fix is to reboot. Also does not support any kind of namespace manipulation.
|-
| Aorus 5 SE4
| 2025-05-07
|
|
|
|
|
|
|
| Some Fn key combo's not working. Fn is read as Touchpad off by default need to disabled as shortcut in DE. Need further testing
|}

## Honor
| Honor MagicBook Pro AMD || 2023-07-12 ||  ||  ||  ||  ||  ||  ||
|}

## Lunnen
| Ground 16
| 2024-02-13
|
|
|
|
|
|
|
| Add  to the kernel parameters to fix flickering screen after sleep and  to fix not working keyboard. Do not forget to turn off Fastboot in BIOS when you disable pnpacpi.
|}

## Mechrevo
| S2 Air || 2020-08-05 || * ||  ||  ||  ||  ||  || || *HDMI 2.0 (4K@60FPS) is noisy, favor HDMI 1.4 (4k@30FPS or lower)
|-
| Code 01 (Tongfang PF5NU1G) || 2020-10-14 ||  ||  ||  ||  ||  ||  || ||  does not seem to have any effect
|-
| Code 01 v2 (Ryzen 7 6800H ver, 2022) || 2024-01-29 ||  ||  ||  ||  ||  ||  || || Needs to configure CPU from bios before install
|-
| WUJIE14X || 2025-07-10 ||  ||  ||  ||  ||  ||  || ||
|-
| WUJIE14S || 2024-09-14 ||  ||  ||  ||  ||  ||  || ||  for UEFI,  for boot entries.  switch performance mode (EC controlled, independent of OS).  does not have a second layer.
|}

## Packard Bell
| dot SE || 2018-09-30 ||  ||  ||  ||  ||  ||  || || See Touchpad Synaptics for advanced functionality
|}

## Panasonic
| Panasonic CF-RZ6 || 2024-03-28 ||  ||  ||  ||  ||  ||  ||  ||
|}

## Positivo
| Positivo Vision R15
| 2025-1-18
|
|
|
|
|
|
|
|
|}

## Purism
| Librem 15v4 || 2019-07-26 ||  ||  ||  ||  ||  ||  || || See https://puri.sm/products.Might be applicable to Librem 13v4 too.
|}

## Starlabs
| Starlite || 2024-11-21 ||  ||  ||  ||  ||  ||  || || Blacklist  to fix random hangs at boot, suspending and resuming
|-
| Starbook  7 || 2024-08-01 ||  ||  ||  ||  ||  ||  || || can't update firmware with
|}

## Teclast
| X16 Pro || 2017-12-25 ||  ||  ||  ||  ||  ||  ||  || Add  to the kernel parameters to avoid instability
|-
| X98 Plus II || 2018-04-23 ||  ||  ||  ||  ||  ||  ||  ||
|-
| X5 Pro || 2017-04-20 ||  ||  ||  ||  ||  ||  ||  ||
|}

## Xiaomi
| RedmiBook 14 ii AMD
| 2020-07-08
|
|
|
|
|
|
|
| *patch ACPI tables to add deep sleep
|}

## Zwide
| N8 Pro
| 2026-04-22
|
|
|
|
|
|
|
|
|}
