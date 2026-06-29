# Multitouch displays

Multitouch devices are handled by the  module, see kernel modules.

## Configuration (USB devices)
Find the vendor ID (VID) and product ID (PID) for your touchscreen using :

Here, VID=0eef (eGalax) and PID=725e. Now, get the MT_CLASS_* definitions from Currently vendor specific classes are available for 3M Cypress and eGalax. If none of this matches your device, you can try to experiment with the other MT_CLS_*. In this example

 #define MT_CLS_EGALAX                           0x0103

You need to convert MT_CLS_* to decimal (In this case, 0x0103 is 259 in decimal).

After loading the , see Kernel modules, you need to pass the devices' options with

 # echo BUS VID PID MT_CLASS_* > /sys/module/hid_multitouch/drivers/hid\:hid-multitouch/new_id

In this example, the touchscreen is an USB device, so BUS=4 and the previous command looks like this:

 # echo 4 0eef 725e 259 > /sys/module/hid_multitouch/drivers/hid\:hid-multitouch/new_id

Reboot. If the touchscreen is detected you should submit your devices' details (relevant  line) to the [http://vger.kernel.org/vger-lists.html#linux-input linux-input mailing list.

If the touchscreen is not working properly, you may need to install a specific driver for your touchscreen, see #Drivers.

## Rotating the touch screen
Store and mark executable (call the script to see its input options).

## Drivers
## eGalax
The driver for eGalax touchscreens is available from the [https://web.archive.org/web/20191021190003/http://home.eeti.com.tw/drivers_Linux.html eGalax website (archive).

## Invert Y-axis
If after installing the eGalax driver the Y-axis of the touchscreen is inverted, edit the file  and change the value of  from 0 to 2:

## Gestures
If you want gestures in your window manager, install  from the Arch User Repository and read its docs.
