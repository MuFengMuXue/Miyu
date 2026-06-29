# Rosegarden

Rosegarden is a digital audio workstation program written in Qt. It acts as an audio and MIDI sequencer, scorewriter and musical composition and editing tool. It is intended to be a free alternative to such applications as Cubase.

## Installation
Install the  package. Be sure to install a MIDI setup first.

## Configuration
## Customizing keyboard shortcuts
The keyboard shortcuts in rosegarden can be customized by editing a set of XML configuration files. The first step is to download the default configuration files which are packaged with the source code, and place them in . A simple way of doing this is to run:

 $ cd ~/.local/share/rosegarden
 $ svn co http://svn.code.sf.net/p/rosegarden/code/trunk/rosegarden/data/rc

which will get the configuration files from the development branch of the source code.

Keyboard shortcuts can then be set or modified by editing the appropriate file in . For example, in order to map the  bar to play/pause, edit the following lines of :

## Usage
## With Timidity and PulseAudio
Launch Timidity as a daemon before launching Rosegarden:

 $ timidity -iA

This way, Rosegarden will not launch jackd and you will still be able to hear sound from other running applications.
