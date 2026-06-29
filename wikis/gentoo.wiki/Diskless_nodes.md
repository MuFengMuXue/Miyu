This page contains [[changes](https://wiki.gentoo.org/index.php?title=Diskless_nodes&oldid=1045876&diff=1344021)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Diskless_nodes/es "Nodos sin disco (100% translated)")
-   [français](https://wiki.gentoo.org/wiki/Diskless_nodes/fr "Nœuds sans disque (68% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Diskless_nodes/hu "Lemez nélküli csomópontok (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Diskless_nodes/ru "Бездисковые рабочие станции (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Diskless_nodes/zh-cn "无盘节点 (46% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Diskless_nodes/ja "ディスクレスノード (76% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Diskless_nodes/ko "무(無)디스크 노드 (67% translated)")

This article provides instructions for creating and setting up diskless nodes with Gentoo Linux.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [About this article]](#About_this_article)
    -   [[1.2] [What is a diskless machine?]](#What_is_a_diskless_machine.3F)
    -   [[1.3] [Before starting]](#Before_starting)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Master and the slaves]](#Master_and_the_slaves)
        -   [[2.1.1] [About kernels]](#About_kernels)
        -   [[2.1.2] [The master kernel]](#The_master_kernel)
        -   [[2.1.3] [About the slave kernel]](#About_the_slave_kernel)
        -   [[2.1.4] [The preliminary slave file system]](#The_preliminary_slave_file_system)
    -   [[2.2] [The DHCP server]](#The_DHCP_server)
        -   [[2.2.1] [About the DHCP server]](#About_the_DHCP_server)
        -   [[2.2.2] [Before getting started]](#Before_getting_started)
        -   [[2.2.3] [Installing the DHCP server]](#Installing_the_DHCP_server)
        -   [[2.2.4] [Configuring the DHCP server]](#Configuring_the_DHCP_server)
        -   [[2.2.5] [Starting the DHCP server]](#Starting_the_DHCP_server)
        -   [[2.2.6] [Troubleshooting the DHCP server]](#Troubleshooting_the_DHCP_server)
    -   [[2.3] [TFTP server and PXE Linux Bootloader and/or Etherboot]](#TFTP_server_and_PXE_Linux_Bootloader_and.2For_Etherboot)
        -   [[2.3.1] [About the TFTP server]](#About_the_TFTP_server)
        -   [[2.3.2] [Installing the TFTP server]](#Installing_the_TFTP_server)
        -   [[2.3.3] [Configuring the TFTP server]](#Configuring_the_TFTP_server)
        -   [[2.3.4] [Starting the TFTP server]](#Starting_the_TFTP_server)
        -   [[2.3.5] [About PXELINUX]](#About_PXELINUX)
        -   [[2.3.6] [Before getting started]](#Before_getting_started_2)
        -   [[2.3.7] [Setting up PXELINUX]](#Setting_up_PXELINUX)
        -   [[2.3.8] [Troubleshooting the network boot process]](#Troubleshooting_the_network_boot_process)
    -   [[2.4] [The NFS server]](#The_NFS_server)
        -   [[2.4.1] [About the NFS server]](#About_the_NFS_server)
        -   [[2.4.2] [About Portmapper]](#About_Portmapper)
        -   [[2.4.3] [Before starting]](#Before_starting_2)
        -   [[2.4.4] [Installing the NFS server]](#Installing_the_NFS_server)
        -   [[2.4.5] [Configuring the NFS server]](#Configuring_the_NFS_server)
        -   [[2.4.6] [Starting the NFS server]](#Starting_the_NFS_server)
    -   [[2.5] [Completing the slave filesystem]](#Completing_the_slave_filesystem)
        -   [[2.5.1] [Copy the missing files]](#Copy_the_missing_files)
        -   [[2.5.2] [Configure diskless networking]](#Configure_diskless_networking)
        -   [[2.5.3] [Initialization scripts]](#Initialization_scripts)

## [Introduction]

### [About this article]

This article will help setting up *diskless* workstations based on the Gentoo Linux distribution. This guide is intended to make the process as user friendly as possible and cater to the Linux newbie, because everyone was at a certain point. While an experienced user could easily tie the multiple articles available on diskless nodes and networking together it\'s hoped that this guide can ease the installation for all interested users, geeks, or not.

### [][What is a diskless machine?]

A diskless machine is a PC without any of the usual boot devices such as hard disks, floppy drives or CD-ROMs. The diskless node boots off the network and needs a server that will provide it with storage space as a local hard disk would. From now on the server will be the *master*, while the diskless machine gets called the *slave* (what\'s in a name :). The slave node needs a network adapter that supports PXE booting or Etherboot; check [Etherboot.org](http://www.etherboot.org) for support listings. Most modern cards support PXE and many built-in adapters on motherboards will also work.

### [Before starting]

Gentoo should be installed on the master node and enough space on the master to store the file systems of the slave nodes that are going to be hosted. Also make sure there is one interface to the internet separated from the local area connection.

## [Configuration]

### [Master and the slaves]

#### [About kernels]

The kernel is the software that sits between the hardware and all other software that is loaded on the machine, essentially the heart of a kernel based operating system. When a computer is started, the BIOS executes the instructions found at the reserved boot space of the hard drive. These instructions are typically a boot loader that loads a kernel. After a kernel has been loaded all processes are handled by the kernel.

For more information on kernels and kernel configuration check out the [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") article.

#### [The master kernel]

The master kernel can be as large and as customized as desired but there are a few required kernel options that need to be selected. Go into the kernel configuration menu by typing:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make menuconfig`

There should be a grey and blue GUI that offers a safe alternative to manually editing the [/usr/src/linux/.config] file. If the kernel is currently functioning well it might be a good idea to save the current configuration file by exiting the GUI and typing:

`root `[`#`]`cp .config .config_working`

Go into the following sub-menus and make sure the listed items are checked as built-in (and *NOT* as modular). The options show below are taken from the 2.6.10 kernel version. If a different version is used, the text or sequence might differ. Just make sure to select at least those shown below.

[KERNEL] **master\'s kernel options**

    [*] Networking support --->
      Networking options --->
        <*> Packet socket
        <*> Unix domain sockets
        [*] TCP/IP networking
        [*]   IP: multicasting
        [ ] Network packet filtering (replaces ipchains)

    File systems --->
      Network File Systems  --->
        <*> NFS server support
        [*]   Provide NFSv3 server support

If access to internet through the master node is required and/or a secure firewall is needed make sure to add support for iptables:

[KERNEL] **Enable iptables support**

    [*] Network packet filtering (replaces ipchains)
      IP: Netfilter Configuration  --->
        <*> Connection tracking (required for masq/NAT)
        <*> IP tables support (required for filtering/masq/NAT)

If packet filtering is required, add the rest as modules later. Make sure to read the [Gentoo Security Handbook Chapter about Firewalls](https://wiki.gentoo.org/wiki/Security_Handbook/Firewalls_and_Network_Security "Security Handbook/Firewalls and Network Security") on how to set this up properly.

** Note**\
These kernel configuration options should only be added to the system specific configuration options and are not meant to completely replace the kernel configuration.

After the master kernel has been re-configured, it needs to be rebuilt:

`root `[`#`]`make && make modules_install `

`root `[`#`]`cp arch/i386/boot/bzImage /boot/bzImage-master`

Then add an entry for that new kernel into [lilo.conf] or [grub.conf] depending on which bootloader is being used and make the new kernel the default one. Now that the new bzImage has been copied into the boot directory all that has to be done is to reboot the system in order to load these new options.

#### [About the slave kernel]

It is recommended that the slave kernel be compiled without any modules, since loading and setting them up via remote boot is a difficult and unnecessary process. Additionally, the slave kernel should be as small and compact as possible in order to efficiently boot from the network. The slave\'s kernel is going to be compiled in the same place where the master was configured.

To avoid confusion and wasting time it is probably a good idea to backup the master\'s configuration file by typing:

`root `[`#`]`cp /usr/src/linux/.config /usr/src/linux/.config_master`

The slave\'s kernel is now to be configured in the same fashion as the master\'s kernel. If a fresh configuration file is needed it can be recovered from the default [/usr/src/linux/.config] file by typing:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`cp .config_master .config`

Now go into the configuration GUI by typing:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make menuconfig`

Make sure to select the following options as built-in and *NOT* as kernel modules:

[KERNEL] **slave\'s kernel options**

    [*] Networking support --->
      Networking options --->
        <*> Packet socket
        <*> Unix domain sockets
        [*] TCP/IP networking
        [*]   IP: multicasting
        [*]   IP: kernel level autoconfiguration
        [*]     IP: DHCP support

    File systems --->
      Network File Systems  --->
        <*> file system support
        [*]   Provide NFSv3 client support
        [*]   Root file system on NFS

** Note**\
An alternative to having an dhcp server is setting up a BOOTP server.

** Important**\
It is important to add the network adapter into the kernel (and not as a module) on the nodes. Using modules however is generally not a problem for diskless nodes.

Now the slave\'s kernel needs to be compiled. Be careful here not to overwrite or mess up the modules (if any) that have been built for the master:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make`

Now create the directory on the master that will be used to hold slaves\' files and required system files. The [/diskless] is used but any location preferred may be chosen here. Now copy the slave\'s bzImage into the [/diskless] directory:

\

** Note**\
If there are different architectures being used it might be useful to save each config into [.config_arch] . Do the same with the images: save them into the [/diskless] as [bzImage_arch] .

\

`root `[`#`]`mkdir /diskless `

`root `[`#`]`cp /usr/src/linux/arch/i386/boot/bzImage /diskless `

#### [The preliminary slave file system]

The master and slave filesystems can be tweaked and changed a lot. Right now the only point of interest is in getting a preliminary filesystem of appropriate configuration files and mount points. First it\'s required to create a directory within [/diskless] for the first slave. Each slave needs its own root file system because sharing certain system files will cause permission problems and hard crashes. These directories can be called anything the administrator deems appropriate but the article suggests using the slaves IP addresses as they are unique and not confusing. The static IP of the first slave will be, for instance, `192.168.1.21`:

`root `[`#`]`mkdir -p /diskless/192.168.1.21/etc`

Various configuration files in [/etc] need to be altered to work on the slave. Copy the master\'s [/etc] directory onto the new slave root by typing:

`root `[`#`]`cp -r /etc/* /diskless/192.168.1.21/etc/`

Still this filesystem isn\'t ready because it needs various mount points and directories. To create them, type:

`root `[`#`]`mkdir /diskless/192.168.1.21/home `

`root `[`#`]`mkdir /diskless/192.168.1.21/dev `

`root `[`#`]`mkdir /diskless/192.168.1.21/proc `

`root `[`#`]`mkdir /diskless/192.168.1.21/tmp `

`root `[`#`]`mkdir /diskless/192.168.1.21/mnt `

`root `[`#`]`chmod a+w /diskless/192.168.1.21/tmp `

`root `[`#`]`mkdir /diskless/192.168.1.21/mnt/.initd `

`root `[`#`]`mkdir /diskless/192.168.1.21/root `

`root `[`#`]`mkdir /diskless/192.168.1.21/sys `

`root `[`#`]`mkdir /diskless/192.168.1.21/var `

`root `[`#`]`mkdir /diskless/192.168.1.21/var/empty `

`root `[`#`]`mkdir /diskless/192.168.1.21/var/lock `

`root `[`#`]`mkdir /diskless/192.168.1.21/var/log `

`root `[`#`]`mkdir /diskless/192.168.1.21/var/run `

`root `[`#`]`mkdir /diskless/192.168.1.21/var/spool `

`root `[`#`]`mkdir /diskless/192.168.1.21/usr `

`root `[`#`]`mkdir /diskless/192.168.1.21/opt `

Most of these \"stubs\" should be recognizable; stubs like [/dev], [/proc], or [/sys] will be populated when the slave starts, the others will be mounted later. The [/diskless/192.168.1.21/etc/conf.d/hostname] file should also be changed to reflect the hostname of the slave. Binaries, libraries and other files will be populated later in this HOWTO right before attempting to boot the slave.

Even though [/dev] is populated by `udev` later on, the [console] entry needs to be created. If not, the error message \"unable to open initial console\" will be encountered.

`root `[`#`]`mknod /diskless/192.168.1.21/dev/console c 5 1`

### [The DHCP server]

#### [About the DHCP server]

DHCP stands for Dynamic Host Configuration Protocol. The DHCP server is the first computer the slaves will communicate with when they PXE boot. The primary purpose of the DHCP server is to assign IP addresses. The DHCP server can assign IP addresses based on hosts ethernet MAC addresses. Once the slave has an IP address, the DHCP server will tell the slave where to get its initial file system and kernel.

#### [Before getting started]

There are following things to make sure, they are working properly before beginning. First check the network connectivity using the [ip link show eth0] command. Verify following 3 entries are shown:

-   `state UP`
-   `UP`
-   `MULTICAST`

on the command line output.

`user `[`$`]`ip link show eth0`

    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
        link/ether 0c:2e:53:f2:00:00 brd ff:ff:ff:ff:ff:ff

** Note**\
If the output `MULTICAST` is not displayed, reconfigure the linux-kernel to include and build multicast support.

Using the [ip maddress show eth0] command it is easy to display multicast addressing assinged on the interface **eth0**. The result shows 3 active multicast address ranges:

`user `[`$`]`ip maddress show eth0`

    2:   eth0
        link  33:33:00:00:00:01
        link  33:33:00:00:00:02 users 2
        link  01:00:5e:00:00:01
        link  33:33:ff:a5:c9:45
        link  33:33:ff:00:00:00
        inet  224.0.0.1
        inet6 ff02::1:ff00:0
        inet6 ff02::1:ffa5:c945
        inet6 ff05::2
        inet6 ff01::2
        inet6 ff02::2
        inet6 ff02::1
        inet6 ff01::1

Command output overview table:

  --------------- ----------------------- ---------------------------------------------------------------
  Address layer   Address range           Description
  `link`          **33:33:**xx:xx:xx:xx   Ethernet Address Mapping Space - *IPv6 Packets over Ethernet*
  `inet`          **224.0.0.0/4**         IP Multicast Address Space
  `inet6`         **ff00::/8**            IPv6 Multicast Address Space
  --------------- ----------------------- ---------------------------------------------------------------

#### [Installing the DHCP server]

If the network does not already have a DHCP server installed, one needs to be installed now:

`root `[`#`]`emerge --ask dhcp`

If the network already has a DHCP server installed, edit the configuration file to get the PXE boot to function correctly.

#### [Configuring the DHCP server]

There is only one configuration file that needs to be edited before starting the DHCP server: [/etc/dhcp/dhcpd.conf]. Copy and edit the provided sample file:

`root `[`#`]`cp /etc/dhcp/dhcpd.conf.sample /etc/dhcp/dhcpd.conf `

`root `[`#`]`nano -w /etc/dhcp/dhcpd.conf`

The general layout of the file is set up in an indented fashion and looks like this:

[CODE] **Sample [dhcpd.conf] layout**

    # global options here
    ddns-update-style none;
    shared-network LOCAL-NET
        group
      }
    }

The `shared-network` block is optional and should be used for IPs that are required to be assigned that belong to the same network topology. At least one `subnet` must be declared and the optional `group` block allows options to be grouped between items. A good example of [dhcpd.conf] looks like this:

[CODE] **Sample [dhcpd.conf]**

    #
    # Sample dhcpd.conf for diskless clients
    #

    # Disable dynamic DNS
    ddns-update-style none;

    # Assume one default gateway for IP traffic will do
    option routers 192.168.1.1;

    # Provide DNS info to clients
    option domain-name-servers 192.168.1.1;
    option domain-name "mydomain.com";

    # Specify the TFTP server to be used
    next-server 192.168.1.1;

    # Declare a vendor-specific option buffer for PXE clients:
    # Code 1: Multicast IP address of boot file server
    # Code 2: UDP port that client should monitor for MTFTP responses
    # Code 3: UDP port that MTFTP servers are using to listen for MTFTP requests
    # Code 4: Number of seconds a client must listen for activity before trying
    #         to start a new MTFTP transfer
    # Code 5: Number of seconds a client must listen before trying to restart
    #         a MTFTP transfer

    option space PXE;
    option PXE.mtftp-ip               code 1 = ip-address;
    option PXE.mtftp-cport            code 2 = unsigned integer 16;
    option PXE.mtftp-sport            code 3 = unsigned integer 16;
    option PXE.mtftp-tmout            code 4 = unsigned integer 8;
    option PXE.mtftp-delay            code 5 = unsigned integer 8;
    option PXE.discovery-control      code 6 = unsigned integer 8;
    option PXE.discovery-mcast-addr   code 7 = ip-address;

    # Declare the subnet where our diskless nodes will live
    subnet 192.168.1.0 netmask 255.255.255.0

      # Provide Etherboot clients with appropriate information
      class "etherboot"

      # Add one host declaration for each diskless host
      host slave21
    }

** Note**\
There is nothing prohibiting the use of both PXE boot and Etherboot together. The above Code Listing is merely an example; if there are issues, please consult the DHCPd documentation.

The IP address after `next-server` will be asked for the specified `filename`. This IP address should be the IP of the tftp server, usually the same as the master\'s IP address. The `filename` is relative to the [/diskless] directory (this is due to the tftp server specific options which will be covered later). Inside the `host` block, the `hardware ethernet` option specifies a MAC address, and `fixed-address` assigns a fixed IP address to that particular MAC address. There is a pretty good man page on [dhcpd.conf] with options that are beyond the scope of this HOWTO. The man page can be read by typing:

`user `[`$`]`man dhcpd.conf`

#### [Starting the DHCP server]

Before starting the dhcp initialization script edit the [/etc/conf.d/dhcp] file so that it looks something like this:

[CODE] **Sample [/etc/conf.d/dhcp]**

    IFACE="eth0"
    # Insert any customizations needed

The `IFACE` variable is the device that the DHCP server will be running on, in this case `eth0`. Adding more arguments to the `IFACE` variable can be useful for a complex network topology with multiple Ethernet cards. To start the dhcp server type:

`root `[`#`]`rc-service dhcpd start`

To add the dhcp server to the start-up scripts type:

`root `[`#`]`rc-update add dhcpd default`

#### [Troubleshooting the DHCP server]

To see if a node boots, take a look at [/var/log/messages]. If the node successfully boots, the [messages] file should have some lines at the bottom looking like this:

[CODE] **Sample log file entries created by dhcp**

    DHCPDISCOVER from 00:00:00:00:00:00 via eth0
    DHCPOFFER on 192.168.1.21 to 00:00:00:00:00:00 via eth0
    DHCPREQUEST for 192.168.1.21 from 00:00:00:00:00:00 via eth0
    DHCPACK on 192.168.1.21 to 00:00:00:00:00:00 via eth0

** Note**\
This log file can also help in discovering the slaves\' MAC addresses.

If the following message is encountered it probably means there is something wrong in the configuration file but that the DHCP server is broadcasting correctly.

[CODE] **Sample dhcp server error**

    no free leases on subnet LOCAL-NET

Every time after changing the configuration file the DHCP server must be restarted. To restart the server type:

`root `[`#`]`rc-service dhcpd restart`

### [][TFTP server and PXE Linux Bootloader and/or Etherboot]

#### [About the TFTP server]

TFTP stands for Trivial File Transfer Protocol. The TFTP server is going to supply the slaves with a kernel and an initial filesystem. All of the slave kernels and filesystems will be stored on the TFTP server, so it\'s probably a good idea to make the master the TFTP server.

#### [Installing the TFTP server]

A highly recommended tftp server is available as the tftp-hpa package. This tftp server happens to be written by the author of SYSLINUX and it works very well with pxelinux. To install simply type:

`root `[`#`]`emerge --ask tftp-hpa`

#### [Configuring the TFTP server]

Edit [/etc/conf.d/in.tftpd]. The tftproot directory needs to specified with `INTFTPD_PATH` and any command-line options with `INTFTPD_OPTS`. It should look something like this:

[FILE] **`/etc/conf.d/in.tftpd`**

    INTFTPD_PATH="/diskless"
    INTFTPD_OPTS="-l -v -s $"

The `-l` option indicates that this server listens in stand alone mode so inetd does not have to be run. The `-v` indicates that log/error messages should be verbose. The `-s /diskless` specifies the root of the tftp server.

#### [Starting the TFTP server]

To start the tftp server type:

`root `[`#`]`rc-service in.tftpd start`

This should start the tftp server with the options that were specified in the [/etc/conf.d/in.tftpd]. If this server is to be automatically started at boot type:

`root `[`#`]`rc-update add in.tftpd default`

#### [About PXELINUX]

This section is not required if only Etherboot is being used. PXELINUX is the network bootloader equivalent to LILO or GRUB and will be served via TFTP. It is essentially a tiny set of instructions that tells the client where to locate its kernel and initial filesystem and allows for various kernel options.

#### [Before getting started]

Now the file pxelinux.0 is required, which comes in the SYSLINUX package by H. Peter Anvin. This package can be installed by typing:

`root `[`#`]`emerge --ask syslinux`

#### [Setting up PXELINUX]

Before starting the tftp server pxelinux needs to be set up. First copy the pxelinux binary into the [/diskless] directory:

`root `[`#`]`cp /usr/share/syslinux/pxelinux.0 /diskless `

`root `[`#`]`mkdir /diskless/pxelinux.cfg `

`root `[`#`]`touch /diskless/pxelinux.cfg/default `

This will create a default bootloader configuration file. The binary [pxelinux.0] will look in the [pxelinux.cfg] directory for a file whose name is the client\'s IP address in hexadecimal. If it does not find that file it will remove the rightmost digit from the file name and try again until it runs out of digits. Versions 2.05 and later of syslinux first perform a search for a file named after the MAC address. If no file is found, it starts the previously mentioned discovery routine. If none is found, the [default] file is used.

[CODE] **Files that PXE looks for in [pxelinux.cfg/] in sequence**

    ## (Leading 01 means Ethernet, next bytes match our slave's MAC address)
    01-00-40-63-c2-ca-c9

    ## (Assigned IP in hexadecimal)
    C0A80115
    C0A8011
    C0A801
    C0A80
    C0A8
    C0A
    C0
    C

    default

** Note**\
These are all in lowercase.

Let\'s start with the [default] file:

[CODE] **Sample [pxelinux.cfg/default]**

    DEFAULT gentoo
    LABEL gentoo
    LINUX /bzImage
    APPEND ip=dhcp root=/dev/nfs nfsroot=192.168.1.1:/diskless/192.168.1.21

The `DEFAULT` tag directs pxelinux to the kernel bzImage that was compiled earlier. The `APPEND` tag appends kernel initialisation options. Since the slave kernel was compiled with `NFS_ROOT_SUPPORT` , the nfsroot will be specified here. The first IP is the master\'s IP and the second IP is the directory that was created in [/diskless] to store the slave\'s initial filesystem. Other NFS options [may also be supplied](https://www.kernel.org/doc/Documentation/filesystems/nfs/nfsroot.txt). For example, to use NFS v4.1 over TCP, append `,tcp,vers=4.1` to the nfsroot kernel option: `nfsroot=192.168.1.1:/diskless/192.168.1.21,tcp,vers=4.1`.

#### [Troubleshooting the network boot process]

There are a few things that can be done to debug the network boot process. Primarily a tool called `tcpdump` can be used. To install `tcpdump` type:

`root `[`#`]`emerge --ask tcpdump`

Now various network traffic can be listened to, to make sure the client/server interactions are functioning. If something isn\'t working there are a few things that could be checked. First make sure that the client/server is physically connected properly and that the networking cables are not damaged. If the client/server is not receiving requests on a particular port make sure that there is no firewall interference. To listen to interaction between two computers type:

`root `[`#`]`tcpdump host client_ip and server_ip`

The `tcpdump` command can also be configured to listen on particular port such as the tftp port by typing:

`root `[`#`]`tcpdump port 69`

A common error that might be received is: \"PXE-E32: TFTP open time-out\". This is probably due to firewall issues. If `TCPwrappers` is being used, it might be worth checking [/etc/hosts.allow] and [/etc/hosts.deny] and make sure that they are configured properly. The client should be allowed to connect to the server.

### [The NFS server]

#### [About the NFS server]

NFS stands for Network File System. The NFS server will be used to serve directories to the slave. This part can be somewhat personalized later, but right now all that is wanted is a preliminary slave node to boot diskless.

#### [About Portmapper]

Various client/server services do not listen on a particular port, but instead rely on RPCs (Remote Procedure Calls). When the service is initialised it listens on a random port and then registers this port with the Portmapper utility. NFS relies on RPCs and thus requires Portmapper to be running before it is started.

#### [Before starting]

The NFS Server needs kernel level support so if the kernel does not have this, the master\'s kernel needs to be recompiled. To double check the master\'s kernel configuration type:

`root `[`#`]`grep NFS /usr/src/linux/.config_master`

The output should look something like this if the kernel has been properly configured:

[KERNEL] **Proper NFS specific options in the master\'s kernel configuration**

    CONFIG_PACKET=y
    # CONFIG_PACKET_MMAP is not set
    # CONFIG_NETFILTER is not set
    CONFIG_NFS_FS=y
    CONFIG_NFS_V3=y
    # CONFIG_NFS_V4 is not set
    # CONFIG_NFS_DIRECTIO is not set
    CONFIG_NFSD=y
    CONFIG_NFSD_V3=y
    # CONFIG_NFSD_V4 is not set
    # CONFIG_NFSD_TCP is not set

#### [Installing the NFS server]

The NFS package that can be acquired through portage by typing:

`root `[`#`]`emerge --ask nfs-utils`

This package will emerge a portmapping utility, nfs server, and nfs client utilities and will automatically handle initialisation dependencies.

#### [Configuring the NFS server]

There are three major configuration files that will have to be edited:

[CODE] **Nfs configuration files**

    /etc/exports
    /diskless/192.168.1.21/etc/fstab
    /etc/conf.d/nfs

The [/etc/exports] file specifies how, to who and what to export through NFS. The slave\'s fstab will be altered so that it can mount the NFS filesystems that the master is exporting.

A typical [/etc/exports] for the master should look something like this:

[FILE] **`/etc/exports`master exports file**

    # one line like this for each slave
    /diskless/192.168.1.21   192.168.1.21(sync,rw,no_root_squash,no_all_squash)
    # common to all slaves
    /opt   192.168.1.0/24(sync,ro,no_root_squash,no_all_squash)
    /usr   192.168.1.0/24(sync,ro,no_root_squash,no_all_squash)
    /home  192.168.1.0/24(sync,rw,no_root_squash,no_all_squash)
    # if you want to have a shared log
    /var/log   192.168.1.21(sync,rw,no_root_squash,no_all_squash)

The first field indicates the directory to be exported and the next field indicates to who and how. This field can be divided in two parts: who should be allowed to mount that particular directory, and what the mounting client can do to the filesystem: `ro` for read only, `rw` for read/write; `no_root_squash` and `no_all_squash` are important for diskless clients that are writing to the disk, so that they don\'t get \"squashed\" when making I/O requests. The slave\'s fstab file, [/diskless/192.168.1.21/etc/fstab] , should look like this:

[CODE] **Sample slave [fstab]**

    # these entries are essential
    master:/diskless/192.168.1.21   /         nfs     sync,hard,intr,rw,nolock,rsize=8192,wsize=8192    0 0
    master:/opt                     /opt      nfs     sync,hard,intr,ro,nolock,rsize=8192,wsize=8192    0 0
    master:/usr                     /usr      nfs     sync,hard,intr,ro,nolock,rsize=8192,wsize=8192    0 0
    master:/home                    /home     nfs     sync,hard,intr,rw,nolock,rsize=8192,wsize=8192    0 0
    none                            /proc     proc    defaults                                     0 0
    # useful but superfluous
    master:/var/log                 /var/log  nfs     hard,intr,rw                                 0 0

In this example, *master* is just the hostname of the master but it could easily be the IP of the master. The first field indicates the directory to be mounted and the second field indicates where. The third field describes the filesystem and should be NFS for any NFS mounted directory. The fourth field indicates various options that will be used in the mounting process (see mount(1) for info on mount options). Some people have had difficulties with soft mount points so here they are made hard mounts, a look into various [/etc/fstab] options should be done to make the cluster more efficient.

The last file that should be edited is [/etc/conf.d/nfs] which describes a few options for nfs when it is initialised and looks like this:

[CODE] **Sample master [/etc/conf.d/nfs]**

    # Config file for /etc/init.d/nfs

    # Number of servers to be started up by default
    RPCNFSDCOUNT=8

    # Options to pass to rpc.mountd
    RPCMOUNTDOPTS=""

The `RPCNFSDCOUNT` should be changed to the number of diskless nodes on the network.

#### [Starting the NFS server]

The nfs server should be started with its init script located in [/etc/init.d] by typing:

`root `[`#`]`rc-service nfs start`

If this script is to be started every time the system boots simply type:

`root `[`#`]`rc-update add nfs default`

### [Completing the slave filesystem]

#### [Copy the missing files]

Now the slave\'s file system will be made in sync with the master\'s and provide the necessary binaries while still preserving slave specific files.

`root `[`#`]`rsync -avz /bin /diskless/192.168.1.21 `

`root `[`#`]`rsync -avz /sbin /diskless/192.168.1.21 `

`root `[`#`]`rsync -avz /lib /diskless/192.168.1.21`

** Note**\
The reason for rsync -avz instead of cp is to maintain symlinks and permissions.

#### [Configure diskless networking]

In order to prevent the networking initscript from killing the connection to the NFS server, an option needs to be added to [/etc/conf.d/net] on the diskless client\'s filesystem.

[CODE] **Editing [/etc/conf.d/net]**

    config_eth0="noop"

** Note**\
For more information, please read [/usr/share/doc/openrc-\*/net.example.bz2] .

#### [Initialization scripts]

Init scripts for slaves are located under [/diskless/192.168.1.21/etc/runlevels] for services needed on the diskless nodes. Each slave can be set up and customized here, it all depends on what each slave is meant to do.

** Warning**\
Do not use the [rc-update] program to add or remove scripts from the slave runlevels when logged on to the master. This would change the master runlevels. The links need to be manually created or by logging into the slave nodes using ssh or connecting a screen and keyboard to the slave.

[CODE] **Typical slave runlevels**

    /diskless/192.168.1.21/etc/runlevels/:
    total 16
    drwxr-xr-x    2 root     root         4096 2003-11-09 15:27 boot
    drwxr-xr-x    2 root     root         4096 2003-10-01 21:10 default
    drwxr-xr-x    2 root     root         4096 2003-03-13 19:05 nonetwork
    drwxr-xr-x    2 root     root         4096 2003-02-23 12:26 single

    /diskless/192.168.1.21/etc/runlevels/boot:
    total 0
    lrwxrwxrwx    1 root     root           20 2003-10-18 17:28 bootmisc -> /etc/init.d/bootmisc
    lrwxrwxrwx    1 root     root           19 2003-10-18 17:28 checkfs -> /etc/init.d/checkfs
    lrwxrwxrwx    1 root     root           17 2003-10-18 17:28 clock -> /etc/init.d/clock
    lrwxrwxrwx    1 root     root           22 2003-10-18 17:28 domainname -> /etc/init.d/domainname
    lrwxrwxrwx    1 root     root           20 2003-10-18 17:28 hostname -> /etc/init.d/hostname
    lrwxrwxrwx    1 root     root           22 2003-10-18 17:28 localmount -> /etc/init.d/localmount
    lrwxrwxrwx    1 root     root           19 2003-10-18 17:28 modules -> /etc/init.d/modules
    lrwxrwxrwx    1 root     root           18 2003-10-18 17:28 net.lo -> /etc/init.d/net.lo
    lrwxrwxrwx    1 root     root           20 2003-10-18 17:28 netmount -> /etc/init.d/netmount
    lrwxrwxrwx    1 root     root           21 2003-10-18 17:28 rmnologin -> /etc/init.d/rmnologin
    lrwxrwxrwx    1 root     root           19 2003-10-18 17:28 urandom -> /etc/init.d/urandom

    /diskless/192.168.1.21/etc/runlevels/default:
    total 0
    lrwxrwxrwx    1 root     root           23 2003-10-18 17:28 consolefont -> /etc/init.d/consolefont
    lrwxrwxrwx    1 root     root           19 2003-10-18 17:28 distccd -> /etc/init.d/distccd
    lrwxrwxrwx    1 root     root           19 2003-10-18 17:28 keymaps -> /etc/init.d/keymaps
    lrwxrwxrwx    1 root     root           17 2003-10-18 17:28 local -> /etc/init.d/local
    lrwxrwxrwx    1 root     root           16 2003-10-18 17:28 sshd -> /etc/init.d/sshd
    lrwxrwxrwx    1 root     root           21 2003-10-18 17:28 syslog-ng -> /etc/init.d/syslog-ng
    lrwxrwxrwx    1 root     root           17 2003-10-18 17:28 vixie-cron -> /etc/init.d/vixie-cron

    /diskless/192.168.1.21/etc/runlevels/nonetwork:
    total 0
    lrwxrwxrwx    1 root     root           17 2003-10-18 17:28 local -> /etc/init.d/local

    /diskless/192.168.1.21/etc/runlevels/single:
    total 0

Now is a good time to boot the slave and cross some fingers. It works? Congratulations, you are now the proud owner of (a) diskless node(s).

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Michael Andrews, Kristian Jerpetjoen, Xavier Neys**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*