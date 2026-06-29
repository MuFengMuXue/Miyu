# Intel NUC

Next Unit of Computing (NUC) is a small-form-factor (SFF) PC designed by Intel and is based on soldered-on low-power Celeron, Pentium, i3, i5 and i7 CPUs. Its motherboard measures 4 × 4 inches (10.16 × 10.16 cm).

The barebone kits consist of the board, in a plastic case with a fan, an external power supply and VESA mounting plate. Intel does offer for sale just the NUC motherboards, which have a built-in CPU, although (as of 2013) the price of a NUC motherboard is very close to the corresponding cased kit; third-party cases for the NUC boards are also available.

## Installation
Follow usual installation guide procedures.

It is highly recommended to update the board BIOS prior to installation. See official Intel BIOS update instructions for details.

## NVMe
Intel NUCs support NVMe drives connected to the PCIe M.2 connector. See Solid State Drives/NVMe.

## Graphics
Most NUCs use integrated Intel graphics. See Hardware video acceleration to use it on supported NUC models.

## Wireless
Most NUC wireless adapters should work out of the box. Make sure relevant firmware is loaded. See Wireless network configuration#iwlwifi for details.

## LEDs
Some NUCs have LEDs which can be controlled by software by installing the kernel driver  or intel_nuc_led. To use this, Software Control must be enabled in the BIOS Power settings.

## Performance
## Boot
Fastest boot times are achieved with UEFI boot and disabling legacy boot in the BIOS settings.

## 4K
If you want to use 4K graphic output, open the BIOS settings and set Devices and Peripherals > Video > IGD Minimum Memory to 512 MB and IGD Aperture Size to 1024 MB.

## Power management
It is possible to reduce power usage, see TLP and Powertop.

## Troubleshooting
## Hades Canyon NUC - no external microphones
External microphones being plugged into the front or back 3.5mm jack may not appear in PulseAudio (only the Internal Microphone array will be used).

To fix this, use  as explained in Advanced Linux Sound Architecture/Troubleshooting#Wrong model autodetection.

Reboot the device, and three new input devices should be listed under Input Devices, Built-in Audio Analog Stereo - Internal Microphone, Headset Microphone, and Microphone.

## TPM
The Intel specifications for some NUC devices indicate that TPM is unavailable. However, those devices are often capable of TPM 2.0 features through a firmware-based implementation called Intel PTT. Storing and retrieving values works as one would expect from a TPM chip.

## Poweroff
After issuing a shutdown, the NUC might remain in some state which is not completely shut down, as indicated by a remaining blue power LED. In this case it is necessary to power off the unit by holding the power button for a few seconds.

The workaround for this issue is to disable all wake-on-CIR (infrared sensor) options in the BIOS. In some cases it might be required to disable the CIR sensor completely to fix the issue.

## iSCSI boot
Following the procedure outlined in iSCSI/Boot.

Chroot into the iSCSI target root, and modify these two configuration files:

{{hc|1=/etc/initcpio/install/iscsi|
2=build () {
        map add_module iscsi_tcp iscsi_ibft libiscsi libiscsi_tcp scsi_transport_iscsi crc32c e1000e
        add_checked_modules "/drivers/net"
        add_binary iscsistart
        add_runscript
}

help () {
cat <<HELPEOF
        This hook allows you to boot from an iSCSI target.
HELPEOF
}
}}

{{hc|1=/etc/initcpio/hooks/iscsi|2=
run_hook () {
        modprobe iscsi_tcp
        modprobe e1000e
        msg "Mounting iSCSI target"
        iscsistart -i INITIATOR_NAME -t TARGET_NAME -g 1 -a PORTAL_IP_ADDRESS -d 1
}
}}

Then, regenerate the initramfs.
