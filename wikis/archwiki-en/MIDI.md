# MIDI

MIDI itself, which stands for "Musical Instrument Digital Interface", is just a protocol and standard for communication between musical instruments and any device that understands the language. It can be used to control an array of synthesizers, make a tin can sound like a drum, or even operate industrial equipments.

The scope of this article, however, will mainly focus on the usage of MIDI in computer systems for playback of files that contain MIDI data. These files usually come with the  extension, and were hugely popular in the golden days of multimedia computing to share music. In professional music composition/arrangement, it still plays a vital role.

## MIDI file
Without going into the details of what the format is composed of, you just need to understand that a MIDI file eg.  does not contain any digital audio data, hence no "PCM stream". It is a common misconception that MIDI is a sound file format, and as such you usually see people complaining that music player applications cannot play the file. Here is a very beginner-friendly outline of what a MIDI/MID file contains:

 # FOOBAR.MID
 Note ON
   Use Instrument #1
   Play Note C1
   Set Volume at 100
   Set Pitch at 50

In order for such a file to be useful, there needs to be an "engine" that can translate the data to music. This engine will have a "tone generator", and this is what we call a "synthesizer". So any player that can play back a MIDI file without MIDI-capable hardware (your computer's sound device), has a synthesizer built-in or uses an external one. A typical keyboard (not the thing you are typing on) is actually made up of two components - a MIDI "controller" (the keys) and a synthesizer (tone generator/module; the thing that makes sound).

So up to this point, you should be able to understand that:

* There needs to be a synthesizer to play a MIDI file.
* A synthesizer can be hardware or software.
* Most computer soundcards/chipsets do NOT have synthesizers.
* You need a synthesizer with a proper "sound bank" (collection of sounds) to be able to enjoy all the glory of MIDI files.
* If a certain instrument is not in the sound bank, your synthesizer will not play anything for notes using that instrument.
* If a certain instrument in the file corresponds to a different one in the sound bank, your synthesizer will play a different sound (obviously).

## General MIDI sound bank
General MIDI (GM) is a specification to standardise numerous MIDI-related matters, particularly that of instruments layout in a collection of sounds. A "soundbank" which is GM-compatible means that it meets the criteria of General MIDI, and as long as the MIDI file is also GM-compatible (as in nothing extraordinary is defined - such as introducing a new instrument or having one in a different location of the sound bank), the playback will be as intended since the sound bank has the correct instrument/handler for the MIDI message/event. One of the most popular sound bank format is SoundFont, particularly SF2. Another popular format is Gravis UltraSound (GUS) patch files.

* If you have a soundcard which can make use of soundfonts, you can load a .sf2 file onto it.
* If you do not have a soundcard which can make use of soundfonts (basically no hardware synthesizer), you can use a software synthesizer and load the SF2 file. In turn, you can find some way to globally make use of this synthesizer.

## List of SoundFonts
*
*
*
*

There are a number of additional SoundFonts in the AUR: search for soundfont-. See also the FluidSynth Wiki.

## Hardware playback
If you simply need to play a MIDI file on a MIDI-capable hardware device (e.g. a hardware synthesizer), you can use the  command from .

To get the list of the available MIDI ports, use the command

 $ aplaymidi -l

Then to play a MIDI file, specify it along with an available port of the preferred MIDI device that you got from the output of the previous command. For example like this:

 $ aplaymidi -p 24:0 midi_file.mid

## SB Audigy 1 - Emu10k1 WaveTable
First, make sure that the Synth mixer control is not muted and that Audigy Analog/Digital output Jack is set to To check and adjust them, use alsamixer'' or your mixer of choice.

Next, build and install the  package from the AUR. Then, load a SoundFont file on the Emux WaveTable, like so:

 $ asfxload /path/to/any/file.sf2

The .sf2 file can be any SoundFont. If you have access to 2GMGSMT.SF2 on Windows, you can use that one.

You should be all set now. To play your .mid files with , you will have to do as follows:

Get a list of the available MIDI ports by running

Then, pick an available "Emu10k1 WaveTable" MIDI port, in this case 29:0, and specify it as such:

 $ aplaymidi -p 29:0 midi_file.mid

## Software playback
"Why can I play MIDI with Windows Media Player, then?"

Well, because Windows has a default software synthesizer which acts globally. Even then, it lacks the quality which should be expected of modern computers. If there were a way to do it on Linux, you would be able to play back MIDI from any player too. Perhaps a MIDI server (which will hold a synthesizer of choice) that sits within the sound server, like Phonon or PulseAudio. Nevertheless, nothing of this sort has been implemented and you can only play MIDI with a player, or sound server, that has a plug-in to source a synthesizer, or has a synthesizer itself.

## Synthesizers
## FluidSynth
MIDI player and a daemon adding MIDI support to ALSA. It supports SoundFonts only. See FluidSynth.

## TiMidity++
MIDI to WAVE converter and player. It supports both SoundFonts and Gravis UltraSound patch files. See Timidity++.

## WildMIDI
[https://github.com/Mindwerks/wildmidi WildMIDI is a simple software MIDI player. It uses Gravis UltraSound patch files to convert MIDI files into audio. SoundFonts are not supported yet.https://github.com/Mindwerks/wildmidi/issues/8 In order to use it, a configuration file  is needed which points to the GUS patches:

The configuration file format is mostly compatible with TiMidity++.

You can simply use WildMIDI to play MIDI files:

 $ wildmidi example.mid

To convert MIDI files to WAV format:
 $ wildmidi example.mid -o example.wav

See  for more options.

## Players
## GStreamer-based players
MIDI files can be played in GNOME Videos and all other players using GStreamer as backend after having installed  and a SoundFont ( for example). It uses FluidSynth as synthesizer and picks up the first usable SoundFont from the  directory.

## VLC
The FluidSynth plugin provides MIDI playback support for VLC using FluidSynth as synthesizer. A SoundFont needs to be installed, and VLC will detect it automatically. If multiple SoundFonts are installed, you can choose one in VLC preferences (Tools > Preferences): you have to show all settings. Then, go to Input/Codecs > Audio codecs > FluidSynth.

And, if you installed e.g. Fluid, set the location to .

## Audacious
The AMIDI-Plug from the  package provides MIDI playback support for Audacious using FluidSynth as synthesizer. You can specify the SoundFont to use for playback in the settings of its MIDI output plugin (File > Preferences > Plugins > Input > AMIDI-Plug > Preferences).

## DeaDBeeF
 player is able to play MIDI files via its WildMidi player plugin. It does not support SoundFonts, just Gravis UltraSound patch files. You can specify the configuration file location in DeaDBeeF by going to Edit > Preferences > Plugins > WildMidi Player > Configure.

## Drumstick
Drumstick MIDI File Player is able to play MIDI files using FluidSynth as synthesizer. Install .
