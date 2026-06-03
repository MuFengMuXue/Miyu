## Name

systemd-user-sessions.service, systemd-user-sessions — Permit user logins after boot, prohibit user logins at shutdown

## Synopsis

`systemd-user-sessions.service`

`/usr/lib/systemd/systemd-user-sessions`

## Description

`systemd-user-sessions.service` is a service that controls user logins through pam_nologin(8). After basic system initialization is complete, it removes `/run/nologin`, thus permitting logins. Before system shutdown, it creates `/run/nologin`, thus prohibiting further logins.

## See Also

systemd(1), systemd-logind.service(8), pam_nologin(8)
