A multiseat system is a computer system with multiple hardware terminals, allowing two or more users to use a single computer. While Linux systems running Xorg always supported multiseat, the level of support changed a lot over time.

** Important**\
This HOWTO\'s goal is creating a cooperative multiseat environment, allowing users to share access to all storage, sound (if desired) and other devices. **Security will therefore be lax.**

## Contents

-   [[1] [Choosing hardware]](#Choosing_hardware)
    -   [[1.1] [Graphics]](#Graphics)
    -   [[1.2] [Input devices]](#Input_devices)
    -   [[1.3] [Sound]](#Sound)
-   [[2] [Multiseat Configuration]](#Multiseat_Configuration)
    -   [[2.1] [Identify devices]](#Identify_devices)
    -   [[2.2] [Assign devices]](#Assign_devices)
    -   [[2.3] [Troubleshooting]](#Troubleshooting)
-   [[3] [X server]](#X_server)
-   [[4] [Sound]](#Sound_2)
    -   [[4.1] [Single shared sound card]](#Single_shared_sound_card)
    -   [[4.2] [Single split sound card and/or multiple sound cards]](#Single_split_sound_card_and.2For_multiple_sound_cards)
        -   [[4.2.1] [ALSA]](#ALSA)
        -   [[4.2.2] [PulseAudio]](#PulseAudio)
    -   [[4.3] [Single sound card per seat]](#Single_sound_card_per_seat)
-   [[5] [Bypassing polkit]](#Bypassing_polkit)
-   [[6] [Testing]](#Testing)

## [Choosing hardware]

### [Graphics]

When designing a multiseat system, the first consideration should be support for multiple graphics adapters. The simplest way to build a system is to make all graphics adapters the same (i.e. use the same chipset, they don\'t need to be identical). All adapters will use the same graphics drivers and no complications should arise.

It is also possible to use entirely different graphics adapters. Such configurations do work, but issues may arise. While it is OK to mix different adapters that all have e.g. Mesa drivers, it is a bad idea to mix adapters with different proprietary drivers with each other or with a mesa driver. Proprietary drivers bring with them their own OpenGL drivers. Thus, Nvidia and AMD drivers are incompatible both with each other and with Mesa. A mixed system will still work, but since only one OpenGL stack can be used at once (chosen by *eselect opengl*), only one kind of graphics card will have any kind of acceleration.

If ultimate performance is not required (as is the case most of the time --- multiseat systems are usually not meant to be gaming rigs), it is recommended to go for an all-mesa stack using AMD cards because it is the easiest to set up and offers acceptable performance and functionality. Otherwise, choose Nvidia with proprietary drivers. The free nouveau drivers for Nvidia cards are, as of 2020, required for older graphics cards no longer supported by proprietary drivers.

Pick a motherboard with multiple large PCIE slots (x16 or x8), depending on how many seats are desired. Slower graphics cards that fit into smaller PCIE slots are available, as are cards for the PCI bus, but they are rarer and thus more expensive so it is prudent to instead invest in a more capable motherboard.

### [Input devices]

Xorg stack supports USB device hotplugging in a multiseat configuration. To make this easier, it is recommended to provide each seat with its own USB hub, preferably powered. This way, unknown devices can be bound to a specific seat depending on which hub they are plugged into. Otherwise, only devices known when configuring the system can be bound to their seats.

### [Sound]

There are several options:

-   use one sound card per seat;
-   use a single sound card, sound is shared between seats;
-   use a single multi-channel sound card and split channels into virtual sound cards.

All options work well and are described below, so choose according to the necessary requirements of the system. The easiest way to get the first option is to either use USB sound cards or to use graphics cards with HDMI outputs, since they can provide sound as well.

## [Multiseat Configuration]

These Desktop Managers support Multiseat Configuration out of the box if either [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") or [Elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") is used:

-   [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM")
-   [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM")

\

### [Identify devices]

Look at the default seat (seat0) status, here is an example:

`user `[`$`]`loginctl seat-status seat0`

     seat0
            Sessions: *11
             Devices:
                      ├ /sys/devices/pci0000:00/0000:00:02.0/0000:03:00.0/drm/card0
                      │ (drm:card0)
                      ├ /sys/devices/pci0000:00/0000:00:02.0/0000:03:00.0/graphics/fb0
                      │ (graphics:fb0) "radeondrmfb"
                      ├ /sys/devices/pci0000:00/0000:00:02.0/0000:03:00.1/sound/card1
                      │ (sound:card1) "Generic"
                      │ └ /sys/devices/pci0000:00/0000:00:02.0/0000:03:00.1/sound/card1/input15
                      │   (input:input15) "HD-Audio Generic HDMI/DP,pcm=3"
                      ├ /sys/devices/pci0000:00/0000:00:12.0/usb3
                      │ (usb:usb3)
                      │ ├ /sys/devices/pci0000:00/0000:00:12.0/usb3/3-1/3-1:1.2/0003:046D:C52B.0006/input/input5
                      │ │ (input:input5) "Logitech Unifying Device. Wireless PID:101b"
                      │ └ /sys/devices/pci0000:00/0000:00:12.0/usb3/3-1/3-1:1.2/0003:046D:C52B.0006/input/input6
                      │   (input:input6) "Logitech Unifying Device. Wireless PID:200a"
                      ├ /sys/devices/pci0000:00/0000:00:14.2/sound/card0
                      │ (sound:card0) "SB"
                      │ ├ /sys/devices/pci0000:00/0000:00:14.2/sound/card0/input7
                      │ │ (input:input7) "HDA ATI SB Line"
                      │ └ /sys/devices/pci0000:00/0000:00:14.2/sound/card0/input9
                      │   (input:input9) "HDA ATI SB Rear Mic"
    >>>               ├ /sys/devices/pci0000:00/0000:00:04.0/0000:02:00.0/drm/card1
                      │ (drm:card1)
    >>>               ├ /sys/devices/pci0000:00/0000:00:04.0/0000:02:00.0/graphics/fb1
                      │ (graphics:fb1) "radeondrmfb"
    >>>               ├ /sys/devices/pci0000:00/0000:00:04.0/0000:02:00.1/sound/card2
                      │ (sound:card2) "HDMI"
    >>>               │ └ /sys/devices/pci0000:00/0000:00:04.0/0000:02:00.1/sound/card2/input16
                      │   (input:input16) "HDA ATI HDMI HDMI/DP,pcm=3"
    >>>               ├ /sys/devices/pci0000:00/0000:00:12.1/usb4/4-1/4-1:1.0/input/input2
                      │ (input:input2) "CHESEN PS2 to USB Converter"
    >>>               ├ /sys/devices/pci0000:00/0000:00:12.1/usb4/4-1/4-1:1.1/input/input3
                      │ (input:input3) "CHESEN PS2 to USB Converter"
    >>>               └ /sys/devices/pci0000:00/0000:00:12.1/usb4/4-2/4-2:1.0/input/input4
                        (input:input4) "Microsoft Microsoft 3-Button Mouse with IntelliEye(TM)"

If unsure, try comparing with [lspci] or [lsusb] to identify devices.

### [Assign devices]

Seats are created based on graphics cards. Hence, first start by assigning a graphics card:

`root `[`#`]`loginctl attach seat1 /sys/devices/pci0000:00/0000:00:04.0/0000:02:00.0/drm/card1 `

`root `[`#`]`loginctl attach seat1 /sys/devices/pci0000:00/0000:00:04.0/0000:02:00.0/graphics/fb1 `

Then, add input devices:

`root `[`#`]`loginctl attach seat1 /sys/devices/pci0000:00/0000:00:12.1/usb4/4-1/4-1:1.0/input/input2 `

`root `[`#`]`loginctl attach seat1 /sys/devices/pci0000:00/0000:00:12.1/usb4/4-1/4-1:1.1/input/input3 `

`root `[`#`]`loginctl attach seat1 /sys/devices/pci0000:00/0000:00:12.1/usb4/4-2/4-2:1.0/input/input4 `

With multiple sound cards, assign one per seat that will run out of the box with per user session pulseaudio:

`root `[`#`]`loginctl attach seat1 /sys/devices/pci0000:00/0000:00:04.0/0000:02:00.1/sound/card2/input16 `

`root `[`#`]`loginctl attach seat1 /sys/devices/pci0000:00/0000:00:04.0/0000:02:00.1/sound/card2 `

Finally, review the status to verify the hardware has been partitioned into two seats:

`user `[`$`]`loginctl seat-status seat0 `

`user `[`$`]`loginctl seat-status seat1 `

[loginctl attach] creates and deletes udev rule files matching [/etc/udev/rules.d/72-seat-\*.rules], so if you wish to back up your seat configuration, these are the files to save and restore.

### [Troubleshooting]

To reset all the previously assigned rules and start over with an empty config use:

`root `[`#`]`loginctl flush-devices `

## [X server]

Best practice for a multiseat [X server](https://wiki.gentoo.org/wiki/X_server "X server") configuration is to leave as much as possible *unconfigured* and rely on auto-detection.

Options specific to each seat can be provided in separate config files located in [/etc/X11/] if ever necessary.

Options common to all seats should reside in files in [/etc/X11/xorg.conf.d/]. These files are always read after the main [xorg.conf] file. The following file is needed to maintain the gpu separation:

[FILE] **`/etc/X11/xorg.conf.d/01-gpu_separation.conf`Maintain GPU separation**

    Section "ServerFlags"
            Option "AutoAddGPU" "off"
            Option "AutoBindGPU" "off"
            Option "SingleCard" "true"
    EndSection

Another example of such a setting could be keyboard layouts.

[FILE] **`/etc/X11/xorg.conf.d/00-keylayouts.conf`Default keyboard settings for all seats**

    Section "InputClass"
        Identifier  "Default Layout"
        MatchIsKeyboard "yes"
        Option      "XkbModel"   "evdev"
        Option      "XkbLayout"  "us"
        Option      "XkbOptions" "terminate:ctrl_alt_bksp"
    EndSection

## [Sound]

### [Single shared sound card]

Nowadays, ALSA is configured for software audio mixing by default, so nothing special needs to be done to support a shared sound configuration.

### [][Single split sound card and/or multiple sound cards]

Suppose the system has a 7.1 sound card integrated on the motherboard, while each graphics card also supports audio output through HDMI. This section describes how to configure all of them at once; cull the examples to your needs.

We will take the 7.1 sound card with several output jacks and configure it so that two of its jacks will act as separate PCM devices while the microphone jack is shared. This makes sense since presumably both users sit in the same room and can use only one microphone.

Next, the default sound cards are configured to be routed to PulseAudio. Since each user will have two sound cards at their disposal, using pulseaudio makes it easy to move audio streams between them. In addition, since all users sit in the same room, it makes sense for them to use headphones. If, however, one has speakers at his disposal, PulseAudio allows others to use them if they need to by pointing their programs to his PulseAudio server. PulseAudio thus allows a great deal of flexibility for audio usage.

#### [ALSA]

The ALSA configuration is global and resides in [/etc/asound.conf]:

[FILE] **`/etc/asound.conf`ALSA configuration**

    pcm.pulse
    ctl.pulse
    pcm.!default
    ctl.!default

    pcm.int
    pcm.dshare
        bindings
    }
    pcm.rshare
    }

    pcm.righto
        ttable.0.2 1
        ttable.1.3 1
    }
    pcm.lefto
        ttable.0.0 1
        ttable.1.1 1
    }

    pcm.left_sound
    pcm.right_sound

The first four blocks simply enable the PulseAudio plugin and set the defaults to go through it.

The pcm.int block gives the .int name to the \"SB\" sound card, which is our example integrated sound card. Different ways can be used to identify sound cards, such as \"hw0,0\". You can get this information using the [aplay] utility\'s `-l` and `-L` options.

The .dshare pcm is a software mixing (dmix) device, which spans two physical jacks. The IPC key needs to be defined so that all programs from all users share the same dmix device, and permissions must allow this too. The .dshare device is defined to use only 4 channels of the .int device and channel bindings are made explicit.

The .rshare device is a dsnoop device, which is a software mixer like dmix but for audio input. This is the microphone jack which all users share.

The .righto and .lefto devices use the .dshare device, but limit themselves to two channels each, using a transfer table specification. They need to specify 4 channels, but the table maps only channels 0 and 1 to channels 0,1 and 2,3 for left and right seats, respectively.

The .left_sound and .right_sound are the actual PCMs the users should use since they combine the channel-mapped outputs with the common .rshare input. If there was no PulseAudio in the mix, these devices should be set as default in the per-user [.asoundrc] files.

Note that there is no mention of HDMI cards. We leave handling those to PulseAudio.

#### [PulseAudio]

Each user runs their own PulseAudio server. This server needs to be configured according to the seat the user is at. We therefore need to prepare per-seat configurations. But pointing the users\' PulseAudio servers to the correct files is not trivial: while the config file can be provided on the command line, PulseAudio servers tend to be started as needed by the programs that output audio and we don\'t have much control over their command lines. A more persistent solution is then to point the default per-user configuration file [\$HOME/.pulse/default.pa] to a seat-specific config file.

First, we prepare the seat-specific files in /etc/pulse. Change the example default.pa file provided by pulseaudio to disable the udev autodetection module, then add the sound cards as below.

[FILE] **`/etc/pulse/left_seat.pa`Left seat sound**

    load-module module-alsa-sink device=left_sound
    load-module module-alsa-source device=left_sound
    load-module module-alsa-card device_id="1" name="pci-0000_01_00.1" card_name="alsa_card.pci-0000_01_00.1" tsched=yes ignore_dB=yes

[FILE] **`/etc/pulse/right_seat.pa`Right seat sound**

    load-module module-alsa-sink device=right_sound
    load-module module-alsa-source device=right_sound
    load-module module-alsa-card device_id="2" name="pci-0000_05_00.1" card_name="alsa_card.pci-0000_05_00.1" tsched=yes ignore_dB=yes

The specification is straightforward. The options for the HDMI sound cards can be obtained by running a pulseaudio instance *with* autodetection and dumping its settings.

Next, we configure the desktop manager to choose the right configuration at login. The XDM-based desktop managers such as KDM have an [Xstartup] file which runs after the X server starts but before the user\'s session is started. It runs as root, but points the HOME variable to the user\'s home. More information is available in the XDM\'s [man page](https://wiki.gentoo.org/wiki/Man_page "Man page").

[FILE] **`/usr/share/config/kdm/Xstartup`Login configuration**

    #!/bin/sh
    case $DISPLAY in
        :0)
            pulseconfig=/etc/pulse/left_seat.pa
            ;;
        :1)
            pulseconfig=/etc/pulse/right_seat.pa
            ;;
    esac

    cd "$HOME"/.pulse/ || exit 0
    [ -h default.pa -o ! -e default.pa ] || exit 0
    dest=$(readlink default.pa)
    if [ ! "$dest" = $pulseconfig ] ; then
        rm default.pa
        ln -s $pulseconfig default.pa || exit 1
    fi
    su -l -c 'pulseaudio -k; pulseaudio -D' $USER
    true

This script simply checks whether the \$HOME/.pulse/default.pa file is a symlink and whether it points to the correct config file. If not, it recreates the correct symlink. It then restarts the PulseAudio daemon; they tend to hang around.

To prevent PulseAudio and possibly other user-launched audio servers such as Music Player Daemon from running while the user is logged in and preventing audio access to other users, we can stop them using the Xreset script.

[FILE] **`/usr/share/config/kdm/Xreset`Logout configuration**

    #!/bin/sh
    su -l -c 'mpd --kill; pulseaudio -k' $USER

### [Single sound card per seat]

For the ones who don\'t like PulseAudio and want to assign sound card per seat, here is possible way. Verify [aplay] is installed or the system. Take note that the output of [aplay -l] will decide which card to attach to which seat so make sure you attach the cards in the right order.

All users should have at least the following file in their home folder (thanks to the guys at alsa mailing list for the help):

[FILE] **`~/.asoundrc`asoundrc basic config**

    defaults.pcm.card 0
    defaults.ctl.card 0

this file defines which sound card to use.

Now under [/etc/profile.d], put the next file:

[FILE] **`/etc/profile.d/define_sound_card.sh`logon seat sound card def script**

    #!/bin/bash
    SOUND_CARD_ID=0

    if [ "$(whoami)" != "root" -a -f ~/.asoundrc -a $(who | grep "$" | grep -cv "pts") -eq 1 ]; then
            index=$(($(echo "$" | cut -f2 -d:)+1))
            line="$(arecord -L | grep -A1 sysdefault  |  tr '\n' ' ' | sed 's/ -- /\n/g' | sed $'q;d')"
            regex="$(echo "$" | sed -e 's/sysdefault:CARD=/\.\*/g;s/,/\.\*/g;s/[[:blank:]][[:blank:]][[:blank:]]*/\.\*/g')"
            card="$(arecord -l | grep "device 0:" | grep "$")"
            SOUND_CARD_ID=$(echo "$" | sed 's/:.*$//g' | awk '')
            sed -i "s/\.card [0-9]*/\.card $/g" ~/.asoundrc
            export SOUND_CARD_ID=$
    fi

Now whenever a user logs in to a seat, the user\'s local [.asoundrc] will be updated to the seat\'s sound card.

There is another more user friendly option, this script: [http://www.4shared.com/file/blo0ratQ/multi_seat_alsa_utils.html](http://www.4shared.com/file/blo0ratQ/multi_seat_alsa_utils.html) will allow user to assign a specific card to a seat. the script assumes that the num val of DISPLAY represents the seat\'s id. just put it in /usr/bin as root:users, 754, run it as root and assign a each seat a card.

Next put in any user\'s home the .asoundrc from before and relog into the session.

If one needs to use different devices under the same card (for example, seat 0 uses O\\B sound card and seat 1 uses the igp to stream movies to tv, the hdmi card is part if the O/B card), this script [http://www.4shared.com/file/SxouTU-\_/multi_seat_alsa_utils_4.html](http://www.4shared.com/file/SxouTU-_/multi_seat_alsa_utils_4.html) supports it.

The latest version of the script can be found at [http://pastebin.com/nUwsxYEx](http://pastebin.com/nUwsxYEx)

## [Bypassing polkit]

Implementing a good security policy governing local users is difficult. While it may be hoped that systemd will at some point provide a better solution, it is currently best to assume that all local users are trusted.

Major desktops now depend on polkit and will force its installation. Polkit can only track one local user, which is the one using the first seat. The other users are identified as \"inactive\", which causes polkit to deny them access to local resources. As a workaround, we can enable access to local devices to inactive users. Create a new policy file:

[FILE] **`/etc/polkit-1/rules.d/00-allow_mounting.rules`polkit workaround**

    polkit.addRule(function(action, subject)
    });

This will allow those users that are in the plugdev group to perform actions in the udisks category. Available actions can be listed using the \"pkaction\" tool, so it is easy to add rules for other categories.

## [Testing]

In order to test a multiseat setup on any computer regardless of the available hardware, emulation may be used:

`user `[`$`]`qemu-system-x86_64 -cdrom livegui-amd64.iso -smp 4 -boot d -m 4095 -vga virtio -display gtk,show-tabs=on -enable-kvm -device pci-bridge-seat,chassis_nr=2,id=head.2 -device virtio-gpu-pci,bus=head.2,addr=02.0,id=video.2 -device virtio-keyboard-pci,bus=head.2,display=video.2 -device virtio-tablet-pci,bus=head.2,display=video.2 -serial mon:stdio`