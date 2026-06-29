# Mouse buttons

This article describes how to configure a mouse with more than 3 buttons.

## Prerequisite testing mouse input in X
This page assumes you are using Xorg (X Window System) and not Wayland.

You will first want to check what X sees from your mouse. X events can be displayed by the xev utility. A window will pop up by running

 $ xev -event button | grep button

Any xevents (like moving, resizing, or clicking in) that window will then be reported to the console you launched xev from. Since you are filtering for lines which contain "button" it will show mouse click and release events with their relevant button numbers. For most mice, this will be '1' for left button, '2' for middle, '3' for right. Other buttons will vary (e.g. for an Logitech MX Master 3 the scroll wheel is 4 & 5, thumb wheel is 6 & 7, the thumb-tip button is 9, and the inner-thumb button is 8).

Example output:

 state 0x0, button 1, same_screen YES
 state 0x100, button 1, same_screen YES
 state 0x0, button 9, same_screen YES
 state 0x0, button 9, same_screen YES

This corresponds to a left mouse click and release followed by a thumb-tip click and release.

You can use xev to confirm your mouse button numbers and to confirm that X is being notified of mouse clicks.

## Rebinding mouse and keyboard functions
This section covers details of using various tools to rearrange mouse and keyboard functions.

## Binding mouse buttons to keyboard functions
## xte
xte from  comes handy when we want to bind  keyboard buttons to mouse.

Here is example  which binds  to mouse button 3 ("right click"):

## Binding keyboard keys to mouse buttons
## xvkbd and xbindkeys
Let us say we want to bind some mouse buttons to keyboard ones. The problem we will encounter is that we do not know how to emulate a key press. Here comes in handy . We can use it along with .

 $ xbindkeys --defaults >> ~/.xbindkeysrc
 $ xbindkeys

To restart xbindkeys type:

 $ pkill -f xbindkeys
 $ xbindkeys

Here is example  config:

 "xvkbd  -text "\m:0x0 + b:8
 "xvkbd  -text "\[Shift\m:0x0 + b:9
 "xvkbd  -text "\[Shift\m:0x0 + b:10
 "xvkbd  -text 2"
        m:0x0 + b:11
 "xvkbd  -text 3"
        m:0x0 + b:12

If you want to check your mouse buttons number use xev. Do not forget to type capital letters in xvkbd -text usage and to escape opening bracket with \ or you get simply [Shift written.

Here is an example for xbindkeys to enable x selection paste(third click pasting), you need both xsel and xvkbd installed, What it does it executes that command whenever button 13 of the mouse is pressed (in ~/.xbindkeysrc) :

 "xvkbd -no-jump-pointer -text "\D1$(xsel)" 2>/dev/null"
 b:13

This is an example for a keybinding for Meta+M:

 "xvkbd  -text "\{+Super_L}m\{-Super_L}""
 b:10

## evrouter
Some programs, especially games, use different methods of reading input, so another program is needed: .

For the  command to be able to read the input devices, it will have to be run in the  group (or as root). This can be achieved by adding yourself to that group:

 # gpasswd -a user input

Now we can use the  option to display what the button to be changed is called:

Now press the buttons that you wish to change:

 Window "(null)": # Window title
 # Window "(null)": # Resource name
 # Window "(null)": # Class name
 "Microsoft Trackball Explorer®" "/dev/input/event1" none key/275 "fill this in!"

 Window "(null)": # Window title
 # Window "(null)": # Resource name
 # Window "(null)": # Class name
 "Microsoft Trackball Explorer®" "/dev/input/event1" none key/276 "fill this in!"

The line that ends with "fill this in!" can be copied into the configuration file which by default is . For example, using the X11 key event emulator built into evrouter:

The 'event1' was changed to 'event*' in case udev gives it a different device number at boot. The 'none' was changed to 'any' so that the rule works even if any modifier keys are pressed when the button is pressed. To determine the key codes (in brackets) you can use

 # xmodmap -pk

See  for a full explanation of the fields.

After setting up the configuration file, run it as a daemon:

 $ evrouter /dev/input/event*

To stop the daemon:

 $ evrouter -q
 $ rm -f /tmp/.evrouter*

## User tools
This section outlines hardware-specific tools which are useful for configuring mouse settings, and in particular their buttons. For the generic remap tools, see Input remap utilities.

* Piper () is a graphical user interface to configure gaming mice, works with Wayland. In order to work with your mouse, it must be in the list of supported devices.
*  for Logitech MX mice will help you set the proper resolution, enable or disable smart scroll (with boot time support too!), etc. Be sure to look at  and set up the options you want to be automatically applied when the mouse gets loaded by udev.
*  is a tool for configuring Logitech mice (Logitech Options for Linux). It may remap buttons to actions, support gestures, smart shift and so on.

## evdev Xorg.conf setup
This section explains setting up mice with more than 3 buttons using . There are other ways to achieve this, but some of the notes and tools described here may be useful for people with other needs. Some parts may help getting extra mouse buttons working using other drivers as well.

We will be using the evdev driver for Xorg. EVentDEVice is an advanced driver for USB input devices which offers much greater power over the standard Xorg  driver. It is also more "direct" than the  driver, allowing lower latency and less translation issues.

* Note that  is both a kernel module and an Xorg input driver. All the Arch kernels come with the  module.

With the Xorg 11R7.0 or newer, only the following changes to  need to be made.

## Finding the mouse name
The first step is to find the name of the mouse / mice. To do this, execute the following command:
 $ grep -E "Name|Handlers" /proc/bus/input/devices | grep -E -B1 'Handlers.*mouse'

This should output something like this:
 N: Name="Logitech USB Gaming Mouse"
 H: Handlers=mouse0 event0 ts0

Or this if you have more than one mouse:
 N: Name="Kensington Kensington Expert Mouse Wireless"
 H: Handlers=event0 mouse0
 --
 N: Name="Logitech USB Receiver"
 H: Handlers=kbd event2 mouse1

The mouse is the one that has the , so the name of the device is .

Copy the name of the device, and open up .

## Configuring Xorg
Now, we need an entry in  that tells X how to use this mouse. It should look something like this:

 Section "InputDevice"
   Identifier      "Evdev Mouse"
   Driver          "evdev"
   Option          "Name" "Logitech USB Gaming Mouse"
   Option          "evBits"  "+1-2"
   Option          "keyBits" "~272-287"
   Option          "relBits" "~0-2 ~6 ~8"
   Option          "Pass"    "3"
   Option          "CorePointer"
 EndSection

Replace the  option with the name you copied from above. You may also omit the  option if you use multiple mice or experience errors when attempting to load Xorg. The other options are all basic mouse configurations for evdev and should work with most mice.

Next, we need to tell X to use the mouse, so look in  for .

Modify the  section to use "Evdev Mouse" as the device. When you are done, it should look something like this:

 Section "ServerLayout"
   Identifier     "Default Layout"
   Screen 0       "Monitor0" 0 0
   InputDevice    "Keyboard0" "CoreKeyboard"
   InputDevice    "Evdev Mouse" "CorePointer"
 EndSection

The only thing you should change in the layout is the  line that refers to your mouse.

That should be all that is required.

* Edit by: xxsashixx
This is for Logitech G5 Mouse users. I have not tested this for other mice, but if you do not add this, your mouse MAY not work.
If you do not need to add this, then do not.

Put
 Option "Device" "/dev/input/eventin the  section or else the mouse will not be picked up.

[# = The number you got from:

 grep -E "Name|Handlers" /proc/bus/input/devices

* Edit by: bapman
With the above method, your mouse might not to work after reboot (event number changes). To fix this, you can use symlinks in . For example:
 Option      "Device" "/dev/input/by-id/usb-Logitech_USB_Receiver-event-mouse"
To find the appropriate id, do:
 ls /dev/input/by-id/

* Edit by: Diamir

With a Desktop type keyboard-mouse, this does not work because there is only one USB attachment and  contains only the keyboard.
In this case, we can create a udev rule to get a consistent link.
The following rules create the link  which points on the correct event entry:
 KERNEL=="eventBUS=="usb", SYSFS{modalias}=="usb:v045Ep008Ad7373dc00dsc00dp00ic03isc00ip00", SYMLINK+="input/usbmouse"

You can call it  and put it in

The cryptic value to use for  can be gotten in the following way:

enter the command

You will find the keyboard and the mouse and see event4 is the mouse in this case:

 I: Bus=0003 Vendor=045e Product=008a Version=0111
 N: Name="Microsoft Microsoft Wireless Optical Desktop� 1.00"
 P: Phys=usb-0000:00:10.0-2/input0
 S: Sysfs=/devices/pci0000:00/0000:00:10.0/usb1/1-2/1-2:1.0/input/input3
 U: Uniq=
 H: Handlers=kbd event0
 B: EV=120013
 B: KEY=1000000000007 ff800000000007ff febeffdff3cfffff fffffffffffffffe
 B: MSC=10
 B: LED=107

 I: Bus=0003 Vendor=045e Product=008a Version=0111
 N: Name="Microsoft Microsoft Wireless Optical Desktop� 1.00"
 P: Phys=usb-0000:00:10.0-2/input1
 S: Sysfs=/devices/pci0000:00/0000:00:10.0/usb1/1-2/1-2:1.1/input/input4
 U: Uniq=
 H: Handlers=kbd mouse0 event1
 B: EV=17
 B: KEY=3000000000000 0 1f0000 f8400244000 601878d800d448 1e000000000000 0
 B: REL=7c3
 B: MSC=10

So I enter the following command (adapt event # to your particular case):
{{bc|1=udevinfo -a -p $(udevinfo -q path -n /dev/input/event4)  grep modalias
ATTRS{modalias}=="input:b0003v045Ep008Ae0111-0,1,2,4,k71,72,73,74,83,86,8A,8C,8E,8F,9B,9C,9E,9F,A3,A4,A5,A6,AB,AC,B5,B6,CE,D2,D5,E2,E7,E8,E9,EA,EB,110,111,112,113,114,1B0,1B1,r0,1,6,7,8,9,A,am4,lsfw"
ATTRS{modalias}=="usb:v045Ep008Ad7373dc00dsc00dp00ic03isc00ip00"
ATTRS{modalias}=="pci:v00001106d00003038sv00001043sd000080EDbc0Csc03i00"}}

grab the ATTRS which becomes with usb: to complete "SYSFS{modalias}== " entry

And finally, use  as the Device Option in :
 Option "Device" "/dev/input/usbmouse"

## evdev Xorg - Post configuration
## Google Chrome
It works. Horizontal scroll works out of the box - push the scroll wheel left or right. Thumb buttons also work as next/previous page.

## Opera
It works. Note: buttons can be mapped to functions easily in . For example, to bind button 8 to back:

# Navigate to mouse set-up and expand the Application drop-down
# In the input column, type: Button 8
# In the actions column, type: Back

## Firefox
## Horizontal scroll
To get back and forward enabled, instead of scroll left/right, change the following settings in :

 mousewheel.default.action.override_x         2
 mousewheel.default.delta_multiplier_x       -100

## Thumb buttons - forward and back
To do this we need to map keystrokes to the desired mouse buttons and install  and .

In most modern applications which use back/forward features, XF86Back is mapped to back and XF86Forward is mapped to forward by default. On most MX mice the thumb buttons resolve to 8 & 9. If your mouse is different, check button numbers using xev and replace the numbers used in the example (b:8 & b:9).

So if you have an MX mouse you would create the file , containing:

 # Mouse Buttons
 "xvkbd -xsendevent -text "\[XF86Back""
 m:0x0 + b:8
 "xvkbd -xsendevent -text "\m:0x0 + b:9

Now to test... Run the following command and if it works as expected remember to add xbindkeys to  or somewhere where it will be executed each time X starts. Also, this should work with Epiphany and Konqueror without any additional configuration or use of  IMWheel.
 xbindkeys

Since xvkbd is not available from the official repositories here is another example using [https://www.hoopajoo.net/projects/xautomation.html xte from the  package

 # Mouse Buttons
 "xte "key XF86Back""
 m:0x0 + b:8
 "xte "key XF86Forward""
 m:0x0 + b:9

## xmodmap tweaking
It may prove to be more comfortable for some to change the ordering of button codes, as the case may be for left-handed people. Depending on the environment you use, the button codes can be configured in two different ways. If you use  to load X, then add this to  (change for the number of buttons you have):
  xmodmap -e "pointer = 1 2 3 6 7 8 9 10 11 12 4 5" &

Note that buttons 4 and 5 must go on the end or else your scroll wheel will not work.

If you use GDM/SDDM/XDM instead of , then create the file  and add this to it (change for the number of buttons you have):
  pointer = 1 2 3 6 7 8 9 10 11 12 4 5

* GDM/SDDM/XDM read the  file if it is present, whereas  does not. Another solution would be to add this to your : . This would allow you to use *DM and  while only having to edit  when you need to make changes.

You may have to play with these numbers a bit to get your desired behavior. Some mice use buttons 6 and 7 for the scroll wheel, in which case those buttons would have to be the last numbers. Keep playing with it until it works!

## xinput tweaking
For debugging purposes  can be used as it is able to change the button map on the fly in userspace. The following line corrects the button mapping (there have been reported cases with Logitech M505/B605 mice and possibly others) so the received events are mapped correctly:

  $ xinput set-button-map "$(xinput | awk -F''/Logitech M505\/B605/ {print $2}' | awk '{print $1}')" 1 2 3 4 5 8 9

## Device-specific configuration
## Logitech G600
It is known that in xorg-server 1.18.0-3 side buttons of G600 are not recognized as a separate keyboard device, but another mouse which causes strange (moving mouse cursor to an edge of screen when one of main mouse buttons are clicked) behavior.
To force xorg to recognize them as a keyboard buttons, add following section to your :

 Section "InputClass"
     Identifier "G600 misconfiguration fix"
     MatchProduct "G600"
     # Match just the keyboard section of the G600
     MatchIsKeyboard "true"
     # evdev assumes it is a mouse when it sees the absolute axis. Stop that from happening.
     Option "IgnoreAbsoluteAxes" "on"
 EndSection

## Mad Catz Mouse
Mad Catz Mouse

## Logitech M560/M545/M546
These mice are designed for Windows 8 and have non-conventional behavior: the mouse appears as a mouse and keyboard and some buttons do not emit the standard mouse button event but a combination of keyboard and mouse button presses instead. This prevents "comfortable" use of this mouse under Linux.

The appropriate driver allows the mouse to be used like an ordinary mouse:

* [https://github.com/kreijack/logitech-m560 kernel module for M560 (already merged into kernel v4.2)
* kernel module for M545/M546

See also Xbindkeys for mouse button mapping.

## Logitech G5 mouse: Binding + and -
If you want to bind the buttons  and  in G5/7 mouse, which normally changes DPI, you have to use  http://piie.net/temp/g5_hiddev.c released by a lomoco author.

 wget http://piie.net/temp/g5_hiddev.c
 gcc -o g5hack g5_hiddev.c
 ./g5hack /dev/usb/hiddev0 3

This will change your DPI to 2000, light the 1st LED and disables DPI on-the-fly changing, so you can use it with evrouter. If you would use it frequently I suggest you to copy it to the  directory:

 # cp g5hack /usr/bin/

If you want to bind your  and  buttons you must copy the line at the bottom (one with the comment '"-" button does not function anymore' above) to the mode you will be using, like, for example, under the "case 3:" you can put it on the line with the comment 'turn on third led' above (deleting the old one before of course).

For the newest G5 mouse which is reported as "product 0xc049" original hack does not work. You have to simply change the  to  and recompile.

You can execute the g5hack tool at system start up using systemd unit. See Systemd#Writing unit files for detail.

## If Arch is a guest virtual machine
If you want to support more than two or three mouse buttons, the capability will depend on your hypervisor software.

## VMware workstation
For your Arch-based guest VM, add the below lines to its .vmx configuration file:
 mouse.vusb.enable = "TRUE"
 mouse.vusb.useBasicMouse = "FALSE"
