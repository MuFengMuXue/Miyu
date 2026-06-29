## Name

systemd-tpm2-clear.service — Request that the TPM security chip is cleared on next boot

## Synopsis

`systemd-tpm2-clear.service`

`/usr/lib/systemd/systemd-tpm2-clear`

## Description

`systemd-tpm2-clear.service` is a service that requests that the TPM is reset by the PC firmware on the next boot. It makes use of the TPM Physical Presence Interface (PPI). Note that this service does not immediately execute the clear operation, but simply asks the PC firmware to execute it at next boot, where the user will be asked for confirmation before the operation is done.

`systemd-tpm2-clear.service` is typically hooked into the `factory-reset.target` unit in order to request the TPM request before an immediate reboot. See Factory Reset for more information.

## Options

The following options are understood:

`--graceful`  
Exit cleanly and execute no operation if the system does not possess a TPM chip.

Added in version 258.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Kernel Command Line

`systemd-tpm2-clear` understands the following kernel command line parameters:

`systemd.tpm2_allow_clear=`  
Takes a boolean argument. If false the service will succeed, but instead of requesting the TPM clear operation from the PC firmware it will not execute any operation. If not specified defaults to true.

Added in version 258.

## See Also

systemd(1), systemd-tpm2-setup.service(8), systemd-factory-reset-request.service(8)
