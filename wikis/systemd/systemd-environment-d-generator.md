## Name

systemd-environment-d-generator, 30-systemd-environment-d-generator — Load variables specified by `environment.d`

## Synopsis

`/usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator`

## Description

`systemd-environment-d-generator` is a systemd.environment-generator(7) that reads environment configuration specified by environment.d(5) configuration files and passes it to the systemd(1) user manager instance.

## See Also

systemd(1), systemctl(1), systemd.environment-generator(7), systemd.generator(7)
