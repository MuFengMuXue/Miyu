# Guitarix

Guitarix is a free and open source software virtual guitar amplifier for Linux. Though originally created to be used with the JACK Audio Connection Kit, it is compatible with PipeWire.

Guitarix takes the signal from a guitar like a real amp, as a mono-signal from a sound card. The input is processed by a main amp and a rack-section. Both can be routed separately and deliver a processed stereo-signal via native JACK or via the new low-level multimedia framework PipeWire. The signal is processed with minimum latency, taking less than 10ms to be processed.

It includes a rack, that can be filled with effects from more than 25 built-in modules including, from a simple noise gate to brain-slashing modulation f/x like flanger, phaser or auto-wah.

## Hardware requirements
In order to use Guitarix, users need to connect the guitar cable into an audio interface. The audio interface converts the audio signal coming from the guitar pickups into a digital signal, then, through an USB-A or USB-C, depending on the interface model, it sends it into the computer. An audio server then is used to send the signal into Guitarix, to allow the use of effects.

## Installation
Install the  package. For a set of extra lv2 plugins for Guitarix, install .
The  package provides extra VST3 plugins to be used with Guitarix.

## Audio server configuration
Since Guitarix interacts with JACK to provide real-time, low-latency audio, users can either use native JACK, or use PipeWire.

## JACK-only
To use it with JACK, install JACK and follow the Professional audio#JACK-only section.

## PipeWire-only
Install PipeWire and follow the Professional audio#PipeWire-only section.

PipeWire provides JACK compatibility through , which can be used with  to create the correct audio routing, manage virtual wiring and sinks. for Guitarix, it will allow to route the audio coming from an audio interface into Guitarix, then to the system speakers.

## System configuration
Before start using Guitarix, users should follow Professional audio#Optimizing system configuration and apply the required system optimizations. The following section resumes it as follows:

## Groups
In order to ensure a low latency for the current user, the user must be a member of the  and  groups.
Install the  package, then add your user to these groups.

## Latency
To reduce the audio latency, copy PipeWire configuration files from  to the user location  and edit :

{{hc|~/.config/pipewire/jack.conf|2=
# global properties for all jack clients

jack.properties = {
    node.latency       = 128/48000
}
}}

## Ulimit
By default, ulimit value is not set to . Therefore, users may find themselves with:

 init *** mlockall failed

This can be fixed by creating an exception rule.

Create/edit the file , and add:

 @audio   -  rtprio     95
 @audio   -  memlock    unlimited

Add your user to the  group and reboot to apply the changes.

## QPWGraph
QPWGraph is a Qt-based Graph/Patchbay for PipeWire, inspired by the JACK tool QjackCtl. It allows to save and manage and route wire sets. For Guitarix, it helps with routing the audio signals from the audio interface.

## Installation
Install the  package.

## Configuration with Guitarix
Run QPWGraph and Guitarix. then, pipe the output of your audio interface to the input of Guitarix and the output of Guitarix to the input of your speakers by dragging the virtual wiring. Once done, you should now be able to play your guitar and hear the audio being routed from Guitarix to your speakers.

## Troubleshooting
