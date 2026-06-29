Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Nouveau_%26_nvidia-drivers_switching/hu "Nouveau és nvidia-drivers átkapcsolás (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Nouveau_%26_nvidia-drivers_switching/ru "Переключение между nouveau и nvidia-drivers (32% translated)")

This article describes how to switch between [NVIDIA\'s binary driver](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") and the open source [nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") driver.

## Contents

-   [[1] [Switching using two kernels]](#Switching_using_two_kernels)
    -   [[1.1] [On boot]](#On_boot)
-   [[2] [Switching using a single kernel and hprofile]](#Switching_using_a_single_kernel_and_hprofile)
-   [[3] [Switching using a single kernel and systemd]](#Switching_using_a_single_kernel_and_systemd)
-   [[4] [Switching using a single kernel in an Optimus system without reboot]](#Switching_using_a_single_kernel_in_an_Optimus_system_without_reboot)

## [Switching using two kernels]

### [On boot]

This method assumes the following:

-   Two kernels, one with the nouveau driver enabled and one with the nouveau driver disabled (or built as a module).
-   The nouveau-less kernel needs to have a *-nvidia* suffix.
-   The [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") bootloader.

It is assumed the system already has a nouveau kernel and want to build the one that will use the NVIDIA driver. Begin with appending the *-nvidia* suffix to the kernel name:

[KERNEL]

    General setup  --->
        (-mykernel-nvidia) Local version - append to kernel release

Now make sure the nouveau driver is disabled or built as a module:

[KERNEL]

    Device Drivers  --->
        Graphics support  --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
            <M> Nouveau (NVIDIA) cards

Now recompile and install the kernel. Make sure to update GRUB to take the new kernel into account. Note that kernels with the same version but with different names are considered unique. To emerge an out-of-tree kernel module to be used with the nouveau kernel, first, copy over the nouveau kernels config file to [/usr/src/linux/.config].

[FILE] **`/etc/portage/make.conf`Set `VIDEO_CARDS` to nvidia nouveau**

    VIDEO_CARDS="... nvidia nouveau ..."

After setting or altering `VIDEO_CARDS` values remember to update the system using the following command so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Blacklist the **nvidia** and **nouveau** modules to block [udev](https://wiki.gentoo.org/wiki/Udev "Udev") from autoloading them.

`root `[`#`]`echo -e "blacklist nouveau\nblacklist nvidia" >> /etc/modprobe.d/nvidia-n-nouveau.conf`

And finally use the [local.d](https://wiki.gentoo.org/wiki/Local.d "Local.d") script below to switch graphics driver depending on what kernel is booted:

[FILE] **`/etc/local.d/nvidia.start`**

    #!/bin/bash

    depend()

    if [[ $(uname -r) == *-nvidia ]] ; then
        modprobe -q nvidia
    cat > /etc/X11/xorg.conf.d/01-nvidia.conf << EOF
    Section "Device"
      Identifier   "Device0"
      Driver       "nvidia"
      Option       "NoLogo" "True"
    EndSection
    EOF
    else
        modprobe -q nouveau
        if [ -f /etc/X11/xorg.conf.d/01-nvidia.conf ] ; then
            rm /etc/X11/xorg.conf.d/01-nvidia.conf
        fi
    fi

Copy it to [/etc/local.d/nvidia.start] and set the executable bit:

`root `[`#`]`chmod +x /etc/local.d/nvidia.start`

## [Switching using a single kernel and hprofile]

Another method is switching between two profiles with [hprofile](https://wiki.gentoo.org/wiki/Hprofile "Hprofile"), using a single kernel: [/etc/init.d/hprofile] has to be modified adding a few lines for VGA switching. Warning: hprofile shall be added in boot runlevel.

## [Switching using a single kernel and systemd]

If the system is configured to use systemd, control setting nvidia and nouveau by using the functionality provided by the kernel command line.

** Note**\
The GRUB menu items shown are for demonstrating the changes to be made. Do not just copy and paste them verbatim into [grub.cfg].

Within the [grub.cfg] file, duplicate the desired menu item and then edit the two versions to specify which modules with be blacklisted, and to pass an environment variable to systemd. If nvidia or nouveau modules were previously blacklisted in [/etc/modprobe.d], then remove that configuration since that will now be controlled directly from the kernel command line.

[FILE] **`/boot/grub/grub.cfg`Before:**

    menuentry 'Gentoo Linux'

[FILE] **`/boot/grub/grub.cfg`After:**

    menuentry 'Gentoo Linux - Nouveau'

    menuentry 'Gentoo Linux - Nvidia'

Next, create a small script similar to the one shown in the \"Switching using two kernels\" section. It is very similar, but slightly modified. For the sake on continuity, place it in the same location. The main difference is that is does not use the kernel\'s name to determine which profile to use, but rather it uses a variable set in the environment by systemd from the kernel command line.

[FILE] **`/etc/local.d/nvidia.start`OpenGL**

    #!/bin/bash

    if [[ "$GPUMOD" == "nvidia" ]] ; then
    cat > /etc/X11/xorg.conf.d/01-nv.conf << EOF
    Section "Device"
      Identifier   "Device0"
      Driver       "nvidia"
      Option       "NoLogo" "True"
    EndSection
    EOF
    else
    cat > /etc/X11/xorg.conf.d/01-nv.conf << EOF
    Section "Device"
      Identifier   "Device0"
      Driver       "nouveau"
    EndSection
    EOF
    fi

As mentioned in the previous section, don\'t forget to set the executable bit.

`root `[`#`]`chmod +x /etc/local.d/nvidia.start`

To have this script get called during the systemd init process, create a service file for it, but it\'s just as effective to integrate it into the currently existing xdm, gdm, sddm or other(?) display manager service file. Do not edit the service file directly, since that will get overwritten the next time that package is merged that the service file belongs to. Instead, create an override for the service file, placed in the [/etc/systemd/system/***service-name***.d/] directory.

So for example when using the [sddm.service], create the directory [/etc/systemd/system/sddm.service.d] and place a file in it with a [.conf] file extension. Add a `[Service]` section that has an entry for `ExecStartPre` to call [nvidia.start] before sddm itself is started.

`root `[`#`]`mkdir /etc/systemd/system/sddm.service.d && touch /etc/systemd/system/sddm.service.d/nv.conf`

[FILE] **`/etc/systemd/system/sddm.service.d/nv.conf`Actual contents may vary**

    [Service]
    ExecStartPre=/etc/local.d/nvidia.start

\

## [Switching using a single kernel in an Optimus system without reboot]

In an Optimus system, the graphics is handled by the Intel integrated card, while the user can choose to run specific programs with the NVidia dedicated card. This means that the modules handling the NVidia card can be safely force-unloaded and reloaded without reboot.

Follow the steps in the [NVIDIA/Bumblebee](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee") page, and then add the `nouveau` flag to `VIDEO_CARDS`:

[FILE] **`/etc/portage/make.conf`Set VIDEO_CARDS variable for Optimus**

    VIDEO_CARDS="intel nvidia nouveau"

Then update the system using the following command so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Also, Bumblebee should NOT start on boot:

`root `[`#`]`rc-update del bumblebee default`

Then, follow the steps at [https://wiki.freedesktop.org/nouveau/Optimus/](https://wiki.freedesktop.org/nouveau/Optimus/). In short, list the available providers (which are the video cards):

`user `[`$`]` xrandr --listproviders`

    Providers: number : 2
    Provider 0: id: 0x8a cap: 0xb, Source Output, Sink Output, Sink Offload crtcs: 2 outputs: 2 associated providers: 1 name:Intel
    Provider 1: id: 0x66 cap: 0x7, Source Output, Sink Output, Source Offload crtcs: 2 outputs: 5 associated providers: 1 name:nouveau

The exact output will differ for each system, but the important parameter is `name`. Then, define which card should be used for offloading:

`root `[`#`]`xrandr --setprovideroffloadsink nouveau Intel`

This will set Nouveau for offloading the Intel card. Replace the names `nouveau` and `Intel` with the names shown before.

After reboot, the system should be using Nouveau to handle the cards. The following script can be used to switch between nouveau and nvidia-drivers:

[FILE] **`/usr/bin/nvgraphicswitch`**

    #!/bin/sh

    Driver="$1"

    /etc/init.d/bumblebee stop
    rmmod -v -f nouveau
    sleep 1

    if [ "$" == nouveau ]; then
        modprobe -q nouveau

    elif [ "$" == nvidia ]; then
        /etc/init.d/bumblebee start;

    else
        echo "Choose a graphics driver [nouveau or nvidia]."
    fi

Make it executable:

`root `[`#`]`chmod +x /usr/bin/nvgraphicswitch`

Testing:

`root `[`#`]`nvgraphicswitch nouveau`

`user `[`$`]` DRI_PRIME=0 glxinfo | grep "OpenGL vendor"`

    OpenGL vendor string: Intel Open Source Technology Center

`user `[`$`]` DRI_PRIME=1 glxinfo | grep "OpenGL vendor"`

    OpenGL vendor string: nouveau

`root `[`#`]`nvgraphicswitch nvidia`

`user `[`$`]` primusrun glxinfo | grep "OpenGL vendor"`

    OpenGL vendor string: NVIDIA Corporation