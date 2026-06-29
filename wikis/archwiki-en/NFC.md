# NFC

Near-field communication devices have become pretty easy to operate and read out under Linux. This page explains how to quickly set up the most common NFC scanners.

## Installation
Install , , ,  and .

The  package ships a  which will cause the  server to start when a program requests it. Alternatively, you can manually start/enable the .

After installing , it is important that you re-plug your card reader as it ships with a few udev rules and kernel module blacklist that need to load before loading the actual driver.

## Scanning an NFC card
Now everything should already be in place for a test scan. Plug in your NFC reader and run . This tool will try to communicate with your scanner and also poll for any NFC cards placed on your scanner. If you try to scan a card after the tool has found your scanner, you should see events printed on your terminal.

## Supported devices
See https://ccid.apdu.fr/#readers for a list of scanners supported by ccid and https://nfc-tools.github.io/resources/ by libnfc.

## Troubleshooting
In case things do not seem to work, investigate the log of

## NXP NCI 2.0 controllers (PN7150/PN7160) — tags not detected
Some laptops (notably ASUS ROG models with a Keystone slot) have a built-in NXP NFC controller connected via I2C. The kernel driver  may load successfully and RF polling appears active in , but no tags are ever discovered.

This is caused by three bugs in the upstream  and  kernel modules affecting NCI 2.0 protocol handling. As of kernel 6.18, these are not yet fixed upstream.

Check if you are affected:

 $ dmesg | grep -i nxp-nci
 $ cat /sys/class/nfc/nfc*/name

If RF polling starts but  never appears, see linux-nxp-nfc-fix for patched DKMS modules.

Known ACPI IDs: , , , .
