# Power management/Suspend and hibernate

There are multiple methods of suspending available, notably:

; Suspend to idle: Called S0ix by Intel, Modern Standby (previously "Connected Standby") by Microsoft and S2Idle by the kernel. Designed to be used instead of the S3 sleeping state for supported systems, by providing identical energy savings but a drastically reduced wake-up time.
; Suspend to RAM (aka suspend): The S3 sleeping state as defined by ACPI. Works by cutting off power to most parts of the machine aside from the RAM, which is required to restore the machine's state. Because of the large power savings, it is advisable for laptops to automatically enter this mode when the computer is running on batteries and the lid is closed (or the user is inactive for some time).
; Suspend to disk (aka hibernate): The S4 sleeping state as defined by ACPI. Saves the machine's state into swap space and completely powers off the machine. When the machine is powered on, the state is restored. Until then, there is zero power consumption.
; Hybrid suspend (aka hybrid sleep): A hybrid of suspending and hibernating, sometimes called suspend to both. Saves the machine's state into swap space, but does not power off the machine. Instead, it invokes the default suspend. Therefore, if the battery is not depleted, the system can resume instantly. If the battery is depleted, the system can be resumed from disk, which is much slower than resuming from RAM, but the machine's state has not been lost.

The kernel provides basic functionality, and some high level interfaces provide tweaks to handle problematic hardware drivers/kernel modules (e.g. video card re-initialization).

## Kernel interface (swsusp)
It is possible to directly inform the in-kernel software suspend code (swsusp) to enter a suspended state; the exact method and state depends on the level of hardware support. On modern kernels, writing appropriate strings to  is the primary mechanism to trigger this suspend.

See kernel documentation for details.

## High level interface (systemd)
systemd provides native commands for suspend, hibernate and a hybrid suspend. This is the default interface used in Arch Linux.

 should work out of the box. For  to work on your system you might need to follow the instructions at #Hibernation.

There are also two modes combining suspend and hibernate:

*  suspends the system both to RAM and disk, so a complete power loss does not result in lost data. This mode is also called suspend to both.
*  initially suspends the system to RAM as long as possible, then wakes it with an RTC alarm and hibernates. The RTC alarm is set with  in . The default value is set by estimating the battery discharge rate to keep the system with 5% of battery, or two hours without one. Said estimation is obtained from the change in battery level after the time specified by  in , at which the system will briefly wake up to do the measurement (a measure is also made if the system is manually woken up from suspension).

See #Sleep hooks for additional information on configuring suspend/hibernate hooks. Also see , , and .

## Changing suspend method
On systems where S0ix suspension does not provide the same energy savings as the regular S3 sleep, or when conserving energy is preferred to a quick resume time, changing the default suspend method is possible.

Run the following command to see all suspend methods hardware advertises support for (current method is shown in square brackets{| class="wikitable sortable"
|+ Supported sleep states in mem_sleep
|-
! mem_sleep string !! Sleep State
|-
| s2idle || [https://docs.kernel.org/admin-guide/pm/sleep-states.html#suspend-to-idle suspend-to-idle
|-
| shallow || standby
|-
| deep || suspend-to-RAM
|}

If your hardware does not advertise the  sleep status, check first if your UEFI advertises some settings for it, generally under Power or Sleep state or similar wording, with options named Windows 10, Windows and Linux or S3/Modern standby support for S0ix, and Legacy, Linux, Linux S3 or S3 enabled for S3 sleep. Failing that, you can keep using , consider using hibernation or try to patch the DSDT tables (or find a patched version online).

Confirm that your hardware does not exhibit issues with S3 sleep by testing a few sleep cycles after changing the sleep method:

 # echo deep > /sys/power/mem_sleep

If no issues have been found, you can make the change permanent through the  directive in :

or through the  kernel parameter.

In some opposite situations, faulty firmware advertises support for  sleep, while only  is supported. In this case, an alternative method for using  is available through the  setting:

## Hibernation
In order to use hibernation, you must create a swap partition or file, configure the initramfs so that the resume process will be initiated in early userspace, and specify the location of the swap space in a way that is available to the initramfs, e.g.  EFI variable defined by systemd or  kernel parameter. These three steps are described in detail below.

## About swap partition/file size
Even if your swap partition is smaller than RAM, you still have a good chance of hibernating successfully. See "image_size" in the kernel documentation for information on the   pseudo-file.

You may either decrease the value of  to make the suspend image as small as possible (for small swap partitions), or increase it to possibly speed up the hibernation process. For systems with a large amount of RAM, smaller values may drastically increase the speed of resuming a hibernating system. systemd#systemd-tmpfiles - temporary files can be used to make this change persistent:

The suspend image cannot span multiple swap partitions and/or swap files. It must fully fit in one swap partition or one swap file.=== Configure the initramfs ===

* When the default systemd-based initramfs (using the  hook) is used, a resume mechanism is already provided and no further hooks are required.
* When using a busybox-based initramfs, the  hook is required in . Whether by label or by UUID, the swap partition is referred to with a udev device node, so the  hook must follow the  hook. For example:

:

:Regenerate the initramfs for these changes to take effect.

:

## Pass hibernate location to initramfs
When the system hibernates, the memory image is dumped to the swap space, which also includes the state of mounted file systems. Therefore, the hibernate location must be made available to the initramfs, i.e. before the root file system is mounted for resuming from hibernate to work.

When the system is running on UEFI,  will automatically pick a suitable swap space to hibernate into, and the information of the used swap space is stored in  EFI variable. Upon next boot,  reads the location off the EFI variable and the system resumes. This means the following steps are not necessary unless the system is using legacy BIOS or you want to choose a different swap space from the automatically-selected one.

## Manually specify hibernate location
The kernel parameter  can be used, where swap_device follows the persistent block device naming. For example:

*
*
*  – if swap is on a LVM logical volume (UUID and Label should also work)

The kernel parameters will only take effect after rebooting. To hibernate right away, obtain the volume's major and minor device numbers from lsblk and echo them in format  to .

For example, if the swap device is :

 # echo 8:3 > /sys/power/resume

If using a swap file, additionally follow the procedures in #Acquire swap file offset.

## Acquire swap file offset
When using a swap file for hibernation, the block device on which the file system lies should be specified in , and additionally the physical offset of swap file must be specified through  kernel parameter. [https://docs.kernel.org/power/swsusp-and-swap-files.html

On file systems other than Btrfs, the value of  can be obtained by running . The output is in a table format and the required value is in the first row of the  column.

For example:

In the example the value of  is the first .

Alternatively, to directly acquire the offset value:

 # filefrag -v swap_file | awk '$1=="0:" {print substr($4, 1, length($4)-2)}'

For Btrfs, do not try to use the filefrag tool, since the "physical" offset you get from filefrag is not the real physical offset on disk; there is a virtual disk address space in order to support multiple devices.Instead, use the  command. E.g.:

In this example, the kernel parameter would be .

To apply the change immediately (without rebooting), echo the resume offset to . For example, if the offset is :

 # echo 38912 > /sys/power/resume_offset

## Change the image compression algorithm for hibernation
The default compression algorithm is selected based on the compile time option , but it can be overridden at boot time and runtime.

Different compression algorithms have different characteristics and hibernation may benefit when it uses any of these algorithms, especially when a secondary algorithm (LZ4) offers better decompression speeds over a default algorithm (LZO), which in turn reduces hibernation image restore time.

You can override the default algorithm in two ways:

1) Passing  as a kernel parameter:

 hibernate.compressor=lzo
 hibernate.compressor=lz4

2) Specifying the algorithm at runtime:

 # echo lzo > /sys/module/hibernate/parameters/compressor
 # echo lz4 > /sys/module/hibernate/parameters/compressor

Currently  and  are the supported algorithms with LZO being the default.

## Maintaining swap file for hibernation with zram
It is possible to solve the hibernation problem with zram RAM-only swap by maintaining two or more swap spaces at the same time. systemd will always ignore zram block devices before triggering hibernation [https://github.com/systemd/systemd/issues/16708#issuecomment-1632592375, therefore keeping both spaces enabled should work without further intervention.

After configuring the swap file, follow the zram page. Make sure zram has the higher swap priority (e.g. ).

## Hibernation into a thinly-provisioned LVM volume
Hibernation into a thinly-provisioned LVM volume is possible, but you have to make sure that the volume is fully allocated. Otherwise resuming from it will fail, see .

You can fully allocate the LVM volume by simply filling it with zeros. E.g.:

 # dd if=/dev/zero of=/dev/vg0/swap bs=1M status=progress

To verify the volume is fully allocated, you can use:

A fully allocated volume will show up as having 100% data usage.

## Disable zswap writeback to use the swap space only for hibernation
zswap has a per-cgroup option to disable writeback. Since there is no global option to disable zswap writeback, you need to use the systemd unit setting  (see ) in all possible unit types. This allows to use zswap just like zram with the added benefit of supporting hibernation.

To avoid having to manually create twelve top level per-type drop-in files (for system and user , , , , ,  units types), install . Enable zswap and reboot for the settings to take effect.

Try to perform memory intensive tasks and confirm that zswap has not written anything to disk:

## Sleep hooks
## Custom systemd units
systemd starts , , , or  for each sleep state, respectively. All the aforementioned targets pull in . Any of the targets can be used to invoke custom units before or after suspend/hibernate. Separate files should be created for user actions and root/system actions. Examples:

Enable  and/or  for the change to take effect.

For root/system actions:

## Combined sleep/resume unit
With the combined unit file, a single hook does all the work for different phases (sleep/resume) and for different targets.

Example and explanation:

* : After started, the service is considered active until it is explicitly stopped.
* : When active, the service will be stopped if no other active service requires it. In this specific example, it will be stopped after  is stopped.
* Because  has , the hook is guaranteed to start/stop properly for different tasks.

## Hooks in /usr/lib/systemd/system-sleep
systemd-sleep runs all executables in , passing two arguments to each of them:

# Either  or , depending on whether the machine is going to sleep or waking up.
# , ,  or , depending on which is being invoked.

An environment variable called  will be set and contain the sleep action that is processing. This is primarily helpful for suspend-then-hibernate where the value of the variable will be , , or  in cases where hibernation has failed.

The output of any custom script will be logged by systemd-suspend.service, systemd-hibernate.service or systemd-hybrid-sleep.service. You can see its output in systemds journalctl:

 # journalctl -b -u systemd-suspend.service

An example of a custom sleep script:

Do not forget to make your script executable.

## Tips and tricks
## Unlocking automatically on resume in trusted locations
When resuming, you can automatically unlock your system if it is connected to certain devices or trusted Wi-Fi networks.

{{hc|/etc/local-scripts/resume-unlock.sh|2=
#!/usr/bin/bash
# Unlock session if at a trusted location

function trusted() {
    # Check if connected to a trusted Wi-Fi network
     $(iwgetid -r) == your_home_ssid  \
        && return 0

    # Check if trusted USB device is connected.
    #lsusb -d xxxx:xxxx && return 0

    return 1 # Not trusted
}

for (( i=0; i Beware that this can cause the system to attempt to hibernate and fail.

## Specified resume device is missing or is not an active swap device
This occurs when systemd-logind cannot find the hibernation target specified in  and .(It does so in case those were filled in manually beforehand, but they are also automatically filled in as part of the hibernation resuming process.)

If you have intentionally specified those manually, make sure that the target partition and/or swap file is accessible (mounted and/or enabled).

Otherwise, write  to  and  to  to clear them, and try again. (Rebooting also clears those, unless the  and/or  kernel parameters are used.)

## System wakes up immediately after hibernating
Beyond the issues described in Wakeup triggers#Instantaneous wakeup after suspending, it is possible for hibernation to appear to succeed, only to end immediately. Check if the journal contains a  line emitted by systemd-sleep: they mean that not enough free swap space was available.

Look nearby for kernel logs like these:

Note that the kernel needs to perform its allocation in a single swap space; thus, if  shows that free space is distributed across several swaps, consider briefly disabling one swap to consolidate their usage, and trying again.

Tweaking swap priority can help keep one swap device mostly empty for hibernation.

## Wake-on-LAN
If Wake-on-LAN is active, the network interface card will consume power even if the computer is hibernated.

## System does not power off when hibernating
When you hibernate your system, the system should power off (after saving the state on the disk). On some firmware the S4 sleeping state does not work reliably. For example, instead of powering off, the system might reboot or stay on but unresponsive. If that happens, it might be instructive to set the  to  in :

With the above configuration, if everything else is set up correctly, on invocation of a  the machine will shut down, saving state to disk as it does so.

## Operating system not found (or wrong OS booting) when booting after hibernation
This can happen when the boot disk is an external disk, and seems to be caused by a BIOS/firmware limitation. The BIOS/firmware tries to boot from an internal disk, while hibernation was done from an OS on an external (or other) disk.

Set  as shown in #System does not power off when hibernating to solve the problem permanently. If you have already locked yourself out, you can try rebooting your system 4 times (wait for the error to appear each time), which on some BIOS'es forces a normal boot procedure.

## Hibernation and multi boot systems
If you are running a multi boot system (including but not limited to dual boot with Windows) and want to be able to boot into your other system while your main Arch Linux is hibernated, you must take extra caution not to mount filesystems that are still in use by the hibernated system. Before attempting to mount such filesystem within another system, you must make sure to unmount this filesystem before hibernating the system. This can be achieved with sleep hooks.

This issue is particularly relevant for the EFI system partition, because the ESP is expected to be shared across multiple systems. Check the matching section in EFI system partition for mitigation strategies, which can be adapted to other filesystems as well.

## Hardware watchdog
A problem may arise when using the hardware watchdog timer (disabled by default, see  in ). A buggy watchdog timer may reset the computer before the system finishes creating the hibernation image.

## Black/blank screen on resuming
Sometimes the screen goes black due to device initialization from within the initramfs. Removing any modules you might have in Mkinitcpio#MODULES, removing the  hook, and then regenerating the initramfs can possibly solve this issue, in particular with graphics drivers for early KMS. Initializing such devices before resuming can cause inconsistencies that prevents the system resuming from hibernation. This does not affect resuming from RAM.

Moving from the ATI video driver to the newer AMDGPU driver could also help to make the hibernation and awakening process successful.

## Blank/black screen after suspend/hibernate
Suspending and hibernation are delicate tasks, requiring system and device state to be preserved while they are powered off. Bugs can be introduced by updates, especially of the kernel; if breakage occurs after an upgrade, consider downgrading the kernel or switching to , and seeing if that fixes the issue.

With NVIDIA cards, the VRAM contents are saved to disk when suspending.[https://us.download.nvidia.com/XFree86/Linux-x86_64/470.63.01/README/powermanagement.html Make sure that you have enough disk space, otherwise you might get a blank screen when resuming. Another cause for this could be fixed by blacklisting the module . === Touchpad causes a kernel panic on resume ===

Laptops with an Intel CPU that load the  kernel module for a touchpad may face kernel panic on resume (blinking caps lock) [https://bbs.archlinux.org/viewtopic.php?id=231881. The module needs to be added to the initramfs, e.g.:

Then regenerate the initramfs.

## PC will not wake from sleep on A520I and B550I motherboards
On some motherboards with A520i and B550i chipsets, the system will not completely enter the sleep state or come out of it. Symptoms include the system entering sleep and the monitor turning off while internal LEDs on the motherboard or the power LED stay on. Subsequently, the system will not come back from this state and require a hard power off. If you have similar issues with AMD, first make sure your system is fully updated and check whether the AMD microcode package is installed.

Verify the line starting with  has the enabled status:

If that is enabled, you can run the following command to disable it:

 # echo GPP0 > /proc/acpi/wakeup

Now test by running  and let the system go to sleep. Then try to wake the system after a few seconds. If it works, you can make the workaround permanent. Create a systemd unit file:

Do a daemon-reload and start/enable the newly created unit.

Alternatively, you can create a udev rule. Assuming ’s sysfs node is  like in the example, run  to get the relevant information and create a udev rule like this one:

{{hc|/etc/udev/rules.d/10-gpp0-acpi-fix.rules|2=
KERNEL=="0000:00:01.1", SUBSYSTEM=="pci", DRIVERS=="pcieport", ATTR{vendor}=="0x1022", ATTR{device}=="0x1483", ATTR{power/wakeup}="disabled"
}}

The udev daemon is already watching for changes in your system by default. If needed you can reload the rules manually.

## Suspend from corresponding laptop Fn key not working
If, regardless of the setting in logind.conf, the sleep button does not work (pressing it does not even produce a message in syslog), then logind is probably not watching the keyboard device. Do:

 # journalctl --grep="Watching system buttons"

You might see something like this:

 May 25 21:28:19 vmarch.lan systemd-logind[210: Watching system buttons on /dev/input/event2 (Power Button)
 May 25 21:28:19 vmarch.lan systemd-logindWatching system buttons on /dev/input/event3 (Sleep Button)
 May 25 21:28:19 vmarch.lan systemd-logind[210: Watching system buttons on /dev/input/event4 (Video Bus)

Notice no keyboard device. List keyboard devices as follows:

Now obtain {{ic|ATTRS{name}}} for the parent keyboard device As an example, on the above list this keyboard device has  as device input event, it can be used to search its respective attribute name:

{{hc|# udevadm info -a /dev/input/event6|2=
...
KERNEL=="event6"
...
ATTRS{name}=="SIGMACHIP USB Keyboard"
}}

Now write a custom udev rule to add the "power-switch" tag:

{{hc|/etc/udev/rules.d/70-power-switch-my.rules|2=
ACTION=="remove", GOTO="power_switch_my_end"
SUBSYSTEM=="input", KERNEL=="event*", ATTRS{name}=="SIGMACHIP USB Keyboard", TAG+="power-switch"
LABEL="power_switch_my_end"
}}

After reloading the udev rules and restarting , you should see  in the journal of logind.

## System freezes for 60 seconds and then wakes back up or hangs after waking up
Since systemd v256, systemd freezes  before sleeping. This process can fail due to kernel bugs, particularly when KVM is in use.[https://github.com/systemd/systemd/issues/33083Messages in the logs will contain  before sleep. When such an issue occurs, trying to login (start another session) would fail with:

To temporarily revert back to the old behavior, edit , , , and  with the following drop-in:

However, this drop-in can itself prevent the system from going to sleep.[https://gitlab.freedesktop.org/drm/amd/-/issues/4178
