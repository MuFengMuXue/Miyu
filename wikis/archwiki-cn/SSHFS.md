相关文章

  * [SCP and SFTP](<../zh-cn/SCP_and_SFTP.html> "SCP and SFTP")
  * [SFTP chroot](<../zh-cn/SFTP_chroot.html> "SFTP chroot")
  * [Pure-FTPd](</wzh/index.php?title=Pure-FTPd&action=edit&redlink=1> "Pure-FTPd（页面不存在）")
  * [Secure Shell (简体中文)](</wzh/index.php?title=Secure_Shell_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Secure Shell \(简体中文\)（页面不存在）")
  * [sftpman](</wzh/index.php?title=Sftpman&action=edit&redlink=1> "Sftpman（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [SSHFS](<https://wiki.archlinux.org/title/SSHFS> "arch:SSHFS")，最近一次同步于 2023-03-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/SSHFS?diff=0&oldid=768113>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SSHFS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 部分内容未翻译（在 [Talk:SSHFS#](<../zh-cn/Talk:SSHFS.html>) 中讨论）

[SSHFS](<https://github.com/libfuse/sshfs>) 是一个通过 [SSH](</wzh/index.php?title=Secure_Shell_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Secure Shell \(简体中文\)（页面不存在）") 挂载基于 FUSE 的文件系统的客户端程序。 

**注意：** 开发者已经停止开发此项目，[rclone](<https://archlinux.org/packages/?name=rclone>)包 提供了相同的挂载功能。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install")软件包 [sshfs](<https://archlinux.org/packages/?name=sshfs>)包。 

**提示：**

  * If you often need to mount sshfs filesystems you may be interested in using an sshfs helper, such as [qsshfs](<https://aur.archlinux.org/packages/qsshfs/>)AUR, [sftpman](</wzh/index.php?title=Sftpman&action=edit&redlink=1> "Sftpman（页面不存在）"), [sshmnt](<https://aur.archlinux.org/packages/sshmnt/>)AUR or [fmount.py](<https://github.com/lahwaacz/Scripts/blob/master/fmount.py>).
  * You may want to use [Google Authenticator](<../zh-cn/Google_Authenticator.html> "Google Authenticator") providing additional security as in two-step authentication.
  * [SSH keys](<../zh-cn/SSH_keys.html> "SSH keys") may be used over traditional password authentication.

###  挂载

只能挂载 SSH 用户可以访问的目录，用 _sshfs_ 挂载远程目录： 
    
    $ sshfs _[user@]host:[dir] mountpoint [options]_
    
示例: 
    
    $ sshfs myuser@mycomputer:/remote/path /local/path -C -p 9876
    
`-p 9876` 指定端口号，`-C` 启用压缩。 

未指定是默认挂载远程用户的主目录，默认的用户名和密码可以通过 `~/.ssh/config` 按主机进行配置，这样可以简化 _sshfs_ 命令。详情请参考 [OpenSSH#Client usage](<../zh-cn/OpenSSH.html#Client_usage> "OpenSSH")。 

需要密码时，SSH 会提示输入，如果不想一直手动输入，可以使用 [SSH keys](<../zh-cn/SSH_keys.html> "SSH keys")。 

###  卸载

要卸载远程系统: 
    
    $ fusermount3 -u _mountpoint_
    
例如: 
    
    $ fusermount3 -u /local/path
    
##  选项

_sshfs_ can automatically convert between local and remote user IDs. Use the `idmap=user` option to translate the UID of the connecting user to the remote user `myuser` (GID remains unchanged): 
    
    $ sshfs _myuser_ @_mycomputer_ :_/remote/path /local/path_ -o idmap=user
    
If you need more control over UID and GID translation, look at the options `idmap=file`, `uidfile` and `gidfile`. 

A complete list of options can be found in [sshfs(1)](<https://man.archlinux.org/man/sshfs.1>). 

## Chrooting

You may want to restrict a specific user to a specific directory on the remote system. This can be done by editing `/etc/ssh/sshd_config`: 
    
    /etc/ssh/sshd_config
    
    .....
    Match User _someuser_ 
           ChrootDirectory _/chroot/%u_
           ForceCommand internal-sftp
           AllowTcpForwarding no
           X11Forwarding no
    .....
    
**注意：** The chroot directory **must** be owned by root, otherwise you will not be able to connect.

See also [SFTP chroot](<../zh-cn/SFTP_chroot.html> "SFTP chroot"). For more information check the [sshd_config(5)](<https://man.archlinux.org/man/sshd_config.5>) man page for `Match`, `ChrootDirectory` and `ForceCommand`. 

## Automounting

Automounting can happen on boot, or on demand (when accessing the directory). For both, the setup happens in the [fstab](<../zh-cn/Fstab.html> "Fstab"). 

**注意：** Keep in mind that automounting is done through the root user, therefore you cannot use hosts configured in `.ssh/config` of your normal user. 

To let the root user use an SSH key of a normal user, specify its full path in the `IdentityFile` option. 

**And most importantly** , use each sshfs mount at least once manually **while root** on the client machine so the host's signature is added to the client's `/root/.ssh/known_hosts` file. This can also be done manually by appending one or more of the the SSH server's public host keys (the `/etc/ssh/ssh_host_*key.pub` files) to `/root/.ssh/known_hosts`. 

### On demand

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Is there a way to make this work with a passphrase-protected private key? E.g. it prompts for the passphrase at first access. Alternatively, clearly state that it is not possible and why. (在 [Talk:SSHFS](<../zh-cn/Talk:SSHFS.html>) 中讨论)

With systemd on-demand mounting is possible using `/etc/fstab` entries. 

Example: 
    
    _user_ @_host_ :_/remote/path /local/path_  fuse.sshfs noauto,x-systemd.automount,_netdev,users,idmap=user,IdentityFile=/home/_user_ /.ssh/id_rsa,allow_other,reconnect 0 0
    
The important mount options here are _noauto,x-systemd.automount,_netdev_. 

  * _noauto_ tells it not to mount at boot
  * _x-systemd.automount_ does the on-demand magic
  * __netdev_ tells it that it is a network device, not a block device (without it "No such device" errors might happen)

**注意：** After editing `/etc/fstab`, [reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") the systemd configuration and the required services, which can be found by running `systemctl list-unit-files --type automount`

### On boot

An example on how to use sshfs to mount a remote filesystem through `/etc/fstab`
    
    _user_ @_host_ :_/remote/path  /local/path_  fuse.sshfs  defaults,_netdev  0  0
    
Take for example the _fstab_ line 
    
    llib@192.168.1.200:/home/llib/FAH  /media/FAH2  fuse.sshfs  defaults,_netdev  0  0
    
The above will work automatically if you are using an SSH key for the user. See [Using SSH Keys](<../zh-cn/Using_SSH_Keys.html> "Using SSH Keys"). 

If you want to use sshfs with multiple users, add the following option: 
    
    user@domain.org:/home/user  /media/user   fuse.sshfs    defaults,**allow_other** ,_netdev    0  0
    
In order to ensure the network is available before trying to mount, it is not only important to set the `_netdev` mount option, but also to add either `--any` or a specific `--interface` to the appropriate [wait-online service](<../zh-cn/Systemd.html#Running_services_after_the_network_is_up> "Systemd") for your network manager. 

### Secure user access

When automounting via [fstab](<../zh-cn/Fstab.html> "Fstab"), the filesystem will generally be mounted by root. By default, this produces undesireable results if you wish access as an ordinary user and limit access to other users. 

An example mountpoint configuration: 
    
    _user_ @_host_ :_/remote/path /local/path_  fuse.sshfs noauto,x-systemd.automount,_netdev,user,idmap=user,follow_symlinks,identityfile=/home/_user_ /.ssh/id_rsa,allow_other,default_permissions,uid=USER_ID_N,gid=USER_GID_N 0 0
    
Summary of the relevant options: 

  * _allow_other_ \- Allow other users than the mounter (i.e. root) to access the share.
  * _default_permissions_ \- Allow kernel to check permissions, i.e. use the actual permissions on the remote filesystem. This allows prohibiting access to everybody otherwise granted by _allow_other_.
  * _uid_ , _gid_ \- set reported ownership of files to given values; _uid_ is the numeric user ID of your user, _gid_ is the numeric group ID of your user.

## Troubleshooting

### Checklist

Read [OpenSSH#Checklist](<../zh-cn/OpenSSH.html#Checklist> "OpenSSH") first. Further issues to check are: 

  1. Is your SSH login sending additional information from server's `/etc/issue` file e.g.? This might confuse SSHFS. You should temporarily deactivate server's `/etc/issue` file: 
         
         $ mv /etc/issue /etc/issue.orig

  2. Keep in mind that most SSH related troubleshooting articles you will find on the web are **not** systemd related. Often `/etc/fstab` definitions wrongly begin with 
         
         _sshfs#_ user@host:/mnt/server/directory ... fuse ...

instead of using the syntax 
         
         user@host:/mnt/server/directory ... fuse._sshfs_ ... _x-systemd_ , ...

  3. Check that the owner of server's source directory and content is owned by the server's user. 
         
         $ chown -R _user_s_ : /mnt/servers/directory

  4. The server's user ID can be different from the client's one. Obviously both user names have to be the same. You just have to care for the client's user IDs. SSHFS will translate the UID for you with the following mount options:
         
         uid=_USER_C_ID_ ,gid=_GROUP_C_ID_

  5. Check that the client's target mount point (directory) is owned by the client user. This directory should have the same user ID as defined in SSHFS's mount options.
         
         $ chown -R _user_c_ : /mnt/client/directory

  6. Check that the client's mount point (directory) is empty. By default you cannot mount SSHFS directories to non-empty directories.

### Connection reset by peer

  * If you are trying to access the remote system with a hostname, try using its IP address, as it can be a domain name resolving issue. Make sure you edit `/etc/hosts` with the server details.
  * Make sure your user can log into the server (especially when using `AllowUsers`).
  * Make sure `Subsystem sftp /usr/lib/ssh/sftp-server` is enabled in `/etc/ssh/sshd_config` on the remote system.
  * If you are using a non-default key name and passing it as `-i .ssh/my_key`, this will not work. You have to use `-o IdentityFile=/home/_user_ /.ssh/_my_key_`, with the full path to the key.
  * If your `/root/.ssh/config/` is a symlink, you will be getting this error as well. See [this serverfault topic](<https://serverfault.com/questions/507748/bad-owner-or-permissions-on-root-ssh-config>)
  * Adding the option `sshfs_debug` (as in `sshfs -o sshfs_debug _user_ @_server_ ...`) can help in resolving the issue.
  * If that does not reveal anything useful, you might also try adding the option `debug`.
  * If you are trying to sshfs into a router running DD-WRT or the like, there is a solution [here](<https://www.dd-wrt.com/wiki/index.php/SFTP_with_DD-WRT>). (Note that the `-osftp_server=/opt/libexec/sftp-server` option can be used to the sshfs command instead of patching dropbear).
  * If you see this only on boot, it may be that systemd is attempting to mount prior to a network connection being available. Enabling the appropriate [wait-online service](<../zh-cn/Systemd.html#Running_services_after_the_network_is_up> "Systemd") for your network manager fixes this.
  * Old Forum thread: [sshfs: Connection reset by peer](<https://bbs.archlinux.org/viewtopic.php?id=27613>).

**注意：** When providing more than one option for sshfs, they must be comma separated. Like so: `sshfs -o sshfs_debug,IdentityFile=_/path/to/key_ _user_ @_server_ ...`).

### Remote host has disconnected

If you receive this message directly after attempting to use _sshfs_ : 

  * First make sure that the **remote** machine has _sftp_ installed! It will not work, if not.
  * Then, check that the path of the `Subsystem sftp` in `/etc/ssh/sshd_config` on the remote machine is valid.

### fstab mounting issues

To get verbose debugging output, add the following to the mount options: 
    
    ssh_command=ssh\040-vv,sshfs_debug,debug
    
**注意：** Here, `\040` represents a space which fstab uses to separate fields.

To be able to run `mount -av` and see the debug output, remove the following: 
    
     noauto,x-systemd.automount
    
### Some directories are empty

sshfs by default does not support symlinks. If those directories happened to be symlinks, use: 
    
    $ sshfs _user_ @_host_ :_/remote/path /local/path_ -o follow_symlinks
    
### Files not refreshed

If you see old content on remote, consider using option `dir_cache=no`: 
    
    $ sshfs _user_ @_host_ :_/remote/path /local/path_ -o dir_cache=no
    
### Limited transfer on fast network

If you observe transfer than is lower than your network capabilities and high CPU usage on the party where files are copied from, disable compression (remove `-C` option or set `-o compression=no`). 

## See also

  * [How to mount chrooted SSH filesystem](<https://wiki.gilug.org/index.php/How_to_mount_SFTP_accesses>), with special care with owners and permissions questions.
