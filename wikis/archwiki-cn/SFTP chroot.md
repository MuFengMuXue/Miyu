**翻译状态：**

  * 本文（或部分内容）译自 [SFTP chroot](<https://wiki.archlinux.org/title/SFTP_chroot> "arch:SFTP chroot")，最近一次同步于 2022-10-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/SFTP_chroot?diff=0&oldid=748771>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SFTP_chroot_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [SSHFS](<../zh-cn/SSHFS.html> "SSHFS")

[OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH") 4.9+ 包含一个用于 SFTP 的内置 chroot，但需要对普通安装进行一些调整。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")并配置 [OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH")。运行后，确保 `sftp-server` 已正确设置： 
    
    /etc/ssh/sshd_config
    
    Subsystem sftp /usr/lib/ssh/sftp-server
    
使用 _sftp_ 或 [SSHFS](<../zh-cn/SSHFS.html> "SSHFS") 访问文件。许多标准的[FTP 客户端](<../zh-cn/List_of_applications/Internet.html#FTP_clients> "List of applications/Internet")也可能有用。 

##  配置

###  设置文件系统

**注意：**

  * 读者可以自行选择文件访问方案。例如，选择性地为一块传入（可写）空间和/或一块只读空间创建一个子文件夹。这不需要在 `/srv/ssh/jail`之下直接完成——它可以在 live 绑定挂载的磁盘分区完成。
  * 也可以 chroot 到 `/home` 目录从而跳过绑定，但是目标用户家目录应归属根：

    # chown root:root /home/<username>
    # chmod 0755 /home/<username>
    
绑定挂载要共享的 live [文件系统](</wzh/index.php?title=Filesystem&action=edit&redlink=1> "Filesystem（页面不存在）")到此目录。此例使用 `/mnt/data/share`，由[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "User") `root` 拥有并具有 `755 的八进制 [权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "Permissions") `： 
    
    # chown root:root /mnt/data/share
    # chmod 755 /mnt/data/share
    # mkdir -p /srv/ssh/jail
    # mount -o bind /mnt/data/share /srv/ssh/jail
    
将以下添加到 [fstab](<../zh-cn/Fstab.html> "Fstab") 以使绑定挂载在重新启动后不失效： 
    
    /mnt/data/share /srv/ssh/jail  none   bind   0   0
    
###  创建一个无特权用户

**注意：** 您无需创建一个组，可以使用 `Match User` 以代替 `Match Group`。

创建 `sftponly` [用户组](<../zh-cn/User_group.html> "User group"): 
    
    # groupadd sftponly 
    
创建一个使用 _sftponly_ 作为主要组的[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "User")并且 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell") 登录访问被拒: 
    
    # useradd -g sftponly -s /usr/bin/nologin -d _/srv/ssh/jail_ _username_
    
设置一个（复杂的）密码以防止 `account is locked` 错误（即使使用密钥验证也可能出现）： 
    
    # passwd _username_
    
###  配置 OpenSSH

**注意：** 您可能想使用 `Match User` 而不是 `Match Group`，如上一步所述。
    
    /etc/ssh/sshd_config
    
    Subsystem sftp /usr/lib/ssh/sftp-server
    
    Match Group sftponly
      ChrootDirectory %h
      ForceCommand internal-sftp
      AllowTcpForwarding no
      X11Forwarding no
      PasswordAuthentication no
    
[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `sshd.service` 以应用更改。 

####  为 authorized_keys 修复路径

**提示：** 在`(pre)auth`错误的情况下，在客户端和服务器上使用 OpenSSH 的 [调试模式](<../zh-cn/SSH_keys.html#Key_ignored_by_the_server> "SSH keys")。

应用 _AuthorizedKeysFile_ 的标准路径时，已 chroot 的用户 [SSH 密钥](<../zh-cn/SSH_keys.html> "SSH keys")验证会失败。欲修复此问题，[附加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append")一个 _AuthorizedKeysFile_ 上的属于根的目录到 `/etc/openssh/sshd_config`，以 `/etc/ssh/authorized_keys` 为例: 
    
    /etc/ssh/sshd_config
    
    AuthorizedKeysFile _/etc/ssh/authorized_keys/%u_ .ssh/authorized_keys
    PermitRootLogin no
    PasswordAuthentication no
    PermitEmptyPasswords no
    Subsystem sftp /usr/lib/ssh/sftp-server
    
创建 _authorized_keys_ 文件夹，在客户端生成一个 [SSH 密钥](<../zh-cn/SSH_keys.html#Choosing_the_key_location_and_passphrase> "SSH keys")，[复制](<../zh-cn/SSH_keys.html#Manual_method> "SSH keys")服务器密钥 `/etc/ssh/authorized_keys`（或任何其他首选方法）的内容并[设置正确的权限](<../zh-cn/SSH_keys.html#Key_ignored_by_the_server> "SSH keys"): 
    
    # mkdir /etc/ssh/authorized_keys
    # chown root:root /etc/ssh/authorized_keys
    # chmod 755 /etc/ssh/authorized_keys
    # echo 'ssh-rsa <key> <username@host>' >> _/etc/ssh/authorized_keys/username_
    # chmod 644 /etc/ssh/authorized_keys/_username_
    
[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `sshd.service`. 

##  技巧提示

###  写权限

[绑定](<#%E8%AE%BE%E7%BD%AE%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>)需要路径完全归属 `root`，但文件和/或子文件夹不需要。 以下示例中，[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "User") _www-demo_ 以 `/srv/ssh/www/demo` 作为 jail 目录: 
    
    # mkdir /srv/ssh/www/demo/public_html
    # chown www-demo:sftponly /srv/ssh/www/demo/public_html
    # chmod 755 /srv/ssh/www/demo/public_html
    
用户现在应可在此目录中创建文件/子目录。欲详细信息，请参阅[文件权限和属性](<../zh-cn/File_permissions_and_attributes.html> "File permissions and attributes")。 

###  仅允许上传

欲仅允许通过 sftp 上传并禁止下载文件，修改 `ForceCommand internal-sftp` 行： 

    /etc/ssh/sshd_config
    
    Match Group sftponly
    	
      ForceCommand internal-sftp -u 0666 -p realpath,open,write,close,lstat
    	
###  日志

用户无法访问 `/dev/log`。当用户连入并尝试下载该文件，即可通过于进程上运行 `strace` 以见此。 

####  创建子目录

在 `ChrootDirectory` 中创建子目录 `dev`，例如： 
    
    # mkdir /usr/local/chroot/user/dev
    # chmod 755 /usr/local/chroot/user/dev
    
现在您应于 `/usr/local/chroot/user/dev/log` 创建被 openssh 接受的套接字。您可以直接将该套接字与 `/dev/log` 或 `/run/systemd/journal/dev-log`（若您使用 journald）绑定或用 `syslog-ng`/`rsyslog` 创建。 

####  绑定 journald
    
    # touch /usr/local/chroot/user/dev/log
    # mount --bind /run/systemd/journal/dev-log /usr/local/chroot/user/dev/log
    
####  Syslog-ng 配置

添加新源到 `/etc/syslog-ng/syslog-ng.conf` 日志的并添加配置，例如修改段： 
    
    source src {
      unix-dgram("/dev/log");
      internal();
      file("/proc/kmsg");
    };
    
成为： 
    
    source src {
      unix-dgram("/dev/log");
      internal();
      file("/proc/kmsg");
      unix-dgram("/usr/local/chroot/theuser/dev/log");
    };
    
并附加： 
    
    #sftp configuration
    destination sftp { file("/var/log/sftp.log"); };
    filter f_sftp { program("internal-sftp"); };
    log { source(src); filter(f_sftp); destination(sftp); };
    
（可选）如果您想将 SSH 消息类似地记录到其自身的文件中： 
    
    #sshd configuration
    destination ssh { file("/var/log/ssh.log"); };
    filter f_ssh { program("sshd"); };
    log { source(src); filter(f_ssh); destination(ssh); };
    
（来自 [Syslog-ng#Move log to another file](</wzh/index.php?title=Syslog-ng&action=edit&redlink=1> "Syslog-ng（页面不存在）")） 

####  OpenSSH 配置

编辑 `/etc/ssh/sshd_config` 以替换所有 `internal-sftp` 的实例为 `internal-sftp -f AUTH -l VERBOSE`。 

####  重启服务

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `syslog-ng` 与 `sshd` 服务。 

`/usr/local/chroot/theuser/dev/log` 现应存在。 

##  SFTP 的替代品

###  安全复制协议 (SCP)

[openssh](<https://archlinux.org/packages/?name=openssh>)包 提供 _scp_ 命令来传输文件。SCP 可能比使用 SFTP 更快 [[1]](<https://superuser.com/questions/134901/whats-the-difference-between-scp-and-sftp>). 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [rssh](<https://aur.archlinux.org/packages/rssh/>)AUR 或 [scponly](<https://archlinux.org/packages/?name=scponly>)包 作为替代 shell 解决方案。 

####  只使用 SCP (Scponly)

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [scponly](<https://archlinux.org/packages/?name=scponly>)包. 

对于现有用户，只需将用户的 shell 设置为 scponly： 
    
    # usermod -s /usr/bin/scponly _username_
    
参见 [Scponly 维基](<https://github.com/scponly/scponly/wiki>)以获得更多细节。 

####  添加 chroot jail

该软件包附带一个用于创建 chroot 的脚本。要使用它，请运行： 
    
    # /usr/share/doc/scponly/setup_chroot.sh
    
  * 提供答案。
  * 核实 `/path/to/chroot` 属于 `root:root` 和有对于其他用户的 `r-x`。
  * 将所选用户的 shell 更改为 `/usr/bin/scponlyc`。
  * sftp 服务器 可能请求一些 libnss 模块例如 libnss_files。将它们复制到 chroot 的 `/lib` 路径。

##  参见

  * <https://www.minstrel.org.uk/papers/sftp/>
  * [sshd_config(5)](<https://man.archlinux.org/man/sshd_config.5>)
