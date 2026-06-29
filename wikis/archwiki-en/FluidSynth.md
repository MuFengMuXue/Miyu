# FluidSynth

FluidSynth is a real-time software synthesizer based on the SoundFont 2 specifications. It is optionally used by .

## Installation
Install the  package.

A SoundFont is also needed. See MIDI#List of SoundFonts for a list of SoundFonts.

Remember to either modify the default SOUND_FONT or redirect that location to a shared sound font with a symlink.

## Usage
There are two ways to use FluidSynth. Either as a MIDI player or as a daemon which provides an ALSA MIDI input and outputs synthesized audio via PipeWire, PulseAudio, JACK, ALSA, etc.

## Standalone mode
You can simply use fluidsynth to play MIDI files:

 $ fluidsynth -a alsa -m alsa_seq -l -i /usr/share/soundfonts/FluidR3_GM.sf2 example.mid

assuming than you installed .

There are many other options to FluidSynth; see  or use  to get help.

One may wish to use  or  instead of  as the argument to the  option.

## Daemon mode
 enumerates valid output devices. See audio.driver for available options.

## Common configuration
*  — System wide defaults, such as a default , audio rate, output device.
*  — Per user overrides for the above, it is safe to copy the template from the system wide configuration and customize.

## PipeWire / PulseAudio / JACK
Software defined audio running as the desktop user (not root). Likely what is in use on your system.

Configure the system wide or user specific options, to include the audio-driver, midi-driver, and sample-rate respectively:

Additional arguments might be required:

*  documentation suggests the default might be 64, my system required 128 to work reliably
*  A float value to adjust the volume (in case you do not want to use PipeWire / PulseAudio / etc to do that)
*
*  Any other options

Start/enable the  user unit.

## ALSA / OSS
ALSA or OSS should offer the lowest latency, however multiple audio clients—e.g. any other audio application, PipeWire, PulseAudio, JACK, etc.—require hardware mixing or ALSA  plugin as the first audio client (to provide software mixing in ALSA). Additionally the rest of the audio stack on a modern system will already be routed (and volume mixed) via PipeWire (usually) or PulseAudio (on new / updated installs likely a PipeWire compatibility interface).

If you want fluidsynth to run as an ALSA sequencer client, edit  and add your SoundFont along with any other changes you would like to make, for example Fluid:

 SOUND_FONT=/usr/share/soundfonts/FluidR3_GM.sf2
 OTHER_OPTS='-a alsa -m alsa_seq -r 48000'

After that, you can start/enable .

## Command line test
The following will give you an output software MIDI port (in addition of hardware MIDI ports on your system, if any):

An example of usage for this is aplaymidi:

 $ aplaymidi -p128:0 example.mid

## SDL_Mixer
To use fluidsynth with programs that use SDL_Mixer, you need to specify the soundfont as:

  $ SDL_SOUNDFONTS=/usr/share/soundfonts/FluidR3_GM.sf2 ./program

## Tips and tricks
## Convert MIDI to MP2/MP3/OGG
Requires  or any other SoundFont of your choice.

 is the default location of FluidR3_GM

Simple command lines to convert midi to mp2:

 $ fluidsynth -l -T raw -F - /usr/share/soundfonts/FluidR3_GM.sf2 example.mid | twolame -b 256 -r - example.mp2

Requires .

Simple command lines to convert midi to mp3:

 $ fluidsynth -l -T raw -F - /usr/share/soundfonts/FluidR3_GM.sf2 example.mid | lame -b 256 -r - example.mp3

Requires .

Simple command lines to convert midi to ogg:

 $ fluidsynth -nli -r 48000 -o synth.cpu-cores=2 -T oga -F example.ogg /usr/share/soundfonts/FluidR3_GM.sf2 example.MID

Here is a little script to convert multiple midi files to ogg in parallel:

 #!/bin/bash
 maxjobs=$(grep processor /proc/cpuinfo | wc -l)
 midi2ogg() {
 	name=$(echo $@ | sed -r s/| sed s/^[.for arg; do
 	fluidsynth -nli -r 48000 -o synth.cpu-cores=$maxjobs -F "/dev/shm/$name.raw" /usr/share/soundfonts/FluidR3_GM.sf2 "$@"
 	oggenc -r -B 16 -C 2 -R 48000 "/dev/shm/$name.raw" -o "$name.ogg"
 	rm "/dev/shm/$name.raw"
 	## Uncomment for replaygain tagging
 	#vorbisgain -f "$name.ogg"
 	done
 }
 export -f midi2ogg
 find . -regex '.*[.-print0 | xargs -0 -n 1 -P $maxjobs bash -c 'midi2ogg "$@"' --

## Troubleshooting
## Conflicting with PulseAudio
If your fluidsynth application is set to use  as driver, the sound card will be accessed directly and PulseAudio and applications using PulseAudio will not be able to work properly. You can modify the  configuration file  and change the driver to , then restart fluidsynth and PulseAudio:

## No MIDI sound / Not the lowest or first MIDI device
Wine, Proton and many other programs will grab the first MIDI device as their default output. Many have methods to configure a non-default or specific MIDI device but disabling the [https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/sound/core/seq/seq_dummy.c?h=v6.13.11#n17 snd_seq_dummy module is simpler, even if it can be useful for professionals who need to duplex MIDI output to multiple devices.

Remove the module right now.

 # rmmod snd_seq_dummy

Then blacklist it from being even loaded in the first place.

## Stuck 'key' (constant sound)
Stop the  user unit, kill all remaining  processes, then start the  user unit.

If using ALSA or OSS, and running as a root service: follow the same instruction for .

## Broken Pipe and all sound stops with Pipewire
If even simple playback tests sometimes make pipewire get stuck and the pipewire log shows messages like snd_pcm_avail after recover: Broken pipe, the audio buffer size might need to be increased:

    fluidsynth -ni --audio-bufsize=128 test.mid        # Fixes "Broken pipe".

## Audio distortions using PipeWire
After starting FluidSynth if you start hearing audio distortions or crackles during any playback, try setting  to 512 or 8192, i.e , in the  section inside the  file, if the recommended value of 128 didn't help.https://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg2038883.html
