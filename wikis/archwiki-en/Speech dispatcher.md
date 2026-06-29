# Speech dispatcher

Speech Dispatcher is a device independent layer for speech synthesis that provides a common easy to use interface for both client applications (programs that want to speak) and for software synthesizers (programs actually able to convert text to speech).

It is a part of the Free(b)soft project, which is intended to allow blind and visually impaired people to work with computer and Internet based on free software.

## Installation
Install the  package. Next, install one of several supported speech synthesizers.

To use Festival, install . Follow configuration instructions in the dedicated section below.

To use a modern neural text to speech system Piper, install  and one of the voice packages for your language, e.g. . Configure speech dispatcher to use Piper as described in the dedicated section below. Alternatively to the above AUR packages, Piper along with voices and the speech dispatcher configuration may be installed using Pied, an automated graphical installer distributed via Flatpak.

To use eSpeak NG, install  and enable the service. Follow configuration instructions in the section below.

## Configuration
The main configuration file is located at  however speech-dispatcher is usually run on a per user basis to allow for multiple users to have differing preferences. User configuration files are stored at . There is also support to allow different speech synthesis engine clients to have their own configurations too.

Use the included spd-conf tool to change configuration options. By default it will run in interactive mode and ask you a series of questions in order to generate the type of file you require. It is recommended that you create a per user configuration unless you are absolutely sure you will be the only user. Altering the system configuration requires root permissions.

## Basic configuration
To use interactive mode and answer questions about what you need run the following:

 $ spd-conf

To create a per user configuration run the following:

 $ spd-conf -uc

To edit the system wide configuration file run the following:

 # spd-conf -C

## Festival specific
If you intend to use Festival as your speech synthesis engine then you should also do the following:

 $ $EDITOR ~/.config/speech-dispatcher/speechd.conf

Find and uncomment (by removing the  from in front of it) the line:

Then save the file.

## Piper specific
Speech dispatcher supports Piper only through a generic interface module that interacts through a custom shell command. An audio player is necessary for this. For PipeWire, use pw-play from ; for PulseAudio, use paplay; for ALSA, use aplay from .

Test your player before putting it into the configuration file. You may get a bogus "dummy module" error or no voice output if your player doesn't work:

 $ echo "Arch Linux is the best" | piper-tts -q -m "/usr/share/piper-voices/en/en_US/ryan/high/en_US-ryan-high.onnx" -f - | your-audio-player

In your user's speech-dispatcher configuration file (see earlier section for how to create it), add the module and configuration file for Piper:

Create the following module configuration file for Piper. In the shell command, edit the path to the model for your desired voice among those in , and the audio player appropriate for your audio back-end:

The shell command needs to filter out the newlines, since  exits on newline. To accomplish this, the input text, which speech-dispatcher substitutes into the shell command as a literal string in place of the  placeholder string, is first assigned to an environment variable, the contents of the variable is then piped into  for substitution of the newline character with a space.

A multi-voice setup can be realized utilizing the  variable. The following example assumes the appropriate  and  files are placed in a flat directory:

 is equal to the third argument provided to  - considered "name" of the voice - and must match the  filename. If a client does not explicitly specify a voice then  equals . Set  as a fallback to catch that situation.

## Socket activation
Speech Dispatcher from version 0.12.0 onwards allows activation via socket. This feature allows Flatpak applications such as Foliate, for example, to use the text-to-speech feature using Speech Dispatcher. To initialize the socket, start the  user unit, which you can also enable so that the socket is always available at system startup.

## Usage
Using speech-dispatcher directly is not a common scenario as its intended to provide an access layer to other speech synthesis engines, that said you can interact with it directly by using the included spd-say binary as follows:

 $ spd-say "Arch Linux is the best"

The Firefox browser is one of the applications that supports speech-dispatcher. Switch to reader view () and a button for narration (headphones icon) should be visible in the small menu. You may need to restart Firefox whenever speech-dispatcher daemon is started or restarted.

The Okular PDF viewer also supports speech-dispatcher. Select text in Text Selection mode, right-click it, and choose Speak Text, or choose Speak Current Page in the Tools menu. You may need to restart Okular whenever speech-dispatcher daemon is started or restarted.

## Troubleshooting
## Logs
Speech-dispatcher writes very little to the system journal, however it does write useful information to its own logs.  You can find the location of these in the output of this command:

 $ /usr/bin/speech-dispatcher -l 3

## Spd-conf tests
 contains a routine to test the operation of speech-dispatcher, you can run it with the following command:

 $ spd-conf -d

Or use the following to get a very verbose log dump:

 $ spd-conf -D

Other tests are available, for example testing ALSA, PulseAudio and Festival, to see a full list of available options run the following:

 $ spd-conf --help

Most of the available tests will run as part of the test routine.

## Speech-dispatcher fails to start
The tests above won't work if speech-dispatcher fails to start.  If you want more information than is in the logs you can attempt to start the server like this:

 $ /usr/bin/speech-dispatcher -l 3

This will output information about the startup process to the terminal.

## Using TTS causes the dummy output module to speak an error message
This happens when speech dispatcher cannot connect to the speech synthesis engine. If you are using Festival then it needs to be running as a server, this can be achieved with the following command:

 $ festival --server &
