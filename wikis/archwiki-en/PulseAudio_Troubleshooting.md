# PulseAudio/Troubleshooting

## Getting debug output from PulseAudio
It can be useful to stop the  and  user units, and start manually in a terminal during debugging:

 $ pulseaudio -v

Add s to increase verbosity.

## Volume
Here you will find some hints on volume issues and why you may not hear anything.

## Auto-Mute Mode
Auto-Mute Mode is a configurable setting from . For more information, see ALSA#Disabling auto mute on startup.

## Muted audio device
If one experiences no audio output via any means while using ALSA, attempt to unmute the sound card. To do this, launch  and make sure each column has a green  under it (this can be toggled by pressing ):

 $ alsamixer -c 0

To troubleshoot via CLI only, install  and check the output of the following command:

 $ pamixer --get-volume-human

If the output says , run  to unmute. If it displays a low percentage value, you can run  several times to turn up the volume gradually.

## Output stuck muted while Master is toggled
In setups with multiple outputs (e.g. 'Headphone' and 'Speaker'), using plain amixer to toggle Master can trigger PulseAudio to mute the active output too, but it does not necessarily unmute it when Master is toggled back to be unmuted. To resolve this, amixer must have the device flag set to  (requires ):

 $ amixer -D pulse sset Master toggle

This will cause amixer to ask PulseAudio to do the toggling rather than toggling it directly.
Because of this, PulseAudio will correctly unmute Master as well as any applicable output.

## Muted application
If a specific application is muted or low while all else seems to be in order, it may be due to individual  settings. With the offending application playing audio, run:

 $ pacmd list-sink-inputs

Find and make note of the  of the corresponding . The   and , among others, should help here. Ensure sane settings are present, specifically those of  and .

If the sink input is muted, it can be unmuted by:

 $ pacmd set-sink-input-mute index false

If the volume needs adjusting, it can be set to 100% by:

 $ pacmd set-sink-input-volume index 0x10000

## Volume adjustment does not work properly
Check .

If the volume does not appear to increment/decrement properly using alsamixer or amixer, it may be due to PulseAudio having a larger number of increments (65537 to be exact). Try using larger values when changing volume (e.g. ).

## Per-application volumes change when the Master volume is adjusted
This is because your PulseAudio configuration uses flat volumes, instead of relative volumes, relative to an absolute master volume. If this is found to be inconvenient, asinine, or otherwise undesireable, relative volumes can be enabled by disabling flat volumes in the PulseAudio daemon's configuration file:

and then restarting PulseAudio by executing

 $ pulseaudio -k
 $ pulseaudio --start

## Volume gets louder every time a new application is started
Per default, it seems as if changing the volume in an application sets the global system volume to that level instead of only affecting the respective application. Applications setting their volume on startup will therefore cause the system volume to "jump".

Fix this by disabling flat volumes, as demonstrated in the previous section. When PulseAudio comes back after a few seconds, applications will not alter the global system volume anymore but have their own volume level again.

## Sound output is only mono on M-Audio Audiophile 2496 sound card
Add the following:

## No sound below a volume cutoff or Clipping on a particular output device
Known issue (will not fix): https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/223133

If sound does not play when PulseAudio's volume is set below a certain level, or if you hear clipping on output even at low volume (including Bluetooth devices), try setting  in :

However, be aware that it may cause another bug preventing PulseAudio to unmute speakers when headphones or other audio devices are unplugged.

## Low volume for internal microphone
If you experience low volume on internal notebook microphone, try setting:

## Clients alter master output volume (a.k.a. volume jumps to 100% after running application)
If changing the volume in specific applications or simply running an application changes the master output volume, this is likely due to flat volumes mode of PulseAudio. Before disabling it, KDE users should try lowering the volume in System Settings > Sound > Notification Sounds to something reasonable. Changing the Event Sounds volume in KMix or another volume mixer application will not help here. This should make the flat-volumes mode work out as intended, if it does not work, some other application is likely requesting 100% volume when its playing something. If all else fails, you can try to disable flat-volumes:

Then restart the PulseAudio daemon:

 $ pulseaudio -k
 $ pulseaudio --start

## No sound after resume from suspend
If audio generally works, but stops after resume from suspend, try "reloading" PulseAudio by executing:

 $ /usr/bin/pasuspender /bin/true

This is better than completely killing and restarting it ( followed by ), because it does not break already running applications.

If the above fixes your problem, you may wish to automate it, by creating a systemd service file.

Create the template service file in

Do a daemon-reload and enable this service for your user account (i.e. )

## ALSA channels mute when headphones are plugged/unplugged improperly
If when you unplug your headphones or plug them in the audio remains muted in alsamixer on the wrong channel due to it being set to 0%, you may be able to fix it by opening  and commenting out the line:

 load-module module-switch-on-port-available

Then restart the  user unit.

## Volume resets to 50% every few seconds
Install  and use hdajackretask:

* Set Not Connected to everything but the ports you are using. It seems the other unused audio ports on the motherboard interfere with the used ones.
* Then, if you want, use the Boot Override to save this change between reboots. There is a possibility it is the Front Green Headphone that is causing the bug, if you need it override the Front Microphone to Headphone and the Front Green Headphone to Not Connected and use the Front Microphone port as your headphone port.

More info about this problem: [https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/1585084.

## Volume low/too quiet on analog headphones/speakers
If you added the  option earlier to the  line in your , try removing it.

## Delay when changing volume using media keys
Edit  and set . This might cause some sound crackles when changing volume, in that case you might want to leave that option enabled and tweak the  and  options instead.

## Microphone
## Microphone not detected by PulseAudio
Determine the card and device number of your microphone:

In  notation, you would specify the above device as .

Then, edit  and insert a  line specifying your device as follows:

 load-module module-alsa-source device=hw:0,0
 # the line above should be somewhere before the line below
 .ifexists module-udev-detect.so

Finally, restart PulseAudio to apply the new settings:

 $ pulseaudio -k ; pulseaudio -D

If everything worked correctly, you should now see your microphone show up when running  (under the Input Devices tab).

## PulseAudio uses wrong microphone
If PulseAudio uses the wrong microphone, and changing the Input Device with pavucontrol did not help, take a look at alsamixer. It seems that pavucontrol does not always set the input source correctly.

 $ alsamixer

Press  and choose your sound card, e.g. HDA Intel. Now press  to display all items. Try to find the item: . With the up/down arrow keys you are able to change the input source.

Now try if the correct microphone is used for recording.

## No microphone on ThinkPad T400/T500/T420
Run:

 $ alsamixer -c 0

Unmute and maximize the volume of the "Internal Mic".

Once you see the device with:

 $ arecord -l

you might still need to adjust the settings. The microphone and the audio jack are duplexed. Set the configuration of the internal audio in pavucontrol to Analog Stereo Duplex.

## No microphone input on Acer Aspire One and Lenovo Ideapad 310-15ISK/330-15ARR
Install and run , unlink the microphone channels and turn down the volume of one of the channels (which one depends on the device) to 0.

Some applications can change microphone levels causing the same issue. Try disabling volume adjustment in the application settings. For example, in Chromium, open  and set Allow WebRTC to adjust the input volume to Disabled. If the application does not have such an option, a workaround is to remap stereo input to mono and use the remapped device as default.

## Static noise in microphone recording
## Incorrect sampling rate
If you are getting static noise in recordings, then the sound card sampling rate might be incorrect. To fix this, we need to set the sampling rate in the daemon.conf configuration file for the sound hardware.

* Determine sound cards in the system.

: The sound card is  where  is the card number and  is the device number. In the above example, it is .
: For more information, see Advanced Linux Sound Architecture#Cards and modules.

* Determine sampling rate of the sound card.
: We aim to find the highest sampling rate supported by the  sound card using a trial-and-error procedure starting from a low value. When the top value is reached, we got a warning message:

: observe, the . This is the maximum sampling rate of our card.

* Setting the sound card sampling rate into PulseAudio configuration.
: The default sampling rate in PulseAudio:

 is disabled and needs to be changed to :

 # sed 's/; default-sample-rate = 48000/default-sample-rate = 44100/g' -i /etc/pulse/daemon.conf

* Restart PulseAudio to apply the new settings:

 $ pulseaudio -k
 $ pulseaudio --start

* Finally check by recording and playing it back. Let us record some voice using a microphone for, say, 10 seconds:

 $ arecord -f cd -d 10 test-mic.wav

: After 10 seconds, let us play the recording:

 $ aplay test-mic.wav

Now hopefully, there is no static noise in microphone recording anymore.

## Incorrect stereo input
Another possible cause is that your microphone has two channels but only one channel can provide a valid sound signal. Some information can be found here. The solution is to remap the stereo input to a mono input:

* Find your source name from the following command:

 $ pacmd list-sources | grep 'name:.*input'

: For example, the result could be .

* Edit PulseAudio#default.pa configuration file and add the following lines, where  is name of the input source from above step:

 load-module module-remap-source source_name=record_mono master=INPUT_NAME master_channel_map=front-left channel_map=mono
 set-default-source record_mono

* Restart PulseAudio:

 $ pulseaudio -k
 $ pulseaudio --start

Now arecord hopefully works.

## USB microphone
Try plugging it into a different port—e.g. ports at the back rather than front.

## No microphone on Steam with enable-remixing = no
When you set  on  you may find that your microphone has stopped working on certain applications like Steam. This happens because these applications capture the microphone as mono only and because remixing is disabled, PulseAudio will no longer remix your stereo microphone to mono.

To fix this you need to tell PulseAudio to do this for you:

1. Find the name of the source

 $ pacmd list-sources

Example output edited for brevity, the name you need is in bold:

    index: 2
        name:
        driver:
        flags: HARDWARE HW_MUTE_CTRL HW_VOLUME_CTRL DECIBEL_VOLUME LATENCY DYNAMIC_LATENCY

2. Add a remap rule to , use the name you found with the previous command, here we will use  as an example:

3. Restart PulseAudio

 $ pulseaudio -k

 $ pulseaudio --start

## Microphone distorted due to automatic adjustment
If your microphone volume creeps up automatically and causes the sound to be distorted, you can fix it by disabling mic boost:

In all files ,

* Under  set  to
* Under  set  to .
* Under  set  to .
* Under  set  to .

including all variations such as  and

Then restart PulseAudio:

 $ pulseaudio -k

## Microphone crackling with Realtek ALC892
Sometimes ALC892 chips have crackling sound while recording using a microphone. Some PulseAudio configuration changes may help:

and add the  option to

then restart PulseAudio.

## Echo test
If you are unsure about your microphone setup, you can hear the input from the microphone in real-time by enabling the loopback module (source):

 $ pactl load-module module-loopback

The module will show up in the Recording tab of the  program, where the source and volume can be configured. While latency should be low, it should be sufficient to get a feeling of the sound quality as you will hear yourself speak in the microphone. To make the change permanent, add the following PulseAudio configuration:

Watch out for feedback! Be ready to lower all volumes in case the microphone picks up the output from the loudspeakers. Naturally, it is better to run such a test with headphones.

## Audio quality
## Troubleshooting buffer underruns (glitches, skips, crackling)
The newer implementation of the PulseAudio sound server uses timer-based audio scheduling instead of the traditional, interrupt-driven approach.

Timer-based scheduling may expose issues in some ALSA drivers. On the other hand, other drivers might have a tendency to experience buffer underruns without it on, so check to see what works on your system.

To turn timer-based scheduling off, add  in :

Then restart the PulseAudio server:

 $ pulseaudio -k
 $ pulseaudio --start

Do the reverse to enable timer-based scheduling, if not already enabled by default.

If you are using Intel's IOMMU and experience buffer underruns, add  to your kernel command line.

If you experience buffer underruns because of kernel page locking or late scheduling, see Gaming#Tweaking kernel parameters for response time consistency.

## Static noise when using headphones
Time-based scheduling may be causing this, disable it as explained in #Troubleshooting buffer underruns (glitches, skips, crackling).

Another reason you are encountering static noise in your headphone jack could be ALSA's loopback mixing.

Make sure you have  installed, launch , then select your audio device (pressing ), navigate all the way left using the , and stop on Loopback, if Enabled disable it using the . This should not impact audio playback or microphone recording negatively, unless you require loopback mixing.

Some notebook models, like Dell XPS 13 9360, suffer from continuous hissing sound when a headphone is plugged in.

Yet another reason for this symptom could be the power-saving mode of your audio device.If you followed Power management#Audio, revert the changes and check if it solves the problem.

## Setting the default fragment number and buffer size in PulseAudio
## Disabling timer-based scheduling
By default, PulseAudio uses timer-based scheduling. In this mode, fixed-size fragments are not used at all, and so the  and  parameters are ignored.
To turn timer-based scheduling off, add  in :

## Decide on audio device parameters
Instructions below will cause PulseAudio to use a fixed size and number for audio fragments. These settings directly affect latency and power consumption. The latency is determined as , and the interrupt rate (i.e. how often the application is notified that some sound has indeed been played) is . The considerations are:

* The total number of fragments must be within the limits accepted by the hardware. Most sound cards are OK with two or more fragments, but some require three or more.
* Giving the sound card more fragments than strictly necessary increases the latency, does not change power consumption, and does not remove the load from the scheduler. Therefore, it is advised only in the cases when the interrupts are not reliably delivered to the CPU, and one extra fragment beyond the minimum required should always be enough.
* Giving the sound card bigger fragments increases latency and decreases power consumption.
* Some applications (games and VoIP) request low latency and result in buffer underruns when PulseAudio cannot fulfill their request.
* Setting the latency too low will put a lot of stress on the scheduler, also resulting in buffer underruns.

If one does not care about excessive power consumption, then 2 or 3 fragments, 5 ms each, are a reasonable choice.

## Modify PulseAudio's configuration file
## See if it helps
Restart the  user unit.

Run your applications, listen to the sounds they produce, inspect the journal.

If the buffer underruns are occasional and mostly correlated to the system being highly loaded: this is a scheduler problem, the latency needs to be increased.

If there is metallic sound with the wrong speed from all applications: the most common reason is that you are trying to configure the fragment size which is way too small, like 1 ms. Do not do this.

If some, but not all, applications experience buffer underruns: this is an application that assumes a low-latency setup. So the fragment size must be decreased so that the application request becomes valid.

## Choppy sound with analog surround sound setup
Try to enable LFE remixing as described in PulseAudio/Examples#LFE remixing.

## Laggy sound
This issue is due to incorrect buffer sizes. First verify that the variables  and  are not being set to non default values in the file . If the issue is still present, try setting them to the following values:

## Choppy/distorted sound
This can result from an incorrectly set sample rate. Try the following setting:

and restart the PulseAudio server.

If one experiences choppy sound in applications using OpenAL, change the sample rate in :

Setting the PCM volume above 0 dB can cause clipping. Running  will allow you to see if this is the problem and if so fix it. Note that ALSA may not [https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/PulseAudioStoleMyVolumes/ correctly export the dB information to PulseAudio. Try the following:

and restart the PulseAudio server. See also #No sound below a volume cutoff or Clipping on a particular output device.

## Sound stuttering when streaming over network
When streaming over Wi-Fi using module-native-protocol-tcp, you can experience periodic sound stuttering with buffer underruns. As a workaround, you can try to use the rtp protocol. Install  on both sides. On the sender side, create an rtp sink:

and switch to it:

On the receiver side, load the rtp module:

## Pops when starting and stopping playback
PulseAudio can suspend sinks after a period of inactivity. This can make an audible noise (like a crack/pop/scratch). Sometimes even when move the slider volume, or open and close windows. This behavior is enabled in default configuration files:

Commenting that line in relevant file fixes that issue. A better solution is to add the following file:

For some devices (eg. Bose Quietcomfort 35 II), setting high enough volume of the device (usually via physical buttons or a slider) eliminates the audible noise after stopping playback.

## Hardware and cards
## No HDMI sound output after some time with the monitor turned off
The monitor is connected via HDMI/DisplayPort, and the audio jack is plugged in the headphone jack of the monitor, but PulseAudio insists that it is unplugged:

This leads to no sound coming from HDMI output. A workaround for this is to switch to another VT and back again. If that does not work, try: turn off your monitor, switch to another VT, turn on your monitor, and switch back. This problem has been reported by ATI/Nvidia/Intel users.

Another workaround could be to disable the switch-on-port-available module by commenting it in  === No HDMI sound using a headless server ===

You might want to use HDMI audio with your a/v receiver but no display. HDMI requires a video signal, which we have from the virtual terminal.

When the video signal turns off, the audio sink gets lost as well, so make sure that console blanking is disabled. See Display Power Management Signaling#Linux console for details.

## No cards
If PulseAudio starts, run . If no cards are reported, make sure that the ALSA devices are not in use:

 $ fuser -v /dev/snd/*
 $ fuser -v /dev/dsp

Make sure any applications using the pcm or dsp files are shut down before restarting PulseAudio.

## Starting an application interrupts other app's sound
If you have trouble with some applications (such as TeamSpeak or Mumble) interrupting sound output of already running applications (such as DeaDBeeF), you can solve this by commenting out the line  in  like shown below:

Then restart PulseAudio:

 $ pulseaudio -k
 $ pulseaudio --start

## The only device shown is "dummy output" or newly connected cards are not detected
If the only playback device is the Dummy Output, PulseAudio cannot access your sound devices. It is possible there is an issue with logind giving permissions, see General troubleshooting#Session permissions for more information.

An application might also not have been configured to work with PulseAudio. This happens with FluidSynth for example. To see which application is responsible for a direct access to the sound card via ALSA, run the following command:

 # fuser -v /dev/snd/*

Try to close these applications. PulseAudio, if running, should take again precedence over these applications and all the applications relying on PulseAudio should work again like expected.

If the above does not work, try to restart .

Restarting  can also be useful if PulseAudio fails to detect any hardware after resuming from hibernate or suspend.

## No 5/7.1 selection for HDMI device
If you are unable to select 5/7.1 channel output for a working HDMI device, then turning off "stream device reading" in  might help.

See #Fallback device is not respected.

## Failed to create sink input: sink is suspended
If you do not have any output sound and receive dozens of error messages related to a suspended sink from running  as root, then backup first and then delete your user-specific PulseAudio folders:

 $ rm -r ~/.pulse ~/.pulse-cookie ~/.config/pulse

## Simultaneous output to multiple sound cards / devices
Simultaneous output to two different devices can be very useful. For example, being able to send audio to your A/V receiver via your graphics card's HDMI output, while also sending the same audio through the analogue output of your motherboard's built-in audio. This is much less hassle than it used to be (in this example, we are using GNOME desktop).

Using , simply select Add virtual output device for simultaneous output on all local sound cards from under the Simultaneous Output tab. Then, under GNOME's sound settings, select the simultaneous output you have just created.

If this does not work, try adding the following to :

 pcm.dsp {
    type plug
    slave.pcm "dmix"
 }

## Simultaneous output to multiple sinks on the same sound card not working
This can be useful for users who have multiple sound sources and want to play them on different sinks/outputs.
An example use-case for this would be if you play music and also voice chat and want to output music to speakers (in this case Digital S/PDIF) and voice to headphones. (Analog)

This is sometimes auto detected by PulseAudio but not always. If you know that your sound card can output to both Analog and S/PDIF at the same time and PulseAudio does not have this option in its profiles in pavucontrol or veromix, then you probably need to create a configuration file for your sound card.

More in detail you need to create a profile-set for your specific sound card.
This is done in two steps mostly.

* Create udev rule to make PulseAudio choose your PulseAudio configuration file specific to the sound card.
* Create the actual configuration.

Create a PulseAudio udev rule.

Now, create a configuration file. If you bother, you can start from scratch and make it saucy. However you can also use the default configuration file, rename it, and then add your profile there that you know works. Less pretty but also faster.

To enable multiple sinks for Asus Xonar Essence STX, you only need to add this in.

This will auto-profile your Asus Xonar Essence STX with default profiles and add your own profile so you can have multiple sinks.

You need to create another profile in the configuration file if you want to have the same functionality with AC3 Digital 5.1 output.

[https://www.freedesktop.org/wiki/Software/PulseAudio/Backends/ALSA/Profiles/ See PulseAudio article about profiles

## Some profiles like SPDIF are not enabled by default on the card
Some profiles like IEC-958 (i.e. S/PDIF) may not be enabled by default on the selected sink. Each time the system starts up, the card profile is disabled and the pulseaudio daemon cannot select it.
You have to add the profile selection to you default.pa file.
Verify the card and profile name with:

 $ pacmd list-cards

Then edit the configuration to add the profile

PulseAudio will add this profile the pool of available profiles

## Only S/PDIF output available
This might happen if PulseAudio use the wrong output device. Firstly, set up proper card profile:

 $ pacmd set-card-profile alsa_card.pci-0000_00_1f.3 output:analog-stereo

or

 $ pacmd set-card-profile alsa_card.pci-0000_00_1f.3 output:analog-stereo+input:analog-stereo

Replace  with your card, and  or  with your profile, remember to choose the profile with analog. Using shell auto completion could help you a lot. One could also use check available cards and profiles with:

 $ pacmd list-cards

One might also need to set sink port by:

 $ pacmd set-sink-port alsa_output.pci-0000_00_1f.3.analog-stereo analog-output-headphones

Check available sink ports with:

 $ pacmd list-sinks

To keep these setting, add them to PulseAudio's configuration file .

## Crackling or popping USB sound issues
Although not related to PulseAudio, it is also possible that the card is not powered properly by its USB port, or that it does not provide enough bandwidth.

Try connecting the USB DAC directly to your computer's USB ports, avoiding any hubs or docks.

## Bluetooth
See Bluetooth headset#Troubleshooting 2.

## Applications
## Audacity
When starting Audacity, you may find that your headphones no longer work. This can be because Audacity is trying to use them as a recording device. To fix this, open Audacity, then set its recording device to .

Under some circumstances, playback may be distorted, very fast, or freeze, as explained upstream, start Audacity with:

 $ env PULSE_LATENCY_MSEC=30 audacity

If the solution above does not fix this issue, one may wish to temporarily disable PulseAudio while running Audacity by using the pasuspender command:

 $ pasuspender -- audacity

Then, be sure to select the appropriate ALSA input and output devices in Audacity.

See also #Some applications do not appear in pavucontrol or play sound and #Setting the default fragment number and buffer size in PulseAudio.

## OpenAL
Some games may prevent you from switching the output device. Trying to move the sink with  gives the following error:

 pactl move-sink-input 11 alsa_output.pci-0000_01_00.1.hdmi-stereo-extra1
 Failure: Invalid argument

OpenAL needs to be configured to allow moving the sink:

## Browsers (firefox) load videos but do no play
Check your  file for the following options:

For me, I have my default sample rate changed from 44.1Khz to 384Khz. After that, firefox starts to having problems playing from netflix, hbo max and paramount+ sites. However, spotify is not affected.

If you have the alternate-sample-rate set to the default 48000, firefox will try to send audio in that sample rate. That triggers a pulseaudio to not resample the audio and send it directly to the audio card, which causes problems of playback.

If you set the alternate-sample-rate to the same as the default sample rate, it will trigger pulseaudio to resample the audio from firefox. Then everything works correctly.

Finally, opera or other chromium based browsers were not affected by this issue since it seems that they always re-sample to match what pulseaudio's default sample rate. Firefox in that regard is trying to be more bit-perfect in playback, which is a good thing. But unfortunately run into this bug/issue with pulseaudio.

## Other issues
## Some applications do not appear in pavucontrol or play sound
To work with PulseAudio, some applications require . This provides the  playback and recording devices. See PulseAudio#ALSA for details.

## Cannot update configuration of sound device in pavucontrol
 is a handy GUI utility for configuring PulseAudio. Under its Configuration tab, you can select different profiles for each of your sound devices e.g. analogue stereo, digital output (IEC958), HDMI 5.1 Surround etc.

However, you may run into an instance where selecting a different profile for a card results in the PulseAudio daemon crashing and auto restarting without the new selection "sticking". If this occurs, use the other useful GUI tool, , to check under the Simultaneous Output tab for a virtual simultaneous device. If this setting is active (checked), it will prevent you changing any card's profile in pavucontrol. Uncheck this setting, then adjust your profile in pavucontrol prior to re-enabling simultaneous output in paprefs.

## PulseAudio overwrites ALSA settings
PulseAudio usually overwrites the ALSA settings — for example set with alsamixer — at start-up, even when the ALSA daemon is loaded. Since there seems to be no other way to restrict this behaviour, a workaround is to restore the ALSA settings again after PulseAudio has started. Add the following command to  or  or any other autostart file:

 restore_alsa() {
  while [ -z "$(pidof pulseaudio)" ]; do
   sleep 0.5
  done
  alsactl -f /var/lib/alsa/asound.state restore
 }
 restore_alsa &

## Daemon startup failed
Try resetting PulseAudio:

 $ rm -rf /tmp/pulse* ~/.pulse* ~/.config/pulse
 $ pulseaudio -k
 $ pulseaudio --start

* Check that options for sinks are set up correctly.
* If you configured in  to load and use the OSS modules, then check with  that  device is not used by another application.
* Set a preferred working resample method. Use  to see a list with all available resample methods you can use.
* To get details about currently appeared unfixed errors or to just get the status of the daemon, use commands like  and  where  option can be used multiple time to set the verbosity of log output equal to the  option where LEVEL is from 0 to 4. See the #Outputs by PulseAudio error status check utilities section.

See also man pages for  and  for more details.

## Outputs by PulseAudio error status check utilities
If the  shows error like:

 N: main.c: User-configured server at "user", refusing to start/autospawn.

then run  command then could be also good to logout and login again.

If the  command shows error like:

 E: [pulseaudio module-udev-detect.c: You apparently ran out of inotify watches, probably because Tracker/Beagle took them all away. I wished people would do their homework first and fix inotify before using it for watching whole directory trees which is something the current inotify is certainly not useful for. Please make sure to drop the Tracker/Beagle guys a line complaining about their broken use of inotify.

This can be resolved temporary by:

 $ echo 100000 > /proc/sys/fs/inotify/max_user_watches

For permanent use save settings in the  file:

See also

* proc_sys_fs_inotify and dnotify, inotify- more details about inotify/max_user_watches
* reasonable amount of inotify watches with Linux
*  - man page

## Daemon already running
On some systems, PulseAudio may be started multiple times. journalctl will report:

 pid.c: Daemon already running.

Make sure to use only one method of autostarting applications.  includes these files:

*
*
* The  and  user units

Also check user autostart files and directories, such as xinitrc,  etc.

## Subwoofer stops working after end of every song
Known issue: https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/494099

To fix this, enable LFE remixing as described in PulseAudio/Examples#LFE remixing.

## Unable to select surround configuration other than "Surround 4.0"
If you are unable to set 5.1 surround output in pavucontrol because it only shows "Analog Surround 4.0 Output", open the ALSA mixer and change the output configuration there to 6 channels. Then restart PulseAudio, and pavucontrol will list many more options.

## Realtime scheduling
If rtkit does not work, you can manually set up your system to run PulseAudio with real-time scheduling, which can help performance. To do this, add the following lines to :

 @pulse-rt - rtprio 9
 @pulse-rt - nice -11

Afterwards, you need to add your user to the  group.

## Fallback device is not respected
PulseAudio does not have a true default device. Instead it uses a [https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/DefaultDevice/ "fallback", which only applies to new sound streams. This means previously run applications are not affected by the newly set fallback device.

 and  handle this gracefully. Alternatively:

# Move the old streams in  manually to the new sound card.
# Stop PulseAudio, erase the "stream-volumes" in  and/or  and restart PulseAudio. This also resets application volumes.
# Disable stream device reading. This may be not wanted when using different soundcards with different applications.

## RTP/UDP packet flood
In some cases, the default configuration might flood the network with UDP packets.To fix this problem, launch  and disable Multicast/RTP Sender.[https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/411688/comments/36

## New audio source streams auto-select to "blank" stream instead of BT headphones
Example scenario: Restarting, stopping, fast forwarding a Youtube video on Firefox 68.0.1 on KDE + Arch might set the "sink" associated with it in PulseAudio to a blank state, and then output sound over laptop speakers. Inconsistently reproducible on Dell 9360.

Fix seems to be to kill and restart PulseAudio.

 $ pulseaudio -k
 $ pulseaudio --start
