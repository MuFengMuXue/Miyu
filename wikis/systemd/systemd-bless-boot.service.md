## Name

systemd-bless-boot.service, systemd-bless-boot — Mark current boot process as successful

## Synopsis

`systemd-bless-boot.service`

`/usr/lib/systemd/systemd-bless-boot`

## Description

`systemd-bless-boot.service` is a system service that marks the current boot process as successful. It's automatically pulled into the initial transaction when systemd-bless-boot-generator(8) detects that systemd-boot(7) style boot counting is used.

Internally, the service operates based on the `LoaderBootCountPath` EFI variable (of the vendor UUID `4a67b082-0a4c-41cf-b6c7-440b29bb8c4f`), which is passed from the boot loader to the OS. It contains a file system path (relative to the EFI system partition) of the UAPI.1 Boot Loader Specification compliant boot loader entry file or unified kernel image file that was used to boot up the system. **systemd-bless-boot.service** removes the two "tries done" and "tries left" numeric boot counters from the filename, which indicates to future invocations of the boot loader that the entry has completed booting successfully at least once. (This service will hence rename the boot loader entry file or unified kernel image file on the first successful boot.)

## Options

The `/usr/lib/systemd/systemd-bless-boot` executable may also be invoked from the command line, taking one of the following command arguments:

`status`  
The current status of the boot loader entry file or unified kernel image file is shown. This outputs one of "`good`", "`bad`", "`indeterminate`", "`clean`", "`dirty`", depending on the state and previous invocations of the command. The string "`indeterminate`" is shown initially after boot, before it has been marked as "good" or "bad". The string "`good`" is shown after the boot was marked as "good" with the `good` command below, and "bad" conversely after the `bad` command was invoked. The string "`clean`" is returned when boot counting is currently not in effect (which includes the case where the current entry was already marked as persistently good). The string "`dirty`" is returned when the system is booted up with a known-bad kernel (i.e. one where the tries left counter has previously reached zero already).

This command is implied if no command argument is specified.

Added in version 240.

`good`  
When invoked, the current boot loader entry file or unified kernel image file will be marked as "good", executing the file rename operation described above. This command is intended to be invoked at the end of a successful boot. The `systemd-bless-boot.service` unit invokes this command.

Added in version 240.

`bad`  
When called the "tries left" counter in the boot loader entry file name or unified kernel image file name is set to zero, marking the boot loader entry or kernel image as "bad", so that the boot loader will not consider it anymore on future boots (at least as long as there are other entries available that are not marked "bad" yet). This command is normally not executed, but can be used to instantly put an end to the boot counting logic if a problem is detected and persistently mark the boot entry as bad.

Added in version 240.

`indeterminate`  
This command undoes any marking of the current boot loader entry file or unified kernel image file as good or bad. This is implemented by renaming the boot loader entry file or unified kernel image file back to the path encoded in the `LoaderBootCountPath` EFI variable. Note that operation will fail if the current kernel is not booted with boot counting enabled (i.e. if the EFI variable is not set). If the boot counter already reached zero tries left on a previous boot this operation will fail too: once an entry is marked `bad` it can only be reset to `good` again, but not to `indeterminate`.

Added in version 240.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## See Also

systemd(1), systemd-boot(7), systemd.special(7)
