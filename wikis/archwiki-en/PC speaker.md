# PC speaker

PC speaker—beeper—is a built-in loudspeaker in most personal computers since the first IBM PC. This speaker is not capable of high quality playback and merely serves as a simple means of auditory feedback in the form of beeps. Some software—e.g. web browsers, editors and terminals—may produce beeps which may or may not be desired by the user. This article serves as a guide for configuring and/or disabling the speaker entirely.

For situations where no sound card or speakers are available and a simple audio notification is desired, see #beep.

## Mechanism
The PC speaker is typically a physical unit connected on the front connections header of the motherboard. Some motherboard manufacturers do not ship their motherboards with a PC speaker at all, whereas others may have the PC speaker soldered directly onto the surface. Laptops typically have no physical PC speaker but have the beeper routed to the laptop internal speakers. In some cases, the beeper is heard on the regular output—i.e. speakers or headphones—of the soundcard, which tends to be unexpectedly loud.

Upon boot the UEFI/BIOS will traditionally generate a beep during power-on self-test (POST). Recent motherboard models omit the POST beep in favor of rapidly booting into the operating system. The UEFI user interface typically allows for toggling the POST beeps but it cannot configure the PC speaker to be turned off completely.

Once the system has booted into Linux and the  kernel module is loaded, the PC speaker can be used by the environment, be invoked manually by the user, and be configured to some extent.

Because the PC speaker is controlled directly by the CPU, along with the fact that they are built for beeping only, PC speaker cannot be used for playing back audio files. If this is really desired, unloading the  module and installing the  package provides a rudimentary audio output.

## Disabling the PC speaker
## Physically
By removing the PC speaker the system will not be able to produce beeps. This can be achieved by physically removing the unit from the motherboard (if possible). Some manufacturers may provide a jumper header to switch it off.

## Globally
The PC speaker can be disabled by unloading the  and  kernel modules:

 # rmmod pcspkr
 # rmmod snd_pcsp

Blacklisting the  and  modules will prevent udev from loading them at boot. Create the file:

Blacklisting it on the kernel command line is yet another way. Simply add  to your boot loader kernel line.

## Console
## Virtual console
In virtual console (TTY) you can set the bell duration to zero milliseconds with :

 $ setterm --blength=0

## Readline-aware shell
For a shell which utilizes the Readline library (e.g. Bash), uncomment this line in  (or add it to ):

 set bell-style none

## Less pager
To disable PC speaker in  pager, you can launch it with  to mute PC speaker for end of file events, or  to mute it altogether. For man pages, launch  or set the  or  environment variables.

Alternatively, you can add these lines to your shell configuration file:

 alias less='less --QUIET'
 alias man='man --pager="less --QUIET"'

## Arch Linux ISO
If you want to disable the init tune on the Arch Linux ISO, you will need to repack the ISO. To do so, first install the  and  packages.

Extract the El Torito boot images and systemd-boot configuration () from the ISO:

 $ osirrox -indev archlinux-YYYY.MM.DD-x86_64.iso -extract_boot_images ./ -extract /loader/loader.conf loader.conf

Make  writable and remove the  option from it:

 $ chmod +w loader.conf
 $ sed '/^beep on/d' -i loader.conf

Add the modified  to the El Torito UEFI boot image:

 $ mcopy -D oO -i eltorito_img2_uefi.img loader.conf ::/loader/

Finally, repack the ISO using the modified boot image and :

## ALSA
For most sound cards the PC speaker is listed as an ALSA channel, named either PC Speaker, PC Beep, or Beep. To mute the speaker, either use  or , for example:

 $ amixer set 'PC Speaker' 0% mute

To unmute the channel, see Advanced Linux Sound Architecture#Unmuting the channels.

## Cinnamon
Cinnamon seems to play a "water drop" sound. To disable it, set in :

 $ gsettings set org.cinnamon.desktop.wm.preferences audible-bell false

## GNOME
Using GSettings:

 $ gsettings set org.gnome.desktop.wm.preferences audible-bell false

## GTK
Append this line to :

 gtk-error-bell = 0

Add the same line to the section of :

 [Settings
 gtk-error-bell = 0

This is documented in the Gnome Developer Handbook.

## Plasma
Bell notification settings can be modified in System Settings > Accessibility Options > Bell.

## PulseAudio
Play a sound instead of a PC speaker beep using PulseAudio#X11 Bell Events.

## Xorg
 $ xset -b

You can add this command to a startup file such as  to make it permanent. See xprofile and  for more information.

## beep
 is a PC speaker beeping program. beep is useful for situations where no sound card and/or speakers are available, and simple audio notification is desired.

## Installation
Install the  package.

You may also need to unmute the PC speaker in ALSA.

## Configuration
beep uses  to control the PC speaker which belongs to the  group, but adding user to  is not recommended by an upstream. To access the device file one has to set the proper permissions.

The following rule will allow any user, who is logged into the currently active virtual console session, to use the PC speaker:

{{hc|/etc/udev/rules.d/70-pcspkr-beep.rules|2=
ACTION!="remove", SUBSYSTEM=="input", ATTRS{name}=="PC Speaker", ENV{DEVNAME}!="", TAG+="uaccess"
}}

Previous solution does not allow to use beep for users logged in remotely—e.g. via OpenSSH,—or processes running as any user other than the one logged into the currently active virtual console session. Alternatively, a new user group may be created with the corresponding rule to set the right permissions on the device file. With this solution any user in the  group will be able to control the PC speaker:

 ACTION=="add", SUBSYSTEM=="input", ATTRS{name}=="PC Speaker", ENV{DEVNAME}!="", GROUP="beep", MODE="0620"

To force reloading rules and device file to apply new user permission without a reboot, execute:

 # udevadm control --reload && rmmod pcspkr && modprobe pcspkr

## Usage
The following example plays slightly higher and shorter sound than beep default—see ,—and repeats it two times:

 $ beep -f 500 -l 50 -r 2

Repositories collecting shell scripts playing various music using beep:

* https://github.com/NaWer/beep
* https://github.com/ShaneMcC/beeps

See also .

## Troubleshooting
## The HD Audio power-saving mode mutes the PC speaker
The PC speaker might remain silent when the HD Audio sound card is in power-saving mode. Apparently—depending on hardware—the beeps are actually fed as an analog input into the card, and will be ignored if the card is asleep. You can debug this by playing music (to keep the card awake) in one virtual console and then beeping in another.

For more information, see Advanced Linux Sound Architecture/Troubleshooting#Power saving.
