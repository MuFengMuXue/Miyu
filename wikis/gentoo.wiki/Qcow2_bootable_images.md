Gentoo provide bootable disk images in qemu's QCOW2 format for amd64 (x86-64) and arm64 (aarch64) and riscv64. The images, updated weekly, include an EFI boot partition and a fully functional Gentoo installation; either with no network activated but a password-less root login on the console ("no root pw"), or with network activated, all accounts initially locked, but cloud-init running on boot ("cloud-init")

## Contents

-   [[1] [Where to download]](#Where_to_download)
    -   [[1.1] [amd64]](#amd64)
    -   [[1.2] [arm64]](#arm64)
    -   [[1.3] [riscv64]](#riscv64)
-   [[2] [Run images]](#Run_images)
    -   [[2.1] [Graphical Option: Virtual Machine Manager with libvirt]](#Graphical_Option:_Virtual_Machine_Manager_with_libvirt)
    -   [[2.2] [Console Option: Install QEMU]](#Console_Option:_Install_QEMU)
        -   [[2.2.1] [amd64]](#amd64_2)
        -   [[2.2.2] [arm64]](#arm64_2)
        -   [[2.2.3] [riscv64]](#riscv64_2)

## [Where to download]

### [amd64]

[https://distfiles.gentoo.org/releases/amd64/autobuilds/current-di-amd64-console/](https://distfiles.gentoo.org/releases/amd64/autobuilds/current-di-amd64-console/)

### [arm64]

[https://distfiles.gentoo.org/releases/arm64/autobuilds/current-di-arm64-console/](https://distfiles.gentoo.org/releases/arm64/autobuilds/current-di-arm64-console/)

### [riscv64]

[https://distfiles.gentoo.org/releases/riscv/autobuilds/current-di-rv64_lp64d-console/](https://distfiles.gentoo.org/releases/riscv/autobuilds/current-di-rv64_lp64d-console/)

## [Run images]

### [Graphical Option: Virtual Machine Manager with libvirt]

1\. Click to *Create a new virtual machine*.

2\. Select the option to *Import existing disk image* and click *Forward*.

3\. *Browse* for the QEMU disk file downloaded from [Qcow2 bootable images](https://wiki.gentoo.org/wiki/Qcow2_bootable_images#Where_to_download "Qcow2 bootable images").

4\. Choose the operating system by typing **Gentoo** into the search-box.

5\. Click *Forward*.

6\. Assign the amount of memory and number of CPU\'s. Click *Forward*.

7\. *Name* the virtual machine.

8\. Click to *Customize configuration before install*. Click *Finish*.

9\. Include firmware to boot by updating **BIOS** to **UEFI x86_64: /usr/share/OVMF/OVMF_CODE_4M.fd**.

10\. Click *Apply*. Click *Begin Installation*.

### [Console Option: Install QEMU]

`root `[`#`]`emerge --ask app-emulation/qemu sys-firmware/edk2-bin`

#### [amd64]

`root `[`#`]`qemu-system-x86_64 \ `

           -m 8G -smp 4 -cpu host -accel kvm -vga virtio -smbios type=0,uefi=on \
           -drive if=pflash,unit=0,readonly=on,file=/usr/share/edk2/OvmfX64/OVMF_CODE_4M.qcow2,format=qcow2 \

-drive file=di-amd64-console.qcow2

#### [arm64]

`root `[`#`]`qemu-system-aarch64 \ `

           -machine virt -cpu neoverse-v1 -m 8G -smp 4 -device virtio-gpu-pci -device usb-ehci -device usb-kbd \
           -drive if=pflash,unit=0,readonly=on,file=/usr/share/edk2/ArmVirtQemu-AARCH64/QEMU_EFI.qcow2 \

-drive file=di-arm64-console.qcow2

#### [riscv64]

`root `[`#`]`qemu-system-riscv64 \ `

-cpu sifive-u54 -machine virt -m 4096 -smp cpus=5,maxcpus=5 \\ -drive if=pflash,unit=0,file=/usr/share/edk2/RiscVVirtQemu/RISCV_VIRT_CODE.qcow2,format=qcow2,readonly=on \\ -drive if=pflash,unit=1,file=/home/huettel/rv64/RISCV_VIRT_VARS.qcow2,format=qcow2,readonly=off \\ -drive file=di-rv64_lp64d-console-last.qcow2 \\ -device virtio-vga \\

-device qemu-xhci -device usb-kbd