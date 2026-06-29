# Xbindkeys

xbindkeys is a program that allows to bind commands to certain keys or key combinations on the keyboard. It works with multimedia keys and is independent of the window manager and desktop environment.

## Installation
Install the  package.

## Configuration
Create a blank , or you can create a sample file:

 $ xbindkeys -d > ~/.xbindkeysrc

Now you can either edit  to set keybindings, or you can do that with the #GUI method.

## Audio control
Here is an example configuration file that binds  key combos on a laptop to pactl commands that adjust audio, such as sound volume and mute status. Note that pound (#) symbols can be used to create comments.

For alternative commands to control volume, see PulseAudio#Keyboard volume control or ALSA#Keyboard volume control.

## Backlight control
Keybindings for backlight control can be defined using the  and  keys. See Backlight#Backlight utilities for the available backlight control utilities.

## GUI method
For graphical configuration install the  package and run:
 $ xbindkeys_config

## Identifying keycodes
To find the keycodes for a particular key, enter the following command:
 $ xbindkeys --key
or the following to grab multiple keys:
 $ xbindkeys --multikey

A blank window will pop up. Press the key(s) to which you wish to assign a command and xbindkeys will output a handy snippet that can be entered into . For example, while the blank window is open, press  to get the following output (results may vary):
 "(Scheme function)"
     m:0x8 + c:32
     Alt + o

# The first line represents a command.
# The second line contains the state (0x8) and keycode (32) as reported by the tool xev.
# The third line contains the keysyms associated with the given keycodes.

To use this output, copy either one of the last two lines to  and replace "(Scheme function)" with the command you wish to perform.

To identify mouse buttons, xev can be used, see == Making changes permanent ==

Once you are done configuring your keys, edit your xprofile or xinitrc file (depending on your window manager) and place
 xbindkeys

before the line that starts your window manager or DE.

## Simulating multimedia keys
The XF86Audio* and other multimedia keys (see LQWiki:XF86 keyboard symbols) are pretty-much well-recognized by the major DEs. For keyboards without such keys, you can simulate their effect with other keys
 # Decrease volume on pressing Super-minus
 "pactl set-sink-volume 0 -1000"
    m:0x50 + c:20
    Mod2+Mod4 + minus
However, to actually call the keys themselves you can use tools like  and . Unfortunately since you would already be holding down some modifier key (Super or Shift, for example), X will see the result as  which will not do anything useful. Here is a script based on xmacro and xmodmap from the  package for doing this[https://bbs.archlinux.org/viewtopic.php?pid=843395.

This works for calling  once (assuming you are using ), but repeatedly calling it without releasing the  key (like tapping on a volume button) does not work. If you would like it to work that way, add the following line to the bottom of the script.
 echo 'KeyStrPress Super_L' | xmacroplay :0
With this modified script, if you press the key combination fast enough your  key will remain 'on' till the next time you hit it, which may result in some interesting side-effects. Just tap it again to remove that state, or use the original script if you want things to 'just work' and do not mind not multi-tapping on volume up/down.

These instructions are valid for pretty much any one of the XF86 multimedia keys (important ones would be , , , , ).

## Mouse chording
By dedicating one button on the mouse as a "chording" key (much like the  key on a keyboard), it is possible to use xbindkeys to configure your mouse to perform more actions than would otherwise be possible. This requires the use of Scheme rather than the simplified xbindkeys syntax.

With this function defined, you can now configure some chorded commands:

This defines "button 10" as as chording key on your mouse. When button 10 is pressed down, the function will create bindings for the buttons defined inside the block. When button 10 is released, those bindings will be removed. So for example: with button 10 held down, pressing and releasing button 1, and then releasing button 10, will result in a virtual "button 8" (back) event being generated.

## Troubleshooting
If, for any reason, a hotkey you already set in  does not work, open up a terminal and type the following:
 $ xbindkeys -n

By pressing the non-working key, you will be able to see any error xbindkeys encounter (e.g: mistyped command/keycode,...).

If the command for a keybind works via the xdotool in command line, but not when activated by the hotkey try adding "+ Release" to the hotkey (especially notable on GNOME):
 "xdotool key --clearmodifiers XF86AudioPlay"
     Mod2 + F7 + Release

This will make the  key play/pause audio. Where the "xdotool" command would work in commandline, if the "+ Release" is removed it will fail with xbindkeys.
