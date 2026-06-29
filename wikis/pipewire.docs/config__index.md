# Configuration

One of the design goals of PipeWire is to be able to closely control
and configure all aspects of the processing graph.

A fully configured PipeWire setup runs various pieces, each with their
configuration options and files:

- **pipewire**: The PipeWire main daemon that runs and coordinates the processing.

- **pipewire-pulse**: The PipeWire PulseAudio replacement server. It also configures
  the properties of the PulseAudio clients connecting to it.

- **wireplumber**: Most configuration of devices is performed by the session manager.
  It typically loads ALSA and other devices and configures the profiles, port volumes and more.
  The session manager also configures new clients and links them to the targets, as configured
  in the session manager policy.

- **PipeWire clients**: Each native PipeWire client also loads a configuration file.
  Emulated JACK client also have separate configuration.

# Configuration Settings

Configuration of daemons:

- PipeWire daemon configuration reference
- PipeWire Pulseaudio daemon configuration reference
- [WirePlumber daemon configuration](https://pipewire.pages.freedesktop.org/wireplumber/)

Configuration of devices:

- [WirePlumber configuration](https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration.html)
- Object property reference
- Configuration Index

Configuration for client applications, either connecting via the
native PipeWire interface, or the emulated ALSA, JACK, or PulseAudio
interfaces:

- PipeWire native and ALSA client configuration reference
- PipeWire JACK client configuration reference
- PipeWire Pulseaudio client configuration reference

# Manual Pages

- pipewire.conf
- client.conf
- pipewire-pulse.conf
- jack.conf
- filter-chain.conf
- pipewire-props
- pipewire-pulse-modules
- libpipewire-modules
