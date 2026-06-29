# RT

The `rt` modules can give real-time priorities to processing threads.

It uses the operating system's scheduler to enable realtime scheduling
for certain threads to assist with low latency audio processing.
This requires `RLIMIT_RTPRIO` to be set to a value that's equal to this
module's `rt.prio` parameter or higher. Most distros will come with some
package that configures this for certain groups or users. If this is not set
up and DBus is available, then this module will fall back to using the Portal
Realtime DBus API or RTKit.

## Module Name

`libpipewire-module-rt`

## Module Options

- `nice.level`: The nice value set for the application thread. It improves
                performance of the communication with the pipewire daemon.
- `rt.prio`: The realtime priority of the data thread. Higher values are
             higher priority.
- `rt.time.soft`, `rt.time.hard`: The amount of CPU time an RT thread can
             consume without doing any blocking calls before the kernel kills
             the thread. This is a safety measure to avoid lockups of the complete
             system when some thread consumes 100%.
- `rlimits.enabled`: enable the use of rtlimits, default true.
- `rtportal.enabled`: enable the use of realtime portal, default true
- `rtkit.enabled`: enable the use of rtkit, default true
- `uclamp.min`: the minimum utilisation value the scheduler should consider
- `uclamp.max`: the maximum utilisation value the scheduler should consider

The nice level is by default set to an invalid value so that clients don't
automatically have the nice level raised.

The PipeWire server processes are explicitly configured with a valid nice level.

## Config override

A `module.rt.args` config section can be added
to override the module arguments.

```
# ~/.config/pipewire/pipewire.conf.d/my-rt-args.conf

module.rt.args = {
    #nice.level = 22
}
```

## Example configuration

```
context.modules = [
{   name = libpipewire-module-rt
    args = {
        #nice.level   = 20
        #rt.prio      = 88
        #rt.time.soft = -1
        #rt.time.hard = -1
        #rlimits.enabled = true
        #rtportal.enabled = true
        #rtkit.enabled = true
        #uclamp.min = 0
        #uclamp.max = 1024
    }
    flags = [ ifexists nofail ]
}
]
```
