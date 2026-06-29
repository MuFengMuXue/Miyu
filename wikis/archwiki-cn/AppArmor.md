相关文章

  * [安全](<../zh-cn/%E5%AE%89%E5%85%A8.html> "安全")
  * [SELinux](<../zh-cn/SELinux.html> "SELinux")
  * [TOMOYO Linux](</wzh/index.php?title=TOMOYO_Linux&action=edit&redlink=1> "TOMOYO Linux（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [AppArmor](<https://wiki.archlinux.org/title/AppArmor> "arch:AppArmor")，最近一次同步于 2025-12-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/AppArmor?diff=0&oldid=853107>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/AppArmor_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[AppArmor](<https://apparmor.net/>) 是一种[强制访问控制](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E5%BC%BA%E5%88%B6%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6> "安全")（Mandatory Access Control, MAC）系统，基于 [Linux 安全模块](<https://en.wikipedia.org/wiki/Linux_Security_Modules> "wikipedia:Linux Security Modules")（Linux Security Modules, LSM）实现。 

就像其他大多数的 Linux 安全模块一样，AppArmor 是对默认的的自主访问控制（Discretionary Access Control, DAC）的补充，而非替代。因此，程序通过 AppArmor 获取到的权限不可能大于原本在 DAC 下拥有的权限。 

Ubuntu，SUSE 和许多其他的发行版默认使用 AppArmor，而 RHEL（及其衍生发行版）所使用的 SELinux 需要特定的用户空间工具才能正常使用。SELinux 通过附加标签的方式管理所有的文件、进程和对象，因而十分灵活。不过，普遍认为 SELinux 难以配置，且需要支持扩展属性的的文件系统才能运作。相反，AppArmor 基于文件路径，配置文件也相对简单易懂。 

AppArmor 通过对特定应用执定专用的规则集，主动保护操作系统和应用程序免受来自内外部的威胁，包括部分零日漏洞攻击。安全策略决定了每个应用所能够访问的系统资源及其权限。没有在安全配置文件中允许的访问，将被默认拦截。AppArmor 随附了一些默认策略，再结合使用高级静态分析与基于学习的工具，即使是极其复杂的应用程序，用户也可以在数小时内完成其 AppArmor 策略的编写。 

任何违反策略的访问都将在系统日志中报告。也可以通过配置 AppArmor，令其在越权访问发生时，在用户桌面实时弹出警告通知。 

##  安装

AppArmor 可以在所有的[官方支持的内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E5%AE%98%E6%96%B9%E6%94%AF%E6%8C%81%E7%9A%84%E5%86%85%E6%A0%B8> "内核")中使用。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [apparmor](<https://archlinux.org/packages/?name=apparmor>)包 以获取管理 AppArmor 的用户空间工具与库。要在启动时加载所有 AppArmor 安全配置文件，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `apparmor.service`。 

要在每次引导时将 AppArmor 作为默认的安全模型启用，设置以下的[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")： 
    
    lsm=landlock,lockdown,yama,integrity,apparmor,bpf
    
**注意：**`lsm=` 内核参数决定了 Linux 安全模块的初始化顺序。内核已配置的 `lsm=` 值可以通过 `zgrep CONFIG_LSM= /proc/config.gz` 查看，当前值可以通过 `cat /sys/kernel/security/lsm` 查看。 

  * 确保 `apparmor` 是参数列表中的第一个“主要”模块。[[1]](<https://docs.kernel.org/admin-guide/LSM/index.html>)合法的值和顺序的样例可以在 [security/Kconfig](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/security/Kconfig>) 查看。
  * `lsm=` 中不应包含 `capability`，因为它始终会被自动隐式包含。

###  自定义内核

自行[编译内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E7%BC%96%E8%AF%91> "内核")时，需要启用以下选项： 
    
    CONFIG_SECURITY_APPARMOR=y
    CONFIG_AUDIT=y
    
要让内核在无需设置内核参数的前提下默认启用 AppArmor Linux 安全模型，需要额外添加 `CONFIG_LSM` 选项，并将 `apparmor` 设定为列表中的第一个“主要”模块。 
    
    CONFIG_LSM="landlock,lockdown,yama,integrity,apparmor,bpf"
    
##  使用方法

###  显示当前状态

检测 AppArmor 是否成功启动： 
    
    $ aa-enabled
    
    Yes
    
显示当前运行状态，执行 [aa-status(8)](<https://man.archlinux.org/man/aa-status.8>)： 
    
    # aa-status
    
    apparmor module is loaded.
    44 profiles are loaded.
    44 profiles are in enforce mode.
     ...
    0 profiles are in complain mode.
    0 processes have profiles defined.
    0 processes are in enforce mode.
    0 processes are in complain mode.
    0 processes are unconfined but have a profile defined.
    
在 _complain_ 模式下，违反策略的访问将被允许，但该行为会被记录在日志中。 _complain_ 模式常用于了解程序正常运行所需要的权限，或是测试新撰写的配置文件是否合适。但是，需要注意的是，在配置文件中被设定为 _deny_ 的规则在 _complain_ 模式下仍然会强制执行。 

在 _enforce_ 模式下，违反策略的访问将被拒绝，并记录到日志中。 

###  解析配置文件

使用 `apparmor_parser` 以加载、卸载、重启、缓存或是统计配置文件。默认行为（`-a`）是以 _enforce_ 模式加载配置文件。要以 _complain_ 模式加载，请使用 `-C` 参数。要覆盖已有配置文件，使用 `-r` 参数。要删除配置文件，使用 `-R` 参数。每次操作也可能应用到多个配置文件上。参见 [apparmor_parser(8)](<https://man.archlinux.org/man/apparmor_parser.8>) 手册页面以了解详情。 

###  停用

要在当前会话临时停用 AppArmor，执行以下命令以停用所有配置文件： 
    
    # aa-teardown 
    
要永久停用 AppArmor 配置文件，请[停用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `apparmor.service`。要阻止内核加载 AppArmor，添加`apparmor=0`到 [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")、或者删除在[安装 AppArmor](<#%E5%AE%89%E8%A3%85>) 时添加的 `lsm=` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。 

##  配置

###  审计与生成配置文件

要创建新的配置文件，确保 [Audit 框架](</wzh/index.php?title=Audit_%E6%A1%86%E6%9E%B6&action=edit&redlink=1> "Audit 框架（页面不存在）")（英语：[Audit framework](<https://wiki.archlinux.org/title/Audit_framework> "en:Audit framework")）正在运行，因为 Arch Linux 使用 [systemd](<../zh-cn/Systemd.html> "Systemd")，内核日志默认不会保存到文件中。AppArmor 可以从用户空间的 auditd 进程抓取内核日志，从而协助编写配置文件。 

**注意：** AppArmor audit 消息使用 [AVC](<https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/security_guide/sec-Audit_Record_Types#sec-Audit_Record_Types>) 记录格式，使用 [ausearch](<https://man.archlinux.org/man/ausearch.8>) 搜索时可能破坏 audit 日志的解析。在此查看漏洞报告：[[2]](<https://bugs.launchpad.net/ubuntu/+source/audit/+bug/1117804>)， [[3]](<https://bugs.archlinux.org/task/60870>)，[[4]](<https://github.com/linux-audit/audit-userspace/issues/351>)

可以使用 [aa-genprof(8)](<https://man.archlinux.org/man/aa-genprof.8>) 或 [aa-autodep(8)](<https://man.archlinux.org/man/aa-autodep.8>) 创建新的 AppArmor 配置文件。新创建的配置文件默认处于 _complain_ 模式：此模式下，违反规则的行为仅会被记录，不会被拒绝。要交互式地创建配置文件，可以使用 [apparmor](<https://archlinux.org/packages/?name=apparmor>)包 包中的 [aa-logprof(8)](<https://man.archlinux.org/man/aa-logprof.8>)。配置完成后，请使用 [aa-enforce(8)](<https://man.archlinux.org/man/aa-enforce.8>) 将配置文件设置为 _enforce_ 模式。此模式下，配置文件中的规则将被严格执行。此外，可以重复执行 [aa-logprof(8)](<https://man.archlinux.org/man/aa-logprof.8>) 以添加额外的规则，也可以使用 [aa-complain(8)](<https://man.archlinux.org/man/aa-complain.8>) 将配置文件重新设置为 _complain_ 模式。可以在此找到更为详细的教程：[AppArmor wiki - Profiling with tools](<https://gitlab.com/apparmor/apparmor/wikis/Profiling_with_tools>)。 

需要注意的是，[aa-logprof(8)](<https://man.archlinux.org/man/aa-logprof.8>) 也提供 _deny_ 规则。不过根据 AppArmor 的设计逻辑，除非规则明确允许，否则任何行为都将被拒绝，因此严格来说没有必要使用 _deny_ 规则。不过， _deny_ 规则有以下两个用途： 

  1. _deny_ 规则的优先级比 _allow_ 规则更高，在 `/etc/apparmor.d/abstractions` 中的许多 [abstraction](<https://man.archlinux.org/man/extra/apparmor/apparmor.d.5.en##include_mechanism>) 中都有使用，用来阻断任何对重要文件（夹）的访问。这样做能防止创建 _allow_ 规则时可能的疏忽，使得配置文件不会太宽松。
  2. _deny_ 规则执行时不会在日志中记录，使得后续执行 _aa-logprof_ 时产生更为简洁的日志。需要注意的是，即使是在 _complain_ 模式下， _deny_ 规则也会被严格执行――因此，如果程序在 _complain_ 模式下还是会出错，应该检查在某一配置文件或其包含的 abstraction 中，是否有一条 _deny_ 规则导致了此问题。

另外，也可以手动编写配置文件， 在此查看教程：[AppArmor wiki - Profiling by hand](<https://gitlab.com/apparmor/apparmor/wikis/Profiling_by_hand>)。 

除了 `/etc/apparmor.d/` 中的默认配置文件外，在 `/usr/share/apparmor/extra-profiles/` 中还有更多预定义的配置文件。不过，这些配置文件并非一定适用于生产环境，因此可能需要手动修改或使用 [aa-logprof(8)](<https://man.archlinux.org/man/aa-logprof.8>)。 

也可以在 [apparmor.d](<https://github.com/roddhjav/apparmor.d>) 项目处找到额外的 AppArmor 规则集。不过，直到撰写本文时，该项目并非稳定可用。 

###  解读配置文件

配置文件是可读性很高的文本文件，保存在 `/etc/apparmor.d/` 下，定义了某个可执行文件的权限。以下是一个典型的配置文件： 
    
    /etc/apparmor.d/usr.bin.test
    
    #include <tunables/global>
    
    profile test /usr/lib/test/test_binary {
        #include <abstractions/base>
    
        # Main libraries and plugins
        /usr/share/TEST/** r,
        /usr/lib/TEST/** rm,
    
        # Configuration files and logs
        @{HOME}/.config/ r,
        @{HOME}/.config/TEST/** rw,
    }
    
以 `@` 符号开头的字符串是在 abstraction（`/etc/apparmor.d/abstractions/`），tunables（`/etc/apparmor.d/tunables/`或配置文件本身中定义的变量。`#include` 将其他配置文件中的内容包含到此配置文件中来。路径后的字符是[访问权限](<https://man.archlinux.org/man/extra/apparmor/apparmor.d.5.en#Access_Modes>)。使用 [AppArmor 的通配符语法](<https://man.archlinux.org/man/extra/apparmor/apparmor.d.5.en#Globbing>)以实现模式匹配。 

以下权限涵盖了最常见的使用场景： 

  * `r`——读取：读取数据
  * `w`——写入：创建，删除，写入文件，或是附加内容到文件尾部
  * `m`——映射：将文件映射为可执行内存
  * `x`——执行：执行文件。需要在前面加上[修饰符](<https://gitlab.com/apparmor/apparmor/wikis/AppArmor_Core_Policy_Reference#execute-rules>)，形如 `px`（执行时切换配置文件）

注意，定义的权限始终无法使程序获得大于原本在 DAC 中拥有的权限。 

此处仅提到了很浅显的内容。要查询更为详细的文档，请查看 [apparmor.d(5)](<https://man.archlinux.org/man/apparmor.d.5>) 手册页和[官方文档](<https://gitlab.com/apparmor/apparmor/wikis/AppArmor_Core_Policy_Reference>)。 

##  提示与技巧

###  拒绝访问后发出桌面通知

当 AppArmor 拒绝了程序的访问后，通知进程可以显示桌面通知。通过以下步骤，可以在登录时自动启动 _aa-notify_ 进程： 

安装 [Audit framework](</wzh/index.php?title=Audit_framework&action=edit&redlink=1> "Audit framework（页面不存在）") 并且[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")用户空间的Linux Audit进程。之后将你的桌面用户添加到 `audit` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")，从而允许其读取审计日志（audit logs）： 
    
    # groupadd -r audit
    # gpasswd -a _user_ audit
    
将 `audit` 用户组添加到 `auditd.conf`： 
    
    /etc/audit/auditd.conf
    
    log_group = audit

**注意：** 自 [audit](<https://archlinux.org/packages/?name=audit>)包 4.1.2-1 版本起，Arch Linux 有了一组 `tmpfiles.d` 配置文件，其中包含以下行: 
    
    /usr/lib/tmpfiles.d/audit.conf
    
    [...]
    d /var/log/audit 700 root root - -
    [...]
    z /var/log/audit 700 root root - -

这会让仅属于 `audit` 用户组的用户，在 `systemd-tmpfiles` 被调用后——例如使用pacman升级系统时，将不能读取目录 `/var/log/audit` 。你可通过创建以下文件覆盖此行为： 
    
    /etc/tmpfiles.d/audit.conf
    
    z /var/log/audit 750 root audit - -

**提示：** 也可以使用已有的系统用户组，例如 `wheel` 或 `adm`。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [python-notify2](<https://archlinux.org/packages/?name=python-notify2>)包 和 [python-psutil](<https://archlinux.org/packages/?name=python-psutil>)包。 

创建一个[桌面配置项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")并填入以下内容： 
    
    ~/.config/autostart/apparmor-notify.desktop
    
    [Desktop Entry]
    Type=Application
    Name=AppArmor Notify
    Comment=Receive on screen notifications of AppArmor denials
    TryExec=aa-notify
    Exec=aa-notify -p -s 1 -w 60 -f /var/log/audit/audit.log
    StartupNotify=false
    NoDisplay=true

重启并检查进程 `aa-notify` 是否运行： 
    
    $ pgrep -ax aa-notify
    
**注意：** 在一些特定的系统配置下，可能会有**海量** 的消息弹出。

要查询更多信息，参见 [aa-notify(8)](<https://man.archlinux.org/man/aa-notify.8>)。 

###  缓存配置文件以提高 AppArmor 启动速度

启动时，AppArmor 需要将配置文件转换为二进制格式，这一步可能会显著延长启动时间。可以用以下命令检查当前 AppArmor 的启动耗时： 
    
    $ systemd-analyze blame | grep apparmor
    
要启用 AppArmor 配置文件缓存功能，取消注释以下内容： 
    
    /etc/apparmor/parser.conf
    
    ## Turn creating/updating of the cache on by default
    write-cache

要改变默认的缓存存储位置，添加以下内容： 
    
    /etc/apparmor/parser.conf
    
    cache-loc=/path/to/location

**注意：** 自版本 2.13.1 起，默认的缓存存储位置已经由 `/etc/apparmor.d/cache.d/` 变为 `/var/cache/apparmor/`。

重启并再次检查 AppArmor 启动耗时，观察有无改善： 
    
    $ systemd-analyze blame | grep apparmor
    
##  排错

###  无法启动 Samba SMB/CIFS 服务

参见 [Samba#AppArmor_权限问题](<../zh-cn/Samba.html#AppArmor_%E6%9D%83%E9%99%90%E9%97%AE%E9%A2%98> "Samba")。 

###  升级到 AppArmor v4 后无法登录

在非常罕见的情况下，升级到 AppArmor v4 [会导致无法登录到任何账户](<https://gitlab.archlinux.org/archlinux/packaging/packages/apparmor/-/issues/2>)。 

[系统日志](<../zh-cn/Systemd/Journal.html> "Systemd/Journal")中可能包含类似如下内容的错误： 
    
    unix_chkpwd[1612]: check pass; user unknown
    unix_chkpwd[1612]: password check failed for user (john)
    gdm-password][1574]: pam_unix(gdm-password:auth): authentication failure; logname= uid=0 euid=0 tty=/dev/tty1 ruser= rhost=  user=john
    kernel: audit: type=1400 audit(1730844640.468:171): apparmor="DENIED" operation="capable" class="cap" profile="unix-chkpwd" pid=1612 comm="unix_chkpwd" capability=2  capname="dac_read_search"
    kernel: audit: type=1400 audit(1730844640.468:172): apparmor="DENIED" operation="capable" class="cap" profile="unix-chkpwd" pid=1612 comm="unix_chkpwd" capability=1  capname="dac_override"

这可能是由于 `root` 账户无法读取 `/etc/shadow` 和/或 `/etc/gshadow` 导致的（例如，这些文件的权限位（Permission bits）尚未设定）。因此，可以试试以下解决办法： 

  1. 重启，然后[停用 AppArmor](<#%E5%81%9C%E7%94%A8>)（在启动时编辑 [Bootloader](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "Bootloader") 参数，或者使用尚未启用 AppArmor 的 fallback 启动项）。
  2. 以 `root` 身份登录，然后设定正确的文件权限：`chmod 600 /etc/shadow /etc/gshadow`
  3. 再次重启。

###  不同 Linux 发行版之间的区别

大多数现有的资料是为运行在 Ubuntu 上的 AppArmor 编写的，而这些并不完全适用于 Arch Linux，因为 Ubuntu 为 AppArmor 应用了许多内核补丁。其他的发行版也可能使用自己的内核补丁，但 Arch Linux 使用的是尽可能接近主线的内核。 

例如，[apparmor.d(5)](<https://man.archlinux.org/man/apparmor.d.5>) 手册早在 v6.17 主线内核支持的前几年就已经记载了 `dbus` 规则[[5]](<https://web.git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c05e705812d1>)。但是，实际的支持程度也受到 [D-Bus 实现方式](<../zh-cn/D-Bus.html#Implementations> "Dbus") 的影响：[dbus](<https://archlinux.org/packages/?name=dbus>)包 软件包在构建时未启用 AppArmor 支持，而该支持是应用 dbus AppArmor 规则所必需的。 

Ubuntu 所使用的 AppArmor 特定内核补丁也可以在此处找到（将下文中的 `_jammy_` 替换为指定的 Ubuntu 版本代号）： 
    
    https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/_jammy_ /log/?qt=grep&q=UBUNTU%3A+SAUCE%3A+apparmor
    
受用户空间工具支持的 ABI 版本也可以在 `/etc/apparmor.d/abi/` 处找到。当前运行的内核所支持的 ABI 可以使用以下命令查看： 
    
    $ aa-features-abi --extract
    
或者 
    
    $ ls /sys/kernel/security/apparmor/features/
    
##  参见

  * [Wikipedia:AppArmor](<https://en.wikipedia.org/wiki/AppArmor> "wikipedia:AppArmor")
  * [AppArmor wiki](<https://gitlab.com/apparmor/apparmor/wikis/home>)
  * [AppArmor Core Policy Reference](<https://gitlab.com/apparmor/apparmor/wikis/AppArmor_Core_Policy_Reference>)——Detailed description of available options in a profile
  * [Ubuntu Tutorial](<https://ubuntuforums.org/showthread.php?t=1008906>)——General overview of available utilities and profile creation
  * [Ubuntu Wiki](<https://help.ubuntu.com/community/AppArmor>)——Basic command overview
  * [AppArmor Versions](<https://gitlab.com/apparmor/apparmor/wikis/AppArmor_versions>)——Version overview and links to the respective release notes
  * [Kernel Interfaces](<https://gitlab.com/apparmor/apparmor/wikis/Kernel_interfaces>)——Low level interfaces to the AppArmor kernel module
  * [wikipedia:Linux Security Modules](<https://en.wikipedia.org/wiki/Linux_Security_Modules> "wikipedia:Linux Security Modules")——Linux kernel module on which basis AppArmor is build upon
  * [AppArmor in openSUSE Security Guide](<https://doc.opensuse.org/documentation/leap/security/single-html/book-security/index.html#part-apparmor>)
