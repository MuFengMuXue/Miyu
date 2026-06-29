# Keyboard input

Prerequisite for modifying the key mapping is knowing how a key press results in a symbol:

# The keyboard sends a scancode to the computer.
# The Linux kernel maps the scancode to a keycode; see Map scancodes to keycodes.
# The keyboard layout maps the keycode to a symbol or keysym, depending on what modifier keys are pressed.
#* For the Linux console, see Linux console/Keyboard configuration.
#* For Xorg and Wayland, see Xorg/Keyboard configuration.

Most of your keys should already have a keycode, or at least a scancode. Keys without a scancode are not recognized by the kernel; these can include additional keys from "gaming" keyboards, etc.

In Xorg, some keysyms (e.g. ,  etc.) can be mapped to actions (i.e. launching an external application). See Keyboard shortcuts#Xorg for details.

In Linux console, some keysyms (e.g.  to ) can be mapped to certain actions (e.g. switch to other console or print some sequence of characters). See Console keyboard configuration#Creating a custom keymap for details.

## Identifying scancodes
## Using evtest
The most reliable way to obtain a scancode is to reference the  evdev event produced when the key is pressed There are multiple evdev API testers, but the most straightforward is  from the  package:

Use the "value" field of . This example shows that NumLock has scancode 70053 and keycode 69.

## Using showkey
The traditional way to get a scancode is to use the  utility. showkey waits for a key to be pressed, or exits if no keys are pressed within 10 seconds. For showkey to work you need to be in a virtual console, not in a graphical environment or logged in via a network connection. Run the following command:

 # stty -echo; showkey --scancodes; stty echo

and try to push keyboard keys; you should see scancodes being printed to the output. The  commands surrounding the  command temporarily turn off the printing of pressed keys within the terminal so you do not see a distorted mess of the output from  and the characters of the keys you are pressing.

## Using dmesg
You can get the scancode of a key by pressing the desired key and looking at the output of dmesg. For example, if you get:

 Unknown key pressed (translated set 2, code 0xa0 on isa0060/serio0

then the scancode you need is .

## Identifying keycodes
The Linux keycodes are defined in  (see the  variables).

## Identifying keycodes in console
The keycodes for virtual console are reported by the  utility. showkey waits for a key to be pressed and if none are, in a span of 10 seconds, it quits. To execute showkey, you need to be in a virtual console, not in a graphical environment. Run the following command:

 # showkey --keycodes

and try to push keyboard keys; you should see keycodes being printed to the output.

## Identifying keycodes in Xorg
The keycodes used by Xorg are reported by a utility called , which is provided by the  package. Of course to execute xev, you need to be in a graphical environment, not in the console.

With the following command you can start xev and show only the relevant parts:

{{hc|$ xev  awk -F'[ )+' '/^KeyPress/ { a} NR in a { printf "%-3s %s\n", $5, $8 }'|
38  a
55  v
54  c
50  Shift_L
133 Super_L
135 Menu
}}

Xbindkeys is another wrapper to xev that reports keycodes.

If you press a key and nothing appears in the terminal, it means that either the key does not have a scancode, the scancode is not mapped to a keycode, or some other process is capturing the keypress. If you suspect that a process listening to X server is capturing the keypress, you can try running xev from a clean X session:

 $ xinit /usr/bin/xterm -- :1

## Identifying keycodes in Wayland
Although xev works through Xwayland, you can also use  to access keycodes under pure Wayland.

For example, this command lets you retrieve only key names and their UTF-8 equivalent:

 $ wev | grep 'sym'

## Tips and tricks
## Configuration of VIA compatible keyboards
[https://www.caniusevia.com/ VIA is a program to remap keys directly into compatible keyboards. In case you have one of those, in order for the keyboard to be picked up by the browser and configure it online, you need to add a custom udev rule changing the permissions of devices accessed through the hidraw driver.

Create the following udev rule:

Then reload the rules to take effect.
