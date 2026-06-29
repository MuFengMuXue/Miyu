# Lenovo ThinkPad X1 Extreme

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Webcam || ||
|-
| Ethernet || ||
|-
| Bluetooth || ||
|-
| Card reader || ||
|-
| Audio || ||
|-
| Wireless || ||
|-
| Thunderbolt || ||
|-
| Fingerprint reader ||  ||
|}

## Firmware update
A UEFI firmware update is strongly recommended for general use of the laptop - the initial 1.13 version devices seem to ship with contains multiple bugs that can result in bricking the laptop: Reddit thread discussing the issue; another Reddit thread discussing a different bricking issue.

Firmware updates are available via fwupd, the Lenovo Vantage application on Windows, or from Lenovo's website.

The latest version, v1.35, is highly recommended. All information on this page assumes the latest firmware.

## Video
Both the HDMI port and DisplayPort outputs created when using either a USB-C adapter or Thunderbolt dock are wired to the Nvidia dGPU.

A BIOS setting can be used to disable the integrated GPU, and run everything on the dedicated Nvidia card. The dedicated GPU cannot be disabled through firmware, so enabling runtime power management in some form is highly recommended when using the iGPU.

## CPU thermal throttling
This laptop is affected by a CPU throttling bug when using Linux.

Basically, the laptop's firmware uses an implementation of Intel's Dynamic Platform and Thermal Framework (DPTF) that does not work with Linux. While newer generations of ThinkPads have gotten a BIOS update to fix this, a Lenovo employee confirmed that older affected Thinkpads (including T580, T480, T480s, X1C6, P1G1 and X1E1) will not get the fix.

A stress test using  indicates that the CPU is limited to 38W/80C at boot, resulting in a sustained all-core frequency of around 2850 MHz on the i7-8750H.

## Fix using reverse-engineered DPTF implementation
There is an ongoing effort to reverse-engineer DPTF on Linux. Results can be found here. Most of the work has been upstreamed already, though the implementation is still far from complete.

Starting with kernel 5.12, the work-in-progress can be utilized by installing and enabling , which will attempt to make use of the firmware's adaptive performance policy.

Unfortunately, the current implementation does not appear to help much on this laptop. While the CPU's limit is raised to 45W/83C, the all-core frequency is erratic, resulting in only a marginal performance improvement.

## Fix using dptfxtract and manual DPTF profile setting
Another option, which does result in full performance, is to extract the DPTF tables and use them in combination with a manual change of the DPTF profile.

## Configuring thermald to use extracted dptf tables
First, make sure  is installed. Next, use Intel's proprietary  tool to extract the DPTF tables:

 # dptfxtract

This will populate  with multiple configuration files of the form , each of which represents a converted DPTF table.

The tool also creates a copy of each of these files in the current working directory, so you may want to remove those:

 # rm thermal-conf.xml.*

The thermald service file shipped with Arch Linux enables adaptive mode by default. In order to use the extracted tables we have to override it.

Create the necessary directory if it does not exist already:

 # mkdir -p /etc/systemd/system/thermald.service.d

Then create the following file:

Afterwards, reload the systemd manager configuration and enable thermald.

## Selecting the appropriate configuration
Out of all the generated configuration files, thermald will use  by default. You can try any of the other configurations by adding the  flag to the  created earlier.

The default configuration file already unlocks full performance. A stress test indicates that the CPU is now limited to 45W/95C, resulting in a sustained all-core frequency of around 3300 MHz on the i7-8750H.

## Manually setting a DPTF profile to prevent temporary re-throttling
The setup above is not perfect, every time the CPU temperature trips over 80C the laptop's embedded controller (EC) will re-throttle the CPU for a few seconds.

This issue can be fixed, without 'fighting the EC', by manually setting the adaptive performance DPTF profile using the following script:

Save the script somewhere and create a systemd service for it:

Do not forget to replace  in the service file.

Finally, reload the systemd manager configuration and enable the service.

## Disabling BDPROCHOT to prevent throttling on battery
The laptop's performance on battery is far below expectations when using Linux. The cause appears to be something called 'lap mode' (documented by Lenovo, here).

Basically, when unplugged, the laptop will by default assume that it is being used on the user's lap. And since Linux has no working DPTF implementation to tell the laptop otherwise, it will always assume it is being used the user's lap. Consequently, In order to keep the laptop base at a 'skin friendly' temperature, the laptop's EC throttles the CPU with BDPROCHOT (BiDirectional PROCessor HOT) when one of many thermal sensors trips a predetermined value. Effectively this will keep the CPU at around 70C max while simultaneously preventing the fans from properly spinning up. A repeated on-again off-again all-core stress test causes the CPU to throttle as low as 800 MHz.

Since there is currently no known way to disable 'lap mode', the only path to full performance on battery is to disable BDPROCHOT altogether. This can be done using the following script:

Save the script somewhere and create a systemd service for it:

A suspend/resume-cycle will cause the EC to re-set the BDPROCHOT-bit.

Create the following file (and make it executable) to run the script on resume:

Do not forget to replace  in both files.

Finally, reload the systemd manager configuration, enable the service and reboot.

The CPU's performance on battery should now be roughly equal as when plugged in.

## Microphone noise reduction
PulseAudio's PulseAudio#Microphone echo/noise cancellation can be used to reduce the amount of microphone noise by adding the following to :

The above mic_geometry is specific to the X1 Extreme.

The module-filter-heuristics and module-filter-apply modules can sometimes result in adding additional noise, so the lines that enable them should be commented out:

Bad sound quality may also result from audio clipping, which can occur if Internal Mic Boost is larger than zero in .

## Fingerprint reader
A reverse engineering effort is ongoing here, and an experimental driver is available on the AUR as .

Upstream libfprint bug is tracked here.
