# KVM

KVM, Kernel-based Virtual Machine, is a hypervisor built into the Linux kernel. It is similar to Xen in purpose but much simpler to get running. Unlike native QEMU, which uses emulation, KVM is a special operating mode of QEMU that uses CPU extensions (HVM) for virtualization via a kernel module.

Using KVM, one can run multiple virtual machines running unmodified GNU/Linux, Windows, or any other operating system. (See Guest Support Status for more information.) Each virtual machine has private virtualized hardware: a network card, disk, graphics card, etc.

Differences between KVM and Xen, VMware, or QEMU can be found at the KVM FAQ.

This article does not cover features common to multiple emulators using KVM as a backend. You should see related articles for such information.

## Checking support for KVM
## Hardware support
KVM requires that the virtual machine host's processor has virtualization support (named VT-x for Intel processors and AMD-V for AMD processors). You can check whether your processor supports hardware virtualization with the following command:

 $ LC_ALL=C.UTF-8 lscpu | grep Virtualization

Alternatively:

 $ grep -E --color=auto 'vmx|svm|0xc0f' /proc/cpuinfo

If nothing is displayed after running either command, then your processor does not support hardware virtualization, and you will not be able to use KVM.

## Kernel support
Arch Linux kernels provide the required kernel modules to support KVM.

* One can check if the necessary modules,  and either  or , are available in the kernel with the following command:

 $ zgrep CONFIG_KVM= /proc/config.gz

The module is available only if it is set to either  or .

* Then, ensure that the kernel modules are automatically loaded, with the command:

If the command returns nothing, the module needs to be loaded manually; see Kernel modules#Manual module handling.

## Para-virtualization with Virtio
Para-virtualization provides a fast and efficient means of communication for guests to use devices on the host machine. KVM provides para-virtualized devices to virtual machines using the Virtio API as a layer between the hypervisor and guest.

All Virtio devices have two parts: the host device and the guest driver.

## Kernel support
Use the following command inside the virtual machine to check if the VIRTIO modules are available in the kernel:

 $ zgrep VIRTIO /proc/config.gz

Then, check if the kernel modules are automatically loaded with the command:

 $ lsmod | grep virtio

In case the above commands return nothing, you need to load the kernel modules manually.

## List of para-virtualized devices
* network device (virtio-net)
* block device (virtio-blk)
* controller device (virtio-scsi)
* serial device (virtio-serial)
* balloon device (virtio-balloon)

## How to use KVM
See the main article: QEMU.

## Tips and tricks
## Nested virtualization
Nested virtualization enables existing virtual machines to be run on third-party hypervisors and on other clouds without any modifications to the original virtual machines or their networking.

On host, enable nested feature for :

 # modprobe -r kvm_intel
 # modprobe kvm_intel nested=1

To make it permanent (see Kernel modules#Setting module options):

Verify that feature is activated:

Enable the "host passthrough" mode to forward all CPU features to the guest system:

# If using QEMU, run the guest virtual machine with the following command: .
# If using virt-manager, change the CPU model to .
# If using virsh, use  and change the CPU line to

Boot the virtual machine and check if the  flag is present:

 $ grep -E --color=auto 'vmx|svm' /proc/cpuinfo

## Enabling huge pages
You may also want to enable hugepages to improve the performance of your virtual machine.
With an up to date Arch Linux and a running KVM, you probably already have everything you need. Check if you have the directory . If not, create it.
Now we need the right permissions to use this directory. The default permission is root's uid and gid with 0755, but we want anyone in the kvm group to have access to hugepages.

Add to your :

Instead of specifying the group name directly, with , you can of course specify the gid as a number, but it must match the  group. The mode of  allows anyone in the group to create files but not unlink or rename each other's files. Make sure  is mounted properly:

Now you can calculate how many hugepages you need. Check how large your hugepages are:

 $ grep Hugepagesize /proc/meminfo

Normally that should be 2048 kB ≙ 2 MB. Let us say you want to run your virtual machine with 1024 MB. 1024 / 2 = 512. Add a few extra so we can round this up to 550. Now tell your machine how many hugepages you want:

 # sysctl -w vm.nr_hugepages=550

If you had enough free memory, you should see:

If the number is smaller, close some applications or start your virtual machine with less memory (number_of_pages x 2):

 $ qemu-system-x86_64 -enable-kvm -m 1024 -mem-path /dev/hugepages -hda  Note the  parameter. This will make use of the hugepages.

Now you can check, while your virtual machine is running, how many pages are used:

Now that everything seems to work, you can enable hugepages by default if you like. Add to your :

See also:

* [https://docs.kernel.org/admin-guide/mm/hugetlbpage.html Summary of hugetlbpage support in the Linux kernel
* Debian Wiki - Hugepages

## Secure Boot
KVM Secure boot has a few requirements before it can be enabled:

# You must use a UEFI with secure boot support compiled in.
# The UEFI must have keys enrolled.

To enable UEFI with secure boot support, install  and set your virtual machine to use the secure boot enabled UEFI. If you are using libvirt, you can do this by adding the following to the XML configuration of your virtual machine.

Next you need to enroll some keys. In this example we will enroll Microsoft and Redhat's secure boot keys. Install  and run the following. Replace  with the name of your virtual machine.

 $ virt-fw-vars --input /usr/share/edk2/x64/OVMF_VARS.4m.fd --output /var/lib/libvirt/qemu/nvram/vm_name_SECURE_VARS.fd --secure-boot --enroll-redhat

Then edit the libvirt XML configuration of your virtual machine to point to the new VARS file.

{{bc|1=

  /usr/share/edk2/x64/OVMF_CODE.secboot.4m.fd
  /var/lib/libvirt/qemu/nvram/{vm-name}_SECURE_VARS.fd

}}

After this secure boot should automatically be enabled. You can double check by entering the virtual machine's BIOS by pressing  when you see the UEFI boot logo.
