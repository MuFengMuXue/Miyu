## Name

systemd-factory-reset-generator — Pull `factory-reset-now.target` into the initial boot transaction when factory reset has been requested

## Synopsis

`/usr/lib/systemd/system-generators/systemd-factory-reset-generator`

## Description

`systemd-factory-reset-generator` is a generator that pulls `factory-reset-now.target` into the initial boot transaction when the factory reset operation has been requested, either via the `systemd.factory_reset=` kernel command line option or via the `FactoryResetRequest` EFI variable.

`systemd-factory-reset-generator` implements systemd.generator(7).

## See Also

systemd(1), systemd-factory-reset(8), Factory Reset
