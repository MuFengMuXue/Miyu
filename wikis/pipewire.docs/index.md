# PipeWire

PipeWire is low-level multimedia framework that provides:

- Graph based processing.
- Support for out-of-process processing graphs with minimal overhead.
- Flexible and extensible media format negotiation and buffer allocation.
- Hard real-time capable plugins.
- Very low-latency for both audio and video processing.

See Overview for an overview of PipeWire and Design
for the design principles guiding PipeWire.

# Documentation

- Configuration
- Programs
- Modules
- Pulseaudio Modules

See our [Wiki](https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/home) for
more information on how to configure and use PipeWire.

# Components

PipeWire ships with the following components:

- A PipeWire Daemon that implements the IPC and graph processing.
- An example PipeWire Session Manager that manages objects in the PipeWire Daemon.
- A set of Programs to introspect and use the PipeWire Daemon.
- A PipeWire Library to develop PipeWire applications and plugins (tutorial).
- The SPA (Simple Plugin API) used by both the PipeWire Daemon and in the PipeWire Library.

# API Documentation

See PipeWire API.

# Resources

- [PipeWire and AGL](https://wiki.automotivelinux.org/_media/pipewire_agl_20181206.pdf)
- [LAC 2020 Paper](https://lac2020.sciencesconf.org//data/proceedings.pdf) and
   [Video](https://tube.aquilenet.fr/w/uy8PJyMnBrpBFNEZ9D48Uu)
- [PipeWire Under The Hood](https://venam.nixers.net/blog/unix/2021/06/23/pipewire-under-the-hood.html)
- [PipeWire: The Linux audio/video bus (LWN)](https://lwn.net/Articles/847412)
- [PipeWire Wikipedia](https://en.wikipedia.org/wiki/PipeWire)
- [Bluetooth, PipeWire and Whatsapp calls](https://gjhenrique.com/pipewire.html)
- [Intoduction to PipeWire](https://bootlin.com/blog/an-introduction-to-pipewire/)
- [A custom PipeWire node](https://bootlin.com/blog/a-custom-pipewire-node/)
- [FOSDEM 2025 talk and slides](https://fosdem.org/2025/schedule/event/fosdem-2025-4749-pipewire-state-of-the-union/)
