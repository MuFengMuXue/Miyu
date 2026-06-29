## Name

loader.conf — Configuration file for systemd-boot

## Synopsis

*`ESP`*`/loader/loader.conf`

## Description

systemd-boot(7) reads *`ESP`*`/loader/loader.conf`. This file configures whether the menu is shown and for how long, the font, audible beep, types of menu entries to show, the default choice, and some aspects of Secure Boot enrollment and firmware handling. See the list of available options below.

The file uses UTF-8 encoding and consists of series of lines separated by "line feed" (i.e. ASCII code 10). Lines that are empty or start with the comment sign ("`#`") are ignored. Other lines consist of an option name, followed by whitespace, and the option value.

Boolean arguments may be written as "`yes`"/"`y`"/"`true`"/"`t`"/"`on`"/"`1`" or "`no`"/"`n`"/"`false`"/"`f`"/"`off`"/"`0`".

Note: **systemd-boot** will also read boot loader entry files, type \#1 (*`ESP`*`/loader/entries/*.conf` and *`XBOOTLDR`*`/loader/entries/*.conf`) and type \#2 (*`ESP`*`/EFI/Linux/*.uki` and *`XBOOTLDR`*`/EFI/Linux/*.uki`). Those files are described by the UAPI.1 Boot Loader Specification.

Note: the behaviour of **systemd-boot** is also influenced by EFI variables. Some of the settings specified in this file can be overridden by those, for example the default boot menu entry or the menu timeouts. See systemd-boot(7) for details.

## Options

The following configuration are supported in `loader.conf`:

default  
A glob pattern to select the default entry by id, which is the file name including literal suffix "`.conf`". The default entry may be changed in the boot menu itself, in which case the name of the selected entry will be stored as an EFI variable, overriding this option.

If set to "`@saved`" the chosen entry will be saved as an EFI variable on every boot and automatically selected the next time the boot loader starts.

**Table 1. Automatically detected entries will use the following names:**

| Name                          | Description                    |
|-------------------------------|--------------------------------|
| auto-efi-default              | EFI Default Loader             |
| auto-efi-shell                | EFI Shell                      |
| auto-osx                      | macOS                          |
| auto-poweroff                 | Power Off The System           |
| auto-reboot                   | Reboot The System              |
| auto-reboot-to-firmware-setup | Reboot Into Firmware Interface |
| auto-windows                  | Windows Boot Manager           |

  

Supported glob wildcard patterns are "`?`", "`*`", and "`[…]`" (including ranges). Note that these patterns use the same syntax as glob(7), but do not support all features. In particular, set negation and named character classes are not supported. The matching is done case-insensitively on the entry ID (as shown by **bootctl list**).

Added in version 239.

timeout  
How long the boot menu should be shown before the default entry is booted, in seconds. This may be changed in the boot menu itself and will be stored as an EFI variable in that case, overriding this option.

If set to "`menu-disabled`" or "`menu-hidden`" or "`0`" (the default), no menu is shown and the default entry will be booted immediately. Unless "`menu-disabled`" is used, the menu can be shown by pressing and holding a key before systemd-boot is launched. Setting this to "`menu-force`" disables the timeout while always showing the menu.

Added in version 239.

console-mode  
This option configures the resolution of the console. This may be changed in the boot menu itself and will be stored as an EFI variable in that case, overriding this option.

Takes a number or one of the special values listed below. The following values may be used:

0  
Standard UEFI 80x25 mode

Added in version 239.

1  
80x50 mode, not supported by all devices

Added in version 239.

2  
the first non-standard mode provided by the device firmware, if any

Added in version 239.

auto  
Pick a suitable mode automatically using heuristics

Added in version 239.

max  
Pick the highest-numbered available mode

Added in version 239.

keep  
Keep the mode selected by firmware (the default)

Added in version 239.

Added in version 239.

editor  
Takes a boolean argument. Enable (the default) or disable the editor. The editor should be disabled if the machine can be accessed by unauthorized persons.

Added in version 239.

auto-entries  
Takes a boolean argument. Enable (the default) or disable entries for other boot entries found on the boot partition. In particular, this may be useful when loader entries are created to show replacement descriptions for those entries.

Added in version 239.

auto-firmware  
A boolean controlling the presence of the "`Reboot Into Firmware Interface`" entry (enabled by default). If this is disabled, the firmware interface may still be reached by using the **f** key.

Added in version 239.

auto-reboot  
A boolean controlling the presence of the "`Reboot The System`" entry (disabled by default). Even if this is disabled, the system may still be rebooted by pressing **Shift**+**b**.

Added in version 255.

auto-poweroff  
A boolean controlling the presence of the "`Power Off The System`" entry (disabled by default). Even if this is disabled, the system may still be powered off by pressing **Shift**+**o**.

Added in version 255.

beep  
Takes a boolean argument. If timeout enabled beep every second, otherwise beep n times when n-th entry in boot menu is selected (default disabled). Currently, only x86 is supported, where it uses the PC speaker.

Added in version 251.

secure-boot-enroll  
Danger: this feature might soft-brick your device if used improperly.

Controls enrollment of secure boot keys found on the ESP if the system is in setup mode:

`if-safe`  
This is the default. Same behavior as `manual`, but will try to automatically enroll the key named "`auto`" if it is considered to be safe. Currently, this is only the case if the system is running inside a virtual machine.

Added in version 253.

`manual`  
Boot entries for found secure boot keys are created that allow manual enrollment.

Added in version 253.

`off`  
No action is taken.

Added in version 253.

`force`  
Always enroll the "`auto`" key if found. Note that a warning message with a timeout will still be shown if this operation is unknown to be safe.

Added in version 253.

The different sets of variables can be set up under `/loader/keys/`*`NAME`* where *`NAME`* is the name that is going to be used as the name of the entry. This allows one to ship multiple sets of Secure Boot variables and choose which one to enroll at runtime.

Supported Secure Boot variables are one database for authorized images, one for the key exchange key (KEK) and one for the platform key (PK). For more information, refer to the UEFI specification, under Secure Boot and Driver Signing. Another resource that describe the interplay of the different variables is the EDK2 documentation.

A complete set of UEFI variable includes `db.auth`, `KEK.auth` and `PK.auth`. Note that these files need to be authenticated UEFI variables. See below for an example of how to generate them from regular X.509 keys.

``` programlisting
uuid=$(systemd-id128 new --uuid)
for key in PK KEK db; do
  openssl req -new -x509 -subj "/CN=${key}/" -keyout "${key}.key" -out "${key}.pem"
  openssl x509 -outform DER -in "${key}.pem" -out "${key}.der"
  sbsiglist --owner "${uuid}" --type x509 --output "${key}.esl" "${key}.der"
done

# See also: Windows Secure Boot Key Creation and Management Guidance
curl --location \
     "https://go.microsoft.com/fwlink/p/?linkid=321192" -o ms-db-2011.der \
     "https://go.microsoft.com/fwlink/p/?linkid=321185" -o ms-kek-2011.der \
     "https://go.microsoft.com/fwlink/p/?linkid=321194" -o ms-uefi-db-2011.der \
     "https://go.microsoft.com/fwlink/p/?linkid=2239776" -o ms-db-2023.der \
     "https://go.microsoft.com/fwlink/p/?linkid=2239775" -o ms-kek-2023.der \
     "https://go.microsoft.com/fwlink/p/?linkid=2239872" -o ms-uefi-db-2023.der
sha1sum -c <<END
580a6f4cc4e4b669b9ebdc1b2b3e087b80d0678d  ms-db-2011.der
31590bfd89c9d74ed087dfac66334b3931254b30  ms-kek-2011.der
46def63b5ce61cf8ba0de2e6639c1019d0ed14f3  ms-uefi-db-2011.der
45a0fa32604773c82433c3b7d59e7466b3ac0c67  ms-db-2023.der
459ab6fb5e284d272d5e3e6abc8ed663829d632b  ms-kek-2023.der
b5eeb4a6706048073f0ed296e7f580a790b59eaa  ms-uefi-db-2023.der
END
for key in ms-*.der; do
  sbsiglist --owner 77fa9abd-0359-4d32-bd60-28f4e78f784b --type x509 --output "${key%der}esl" "${key}"
done

# Optionally add Microsoft Windows certificates (needed to boot into Windows).
cat ms-db-*.esl >>db.esl

# Optionally add Microsoft UEFI certificates for firmware drivers / option ROMs and third-party
# boot loaders (including shim). This is highly recommended on real hardware as not including this
# may soft-brick your device (see next paragraph).
cat ms-uefi-*.esl >>db.esl

# Optionally add Microsoft KEK certificates. Recommended if either of the Microsoft keys is used as
# the official UEFI revocation database is signed with this key. The revocation database can be
# updated with fwupdmgr(1).
cat ms-kek-*.esl >>KEK.esl

attr=NON_VOLATILE,RUNTIME_ACCESS,BOOTSERVICE_ACCESS,TIME_BASED_AUTHENTICATED_WRITE_ACCESS
sbvarsign --attr "${attr}" --key PK.key --cert PK.pem --output PK.auth PK PK.esl
sbvarsign --attr "${attr}" --key PK.key --cert PK.pem --output KEK.auth KEK KEK.esl
sbvarsign --attr "${attr}" --key KEK.key --cert KEK.pem --output db.auth db db.esl
```

This feature is considered dangerous because even if all the required files are signed with the keys being loaded, some files necessary for the system to function properly still won't be. This is especially the case with Option ROMs (e.g. for storage controllers or graphics cards). See Secure Boot and Option ROMs for more details.

Added in version 252.

secure-boot-enroll-action  
Specifies the action to take after the automatic enrollment of secure boot keys is completed.

reboot  
Reboot the system after enrollment. This is the default.

shutdown  
Shut down the system after enrollment.

This option is only relevant if "`secure-boot-enroll`" is enabled.

Added in version 258.

secure-boot-enroll-timeout-sec  
How long the warning should be shown in seconds before the key enrollment process starts.

If set to "`hidden`" or "`0`", no warning is shown and the keys will be enrolled immediately. The default timeout (if not set explicitly) is 15 seconds.

This option is only relevant if "`secure-boot-enroll`" is enabled.

Added in version 259.

reboot-for-bitlocker  
Caveat: This feature is experimental, and is likely to be changed (or removed in its current form) in a future version of systemd.

Work around BitLocker requiring a recovery key when the boot loader was updated (disabled by default).

Try to detect BitLocker encrypted drives along with an active TPM. If both are found and Windows Boot Manager is selected in the boot menu, set the "`BootNext`" EFI variable and restart the system. The firmware will then start Windows Boot Manager directly, leaving the TPM PCRs in expected states so that Windows can unseal the encryption key. This allows systemd-boot(7) to be updated without having to provide the recovery key for BitLocker drive unlocking.

Note that the PCRs that Windows uses can be configured with the "`Configure TPM platform validation profile for native UEFI firmware configurations`" group policy under "`Computer Configuration\Administrative Templates\Windows Components\BitLocker Drive Encryption`". When Secure Boot is enabled, changing this to PCRs "`0,2,7,11`" should be safe. The TPM key protector needs to be removed and then added back for the PCRs on an already encrypted drive to change. If PCR 4 is not measured, this setting can be disabled to speed up booting into Windows.

Added in version 251.

reboot-on-error  
Controls auto reboot in case the selected entry fails to start.

`yes`  
Reboot the system if the selected boot entry failed to start.

`no`  
Don't reboot - pass control back to EFI firmware.

`auto`  
Perform the reboot if and only if boot counting is enabled for this entry and the tries left counter wasn't already at 0.

This is the default, as it is typically a safe option, that ensures a clean measurement log on each boot attempt, but also does not risk an unbounded reboot loop.

Added in version 258.

log-level  
Controls the log level used by systemd-boot(7).

Valid values are "`emerg`", "`alert`", "`crit`", "`err`", "`warning`", "`notice`", "`info`", and "`debug`".

If unspecified, "`info`" will be used, unless one has already been configured via an SMBIOS Type 11 string, see smbios-type-11(7).

Note that the configured level will only be used after `loader.conf` has been parsed, so log messages generated before that point may be unaffected by this setting.

Added in version 259.

## Example

``` programlisting
# /boot/efi/loader/loader.conf
timeout 0
default 01234567890abcdef1234567890abdf0-*
editor no
```

The menu will not be shown by default (the menu can still be shown by pressing and holding a key during boot). One of the entries with files with a name starting with "`01234567890abcdef1234567890abdf0-`" will be selected by default. If more than one entry matches, the one with the highest priority will be selected (generally the one with the highest version number). The editor will be disabled, so it is not possible to alter the kernel command line.

## See Also

systemd-boot(7), bootctl(1)
