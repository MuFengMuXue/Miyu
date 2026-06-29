**翻译状态：**

  * 本文（或部分内容）译自 [init](<https://wiki.archlinux.org/title/init> "arch:init")，最近一次同步于 2022-03-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/init?diff=0&oldid=723712>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/init_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch boot process](<../zh-cn/Arch_boot_process.html> "Arch boot process")
  * [ConsoleKit](</wzh/index.php?title=ConsoleKit&action=edit&redlink=1> "ConsoleKit（页面不存在）")

**警告：** Arch Linux 只提供对 systemd 的官方支持。[[1]](<https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/message/RSVHZP56KEQ4C6PRTROIMJRM45MTOFK7/>)如使用其他 init 系统，在请求支持时请注明。

[Init](<https://zh.wikipedia.org/wiki/Init> "zhwp:Init") 是系统启动时创建的第一个进程。它是一个[守护进程](<../zh-cn/Systemd.html> "Daemons")，会一直运行到系统关闭。init 是其他所有进程的直接或间接祖先，并自动监护所有孤儿进程。内核按照硬编码的文件名启动它，如果内核不能启动它，将会导致[内核崩溃](<../zh-cn/General_troubleshooting.html#%E5%86%85%E6%A0%B8%E5%B4%A9%E6%BA%83%EF%BC%88Kernel_panic%EF%BC%89> "General troubleshooting")。init 的[进程标识符](<https://zh.wikipedia.org/wiki/%E8%BF%9B%E7%A8%8BID> "zhwp:进程ID")（PID）通常是 1。 

在系统启动和关闭时，init 进程会启动 init 脚本（或称 rc）来保障基本功能。这包括挂载和卸载[文件系统](<../zh-cn/File_systems.html> "File systems")，以及启动守护进程。进一步，有一个服务管理器提供对已启动进程的主动控制，称为[进程监控](<https://en.wikipedia.org/wiki/Process_supervision> "w:Process supervision")。例如监测崩溃的进程并适时重启。 

这些元素加起来就成了 init **系统** 。某些 init 将服务管理器包含在 init 进程中，或是有紧密联系的 init 脚本。在下面，这类 init 将被称为整合式的。其他的分类下的条目可能会相互依赖。 

##  整合式 init

  * **anopa** — 围绕 s6 监视套件构建的 init 系统。

     <https://jjacky.com/anopa/> || [anopa](<https://aur.archlinux.org/packages/anopa/>)AUR

  * **GNU Shepherd** — 用 [Guile](<https://www.gnu.org/software/guile/>) 编写的 init 系统。

     <https://www.gnu.org/software/shepherd/> || [shepherd](<https://aur.archlinux.org/packages/shepherd/>)AUR

  * **[OpenRC](<../zh-cn/OpenRC.html> "OpenRC")** — 基于依赖的 init 系统。

     <https://www.gentoo.org/proj/en/base/openrc/> || [openrc](<https://aur.archlinux.org/packages/openrc/>)AUR [openrc-arch-services-git](<https://aur.archlinux.org/packages/openrc-arch-services-git/>)AUR

  * **[systemd](<../zh-cn/Systemd.html> "Systemd")** — 基于依赖的 init 系统，具备激进的并行化，使用 cgroups 提供进程监护，及依赖于给定挂载点或 dbus 服务的能力。

     <https://freedesktop.org/wiki/Software/systemd/> || [systemd](<https://archlinux.org/packages/?name=systemd>)包

## init

  * **[BusyBox](<../zh-cn/BusyBox.html> "BusyBox")** — 用于救援和嵌入式系统的工具。

     <https://busybox.net/> || [busybox](<https://archlinux.org/packages/?name=busybox>)包

  * **sinit** — 基于 Rich Felker 所作最简 init 的简单init。

     <https://core.suckless.org/sinit> || [sinit](<https://aur.archlinux.org/packages/sinit/>)AUR

  * **[SysVinit](<../zh-cn/SysVinit.html> "SysVinit")** — 传统的 system V init。

     <https://savannah.nongnu.org/projects/sysvinit> || [sysvinit](<https://aur.archlinux.org/packages/sysvinit/>)AUR

##  init 脚本

  * **initscripts-fork** — 另行维护的 Arch Linux 的 SysVinit 脚本分支。

     <https://bitbucket.org/TZ86/initscripts-fork/overview> || [initscripts-fork](<https://aur.archlinux.org/packages/initscripts-fork/>)AUR

  * **minirc** — 为 BusyBox 设计的最简 init 脚本。

     <https://github.com/hut/minirc/> || [minirc-git](<https://aur.archlinux.org/packages/minirc-git/>)AUR

  * **kisslinux-init** — KISS Linux 的 init 框架。

     <https://github.com/kisslinux/init> || [kisslinux-init](<https://aur.archlinux.org/packages/kisslinux-init/>)AUR

##  服务管理器

  * **[monit](</wzh/index.php?title=Monit&action=edit&redlink=1> "Monit（页面不存在）")** — monit是 Unix 和 Linux 系统的进程管理工具。monit 支持直接从命令行或是原生的 HTTP(S) 网络服务器查看系统状态。

     <https://mmonit.com/monit/> || [monit](<https://archlinux.org/packages/?name=monit>)包

  * **perp** — 适用于 UNIX 的持久进程（服务）监管器和管理框架。

     <http://b0llix.net/perp/> || [perp](<https://aur.archlinux.org/packages/perp/>)AUR

  * **[runit](</wzh/index.php?title=Runit&action=edit&redlink=1> "Runit（页面不存在）")** — UNIX init 框架，用于替代 SysVinit 和其他 init 框架。

     <http://smarden.org/runit/> || [busybox](<https://archlinux.org/packages/?name=busybox>)包

  * **s6** — 一小组 UNIX 程序, 设计来允许代替 daemontools 和 runit 的服务监管。

     <https://skarnet.org/software/s6/> || [s6](<https://aur.archlinux.org/packages/s6/>)AUR

  * **Supervisor** — 一个允许用户在类 UNIX 系统上监控进程的系统。

     <https://supervisord.org/> || [supervisor](<https://archlinux.org/packages/?name=supervisor>)包

##  配置

###  迁移正在运行的服务

为了在新 init 下运行守护进程，首先要保存正在运行的守护进程清单： 
    
    $ systemctl list-units --state=running "*.service" > daemons.list
    
然后相应配置 [#init 脚本](<#init_%E8%84%9A%E6%9C%AC>)。参看[[2]](<https://unix.stackexchange.com/questions/175380/how-to-list-all-running-daemons>)。 

**注意：**[systemd-tmpfiles(8)](<https://man.archlinux.org/man/systemd-tmpfiles.8>)、[内核模块](<../zh-cn/Kernel_module.html> "Kernel module")和 [sysctl](<../zh-cn/Sysctl.html> "Sysctl")可能也需要配置。

### logind

[logind](<https://www.freedesktop.org/wiki/Software/systemd/logind/>) 要求 init 进程是 systemd。因此，[本地会话](<../zh-cn/General_troubleshooting.html#%E4%BC%9A%E8%AF%9D%E6%9D%83%E9%99%90> "General troubleshooting")和其他功能不可用。 

**提示：** 有一个单独版本的 logind。[elogind-git](<https://aur.archlinux.org/packages/elogind-git/>)AUR [[3]](<https://lists.gnu.org/archive/html/guix-devel/2015-04/msg00352.html>)

设备权限

将用户添加到相应的[用户组](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups")以允许设备访问和重启。应当先用 `id _user_` 检查当前所属的用户组。 以下命令允许用户访问大多数设备： 
    
    # usermod -a -G video,audio,power,disk,storage,optical,lp,scanner,input _user_
    
另可参见 [systemd 之前的群组](<../zh-cn/Users_and_groups.html#systemd_%E4%B9%8B%E5%89%8D%E7%9A%84%E7%BE%A4%E7%BB%84> "Users and groups")。 

要创建 [polkit](<../zh-cn/Polkit.html> "Polkit") 使用的组规则，参见[跳过口令提示](<../zh-cn/Polkit.html#%E8%B7%B3%E8%BF%87%E5%8F%A3%E4%BB%A4%E6%8F%90%E7%A4%BA> "Polkit")。 

没有 root 权限的 X

因为 `Xorg.wrap` 不检查 logind 是否活跃，[Xorg 的根权限](<../zh-cn/Xorg.html#%E6%B2%A1%E6%9C%89_root_%E6%9D%83%E9%99%90%E7%9A%84_Xorg> "Xorg")需要手动启用： 
    
    /etc/X11/Xwrapper.config
    
    needs_root_rights = yes

电源管理

参见 [pm-utils](<https://aur.archlinux.org/packages/pm-utils/>)AUR 和 [acpid](<../zh-cn/Acpid.html> "Acpid") 以替换[用 systemd 进行的电源管理](<../zh-cn/Power_management.html#%E7%94%A8_systemd_%E8%BF%9B%E8%A1%8C%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86> "Power management")。 

###  定时任务

Arch 默认使用 [timer](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/Timers") 而非 [cron](<../zh-cn/Cron.html> "Cron")。可在 [archlinux-cronjobs](<https://github.com/notfoss/archlinux-cronjobs>) 参看基本的 cron 任务。 

### D-Bus

dbus-daemon 的用户实例由 [systemd 用户服务](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")启动。[[4]](<https://archlinux.org/news/d-bus-now-launches-user-buses/>)在需要桌面应用间通讯时，恢复`30-dbus.sh`： 
    
    /etc/X11/xinit/xinitrc.d/30-dbus.sh
    
    #!/bin/bash
    
    # launches a session dbus instance
    if [ -z "${DBUS_SESSION_BUS_ADDRESS-}" ] && type dbus-launch >/dev/null; then
      eval $(dbus-launch --sh-syntax --exit-with-session)
    fi

##  提示与技巧

### systemd-nspawn

[systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn") 是 systemd 系统的工具。从 Linux 2.6.19 起，可以在非 systemd 系统上用 PID 名称空间运行 systemd。这需要内核配置了 `CONFIG_PID_NS` 和`CONFIG_NAMESPACES`。 

PID 名称空间创建一个新的进程架构，从 PID 1 开始。另外，systemd 需要一个已经 chroot 的文件系统才能挂载。因此，你必须至少做一个绑定挂载，否则某些服务可能会报这样的错： 
    
    "Failed at step NAMESPACE spawning" due to "Invalid operation" 
    
这是因为 systemd 尝试以 `private` 选项重新挂载根目录。 

可以用 [jchroot](<https://github.com/vincentbernat/jchroot>) 设置一个有新 PID 名称空间的 chroot。 

确保不要在 chroot 前挂载新根目录的 `/proc`，否则 systemd 会检测到 chroot 环境。在 systemd 运行以后可以挂载。 

###  替换 udev

**警告：** 替换 udev 并非必要，因为即使 systemd 不是 PID 1，systemd-udev 也能工作。某些替换比如 eudev 无法与 [systemd](<https://archlinux.org/packages/?name=systemd>)包 共存，请确保在安装**之前** 启动了另外的 init。

  * **eudev** — eudev 是 Gentoo 项目开发的 udev 分支项目。需要与 OpenRC 配合设计和测试。

     [Gentoo:eudev](<https://wiki.gentoo.org/wiki/eudev> "gentoo:eudev") || [eudev](<https://aur.archlinux.org/packages/eudev/>)AUR

  * **mdev** — 用于嵌入式系统的设备管理器。

     <https://git.busybox.net/busybox/plain/docs/mdev.txt> || [busybox](<https://archlinux.org/packages/?name=busybox>)包

  * **smdev** — smdev 是一个简单的管理设备节点的程序。其基本与 mdev 兼容，但没有后者的全部特性。

     <https://git.suckless.org/smdev/> || [smdev](<https://aur.archlinux.org/packages/smdev/>)AUR

##  参见
