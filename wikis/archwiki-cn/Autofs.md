[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Autofs](<../zh-cn/Talk:Autofs.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Autofs](<https://wiki.archlinux.org/title/Autofs> "arch:Autofs")，最近一次同步于 2016-03-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Autofs?diff=0&oldid=419560>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Autofs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** Translation barely started and last touched in 2016（在 [Talk:Autofs#](<../zh-cn/Talk:Autofs.html>) 中讨论）

本文将概述AutoFS的配置方法,当未被挂载的可移除文件系统或是网络共享的文件系统被用户访问时，这个软件包可以提供的自动挂载的支持。 

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")软件包 [autofs](<https://aur.archlinux.org/packages/autofs/>)AUR。 

**提示：** 你将不再需要载入`autofs4` 模式.

##  配置

AutoFS uses template files for configuration which are located in `/etc/autofs` The main template is called `auto.master`, which can point to one or more other templates for specific media types. 

  * Open the file `/etc/autofs/auto.master` with your favorite editor, you will see something similar to this:

    /etc/autofs/auto.master
    
    #/media /etc/autofs/auto.media

The first value on each line determines the base directory under which all the media in a template are mounted, the second value is which template to use. The default base path is `/media`, but you can change this to any other location you prefer. For instance: 
    
    /etc/autofs/auto.master
    
    /media/misc     /etc/autofs/auto.misc     --timeout=5
    /media/net      /etc/autofs/auto.net      --timeout=60

**注意：** Make sure there is an empty line on the end of template files (press `ENTER` after last word). If there is no correct EOF (end of file) line, the AutoFS daemon will not properly load.

The optional parameter `timeout` sets the amount of seconds after which to unmount directories. 

The base directory will be created if it does not exist on your system. The base directory will be mounted on to load the dynamically loaded media, which means any content in the base directory will not be accessible while autofs is on. This procedure is however non-destructive, so if you accidentally automount into a live directory you can just change the location in `auto.master` and restart AutoFS to regain the original contents. 

If you still want to automount to a target non-empty directory and want to have the original files available even after the dynamically loaded directories are mounted, you can use autofs to mount them to another directory (e.g. /var/autofs/net) and create soft links. 
    
    # ln -s /var/autofs/net/share_name /media/share_name
    
Alternatively, you can have autofs mount your media to a specific folder, rather than inside a common folder. 
    
    /etc/autofs/auto.master
    
    /-     /etc/autofs/auto.template
    
    /etc/autofs/auto.template
    
    /path/to/folder     -options :/device/path
    /home/user/usbstick  -fstype=auto,async,nodev,nosuid,umask=000  :/dev/sdb1

**注意：** This can cause problems with resources getting locked if the connection to the share is lost. When trying to access the folder, programs will get locked into waiting for a response, and either the connection has to be restored or the process has to be forcibly killed before unmounting is possible. To mitigate this, only use if you will always be connected to the share, and do not use your home folder or other commonly used folders lest your file browser reads ahead into the disconnected folder

  * Open the file `/etc/nsswitch.conf` and add an entry for automount:

    automount: files
    
  * When you are done configuring your templates (see below), launch the AutoFS daemon as root by [enabling](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enabling") and starting the `autofs.service`.

Devices are now automatically mounted when they are accessed, they will remain mounted as long as you access them. 

### Removable media

  * Open `/etc/autofs/auto.misc` to add, remove or edit miscellaneous devices. For instance:

    /etc/autofs/auto.misc
    
    #kernel   -ro                                        ftp.kernel.org:/pub/linux
    #boot     -fstype=ext2                               :/dev/hda1
    usbstick  -fstype=auto,async,nodev,nosuid,umask=000  :/dev/sdb1
    cdrom     -fstype=iso9660,ro                         :/dev/cdrom
    #floppy   -fstype=auto                               :/dev/fd0
    
If you have a CD/DVD combo-drive you can change the `cdrom` line with `-fstype=auto` to have the media type autodetected. 

### NFS network mounts

AutoFS provides a new way of automatically discovering and mounting [NFS](<../zh-cn/NFS.html> "NFS")-shares on remote servers (the AutoFS network template in `/etc/autofs/auto.net` has been removed in autofs5). To enable automatic discovery and mounting of network shares from all accessible servers without any further configuration, you will need to add the following to the `/etc/autofs/auto.master` file: 
    
    /net -hosts --timeout=60
    
**Each host name needs to be resolveable, e.g. the name an IP address in`/etc/hosts` or via [DNS](<https://en.wikipedia.org/wiki/Domain_Name_System> "wikipedia:Domain Name System") and please make sure you have [nfs-utils](<https://archlinux.org/packages/?name=nfs-utils>)包 installed and working. You also have to enable RPC (systemctl start|enable rpcbind) to browse shared Folders.**

For instance, if you have a remote server _fileserver_ (the name of the directory is the hostname of the server) with an NFS share named _/home/share_ , you can just access the share by typing: 
    
    # cd /net/fileserver/home/share
    
**注意：** Please note that _ghosting_ , i.e. automatically creating directory placeholders before mounting shares is enabled by default, although AutoFS installation notes claim to remove that option from `/etc/conf.d/autofs` in order to start the AutoFS daemon.

The `-hosts` option uses a similar mechanism as the `showmount` command to detect remote shares. You can see the exported shares by typing: 
    
    # showmount <servername> -e 
    
Replacing _< servername>_ with the name of your own server. 

An alternative Way is to use the automount-service from Systemd, see [NFS with systemd-automount](<../zh-cn/NFS.html#Mount_using_/etc/fstab_with_systemd> "NFS")

#### Manual NFS configuration

To mount a NFS share on server_name called /srv/shared_dir to another computer named client_pc at location /mnt/foo, edit auto.master and create a config file for the share (auto.server_name): 
    
    /etc/autofs/auto.master
    
    /mnt   /etc/autofs/auto.server_name --timeout 60
    
    /etc/autofs/auto.server_name
    
    foo  -rw,soft,intr,rsize=8192,wsize=8192 server_name:/srv/shared_dir

### Samba

The Arch package does not provide any [Samba](<../zh-cn/Samba.html> "Samba") or CIFS templates/scripts (23.07.2009), but the following should work for single shares: 

Add the following to `/etc/autofs/auto.master`: 
    
    /media/[my_server] /etc/autofs/auto.[my_server] --timeout=60 --ghost
    
where `--timeout` defines how many seconds to wait before the file system is unmounted. The `--ghost` option creates empty folders for each mount-point in the file in order to prevent timeouts, if a network share cannot be contacted. 

Next create a file `/etc/autofs/auto.[my_server]`
    
    [any_name] -fstype=cifs,[other_options] ://[remote_server]/[remote_share_name]
    
You can specify a user name and password to use with the share in the `other_options` section: 
    
    [any_name] -fstype=cifs,username=[username],password=[password],[other_options] ://[remote_server]/[remote_share_name]
    
**注意：** Escape $, and other characters, with a backslash when neccessary.

###  FTP and SSH (with FUSE)

Remote FTP and [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") servers can be accessed seamlessly with AutoFS using [FUSE](<https://en.wikipedia.org/wiki/Filesystem_in_Userspace> "wikipedia:Filesystem in Userspace"), a virtual file system layer. 

#### Remote FTP

First, install the [curlftpfs](<https://archlinux.org/packages/?name=curlftpfs>)包 package. Load the **fuse** module: 
    
    # modprobe fuse
    
Create a `/etc/modules-load.d/fuse.conf` file containg `fuse` to load it on each system boot. 

Next, add a new entry for FTP servers in `/etc/autofs/auto.master`: 
    
    /media/ftp        /etc/autofs/auto.ftp    --timeout=60
    
Create the file `/etc/autofs/auto.ftp` and add a server using the `<ftp://myuser:mypassword@host:port/path>` format: 
    
    servername -fstype=curl,rw,allow_other,nodev,nonempty,noatime    :ftp\://myuser\:mypassword\@remoteserver
    
**注意：** Your passwords are plainly visible for anyone that can run `df` (only for mounted servers) or view the file `/etc/autofs/auto.ftp`.

If you want slightly more security you can create the file `~root/.netrc` and add the passwords there. Passwords are still plain text, but you can have mode 600, and `df` command will not show them (mounted or not). This method is also less sensitive to special characters (that else must be escaped) in the passwords. The format is: 
    
    machine remoteserver  
    login myuser
    password mypassword
    
The line in `/etc/autofs/auto.ftp` looks like this without user and password: 
    
    servername -fstype=curl,allow_other    :ftp\://remoteserver
    
Create the file `/sbin/mount.curl` with this code: 
    
    /sbin/mount.curl
    
     #! /bin/sh
     curlftpfs $1 $2 -o $4,disable_eprt
    
Create the file `/sbin/umount.curl` with this code: 
    
    /sbin/umount.curl
    
     #! /bin/sh
     fusermount -u $1
    
Set the permissions for both files: 
    
    # chmod 755 /sbin/mount.curl
    # chmod 755 /sbin/umount.curl
    
After a restart your new FTP server should be accessible through `/media/ftp/servername`. 

#### Remote SSH

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** All the _ssh*_ commands should be executed as the same user, as before [this edit](<https://wiki.archlinux.org/index.php?title=Autofs&diff=prev&oldid=318335>). It should not matter if it is root or unprivileged.（在 [Talk:Autofs](<../zh-cn/Talk:Autofs.html>) 中讨论）

These are basic instructions to access a remote filesystem over [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") with AutoFS. 

**注意：** Password-less authentication may be convenient but also has security implications. See [SSH keypair](<../zh-cn/Using_SSH_Keys.html> "Using SSH Keys") for more details

Install the [sshfs](<https://archlinux.org/packages/?name=sshfs>)包 package. 

Load the `fuse` module: 
    
    # modprobe fuse
    
Create a `/etc/modules-load.d/fuse.conf` file containg `fuse` to load it on each system boot if you have not one yet. 

Install [openssh](<https://archlinux.org/packages/?name=openssh>)包. 

Generate an [SSH keypair](<../zh-cn/Using_SSH_Keys.html> "Using SSH Keys"): 
    
    $ ssh-keygen
    
When the generator ask for a passphrase, just press `ENTER`. Using SSH keys without a passphrase is less secure, yet running AutoFS together with passphrases poses some additional difficulties which are not (yet) covered in this article. 

Next, copy the public key to the remote SSH server: 
    
    $ ssh-copy-id username@remotehost
    
**As root** , see that you can login to the remote server without entering a password: 
    
    # ssh username@remotehost
    
**注意：** This will add the remote server to root's list of `known_hosts`. Hosts can be also be manually added to `/etc/ssh/ssh_known_hosts`.

Create a new entry for SSH servers in `/etc/autofs/auto.master`: 
    
    /media/ssh		/etc/autofs/auto.ssh	--timeout=60
    
Create the file `/etc/autofs/auto.ssh` and add an SSH server: 
    
    /etc/autofs/auto.ssh
    
    servername     -fstype=fuse,rw,allow_other,IdentityFile=/home/username/.ssh/id_rsa :sshfs\#username@host\:/

After a restart your SSH server should be accessible through `/media/ssh/servername`. 

## MTP

Media Transfer Protocol ([MTP](<../zh-cn/%E5%AA%92%E4%BD%93%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE.html> "MTP")) is used in some Android devices. 

Install the [mtpfs](<https://archlinux.org/packages/?name=mtpfs>)包 package. 

Create a new entry for MTP Device in `/etc/autofs/auto.misc`: 
    
    android -fstype=fuse,allow_other,umask=000     :mtpfs
    
## Troubleshooting and tweaks

This section contains a few solutions for common issues with AutoFS. 

### Using NIS

Version 5.0.5 of AutoFS has more advanced support for [NIS](</wzh/index.php?title=NIS&action=edit&redlink=1> "NIS（页面不存在）"). To use AutoFS together with NIS, add `yp:` in front of the template names in `/etc/autofs/auto.master`: 
    
    /home   yp:auto_home    --timeout=60 
    /sbtn   yp:auto_sbtn    --timeout=60
    +auto.master
    
On earlier versions of NIS (before 5.0.4), you should add `nis` to `/etc/nsswitch.conf`: 
    
    automount: files nis
    
### Optional parameters

You can set parameters like `timeout` systemwide for all AutoFS media in `/etc/default/autofs`: 

  * Open the `/etc/default/autofs` file and edit the `OPTIONS` line:

    OPTIONS='--timeout=5'
    
  * To enable logging (default is no logging at all), uncomment and add `--verbose` to the `OPTIONS` line in `/etc/default/autofs` e.g.:

    OPTIONS='--verbose --timeout=5'
    
After restarting the `autofs` daemon, verbose output is visible in `systemctl status` or in `journalctl`. 

### Identify multiple devices

If you use multiple USB drives/sticks and want to easily tell them apart, you can use AutoFS to set up the mount points and [Udev](<../zh-cn/Udev.html> "Udev") to create distinct names for your USB drives. See [udev#Setting static device names](<../zh-cn/Udev.html#Setting_static_device_names> "Udev") for instructions on setting up Udev rules. 

### AutoFS permissions

If AutoFS is not working for you, make sure that the permissions of the templates files are correct, otherwise AutoFS will not start. This may happen if you backed up your configuration files in a manner which did not preserve file modes. Here are what the modes should be on the configuration files: 

  * 0644 - /etc/autofs/auto.master
  * 0644 - /etc/autofs/auto.media
  * 0644 - /etc/autofs/auto.misc
  * 0644 - /etc/conf.d/autofs

In general, scripts (like previous `auto.net`) should have executable (`chmod a+x filename`) bits set and lists of mounts should not. 

If you are getting errors in `/var/log/daemon.log` similar to this, you have a permissions problem: 
    
    May  7 19:44:16 peterix automount[15218]: lookup(program): lookup for petr failed
    May  7 19:44:16 peterix automount[15218]: failed to mount /media/cifs/petr
    
### fusermount problems

With certain versions of util-linux, you may not be able to unmount a fuse file system drive mounted by autofs, even if you use the "user=" option. See the discussion here: <http://fuse.996288.n3.nabble.com/Cannot-umount-as-non-root-user-anymore-tp689p697.html>

### Debugging auto mount issues

For better debugging you might try running automount in foreground. 
    
    # systemctl stop autofs.service
    # automount -f -v
    
Of if you want more debug info than try: 
    
    # automount -f --debug
    
## Alternatives to AutoFS

  * [Systemd](<../zh-cn/Systemd.html> "Systemd") can automount filesystems upon demand; see [here](<../zh-cn/Fstab.html#Automount_with_systemd> "Fstab") for the description and the article on [sshfs](<../zh-cn/SSHFS.html#On_demand> "SSHFS") for an example.
  * [Thunar Volume Manager](</wzh/index.php?title=Thunar_Volume_Manager&action=edit&redlink=1> "Thunar Volume Manager（页面不存在）") is an automount system for users of the [Thunar](<../zh-cn/Thunar.html> "Thunar") file manager.
  * [PCManFM](<../zh-cn/PCManFM.html> "PCManFM") is a lightweight file manager with built-in support for accessing remote shares
  * [Udisks](<../zh-cn/Udisks.html> "Udisks") is a minimalistic automatic disk mounting service

## See also

  * FTP and SFTP usage with AutoFS is based on this Gentoo Wiki article: <https://web.archive.org/web/20130414074212/http://en.gentoo-wiki.com/wiki/Mounting_SFTP_and_FTP_shares>
  * More information on SSH can be found on the [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") and [Using SSH Keys](<../zh-cn/Using_SSH_Keys.html> "Using SSH Keys") pages of this wiki.
  * Ubuntu's Autofs help wiki is at <https://help.ubuntu.com/community/Autofs>
  * [mount(8) § FILESYSTEM-INDEPENDENT MOUNT OPTIONS](<https://man.archlinux.org/man/mount.8#FILESYSTEM-INDEPENDENT_MOUNT_OPTIONS>)
  * For fuse specific mount options check <https://manpages.ubuntu.com/manpages/precise/man8/mount.fuse.8.html>
