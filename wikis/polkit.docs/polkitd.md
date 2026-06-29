# polkitd(8)

## Name
polkitd — The polkit system daemon

## Synopsis
```
polkitd
```

## DESCRIPTION

`polkitd` provides the *org.freedesktop.PolicyKit1* D-Bus service on the system message bus. Users or administrators should never need to start this daemon as it will be automatically started by `dbus-daemon(1)` or `systemd(1)` whenever an application calls into the service.

`polkitd` may be configured via the [`polkitd.conf(5)`](#polkitd.conf.5) configuration file.

`polkitd` can be started as the *polkitd* system user directly, or alternatively it can be started with superuser privileges in which case it will drop privileges early by switching to that same system user.

See the [`polkit(8)`](#polkit.8) man page for more information.

## SEE ALSO

[`polkit(8)`](#polkit.8), [`pkaction(1)`](#pkaction.1), [`pkcheck(1)`](#pkcheck.1), [`pkexec(1)`](#pkexec.1), [`pkttyagent(1)`](#pkttyagent.1), `dbus-daemon(1)`, `systemd(1)`
