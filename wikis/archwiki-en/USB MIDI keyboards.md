# USB MIDI keyboards

This how-to assumes that you are using ALSA and that your sound card is set up so you can listen to music. Known to work using this how-to is the Evolution MK-631 USB midi keyboard with SB Live! Value card. Execute these instructions as an unprivileged user unless otherwise noted.

## Preliminary Testing
## ALSA
Install the  package.

Type . It should output something like:

Not much will show up there, so press Ctrl+C to quit the program.

## Plugging the keyboard
Now plug the keyboard in and turn it on. The keyboard should power up. Output of  should contain:

Output of  should contain the following modules:

Now type  to list all MIDI input ports. The output should contain:

The client number is probably going to be different though. Take note of it.

## Verifying Events
Type  where you should replace  with the client number of your keyboard. You should see:

popping out all the time. Pressing a key should produce:

Various other events (turning control knobs, changing channels, etc.) should register in the list. This is a handy  way of ensuring that your keyboard is running properly.

To send MIDI events back to the keyboard or another MIDI output device, you can use run  and specify a MIDI file.

## Recording
First, use  to list the available input devices, and determine the  for the desired device.
Then, execute the following to start recording:

To stop recording, simply  the process.

 provides details about additional options available with this tool.

## Playing
To hear a sound when you push a button on your keyboard, you need a synthesizer that converts the MIDI signal into audio.

Some soundcards have a built-in hardware synthesizer, but these are not common in modern sound cards, especially not in onboard sound cards. An easier option is a software synthesizer, which is just a program which you can load with you own instrument samples.

## Hardware synthesizer
Type  to list all MIDI output ports. It depends a lot on your sound card. On SB Live! Value, you get the following output:

Here client 65 is the actual MIDI synthesizer. Assuming the soundcard is set up properly, you should be able to route the output of the keyboard to the MIDI synthesizer. Assuming out is the output client number (65 in our example) and in is the input client number (72 in our example), type . Now you can play your keyboard via the MIDI output of your sound card.

## Software synthesizer
## Qsynth
# Install .
# Start QSynth and go to Setup, where you need to load soundfont in SF2 format. You can get free SoundFonts from , or from http://soundfonts.narod.ru/ (in Russian). When QSynth asks you to restart the engine after loading the SoundFont, do so.
# Run  to list all MIDI output ports. Find the one that contains  and note the client number.
# Run  to list all MIDI input ports. Note the Keyboard client number.
# Assuming out is the output client number and in is the input client number (72 in our example), run . Now you can play your keyboard and QSynth should produce sounds.

## Qsynth using JACK
# We need to install , JACK,
# Launch qjackctl and check the settings:
# Start jackd using qjackctl (the Play button)
# Connect your USB keyboard
# Start QSynth and go to Setup, where you need to load soundfont in SF2 format. You can get free SoundFonts from http://soundfonts.narod.ru/ (in Russian). When QSynth asks you to restart the engine after loading the SoundFont, do so.
# Go to qjackctl, click Connect and choose the ALSA tab. On the left side you will see connected MIDI keyboard, on the left side - QSynth. Choose MIDI keyboard and QSynth, and click Connect.
