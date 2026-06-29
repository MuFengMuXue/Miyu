# PipeWire/Examples

## Surround sound systems
## Splitting front/rear
When using PipeWire as a PulseAudio/JACK replacement, you can set up PipeWire to replicate the PulseAudio example for splitting front/rear. Doing this allows you to send audio streams using PulseAudio to a separate sink for speakers or headphones.

Connect speakers to the line-out port and headphones to the rear port. In  set the soundcard used to Analog Surround 4.0 Output.

## Using a PipeWire config file
Create an additional PipeWire config file  or  with the following content and adapt the  lines:

 context.modules = [
     {   name = libpipewire-module-loopback
         args = {
             node.name = "speakers"
             node.description = "Speakers"
             capture.props = {
                 media.class = "Audio/Sink"
                 audio.position = [ FL FR ]
             }
             playback.props = {
                 target.object = "alsa_output.pci-0000_00_14.2.analog-surround-40"
                 stream.dont-remix = true
                 node.passive = true
                 audio.position = [ FL FR ]
             }
         }
     }
     {   name = libpipewire-module-loopback
         args = {
             node.name = "headphones"
             node.description = "Headphones"
             capture.props = {
                 media.class = "Audio/Sink"
                 audio.position = [ FL FR ]
             }
             playback.props = {
                 target.object = "alsa_output.pci-0000_00_14.2.analog-surround-40"
                 stream.dont-remix = true
                 node.passive = true
                 audio.position = [ RL RR ]
             }
         }
     }
 ]

Restart PipeWire and you should see two new outputs in . Similar examples can be found in the PipeWire Loopback module documentation

## Using  and
Using the following commands, make new sinks for the speakers and for the headphones, link the speakers to the front channels and link the headphones to the rear channels:

  pactl load-module module-null-sink sink_name=speakers object.linger=1 media.class=Audio/Sink channel_map=FL,FR
  pactl load-module module-null-sink sink_name=headphones object.linger=1 media.class=Audio/Sink channel_map=RL,RR

 keeps the sinks alive after the creating client disconnects. You can name  whatever you want.

In order to unload module, you can use , where  is output of  command. Unloading individual modules through  is not currently supported However, you may use it to unload all  modules using .

Using , connect the monitors of the new sinks to the sound card's playback ports. Find out the name of the channels by running [https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Migrate-JACK.

  pw-link speakers:monitor_1 alsa_output.pci-0000_00_14.2.analog-surround-40:playback_FL
  pw-link speakers:monitor_2 alsa_output.pci-0000_00_14.2.analog-surround-40:playback_FR
  pw-link headphones:monitor_1 alsa_output.pci-0000_00_14.2.analog-surround-40:playback_RL
  pw-link headphones:monitor_2 alsa_output.pci-0000_00_14.2.analog-surround-40:playback_RR

To individually control the volumes, one option is to use ALSA utilities—such as —to control Front and Rear/Surround (ALSA naming) channels. A script to automatically do that depending on what is your currently default PulseAudio sink can be found here.

## Echo cancellation
PipeWire can remove your speakers' sounds from your microphone in real time, which makes it possible to attend audio chats without having to use headphones, even while other applications are playing audio.

Usually, voice chat applications do cancel out feedback, but they are only aware of audio that goes through them. As an example, if another voice chat attendant talks on your speakers, the chat application "knows" about it and is able to selectively erase this noise from your microphone, which would otherwise be repeated back into the voice chat as an annoying echo. The problems with this approach tend to start when other applications are playing to your speakers, because this audio the voice chat does not know about, and the other participants may hear it and complain. Example situations:

* Playing an online video game while using a separate voice chat application
* Using a synchronized video playback solution, such as Jellyfin SyncPlay or Watch2Gether, while using a voice chat application

This is the problem that system-wide echo cancellation solves; instead of having the voice chat app suppress the echo – and fail in the above situations – you make PipeWire do that, which innately "knows about" all audio that is played on the speakers.

Assuming a blank PipeWire configuration, system-wide echo cancellation can be enabled by creating a world-readable configuration file in  whose name ends with ".conf", for example :

Default values for "aec.args" can be found here, just search for "webrtc." in the "aec-webrtc.cpp".
  context.modules = [

      # Echo cancellation
      {   name = libpipewire-module-echo-cancel
          args = {
              # Monitor mode: Instead of creating a virtual sink into which all
              # applications must play, in PipeWire the echo cancellation module can read
              # the audio that should be cancelled directly from the current fallback
              # audio output
              monitor.mode = true
              capture.props = {
                  # The audio source / microphone the echo should be cancelled from
                  # Can be found with: pw-cli list-objects Node | grep node.name
                  # Optional; if not specified the module uses/follows the fallback audio source
                  #node.target = "alsa_input.usb-UGREEN_Camera_UGREEN_Camera_SN0001-02.analog-stereo"
                  # Passive node: Do not keep the microphone alive when this capture is idle
                  node.passive = true
                  # Force quantum of input stream in the graph
                  # Fiddle with if experiencing voice distortion/crackling
                  # Default: 0/unset
                  #node.force-quantum = 256
              }
              # Output sink to be filtered from input
              # Can be found with: pw-cli list-objects Node | grep node.name
              # Optional; if not specified the module uses/follows the fallback audio source
              #sink.props = {
              #   node.target = "alsa_output.pci-0000_0f_00.4.analog-stereo"
              #}
              source.props = {
                  # The virtual audio source that provides the echo-cancelled microphone audio
                  node.name = "source_ec"
                  node.description = "Echo-cancelled source"
              }
              aec.args = {
                  # Settings for the WebRTC echo cancellation engine
                  # Gain control: On-the-fly microphone audio normalization
                  # Default: false
                  # Caution, the PipeWire WebRTC source code advises against enabling it:
                  #  > Note: AGC seems to mess up with Agnostic Delay Detection, especially
                  #  > with speech, result in very poor performance, disable by default
                  #webrtc.gain_control = true
                  # Extended filter: Widened audio delay window (?)
                  # Default: true
                  # Quote from the old source of the abandoned Mozilla Positron project (2016):
                  #  > The extended filter mode gives us the flexibility to ignore the system's
                  #  > reported delays. We do this for platforms which we believe provide results
                  #  > which are incompatible with the AEC's expectations.
                  # Suggestion: Turn it off unless required
                  webrtc.extended_filter = false
              }
          }
      }
  ]

Configuration changes such as these require a PipeWire restart (i.e. the  and  user unit) to become effective.

## Mixing additional audio into the microphone's audio
The echo cancellation example above can be extended to provide a virtual sink that copies audio into your microphone.

It is a re-creation of PulseAudio/Examples#Mixing additional audio into the microphone's audio and solves the same use-case.

To achieve this you additionally load two instances of the "Combine stream" module, as shown below.

Currently, after each reboot or PipeWire restart the setup requires manual user action in e.g. Helvum to complete it; see the "TODO" comment in the configuration example.

  context.modules = [

      # (Configuration for system-wide echo cancellation, see above)

      # Audio effects sink (stereo)
      {   name = libpipewire-module-combine-stream
          args = {
              combine.mode = sink
              node.name = sink_fx
              node.description = "Effects sink (play shared audio here)"
              combine.props = {
                  audio.position = [ FL FR ]
              }
              stream.props = {
                  # If you have an upmix configuration in client.conf.d, set the same
                  # parameters here, or else your sound effects application will not
                  # be upmixed in your local audio output
                  #channelmix.upmix = true  # (...)
                  # Possible alternative: Poor man's stereo upmix, i.e. mirroring front
                  # to rear speakers
                  #combine.audio.position = [ FL FR FL FR ]
                  #audio.position = [ FL FR RL RR ]
              }
          }
      }

      # Main source
      # Virtual source that supplies these sources mixed together:
      #  - source_ec (Echo-cancelled source)
      #  - sink_fx.monitor (Monitor of the audio effects sink)
      {   name = libpipewire-module-combine-stream
          args = {
              combine.mode = source
              node.name = source_main
              node.description = "Main source (record from here)"
              #combine.latency-compensate = false
              combine.props = {
                  audio.position = [ FL FR ]
              }
              stream.rules = [
                  {   matches = [
                          {
                              node.name = "source_ec"
                              media.class = "Audio/Source"
                          }
                      ]
                      actions = {
                          create-stream {
                          }
                      }
                  }
                  # TODO Block with matches= and actions= that matches the monitor of
                  # sink_fx and hooks it up to source_main
                  # No PipeWire configuration known yet that automates this
                  # See this PipeWire issue for news:
                  # https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/3710
                  # For the time being, add the required connections manually in Helvum,
                  # i.e. connect these points:
                  #  - sink_fx.monitor_FL -> source_main.output.input_FL
                  #  - sink_fx.monitor_FR -> source_main.output.input_FR
              ]
          }
      }
  ]
