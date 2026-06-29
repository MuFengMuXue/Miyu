## Name

importctl — Download, import or export disk images

## Synopsis

`importctl` \[OPTIONS...\] {COMMAND} \[NAME...\]

## Description

**importctl** may be used to download, import, and export disk images via systemd-importd.service(8).

**importctl** operates both on block-level disk images (such as DDIs), file-system-level images (tarballs), as well as OCI images. It supports disk images in one of the four following classes:

- VM images or full OS container images, that may be run via systemd-vmspawn(1) or systemd-nspawn(1), and managed via machinectl(1).

- Portable service images, that may be attached and managed via portablectl(1).

- System extension (sysext) images, that may be activated via systemd-sysext(8).

- Configuration extension (confext) images, that may be activated via systemd-confext(8).

When images are downloaded or imported they are placed in the following directories, depending on the `--class=` parameter:

**Table 1. Classes and Directories**

| Class        | Directory              |
|--------------|------------------------|
| "`machine`"  | `/var/lib/machines/`   |
| "`portable`" | `/var/lib/portables/`  |
| "`sysext`"   | `/var/lib/extensions/` |
| "`confext`"  | `/var/lib/confexts/`   |

  

## Commands

The following commands are understood:

**pull-tar** *`URL`* \[*`NAME`*\]  
Downloads a `.tar` image from the specified URL, and makes it available under the specified local name in the image directory for the selected `--class=`. The URL must be of type "`http://`" or "`https://`", and must refer to a `.tar`, `.tar.gz`, `.tar.xz` or `.tar.bz2` archive file. If the local image name is omitted, it is automatically derived from the last component of the URL, with its suffix removed.

The image is verified before it is made available, unless `--verify=no` is specified. Verification is done either via a file with the name of the image and the suffix `.sha256` and a detached `.sha256.asc` or `.sha256.gpg` signature or via separate `SHA256SUMS` and `SHA256SUMS.asc` or `SHA256SUMS.gpg` files. The signature files need to be made available on the same web server, under the same URL as the `.tar` file. With `--verify=checksum`, only the SHA256 checksum for the file is verified, based on the `.sha256` suffixed file or the `SHA256SUMS` file. With `--verify=signature`, the sha checksum file is first verified with the detached GPG signature of `.sha256` or `SHA256SUMS`. The public key for this verification step needs to be available in `/usr/lib/systemd/import-pubring.pgp` or `/etc/systemd/import-pubring.pgp`.

If `-keep-download=yes` is specified the image will be downloaded and stored in a read-only subvolume/directory in the image directory that is named after the specified URL and its HTTP etag (see HTTP ETag for more information). A writable snapshot is then taken from this subvolume, and named after the specified local name. This behavior ensures that creating multiple instances of the same URL is efficient, as multiple downloads are not necessary. In order to create only the read-only image, and avoid creating its writable snapshot, specify "`-`" as local name.

Note that pressing Control-c during execution of this command will not abort the download. Use **cancel-transfer**, described below.

Added in version 256.

**pull-raw** *`URL`* \[*`NAME`*\]  
Downloads a `.raw` disk image from the specified URL, and makes it available under the specified local name in the image directory for the selected `--class=`. The URL must be of type "`http://`" or "`https://`". The image must either be a qcow2 or raw disk image, optionally compressed as `.gz`, `.xz`, or `.bz2`. If the local name is omitted, it is automatically derived from the last component of the URL, with its suffix removed.

Image verification is identical for raw and tar images (see above).

If the downloaded image is in qcow2 format it is converted into a raw image file before it is made available.

If `-keep-download=yes` is specified the image will be downloaded and stored in a read-only file in the image directory that is named after the specified URL and its HTTP etag. A writable copy is then made from this file, and named after the specified local name. This behavior ensures that creating multiple instances of the same URL is efficient, as multiple downloads are not necessary. In order to create only the read-only image, and avoid creating its writable copy, specify "`-`" as local name.

Note that pressing Control-c during execution of this command will not abort the download. Use **cancel-transfer**, described below.

Added in version 256.

**pull-oci** *`REF`* \[*`NAME`*\]  
Downloads the specified OCI container image, and makes it available under the specified local name in the image directory for the selected `--class=`. The first argument must be an OCI container reference, such as "`library/nginx`" If the local name is omitted, it is automatically derived from the last component of the URL, with its suffix removed.

When downloading images of this type no image verification is done beyond the usual authentication of the HTTPS certificates.

Note that pressing Control-c during execution of this command will not abort the download. Use **cancel-transfer**, described below.

Added in version 260.

**import-tar** *`FILE`* \[*`NAME`*\], **import-raw** *`FILE`* \[*`NAME`*\]  
Imports a TAR or RAW image, and places it under the specified name in the image directory for the image class selected via `--class=`. When **import-tar** is used, the file specified as the first argument should be a tar(1) archive, possibly compressed with xz(1), gzip(1), zstd(1), or bzip2(1). It will then be unpacked into its own subvolume/directory. When **import-raw** is used, the file should be a qcow2 or raw disk image, possibly compressed with xz, gzip, zstd or bzip2. If the second argument (the resulting image name) is not specified, it is automatically derived from the file name. If the filename is passed as "`-`", the image is read from standard input, in which case the second argument is mandatory.

No cryptographic validation is done when importing the images.

Much like image downloads, ongoing imports may be listed with **list** and aborted with **cancel-transfer**.

Added in version 256.

**import-fs** *`DIRECTORY`* \[*`NAME`*\]  
Imports an image stored in a local directory into the image directory for the image class selected via `--class=` and operates similarly to **import-tar** or **import-raw**, but the first argument is the source directory. If supported, this command will create a btrfs(8) snapshot or subvolume for the new image.

Added in version 256.

**export-tar** *`NAME`* \[*`FILE`*\], **export-raw** *`NAME`* \[*`FILE`*\]  
Exports a TAR or RAW image and stores it in the specified file. The first parameter should be an image name. The second parameter should be a file path the TAR or RAW image is written to. If the path ends in "`.gz`", the file is compressed with gzip(1), if it ends in "`.xz`", with xz(1), if it ends in "`.zst`", with zstd(1), and if it ends in "`.bz2`", with bzip2(1). If the path ends in neither, the file is left uncompressed. If the second argument is missing, the image is written to standard output. The compression may also be explicitly selected with the `--format=` switch. This is in particular useful if the second parameter is left unspecified.

Much like image downloads and imports, ongoing exports may be listed with **list** and aborted with **cancel-transfer**.

Note that, currently, only directory and subvolume images may be exported as TAR images, and only raw disk images as RAW images.

Added in version 256.

**list-transfer**  
Shows a list of image downloads, imports and exports that are currently in progress.

Added in version 256.

**cancel-transfer** *`ID`*…  
Aborts a download, import or export of the image with the specified ID. To list ongoing transfers and their IDs, use **list**.

Added in version 256.

**list-images**  
Shows a list of already downloaded/imported images.

Added in version 256.

## Options

The following options are understood:

`--read-only`  
When used with **pull-raw**, **pull-tar**, **import-raw**, **import-tar** or **import-fs** a read-only image is created.

Added in version 256.

`--verify=`  
When downloading an image, specify whether the image shall be verified before it is made available. Takes one of "`no`", "`checksum`" and "`signature`". If "`no`", no verification is done. If "`checksum`" is specified, the download is checked for integrity after the transfer is complete, but no signatures are verified. If "`signature`" is specified, the checksum is verified and the image's signature is checked against a local keyring of trustable vendors. It is strongly recommended to set this option to "`signature`" if the server and protocol support this. Defaults to "`signature`".

Added in version 256.

`--force`  
When downloading an image, and a local copy by the specified local name already exists, delete it first and replace it by the newly downloaded image.

Added in version 256.

`--format=`  
When used with the `export-tar` or `export-raw` commands, specifies the compression format to use for the resulting file. Takes one of "`uncompressed`", "`xz`", "`gzip`", "`zst`", "`bzip2`". By default, the format is determined automatically from the output image file name passed.

Added in version 256.

`-q`, `--quiet`  
Suppresses additional informational output while running.

Added in version 256.

`-H`, `--host=`  
Execute the operation remotely. Specify a hostname, or a username and hostname separated by "`@`", to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by "`:`", and then a container name, separated by "`/`", which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with **machinectl -H *`HOST`***. Put IPv6 addresses in brackets.

`-M`, `--machine=`  
Connect to systemd-importd.service(8) running in a local container, to perform the specified operation within the container.

Added in version 256.

`--class=`, `-m`, `-P`, `-S`, `-C`  
Selects the image class for the downloaded images. This primarily selects the directory to download into. The `--class=` switch takes "`machine`", "`portable`", "`sysext`" or "`confext`" as argument. The short options `-m`, `-P`, `-S`, `-C` are shortcuts for `--class=machine`, `--class=portable`, `--class=sysext`, `--class=confext`.

Note that `--keep-download=` defaults to true for `--class=machine` and false otherwise, see below.

Added in version 256.

`--keep-download=`, `-N`  
Takes a boolean argument. When specified with **pull-raw** or **pull-tar**, selects whether to download directly into the specified local image name, or whether to download into a read-only copy first of which to make a writable copy after the download is completed. Defaults to true for `--class=machine`, false otherwise.

The `-N` switch is a shortcut for `--keep-download=no`.

Added in version 256.

`--json=`*`MODE`*  
Shows output formatted as JSON. Expects one of "`short`" (for the shortest possible output without any redundant whitespace or line breaks), "`pretty`" (for a pretty version of the same, with indentation and line breaks) or "`off`" (to turn off JSON output, the default).

`-j`  
Equivalent to `--json=pretty` if running on a terminal, and `--json=short` otherwise.

`--no-pager`  
Do not pipe output into a pager.

`--no-legend`  
Do not print the legend, i.e. column headers and the footer with hints.

`--no-ask-password`  
Do not query the user for authentication for privileged operations.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Examples

**Example 1. Download an Ubuntu TAR image and open a shell in it**

``` programlisting
# importctl pull-tar -mN https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64-root.tar.xz
# systemd-nspawn -M jammy-server-cloudimg-amd64-root
```

This downloads and verifies the specified `.tar` image, and then uses systemd-nspawn(1) to open a shell in it.

  

**Example 2. Download an Ubuntu RAW image, set a root password in it, start it as a service**

``` programlisting
# importctl pull-raw -mN \
      https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64-disk-kvm.img \
      jammy
# systemd-firstboot --image=/var/lib/machines/jammy.raw --prompt-root-password --force
# machinectl start jammy
# machinectl login jammy
```

This downloads the specified `.raw` image and makes it available under the local name "`jammy`". Then, a root password is set with systemd-firstboot(1). Afterwards the machine is started as system service. With the last command a login prompt into the container is requested.

  

**Example 3. Exports a container image as tar file**

``` programlisting
# importctl export-tar -m fedora myfedora.tar.xz
```

Exports the container "`fedora`" as an xz-compressed tar file `myfedora.tar.xz` into the current directory.

  

## Exit status

On success, 0 is returned, a non-zero failure code otherwise.

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

## See Also

systemd(1), systemd-importd.service(8), systemd-nspawn(1), systemd-vmspawn(1), machinectl(1), portablectl(1), systemd-sysext(8), systemd-confext(8), tar(1), xz(1), gzip(1), zstd(1), bzip2(1)

  

<sup>\[1\]</sup> It is recommended for other tools to set and check `$SUDO_UID` as appropriate, treating it is a common interface.
