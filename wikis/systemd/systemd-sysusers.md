## Name

systemd-sysusers, systemd-sysusers.service — Allocate system users and groups

## Synopsis

`systemd-sysusers` \[OPTIONS...\] \[*`CONFIGFILE`*...\]

`systemd-sysusers.service`

## Description

**systemd-sysusers** creates system users and groups, based on files in the format described in sysusers.d(5).

If invoked with no arguments, directives from the configuration files found in the directories specified by sysusers.d(5) are executed. When invoked with positional arguments, if option `--replace=`*`PATH`* is specified, arguments specified on the command line are used instead of the configuration file *`PATH`*. Otherwise, just the configuration specified by the command line arguments is executed. If the string "`-`" is specified instead of a filename, the configuration is read from standard input. If the argument is a file name (without any slashes), all configuration directories are searched for a matching file and the file found that has the highest priority is executed. If the argument is a path, that file is used directly without searching the configuration directories for any other matching file.

## Options

The following options are understood:

`--root=`*`root`*  
Takes a directory path as an argument. All paths will be prefixed with the given alternate *`root`* path, including config search paths.

Added in version 215.

`--image=`*`image`*  
Takes a path to a disk image file or block device node. If specified all operations are applied to file system in the indicated disk image. This is similar to `--root=` but operates on file systems stored in disk images or block devices. The disk image should either contain just a file system or a set of file systems within a GPT partition table, following the UAPI.2 Discoverable Partitions Specification. For further information on supported disk images, see systemd-nspawn(1)'s switch of the same name.

Added in version 247.

`--image-policy=`*`policy`*  
Takes an image policy string as argument, as per systemd.image-policy(7). The policy is enforced when operating on the disk image specified via `--image=`, see above. If not specified, defaults to the "`*`" policy, i.e. all recognized file systems in the image are used.

`--replace=`*`PATH`*  
When this option is given, one or more positional arguments must be specified. All configuration files found in the directories listed in sysusers.d(5) will be read, and the configuration given on the command line will be handled instead of and with the same priority as the configuration file *`PATH`*.

This option is intended to be used when package installation scripts are running and files belonging to that package are not yet available on disk, so their contents must be given on the command line, but the admin configuration might already exist and should be given higher priority.

**Example 1. RPM installation script for radvd**

``` programlisting
echo 'u radvd - "radvd daemon"' | \
          systemd-sysusers --replace=/usr/lib/sysusers.d/radvd.conf -
```

This will create the radvd user as if `/usr/lib/sysusers.d/radvd.conf` was already on disk. An admin might override the configuration specified on the command line by placing `/etc/sysusers.d/radvd.conf` or even `/etc/sysusers.d/00-overrides.conf`.

Note that this is the expanded form, and when used in a package, this would be written using a macro with "radvd" and a file containing the configuration line as arguments.

  

Added in version 238.

`--dry-run`  
Process the configuration and figure out what entries would be created, but do not actually write anything.

Added in version 250.

`--inline`  
Treat each positional argument as a separate configuration line instead of a file name.

Added in version 238.

`--cat-config`  
Copy the contents of config files to standard output. Before each file, the filename is printed as a comment.

`--tldr`  
Copy the contents of config files to standard output. Only the "interesting" parts of the configuration files are printed, comments and empty lines are skipped. Before each file, the filename is printed as a comment.

`--no-pager`  
Do not pipe output into a pager.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Credentials

**systemd-sysusers** supports the service credentials logic as implemented by `ImportCredential=`/`LoadCredential=`/`SetCredential=` (see systemd.exec(5) for details). The following credentials are used when passed in:

`passwd.hashed-password.`*`user`*  
A UNIX hashed password string to use for the specified user, when creating an entry for it. This is particularly useful for the "`root`" user as it allows provisioning the default root password to use via a unit file drop-in or from a container manager passing in this credential. Note that setting this credential has no effect if the specified user account already exists. This credential is hence primarily useful in first boot scenarios or systems that are fully stateless and come up with an empty `/etc/` on every boot.

Added in version 249.

`passwd.plaintext-password.`*`user`*  
Similar to "`passwd.hashed-password.`*`user`*" but expect a literal, plaintext password, which is then automatically hashed before used for the user account. If both the hashed and the plaintext credential are specified for the same user the former takes precedence. It's generally recommended to specify the hashed version; however in test environments with weaker requirements on security it might be easier to pass passwords in plaintext instead.

Added in version 249.

`passwd.shell.`*`user`*  
Specifies the shell binary to use for the specified account when creating it.

Added in version 249.

`sysusers.extra`  
The contents of this credential may contain additional lines to operate on. The credential contents should follow the same format as any other `sysusers.d/` drop-in. If this credential is passed it is processed after all of the drop-in files read from the file system.

Added in version 252.

Note that by default the `systemd-sysusers.service` unit file is set up to inherit the "`passwd.hashed-password.root`", "`passwd.plaintext-password.root`", "`passwd.shell.root`" and "`sysusers.extra`" credentials from the service manager. Thus, when invoking a container with an unpopulated `/etc/` for the first time it is possible to configure the root user's password to be "`systemd`" like this:

``` programlisting
# systemd-nspawn --image=… --set-credential=passwd.hashed-password.root:'$y$j9T$yAuRJu1o5HioZAGDYPU5d.$F64ni6J2y2nNQve90M/p0ZP0ECP/qqzipNyaY9fjGpC' …
```

Note again that the data specified in this credential is consulted only when creating an account for the first time, it may not be used for changing the password or shell of an account that already exists.

Use mkpasswd(1) for generating UNIX password hashes from the command line.

## Exit status

On success, 0 is returned, a non-zero failure code otherwise.

## See Also

systemd(1), sysusers.d(5), Users, Groups, UIDs and GIDs on systemd systems, systemd.exec(5), mkpasswd(1)
