# Touchatag RFID Reader

Touchatag is a RFID tag reader from Touchatag. It is a cheap set consisting of an ACR122U USB tag reader and MiFare Ultralight RFID tags (USB ID , use  to check the firmware version − 2.14 as of 2020-05-10 − under the  descriptor).

## Installation
Stop the conflicting drivers (,  and ) from loading.

See the note about blacklisting drivers: they can still be loaded manually, so you should create the following file:

Reload udev rules, unload the conflicting modules if they were loaded already:

 # rmmod pn533_usb pn533 nfc

or simply reboot.

There are two options for connecting the tag reader to libnfc. Difference between them is detailed on stackoverflow.

## USB
This is the modern and recommended way to use this device.

To use , you do not need to run the pcsc daemon (libnfc README currently tells you to run it, but this is for the PC/SC way).

Install .

## PC/SC
This is the legacy and deprecated way to use this device.

Install  and .

## Usage
## USB
Check if the device is detected:

Reading NFC cards works as well:

## PC/SC
To test the device run:

 # pcscd -f

Start , then put a tag on the reader, the result should look like the following:

## Tips and tricks
## tagEventor
tagEventor runs in the background and executes scripts when a tag enters or leaves your tag reader.

Download a binary version or compile your own.

Run tagEventor to test your installation:

 # tagEventor -v 1

The scripts are located in . Read the tagEventor documentation on how to use them.

## Troubleshooting
## Firmware is bogus! Upgrade the reader firmware
If you encounter a problem like this:

 ccid_usb.c:859:ccid_check_firmware() Firmware (1.00) is bogus! Upgrade the reader firmware or get a new reader.
 ifdhandler.c:104:IFDHCreateChannelByName() failed
 readerfactory.c:1050:RFInitializeReader() Open Port 200000 Failed (usb:072f/2200:libusb:006)
 readerfactory.c:233:RFAddReader() ACS ACR122U PICC Interface init failed.

The [https://github.com/nfc-tools/libnfc/blob/master/README.md libnfc README suggests to do the following:

Removing the bogus firmware detection of libccid: edit  configuration file (usually ) and locate , turn  into  to allow bogus devices and restart .
