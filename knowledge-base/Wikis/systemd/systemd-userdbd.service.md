## Name

systemd-userdbd.service, systemd-userdbd — JSON User/Group Record Query Multiplexer/NSS Compatibility

## Synopsis

`systemd-userdbd.service`

`/usr/lib/systemd/systemd-userdbd`

## Description

**systemd-userdbd** is a system service that multiplexes user/group lookups to all local services that provide JSON user/group record definitions to the system. In addition it synthesizes JSON user/group records from classic UNIX/glibc NSS user/group records in order to provide full backwards compatibility. It may also pick up statically defined JSON user/group records from files in `/etc/userdb/`, `/run/userdb/`, `/run/host/userdb/` and `/usr/lib/userdb/` with the "`.user`" or "`.group`" extension. For more details about the extensions read the nss-systemd(8) manpage.

Most of **systemd-userdbd**'s functionality is accessible through the userdbctl(1) command.

The user and group records this service provides access to follow the JSON User Records and JSON Group Record definitions. This service implements the User/Group Record Lookup API via Varlink, and multiplexes access other services implementing this API, too. It is thus both server and client of this API.

This service provides three distinct Varlink services: `io.systemd.Multiplexer` provides a single, unified API for querying JSON user and group records. Internally it talks to all other user/group record services running on the system in parallel and forwards any information discovered. This simplifies clients substantially since they need to talk to a single service only instead of all of them in parallel. `io.systemd.NameServiceSwitch` provides compatibility with classic UNIX/glibc NSS user records, i.e. converts struct passwd and struct group records as acquired with APIs such as getpwnam(1) to JSON user/group records, thus hiding the differences between the services as much as possible. `io.systemd.DropIn` makes JSON user/group records from the aforementioned drop-in directories available.

## See Also

systemd(1), nss-systemd(8), userdbctl(1), systemd-homed.service(8)
