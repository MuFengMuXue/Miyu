# HP Chromebook 14

The HP Chromebook 14 (and newer chromebooks in general) features a "legacy boot" mode that makes it easy to boot Linux and other operating systems. The legacy boot mode is provided by the SeaBIOS payload of coreboot. SeaBIOS behaves like a traditional BIOS that boots into the GPT of a disk, and from there into your standard boot loaders like Syslinux and GRUB.

## Installation
Go to the Chromebook page, read the Introduction and continue by following the Installation guide.

## Post Installation Configuration
For information on general Chromebook post installation configuration (hotkeys, power key handling ...) see Post installation configuration on the Chromebook page.

## Touchpad Configuration
Add the Xorg touchpad configuration below for better usability (higher sensitivity).

Reboot for the touchpad to become operational.

## Keyboard Keymapping Fix
We will create a custom hwdb config file to bypass the default mapping in  of the keys between escape and power so they will work as  to  and the search button as  (aka .

Creating the following configuration file:

Then follow the steps at Map scancodes to keycodes#Using udev.

## Adding hotkeys back
Once you have applied the above fix you can set the function and arrow keys to act similar to how they are in ChromeOS using a modifier key. The example below uses  (Search on the chromebook's keyboard). This can be changed to  or  if you prefer.

See Chrome OS devices#Using Xbindkeys.

To make the change permanent, see Xbindkeys#Making changes permanent.

## Locating the Write-Protect Screw
* Remove the visible screws and another 4 hidden screws under rubber stubs (not the rubber feet) at the bottom.
* Flip the laptop right side up and use a thin blunt object to pry the keyboard surface from the bottom half.
* The bios screw is located to the left of the fan, it can be recognized by the fact that the copper circle it sits on is split in half "( )" vs "O". The screw connects the two halves, making the bios unwritable.
* Once this screw is removed, it is advisable to unplug the battery and plug it back in to ensure that the removal is recognized.

See disassembly pictures [https://imgur.com/a/hFq7S and the location of the write-protect screw.
