[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Using+autofs+%28automount%29+with+NFS&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Using_autofs_(automount)_with_NFS "Using autofs (automount) with NFS (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Using_autofs_(automount)_with_NFS/tr "NFS ile autofs (automount) kullanımı (6% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Using_autofs_(automount)_with_NFS/ru "Использование autofs (automount) с NFS (100% translated)")

## Contents

-   [[1] [Autofs -- Automount (en)]](#Autofs_.E2.80.93_Automount_.28en.29)
-   [[2] [Autofs]](#Autofs)
-   [[3] [Installation]](#Installation)
-   [[4] [Testing the mounts]](#Testing_the_mounts)
-   [[5] [Terminal commands]](#Terminal_commands)
-   [[6] [Configuration]](#Configuration)
-   [[7] [Explanation of auto.master]](#Explanation_of_auto.master)
-   [[8] [Explanation of auto.shares]](#Explanation_of_auto.shares)
-   [[9] [Remarks]](#Remarks)

# [][Autofs -- Automount (en)]

[![Manjaro-logo.png](/images/0/07/Manjaro-logo.png)](//wiki.manjaro.org/index.php?title=File:Manjaro-logo.png)

\

# [Autofs]

Autofs is a program which makes it possible to mount external devices on demand. Other ways of mounting can be done with the use of a manual command for a temporary mount, or by using the /etc/fstab file if you want to mount a device permanently.

Autofs can be used to mount:

-   USB-flash-disks
-   external hard disks
-   network attached storage devices
-   CD-ROM / DVD / BlueRay and so on.

Autofs mounts these devices in local folders. When you want, or a program you use wants, to read from or write to the device, autofs will do that in those local folders. When you work a lot with mounted systems you will love the way this is done.

Some people believe that since autofs is not maintained heavily it won't exist much longer, but think about this: why do you need to maintain a program which already does what it is supposed to do?

Another way of mounting on the fly is described on this wiki page: [Fstab - Use SystemD automount](//wiki.manjaro.org/index.php?title=Fstab_-_Use_SystemD_automount "Fstab - Use SystemD automount")

# [Installation]

At the time of writing, the autofs version number was 5.1.3-1. It can be installed from the standard Manjaro repositories using Octopi, Pamac or Pacman. When you want to use autofs with nfs you need one extra package and that is nfs-utils. So, install that as well. The description calls it: *support programs for the network filesystem*

# [Testing the mounts]

Before you will install and setup autofs it is a good thing to test if you can mount the device you want to mount.

Let's find out first what you can mount. The nfs-utils package has a nice command for that: showmount:

**showmount -e 192.168.1.9**

When the device is on the output will be something like:

**Export list for 192.168.1.9:** **/HDD1 \***

There is a disk called HDD1 in the device on address 192.168.1.9.

Remark: *You do need to know the IP-address of the device to use showmount.*

Now let's mount it to our local folder /mnt:

'''sudo mount -t nfs 192.168.1.9:/HDD1 /mnt'''

Type 'ls /mnt' to find out what is on the disk you just mounted. When you see contents the mount has succeeded and we can now continue with the configuration of autofs.

# [Terminal commands]

Commands you can use are:

**sudo systemctl enable autofs** *Command to enable autofs so it can be started either manually or at next boot*

**sudo systemctl start autofs** *Command to manually start autofs*

**sudo systemctl restart autofs** *Command to manually restart autofs*

**sudo systemctl stop autofs** *Command to manually stop autofs*

**sudo systemctl status autofs** *Command to read the status of autofs*

When autofs is running this is the output of the status command:

**sudo systemctl status autofs**

     ● autofs.service - Automounts filesystems on demand
        Loaded: loaded (/usr/lib/systemd/system/autofs.service; enabled; vendor preset: disabled)
        Active: active (running) since Sat 2017-12-02 07:13:22 CET; 1h 9min ago
       Process: 1069 ExecStart=/usr/bin/automount $OPTIONS --pid-file /run/autofs.pid (code=exited, status=0/SUCCESS)
      Main PID: 1089 (automount)
         Tasks: 5 (limit: 4915)
        CGroup: /system.slice/autofs.service
                └─1089 /usr/bin/automount --pid-file /run/autofs.pid
     Dec 02 07:13:22 Desktop-Jan systemd[1]: Starting Automounts filesystems on demand...
     Dec 02 07:13:22 Desktop-Jan automount[1089]: -
     Dec 02 07:13:22 Desktop-Jan systemd[1]: Started Automounts filesystems on demand.

After a stop it looks like this:

**sudo systemctl status autofs**

     ● autofs.service - Automounts filesystems on demand
        Loaded: loaded (/usr/lib/systemd/system/autofs.service; enabled; vendor preset: disabled)
        Active: inactive (dead) since Sat 2017-12-02 08:27:27 CET; 1s ago
       Process: 1069 ExecStart=/usr/bin/automount $OPTIONS --pid-file /run/autofs.pid (code=exited, status=0/SUCCESS)
      Main PID: 1089 (code=exited, status=0/SUCCESS)
     Dec 02 07:13:22 Desktop-Jan systemd[1]: Starting Automounts filesystems on demand...
     Dec 02 07:13:22 Desktop-Jan automount[1089]: -
     Dec 02 07:13:22 Desktop-Jan systemd[1]: Started Automounts filesystems on demand.
     Dec 02 08:27:26 Desktop-Jan systemd[1]: Stopping Automounts filesystems on demand...
     Dec 02 08:27:27 Desktop-Jan systemd[1]: Stopped Automounts filesystems on demand.

# [Configuration]

After installation we need to configure a few files specific to what we need and want. These files are placed in the folder: **/etc/autofs**. In fact there are 2 files needed: auto.master and auto.\<any name you like\>. Since /etc/autofs is a folder owned by root you need root privileges to write and/or edit them.

In auto.master we write:

-   the base folder where mounts are connected to the local filesystem
-   the name of the file in which the mount can be configured
-   a timeout value (time after which the mount is automatically unmounted when not needed anymore)
-   ghost, an option which places empty folders in the base folder to make it possible, after the time-out, to mount the device again.

A typical line in the auto.master file can look like this:

**/mnt /etc/autofs/auto.NAS1 \--timeout=10 \--ghost**

When you have more than one external device you want to mount using autofs you can do 2 things:

-   write an extra line in the auto.master file for each device. For example:

**/mnt /etc/autofs/auto.NAS1 \--timeout=10 \--ghost**

**/mnt /etc/autofs/auto.NAS2 \--timeout=10 \--ghost**

and create extra config files for each device, or

-   use 1 line in the auto.master file using 1 config file for all devices and write more than 1 line in this config file. This is totally up to you.

I use this:

*/etc/autofs/auto.master:*

**/mnt /etc/autofs/auto.shares \--time-out=5 \--ghost**

*/etc/autofs/auto.shares:*

**NAS-Seagate -fstype=nfs,rw,soft,retry=0 Seagate:/shares/Folder1**

**NAS-WD -fstype=nfs,rw,soft,retry=0 WD:/nfs/Public**

This way I have one master file which, with one line, controls the base of the system and one file which controls all my shares. But again, this is totally up to you.

# [Explanation of auto.master]

This file is created when you install the autofs package. You will need to edit it to make it work for you. The complete file looks like this when created:

     # key [ -mount-options-separated-by-comma ] location
     # For details of the format look at autofs(5).
     #
     #/misc /etc/auto.misc
     #
     # NOTE: mounts done from a hosts map will be mounted with the
     #  "nosuid" and "nodev" options unless the "suid" and "dev"
     #  options are explicitly given.
     #
     #/net  -hosts
     #
     # Include central master map if it can be found using
     # nsswitch sources.
     #
     # Note that if there are entries for /net or /misc (as
     # above) in the included master map any keys that are the
     # same will not be seen as the first read key seen takes
     # precedence.
     #
     #/net        -hosts           -nosuid
     +auto.master

Add your line or lines just before the last visible line: +auto.master

After that line an empty line should exist or the configuration will not succeed, so place the cursor after +auto.master and click on ENTER.

Format of the line you add:

*base-folder name_of_share_file options*.

In my example this is:

**/mnt /etc/autofs/auto.shares \--time-out=5 \--ghost**

***NOTE: Make sure the used filename in the auto.master file should be exactly the same as the name of the file you use, including the path.***

The base folder can be /. In this case it is written as: /- You use direct addressing now. The address you write in the shares file (see next paragraph) becomes the complete address. When you write the name of a folder in the master file you use indirect addressing: the complete path is now the sum of the path in the master file + the one in the shares file.

# [Explanation of auto.shares]

This file can have any extention name you like. Make it a descriptive one to easily find it, especially when you use more than one. The line or lines in this file are all built according to this template:

*name_of_sub-folder options source*

(separated with at least one space)

After mounting the external device can be found in the following directory structure:

**/base-folder/sub-folder**

You define the base folder in the auto.master file (first item in the line) and the sub-folder is defined in the auto.xxxx file (also first item on the line)

My shares are mounted at: /mnt/NAS-WD and /mnt/NAS-Seagate.

/mnt is the base-folder (from auto.master) and both NAS folders are written in the shares file.

Options you can use are plenty. See the man pages for autofs, automount and nfs. The ones I used here work for me. They take care of the following:

-   **-fstype=nfs**

The used filesystem is nfs (Network File System), a file-system used much in Linux environments.

-   **rw**

The mount is readable and writable. If you only need read access then use ro (read only)

-   **soft**

If the server fails an I/O error is given, but the file-manager keeps running. When you use hard instead of soft, it hangs till the connection has been re-established.

-   **retry=0**

This makes sure that mount stops immediately when the server is not reachable. If not, mount will keep trying for 2 minutes to reach the server and block the program which wants to reach the server.

# [Remarks]

-   It is said that when you make a change in the shares file, the change will be active straight away. When changing the master file you need to restart the autofs.service like this:

**sudo systemctl restart autofs** *It is advisable to also restart after changing the shares file, just to be sure.*

-   The permissions of both the master and the share file(s) should be 644. That means Read/Write permission for user, Read for group and Read for others.

<!-- -->

-   Test if the system works. First example is the result when nothing is mounted, in the second example you see the result when the NAS-WD is mounted:

\$ /etc/autofs \> **sudo ps -A\|grep \"nfs\\\|rpc\"**

       240 ?       00:00:00 rpcbind
     23222 ?       00:00:00 rpciod
     23227 ?       00:00:00 nfsiod

\$ /etc/autofs \> **cd /mnt/NAS-WD** *Change directory to the mount*

\$ /mnt/NAS-WD \> **sudo ps -A\|grep \"nfs\\\|rpc\"**

       240 ?       00:00:00 rpcbind
     23222 ?       00:00:00 rpciod
     23227 ?       00:00:00 nfsiod
     29106 ?       00:00:00 rpc.statd

There are many webpages about autofs, with and without nfs. Just google it and you will find many different ways of setting it up. The way described here works for me and is pretty easy to setup.