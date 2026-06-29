# Modules

A PipeWire module is effectively a PipeWire client in an `.so` file that
shares the pw_context with the loading entity. Usually modules are
loaded when they are listed in the configuration files. For example the
default configuration file loads several modules:

```
context.modules = [
    ...
    # The native communication protocol.
    {   name = libpipewire-module-protocol-native }

    # The profile module. Allows application to access profiler
    # and performance data. It provides an interface that is used
    # by pw-top and pw-profiler.
    {   name = libpipewire-module-profiler }

    # Allows applications to create metadata objects. It creates
    # a factory for Metadata objects.
    {   name = libpipewire-module-metadata }

    # Creates a factory for making devices that run in the
    # context of the PipeWire server.
    {   name = libpipewire-module-spa-device-factory }
    ...
]
```
The matching libraries are:
```
$ ls -1 /usr/lib64/pipewire-0.3/libpipewire-module*
...
/usr/lib64/pipewire-0.3/libpipewire-module-metadata.so
/usr/lib64/pipewire-0.3/libpipewire-module-profiler.so
/usr/lib64/pipewire-0.3/libpipewire-module-protocol-native.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-device-factory.so
...
```

A module's entry point is the `pipewire__module_init` function, see PIPEWIRE_SYMBOL_MODULE_INIT.

```
int pipewire__module_init(struct pw_impl_module *module, const char *args).`
```

See the Example Sink and Example Source
modules for a general oveview of how modules look like.

List of known modules:

- Access
- Adapter
- AVB
- Client Device
- Client Node
- Combine Stream
- Echo Cancel
- Example Filter
- Example Sink
- Example Source
- Fallback Sink
- FFADO firewire audio driver
- Filter-Chain
- JACK DBus detect
- JACK Tunnel
- Link Factory
- Loopback
- Metadata
- Netjack2 driver
- Netjack2 manager
- Parametric-Equalizer
- Unix Pipe Tunnel
- Portal
- Profiler
- Protocol Native
- Protocol Pulse
- Protocol Simple
- Pulse Tunnel
- AirPlay Sink
- RAOP Discover
- ROC sink
- ROC source
- SchedulerV1
- SAP Announce and create RTP streams
- RTP sink
- RTP source
- RTP session
- RT
- SPA Node
- SPA Node factory
- SPA Device
- SPA Device factory
- sendspin receiver
- sendspin sender
- Session Manager
- Snapcast Discover
- VBAN receiver
- VBAN sender
- X11 Bell
- Zeroconf Discover
