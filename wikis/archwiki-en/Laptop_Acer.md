# Laptop/Acer

## Model list
## Aspire
| Aspire 5100-3825
| 2006-12-18
|
|
|
|
|
|
|
|
|-
| Aspire A314-35
| 2025-07-15
|
|
|
|
|
|
|
| ASPM not available for power managment.
|-
| Aspire 1501LMi
| 2007-08-01
|
|
|
|
|
|
|
|
|-
| Aspire 5024
| 2006-05-23
|
|
|
|
|
|
|
| Suspend: Video and Wi-Fi problems
|-
| Aspire 7720
| 2009-02
|
|
|
|
|
|
|
| Update BIOS to fix ACPI and wireless problems. Hibernation is flaky (often hangs in the middle of restoring). Card reader only accepts SD cards. Special keys (Acer Arcade, direct access to browser/mail) seem to not work.
|-
| Aspire v5-171
| 2013-10-06
|
|
|
|
|
|
|
|
|-
| Aspire 5745(P)G
| 2014-04-20
|
|
|
|
|
|
|
| Update to BIOS v1.15 to see battery informations.
|-
| Aspire E5-573
| 2015-12
|
|
|
|
|
|
|
|
|-
| Aspire 7730
| 2009-08
|
|
|
|
|
|
|
| Add  to  to get headphone output working. Fix CD boot problem with  at ramfs.
|-
| Aspire 4935
| 2009-08
|
|
|
|
|
|
|
| Audio "hot key"/"touch panel" does not work.
|-
| Aspire 2920Z
| 2009-02
|
|
|
|
|
|
|
| Blue e on the left.
|-
| Aspire 5735z
| 2014-09-03
|
|
|
|
|
|
|
|
|-
| Aspire E1-531
| 2016-07-01
|
|
|
|
|
|
|
|
|-
| Aspire V3-371
| 2015-07-06
|
|
|
|
|
|
|
| See #Flaky Secure Boot
|-
| Aspire V3-372
| 2016-09-29
|
|
|
|
|
|
|
| See #Flaky Secure Boot. Set touchpad to basic in BIOS, then enable it with .
|-
| Aspire V3-572G
| 2017-09-11
|
|
|
|
|
|
|
| Suspend/resume does not work with Nvidia proprietary drivers ("gpu has fallen off the bus"). To fix, append  to kernel parameters. Headphone microphone does not work. To fix, create a file on /etc/modprobe.d and insert
|-
| Aspire F5-573G-7791
| 2016-12-01
|
|
|
|
|
|
|
| See #Flaky Secure Boot. Reportedly fixed on firmware update 1.31.
|-
| Aspire E5-575G-5538
| 2017-02-01
|
|
|
|
|
|
|
| See #Flaky Secure Boot.
|-
| Aspire E5-553-T337
| 2018-08-07
|
|
|
|
|
|
|
|
|-
| Aspire E5-422G-68PL
| 2020-07-21
|
|
|
|
|
|
|
| Sleep & Hibernation issues when R5 GPU gets used in any way. Disable "Advanced Features" for the Touchpad in BIOS to unlock more functions than with it on Windows.
|-
| Aspire 3 A315-41-R09T
| 2019-03-01
|
|
|
|
|
|
|
| Add  to fix erratic behavior and freezing at boot or shutdown. Using  only during installation is suggested.
|-
| Aspire 3 A315-51-524S
| 2019-11-11
|
|
|
|
|
|
|
|-
| Aspire 3 A315-510P
| 2024-02-08
|
|
|
|
|
|
|
| Use acer-wmi-battery for battery health control. Secure boot with custom keys works.
|-
| Aspire 3 A315-53G-52A4
| 2019-11-01
|
|
|
|
|
|
|
|
|-
| Aspire E5-476G
| 2019-06-01
|
|
|
|
|
|
|
|
|-
| Aspire 5 A515-51G-5072
| 2024-02-17
|
|
|
|
|
|
|
| - Reboot the laptop if bootable USB fails to get recognized. - Add  and  as kernel parameters to supress boot log spam. - Add  in NetworkManager config to prevent WiFi throttling. - Use EnvyControl to shut off Nvidia dGPU. - Hibernate does not work.
|-
| Aspire 5 A515-56-5952
| 2025-07-26
|
|
|
|
|
|
|
| On old kernel versions, may need to disable VMD in BIOS to improve battery life (use  to show hidden settings).Hibernation works. S3 sleep support is flaky. Some have had success downgrading the BIOS to v1.28.S0ix sleep does not work - though fans & LEDs turn off, the laptop only reaches C10 when put to sleep. Battery life in sleep mode is therefore limited.
|-
| Aspire A514-53
| 2023-05-19
|
|
|
|
|
|
|
|
|-
| Aspire A515-45-R5SM
| 2023-06-10
|
|
|
|
|
|
|
| Fingerprint reader only seems to work occasionally
|-
| Aspire A514-55
| 2024-05-17
|
|
|
|
|
|
|
|
|-
| Aspire 5 Spin A5SP14-51MTN
| 2024-04-05
|
|
|
|
|
|
|
|-
| Aspire VX5-591G
| 2025-03-01
|
|
|
|
|
|
|
|
|-
| Aspire A15-41M
| 2025-04-05
|
|
|
|
|
|
|
| Drive advertises OPAL support, but if the drive loses power (including during hibernation), the UEFI discards the entire drive trying to probe for a filesystem in the encrypted region, even when it is marked as "Hidden for EFI", which is against spec. One can  never shutdown/hibernate. Tested on UEFI: 1.08, 1.10
|-
| Aspire A315-510P
| 2025-10-14
|
|
|
|
|
|
|
| Uses an UFS drive, requires adding  to /etc/mkinitcpio.conf
|-
| Aspire A515-57
| 2025-11-16
|
|
|
|
|
|
|
| s2idle sleep drains battery quickly (cause unknown), s3 works as expected
|-
| Aspire AG15-42P
| 2026-03-26
|
|
|
|
|
|
| Secure boot prevents boot from usb
| MT7902 driver not yet implemented in current kernel, expected in 7.1, current fix is external link
|}

## AspireOne
| AspireOne D255e
| 2011-04-27
|
|
|
|
|
|
|
|
|-
| Aspire One Cloudbook 11
| 2016-08
|
|
|
|
|
|
|
| See #Flaky Secure Boot.
|}

## Travelmate
| Travelmate 6292
| 2008-06-24
|
|
|
|
|
|
|
|
|-
| Travelmate 4750
| 2013-08-17
|
|
|
|
|
|
|
|
|-
| TravelMate 8371G (TM8371G-944G32n)
| 2010-05
|
|
|
|
|
|
|
| No fan control. Suspend to RAM requires . Fingerprint reader does not seem to have a driver.
|-
| TravelMate TimelineX 8473T
| 2016-02-01
|
|
|
|
|
|
|
| Sound, sleep, wireless, brightness require configuration.
|}

## Nitro
| Nitro VN7-791G-74DL
| 2016-01-01
|
|
|
|
|
|
|
| Fan control requires porting drivers from windows
|-
| Nitro VN7-792G-710p
| 2016-10-01
|
|
|
|
|
|
|
|
|-
| Nitro VN7-792G-751Y
| 2016-12-01
|
|
|
|
|
|
|
| *HDMI and Microphone do not work
|-
| Nitro VN7-572G
| 2019-02-01
|
|
|
|
|
|
|
| Sound Recording: problem seems already reportedSee #Flaky Secure Boot.
|-
| Nitro VN7-571G-51R8
| 2024-07-15
|
|
|
|
|
|
|
|
|-
| Nitro AN515-43
| 2022-02-01
|
|
|
|
|
|
|
| For fan control, use
|-
| Nitro AN515-45
| 2022-09-06
|
|
|
|
|
|
|
| For better power optimization, use . For fan control, use  with AN515-43 configuration. For switching between GPUs see PRIME#PRIME render offload.
|-
| Nitro ANV15-41
| 2025-11-30
|
|
|
|
|
|
|
| After installing  or Div-Acer-Manager-MAX firmware setup may become inaccessible due to reverse-engineered WMI drivers corrupting ACPI settings.
|}

## Predator
| Predator Helios 300, PH315-53
| 2021-07
|
|
|
|
|
|
|
|
|-
| Predator Helios 500, PH517-61
| 2022-09
|
|
|
|
|
|
| ITE8987 SuperIO not supported:
* PWM Fan speed cannot be manually set
* Cannot read fan speed
* Cannot set RGB lighting for keyboard
* Cannot turn border lighting around trackpad on and off
* Predator quicklaunch keys does not function
|
|}

## Swift
| Swift 3 SF315-52-52YN
| 2020-09-05
|
| *
|
|
|
|
|
| *See Acer Swift 5#Kernel modules parameters
|-
| Swift 5 SF515-51T
| 2019-06-01
|
| *
|
|
|
|
|
| *See Acer Swift 5#Kernel modules parameters
|-
| Swift Go SFG16-72
| 2024-10-07
|
|
|
|
|
|
|
| acer-wmi-battery for battery health control
|}

## Enduro
| Enduro N3 EN314-51W-55LW
| 2021-08-28
|
|
|
|
|
|
|
| *See #Flaky Secure Boot and #Switching NVMe mode to AHCI
|}

## Spin
| Spin SP514-51N-70LZ
| 2026-04-26
|
|
|
|
|
| *
|
| *Kernel Parameter - mem_sleep_default=deepAcer-wmi-battery for battery health controlFan Control: nbfc needs a config profileCamera: only detected by plasma-cameraSecure Boot: UntestedFingerprint: Not working
|}
## Troubleshooting
## Flaky Secure Boot
Some models have a peculiar Secure Boot implementation which requires the following workaround to boot successfully the installation medium:

# To start on a clean slate, clear trusted boot loaders within the Secure Boot settings
# Save, reboot, return to UEFI
# Add the boot loader as a trusted UEFI file
## To add a file as a trusted boot loader, you may have to set a supervisor password: do not lose it
# Save, reboot, return to UEFI
# Disables Secure Boot
# The boot loader should now appear in the list even if Secure Boot is disabled

You may have to repeat these steps every firmware update.

## Firmware Setup became inaccessible after Linux installation
Commonly, once a new Linux entry has been added to the EFI partition, trying to access Acer UEFI instead results in being permanently stuck on the loading screen.

This is because the Acer BIOS requires all  files to be marked as trusted, even if Secure Boot is disabled. Therefore, you must first remove them from the bootable entries to regain access to the BIOS, then manually mark these files as being safe.

The exact process will depend on your installation. For example:

# Start Arch from a bootable USB.
# Use the  command to remove the non-verified entries.
# Reboot and try to access the BIOS (by pressing ). It should now work.
# If available, enable the F12 Boot Menu option (to use as a fallback next time).
# Enable Secure Boot and set a Supervisor Password.
# Select and mark the  files as trusted for execution.
# Disable Secure Boot and remove the Supervisor Password.
# Reboot and re-enter the BIOS to set up again the appropriate boot priority order.

At that point, both the Linux boot loader and the Acer BIOS should be accessible without issues.

## Aspire 3 A315-56 internal storage not showing up
The firmware has a bug where you cannot see the internal SATA storage after first booting up. At boot, the boot loader can see the internal storage but the initial ramdisk is unable to see it due to this bug.

The only known solution to this is suspending and waking it up.

Add an early custom hook to put the laptop to sleep before the step to mount the filesystems:

{{hc|/etc/initcpio/install/suspend-to-ram|
#!/bin/bash
build() {
        add_binary date
        add_runscript
}
help() {
        echo "Suspend to RAM before filesystems get mounted so the initial ramdisk can see the internal storage"
}
}}

{{hc|/etc/initcpio/hooks/suspend-to-ram|2=
#!/bin/bash
run_hook() {
        FILE='/sys/class/rtc/rtc0/wakealarm'
        EPOCH_TIME="$(date '+%s')"
        if ! echo 0 > "$FILE"; then
                reboot -f
        elif ! echo "$((EPOCH_TIME + 2))" > "$FILE"; then
                reboot -f
        elif ! echo mem > /sys/power/state; then
                reboot -f
        fi
}
}}

This custom hook will reset the RTC alarm clock and set an alarm 2 seconds into the future for device wake-up, so you do not have to manually wake-up the laptop.

Add it the mkinitcpio HOOKS:

Finally regenerate the initramfs.

## Switching NVMe mode to AHCI
Linux does not support Optane with RAID NVMe mode which is default on some devices. The workaround is to swich NVMe mode to AHCI.

One can switch the mode on the Main tab of BIOS setup. This option is hidden by default and unavailable until Supervisor password set.

To set Supervisor password:

# Enter BIOS setup by pressing  on boot-up.
# Navigate to Security tab.
# Select Set Supervisor Password option.
# Enter the new password.
# Exit BIOS setup saving changes.

To change NVMe mode (might not be possible until Supervisor password set):

# Enter BIOS setup by pressing  on boot-up.
# Enter Supervisor password.
# Navigate to Main tab.
# Hit . Option SATA mode will appear.
# Set SATA Mode to AHCI.
# Exit BIOS setup saving settings.

## Mode key and fan speed monitoring are not working for some gaming laptops
If your laptop uses predator sense app v4 or newer on windows, but mode key and fan speed monitoring are not working on linux, try  kernel module parameter to enable these features. And you can change mode key's behavior (toggling turbo mode or rotating each mode) using .
