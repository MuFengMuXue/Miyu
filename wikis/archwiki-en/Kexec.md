# Kexec

Kexec is a system call that enables you to load and boot into another kernel from the currently running kernel. This is useful for kernel developers or other people who need to reboot very quickly without waiting for the whole BIOS boot process to finish. Note that kexec may not work correctly for you due to devices not fully re-initializing when using this method, however this is rarely the case.

## Installation
Install the  package.

## Rebooting using kexec
## Manually
You can manually invoke kexec using:

 # kexec -l /boot/vmlinuz-linux --initrd=/boot/initramfs-linux.img --reuse-cmdline
 # kexec -e

It is also possible to load kernel manually and then let systemd handle service shutdown and kexec for you.

 # kexec -l /boot/vmlinuz-linux --initrd=/boot/initramfs-linux.img --reuse-cmdline
 # systemctl kexec

## systemd
By default, if systemd-boot is used and no kernel was loaded manually using  before, systemd will load the kernel specified in the default boot loader entry. For example, to reboot into the newer kernel after a system update, you may simply run:

 # systemctl kexec

The command will refuse to execute if you have several  entries (e.g. for Microcode updates) which are currently not supported.

## Custom unit file
If the default behavior does not work for you or you desire to conveniently load custom kernels, you may wrap the kernel loading into a service unit. Create a new unit file, , that will load the specified kernel to be kexec'ed:

Then enable the service file for the kernel you want to load, (e.g. for  it will be  )

Ensure that the shutdown hook is not part of your initramfs image by removing it from the  array in . If it is, remove it and regenerate the initramfs.

Then to kexec

 # systemctl kexec

If you wish to load a different kernel for the next kexec, for example , disable the service for the current kernel and enable the one for the new kernel.

## Separate /boot partition
The above systemd unit file will fail if  is not on the root file system, as systemd will likely unmount  before it runs the kexec-load unit file. An alternative approach is to load a "hook" unit file that does nothing on startup and invokes kexec upon termination. By making this unit file conflict with  and only , you can ensure the new kernel gets loaded early enough and only after a  command. Here is an alternate  file that follows this strategy:

Note that  is not really needed, as it is implicitly guaranteed by strict ordering on  which itself  with .

## Troubleshooting
## System hangs or reboots after "kexec_core: Starting new kernel"
The troubleshooting information on General troubleshooting#Boot problems may be helpful for diagnosing the problem.

In some cases a hanging system might be an acpi related problem which can be checked on-the-fly like this:

Please adapt the name of the initramfs image and the kernel according to your output of .

Adding the  kernel parameter to the kexec command line has been suggested in and may solve the issue [https://bbs.archlinux.org/viewtopic.php?id=219878 in some cases without the need to completely disable ACPI via .

## No kernel mode-setting (Nvidia)
The graphics driver needs to be unloaded before a kexec, or the next kernel will not be able to gain exclusive control of the device. This is difficult to achieve manually because any programs which need exclusive control over the GPU (Xorg, display managers) must not be running. Below is an example systemd service that will unload the KMS driver right before kexec, which requires that you use .

Afterwards, enable
