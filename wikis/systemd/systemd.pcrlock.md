## Name

systemd.pcrlock, systemd.pcrlock.d — PCR measurement prediction files

## Synopsis

|                                                  |
|--------------------------------------------------|
| `/etc/pcrlock.d/*.pcrlock`                       |
| `/etc/pcrlock.d/*.pcrlock.d/*.pcrlock`           |
| `/run/pcrlock.d/*.pcrlock`                       |
| `/run/pcrlock.d/*.pcrlock.d/*.pcrlock`           |
| `/var/lib/pcrlock.d/*.pcrlock`                   |
| `/var/lib/pcrlock.d/*.pcrlock.d/*.pcrlock`       |
| `/usr/local/lib/pcrlock.d/*.pcrlock`             |
| `/usr/local/lib/pcrlock.d/*.pcrlock.d/*.pcrlock` |
| `/usr/lib/pcrlock.d/*.pcrlock`                   |
| `/usr/lib/pcrlock.d/*.pcrlock.d/*.pcrlock`       |

## Description

`*.pcrlock` files define expected TPM2 PCR measurements of components involved in the boot process. systemd-pcrlock(8) uses such pcrlock files to analyze and predict TPM2 PCR measurements. The pcrlock files are JSON arrays that follow a subset of the TCG Canonical Event Log Format (CEL-JSON) specification. Specifically the "`recnum`", "`content`", and "`content_type`" record fields are not used and ignored if present. Each pcrlock file defines one set of expected, ordered PCR measurements of a specific component of the boot.

\*.pcrlock files may be placed in various `.d/` drop-in directories (see above for a full list). All matching files discovered in these directories are sorted alphabetically by their file name (without taking the actual directory they were found in into account): pcrlock files with alphabetically earlier names are expected to cover measurements done before those with alphabetically later names. In order to make positioning pcrlock files in the boot process convenient the files are expected (by convention, this is not enforced) to be named "*`NNN`*`-`*`component`*`.pcrlock`" (where *`NNN`* is a three-digit decimal number), for example `750-enter-initrd.pcrlock`.

For various components of the boot process more than one alternative pcrlock file shall be supported (i.e. "variants"). For example to cover multiple kernels installed in parallel in the access policy, or multiple versions of the boot loader. This can be done by placing `*.pcrlock.d/*.pcrlock` in the drop-in dirs, i.e. a common directory for a specific component, that contains one or more pcrlock files each covering one *variant* of the component. Example: `650-kernel.pcrlock.d/6.5.5-200.fc38.x86_64.pcrlock` and `650-kernel.pcrlock.d/6.5.7-100.fc38.x86_64.pcrlock`

Use **systemd-pcrlock list-components** to list all pcrlock files currently installed.

Use the various **lock-\*** commands of **systemd-pcrlock** to automatically generate suitable pcrlock files for various types of resources.

## Well-known Components

Components of the boot process may be defined freely by the administrator or OS vendor. The following components are well-known however, and are defined by systemd. The list below is useful for ordering local pcrlock files properly against these components of the boot.

`240-secureboot-policy.pcrlock`  
The SecureBoot policy, as recorded to PCR 7. May be generated via **systemd-pcrlock lock-secureboot-policy**.

Added in version 255.

`250-firmware-code-early.pcrlock`  
Firmware code measurements, as recorded to PCR 0 and 2, up to the separator measurement (see `400-secureboot-separator.pcrlock` below). May be generated via **systemd-pcrlock lock-firmware-code**.

Added in version 255.

`250-firmware-config-early.pcrlock`  
Firmware configuration measurements, as recorded to PCR 1 and 3, up to the separator measurement (see `400-secureboot-separator.pcrlock` below). May be generated via **systemd-pcrlock lock-firmware-config**.

Added in version 255.

`350-action-efi-application.pcrlock`  
The EFI "Application" measurement done once by the firmware. Statically defined.

Added in version 255.

`400-secureboot-separator.pcrlock`  
The EFI "separator" measurement on PCR 7 done once by the firmware to indicate where firmware control transitions into boot loader/OS control. Statically defined.

Added in version 255.

`500-separator.pcrlock`  
The EFI "separator" measurements on PCRs 0-6 done once by the firmware to indicate where firmware control transitions into boot loader/OS control. Statically defined.

Added in version 255.

`550-firmware-code-late.pcrlock`  
Firmware code measurements, as recorded to PCR 0 and 2, after the separator measurement (see `400-secureboot-separator.pcrlock` above). May be generated via **systemd-pcrlock lock-firmware-code**.

Added in version 255.

`550-firmware-config-late.pcrlock`  
Firmware configuration measurements, as recorded to PCR 1 and 3, after the separator measurement (see `400-secureboot-separator.pcrlock` above). May be generated via **systemd-pcrlock lock-firmware-config**.

Added in version 255.

`600-gpt.pcrlock`  
The GPT partition table of the booted medium, as recorded to PCR 5 by the firmware. May be generated via **systemd-pcrlock lock-gpt**.

Added in version 255.

`620-secureboot-authority.pcrlock`  
The SecureBoot authority, as recorded to PCR 7. May be generated via **systemd-pcrlock lock-secureboot-authority**.

Added in version 255.

`700-action-efi-exit-boot-services.pcrlock`  
The EFI action generated when `ExitBootServices()` is generated, i.e. when the UEFI environment is left and the OS takes over. Covers the PCR 5 measurement. Statically defined.

Added in version 255.

`710-kernel-cmdline.pcrlock`  
The kernel command line, as measured by the Linux kernel to PCR 9. May be generated via **systemd-pcrlock lock-kernel-cmdline**.

Added in version 255.

`720-kernel-initrd.pcrlock`  
The kernel initrd, as measured by the Linux kernel to PCR 9. May be generated via **systemd-pcrlock lock-kernel-initrd**.

Added in version 255.

`750-enter-initrd.pcrlock`  
The measurement to PCR 11 systemd-pcrphase-initrd.service(8) makes when the initrd initializes. Statically defined.

Added in version 255.

`800-leave-initrd.pcrlock`  
The measurement to PCR 11 systemd-pcrphase-initrd.service(8) makes when the initrd finishes. Statically defined.

Added in version 255.

`820-machine-id.pcrlock`  
The measurement to PCR 15 systemd-pcrmachine.service(8) makes at boot, covering `/etc/machine-id` contents. May be generated via **systemd-pcrlock lock-machine-id**.

Added in version 255.

`830-root-file-system.pcrlock`  
The measurement to PCR 15 systemd-pcrfs-root.service(8) makes at boot, covering the root file system identity. May be generated via **systemd-pcrlock lock-file-system**.

Added in version 255.

`850-sysinit.pcrlock`  
The measurement to PCR 11 systemd-pcrphase-sysinit.service(8) makes when the main userspace did basic initialization and will now proceed to start regular system services. Statically defined.

Added in version 255.

`900-ready.pcrlock`  
The measurement to PCR 11 systemd-pcrphase.service(8) makes when the system fully booted up. Statically defined.

Added in version 255.

`950-shutdown.pcrlock`  
The measurement to PCR 11 systemd-pcrphase.service(8) makes when the system begins shutdown. Statically defined.

Added in version 255.

`990-final.pcrlock`  
The measurement to PCR 11 systemd-pcrphase-sysinit.service(8) makes when the system is close to finishing shutdown. Statically defined.

Added in version 255.

## See Also

systemd(1), systemd-pcrlock(8)
