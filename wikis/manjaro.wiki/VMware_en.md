[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-VMware&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=VMware "VMware (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=VMware/tr "VMware (17% translated)") • ‎[português do Brasil](//wiki.manjaro.org/index.php?title=VMware/pt-br "VMware (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=VMware/ru "VMware (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=VMware/zh-cn "VMware/zh-cn (0% translated)")

## Contents

-   [[1] [VMware Workstation on Manjaro]](#VMware_Workstation_on_Manjaro)
    -   [[1.1] [**DISCLAIMER**]](#DISCLAIMER)
-   [[2] [How to use the AUR PKGBUILD]](#How_to_use_the_AUR_PKGBUILD)
    -   [[2.1] [Important kernel precaution]](#Important_kernel_precaution)
    -   [[2.2] [Building steps]](#Building_steps)
    -   [[2.3] [Optional services]](#Optional_services)
-   [[3] [Installing Manjaro under VMWare]](#Installing_Manjaro_under_VMWare)
-   [[4] [Copy and Paste]](#Copy_and_Paste)
-   [[5] [Resources]](#Resources)

## [VMware Workstation on Manjaro]

### [**DISCLAIMER**]

**Tip**

------------------------------------------------------------------------

**Read the [VMware Workstation 16 supported OS](https://kb.vmware.com/s/article/80807) article**.

VMware is a commercially developed application with a limited list of supported operating systems.

This guide is a courtesy to the forum **don\'t expect any support** on VMware related issues.

As you can see from above reference - Archlinux and derivatives are unsupported platforms for running VMware products and as such it is unsupported on Manjaro.

So even when it is possible to install and run VMware on Manjaro - \*\*do not expect support\*\* on configuration of virtual machines or system issues arising from your VMware installation. You must have the required level of troubleshooting skills to solve these when they arise - and they will.

-   If you need help configuring vmware virtual machines - your should look in the VMware documentation.
-   If you need help troubleshooting installation issues - use the comment section for the AUR PKGBUILD

## [How to use the AUR PKGBUILD]

There is a lot of AUR helpers and they all mimic what you should do manually - the Arch way is usually the best way.

### [Important kernel precaution]

The AUR PKGBUILD is created for Archlinux and therefore the kernel headers dependency must be solved manually on Manjaro. Archlinux only have two kernel versions - linux and linux-lts.

Archlinux kernels follow the release schedule on kernel.org and on Manjaro you will need to use the same kernel versions which - at the time of writing in March 2021 - is (check with [https://kernel.org](https://kernel.org) if in doubt)

-   **Linux 5.10.x (LTS)**
-   **Linux 5.11.x (mainline)**

Using other kernels - like 5.4LTS - will most likely fail.

### [Building steps]

1\. Update your system and install the necessary build tools

[user \$ ][ sudo pacman -Syu git base-devel \--needed [COPY TO CLIPBOARD]]

\

2\. Then check your kernel version(s) - example - remember to use the same version as Arch

[user \$ ][ mhwd-kernel -li [COPY TO CLIPBOARD]]

\

3\. Then install the headers for your kernel(s) and dkms. Substitute *\$KERNELXYY* with your currently running kernel

[user \$ ][ sudo pacman -Syu \$KERNELXYY-headers dkms [COPY TO CLIPBOARD]]

\

4\. Clone the PKGBUILKD script

[user \$ ][ git clone https://aur.archlinux.org/vmware-workstation.git \~/vmware-workstation [COPY TO CLIPBOARD]]

\

5\. Familiarize yourself with the content - it is all text files and you should read them and verify what they are doing.

[user \$ ][ ls \~/vmware-workstation [COPY TO CLIPBOARD]]

\

6\. When you are satisfied - cd into the folder

[user \$ ][ cd \~/vmware-workstation [COPY TO CLIPBOARD]]

\

7\. Run makepkg to install dependencies, build and install the package.

[user \$ ][ makepkg -is [COPY TO CLIPBOARD]]

\

The installer will write messages in the terminal on what to do next - follow the directions to load the kernel modules and enable vmware network service and usb service as needed.

[user \$ ][ sudo modprobe -a vmw_vmci vmmon [COPY TO CLIPBOARD]]

\

### [Optional services]

There are three services that can be optionally be enabled:

-   vmware-networks.service: Provides network access inside VMs, most people will want this enabled
-   vmware-usbarbitrator.service: Allows USB devices to be connected inside VMs
-   vmware-hostd.service: Enables sharing of VMs on the network

To start and enable vmware network

[user \$ ][ sudo systemctl enable \--now vmware-networks.service [COPY TO CLIPBOARD]]

\

To start and enable usb passthrough

[user \$ ][ sudo systemctl enable \--now vmware-usbarbitrator.service [COPY TO CLIPBOARD]]

\

To start and enable the sharing of a virtual machine

[user \$ ][ sudo systemctl enable \--now vmware-hostd.service [COPY TO CLIPBOARD]]

\

## [Installing Manjaro under VMWare]

There are no special requirements to installing Manjaro on VMWare. **open-vmware-tools** is pre-installed. It should \"just work\"

## [Copy and Paste]

Ensure you are using Xorg as Wayland has some limitations. See: [https://kb.vmware.com/s/article/74671](https://kb.vmware.com/s/article/74671)

If copy and paste does not work, you may need to install gtkmm3 and re-boot. vmware-user-suid-wrapper depends on gtkmm, but it\'s not a required dependency of the package. See: [https://bugs.archlinux.org/task/43159](https://bugs.archlinux.org/task/43159)

## [Resources]

-   [Manjaro Forum - (root tip) Installing VMware on Manjaro](https://forum.manjaro.org/t/root-tip-installing-vmware-on-manjaro/57596)
-   [VMware KB - Workstation/Player 16 Supported OS](https://kb.vmware.com/s/article/80807)
-   [Manjaro Forum Search - VMware](https://forum.manjaro.org/search?q=vmware)