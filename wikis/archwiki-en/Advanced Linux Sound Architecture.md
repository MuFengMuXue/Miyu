# Advanced Linux Sound Architecture

The Advanced Linux Sound Architecture (ALSA) provides kernel driven sound card drivers. It replaces the original Open Sound System (OSS).

Besides the sound device drivers, ALSA also bundles a user space driven library for application developers. They can then use those ALSA drivers for high level API development. This enables direct (kernel) interaction with sound devices through ALSA libraries.

## Installation
The ALSA drivers are part of the Linux kernel. The ALSA library () is usually installed as a dependency. Therefore, manual installation is not necessary.

udev will automatically detect your hardware and select needed drivers at boot time, therefore, your sound should already be working.

However, your sound may be initially muted. If it is, see #Unmuting the channels.

## Firmware
The Sound Open Firmware (SOF) () is usually required for laptops—they tend to utilize Cadence Tensilica Xtensa architecture DSPs, see the list of the supported platforms. In case of the missing firmware the journal will provide messages such as:

 error: sof firmware file is missing
 error: failed to load DSP firmware -2
 error: sof_probe_work failed err: -2

For more SOF troubleshooting information, see Overview of Intel hardware platforms.

The  package is needed for laptops with Cirrus Logic smart amplifiers. See also:

* Audio drivers for Cirrus Logic CS35L54/56/57/63 Boosted Smart Amplifiers,
* .

The  package is needed for some Intel audio devices.

The  package contains firmware that may be required for certain sound cards.

See also #Cards and modules and Linux firmware.

## ALSA utilities
Install the  package. This contains (among other utilities) the  and  utilities. amixer is a shell command to change audio settings, while alsamixer provides a more intuitive ncurses based interface for audio device configuration.

## ALSA and systemd
The  package comes with systemd unit configuration files  and  by default.

These are automatically installed and activated during installation (via package provided symlink to sound.target). The options are as follows:

*  reads  on boot and writes updated values on shutdown, provided  does not exist. As  is not created without a conscious action of the user, it is the default method.
*  (Re-)Starts alsactl in daemon mode to continuously keep track of, and persist, volume changes, under the condition that the user has consciously created .

Evidently, both methods are mutually exclusive. You can decide for one of the two approaches depending on your requirements. To edit these units, see systemd#Editing provided units. You can check their status using systemctl.

For further information, see .

## User privileges
Local users have permission to play audio and change mixer levels. To allow remote users to use ALSA, you need to add those users to the  group.

## OSS emulation
OSS emulation is the ability to intercept OSS calls and reroute them through ALSA instead. This emulation layer is useful e.g. for legacy applications which try to open  and write sound data to them directly. Without OSS or the emulation library,  will be missing, and the application will not produce any sound.

If you want OSS applications to work with dmix, install the  package as well.

Load the  and  kernel modules. Configure them to load at boot.

## Unmuting the channels
By default, ALSA has all channels muted. Those have to be unmuted manually.

## Unmute with amixer
Unmuting the sound card's master volume can be done by using amixer:

 $ amixer sset Master unmute
 $ amixer sset Speaker unmute
 $ amixer sset Headphone unmute

## Unmute with alsamixer
Unmuting the sound card can be done using alsamixer:

 $ alsamixer

The  label below a channel indicates that the channel is muted, and  indicates that it is open.

Scroll to the  and  channels with the  and  keys and unmute them by pressing the  key.

Use the  key to increase the volume and obtain a value of  dB gain. The gain can be found in the upper left next to the  field.

## Unmute 5.1/7.1 sound
To get full 5.1 or 7.1 surround sound, you will likely need to unmute other channels such as , , ,  (subwoofer) and . (Those are channel names with Intel HD Audio; they may vary with different hardware)

## Enable the microphone
To enable your microphone, switch to the Capture tab with  and enable a channel with . See /Troubleshooting#Microphone if microphone does not work.

## Test your changes
Next, test to see if sound works:

 $ speaker-test -c 2

Change  to fit your speaker setup. Use  for 7.1, for instance:

 $ speaker-test -c 8

If audio is being outputted to the wrong device, try manually specifying it with the argument .

 $ speaker-test -D default:PCH -c 8

 accepts PCM channel names as values, which can be retrieved by running the following:

## Additional notes
* If your system has more than one soundcard, then you can switch between them by pressing

* Some cards need to have digital output muted or disabled in order to hear analog sound and vice versa.

* Some machines, like the Thinkpad T61, have a  channel which must be unmuted and adjusted as well.

* Some machines, like the Dell E6400, may also require the  and  channels to be unmuted and adjusted.

* If your volume adjustments seem to be lost after you reboot, try running alsamixer as root.

## Driver configuration
For more information, see Advanced Linux Sound Architecture - Driver Configuration guide.

To reload ALSA driver configuration you have to reload corresponding modules. Before doing this, all processes using the corresponding ALSA driver—such as PipeWire—must be stopped. To identify processes using sound device files, utilize :

 # fuser --all --verbose /dev/snd/*

See also:

* ALSA SoundCard Matrix
*
* Kernel modules#Manual module handling

## Cards and modules
Run  to identify the modules in use for PCI devices.

Run  for USB devices.

Run  to get a full list of loaded sound modules.

Run  to get the list of your sound cards with their corresponding indexes (card numbers).

Run  to get the card indexes with their corresponding module names.

## Card index
If you want to change your sound card order (or if your sound card order changes on boot, and you want to make it permanent), reserve the index for the given driver with the  option of the  module. See also Kernel module#Setting module options.

The following sample assumes you want your USB sound card always be the first (i.e. with index ), no matter when the module is loaded (e.g. the card could be unplugged on boot):

When a module name is prepended with an exclamation mark (), the corresponding index will be given for any modules but that name. For example, reserve the first index () for any modules but  to avoid USB sound cards from getting it:

 options snd slots=!snd_usb_audio

You can also provide an index of  to instruct ALSA to never use a card as the primary one: negative value is interpreted as a bitmask of permissible indexes. The alternative to the previous sample using the  option of the specific module:

 options snd_usb_audio index=-2

If several sound cards use the same module, and their order is always the same, you can change the order with just  option. The following sample assumes there are two audio cards using the HD Audio module (e.g. an integrated audio card and HDMI output of non-integrated video card), and you want to swap their indexes:

 options snd_hda_intel index=1,0

The  option can be combined with the  one as long as they do not conflict:

 options snd slots=,snd_hda_intel,snd_hda_intel,snd_usb_audio,snd_usb_audio,snd_usb_audio
 options snd_hda_intel index=2,1
 options snd_usb_audio index=3,4,5 vid=0xVID_3,0xVID_4,0xVID_5 pid=0xPID_3,0xPID_4,0xPID_5

See also:

* MultipleCards
* MultipleUSBAudioDevices

## Card disabling
To disable all cards controlled by a given kernel module, prevent the module from loading using install or module_blacklist approach.

To select which card should be disabled, use the  option of a kernel module. For example, disable the second card operated by a module:

See also /Troubleshooting#Codec probing for an HD Audio card codec disabling.

## Library configuration
The system configuration file is , and the per-user configuration file is .

The syntax of library configuration—i.e. whitespace, line continuation, comments, including configuration files, punctuators (separators), assignments, compound assignments, operation modes—is explained in Configuration files.

ALSA library configuration is loaded for each instance of the library, so to reload it, all you have to do is restart the programs that are using it.

For more information, see:

* Configuring ALSA
* .asoundrc article on the ALSA unofficial wiki
* .asoundrc article on the ALSA project wiki

## Basic syntax
## Operation modes
There are different operation modes for parsing nodes, the default mode is merge and create. If operation mode is either merge/create or merge, type checking is done. Only same type assignments can be merged, so strings cannot be merged with integers. Trying to define a simple assignment in default operation mode to a compound (and vice versa) will also not work.

Prefixes of operation modes:

*  — merge and create
*  — merge
*  — do not override
*  — override

Using override operation mode, when done correctly, is usually safe; however, one should bear in mind that there might be other necessary keys in a node for proper functioning.

## Nesting
Sometimes, it may be useful and even easier to read using nesting in configuration.

{{hc|Nesting PCM plugins|2=
pcm.azalia {	type hw; card 0	}
pcm.!default {	type plug; slave.pcm "azalia"	}

# is equivalent to

pcm.!default {	type plug; slave.pcm {	type hw; card 0;	}	}

# which is also equivalent to

pcm.!default.type plug;
pcm.default.slave.pcm.type hw;
pcm.default.slave.pcm.card 0;
}}

## Set the default sound card
## An example of setting default device using "defaults" node
Assuming that "defaults" node is set in , where "defaults.pcm.card" and its "ctl" counterpart have assignment values "0" (type integer), user wants to set default pcm and control device to (third) sound card "2" or "SB" for an Azalia sound card.

Using double quotes here automatically sets values data type to string, so in the above example, setting defaults.pcm.!card "2" would result in retaining last default device, in this case card 0. Using double quotes for strings is not mandatory as long as no special characters are used, which ideally should never be the case. This may be irrelevant in other assignments.

## Setting the default sound card via defaults node
Putting the previous example regarding  and  into practice, assuming we have 2 cards with index 0 and 1 respectively and wish to simply change the default card to index 1, would lead to the following configuration in  or the user-specific  to change both the playback and the mixer control card.

## Select the default PCM via environment variable
Probably, it is enough to set ALSA_CARD to the name of the device.  First, get the names with , then set ALSA_CARD to the name which comes after the colon and before the bracket; e.g. if you have

 card 1: HDMI ATI HDMI, device 3: HDMI 0 0

then set .

Other variables are also checked in the default global configuration . By looking there for constructs of the form , the following table emerges:

{| class="wikitable"
|-
! style="width: 7.5%;"| !! Variable name !! Used by
|-
|  || ALSA_CARD || pcm.default , pcm.hw , pcm.plughw , ctl.sysdefault , ctl.hw ,  rawmidi.default , rawmidi.hw , hwdep.hw
|-
|  || ALSA_CTL_CARD || ctl.sysdefault , ctl.hw
|-
|  || ALSA_HWDEP_CARD || hwdep.default , hwdep.hw
|-
|  || ALSA_HWDEP_DEVICE || hwdep.default , hwdep.hw
|-
|  || ALSA_PCM_CARD || pcm.default , pcm.hw , pcm.plughw
|-
|  || ALSA_PCM_DEVICE || pcm.hw  , pcm.plughw
|-
|  || ALSA_RAWMIDI_CARD || rawmidi.default , rawmidi.hw
|-
|  || ALSA_RAWMIDI_DEVICE || rawmidi.default , rawmidi.hw
|}

Alternatively, you can override the behavior in your own configuration file, preferably the global one ().  Add:

 pcm.!default {
    type plug
    slave.pcm {
        @func getenv
        vars [ ALSAPCM ]
        default "hw:Audigy2"
    }
 }

In this case as well, replace  with the name of your device. You can get the names with  or you can also use PCMs like surround51. But if you need to use the microphone, it is a good idea to select full-duplex PCM as default.

Now, you can select the sound card when starting programs by just changing the environment variable . It works fine for all programs that do not allow to select the card; for the others, ensure you keep the default card.
For example, assuming you wrote a downmix PCM called , you can use it with  using the commandline

## Addressing hardware directly
First, you will have to find out the card and device id that you want to set as the default:

For example, the last entry in this list has the card index (card number) , card ID strings   and the device ID . To set this card as the default, you can either use the system-wide file  or the user-specific file . You may have to create the file if it does not exist. Then insert the following options with the corresponding card.

 pcm.!default {
    type hw
    card Audio #or card 2
    hint {
     show on # for some applications
    }
 }

 ctl.!default {
    type hw
    card Audio
 }

 pcm.dmixer {
 	type dmix
 	ipc_key 2048
 	slave {
 		pcm "hw:Audio" #or "hw:2"
 	}
 }

 pcm.dsnooper {
 	type dsnoop
 	ipc_key 2048
 	slave {
 		pcm "hw:Audio"
 	}
 }

It is recommended to use sound card ID strings instead of number references to overcome the boot order problem.

 and  are spares for applications which does not support without mixing.

For example,  enables mixing for Chromium tempolary.

The  options affect which card and device will be used for audio playback while the  option affects which card is used by control utilities like alsamixer.

The changes should take effect as soon as you (re-)start an application (e.g. MPlayer). You can also test with a command like aplay:

 $ aplay -D default:PCH your_favourite_sound.wav

If you receive an error regarding your asound configuration, check the upstream documentation for possible changes to the configuration file format.

## Plugins
Install the  package if you need to enable #Upmixing, #Downmixing, #High quality resampling and other advanced features.

For more information, see PCM (digital audio) plugins.

## Software mixing
Mixing enables multiple applications to output sound at the same time. Most discrete sound cards support hardware mixing, which is enabled by default if available. Integrated motherboard sound cards (such as Intel HD Audio), usually do not support hardware mixing. On such cards, software mixing is done by an ALSA plugin called . This feature is enabled automatically if hardware mixing is unavailable.

To manually enable , add the following to your ALSA configuration file:

{{hc|/etc/asound.conf|2=
pcm.dsp {
    type plug
    slave.pcm "dmix"
}
}}

## Upmixing
In order for stereo sources like music to be able to saturate a 5.1 or 7.1 sound system, you need to use upmixing. In darker days, this used to be tricky and error prone, but nowadays, plugins exist to easily take care of this task. We will use the upmix plugin, included in the  package.

Then add the following to your ALSA configuration file of choice (either  or ):

 pcm.upmix71 {
    type upmix
    slave.pcm "surround71"
    delay 15
    channels 8
 }

You can easily change this example for 7.1 upmixing to 5.1 or 4.0.

The following example adds a new PCM channel that you can use for upmixing. If you want all sound sources to go through this channel, add it as a default below the previous definition like so:

 pcm.!default "plug:upmix71"

The plugin automatically allows multiple sources to play through it without problems so setting is as a default is actually a safe choice.
If this is not working, you have to setup your own dmixer for the upmixing PCM like this:

 pcm.dmix6 {
    type asym
    playback.pcm {
        type dmix
        ipc_key 567829
        slave {
            pcm "hw:0,0"
            channels 6
        }
    }
 }

and use "dmix6" instead of "surround71".
If you experience skipping or distorted sound, consider increasing the buffer_size (to 32768, for example) or use a high quality resampler.

## Downmixing
If you want to downmix sources to stereo because you, for instance, want to watch a movie with 5.1 sound on a stereo system, use the  plugin, included in the  package.

Again, in your configuration file, add this:

 pcm.!surround51 {
    type vdownmix
    slave.pcm "default"
 }
 pcm.!surround40 {
    type vdownmix
    slave.pcm "default"
 }

## Multiband EQ
Multiband EQ (mbeq)

: is a fairly typical multiband graphical equalizer. It is implemented using a fast Fourier transform (FFT), so it takes quite a lot of CPU power, but should have less phase effects than an equivalent filter implementation. If the input signal is at too low sample rate, then the top bands will be ignored—the highest useful band will always be a high shelf.

mbeq is part of Steve Harris' LADSPA plugin suite.

Install the ,  and  packages if you do not already have them.

If you have not already created either an  or a  file, then create either one and insert the following:

{{hc|/etc/asound.conf|2=
pcm.eq {
    type ladspa

    # The output from the EQ can either go direct to a hardware device
    # (if you have a hardware mixer, e.g. SBLive/Audigy) or it can go
    # to the software mixer shown here.
    #slave.pcm "plughw:0,0"
    slave.pcm "plug:dmix"

    # Sometimes, you may need to specify the path to the plugins,
    # especially if you have just installed them.  Once you have logged
    # out/restarted, this should not be necessary, but if you get errors
    # about being unable to find plugins, try uncommenting this.
    #path "/usr/lib/ladspa"

    plugins [
    {
        label mbeq
        id 1197
        input {
            # The following setting is just an example, edit to your own taste:
            # bands:
            #   50 Hz,  100 Hz,  156 Hz,  220 Hz,  311 Hz,   440 Hz,   622 Hz,  880 Hz,
            # 1250 Hz, 1750 Hz, 2500 Hz, 3500 Hz, 5000 Hz, 10000 Hz, 20000 Hz
            controls [ -5 -5 -5 -5 -5 -10 -20 -15 -10 -10 -10 -10 -10 -3 -2 ]
            }
        }
    ]
}

# Redirect the default device to go via the EQ - you may want to do
# this last, once you are sure everything is working.  Otherwise, all
# your audio programs will break/crash if something has gone wrong.
pcm.!default {
    type plug
    slave.pcm "eq"
}

# Redirect the OSS emulation through the EQ too (when programs are running through "aoss")
pcm.dsp0 {
    type plug
    slave.pcm "eq"
}
}}

## ALSAEqual
## System-wide
Install the  package.

After installing the package, add the following to your ALSA configuration file:

{{hc|/etc/asound.conf|2=
ctl.equal {
    type equal;
}

pcm.plugequal {
    type equal;
    # Normally, the equalizer feeds into dmix so that audio
    # from multiple applications can be played simultaneously:
    slave.pcm "plug:dmix";
    # If you want to feed directly into a device, specify it instead of dmix:
    #slave.pcm "plughw:0,0";
}

# Configuring pcm.!default will make the equalizer your default sink
pcm.!default {
# If you do not want the equalizer to be your default,
# give it a different name, like pcm.equal commented below
# Then you can choose it as the output device by addressing
# it in individual apps, for example mpg123 -a equal 06.Back_In_Black.mp3
# pcm.equal {
    type plug;
    slave.pcm plugequal;
}
}}

To change your equalizer settings, run
 $ alsamixer -D equal

Note that the equalizer configuration is different for each user (until not specified else). It is saved in .
So if you want to use ALSAEqual with mpd or another software running under different user, you can configure it using
 $ su mpd -c 'alsamixer -D equal'
or for example, you can make a symlink to your  in their home directory.

## Specific outputs only
If you wish to apply an equalizer to a specific output device only (for example your speakers connected to the S/PDIF output, but not your headphones connected to the headphone jack), but also want be able to output from multiple applications and to both output devices simultaneously, you need to create two  devices that feed into their respective devices () directly. The following works for stereo output and maintains a regular stereo input, applying the equalizer to the S/PDIF output only.

{{hc|/etc/asound.conf|2=
#
#  (capture.pcm)   dmixa
#
#  (playback.pcm) --> stereo2quad ==> quad
#
#                                        --> softvol --> plugequal --> dmixd
#

# dmix for analog output
pcm.dmixa {
  type dmix
  ipc_key 1024
  ipc_perm 0666
  slave.pcm "hw:PCH,0"
  slave {
    period_time 0
    period_size 1024
    buffer_size 4096
    channels 2
  }
  bindings {
    0 0
    1 1
  }
}

# dmix for digital output
pcm.dmixd {
  type dmix
  ipc_key 2048
  ipc_perm 0666
  slave.pcm "hw:PCH,1"
  slave {
    period_time 0
    period_size 1024
    buffer_size 4096
    channels 2
  }
  bindings {
    0 0
    1 1
  }
}

# equalizer with controls
pcm.plugequal {
  type equal
  slave {
    pcm "plug:dmixd"
  }
}
ctl.equal {
 type equal
}

# Volume control for S/PDIF
pcm.softvol {
    type softvol
    slave.pcm "plug:plugequal"
    control {
        name "S/PDIF"
    }
}

# multi:
# "a" (analog)  -> dmix,
# "d" (digital) -> softvol -> plugequal -> dmix
pcm.quad {
    type multi
    slaves {
      a.pcm "dmixa"
      a.channels 2
      d.pcm "plug:softvol" # detour via softvol and equalizer
      d.channels 2
    }
    bindings {
      0 { slave a; channel 0; }
      1 { slave a; channel 1; }
      2 { slave d; channel 0; }
      3 { slave d; channel 1; }
    }
}

# stereo to quad
pcm.stereo2quad {
  type route
  slave.pcm "quad"
  ttable [
    [ 1 0 1 0 ]
    [ 0 1 0 1 ]
  ]
}

# playback to stereo to quad, capture as usual
pcm.!default {
  type asym
  playback.pcm "plug:stereo2quad"
  capture.pcm "plug:dnsoop"
}
}}

## Managing states
Install the  package.

Configure the equalizer as usual with
 $ alsamixer -D equal

When you are satisfied with the state, you may give it a name (foo in this example) and save it:
 $ alsaequal-mgr save foo

The state "foo" can then be restored at a later time with
 $ alsaequal-mgr load foo

This, however, only restores . You then have to update the equalizer by .

You can thus create different equalizer states for games, movies, music genres, VoIP apps, etc. and reload them as necessary.

See the project page and the help message for more options.

## Tips and tricks
## High quality resampling
When #Software mixing is enabled, ALSA is forced to resample everything to the same frequency (48 kHz by default when supported). By default, it will try to use the speexrate converter to do so, and fallback to low-quality linear interpolation if it is not available. Thus, if you are getting poor sound quality due to bad resampling, the problem can be solved by simply installing the  package.

For even higher quality resampling, you can change the default rate converter to  or . Both perform well enough that in practice it does not matter which one you choose, so using the best converter is usually not worth the extra CPU cycles it requires.

To change the default converter, place the following contents in your  or :

 defaults.pcm.rate_converter "speexrate_medium"

## Disabling auto mute on startup
Auto-Mute Mode can be configured on startup with amixer. For example, to disable it:

 # amixer -c 0 sset "Auto-Mute Mode" Disabled

Alternatively, the ncurses based interface can be utilized through alsamixer. In order to save any modifications, use:

 # alsactl store

or

 # alsactl daemon

See also #ALSA and systemd.

## Hot-plugging a USB sound card
See Writing Udev rules for ALSA.

## Simultaneous output
You might want to play music via external speakers connected via mini jack and internal speakers simultaneously. This can be done by unmuting Auto-Mute item using  or :
 $ amixer sset "Auto-Mute" unmute

and then unmuting other required items, such as Headphones, Speaker, Bass Speaker...

## Keyboard volume control
Map the following commands to your volume keys: , , .

To raise the volume:
 amixer set Master 5%+

To lower the volume:
 amixer set Master 5%-

To toggle mute/unmute of the volume:
 amixer set Master toggle

## Virtual sound device using snd_aloop
You might want a jack alternative to create a virtual recording or play device in order to mix different sources, using the  module:

 modprobe snd_aloop

List your new virtual devices using:
 aplay -l

now you can for example using ffmpeg:
 ffmpeg -f alsa -i hw:1,1,0 -f alsa -i hw:1,1,1 -filter_complex amerge output.mp3

In the hw:R,W,N phrase, R is your virtual card device number. W should be set to 1 for recording devices, or 0 for playing. N is your sub device. You can use all the virtual devices available and play/stop using  applications like mplayer:
 mplayer -ao alsa:device=hw=1,0,0 fileA
 mplayer -ao alsa:device=hw=1,0,1 fileB

Another thing you could do with this approach is using festival to generate a voice into a recording stream using a script like this:

 #!/bin/sh
 echo "$1" | iconv -f utf-8 -t iso-8859-1 | text2wave  > "_tmp_.wav"
 mplayer -ao alsa:device=hw=2,0,0 "_tmp.wav"
 rm "_tmp.wav"

## Reconfiguring input/output ports
The  package contains the hdajackretask tool, which can be used (on Intel HDA cards) to reconfigure the sound card input/output ports; for instance, to turn a microphone jack into a headphone jack.

## apulse
 provides an alternative partial implementation of the PulseAudio API. It lets you use ALSA for applications that support only PulseAudio for sound. Usage is simply:

 $ apulse application
