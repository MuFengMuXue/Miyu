# PipeWire

PipeWire is a new low-level multimedia framework. It aims to offer capture and playback for both audio and video with minimal latency and support for PulseAudio, JACK, ALSA and GStreamer-based applications.

The daemon based on the framework can be configured to be both an audio server (with PulseAudio and JACK features) and a video capture server.

PipeWire also supports containers like Flatpak and does not rely on the  and  user groups. Instead, it uses a Polkit-like security model, asking Flatpak or Wayland for permission to record screen or audio.

## Installation
Install the  package from the official repositories. There is also  for multilib support.

Optionally, install  to review the documentation.

Pipewire can work as drop-in replacement for other audio servers. See #Audio for details.

## Session manager
Like JACK, PipeWire implements no connection logic internally. The burden of watching for new streams and connecting them to the appropriate output device or application is left to an external component known as a session manager.

## WirePlumber
WirePlumber is the recommended session manager. It is based on a modular design, with Lua plugins that implement the actual management functionality.

The stock configuration files are stored in . The recommended way to customize Wireplumber is adding snippets overriding specific settings in  or . WirePlumber changed its configuration format in version 0.5 from  to . See https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/migration.html#config-migration for migration instructions.

## PipeWire Media Session
 is deprecated and no longer recommended. It was mostly implemented for testing and as an example for building new session managers.

## Startup
Pipewire uses systemd/User for management of the server and automatic socket activation: it will start automatically when needed.

To preemptively start PipeWire at login, enable/start the ,  and  user units.

## GUI
*
*
*
*
*
*

## TUI
*
*

## Configuration
The PipeWire package provides an initial set of [https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Config-PipeWire#configuration-file-pipewireconf configuration files in . You should not edit these files directly, as package updates will overwrite your changes. To configure PipeWire, you can copy files from  to the alternate system-wide location , or to the user location . An equally named file in a directory with a higher precedence makes the analogous files ignored.

PipeWire brings a custom Pro Audio (do not confuse with pro audio) profile in addition to the PulseAudio profiles, selectable through .

## Usage
## Audio
PipeWire can be used as an audio server, similar to PulseAudio and JACK. It aims to replace both PulseAudio and JACK, by providing a PulseAudio-compatible server implementation and ABI-compatible libraries for JACK clients. See the blog post PipeWire Late Summer Update 2020 for more information.

First, install . Depending on the type of audio clients, you may also need to take some extra steps. You may need to install additional firmware for your audio device, see Advanced Linux Sound Architecture#Firmware.

## ALSA clients
Install  (and remove  if it was installed) to route all applications using the ALSA API through PipeWire.

## PulseAudio clients
Install . It will replace  and . Reboot, re-login or stop  and start the  user unit to see the effect.

Normally, no further action is needed as the user service  should be enabled automatically by the package. To check if the replacement is working, run the following command for the Server Name and default input/output:

{{hc|$ pactl info|2=
...
Server Name: PulseAudio (on PipeWire x.y.z)
...
Default Sink: alsa_output.{bus}-{device}.{profile}
Default Source: alsa_input.{bus}-{device}.{profile}
...
}}

 is provided by PulseAudio client library package (), which is installed with pipewire-pulse as a dependency.

## Setting overall or individual channel volume
To adjust output channel volume, the sink needs to be specified using {{ic|pactl get-sink-volume {sink}}} using the value of Default Sink: (above) or Name: (below), default sink device (@DEFAULT_SINK@), or Sink # (e.g. 1 below):

Hint: if audio is playing,  for RUNNING as other devices will be SUSPENDED.

The balance ratio is calculated automatically. To set the overall volume of the default device use:
To set individual channels, provide each channel volume separately:

Source inputs are handled similarly.  For further configuration (e.g. regarding modules) see the official upstream Wiki about Migration from PulseAudio and Pipewire-Pulse Configuration.

## JACK clients
Install  for JACK support. There is also  for multilib support.

 may be used to start JACK clients, but it is technically not required, as it only serves as a wrapper around the ,  and  environment variables.

It is possible to request a custom buffer size by setting a quotient of buffersize/samplerate (which equals the block latency in seconds):

 PIPEWIRE_LATENCY="128/48000" application

## Bluetooth devices
PipeWire handles Bluetooth audio devices if the  package is installed.

## Automatic profile selection
WirePlumber has profile auto-switching enabled by default. It can automatically switch between HSP/HFP and A2DP profiles whenever an input stream is detected. You can disable it with the following command:

 $ wpctl settings --save bluetooth.autoswitch-to-headset-profile false

 has it disabled by default. You can set  property to  to enable it:

{{hc|/etc/pipewire/media-session.d/bluez-monitor.conf (or ~/.config/pipewire/media-session.d/bluez-monitor.conf)|output=
...
rules = [
    {
        ...
        actions = {
            update-props = {
                ...
                bluez5.autoswitch-profile = true
...
}}

## PipeWire patch sets for command line
 can be used to visualize and create connections, and also save and load patch sets.

For non-GUI needs, the following are bash scripts to save wiresets, load wiresets, and dewire all connections. For saving and loading, use a command-line parameter for the filename.

{{hc|pw-savewires|
#!/bin/bash

if  "$#" -ne 1 ; then
    echo
    echo 'usage: pw-savewires filename'
    echo
    exit 1
fi

rm -- "$1" &> /dev/null

link_nodeOutput=''

while IFS= read -r line; do
    if "$line" =~ [| ]];
    then
        link_nodeInput=`echo $line | cut -d ">" -f 2`
        echo "Saving $link_nodeOutput, ${link_nodeInput//' '}"
        echo "$link_nodeOutput ${link_nodeInput//' '}" >> "$1"
    else
        link_nodeOutput="$line"
    fi
done " -f 2`
        echo "Removing $link_nodeOutput, ${link_nodeInput//' '}"
        pw-link -d $link_nodeOutput ${link_nodeInput//' '}
    else
        link_nodeOutput="$line"
    fi
done
        remote.source.port = 10001
        remote.repair.port = 10002
        remote.control.port = 10003
        sink.props = {
            node.name = "my-roc-sink"
            node.description = "my-roc-sink"
        }
    }
  }
]
}}

See PipeWire documentation for more options.

Restart the  user unit on both machines.

## Run PipeWire on top of native JACK
PipeWire can also run as a JACK client on top of the native JACK daemon if desired.

See JACK and PipeWire (PipeWire wiki) and JACK Bridge (PipeWire wiki) for more information and additional configuration (like available channels for example).

To use it install the  and start JACK. Pipewire should be bridged automatically.

## Use ALSA dmix devices as PipeWire sinks
It is possible to have a PipeWire server (or multiple, for each user) output to ALSA via ALSA dmix devices. This allows you to use ALSA as the primary audio output system while being able to use non-ALSA devices such as Bluetooth headphones.

## ALSA dmix setup
Suppose you have two cards,  and :

and your PCMs look like:

and suppose your ALSA configuration looks something like this:

{{hc|/etc/asound.conf|
ctl.!default {
  type hw
  card PCH
}

pcm.!default {
  type plug
  slave.pcm "dmix:PCH,0"
}

pcm.dhdmi {
  type plug
  slave.pcm "dmix:HDMI,9"
}
}}

In this particular example, the dmix devices would be  and .

## PipeWire dmix setup
First of all, stop WirePlumber from monitoring and adding hardware ALSA devices by disabling the  feature:

{{hc|/etc/wireplumber/wireplumber.conf.d/disable-alsa-monitor.conf (or ~/.config/wireplumber/wireplumber.conf.d/disable-alsa-monitor.conf)|output=
wireplumber.profiles = {
  main = {
    monitor.alsa = disabled
  }
}
}}

Now, configure PipeWire to use dmix devices. The default configuration file () contains a commented out example which you can use as a basis.

Add your own element to the  array:

{{hc|/etc/pipewire/pipewire.conf.d/alsa-dmix.conf (or ~/.config/pipewire/pipewire.conf.d/alsa-dmix.conf)|output=
context.objects = [
    # We do not start with dmix, but with an input device.
    # Do not forget to add an input device.
    # On a friend's Laptop, I saw Zoom having a nervous
    # breakdown and endlessly crying because no input device
    # was configured! You have been warned.
    { factory = adapter
        args = {
            factory.name           = api.alsa.pcm.source
            node.name              = "alsa-mic-internal" # name of pulse device (mpv)
            node.description       = "Mic Internal" # name of pulse device (pavucontrol)
            media.class            = "Audio/Source"
            api.alsa.path          = "hw:PCH,0"
        }
    }
    # Okay, now we add our dmix PCMs
    { factory = adapter
        args = {
            factory.name           = api.alsa.pcm.sink # sink for dmix
            node.name              = "alsa-dmix-internal" # name of pulse device (mpv)
            node.description       = "PCM Internal" # name of pulse device (pavucontrol)
            media.class            = "Audio/Sink" # Sink for dmix
            api.alsa.path          = "dmix:PCH,0"
        }
    }

    { factory = adapter
        args = {
            factory.name           = api.alsa.pcm.sink # sink for dmix
            node.name              = "alsa-dmix-hdmi" # name of pulse device (mpv)
            node.description       = "PCM HDMI" # name of pulse device (pavucontrol)
            media.class            = "Audio/Sink" # Sink for dmix
            # remember this is a non-default dmix from /etc/asound.conf
            api.alsa.path          = "dmix:HDMI,9"
        }
    }
]
}}

As a user (non-root), check out the output of , and set the default input(source) and output(sink) devices to your liking with .  is the number before sink/source names.

Now, you can fully test your configuration.

## Switching between device profiles
Some hardware audio devices, like , function differently depending on which profile the device is running in. In the case of , there are separate profiles for HDMI and analog output.

Switching to HDMI with WirePlumber:

Switching to analog with WirePlumber:

## Multi-user audio sharing
Sometimes it is useful to let other users connect to your PipeWire instance. For example, if you login into a different user's account using Xephyr and want the audio you play in the Xephyr session to come out the speakers which are managed by the outer user.

One method to do this is to configure the outer user's pipewire-pulse config to listen for localhost tcp connections.

Create a file like under the outer user's home directory:
{{hc|
~/.config/pipewire/pipewire-pulse.conf.d/pulse-server.conf
|output=
pulse.properties  {
    server.address  [
        "unix:native"
        "tcp:127.0.0.1:4713"   # Now the outer user's pipewire server listens on the IP4 loopback
    ]
}
}}

Then set the environment variable  in the inner user's session. For example, ing it before you start Xephyr as the inner user. More information and alternative setups can be found on this forum thread.

## WebRTC screen sharing
Most applications used to rely on X11 for capturing the desktop (or individual applications), for example when using WebRTC in web browsers (e.g. on Google Meet). On Wayland, the screen sharing mechanism is handled through the XDG Desktop Portal and PipeWire, which enables sharing content under Wayland with fine-grained access controls.

Firefox (84+) and Chromium (110+) support this method by default, while on older versions of Chromium (73+), one needs to enable WebRTC PipeWire support by setting the corresponding (experimental) flag at the URL  or via CLI argument .

 (27+) supports this method by using the new PipeWire capture source.

## Video
Although the software is not yet production-ready, it is safe to play around with. Most applications that rely on GStreamer to handle e.g. video streams should work out-of-the-box using the PipeWire GStreamer plugin, see GStreamer#PipeWire. Applications like e.g.  are therefore already able to share video input using it.

Using , it should also be possible to use the  script to preload a library () that intercepts v4l2 calls and routes video through pipewire.

## Audio post-processing
## Pipewire module-filter-chain
Pipewire has an internal module called filter-chain that can create nodes to process audio input and output. See  for examples including equalization, virtual surround sound, LADSPA plugins and channel mixing.

## LADSPA
You can install many LADSPA plugins from the official repositories and use them in Pipewire filter chains.
To list plugin labels and available controls provided by a specific file use  from the  package:

 $ analyseplugin /usr/lib/ladspa/lsp-plugins-ladspa.so

## Systemwide parametric equalization
PipeWire filter-chain supports Parametric EQ Create a config file inside  (or ), then edit it to incorporate desired parameters using the following example:

{{bc|1=
context.modules = [
    {
        name = libpipewire-module-filter-chain
        args = {
            node.description = "Equalizer Sink"
            media.name       = "Equalizer Sink"
            filter.graph = {
                nodes = [
                    {
                        type  = builtin
                        name  = eq
                        label = param_eq
                        config = {
                            filters = [
                                { type = bq_peaking, freq = 100, gain = 0.0, q = 1.0 },
                                { type = bq_peaking, freq = 500, gain = 0.0, q = 1.0 },
                                { type = bq_peaking, freq = 2000, gain = 0.0, q = 1.0 },

                        }
                    }
                ]
                links = }
            audio.channels = 2
            audio.position = [ FL FR
            capture.props = {
                node.name   = "effect_input.eq"
                media.class = Audio/Sink
            }
            playback.props = {
                node.name   = "effect_output.eq"
                node.passive = true
            }
        }
    }
]

}}

You can use arbitrary amount of filters.

If you require a pre-amp, apply a  filter at frequency 0, for example:

 { type = bq_highshelf, freq = 0, gain = -5.0, q = 1.0 },

Restart Pipewire, select "Equalizer Sink" as your default sound output device; this should then apply to all applications.

Alternatively, instead of specifying the  array, you can provide a  property, pointing to a parametric equalizer configuration generated from the AutoEQ project or Squiglink, like:

{{bc|1=
config = {
    filename = "/path/to/parametric.txt"
}
}}

## EasyEffects
EasyEffects (formerly PulseEffects) is a Qt utility which provides a large array of audio effects and filters to individual application output streams and microphone input streams. Notable effects include an input/output equalizer, output loudness equalization and bass enhancement, input de-esser and noise reduction plug-in. See the GitHub page for a full list of effects.

In order to use EasyEffects, install . See Community Presets for a collection of preset configurations. See AutoEq for collection of algorithmically generated EQ presets for headphones.

## NoiseTorch
NoiseTorch is an alternative way for noise suppression, packaged with . There also exists .

After starting it the module can be loaded for the selected microphone. It is possible to adjust the voice activation threshold, which should be set to the highest level, not filtering out any actual voice.

You can start audio processing with systemd automatically, see Note that the noisetorch binary path is different if installed from AUR.

## Noise suppression for voice
Install the  package.

You may follow the instructions given on [https://github.com/werman/noise-suppression-for-voice#pipewire GitHub.

## JamesDSP
JamesDSP for Linux (available as ) provides open-source sound effects for PipeWire and PulseAudio. It uses its own effects engine and without depending on LADSPA, Calf, etc. JamesDSP was initially published as an audio effects processor for Android devices.

## Using LADSPA, LV2 and VST plugins
If you want to choose between the full list of available LADSPA, LV2 and VST plugins, you can apply them using  with .

Start Carla and go to Settings > Configure Carla > Engine. Make sure Audio driver is set to JACK and choose a process mode depending on your needs. You can also choose the process mode by running Carla with a specific command, for example  for the Continuous Rack mode.

You can connect application outputs to Carla manually, but if you want to pass multiple applications through Carla, it might be more convenient to create a single virtual device between applications and Carla and optionally use it as a default device. At the begin, create a new null sink named .

{{hc|/etc/pipewire/pipewire.conf.d/10-default-null-sink.conf (or ~/.config/pipewire/pipewire.conf.d/10-default-null-sink.conf)|2=
context.objects = [
  {
    factory = adapter
    args = {
      factory.name = support.null-audio-sink
      node.name = "default_null_sink"
      media.class = Audio/Sink
      audio.position = [ FL FR ]
      monitor.channel-volumes = true
      monitor.passthrough = true
    }
  }
]
}}

Restart PipeWire to apply changes.

Alternatively, you can create a temporary virtual device with  or, if  is installed, with . See the PipeWire wiki for details.

In the Rack tab, add whichever plugin you want. Make sure they are stereo type. You can change their order. In the Continuous Rack process mode, the one on top of the list will be the first to receive the audio stream, just like in EasyEffects. Afterwards go to the Patchbay tab and connect the  L/R monitors to Carla inputs, then Carla outputs to the playbacks of your desired device (speakers, earphones, HDMI, etc). Save the configuration to a local file, for example . Carla will automatically restore the connections after opening this file.

You can test the effects while a multimedia application is reproducing audio, i.e. watching a video on a website through Firefox. There are two methods to do it. The first one, inside Carla Patchbay tab, disconnecting all Firefox connections and linking its L/R outputs to  playbacks. The second through , locating Firefox audio stream and redirecting it to  (this should remember the connection to automatically redirect the application to the same sink on the next instance).

To run Carla with the Continuous Rack process mode and load the saved file at startup, create a systemd user service:

Then enable the  user unit.

Note that if you set the  as the default device in system settings, all applications will be redirected to it and the volume keys will change its level, not the one on the speakers. If you want to control volume speakers, leave them as the default in system settings and redirect your desired application to  inside pavucontrol (Pipewire compatibility layer will remember the connection on the next instance of the same application).

## Troubleshooting
## Audio
## Microphone is not detected by PipeWire
If you are using a built in microphone of a laptop, or connected using the headphone jack: First make sure the analog input is enabled in the profile in use. You can check the profile in  (and possibly in your desktop environment sound settings). In pavucontrol, on the Configuration tab, under "Built-in Audio" (or similar) make sure "Analog Stereo Duplex" is selected. If you use an advanced sound setup such as 5.1 or sound over HDMI, make sure a profile that includes "+ Analog Stereo Input" is selected.

PipeWire's  module uses  to detect devices by default. If this is not working for you, try to turn off , or optionally turn on  in :

{{hc|/etc/wireplumber/wireplumber.conf.d/alsa-config.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-config.conf)|output=
monitor.alsa.properties = {
  # Use ALSA-Card-Profile devices. They use UCM or the profile
  # configuration to configure the device and mixer settings.
  # alsa.use-acp = true
  # Use UCM instead of profile when available. Can be disabled
  # to skip trying to use the UCM profile.
  alsa.use-ucm = true
}
}}

With :

{{hc|/etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf)|output=
...
rules = [
    {
        ...
        actions = {
        update-props = {
            ...
            api.alsa.use-acp = false
...
}}

Then, restart WirePlumber and check available devices:

An alternative solution suggested in this PipeWire issue is to add the microphone manually. First of all, make sure the microphone is detected by ALSA.

Choose your microphone from the list, and to further test the microphone, run the following commands.

If the microphone is working with , but not detected by PipeWire, try to add a config file to manually add this device.

{{hc|/etc/pipewire/pipewire.conf.d/microphone.conf (or ~/.config/pipewire/pipewire.conf.d/microphone.conf)|2=
context.objects = [
    { factory = adapter
        args = {
            factory.name           = api.alsa.pcm.source
            node.name              = "microphone"
            node.description       = "Undetected Microphone"
            media.class            = "Audio/Source"
            api.alsa.path          = "hw:card_number,device_number"
        }
    }
]
}}

And then restart PipeWire to reload the config.

## Sound does not automatically switch when connecting a new device
To automatically switch to newly connected devices, create this file:

{{hc|/etc/pipewire/pipewire-pulse.conf.d/switch-on-connect.conf (or ~/.config/pipewire/pipewire-pulse.conf.d/switch-on-connect.conf)|2=
pulse.cmd = [
    { cmd = "load-module" args = "module-switch-on-connect" }
]
}}

Then restart the  with systemctl --user and check that  is loaded.

## No sound after connecting to Bluetooth device
As of 2020-12-07, if there is no sound after connecting a Bluetooth device, you might need to switch the default sink and/or move a sink input to the correct sink. Use  to list the available sinks and  to switch the default sink to the Bluetooth device. This can be automated via udev using a script similar to this one.

See this Reddit thread for a discussion of the issue. According to author of the script, the headset profile (HSP) might still have problems.

## No sound in mpv, vlc, totem, but sound works in web browser and GNOME speaker test
## Condition description
The best tool to verify the condition of this issue is to use  on a file that is expected to work with installed codecs:

 $ mpv --ao=alsa test_file.mpv
 $ mpv --ao=pcm test_file.mpv
 $ mpv --ao=jack test_file.mpv
 $ mpv --ao=pulse test_file.mpv
 $ mpv --ao=openal test_file.mpv

This recipie applies if some or all of the above tests produce sound and the same test with  option does not produce sound:

 $ mpv --ao=pipewire test_file.mpv

Gnome desktop speaker test and web browser 'youtube' produce valid sound outcomes.

Switching inputs, muting, unmuting, changing volume in Gnome does not resolve the issue.

Sink status reported by  as 'SUSPENDED' is of no concern, because status properly changes when running video through a web browser.

Use of  does not point to any obvious issues.

Inspection of relevant  unit logs does not point to any obvious issues.

## Reason for the issue
It seems that a path from  to hardware got muted or changed somehow.  The original author does not know how to identify and point out at the issue using command line tooling.

## Solution
Install the  package.  Run , select the appropriate source in the Configuration tab,  select it again in the Output device tab and then use Mute button to mute and unmute the source while  video is running.

In another case, removing  and rebooting solved the same problem.

## Low volume
After replacing PulseAudio with Pipewire, sound may work fine, but after a reboot, the volume becomes intolerably low.

Open , use  to select the proper soundcard, and make sure the ALSA volumes are at 100%.  should maintain this setting after reboot.

## Increasing RLIMIT_MEMLOCK
 Dec 13 11:11:11 HOST pipewire-pulseFailed to mlock memory 0x7f4f659d8000 32832: This is not a problem but for best performance, consider increasing RLIMIT_MEMLOCK

Install  and add your own user to the  group.

Alternatively, increasing memlock from 64kB to 128kB seems enough to fix this. If you are running  under systemd/User, add:

 username	soft	memlock	64
 username	hard	memlock	128

to

## Changing the default sample rate
By default PipeWire sets a fixed global sample rate of 48kHz. If you need to change it, you can set a new default (although it isn't recommended):

{{hc|/etc/pipewire/pipewire.conf (or ~/.config/pipewire/pipewire.conf)|output=
...
context.properties = {
    ...
    default.clock.rate          = sample_rate'
    ...
}}

This, however, isn't recommended as this will affect latencies as the quantum values aren't re-calculated automatically. You will have to change these yourself if you want to preserve the same ratio. To quote the documentation:
: The default clock rate determines the real time duration of the min/max/default quantums. You might want to change the quantums when you change the default clock rate to maintain the same duration for the quantums.

Keep in mind that the rates of the streams will remain the same. All that PipeWire will be doing here is resampling to meet your new rate. So the 48kHz streams that would've been left unaltered will now be resampled.

If you have gear that can handle different sample rates, it is instead recommended to leave the defaults and follow as indicated here: #Changing the allowed sample rate(s)

## Changing the allowed sample rate(s)
PipeWire can also change dynamically the output sample rates supported by your DAC. The sample rate follows the sample rate of the audio stream being played.

{{hc|/etc/pipewire/pipewire.conf (or ~/.config/pipewire/pipewire.conf)|output=
...
context.properties = {
    ...
    default.clock.allowed-rates = [ sample_rate_1 sample_rate_2 sample_rate_3 ...
    ...
}}
for example, .

Say the default sample rate is , which is the default. Normally if a stream outputs audio at 44100Hz (i.e. a music player playing a song at CD quality), Pipewire will resample the stream to 48kHz. However, if you have  in this list, Pipewire will instead do the following. Pipewire will see that the stream is at 44100Hz, then check if  is in the allowed rates and that the receiving output device (i.e. DAC) supports the rate. In such case, the DAC will play the song losslessly. If the rate isn't in the list or if the DAC doesn't support the rate, PipeWire will simply fall back to resampling the stream to the default sample rate.

According to the developer: "PipeWire allows up to 16 different sample rates and will switch when possible". That means, with configuration above, no resampling is done when supported. Since PipeWire 0.3.61 up to 32 different sample rates can be configured.

## Getting allowed sample rate(s)
Consult your hardware manual for supported values of your DAC. Supported rates by the kernel driver codec are listed with the following command.

 $ grep -E 'Codec|Audio Output|rates' /proc/asound/card*/codec#*

If your DAC does not report codec information, you can try to obtain supported rates like this:

 $ grep -m1 -Hn "" /proc/asound/card?/stream? | tee /dev/tty | awk -F':' '{print $1}' | xargs grep 'Rates'

## Checking currently used sample rate
To check which output sample rate is being used for a card run:

In  or   is short for "capture" and  is for "playback".

Command:
 $ pw-top
also shows currently used sample rate for each card and audio stream.

## Sound quality
## Lossless
Lossless output (no resampling) is easy to configure with PipeWire. All you should have to do is set the following, which is described here: #Changing the allowed sample rate(s). Read that section for further context. These are the industry standard rates that you'll encounter, being the CD quality family (44100Hz, 88200Hz, 176400Hz) and DVD quality family (48kHz, 96kHz, 192kHz). Most audio streams will be in one of these rates. As long as your player of choice is the main stream, and your DAC supports the rate, PipeWire will use it. Ensure that your player is the only stream playing or resampling may occur as everything else is resampled to match the sample rate of the main graph.

{{hc|/etc/pipewire/pipewire.conf (or ~/.config/pipewire/pipewire.conf)|output=
...
context.properties = {
    ...
    default.clock.allowed-rates = [ 44100 88200 176400 48000 96000 192000 ]
    ...
}}

## Resampling
If you used PulseAudio with  or , then you might consider setting  to  or the maximum :

{{hc|/etc/pipewire/client.conf.d/resample.conf (or ~/.config/pipewire/client.conf.d/resample.conf)|output=
stream.properties = {
    resample.quality = 10
}
}}

Do not forget to restart the  and  user units (never forget  if you want your configuration changes to be applied).

There is a very little quality difference between  and , but the CPU load difference is 2-3x. And the latency difference between , ,  is yet to be investigated by anybody.  on 44100→48000 Hz on Ryzen 2600 causes  or  processes to cause 4.0% one CPU core load.

You can compare resamplers here: https://src.infinitewave.ca/ (do not pay attention to anything above 18 KHz and over 120 dB). speex is listed as "Xiph.org Speex".

PipeWire uses its own resampling algorithm called Spa. Like with SoX's , Speex's , PipeWire includes its standalone version: . Usage:

 $ spa-resample -q 14 -f s24 -r 48000 input16bit44100orAnythingElse.wav output24bit48000hz.wav

It is probably somehow possible to use other resamplers by creating your own sink. Or just use a plugin in your music player (e.g., Qmmp has SoX plugin).

## External sound card not activated after reconnect
Check  if there is any entry with default profile "off" and remove it. If that does not help, remove all files from  and restart the  user unit.

## No Sound or pactl info shows Failure: Connection refused
It means applications are unable to connect to the PipeWire-Pulse service check if the  user unit is running.

If that does not fix it, run  and pastebin  while seeking help on IRC (#pipewire on OFTC) or the mailing-lists.

## Low audio quality on Bluetooth
In case Bluetooth playback stutters, check the unit status of the  user unit for errors similar as below:

 Feb 17 18:23:01 HOST pipewire(bluez_input.18:54:CF:04:00:56.a2dp-sink-60) client too slow! rate:512/48000 pos:370688 status:triggered

If they appear, check the currently selected codec using  and try changing it by setting  to one of . You can also try mSBC support (fixes mic on Sony 1000XM3, i.e. Headphones WH-1000XM3 and Earbuds WF-1000XM3), and the SBC-XQ codec.

With :

{{hc|/etc/wireplumber/wireplumber.conf.d/bluez-config.conf (or ~/.config/wireplumber/wireplumber.conf.d/bluez-config.conf)|output=
monitor.bluez.properties = {
  bluez5.enable-sbc-xq = true
  bluez5.enable-msbc = true
  bluez5.codecs = [ sbc sbc_xq
}
}}

With :

{{hc|/etc/pipewire/media-session.d/bluez-monitor.conf (or ~/.config/pipewire/media-session.d/bluez-monitor.conf)|output=
...
properties = {
  ...
  bluez5.enable-msbc = true
  bluez5.enable-sbc-xq = true
  bluez5.codecs = sbc_xq
...
}}

Restart PipeWire by restarting the  user unit for the changes to take effect.

## Noticeable audio delay or audible pop/crack when starting playback
This is caused by node suspension when inactive.

With , create a new file to overwrite the default configuration:

{{hc|/etc/wireplumber/wireplumber.conf.d/disable-suspension.conf (or ~/.config/wireplumber/wireplumber.conf.d/disable-suspension.conf)|2=
monitor.alsa.rules = [
  {
    matches = [
      {
        # Matches all sources
        node.name = "~alsa_input.*"
      },
      {
        # Matches all sinks
        node.name = "~alsa_output.*"
      }
    ]
    actions = {
      update-props = {
        session.suspend-timeout-seconds = 0
      }
    }
  }
]
# bluetooth devices
monitor.bluez.rules = [
  {
    matches = [
      {
        # Matches all sources
        node.name = "~bluez_input.*"
      },
      {
        # Matches all sinks
        node.name = "~bluez_output.*"
      }
    ]
    actions = {
      update-props = {
        session.suspend-timeout-seconds = 0
      }
    }
  }
]
}}

Restart  and  to apply changes.

Instead of disabling suspension entirely, you can also change the timeout value to the desired number of seconds of delay before source suspension.

Some devices implement their own detection of silence and suspension. For them disabling node suspention alone won't work. It's possible to work around them by adding a small amount of noise, making it so the output never goes fully silent:

It may be necessary to play with  and  parameters to make it so the noise is sufficiently silent and simultaneously loud enough to prevent detection of silence. See PipeWire documentation.

With :

Disable this by editing  depending on where the delay occurs and changing property  to 0 to disable or experiment with other values and see what works.

Alternatively you can comment out the line  in .

Restart both  and  to apply these changes, or alternatively reboot.

## Audio cutting out when multiple streams start playing
This problem can typically be diagnosed by reading the journal of the  user unit and finding lines similar to:

 pipewire-pulsepulse-server 0x56009b9d5de0: [Nightly UNDERFLOW channel:0 offset:370676 underrun:940

According to the official PipeWire troubleshooting guide, to solve this problem for :

{{hc|/etc/wireplumber/wireplumber.conf.d/alsa-config.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-config.conf)|2=
monitor.alsa.rules = [
  {
    matches = [
      {
        node.name = "~alsa_output.*"
      }
    ]
    actions = {
      update-props = {
        api.alsa.period-size   = 1024
        api.alsa.headroom      = 8192
      }
    }
  }
]
}}

With :

If you experience audio stuttering because of kernel page locking or late scheduling see Gaming#Tweaking kernel parameters for response time consistency.

## Audio is distorted
* For microphones, try navigating to the card that is having issues after running  and use the arrow keys to reduce any "Mic Boost" or "Internal Mic Boost" options.
* Follow #Changing the default sample rate, reducing the sample rate to  (44.1 kHz).

## Audio problems after standby
If the sound is missing or otherwise garbled after waking the machine up from sleep, it might help to reinitialize ALSA:

 # alsactl init

## High latency with USB DACs (e.g. Schiit DACs)
Changing sample rates or formats might help reduce latency with some DACs such as Schiit Hel 2.For :

Copy the default configuration file  into  (or ).
Then append a new rule-block similar to the following one:

{{hc|/etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf)|output=
...
rules = {
    ...
    {
        matches = [
            {
                node.name = "alsa_output.name-of-node"
            }

        actions = {
            update-props = {
                audio.format = "S24_3LE"
                audio.rate = 96000
                # Following value should be doubled until audio does not cut out or other issues stop occurring
                api.alsa.period-size = 128
...
}}

For :

{{hc|/etc/wireplumber/wireplumber.conf.d/update-rate-and-format.conf (or ~/.config/wireplumber/wireplumber.conf.d/update-rate-and-format.conf)|2=
monitor.alsa.rules = [
  {
    matches = [
      {
        node.name = "alsa_output.name-of-node"
      }
    ]
    actions = {
      update-props = {
        audio.format = "S24_3LE"
        audio.rate = 96000
        # Following value should be doubled until audio does not cut out or other issues stop occurring
        api.alsa.period-size = 128
      }
    }
  }
]
}}

 node can be obtained using .

Your DAC might support a different format or sample rate. You can check what your DAC supports by querying ALSA:

First get the card number of your DAC:

So in this example it would be card 3.
Get all supported sample rates and formats:

In this case  are the supported formats and  are the supported sample rates across all formats.

## No sound from USB DAC until 30% volume
Some USB DACs will have no sound output until a certain level of volume is reached Typically, this is around 15% to 30%, which may result in an uncomfortably loud initial volume and the inability to maintain a low volume. The solution is to ignore hardware mixer volume control by setting  for the device to .

To achieve this with , use:

{{hc|/etc/wireplumber/wireplumber.conf.d/alsa-soft-mixer.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-soft-mixer.conf)|output=
monitor.alsa.rules = [
  {
    matches = [
      {
        device.name = "alsa_card.name-of-device"
      }

    actions = {
      update-props = {
        # Do not use the hardware mixer for volume control. It
        # will only use software volume. The mixer is still used
        # to mute unused paths based on the selected port.
        api.alsa.soft-mixer = true
      }
    }
  }
]
}}

Refer to WirePlumber#Obtain interface name for rules matching to find the correct value to replace .

Alternatively, you may specify  to apply the rules to all your audio devices.

Then, restart pipewire, e.g. by running . Set your master volume in , then save the settings by running  as root. You should now be able to use your volume mixer as normal.

## Realtime audio does not work
If  shows up in the status of the  user unit, then the priority of the pipewire daemon was not changed to realtime. See for this issue.

## Simultaneous output to multiple sinks on the same sound card
Create a copy of  so that changes persist across updates. Here we define a profile joining the two default mappings for Analog and HDMI.

Then configure your session manager to use the new card-profile for matching devices. Identifying information can be found using  or wpctl.

For :

{{hc|/etc/wireplumber/wireplumber.conf.d/alsa-custom.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-custom.conf)|2=
monitor.alsa.rules = [
  {
    matches = [
      {
        device.nick = "HDA Intel PCH"
      }

    actions = {
      update-props = {
        api.alsa.use-acp = true
        api.acp.auto-profile = false
        api.acp.auto-port = false
        device.profile-set = "multiple.conf"
        device.profile = "multiple"
      }
    }
  }
]
}}

For :

{{hc|/etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf)|2=
rules = [
    {
        matches = [ { alsa.card_name = "HDA Intel PCH" } ]
        actions = {
            update-props = {
                api.alsa.use-acp = true
                device.profile-set = "multiple.conf"
                device.profile = "multiple"
                api.acp.auto-profile = false
                api.acp.auto-port = false
            }
        }
    }
]
}}

## No notification sounds from Discord
This might cause by having the min.quantum too low, try setting it to more than 700. You can make an override for Discord specifically by appending the following rule to the pulse.rules section of pipewire-pulse.conf.

{{hc|/etc/pipewire/pipewire-pulse.conf (or ~/.config/pipewire/pipewire-pulse.conf)|output=
...
pulse.rules = [
  ...
    {
        # Discord notification sounds fix
        matches = [ { application.process.binary = "Discord" } ]
        actions = {
            update-props = {
                pulse.min.quantum      = 1024/48000     # 21ms
            }
        }
    }
...
}}

## FMOD games crashing under PipeWire
Some games that use an old version of the FMOD audio engine, like Pillars of Eternity, invoke  and crash if the PulseAudio binary is not present. A workaround is to symlink  to .# ln -s /bin/true /bin/pulseaudio

Note that if you wish to reinstall PulseAudio, you need to remove the symlink.

## Auto-switching is not working
If auto-switching is not working it may be an issue with WirePlumber state. As suggested by [https://gitlab.freedesktop.org/pipewire/wireplumber/-/issues/191#note_1252549 this comment you can delete WirePlumber's local state and restart the daemon to see if that helps:

 $ rm -r ~/.local/state/wireplumber/

Then restart the  user unit.

## Missing realtime priority/crackling under load after suspend
Due to a bug from 2011 in rtkit, suspend events cause PipeWire's realtime priority to be revoked and not restored. To disable the protection which causes this, edit :

Then restart the  unit and  user unit, along with the media session service.

## No sound during streaming to RAOP devices (Sonos etc.)
Set up mDNS hostname resolution using either Avahi or systemd-resolved.

## No sound devices show up in KDE Plasma
PipeWire clients (including the desktop environment) may rely on the XDG_RUNTIME_DIR environment variable to connect to the PipeWire daemon. If you experience no sound devices immediately after login, it may be because this variable has manually been set to the wrong path.

Although this be resolved by manually restarting PipeWire, other issues can still occur such as being unable to screen share in Chromium (with ).  is automatically set by , so you should remove any instances of it being set in your initialization files.

## Device volume for SDDM and LightDM users is not restored on login
If you use SDDM or LightDM and notice that your audio volume level is not properly restored after logging in, mask PipeWire for the display manager's user, since WirePlumber running under the display manager can interfere with your user's WirePlumber session.

 # systemctl --user -M user@ mask pipewire.socket

Replace  with  for SDDM or  for LightDM.

For more details, see this [https://wiki.debian.org/PipeWire#Device_volume_for_SDDM_users_is_not_restored_on_login Debian Wiki article.

## Terminal bell not working
From PipeWire's perspective, one must have the module x11.bell loaded. This shall be the configuration default (see also in config files mentioned above). Check if you have package  installed. Also, your window manager might influence the terminal bell, e.g., for xfwm, check in the xfwm-terminal settings that "Audible bell" is activated. Now, restart pipewire service:

 $ systemctl --user restart pipewire

You can try if the terminal bell works with:

 $ echo $'\a'

## No sound until after first playback attempt
When PipeWire is started using socket activation, some PipeWire-native applications may attempt to play audio before WirePlumber configures the nodes, resulting in an error, for example:

As a workaround, you can enable the  user unit.

## XiiSound / HAVIT Fuxi-H3 (040b:0897)
This USB headset has several quirks with PipeWire and WirePlumber:

* Audio only works at 100% volume — the hardware volume range is too narrow (0.00dB to 0.39dB) and PipeWire's dB mapping collapses any lower volume to silence.
* Left channel is silent — the device exposes a secondary ALSA mixer control (, numid=10) for the left channel that WirePlumber does not initialize, leaving it at 0%.
* Microphone initializes muted — WirePlumber may start the capture source with mute enabled.

Fix 1 — Force software mixer:

Create :

 monitor.alsa.rules = [
   {
     matches = [
       {
         device.name = "alsa_card.usb-XiiSound_Technology_Corporation_Fuxi-H3-00"
       }
     ]
     actions = {
       update-props = {
         api.alsa.soft-mixer = true
         api.alsa.ignore-dB = true
         api.alsa.split-enable = false
       }
     }
   }
 ]

Restart WirePlumber:

 $ systemctl --user restart wireplumber

Fix 2 — Restore left channel:

 $ amixer -c 0 cset numid=10 100

Fix 3 — Unmute microphone:

 $ pactl set-source-mute alsa_input.usb-XiiSound_Technology_Corporation_Fuxi-H3-00.mono-fallback 0

Persist across reboots:

 # alsactl store 0

## Video
## OBS (etc.) display nothing, even if they ask for a window/screen
If you are sure that you have  installed as well as either  or , check the running state of the daemons.

In OBS, if everything is working, you should see this in :

 ...
 info: desktop selected, setting up screencast
 info: [pipewire created stream 0x5632d7456850
 info: playing stream…

For multi-monitor setups the  package will allow to capture of all the screens.
