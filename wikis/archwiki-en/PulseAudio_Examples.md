# PulseAudio/Examples

## Creating user configuration files
System-wide configuration files are located under  while user configuration files are located under , which defaults to . For the examples below which modify the user's configuration file it may be necessary to first create the file. This can be done either by copying the system file under  to the user's configuration directory, or by creating a new file that includes it with the syntax . For simple changes the latter is preferred because the user will not be required to update the file when system-wide defaults change.

## User client configuration file example
This syntax works for ,  and , even if the latter makes no sense as a user configuration file.

## Set default input source
List available input sources:

The  in front of the index indicates the current default input.

To set a system wide default, add the source name in the  file:

For temporary use:

 $ pacmd set-default-source alsa_output.pci-0000_04_01.0.analog-stereo.monitor

## Set the default output sink
To list the output sinks available, type the following command:

The  in front of the index indicates the current default output.

To set a system wide default, add the source name in the  file:

or per-user configuration  file (which loads the default configuration from  and overwrites the lines specified in this file):

When done then you can logout/login or restart PulseAudio manually for these changes to take effect.

## Set the default output sink profile
Sometimes PulseAudio neglects to load the desired profile on start (e.g. a profile for having #Independent analog and digital outputs on the same card). To change the default profile, append the following to :

Find  by running:

For example, if you want to use the device with index number 2, its  is .

To find , set the desired profile manually (e.g. using ), then run:

In this case,  should now be changed to this:

You can test your configuration by running .

## Independent analog and digital outputs on the same card
Sound cards may have both analog and digital (iec958) outputs.  PulseAudio does not generate combined profiles by default, you can choose either digital or analog profiles.

The easiest way to make both outputs available is to add a combined profile to the end of default profile configuration file:

This way a defined profile is added to the end of the list of available profiles.

Although this works, PulseAudio has a nasty habit of falling back to auto-generated profiles, so you may eventually need to set your card back to the combined profile.  The best way to overcome this is by writing a custom configuration with disabled . Copy  to , and edit it to suit your needs (this example is for stereo output/input):

Now that you have your custom profile you need to tell PulseAudio to use it. This can be done by defining an udev rule.

First get relevant information about your sound card:

Now create a configuration file:

{{hc|/usr/lib/udev/rules.d/91-pulseaudio-custom.rules|2=
SUBSYSTEM!="sound", GOTO="pulseaudio_end"
ACTION!="change", GOTO="pulseaudio_end"
KERNEL!="card*", GOTO="pulseaudio_end"

SUBSYSTEMS=="pci", ATTRS{vendor}=="0x8086", ATTRS{device}=="0x1c20", ENV{PULSE_PROFILE_SET}="custom-profile.conf"

LABEL="pulseaudio_end"
}}

Now tell udev to reload sound subsystem  (as the root user) and restart PulseAudio. Your sound card should now use only the defined profile and have both analog and digital outputs available.

## Simultaneous HDMI and analog output
PulseAudio allows for simultaneous output to multiple sources.  In this example, some applications are configured to use HDMI while others are configured to use analog.  Multiple applications are able to receive audio at the same time. (aplay is from the  package.)

Or by using the pacmd command:

The key to a configuration like this is to understand that whatever is selected in pavucontrol under Configuration > Internal Audio is the default device. Load pavucontrol > Configuration and select HDMI as the profile.

To setup the analog device as a secondary source, add the following to  or :

 ### Load analog device
 load-module module-alsa-sink device=hw:card,device
 load-module module-combine-sink sink_name=combined
 set-default-sink combined

Restart PulseAudio, run pavucontrol and select the Output Devices tab. Three settings should be displayed:

# Internal Audio Digital Stereo (HDMI)
# Internal Audio
# Simultaneous output to Internal Audio Digital Stereo (HDMI), Internal Audio

Now start a program that will use PulseAudio such as MPlayer, VLC, mpd, etc. and switch to the Playback tab. A drop-down list should be available for the running program to select one of the three sources.

Also see this thread for a variation on this theme and PulseAudio FAQ.

## Alternative solution using module-loopback with delay compensation
If the example above does not work for you, for instance because of echos / delays, you can try the following configuration.

In this case, the HDMI-Audio was 65ms behind analog when using .

Add these lines somewhere before  to make sure it will not conflict with this manual configuration.

## Simultaneous output to multiple HDMI / DisplayPort outputs
By default, PulseAudio uses only one HDMI / DisplayPort output per device. It allows you to choose an output by setting a profile, but does not allow to use multiple outputs at the same time. As a workaround, you can manually add another output as a separate PulseAudio device.

## Finding HDMI / DisplayPort output
Find the working output by listing the available cards:

In case your HDMI / DisplayPort output is wired to the NVIDIA card, but  does not detect an NVIDIA audio card, follow NVIDIA/Troubleshooting#No audio over HDMI.

## Testing for the correct card
Now that we have a list of detected cards and devices, users will need to test for which one is outputting to the TV/monitor; for example, to test card 1, device 3 from the list above:

 $ aplay -D plughw:1,3 /usr/share/sounds/alsa/Front_Right.wav

If you get , this probably means the device is already being used by PulseAudio; you may need to stop it temporarily.

If there is no audio, then try substituting a different card and/or device number. In this example, the TV/monitor is connected to card , device .

## Manually configuring PulseAudio to add the additional output
Having identified which HDMI / DisplayPort device is working, PulseAudio can be forced to use it by creating a .pa configuration file in :

 load-module module-alsa-sink device=hw:1,7

where the  is the card and the  is the device found to work in the previous section.

Restart PulseAudio:

 $ pulseaudio -k
 $ pulseaudio --start

Both outputs should now be available as separate devices (see the Output Devices tab in ).

If the second device does not appear, this may be because the output you chose is already used by PulseAudio by default; change it by choosing a different profile (you can use the Configuration tab in pavucontrol), or set a different output in the configuration file you created, then restart PulseAudio.

The Playback tab in pavucontrol allows you to route applications to specific outputs.

If you want to output the same audio to both outputs, you can use  or  in a way similar to that described in #Simultaneous HDMI and analog output (but you do not need to add  because you have already added it).

## Automatically switch audio to HDMI / DisplayPort
Instead of creating an additional PulseAudio device, you can create a script to switch to the desired audio profile if an HDMI / DisplayPort cable is plugged in (adapt the names of all devices to match your system):

{{hc|/usr/local/bin/hdmi_sound_toggle.sh|2=
#!/bin/bash

export PATH=/usr/bin

USER_NAME=$(who | awk -v vt=tty$(fgconsole) '$0 ~ vt {print $1}')
USER_ID=$(id -u "$USER_NAME")
CARD_PATH="/sys/class/drm/card0/"
AUDIO_OUTPUT="analog-surround-40"
PULSE_SERVER="unix:/run/user/"$USER_ID"/pulse/native"

for OUTPUT in $(cd "$CARD_PATH" && echo card*); do
  OUT_STATUS=$(
	name:
	name:
}}

Load the plugin (new sink_name is up to you, master=headphone's sink name):

 $ pacmd load-module module-ladspa-sink sink_name=binaural master=bluez_sink.00_1F_82_28_93_51 plugin=bs2b label=bs2b control=700,4.5

Use  to transfer streams to the new sink, or:

 $ pactl move-sink-input sink-input-id binaural-sink-name

## PulseAudio over network
One of PulseAudio's unique features is its ability to stream audio from clients over TCP to a server running the PulseAudio daemon reliably within a LAN. Ensure that client and server systems agree on the time (i.e., use NTP), or audio streams may be choppy or may not work at all. For a more detailed guide visit the official PulseAudio documentation.

To enable the TCP module on the server (the computer that actually outputs sound), create the following .pa file:

Or you can use the  GUI application (root is not required). Go to Network Server > Enable network access to local sound devices.

To make sure  is loaded on the server, you can use:

 $ pacmd list-modules | grep module-native-protocol-tcp

It is a requirement that both the client and server share the same cookie. Ensure that the clients and server share the same cookie file found under . It does not matter whose cookie file you use (the server or a client's), just that the server and client(s) share the same one.

If it is undesirable to copy the cookie file from clients, anonymous clients can access the server by passing  to  on the server (again in ):

 load-module module-native-protocol-tcp auth-anonymous=1

It is also possible to authenticate based on client IP address:

 load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;192.168.0.0/24

Change the LAN IP subnet to match that of those clients you wish to have access to the server.

## Selecting the server
For a single shell or command you can set the  environment variable to the host name or IP address of the desired PulseAudio server:

 $ env PULSE_SERVER=server-hostname-or-ip ffplay /usr/share/sounds/freedesktop/stereo/audio-channel-front-center.oga

Alternatively, you can create or modify  or  to set a default-server persistently:

 default-server = server-hostname-or-ip

It is also possible to specify multiple servers separated by spaces which are subsequently tried by PulseAudiodefault-server = server1 backup

## Selecting the server with Zeroconf
For the remote PulseAudio server to appear in the PulseAudio Device Chooser (), load the appropriate zeroconf modules, and enable the Avahi daemon. On both machines, the client and server, install the  package. Start/enable  afterwards.

On the server, add  to . On the client, add  to . Now redirect any stream or complete audio output to the remote PulseAudio server by selecting the appropriate sink.

If you have issues with the remote syncs appearing on the client, try restarting the Avahi daemon on the server to rebroadcast the available interfaces.

Run the graphical PulseAudio Volume Control . Under the Output Devices tab, you should see the local and remote output devices. Under the Playback tab, to the left of the "X" Mute Audio button, you should see a box containing the name of an output device. That box is actually a button, which will display a drop-down radio-button list of the available output devices, with one output device selected. Selecting an output device from the list will allow the audio stream to be switched to the PulseAudio server associated with that output device. This control is not at all obvious until you have used it, and is especially useful with a remote Headless sound server.

Similarly, under the Input Devices tab, local and remote input devices will be seen. And under the Recording tab, there will be a box, to the left of the "X" Mute Audio button, with the name of an input device which is actually a button which will display a drop-down radio-button list of available input devices.

## Using RTP/UDP instead of native-protocol-tcp
There are serious issues with trying to send data in real time over TCP, especially over lossy connections like Wi-Fi. This is why RTP over UDP was invented. It can be used to increase reliability and reduce latency.

When RTP is working properly, late or dropped packets will just create a few milliseconds of silence instead of a long pause while TCP is orchestrating the packet resend logistics. As an added bonus, if the remote server is ever restarted, the connection will be re-established automatically.  However there will no longer be a way to remotely control the server's master volume, with each client machine having its own independent master volume instead.

To use RTP instead of , PulseAudio clients must connect to a local PulseAudio server first. This local server then connects to the remote PulseAudio server through RTP.

To use RTP in PulseAudio, install  on the remote and local servers.

To configure the remote PulseAudio server, add the following to  (or to  if running PulseAudio in  mode):

 load-module module-rtp-recv latency_msec=10 sap_address=0.0.0.0

 is important to prevent PulseAudio from trying to use multicast, which [https://datatracker.ietf.org/doc/html/draft-mcbride-mboned-wifi-mcast-problem-statement-01.html#section-1 does not work at all over Wi-Fi. Use  to tune the receiving buffer size on the remote end. If you find the audio is spotty, try increasing this number. If you care more about latency, try decreasing it. Restart the remote server to cause the changes to take effect.

To configure the local PulseAudio server, add the following to :

 load-module module-null-sink sink_name=rtp sink_properties="device.description='RTP'"
 load-module module-rtp-send source=rtp.monitor destination_ip=remote_host

 is the host name of the remote PulseAudio server.

After restarting the local server, a new sink labelled "RTP" will appear in pavucontrol. To route a particular client's output to it, find the client under the Playback tab, then change the client from its current sink (e.g. "Built-in Audio Analog Stereo") to "RTP". To use the RTP sink by default for all clients, add this to , then restart the local PulseAudio server:

 set-default-sink rtp

## Enable autodiscover AirPlay (raop) server support
To autodiscover and use a AirPlay server, ensure the  is installed and Avahi is running (this is for autodetection itself).  Also install  (for the raop protocol).  Then, add the following to :

 load-module module-raop-discover

Restart  and devices should automatically appear in the list of sinks.

This example is taken from julianxhokaxhiu's gist.

## ALSA monitor source
To be able to record from a monitor source (a.k.a. "What-U-Hear", "Stereo Mix") using an ALSA application, run  to find out the name of the source in PulseAudio (e.g. ). Then install  and add lines like the following to  or  (see PulseAudio#ALSA for details):

 pcm.pulse_monitor {
   type pulse
   device alsa_output.pci-0000_00_1b.0.analog-stereo.monitor
 }

 ctl.pulse_monitor {
   type pulse
   device alsa_output.pci-0000_00_1b.0.analog-stereo.monitor
 }

Now you can select  as a recording source.

Alternatively, you can use pavucontrol to do this: make sure you have set up the display to All Input Devices, then select Monitor of sound card as the fallback recording source.

## Monitor specific output
It is possible to monitor a specific output, for example to stream audio from a music player into a VoIP application.
Simply create a null output device:

 $ pactl load-module module-null-sink sink_name=name sink_properties=device.description=description

In PulseAudio Volume Control (pavucontrol), under the Playback tab, change the output of an application to "name", and in the Recording tab change the input of an application to "Monitor of name". Audio will now be outputted from one application into the other.

## Capturing sound of only the specified applications
For multiple reasons, you may only want to capture audio from a single application. Maybe because you are trying to capture a game and do not want the voice call chatter to be included.
This involves creating a null sink, redirecting the existing audio output of the application to this null sink and loading the loopback module so you can still hear the sound emitted by the application. You can create a short script as a hook for the recording software of your choice:

It is necessary to restore the default sink, as PulseAudio may see only a single sink is in-use and redirect all future audio streams to the null sink, leading to unwanted audio to be included.

You can then use the new sink in the recording software of your choice. E.g with raw :

 $ SOURCE=$(pactl list short sources | grep gameaudio.monitor | cut -d "	" -f1)
 $ ffmpeg -f pulse -ac 2 -i $SOURCE file.ogg

## PulseAudio through JACK
The JACK Audio Connection Kit is popular for audio work, and is widely supported by Linux audio applications. It fills a similar niche as PulseAudio, but with more of an emphasis on professional audio work. It can offer lower latency audio monitoring along with greater control of input and output of multi-i/o sound devices.

## The KXStudio method
JACK now has native features for bridging between ALSA, PulseAudio, and JACK. This will allow you to simultaneously have JACK and PulseAudio running with both outputting at the same time, with no configuration editing or terminal commands required.

If you have  installed, make sure that it is not running (it might be running minified in the system tray). Also ensure that no  process is running (use  in a terminal to check).

Install , as well as . Once installed and started, JACK Bridges configuration is found in the bottom right of the Cadence window. Set ALSA Audio > Bridge Type to ALSA -> PulseAudio -> JACK (Plugin), then start JACK and enable the PulseAudio bridge. Make sure in pavucontrol that all output devices besides the JACK sink are muted, and all input devices besides the JACK input are muted. Now PulseAudio programs should begin outputting to JACK.

If PulseAudio is not running, Cadence will try to start its own PulseAudio instance, so you should either start the  user unit before starting Cadence or stop the  user unit to prevent conflicts.

## The manual sink configuration method
This configuration provides a method of allowing JACK and PulseAudio to run at the same time and output to each other. It uses manual configuration of the systems that bridge between JACK and PulseAudio. This configuration has no reliance on scripts or commands and is entirely based in configuration.

This configuration only works with  (use jackdbus or jack_control to start JACK).

To use this configuration, just install the  package.  is already configured to load the modules in  if they are present. If you want to be sure, open the file and look for the line:

 load-module module-jackdbus-detect options

Where  can be any options supported by this module, usually .

As described on the JACK DBus packaging page:

Server auto-launching is implemented as D-Bus call that auto-activates JACK D-Bus service, in case it is not already started, and starts the JACK server. Correct interaction with PulseAudio is done using a D-Bus based audio card "acquire/release" mechanism. When JACK server starts, it asks this D-Bus service to acquire the audio card and PulseAudio will unconditionally release it. When JACK server stops, it releases the audio card that can be grabbed again by PulseAudio.

 dynamically loads and unloads  and  when jackdbus is started and stopped.

If PulseAudio sound does not work, check with pavucontrol to see if the relevant programs appear in the Playback tab. If not, add the following to  or  to redirect ALSA to PulseAudio:

 pcm.pulse {
     type pulse
 }

 ctl.pulse {
     type pulse
 }

 pcm.!default {
     type pulse
 }

 ctl.!default {
     type pulse
 }

If it still does not work, check with pavucontrol in the Playback tab and make sure the relevant programs are outputting to PulseAudio JACK Sink instead of your audio card (which JACK has control of, so it will not work). Also ensure that in the JACK graph the PulseAudio JACK Source is connected to the system audio output.

## The shell script method
This method allows JACK and PulseAudio to output at the same time. It mostly relies on shell scripts that are automatically run by QjackCtl to manage aspects of how the JACK sinks and PulseAudio behave.

The basic idea is that killing PulseAudio is a bad idea because it may crash any applications using PulseAudio and disrupt any audio playing.

The flow of how this setup works:

# PulseAudio releases the sound card
# JACK grabs sound card and starts up
# script redirects PulseAudio to JACK
# manually send PulseAudio applications to JACK output (pavucontrol may come in helpful for this)
# use JACK programs etc
# via script, stop redirecting PulseAudio to JACK
# stop JACK and release sound card
# PulseAudio grabs sound card and reroutes audio to it directly

Open QjackCtl > Setup > Options and set up these scripts (do not forget to make them executable):

Execute script on Startup:

Execute script after Startup:

Execute script on Shutdown:

Execute script after Shutdown:

## The PulseAudio kill method
This method relies on shell scripts to automatically stop PulseAudio when JACK is started, and automatically restart it when JACK is stopped. This will result in lower CPU usage than having both running, but can cause errors in already running PulseAudio application and does not allow simultaneous output of both.

Open QjackCtl > Setup > Options and set up these scripts (do not forget to make them executable):

Execute script on Startup:

{{hc|jack-startup.sh|
#!/bin/sh
# Stop PulseAudio clients (for example PulseAudio system tray)
killall pasystray

# And stop PulseAudio before starting JACK
systemctl --user stop pulseaudio.{service,socket}
}}

Execute script after Shutdown:

{{hc|jack-shutdown.sh|
#!/bin/sh
# Start PulseAudio after stopping JACK
systemctl --user start pulseaudio.{service,socket}

# And start PulseAudio clients (for example PulseAudio system tray)
pasystray &
}}

## Troubleshooting
## When JACK is started, Firefox, Chrome and other applications stop playing video and audio
Firefox/Chrome/etc. is using PulseAudio soundcard sink instead of the JACK sink. Open  and on the Playback tab switch all audiostreams from something like "Built-in Audio Analog Stereo" to something like "Jack sink (PulseAudio JACK Sink)".

## After starting JACK, the sound from PulseAudio becomes distorted
In QjackCtl click Setup and on the Settings tab, Parameters subtab untick Realtime. In addition, tweaking Sample Rate, Frames/Period and Period/Buffer may help. Look for latency in the bottom right corner, as you still want minimal latency for audio production. Also, Sample Rate should probably match one of the rates supported by your audio interface ( and look for , there could be multiple occurrences).

## PulseAudio through OSS
Add the following to :

 load-module module-oss

Then start PulseAudio as usual, making sure that sinks and sources are defined for OSS devices.

## PulseAudio from within a chroot
PulseAudio clients, if not set up to connect to any specific server as described in #PulseAudio over network, will attempt to connect to the local PulseAudio server, failing which it will spawn a new server.

To allow for chrooted applications to access the PulseAudio server, you need to make the PulseAudio Unix socket available inside the chroot environment. By default, it is located at , and since  is  by default, you can simply do .

 should also be mounted for efficiency and good performance. Note that mounting  would normally also allow sharing of the  directory.

By default, PulseAudio selects the path to the Unix socket via , so be sure to drag it along when you chroot as a normal user using sudo (see Sudo#Environment variables).

The UID inside the chroot must match the UID of the PulseAudio server for the Unix socket connection to work. Alternatively, you can reconfigure the PulseAudio server as described in #Allowing multiple users to share a PulseAudio daemon.

## Remapping sinks
The module-remap-sink module creates a virtual sink, which is identified as a unique sink, but is connected to the master sink by a virtual stream. In doing so, it has the ability to remap how the master sink's channels are used for playback.

## Remapping select audio sources
Naturally, the virtual sink has its own monitor, which can be used as a source only capturing applications using the virtual sink. sink_name can be determined by looking at the  field in . As with other modules, it can be invoked from , or using :

 $ pacmd load-module module-remap-sink sink_name=secondary master=sink_name

For instance, to record a program's output without including any other system sounds, you could:

* Load the module by running the command.
* Using pavucontrol, in the Playback tab, change the desired program's output device to the remapping. Repeat for any other programs whose audio should be included.
* Activate the recording program.
* In pavucontrol, in the Recording tab, change the recording program's input to the Monitor of option for the remapping.

## Remap stereo to mono
Remap a stereo input-sink to a mono sink by creating a virtual sink. It would be useful if you only have one speaker. Add to :

 load-module module-remap-sink master=alsa_output.pci-0000_00_1f.5.analog-stereo sink_name=mono sink_properties="device.description='Mono'" channels=2 channel_map=mono,mono
 # Optional: Select new remap as default
 set-default-sink mono

(replace  in the sound card name shown from )

Switch player between virtual mono sink and real stereo sink.

## Remap left or right to mono
Particularly useful in the case an audio stream has different content in the left and right channels, such as Japanese television broadcasts with bilingual audio.

 # For Japanese bilingual TV
 load-module module-remap-sink sink_name=Left-to-Mono sink_properties="device.description='Left to Mono (5.1 AC3 on ALC892 Digital)'" master=alsa_output.pci-0000_00_1b.0.iec958-ac3-surround-51 channels=2 master_channel_map=mono,mono channel_map=front-left,rear-left
 load-module module-remap-sink sink_name=Right-to-Mono sink_properties="device.description='Right to Mono (5.1 AC3 on ALC892 Digital)'" master=alsa_output.pci-0000_00_1b.0.iec958-ac3-surround-51 channels=2 master_channel_map=mono,mono channel_map=front-right,rear-right

Replace  (5.1 AC3 on ALC892 Digital) with your own card ().

## Remap for broadcasting software
If you do not want to capture sound from the application you need to create Remap sink:

 ### Create Remap sink
 load-module module-remap-sink sink_name=Remap_sink master=SINK_NAME channels=2 remix=no
 set-default-sink Remap_sink

Then restart PulseAudio daemon:

 $ pulseaudio -k
 $ pulseaudio --start

Now you need set the  as the default sound source in broadcast software

## Remap left (or right) input to mono for stereo use
Sometimes the incoming audio is only present on one channel (e.g. when using a mono XLR microphone on a two channel audio interface that is configured as stereo input by default). Using , the left channel can be remapped to be a mono source for further use:

 load-module module-remap-source master=alsa_input.usb-BEHRINGER_UMC204HD_192k-00.analog-stereo channels=1 master_channel_map=front-left channel_map=mono

## Swap left/right channels
This is the same as "reverse stereo", where the left and right channels are to be swapped.

First, identify the card you want its channels swapped:

 $ cat /proc/asound/cards

and use the name string for the device you wish to use (the one in square brackets, e.g. ).

Add the following line somewhere before :

Then restart PulseAudio.

PulseAudio FAQ: How can I reverse my left and right speaker channels?

Alternatively, you can create a virtual device using  load-module module-remap-sink sink_name=reverse-stereo master=0 channels=2 master_channel_map=front-right,front-left channel_map=front-left,front-right
 set-default-sink reverse-stereo

## Pipe a source directly into a sink
Sometimes you want an input to be replicated to an output, e.g. if you want to play back your microphone on your speakers for troubleshooting, or want to hear your capture card's captured audio. Here is how to set that up dynamically using [https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#module-loopback module-loopback:

 $ pactl load-module module-loopback source=input_name sink=sink_name

This command will print the module's ID so that you can stop the piping later like this:

 $ pactl unload-module id

If you lose the ID, you can obtain it from .

## Capture digital input from S/PDIF and play on analog output in (nearly) real time
Sometimes you have a digital sound source that outputs S/PDIF signal encoded in PCM or AC3 (for example a smart TV) and you would like to use your Linux box as a converter for this signal to analog audible signal that you can play on your speakers. The challenge is to have no audible delay between your digital source and analog output (which can result in audio/video out of sync in our smart TV example).

You can use  tool for that purpose.

The usage is fairly simple. Just connect S/PDIF cable to your sound card digital input and issue:

 $ audio_async_loopback digital-input-device-name latency-in-microseconds

For example:

 $ audio_async_loopback alsa_input.pci-0000_04_00.0.iec958-stereo 12500

To find out your digital-input-device-name, use command:

 $ pacmd list-sources | grep 'name:'

Usually the digital input contains  substring. If still unsure, remove grep part from command and check field:

 properties:
    device.description

latency-in-microseconds is a matter of trial and error to determine, depending highly of your hardware speed. You can try to omit this parameter, letting audio_async_loopback to determine the latency automatically. If you hear clicks and cracks, increase the value. If sound is clear but audio is out of sync or delayed, decrease the value. You can also do a fine-tuning of different buffers in  before building the package but this should not be necessary.

Author also recommends setting input volume to 100% (you can do it in your favorite PulseAudio mixer) and setting PulseAudio to work with 48kHz sampling rate for this tool to function correctly.

To set the sampling rate, edit  and change line:

 default-sample-rate = 44100

to:

 default-sample-rate = 48000

To apply changes, restart .

## PulseAudio as a minimal unintrusive dumb pipe to ALSA
Some people do not want to run PulseAudio all the time for various reasons. This example will turn the full fledged audio server into an unobtrusive dumb pipe to ALSA devices that automatically starts and stops itself when done, allowing applications that requires PulseAudio to fully function while not touching any ALSA setting nor setting itself as the default ALSA device.

This configuration tells native PulseAudio clients to autospawn the daemon when they need it, then the daemon is configured to autoexit as soon as all clients have disconnected. The daemon itself uses a plain simple static configuration that uses your configured  ALSA devices and nothing more. No replacement of ALSA's default, no playing with mixer levels, nothing but record/playback. Also make sure  is not installed so standard ALSA clients do not default to pulse. Since  contains only a configuration file , if it is installed as dependency, one could simply comment all contents in .  functions properly as well as any other ALSA clients. Also make sure common frameworks like Xine, Gstreamer and Phonon are configured to use ALSA: by default if they detect PulseAudio is installed they will try to use it before ALSA.

## Having both speakers and headphones plugged in and switching in software on-the-fly
By design, PulseAudio automatically turns off Line Out when headphones are plugged in and uses Headphone slider instead. You can observe this behavior in . What we want is to have Headphone and Line Out sliders working separately and at the same time. This is extremely useful if you want to remap Realtek's jacks to have, say, Rear Green for headphones and Blue for speakers (with the help of hdajackretask from ).

To achieve this, you should directly edit PulseAudio mixer configuration.

1. We tell PulseAudio that headphones are always plugged in.

Edit: .

Find:

Change  to .

2. By default, Line Out's volume controlled only by Master, and not by Line Out slider itself. We want to merge Line Out with Master.

Add this snippet to the end of the file:

3. We need to completely cut off Line Out when we use headphones.

Edit: .

Add this snippet to the end of the file:

4. Like PulseAudio, ALSA itself cuts off speakers when headphones are plugged in. Run  (in case of Realtek HDA ) and change  to .

5. Restart PulseAudio:

Now you have two separate ports on the same sink in PulseAudio. They mute each other, so you can switch to headphones and this will mute Line Out, and vice versa.
To switch between ports you can use GNOME or Plasma sound mixer, or install appropriate desktop extension.

## Allowing multiple users to share a PulseAudio daemon
Normally each system user runs their own instance of PulseAudio and the instance is only accessible by the user running it. This is a security measure which prevents other users from accessing potentially sensitive audio channels such as voice calls. However, there are situations in which it is desirable to isolate an application by running it as a separate user. For example, one may wish to run a web browser as a different user while still being able to listen to audio from the browser while using the primary user account. Another use is to share a Bluetooth headset among multiple system users.

This can be achieved by creating a UNIX socket to allow other users to access the primary user's PulseAudio daemon. With this setup, the primary user account runs the PulseAudio daemon and the other user accounts connect to it and share it. Note that the following assumes that the environment variable  points to the default location . If this is not the case, replace  with the correct path in the examples below.

## Primary user setup
The primary user should add the following directive to create a UNIX socket and accept connections from other users:

Note that this will allow all users on the system to access the primary user's PulseAudio server and thus all audio data. A more secure solution is to create a custom user group for shared audio and limit the socket to it. For example, to allow only users in the group  to access the socket, change the line to

Since the PulseAudio server reads  directly, this will not work if the secondary user is chrooted; in this case, use cookie files for authentication as described below.

After adding the line, start the PulseAudio daemon on the primary user's account.

## Secondary user setup
The secondary user should add the following line to :

where  is the path to the UNIX socket set in the primary user's  file above. If the primary user has restricted the socket to a specific system group, the secondary user must be added to it.

If the socket is not restricted to a specific system group and  is not used, the secondary user will also need to copy the primary user's PulseAudio daemon cookie () to  in their configuration directory. Alternatively, the primary user can copy the cookie to a location accessible by the intended system users (e.g. ) and the secondary user can access it by adding the following line to the client configuration file:

The secondary user should now have full access to the primary user's PulseAudio daemon and all audio should be accessible to bother users. To grant access to more users, simply repeat the setup for the secondary user on each user account.

## Alternative setup
If there is no primary user to reliably run the shared PulseAudio daemon, the following script can be used by all users in a group ( in this example) to check if a shared server is already running and launch one if not (requires ).

{{hc|1=pulseaudio-shared|2=
#!/usr/bin/bash
set -eu

# The group with access to the shared PulseAudio daemon.
PA_GROUP=sharepulse

# The shared directory.
PA_DIR=/tmp/sharepulse

# Restrict access to users outside of the group.
umask 007

# Create a group-restricted common directory for the socket and cookie if missing.
if  ! -e $PA_DIR
then
  /usr/bin/mkdir -p -- "$PA_DIR"
  /usr/bin/chgrp -- "$PA_GROUP" "$PA_DIR"
  /usr/bin/chmod -- g+s "$PA_DIR"
fi

function start_daemon()
{

  # Only start the daemon if one is not already running.
  if  ! -e $PA_DIR/socket
  then
    echo "Attempting to (re)start the PulseAudio daemon."

    # Create a new random common cookie.
    /usr/bin/dd if=/dev/urandom of="$PA_DIR/cookie" bs=256 count=1

    # Copy it to the configuration directory of the user running the daemon.
    /usr/bin/cp -- "$PA_DIR/cookie" "${XDG_CONFIG_HOME:-$HOME/.config}/pulse/cookie"

    # Start the daemon.
    /usr/bin/pulseaudio "$@" || true

    # Kill the daemon if it is not the owner of the socket.
    if  ! -O $PA_DIR/socket
    then
      /usr/bin/pulseaudio --check && /usr/bin/pulseaudio -k
    fi
  fi
}

# Restart the daemon when necessary.
while true
do
  # Wait for the socket to be deleted when a running daemon is killed. If the
  # socket does not exist then this will be skipped.
  inotifywait -e delete_self "$PA_DIR/socket" || true
  start_daemon
done
}}

Each user will need to add the following lines to their PulseAudio configuration files to configure the daemon and clients to use the shared socket and cookie:

pulseaudio-shared should be run by each user when logging in (e.g. via their Bash profile or their desktop environment's autostart file) to start the daemon when needed. Any arguments passed to the script will be passed through to the PulseAudio daemon. When any shared daemon is stopped,  pulseaudio-shared will automatically restart as the current user and all other users should reconnect to the new daemon automatically.

## Troubleshooting
## No sound when switching TTY
If the sound stops when switching between users on different TTYs or desktop environments () then the users likely do not have access to the sound hardware when their TTY session is not selected. This can be fixed by adding the users to the  group; see Users and groups#Pre-systemd groups.

## Mixing additional audio into the microphone's audio
Using a setup of null sinks and loopbacks you can mix arbitrary applications' audio output into your microphone's audio, for example to play sound effects or music on voice chat applications.

The setup suggested here will also play your sound effects back to you and use PulseAudio echo cancellation to prevent the effects from feeding back into your microphone.

## PulseAudio management with pulse-autoconf
As of August 2020 there is , a PulseAudio server dynamic configuration daemon that supports this setup with its 'EchoCancellationWithSourcesMix' preset and that comes with further benefits, such as dynamically reacting to changes in the PulseAudio server, for example when a headset or a webcam is plugged in or unplugged.

If  does not work out for your use case, read on for the manual way.

## PulseAudio configuration
Symbology: , {{ic|{Audio source}}}, , {{ic|{m} = Monitor of audio sink}}, {{ic|{}* = Fallback (default) source}},

 {Microphone}
     ||
 {src_ec} -----------------> -----> (Voice chat)
               Loopback            ^                                |
                                   | Loopback                       |
                                   |                                v
 (Soundboard) ---------> [sink_fx{m} -----------------------> Loopback             ||
                                                               [Speakers
; {src_ec}, : Echo cancellation "clones" of the microphone and speakers
; [sink_fx
: Virtual sink into which the sound effects are played
; : Virtual sink where the microphone and the sound effects are mixed together
; {src_main}
: Remap of "Monitor of sink_mix", to work around applications that do not allow recording from monitor sources

## Applications configuration
The applications providing the sound effects must

* Output to "sink_fx"

All other applications, including the voice chat, must

* Record audio from "src_main"
* Output to "sink_main"

Accordingly, these devices will be set as defaults. Controlling which application uses which audio source/sink can usually be done in the  graphical PulseAudio control panel.

For some applications changing their sources or sinks in  has no effect. In this case you can typically select the source or sink in the applications' audio settings.

No application whatsoever must record from, or output to, the "real" microphone or speakers, as this would bypass the echo cancellation.

Any echo cancellation or other audio processing provided by the voice chat application should be disabled – PulseAudio is doing this already, and as the application is not aware of the sound effects being played on the speakers, it will likely be ineffective in filtering them from the microphone anyway.

## Setup steps
# Connect your microphone and headphones and make sure PulseAudio is configured correctly for their use, for example in the Configuration tab in
# First time only:
## Save the template script below to an executable file of your choice
## Find the names of your microphone and headphones with  and , respectively
## In the script, replace the values of  and  with the names of your microphone/headphones
# Run the script
# Run your voice chat application and make it record audio from "src_main" and output audio to "sink_main"
# Run your sound effects application(s) and make them play to "sink_fx"

As for applications that can play sound effects,  has been found to work quite well.
It however needs to be closed and re-opened when PulseAudio is restarted.

## Teardown
The changes that the script makes to the running PulseAudio server are not permanent and will be lost when PulseAudio terminates.

To ditch the custom configuration, just restart PulseAudio, e.g. with . (PulseAudio is socket-activated and will automatically start on demand.)

## Template script
This script has been inspired by https://askubuntu.com/a/915064 , for more in-depth information also see that post's author's [https://github.com/toadjaune/pulseaudio-config pulseaudio-config GitHub repository.

Using  to work around applications that do not accept a monitor as source is taken from https://unix.stackexchange.com/a/608482 .

## Invert phase of one audio channel
This is useful for compensating when one of your speakers is wired with the wrong polarity. To test if this is needed, see Adapted from a more general example of [https://askubuntu.com/a/194345 Assigning a LADSPA filter to a single audio channel.
Requires .

## Renaming devices
Sound devices will sometimes have confusing names assigned to them by default. Names like "CM106 Like Sound Device" are not very descriptive. This can be easily fixed and it works for both PulseAudio sources and sinks.

The easiest method is to add the following lines to the end of the  file.

To update a source name:

 update-source-proplist device_name device.description="new_name"

And to update a sink name:

 update-sink-proplist device_name device.description="new_name"

The device name can be queried using the command  for sources, or  for sinks.

This configuration can also be persisted on a per-user basis:

The default PulseAudio configuration needs to be included, otherwise the daemon will not start.

## Use dynamic default sink with modules
If you load a module that uses for example , you can set a "dynamic" default sink with .

This way the active chosen default sink will be used.
If you change the default sink, the new default sink will be used on command reload/re-run or PulseAudio restart.
