## Name

systemd-boot-clear-sysfail.service — Clear LoaderEntrySysFail entry

## Synopsis

`systemd-boot-clear-sysfail.service`

## Description

`systemd-boot-clear-sysfail.service` is a system service that automatically clears the 'LoaderEntrySysFail' boot loader entry if the boot was successful and the 'LoaderSysFailReason' EFI variable, which indicates the reason for the system failure, is not set.

The `systemd-boot-clear-sysfail.service` unit invokes the **bootctl --graceful set-sysfail ""** command, which clears the LoaderEntrySysFail entry. The service is conditionalized so that it is run only when a LoaderSysFailReason entry is not set.

For further details see bootctl(1), regarding the command this service invokes.

## See Also

systemd(1), bootctl(1), systemd-boot(7)
