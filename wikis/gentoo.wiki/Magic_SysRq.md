Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Magic_SysRq/hu "Magic SysRq (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Magic_SysRq/ja "マジック SysRq (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Magic_SysRq_key "wikipedia:Magic SysRq key")

[[]][Official documentation](https://www.kernel.org/doc/html/latest/admin-guide/sysrq.html)

**Magic SysRq** (Magic System Request) is a kernel hack that enables the kernel to listen to specific key presses and respond by calling a specific kernel function. Magic SysRq is activated via input from the keyboard or a serial line.

** Warning**\
Magic SysRq **should not** be enabled [in kernel] for production or mission critical systems! Even if Magic SysRq is disabled at boot using for example [sysctl], it still leaves [/proc/sysrq-trigger] open. Not to mention the fact that re-enabling SysRq is as easy as disabling it.

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [External resources]](#External_resources)

## [Kernel]

A basic Magic SysRq configuration:

[KERNEL] **Enable Magic SysRq (`CONFIG_MAGIC_SYSRQ` and `CONFIG_MAGIC_SYSRQ_DEFAULT_ENABLE` respectively)**

    Kernel hacking  --->
       Generic Kernel Debugging Instruments --->
          [*] Magic SysRq key
          (0x1) Enable magic SysRq key functions by default

** Important**\
The `CONFIG_MAGIC_SYSRQ_DEFAULT_ENABLE` value must always be written in the kernel with hexadecimal (0x) form (not integer numbers).

## [Usage]

### [Invocation]

On **[amd64]** and **[x86]** systems the key combination of [Alt]+[SysRq]+\<command key\> will result in Magic SysRQ invocation. See the following table for some possible options:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------
  Command key                                                                                                                                                          Description
  [b]   Immediately reboot the system without syncing or unmounting the disks.
  [e]   Send a SIGTERM to all processes, except for init.
  [f]   Calls the OOM killer to kill a memory hog process; does not panic if nothing can be killed.
  [s]   Attempts to sync all mounted filesystems.
  [u]   Attempts to remount all mounted filesystems read-only.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------

More information can be found in the [official Magic SysRQ Linux Kernel documentation](https://www.kernel.org/doc/html/latest/admin-guide/sysrq.html).

** Note**\
Not all keyboards include a [SysRq] key. Typically [Print Screen] is the same key.

## [External resources]

-   [Magic SysRq Key](http://www.linuxhowtos.org/Tips%20and%20Tricks/sysrq.htm) at LinuxHowtos.org.
-   [Wikipedia:System request](https://en.wikipedia.org/wiki/System_request "wikipedia:System request") - History on the system request key.