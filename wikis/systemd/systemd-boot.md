## Name

systemd-boot, sd-boot — A simple UEFI boot manager

## Description

**systemd-boot** (short: **sd-boot**) is a simple UEFI boot manager. It provides a textual menu to select the entry to boot and an editor for the kernel command line. **systemd-boot** supports systems with UEFI firmware only.

**systemd-boot** loads boot entry information from the EFI system partition (ESP), usually mounted at `/efi/`, `/boot/`, or `/boot/efi/` during OS runtime, as well as from the Extended Boot Loader partition (XBOOTLDR) if it exists (usually mounted to `/boot/`). Configuration file fragments, kernels, initrds and other EFI images to boot generally need to reside on the ESP or the Extended Boot Loader partition. Linux kernels must be built with `CONFIG_EFI_STUB` to be able to be directly executed as an EFI image. During boot **systemd-boot** automatically assembles a list of boot entries from the following sources:

- Boot entries defined with UAPI.1 Boot Loader Specification Type \#1 description files located in `/loader/entries/` on the ESP and the Extended Boot Loader Partition. These usually describe Linux kernel images with associated initrd images, but alternatively may also describe other arbitrary EFI executables.

- Unified kernel images, UAPI.1 Boot Loader Specification Type \#2, which are executable EFI binaries in `/EFI/Linux/` on the ESP and the Extended Boot Loader Partition.

- The Microsoft Windows EFI boot manager, if installed.

- The Apple macOS boot manager, if installed.

- The EFI Shell binary, if installed.

- A "`Reboot Into Firmware Interface`" option, if supported by the UEFI firmware.

- Secure Boot variable enrollment if the UEFI firmware is in setup mode and files are provided on the ESP.

**systemd-boot** supports the following features:

- Basic boot manager configuration changes (such as timeout configuration, default boot entry selection, …) may be made directly from the boot loader UI at boot-time, as well as during system runtime with EFI variables.

- The boot manager integrates with the **systemctl** command to implement features such as **systemctl reboot --boot-loader-entry=…** (for rebooting into a specific boot menu entry, i.e. "reboot into Windows") and **systemctl reboot --boot-loader-menu=…** (for rebooting into the boot loader menu), by implementing the Boot Loader Interface. See systemctl(1) for details.

- An EFI variable set by the boot loader informs the OS about the EFI System Partition used during boot. This is then used to automatically mount the correct EFI System Partition to `/efi/` or `/boot/` during OS runtime. See systemd-gpt-auto-generator(8) for details.

- The boot manager provides information about the boot time spent in UEFI firmware using the Boot Loader Interface. This information can be displayed using systemd-analyze(1).

- The boot manager implements boot counting and automatic fallback to older, working boot entries on failure. See Automatic Boot Assessment.

- The boot manager optionally reads a random seed from the ESP partition, combines it with a 'system token' stored in a persistent EFI variable and derives a random seed to use by the OS as entropy pool initialization, providing a full entropy pool during early boot.

- The boot manager allows for Secure Boot variables to be enrolled if the UEFI firmware is in setup mode. Additionally, variables can be automatically enrolled if configured.

bootctl(1) may be used from a running system to locate the ESP and the Extended Boot Loader Partition, list available entries, and install **systemd-boot** itself.

kernel-install(8) may be used to copy kernel images onto the ESP or the Extended Boot Loader Partition and to generate description files compliant with the Boot Loader Specification.

systemd-stub(7) may be used as UEFI boot stub for executed kernels, which is useful to show graphical boot splashes before transitioning into the Linux world. It is also capable of automatically picking up auxiliary credential files (for boot parameterization) and system extension images, as companion files to the booted kernel images.

## Key bindings

The following keys may be used in the boot menu:

**↑** (Up), **↓** (Down), **j**, **k**, **PageUp**, **PageDown**, **Home**, **End**  
Navigate up/down in the entry list

Added in version 239.

**↵** (Enter), **→** (Right)  
Boot selected entry

Added in version 239.

**d**  
Make selected entry the preferred boot entry

An EFI variable is set to allow this setting to persist.

Added in version 260.

**D**  
Make selected entry the default boot entry

An EFI variable is set to allow this setting to persist.

Added in version 260.

**e**  
Edit the kernel command line for selected entry

Added in version 239.

**+**, **t**  
Increase the timeout before default entry is booted

An EFI variable is set to allow this setting to persist.

Added in version 239.

**-**, **T**  
Decrease the timeout

An EFI variable is set to allow this setting to persist.

Added in version 239.

**r**  
Change screen resolution, skipping any unsupported modes.

An EFI variable is set to allow this setting to persist.

Added in version 250.

**R**  
Reset screen resolution to firmware or configuration file default.

An EFI variable is set to allow this setting to persist.

Added in version 250.

**p**  
Print status

Added in version 250.

**h**, **?**, **F1**  
Show a help screen

Added in version 239.

**f**  
Reboot into firmware interface.

For compatibility with the keybindings of several firmware implementations this operation may also be reached with **F2**, **F10**, **Del** and **Esc**.

Added in version 250.

**Shift**+**o**  
Power off the system.

Added in version 255.

**Shift**+**b**  
Reboot the system.

Added in version 255.

The following keys may be pressed during bootup or in the boot menu to directly boot a specific entry:

**l**  
Linux

Added in version 239.

**w**  
Windows

Added in version 239.

**a**  
macOS

Added in version 239.

**s**  
EFI shell

Added in version 239.

**1**, **2**, **3**, **4**, **5**, **6**, **7**, **8**, **9**  
Boot entry number 1 … 9

Added in version 239.

The boot menu is shown when a non-zero menu timeout has been configured. If the menu timeout has been set to zero, hold down a key (**space** is recommended) before the boot loader initializes to bring up the boot menu. Note that depending on the firmware implementation the time window where key presses are accepted before the boot loader initializes might be short. If the window is missed, reboot and try again, possibly repeatedly pressing a suitable key; on most systems it should be possible to hit the time window after a few attempts. Keys other than the space bar may be used, except for the keys listed above. If showing the menu on demand doesn't work well, consider setting a non-zero timeout to show the boot menu unconditionally. Some desktop environments might offer an option to boot directly into the boot menu, which also avoids the problem altogether. Alternatively, use the command line **systemctl reboot --boot-loader-menu=** with a non-zero value from the shell.

In the editor, most keys simply insert themselves, but the following keys may be used to perform additional actions:

**←** (Left), **→** (Right), **Home**, **End**  
Navigate left/right

Added in version 239.

**Esc**, **Ctrl**+**c**  
Abort the edit and quit the editor

Added in version 239.

**Ctrl**+**k**  
Clear the command line forwards

Added in version 239.

**Ctrl**+**w**, **Alt**+**Backspace**  
Delete word backwards

Added in version 239.

**Ctrl**+**Del**, **Alt**+**d**  
Delete word forwards

Added in version 239.

**↵** (Enter)  
Boot entry with the edited command line

Added in version 239.

Note that unless configured otherwise in the UEFI firmware, systemd-boot will use the US keyboard layout, so key labels might not match for keys like +/-.

## Files

The files **systemd-boot** processes generally reside on the UEFI ESP which is usually mounted to `/efi/`, `/boot/` or `/boot/efi/` during OS runtime. It also processes files on the Extended Boot Loader partition which is typically mounted to `/boot/`, if it exists.

**systemd-boot** reads runtime configuration such as the boot timeout and default entry from `/loader/loader.conf` on the ESP (in combination with data read from EFI variables). See loader.conf(5).

Boot entry description files following the UAPI.1 Boot Loader Specification are read from `/loader/entries/` on the ESP and the Extended Boot Loader partition.

Unified kernel boot entries following the UAPI.1 Boot Loader Specification are read from `/EFI/Linux/` on the ESP and the Extended Boot Loader partition.

Optionally, a random seed for early boot entropy pool provisioning is stored in `/loader/random-seed` in the ESP.

During initialization, **systemd-boot** automatically loads all driver files placed in the `/EFI/systemd/drivers/` directory of the ESP. The files placed there must have an extension of the EFI architecture ID followed by `.efi` (e.g. for x86-64 this means a suffix of `x64.efi`). This may be used e.g. to add support for hardware not supported natively by the firmware.

Enrollment of Secure Boot variables can be performed manually or automatically if files are available under `/loader/keys/`*`NAME`*`/{db,dbx,KEK,PK}.auth`, *`NAME`* being the display name for the set of variables in the menu. If one of the sets is named `auto` then it might be enrolled automatically depending on the execution environment and the value of the "`secure-boot-enroll`" option. See loader.conf(5).

## EFI Variables

The following EFI variables are defined, and may be set or read by **systemd-boot** for communication between the boot loader and the OS. The vendor UUID "`4a67b082-0a4c-41cf-b6c7-440b29bb8c4f`" is used in all cases.

`LoaderBootCountPath`  
If boot counting is enabled, contains the path to the file in whose name the boot counters are encoded. Set by the boot loader. systemd-bless-boot.service(8) uses this information to mark a boot as successful as determined by the successful activation of the `boot-complete.target` target unit.

Added in version 240.

`LoaderConfigTimeout`, `LoaderConfigTimeoutOneShot`  
The menu timeout in seconds. Read by the boot loader. `LoaderConfigTimeout` is maintained persistently, while `LoaderConfigTimeoutOneShot` is a one-time override which is read once (in which case it takes precedence over `LoaderConfigTimeout`) and then removed. `LoaderConfigTimeout` may be manipulated with the **t**/**T** keys, see above.

Added in version 240.

`LoaderConfigConsoleMode`  
The numerical menu console mode. Read by the boot loader. `LoaderConfigConsoleMode` is maintained persistently. `LoaderConfigConsoleMode` may be manipulated with the **r**/**R** keys, see above.

Added in version 250.

`LoaderDevicePartUUID`  
Contains the partition UUID of the partition the boot loader has been started from on the current boot (usually an EFI System Partition). Set by the boot loader. (Note that systemd-stub(7) will set this too, if not set yet, to support systems that boot directly into a unified kernel image, bypassing any boot loader.) systemd-gpt-auto-generator(8) uses this information to automatically find the disk booted from, in order to discover various other partitions on the same disk automatically.

Added in version 220.

`LoaderDeviceURL`  
If the boot loader has been invoked via network booting this variable contains the originating URL. This may be used to automatically acquire additional resources from the same source.

Added in version 258.

`LoaderEntries`  
A list of the identifiers of all discovered boot loader entries. Set by the boot loader.

Added in version 240.

`LoaderEntryPreferred`, `LoaderEntryDefault`, `LoaderEntrySysFail`, `LoaderEntryOneShot`  
The identifier of the default boot loader entry. Can be set in the OS and the boot loader. `LoaderEntryOneShot` sets the default entry for the next boot only, while `LoaderEntryDefault` sets it persistently for all future boots. `LoaderEntryPreferred` is like `LoaderEntryDefault` but additionally takes into account boot assessment and skips boot entries with a tries-left counter equal to zero. bootctl(1)'s `set-default` and `set-oneshot` commands make use of these variables. The boot loader modifies `LoaderEntryDefault` on request, when the **d** key is used, see above.

Added in version 240.

`LoaderEntryLastBooted`  
The identifier of the boot loader entry last attempted. Set and read by the boot loader, only when `/loader/loader.conf` has default set to "`@saved`". See loader.conf(5).

The boot loader will ensure `LoaderEntryLastBooted` is up-to date for every boot, updating it as needed and will omit changing it all together when `LoaderEntryOneShot` is set.

The boot loader reads the variable, which takes higher priority than `LoaderEntryDefault`. The variable is ignored when `LoaderEntryOneShot` is set.

`LoaderEntryLastBooted` cannot be used as indication that the last boot was successful or not.

Added in version 250.

`LoaderEntrySelected`  
The identifier of the boot loader entry currently being booted. Set by the boot loader.

Added in version 240.

`LoaderFeatures`  
A set of flags indicating the features the boot loader supports. Set by the boot loader. Use bootctl(1) to view this data.

Added in version 240.

`LoaderFirmwareInfo`, `LoaderFirmwareType`  
Brief firmware information. Set by the boot loader. Use bootctl(1) to view this data.

Added in version 240.

`LoaderTpm2ActivePcrBanks`  
Hexadecimal string representation of a bitmask with values defined by the TCG EFI Protocol Specification for TPM 2.0 as EFI_TCG2_BOOT_HASH_ALG\_\*. If no TPM2 support or no active banks were detected, will be set to `0`. Set by the boot loader. Use systemd-analyze(1) to view this data.

Added in version 258.

`LoaderImageIdentifier`  
The file system path to the EFI executable of the boot loader for the current boot, relative to the partition's root directory (i.e. relative to the partition indicated by `LoaderDevicePartUUID`, see above). Set by the boot loader. (Note that **systemd-stub** will set this too, if not set yet, to support systems that directly boot into a unified kernel image, bypassing any boot loader.) Use bootctl(1) to view this data.

Added in version 220.

`LoaderInfo`  
Brief information about the boot loader. Set by the boot loader. Use bootctl(1) to view this data.

Added in version 240.

`LoaderTimeExecUSec`, `LoaderTimeInitUSec`, `LoaderTimeMenuUsec`  
Information about the time spent in various parts of the boot loader. Set by the boot loader. Use systemd-analyze(1) to view this data.

Added in version 240.

`LoaderSystemToken`  
A binary random data field, that is used for generating the random seed to pass to the OS (see above). Note that this random data is generally only generated once, during OS installation, and is then never updated again.

Added in version 243.

Many of these variables are defined by the Boot Loader Interface.

## SMBIOS Type 11 Strings

**systemd-boot** can be configured using SMBIOS Type 11 strings. Applicable strings consist of a name, followed by "`=`", followed by the value. Unless **systemd-boot** detects it is running inside a confidential computing environment, **systemd-boot** will search the table for a string with a specific name, and if found, use its value. The following strings are read:

`io.systemd.boot.kernel-cmdline-extra`  
If set, the value of this string is added to the list of kernel command line arguments for Boot Loader Specification Type 1 entries that are measured in PCR12 and passed to the kernel.

Added in version 256.

`io.systemd.boot-entries.extra:`*`ID=DEFINITION`*  
This allows inserting additional entries into the **systemd-boot** menu. Take a pair of menu entry identifier and menu entry definition string. The former should be suitable for use as a filename of a Boot Loader Specification Type \#1 entry filename (note that it is used for identification purposes only, no file of this name is actually accessed), the latter shall follow the syntax of the contents of a Type \#1 entry. Any menu entry defined this way is processed and shown in pretty much the same way as a Type \#1 entry read from the ESP or XBOOTLDR partition. Example:

``` programlisting
io.systemd.boot-entries.extra:fooos-current.conf=title FooOS (Current)
uki-url http://example.com/somedir/fooos.efi
```

Note that this example contains a newline character. When generating this string from a shell care must be taken to encode it correctly.

Pass multiple strings formatted this way to generate multiple menu entries.

Added in version 258.

`io.systemd.boot.loglevel`  
If set, the value of this string is used as log level. Valid values (from most to least critical) are "`emerg`", "`alert`", "`crit`", "`err`", "`warning`", "`notice`", "`info`", and "`debug`".

Added in version 259.

## Boot Counting

**systemd-boot** implements a simple boot counting mechanism on top of the UAPI.1 Boot Loader Specification, for automatic and unattended fallback to older kernel versions/boot loader entries when a specific entry continuously fails. Any boot loader entry file and unified kernel image file that contains a "`+`" followed by one or two numbers (if two they need to be separated by a "`-`"), before the `.conf` or `.efi` suffix is subject to boot counting: the first of the two numbers ('tries left') is decreased by one on every boot attempt, the second of the two numbers ('tries done') is increased by one (if 'tries done' is absent it is considered equivalent to 0). Depending on the current value of these two counters the boot entry is considered to be in one of three states:

1.  If the 'tries left' counter of an entry is greater than zero the entry is considered to be in 'indeterminate' state. This means the entry has not completed booting successfully yet, but also has not been determined not to work.

2.  If the 'tries left' counter of an entry is zero it is considered to be in 'bad' state. This means no further attempts to boot this item will be made (that is, unless all other boot entries are also in 'bad' state), as all attempts to boot this entry have not completed successfully.

3.  If the 'tries left' and 'tries done' counters of an entry are absent it is considered to be in 'good' state. This means further boot counting for the entry is turned off, as it successfully booted at least once. The systemd-bless-boot.service(8) service moves the currently booted entry from 'indeterminate' into 'good' state when a boot attempt completed successfully.

Generally, when new entries are added to the boot loader, they first start out in 'indeterminate' state, i.e. with a 'tries left' counter greater than zero. The boot entry remains in this state until either it managed to complete a full boot successfully at least once (in which case it will be in 'good' state) — or the 'tries left' counter reaches zero (in which case it will be in 'bad' state).

Example: let's say a boot loader entry file `foo.conf` is set up for 3 boot tries. The installer will hence create it under the name `foo+3.conf`. On first boot, the boot loader will rename it to `foo+2-1.conf`. If that boot does not complete successfully, the boot loader will rename it to `foo+1-2.conf` on the following boot. If that fails too, it will finally be renamed `foo+0-3.conf` by the boot loader on next boot, after which it will be considered 'bad'. If the boot succeeds however the entry file will be renamed to `foo.conf` by the OS, so that it is considered 'good' from then on.

The boot menu takes the 'tries left' counter into account when sorting the menu entries: entries in 'bad' state are ordered at the beginning of the list, and entries in 'good' or 'indeterminate' at the end. The user can freely choose to boot any entry of the menu, including those already marked 'bad'. If the menu entry to boot is automatically determined, this means that 'good' or 'indeterminate' entries are generally preferred (as the bottom item of the menu is the one booted by default), and 'bad' entries will only be considered if there are no 'good' or 'indeterminate' entries left.

The kernel-install(8) kernel install framework optionally sets the initial 'tries left' counter to the value specified in `/etc/kernel/tries` when a boot loader entry is first created.

## Using **systemd-boot** in virtual machines

When using qemu with OVMF (UEFI Firmware for virtual machines) the `-kernel` switch works not only for linux kernels, but for any EFI binary, including `systemd-boot` and unified linux kernels (UKIs). Example command line for loading **systemd-boot** on x64:

**qemu-system-x86_64 -drive if=pflash,format=qcow2,readonly=on,file=/usr/share/edk2/ovmf/OVMF_CODE_4M.qcow2 -kernel /usr/lib/systemd/boot/efi/systemd-bootx64.efi -drive file=*`...`* *`[ ... ]`***

(The path to the firmware file might need to be adjusted depending on the distribution.) `systemd-boot` will detect that it was started directly instead of being loaded from ESP and will search for the ESP in that case, taking into account boot order information from the hypervisor (if available). Note that for this to yield a useful result, another `-drive` argument needs to be used to attach an actual disk image with an ESP.

## See Also

bootctl(1), loader.conf(5), systemd-bless-boot.service(8), systemd-boot-random-seed.service(8), kernel-install(8), systemd-stub(7), UAPI.1 Boot Loader Specification, Boot Loader Interface, TPM2 PCR Measurements Made by systemd
