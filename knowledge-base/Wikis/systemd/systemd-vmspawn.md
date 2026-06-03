## Name

systemd-vmspawn — Spawn an OS in a virtual machine

## Synopsis

`systemd-vmspawn` \[OPTIONS...\] \[ARGS...\]

## Description

**systemd-vmspawn** may be used to start a virtual machine from an OS image. In many ways it is similar to systemd-nspawn(1), but launches a full virtual machine instead of using namespaces.

File descriptors for `/dev/kvm` and `/dev/vhost-vsock` can be passed to **systemd-vmspawn** via systemd's native socket passing interface (see sd_listen_fds(3) for details about the precise protocol used and the order in which the file descriptors are passed), these file descriptors must be passed with the names "`kvm`" and "`vhost-vsock`" respectively.

Note: on Ubuntu/Debian derivatives **systemd-vmspawn** requires the user to be in the "`kvm`" group to use the VSOCK options.

## Options

The excess arguments are passed as extra kernel command line arguments using SMBIOS.

The following options are understood:

`-q`, `--quiet`  
Turns off any status output by the tool itself. When this switch is used, the only output from vmspawn will be the console output of the Virtual Machine OS itself.

Added in version 256.

`--system`, `--user`  
Specify whether to interact with the user manager or the system manager and whether to register with the user machined instance or the system machined instance. If unspecified, the system manager and machined instance will be used when running as root, otherwise the user manager and machined instance will be used.

Added in version 260.

### Image Options

`-D`, `--directory=`  
Directory to use as file system root for the virtual machine.

One of either `--directory=` or `--image=` must be specified. If neither are specified `--directory=.` is assumed.

Note: If mounting a non-root owned directory you may require `--private-users=` to map into the user's subuid namespace. An example of how to use `/etc/subuid` for this is given later.

Added in version 256.

`-i`, `--image=`  
Root file system disk image (or device node) for the virtual machine.

Added in version 255.

`--image-format=`*`FORMAT`*  
Specifies the format of the disk image passed to `--image=`. Takes either "`raw`" or "`qcow2`". Defaults to "`raw`". Note that "`qcow2`" is only supported for regular files, not block devices.

Added in version 260.

`-x`, `--ephemeral`  
If specified, the VM is run with a temporary snapshot of its file system that is removed immediately when the VM terminates. Only works with `--image=` currently. Note that `--ephemeral` will not work with `--extra-drive=`.

Added in version 260.

### Host Configuration

`--cpus=`*`CPUS`*  
The number of CPUs to start the virtual machine with. Defaults to 1.

Added in version 255.

`--ram=`*`BYTES`*  
The amount of memory to start the virtual machine with. Defaults to 2G.

Added in version 255.

`--kvm=`*`BOOL`*  
Controls whether to enable KVM acceleration. If not specified or set to `auto`, KVM support will be detected automatically. If true, KVM is insisted on. If false, disable KVM.

Added in version 255.

`--vsock=`*`BOOL`*  
Controls whether to allocate a VSOCK socket for guest. If not specified or set to `auto`, VSOCK networking support will be detected automatically. If true, VSOCK is insisted on. If false, VSOCK networking is disabled.

Added in version 255.

`--vsock-cid=`*`CID`*  
Sets the specific CID to use for the guest. Valid CIDs are in the range `3` to `4294967294` (`0xFFFF_FFFE`). CIDs outside of this range are reserved. By default, vmspawn will attempt to derive a CID for the guest derived from the machine name, falling back to a random CID if this CID is taken.

Added in version 255.

`--tpm=`*`BOOL`*  
Controls whether to serve a TPM device for guest, via swtpm(8). If not specified or set to `auto`, vmspawn will detect the presence of swtpm binary automatically. If yes, swtpm support is insisted on. If no, TPM is disabled.

Added in version 256.

`--tpm-state=`*`PATH`*`|auto|off`  
Configures where to place TPM state, in case TPM support is enabled (see `--tpm=` above). This takes an absolute file system path to a directory to persistently place the state in. If the directory is missing it is created as needed. If set to the special string "`auto`" a persistent path is automatically derived from the VM image path or directory path, with the "`.tpmstate`" suffix appended. If set to the special string "`off`" the TPM state is only maintained transiently and flushed out when the VM shuts down. This mode is not suitable for VMs which lock disk encryption keys to the TPM, as these keys will be lost on every reboot. Defaults to "`auto`".

If `--ephemeral` is specified, "`auto`" behaves like "`off`".

Added in version 258.

`--linux=`*`PATH`*  
Set the linux kernel image to use for direct kernel boot. If a directory type image is used and `--linux=` was omitted, vmspawn will search for boot loader entries according to the UAPI.1 Boot Loader Specification assuming XBOOTLDR to be located at /boot and ESP to be /efi respectively. If no kernel was installed into the image then the image will fail to boot.

Added in version 256.

`--initrd=`*`PATH`*  
Set the initrd to use for direct kernel boot. If the `--linux=` supplied is a UAPI.1 Boot Loader Specification Type \#2 entry, then this argument is not required. If no initrd was installed into the image then the image will fail to boot.

`--initrd=` can be specified multiple times and vmspawn will merge them together.

Added in version 256.

`-n`, `--network-tap`  
Create a TAP device to network with the virtual machine.

Note: root privileges are required to use TAP networking. Additionally, systemd-networkd(8) must be running and correctly set up on the host to provision the host interface. The relevant "`.network`" file can be found at `/usr/lib/systemd/network/80-vm-vt.network`.

Added in version 255.

`--network-user-mode`  
Use user mode networking.

Added in version 255.

`--firmware=`*`PATH`*  
Takes an absolute path, or a relative path beginning with `./`. Specifies a JSON firmware definition file, which allows selecting the firmware to boot in the VM. If not specified, a suitable firmware is automatically discovered. If the special string "`list`" is specified lists all discovered firmwares.

Added in version 256.

`--discard-disk=`*`BOOL`*  
Controls whether qemu processes discard requests from the VM. This prevents long running VMs from using more disk space than required. This is enabled by default.

Added in version 256.

`--secure-boot=`*`BOOL`*  
Configure whether to search for firmware which supports Secure Boot.

If the option is not specified or set to `auto`, the first firmware detected will be used. If the option is set to yes, then the first firmware with Secure Boot support will be selected. If no is specified, then the first firmware without Secure Boot will be selected.

Added in version 255.

`--grow-image=`*`BYTES`*, `-G `*`BYTES`*  
Grows the image file specified by `--image=` to the specified size in bytes if it is smaller. Executes no operation if no image file is used or the image file is already as large or larger than requested. The specified size accepts the usual K, M, G suffixes (to the base of 1024). Specified values are rounded up to multiples of 4096.

Added in version 258.

`--smbios11=`*`STRING`*, `-s `*`STRING`*  
Passes the specified string into the VM as an SMBIOS Type \#11 vendor string. This is useful to parameterize the invoked VM in various ways. See smbios-type-11(7) for details.

Added in version 258.

`--notify-ready=`  
Configures support for notifications from the VM's init process to **systemd-vmspawn**. If true, **systemd-vmspawn** will consider the machine as ready only when it has received a "`READY=1`" message from the init process in the VM. If false, **systemd-vmspawn** will consider the machine as ready immediately after creation. In either case, **systemd-vmspawn** sends its own readiness notification to its manager after the spawned VM is ready. For more details about notifications see sd_notify(3).

Defaults to true. (Note that this is unlike the option of the same name to systemd-nspawn(1) that defaults to false.)

Added in version 258.

### System Identity Options

`-M`, `--machine=`  
Sets the machine name for this virtual machine. This name may be used to identify this virtual machine during its runtime (for example in tools like machinectl(1) and similar).

Added in version 255.

`--uuid=`  
Set the specified UUID for the virtual machine. The init system will initialize `/etc/machine-id` from this if this file is not set yet. Note that this option takes effect only if `/etc/machine-id` in the virtual machine is unpopulated.

Added in version 256.

### Property Options

`-S`, `--slice=`  
Make the VM part of the specified slice, instead of the default `machine.slice`. This applies only if the machine is run in its own scope unit, i.e. if `--keep-unit` is not used.

Added in version 258.

`--property=`  
Set a unit property on the scope unit to register for the machine. This applies only if the machine is run in its own scope unit, i.e. if `--keep-unit` is not used. Takes unit property assignments in the same format as **systemctl set-property**. This is useful to set memory limits and similar for the VM.

Added in version 258.

`--register=`  
Controls whether the virtual machine is registered with systemd-machined(8). Takes a boolean argument, which defaults to "`yes`" when running as root, and "`no`" when running as a regular user. This ensures that the virtual machine is accessible via machinectl(1).

Note: root privileges are required to use this option as registering with systemd-machined(8) requires privileged D-Bus method calls.

Added in version 256.

### User Namespacing Options

`--private-users=`*`UID_SHIFT[:UID_RANGE]`*  
Controls user namespacing under `--directory=`. If enabled, virtiofsd(1) is instructed to map user and group ids (UIDs and GIDs). This involves mapping the private UIDs/GIDs used in the virtual machine (starting with the virtual machine's root user 0 and up) to a range of UIDs/GIDs on the host that are not used for other purposes (usually in the range beyond the host's UID/GID 65536).

If one or two colon-separated numbers are specified, user namespacing is turned on. *`UID_SHIFT`* specifies the first host UID/GID to map, *`UID_RANGE`* is optional and specifies number of host UIDs/GIDs to assign to the virtual machine. If *`UID_RANGE`* is omitted, 65536 UIDs/GIDs are assigned.

When user namespaces are used, the GID range assigned to each virtual machine is always chosen identical to the UID range.

Added in version 256.

### Mount Options

`--bind=`*`PATH`*, `--bind-ro=`*`PATH`*  
Mount a directory from the host into the virtual machine. Takes one of: a path argument — in which case the specified path will be mounted from the host to the same path in the virtual machine, or a colon-separated pair of paths — in which case the first specified path is the source in the host, and the second path is the destination in the virtual machine. If the source path is not absolute, it is resolved relative to the current working directory. The `--bind-ro=` option creates read-only bind mounts. Backslash escapes are interpreted, so "`\:`" may be used to embed colons in either path. This option may be specified multiple times for creating multiple independent bind mount points.

Added in version 256.

`--extra-drive=[`*`FORMAT`*`:]`*`PATH`*  
Takes a disk image or block device on the host and supplies it to the virtual machine as another drive. Optionally, the image format can be specified by prefixing the path with "`raw`" or "`qcow2`" and a colon. The format defaults to "`raw`". Note that "`qcow2`" is only supported for regular files, not block devices.

Added in version 256.

`--bind-user=`  
Binds the home directory of the specified user on the host into the virtual machine. Takes the name of an existing user on the host as argument. May be used multiple times to bind multiple users into the virtual machine. This does two things:

1.  The user's home directory is made available from the host into `/run/vmhost/home/` using virtiofs. virtiofsd id translation to map the host user's UID/GID to its assigned UID/GID in the virtual machine.

2.  JSON user and group records are generated in that describes the mapped user which are passed into the virtual machine using "`userdb.transient.*`" credentials. They contain a minimized representation of the host's user record, adjusted to the UID/GID and home directory path assigned to the user in the virtual machine. The nss-systemd(8) glibc NSS module will pick up these records from there and make them available in the virtual machine's user/group databases.

The combination of the two operations above ensures that it is possible to log into the virtual machine using the same account information as on the host. The user is only mapped transiently, while the virtual machine is running, and the mapping itself does not result in persistent changes to the virtual machine (except maybe for log messages generated at login time, and similar). Note that in particular the UID/GID assignment in the virtual machine is not made persistently. If the user is mapped transiently, it is best to not allow the user to make persistent changes to the virtual machine. If the user leaves files or directories owned by the user, and those UIDs/GIDs are reused during later virtual machine invocations (possibly with a different `--bind-user=` mapping), those files and directories will be accessible to the "new" user.

The user/group record mapping only works if the virtual machine contains systemd 258 or newer, with **nss-systemd** properly configured in `nsswitch.conf`. See nss-systemd(8) for details.

Note that the user record propagated from the host into the virtual machine will contain the UNIX password hash of the user, so that seamless logins in the virtual machine are possible. If the virtual machine is less trusted than the host it is hence important to use a strong UNIX password hash function (e.g. yescrypt or similar, with the "`$y$`" hash prefix).

Added in version 259.

`--bind-user-shell=`  
When used with `--bind-user=`, includes the specified shell in the user records of users bound into the virtual machine. Takes either a boolean or an absolute path.

- If false (the default), no shell is passed in the user records for users bound into the virtual machine. This causes bound users to the use the virtual machine's default shell.

- If true, the shells specified by the host user records are included in the user records of all users bound into the virtual machine.

- If passed an absolute path, sets that path as the shell for user records of all users bound into the virtual machine.

Note: This will not check whether the specified shells exist in the virtual machine.

This operation is only supported in combination with `--bind-user=`.

Added in version 259.

`--bind-user-group=`*`NAME`*  
When used with `--bind-user=`, includes the specified group as an auxiliary group in the user records of users bound into the virtual machine. Takes a group name.

Note: This will not check whether the specified groups exist in the virtual machine.

This operation is only supported in combination with `--bind-user=`.

Added in version 259.

### Integration Options

`--forward-journal=`*`FILE|DIR`*  
Forward the virtual machine's journal to the host. systemd-journal-remote(8) is currently used to receive the guest VM's forwarded journal entries. This option determines where this journal is saved on the host and has the same semantics as `-o`/`--output` described in systemd-journal-remote(8).

Added in version 256.

`--pass-ssh-key=`*`BOOL`*  
By default, an SSH key is generated to allow **systemd-vmspawn** to open a D-Bus connection to the VM's systemd bus. Setting this to "no" will disable SSH key generation.

The generated keys are ephemeral. That is they are valid only for the current invocation of **systemd-vmspawn**, and are typically not persisted.

Added in version 256.

`--ssh-key-type=`*`TYPE`*  
Configures the type of SSH key to generate, see ssh-keygen(1) for more information.

By default, "`ed25519`" keys are generated, however "`rsa`" keys may also be useful if the VM has a particularly old version of sshd(8).

Added in version 256.

### Input/Output Options

`--console=`*`MODE`*  
Configures how to set up the console of the VM. Takes one of "`interactive`", "`read-only`", "`native`", "`gui`". Defaults to "`interactive`". "`interactive`" provides an interactive terminal interface to the VM. "`read-only`" is similar, but is strictly read-only, i.e. does not accept any input from the user. "`native`" also provides a TTY-based interface, but uses qemu native implementation (which means the qemu monitor is available). "`gui`" shows the qemu graphical UI.

Added in version 256.

`--background=`*`COLOR`*  
Change the terminal background color to the specified ANSI color as long as the VM runs. The color specified should be an ANSI X3.64 SGR background color, i.e. strings such as "`40`", "`41`", …, "`47`", "`48;2;…`", "`48;5;…`". See ANSI Escape Code (Wikipedia) for details. Assign an empty string to disable any coloring. This only has an effect in `--console=interactive` and `--console=read-only` modes.

Added in version 256.

### Credentials

`--load-credential=`*`ID`*`:`*`PATH`*, `--set-credential=`*`ID`*`:`*`VALUE`*  
Pass a credential to the virtual machine. These two options correspond to the `LoadCredential=` and `SetCredential=` settings in unit files. See systemd.exec(5) for details about these concepts, as well as the syntax of the option's arguments.

In order to embed binary data into the credential data for `--set-credential=`, use C-style escaping (i.e. "`\n`" to embed a newline, or "`\x00`" to embed a `NUL` byte). Note that the invoking shell might already apply unescaping once, hence this might require double escaping!

Added in version 255.

### Other

`--no-pager`  
Do not pipe output into a pager.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

`--no-ask-password`  
Do not query the user for authentication for privileged operations.

## Environment

`$SYSTEMD_LOG_LEVEL`  
The maximum log level of emitted messages (messages with a higher log level, i.e. less important ones, will be suppressed). Takes a comma-separated list of values. A value may be either one of (in order of decreasing importance) `emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, or an integer in the range 0…7. See syslog(3) for more information. Each value may optionally be prefixed with one of `console`, `syslog`, `kmsg` or `journal` followed by a colon to set the maximum log level for that specific log target (e.g. `SYSTEMD_LOG_LEVEL=debug,console:info` specifies to log at debug level except when logging to the console which should be at info level). Note that the global maximum log level takes priority over any per target maximum log levels.

`$SYSTEMD_LOG_COLOR`  
A boolean. If true, messages written to the tty will be colored according to priority.

This setting is only useful when messages are written directly to the terminal, because journalctl(1) and other tools that display logs will color messages based on the log level on their own.

`$SYSTEMD_LOG_TIME`  
A boolean. If true, console log messages will be prefixed with a timestamp.

This setting is only useful when messages are written directly to the terminal or a file, because journalctl(1) and other tools that display logs will attach timestamps based on the entry metadata on their own.

`$SYSTEMD_LOG_LOCATION`  
A boolean. If true, messages will be prefixed with a filename and line number in the source code where the message originates.

Note that the log location is often attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.

`$SYSTEMD_LOG_TID`  
A boolean. If true, messages will be prefixed with the current numerical thread ID (TID).

Note that the this information is attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.

`$SYSTEMD_LOG_TARGET`  
The destination for log messages. One of `console` (log to the attached tty), `console-prefixed` (log to the attached tty but with prefixes encoding the log level and "facility", see syslog(3), `kmsg` (log to the kernel circular log buffer), `journal` (log to the journal), `journal-or-kmsg` (log to the journal if available, and to kmsg otherwise), `auto` (determine the appropriate log target automatically, the default), `null` (disable log output).

`$SYSTEMD_LOG_RATELIMIT_KMSG`  
Whether to ratelimit kmsg or not. Takes a boolean. Defaults to "`true`". If disabled, systemd will not ratelimit messages written to kmsg.

`$SYSTEMD_PAGER`, `$PAGER`  
Pager to use when `--no-pager` is not given. `$SYSTEMD_PAGER` is used if set; otherwise `$PAGER` is used. If neither `$SYSTEMD_PAGER` nor `$PAGER` are set, a set of well-known pager implementations is tried in turn, including less(1) and more(1), until one is found. If no pager implementation is discovered, no pager is invoked. Setting those environment variables to an empty string or the value "`cat`" is equivalent to passing `--no-pager`.

Note: if `$SYSTEMD_PAGERSECURE` is not set, `$SYSTEMD_PAGER` and `$PAGER` can only be used to disable the pager (with "`cat`" or ""), and are otherwise ignored.

`$SYSTEMD_LESS`  
Override the options passed to **less** (by default "`FRSXMK`").

Users might want to change two options in particular:

`K`  
This option instructs the pager to exit immediately when **Ctrl**+**C** is pressed. To allow **less** to handle **Ctrl**+**C** itself to switch back to the pager command prompt, unset this option.

If the value of `$SYSTEMD_LESS` does not include "`K`", and the pager that is invoked is **less**, **Ctrl**+**C** will be ignored by the executable, and needs to be handled by the pager.

`X`  
This option instructs the pager to not send termcap initialization and deinitialization strings to the terminal. It is set by default to allow command output to remain visible in the terminal even after the pager exits. Nevertheless, this prevents some pager functionality from working, in particular paged output cannot be scrolled with the mouse.

Note that setting the regular `$LESS` environment variable has no effect for **less** invocations by systemd tools.

See less(1) for more discussion.

`$SYSTEMD_LESSCHARSET`  
Override the charset passed to **less** (by default "`utf-8`", if the invoking terminal is determined to be UTF-8 compatible).

Note that setting the regular `$LESSCHARSET` environment variable has no effect for **less** invocations by systemd tools.

`$SYSTEMD_PAGERSECURE`  
Common pager commands like less(1), in addition to "paging", i.e. scrolling through the output, support opening of or writing to other files and running arbitrary shell commands. When commands are invoked with elevated privileges, for example under sudo(8) or pkexec(1), the pager becomes a security boundary. Care must be taken that only programs with strictly limited functionality are used as pagers, and unintended interactive features like opening or creation of new files or starting of subprocesses are not allowed. "Secure mode" for the pager may be enabled as described below, *if the pager supports that* (most pagers are not written in a way that takes this into consideration). It is recommended to either explicitly enable "secure mode" or to completely disable the pager using `--no-pager` or `PAGER=cat` when allowing untrusted users to execute commands with elevated privileges.

This option takes a boolean argument. When set to true, the "secure mode" of the pager is enabled. In "secure mode", `LESSSECURE=1` will be set when invoking the pager, which instructs the pager to disable commands that open or create new files or start new subprocesses. Currently only less(1) is known to understand this variable and implement "secure mode".

When set to false, no limitation is placed on the pager. Setting `SYSTEMD_PAGERSECURE=0` or not removing it from the inherited environment may allow the user to invoke arbitrary commands.

When `$SYSTEMD_PAGERSECURE` is not set, systemd tools attempt to automatically figure out if "secure mode" should be enabled and whether the pager supports it. "Secure mode" is enabled if the effective UID is not the same as the owner of the login session, see geteuid(2) and sd_pid_get_owner_uid(3), or when running under sudo(8) or similar tools (`$SUDO_UID` is set <sup>\[1\]</sup>). In those cases, `SYSTEMD_PAGERSECURE=1` will be set and pagers which are not known to implement "secure mode" will not be used at all. Note that this autodetection only covers the most common mechanisms to elevate privileges and is intended as convenience. It is recommended to explicitly set `$SYSTEMD_PAGERSECURE` or disable the pager.

Note that if the `$SYSTEMD_PAGER` or `$PAGER` variables are to be honoured, other than to disable the pager, `$SYSTEMD_PAGERSECURE` must be set too.

`$SYSTEMD_COLORS`  
Takes a boolean argument, or a special value. By default (unset), **systemd** and related utilities will use colors in their output if possible. If `$COLORTERM` is set to "`truecolor`" or "`24bit`", 24-bit colors will be enabled, 256 colors otherwise, unless `$NO_COLOR` or `$TERM` indicates colors are disabled.

`true`  
Same as unset, except that `$NO_COLOR` is ignored.

`false`  
The output will be monochrome.

"`16`", "`256`", "`24bit`"  
Always use the base 16 ANSI colors, 256 colors, or 24 bit color, respectively.

"`auto-16`", "`auto-256`", "`auto-24bit`"  
Use the given quantity of colours, subject to `$TERM`, and what the console is connected to.

`$SYSTEMD_URLIFY`  
The value must be a boolean. Controls whether clickable links should be generated in the output for terminal emulators supporting this. This can be specified to override the decision that **systemd** makes based on `$TERM` and other conditions.

## Examples

**Example 1. Run an Arch Linux VM image generated by mkosi**

``` programlisting
$ mkosi -d arch -p systemd -p linux --autologin -o image.raw -f build
$ systemd-vmspawn --image=image.raw
```

  

**Example 2. Import and run a Fedora 43 Cloud image using machinectl**

``` programlisting
$ curl -L \
       -O https://download.fedoraproject.org/pub/fedora/linux/releases/43/Cloud/x86_64/images/Fedora-Cloud-Base-43-1.6.x86_64.raw.xz \
       -O https://download.fedoraproject.org/pub/fedora/linux/releases/43/Cloud/x86_64/images/Fedora-Cloud-43-1.6-x86_64-CHECKSUM \
       -O https://fedoraproject.org/fedora.gpg
$ gpgv --keyring ./fedora.gpg Fedora-Cloud-43-1.6-x86_64-CHECKSUM
$ sha256sum -c Fedora-Cloud-43-1.6-x86_64-CHECKSUM
# machinectl import-raw Fedora-Cloud-Base-43-1.6.x86_64.raw.xz fedora-43-cloud
# systemd-vmspawn -M fedora-43-cloud
```

  

**Example 3. Build and run systemd's system image and forward the VM's journal to a local file**

``` programlisting
$ mkosi build
$ systemd-vmspawn \
    -D mkosi.output/system \
    --private-users $(grep $(whoami) /etc/subuid | cut -d: -f2) \
    --linux mkosi.output/system.efi \
    --forward-journal=vm.journal \
    enforcing=0
```

Note: this example also uses a kernel command line argument to ensure SELinux is not started in enforcing mode.

  

**Example 4. SSH into a running VM using systemd-ssh-proxy**

``` programlisting
$ mkosi build
$ my_vsock_cid=3735928559
$ systemd-vmspawn \
    -D mkosi.output/system \
    --private-users $(grep $(whoami) /etc/subuid | cut -d: -f2) \
    --linux mkosi.output/system.efi \
    --vsock-cid $my_vsock_cid \
    enforcing=0
$ ssh root@vsock/$my_vsock_cid -i /run/user/$UID/systemd/vmspawn/machine-*-system-ed25519
```

  

## Exit status

If an error occurred the value errno is propagated to the return code. If EXIT_STATUS is supplied by the running image that is returned. Otherwise, EXIT_SUCCESS is returned.

## See Also

systemd(1), mkosi(1), machinectl(1), importctl(1), UAPI.1 Boot Loader Specification

  

<sup>\[1\]</sup> It is recommended for other tools to set and check `$SUDO_UID` as appropriate, treating it is a common interface.
