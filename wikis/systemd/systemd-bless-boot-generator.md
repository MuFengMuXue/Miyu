## Name

systemd-bless-boot-generator — Pull `systemd-bless-boot.service` into the initial boot transaction when boot counting is in effect

## Synopsis

`/usr/lib/systemd/system-generators/systemd-bless-boot-generator`

## Description

`systemd-bless-boot-generator` is a generator that pulls `systemd-bless-boot.service` into the initial boot transaction when boot counting, as implemented by systemd-boot(7), is enabled.

`systemd-bless-boot-generator` implements systemd.generator(7).

## See Also

systemd(1), systemd-bless-boot.service(8), systemd-boot(7)
