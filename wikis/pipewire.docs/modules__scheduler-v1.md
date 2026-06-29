# SchedulerV1

## Module Name

`libpipewire-module-scheduler-v1`

## Module Options

Options specific to the behavior of this module

## General options

Options with well-known behavior:

## Config override

A `module.scheduler-v1.args` config section can be added
to override the module arguments.

```
# ~/.config/pipewire/pipewire.conf.d/my-scheduler-v1-args.conf

module.scheduler-v1.args = {
}
```

## Example configuration

```
context.modules = [
 {   name = libpipewire-module-scheduler-v1
     args = {
     }
 }
]
```

Since: 1.7.0
