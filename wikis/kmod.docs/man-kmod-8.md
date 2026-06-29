# KMOD(8) "kmod" "kmod"


## Name

kmod - Program to manage Linux Kernel modules


## Synopsis

`kmod` [`OPTIONS`] [_COMMAND_] [`COMMAND_OPTIONS`]


## Description

`kmod` is a multi-call binary which implements the programs used to control
Linux Kernel modules. Most users will only run it using its other names.


## Options

`-V`, `--version`
	Show the program version and exit.

`-h`, `--help`
	Show the help message.


## Commands

`help`
	Show the help message.

`list`
	List the currently loaded modules.

`static-nodes`
	Output the static device nodes information provided by the modules of
	the currently running kernel version.


## See Also

`lsmod`(8), `rmmod`(8), `insmod`(8), `modinfo`(8), `modprobe`(8), `depmod`(8)
