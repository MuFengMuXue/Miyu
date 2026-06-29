# Chromebook Pixel 2

This page details installing Arch Linux on the Google Chromebook Pixel (2015).  It is commonly referred to as the Chromebook Pixel 2, sometimes referred to by its codename Samus, and sometimes called the Chromebook Pixel LS (which stands for "Ludicrous Speed") when referring to the upgraded version with a Intel Core i7.

## Installation
# Enable developer mode.
# Use the superuser shell in order to enable SeaBIOS.
# You have the option to Boot to SeaBIOS by default so you can boot without any keyboard shortcuts.
# Install Arch Linux.
# Continue reading below to correctly configure GRUB before rebooting.

## GRUB
GRUB does not detect the correct video mode and does not display the menu by default.  is set to auto.    Using , on the grub command line, it is detected at .  The options to display the menu are to either turn off  or set the correct display. In  either,

 GRUB_TERMINAL_OUTPUT=console

or,

 GRUB_GFXMODE=1280x850x16

and then regenerate the configuration file.

If you forget to do this you can boot off the installation media again mount your disks and  in.

## Linux
Touchpad, touchscreen, and audio have been working in the vanilla Linux kernel since v4.9.

## Suspend
Since kernel 5.x suspend seems to not work out-of-the-box anymore and instead shuts down when lid is closed. Install  and , then create:

This should make suspend work on lid close.

## Audio, Brightness, and Touch
 contains some helpful scripts for managing audio (e.g. switching between speaker and headphone output), setting screen backlight and keyboard LED brightness, and fixing the Atmel maXTouch bug (see #Unresolved Issues).

## Audio scripts fail
If audio scripts from above do not work, create

and make sure to install

## Kernel 5.5 Audio Issues
After Linux Kernel 5.5, there is an extra kernel options to enable SST audio driver for bdw-rt5677 (Which is initially disabled after 5.5).
Add the following switches in the kernel parameters to enable audio

 snd_intel_dspcfg.dsp_driver=2

## Enable pulseaudio-alsa without scripts
The hardware and driver mismatch the left and right channel, and it is defaultly muted.
Just run , and turn on the following switches will make audio works:

 Stereo DAC MIXL DAC1 R
 Stereo DAC MIXR DAC1 L

This switches will make all audio works, and enable the auto switch to headphone when connected.

## Keyboard Bindings
xkeyboard-config 2.16-1 added a  model that enables the Chrome OS style functions for the function keys.  You can, for example, set this using .  See the  definition in  for the full mappings.

The search button acts as a  key, which may be undesirable for keyboard layouts that make good use of this position. Using xmodmap, you can rebind this to whatever you would like. Example using  for a keyboard layout with six layers:

 $ xmodmap -e "keycode 133 = Tab Tab Tab Tab Tab Tab"

Add this to your .xinitrc to load at login.

## Unresolved Issues
*  provides a  model which can be specified, for example, with  but when using GNOME on Wayland the model is not recognized. The media keys still behave as function keys and  does not show the  model being used.
* Touchpad occasionally does not work after waking from sleep using linux 4.9-1+. If this happens, reloading the touchpad driver via  usually restores touchpad functionality. This fix is also available as  from .
