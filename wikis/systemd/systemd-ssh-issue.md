## Name

systemd-ssh-issue — Generator for SSH login prompt drop-ins

## Synopsis

`/usr/lib/systemd/systemd-ssh-issue ``--make-vsock`  
`/usr/lib/systemd/systemd-ssh-issue ``--rm-vsock`

## Description

**systemd-ssh-issue** is a small tool that generates a `/run/issue.d/50-ssh-vsock.issue` drop-in file in case `AF_VSOCK` support is available in the kernel and the VM environment. The file contains brief information about how to contact the local system via SSH-over-`AF_VSOCK`, in particular it reports the system's `AF_VSOCK` CID. The file is typically read and displayed by agetty(8) on console or serial login prompts.

This tool is automatically used by systemd-ssh-generator(8) in the `AF_VSOCK` socket units it generates.

## Options

The following options are understood:

`--make-vsock`  
Generates the issue file. This command has no effect if called on systems lacking `AF_VSOCK` support.

Added in version 258.

`--rm-vsock`  
Removes the issue file if it exists.

Added in version 258.

`--issue-path=`  
Changes the path to the issue file to write to/remove. If not specified, defaults to `/run/issue.d/50-ssh-vsock.issue`. If specified as empty string or "`-`" writes the issue file contents to standard output.

Added in version 258.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Exit status

On success, 0 is returned, a non-zero failure code otherwise.

## See Also

systemd(1), systemd-ssh-generator(8), vsock(7), ssh(1), sshd(8), agetty(8)
