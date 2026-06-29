## Name

systemd-getty-generator — Generator for enabling getty instances on the console

## Synopsis

`/usr/lib/systemd/system-generators/systemd-getty-generator`

## Description

`systemd-getty-generator` is a generator that automatically instantiates `serial-getty@.service` on the kernel consoles, if they can function as ttys and are not provided by the virtual console subsystem. It will also instantiate `serial-getty@.service` instances for virtualizer consoles, if execution in a virtualized environment is detected. If execution in a container environment is detected, it will instead enable `console-getty.service` for `/dev/console`, and `container-getty@.service` instances for additional container pseudo TTYs as requested by the container manager (see `Container Interface`). This should ensure that the user is shown a login prompt at the right place, regardless of which environment the system is started in. For example, it is sufficient to redirect the kernel console with a kernel command line argument such as `console=` to get both kernel messages and a getty prompt on a serial TTY. See The kernel's command-line parameters for more information on the `console=` kernel parameter.

`systemd-getty-generator` implements systemd.generator(7).

Further information about configuration of gettys can be found in systemd for Administrators, Part XVI: Gettys on Serial Consoles (and Elsewhere).

## Kernel Command Line

`systemd-getty-generator` understands the following kernel-command-line(7) parameters:

`systemd.getty_auto=`  
This kernel command line option may be used to control the execution mode of the generator. Takes an optional boolean argument. Since v258, this also takes comma-separated list of special values: "`credential`", "`container`", "`console`", and "`builtin`".

When "`credential`" is specified, the two credentials `getty.ttys.serial` and `getty.ttys.container` will be parsed. See System Credentials section below for more details.

When "`container`" is specified, `console-getty.service` and `container-getty@.service` will be enabled when the system is running in a container. This option will be ignored when the system is not in a container.

When "`console`" is specified, `serial-getty@.service` for active kernel consoles will be enabled. This option will be ignored when the system is running in a container.

When "`builtins`" is specified, `serial-getty@.service` for available virtualizer consoles will be enabled. This option will be ignored when the system is running in a container.

When yes, the above four options will be enabled. When no, all options are disabled and no service will be enabled. When the kernel command line option is specified without an argument, defaults to yes. The generator is enabled by default, and a false value may be used to disable it.

Added in version 250.

## Environment

`$SYSTEMD_GETTY_AUTO`  
This environment variable may be used to control the execution mode of the generator. Takes the same value as `systemd.getty_auto=` kernel command line option.

Added in version 250.

## System Credentials

`getty.auto`  
The system credential may be used to control the execution mode of the generator. Takes the same value as `systemd.getty_auto=` kernel command line option.

Added in version 258.

`getty.ttys.serial`, `getty.ttys.container`  
These system credentials may be used to spawn additional login prompts on selected TTYs. The two credentials should contain a newline-separated list of TTY names to spawn instances of `serial-getty@.service` (in case of `getty.ttys.serial`) and `container-getty@.service` (in case of `getty.ttys.container`) on. Any lines starting with a "`#`" will be ignored.

Added in version 254.

## See Also

systemd(1), kernel-command-line(7), systemd.system-credentials(7), agetty(8)
