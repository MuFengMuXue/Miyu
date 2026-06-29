# Logitech MX Revolution

This article shows how to configure a Logitech MX Revolution mouse.

## Install
Install  and .

## Configuration
## Xorg
Xorg is able to auto-detect this mouse just fine. However, it has a 17 key mapping.

Edit the mouse section of :

 Section "InputDevice"
     Identifier  "Mouse0"
     Driver      "mouse"
     Option      "Protocol" "auto"
     Option      "Device" "/dev/input/mice"
     Option      "ZAxisMapping" "4 5"
     #Option      "XAxisMapping" "6 7"  #uncomment if you want horizontal scrolling with mouse wheel
     Option      "Buttons"    "17"
 EndSection

## Bind mouse buttons with Xbindkeys
We will put all of the settings into  the configuration file of Xbindkeys.

You will want to put in  events to send to xvkbd. Here is a sample:

 "/usr/bin/xvkbd -text "\m:0x0 + b:8
 "/usr/bin/xvkbd -text "\[Alt_L\m:0x0 + b:9
 "/usr/bin/xvkbd -text "\[Control_L\m:0x0 + b:6
 "/usr/bin/xvkbd -text "\[Control_L\m:0x0 + b:7

For some reason some combinations of keyboard events refuse to work with certain buttons for me.

 refers to your first mouse. The "+b:8" refers to the button you push. Here is a list of all the buttons:

 # Mappings for keys for MX Revo
 # b:1	-	left mouse button
 # b:2	-	left and right mouse button together
 # b:3 	-	right mouse button
 # b:4	-	mouse wheel up
 # b:5	-	mouse wheel down
 # b:6	-	mouse wheel left
 # b:7	-	mouse wheel right
 # b:8	-	back button
 # b:9	-	forward button
 # b:10	-	-none-
 # b:11	-	-none-
 # b:12	-	-none-
 # b:13	-	media wheel up
 # b:14	-	-none-
 # b:15	-	media wheel down
 # b:16	-	-none-
 # b:17	-	media wheel press

To remap the seach button to something instead of search, put something along the lines of the following into .

Example here is to remap it to  to close a window.

 "/usr/bin/xvkbd -text "\[Alt_L\c:0xE1

Alternatively, Gnome will recognize the small middle search button as a keyboard event. Thus, you just have to go into keyboard shortcuts and remap that to something. This is probably the most reliable way to go about using this key.

## Bind mouse buttons with Xmodmap
It is possible to use xmodmap to register the button press as a middle click. Begin by assigning the key event to Pointer_Button 2.

 echo "keycode 225 = Pointer_Button2" >> ~/.Xmodmap

Now, you can create a startup script that feeds that input into xmodmap and autostart it.

 #!/bin/sh
 xmodmap ~/.Xmodmap

And do not forget to make it executable.

The trick only works when "mousekeys" are on. So either gnome-keyboard-properties -> Mousekeys -> Enable pointer OR toggle with SHIFT-ALT-NUMLOCK (you want to be able to toggle so you can use the numeric keypad at times). Or in KDE System Settings -> Keyboard & Mouse -> Mouse -> Mouse Navigation -> Check "Move pointer with keyboard (using the num pad)"

Lastly, add xbindkeys to your startup and you should be good to go.

The best way to map the search button to middle click is to add the following lines to :
 # Enable mouse button emulation
 dev.mac_hid.mouse_button_emulation = 1
 # Set 2nd button to 217 - the middle button of MX Revolution mouse.
 dev.mac_hid.mouse_button2_keycode = 217
 # Optionally reset default mapping of Alt_R to right click
 # by mapping right click to a non-existing key
 dev/mac_hid/mouse_button3_keycode = 999

## Mouse Wheel Mode
In order to enable or disable mouse wheel's free spinning, you can use . Giving the following command from shell, or, alternatively, putting it in a script executed at the startup should enable/disable free spinning.
 # revoco free  # in order to enable free spinning
 # revoco click # in order to disable free spinning

It is also possible to remap the button to toggle between free and click.
 # revoco manual 6 # use search button instead of middle click.
This will free the wheel button allowing it to act as a normal mouse 3 button.

More Info can be found [https://github.com/sebastien/revoco here
