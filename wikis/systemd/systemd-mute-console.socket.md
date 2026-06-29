## Name

systemd-mute-console, systemd-mute-console@.service, systemd-mute-console.socket — Temporarily mute kernel log output and service manager status output to the system console

## Synopsis

`systemd-mute-console` \[OPTIONS...\]

`systemd-mute-console@.service`

`systemd-mute-console.socket`

## Description

The **systemd-mute-console** tool and service may be used to temporarily mute the log output of the kernel as well as the status output of the service manager to the system console. It may be used by tools running on the console to ensure their terminal output is not interrupted by unrelated messages.

The tool can be invoked directly in which case it will mute the two outputs and then issue an sd_notify(3) "`READY=1`" notification once that is completed. On `SIGINT` or `SIGTERM` output is unmuted again. Alternatively it can be invoked via Varlink IPC.

## Options

The following options are understood:

`--kernel=`*`bool`*, `--pid1=`*`bool`*  
Individually controls which output to mute. If true is specified the respective output is muted, if false the output is left as is. Defaults to true.

Added in version 259.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## See Also

systemd(1), systemd-firstboot(1)
