# Lenovo ThinkPad T495

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| TrackPoint ||  ||
|-
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Mobile broadband || ||
|-
| Fingerprint scanner ||  ||
|-
| MicroSD Reader ||  ||
|-
| Smartcard Reader ||  ||
|-
| TPM ||  ||
|}

## Fingerprint sensor
The fingerprint sensor works: use fwupd to install the latest firmware for "Synaptics Prometheus Fingerprint Reader".

fprint has more details on how to setup the fingerprint, for PAM-based authentication for example.

## Battery and power management
TLP prevents plugged in USB devices from working when running on battery. This can be fixed by blacklisting power management of the USB3.1 PCI device in TLP. Find the proper USB IDs via:

and create the following:

## Ethernet connection
Some models might have issues in noticing ethernet's link state changes (cable connect/disconnect events) when running on battery.

The issue can be noticed by trying to connect the ethernet cable while the computer is running on battery: if there is no connection until you connect the power cable you are affected.

To fix the issue one can try blacklisting the  module by appending the following line to :

Install then the  package (or  if running the , or  for other kernels).

Reboot and the problem should be gone.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || Enables Fn lock
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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Keyboard settings
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggle Keyboard Backlight
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.

## Known issues
The following issues are commonly seen even with recent kernels such as 5.9.3:

## Kernel warning: irq 7: nobody cared
Please see https://bugzilla.kernel.org/show_bug.cgi?id=201817 for more information.

## Kernel warning: nvme_poll_irqdisable
Please see https://bugzilla.kernel.org/show_bug.cgi?id=202891 for more information.

## Kernel warning: pending airtime underflow
Please see https://bugzilla.kernel.org/show_bug.cgi?id=205869 for more information.

## Kernel error: pci 0000:00:00.2: AMD-Vi: Unable to read/write to IOMMU perf counter.
It seems like this message could be ignored, i.e. treated as a warning.

Please see Gentoo:Lenovo Thinkpad T495#Unable to write to IOMMU and https://bugzilla.kernel.org/show_bug.cgi?id=201753 for more information.

## Kernel error: tpm tpm0: Bug: TPM interrupt not working, polling instead.
As a workaround you can turn off the TPM in BIOS settings.

Please see https://bugzilla.kernel.org/show_bug.cgi?id=204121 and https://bugzilla.redhat.com/show_bug.cgi?id=1770021 for more information.

## Kernel error: Bug: TPM interrupt not working, polling instead
As a workaround you can turn off the TPM in BIOS settings.

Please see https://bugzilla.kernel.org/show_bug.cgi?id=204121 and https://bugzilla.redhat.com/show_bug.cgi?id=1770021 for more information.

## Kernel error: *ERROR* mstb 000000002ef7ea2e port 3: DPCD read on addr 0x60 for 1 bytes NAKed
 drm_kms_helper *ERROR* mstb 000000002ef7ea2e port 3: DPCD read on addr 0x60 for 1 bytes NAKed

Please see https://bugzilla.redhat.com/show_bug.cgi?id=1874782 for more information.

## systemd-modules-load: Failed to find module 'platform-integrity'
You can comment or remove loading of  module.

Please see https://forum.endeavouros.com/t/failed-to-find-module-platform-integrity-after-update/9279/10 for more information.

## Kernel error: drm_kms_helper *ERROR* CRTC:67:crtc-0 flip_done timed out
Occasionally after resuming from sleep, the display freezes with the following showing up in the kernel log:

There is currently no known workarounds for this issue. https://gitlab.freedesktop.org/drm/amd/-/issues/1000
