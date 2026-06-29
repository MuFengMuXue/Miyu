**翻译状态：**

  * 本文（或部分内容）译自 [Systemd](<https://wiki.archlinux.org/title/Systemd> "arch:Systemd")，最近一次同步于 2025-01-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemd?diff=0&oldid=825689>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")
  * [systemd/定时器](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/定时器")
  * [systemd/日志](<../zh-cn/Systemd/Journal.html> "Systemd/日志")
  * [Systemd/FAQ](<../zh-cn/Systemd/FAQ.html> "Systemd/FAQ")
  * [init](<../zh-cn/Init.html> "Init")
  * [守护程序](<../zh-cn/Systemd.html> "守护程序")
  * [udev](<../zh-cn/Udev.html> "Udev")
  * [性能优化/启动过程](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96/%E5%90%AF%E5%8A%A8%E8%BF%87%E7%A8%8B.html> "性能优化/启动过程")
  * [允许用户关机](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86.html#%E5%85%81%E8%AE%B8%E7%94%A8%E6%88%B7%E5%85%B3%E6%9C%BA> "允许用户关机")

摘自[项目主页](<https://systemd.io/>)： 

     _systemd_ 是一个 Linux 系统基础组件的集合，提供了一个系统和服务管理器，运行为 PID 1 并负责启动其它程序。功能包括：支持并行化任务；同时采用 socket 式与 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 总线式启用服务；按需启动守护进程（daemon）；利用 Linux 的 [cgroups](<../zh-cn/%E6%8E%A7%E5%88%B6%E7%BB%84.html> "Cgroups") 监视进程；支持快照和系统恢复；维护挂载点和自动挂载点；各服务间基于依赖关系进行精密控制。 _systemd_ 支持 SysV 和 LSB 初始脚本，可以替代 sysvinit。除此之外，功能还包括日志进程、控制基础系统配置，维护登录用户列表以及系统账户、运行时目录和设置，可以运行容器和虚拟机，可以简单的管理网络配置、网络时间同步、日志转发和名称解析等。

在历史上，systemd中的“服务”（service）被称作[守护进程（daemon）](<https://en.wikipedia.org/wiki/Daemon_\(computing\)> "wikipedia:Daemon \(computing\)")，它们在后台运行（即没有UI、不与终端交互），等待特定事件的发生并提供服务。例如，Web服务器会等待一个请求以提供相应的页面，SSH服务器会等待登录请求。除了这种提供完整功能的，还有一些守护进程的工作是隐藏在幕后的，如负责向日志文件写入消息的`syslog`、`metalog`，确保系统时间准确的[ntpd](<../zh-cn/Network_Time_Protocol_daemon.html> "Ntpd")。更多信息详见[daemon(7)](<https://man.archlinux.org/man/daemon.7>)。 

**注意：**[Arch Linux 论坛的这篇帖子](<https://bbs.archlinux.org/viewtopic.php?pid=1149530#p1149530>) 详细地解释了 Arch Linux 迁移到 systemd 的原因。

##  systemctl 基本用法

监视和控制 _systemd_ 的主要命令是 _systemctl_ 。其用途包括查看系统状态以及管理系统和服务。详见 [systemctl(1)](<https://man.archlinux.org/man/systemctl.1>)。 

**提示：**

  * 在 _systemctl_ 参数中添加 `-H _用户名_ @_主机名_` 可以远程控制其他机器。该功能使用 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 连接到远程的 _systemd_ 实例。
  * [Plasma](<../zh-cn/KDE.html> "Plasma") 用户可以安装 _systemctl_ 图形前端 [systemdgenie](<https://archlinux.org/packages/?name=systemdgenie>)包。安装后可以在 _系统管理_ 下找到。

###  使用单元

单元（unit）通常包括但不限于：服务（ _.service_ ）、挂载点（ _.mount_ ）、设备（ _.device_ ）和套接字（ _.socket_ ）。 

使用 _systemctl_ 时，通常需要使用单元文件的全名，包括扩展名（例如 `sshd.socket`）。不过在以下 _systemctl_ 命令中可以使用简写： 

  * 如果无扩展名，systemctl 会假定扩展名为 _.service_ 。例如，`netctl` 和 `netctl.service` 是等价的。
  * 挂载点会自动转化为相应的 _.mount_ 单元。例如，`/home` 等价于 `home.mount` 。
  * 与挂载点类似，设备会自动转化为相应的 _.device_ 单元，因此 `/dev/sda2` 等价于 `dev-sda2.device`。

详见 [systemd.unit(5)](<https://man.archlinux.org/man/systemd.unit.5>)。 

**注意：** 有一些单元的名称包含一个 `@` 符号（例如：`name@_string_.service` ），这意味着它是模板单元 `name@.service` 的一个 [实例](<https://0pointer.net/blog/projects/instances.html>)，模板单元的实际文件名中不包括 `_string_` 部分（如 `name@.service`）。` _string_` 被称作实例标识符，在 _systemctl_ 调用模板单元时，会将其当作一个参数传给模板单元，模板单元会使用这个传入的参数代替模板中的 `%i` 指示符。在启动单元时，尝试从模板单元实例化之前， _systemd_ 会先检查 `name@string.suffix` 文件是否存在。如果存在，就直接使用这个文件，而不是模板实例化（不过，这种“碰撞”非常少见）。大多数情况下，包含 `@` 标记都意味着这个文件是模板。如果一个模板单元被调用时没有指定实例标识符，该调用通常会失败，除非是在某些特殊的 _systemctl_ 命令（如`cat`）中使用。

因为调用 _systemctl_ 时默认了 `--system` 参数，下列命令默认对**系统单元** 进行操作。若要对（**调用用户** 的）**用户单元** 进行操作，则需在非root身份下执行[systemctl --user](<../zh-cn/Systemctl_--user.html> "Systemctl --user")。参看[systemd/用户#基础设置](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#%E5%9F%BA%E7%A1%80%E8%AE%BE%E7%BD%AE> "Systemd/用户")以为**所有用户** 启用或禁用单元。 

**提示：**

  * 下面的大部分命令都可以跟多个单元名，详细信息参见 [systemctl(1)](<https://man.archlinux.org/man/systemctl.1>)。
  * `--now` 选项可与 `enable`、`disable` 和 `mask` 同时使用，可使这些动作**立即** 生效，而非重启后生效。
  * 一个软件包可能会为不同的功能提供多个不同的单元。如果你刚安装了软件包，可以通过 `pacman -Qql _package_ | grep -Fe .service -e .socket` 命令检查这个软件包提供了哪些单元。

动作 | 命令 | 注释   
---|---|---  
分析系统状态   
**显示系统状态** | `systemctl status` |   
**列出正在运行的** 单元 |  `systemctl` 或  
`systemctl list-units` |   
**列出失败的** 单元 | `systemctl --failed` |   
**列出已安装的** 单元1 | `systemctl list-unit-files` |   
**显示特定PID对应进程的状态** | `systemctl status _pid_` |  [cgroup slice](<../zh-cn/%E6%8E%A7%E5%88%B6%E7%BB%84.html> "Cgroups")，内存占用，父进程   
检查单元状态   
显示单元的**手册页** | `systemctl help _单元_` | 如果单元支持   
显示单元的**状态** | `systemctl status _单元_` | 包括其是否在运行   
**检查** 单元是否配置为自动启动（enabled） | `systemctl is-enabled _单元_` |   
启动（start）、重新启动和重新加载单元   
立即**启动** 单元 | 以root身份执行`systemctl start _单元_` |   
立即**停止** 单元 | 以root身份执行`systemctl stop _单元_` |   
**重新启动** 单元 | 以root身份执行`systemctl restart _单元_` |   
**重新加载** 单元及其配置 | 以root身份执行`systemctl reload _单元_` |   
**重新加载 systemd** 配置2 | 以root身份执行`systemctl daemon-reload` | 扫描单元的变动   
启用（enable）单元   
**启用** 单元：开机时自动**启动** 该单元 | 以root身份执行`systemctl enable _单元_` |   
**启用** 单元，并立即**启动** 它 | 以root身份执行`systemctl enable --now _单元_` |   
**取消** 开机自动启动单元 | 以root身份执行`systemctl disable _单元_` |   
**重新启用** 单元3 | 以root身份执行`systemctl reenable _单元_` | 先取消启用，再启用   
屏蔽单元   
**屏蔽** 单元，使其无法启动4 | 以root身份执行`systemctl mask _单元_` |   
**取消屏蔽** 单元 | 以root身份执行`systemctl unmask _单元_` |   
  
  1. [systemd.unit(5) § UNIT FILE LOAD PATH](<https://man.archlinux.org/man/systemd.unit.5#UNIT_FILE_LOAD_PATH>) 中描述了查找单元文件的路径。
  2. 这不会要求已改变的单元重新加载自己的配置（见**重新加载** 动作）。
  3. 可在单元的`[Install]`节发生变更（在上一次启用后）时使用。
  4. 既不能手动启动，也无法作为依赖启动。因此屏蔽单元是危险的。 查看已屏蔽的单元：
         
         # systemctl list-unit-files --state=masked

###  电源管理

安装 [polkit](<../zh-cn/Polkit.html> "Polkit") 后才能以普通用户身份使用电源管理。如果你正登录在一个本地的 _systemd-logind_ 用户会话，且当前没有其它活动的会话，那么以下命令无需 root 权限即可执行。否则（例如，当前有另一个用户登录在某个 tty）， _systemd_ 将会自动请求输入 root 密码。 

动作 | 命令   
---|---  
重启 |  `systemctl reboot`  
关机 |  `systemctl poweroff`  
待机 |  `systemctl suspend`  
休眠（将内存写入硬盘） |  `systemctl hibernate`  
进入混合休眠模式（同时休眠到硬盘并待机） |  `systemctl hybrid-sleep`  
先待机，在一个特定时间唤醒后进入休眠模式 |  `systemctl suspend-then-hibernate`  
使用[#软重启](<#%E8%BD%AF%E9%87%8D%E5%90%AF>)来仅重启用户空间 |  `systemctl soft-reboot`  
  
####  软重启

软重启是一种不涉及内核，仅重启用户空间的重启操作。这个操作由 [systemd-soft-reboot.service(8)](<https://man.archlinux.org/man/systemd-soft-reboot.service.8>) 实现，并且可以通过 `systemctl soft-reboot` 来进行一次软重启。正如 [kexec](</wzh/index.php?title=Kexec&action=edit&redlink=1> "Kexec（页面不存在）") 一样，这个操作跳过了重新初始化固件，也不会进行内核初始化和初始化 RAM 文件系统。同时，未锁定的 [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt") 设备也将保持解锁状态。 

当 `/run/nextroot` 包含了一个合法的 rootfs 结构（比如说挂载了另一个发行版的根分区或者另一个快照）， _软重启操作_ 将会切换系统根分区到其中。切换之后并不会丢失一些由内核管理的状态，比如说[网络连接](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")。 

**提示：**`/run/nextroot/`不一定是一个挂载点或者存在于物理设备上。例如，它可以在 `/run/` tmpfs 中。 _systemd_ 将会在软重启时自动将`/run/nextroot/` 转化为一个挂载点。 

**注意：** 不要在涉及内核和 initramfs 的更新后执行 `systemctl soft-reboot`。

##  编写单元文件

`systemd` [单元文件](<https://www.freedesktop.org/software/systemd/man/systemd.unit.html>)的语法来源于[XDG 桌面项配置的.desktop文件](<../zh-cn/Desktop_entries.html> "Desktop entries")，最初的源头则是[Microsoft Windows的.ini文件](<https://en.wikipedia.org/wiki/INI_file> "wikipedia:INI file")。单元文件可以从多个地方加载，`systemctl show --property=UnitPath` 可以显示加载目录。主要的加载目录为（按优先级从低到高排列）： 

  * `/usr/lib/systemd/system/` ：软件包安装的单元
  * `/etc/systemd/system/` ：系统管理员安装的单元

**注意：**

  * 当 `systemd` 运行在[用户模式](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86> "Systemd/用户")下时，使用的加载路径是完全不同的。
  * systemd 单元名仅能包含 ASCII 字符，下划线和点号以及有特殊意义的字符('@', '-')。其它字符需要用C风格的"\x2d" 替换或使用对应的预定义语法（“@”，“-”）。参阅 [systemd.unit(5)](<https://man.archlinux.org/man/systemd.unit.5>) 和 [systemd-escape(1)](<https://man.archlinux.org/man/systemd-escape.1>) 。

单元文件的语法，可以参考系统已经安装的单元，也可以参考 [systemd.service(5) § EXAMPLES](<https://man.archlinux.org/man/systemd.service.5#EXAMPLES>)。 

**提示：** 在单元文件中以`#`开头的行将被视作注释，但`#`仅能在一行开头使用。不要在 _systemd_ 的参数后面使用行末注释，否则该单元将不能正常启动。

[systemd-analyze(1)](<https://man.archlinux.org/man/systemd-analyze.1>) 可以帮助你检查错误。请参见那一章节的 `systemd-analyze verify FILE...` 部分。 

###  处理依赖关系

使用 systemd 时，可通过正确编写单元配置文件来解决单元间的依赖关系。典型的情况是，**单元A** 要求**单元B** 在**A** 启动之前运行。在此情况下，可向**单元A** 配置文件中的 `[Unit]` 段添加 `Requires=_B_` 和 `After=_B_` 即可。若此依赖关系是可选的，可添加 `Wants=_B_` 和 `After=_B_`。请注意 `Wants=` 和 `Requires=` 并不暗含 `After=` ，即如果 `After=`选项没有指定，这两个单元将被并行启动。 

依赖关系通常被用在服务（service）而不是[目标（target）](<#%E7%9B%AE%E6%A0%87%EF%BC%88target%EF%BC%89>)上。例如，`network.target` 一般会被某个配置网络接口的服务引入作为依赖。所以，若要让自定义单元在系统到达`network.target`后再启动， 将自定义的单元排在该类配置网络接口的服务之后即可，因为该类服务启动时 `network.target` 一定已经启动。 

###  服务（service）类型

编写自定义的服务（service）文件时，可以选择几种不同的服务启动方式。启动方式可通过配置文件 `[Service]` 段中的 `Type=` 参数进行设置。 

  * `Type=simple` ：（默认值） systemd认为该服务将立即启动且服务进程不会fork。如果其他服务需要在此服务之后启动，请不要使用此类型，除非它是通过套接字激活的。
  * `Type=forking` ：systemd认为当该服务进程fork，且父进程退出后服务启动成功。对于典型的守护进程，除非你确定此启动方式无法满足需求，使用此类型启动即可。使用此启动类型应同时指定 `PIDFile=`，以便systemd能够跟踪服务的主进程。
  * `Type=oneshot` ：这一选项适用于只执行一项任务、随后立即退出的服务。可能需要同时设置 `RemainAfterExit=yes`使得systemd在服务进程退出之后仍然认为服务处于启用状态，这对于改变系统状态（如挂载分区）的单元尤其适用。对于 simple 和 oneshot 类型的区别，请参阅 [[1]](<https://trstringer.com/simple-vs-oneshot-systemd-service/>)。
  * `Type=notify` ：与 `Type=simple` 相同，但约定服务会在就绪后向systemd发送一个信号以通知systemd。这一通知的参考实现由 `libsystemd-daemon.so` 提供。
  * `Type=dbus` ：若以此方式启动，当指定的 `BusName` 出现在DBus系统总线上时，systemd认为服务就绪。
  * `Type=idle` ：`systemd`会等待所有活动任务都完成后再执行服务进程。其他行为与 `Type=simple` 类似。

`type` 的更多解释可以参考 [systemd.service(5) § OPTIONS](<https://man.archlinux.org/man/systemd.service.5#OPTIONS>)。 

###  修改现存单元文件

为了避免和 pacman 冲突，不应该直接编辑软件包提供的文件。有两种方法可以不改动原始文件就做到修改单元文件：创建一个优先级更高的本地单元文件以[覆盖原有的单元文件](<#%E6%9B%BF%E6%8D%A2%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6>)或创建一个片段（[drop-in snippets](<#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5>)），应用到原始单元文件之上。两种方法都需要在修改后重新加载单元：用 `systemctl edit` 编辑单元(会自动重载单元)或通过下面命令重新加载单元： 
    
    # systemctl daemon-reload
    
**提示：**

  * `systemd-delta` 命令用来查看哪些单元文件被覆盖、扩增，哪些被修改。
  * 使用 `systemctl cat _unit_` 可以查看单元的内容和所有相关的片段。

####  替换单元文件

要替换 `/usr/lib/systemd/system/_unit_`, 创建文件 `/etc/systemd/system/_unit_` 并[重新启用](<#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83>)单元以更新符号链接： 
    
    # systemctl reenable _unit_
    
或者运行： 
    
    # systemctl edit --full _unit_
    
这将会在默认编辑器中打开 `/etc/systemd/system/_unit_`。如果文件不存在，可以将软件包安装的版本复制到这里，在编辑完成之后，会自动加载新版本。 

**注意：** 即使 Pacman 更新了新的单元文件，软件包中的版本也不会被使用，所以这个方式会增加系统维护的难度，推荐使用下面一种方法。

####  附加配置片段

要为单元文件`/usr/lib/systemd/system/_unit_`附加配置片段，先创建名为 `/etc/systemd/system/_unit_.d/` 的目录，然后放入 `*.conf` 文件，其中可以添加或覆盖参数。这里设置的参数优先级高于原来的单元文件。 _systemd_ 会解析这些参数并将这些文件应用到原单元文件上。 

要附加配置片段，最简单的方法是执行： 
    
    # systemctl edit _unit_ --drop-in=_drop_in_name_
    
这将会在编辑器中打开文件 `/etc/systemd/system/_unit_.d/_drop_in_name_.conf`，编辑完成之后自动加载。若省略`--drop-in=`选项， _systemd_ 将使用默认文件名：`override.conf`。 

**注意：**

  * 附加配置片段中的键（配置项）仍必须置于相应的节（section）下。
  * 并不是所有参数都会被子配置文件覆盖。例如要修改 `Conflicts=` 就必须[替换原始文件](<https://lists.freedesktop.org/archives/systemd-devel/2017-June/038976.html>)。
  * 你可以使用顶级附加配置文件来影响所有相同类型的单元。例如，在 `/etc/systemd/system/service.d/` 中的附加配置文件会影响所有 _.service_ 单元。你可以在[#Notifying_about_failed_services](<#Notifying_about_failed_services>)中看到一个示例。

####  重置到软件包的版本

要回退使用`systemctl edit`对单元进行的所有变更，执行: 
    
    # systemctl revert _unit_
    
####  示例

如果想添加一个额外的依赖，创建如下文件即可： 
    
    /etc/systemd/system/<unit>.d/customdependency.conf
    
    [Unit]
    Requires=<新依赖>
    After=<新依赖>

要修改一个单元的 `ExecStart` 命令，创建下面文件: 
    
    /etc/systemd/system/_unit_.d/customexec.conf
    
    [Service]
    ExecStart=
    ExecStart=<新命令>

修改 `ExecStart` 前必须将其置空，参见 [[2]](<https://bugzilla.redhat.com/show_bug.cgi?id=756787#c9>) 。所有可能多次赋值的变量都需要这个操作，例如定时器的 `OnCalendar` 。 

下面是自动重启服务的一个例子： 
    
    /etc/systemd/system/_unit_.d/restart.conf
    
    [Service]
    Restart=always
    RestartSec=30

###  服务日志级别

对于直接向 journald 或 syslog 发送日志的服务，你可以通过在 `[Service]` 部分设置 `LogLevelMax=` 参数来控制其详细程度，该参数的值可以是 0 到 6 之间的数字。例如： 
    
    /etc/systemd/system/_unit_.d/override.conf
    
    [Service]
    LogLevelMax=3

标准的日志级别与用于过滤 [journal](<../zh-cn/Systemd/Journal.html> "Journal") 的级别相同。设置较低的数字会排除所有较高且不太重要的日志消息。 

####  抑制服务的标准输出

如果服务正在回显 stdout 和/或 stderr 输出，默认情况下这些输出也会进入 journal。可以通过在 `[Service]` 部分设置 `StandardOutput=null` 和/或 `StandardError=null` 来抑制此行为。除了 `null` 之外，还可以使用其他值来进一步调整此行为。参见 [systemd.exec(5) § LOGGING_AND_STANDARD_INPUT/OUTPUT](<https://man.archlinux.org/man/systemd.exec.5#LOGGING_AND_STANDARD_INPUT/OUTPUT>)。 

##  目标（target）

_systemd_ 使用**目标** 来通过依赖关系将多个单元组织起来。**目标** 还是系统的标准化同步点（确保系统处于特定状态）。**目标** 与[runlevels](<https://en.wikipedia.org/wiki/Runlevel> "wikipedia:Runlevel")的设计目的相似，但两者也有些许不同。每一个**目标** 都以名称而不是数字标识，用以达成特定的目的。多个**目标** 可以同时被激活。有的**目标** 继承另一个**目标** 的所有服务，同时向其中增添一些服务。有些 _systemd_**目标** 模仿了常见的SystemVinit runlevels。 

###  获取当前目标

使用 _systemd_ 的命令而非`runlevel`： 
    
    $ systemctl list-units --type=target
    
###  创建自定义目标

在sysvinit中有明确定义的运行级别（如：0、1、3、5、6）与 _systemd_ 中特定的**目标** 存在一一对应的关系。然而，对于用户自定义运行级别（2、4）却没有。如需要同样功能，建议你以原有运行级别所对应的 systemd 目标为基础，新建一个`/etc/systemd/system/<目标名>.target`（可参考`/usr/lib/systemd/system/graphical.target`）, 然后创建目录`/etc/systemd/system/<目标名>.wants`，并向其中加入需启用的服务链接（指向`/usr/lib/systemd/system/`中的对应文件）。 

###  “SysV运行级别”与“systemd目标”对照表

SysV 运行级别 | Systemd 目标 | 注释   
---|---|---  
0 | poweroff.target | 关闭系统（halt）   
1, s, single | rescue.target | 单用户模式   
2, 4 | multi-user.target | 用户自定义运行级别，默认与级别3相同。   
3 | multi-user.target | 多用户，无图形界面。用户可以通过终端或网络登录。   
5 | graphical.target | 多用户，图形界面。继承级别3的服务，并启动图形界面服务。   
6 | reboot.target | 重启   
emergency | emergency.target | 急救模式（Emergency shell）   
  
###  切换当前运行目标

systemd中，目标通过“目标单元”访问。通过如下命令切换： 
    
    # systemctl isolate graphical.target
    
该命令仅更改当前运行目标，对下次启动无影响。这等价于sysvinit中的`telinit 3`或`telinit 5`命令。 

###  更改开机默认启动目标

开机启动的目标是`default.target`，默认符号链接到`graphical.target`（大致相当于原来的运行级别5）。 

用 _systemctl_ 检查当前的默认启动目标： 
    
    # systemctl get-default
    
用 _systemctl_ 修改`default.target`符号链接以变更开机默认启动目标： 
    
    # systemctl set-default multi-user.target
    
    Removed /etc/systemd/system/default.target.
    Created symlink /etc/systemd/system/default.target -> /usr/lib/systemd/system/multi-user.target.

另一方法是向bootloader添加[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")： 

  * `systemd.unit=multi-user.target` （大致相当于运行级别3）
  * `systemd.unit=rescue.target` （大致相当于运行级别1）

###  默认目标顺序

Systemd 根据下面顺序选择 `default.target`： 

  1. 上面的内核参数
  2. `/etc/systemd/system/default.target` 软链接
  3. `/usr/lib/systemd/system/default.target` 软链接

##  systemd组件

_systemd_ 的部分组件如下： 

  * [kernel-install](</wzh/index.php?title=Kernel-install&action=edit&redlink=1> "Kernel-install（页面不存在）")——一个用以自动将[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel")及对应的[initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs")镜像移动到boot分区的脚本；
  * [systemd-analyze(1)](<https://man.archlinux.org/man/systemd-analyze.1>)——可用于确定启动性能、统计信息并检索其他状态和跟踪信息，以及验证单元文件的正确性。它还用于访问高级调试所需的特殊功能。
  * [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot")——简单的UEFI[启动管理器](<../zh-cn/Boot_manager.html> "Boot manager")；
  * [systemd-creds](</wzh/index.php?title=Systemd-creds&action=edit&redlink=1> "Systemd-creds（页面不存在）")——安全地存储并获取systemd单元使用的credentials；
  * [systemd-cryptenroll](</wzh/index.php?title=Systemd-cryptenroll&action=edit&redlink=1> "Systemd-cryptenroll（页面不存在）")——Enroll PKCS#11, FIDO2, TPM2 token/devices to LUKS2 encrypted volumes；
  * [systemd-firstboot](</wzh/index.php?title=Systemd-firstboot&action=edit&redlink=1> "Systemd-firstboot（页面不存在）")——负责在系统第一次启动前的设置初始化；
  * [systemd-homed](</wzh/index.php?title=Systemd-homed&action=edit&redlink=1> "Systemd-homed（页面不存在）")——portable human-user [accounts](<../zh-cn/Users_and_groups.html> "Users and groups")；
  * [systemd-logind(8)](<https://man.archlinux.org/man/systemd-logind.8>)——[会话管理](<https://dvdhrm.wordpress.com/2013/08/24/session-management-on-linux/>)；
  * [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")——[网络配置](<../zh-cn/Network_configuration.html> "Network configuration")管理；
  * [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn")——轻量namespace容器；
  * [systemd-repart](</wzh/index.php?title=Systemd-repart&action=edit&redlink=1> "Systemd-repart（页面不存在）")——创建[分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")，添加或扩大分区；
  * [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")——网络[域名解析](<../zh-cn/Domain_name_resolution.html> "Domain name resolution")；
  * [systemd-run(1)](<https://man.archlinux.org/man/systemd-run.1>) / [run0(1)](<https://man.archlinux.org/man/run0.1>)——以交互式的方式临时的提升或获得不同的权限。
  * [systemd-stub(7)](<https://man.archlinux.org/man/systemd-stub.7>)——用于创建[统一内核镜像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核镜像")的UEFI boot stub；
  * [systemd-sysusers(8)](<https://man.archlinux.org/man/systemd-sysusers.8>)——在安装软件包或系统启动时创建系统用户和组、将用户加入组；
  * [systemd-timesyncd](<../zh-cn/Systemd-timesyncd.html> "Systemd-timesyncd")——通过网络同步[系统时间](<../zh-cn/System_time.html> "System time")；
  * [systemd/Journal](<../zh-cn/Systemd/Journal.html> "Systemd/Journal")——系统日志；
  * [systemd/Timers](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/Timers")——用于控制 _.service_ 文件或事件的间隔或实时计时器，可替代[cron](<../zh-cn/Cron.html> "Cron")。

###  systemd.mount - 挂载

_systemd_ 负责挂载`/etc/fstab`中指定的分区和文件系统。[systemd-fstab-generator(8)](<https://man.archlinux.org/man/systemd-fstab-generator.8>)将`/etc/fstab`中的所有条目翻译为 _systemd_ 单元。该过程将在系统启动或系统管理器的配置被重新加载时执行。 

_systemd_ 扩展了通常[fstab](<../zh-cn/Fstab.html> "Fstab")的用法并提供了更多挂载选项。这些挂载选项可影响挂载点单元的依赖关系。例如，它们可以确保某一挂载操作只会在连接网络或另一分区挂载后进行。 _systemd_ 的特定挂载选项（大多以`x-systemd.`开头）的完整列表见[systemd.mount(5) § FSTAB](<https://man.archlinux.org/man/systemd.mount.5#FSTAB>)。 

_automounting_ 是这些挂载选项的一个例子。它意味着资源只会在请求时挂载，而非在系统启动时自动挂载，详见[fstab#通过 systemd 自动挂载](<../zh-cn/Fstab.html#%E9%80%9A%E8%BF%87_systemd_%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Fstab")。 

####  GPT分区自动挂载

在UEFI启动的系统上，GPT分区如`root`、`home`、`swap`等可以根据[Discoverable Partitions Specification](<https://uapi-group.org/specifications/specs/discoverable_partitions_specification/>)自动挂载。因此，可在[fstab](<../zh-cn/Fstab.html> "Fstab")中省略自动挂载的分区。此外，若根分区已被自动挂载，可省去内核命令行中的`root=`。详见[systemd-gpt-auto-generator(8)](<https://man.archlinux.org/man/systemd-gpt-auto-generator.8>)。 

使用GPT分区自动挂载的先决条件有： 

  * 使用[mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")时，需要[systemd hook](<../zh-cn/Mkinitcpio.html#Common_hooks> "Mkinitcpio")。
  * 所有自动挂载的分区必须与ESP分区在同一块物理硬盘上。
  * 必须设置正确的GPT分区类型。详见[Partitioning#Partition scheme](<../zh-cn/%E5%88%86%E5%8C%BA.html#Partition_scheme> "Partitioning")。
  * 引导加载程序必须设置[LoaderDevicePartUUID](<https://systemd.io/BOOT_LOADER_INTERFACE/>)EFI变量，以便识别使用的EFI系统分区。[systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot")，[systemd-stub(7)](<https://man.archlinux.org/man/systemd-stub.7>)，[GRUB](<../zh-cn/GRUB.html> "GRUB") (使用 _grub-mkconfig_ 生成`grub.cfg`），[rEFInd（默认未启用）](<../zh-cn/REFInd.html#LoaderDevicePartUUID> "REFInd")支持该特性。若使用自定义的`grub.cfg`，则需要[加载bli模块](<../zh-cn/GRUB.html#LoaderDevicePartUUID> "GRUB")。 可通过执行`bootctl`并检查`Boot loader sets ESP information`的状态进行确认，或在用[统一内核镜像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核镜像")启动时检查`Stub sets ESP information`的状态。

_udev_ 会创建一个指向根卷块设备的`/dev/gpt-auto-root`符号链接。如果根分区使用LUKS加密，`/dev/gpt-auto-root`将指向解锁/映射的卷，而`/dev/gpt-auto-root-luks`将指向加密分区。 

**提示：** 某个分区的自动挂载可通过如下两种方式关闭：修改分区的[类型GUID](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table")或设置分区属性的63"do not automount"位，详见[gdisk#Prevent GPT partition automounting](<../zh-cn/GPT_fdisk.html#Prevent_GPT_partition_automounting> "Gdisk")。

#####  /var

要自动挂载`/var`分区，分区的PARTUUID必须与以machine ID为密钥，分区类型UUID为消息的SHA256 HMAC哈希计算结果相同。可通过如下命令得到符合要求的PARTUUID： 
    
    $ systemd-id128 -u var-partition-uuid
    
**注意：**[systemd-id128(1)](<https://man.archlinux.org/man/systemd-id128.1>)从`/etc/machine-id`读取machine ID，因此必须在系统安装后才能得到符合要求的PARTUUID。

### systemd-sysvcompat

[systemd-sysvcompat](<https://archlinux.org/packages/?name=systemd-sysvcompat>)包（由[base](<https://archlinux.org/packages/?name=base>)包需要）的主要工作是提供传统的Linux [init](<../zh-cn/Init.html> "Init")可执行文件。在由systemd控制的系统上，`init`只是一个到`systemd`可执行文件的符号链接。 

此外，该包还提供了[SysVinit](<../zh-cn/SysVinit.html> "SysVinit")用户可能需要的功能的4个快捷方式：[halt(8)](<https://man.archlinux.org/man/halt.8>)，[poweroff(8)](<https://man.archlinux.org/man/poweroff.8>)，[reboot(8)](<https://man.archlinux.org/man/reboot.8>)和[shutdown(8)](<https://man.archlinux.org/man/shutdown.8>)。这4个命令都是到`systemctl`的符号链接，其行为受 _systemd_ 控制。因此，在[#电源管理](<#%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86>)中提到的规则对它们同样适用。 

在由systemd控制的系统上，可通过`init=`[内核启动参数](<../zh-cn/Kernel_parameters.html#%E5%8F%82%E6%95%B0%E5%88%97%E8%A1%A8> "Kernel parameters")取消对System V的兼容性支持。详见[/bin/init is in systemd-sysvcompat ?](<https://bbs.archlinux.org/viewtopic.php?id=233387>)。 

###  systemd-tmpfiles - 临时文件

_systemd-tmpfiles_ 创建，删除并清理临时文件/文件夹。 _systemd-tmpfiles_ 读取`/etc/tmpfiles.d/`、`/usr/lib/tmpfiles.d/`中的配置文件（前者比后者优先级高）以确定执行什么操作。 

这些配置文件通常与服务文件一同提供，并以`/usr/lib/tmpfiles.d/<程序>.conf`风格命名。例如，[Samba](<../zh-cn/Samba.html> "Samba")守护进程需要`/run/samba`目录存在且权限设置正确，因此[samba](<https://archlinux.org/packages/?name=samba>)包中附带了如下配置： 
    
    /usr/lib/tmpfiles.d/samba.conf
    
    D /run/samba 0755 root root
    
配置文件也可能用于在启动时向特定文件中写入值。例如，要禁止系统从USB设备唤醒。在之前可使用`/etc/rc.local`在启动时执行`echo USBE > /proc/acpi/wakeup`，而现在可以这么做： 
    
    /etc/tmpfiles.d/disable-usb-wake.conf
    
    #    Path                  Mode UID  GID  Age Argument
    w    /proc/acpi/wakeup     -    -    -    -   USBE
    
可以通过在参数中使用 `\n` 或者在多行配置的情况下用 `w+` 类型来进行 _追加_ （包括第一行）。 
    
    /etc/tmpfiles.d/disable-usb-wake.conf
    
    #    Path                  Mode UID  GID  Age Argument
    w+   /proc/acpi/wakeup     -    -    -    -   USBE
    w+   /proc/acpi/wakeup     -    -    -    -   LID0
    
详见[systemd-tmpfiles(8)](<https://man.archlinux.org/man/systemd-tmpfiles.8>)、[tmpfiles.d(5)](<https://man.archlinux.org/man/tmpfiles.d.5>)。 

**注意：** 若要向`/sys`中的配置文件写入值，可能不能使用该方法。因为 _systemd-tmpfiles-setup_ 服务可能在相关模块加载前运行。在这种情况下，可先通过`modinfo <模块名>`检查该模块是否可通过设定模块参数来修改相应的选项。若有对应的模块参数，可通过[/etc/modprobe.d目录中的配置文件](<../zh-cn/Kernel_modules.html#Setting_module_options> "Kernel modules")设定相应参数以达到修改选项的目的。否则，将只能通过[udev 规则](<../zh-cn/Udev_%E8%A7%84%E5%88%99.html> "Udev 规则")来在设备被识别时设定相应属性。

###  Drop-in 配置文件

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 本页面是关于PID 1（init）的，单元文件的drop-in配置已经提到。Drop-in是一个通用概念，加上其他systemd组件有专门的wiki页面。因此本节似乎不属于这里。（在 [Talk:Systemd#YHNdnzj : Configuration files in conf.d / drop-in snippets: misplaced?](</wzh/index.php?title=Talk:Systemd&action=edit&redlink=1> "Talk:Systemd（页面不存在）") 中讨论）

为了避免与pacman更新冲突，不应直接编辑由软件包提供的配置文件。为此，许多（但不是所有）systemd软件包提供了一种修改配置的方式，但不直接修改原始文件，而是通过创建drop-in片段来实现。请检查软件包手册以查看是否支持drop-in配置文件。 

要为单元文件`/etc/systemd/_unit_.conf`创建drop-in配置文件，请创建目录`/etc/systemd/_unit_.conf.d/`并在其中放置 _.conf_ 文件以覆盖或添加新选项。 _systemd_ 将解析并应用这些文件到原始单元之上。 

检查整体配置： 
    
    $ systemd-analyze cat-config systemd/_unit_.conf
    
应用的drop-in片段文件及其内容将列在最后。[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart")服务以使更改生效。 

##  小技巧

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 我们应该在某个地方明确记录套接字激活相对于简单服务启动的优势。这在页面开头和相关页面（如[Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）")）中简要提到。 (在 [Talk:Systemd](<../zh-cn/Talk:Systemd.html>) 中讨论)

###  激活套接字

有一些包提供了一个 _.socket_ 单元。例如，[cups](<https://archlinux.org/packages/?name=cups>)包 提供了一个 `cups.socket` 单元[[3]](<https://0pointer.de/blog/projects/socket-activation2.html>)。如果 `cups.socket` 被[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")（并且 `cups.service` 保持关闭）， _systemd_ 并不会立刻启动 CUPS，它会监听适当的套接字并且当任何一个程序尝试连接 CUPS 服务中的一个时， _systemd_ 会启动 `cups.service` 并且透明地将这些端口的控制权移交给 CUPS 进程。 

###  GUI配置工具

  * **systemadm** — 用于 _systemd_ 单元的图形化浏览器。可显示单元列表，并能按类型筛选。

     <https://cgit.freedesktop.org/systemd/systemd-ui/> || [systemd-ui](<https://archlinux.org/packages/?name=systemd-ui>)包

  * **SystemdGenie** — 基于KDE的 _systemd_ 管理工具。

     <https://invent.kde.org/system/systemdgenie> || [systemdgenie](<https://archlinux.org/packages/?name=systemdgenie>)包

###  在网络已连接后再启动某服务

如果需要将某服务延迟到网络已连接后再启动, 直接在 _.service_ 文件中包含以下依赖项： 
    
    /etc/systemd/system/<单元名>.service
    
    [Unit]
    ...
    Wants=network-online.target
    After=network-online.target
    ...

要使`network-online.target`正确反映网络状态，必须启用所使用的[网络管理器](<../zh-cn/Network_manager.html> "Network manager")的网络等待服务。 

  * 若使用[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager"), `NetworkManager-wait-online.service`应该与`NetworkManager.service`一同启用。可通过`systemctl is-enabled NetworkManager-wait-online.service`进行检查。若服务没用启用，[重新启用](<#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83>)`NetworkManager.service`。
  * 若使用[netctl](<../zh-cn/Netctl.html> "Netctl"), [启用](<#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83>)`netctl-wait-online.service` (除非使用了 _netctl-auto_ ； 详见[FS#75836](<https://bugs.archlinux.org/task/75836>))。
  * 若使用[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd"), `systemd-networkd-wait-online.service`应该与`systemd-networkd.service`一同启用。可通过`systemctl is-enabled systemd-networkd-wait-online.service`进行检查。若服务没用启用，[重新启用](<#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83>)`systemd-networkd.service`。

如果需要更为详细的解释，请查看[网络配置同步点](<https://systemd.io/NETWORK_ONLINE/#discussion>)中的讨论。 

若某服务需要执行DNS查询，其应该被排在`nss-lookup.target`后： 
    
    /etc/systemd/system/<单元名>.service
    
    [Unit]
    ...
    Wants=network-online.target
    After=network-online.target nss-lookup.target
    ...

详见[systemd.special(7) § Special Passive System Units](<https://man.archlinux.org/man/systemd.special.7#Special_Passive_System_Units>). 

要`nss-lookup.target`发挥作用，必须有一个单元通过`Wants=nss-lookup.target`引入`nss-lookup.target`，并通过`Before=nss-lookup.target`排在`nss-lookup.target`之前。一般情况下，上述配置由本地[DNS解析器](<../zh-cn/DNS_resolver.html> "DNS resolver")完成。 

检查哪一个正在运行的单元引入了`nss-lookup.target`： 
    
    $ systemctl list-dependencies --reverse nss-lookup.target
    
###  默认启用新安装的单元

Arch Linux附带的`/usr/lib/systemd/system-preset/99-default.preset`包含`disable *`，这会导致默认情况下的 _systemctl preset_ 是禁用所有新安装的的单元。因此某个新包安装后, 用户必须手动启用新单元。 

若上述行为不符合预期, 创建一个从`/etc/systemd/system-preset/99-default.preset`到`/dev/null`的符号链接来覆盖该配置文件，这会导致 _systemctl preset_ 无视单元类型直接启用所有单元，除非 _systemctl preset_ 的配置目录中有文件另有声明。用户单元不受影响。详见[systemd.preset(5)](<https://man.archlinux.org/man/systemd.preset.5>)。 

**注意：** 若某个软件包含有多个互相冲突的单元，默认启用所有单元可能会出现问题。 _systemctl preset_ 原本旨在供发行版或系统管理员使用。在有两个冲突单元将被同时启用的情况下，应明确在 _systemctl preset_ 的配置文件中禁用其中一个单元，详见[systemd.preset(5)](<https://man.archlinux.org/man/systemd.preset.5>)。

###  应用程序环境沙盒

可通过一个单元文件创建一个沙盒以在加固的虚拟环境中隔离应用程序及其进程。 _systemd_ 充分利用[namespaces](<https://en.wikipedia.org/wiki/Linux_namespaces> "wikipedia:Linux namespaces")，一系列允许/拒绝[capabilities](<../zh-cn/Capabilities.html> "Capabilities")和[cgroups](</wzh/index.php?title=Control_groups&action=edit&redlink=1> "Control groups（页面不存在）")，以通过可拓展的执行环境设置（[systemd.exec(5)](<https://man.archlinux.org/man/systemd.exec.5>)）将进程禁锢在容器中。 

将现有 _systemd_ 单元文件进行沙盒化加固通常需要结合使用[strace](<https://archlinux.org/packages/?name=strace>)包，[stderr](<https://en.wikipedia.org/wiki/Standard_streams#Standard_error_.28stderr.29> "wikipedia:Standard streams")和[journalctl(1)](<https://man.archlinux.org/man/journalctl.1>)等进行大量试验。因此，最好先在上游文档中搜索已完成的测试以作为试验的基础。 

首先，最好通过以下命令获得特定单元可能的加固选项作为基础： 
    
    $ systemd-analyze security <单元>
    
关于如何使用 systemd 部署沙盒的一些示例： 

  * `CapabilityBoundingSet`定义了一个列表，以指明某个单元可以/不能使用哪些[capabilities(7)](<https://man.archlinux.org/man/capabilities.7>)。详见[systemd.exec(5) § CAPABILITIES](<https://man.archlinux.org/man/systemd.exec.5#CAPABILITIES>)。 
    * 例如，对`CAP_SYS_ADM` capability的控制应该是[安全沙盒的目标](<https://lwn.net/Articles/486306/>): `CapabilityBoundingSet=~ CAP_SYS_ADM`

###  通知失败的单元

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[systemd/Timers#MAILTO](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html#MAILTO> "Systemd/Timers")。**

**附注：** 相同话题，不同解决方案（在 [Talk:Systemd](<../zh-cn/Talk:Systemd.html>) 中讨论）

要在服务故障时发出通知，可在相应服务的单元文件中添加`OnFailure=`设置，这可通过[#附加配置片段](<#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5>)完成。若要在每一个服务的单元文件中添加该设置，可使用一个顶层附加配置片段，详见[systemd.unit(5)](<https://man.archlinux.org/man/systemd.unit.5>)。 

为服务单元创建顶层附加配置片段： 
    
    /etc/systemd/system/service.d/toplevel-override.conf
    
    [Unit]
    OnFailure=failure-notification@%n.service

这将向每个服务单元文件中添加`OnFailure=failure-notification@%n.service`。若**单元甲** 失败，会启动`failure-notification@**单元甲**.service`来递送相关通知（或执行其它配置的动作）。 

创建`failure-notification@.service`模板单元： 
    
    /etc/systemd/system/failure-notification@.service
    
    [Unit]
    Description=Send a notification about a failed systemd unit
    
    [Service]
    Type=oneshot
    ExecStart=/_path_ /_to_ /failure-notification.sh %i
    # 以临时用户/组运行并启用其他安全措施
    DynamicUser=true

接下来可创建`failure-notification.sh`脚本，定义执行的操作或发送通知的方式（邮件、桌面通知、gotify、XMPP等）。`%i`将被替换为失败单元的名称并作为参数被传递给`failure-notification.sh`脚本。 

为防止`failure-notification@.service`的实例启动失败时引发`failure-notification@.service`实例的递归性启动，在`failure-notification@.service`单元的配置目录下创建一个与顶层附加配置片段文件名相同的空的附加配置片段（该空的附加配置片段比全局附加配置片段优先级更高）： 
    
    # mkdir -p /etc/systemd/system/failure-notification@.service.d
    # touch /etc/systemd/system/failure-notification@.service.d/toplevel-override.conf
    
##  疑难解答

###  寻找失败的单元

要寻找启动失败的 _systemd_ 单元，执行： 
    
    $ systemctl --state=failed
    
可通过它们的日志查找失败的原因。详见[systemd/Journal#过滤输出](<../zh-cn/Systemd/Journal.html#%E8%BF%87%E6%BB%A4%E8%BE%93%E5%87%BA> "Systemd/Journal")。 

###  诊断系统启动问题

_systemd_ 有许多用于调试系统启动过程中的问题的选项。要捕获在 _systemd_ 接管[启动流程](<../zh-cn/Boot_process.html> "Boot process")前的日志，参阅[boot debugging](<../zh-cn/Boot_debugging.html> "Boot debugging")。还可参阅此[系统调试文档](<https://systemd.io/DEBUGGING/>)。 

###  诊断一个服务

如果某个 _systemd_ 服务的工作状况不合预期或想了解发生了什么的更多信息，将`SYSTEMD_LOG_LEVEL`[环境变量](<../zh-cn/Environment_variable.html> "Environment variable")的值设为`debug`。例如，要以调试模式运行 _systemd-networkd_ 守护进程： 

在此服务的配置文件中加入如下[配置片段](<#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5>)： 
    
    [Service]
    Environment=SYSTEMD_LOG_LEVEL=debug
    
或者手动设置该环境变量以达到相同效果： 
    
    # SYSTEMD_LOG_LEVEL=debug /lib/systemd/systemd-networkd
    
之后，[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") _systemd-networkd_ 并以`-f`/`--follow`启动journalctl观察该单元的日志。 

###  关机/重启十分缓慢

如果关机十分缓慢（甚至跟死机了一样），很可能是某个拒不退出的服务在作怪。对于每个服务 _systemd_ 会等待一段时间，然后再尝试杀死它。要确定是否受到该问题影响，详见 _systemd_ 文档中的[Shutdown completes eventually 这篇文章](<https://systemd.io/DEBUGGING/#shutdown-completes-eventually>)。 

一个常见的原因是存在一个搁置的关机或挂起进程。要确认是否为这种情况，执行下列命令中的任何一个并观察有无类似的输出： 
    
    # systemctl poweroff
    
    Failed to power off system via logind: There's already a shutdown or sleep operation in progress
    
    # systemctl list-jobs
    
      JOB UNIT                    TYPE  STATE
    ...
    21593 systemd-suspend.service start running
    21592 suspend.target          start waiting
    ..
    
该问题的[解决方法](<https://unix.stackexchange.com/a/579531>)是取消这些关机/挂起工作： 
    
    # systemctl cancel
    # systemctl stop systemd-suspend.service
    
并再次尝试关机或重启。 

###  一些短命进程似乎没有产生任何日志输出

对于短命的服务进程（启动后迅速失败），若以root身份执行`journalctl -u <单元名>`可能看不到任何输出，此时可转而使用进程的PID。例如，若`systemd-modules-load.service`单元失败，通过`systemctl status systemd-modules-load`得到的对应进程PID为123，以root身份执行`journalctl -b _PID=123`或许就能得到日志输出。上述问题的原因是日志元数据（如`_SYSTEMD_UNIT`、`_COMM`）以异步方式被采集，且依赖于`/proc`中相应进程的目录。修复该问题需要修改内核以通过socket提供需要的数据（类似于`SCM_CREDENTIALS`）。简而言之，该问题是一个[bug](<https://github.com/systemd/systemd/issues/2913>)，只需记住由于 _systemd_ 的设计，在启动后迅速失败的单元可能不会打印任何输出到系统日志中。 

###  systemd-tmpfiles-setup.service在系统启动时失败

自 _systemd_ 219开始，`/usr/lib/tmpfiles.d/systemd.conf`为`/var/log/journal`下的目录指定了ACL选项。因此存放日志的文件系统必须启用ACL支持。 

如何在存放`/var/log/journal`的文件系统上启用ACL的说明见[Access Control Lists#启用 ACL](<../zh-cn/Access_Control_Lists.html#%E5%90%AF%E7%94%A8_ACL> "Access Control Lists")。 

###  在远程主机上关闭救援（emergency）模式

当救援模式被触发时，机器不会连接网络，因此对于托管于Azure或Google Cloud的远程主机，或许需要关闭救援模式。 

要关闭救援模式，[屏蔽](<#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83>)`emergency.service`和`emergency.target`。 

##  参见

  * [Wikipedia:systemd](<https://en.wikipedia.org/wiki/systemd> "wikipedia:systemd")
  * [官方网站](<https://systemd.io/>)
    * [systemd 优化](<https://systemd.io/OPTIMIZATIONS/>)
    * [systemd 常见问题解答](<https://systemd.io/FAQ/>)
    * [systemd 技巧与窍门](<https://systemd.io/TIPS_AND_TRICKS/>)
  * [systemd(1)](<https://man.archlinux.org/man/systemd.1>)
  * 其他发行版 
    * [Gentoo:Systemd](<https://wiki.gentoo.org/wiki/Systemd> "gentoo:Systemd")
    * [Debian:Systemd](<https://wiki.debian.org/Systemd> "debian:Systemd")
    * [Ubuntu:Systemd](</wzh/index.php?title=Ubuntu:Systemd&action=edit&redlink=1> "Ubuntu:Systemd（页面不存在）")
    * [Fedora:Systemd](<https://fedoraproject.org/wiki/Systemd> "fedora:Systemd")
    * [openSUSE:Systemd](</wzh/index.php?title=OpenSUSE:Systemd&action=edit&redlink=1> "OpenSUSE:Systemd（页面不存在）")
  * [如何使用 Systemctl 管理 Systemd 服务和单元](<https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units>)
  * [使用 systemd-logind 进行会话管理](<https://dvdhrm.wordpress.com/2013/08/24/session-management-on-linux/>)
  * [Emacs 对 Systemd 文件的语法高亮](<../zh-cn/Emacs.html#Syntax_highlighting_for_systemd_Files> "Emacs")
  * [两篇](<https://www.h-online.com/open/features/Control-Centre-The-systemd-Linux-init-system-1565543.html>) [部分](<https://www.h-online.com/open/features/Booting-up-Tools-and-tips-for-systemd-1570630.html>)介绍文章，发表于 _The H Open_ 杂志。
