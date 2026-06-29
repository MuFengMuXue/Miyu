# Procfs

The proc file system, also called procfs, is a pseudo file system that is usually mounted at  and contains information about the running system:

* Processes, the most prominent use.
* Kernel information and parameters.
* System metrics, such as CPU usage.

## Content
## Kernel & system information
There are many files under  which provide a lot of information about the system as well as the kernel. There are too many to cover them all here, but some of them are listed below with brief information about what they are.

*  - informations about CPU
*  - information about the physical memory
*  - information about the virtual memory
*  - information about the mounts
*  - information about filesystems that have been compiled into the kernel and whose kernel modules are currently loaded
*  - current system uptime
*  - kernel command line

## Processes
Inside  is stored information about every process currently running.
Below is an example showing some of the PIDs currently running:

Lets take for example pid 1057 and see what is inside:

Some of the fields:

*  - arguments used to start program.
*  - current working directory for the process.
*  - environment variables inside the process (zero-delimited).
*  - directory containing open file descriptors for the process.
*  - symbolic link to process executable.
*  - memory mapping of the process.
*  - virtual memory of the process.

## Usage
You can interact with  contents as with regular files.

To read from a file:

 $ cat /proc/cmdline

To write to a file:

 # echo 1 > /proc/sys/kernel/sysrq
