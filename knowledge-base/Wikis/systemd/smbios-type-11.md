## Name

smbios-type-11 — SMBIOS Type 11 strings

## Synopsis

`/sys/firmware/dmi/entries/11-*/raw`

## Description

Various OS components process SMBIOS Type 11 vendor strings that a virtual machine manager (VMM) may set and a virtual machine (VM) receives. SMBIOS Type 11 vendor strings may play a similar role as kernel-command-line(7) parameters but generally are under control of the VMM rather than the boot loader or UKI.

For details on SMBIOS Type 11 see the System Management BIOS specifications.

## Strings

The following strings are supported:

`io.systemd.credential:`*`CREDENTIAL=VALUE`*, `io.systemd.credential.binary:`*`CREDENTIAL=VALUE`*  
This allows passing additional system credentials into the system, in textual or binary (Base64) form. See systemd.exec(5) and System and Service Credentials for details.

Added in version 252.

`io.systemd.stub.kernel-cmdline-extra=`*`CMDLINE`*  
This allows configuration of additional kernel command line options, and is read by the kernel UEFI stub. For details see systemd-stub(7).

Added in version 254.

`io.systemd.boot.kernel-cmdline-extra=`*`CMDLINE`*  
This allows configuration of additional kernel command line options for Boot Loader Specification Type 1 entries, and is read by **systemd-boot**. For details see systemd-boot(7).

Added in version 256.

`io.systemd.boot-entries.extra:`*`ID=DEFINITION`*  
This allows inserting additional entries into the **systemd-boot** menu. For details see systemd-boot(7).

Added in version 258.

`io.systemd.boot.loglevel=`*`LEVEL`*  
This allows configuration of the log level, and is read by **systemd-boot** and **systemd-stub**. For details see systemd-boot(7) and systemd-stub(7).

Added in version 259.

`io.systemd.boot.timeout=`*`TIMEOUT`*  
This allows configuration of the menu timeout in seconds, and is read by **systemd-boot**. For details see systemd-boot(7).

Added in version 260.

## See Also

systemd(1), kernel-command-line(7), systemd.system-credentials(7)
