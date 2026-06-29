# Mbrola

mbrola is a non-free phonemes-to-audio program to use with text-to-speech applications. It is free to use for non-commercial, non-military applications.

## Installation
Install the  package.

## Add voices
Packages named mbrola-voices-xxx are available in the AUR.

## Testing
Once you have installed the wanted voice(s) go to the directory of the installed language:

 $ cd /usr/share/mbrola/us1/

then list the test files:

 $ ls test/

If there are no test files for this language, try with another language or skip to #Install a text-to-phonemes program.

Else choose a test file (files with .pho extension) and try:

 $ mbrola ./us1 ./test/mbrola.pho ~/test.wav; aplay ~/test.wav; rm ~/test.wav

If the installation worked ok, you should hear the voice now.

Note that we this test did not give a text file to mbrola but a phoneme file. To make it a text-to-speech system, see below.

## Install a text-to-phonemes program
To obtain a full TTS system we need a text-to-phonemes program compatible with mbrola: List of TTS programs compatible with mbrola.
