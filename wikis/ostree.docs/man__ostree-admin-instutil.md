## Name

ostree-admin-instutil — Utility functions intended primarily for operating system installation programs

## Synopsis

`ostree admin instutil` {SUBCOMMAND} \[ARGS\]

## Description

Use the subcommands to toggle admin installation utilities for selinux policies and kernel arguments.

## Subcommands

`selinux-ensure-labeled` \[SUBPATH PREFIX\]

  
Ensure all files and directories are labeled according to SELinux policy of the first deployment.

`set-kargs` \[--merge\] \[--import-proc-cmdline\] \[--append="NAME=VALUE"\] \[--replace="NAME=VALUE"\] \[MORE_APPEND_ARGS\]

  
Replace the kernel arguments of the default deployment. The new arguments are based on an empty list (the default), the current options (--merge), or the arguments of the loaded kernel (--import-proc-cmdline), and new options either are added to the end (--append="NAME=VALUE") or replace existing arguments of the same name (--replace="NAME=VALUE").
