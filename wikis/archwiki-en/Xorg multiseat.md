# Xorg multiseat

Multiseat is a certain setup where N users work simultaneously on one computer. This is achieved by having N monitors, N keyboards and N mice. The advantages are quite obvious:
* Less power consumption (only one computer)
* Less hardware to purchase

## Requirements
## Keyboards and mice
Any standard PS/2 or USB keyboards will suffice. Same thing for mice.

## Graphics hardware
For the best possible result you will need two graphics cards. I used an nVidia FX5500 AGP and an nVidia 6200 PCI. If you look around a bit you can certainly find new and decent PCI graphics card for a soft price.

It is possible to use only one videocard which has dual heads (like most nvidia cards will have), but this has some limitations: you have to use Xephyr on the second monitor which seems quite a messy solution from what I have read, and for optimal usage both screens need the same resolution.

If you have two pci-express slots, take advantage of them! That way you will even be able to play two games at the same time. (PCI is too slow to play comfortably)

## Processors and memory
If you really are working with two users on the same computer, I would at least recommend a dual-core processor and plenty of RAM. A fast hard drive (10.000 RPM or higher) is also recommended for comfortable use.

## Software
You will need Xorg with the drivers for your graphics card (according to some sources, the closed source nvidia driver works better than the open source nvidia driver for this, I have not tested this myself) and the evdev () driver. That's all. All this can be found in the Arch Linux core and extra repositories.

## Some X knowledge
If you know how X works this will be a lot easier. Before you start, it is recommend generating a clean configuration with  that works with a single screen. Read through this xorg configuration and make yourself familiar. And as usual the manpages will provide you with most of the answers. You may reference some man pages: , , , , .

You can also look at the output of the following commands to get some hints:

## Definitions
For this article to be clear, I will be using the following definitions:
* screen: A screen is something Xorg can display its stuff on. A screen has a monitor and a graphics card assigned to it.
* monitor: A physical monitor like the one you are now sitting in front of.
* server layout: a definition of which screen, keyboard and mouse to use.
* seat: A workplace with a physical monitor, physical keyboard and physical mouse.

## Tips and tricks
* Set up ssh on your computer, so you can ssh to the machine from another computer (such as a laptop). This is very useful because you will probably run into X not responding anymore or not giving you picture at all.
* Finding out which keyboard and mouse is which: open a terminal and use cat to find out. For example, . If you then move your mouse and you see all weird things happening than that is the mouse you are moving. Same goes for keyboards, which are called eventN.
* Try a basic configuration first. Do not start with the fancy stuff yet, get a very basic Xorg working first.
* Create a backup of all relevant configuration files. What do you mean you will skip this one?

## About evdev
evdev is an Xorg driver which can make use of the kernel event devices, which you can find in .

## Attaching devices to a seat
systemd's  lets you assign devices to seats by creating udev rules.

## Identify devices
Look at the default seat (seat0) status, here is an example:

If you are unsure, try comparing with or  to identify devices.

## Assign devices
Seats are created based on graphics cards. Hence we will start by assigning a graphics card:

Then add input devices.  This first example (not recommended) adds three USB devices by port and subdevice from the list above:

This is less than ideal, because replacing the keyboard with another will only work if the new keyboard contains the same subdevices ( and ), and if the keyboard and mouse are accidentally swapped into each other's USB port, they will not be assigned to the intended seat and will end up back in the default .  It would be more flexible to add a specific USB port to the seat instead, allowing any device plugged into that USB port to be assigned to the seat (keyboard, mouse, USB sound card, etc.)  Here, two USB ports are assigned to the seat, which you can see has just come from the same list above with the end part removed:

With multiple sound cards you can assign one per seat that will run out of the box with per user session PulseAudio:

You should be able to see that the hardware has been partitioned into two seats:

The seat names are just string tags, so you can call a seat anything you like - ,  and  are all valid names.  While you do not have to use the  prefix, this is not recommended as some programs (e.g. LightDM) apply their default options only to seats matching the expression , so any name that does not start with the word  may require extra manual configuration.   is the default seat name and cannot be changed.

Any device that is not specifically tagged to a seat will end up in .  If a device is tagged to a given seat, then all child devices belong to that seat as well.  This is most useful with hot pluggable interfaces, such as the above example that assigns USB ports to specific seats so that any devices plugged into those ports will automatically inherit the seat set on on the USB port itself.

 creates and deletes udev rule files matching , so if you wish to back up your seat configuration, these are the files to save and restore.

Each seat will not appear as ready until a device tagged  appears.  The default udev rules automatically apply this tag to any  or  device.  Thus if you do not make a one of these devices part of a seat (e.g. a visually impaired user with only keyboard and audio) then the udev rules created by  will need to be manually edited and this tag specified before the seat becomes available for use.  Look at the default udev rules for examples.

## Setting up Xorg
Since you can attach devices to seats with loginctl there is no need to have an specific Xorg configuration, so if you attached devices via loginctl creating Xorg configuration files may be skipped. Also note that setting  options to  forces Xorg to just ignore most of the loginctl attachments.

If you do choose to use a custom Xorg configuration (for example you have an nVidia card and want to set advanced display options) then the process is much the same as usual, with the major difference being that you define one  section for each seat, and include the  statement in each server layout to indicate which seat it should apply to.  You can also apply  directives to graphics devices and monitors themselves to avoid defining a , if you do not need any  functionality.  Be aware that any section missing a  directive will be visible for all server layouts and seats, so make sure some other part of the configuration prevents multiple seats from trying to access the same devices.  (A common mistake is allowing both seats to access the same display device, which will result in one seat working and the others failing to start.)

An example follows for this type of manual configuration.  You can create parts of, or the entire, configuration set for two server layouts, each assigned with their own keyboard, mouse, video card and monitor.  If you omit a part (such as the  section), then the Xorg defaults will apply.

## Defining available input devices
This part of the configuration tells Xorg which input devices it has available. Input devices are keyboards and mice, but can also be, for example, touchscreens and pens.

Configure your devices as read in Xorg#Input devices. The "Identifier" will let you assign to a ServerLayout and "Device" defines which physical device are you configuring.

Same for other input devices.

## Monitors
Configure your monitors as seen on Xorg#Monitor settings. Pay close attention to the identifier.

## ServerFlags
## Graphics card
Take a close look at the BusID. This option specifies which hardware card to use. You can find out the BusId's with . However, you will soon find out this does not always match. That's because lspci displays the device address in hexadecimal form. Xorg however uses decimal form. So you will need to convert your address from hexadecimal form to decimal. Thus a device address of 0:0a:0 in lspci would become 0:10:0 in .

Another more advanced example where nVidia TwinView is used so that one seat has dual monitors, with one monitor landscape and the other portrait:

{{hc|42-graphic-seat-nvidia.conf|2=
Section "Device"
        Identifier "nvidia"
        Driver "nvidia"
        BusID "PCI:66:0:0"  # lspci reports this as 42:00.0, so 42 hex is 66 decimal

        # See the nVidia documentation for what these options do.  They of
        # course only apply if you have an nVidia card and you are using their
        # closed-source driver.
        Option "UseDisplayDevice" "DP-3"
        Option "MetaModes" "DP-3: 2560x1600, DP-0: 1600x1200 { Rotation=left }"
        Option "TwinViewOrientation" "LeftOf"

        # Not needed, avoid errors in logs
        Option "ConnectToAcpid" "false"

        # Do not automatically set the DPI based on screen size, use the traditional
        # value to avoid fonts becoming overly large.
        Option "UseEdidDpi" "False"
        Option "DPI" "96 x 96"

        # No MatchSeat option is needed here if it's given in the ServerLayout instead.
        #Option "MatchSeat" "seat-nvidia"
EndSection
}}

## Screens
Pay close attention to the "monitor" option.

## ServerLayout
Create a section for every seat (pay attention to Identifier) you have with their respective keyboards, mice and screens.

Additional Tips:

* Make sure to delete the  file in respective user directories before the initial reboot.

* To avoid tearing this seems to help on nearly all configurations - add this to /etc/environment:

## Testing
Before we start modifying our login manager, we will first start with testing out the individual seats. If these are working, then we are good to go.

I have used twm (tiny window manager) to test out if my seats work, but there is no reason you cannot use KDE, gnome, or any other desktop environment or window manager. I have used this in my :
 exec twm

Use the following command to test out an individual seat:
 startx -- -layout seat0 -config xorg.conf.multiseat

Do this for every seat you have. If they are all working correctly and the keyboard/mouse combination matches, then congratulations! You are almost finished! In case you are wondering why I did not you use the full path to my new configuration file, that's because X does not allow that when running as non-root. It will search for xorg.conf.multiseat relative to .

## Setting up the loginmanager
## For XDM
Open  and set the following variables (This sample demos two seats):

Also if you use the Arch Linux theme edit  for every screen:

## For LightDM
LightDM has automatic multiseat detection (pulling from the seat list provided by ).  If you have a manual Xorg configuration file and want to use it, make sure you specify valid  values there (see above).  This is because LightDM automatically passes  or similar to , so Xorg will ignore any sections that have a  that does not match the current seat.  (So if you forget to specify  at all, those sections will apply to every seat which, in the case of display devices, means one or more seats likely will not start at all as they all compete for the same display.)

If you need you can configure it on

## For Auto Login multiseat (without Display Manager)
edit a script /boot/twin.sh

## Sound
## One sound card for each seat
As soon as you attach the sound card to the seat, PulseAudio will detect and use it.

## Multiple users on single sound card: PulseAudio
If two users want to use the sound card simultaneously, it is necessary to use a sound server, PulseAudio being most prevalent. Usually, the PulseAudio server runs only for active user and does not allow for multiple user instances. Solution to this problem is using the system-wide PulseAudio server. Although this approach is discouraged by its authors, it is probably most applicable setup.

;Configuring for multiple users, without system-mode daemon
This results in all the mixing transferred to a single server.

Copy the default configuration to the main user's home directory:

 $ cp /etc/pulse/default.pa ~/.pulse/

or:

 $ cp /etc/pulse/default.pa ~/.config/pulse/

Edit the file, adding at the end:

 load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1

Restart PulseAudio, if already running:

 $ pulseaudio -k
 $ pulseaudio --daemonize=no

Repeat this procedure for each secondary user, as the user:

 $ echo "default-server = 127.0.0.1" > ~/.pulse/client.conf

;Configuring for system-wide PulseAudio
* Create user pulse and put it into group audio (PulseAudio drops root privileges and changes to user pulse. Group membership allows for device access.)
* Create group pulse-access and put users, who will play sound locally into it (Group membership is used for access control for local access to PA daemon.)
* In /etc/pulse/default.pa state explicitly the access rights

 load-module module-native-protocol-unix auth-group=pulse-access
 auth-group-enable=1

Create /etc/dbus-1/system.d/pulseaudio.conf with this content
/etc/dbus-1/system.d/pulseaudio.conf:

Start PA as system-wide, under root:

 # pulseaudio --system

In  should appear files for communication with
daemon, namely pid and native.

;User access
You can check communication with system daemon as non-root by e.g. .

It is possible to enable automatic network connection to local daemon in :

 auto-connect-localhost = yes

The users should be able to connect to PA server. All the cons for system-wide daemon become essentially pros, e.g. ability to control volume of other users streams in pavucontrol.

;Troubleshooting
It is possible to enable the http interface to PA for debugging in /etc/pulse/default.pa  and then connect to it at http://localhost:4714/

## Multiple users on single sound card: ALSA
Setup with PulseAudio removed, shared audio through an  equalizer and software mixing. The relevant hardware used is an ATI Radeon HD 5850 and an Intel Sandy Bridge (onboard) HD 3000. Configuration steps may vary.

Specific hardware could be addressed in  to allocate audio to both users simultaneously if required. Another option enables two different users to both access audio with their own equalizer (described further down). The sound card will be shared equally among the seats using ALSA with PulseAudio removed - libpulse itself should be kept for various software dependencies however.

Next, remove respective  files (as well as related PulseAudio configuration files if you removed that) and follow this template with  for sound:

{{bc|
defaults.pcm.rate_converter "samplerate_best"

ctl.equal {
 type equal;
}

pcm.plugequal {
  type equal;
  # Modify the line below if you do not
  # want to use sound card 0.
  #slave.pcm "plughw:0,0";
  #by default we want to play from more sources at time:
  slave.pcm "plug:dmix";
}
#pcm.equal {
  # If you do not want the equalizer to be your
  # default soundcard comment the following
  # line and uncomment the above line. (You can
  # choose it as the output device by addressing
  # it with specific apps,eg mpg123 -a equal 06.Back_In_Black.mp3)
pcm.!default {
  type plug;
  slave.pcm plugequal;
}
}}

Only the last user to login will have audio control and access but if
you wish to share audio equally among different users, add each user to
the audio group:

Example:

Then put this in each user's respective ~/.asoundrc rather than using /etc/asound.conf (this option also contains various tweaks to improve audio quality):
{{bc|1=
defaults.pcm.rate_converter "samplerate_best"

ctl.equal {
 type equal;
}

pcm.ossmix {
    type dmix
    ipc_key 1024 # must be unique!
    ipc_key_add_uid false   # let multiple users share
    ipc_perm 0666           # IPC permissions for multi-user sharing (octal, default 0600)
    slave {
        pcm "hw:0,0"      # you cannot use a "plug" device here, darn.
        period_time 0
        period_size 1024 # must be power of 2.
        buffer_size 8192  # ditto.
        rate 44100
       #format "S32_LE"
       #periods 128 # dito.
       #rate 8000 # with rate 8000 you *will* hear,
       # if ossmix is used :)
    }
    # bindings are cool. This says, that only the first
    # two channels are to be used by dmix, which is
    # enough for (most) oss apps and also lets
    # multichannel chips work much faster:
    bindings {
        0 0 # from 0 => to 0
        1 1 # from 1 => to 1
    }
}

pcm.plugequal {
  type equal;
  # Modify the line below if you do not
  # want to use sound card 0.
  #slave.pcm "plughw:0,0";
  #by default we want to play from more sources at time:
  slave.pcm "plug:ossmix";
}

#pcm.equal {
  # If you do not want the equalizer to be your
  # default soundcard comment the following
  # line and uncomment the above line. (You can
  # choose it as the output device by addressing
  # it with specific apps,eg mpg123 -a equal 06.Back_In_Black.mp3)
pcm.!default {
  type plug;
  slave.pcm plugequal;
}
}}

Accessing the equalizer can be done with:

Each user has an equalizer they can configure separately.

Make sure to turn down and mute the audio channels that you do not use, turn off auto-mute microphone, and make sure no channel has a gain higher than 0 to avoid ALSA audio bugs. This can be done via alsamixer.

## Troubleshooting
## Xorg will not start
Look at the log files in .  There will be one for each seat.  Reading the log file will show you which devices the seat is trying to use, and you may see something like both seats are trying to use the same display device, because you have not correctly assigned it to a particular seat.

If you are using a display manager, find out where its log files are so you can check that it is starting the Xorg server properly, and passing the required  parameter.

## My Windows key does not work anymore
Put this in a startup file:
 xmodmap -e "add Mod4 = Super_L Super_R"

## Unreliable behaviour (black picture without cursor)
If everything seems to be set up correctly, but for some reason you always get a black picture without a cursor, try setting the first initialized card in the BIOS to be the PCI card one.

## Little black boxes/dots on the desktop
This is actually portions of the virtual terminals being painted on top of X. It seems to be caused by the Linux kernel framebuffer. This can be fixed by disabling the framebuffer, or by removing the "-sharevts" option from the primary seat's X args.

## Multimedia keys not working
If your keyboard(s) has extra "multimedia" keys, you may find that they stopped working in your multiseat setup. This is because such keyboards are often represented as more then one "event" device. As you did above, cat each /dev/input/event* device, this time pressing multimedia keys. Once you have found the right event device, add a separate keyboard InputDevice section for it, then add that InputDevice section to the corresponding ServerLayout section with the "SendCoreEvents" option, which indicates that input from this device should be handled, despite not being the core keyboard. In the end you should have sections something like the following:

## The Ctrl-Alt-Fx, Alt-Fx keys mess up with virtual terminals
(Oct 2010) I follows this guide and everything works, except for Alt-F1, Alt-F2,... mess things up. Then I follow this guide https://help.ubuntu.com/community/MultiseatX (read the part for Ubuntu 10.04):

Then fix in the /usr/share/config/kdm/kdmrc as follow

It works for my computer: one on-board Intel card (xf86-video-intel driver), and one Nvidia card (xf86-video-nouveau driver). You can check if the parameters are passed correctly by:

The ServerVT=7, ServerVT=8 would be pass to as vt7, vt8

## Fix VT behaviour using fbcon kernel parameter
Pass  to the kernel command line. (Number can differ, see the kernel documentation)

The value above cause  switching on video card number n, other video cards just show Xorg.
