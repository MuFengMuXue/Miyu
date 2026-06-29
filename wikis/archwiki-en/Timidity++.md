# Timidity++

TiMidity++ is a software synthesizer that can play MIDI files without a hardware synthesizer. It can either render to the sound card in real time, or it can save the result to a file, such as a PCM .wav  file.

## Installation
Install the  package.

You should also install a SoundFont or Gravis UltraSound (GUS) patch files to be able to produce sound. See MIDI#List of SoundFonts.

If you use , install  since TiMidity++ sometimes depends on ALSA.

## Configuration
To configure your preferred SoundFont, add the following lines to  based on your choice.

For FreePats:

For Fluid:

## Daemon
If you intended to use TiMidity++ as an ALSA sequencer client, you should add yourself to the  user group first. As with most group changes, you will typically need to restart your user session (e.g. log out and log in again), so that the new group is visible in the output of the  command.

Start/enable the  user unit. Note that starting the service may fail if you have changed your  group membership but not yet restarted your session.

If you are using PulseAudio, that may also cause the service to fail. You may want to add the following command as an autostart program in your desktop environment. Or, if you just want to start TiMidity++ in daemon mode once, you can use the following command which will make console output viewable:

 $ timidity -iA

## Usage
## Play files
There are two ways to use TiMidity++. Either as MIDI player or as daemon adding MIDI support to ALSA.

## Standalone mode
You can simply use TiMidity++ to play MIDI files:
 $ timidity example.mid

Add option  for a text-based interface. There are many other options to TiMidity++. See  or use  to get help.

## Daemon mode
If you are runing TiMidity++ as a daemon (ALSA sequencer client), it will provide MIDI output support for other programs such as rosegarden, aplaymidi, vkeybd, etc.

This will give you four output software MIDI ports (in addition of hardware MIDI ports on your system, if any):

You can now play MIDI files using aplaymidi:

 $ aplaymidi filename.mid --port 128:0

Another example is vkeybd, a virtual MIDI keyboard for X.

You can install .

 $ vkeybd --addr 128:0

Option  connects the input (readable) software MIDI port provided by vkeybd to the first output (writable) ALSA port provided by Timidity. Alternatively you can use aconnect,  or kaconnect. As a result when you play around with the keys on the vkeybd TiMidity++ plays the appropriate notes.

## Connect to virtual MIDI device
Once you have the TiMidity++ daemon running and it is working with aplaymidi, you can connect it to a virtual MIDI device that will work in programs such as rosegarden or scala.

Load the  kernel module and (optionally) configure your system to load the module at boot.

Use aconnect to verify the port numbers:

Now create the connection:
 $ aconnect 20:0 128:0

You should now have a working MIDI output device on your system ().

## Tips and tricks
## Convert files
TiMidity++ can also convert MIDI files into other formats. The following command saves the resulting sound to a WAV file:
 $ timidity input.mid -Ow -o out.wav
To convert to another formats, you can use FFmpeg. This will convert it to mp3:
 $ timidity input.mid -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 256k out.mp3

## How to make DOSBox use TiMidity++
First of all, you need to write a configuration file. Input the following in DOSBox to create a configuration file:
 config -writeconf dosbox.conf
you can replace  by any name that you want, add a dot in front of it if you want to hide it.

Make sure you started TiMidity++ as daemon as the instructions above, use the aconnect command.

Edit this configuration file with any editor, go to the section:

put the ALSA connection port into the back of config=, in default:
 config=128:0

Restart DOSBox within a terminal so you can see its debug messages, by no accident you should see a successful initiation on port 128:0.

## Troubleshooting
## TiMidity++ does not play MIDI files
It may be that your SoundFile is not set up correctly. Just run:
 $ timidity example.mid

If you find a line like this in the terminal output, your SoundFile is not set up properly.

 No instrument mapped to tone bank 0, program XX - \
 this instrument will not be heard

Make sure you have installed some samples and your SoundFile is added to . See Configuration for more details.

## Daemon mode plays sound out of pace
TiMidity++'s ALSA output module (default) may cause this issue in ALSA server mode. Try another output option, for example, libao:

 $ timidity -iA -OO

And test it using aplaymidi. If this does not work, you may want to configure JACK and set TiMidity++'s output to jack.
