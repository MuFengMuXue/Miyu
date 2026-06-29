# PipeWire Session Manager

The PipeWire Daemon is primarily a framework that allows devices and
applications to exchange data.

It provides the mechanism to do so but the policy deciding which components
can talk to each other and when is controlled by the session manager.  As
outlined in Objects Design, PipeWire provides a media graph
consisting of devices, nodes and ports. The session manager is the one that
decides on the links between those elements.

Two prominent session managers currently exist:

- [PipeWire Media Session](https://gitlab.freedesktop.org/pipewire/media-session), the
example session manager.
- [WirePlumber](https://gitlab.freedesktop.org/pipewire/wireplumber), a
modular session manager based on GObject.
[Documentation](https://pipewire.pages.freedesktop.org/wireplumber/)

This page describes some of the requirements for session managers in general.

# Client Management

PipeWire provides a permission system to limit client's
access to resources but only Access "basic permission
handling". The session manager is expected to decide whether clients may
access specific resources.

# Device Management

PipeWire's responsibility is to open devices, however the decision on which
devices should be opened is the job of a session manager, including the
configuration of those devices.

# Endpoint Grouping

An endpoint is, effectively, a group of nodes that are a logical unit that can
consume or produce media data. For example, a Bluetooth speaker may present as
several nodes but is only one logical unit to stream audio to.

See Objects Design for details on Endpoints.
