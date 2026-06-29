# Zeroconf Discover

Use zeroconf to detect and load module-pulse-tunnel with the right
parameters. This will automatically create sinks and sources to stream
audio to/from remote PulseAudio servers. It also works with
module-protocol-pulse.

## Module Name

`libpipewire-module-zeroconf-discover`

## Module Options

- `pulse.discover-local` = allow discovery of local services as well.
   false by default.
- `pulse.latency`: the latency to end-to-end latency in milliseconds to
                   maintain (Default 200ms).

## Example configuration

```
# ~/.config/pipewire/pipewire.conf.d/my-zeroconf-discover.conf

context.modules = [
{   name = libpipewire-module-zeroconf-discover
    args = { }
}
]
```
