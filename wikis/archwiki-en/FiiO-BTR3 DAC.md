# FiiO-BTR3 DAC

From the manufacturer's website:
:The BTR3 is a Bluetooth amplifier which supports multiple wireless audio codecs (i.e. AAC, SBC, aptX, aptX Low Latency, aptX HD, LDAC, LHDC and HWA).

## Installation
PulseAudio has issues with supported high sample rates - set them in the configuration as default:

If your device still is not working, try updating the firmware.

## Firmware update
Install the  package, and download the firmware:

1. Power on the BTR3
2. Hold the unlabeled button for 5 sec
3. Hold the unlabeled button and vol + button for 5 sec
4. Check if the device is found:

5. Optional: Backup your firmware:
 dfu-util -d 0a12:ffff -U backup_fiio_btr3.dfu
6. Flash your new firmware:
 dfu-util -d 0a12:ffff -D BTR3-1.2-0531.dfu
7. If dfu-util ends with an Error because the device was rebooted - you are finished
