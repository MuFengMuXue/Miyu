# Logitech G300

## Installation
Install  for drivers for the mouse. It can change colors, binding, and even create custom macros. After installation, use the ratslap binary to change the mouse.

## Alternative script
Alternatively, if using the buttons is not required, disabling them with the following script allows using it as a simple mouse without requiring the installation of .

G300 is recognized as both mouse and keyboard, you can check with:

 $ xinput list | grep G300

We have to disable the G300 keyboard to make it work correctly as follows:

 #!/bin/sh
 DEVICE_ID=$(xinput list |  grep "Logitech Gaming Mouse G300" | grep keyboard | sed 's/.*id=\(0-9*\).*/\1/')

 if xinput -list-props $DEVICE_ID | grep "Device Enabled" | grep "1$" > /dev/null
 then
         xinput set-int-prop $DEVICE_ID "Device Enabled" 8 0
 fi

Make this executable and run it to see if everything is working. You can also put it into your xinitrc.d to make it load automatically.

Another shorter version:

 #!/bin/sh
 G300ID=$( xinput --list | grep G300.*Keyboard | cut --field 2 | tr --delete "id=" )

 let $( xinput --list-props $G300ID | grep "Device Enabled" | cut --field 3 ) && xinput --disable $G300ID
