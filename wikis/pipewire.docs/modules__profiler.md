# Profiler

The profiler module provides a Profiler interface for applications that
can be used to receive profiling information.

Use tools like pw-top and pw-profiler to collect profiling information
about the pipewire graph.

## Module Name

`libpipewire-module-profiler`

## Module Options

- `profile.interval.ms`: Can be used to avoid gathering profiling information
			    on every processing cycle. This allows trading off
			    CPU usage for profiling accuracy. Default 0

## Config override

A `module.profiler.args` config section can be added
to override the module arguments.

```
# ~/.config/pipewire/pipewire.conf.d/my-profiler-args.conf

module.profiler.args = {
    #profile.interval.ms = 10
}
```

## Example configuration

The module is usually added to the config file of the main pipewire daemon.

```
context.modules = [
{ name = libpipewire-module-profiler
  args = {
      #profile.interval.ms = 0
  }
}
]
```

## See also

- `pw-top`: a tool to display realtime profiler data
- `pw-profiler`: a tool to collect and render profiler data
