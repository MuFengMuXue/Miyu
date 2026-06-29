# JACK Audio Connection Kit

From Wikipedia:JACK Audio Connection Kit:
:JACK Audio Connection Kit (or JACK; a recursive acronym) is a professional sound server daemon that provides real-time, low-latency connections for both audio and MIDI data between applications that implement its API.

## Installation
There are three different implementations of the JACK API: ,  and . For an overview, refer to #Comparison of JACK implementations.

Install one of the above packages. For 32-bit application support, also install the  or  package (respectively) from the multilib repository.

For the official JACK example-clients and tools install .

For an alternative ALSA MIDI support in  install .

For dbus support with  install .

## Configuration
Depending on your use-case and hardware, the system may need further configuration, to allow a JACK implementation to use additional resources or to function properly.

## Latency
The latency of a running JACK instance (i.e. how much time is spent processing one block of audio) is defined by its / ratio.

When looking at  as an example, these parameters are defined by the  and  flags (respectively).

## Realtime scheduling and additional resources
All JACK implementations may make use of elevated realtime scheduling priority, which allows them to make use of the CPU cycles more often than other applications (see e.g.  in ).

The  package provides the  system group, which is permitted elevated  and unlimited  with a sysctl drop-in configuration file and is permitted to alter the system's  file, which may be used by applications to prevent the CPU to use higher C states.

Install the  package and add your user to the  group to be able to use realtime scheduling priority that is higher than the default.

## Realtime kernel and advanced modifications
A realtime kernel (such as  or ) may be used in situations where very low latencies are required. Refer to professional audio for further information and other advanced modifications.

## Starting the audio graph
The different JACK implementations have varying ways of starting the audio graph.

## Jack
Jack1 only supports starting via the  executable or by using one of the graphical frontends, that support starting via the library interface.

## Jack2
Jack2 supports starting via the  executable, the  script (provided by the  package), the  systemd user service (refer to  for configuration documentation) or by using one of the graphical frontends, that support starting via the library or dbus interface.

## Pipewire-jack
Pipewire's JACK implementation does not provide the  executable or dbus integration. The audio graph is started by the  systemd user service.

## Comparison of JACK implementations
The following table lists the current implementations of the JACK API and their differing feature sets.

{| class="wikitable sortable" style="text-align: center;"
! Name !! Maintenance || Language !! SMP support !! Jackd executable !! Dbus integration !! Systemd integration !! Firewire support !! ALSA MIDI support !! Multi soundcard support !! Network support
|-
|  || Inactive || C ||  ||  ||  ||  || ALSA/ || Builtin ||  || netJACK1/ /
|-
|  || Active || C/C++ ||  ||  ||  ||  || ALSA/ || Builtin/  || Builtin/ || netJACK2/ /
|-
|  || Active || C/C++ ||  ||  ||  ||  || ALSA || Builtin || Builtin || /
|-
|}

## Comparison of JACK control GUIs
The following table lists control GUIs for JACK and their differing features and levels of support towards the JACK implementations.

{| class="wikitable sortable" style="text-align: center;"
! Name !! jack1 start/ stop !! jack2 start/ stop !! pipewire-jack start/ stop !! Patchbay !! Save graph connections !!  support
|-
| ||  ||  ||  ||  (Catia) ||  (LADISH via Claudia is unsupported) ||
|-
| ||  ||  ||  ||  ||  ||
|-
| ||  ||  ||  ||  ||  ||
|-
| ||  ||  ||  ||  ||  ||
|-
| ||  ||  ||  ||  ||  ||
|-
| ||  ||  ||  ||  ||  ||
|-
| ||  ||  ||  ||  ||  ||
|}

## Tips and tricks
## Applications for interacting with JACK and its audio graph
*
*
*
*
*
*
*
*

## Using MIDI devices
JACK can handle one soundcard very well, and an arbitrary number of MIDI devices (connected e.g. via USB).
If you start JACK and want to use a MIDI keyboard or a synthesizer or some other pure MIDI device, you have to start JACK with a proper soundcard (one that actually outputs or inputs PCM sound).
As soon you have done that, you can connect the MIDI device. E.g. with QjackCtl (), you click on the connect button and you will find your device listed under JACK-MIDI or ALSA-MIDI, depending on the driver.

For JACK-MIDI, you may want to set the MIDI Driver to seq or raw in QjackCtl Setup > Settings. This should make your MIDI device appear under the MIDI tab. You can also change the name of the client (from a generic "midi_capture_1" to something more descriptive), if you enable Setup > Display > Enable client/port aliases and then Enable client/port aliases editing (rename).

For ALSA-MIDI, make sure to turn on Enable ALSA Sequencer support in QjackCtl Setup > Misc. This will add the ALSA tab in QjackCtl Connect window where your MIDI controller will show up.

For bridging ALSA-MIDI to JACK-MIDI, you may consider using a2jmidid (). The following command will export all available ALSA MIDI ports to JACK MIDI ports:

 $ a2j_control --ehw && a2j_control --start

They will be visible in QjackCtl under the MIDI tab labelled "a2j" client.
You can automate starting of a2jmidid by adding to QjackCtl Setup > Options > Execute script after Startup:

*Q: What is the difference between JACK-MIDI and ALSA-MIDI?
*A: The former has improved timing and sample accurate MIDI event alignment. It extends or may even replace the latter but at this point they both co-exist.

To install some M-Audio MIDI keyboards, you will need the firmware package . Also, the  module has to be available.

See [https://alsa.opensrc.org/USBMidiDevices USBMidiDevices article for more information about specific USB MIDI devices.

## A shell-based example setup
JACK2 can be directly launched with the jackd executable, or controlled with the D-Bus-based jack_control binary. jack_control makes it easy to start and configure JACK2 via a shell script. Note that you must install the  package to use jack_control. For the a2j_control commands you also need  installed (see #Using MIDI devices for more information).

Create a shell script that can be executed at X login:

The above will start a working JACK instance which other programs can then utilize.  Details of each line follow.  When discovering your own best configuration, it is helpful to do trial and error using QjackCtl's GUI with a non-D-Bus JACK2 version.

## Details of the shell-based example setup
 $ jack_control start

Starts JACK if it is not already started.

 $ jack_control ds alsa

Sets JACK to use the ALSA driver set.

 $ jack_control dps device hw:HD2

Sets JACK to use ALSA-compatible sound card named HD2. One can find the names with . Most ALSA tutorials and default configurations use card numbers, but this can get confusing when external MIDI devices are in use; names make it easier.

 $ jack_control dps rate 48000

Sets JACK to use 48000 khz sampling. Happens to work very well with this card. Some cards only do 44100, many will go much higher. The higher you go, the lower your latency, but the better your card and your CPU have to be, and software has to support this as well.

 $ jack_control dps nperiods 2

Sets JACK to use 2 periods. 2 is right for motherboard, PCI, PCI-X, etc.; 3 for USB.

 $ jack_control dps period 64

Sets JACK to use 64 frames per period. Lower is less latency, but the setting in this script gives 2.67 ms latency, which is nicely low without putting too much stress on the particular hardware this example was built for. If a USB sound system were in use it might be good to try 32. Anything less than 3-4 ms should be fine for realtime synthesis and/or FX, 5 ms is the smallest a human being can detect. QjackCtl will tell you how you are doing; at no-load, which means no clients attached, you will want a max of 3-5% CPU usage, and if you cannot get that without xruns (the red numbers which mean the system cannot keep up with the demands), you will have to improve your hardware.

 $ sleep 10

Wait for the above to settle.

 $ a2j_control --ehw && a2j_control --start

Start the ALSA-to-JACK MIDI bridge. Good for mixing in applications which take MIDI input through ALSA but not JACK.

 $ sleep 10

Wait for the above to settle.

 $ qjackctl &

Load QjackCtl. GUI configuration tells it to run in the system tray. It will pick up the JACK session started by D-Bus just fine, and very smoothly too. It maintains the patchbay, the connections between these applications and any other JACK-enabled applications to be started manually. The patchbay is set up using manual GUI, but connections pre-configured in the patchbay are automatically created by QjackCtl itself when applications are started.

## A GUI-based example setup
This example setup utilizes a more GUI focused configuration and management of JACK

* Install  and .
* Install , and tell your GUI window/desktop system to run it at startup.
* Make sure QjackCtl is told to:
** use the D-Bus interface,
** run at startup,
** save its configuration to the default location,
** start the JACK audio server on application startup,
** enable the system tray icon, and
** start minimized to system tray.
* Reboot.
* After logging in, you will see QjackCtl in your system tray. Left-click on it.
* Tweak settings in the QjackCtl GUI to lower latency.  The Frame Size, Frame Buffer, and Bitrate settings all affect latency.  Larger frame sizes lower latency, lower frame buffers lower latency, and higher bitrate settings lower latency, but all increase load on the sound card and your CPU.  A Latency of about ~5ms is desirable for direct monitoring of instruments or microphones, as the latency begins to become perceptible at higher latencies.

## An alternative GUI-based setup
If you use JACK for demanding tasks, but every now and then, it is possible to suspend a running PulseAudio session with QjackCtl just when you are using it. On a virgin config, modify the Server prefix option in the Settings > Advanced submenu, so that it states :

    pasuspender -- jackd

The PulseAudio session should resume fine after you close QjackCtl. Tip courtesy of this post.

## Playing nice with ALSA
To allow ALSA programs to play while jack is running you must install the jack plugin for ALSA with .

And enable it by editing (or creating) /etc/asound.conf (system wide settings) to have these lines if you have a simple 2-channel setup:
{{bc|
# convert ALSA API over JACK API
# use it with
# % aplay foo.wav

# use this as default
pcm.!default {
    type plug
    slave.pcm "jack"
    hint.description "Jack Audio"
}}}

If you have a different number of output/input channels or your first two channels are not the ones you wish to route audio to, you cannot use the predefined jack pcm source from , but rather something like:
{{bc|
pcm.!jack {
    type jack
    # If "mpv --ao:alsa ..." gives you this error:
    # Unable to set buffer time near: Invalid argument
    # uncomment the following to allow non-jack-aligned period size:
    #align_psize = 0
    playback_ports {
        0 system:playback_2
        1 system:playback_3
    }
}

pcm.!default {
    type plug
    slave.pcm "jack"
    hint.description "Jack Audio"
}}}

You need not restart your computer or anything. Just edit the ALSA configuration files, start up jack, and there you go...

Remember to start it as a user. If you start it with  as user X, it will not work for user Y.

For another (more robust but definitely more complex) approach, is to configure and use an ALSA loopback device, by loading the  kernel module, as is described in [https://alsa.opensrc.org/Jack_and_Loopback_device_as_Alsa-to-Jack_bridge this article. This snd-aloop approach can also be used to bridge Wine's ALSA output to JACK as explained in === GStreamer ===

GStreamer requires the  package to work with JACK, which contains the jackaudiosink plugin that adds JACK playback support.

Further information (outdated): https://jackaudio.org/faq/gstreamer_via_jack.html

## PulseAudio
If you need to keep PulseAudio installed (in the event it is required by other packages, like ), you may want to prevent it from spawning automatically with X and taking over from JACK.

Edit , uncomment "autospawn" and set it to "no":
 ;autospawn = yes
 autospawn = no

If you want both to play along, see: PulseAudio/Examples#PulseAudio through JACK

Cadence and other JACK GUI applications are known to write values to . These values override any system-wide defaults enabling unexpected behavior (e.g. flat volumes). Refer to PulseAudio#Configuration on how to update these configurations.

## FireWire
In order to prevent ALSA from messing around with your firewire devices you have to blacklist all firewire related kernel modules. This also prevents PulseAudio from using IEEE 1394. Create the following file:

The list of modules is the most recent available at the time of writing at [https://github.com/takaswie/snd-firewire-improve ALSA Firewire Improve Repository.

Now you can unload your loaded firewire modules or reboot.

## Network / remote audio
JACK can be configured to send audio data over a network to a "master" machine, which then outputs the audio to a physical device.  This can be useful to mix audio from a number of "slave" computers without requiring additional cables or hardware mixers, and keeping the audio path digital for as long as possible (as hardware mixers with digital inputs are very rare).

The configuration is very simple, however it requires a network that supports multicast traffic (i.e. IGMP snooping must be enabled on managed network switches), and it requires all machines be running the same JACK major version (JACK1 or JACK2) as the protocols are not interoperable between versions.  For JACK2, the  module must be loaded:

The  option tells the netmanager to automatically map any incoming connections to the default audio device.  Without this, each incoming connection would have to be manually mapped on each connection.  You can use  instead to see all available options, however note that the options are printed in the  server output, the  command will not show anything.

On the client, JACK must be started in network mode:

The two machines will connect and on the master the new audio source will be visible:

If you passed the  option to  as above, then the remote system will now be able to play audio.

## Troubleshooting
## "Cannot lock down memory area (Cannot allocate memory)" message on startup
See Realtime process management#Configuring PAM and ensure that the user is in the  user group.

## jack2 and qjackctl errors
Still having the "Cannot allocate memory" and/or "Cannot connect to server socket err = No such file or directory" error(s) when pressing qjackctl's start button?

Please delete , , . Kill jackdbus and restart from scratch :)
(Thanks to nedko)

Also try running
 $ fuser /dev/snd/*
and check the resulting PID's with
 $ ps ax | grep here
This will hopefully show the conflicting programs.

## "ALSA: cannot set channel count to 1 for capture" error in logs
Change ALSA input and output channels from 1 to 2

## Crackling or pops in audio
Your CPU or sound card is too weak to handle your settings for JACK. Lower the bitrate, lower the frame size, and raise the frame period in small increments until crackling stops. You can also try changing the sampling rate to 44100 or whatever is natively supported. This allows jack to send audio to the system without having to resample. In  with , this is accomplished with

 jack_control dps rate 44100

## No audio
If everything appears to be working - you can visually "see" sound in Jack and other things such as PulseAudio can emit sound, check the maximum sample size supported by your sound card. If your card only supports 16 bit samples then you will hear nothing until you tell Jack not to use large samples:

 jack_control dps shorts true

If you install  then you can run  to send a test tone to Jack's output.

## Problems with specific applications
## VLC - no audio after starting JACK
Run VLC and change the following menu options:
* Tools > Preferences
* Show settings: All
* Audio > Output modules > Audio output module: JACK audio output
* Audio > Output modules > JACK: Automatically connect to writable clients (enable)
