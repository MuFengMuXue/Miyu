# Huawei E1550 3G modem

This article describes how to configure Huawei E1550 3G modems.

## Preparing device
This modem is a generic device, but there are two caveats:

## Switching into modem mode
By default kernel recognizes it as usb-storage device (SCSI CD-ROM). It is true, because of this modem
contains MicroSD card (up to 4Gb) reader and internal flash.

To turn on modem you should run
 $ /lib/udev/usb_modeswitch --vendor 0x12d1 --product 0x1446 --type option-zerocd
command.

See also the  package, which you may need in future since in udev-157 modem-modeswitch has been renamed and changed as described in the commit. This package does not need any modifications, just install it.

Also you can create udev's config:

{{hc|/etc/udev/rules.d/15-huawei-e1550.rules|2=
ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="12d1", ATTRS{idProduct}=="1446", RUN+="/lib/udev/usb_modeswitch --vendor 0x12d1 --product 0x1446 --type option-zerocd"
}}

After that, modem changes its USB IDs to 12d1:140c and  shows new USB endpoints.

## Loading the driver
usbserial is proper driver for this modem, but probably it does not recognize it, so you should
force it, passing USB IDs.

 # modprobe usbserial vendor=0x12d1 product=0x140c

or put options into

(do not forget to  if it is already loaded before)

## Naming the device (optional)
You can generate symlinks to the ttyUSB* ports for a more human readable configuration with udev rules.

For a Huawei device which identifies with the USB ID 12D1:1001 after modeswitching and has 3 serial ports:
  SUBSYSTEMS=="usb", ATTRS{modalias}=="usb:v12D1p1001*", KERNEL=="ttyUSB*", ATTRS{bInterfaceNumber}=="00", ATTRS{bInterfaceProtocol}=="ff", SYMLINK+="ttyUSB_utps_modem"
  SUBSYSTEMS=="usb", ATTRS{modalias}=="usb:v12D1p1001*", KERNEL=="ttyUSB*", ATTRS{bInterfaceNumber}=="01", ATTRS{bInterfaceProtocol}=="ff", SYMLINK+="ttyUSB_utps_diag"
  SUBSYSTEMS=="usb", ATTRS{modalias}=="usb:v12D1p1001*", KERNEL=="ttyUSB*", ATTRS{bInterfaceNumber}=="02", ATTRS{bInterfaceProtocol}=="ff", SYMLINK+="ttyUSB_utps_pcui"

For a Huawei device which identifies with the USB ID 12D1:1003 after modeswitching and has 2 serial ports:
  SUBSYSTEMS=="usb", ATTRS{modalias}=="usb:v12D1p1003*", KERNEL=="ttyUSB*", ATTRS{bInterfaceNumber}=="00", ATTRS{bInterfaceProtocol}=="ff", SYMLINK+="ttyUSB_utps_modem"
  SUBSYSTEMS=="usb", ATTRS{modalias}=="usb:v12D1p1003*", KERNEL=="ttyUSB*", ATTRS{bInterfaceNumber}=="01", ATTRS{bInterfaceProtocol}=="ff", SYMLINK+="ttyUSB_utps_pcui"

## Connecting to the network
Now you have new 2 or 3  devices.Most likely first of them (ttyUSB0 if you had not such devices before) is PPP compatible modem. Use it as usual with pppd, kppp, gnome-ppp, network-manager, etc.

## Using gammu
Use  to access cell phones functionalities.

Edit

you can also generate the config using
 $ gammu-detect > ~/.gammurc

Sending SMS:
 $ gammu sendsms TEXT +7123456789 -text qwe

find device info:
 $ gammu identify

for gui use  or .

## USSD Requests
Use ussd.php tool.
