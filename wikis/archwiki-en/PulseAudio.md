# PulseAudio

PulseAudio is a general purpose sound server intended to run as a middleware between your applications and your hardware devices, either using Advanced Linux Sound Architecture (ALSA) or Open Sound System (OSS). It also offers easy network streaming across local devices using Avahi if enabled. While its main purpose is to ease audio configuration, its modular design allows more advanced users to configure the daemon precisely to best suit their needs.

## Installation
Install the  package.

Some PulseAudio modules are not included in the main package and must be installed separately if needed:

*  for PulseAudio to manage ALSA as well, see #ALSA
*  for Bluetooth support (BlueZ), see the Bluetooth headset page
*  for equalizer sink (qpaeq)
*  for JACK sink, source and jackdbus detection
*  for infrared volume control with LIRC
*  for Zeroconf (Avahi/DNS-SD) support

## Front-ends
There are a number of front-ends available for controlling the PulseAudio daemon:

## Console
*
*
*
*
*
*
*
*

## Graphical
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*

## Configuration
By default, PulseAudio is configured to automatically detect all sound cards and manage them. It takes control of all detected ALSA devices and redirects all audio streams to itself, making the PulseAudio daemon the central configuration point. The daemon should work mostly out of the box, only requiring a few minor tweaks.

While PulseAudio usually runs fine out of the box and requires only minimal configuration, advanced users can change almost every aspect of the daemon by either altering the default configuration file to disable modules or writing your own from scratch.

PulseAudio runs as a server daemon that can run either system-wide or on per-user basis using a client/server architecture. The daemon by itself does nothing without its modules except to provide an API and host dynamically loaded modules. The audio routing and processing tasks are all handled by various modules, including PulseAudio's native protocol itself (provided by module-native-protocol-unix). Clients reach the server through one of many protocol modules that will accept audio from external sources, route it through PulseAudio and eventually have it go out through a final other module. The output module does not have to be an actual sound output: it can dump the stream into a file, stream it to a broadcasting server such as Icecast, or even just discard it.

You can find a detailed list of all available modules at PulseAudio Loadable Modules. To enable them you can just add a line  to .

## Configuration files
PulseAudio will first look for configuration files in the home directory , and if they are not found, the system-wide configuration from  will be applied.

## daemon.conf
This is the main configuration file to configure the daemon itself. It defines base settings like the default sample rates used by modules, resampling methods, realtime scheduling and various other settings related to the server process. These can not be changed at runtime without restarting the PulseAudio daemon. The defaults are sensible for most users, see the  man page for additional information. Boolean options accepts any of these: , ,  and  as well as , ,  and .

{| class="wikitable"
! Option || Description
|-
| daemonize || Controls whether the server will daemonize itself and return. Set to  when debugging so you can see the debugging information on the terminal.
|-
| resample-method || Which resampler to use when audio with incompatible sample rates needs to be passed between modules (e.g. playback of 96kHz audio on hardware which only supports 48kHz). The available resamplers can be listed with . Choose the best tradeoff between CPU usage and audio quality for the present use-case.
|-
| avoid-resampling || With , PulseAudio automatically configures the hardware to the sample rate which the application uses, if the hardware supports this sample rate (needs PA 11 or higher)

|-
| enable-remixing || When the input and output have a different channel count (for example, outputting a 6 channel movie into a stereo sink), PulseAudio can either remix all the channels (default, ) or just trivially map the channels by their name (left goes to left, right to right, all others ignored) when .
|-
| system-instance || If set to , run the daemon as a system-wide instance. Highly discouraged as it can introduce security issues. Useful on Multiseat systems, or headless systems that have no real local users. Defaults to .
|-
| flat-volumes || If set to , scales the device-volume with the volume of the "loudest" application. For example, raising the VoIP call volume will raise the hardware volume and adjust the music-player volume so it stays where it was, without having to lower the volume of the music-player manually. Defaults to .
|-
| realtime-scheduling || If your kernel supports realtime scheduling (i.e. realtime kernel), set this to  to ensure PulseAudio can deliver low-latency glitch-free playback. You can adjust  as well to have it use the correct priority, especially when JACK is also running on the system.
|-
| nice-level || Since PulseAudio runs in userspace and involves inter-process communication, audio can be subject to dropouts if the daemon does not have enough CPU time to process the audio. The default usually is enough, but can be tweaked to give PulseAudio the wanted priority over (or below) other applications.
|-
| exit-idle-time || If you want to run PulseAudio only when needed and use ALSA otherwise, you can set a delay in seconds after which the daemon will automatically shutdown after all clients are disconnected. Set it to -1 to disable this feature.
|-
| log-level || When debugging, you may want to increase the logging level of the daemon to see exactly why a specific module fails to load. High logging levels will sometimes print useful information such as detected minimum latency for the system, which can then be used to tweak  and .
|-
| default-sample-format || This usually does not need to be changed, but if your sound card's native format is different, performance and quality can be improved by setting the right format here.
|-
| default-sample-rate || The default sample rate used by PulseAudio unless overriden at module level. Change this if your sound card does not support 44100Hz or if you wish to upsample all audio. See previous note about CPU usage.
|-
| alternate-sample-rate || To fix a common limitation where movies at 48000Hz were needlessly downsampled to 44100Hz, some modules support changing their sample rate dynamically to avoid resampling when possible. See manual for more in-depth information. This usually does not need to be changed.
|-
| default-sample-channels || The default number of channels when not specified. Usually do not need any change as you can configure more channels on per-module basis.
|-
| default-fragments || Audio samples are split into multiple fragments of  each. The larger the buffer is, the less likely audio will skip when the system is overloaded. On the downside this will increase the overall latency. Increase this value if you have issues.
|-
| default-fragment-size-msec || The size in milliseconds of each fragment. This is the amount of data that will be processed at once by the daemon.
|}

## default.pa
This file is a startup script and is used to configure modules. It is actually parsed and read after the daemon has finished initializing and additional commands can be sent at runtime using  or . The startup script can also be provided on the command line by starting PulseAudio in a terminal using . This will make the daemon load the CLI module and will accept the configuration directly from the command line, and output resulting information or error messages on the same terminal. This can be useful when debugging the daemon or just to test various modules before setting them permanently on disk. The manual page is quite self-explanatory, consult  for the details of the syntax.

The default configuration also loads  to apply settings specified by .

## system.pa
This file is a startup script used in place of  when PulseAudio is running in system-wide mode.

## client.conf
This is the configuration file read by every PulseAudio client application. It is used to configure runtime options for individual clients. It can be used to set and configure the default sink and source statically as well as allowing (or disallowing) clients to automatically start the server if not currently running. If autospawn is enabled, clients will automatically start PulseAudio if it is not already running when a client attempts to connect to it. This can be useful if you do not want PulseAudio to always be running to conserve system resources. Otherwise, you really should have it start with your X11 session.

## Configuration command
The main command to configure a server during runtime is . Run  for a list options, or just run  to enter the shell interactive mode and  to exit. All modifications will immediately be applied.

Once your new settings have been tested and meet your needs, edit the  accordingly to make the change persistent. See PulseAudio/Examples for some basic settings.

It is important to understand that the "sources" (processes, capture devices) and "sinks" (sound cards, servers, other processes) accessible and selectable through PulseAudio depend upon the current hardware "Profile" selected. These "Profiles" are those ALSA "pcms" listed by the command , and more specifically by the command , which will include a line "index:", a list beginning "profiles:", and a line "active profile: " in the output, among other things. "Profiles" correspond to different card input/output configurations, notably the number of available input/output channels.

The "active profile" can be set with the command , with no comma separating INDEX and PROFILE, where INDEX is just the number on the line "index:" and a PROFILE name is everything shown from the beginning of any line under "profiles:" to just before the colon and first space, as shown by the command . For instance, .

It may be easier to select a "profile" with a graphical tool like , under the Configuration tab, or KDE System Settings, under the Sound tab. Each audio "card", which are those devices listed by the command , or again by the command , will have its own selectable "profile". When a "profile" has been selected, the then available "sources" and "sinks" can be seen by using the commands  and . Note that the "index" of the available sources and sinks will change each time a card profile is changed.

The selected "Profile" can be an issue for some applications, especially the Adobe Flash players, typically  and . Often, these Flash players will only work when one of the Stereo profiles is selected, and otherwise, will play video with no sound, or will simply "crash". When all else fails, you might try selecting a different profile.

Of course, when configuring some variation of Surround Sound in PulseAudio, the appropriate Surround profile will have to be selected, before Surround Sound will work, or in order to do things like remap the speaker channels.

If the only profile you seem to have is "HiFi", this means that you are using ALSA Use Case Manager profiles instead of PulseAudio profiles. See PulseAudio/Examples#Disabling UCM/"HiFi" for information on how to get back to using PulseAudio profiles.

## Connection and authentication
Since PulseAudio runs as a daemon as the current user, clients needs to know where to find the daemon socket to connect to it as well as a shared random cookie file clients use to authenticate with it. By default, clients should be able to locate the daemon without problem using environment variables, X11 root window properties, the  option in  and finally by trying the default location  (typically ). However, if you have clients that needs to access PulseAudio outside of your X11 session like mpd running as a different user, you will need to tell it how to connect to your PulseAudio instance. See PulseAudio/Examples#Allowing multiple users to share a PulseAudio daemon for a complete example. An authentication cookie containing random bytes is enabled by default to ensure audio does not leak from one user to another on a multi-user system. If you already control who can access the server using user/group permissions, you can disable the cookie by passing  to .

## Environment variables
These two variables are the important ones in order for libpulse clients to locate PulseAudio if you moved its socket to somewhere else. See  for more details and other useful environment variables clients will read.

{| class="wikitable"
! Variable || Definition
|-
|  || Defines where the server is. It takes a protocol prefix like  or  followed by the path or IP of the server. Example: .
|-
|  || Point this to the location of a file that contains the random cookie generated by PulseAudio. This file will be read by clients and its content sent to the server, thus the file has to be readable by all audio clients. It does not need to be the same file, as long as its content matches the one the daemon uses.
|}

## X11 properties
When using SSH X11 forwarding (i.e. when the  and  environment variables are present), libpulse clients also use window properties on the root window of the X11 server to help find the daemon.

X11 properties can be queried using , or with  to read pulse-specific properties.  can also be used to update the properties from environment variables (, or  to remove them entirely). If possible, it is recommended to let PulseAudio do it by itself using the  module or the  command.

{| class="wikitable"
! Variable || Definition
|-
|  || String value ( or ), works the same as the environment variable of the same name.
|-
|  || String value that contains the hexadecimal representation of the authentication cookie.
|}

## Running
PulseAudio on Arch has  enabled by default for the systemd/User instance. This means that PulseAudio will automatically start when needed.

For more information, see PulseAudio: Running.

## Stopping
Stop the  and  user units.

## Back-end configuration
## ALSA
If you have applications that do not support PulseAudio explicitly but rely on ALSA, these applications will try to access the sound card directly via ALSA and will therefore bypass PulseAudio. PulseAudio will thus not have access to the sound card any more. As a result, all applications relying on PulseAudio will not be working any more, leading to this issue. To prevent this, you will need to install the  package. It contains the necessary  for configuring ALSA to use PulseAudio. Also make sure that  does not exist, as it would override the  file.

Also install  and  if you run a x86_64 system and want to have sound for 32-bit multilib programs like Wine and Steam.

To prevent applications from using OSS emulation and bypassing PulseAudio (thereby preventing other applications from playing sound), make sure the module  is not being loaded at boot. If it is currently loaded (), disable it by executing:
 # rmmod snd_pcm_oss

## Enable DTS via ALSA
To enable PulseAudio DTS (Digital Theater System) via ALSA install  package and enable it:

Finally restart PulseAudio. If experience volume issues with your DTS device and/or PulseAudio, you may fix it by looking for more setting option at dcaenc's GitLab.

## Expose PulseAudio sources, sinks and mixers to ALSA
Although  contains the necessary configuration file to allow ALSA applications to use PulseAudio's default device, ALSA's  plugin is more versatile than that:

{{hc|~/.asoundrc (or /etc/asound.conf)|2=
# Create an alsa input/output using specific PulseAudio sources/sinks
pcm.pulse-example1 {
    type pulse
    device "my-combined-sink" # name of a source or sink
    fallback "pulse-example2" # if combined not available
}

pcm.pulse-example2 {
    type pulse
    device "other-sound-card" # name of a source or sink
    # example: device "alsa_output.pci-0000_00_1b.0.analog-stereo"
}

# Create an ALSA mixer using specific PulseAudio sources/sinks
# these can be tested with "alsamixer -D pulse-example3"
ctl.pulse-example3 {
    type pulse
    device "my-output" # name of source or sink to control

    # example: always control the laptop speakers:
    # device "alsa_output.pci-0000_00_1b.0.analog-stereo"
    fallback "pulse-example4" # supports fallback too
}

# Mixers also can control a specific source and sink, separately:
ctl.pulse-example4 {
    type pulse
    sink "my-usb-headphones"
    source "my-internal-mic"

    # example: output to HDMI, record using internal
    sink "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra1"
    source "alsa_input.pci-0000_00_1b.0.analog-stereo"
}

# These can override the default mixer (example: for pnmixer integration)
ctl.!default {
    type pulse
    sink "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra1"
    source "alsa_input.pci-0000_00_1b.0.analog-stereo"
}
}}

The source code can be read to know all available options.

## ALSA/dmix without grabbing hardware device
You may want to use ALSA directly in most of your applications while still being able to use applications which require PulseAudio at the same time. The following steps allow you to make PulseAudio use dmix instead of grabbing ALSA hardware device.

* Remove the  package, which provides compatibility layer between ALSA applications and PulseAudio. After this your ALSA applications will use ALSA directly without being hooked by PulseAudio.

* In , comment or delete the  line and add the following lines:

* Optional: If you use  you may want to control ALSA volume instead of PulseAudio volume: set  as an environment variable.

* Now, reboot your computer and try running ALSA and PulseAudio applications at the same time. They both should produce sound simultaneously.
:Use  to control PulseAudio volume if needed.

## OSS
There are multiple ways of making OSS-only programs output to PulseAudio:

## ossp
Install the  package and start .

## padsp wrapper
Programs using OSS can work with PulseAudio by starting it with  (included with ):

 $ padsp OSSprogram

A few examples:

 $ padsp aumix
 $ padsp sox foo.wav -t ossdsp /dev/dsp

You can also add a custom wrapper script like this:

Make sure  comes before  in your .

## GStreamer
 provides the pulseaudio plugin for applications using GStreamer.

## OpenAL
OpenAL Soft should use PulseAudio by default, but can be explicitly configured to do so:

## libao
Edit the libao configuration file:

Be sure to remove the  option of the  driver or adjust it to specify a specific PulseAudio sink name or number.

## Audio post-processing
## PulseEffects
PulseEffects is a GTK advanced utility for applying several audio effects (e.g. Noise reduction, Equalizer etc.) to audio input and output.

You may need to also install its optional dependency  in order to get plugins to work. If PulseEffects plugins are greyed out after installing plugins, trying to start the daemon produces an error, or no devices are shown in the Settings > PulseAudio tab, consider clearing the cache as shown in A collection of PulseEffects presets can be found in [https://github.com/wwmm/easyeffects/wiki/Community-presets community presets.

## Equalization
If you want to use a different equalizer rather that the one integrated in #PulseEffects, there are the following options.

## LADSPA module
Install , an equalizer based on LADSPA . Launch  GUI and tweak the parameters to match your expectations.

## Integrated module
PulseAudio has an integrated 10-band equalizer system. In order to use it, install  and load :

 $ pactl load-module module-equalizer-sink

Also load  if your configuration does not load it by default.

To start the GUI, run .

To load the equalizer module on every boot, create a .pa file in  or edit  and add the following lines:

 ### Load the integrated PulseAudio equalizer
 load-module module-equalizer-sink

## Dynamic Range Compression
Dynamic range compression can be done with #PulseEffects, however PulseEffects might introduce much overhead and latency to audio stream, so if you only need a compression effect and a minor load on the system, other options are available using a module-ladspa-sink.

## Steve Harris plugin
Steve Harris LADSPA is a set of plugins containing various compression modules. Install  and edit the configuration as the following:

You have to specify your card sink name, get it from . In order to apply the changes, stop and restart PulseAudio. The above configuration has empty control options using the default values.

To tweak the module with custom control parameters, fill them respecting the right order.

{| class="wikitable"
! Control option || Description
|-
| RMS/peak (0/1) || The blanace between the RMS and peak envelope followers. RMS is generally better for subtle, musical compression and peak is better for heavier, fast compression and percussion.
|-
| Attack time (ms) || The attack time in milliseconds.
|-
| Release time (ms) || The release time in milliseconds.
|-
| Threshold level (dB) || The point at which the compressor will start to kick in.
|-
| Ratio (1:n) || The gain reduction ratio used when the signal level exceeds the threshold. 1 means no compression; higher values stronger compression.
|-
| Knee radius (dB) || The distance from the threshold where the knee curve starts.
|-
| Makeup gain (dB) || Controls the gain of the makeup input signal in decibels.
|}

Other plugins can be found in Steve Harris' LADSPA Plugin Documentation.

## Calf plugin
For a more professional compressor, you can use the one developed by Calf Studio Gear. Install  and edit the configuration as the following

The plugin has 11 control options. If you want to insert custom values, read the following table and do not forget to specify them in the right order.

{| class="wikitable"
! Control option        || Default     || Min             || Max     || Type       || Info
|-
| Bypass        || 0           || 0               || 1       || Bool       ||
|-
| Level in      || 1           || 0.015625        || 64      || Float db   ||
|-
| Threshold     || 0.125       || 0.000976563     || 1       || Float dbFs || For example, to set -18 db, the right value is 10^(-18/20) = 0.158
|-
| Ratio         || 2           || 1               || 20      || Float      ||
|-
| Attack        || 20          || 0.01            || 2000    || Float ms   ||
|-
| Release       || 250         || 0.01            || 2000    || Float ms   ||
|-
| Makeup        || 1           || 1               || 64      || Float db   ||
|-
| Knee          || 2.828427125 || 1               || 8       || Float db   ||
|-
| RMS/Peak      || 0           || 0               || 1       || Bool       || 0 = RMS; 1 = Peak
|-
| Stereo Link   || 0           || 0               || 1       || Bool       || 0 = Average; 1 = Max
|-
| Mix           || 1           || 0               || 1       || Float      || Percentage
|-
| colspan="6" | To understand the meaning of every single option, read the Calf Compressor Documentation.
|}

## Microphone echo/noise cancellation
Arch does not load the PulseAudio echo-cancellation module by default, therefore, we have to add it in . First you can test if the module is present with  and entering . If you cannot find a line showing  you have to create:

then restart PulseAudio:

 $ pulseaudio -k
 $ pulseaudio --start

and check if the module is activated by starting pavucontrol. Under Recording, the input device should show Echo-Cancel Source Stream from.

Turning on  in the  can also significantly reduce background noise if you have more than one microphone (which is common on many new laptops). However, beamforming requires specifying your  (see below).

If you want existing streams to be automatically moved to the new sink and source, you have to load the module-switch-on-connect with  before.

## Possible 'aec_args' for 'aec_method=webrtc'
Here is a list of possible 'aec_args' for 'aec_method=webrtc' with their default values *  - Analog AGC - 'Automatic Gain Control' done over changing the volume directly - Will most likely lead to distortions.
*  - Digital AGC - 'Automatic Gain Control' done in post processing (higher CPU load).
*  - Allow enabling of the webrtc experimental AGC mechanism.
*  - Initial volume when using AGC - Possible values 0-255 - A too low initial volume may prevent the AGC algorithm from ever raising the volume high enough [https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/9.0/.
*  - ?
*  - Noise suppression.
*  - VAD - Voice activity detection.
*  - The extended filter is more complex and less sensitive to incorrect delay reporting from the hardware than the regular filter. The extended filter mode is disabled by default, because it seemed produce worse results during double-talk Enable this option if your microphone or speaker has a larger latency, for example, if you use a wireless microphone or some HDMI TVs as speaker.
*  - Some bits for webrtc intelligibility enhancer.
*  - Drift compensation to allow echo cancellation between different devices (such as speakers on your laptop and the microphone on your USB webcam). - only possible with "mobile=0".
*  - This can significantly reduce background noise. See [https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#aec_args**  - Only with "beamforming=1".
**  - Only with "beamforming=1". Note: If the module does not want to load with this argument, set azimuth (a) to the desired value, but set elevation (e) and radius (r) to 0.
*  - ?
**  - Possible Values "quiet-earpiece-or-headset,earpiece,loud-earpiece,speakerphone,loud-speakerphone" - only valid with "mobile=1".
**  - ? - only valid with "mobile=1".

## Disable audio post processing in certain applications
If you are using the module-echo-cancel, you probably do not want other applications to do additional audio post processing. Here is a list for disabling audio post processing in following applications:

* Mumble:
*# Configure > Settings > Audio Input
*# Echo Cancellation: select Disabled
*# Noise suppression: select Disabled
*# Max. Amplification: set slider to 1.00
* TeamSpeak:
*# Tools -> Options -> Capture
*# Uncheck: 'Typing attenuation', 'Remove background noise', 'Echo cancellation' and 'Echo reduction (Ducking)'
* Firefox: see Firefox tweaks#Disable WebRTC audio post processing
* Steam:
*# Settings > Voice > Advanced Options > Show
*# Disable the following sliders: Echo cancellation, Noise cancellation, Automatic volume/gain control

## Script for reloading module-echo-cancel
Since the module-echo-cancel is not always needed, or must be reloaded if the source_master or sink_master has changed, it is nice to have a easy way to load or reload the module-echo-cancel.

Create the following script and make it executable:

To run the script easily from the graphical environment, you can create a desktop launcher for it.

## Recurrent neural network noise suppression (RNNoise)
Installing the package  will allow real-time noise suppression based on RNNoise: Learning Noise Suppression [https://jmvalin.ca/demo/rnnoise/. Configuration details can be found on the projects Github site An alternative is  which is built on top of RNNoise. There is not only input noise cancellation but also an output.

## Applications
## QEMU
Refer to QEMU#Creating an audio backend for a detailed guide on how to configure PulseAudio within QEMU.

## AlsaMixer.app
Install  and make  dockapp for the  use PulseAudio, e.g.:

 $ AlsaMixer.app --device pulse

Here is a two examples where the first one is for ALSA and the other one is for PulseAudio. You can run multiple instances of it. Use the  option to choose which of the control buttons to bind to the mouse wheel.

 $ AlsaMixer.app -3 Mic -1 Master -2 PCM --card 0 -w 1
 $ AlsaMixer.app --device pulse -1 Capture -2 Master -w 2

See #ALSA for details.

## XMMS2
Make it switch to PulseAudio output:

 $ xmms2 server config output.plugin pulse

and to ALSA:

 $ xmms2 server config output.plugin alsa

To make XMMS2 use a different output sink, e.g.:

 $ xmms2 server config pulse.sink alsa_output.pci-0000_04_01.0.analog-stereo.monitor

See also [https://github.com/xmms2/wiki/wiki/Using-the-application the official guide.

## KDE Plasma Workspaces and Qt
PulseAudio will automatically be used by KDE / Qt applications. It is supported by default in the KDE sound mixer. For more information see the KDE page in the PulseAudio wiki.

If the phonon-gstreamer backend is used for Phonon, GStreamer should also be configured as described in #GStreamer.

## Audacious
Audacious natively supports PulseAudio. In order to use it, set File > Settings > Audio > Output plugin > PulseAudio Output.

## Music Player Daemon (MPD)
Configure MPD to use PulseAudio. See also Music Player Daemon/Tips and tricks#PulseAudio.

## MPlayer
MPlayer natively supports PulseAudio output with the  option. It can also be configured to default to PulseAudio output, in  for per-user, or  for system-wide:

## mpv
mpv supports PulseAudio same as written for #MPlayer. Configuration in  per-user, or  system-wide.

## guvcview
 when using the PulseAudio input from a Webcam may have the audio input suspended resulting in no audio being recorded.  You can check this by executing:

 $ pactl list sources

If the audio source is "suspended" then create the folowing .pa file:

And then either restarting PulseAudio or your computer will only idle the input source instead of suspending it.  guvcview will then correctly record audio from the device.

## Networked audio
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

## Starting system-wide on boot
The PulseAudio daemon normally starts as a user service when a user logs in and attempts to play some sort of audio. For running a dedicated PulseAudio server accepting client connections over TCP, the daemon must be started on boot as a system service.  Note that in most desktop use cases, system mode likely is not the right choice.

To run PulseAudio in a system mode, first we need to set up users and groups needed by system-wide PulseAudio server instance # Add user . PulseAudio daemon switches to this user after starting.
# Optionally add user  to the  group, if you have it (BlueZ) and want PulseAudio to use Bluetooth.
# Add group . This group is used by PulseAudio server for access control.
# Add users to  group, if you want them to have access to the system-wide PulseAudio instance.

Create the service  in  containing the following:

Then enable  at the system level. You will also need to disable the user-level PulseAudio service across the whole system by masking the  with the  flag.

This is necessary even if you are accessing the system over SSH, to make sure the user-level PulseAudio service will never start.

When PulseAudio starts in the system mode,  is used instead of , so be sure to put any necessary settings in .

## Selecting the server
For a single shell or command you can set the  environment variable to the host name or IP address of the desired PulseAudio server:

 $ env PULSE_SERVER=server-hostname-or-ip mplayer test.mp3

Alternatively, you can create or modify  or  to set a default-server persistently:

 default-server = server-hostname-or-ip

It is also possible to specify multiple servers separated by spaces which are subsequently tried by PulseAudio[https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/ServerStrings/:

 default-server = server1 backup

## Tips and tricks
## Keyboard volume control
Map the following commands to your volume keys: ,  and .

First find out which sink corresponds to the audio output you would like to control.
To list available sinks:

 $ pactl list sinks short

Suppose sink 0 is to be used, to raise the volume:

 $ sh -c "pactl set-sink-mute 0 false ; pactl set-sink-volume 0 +5%"

To lower the volume:

 $ sh -c "pactl set-sink-mute 0 false ; pactl set-sink-volume 0 -5%"

To mute/unmute the volume:

 $ pactl set-sink-mute 0 toggle

To mute/unmute the microphone:

 $ pactl set-source-mute 1 toggle

## Play sound from a non-interactive shell (systemd service, cron)
Replace  with the user running PulseAudio:

 # machinectl shell --uid=user .host /usr/bin/paplay /usr/share/sounds/freedesktop/stereo/complete.oga

## X11 Bell Events
To get PulseAudio to handle X11 bell events, run the following commands after the X11 session has been started:

 $ pactl upload-sample /usr/share/sounds/freedesktop/stereo/bell.oga bell-window-system
 $ pactl load-module module-x11-bell display=$DISPLAY

Or use configuration files  or :

To adjust the volume of the X11 bell, run the following command:

 $ xset b 100

100 is a percentage. This requires the  package. See Autostarting for a way to run these commands automatically when the X11 session is started.

## Switch on connect
The switch-on-connect module switches the output sound to new devices when connected. For example, if you plug in a USB headset, the output will be switched to that. If you unplug it, the output will be set back to the last device.

This module is disabled by default for being too aggressive, but can be enabled by adding the line  to your .

## Script for switching output ports
Some sound cards present the option of multiple analog outputs, being switchable through using PulseAudio ports. But switching manually can become a chore, so you can automate this with the pactl command.

List available ports:

Current port can be obtained through:

 $ LC_ALL=C.UTF-8 pactl list sinks | grep "Active Port" | cut -d ' ' -f 3-

Switch the active port:

 $ pactl set-sink-port sink-index port

This process can be automated through a simple script. This script then can be given a shortcut by the user:

This script is intended to swap between two ports. First checking the current port then swapping it. Users might need to change the sink index number and the port names to fit their machine.

## Disable muting media on entering voice call (module-role-cork)
When entering a voice call (e.g. in Microsoft Teams, maybe others too) any media applications might be muted. To disable this behaviour you can simply disable this module in PulseAudio configuration:

## Advanced configuration and use cases
See PulseAudio/Examples.

## Troubleshooting
See PulseAudio/Troubleshooting.
