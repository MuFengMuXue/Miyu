# Kernel

According to Wikipedia:
:The Linux kernel is an open-source monolithic Unix-like computer operating system kernel.

Arch Linux is based on the Linux kernel. There are various alternative Linux kernels available for Arch Linux in addition to the latest stable kernel. This article lists some of the options available in the repositories with a brief description of each. There is also a description of patches that can be applied to the system's kernel. The article ends with an overview of custom kernel compilation with links to various methods.

Kernel packages are installed under the  path and subsequently used to copy the vmlinuz executable image to . When installing a different kernel or switching between multiple kernels, you must configure your boot loader to reflect the changes. For downgrading the kernel to an older version, see Downgrading packages#Downgrading the kernel.

## Officially supported kernels
Community support on [https://bbs.archlinux.org/viewforum.php?id=22 forum and bug reporting is available for officially supported kernels.

*
*
*
*
*

## Compilation
Following methods can be used to compile your own kernel:

; /Arch Build System: Takes advantage of the high quality of existing  PKGBUILD and the benefits of package management.
; /Traditional compilation: Involves manually downloading a source tarball, and compiling in your home directory as a normal user.

Some of the listed packages may also be available as binary packages via Unofficial user repositories.

## kernel.org kernels
*
*
*
*
*

## Unofficial kernels
*
*
*
*
:* Repository,  by pf-kernel developer post-factum
*
*
*
* .
*
*

Many of these unofficial kernels contain features that need to be enabled manually. Try reading the documentation in the patches themselves (many already include changes to the  directory in the kernel source) or searching up the name of the patchset on the web.

## Troubleshooting
## Kernel panics
A kernel panic occurs when the Linux kernel enters an unrecoverable failure state. The state typically originates from buggy hardware drivers resulting in the machine being deadlocked, non-responsive, and requiring a reboot. Just prior to deadlock, a diagnostic message is generated, consisting of: the machine state when the failure occurred, a call trace leading to the kernel function that recognized the failure, and a listing of currently loaded modules. Thankfully, kernel panics do not happen very often using mainline versions of the kernel--such as those supplied by the official repositories--but when they do happen, you need to know how to deal with them.

## Examine panic message
If a kernel panic occurs very early in the boot process, you may see a message on the console containing , but once systemd is running, kernel messages will typically be captured and written to the system log. However, when a panic occurs, the diagnostic message output by the kernel is almost never written to the log file on disk because the machine deadlocks before  gets the chance.

## QR code on a blue screen
Since  6.10 (for ), the kernel will display a panic as a QR code (by default) in a blue screen. The stack trace is visible at the URL given by the QR code. For Arch Linux, it is a link to https://panic.archlinux.org/panic_report. The URL contains various information and the stack trace compressed by gzip and encoded in the URL fragment which is not transferred to the server (it is processed on the client side).

An example panic with a link and screenshot can be seen in a forum post.

You can revert to the old behavior by passing the parameter  to the  kernel module (or  as kernel parameter) to display the stack trace in a console.

## Console way
The "old" style way of viewing the crash on the console as it happens is still available (without resorting to setting up a kdump crashkernel). Boot with the following kernel parameters and attempting to reproduce the panic on tty1:

 systemd.journald.forward_to_console=1 console=tty1

## Example scenario: bad module
It is possible to make a best guess as to what subsystem or module is causing the panic using the information in the diagnostic message. In this scenario, we have a panic on some imaginary machine during boot. Pay attention to the lines highlighted in bold:

# Indicates the type of error that caused the panic. In this case it was a programmer bug.
# Indicates that the panic happened in a function called fw_core_init in module firewire_core.
# Indicates that firewire_core was the latest module to be loaded.
# Indicates that the function that called function fw_core_init was do_one_initcall.
# Indicates that this oops message is, in fact, a kernel panic and the system is now deadlocked.

We can surmise then, that the panic occurred during the initialization routine of module firewire_core as it was loaded.  (We might assume then, that the machine's firewire hardware is incompatible with this version of the firewire driver module due to a programmer error, and will have to wait for a new release.) In the meantime, the easiest way to get the machine running again is to prevent the module from being loaded.  We can do this in one of two ways:

* If the module is being loaded during the execution of the initramfs, reboot with the kernel parameter .
* Otherwise reboot with the kernel parameter .

## Reboot into root shell and fix problem
You will need a root shell to make changes to the system so the panic no longer occurs. If the panic occurs on boot, there are several strategies to obtain a root shell before the machine deadlocks:

* Reboot with the kernel parameter , , or  to receive a prompt to login just after the root filesystem is mounted and  is started.

:

* Reboot with the kernel parameter , , , , , or  to receive a prompt to login just after local filesystems are mounted.
* Reboot with the kernel parameter  to obtain a very early root shell on tty9.  Switch to it with by pressing .
* Experiment by rebooting with different sets of kernel parameters to possibly disable the kernel feature that is causing the panic.  Try the "old standbys"  and .

:

* As a last resort, boot with an Arch Linux installation medium and mount the root filesystem on  then execute  as the root user.
* Disable the service or program that is causing the panic, roll-back a faulty update, or fix a configuration problem.

## Debugging regressions
See General troubleshooting#Debugging regressions.

Try  to check if the issue is already fixed upstream. The pinned comment also mentions a repository which contains already built kernels, so it may not be necessary to build it manually, which can take some time.

It may also be worth considering trying the LTS kernel () to debug issues which did not appear recently. Older versions of the LTS kernel can be found in the Arch Linux Archive.

If the issue still persists, bisect the  kernel to identify the source of the problem.

Report the bug in accordance to the kernel process for reporting regressions. Note that it is not necessary to do a full bisection down to a single commit, it is acceptable to report a range, but the more precise you can be the better your bug report will be handled.   Depending on the Bugtracker () entry in the  file this then entails opening an issue via the subsystems mailing lists, Kernel Bugzilla, or in other issue trackers like the DRM Gitlab. It is important to try the "vanilla" version without any patches to make sure it is not related to them. If a patch causes the issue, report it to the author of the patch.

## stable/linux
Note that, by default, linux-git builds from Linus' repo but the Arch official kernel builds from the stable kernel repo. They do not share the same tags -- e.g. Linus has v5.17 but not v5.17.7. If you know which kernel upgrade introduced the bug for you it might be easier to bisect over the stable repo because its tags match the version numbers of the  package.

You can do this by creating:

before following the bisection instructions on the . This will point the downloaded  but point it at  at the version you choose, from which you can start your bisection.

If you successfully identify a bug in stable, make sure to report it as such.

## Building a smaller kernel
You can shorten kernel build times by building only the modules required by the local system using modprobed-db, or by . Of course you can completely drop irrelevant drivers, for example sound drivers to debug a network problem.
