# btrfs(8)

## SYNOPSIS

**btrfs** \[global options\] \<group\> \[\<group\>...\] \<command\> \[options\] \[\<args\>\]

## DESCRIPTION

The `btrfs` utility is a toolbox for managing btrfs filesystems. There are command groups to work with subvolumes, devices, for whole filesystem or other specific actions. See section `COMMANDS<man-btrfs8-commands>`.

There are also standalone tools for some tasks like `btrfs-convert` or `btrfstune` that were separate historically and/or haven't been merged to the main utility. See section `STANDALONE TOOLS<man-btrfs8-standalone-tools>` for more details.

For other topics (mount options, etc) please refer to the separate manual page `btrfs-man5`.

## COMMAND SYNTAX

Any command name can be shortened so long as the shortened form is unambiguous, however, it is recommended to use full command names in scripts. All command groups have their manual page named **btrfs-\<group\>**.

For example: it is possible to run `btrfs sub snaps` instead of `btrfs subvolume snapshot`. But `btrfs file s` is not allowed, because `file s` may be interpreted both as `filesystem show` and as `filesystem sync`.

If the command name is ambiguous, the list of conflicting options is printed.

*Sizes*, both upon input and output, can be expressed in either SI or IEC-I units (see `numfmt(1)`) with the suffix B appended. All numbers will be formatted according to the rules of the C locale (ignoring the shell locale, see `locale(7)`).

For an overview of a given command use `btrfs command --help` or `btrfs [command...] help --full` to print all available options for all commands.

There are global options that are passed between *btrfs* and the *group* name and affect behaviour not specific to the command, e.g. verbosity or the type of the output:

``` bash
btrfs -q subvolume create ...
btrfs --dry-run subvolume create ...
```

`--format <format>`
if supported by the command, print subcommand output in that format (text, json)


-v\|--verbose
increase verbosity of the subcommand

-q\|--quiet
print only errors

--log \<level\>
set log level (default, info, verbose, debug, quiet)

The remaining options are relevant only for the main tool:

`--help`
print condensed help for all subcommands

`--version`
print version string

## COMMANDS

balance
Balance btrfs filesystem chunks across single or several devices. See `btrfs-balance` for details.

check
Do off-line check on a btrfs filesystem. See `btrfs-check` for details.

device
Manage devices managed by btrfs, including add/delete/scan and so on. See `btrfs-device` for details.

filesystem
Manage a btrfs filesystem, including label setting/sync and so on.
See `btrfs-filesystem` for details.

inspect-internal
Debug tools for developers/hackers. See `btrfs-inspect-internal` for details.

property
Get/set a property from/to a btrfs object. See `btrfs-property` for details.

qgroup
Manage quota group(qgroup) for btrfs filesystem. See `btrfs-qgroup` for details.

quota
Manage quota on btrfs filesystem like enabling/rescan and etc. See `btrfs-quota` and `btrfs-qgroup` for details.

receive
Receive subvolume data from stdin/file for restore and etc. See `btrfs-receive` for details.

replace
Replace btrfs devices. See `btrfs-replace` for details.

rescue
Try to rescue damaged btrfs filesystem. See `btrfs-rescue` for details.

restore
Try to restore files from a damaged btrfs filesystem. See `btrfs-restore` for details.

scrub
Scrub a btrfs filesystem. See `btrfs-scrub` for details.

send
Send subvolume data to stdout/file for backup and etc. See `btrfs-send` for details.

subvolume
Create/delete/list/manage btrfs subvolume. See `btrfs-subvolume` for details.

## STANDALONE TOOLS

New functionality could be provided using a standalone tool. If the functionality proves to be useful, then the standalone tool is declared obsolete and its functionality is copied to the main tool. Obsolete tools are removed after a long (years) depreciation period.

Tools that are still in active use without an equivalent in `btrfs`:

btrfs-convert
in-place conversion from ext2/3/4 filesystems to btrfs

btrfstune
tweak some filesystem properties on a unmounted filesystem

btrfs-select-super
rescue tool to overwrite primary superblock from a spare copy

btrfs-find-root
rescue helper to find tree roots in a filesystem

For space-constrained environments, it's possible to build a single binary with functionality of several standalone tools. This is following the concept of busybox where the file name selects the functionality. This works for symlinks or hardlinks. The full list can be obtained by `btrfs help --box`.

## EXIT STATUS

**btrfs** returns a zero exit status if it succeeds. Non zero is returned in case of failure.

## AVAILABILITY

**btrfs** is part of btrfs-progs. Please refer to the documentation at <https://btrfs.readthedocs.io>.

## SEE ALSO

`btrfs-man5`, `btrfs-balance`, `btrfs-check`, `btrfs-convert`, `btrfs-device`, `btrfs-filesystem`, `btrfs-inspect-internal`, `btrfs-property`, `btrfs-qgroup`, `btrfs-quota`, `btrfs-receive`, `btrfs-replace`, `btrfs-rescue`, `btrfs-restore`, `btrfs-scrub`, `btrfs-send`, `btrfs-subvolume`, `btrfstune`, `mkfs.btrfs`
