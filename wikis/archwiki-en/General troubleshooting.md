# General troubleshooting

This article explains some methods for general troubleshooting. For application specific issues, please reference the particular wiki page for that program.

## General procedures
It is crucial to always read any error messages that appear. Sometimes it may be hard, e.g. with graphical applications, to get a proper error message.

# Run the application in a terminal so it is possible to inspect the output.
## Increase the verbosity (usually // or /) if there is still not enough information to debug.
## Sometimes there is no such parameter and it needs to be specified as a directive in the applications' configuration file.
## An application may also use log files, which are usually located in ,  or
## If there is no way to increase the verbosity, it is always possible to run strace and similar.
# Check the journal. It is possible that an error may also leave traces in the journal, especially if it depends on other applications.
## dmesg reads from the kernel ring buffer. This is useful if the disk is for some reason inaccessible but this may also result in incomplete logs because the kernel ring buffer is not infinite in size. Use journalctl if possible.
## journalctl has more filtering options than dmesg and uses human-readable timestamps by default.
# It is always recommended to check the relevant issue trackers to see if there are known issues with already existing solutions.
## Depending on upstreams' choices, there is usually an issue tracker and sometimes also a forum or even e.g. an IRC channel.
## There is the Arch Linux bug tracker, which should be primarily used for packaging bugs.

## Additional support
If you require any additional support, you may ask on the forums or on IRC.

When asking for support post the complete output/logs, not just what you think are the significant sections. Sources of information include:

* Full output of any command involved - do not just select what you think is relevant.
* systemd's journal.
** For more extensive output, use the  boot parameter. This will produce a tremendous amount of output, so only enable it if it is really needed.
** Do not use the  parameter because this needlessly clutters the output and makes it harder to read.
** Use  unless you need logs from a previous boot. Not specifying this may lead to extremely large pastes that may even be too big for any pastebins.
* Relevant configuration files
* Drivers involved
* Versions of packages involved
* Kernel:  or  (both with root privileges).
* Xorg: depending on the setup the display manager in use is relevant here, too.
**  may be located in one of several places: the system journal,  or .
** Some display managers like LightDM may also place the  in its own log directory.
* Pacman: If a recent upgrade broke something, look in .
** It may be useful to use pacmans  parameter.

One of the better ways to post this information is to use a pastebin.

A link will then be output that you can paste to the forum or IRC.

Additionally, you may wish to review how to properly report issues before asking.

## Boot problems
When diagnosing boot problems, it is very important to know in which stage the boot fails.

# Firmware (UEFI or BIOS)
## Usually only has very basic tools for debugging.
## Make sure Secure Boot is disabled.
# Boot loader
## One of the most common things done here is the changing of kernel parameters.
## Common boot issue during the boot loader stage could be caused by ACPI.
# initramfs
## Usually provides an emergency shell.
## Depending on the hooks chosen, either the dmesg or the journal is available within it.
# The actual system
## Depending on how badly it is broken, a simple invocation of the debug shell may suffice here.

If the debugging tools provided by any stage are not enough to fix the broken component, try using a e.g. USB stick with the latest Arch Linux ISO on it.

## Console messages
After the boot process, the screen is cleared and the login prompt appears, leaving users unable to read init output and error messages. This default behavior may be modified using methods outlined in the sections below.

Note that regardless of the chosen option, kernel messages can be displayed for inspection after booting by using  or . To display all logs from the current boot use .

## Flow control
This is basic management that applies to most terminal emulators, including virtual consoles (VC):

* Press  to pause the output.
* And  to resume it.

This pauses not only the output, but also programs which try to print to the terminal, as they will block on the  calls for as long as the output is paused. If your init appears frozen, make sure the system console is not paused.

To see error messages which are already displayed, see Getty#Have boot messages stay on tty1.

## Printing more kernel messages
Most kernel messages are hidden during boot. You can see more of these messages by adding different kernel parameters. The simplest ones are:

* , which has the following effects:
** The kernel will raise its console logging level such that all messages in the kernel log buffer will be printed to the console. ** systemd will raise its log level such that it will log debug messages that otherwise would not be produced anywhere. [https://github.com/systemd/systemd/blob/v251/src/basic/log.c#L1125-L1126
* , which has the same effect on the kernel as  or  (since debug messages are at ), but prevents the log level from being raised later in the boot.

Other parameters you can add that might be useful in certain situations are:

*  prints kernel messages very early in the boot process, in case the kernel would crash before output is shown. You must change  to  for EFI systems.
*  allocates a larger (16 MiB) kernel message buffer, to ensure that debug output is not overwritten.

## Producing debug kernel messages
#Printing more kernel messages indicates how to print of the kernel log buffer to the console, but that buffer itself won't contain any messages it didn't already (aside from the debug systemd output). This heading discusses methods for getting more detailed information out of the kernel log.

## Dynamic debugging
Messages printed with pr_debug or related functions such as , , and  will not be produced unless you either:

* Modify the kernel source to define  where desired.
* Utilize the kernel's dynamic debug feature to enable debugging messages.

This section will discuss how to use dynamic debug, which is useful if you have already looked at your kernel log with everything up to informational logs, and would like even more debugging information from a particular location.

Firstly, you must be running a kernel that was compiled with the  kernel configuration option set. This is already the case for , so no action is required if you are using that kernel.

Then, you need to know where you want to see debug messages from. A couple of options are:
* Going with the kernel module name, if the issue seems to be isolated to a module. For example, to troubleshoot Intel graphics, you might concern yourself with the  DRM kernel module.
* Going with a directory in the kernel that corresponds with functionality you are interested in. You will want to check out (or navigate online) the kernel source code to understand the structure. As an example, to inspect debug messages for all DRM kernel modules, you could go with the path drivers/gpu/drm.

Using that "source" of messages, you have to come up with a dynamic debug query that indicates which debug messages to enable, of the format:

 match_type match_parameter flags

Where:
* match_type is the type of match to make. Corresponding to the two options given earlier, this could be  or .
* match_parameter is the module or file path to watch. In the latter case, using asterisks for wildcards is permissible.
* flags dictates what to do with the match. This could be  to start printing its messages, or  to undo that.

Some examples of queries are:

*  to print debug messages from the  kernel module.
*  to print debug messages from DRM drivers.
*  to print debug messages.

Finally, to actually enact the query, you can either:

* Do so during runtime, by running:

 # echo "query" > /sys/kernel/debug/dynamic_debug/control

:This assumes that debugfs is mounted at , which you can verify using . * Do so at boot, by adding the  kernel parameter

This is a greatly simplified overview of dynamic debug's capabilities; see [https://docs.kernel.org/admin-guide/dynamic-debug-howto.html#command-language-reference the documentation for further details.

## Subsystem-specific debugging
There are also a number of separate debug parameters for enabling debugging in specific subsystems e.g. , . Also,  can be useful to investigate boot freezes. (Look for calls that did not return.) Check the kernel parameter documentation for specific information.

## netconsole
netconsole is a kernel module that sends all kernel log messages (i.e. dmesg) over the network to another computer, without involving user space (e.g. syslogd). Name "netconsole" is a misnomer because it is not really a "console", more like a remote logging service.

It can be used either built-in or as a module. Built-in netconsole initializes immediately after NIC cards and will bring up the specified interface as soon as possible. The module is mainly used for capturing kernel panic output from a headless machine, or in other situations where the user space is no more functional.

Be aware that you need to set the kernel options  and  for netconsole to send out kernel messages.

## Recovery shells
Getting an interactive shell at some stage in the boot process can help you pinpoint exactly where and why something is failing. There are several kernel parameters for doing so, but they all launch a normal shell which you can  to let the kernel resume what it was doing:

*  launches a shell shortly after the root file system is remounted read/write
*  launches a shell even earlier, before most file systems are mounted
*  (as a last resort) changes the init program to a root shell.  and  both rely on systemd, but this should work even if systemd is broken.

Another option is systemd's debug-shell which adds a root shell on  (accessible with ). It can be enabled by either adding  to the kernel parameters, or by enabling .

## Debugging kernel modules
See Kernel modules#Obtaining information.

## Debugging hardware
* You can display extra debugging information about your hardware by following udev#Debug output.
* Ensure that Microcode updates are applied on your system.
* To test the RAM, see Stress testing#Memtest86+.
* To see if your system is overheating, use lm_sensors.
* To check your storage health, see S.M.A.R.T.

## Debugging freezes
Unfortunately, freezes are usually hard to debug and some of them take a lot of time to reproduce. There are some types of freezes which are easier to debug than others:

* Is sound still playing? If so, just the display may be frozen. This may be a problem with the video driver.
* Is the machine still responding? Try SSH if switching to another TTY does not work.
* Is the disk activity LED (if present) indicating that a lot is being written to disk? Heavy swapping may temporarily freeze the system. See this StackExchange answer for information about freezes on large writes.

If nothing else helps, try a clean shutdown. Pressing the power button once may unfreeze the system and show the classic "shutdown screen" which displays all the units that are getting stopped. Alternatively, using the magic SysRq keys may also help to achieve a clean shutdown. This is very important because the journal may contain hints why the machine froze. The journal may not be written to disk on an unclean shutdown. Hard freezes in which the whole machine is unresponsible are harder to debug since logs can not be written to disk in time.

Remote logging may help if the freeze does not permit writing anything to disk. A crude remote logging solution, which needs to be invoked from another device, can be used for basic debugging:

 $ ssh freezing_host journalctl -f

Many fatal freezes in which the whole system does not respond anymore and require a forced shutdown may be related to buggy firmware, drivers or hardware. Trying a different kernel (see Kernel#Debugging regressions) or even a different Linux distribution or operating system, updating the firmware and running hardware diagnostics may help finding the problem.

If a freeze does not permit gathering any kind of logs or other information required for debugging, try reproducing the freeze in a live environment. If a graphical environment is required to reproduce the freeze or if the freeze can be reproduced on the archiso, use the live environment of a different distribution, which is preferably not based on Arch Linux to eliminate the possibility that the freeze is related to the version or patches of the kernel.
Should the freeze still happen in a live environment, chances are that it may be hardware-related. If it does not happen anymore, it is necessary to be aware of the differences of both systems. Different configurations, differences in versions and kernel parameters and other, similar changes may have fixed the freeze.

However, a blinking caps lock LED may indicate a kernel panic. Some setups may not show the TTY when a kernel panic occurred, which may be confusing and can be interpreted as another kind of freeze.

## Debugging regressions
If an update causes an issue but downgrading the specific package fixes it, it is likely a regression. If this happened after a normal full system upgrade, check your  to determine which package(s) may have caused the issue. The most important part of debugging regressions is checking if the issue was already fixed, as this can save much time. To do so, first ensure the application is fully updated (e.g. ensure the application is the same version as in the official repositories). If it already is or if updating it does not fix the issue, try using the development version, usually a VCS version, which may already be packaged in the AUR. If this fixes the issue and the version with the fixes is not yet in the official repositories, wait until the new version arrives in them and then switch back to it.

If the issue still persists, debug the issue and/or bisect the application and report the bug on the upstream bug tracker so it can be fixed.

## Cannot use some peripherals after kernel upgrade
This will manifest commonly (but probably not only) as:

* newly plugged USB devices showing up with dmesg but not in ,
* file systems unable to be mounted if they were not already used before the kernel update,
* the inability to use a wired/wireless connection on a laptop if it was not already used before the kernel update,
*  when using modprobe to load a module that was not already used before the kernel package update.

As partially covered in System maintenance#Restart or reboot after upgrades, the kernel is not updated when you update the package but only once you reboot afterwards. Meanwhile, the kernel modules, located in  are removed by pacman when installing the new kernel. As explained in , this approach avoids leaving files on the system not handled by the package manager but leads to the aforementioned symptoms. To fix them, reboot systematically after updating the kernel. The long-term evolution, yet to be implemented, will be to use versioned kernel packages : the main blocker being how to handle the removal of the previous kernel versions once they are not needed anymore.

Another solution is available as , where two pacman hooks use rsync to keep the kernel modules on the file system after the kernel update and  that marks the old modules for removal four weeks after once enabled.

## Package management
See Pacman#Troubleshooting for general topics, and pacman/Package signing#Troubleshooting for issues with PGP keys.

## Fixing a broken system
If a partial upgrade was performed, try updating your whole system. A reboot may be required.

 # pacman -Syu

If you usually boot into a GUI and that is failing, perhaps you can press  through  and get to a working tty to run pacman through.

If the system is broken enough that you are unable to run pacman, boot using a monthly Arch ISO from a USB flash drive, an optical disc or a network with PXE.  (Do not follow any of the rest of the installation guide.)

Mount your root file system:

 # mount /dev/rootFileSystemDevice /mnt

Mount any other partitions that you created separately, adding the prefix  to all of them, i.e.:

 # mount /dev/bootDevice /mnt/boot

Try using your system's pacman while chrooted:

 # arch-chroot /mnt
 # pacman -Syu

If that fails, exit the chroot, and try:

 # pacman -Syu --sysroot /mnt

If that fails, try:

 # pacman -Syu --root /mnt --cachedir /mnt/var/cache/pacman/pkg

## fuser
fuser is a command-line utility for identifying processes using resources such as files, file systems and TCP/UDP ports.

fuser is provided by the  package, which should be already installed as a dependency of the  meta package. See  for details.

## Session permissions
First, make sure you have a valid local session within X:

 $ loginctl show-session $XDG_SESSION_ID

This should contain  and  in the output. If it does not, make sure that X runs on the same tty where the login occurred. This is required in order to preserve the logind session.

Basic polkit actions do not require further set-up. Some polkit actions require further authentication, even with a local session. A polkit authentication agent needs to be running for this to work. See polkit#Authentication agents for more information on this.

## Message: "error while loading shared libraries"
If, while using a program, you get an error similar to:

 error while loading shared libraries: libusb-0.1.so.4: cannot open shared object file: No such file or directory

Use pacman or pkgfile to search for the package that owns the missing library:

In this case, the  package needs to be installed. Alternatively, the program requesting the library may need to be rebuilt following a soname bump.

The error could also mean that the package that you used to install your program does not list the library as a dependency in its PKGBUILD: if it is an official package, report a bug; if it is an AUR package, report it to the maintainer using its page in the AUR website.
