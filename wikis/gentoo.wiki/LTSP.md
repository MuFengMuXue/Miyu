[]  As of **Feb 21, 2017**, the information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=LTSP&action=edit).

**Resources**

[[]][Home](https://www.ltsp.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Linux_Terminal_Server_Project "wikipedia:Linux Terminal Server Project")

[[]][Official documentation](https://ltsp.org/docs/)

[[]][[#ltsp](ircs://irc.libera.chat/#ltsp)] ([[webchat](https://web.libera.chat/#ltsp)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/ltsp)

The **Linux Terminal Server Project** is a collection of scripts and documentation to create a cluster of thin clients. For instance, an entire client chroot environment is built with a single command: [ltsp-build-client]. This article will guide the administrator through the installation and configuration of a basic LTSP 5 system.

This guide shows how to install and configure the Gentoo LTSP 5 port, and assumes some knowledge of thin client architecture and experience in manually installing Gentoo. Also, a server and client with the specifications listed in the [LTSP manual](https://ltsp.org/docs/installation/) are required. Concerning the client network card, only PXE is included in this manual.

In addition to this guide, several other resources can be of aid while configuring the system. These can be found in the [External resources](#External_resources) section below.

** Note**\
This tutorial uses **[i686]** as architecture for the client install (`x86` before ltsp-server-5.2.19)

## Contents

-   [[1] [Server preparation]](#Server_preparation)
    -   [[1.1] [Installation]](#Installation)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [DHCP and PXE-boot]](#DHCP_and_PXE-boot)
    -   [[1.4] [NFS and Xinetd]](#NFS_and_Xinetd)
    -   [[1.5] [NBD]](#NBD)
    -   [[1.6] [System logging]](#System_logging)
    -   [[1.7] [Sound]](#Sound)
-   [[2] [Client install]](#Client_install)
    -   [[2.1] [Configuration]](#Configuration)
        -   [[2.1.1] [Video cards]](#Video_cards)
        -   [[2.1.2] [Network cards]](#Network_cards)
        -   [[2.1.3] [Kernel]](#Kernel_2)
    -   [[2.2] [Building the client]](#Building_the_client)
    -   [[2.3] [Finishing the install]](#Finishing_the_install)
    -   [[2.4] [Client configuration]](#Client_configuration)
    -   [[2.5] [LDM]](#LDM)
    -   [[2.6] [NBD boot]](#NBD_boot)
    -   [[2.7] [5.2 client]](#5.2_client)
-   [[3] [Tips and tricks]](#Tips_and_tricks)
    -   [[3.1] [NBD swap from USB]](#NBD_swap_from_USB)
    -   [[3.2] [Decreasing chroot size]](#Decreasing_chroot_size)
    -   [[3.3] [X11 keyboard layout]](#X11_keyboard_layout)
    -   [[3.4] [Quickstart]](#Quickstart)
    -   [[3.5] [Portage profile]](#Portage_profile)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [python_get_implementational_package not installed]](#python_get_implementational_package_not_installed)
    -   [[4.2] [do not move package and distfiles dir]](#do_not_move_package_and_distfiles_dir)
    -   [[4.3] [virtual terminals on clients]](#virtual_terminals_on_clients)
    -   [[4.4] [Locales]](#Locales)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Server preparation]

### [Installation]

Gentoo\'s LTSP packages are stored in the [*ltsp*](https://gitweb.gentoo.org/proj/ltsp.git/) [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"). To [use](https://wiki.gentoo.org/wiki/Project:Overlays/Old_User_Guide "Project:Overlays/Old User Guide") the Gentoo LTSP-Overlay, get it with [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]].

`root `[`#`]`eselect repository enable ltsp`

The LTSP server package needs a tftp and dhcp server. In this tutorial [[[net-dns/dnsmasq]](https://packages.gentoo.org/packages/net-dns/dnsmasq)[]] is [used](#DHCP_and_PXE-boot). It also requires a system logger which can accept client messages over tcp, for which [[[app-admin/syslog-ng]](https://packages.gentoo.org/packages/app-admin/syslog-ng)[]] is [used](#System_Logging) in this tutorial. Don\'t forget to add a window manager, ltsp-client won\'t log in if no window manager is installed on the server.

`root `[`#`]`emerge --ask app-admin/syslog-ng net-misc/ltsp-server`

### [Kernel]

Besides the obvious drivers, the server kernel ought to have the following settings. If NFS is going to be used to serve the chroot environments, make sure to compile it in as well and reboot afterwards.

[KERNEL] **LTSP server**

    File systems  --->
        [*] FUSE (Filesystem in Userspace) support
        [*] Network File Systems  --->
            <*> NFS server support
            [*]  NFS server support for NFS version 3

### [DHCP and PXE-boot]

First, setup the server to provide client machines with a kernel at boottime. Although the server depends on a range of possible packages, the manual will use the ones listed in this paragraph. The PXE bootloader is provided by [[[sys-boot/syslinux]](https://packages.gentoo.org/packages/sys-boot/syslinux)[]]. Dnsmasq is a DHCP/DNS/TFTP server. Advanced TFTP is also one of the TFTP server options, and the only one to support multicast TFTP.^**[1](#External_resources)**^ The chroot environments as well as the kernels served at boot time are stored in /opt/ltsp.

Configure [[[net-dns/dnsmasq]](https://packages.gentoo.org/packages/net-dns/dnsmasq)[]] as a DHCP/TFTP server. The TFTP server is used by the client nodes to retrieve the kernel, initramfs and lts.conf. For help on configuration, view the Gentoo Wiki [Dnsmasq](https://wiki.gentoo.org/wiki/Dnsmasq "Dnsmasq") page.

Setup the PXE bootloader; view the [PXE install](https://wiki.gentoo.org/wiki/Syslinux#pxelinux_bootloader_installation "Syslinux") section for more detail. In the example configuration, the system mounts the local client disk after booting and loading the kernel from the server. Make sure the kernel and initramfs are in /var/lib/tftpboot as well as the custom real_init option. You can test the work so far with a working kernel and system.

[FILE] **`/var/lib/tftpboot/pxelinux.cfg/default`ltsp-client 5.3+**

    kernel kernel-YOURKERNELVERSION
    append initrd=initramfs-YOURKERNELVERSION root=/dev/nfs nfsroot=YOURSERVERIP:/opt/ltsp/i686 real_init=/sbin/init-ltsp

Start the services, now and at every boot

`root `[`#`]`/etc/init.d/dnsmasq start`

`root `[`#`]`rc-update add dnsmasq default`

### [NFS and Xinetd]

The chroot environments are shared with NFS. Xinetd is used for **ldminfod** and **nbd** sharing. By default only the localhost is allowed access, so edit the /etc/xinetd.conf and restart the service.

[FILE] **`/etc/xinetd.conf`**

    only_from = 192.168.0.1/24

`root `[`#`]`/etc/init.d/nfs start `

`root `[`#`]`/etc/init.d/xinetd start `

`root `[`#`]`rc-update add nfs default `

`root `[`#`]`rc-update add xinetd default `

### [NBD]

Booting from NBD is still considered testing and doesn\'t work quite out-of-the-box. On the server, several changes are required besides installing [[[sys-block/nbd]](https://packages.gentoo.org/packages/sys-block/nbd)[]]. First, create an nbd-server initscript.

[FILE] **`/etc/init.d/nbd-server`**

    #!/sbin/openrc-run

    command="/usr/bin/nbd-server"
    pidfile="/var/run/$.pid"

    depend()

For the initscript to work, a default config file has to be created also:

[FILE] **`/etc/nbd-server/config`**

    [generic]
    [ltsp]
    exportname = /opt/ltsp/images/i686.img
    readonly = true

Now, start the service now and at every boot.

`root `[`#`]`/etc/init.d/nbd-server start`

`root `[`#`]`rc-update add nbd-server default`

### [System logging]

System logging is performed by [[[app-admin/sysklogd]](https://packages.gentoo.org/packages/app-admin/sysklogd)[]]. Log files are not stored locally however, but sent to the server specified by `SYSLOG_HOST` in [lts.conf]. While executing, the ltsp-client-setup script adds the syslog-ng configuration to perform this. To allow the server to process these incoming log messages, some changes have to be made in that configuration as well. In the syslog-ng setting below, messages are logged to a file named after each client\'s fully qualified domain name.

** Note**\
Remote logging is only activated if `SYSLOG_HOST` is specified.

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    source net ;
    destination remote ;
    log ;

`root `[`#`]`/etc/init.d/syslog-ng restart`

### [Sound]

As you might have seen in the list of emerged dependencies for ltsp, both for the client and the server, [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") was among them. In addition to [[[media-sound/pulseaudio]](https://packages.gentoo.org/packages/media-sound/pulseaudio)[]], its alsa-plugin needs to be installed on both client and server with the `pulseaudio` use flag enabled. Refer to the [Gentoo Wiki](https://wiki.gentoo.org/wiki/PulseAudio#PA_installation "PulseAudio") chapter for detailed installation instructions.

## [Client install]

The ltsp-server package amongst others ships a command called [ltsp-build-client]. This command is responsible for building the entire chroot environment. And while [ltsp-build-client] and available plugins setup the environment, Kicktoo actually builds it. You can also use the [Quickstart](#Quickstart) alternative.

** Note**\
By default a 5.3 client is installed, for a 5.2 client, read the [instructions](#5.2_Client).

** Note**\
By default an NFS client is installed, for an NBD client, read the [instructions](#NBD_Boot).

### [Configuration]

You can invoke the build script with command line arguments or configure the config file in [/etc/ltsp/ltsp-build-client.conf]. During the build, the packaged kicktoo profile in /etc/ltsp/profiles/kicktoo.profile is invoked. For both, example config files were included in the installation of ltsp-server, but other profiles can be configured. Commandline options take precedence over config file options.

#### [Video cards]

Make sure to check if the video card drivers that are needed are installed. By default only `fbdev` and `vesa` are included.

[FILE] **`/etc/ltsp/ltsp-build-client.conf`**

    VIDEO_CARDS="vesa intel radeon mach64"

#### [Network cards]

If Genkernel is used with non default network cards, add the `post_install_initramfs_builder()` function in the kicktoo profile to add Genkernel network modules. This will be included in the next release (5.4.5).

[FILE] **`/etc/ltsp/profiles/kicktoo.profile`**

    post_install_initramfs_builder() " == "genkernel" ]; then
            # add you're own network drivers if needed
            # eg. "MODULES_NET=\"\$\" via-rhine"
            echo "MODULES_NET=\"\$\"" >> "$/usr/share/genkernel/arch/$/modules_load"
        fi
    }

#### [Kernel]

A separate section for the client kernel is in order. A standard Genkernel kernel is created during the installation when configuration changes are made. It\'s advisable to take a closer look at the client\'s kernel config and use the config during the client install. Make sure the network drivers are included as modules.

[KERNEL] **LTSP client**

    General setup  --->
        [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
    [*] Networking support  --->
        Networking options  --->
            [*] IP: kernel level autoconfiguration
            [*] IP: DHCP support
            [*] IP: BOOTP support
    Device Drivers -->
        [*] Block devices  --->
            <M>   Network block device support
    File systems  --->
        <*> Kernel automounter version 4 support (also supports v3)
        <*> FUSE (Filesystem in Userspace) support
        [*] Network File Systems  --->
            <M>   NFS client support
            [*]     NFS client support for NFS version 3
            [*]     NFS client support for the NFSv3 ACL protocol extension
            [*]     NFS client support for NFS version 4 (EXPERIMENTAL)

[FILE] **`/etc/ltsp/ltsp-build-client.conf`**

    KERNEL_SOURCES="=sys-kernel/gentoo-sources-2.6.34-r12"
    KERNEL_CONFIG_URI="tftp://192.168.67.1/ltsp/x86/gentoo-sources-2.6.34-r12.config"

### [Building the client]

When all configuration has been done, start building the client.

`root `[`#`]`ltsp-build-client --config=/etc/ltsp/my-ltsp-build-client.conf`

After invoking the [ltsp-build-client] command, the environment is preparing. For each architecture the first build takes up the most time because binary packages are created from source in the first run. These binary packages are stored in [/usr/portage/packages] through a bind mount on the server. Any consequent builds use these packages to speed up the process.

** Note**\
When having to perform [ltsp-build-client] again, it is recommended to first copy the downloaded stage outside the chroot and point the [ltsp-build-client] command to it, so it won\'t have to be downloaded again.

### [Finishing the install]

Some things still need to be done after building the environment. First up is the kernel, which needs to be put inside the tftproot. In the default setup, this is copied from the chroot in [/opt/ltsp] and copied to the tftproot in an ltsp subdir in [/var/lib/tftpboot], [/tftpboot] or [/srv/tftp], if one exists. Calling [ltsp-update-kernels] with a different tftproot location:

`root `[`#`]`ltsp-update-kernels --tftpdirs="/opt/tftproot"`

The pxelinux configuration has to be updated to reflect the changes in the setup. See the [PXE boot section](#DHCP_and_PXE-boot) for more info.

For a user to be able to login over ssh from the thin client to the server, the client needs the server ssh-keys. Although executed when building the client, these can be updated to the clients chroot with the following command:

`root `[`#`]`ltsp-update-sshkeys`

### [Client configuration]

While some properties of the client\'s environment are more or less statically set in the chroot environment, others can be changed at boot time. The [lts.conf] file allows properties to be set for all clients or for each workstation specifically. Explaining the syntax of the file goes beyond the scope of this tutorial, but it is explained on the [LTSP wiki](http://sourceforge.net/apps/mediawiki/ltsp/index.php?title=Ltsp_LtsConf) and in the lts.conf man page. The latter is available after emerging the [ltsp-docs] package.

The lts.conf file is downloaded at client boot time from a preconfigured location in the tftproot, namely [/ltsp/i686/lts.conf]. Create the lts.conf there and change your architecture if applicable.

[FILE] **`/var/lib/tftpboot/ltsp/i686/lts.conf`**

    [default]
     SERVER=192.168.67.1

** Note**\
The default LTSP server ip is set to 192.168.67.1, change the ip if it is different.

The script that invokes the download is [/etc/init.d/ltsp-client-setup]. Together with [/etc/init.d/ltsp-client] it is responsible for settings like the swap configuration, sound daemon, and date among others. While [ltsp-client-setup] performs the environment settings, [ltsp-client] starts the sound daemon and the ldm login process. Some of these settings will now be discussed in detail.

### [LDM]

If all is well, LDM will be started by [ltsp-client] and it should be possible to log in with a user on the server. If not, it might be worth checking if the LDM Info Daemon is disabled in [/etc/xinitd.d/ldminfod]. When the X server cannot start it might help to add a customized [xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf") file. As many different xorg.conf files can exist for many different clients in the same chroot, make sure to name them properly.

[FILE] **`/var/lib/tftproot/ltsp/i686/lts.conf`**

    [acer-aspire-one]
      X_CONF = /etc/X11/xorg-acer-aspire-one.conf

    [00:1E:68:C2:FF:EE]
      LIKE=acer-aspire-one

To choose another window manager, install it on the server and put the following in the LTSP configuration file (replace Fluxbox with the chosen window manager).

[FILE] **`/var/lib/tftpboot/ltsp/i686/lts.conf`**

    LDM_XSESSION = /usr/bin/fluxbox

### [NBD boot]

If the `nbd` USE flag was enabled, it will be possible to generate a NBD bootable image and initramfs. This is optional (and testing) for now, so there are some steps to be followed to accomplish this. First, before the client install, configure the initramfs-builder for using [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut"). This generates an initramfs which allows to boot an NBD image.

[FILE] **`/etc/ltsp/ltsp-build-client.conf`**

    INITRAMFS_BUILDER="dracut"

** Warning**\
A Dracut initramfs won\'t boot from NFS (tested \<025).

An image has to be generated with [ltsp-build-client]. The resulting image ends up in [/opt/ltsp/image/i686.img].

`root `[`#`]`ltsp-update-image i686`

Because Dracut\'s named export function isn\'t bugfree yet, export names can\'t end with a number (like **[amd64]**). It is therefore advised to configure the [/etc/nbd-server/config] file manually. Look at the example in the [server NBD part](#NBD) of the manual for a working example.

### [5.2 client]

** Warning**\
This is deprecated.

A 5.2 client is somewhat different from a 5.3 client. The main difference is that a 5.2 client has to be specifically prepared to function as an LTSP client while a 5.3 client takes care of this during the boot init process. In theory ltsp-client-5.3 can be installed on any Gentoo system, allowing it to be booted as an LTSP client.

Starting from ltsp-server-5.3, it\'s possible to install a 5.2 or a 5.3 client. This can be done by setting one of the different provided build profiles. By default, the kicktoo-5.3.profile is used.

[FILE] **`/etc/ltsp/ltsp-build-client.conf`**

    INSTALLER_PROFILE=/etc/ltsp/profiles/quickstart-5.2.profile

Booting a 5.3 client requires the following PXE configuration, without a real_init.

[FILE] **`/var/lib/tftpboot/pxelinux.cfg/default`ltsp-client-5.2**

    kernel kernel-YOURKERNELVERSION
    append initrd=initramfs-YOURKERNELVERSION root=/dev/nfs nfsroot=YOURSERVERIP:/opt/ltsp/i686

## [Tips and tricks]

Several optional tips and tricks concerning LTSP can be found here. Most of them are Gentoo specific. Non-Gentoo specific tips & tricks can be found on the [LTSP Wiki](http://wiki.ltsp.org/wiki/Tips_and_Tricks).

### [NBD swap from USB]

The [nbdswapd] allows clients to use swap space through a NBD. For this to work, the [ltsp-server] has to be emerged with the `nbd` USE flag enabled. Also, the lts.conf needs to be updated and the [nbdswapd.conf] has to contain the mountpoint of your usb stick and the desired swap size (64Mb by default).

[FILE] **`/etc/ltsp/nbdswapd.conf`**

    SIZE=128
    SWAPDIR=/mnt/usbswap

[FILE] **`/var/lib/tftpboot/ltsp/i686/lts.conf`**

    [default]
      NBD_SWAP = True

### [Decreasing chroot size]

It is possible to make the built LTSP client chroot smaller using a combination of several methods. It\'s possible to get a chroot less than 1Gb. First up is the [EXCLUDE] var in the ltsp-build-client program. This can be used to automatically unmerge packages at the end of the client build.

[FILE] **`/etc/ltsp/ltsp-build-client.conf`**

    EXCLUDE="sys-apps/man-pages sys-kernel/genkernel"

If there is never any intention to do any maintenance on the chroot again, you can even unmerge gcc this way. Also you can remove the build time dependencies in the chroot by [chrooting](#Chrooting) into the client chroot and executing the following command.

`root `[`#`]`emerge --depclean --with-bdeps=n`

** Note**\
If a client is built a second time from binary packages, those build time dependencies won\'t be installed.

### [X11 keyboard layout]

At the moment, X configuration is disabled. Therefore, all LTSP X settings (in [lts.conf]) does not work, especially `XKBLAYOUT`. For setting the X layout of clients do the following:

`root `[`#`]`mkdir /opt/ltsp/i686/etc/X11/xorg.conf.d/`

`root `[`#`]`cp /opt/ltsp/i686/usr/share/X11/xorg.conf.d/10-evdev.conf /opt/ltsp/i686/etc/X11/xorg.conf.d/10-evdev.conf`

Then edit the file and add the line to the keyboard section of the evdev.conf

[FILE] **`/opt/ltsp/i686/etc/X11/xorg.conf.d/10-evdev.conf`**

    Option "XkbLayout" "fr"

### [Quickstart]

** Warning**\
Support for Quickstart is deprecated, see the Gentoo Bug, comment 186, for more info.

There is also the option to use [Quickstart](http://dev.gentoo.org/~agaffney/quickstart.php) as a possible installer for [ltsp-build-client] (instead of the kicktoo default). Quickstart was the foundation of Kicktoo, but is not under active development anymore. To use this option, emerge it and do the following:

[FILE] **`/etc/ltsp/ltsp-build-client.conf`**

    INSTALLER=quickstart
    INSTALLER_PROFILE=/etc/ltsp/profiles/quickstart.profile

### [Portage profile]

Since ltsp-server-5.3, most of the Portage settings needed to build an ltsp-client chroot are not set in the Quickstart or Kicktoo profiles anymore. Instead they are derived from an LTSP Portage profile. This profile is present in the ltsp ebuild repository, and symlinked to the \$/make.profile during the ltsp-client install.

** Warning**\
Any changes made in this profile will be reset when syncing the ebuild repository.

## [Troubleshooting]

**Bugs** can be reported in two locations:

-   [[[Gentoo]](https://bugs.gentoo.org/show_bug.cgi?id=177580)[]] - For issues related to Gentoo.
-   [[[Upstream]](https://launchpad.net/ltsp/+bugs)[]] - For issues related to LTSP itself.

Check the sections below for workarounds, and see if an existing bug has been opened *before* entering a potential duplicate bug.

### [python_get_implementational_package not installed]

-   reported on: 2011-06-06
-   reported by: [Wimmuskee](https://wiki.gentoo.org/wiki/User:Wimmuskee "User:Wimmuskee")
-   no bug

**problem**

`An emerge error for "=dev-lang/python-2.6* is not installed", with a "die "$(python_get_implementational_package) is not installed";"`

**solution**

`This means that some of your binary packages were installed against Python 2.6, Remove your binary packages to let them compile against your new python environment.`

### [do not move package and distfiles dir]

-   reported on: 2012-02-19
-   reported by: [Wimmuskee](https://wiki.gentoo.org/wiki/User:Wimmuskee "User:Wimmuskee")
-   no bug

**problem**

`The ltsp-build-client and ltsp-chroot programs asume the portage package and distfiles dirs are at Gentoo defaults when they bind mount it into the chroot. Symlinking to another location won't work, neither is moving the dir although refering correctly in /etc/portage/make.conf, all created packages will still be made in /usr/portage version.`

**solution**

`Leave the packagedir to default.`

### [virtual terminals on clients]

Several programs will fight for the virtual terminals on the clients. Comment out getty in inittab:

[FILE] **`/opt/ltsp/i686/etc/inittab`commenting example**

    ...
    # TERMINALS
    #c1:12345:respawn:/sbin/agetty 38400 tty1 linux
    #c2:2345:respawn:/sbin/agetty 38400 tty2 linux
    #c3:2345:respawn:/sbin/agetty 38400 tty3 linux
    #c4:2345:respawn:/sbin/agetty 38400 tty4 linux
    #c5:2345:respawn:/sbin/agetty 38400 tty5 linux
    #c6:2345:respawn:/sbin/agetty 38400 tty6 linux
    ...

### [Locales]

ltsp-build-client does not work witch all locale. quickstart actually requires `C` locale. So if ltsp-build-client shouts with the following message:

`root `[`#`]`ltsp-build-client ... `

No fetcher for protocol: file

unset your locale, remove the directory and restart:

`root `[`#`]`unset LANG; unset LC_ALL; ltsp-build-client --purge`

## [See also]

**Diskless Install**

-   [Gentoo Diskless install using PXE boot](https://wiki.gentoo.org/wiki/Installation_alternatives#Diskless_install_using_PXE_and_kernel.2Finitrd.2Fsquashfs_from_the_LiveCD "Installation alternatives")
-   [Diskless nodes](https://wiki.gentoo.org/wiki/Diskless_nodes "Diskless nodes") --- provides instructions for creating and setting up diskless nodes with Gentoo Linux.

## [External resources]

**Diskless Install**

-   [Syslinux\' PXE Linux page](http://syslinux.zytor.com/wiki/index.php/PXELINUX)
-   [Etherboot Project page](http://etherboot.org/wiki/index.php)

**Union Mounts**

-   [Unionfs: Bringing Filesystems Together](http://www.linuxjournal.com/article/7714)
-   [Aufs](http://aufs.sourceforge.net/)
-   [aufs example](http://www.mail-archive.com/aufs-users@lists.sourceforge.net/msg00687.html)
-   [HOWTO Simple NFS Single System Image with Genkernel 4](https://svn.gentooexperimental.org/genkernel/doc/HOWTO-Genkernel-SSI.txt)

**Other**

-   [LTSP Upstream development](https://launchpad.net/ltsp)
-   [Mailing lists](http://sourceforge.net/mail/?group_id=17723)
-   [into your favorite Linux distro](http://wiki.ltsp.org/wiki/Packaging)
-   [OpenSUSE LTSP Tips & Tricks](http://en.opensuse.org/LTSP/Tips_and_Tricks)
-   [FreeNX](https://launchpad.net/~freenx-team)
-   [LTSP: Thin clients made easy](http://www.tuxradar.com/content/ltsp-thin-clients-made-easy)
-   [A Beginner \"How To\" for gtkrc themes](http://ubuntuforums.org/showthread.php?t=377397)
-   [Ubuntu Community LTSP docs](https://help.ubuntu.com/community/UbuntuLTSP)