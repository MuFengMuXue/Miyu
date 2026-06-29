# Multi-pointer X

Xorg servers starting from version 1.7 have a feature called "multi-pointer". Basically it allows to have multiple mouse cursors (each with its own keyboard focus) on the screen and control them with separate physical input devices. It can be used as a crude multiseat solution.

## Basic concepts
## Master and slave devices
With the introduction of XInput2, input devices are organised in a two-level hierarchy:
* Master devices, which correspond to cursors on the screen
* Slave devices, which correspond to physical input devices
Master devices come in pairs, one for pointer and one for keyboard. Each master device can have a number of slave devices attached, so that cursor of a master device can be controlled by all slave devices attached to it.

## Client pointer
When an application grabs input (e.g. a fullscreen game), it grabs a master device that is set as its client pointer. By default, the client pointer is set to "Virtual core pointer", but it can be set to a different one with a "xinput" utility.

## Configuration
## configuration file
## xinput utility
More pointers can be added with  CLI utility. Here is how to do it:

Create a new pair of master devices named "name pointer" and "name keyboard":

 xinput create-master ''Find out names and ids of existing slave devices:

 xinput list

Reattach slave devices to newly created master devices:

 xinput reattach [slave device name or id device name or id

For example, say we create a device called "Auxiliary" (use  to reverse this):

 xinput create-master Auxiliary

When we list the xinput devices you should see something like this:

 Virtual core pointer
   >Virtual Core XTEST pointer
   >your main mouse
 Virtual core keyboard
   >Virtual Core XTEST pointer
   >your main keyboard
   >function buttons
 Auxiliary pointer
   >auxiliary XTEST pointer
 Auxiliary keyboard
   >auxiliary XTEST keyboard

What you then want to do is simply attach your secondary mouse and keyboard to the respective auxiliary positions. The XTEST devices are irrelevant here. I found the easiest way to determine whats what was to just unplug stuff and type "xinput list" again.

To attach devices, you type:

 xinput reattach id # "Auxiliary pointer"

and then do so for your keyboard as well!

If the support from the DE/WM is bad for multi-pointer, it would be a good idea to make use of  if the master devices is added to be used by only one window, window id can be found from  or similar tools.

 xinput set-cp id device name or id

Shamelessly stolen from Antonio Ospite at ao2.it

## Troubleshooting
## Flicker
The Compton compositor can cause the cursors to flicker and should be disabled.

## Software support
It is possible to use multi-pointer with software that does not explicitly support it, but with limited functionality. Applications which do not support it will not distinguish between multiple pointers and will interpret all actions as if done by single master device pair.

## Window managers
In window managers multi-pointer support could mean:
* recognizing multiple focuses
* setting the client pointer of a focused window to the pointer that "focused" it
* letting move and resize windows simultaneously
As of 24 December 2016, only multicursor-wm (development stops around 2011) supports multi-pointer.

As of 2020-06-01, Dwm works but not so well, there are focus issues when auto-focus on hover is set in  such that the keyboard focus jumps between application easily.  can be used to aid this behavior.

## Desktop managers
Desktop manager should also be able to provide the same support as Window managers.

As of 2021-01-14, Plasma works quite well such that some applications is able to handle the focus correctly but the tools that it came with such as Application Runner (kickoff) and krunner does not accept input from second master devices.

## Useful links
* Xorg wiki article
* Xorg multiseat. A how-to for a more complicated multi-user environment. Requires 2 different xorg sessions and graphics cards!!
* Article from Suckless DWM
