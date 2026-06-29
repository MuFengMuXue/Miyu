[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=High_Performance_Computing_on_Gentoo&action=edit).

This document was written by people at the Adelie Linux R&D Center as a step-by-step guide to turn a Gentoo System into a High Performance Computing (HPC) system.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Configuring Gentoo Linux for Clustering]](#Configuring_Gentoo_Linux_for_Clustering)
    -   [[2.1] [Recommended Optimizations]](#Recommended_Optimizations)
    -   [[2.2] [Communication Layer (TCP/IP Network)]](#Communication_Layer_.28TCP.2FIP_Network.29)
    -   [[2.3] [NFS/NIS]](#NFS.2FNIS)
    -   [[2.4] [RSH/SSH]](#RSH.2FSSH)
    -   [[2.5] [NTP]](#NTP)
    -   [[2.6] [IPTABLES]](#IPTABLES)
-   [[3] [HPC Tools]](#HPC_Tools)
    -   [[3.1] [OpenPBS]](#OpenPBS)
    -   [[3.2] [MPICH]](#MPICH)
-   [[4] [Bibliography]](#Bibliography)

## [Introduction]

Gentoo Linux, a special flavor of Linux that can be automatically optimized and customized for just about any application or need. Extreme performance, configurability and a top-notch user and developer community are all hallmarks of the Gentoo experience.

Thanks to a technology called Portage, Gentoo Linux can become an ideal secure server, development workstation, professional desktop, gaming system, embedded solution or\... a High Performance Computing system. Because of its near-unlimited adaptability, we call Gentoo Linux a metadistribution.

This document explains how to turn a Gentoo system into a High Performance Computing system. Step by step, it explains what packages one may want to install and helps configure them.

Obtain Gentoo Linux from the website [\[1\]](https://www.gentoo.org/), and refer to the [documentation](https://wiki.gentoo.org/wiki/Main_Page "Main Page") at the same location to install it.

## [Configuring Gentoo Linux for Clustering]

### [Recommended Optimizations]

** Note**\
We refer to the [Gentoo Linux Handbooks](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") in this section.

During the installation process, you will have to set your USE variables in [/etc/portage/make.conf]. We recommended that you deactivate all the defaults (see [/etc/portage/make.profile/make.defaults]) by negating them in [make.conf]. However, you may want to keep such use variables as 3dnow, gpm, mmx, nptl, nptlonly, sse, ncurses, pam and tcpd. Refer to the USE documentation for more information.

[CODE] **USE Flags**

    USE="-oss 3dnow -apm -avi -berkdb -crypt -cups -encode -gdbm -gif gpm -gtk
    -imlib -java -jpeg -kde -gnome -libg++ -libwww -mikmod mmx -motif -mpeg ncurses
    -nls nptl nptlonly -ogg -opengl pam -pdflib -png -python -qt4 -qtmt
    -quicktime -readline -sdl -slang -spell -ssl -svga tcpd -truetype -vorbis -X
    -xml2 -xv -zlib"

** Note**\
The *tcpd* USE flag increases security for packages such as xinetd.

When you install miscellaneous packages, we recommend installing the following:

`root `[`#`]`emerge --ask nfs-utils portmap tcpdump ssmtp iptables xinetd`

### [][Communication Layer (TCP/IP Network)]

A cluster requires a communication layer to interconnect the slave nodes to the master node. Typically, a FastEthernet or GigaEthernet LAN can be used since they have a good price/performance ratio. Other possibilities include use of products like [Myrinet](http://www.myricom.com/), [QsNet](http://quadrics.com/) or others.

A cluster is composed of two node types: master and slave. Typically, your cluster will have one master node and several slave nodes.

The master node is the cluster\'s server. It is responsible for telling the slave nodes what to do. This server will typically run such daemons as dhcpd, nfs, pbs-server, and pbs-sched. Your master node will allow interactive sessions for users, and accept job executions.

The slave nodes listen for instructions (via ssh/rsh perhaps) from the master node. They should be dedicated to crunching results and therefore should not run any unnecessary services.

The rest of this documentation will assume a cluster configuration as per the hosts file below. You should maintain on every node such a hosts file ([/etc/hosts]) with entries for each node participating node in the cluster.

[FILE] **`/etc/hosts`**

    # Adelie Linux Research & Development Center
    # /etc/hosts

    127.0.0.1       localhost

    192.168.1.100   master.adelie master

    192.168.1.1     node01.adelie node01
    192.168.1.2     node02.adelie node02

To setup your cluster dedicated LAN, edit your [/etc/conf.d/net] file on the master node.

[FILE] **`/etc/conf.d/net`**

    # Global config file for net.* rc-scripts

    # This is basically the ifconfig argument without the ifconfig $iface
    #

    config_eth0="192.168.1.100/24"
    # Network Connection to the outside world using dhcp -- configure as required for you network
    config_eth1="dhcp"

Finally, setup a DHCP daemon on the master node to avoid having to maintain a network configuration on each slave node.

[FILE] **`/etc/dhcp/dhcpd.conf`**

    # Adelie Linux Research & Development Center
    # /etc/dhcp/dhcpd.conf

    log-facility local7;
    ddns-update-style none;
    use-host-decl-names on;

    subnet 192.168.1.0 netmask 255.255.255.0
            host node02.adelie
    }

### [][NFS/NIS]

The Network File System (NFS) was developed to allow machines to mount a disk partition on a remote machine as if it were on a local hard drive. This allows for fast, seamless sharing of files across a network.

There are other systems that provide similar functionality to NFS which could be used in a cluster environment. The [Andrew File System from IBM](http://www.openafs.org), recently open-sourced, provides a file sharing mechanism with some additional security and performance features. The [Coda File System](http://www.coda.cs.cmu.edu/) is still in development, but is designed to work well with disconnected clients. Many of the features of the Andrew and Coda file systems are slated for inclusion in the next version of [NFS (Version 4)](http://www.nfsv4.org). The advantage of NFS today is that it is mature, standard, well understood, and supported robustly across a variety of platforms.

`root `[`#`]`emerge --ask nfs-utils portmap`

Configure and install a kernel to support NFS v3 on all nodes:

[KERNEL] **Required Kernel Configurations for NFS**

    CONFIG_NFS_FS=y
    CONFIG_NFSD=y
    CONFIG_SUNRPC=y
    CONFIG_LOCKD=y
    CONFIG_NFSD_V3=y
    CONFIG_LOCKD_V4=y

On the master node, edit your [/etc/hosts.allow] file to allow connections from slave nodes. If your cluster LAN is on 192.168.1.0/24, your [hosts.allow] will look like:

[FILE] **`/etc/hosts.allow`**

    portmap:192.168.1.0/255.255.255.0

Edit the [/etc/exports] file of the master node to export a work directory structure ([/home] is good for this).

[FILE] **`/etc/exports`**

    /home/  *(rw)

Add nfs to your master node\'s default runlevel:

`root `[`#`]`rc-update add nfs default`

To mount the nfs exported filesystem from the master, you also have to configure your salve nodes\' [/etc/fstab]. Add a line like this one:

[FILE] **`/etc/fstab`**

    master:/home/  /home  nfs  rw,exec,noauto,nouser,async  0 0

You\'ll also need to set up your nodes so that they mount the nfs filesystem by issuing this command:

`root `[`#`]`rc-update add nfsmount default`

### [][RSH/SSH]

SSH is a protocol for secure remote login and other secure network services over an insecure network. OpenSSH uses public key cryptography to provide secure authorization. Generating the public key, which is shared with remote systems, and the private key which is kept on the local system, is done first to configure OpenSSH on the cluster.

For transparent cluster usage, private/public keys may be used. This process has two steps:

-   Generate public and private keys
-   Copy public key to slave nodes

For user based authentication, generate and copy as follows:

`root `[`#`]`ssh-keygen -t dsa`

    Generating public/private dsa key pair.
    Enter file in which to save the key (/root/.ssh/id_dsa): /root/.ssh/id_dsa
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /root/.ssh/id_dsa.
    Your public key has been saved in /root/.ssh/id_dsa.pub.
    The key fingerprint is:
    f1:45:15:40:fd:3c:2d:f7:9f:ea:55:df:76:2f:a4:1f root@master

    WARNING! If you already have an "authorized_keys" file,
    please append to it, do not use the following command.

`root `[`#`]`scp /root/.ssh/id_dsa.pub node01:/root/.ssh/authorized_keys`

    root@master's password:
    id_dsa.pub   100%  234     2.0MB/s   00:00

`root `[`#`]`scp /root/.ssh/id_dsa.pub node02:/root/.ssh/authorized_keys`

    root@master's password:
    id_dsa.pub   100%  234     2.0MB/s   00:00

** Note**\
Host keys must have an empty passphrase. RSA is required for host-based authentication.

For host based authentication, you will also need to edit your [/etc/ssh/shosts.equiv].

[FILE] **`/etc/ssh/shosts.equiv`**

    node01.adelie
    node02.adelie
    master.adelie

And a few modifications to the [/etc/ssh/sshd_config] file:

[FILE] **`/etc/ssh/sshd_config`sshd configurations**

    # $OpenBSD: sshd_config,v 1.42 2001/09/20 20:57:51 mouring Exp $
    # This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin

    # This is the sshd server system-wide configuration file. See sshd(8)
    # for more information.

    # HostKeys for protocol version 2
    HostKey /etc/ssh/ssh_host_rsa_key

If your application require RSH communications, you will need to emerge [[[net-misc/netkit-rsh]](https://packages.gentoo.org/packages/net-misc/netkit-rsh)[]] and [[[sys-apps/xinetd]](https://packages.gentoo.org/packages/sys-apps/xinetd)[]].

`root `[`#`]`emerge --ask xinetd netkit-rsh`

Then configure the rsh deamon. Edit your [/etc/xinet.d/rsh] file.

[FILE] **`/etc/xinet.d/rsh`**

    # Adelie Linux Research & Development Center
    # /etc/xinetd.d/rsh

    service shell


Edit your [/etc/hosts.allow] to permit rsh connections:

[FILE] **`/etc/hosts.allow`**

    # Adelie Linux Research & Development Center
    # /etc/hosts.allow

    in.rshd:192.168.1.0/255.255.255.0

Or you can simply trust your cluster LAN:

[FILE] **`/etc/hosts.allow`**

    # Adelie Linux Research & Development Center
    # /etc/hosts.allow

    ALL:192.168.1.0/255.255.255.0

Finally, configure host authentication from [/etc/hosts.equiv].

[FILE] **`/etc/hosts.equiv`**

    # Adelie Linux Research & Development Center
    # /etc/hosts.equiv

    master
    node01
    node02

And, add xinetd to your default runlevel:

`root `[`#`]`rc-update add xinetd default`

### [NTP]

The Network Time Protocol (NTP) is used to synchronize the time of a computer client or server to another server or reference time source, such as a radio or satellite receiver or modem. It provides accuracies typically within a millisecond on LANs and up to a few tens of milliseconds on WANs relative to Coordinated Universal Time (UTC) via a Global Positioning Service (GPS) receiver, for example. Typical NTP configurations utilize multiple redundant servers and diverse network paths in order to achieve high accuracy and reliability.

Select a NTP server geographically close to you from [Public NTP Time Servers](http://www.eecis.udel.edu/~mills/ntp/servers.html), and configure your [/etc/conf.d/ntp] and [/etc/ntp.conf] files on the master node.

[FILE] **`/etc/conf.d/ntp`**

    # /etc/conf.d/ntpd

    # NOTES:
    #  - NTPDATE variables below are used if you wish to set your
    #    clock when you start the ntp init.d script
    #  - make sure that the NTPDATE_CMD will close by itself ...
    #    the init.d script will not attempt to kill/stop it
    #  - ntpd will be used to maintain synchronization with a time
    #    server regardless of what NTPDATE is set to
    #  - read each of the comments above each of the variable

    # Comment this out if you dont want the init script to warn
    # about not having ntpdate setup
    NTPDATE_WARN="n"

    # Command to run to set the clock initially
    # Most people should just uncomment this line ...
    # however, if you know what you're doing, and you
    # want to use ntpd to set the clock, change this to 'ntpd'
    NTPDATE_CMD="ntpdate"

    # Options to pass to the above command
    # Most people should just uncomment this variable and
    # change 'someserver' to a valid hostname which you
    # can acquire from the URL's below
    NTPDATE_OPTS="-b ntp1.cmc.ec.gc.ca"

    ##
    # A list of available servers is available here:
    # http://www.eecis.udel.edu/~mills/ntp/servers.html
    # Please follow the rules of engagement and use a
    # Stratum 2 server (unless you qualify for Stratum 1)
    ##

    # Options to pass to the ntpd process that will *always* be run
    # Most people should not uncomment this line ...
    # however, if you know what you're doing, feel free to tweak
    #NTPD_OPTS=""

Edit your [/etc/ntp.conf] file on the master to setup an external synchronization source:

[FILE] **`/etc/ntp.conf`**

    # Adelie Linux Research & Development Center
    # /etc/ntp.conf

    # Synchronization source #1
    server ntp1.cmc.ec.gc.ca
    restrict ntp1.cmc.ec.gc.ca
    # Synchronization source #2
    server ntp2.cmc.ec.gc.ca
    restrict ntp2.cmc.ec.gc.ca
    stratum 10
    driftfile /etc/ntp.drift.server
    logfile /var/log/ntp
    broadcast 192.168.1.255
    restrict default kod
    restrict 127.0.0.1
    restrict 192.168.1.0 mask 255.255.255.0

And on all your slave nodes, setup your synchronization source as your master node.

[FILE] **`/etc/conf.d/ntp`On slave node**

    # /etc/conf.d/ntpd

    NTPDATE_WARN="n"
    NTPDATE_CMD="ntpdate"
    NTPDATE_OPTS="-b master"

[FILE] **`/etc/ntp.conf`On slave node**

    # Adelie Linux Research & Development Center
    # /etc/ntp.conf

    # Synchronization source #1
    server master
    restrict master
    stratum 11
    driftfile /etc/ntp.drift.server
    logfile /var/log/ntp
    restrict default kod
    restrict 127.0.0.1

Then add ntpd to the default runlevel of all your nodes:

`root `[`#`]`rc-update add ntpd default`

** Note**\
NTP will not update the local clock if the time difference between your synchronization source and the local clock is too great.

### [IPTABLES]

To setup a firewall on your cluster, you will need iptables.

`root `[`#`]`emerge --ask iptables`

Required kernel configuration:

[KERNEL] **IPtables kernel configuration**

    CONFIG_NETFILTER=y
    CONFIG_IP_NF_CONNTRACK=y
    CONFIG_IP_NF_IPTABLES=y
    CONFIG_IP_NF_MATCH_STATE=y
    CONFIG_IP_NF_FILTER=y
    CONFIG_IP_NF_TARGET_REJECT=y
    CONFIG_IP_NF_NAT=y
    CONFIG_IP_NF_NAT_NEEDED=y
    CONFIG_IP_NF_TARGET_MASQUERADE=y
    CONFIG_IP_NF_TARGET_LOG=y

And the rules required for this firewall:

[FILE] **`/var/lib/iptables/rule-save`**

    # Adelie Linux Research & Development Center
    # /var/lib/iptables/rule-save

    *filter
    :INPUT ACCEPT [0:0]
    :FORWARD ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
    -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
    -A INPUT -s 192.168.1.0/255.255.255.0 -i eth1 -j ACCEPT
    -A INPUT -s 127.0.0.1 -i lo -j ACCEPT
    -A INPUT -p icmp -j ACCEPT
    -A INPUT -j LOG
    -A INPUT -j REJECT --reject-with icmp-port-unreachable
    COMMIT
    *nat
    :PREROUTING ACCEPT [0:0]
    :POSTROUTING ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    -A POSTROUTING -s 192.168.1.0/255.255.255.0 -j MASQUERADE
    COMMIT

Then add iptables to the default runlevel of all your nodes:

`root `[`#`]`rc-update add iptables default`

## [HPC Tools]

### [OpenPBS]

The Portable Batch System (PBS) is a flexible batch queuing and workload management system originally developed for NASA. It operates on networked, multi-platform UNIX environments, including heterogeneous clusters of workstations, supercomputers, and massively parallel systems. Development of PBS is provided by Altair Grid Technologies.

`root `[`#`]`emerge --ask openpbs`

** Note**\
OpenPBS ebuild does not currently set proper permissions on var-directories used by OpenPBS.

Before starting using OpenPBS, some configurations are required. The files you will need to personalize for your system are:

-   [/etc/pbs_environment]
-   [/var/spool/PBS/server_name]
-   [/var/spool/PBS/server_priv/nodes]
-   [/var/spool/PBS/mom_priv/config]
-   [/var/spool/PBS/sched_priv/sched_config]

Here is a sample [sched_config]:

[FILE] **`/var/spool/PBS/sched_priv/sched_config`**

    #
    # Create queues and set their attributes.
    #
    #
    # Create and define queue upto4nodes
    #
    create queue upto4nodes
    set queue upto4nodes queue_type = Execution
    set queue upto4nodes Priority = 100
    set queue upto4nodes resources_max.nodect = 4
    set queue upto4nodes resources_min.nodect = 1
    set queue upto4nodes enabled = True
    set queue upto4nodes started = True
    #
    # Create and define queue default
    #
    create queue default
    set queue default queue_type = Route
    set queue default route_destinations = upto4nodes
    set queue default enabled = True
    set queue default started = True
    #
    # Set server attributes.
    #
    set server scheduling = True
    set server acl_host_enable = True
    set server default_queue = default
    set server log_events = 511
    set server mail_from = adm
    set server query_other_jobs = True
    set server resources_default.neednodes = 1
    set server resources_default.nodect = 1
    set server resources_default.nodes = 1
    set server scheduler_iteration = 60

To submit a task to OpenPBS, the command `qsub` is used with some optional parameters. In the example below, \"-l\" allows you to specify the resources required, \"-j\" provides for redirection of standard out and standard error, and the \"-m\" will e-mail the user at beginning (b), end (e) and on abort (a) of the job. In the next example, a script is submitted on 2 nodes.

`root `[`#`]`qsub -l nodes=2 -j oe -m abe myscript`

Normally jobs submitted to OpenPBS are in the form of scripts. Sometimes, you may want to try a task manually. To request an interactive shell from OpenPBS, use the \"-I\" parameter.

`root `[`#`]`qsub -I`

To check the status of your jobs, use the qstat command:

`root `[`#`]`qstat`

    Job id  Name  User   Time Use S Queue
    ------  ----  ----   -------- - -----
    2.geist STDIN adelie 0        R upto1nodes

### [MPICH]

Message passing is a paradigm used widely on certain classes of parallel machines, especially those with distributed memory. MPICH is a freely available, portable implementation of MPI, the Standard for message-passing libraries.

The mpich ebuild provided by Adelie Linux allows for two USE flags: *doc* and *crypt*. *doc* will cause documentation to be installed, while *crypt* will configure MPICH to use `ssh` instead of `rsh`.

`root `[`#`]`emerge --ask mpich`

You may need to export a mpich work directory to all your slave nodes in [/etc/exports]:

[FILE] **`/etc/exports`**

    /home  *(rw)

Most massively parallel processors (MPPs) provide a way to start a program on a requested number of processors; `mpirun` makes use of the appropriate command whenever possible. In contrast, workstation clusters require that each process in a parallel job be started individually, though programs to help start these processes exist. Because workstation clusters are not already organized as an MPP, additional information is required to make use of them. Mpich should be installed with a list of participating workstations in the file [machines.LINUX] in the directory [/usr/share/mpich/]. This file is used by `mpirun` to choose processors to run on.

Edit this file to reflect your cluster-lan configuration:

[FILE] **`/usr/share/mpich/machines.LINUX`**

    # Change this file to contain the machines that you want to use
    # to run MPI jobs on. The format is one host name per line, with either
    #    hostname
    # or
    #    hostname:n
    # where n is the number of processors in an SMP. The hostname should
    # be the same as the result from the command "hostname"
    master
    node01
    node02
    # node03
    # node04
    # ...

Use the script `tstmachines` in [/usr/sbin/] to ensure that you can use all of the machines that you have listed. This script performs an `rsh` and a short directory listing; this tests that you both have access to the node and that a program in the current directory is visible on the remote node. If there are any problems, they will be listed. These problems must be fixed before proceeding.

The only argument to `tstmachines` is the name of the architecture; this is the same name as the extension on the machines file. For example, the following tests that a program in the current directory can be executed by all of the machines in the LINUX machines list.

`root `[`#`]`/usr/local/mpich/sbin/tstmachines LINUX`

** Note**\
This program is silent if all is well; if you want to see what it is doing, use the -v (for verbose) argument:

`root `[`#`]`/usr/local/mpich/sbin/tstmachines -v LINUX`

The output from this command might look like:

[CODE] **Output of the above command**

    Trying true on host1.uoffoo.edu ...
    Trying true on host2.uoffoo.edu ...
    Trying ls on host1.uoffoo.edu ...
    Trying ls on host2.uoffoo.edu ...
    Trying user program on host1.uoffoo.edu ...
    Trying user program on host2.uoffoo.edu ...

If `tstmachines` finds a problem, it will suggest possible reasons and solutions. In brief, there are three tests:

\

-   *Can processes be started on remote machines?* tstmachines attempts to run the shell command true on each machine in the machines files by using the remote shell command.
-   *Is current working directory available to all machines?* This attempts to ls a file that tstmachines creates by running ls using the remote shell command.
-   *Can user programs be run on remote systems?* This checks that shared libraries and other components have been properly installed on all machines.

And the required test for every development tool:

`root `[`#`]`cd ~ `

`root `[`#`]`cp /usr/share/mpich/examples1/hello++.c ~ `

`root `[`#`]`make hello++ `

`root `[`#`]`mpirun -machinefile /usr/share/mpich/machines.LINUX -np 1 hello++`

For further information on MPICH, consult the documentation at [http://www-unix.mcs.anl.gov/mpi/mpich/docs/mpichman-chp4/mpichman-chp4.htm](http://www-unix.mcs.anl.gov/mpi/mpich/docs/mpichman-chp4/mpichman-chp4.htm) .

## [Bibliography]

The original document is published at the Adelie Linux R&D Centre web site, and is reproduced here with the permission of the authors and [Cyberlogic](http://www.cyberlogic.ca)\'s Adelie Linux R&D Centre.

-   [Gentoo](https://www.gentoo.org/)
-   [Linux NFS Project](http://nfs.sourceforge.net/)
-   [Mathematics and Computer Science Division, Argonne National Laboratory](http://www-unix.mcs.anl.gov/mpi/mpich/)
-   [NTP](http://www.ntp.org/)
-   [David L. Mills, University of Delaware](http://www.eecis.udel.edu/~mills/)
-   [Secure Shell Working Group, IETF, Internet Society](http://www.ietf.org/html.charters/secsh-charter.html)
-   [Guardian Digital](http://www.linuxsecurity.com/)
-   [Altair Grid Technologies, LLC.](http://www.openpbs.org/)

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Marc St-Pierre, Benoit Morin, Jean-Francois Richard, Olivier Crete, Donnie Berkholz, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*