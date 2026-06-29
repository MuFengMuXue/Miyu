## Name

systemd-pcrphase.service, systemd-pcrphase-sysinit.service, systemd-pcrphase-initrd.service, systemd-pcrmachine.service, systemd-pcrproduct.service, systemd-pcrfs-root.service, systemd-pcrfs@.service, systemd-pcrnvdone.service, systemd-pcrextend — Measure boot phases, machine ID, product UUID and file system identity into TPM PCRs and NvPCRs

## Synopsis

`systemd-pcrphase.service`

`systemd-pcrphase-sysinit.service`

`systemd-pcrphase-initrd.service`

`systemd-pcrmachine.service`

`systemd-pcrproduct.service`

`systemd-pcrfs-root.service`

`systemd-pcrfs@.service`

`systemd-pcrnvdone.service`

`/usr/lib/systemd/systemd-pcrextend` \[*`STRING`*\]

## Description

`systemd-pcrphase.service`, `systemd-pcrphase-sysinit.service`, and `systemd-pcrphase-initrd.service` are system services that measure specific strings into TPM2 PCR 11 during boot at various milestones of the boot process.

`systemd-pcrmachine.service` is a system service that measures the machine ID (see machine-id(5)) into PCR 15.

`systemd-pcrproduct.service` is a system service that measures the firmware product UUID (as provided by one of SMBIOS, Devicetree, …) into a NvPCR named "`hardware`".

`systemd-pcrnvdone.service` is a system service that measures a separator event into PCR 9 once all NvPCRs have completed initialization.

`systemd-pcrfs-root.service` and `systemd-pcrfs@.service` are services that measure file system identity information (i.e. mount point, file system type, label and UUID, partition label and UUID) into PCR 15. `systemd-pcrfs-root.service` does so for the root file system, `systemd-pcrfs@.service` is a template unit that measures the file system indicated by its instance identifier instead.

These services require systemd-stub(7) to be used in a unified kernel image (UKI). They execute no operation when the stub has not been used to invoke the kernel. The stub will measure the invoked kernel and associated vendor resources into PCR 11 before handing control to it; once userspace is invoked these services then will extend TPM2 PCR 11 with certain literal strings indicating phases of the boot process. During a regular boot process PCR 11 is extended with the following strings:

1.  "`enter-initrd`" — early when the initrd initializes, before activating system extension images for the initrd. It acts as a barrier between the time where the kernel initializes and where the initrd starts operating and enables system extension images, i.e. code shipped outside of the UKI. (This extension happens when the systemd-pcrphase-initrd.service(8) service is started.)

2.  "`leave-initrd`" — when the initrd is about to transition into the host file system. It acts as barrier between initrd code and host OS code. (This extension happens when the systemd-pcrphase-sysinit.service(8) service is stopped.)

3.  "`sysinit`" — when basic system initialization is complete (which includes local file systems having been mounted), and the system begins starting regular system services. (This extension happens when the systemd-pcrphase-sysinit.service(8) service is started.)

4.  "`ready`" — during later boot-up, after remote file systems have been activated (i.e. after `remote-fs.target`), but before users are permitted to log in (i.e. before `systemd-user-sessions.service`). It acts as barrier between the time where unprivileged regular users are still prohibited to log in and where they are allowed to log in. (This extension happens when the systemd-pcrphase-sysinit.service(8) service is started.)

5.  "`shutdown`" — when the system shutdown begins. It acts as barrier between the time the system is fully up and running and where it is about to shut down. (This extension happens when the `systemd-pcrphase.service` service is stopped.)

6.  "`final`" — at the end of system shutdown. It acts as barrier between the time the service manager still runs and when it transitions into the final shutdown phase where service management is not available anymore. (This extension happens when the systemd-pcrphase-sysinit.service(8) service is stopped.)

During a regular system lifecycle, PCR 11 is extended with the strings "`enter-initrd`", "`leave-initrd`", "`sysinit`", "`ready`", "`shutdown`", and "`final`".

Specific phases of the boot process may be referenced via the series of strings measured, separated by colons (the "phase path"). For example, the phase path for the regular system runtime is "`enter-initrd:leave-initrd:sysinit:ready`", while the one for the initrd is just "`enter-initrd`". The phase path for the boot phase before the initrd is an empty string; because that's hard to pass around a single colon ("`:`") may be used instead. Note that the aforementioned six strings are just the default strings and individual systems might measure other strings at other times, and thus implement different and more fine-grained boot phases to bind policy to.

By binding policy of TPM2 objects to a specific phase path it is possible to restrict access to them to specific phases of the boot process, for example making it impossible to access the root file system's encryption key after the system transitioned from the initrd into the host root file system.

Use systemd-measure(1) to pre-calculate expected PCR 11 values for specific boot phases (via the `--phase=` switch).

`systemd-pcrfs-root.service` and `systemd-pcrfs@.service` are automatically pulled into the initial transaction by systemd-gpt-auto-generator(8) for the root and `/var/` file systems. systemd-fstab-generator(8) will do this for all mounts with the `x-systemd.pcrfs` mount option in `/etc/fstab`.

## Options

The `/usr/lib/systemd/system-pcrextend` executable may also be invoked from the command line, where it expects the word to extend into a PCR or NvPCR, as well as the following switches:

`--bank=`  
Takes the PCR banks to extend the specified word into. If not specified, the tool automatically determines all enabled PCR banks and measures the word into all of them.

Added in version 252.

`--pcr=`  
Takes the index of the PCR to extend. If `--machine-id` or `--file-system=` are specified defaults to 15, otherwise (and unless `--product-id` is specified) defaults to 11. May not be combined with `--nvpcr=`.

Added in version 255.

`--nvpcr=`  
Takes a name of an NvPCR to extend. NvPCRs are additional PCRs implemented via TPM NV indexes. The name should be a short string such as "`hardware`" or "`disk-encryption`". If `--product-id` is specified defaults "`hardware`". May not be combined with `--pcr=`.

Added in version 259.

`--tpm2-device=`*`PATH`*  
Controls which TPM2 device to use. Expects a device node path referring to the TPM2 chip (e.g. `/dev/tpmrm0`). Alternatively the special value "`auto`" may be specified, in order to automatically determine the device node of a suitable TPM2 device (of which there must be exactly one). The special value "`list`" may be used to enumerate all suitable TPM2 devices currently discovered.

Added in version 252.

`--graceful`  
If no TPM2 firmware, kernel subsystem, kernel driver or device support is found, exit with exit status 0 (i.e. indicate success). If this is not specified, any attempt to measure without a TPM2 device will cause the invocation to fail.

Added in version 253.

`--early`  
Selects early-boot mode. Specifically this means that the NvPCR anchor secret is not attempted to be written into `/var/lib/` and the boot loader partition in addition to `/run/`. (Unlike the latter the former are generally not mounted and writable during early boot or in the initrd.)

Added in version 259.

`--machine-id`  
Instead of measuring a word specified on the command line into PCR 11, measure the host's machine ID into PCR 15.

Added in version 253.

`--product-id`  
Instead of measuring a word specified on the command line into PCR 11, measure the firmware's product UUID into an NvPCR named "`hardware`".

Added in version 259.

`--file-system=`  
Instead of measuring a word specified on the command line into PCR 11, measure identity information of the specified file system into PCR 15. The parameter must be the path to the established mount point of the file system to measure.

Added in version 253.

`--event-type=`  
Set the event log event type for this measurement. Pass "`help`" for a list of currently defined identifiers. Defaults to an appropriate value for `--machine-id`, `--product-id`, `--file-system=`, and otherwise to "`phase`".

Added in version 259.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Files

`/run/log/systemd/tpm2-measure.log`  
Measurements are logged into an event log file maintained in `/run/log/systemd/tpm2-measure.log`, which contains a JSON-SEQ series of objects that follow the general structure of the TCG Canonical Event Log Format (CEL-JSON) event objects (but lack the "`recnum`" field).

A `LOCK_EX` BSD file lock (flock(2)) on the log file is acquired while the measurement is made and the file is updated. Thus, applications that intend to acquire a consistent quote from the TPM with the associated snapshot of the event log should acquire a `LOCK_SH` lock while doing so.

Added in version 252.

`/usr/lib/nvpcr/*.nvpcr`  
Definition files for NvPCRs.

Added in version 259.

## See Also

systemd(1), systemd-stub(7), systemd-measure(1), systemd-gpt-auto-generator(8), systemd-fstab-generator(8), TPM2 PCR Measurements Made by systemd
