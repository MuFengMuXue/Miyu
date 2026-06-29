# Kdump

Kdump is a standard Linux mechanism to dump machine memory content on kernel crash. Kdump is based on Kexec. Kdump utilizes two kernels: the regular system kernel and kdump capture kernel (called from now on, the kdump kernel). System kernel is the normal kernel, booted with the  parameter - we need to tell the system kernel to reserve some amount of physical memory where the kdump kernel will be loaded/executed. Then it is necessary to load the kdump kernel in advance, because when the system kernel crashes, there is no reliable way to read data from disk, for example, given that such kernel is broken.

Once a kernel crash happens, the system kernel crash handler uses the Kexec mechanism to boot the kdump kernel in its pre-reserved memory. The memory from system kernel is preserved in such kexec boot, and it is accessible from the kdump kernel at the moment of crash. Once the kdump kernel is booted, the user can collect the file  to get access to memory of the crashed system kernel. Such crash dump can be saved to disk or copied over network to some other machine for further post-mortem investigation.

In server production environments, the system and kdump kernels could be different - system kernel needs a lot of features and is compiled with a many kernel flags/drivers, while the kdump kernel goal is to be minimalistic and take as small amount of memory as possible, e.g. it could be compiled without network support if we store the crash dump to disk only. But for desktops and in general, for non-specific setups, the same kernel is used both as system and kdump kernels. It means we will load the same kernel code twice - one time as normal system kernel, another one to the reserved memory area, but with different kernel parameters.

## Alternatives to setup kdump
## The automatic way: kdumpst
The  tool is an automatic way for loading kdump. It is highly customizable - it defaults to another method of log collecting (called pstore), but can be easily set to use kdump (a matter of setting  on . The tool also fallbacks to kdump in case pstore RAM region is not available.

After installing kdumpst, one can check the journal and the following message means kdump is loaded: . If a kernel crash happens, the kdump will be collected and in the subsequent boot, a message indicates the success of the operation: . In that folder, the user will find a lightweight zip blob, that included a dmesg plus some extra data. The vmcore itself is saved on . For questions/issues, the #kdump IRC channel at OFTC could be used, or open issues in the kdumpst repository.

## The automatic way: simple-kdump
The  tool provides a simple and easy-to-config way to setup and collect kdump.
Unlike , it is boot loader independent, has one and only one objective, save the vmcore file
to .

It is mostly all the manual setups mentioned in later sections with slightly better organization using systemd, but re-use the Arch Linux kernels (or whatever kernel the end user choose), so it is super flex and simple.

After installing , fill  using any booting kernel/initramfs combination, which has the  enabled.
It is recommended to use the Arch Linux linux or linux-lts kernel, which already have all the needed features enabled.

Then add  kernel parameter and reboot. Recommended to use value no smaller than 512M

Finally enable and start , then refer to #Testing kdump by crashing the kernel to verify the kdump behavior.

The kexec kernel should reach target , with a prompt asking login for the emergency shell. You can ignore that login as the vmcore collection will happen at the background and reboot automatically.

After the reboot, there should be a new crash dump at .

## Manual steps
In case the preference is for doing that manually, the below guide will help with that.

## Compiling kernel
Both System/kdump kernels requires some configuration flags that may not be set by default. Please consult Kernel Compilation article for more information about compiling a custom kernel in Arch. Here we will emphasize on Kdump specific configurations. Current default Arch kernel builds have these flags already set.  You can verify if your running kernel has these set by looking in .

Please note that, the default  and  kernels all have the needed options enabled.
But unfortunately the default kernels have debug info striped, thus one still needs to recompile the kernel to have all the debug info so that the vmcore can be properly analyzed.

To create a kernel you need to edit the kernel  file and enable following configuration options:

The last two are for the extra debuginfo so that tools like  or  can analyze the vmcore.
(Or is there a way to use debuginfod to download the kernel debuginfo?)

Also change package base name to something like linux-kdump to distinguish the kernel from the default Arch one. Compile kernel package and install it. Save ./src/linux-X.Y/vmlinux uncompressed system kernel binary - it contains debug symbols and you will need them later when analyzing the crash.

For reference, some details about building a kdump kernel or configuring the kernel parameters for kdump could be found in the kernel Kdump documentation.

## Reuse existing kernel and initramfs
The simplest way to setup kdump is to use the existing kernel and initramfs.
The example here will use  kernel as an example,
which generates its initramfs at .

The core idea is to boot the kexec environment just as a regular Arch Linux boot sequence.
But with extra systemd options to slightly change the boot sequence (to skip re-setup kexec environment, collect vmcore, and reboot).

Thus we do not need to generate a special initramfs, unlike other distros (and our default initramfs generated by mkinitcpio is already way smaller than our competitors).

## Setup the kdump kernel
First, you need to reserve memory in the system kernel, for the kdump kernel loading. Edit your boot loader configuration and add  kernel parameter.

Depending on the machine and how the kdump kernel was built, something from 256M to 512M is usually enough - it worth trying after setting everything to check if it succeeds. Note that the reserved memory is unavailable to the system kernel.

Reboot into your system kernel.  To make sure that the kernel is booted with correct options please check the files  and  to see if the memory was indeed pre-reserved (sometimes it is possible, though rare, that such memory reservation fails - if it happens, check the  to get more information).

Next you need to tell Kexec that you want to use your kdump kernel. Specify your kernel, initramfs file, root device and other parameters if needed: (here we use default  kernel)

 # kexec -p /boot/vmlinuz-linux --initrd=/boot/initramfs-linux.img] --append="root=irqpoll nr_cpus=1 reset_devices"

It loads the kdump kernel into the reserved area. Without the  flag kexec would boot the kernel right away, but in presence of such flag, the kdump kernel will be loaded into the reserved memory but its boot is postponed until a crash happens.

Instead of running kexec manually you might want to setup Systemd service that will run kexec on boot:

Then enable .

Note, since the service is enabled, and our kexec environment boots exactly like a regular boot,
it will try to start  but fail since there is not enough memory.
Thus in the  option,  is specified to avoid the kdump service itself.

To check whether the crash kernel is already loaded please run following command:
 $ cat /sys/kernel/kexec_crash_loaded

## Testing kdump by crashing the kernel
If you want to test crash then you can use sysrq for this.
 # sync; echo 1 > /proc/sys/kernel/sysrq; echo c > /proc/sysrq-trigger

Once crash happens kexec will load your kdump kernel, which should look exactly like a regular boot, but with much smaller memory (the reserved size) and only one CPU core.

## Saving the crashed kernel memory
Once booted into the kdump kernel, the idea is to save the relevant contents from  to analyze it later. Though this is exposed as a file (hence it is possible to copy it, like in , this is not the recommended way. The vmcore is a full copy of system memory, so this file will have 64G if your machine has 64G, for example. It includes all data from all the userpace loaded, as well as free memory. So, the best way for saving it is use the  utility. Such application is able to remove free memory and userspace irrelevant data, as well as compress the vmcore! Example of the usage:

 # makedumpfile -z -d 31 /proc/vmcore /root/vmcore.crashdump_compressed

You can also save out the dmesg log from the crashed kernel using this command:

 # makedumpfile --dump-dmesg /proc/vmcore /root/vmcore.dmesg

The following systemd service can be used to automatically save the crash dumps and reboot into the system kernel again:

This can be invoked from the kdump kernel command line - for that, we should edit the kdump load service as below:

## Early kdump using mkinitcpio
You might encounter a situation where the kernel crashes before the systemd service can be started.  In this case, it might be helpful to run kexec as a mkinitcpio hook rather than a service.

First make a copy of your initramfs.  This will be used to run the crash kernel.

 # cp /boot/initramfs-linux.img /boot/initramfs-linux-crash.img

Next, create the mkinitcpio install file.  This builds allows us to build the main initramfs with a copy of the crash initramfs for the crash kernel and the
{{hc|/etc/initcpio/install/kdump|
build() {
        add_binary kexec
        add_file /boot/initramfs-linux-crash.img /crash/initramfs.img
        add_file /boot/vmlinuz-linux /crash/vmlinuz
        add_runscript
}

help() {
        cat <<HELPEOF
Installs the crash kernel on boot
HELPEOF
}
}}

Next, make the mkinitcpio hook file.  This runs kexec as an earlyhook, hopefully before anything in the kernel can crash.  An important note here is that we run the kernel in emergency mode, because running the kernel in rescue or normal might might just lead to another the same crash happening in the crash kernel.

{{hc|/etc/initcpio/hook/kdump|
run_earlyhook() {
	msg 'Loading crash kernel..'
	if [ -e /crash/vmlinuz ; then
		if [ -e /crash/initramfs.img ]; then
			kexec -p /crash/vmlinuz --initrd=/crash/initramfs.img --append="root=irqpoll nr_cpus=1 reset_devices emergency"
		else
			msg 'No initramfs found'
		fi
	else
		msg 'No vmlinuz found'
	fi
}
}}

Now run mkinitcpio with the new hook

 # mkinitcpio -A kdump

When the crash happens, you will be loaded into emergency kernel mode.  After entering your password, you will be at a terminal.  The first thing you will need to do is make your root filesystem writable.

 $ mount -o remount, rw /

Now you can save the dump using makedumpfile (see #Saving the crashed kernel memory)

## Analyzing the kernel core dump
The best way for studying the saved kernel core dump involves tools aimed specifically at that. The most common alternative is the gdb-based . Run crash as in
 $ crash vmlinux path/crash.dump
Where the vmlinux should contain debug symbols included in order to extract more information from the saved crash dump.

Follow man crash or [https://crash-utility.github.io/crash_whitepaper.html for more information about debugging practices.

Another recent alternative is , a python-based and fully scriptable tool to extract information from the vmcore.
