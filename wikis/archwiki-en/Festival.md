# Festival

Festival is a general multi-lingual speech synthesis system developed at CSTR (Centre for Speech Technology Research). It offers a general framework for building speech synthesis systems as well as including examples of various modules. As a whole it offers full text to speech through a number APIs: from shell level, though a Scheme command interpreter, as a C++ library, from Java, and an Emacs interface. Festival is multi-lingual (currently British English, American English, Italian, Czech and Spanish, with other languages available in prototype.)

## Installation
Install the  package, and one or more speakers/voices:

*  provides a British and American English Male speaker.
*  provides American Male/Female and Scottish English Male speaker.

More speakers are available in the AUR.

## Configuration
There is no global  configuration file, but you can configure festival with your  file, or by directly editing . Both of these are scheme files, using scheme syntax and rerun everytime festival is run.

## Sound server
You must select a sound server (either PulseAudio or ALSA).  The following settings will allow Festival to work if audio from other sources is already playing.  Add one of these to your config:

For PulseAudio:

 (Parameter.set 'Audio_Required_Format 'aiff)
 (Parameter.set 'Audio_Method 'Audio_Command)
 (Parameter.set 'Audio_Command "paplay $FILE --client-name=Festival --stream-name=Speech")

For ALSA: (Parameter.set 'Audio_Method 'Audio_Command)
 (Parameter.set 'Audio_Command "aplay -q -c 1 -t raw -f s16 -r $SR $FILE")

## Voices
Arch splits the set of official voices into  (recommended) and . The [https://aur.archlinux.org/packages/?K=festival AUR has some others, in various states of maintenance which may or may not be currently working.

To see what voices are currently installed and what the default is, first enter Festival's #Interactive shell (a REPL scheme). To permanently change the default voice add it to your config, for example:

 (set! voice_default voice_cmu_us_rms_cg)

Append to  to apply for all users.

## Manually
You can also get voices straight from Festvox [http://festvox.org/packed/festival/2.5/voices/. You will need to unzip and move the folder containing the voice to  and the way to tell what folder contains the voice is to look for a  subfolder inside of it. You can then test that your new voices are found by loading up the festival prompt.

## Usage
## Using Files as Input or Output
To read a text file:

 $ festival --tts text_file

To read a selection you highlighted with the cursor:

 $ xsel | festival --tts

Convert a text file to an mp3 audio:

 $ text2wave text_file | lame - text.mp3

Record audio with a select voice:

 $ text2wave -o output.wav -eval '(voice_german_de2_os)' text_file

## Interactive
Festival has an interactive prompt you can use for testing. Type  to enter it. The following are some examples:

To show the voice festival speaks with:

 voice_default

To list available voices:

 (voice.list)

To select another voice, enter . For example:

 (voice_cmu_us_rms_cg)

To hear it speak:

 (SayText "Arch makes me happy")

To list available commands:

 help

To exit the shell:

 (quit)

## Troubleshooting
## Can't open /dev/dsp
If festival returns the following error message:

 Linux: can't open /dev/dsp

See #Sound server above.

## ALSA playing at wrong speed
If the solution above gives you a squeaky voice, you might want to try changing your aplay options:

 (Parameter.set 'Audio_Method 'Audio_Command)
 (Parameter.set 'Audio_Command "aplay -Dplug:default -f S16_LE -r $SR $FILE")

## Command aplay not found
Install the  package.

## Killing festival process doesn't stop audio
Killing a background festival process will not stop the audio from continuing to play.

To stop audio from playing, the child  processes must be killed. This can be done by executing:

 $ pkill audsp

## Server
Install  to use Festival with Speech dispatcher (i.e. with the Listen feature in Firefox's Reader mode).
