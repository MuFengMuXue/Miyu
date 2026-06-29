## Name

systemd-tpm2-generator — Generator for inserting TPM2 synchronization point in the boot process

## Synopsis

`/usr/lib/systemd/system-generators/systemd-tpm2-generator`

## Description

**systemd-tpm2-generator** is a generator that adds a `Wants=` dependency from `sysinit.target` to `tpm2.target` when it detects that the firmware discovered a TPM2 device but the OS kernel so far did not. `tpm2.target` is supposed to act as synchronization point for all services that require TPM2 device access. See systemd.special(7) for details.

The `systemd.tpm2_wait=` kernel command line option may be used to override behaviour of the generator. It accepts a boolean value: if true then `tpm2.target` will be added as synchronization point even if the firmware has not detected a TPM2 device. If false, the target will not be inserted even if firmware reported a device but the OS kernel does not expose a device for it yet. The latter might be useful in environments where a suitable TPM2 driver for the available hardware is not available.

**systemd-tpm2-generator** implements systemd.generator(7).

## See Also

systemd(1), systemd.special(7), kernel-command-line(7)
