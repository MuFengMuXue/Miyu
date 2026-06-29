Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Chroot/de "Chroot (94% translated)")
-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/Chroot/tr "Chroot (7% translated)")
-   [español](https://wiki.gentoo.org/wiki/Chroot/es "Chroot (18% translated)")
-   [français](https://wiki.gentoo.org/wiki/Chroot/fr "Chroot (90% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Chroot/it "Chroot (18% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Chroot/hu "chroot (94% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Chroot/pt-br "Chroot (18% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Chroot/sv "Chroot (18% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Chroot/ru "Chroot (73% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Chroot/ta "chroot (18% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Chroot/zh-cn "Chroot (66% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Chroot/ja "Chroot (99% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Chroot/ko "Chroot (16% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Chroot "wikipedia:Chroot")

[**chroot**] **(*Ch*ange *root*)** is a Unix system utility used to change the apparent root directory to create a new environment logically separate from the main system\'s root directory. This new environment is known as a \"chroot jail.\" A user operating inside the jail cannot see or access files outside of the environment they have been locked into.

One of the main uses for chrooting is to create a separate Linux system on top of a the current one for the purpose of testing or software compatibility. Chroot is often seen as a lightweight alternative to virtualization because it is able to run without the overhead of a hypervisor.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Setting up the environment]](#Setting_up_the_environment)
    -   [[1.2] [Unpacking the system files]](#Unpacking_the_system_files)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [systemd-nspawn]](#systemd-nspawn)
    -   [[3.2] [Init scripts]](#Init_scripts)
-   [[4] [Sound and graphics]](#Sound_and_graphics)
    -   [[4.1] [Wayland]](#Wayland)
    -   [[4.2] [PipeWire]](#PipeWire)
    -   [[4.3] [Xorg]](#Xorg)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Prerequisites]

### [Setting up the environment]

When creating a new chroot setup, the first thing needed is a directory in which the chroot can reside. For example, a chroot could be created in [/mnt/mychroot]:

`root `[`#`]`mkdir /mnt/mychroot `

`root `[`#`]`cd /mnt/mychroot `

To mount an existing installation from a partition the following command can be run. Be sure to replace the `<DEVICE>` string in the example below with the drive and partition of the existing installation:

`root `[`#`]`mkdir /mnt/mychroot `

`root `[`#`]`mount /dev/<DEVICE> /mnt/mychroot `

If an installation has been previously created in a sub directory of the current root file system, the above steps need not be repeated.

### [Unpacking the system files]

When building a new install, the next step is to download the stage3 tarball and unpack it to chroot location. For more information on this process please see [Downloading the stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Downloading_the_stage_tarball "Handbook:AMD64/Installation/Stage") and [Unpacking the stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Unpacking_the_stage_tarball "Handbook:AMD64/Installation/Stage") in the Gentoo [Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page").

`root `[`#`]`links http://distfiles.gentoo.org/releases/amd64/autobuilds/ `

`root `[`#`]`tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C /mnt/mychroot `

Note that unpacking must as **root** user - otherwise on system update you will get error **/proc: mount failed**.

## [Configuration]

Before entering the chroot a number of directories must be mounted:

`root `[`#`]`mount --rbind /dev /mnt/mychroot/dev `

`root `[`#`]`mount --make-rslave /mnt/mychroot/dev `

`root `[`#`]`mount -t proc /proc /mnt/mychroot/proc `

`root `[`#`]`mount --rbind /sys /mnt/mychroot/sys `

`root `[`#`]`mount --make-rslave /mnt/mychroot/sys `

`root `[`#`]`mount --rbind /tmp /mnt/mychroot/tmp `

`root `[`#`]`mount -t tmpfs -o mode=0755 tmpfs /mnt/mychroot/run `

Some basic configuration files must be copied from the host. Do not copy [/etc/portage/make.conf] when using an existing installation:

`root `[`#`]`cp /etc/portage/make.conf /mnt/mychroot/etc/portage # When using an existing installation, skip this command. `

`root `[`#`]`cp /etc/resolv.conf /mnt/mychroot/etc `

## [Usage]

Once done, enter the chroot environment by executing the following commands:

`root `[`#`]`chroot /mnt/mychroot /bin/bash `

`root `[`#`]`. /etc/profile `

`root `[`#`]`export PS1="(chroot) $PS1" `

To persist that - you can add them to .bashrc:

[FILE] **`/root/.bashrc`**

    . /etc/profile
    export PS1="(chroot) $PS1"

If you are getting error like **Error opening terminal: xterm-kitty** - add to .bashrc

[FILE] **`/root/.bashrc`**

    export TERM=xterm

When creating a new installation, Portage should be synced to make sure everything is up to date.

`(chroot) root #``emerge-webrsync`

`(chroot) root #``emerge --sync`

The system is now ready. Feel free to install software, mess with settings, test experimental packages and configurations \-- all without having any effect on the main system. To leave the chroot simply type [exit] or press [Ctrl]+[d]. Doing so will return the console to the normal environment. Do not forget to [umount] the directories that have been mounted.

### [systemd-nspawn]

If the system uses systemd, [[systemd-nspawn](https://wiki.gentoo.org/wiki/Systemd-nspawn "Systemd-nspawn")] can be used, which can automatically handle much of the boilerplate required in administering chroots. For example, to enter a chroot via systemd-nspawn with the same configuration as specified in the Configuration section, simply run:

`root `[`#`]`cp /etc/portage/make.conf /mnt/mychroot/etc/portage `

`root `[`#`]`systemd-nspawn -D /mnt/mychroot --bind=/tmp --resolv-conf=/etc/resolv.conf `

### [Init scripts]

If setting up chroots is a task that must be performed often, it is possible to speed up the mounting of the directories by using an init script. The script could be added to the default runlevel and therefore set up automatically on system boot:

[FILE] **`/etc/init.d/mychroot`**

    #!/sbin/openrc-run

    depend()

    start()

    stop()

When using a different directory or partition, add the necessary mounting commands in the `start()` function and change [/mnt/chroot] to the appropriate name.

## [Sound and graphics]

The software running inside the chroot will by default not have access to the system sound- and display-server. Fixing this is done by either sharing a **socket**, or by running the communication with TCP over localhost.

### [Wayland]

Wayland uses a socket to connect clients with the compositor. This socket needs to be shared with the chroot to make graphical applications work. The general procedure for finding this socket is:^[\[1\]](#cite_note-1)^

1.  If `WAYLAND_SOCKET` is set, interpret it as a file descriptor number on which the connection is already established, assuming that the parent process configured the connection for us.
2.  If `WAYLAND_DISPLAY` is set, concat with `XDG_RUNTIME_DIR` to form the path to the Unix socket.
3.  Assume the socket name is `wayland-0` and concat with `XDG_RUNTIME_DIR` to form the path to the Unix socket.

Using `WAYLAND_DISPLAY` and `XDG_RUNTIME_DIR` is fine in most cases and will be used here. By default (outside the chroot) `XDG_RUNTIME_DIR` is set to [/run/user/\$(uid)]. This directory will not be available in the chroot because the [#Configuration](https://wiki.gentoo.org/wiki/Chroot#Configuration "Chroot") instructions **bind mounts** [/run] non-recursively. Assuming the user\'s uid is 1000, the to-be-set destination being unavailable can be solved by either bind-mounting [/run/user/1000] with:

`root `[`#`]`mkdir -p /mnt/mychroot/run/user/1000`

`root `[`#`]`mount --bind /run/user/1000 /mnt/mychroot/run/user/1000`

or by simply recursively bind mounting [/run] with:

`root `[`#`]`mount --rbind /run /mnt/mychroot/run`

The Wayland library [[[dev-libs/wayland]](https://packages.gentoo.org/packages/dev-libs/wayland)[]] uses the same procedure for finding out the socket as listed above. So to share the socket with the chroot, the only thing that\'s needed to do is defining `XDG_RUNTIME_DIR` and `WAYLAND_DISPLAY`. Here it is assumed that the Wayland socket name `WAYLAND_DISPLAY` is `wayland-0`.

`(chroot) root #``useradd -m user`

`(chroot) root #``su -l user`

`(chroot) user $``export XDG_RUNTIME_DIR=/run/user/1000`

`(chroot) user $``export WAYLAND_DISPLAY=wayland-0`

`(chroot) user $``MOZ_ENABLE_WAYLAND=1 firefox-bin`

Permission errors will occur if the user in the chroot does not have permissions to access the Wayland socket. This can be solved by using [user namespace remapping](https://man7.org/linux/man-pages/man7/user_namespaces.7.html) or [ACLs](https://wiki.gentoo.org/wiki/Filesystem/Access_Control_List_Guide "Filesystem/Access Control List Guide"). The easiest solution is to just make sure that the user ids match. The [useradd -u, \--uid UID] option can be used when creating a user.

### [PipeWire]

Like Wayland, PipeWire uses a socket to connect clients to the PipeWire daemon.

Applications assume that the PipeWire socket will be located in `$/pipewire-0`, so the only thing that\'s needed to get PipeWire clients to connect to the host\'s daemon is to expose `XDG_RUNTIME_DIR` to the chroot. This process is identical to the one described in [#Wayland](https://wiki.gentoo.org/wiki/Chroot#Wayland "Chroot"). To expose `XDG_RUNTIME_DIR`, often /run/user/\$(uid), the following commands are used:

`root `[`#`]`mkdir -p /mnt/mychroot/run/user/1000`

`root `[`#`]`mount --bind /run/user/1000 /mnt/mychroot/run/user/1000`

`XDG_RUNTIME_DIR` will not be set when logging in inside the chroot, therefore `XDG_RUNTIME_DIR` needs to exported so the PipeWire client can find the socket:

`(chroot) user $``export XDG_RUNTIME_DIR=/run/user/1000`

`(chroot) user $``pw-cli`

### [Xorg]

Xorg by default listens on a socket located in `/tmp/.X11-unix/X$`, as well as on localhost TCP port `6000 + $`^[\[2\]](#cite_note-2)^. The instructions in [#Configuration](https://wiki.gentoo.org/wiki/Chroot#Configuration "Chroot") bind mounts [/tmp], and therefore no additional configuration is needed except setting the DISPLAY variable before running a graphical application:

`(chroot) user $``DISPLAY=:0 firefox-bin`

If the uid of the user inside the chroot does not match the uid outside the chroot, then setting permissions with xhost will be needed. To allow all local connections, run outside the chroot:

`user `[`$`]`xhost +local:`

## [See also]

-   [Project:X86/Chroot Guide](https://wiki.gentoo.org/wiki/Project:X86/Chroot_Guide "Project:X86/Chroot Guide") --- provides instructions on how to create a fresh Gentoo installation inside a [chroot] to assist in testing Gentoo packages for stabilization and for other sundry testing.
-   [Knowledge Base:Chrooting returns exec format error](https://wiki.gentoo.org/wiki/Knowledge_Base:Chrooting_returns_exec_format_error "Knowledge Base:Chrooting returns exec format error")
-   [Chrooting proxy services](https://wiki.gentoo.org/wiki/Chrooting_proxy_services "Chrooting proxy services")
-   [Security Handbook/Chrooting and virtual servers](https://wiki.gentoo.org/wiki/Security_Handbook/Chrooting_and_virtual_servers "Security Handbook/Chrooting and virtual servers")
-   [PRoot](https://wiki.gentoo.org/wiki/PRoot "PRoot") --- a user-space implementation of chroot, mount \--bind, and binfmt_misc.
-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.

## [External resources]

-   [*chroot*](https://wiki.archlinux.org/index.php/Chroot) on Archlinux\'s wiki

## [References]

1.  [[[↑](#cite_ref-1)] [[https://wayland-book.com/protocol-design/wire-protocol.html](https://wayland-book.com/protocol-design/wire-protocol.html)]]
2.  [[[↑](#cite_ref-2)] [So if DISPLAY=:12, then Xorg will listen on localhost TCP port 6012]]