# NAME

iptables-restore — Restore IP Tables

ip6tables-restore — Restore IPv6 Tables

# SYNOPSIS

**iptables-restore** \[**-chntvV**\] \[**-w** *seconds*\] \[**-M** *modprobe*\] \[**-T** *name*\] \[*file*\]

**ip6tables-restore** \[**-chntvV**\] \[**-w** *seconds*\] \[**-M** *modprobe*\] \[**-T** *name*\] \[*file*\]

# DESCRIPTION

**iptables-restore** and **ip6tables-restore** are used to restore IP and IPv6 Tables from data specified on STDIN or in *file*. Use I/O redirection provided by your shell to read from a file or specify *file* as an argument.

**-c**, **--counters**
Restore the values of all packet and byte counters.

**-h**, **--help**
Print a short option summary.

**-n**, **--noflush**
Don't flush the previous contents of the table. If not specified, both commands flush (delete) all previous contents of the respective table. Note that this option will flush user-defined chains if they are declared. Example:


    *filter
    :FILTERS - [0:0]
    -A FILTERS ...

will flush and re-build the FILTERS chain from scratch, while retaining the content of all other chains in the table.

**-t**, **--test**
Only parse and construct the ruleset, but do not commit it.

**-v**, **--verbose**
Print additional debug info during ruleset processing. Specify multiple times to increase debug level.

**-V**, **--version**
Print the program version number.

**-w**, **--wait** \[*seconds*\]
Wait for the xtables lock. To prevent multiple instances of the program from running concurrently, an attempt will be made to obtain an exclusive lock at launch. By default, the program will exit if the lock cannot be obtained. This option will make the program wait (indefinitely or for optional *seconds*) until the exclusive lock can be obtained.

**-M**, **--modprobe** *modprobe*
Specify the path to the modprobe(8) program. By default, iptables-restore will inspect */proc/sys/kernel/modprobe* to determine the executable's path.

**-T**, **--table** *name*
Restore only the named table even if the input stream contains other ones.

# BUGS

None known as of iptables-1.2.1 release

# AUTHORS

Harald Welte \<laforge@gnumonks.org\> wrote iptables-restore based on code from Rusty Russell.
Andras Kis-Szabo \<kisza@sch.bme.hu\> contributed ip6tables-restore.

# SEE ALSO

**iptables-apply**(8), **iptables-save**(8), **iptables**(8)

The iptables-HOWTO, which details more iptables usage, the NAT-HOWTO, which details NAT, and the netfilter-hacking-HOWTO which details the internals.
