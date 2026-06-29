**翻译状态：**

  * 本文（或部分内容）译自 [Systemd/Journal](<https://wiki.archlinux.org/title/Systemd/Journal> "arch:Systemd/Journal")，最近一次同步于 2023-02-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemd/Journal?diff=0&oldid=767038>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Journal_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

主文档请参考 [systemd](<../../zh-cn/Systemd.html> "Systemd")。 

_systemd_ 提供了自己的日志系统（logging system），称为 journal。使用 systemd 日志，无需额外安装日志服务（syslog）。使用 [journalctl(1)](<https://man.archlinux.org/man/journalctl.1>) 命令读取日志。 

Arch Linux 中， `/var/log/journal/` 目录是 [systemd](<https://archlinux.org/packages/?name=systemd>)包 软件包的一部分。默认情况下 `/etc/systemd/journald.conf` 中的`Storage=` 为 `auto`，systemd 会将日志记录写入 `/var/log/journal`。若被删除，systemd **不会** 自动创建此目录，而是将日志写入 `/run/log/journal`，重启时内容会消失。如果 `journald.conf` 中的 `Storage=persistent`， `systemd-journald.service` [重启](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启")或系统重启时会重新创建 `/var/log/journal/`。 

Systemd 日志可以按照[#优先级](<#%E4%BC%98%E5%85%88%E7%BA%A7>)和[#功能](<#%E5%8A%9F%E8%83%BD>)标记日志，符合 [syslog](<https://en.wikipedia.org/wiki/Syslog> "wikipedia:Syslog") 协议 ([RFC 5424](<https://tools.ietf.org/html/rfc5424> "rfc:5424")) 标准。 

**提示：** 如果 `/var/log/journal/` 位于 [btrfs](<../../zh-cn/Btrfs.html> "Btrfs") 文件系统，应该考虑对这个目录禁用写入时复制，方法参阅 [Btrfs#Copy-on-Write (CoW)](<../../zh-cn/Btrfs.html#Copy-on-Write_\(CoW\)> "Btrfs")。

##  优先级

日志会带 syslog 优先级代码，标记消息的重要性，参考 [RFC 5424 6.2.1](<https://tools.ietf.org/html/rfc5424#section-6.2.1> "rfc:5424")。 

数值 | 优先级 | 关键字 | 描述 | 示例   
---|---|---|---|---  
0 | Emergency | emerg | System is unusable | Severe Kernel BUG, [systemd dumped core](</wzh/index.php?title=Systemd-coredump&action=edit&redlink=1> "Systemd-coredump（页面不存在）").  
This level should not be used by applications.   
1 | Alert | alert | Should be corrected immediately | Vital subsystem goes out of work. Data loss.   
`kernel: BUG: unable to handle kernel paging request at ffffc90403238ffc`.   
2 | Critical | crit | Critical conditions | Crashes, coredumps. Like familiar flash:  
`systemd-coredump[25319]: Process 25310 (plugin-containe) of user 1000 dumped core`  
Failure in the system primary application, like X11.   
3 | Error | err | Error conditions | Not fatal error reported:  
`kernel: usb 1-3: 3:1: cannot get freq at ep 0x84`,  
`systemd[1]: Failed unmounting /var.`,  
`libvirtd[1720]: internal error: Failed to initialize a valid firewall backend`).   
4 | Warning | warning | May indicate that an error will occur if action is not taken. | A non-root file system has only 1GB free.  
`org.freedesktop. Notifications[1860]: (process:5999): Gtk-WARNING **: Locale not supported by C library. Using the fallback 'C' locale`.   
5 | Notice | notice | Events that are unusual, but not error conditions. |  `systemd[1]: var.mount: Directory /var to mount over is not empty, mounting anyway`. `gcr-prompter[4997]: Gtk: GtkDialog mapped without a transient parent. This is discouraged`.   
6 | Informational | info | Normal operational messages that require no action. |  `lvm[585]: 7 logical volume(s) in volume group "archvg" now active`.   
7 | Debug | debug | Messages which may need to be enabled first, only useful for debugging |  `kdeinit5[1900]: powerdevil: Scheduling inhibition from ":1.14" "firefox" with cookie 13 and reason "screen"`  
  
These rules are recommendations, and the priority level of a given error is at the application developer's discretion. It is always possible that the error will be at a higher or lower level than expected. 

Examples: 

  * Info message: 
        
        pulseaudio[2047]: W: [pulseaudio] alsa-mixer.c: Volume element Master has 8 channels. That's too much! I can't handle that!

It is an warning or error by definition.
  * Plaguing alert message: 
        
        sudo[21711]:     user : a password is required ; TTY=pts/0 ; PWD=/home/user ; USER=root ; COMMAND=list /usr/bin/pacman --color auto -Sy

The [reason](<https://bbs.archlinux.org/viewtopic.php?id=184455>) \- user was manually added to sudoers file, not to wheel group, which is arguably normal action, but sudo produced an alert on every occasion.

##  功能

日志文件会带上 syslog 功能码，标记发出日志的程序类型 [RFC 5424 6.2.1](<https://tools.ietf.org/html/rfc5424#section-6.2.1> "rfc:5424")。 

功能码 | 关键字 | 描述 | 信息   
---|---|---|---  
0 | kern | kernel messages   
1 | user | user-level messages   
2 | mail | mail system | Archaic POSIX still supported and sometimes used system, for more [mail(1)](<https://man.archlinux.org/man/mail.1>))   
3 | daemon | system daemons | All daemons, including systemd and its subsystems   
4 | auth | security/authorization messages | Also watch for different facility 10   
5 | syslog | messages generated internally by syslogd | As it standartized for syslogd, not used by systemd (see facility 3)   
6 | lpr | line printer subsystem (archaic subsystem)   
7 | news | network news subsystem (archaic subsystem)   
8 | uucp | UUCP subsystem (archaic subsystem)   
9 |  | clock daemon | systemd-timesyncd   
10 | authpriv | security/authorization messages | Also watch for different facility 4   
11 | ftp | FTP daemon   
12 | - | NTP subsystem   
13 | - | log audit   
14 | - | log alert   
15 | cron | scheduling daemon   
16 | local0 | local use 0 (local0)   
17 | local1 | local use 1 (local1)   
18 | local2 | local use 2 (local2)   
19 | local3 | local use 3 (local3)   
20 | local4 | local use 4 (local4)   
21 | local5 | local use 5 (local5)   
22 | local6 | local use 6 (local6)   
23 | local7 | local use 7 (local7)   
  
So, useful facilities to watch: 0,1,3,4,9,10,15. 

##  过滤输出

`journalctl`可以根据特定字段过滤输出。如果过滤的字段比较多，需要较长时间才能显示出来。 

示例： 

  * 显示 `_PATTERN_` 模式的日志: 
        
        # journalctl --grep=_PATTERN_

  * 显示本次启动后的所有日志：
        
        # journalctl -b

  * `journalctl -b -0` 显示本次启动的信息
  * `journalctl -b -1` 显示上次启动的信息
  * `journalctl -b -2` 显示上上次启动的信息 `journalctl -b -2`
  * 只显示错误、冲突和重要告警信息 
        
        # journalctl -p err..alert

也可以使用数字， `journalctl -p 3..1`。If single number/keyword used, `journalctl -p 3` \- all higher priority levels also included.
  * 包含日志消息类型的描述：
        
        # journalctl -x

注意在报告 bug 和寻求帮助时不要使用此命令，因为这个命令会产生大量的输出。用 `journalctl --list-catalog` 可以查看所有类型的描述。
  * 显示从某个日期 ( 或时间 ) 开始的消息: 
        
        # journalctl --since="2012-10-30 18:17:16"

  * 显示从某个时间 ( 例如 20分钟前 ) 的消息: 
        
        # journalctl --since "20 min ago"

  * 显示最新信息
        
        # journalctl -f

  * 显示特定程序的所有消息: 
        
        # journalctl /usr/lib/systemd/systemd

  * 显示特定进程的所有消息: 
        
        # journalctl _PID=1

  * 显示指定单元的所有消息：
        
        # journalctl -u man-db.service

  * Show all messages from user services by a specific unit: 
        
        $ journalctl --user -u dbus

  * 显示内核环缓存消息r: 
        
        # journalctl -k

  * Show auth.log equivalent by filtering on syslog facility: 
        
        # journalctl -f -l SYSLOG_FACILITY=10

  * If your journal directory (by default located under `/var/log/journal`) contains huge amount of log data then `journalctl` can take several minutes in filtering output. You can speed it up significantly by using `--file` option to force `journalctl` to look only into most recent journal: 
        
        # journalctl --file /var/log/journal/*/system.journal -f

详情参阅[journalctl(1)](<https://man.archlinux.org/man/journalctl.1>)、[systemd.journal-fields(7)](<https://man.archlinux.org/man/systemd.journal-fields.7>)，以及 Lennert 的这篇[博文](<http://0pointer.de/blog/projects/journalctl.html>)。 

  * By default, _journalctl_ truncates lines longer than screen width, but in some cases, it may be better to enable wrapping instead of truncating. This can be controlled by the `SYSTEMD_LESS` [environment variable](<../../zh-cn/Environment_variable.html> "Environment variable"), which contains options passed to [less](<../../zh-cn/Core_utilities.html#Essentials> "Core utilities") (the default pager) and defaults to `FRSXMK` (see [less(1)](<https://man.archlinux.org/man/less.1>) and [journalctl(1)](<https://man.archlinux.org/man/journalctl.1>) for details).

    By omitting the `S` option, the output will be wrapped instead of truncated. For example, start _journalctl_ as follows: 
    
    $ SYSTEMD_LESS=FRXMK journalctl

    To set this behaviour as default, [export](<../../zh-cn/Environment_variables.html#Per_user> "Environment variables") the variable from `~/.bashrc` or `~/.zshrc`.

  * While the journal is stored in a binary format, the content of stored messages is not modified. This means it is viewable with _strings_ , for example for recovery in an environment which does not have _systemd_ installed, e.g.:{{bc|$ strings /mnt/arch/var/log/journal/af4967d77fba44c6b093d0e9862f6ddd/system.journal | grep -i _message_

##  日志大小限制

如果按上面的操作保留日志的话，默认日志最大限制为所在文件系统容量的 10%，即：如果 `/var/log/journal` 储存在 50GiB 的根分区中，那么日志最多存储 5GiB 数据。用 `systemd-journald` 日志查看当前设置: 
    
    # journalctl -b -u systemd-journald
    
可以修改配置文件指定最大限制。如限制日志最大 50MiB： 
    
    /etc/systemd/journald.conf
    
    SystemMaxUse=50M

还可以通过配置片段而不是全局配置文件进行设置： 
    
    /etc/systemd/journald.conf.d/00-journal-size.conf
    
    [Journal]
    SystemMaxUse=50M

修改配置后要立即生效，请[重启](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `systemd-journald.service` 服务。 

详情参见 [journald.conf(5)](<https://man.archlinux.org/man/journald.conf.5>). 

##  配合 syslog 使用

systemd 提供了 socket `/run/systemd/journal/syslog`，以兼容传统日志服务。所有系统信息都会被传入。要使传统日志服务工作，需要让服务链接该 socket，而非 `/dev/log`（[官方说明](<https://lwn.net/Articles/474968/>)）。Arch 软件仓库中的 [syslog-ng](<https://archlinux.org/packages/?name=syslog-ng>)包 已经包含了需要的配置。 

`journald.conf` 使用 `no` 转发socket . 为了使 _syslog-ng_ 配合 _journald_ , 你需要在 `/etc/systemd/journald.conf` 中设置 `ForwardToSyslog=yes` . 参阅 [Syslog-ng#Overview](</wzh/index.php?title=Syslog-ng&action=edit&redlink=1> "Syslog-ng（页面不存在）") 了解更多细节. 

如果你选择使用 [rsyslog](<https://aur.archlinux.org/packages/rsyslog/>)AUR , 因为 [rsyslog](</wzh/index.php?title=Rsyslog&action=edit&redlink=1> "Rsyslog（页面不存在）") 从日志中[直接](<https://lists.freedesktop.org/archives/systemd-devel/2014-August/022295.html#journald>)传出消息,所以不再必要改变那个选项.. 

设置开机启动 syslog-ng： 
    
     # systemctl enable syslog-ng
    
[这里](<http://0pointer.de/blog/projects/>)有一份很不错的 `journalctl` 指南。 

### Per unit size limit by a journal namespace

[Edit](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") the unit file for the service you wish to configure (for example sshd) and add `LogNamespace=ssh` in the `[Service]` section. 

Then create `/etc/systemd/journald@ssh.conf` by copying `/etc/systemd/journald.conf`. After that, edit `journald@ssh.conf` and adjust `SystemMaxUse` to your liking. 

[Restart](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart")ing the service should automatically start the new journal service `systemd-journald@ssh.service`. The logs from the namespaced service can be viewed with `journalctl --namespace ssh`. 

See [systemd-journald.service(8) § JOURNAL NAMESPACES](<https://man.archlinux.org/man/systemd-journald.service.8#JOURNAL_NAMESPACES>) for details about journal namespaces. 

##  手动清理日志

`/var/log/journal` 存放着日志, `rm` 应该能工作. 或者使用`journalctl`, 

例如: 

  * 清理日志使总大小小于 100M: 
        
        # journalctl --vacuum-size=100M

  * 清理最早两周前的日志. 
        
        # journalctl --vacuum-time=2weeks

Journal files must have been rotated out and made inactive before they can be trimmed by vacuum commands. Rotation of journal files can be done by running `journalctl --rotate`. The `--rotate` argument can also be provided alongside one or more vacuum criteria arguments to perform rotation and then trim files in a single command. 

参阅 [journalctl(1)](<https://man.archlinux.org/man/journalctl.1>) 获得更多信息. 

##  转发 journald 到 /dev/tty12

建立一个 [Systemd#替换单元文件](<../../zh-cn/Systemd.html#%E6%9B%BF%E6%8D%A2%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")|drop-in directory]] `/etc/systemd/journald.conf.d` 然后在其中建立 `fw-tty12.conf` : 
    
    /etc/systemd/journald.conf.d/fw-tty12.conf
    
    [Journal]
    ForwardToConsole=yes
    TTYPath=/dev/tty12
    MaxLevelConsole=info

然后重新启动 systemd-journald. 

##  查看特定位置的日志

有时你希望查看另一个系统上的日志.例如从 Live 环境修复现存的系统. 

这种情况下你可以挂载目标系统 ( 例如挂载到 `/mnt` ),然后用 `-D`/`--directory` 参数指定目录,例如: 
    
    # journalctl -D _/mnt_ /var/log/journal -n 1000
    
##  普通用户访问日志

在默认的配置中，普通用户仅能访问自己的日志，要让普通用户访问系统日志，可以将用户加入 `systemd-journal` [用户组](<../../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户和用户组")。`adm` 和 `wheel` 组中的用户也可以读取日志。 

更多信息请参考 [journalctl(1) § DESCRIPTION](<https://man.archlinux.org/man/journalctl.1#DESCRIPTION>) 和[用户和用户组#用户组管理](<../../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户和用户组")。 
