# Shairport Sync

Shairport Sync is an AirPlay audio player — it plays audio streamed from iTunes, iOS devices and third-party AirPlay sources such as ForkedDaapd and others. Audio played by a Shairport Sync-powered device stays synchronised with the source and hence with similar devices playing the same source. In this way, synchronised multi-room audio is possible without difficulty.

Shairport Sync does not support AirPlay video or photo streaming.

Shairport Sync is a fork of the original Shairport which was based on reverse-engineering Apple's key used in its AirPort Express. Be advised that this functionality may be removed at Apple's discretion.

## Installation
Install the  package.

## Configuration
The configuration file can be found at . It contains useful comments and configuration hints. More documentation is available in the README file.

## Audio backend
Shairport Sync works well with PulseAudio, while the timing information is not as accurate as that of ALSA or sndio, it is often impractical to remove or disable PulseAudio. In that case, the pa backend can be used.If you would like to change the backend, check the list of output devices, e.g. by using tools from , and look at the raw audio device, like:

Then add the device name:

{{hc|/etc/shairport-sync.conf|2=
// These are parameters for the "alsa" audio back end.
// For this section to be operative, Shairport Sync must be built with the following configuration flag:
// --with-alsa
alsa =
{
    output_device = "sysdefault";
}
}}

## System service
## Starting
Start/enable .

## Daemon Setup
If you want to run shairport-sync as a daemon you will need to have a folder created in  which is a tempfs by default in Arch Linux. To have a folder created automatically on boot create a tempfiles configuration file, for example:

you can now use  to run shairport-sync as a daemon, and  to kill the daemon.

## User service
According to the [https://github.com/mikebrady/shairport-sync/issues/471#issuecomment-394089069 author, the PulseAudio backend with the default PulseAudio configuration can only work as a user service. As of 2022-01-27, it seems to just work as a system service with pulseaudio (pipewire-pulse) without modification, not needing the user service.

To run shairport-sync as user daemon, you can add it to the desktop environment autostart, or enable  as a  user unit.

Next, edit  and comment out the next lines:

 ...
 #Requires=avahi-daemon.service
 #After=avahi-daemon.service
 ...
 [Service
 ...
 #User=shairport-sync
 #Group=shairport-sync
 ...

Now, you are ready to enable/start  as user:

To obtain logs, use the journal or check the unit status.
