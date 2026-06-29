# Xmodmap

xmodmap is a utility for modifying keymaps and pointer button mappings in Xorg.

xmodmap is not directly related to X keyboard extension (XKB), as it uses different (pre-XKB) ideas on how keycodes are processed within X. Generally, it is only recommended for the simplest tasks. See X keyboard extension for advanced layout configuration.

## Introduction
There are two types of keyboard values in Xorg: keycodes and keysyms.

; keycode
: The keycode is the numeric representation received by the kernel when a key or a mouse button is pressed.
; keysym
: The keysym is the value assigned to the keycode. For example, pressing  generates the , which is mapped to the , which matches  in the ASCII table.
: The keysyms are managed by Xorg in a table of keycodes defining the keycode-keysym relations, which is called the keymap table. This can be shown by running .

## Installation
xmodmap can be installed through the  package.

Optionally, install , which is a graphical front-end to xmodmap.

## Keymap table
Print the current keymap table formatted into expressions:

Each keycode is followed by the keysym it is mapped to. The above example indicates that the keycode  is mapped to the lowercase , while the uppercase  is mapped to keycode  plus .

Each keysym column in the table corresponds to a particular combination of modifier keys:
#
#
#
#
#
#

Not all keysyms have to be set, but to assign only a latter keysym, use the  value.

To see which keycode corresponds to a key, see Keyboard input#Identifying keycodes in Xorg for details on the xev utility which will output relevant keycode/keysym information about a key when you press it.

Note that xmodmap is influenced by xkbd settings, so all eight keysym are available for the US(intl) xkbd layout but not for the default US (it is missing the ralt_switch symbol defined in level3). To have all 8 keysyms available you should configure the (intl) variant of the keyboard.  Using US layout as an example,  before calling xmodmap to test your changes in the current X session. To permanently make this change, edit the xorg configuration or your .xprofile or .xinitrc file.  See Xorg/Keyboard configuration#Setting keyboard layout for a full explanation.

## Custom table
To create a key map (i.e. ):
 $ xmodmap -pke > ~/.Xmodmap

To test the changes:
 $ xmodmap ~/.Xmodmap

## Activating the custom table
With GDM, XDM or LightDM there is no need to source . For startx, use:

Alternatively, edit the global startup script .

## Test changes
To make temporary changes:
 $ xmodmap -e "keycode 46 = l L l L lstroke Lstroke lstroke"
 $ xmodmap -e "keysym a = e E"

## Modifier keys
xmodmap can also be used to override modifier keys, e.g. to swap  and  (the Windows key).

Print the current modifier table verbosely (full sample):

## Finding the keysym column modifier keys
;ISO_Level3_Shift
:The AltGr key on non-US keyboards calls modifier ISO_Level3_Shift. (On US keyboards, the right-alt  has the same function as the left-alt , which makes setting the layout as US international preferable. See #Keymap table.)
;Mode_switch
:The Mode_switch modifier may be mapped by default to a key that is not on your keyboard.

## Reassigning modifiers to keys on your keyboard
Before assignment, the modifier keys need to be cleared.  This applies to both modifiers you intend to assign and modifiers on keys that you intend to use.  For example, if you intend to assign  to your A key and  to your NumLock key, you need to first clear the modifiers for both  and , then assign the keysyms, and finally add back the modifiers.

 is a comment, so only the modifiers  and  get cleared in the following example. Then the keysyms , ,  and  are assigned to the opposite modifier. Assigning both left and right to the same modifier means that both keys are treated the same way.

The following example modifies  to , and  to :

## Compose key
A compose key serves to create special characters and symbols that may not be directly accessible on the keyboard. This is especially useful for typing accented letters from non-English languages. For example, pressing    in succession will produce é. Some characters require more than 2 keys to be pressed after .
Usually a modifier key of choice is mapped to . The compose key can be set in the GUI settings of most desktop environments, but these options will not work if a custom key map table is used as described in this article.
To set the compose key using , use the  identifier. For example, to map the right alt key () to the compose key:

The keycode number could vary based on keyboard models.

## Reverse scrolling
The natural scrolling feature available in OS X Lion (mimicking smartphone or tablet scrolling) can be replicated with xmodmap. Since the synaptics driver uses the buttons 4/5/6/7 for up/down/left/right scrolling, you simply need to swap the order of how the buttons are declared in :

Then update xmodmap:
 $ xmodmap ~/.Xmodmap

## Swapping mouse buttons
The left, middle and right mouse buttons correspond to buttons 1,2 and 3 respectively in the synaptics driver. To swap left and right mouse buttons, again simply reverse the order in which they are listed in your :

This should suffice for a simple mouse setup. Again, update xmodmap:
 $ xmodmap ~/.Xmodmap

## Templates
## Spanish
## Esperanto
Next is an example to make it possible to type Esperanto letters by pressing  and the relevant letter. For example, if you type , you will get the letter "Ĉ".

## Turn CapsLock into Control
Simplest example of changing  into .

## Turn CapsLock into Control, and LeftControl into Hyper
Laptop users may prefer having  as . The  key can be used as a  modifier (an additional modifier for emacs, openbox or i3).

## Turn Super_R into Hyper_R
Users who wish to have a  key on full keyboard layout may wish to use the Right  key as .

## Switch every number key N with Shift-N and vice-versa, for Croatian layout
Should work fine for layouts similar to Croatian as well.
