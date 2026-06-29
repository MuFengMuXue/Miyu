# Linux console/Keyboard configuration

Keyboard mappings, console fonts and console maps are provided by the  package (a dependency of systemd), which also provides low-level tools for managing the text console. In addition, systemd provides the  tool, which can control both the system locale and keyboard layout settings for both the console and Xorg.

## Viewing keyboard settings
Use  to view the current keyboard configuration.

## Keymaps
The keymap files are stored in the  directory tree. A keymap file fully describes the keyboard layout, possibly with symbols for different languages and layout switching is simulated via  keysym usage.

The  statement can be used to share common parts of keymap files. Where to look for an include file is described in the source code only.

For more details see .

## Listing keymaps
The naming conventions of console keymaps are somewhat arbitrary, but usually they are based on:

* Language codes: where the language code is the same as its country code (e.g.  for German, or  for French).
* Country codes: where variations of the same language are used in different countries (e.g. for United Kingdom English, or  for United States English); a list of country codes can also be found in wikipedia:ISO 3166-1#Codes.
* Keyboard layouts: where the layout is not related to a particular country or language (e.g.  for the Dvorak keyboard layout).

For a list of all the available keymaps, use the command:

 $ localectl list-keymaps

To search for a keymap, use the following command, replacing  with the code for your language, country, or layout:

 $ localectl list-keymaps | grep -i search_term

Alternatively, using find:

 $ find /usr/share/kbd/keymaps/ -type f -name "*search_term*"

## Loadkeys
It is possible to set a keymap just for the current session. This is useful for testing different keymaps, solving problems etc. The loadkeys tool is used for this purpose:

 # loadkeys keymap

See  for details. The same tool is used internally by  when loading the keymap configured in .

## Persistent configuration
A persistent keymap can be set in , which is read by systemd on start-up. The  variable is used for specifying the keymap. If the variable is empty or not set, the  keymap is used as default value. See  for all options. For example:

For convenience, localectl may be used to set the console keymap. It will change the  variable in  and also set the keymap for the current session:

 # localectl set-keymap --no-convert keymap

The  option can be used to prevent  from automatically changing the Xorg keymap to the nearest match. See  for more information.

If required, the keymap from  can be loaded during early userspace by the  mkinitcpio hook.

## Creating a custom keymap
When using the console, you can use hotkeys to print a specific character. Moreover we can also print a sequence of characters and some escape sequences. Thus, if we print the sequence of characters constituting a command and afterwards an escape character for a new line, that command will be executed.

One method of doing this is editing the keymap file. However, since it will be rewritten anytime the package it belongs to is updated, editing this file is discouraged. It is better to integrate the existing keymap with a personal keymap. The  utility can do this.

First, create a keymap file. This keymap file can be anywhere, but one method is to mimic the directory hierarchy in : create the  directory, then edit .

As a side note, it is worth noting that such a personal keymap is useful also to redefine the behaviour of keys already treated by the default keymap: when loaded with , the directives in the default keymap will be replaced when they conflict with the new directives and conserved otherwise. This way, only changes to the keymap must be specified in the personal keymap.

## Adding directives
Two kinds of directives are required in this personal keymap. First of all, the keycode directives, which matches the format seen in the default keymaps. These directives associate a keycode with a keysym. Keysyms represent keyboard actions. The actions available include outputting character codes or character sequences, switching consoles or keymaps, booting the machine, and many other actions. The full currently active keymap can be obtained with

 # dumpkeys -l

Most keysyms are intuitive. For example, to set key 112 to output an 'e', the directive will be:

 keycode 112  = e

To set key 112 to output a euro symbol, the directive will be:

 keycode 112 = euro

Some keysym are not immediately connected to a keyboard actions. In particular, the keysyms prefixed by a capital F and one to three digits (F1-F246) constituting a number greater than 30 are always free. This is useful directing a hotkey to output a sequence of characters and other actions:

 keycode 112 = F70

Then, F70 can be bound to output a specific string:

 string F70 = "Hello"

When key 112 is pressed, it will output the contents of F70. In order to execute a printed command in a terminal, a newline escape character must be appended to the end of the command string. For example, to enter a system into hibernation, the following keymap is added:

 string F70 = "sudo systemctl hibernate\n"

## Other examples
* To make the Right Alt key same as Left Alt key (for Emacs), use the following line in your keymap. It will include the file , check it for details.

 include "linux-with-two-alt-keys"

* To swap CapsLock with Escape (for Vim), remap the respective keycodes:

 keycode 1 = Caps_Lock
 keycode 58 = Escape

* To make CapsLock another Control key, remap the respective keycode:

 keycode 58 = Control

* To swap CapsLock with Left Control key, remap the respective keycodes:

 keycode 29 = Caps_Lock
 keycode 58 = Control

## Saving changes
In order to make use of the personal keymap, it must be loaded with loadkeys:

 # loadkeys /usr/local/share/kbd/keymaps/personal.map

However this keymap is only active for the current session. In order to load the keymap at boot, specify the full path to the file in the  variable in /etc/vconsole.conf. The file does not have to be gzipped as the official keymaps provided by .

## Adjusting typematic delay and rate
The typematic delay indicates the amount of time (typically in milliseconds) a key needs to be pressed and held in order for the repeating process to begin. After the repeating process has been triggered, the character will be repeated with a certain frequency (usually given in Hz) specified by the typematic rate. These values can be changed using the kbdrate command. Note that these settings are configured separately for the console and for Xorg.

 # kbdrate delay rate

For example to set a typematic delay to 200ms and a typematic rate to 30Hz, use the following command:

 # kbdrate -d 200 -r 30

Issuing the command without specifying the delay and rate will reset the typematic values to their respective defaults; a delay of 250ms and a rate of 11Hz:

 # kbdrate

## systemd service
A systemd service can be used to set the keyboard rate. For example:

Then start/enable the  systemd service.

## Layout switching
Layout switching can only be simulated by establishing a different layout on one of the higher layers (typically the 3rd, ).

For a list of layouts that likely support this, run

 $ find /usr/share/kbd/keymaps -exec zgrep -l 'AltGr_Lock' '{}' ';'

You can test this by passing main and augmenting layout to loadkeys, e.g.

 # loadkeys us mk

If it worked, the 3rd level shift () will allow you to access the second layout, the  (often , you will have to inspect the keymap file with zless) will provide an effective toggle.

For a permanent configuration, set the  next to the  in .
