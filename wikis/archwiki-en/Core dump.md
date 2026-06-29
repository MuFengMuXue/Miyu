# Core dump

A core dump is a file containing a process's address space (memory) when the process terminates unexpectedly. Core dumps may be produced on-demand (such as by a debugger), or automatically upon termination. Core dumps are triggered by the kernel in response to program crashes, and may be passed to a helper program (such as ) for further processing. A core dump is not typically used by an average user, but developers could use it as a post-mortem snapshot of the program's state at the time of the crash, especially if the fault is hard to reliably reproduce.

## Disabling automatic core dumps
Users may wish to disable automatic core dumps for a number of reasons:
* Performance: generating core dumps for memory-heavy processes can waste system resources and delay the cleanup of memory.
* Disk space: core dumps of memory-heavy processes may consume disk space equal to, if not greater, than the process's memory footprint if not compressed.
* Security: core dumps, although typically readable only by root, may contain sensitive data (such as passwords or cryptographic keys), which are written to disk following a crash.

## Using sysctl
sysctl can be used to set the  to nothing to disable core dump handling. Create this file

To apply the setting immediately, use :

 # sysctl -p /etc/sysctl.d/50-coredump.conf

## Using systemd
systemd's default behavior is defined in , which sets  to call . It generates core dumps for all processes in .  behavior can be overridden by creating a configuration snippet in the  directory with the following content (See , Then reload the systemd manager configuration with daemon-reload.

See .

## Using PAM limits
See limits.conf#core.

## Using ulimit
Command-line shells such as bash or zsh provide a builtin ulimit command which can be used to report or set resource limits of the shell and the processes started by the shell. See  or  for details.

To disable core dumps in the current shell:

 $ ulimit -c 0

If the system is setup to pipe coredumps into a program such as systemd-coredump using , the Linux kernel itself ignores the ulimit setting (see ), so then it depends on the program the dump gets piped to whether this setting is respected or not (systemd-coredump will still use it).

For programs not using the ulimit setting of the crashed process,   can be used to disable coredump processing for selected processes.

## Making a core dump
To generate a core dump of an arbitrary process, first install the  package. Then attach to this process by following Debugging/Getting traces#Attaching to an existing process.

Then at the  prompt:

 (gdb) generate-core-file
 Saved corefile core.2071
 (gdb) quit

Now you have a coredump file called .

## Where do they go?
The  sysctl decides where automatic core dumps go. By default, core dumps are sent to systemd-coredump which can be configured in . By default, all core dumps are stored in  (due to ) and they are compressed with  (due to ). Additionally, various size limits for the storage can be configured.

To retrieve a core dump from the journal, see .

## Managing the core dump files
Use coredumpctl to find the corresponding dump. Note that regular users can run coredumpctl without special privileges to manage core dumps of their processes.

 # coredumpctl list

## Cleanup of core dump files
The core dump files stored in  will be automatically cleaned by , which is triggered daily with . Core dumps are configured to persist for at least 2 weeks, see .

See Journal#Clean journal files manually to remove the entries.

## Analyzing a core dump
First, you need to uniquely identify the relevant dump. This is possible by specifying a , name of the executable, path to the executable or a journalctl predicate (see  and  for details). To see details of the core dumps:

 # coredumpctl info match

Pay attention to "Signal" row, that helps to identify crash cause. For the analysis one usually examine the backtrace using a debugger ( by default):

 # coredumpctl debug match

When gdb is started, use the  command to print the full backtrace:

 (gdb) thread apply all backtrace full

In many cases, the output will contain question marks as placeholders for missing debugging symbols. See Debugging/Getting traces for how to obtain them.
