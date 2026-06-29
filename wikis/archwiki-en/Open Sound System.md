# Open Sound System

The Open Sound System (OSS) was the original sound system for Linux.

It was superseded by the Advanced Linux Sound Architecture (ALSA), which has a number of advantages over OSS:

* Better support for USB audio devices.
** OSS has experimental output support for USB audio devices, but no input.
* Support for Bluetooth audio devices.
* Support for AC'97 and HD Audio dial-up softmodems.
* Better support for MIDI devices.
** OSS supports MIDI devices with the help of a software synthesizer such as Timidity or FluidSynth.
* Support for suspend.
* Better support for jack detection.

## Installation
Install the  package, or the package with non-free drivers .

This will install the OSS, run the OSS install script (temporarily disabling the ALSA modules) and install the OSS kernel modules. Since ALSA is enabled by default, you need to disable it so it does not conflict with OSS. You can do this by blacklisting the  module.

After blacklisting the module, you can enable  to start at boot.

To start using OSS without needing to reboot, check if any ALSA modules are still loaded (ALSA modules start with "snd"):

 # lsmod | grep snd

Remove the ALSA modules as follows:

 # lsmod | awk ' { print $1 } ' | grep snd | xargs rmmod

Then restart OSS:

 # soundoff && soundon

To completely remove ALSA from your system, you can compile a custom kernel and disable ALSA in its configuration. See Gentoo:ALSA#Kernel for the details.

In case you are not part of the audio group, add yourself and relogin for the changes to take effect:
 # gpasswd -a $USER audio

In case OSS is not able to detect your card when starting it, run:

 # ossdetect -v
 # soundoff && soundon

## Testing
Test OSS by running:

 $ osstest

You should be able to hear music during the test process. If there is no audio, try to adjust the volume or refer to the #Troubleshooting section.

If you want to hear sounds from more than one application simultaneously, you need , OSS's software mixer.

Check that vmix is enabled by running:

 $ ossmix -a | grep -i vmix

You should see a line like . If you do not see any lines beginning with , it probably means that  has not been attached to your sound device. To attach , issue the command:

 $ vmixctl attach device

where device is your sound device, e.g. .

To avoid having to issue this command manually in the future, you can add it to , as suggested by the official documentation.

If you get a  error, you need to add  to  and then reboot.

See which devices are detected by running:

 $ ossinfo

You should be able to see your devices listed under Device Objects or Audio Devices. If the device that you want to use is not at the top of one of these sections, you have to edit  and place the driver for your device at the very top. It may be required to restart OSS:

 # soundoff && soundon

If this does not work, comment all drivers listed except the ones for your device.

## Volume control mixer
To control the volume of various devices, mixers levels will need to be set. There are two mixers:

; ossmix: a command-line mixer, similar to the BSD audio mixer .
; ossxmix: a GTK-based graphical mixer.

## Color definitions
For high definition (HD) audio,  will color jack configurations by their pre-defined jack colors:

{| class="wikitable"
! Color
! Type
! Connector
|-
|style="color:black;background:lightgreen"| green
| front channels (stereo output)
| 3.5mm TRS
|-
|style="color:white;background:black"| black
| rear channels (stereo output)
| 3.5mm TRS
|-
|style="color:white;background:gray"| grey
| side channels (stereo output)
|3.5mm TRS
|-
|style="color:black;background:gold"| gold
| center and subwoofer (dual output)
|3.5mm TRS
|-
|style="color:black;background:lightblue"| blue
| line level (stereo input)
|3.5mm TRS
|-
|style="color:black;background:pink"| pink
| microphone (mono input)
|3.5mm TS
|}

## Saving mixer levels
Mixer levels are saved when you shut off your computer.  If you want to save the mixer level immediately, execute as root:
 # savemixer

 can be used to write mixer levels to a file with the  switch and restore by the  switch.

## Other mixers
Other mixers that have support for OSS:
*
*

## Configuring applications for OSS
## GStreamer-based
If you have problems with applications that use GStreamer for audio, you can try removing  and installing the  package which is needed by  and .

## OpenAL-based
By default OpenAL uses ALSA. To change this, simply define the usage of OSS in :

## Audacity
If Audacity starts, but it complains that it cannot open the device or simply does not play anything, then you may be using  which prevents Audacity from having exclusive access to your sound device. To fix this, before running Audacity, run:

 $ ossmix vmix0-enable OFF

You can restore  after closing Audacity with:

 $ ossmix vmix0-enable ON

## Gajim
By default, Gajim uses  to play a sound. For OSS you can change it to the equivalent  by going to Edit > Preferences > Advanced, opening the Advanced Configuration Editor and modifying the  variable accordingly.

## MOC
To use MOC with OSS v4.1 you must change  to  in your configuration file (located in ). For issues with the interface try changing the  by pressing  in  (to change to the sofware mixer).

## MPD
MPD is configured through  or . Check both of these files, looking for something that looks like:

{{hc|/etc/mpd.conf|
...
audio_output {
    type    "alsa"
    name    "Some Device Name"
}
...
}}

If you find an uncommented (the lines do not begin with #'s) ALSA configuration like the one above, comment all of it out, or delete it, and add the following:

{{hc|/etc/mpd.conf|
...
audio_output {
    type    "oss"
    name    "My OSS Device"
}
...
}}

Further configuration might not be necessary for all users. However, if you experience issues (in that MPD does not work properly after it has been restarted), or if you like having specific (i.e. more user-configured, less auto-configured) configuration files, the audio output for OSS can be more specifically configured by finding the card identifier:

 $ ossinfo | grep /dev/dsp

Look for the line that says something similar to . Take note of what your  is, and add these lines to your OSS  in your MPD configuration file:

{{hc|/etc/mpd.conf|
...
audio_output {
    type            "oss"
    name            "My OSS Device"
    device          "/dev/oss//pcm0"
    mixer_device    "/dev/oss//mix0"
}
...
}}

See also: Music Player Daemon#System-wide configuration.

## MPlayer
If you are using a GUI (SMplayer, GNOME MPlayer, etc.) you can select OSS as the default output in the settings dialogs. If you use MPlayer from the command-line, you should specify the sound output:
 $ mplayer -ao oss /some/file/to/play.mkv

If you do not want to bother typing it over and over again add  to your configuration file (at ).

See also: MPlayer#Configuration.

## VLC media player
You can select OSS as the default output in the audio settings.

## Wine
To set OSS support in Wine start:
 $ winecfg
and go to the  tab and select the .

See also: Wine#Sound.

## Other applications
* If you can not get sound from an application not listed here, try looking at the Configuring Applications for OSSv4 page.
* Search for OSS specific packages with pacman or by looking in the AUR.

See also: ossapps.

## Tips and tricks
## More convenient and precise volume control
The volume lever of ossxmix is very small, making it difficult to finely control the volume.

Run  to find the control you want to control (refer to ), this example is .

Bind the following commands to the keyboard shortcuts of the desktop environment.

Increase the volume by 1 (the volume can be between 0 and 100):

 $ ossmix codec1.jack.green.front +1

Decrease the volume by 1 (The  is needed on some systems so that the  will not be mistaken for a parameter.):

 $ ossmix -- codec1.jack.green.front -1

Then you can easily control the volume.

## Keyboard volume control
An easy way to mute/unmute and increase/decrease the volume is to use the ossvol script.

Download the script and place it at .

Once you installed it, type:
 $ ossvol -t
to toggle mute, or:
 $ ossvol -h
to see the available commands.

If you want to use multimedia keys with , map the following commands to your volume keys: ,  and :

To mute/unmute the volume:

 $ ossvol -t

To lower the volume:

 $ ossvol -d 2

To raise the volume:

 $ ossvol -i 2

## Changing the sample rate
Changing the output sample rate is not obvious at first. Sample rates can only be changed by root and  must be unused by any programs when a change is requested. Before you follow any of these steps, ensure you are going through a receiver/amplifier and using quality speakers and not simply computer speakers. If you are only using computer speakers, do not bother changing anything here as you will not notice a difference.

By default the sample rate is 48000hz. There are several conditions in which you may want to change this. This all depends on your usage patterns. You want the sample rate you are using to match the media you use the most. If your computer has to change the sampling rate of the media to suit the hardware it is likely, though not guaranteed, that you will have a loss in audio quality. This is most noticeable in down sampling (ie. 96000hz &rarr; 48000hz). There is an article about this issue in Stereophile which was discussed on Apple's CoreAudio API mailing list if you wish to learn more about this issue.

Some example sample rates:

; 44100hz: Sample rate of standard Red Book audio CDs.
; 88000hz: Sample rate of SACD high definition audio discs/downloads. It is rare that your motherboard will support this sample rate.
; 96000hz: Sample rate of most high definition audio downloads. If your motherboard is an AC'97 motherboard, this is likely to be your highest bitrate.
; 192000hz: Sample rate of BluRay, and some (very few) high definition downloads. Support for external audio receiver equipment is limited to high end audio. Not all motherboards support this. An example of a motherboard chipset that would support this includes HD Audio.

To check what your sample rate is currently set to, run:

 $ ossmix | grep rate

You are likely to see .

If you do not see a  (or , etc.) being outputted, then it probably means that  is disabled. In that case, OSS will use the rate requested by the program which uses the device, so this section does not apply. Exception to this are Envy24 (and Envy24HT) cards that have a special setting  which has a similar function (see the  manpage).

To change your sample rate:
# First, make sure your card is able to use the new rate. Run  and see if the wanted rate is in the Native sample rates output.
# As root, run . Be aware, this will close any program that currently has an open sound channel.
# After all programs occupying  are terminated, run as root:  replacing the rate with your desired sample rate (and  if applicable).
# Run  and check for  to see if you were successful.
#To make the changes permanent add the following to the  file:

and make it executable.

## Disable virtual mixing and COOKEDMODE to reduce distortion
vmix is a virtual mixer audio that mixes multiple audio streams but can reduce the sound quality. Simply unchecking vmix-things in OSS Mixer GUI does not always work.

Turn off  to disable format conversions for all applications and devices.

Edit the following:

Restart  or your computer ifyou encounter errors.

After that you can still control the volume via ossmix or ossxmix.

## Start ossxmix docked to the system tray on startup
## KDE
Create an application launcher file named  in you local application launchers directory ( with:

To have it autostart with your system, add it to the list in System Settings > System Administration > Startup and Shutdown > Autostart.

## GNOME
As root create a file  with the following content:

Then go to System > Preferences > Start Up Applications and:
* Click Add, type  in the Name field and  in Command field then click Add Button.
* Login and logout to see the changes.

## Record sound output from a program
See upstream article on Recording sound output of a program.

## Suspend and hibernation
OSS does not automatically support suspend, it must be manually stopped prior to suspending or hibernating and restarted afterwards.

OSS provides  and  to enable and disable OSS, although they only stop OSS if all processes that use sound are terminated first.

The following script is a rather basic method of automatically unloading OSS prior to suspending and reloading afterwards.

{{hc|/usr/lib/systemd/system-sleep/50osssound.sh|
#!/bin/sh
suspend_osssound()
{
    /usr/lib/oss/scripts/killprocs.sh
    /usr/bin/soundoff
}

resume_osssound()
{
    /usr/bin/soundon
}

case $1 in
    pre)
        suspend_osssound
 	;;
    post)
 	resume_osssound
 	;;
    *) exit $NA
 	;;
esac
}}

Save the contents of this script (as root) into  and make it executable.

With this, all your applications should be fine.

## Changing the default sound output
When running , the first test passes for the first channel, but not for the stereo or right channel, it sounds distorted/hisses.  If this is what your sound is like, then it is set to the wrong output.

 *** Scanning sound adapter #-1 ***
 /dev/oss/oss_hdaudio0/pcm0 (audio engine 0): HD Audio play front
 - Performing audio playback test...
  OK  OK  OK

The left sounded good, the right and stereo were the distorted ones.

Let the test continue until you get a working output:
 /dev/oss/oss_hdaudio0/spdout0 (audio engine 5): HD Audio play spdif-out
 - Performing audio playback test...
  OK  OK  OK

If this passed the test on all left, right and stereo, proceed to next step.

For the command to change the default output see upstream's
wiki article. Change it to what works for you, for example:

 # ln -sf /dev/oss/oss_hdaudio0/spdout0 /dev/dsp_multich

For surround sound (4.0-7.1) choose , for only 2 channels,  is sufficient. See this for all available devices.

## Settings for a specific driver
If something is not working, there is a possibility that some of your OSS settings are driver specific or just wrong for your driver.

To solve this:
* Find out which driver is used

* Locate configuration file for device in:
 # cd /usr/lib/oss/conf/

* Try changing defaults. There are only few settings, and they are self explanatory

For example, the setting:
 ich_jacksense = 1
in  turns on  (which is responsible for recognizing plugged headphones and muting the speaker). Other settings for  can be found in  where you have to change the  variable.

* Restart the  for changes take effects.

## Troubleshooting
## Troubleshooting HD Audio devices
## Understanding the problem
If you have a HD Audio sound device, it is very likely that you will have to adjust some mixer settings before your sound works.

HD Audio devices are very powerful in the sense that they can contain a lot of small circuits (called widgets) that can be adjusted by software at any time. These controls are exposed to the mixer, and they can be used, for example, to turn the earphone jack into a sound input jack instead of a sound output jack.

However, there are also bad side effects, mainly because the HD Audio standard is more flexible than it perhaps should be, and because the vendors often only care to get their official drivers working.

When using HD Audio devices, you often find disorganized mixer controls, that do not work at all by default, and you are forced to try every mixer control combination possible, until it works.

## Solution
Open  and try to change every mixer control in the middle area, that contains the sound card specific controls, as explained in the #Volume control mixer section.

You will probably want to setup a program to record/play continuously in the background (e.g.   for recording or  for playing), while changing mixer settings in  in the foreground.

* Raise every volume control slider.
* In each option box, try to change the selected option, trying all the possible combinations.
* If you get noise, try to lower and/or mute some volume controls, until you find the source of the noise.
* Editing , uncommenting and changing  to a value from 0-7 can give you more jack options in .

## MMS sound cracking in Totem
If you hear various cracks or strange noises in Totem during playback, you can try using another backend such as FFmpeg. This will not fix the issue that somehow pops up in GStreamer when playing MMS streams but it will give you the option to play it with good sound quality. Playing it in MPlayer is simple:

 # mplayer mmsh://yourstreamurl

## Microphone playing through output channels
By default, OSS plays back the microphone through the speakers. To disable this in ossxmix find the "Misc" section and uncheck every "input-mix-mute" box.

## Add additional HD Audio sound cards support
OSS provides a "generic" codec driver that should be able to parse 99% of all HDAudio codecs.

If the device are not listed in the  source file, add them to it, recompile and start the drivers.

To find the device/vendor IDs for "Multimedia controller" device class, do the following:

In this example, "Vendor ID" is "8086" and "Device ID" is "a170".

Change 5 lines of code in the source code, taking "the latest source package"(currently "oss-v4.2-build2020-src-gpl.tar.bz2") as an example:

It is better to modify the existing "Controller" ( in this example), appending a new line of code may fail. It does not matter if it is .

The last line of code is a bit complicated. This example is an ALC1150 sound card chip. The "Vendor_id" of "ALC1150" is "0x10ec0900", you can get it through a search engine, or try the following:

For sound card chips of different manufacturers, different paragraphs need to be modified. In the example, the paragraph of Realtek manufacturer:

{{hc|oss-v4.2-build2020-src-gpl/kernel/drv/oss_hdaudio/hdaudio_codecids.h|
  {0x10ec0889, "ALC889", VF_ALC88X_HACK, (char **) &alc883remap},
  {0x10ec0900, "ALC1150", VF_ALC88X_HACK, (char **) &alc883remap},
  {0x10ec0899, "ALC899", VF_ALC88X_HACK, (char **) &alc883remap},
}}

It is very important that on the hardware of this example, modifying the second-to-last line works, but modifying the same code on the first-to-last line fails. You will need to try and modify the same code over and over on different lines to work on your hardware.

For example, try on the 4th last line:

  {0x10ec0887, "ALC887", VF_ALC88X_HACK, (char **) &alc883remap},
  {0x10ec0900, "ALC1150", VF_ALC88X_HACK, (char **) &alc883remap},
  {0x10ec0889, "ALC889", VF_ALC88X_HACK, (char **) &alc883remap},
  {0x10ec0892, "ALC892", VF_ALC88X_HACK, (char **) &alc883remap},
  {0x10ec0899, "ALC899", VF_ALC88X_HACK, (char **) &alc883remap},
