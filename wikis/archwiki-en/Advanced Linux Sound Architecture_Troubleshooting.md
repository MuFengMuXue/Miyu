# Advanced Linux Sound Architecture/Troubleshooting

The  package contains the alsa-info.sh script, which can be used to gather detailed data on the ALSA state.

See also SoundcardTesting.

## Volume
## Output is muted after reboot
Run the following command:

 # alsactl restore

If the problem persists, verify that the  option in  is set to .

## Volume is too low
Run  and try to increase the value of the sliders, unmuting channels if necessary. Note that if you have many sliders, you may have to scroll to the right to see any missing sliders.

If all the sliders are maxed out, and the volume is still too low, you can try running the following script to reset your codec settings:

 $ wget -O hda-analyzer.py https://git.alsa-project.org/?p=alsa.git;a=blob_plain;f=hda-analyzer/run.py

Close the analyzer, and when prompted as to whether you want to reset the codecs, say "yes".

If the volume is still too low, run  again: resetting the codecs may have caused new sliders to become enabled and some of them may be set to a low value.

## Volume is still too low
If you are facing low volume even after maxing out your speakers/headphones, you can give the softvol plugin a try. Add the following to :

{{hc|/etc/asound.conf|2=
pcm.!default {
    type plug
    slave.pcm "softvol"
}

pcm.softvol {
    type softvol
    slave {
        pcm "dmix"
    }
    control {
        name "Pre-Amp"
        card 0
    }
    min_dB -5.0
    max_dB 20.0
    resolution 6
}
}}

After the changes are loaded successfully, you will see a  section in alsamixer. You can adjust the levels there.

## Random lack of sound on startup
You can quickly test sound by running . If there is no sound, you may see something similar to:

 ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave
 Playback open error: -16
 Device or resource busy

If you have no sound on startup, this may be because your system has multiple sound cards, and their order may sometimes change on startup.  If this is the case, try setting the default sound card.

If you use MPD and the above configuration tips do not work, try following https://mpd.wikia.com/wiki/Configuration#ALSA_MPD_software_volume_control.

## Microphone
## No microphone input
In , make sure that all the volume levels are up under recording, and that CAPTURE is toggled active on the microphone (e.g. Mic, Internal Mic) and/or on Capture (in alsamixer, select these items and press ). Try making positive Mic Boost and raising Capture and Digital levels higher; this may make static or distortion, but then you can adjust them back down once you are hearing something when you record.

As the PulseAudio wrapper is shown as "default" in alsamixer, you may have to press  to select your actual sound card first. You may also need to enable and increase the volume of Line-in in the Playback section.

To test the microphone, run these commands (see  for further information):

 $ arecord --duration=5 --format=dat test-mic.wav
 $ aplay test-mic.wav

Alternatively, you can run this command:

 $ arecord -vv --format=dat /dev/null

alongside alsamixer to easily identify channel which you should select and unmute.

To test a particular device, use the  parameter followed by the hardware PCM name in the form  for card C device D, or  for plugged hardware. For instance:

 $ arecord -vvv --format=dat --device=plughw:0,0 /dev/null

If all fails, you may want to eliminate hardware failure by testing the microphone with a different device.

For at least some computers, muting a microphone (MM) simply means its input does not go immediately to the speakers. It still receives input.

Some programs use try to use OSS as the main input software. If you have enabled the ,  or  kernel modules previously (they are not loaded by default), try unloading them.

See also:

* #Wrong model autodetection
* Record from mic

## Setting the default microphone/capture device
Some applications (Pidgin, Adobe Flash) do not provide an option to change the capture device. It becomes a problem if your microphone is on a separate device (e.g. USB webcam or microphone) than your internal sound card. To change only the default capture device, leaving the default playback device as is, you can modify your  file to include the following:

{{hc|~/.asoundrc|
pcm.usb
{
    type hw
    card U0x46d0x81d
}

pcm.!default
{
    type asym
    playback.pcm
    {
        type plug
        slave.pcm "dmix"
    }
    capture.pcm
    {
        type plug
        slave.pcm "usb"
    }
}
}}

Replace U0x46d0x81d with your capture device's card name in ALSA. You can use  to list all the capture devices detected by ALSA.

## Internal microphone not working
First make sure the volume is enabled under the  view in alsamixer. In some cases, the "Internal Microphone" is not displayed in the capture list available when pressing F4. If so, specifying the card number given by  to start alsamixer (for example  ) can make it appear.

## Audio quality
## Crackling sound through mini-jack (headphones connector)
Following Advanced Linux Sound Architecture#Simultaneous output might lead to crackling sound through headphones or external speakers. This can be fixed by muting or setting the volume to  on Mic. Use  or :

 $ amixer sset "Mic" 0%
 $ amixer sset "Mic" mute

## Popping sound after resuming from suspension
You might hear a popping sound after resuming the computer from suspension. This can be fixed by editing  and removing the line that says

## Sound skipping during playback
Run , and if channels exist for nonexistent output devices then disable them (e.g. alsamixer showing a center speaker but you not having one).

## Poor sound quality or clipping
If you experience poor sound quality, try setting the PCM volume (in alsamixer) to a level such that gain is 0.

If  driver has been loaded, you could try to enable :

{{hc|/etc/asound.conf|2=
pcm.!default {
    type plug
    slave.pcm "softvol"
}
pcm.dmixer {
    type dmix
    ipc_key 1024
    slave {
        pcm "hw:0"
        period_size 4096
        buffer_size 131072
        rate 50000
    }
    bindings {
        0 0
        1 1
    }
}
pcm.dsnooper {
    type dsnoop
    ipc_key 1024
    slave {
        pcm "hw:0"
        channels 2
        period_size 4096
        buffer_size 131072
        rate 50000
    }
    bindings {
        0 0
        1 1
        }
}
pcm.softvol {
  type softvol
  slave { pcm "dmixer" }
  control {
    name "Master"
    card 0
  }
}
ctl.!default {
  type hw
  card 0
}
ctl.softvol {
  type hw
  card 0
}
ctl.dmixer {
  type hw
  card 0
}
}}

## Pops when starting and stopping playback
Some modules (e.g. ) can power off your sound card when it is not used. This might cause audible click noises—like a crack/pop/scratch—at each power-down/up depending on the device (sometimes even when moving the volume slider or opening and closing windows on some desktop environments).

For more information, see Power management#Audio and #Power saving.

## Hardware and cards
## HD Audio
For more information, see Module snd-hda-intel and the output of .

See also:

* Advanced Linux Sound Architecture#Driver configuration
* Intel High Definition Audio (HD Audio)

## Power saving
Power saving is enabled by default and might cause the following issues:

* #Pops when starting and stopping playback
* PC speaker#The HD Audio power-saving mode mutes the PC speaker
* VirtualBox/Install Arch Linux as a guest#Linux guests have slow/laggy audio

To completely disable the power-saving mode for the  module, use the following kernel module parameters:

## Codec probing
A codec is a hardware component of an HD Audio sound card. One card might incorporate more than one codec, one codec might correspond to more than one ALSA device.

A codec slot is a number (it begins from zero) identifying the codec on a given sound card. You can get the codec slot number from  file and  directory names—here  is a card index, and  is a codec slot.

To disable a codec—and subsequently all of the related ALSA devices—use the  option of the  module.

## Wrong model autodetection
Wrong model autodetection might cause the following issues:

* #No microphone input
* Microphone is not detected if it is plugged in a combined headset/microphone 4-pole 3.5 mm TRRS jack
:
* No headphone output

See HD-Audio Codec-Specific Models for possible  strings for a given sound card chip.

The sound card chip can be found in:

* —see Chip: in the upper-left corner,
* output of ,
* output of ,
*  file.

To force, use the  option of the  module.

## Message Signaled Interrupts
Whether Message Signaled Interrupts (MSI) should be enabled or not hardly depends on the hardware. In the case of wrong autodetection different kinds of bad things could happen:

* erroneous disablement might lead to the sound card is not detected;
* erroneous enablement might lead to poor audio quality (stuttering), or even kernel lockup.

To check the MSI capability status, run  and  with root user privileges.

## DMA pointer
Click noises (crackling, popping) on input and/or output of an HD Audio card might be caused by DMA position problem. Try to change the  option of the  module.

## Fix wrong audio pin mapping
If the mappings to your audio pins(plugs) do not correspond but ALSA works fine, you could try HDA Analyzer -- a pyGTK2 GUI for HD-audio control can be found at the ALSA wiki.
Try tweaking the Widget Control section of the PIN nodes, to make microphones IN and headphone jacks OUT. Referring to the Config Defaults heading is a good idea.

## Verifying output parameters
Check the contents of , where , , and  are system dependent. In order to find this file, execute the following command chain while outputting something via ALSA:

 $ find /proc/asound/ -name hw_params \
 | xargs -I FILE grep -v -l "closed" FILE \
 | grep '/proc/asound/card./pcm.p/sub./hw_params'

Here is an example output for audio with a bit depth of 24 bits and a sampling frequency of 44.1 kilohertz:

For more information see the Proc asound documentation.

## S/PDIF output does not work
S/PDIF (IEC958) utilizes two modes:

* Audio mode is digital PCM signal, so the receiver just converts the data with digital-to-analog converter (DAC).

* Non-audio mode is an encoded bitstream, so the receiver must decode the data first, and put it to DAC then. Dolby Digital and DTS Digital Surround are examples of encoded bitstream formats.

ALSA should detect appropriate mode automatically, but if it fails, you can force the mode with  (—audio, —non-audio):

 # iecset audio on
 # iecset audio off

For more information, see DigitalOut.

## HDMI
## HDMI output does not work
The procedure described below can be used to test HDMI audio. Before proceeding, make sure you have enabled and unmuted the output with .

Connect your PC to the Display via HDMI cable and enable the display with xrandr.

Use  to discover the card and device number. For example:

Send sound to the device. Following the example in the previous step, you would send sound to , :

 $ aplay -D plughw:1,3 /usr/share/sounds/alsa/Front_Center.wav

If aplay does not output any errors, but still no sound is heard, "reboot" the receiver, monitor or tv set. Since the HDMI interface executes a handshake on connection, it might have noticed before that there was no audio stream embedded, and disabled audio decoding. If you are using a standalone window manager, you may need to have sound playing while plugging in the HDMI cable.

mplay and other application could be configured to use special HDMI device as audio output. But flashplugin could only use default device. The following method is used to override default device. But you need to change it back when your TV is disconnected from HDMI port.

If the test is successful, create or edit your  file to set HDMI as the default audio device.

{{hc|~/.asoundrc|
pcm.!default {
    type hw
    card 1
    device 3
}
}}

Or if the above configuration does not work try:

Or if you alternatively succeed with

 $ speaker-test -Dplug:hdmi

for your HDMI or DisplayPort port the following configuration will work (successfully tested on Lenovo ThinkPad T430s):

{{hc|~/.asoundrc|
pcm.!default {
    type plug
    slave.pcm "hdmi"
}
}}

## HDMI 5.1 sound goes to wrong speakers
Sound can be redirected to the intended speakers using ALSA's  function.

{{hc|/etc/asound.conf|2=
pcm.!hdmi-remap {
    type asym
    playback.pcm {
        type plug
        slave.pcm "remap-surround51"
    }
}

pcm.!remap-surround51 {
    type route
    slave.pcm "hw:0,3"
    ttable {
        0.0= 1
        1.1= 1
        2.4= 1
        3.5= 1
        4.2= 1
        5.3= 1
    }
}
}}

## Applications
## SDL: No sound with SDL applications
If you get no sound using SDL based applications, try setting the environment variable  to .

## OpenAL: No sound in applications that use OpenAL
OpenAL defaults to PulseAudio. To instruct it to try ALSA first:

## Others: Generic application problems
For other applications who insist on their own audio setup, e.g., XMMS or MPlayer, you would need to set their specific options.

For MPlayer or mpv, add the following line to the respective configuration file:
 ao=alsa

Eg. for XMMS2, go into their options and make sure the sound driver is set to ALSA, not oss.

To do this in XMMS:
* Open XMMS
** Options > Preferences.
** Choose the ALSA output plugin.

For applications which do not provide a ALSA output, you can use aoss from the alsa-oss package. To use aoss, when you run the program, prefix it with , e.g.:
 aoss realplay

pcm.!default{ ... }  doesnt work for me anymore. but this does:
 pcm.default pcm.dmixer

## Other issues
## Simultaneous playback problems
If you are having problems with simultaneous playback, and if PulseAudio is installed, its default configuration is set to "hijack" the soundcard. Some users of ALSA may not want to use PulseAudio and are quite content with their current ALSA settings. One fix is to edit  and comment out the following lines:
{{bc|1=
# Use PulseAudio by default
pcm.!default {
    type pulse
    fallback "sysdefault"
    hint {
        show on
        description "Default ALSA Output (currently PulseAudio Sound Server)"
    }
}
}}

Commenting the following out also may help:
{{bc|1=
ctl.!default {
    type pulse
    fallback "sysdefault"
}
}}

This may be a much simpler solution than completely uninstalling PulseAudio.

Effectively, here is an example of a working :
{{bc|1=
pcm.dmixer {
    type dmix
    ipc_key 1024
    ipc_key_add_uid 0
    ipc_perm 0660
}
pcm.dsp {
    type plug
    slave.pcm "dmix"
}
}}

## Removing old ALSA state file (asound.state)
The  package provides  which automatically stores the current ALSA state to  upon system shutdown.  This can be problematic for users who are trying to reset their current ALSA state as the  file will be recreated with the current state upon every shutdown (e.g., attempting to remove user-defined channels from the mixer).  The  service may be temporarily disabled by creating the following empty file:

 # mkdir -p /etc/alsa
 # touch /etc/alsa/state-daemon.conf

The presence of  prevents  from saving  during shutdown. After disabling this service, the  file may be removed as such:

 # rm /var/lib/alsa/asound.state

After rebooting, the previous ALSA state should be lost and the current state should be reset to defaults.  Re-enable  by deleting the condition file we created:

 # rm /etc/alsa/state-daemon.conf

On the next shutdown, the  file should be recreated with ALSA defaults.  The file may also be generated immediately using:

 # alsactl store

If you want to clean ALSA state without rebooting, you can use  to remove the sound driver module, then manually delete the unwanted entries in , and then use  to reinstall the sound driver module.

## Problems with availability to only one user at a time
You might find that only one user can use the dmixer at a time.  This is probably ok for most, but for those who run mpd as a separate user this poses a problem.  When mpd is playing a normal user cannot play sounds though the dmixer.  While it is quite possible to just run mpd under a user's login account, another solution has been found.  Adding the line  to the  block disables this locking.  The following is a snippet from , the rest is the same as above.

{{bc|1=
...
pcm.dmixer {
    type dmix
    ipc_key 1024
    ipc_key_add_uid 0
    ipc_perm 0660
slave {
 ...
}}

## Crackling/popping on Dell laptops
Check if you have  installed and if anything (e.g. ) is reading or writing to the interface exposed by the module, as i8kutils BIOS system calls block the kernel for a moment on some systems. See warning in Fan speed control#Dell laptops for more details.
