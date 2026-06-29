# Pacat

is a simple tool for playing back or capturing raw or encoded audio files on a PulseAudio sound server. It understands all audio file formats supported by .

It is also present under the aliases , , , and .

## Installation
 is installed by default with PulseAudio, as part of the  package.

## Usage
See the  man page for information on 's flags.

*  is equivalent to
*  is equivalent to
*  is equivalent to
*  is equivalent to
* When invoking  directly, the defaults are equivalent to .

To summarize,  and  both record by default, whereas  and  play back by default.  and  both deal with encoded audio, whereas  and  work on raw PCM (and thus can be used in pipelines).

Note that a single instance of  cannot record and play back at the same time; for that, see #Playing back an audio input.

## Select a sink or source
Configuring which sink to play to, or which source to record, can be done using a PulseAudio front-end, or programmatically using the  option.

To list the available sinks:

To list the available sources:

Removing the  keyword produces detailed output about each sink/source.

There are two ways to refer to a given sink/source: either by name, or by ID. Taking the following source list as an example:

Then the following two lines produce the same result.

## Tips and tricks
## Low-latency playback
By default,  lets the PulseAudio server pick the latency, "usually relatively high for power saving reasons". If this is not desirable, for example for #Playing back an audio input, one can pass the  (in bytes) or  option to . For example:

Note that this usually only needs to be done when playing back, not when recording.

## Playing back an audio input
If you are recording an external audio source (for example via a jack male-male cable), you may want to have feedback on what you are recording. This can be done by using  to capture the input, and piping it into  to play it back.

 $ parec | pacat

It may be practical to #Select a sink or source directly, for example:

 $ parec -d 0 | pacat -d 1

It is possible to record the sound at the same time by adding tee to the pipeline:

 $ parec | tee speech.raw | pacat

Though you may want to launch a separate instance of  or  instead.

## Recording from multiple sources
It is possible to record from both sinks and sources in a single command by using the  argument several times. For instance, recording a video conference including the speech of your guests (sink) and your own voice (source) might look like

 $ parec -d alsa_input.pci-0000_00_1f.3.analog-stereo -d alsa_output.pci-0000_00_1f.3.analog-stereo --file-format=wav $(date +%F).wav

## Playing back audio from a remote server
First of all, set up  to your liking, see PulseAudio/Examples#PulseAudio over network.
Then, you can play back the audio from a remote server via:

 $ parec -s 192.168.0.1:4713 | pacat --latency-msec=1
