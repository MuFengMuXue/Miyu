相关文章

  * [SSHFS](<../zh-cn/SSHFS.html> "SSHFS")
  * [SFTP chroot](<../zh-cn/SFTP_chroot.html> "SFTP chroot")
  * [Pure-FTPd](</wzh/index.php?title=Pure-FTPd&action=edit&redlink=1> "Pure-FTPd（页面不存在）")

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[SFTP chroot](<../zh-cn/SFTP_chroot.html> "SFTP chroot")。**

**附注：** Instructions seem to be the same as in [SFTP chroot](<../zh-cn/SFTP_chroot.html> "SFTP chroot") and has more content.（在 [Talk:SCP 与 SFTP#Incorrect 'Considered for redirection' banner?](</wzh/index.php?title=Talk:SCP_%E4%B8%8E_SFTP&action=edit&redlink=1> "Talk:SCP 与 SFTP（页面不存在）") 中讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [SCP and SFTP](<https://wiki.archlinux.org/title/SCP_and_SFTP> "arch:SCP and SFTP")，最近一次同步于 2024-09-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/SCP_and_SFTP?diff=0&oldid=815869>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SCP_and_SFTP_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

The [Secure copy (SCP)](<https://en.wikipedia.org/wiki/Secure_copy> "wikipedia:Secure copy") is a protocol to transfer files via a [Secure Shell](<../zh-cn/Secure_Shell.html> "Secure Shell") connection. The [SSH file transfer protocol (SFTP)](<https://en.wikipedia.org/wiki/SSH_file_transfer_protocol> "wikipedia:SSH file transfer protocol") is a related protocol, also relying on a secure shell back-end. Both protocols allow secure file transfers, encrypting passwords and transferred data. The SFTP protocol, however, features additional capabilities like, for example, resuming broken transfers or remote file manipulation like deletion. 

##  Secure file transfer protocol (SFTP)

Install and configure [OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH"). Once running, SFTP is available by default. 

Access files with the _sftp_ program or [SSHFS](<../zh-cn/SSHFS.html> "SSHFS"). Many standard FTP programs should work as well. 

##  Secure file transfer protocol (SFTP) with a chroot jail

Sysadmins can jail a subset of users to a chroot jail using [openssh](<https://archlinux.org/packages/?name=openssh>)包 thus restricting their access to a particular directory tree. This can be useful to simply share some files without granting full system access or shell access. Users with this type of setup may use SFTP clients such as [filezilla](<https://archlinux.org/packages/?name=filezilla>)包 to put/get files in the chroot jail. 

### Setup the filesystem

Create a jail directory: 
    
    # mkdir -p /var/lib/jail
    
Optionally, bind mount the filesystem to be shared to this directory. In this example, `/mnt/data/share` is to be used. It is owned by root and has octal permissions of 755. 
    
    # mount -o bind /mnt/data/share /var/lib/jail
    
**提示：** Consider adding an entry to `/etc/fstab` to make the bind mount survive a reboot.

### Create an unprivileged user

Create the share user and setup a good password: 
    
    # useradd -g sshusers -d /var/lib/jail foo
    # passwd foo
    
### Setup OpenSSH

Add the following to the end of `/etc/ssh/sshd_config` to enable the share and to enforce the restrictions: 
    
    /etc/ssh/sshd_config
    
    ...
     Match group sshusers
      ChrootDirectory %h
      X11Forwarding no
      AllowTcpForwarding no
      PasswordAuthentication yes
      ForceCommand internal-sftp
    
[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `sshd.service` to re-read the configuration file. See [SFTP chroot](<../zh-cn/SFTP_chroot.html> "SFTP chroot") to configure the keys correctly when using chroot or it will get permission denied. 

Test that in fact, the restrictions are enforced by attempting an ssh connection via the shell. The ssh server should return a polite notice of the setup: 
    
    $ ssh foo@someserver.com
    
    foo@someserver.com's password:
    This service allows sftp connections only.
    Connection to someserver.com closed.
    
##  Secure copy protocol (SCP)

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install"), configure and [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") [OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH"). It contains the _scp_ utility to transfer files. 

More features are available by installing additional packages, for example [rssh](<https://aur.archlinux.org/packages/rssh/>)AUR or [scponly](<https://archlinux.org/packages/?name=scponly>)包 described below. 

**注意：** Since OpenSSH 9.0 the _scp_ utility uses the SFTP protocol by default. The `-O` option must be used to use the legacy SCP protocol.

**警告：** The scp protocol is outdated, inflexible and not readily fixed. Its authors recommend the use of more modern protocols like sftp and rsync for file transfer instead.[[1]](<https://lists.mindrot.org/pipermail/openssh-unix-dev/2019-March/037672.html>)

### General Usage

#### Linux to Linux

Copy file from a remote host to local host SCP example: 
    
    $ scp username@from_host:file.txt /local/directory/
    
Copy file from local host to a remote host SCP example: 
    
    $ scp file.txt username@to_host:/remote/directory/
    
Copy directory from a remote host to local host SCP example: 
    
    $ scp -r username@from_host:/remote/directory/  /local/directory/
    
Copy directory from local host to a remote host SCP example: 
    
    $ scp -r /local/directory/ username@to_host:/remote/directory/
    
Copy file from remote host to remote host SCP example: 
    
    $ scp username@from_host:/remote/directory/file.txt username@to_host:/remote/directory/
    
#### Linux to Windows

Use a Windows program such as [WinSCP](<https://winscp.net/eng/download.php>)

### Scponly

[Scponly](<https://github.com/scponly/scponly/wiki>) is a limited shell for allowing users scp/sftp access and only scp/sftp access. Additionally, one can setup _scponly_ to chroot the user into a particular directory increasing the level of security. 

[install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [scponly](<https://archlinux.org/packages/?name=scponly>)包. 

For existing users, simply set the user's shell to scponly: 
    
    # usermod -s /usr/bin/scponly _username_
    
#### Adding a chroot jail

The package comes with a script to create a chroot. To use it, run: 
    
    # /usr/share/doc/scponly/setup_chroot.sh
    
  * Provide answers
  * Check that `/path/to/chroot` has `root:root` owner and `r-x` for others
  * Change the shell for selected user to `/usr/bin/scponlyc`
  * sftp-server may require some libnss modules such as libnss_files. Copy them to chroot's `/lib` path.

#### Uploads to Chroot jail root dir

For security reasons the directory set as the chroot directory must be owned by root with only root having write access to it otherwise sftp/ssh connections will be denied. This of course means regular users cannot upload files to the root directory. In order to get around this while not compromising security you can create a folder inside the chroot directory which the regular user or group has write access to, e.g: 
    
    # cd /var/lib/jail
    # mkdir uploads
    # chown :sshusers uploads
    # chmod 730 uploads
    
**注意：** This will only allow users of group "sshusers" to upload to (but not list the contents of) the "uploads" directory. Use `chmod 770` to allow sshusers to view contents.

Some applications utilizing SFTP do not allow input of sub-directories when performing operations (e.g. uploading files), and will attempt to upload files to the chroot base directory (which will be denied). In order to force these applications to use a specific sub-directory you can append the following to the "ForceCommand" option: 
    
    /etc/ssh/sshd_config
    
    ...
     Match group sshusers
      ...
      ForceCommand internal-sftp -d /uploads
    
Users on connect will then have their start directory change to the specified sub-directory (remember to restart the sshd server). 
