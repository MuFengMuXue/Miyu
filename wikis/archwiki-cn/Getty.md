**翻译状态：**

  * 本文（或部分内容）译自 [Getty](<https://wiki.archlinux.org/title/Getty> "arch:Getty")，最近一次同步于 2018-08-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/Getty?diff=0&oldid=532676>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Getty_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Display manager](<../zh-cn/Display_manager.html> "Display manager")

[getty](<https://en.wikipedia.org/wiki/getty_\(Unix\)> "w:getty \(Unix\)") 是管理终端线路及其所连终端的程序的通用名称。其目的是保护系统，防止未经授权的访问。通常，每个 getty 进程由 [systemd](<../zh-cn/Systemd.html> "Systemd") 启动，一个进程管理一条终端线路。 

##  安装

_agetty_ 是 Arch Linux 中默认的 getty 程序，它是 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 包的一部分。它在等待登录时修改 TTY 设置，使得换行符不会转换为 CR-LF，否则会使打印到控制台的消息产生“阶梯效应”。Agetty 管理着虚拟控制台，Arch Linux 中默认提供六个虚拟控制台。一般按 `Ctrl+Alt+F1` 到 `Ctrl+Alt+F6` 来访问它们。 

其他可选替代包括： 

  * **mingetty** — 一个允许自动登录的最小化 getty。

     [mingetty](<https://aur.archlinux.org/packages/mingetty/>)AUR || [mingetty](<https://aur.archlinux.org/packages/mingetty/>)AUR

  * **fbgetty** — 类似于 mingetty，支持帧缓冲。

     <http://projects.meuh.org/fbgetty/>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-18 ⓘ] || [fbgetty](<https://aur.archlinux.org/packages/fbgetty/>)AUR

  * **mgetty** — 在 Unix 下处理调制解调器各个方面功能的程序。

     <http://mgetty.greenie.net/> || [mgetty](<https://aur.archlinux.org/packages/mgetty/>)AUR

##  添加额外的虚拟控制台

打开 `/etc/systemd/logind.conf` 文件并将 **NAutoVTs=6** 设置为你想要在启动时得到的虚拟控制台数量。 

如果你想临时获取一个控制台，可以为所需的 TTY 启动一个 getty 服务，执行： 
    
    $ systemctl start getty@ttyN.service
    
##  自动登录到虚拟控制台

配置自动登录要使用 systemd 的[附加代码片段 (drop-in snippet)](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd") 功能来重写传递给 _agetty_ 的默认参数。 

虚拟控制台和串口控制台的配置是不同的。大多数情况下，你应该是想在虚拟控制台下设置自动登录（这种控制台的设备名称为 `tty _N_`，其中 `_N_` 是一个数字）。串口控制台的自动登录配置稍有不同，它们的设备名称类似于 `ttyS _N_`，其中 `_N_` 是一个数字。 

###  虚拟控制台

**注意：**[根据用户报告](<https://bbs.archlinux.org/viewtopic.php?id=238576>)这种方法可能会影响系统休眠。

要[修改现存单元文件](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")，可以手动创建下列附加文件，或执行 `systemctl edit getty@tty1` 并输入附加代码片段 (drop-in snippet) 的内容： 
    
    /etc/systemd/system/getty@tty1.service.d/override.conf
    
    [Service]
    ExecStart=
    ExecStart=-/usr/bin/agetty --autologin _username_ --noclear %I $TERM

**提示：** 默认 `getty@.service` 中的 `Type=idle` 选项将会推迟该服务的启动时间，直到所有任务（该单元的前置任务）已经完成，防止启动信息淹没了登录提示符。当 [自动启动 X](</wzh/index.php?title=Start_X_at_login&action=edit&redlink=1> "Start X at login（页面不存在）") 时，可以通过添加 `Type=simple` 到 [附加代码片段 (drop-in snippet)](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd") 来立即启动 `getty@tty1.service`，因为此时 init 进程和 _startx_ 都被 [屏蔽](<../zh-cn/Silent_boot.html> "Silent boot") 了输出，避免残留启动时的信息。

如果你想用 _tty_ 而不是 _tty1_ ，请参阅 [Systemd 常见问题](<../zh-cn/Systemd_FAQ.html#%E5%A6%82%E4%BD%95%E4%BF%AE%E6%94%B9%E9%BB%98%E8%AE%A4%E7%9A%84_tty_%E6%8E%A7%E5%88%B6%E5%8F%B0%EF%BC%88getty%EF%BC%89%E6%95%B0%E9%87%8F%EF%BC%9F> "Systemd FAQ")。 

###  串口控制台

创建以下文件（及目录）： 
    
    /etc/systemd/system/serial-getty@ttyS0.service.d/autologin.conf
    
    [Service]
    ExecStart=
    ExecStart=-/usr/bin/agetty --autologin _username_ -s %I 115200,38400,9600 vt102

###  Nspawn 控制台

要为 [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn") 容器配置自动登录，需要重写 _console-getty_ 服务： 
    
    /etc/systemd/system/console-getty.service.d/override.conf
    
    [Service]
    ExecStart=
    ExecStart=-/sbin/agetty --noclear --autologin _username_ --keep-baud console 115200,38400,9600 $TERM

##  将引导消息保留在 tty1 上

默认情况下，Arch 会启动 `getty@tty1` 服务。该服务单元文件已经写入了 `--noclear` 参数，它可以阻止 agetty 清空屏幕。但是 [systemd](<../zh-cn/Systemd.html> "Systemd") 会在启动该服务之前清空屏幕。要关闭这项特性，请创建 `/etc/systemd/system/getty@tty1.service.d/noclear.conf` 文件： 
    
    /etc/systemd/system/getty@tty1.service.d/noclear.conf
    
    [Service]
    TTYVTDisallocate=no

这将仅改写 TTY1 上的 _agetty_ 的 `TTYVTDisallocate` 参数，并保持全局服务文件 `/usr/lib/systemd/system/getty@.service` 不变。可参阅 [Systemd#修改现存单元文件](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")。 

**注意：**

  * 确保从 [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") 中移除了 `quiet`。
  * KMS 晚启动可能会造成部分早期启动信息丢失。请参阅 [Kernel mode setting#KMS 早启动](<../zh-cn/Kernel_mode_setting.html#KMS_%E6%97%A9%E5%90%AF%E5%8A%A8> "Kernel mode setting") 或 [Kernel mode setting#禁用 KMS](<../zh-cn/Kernel_mode_setting.html#%E7%A6%81%E7%94%A8_KMS> "Kernel mode setting")。

##  参考资料

  * [Systemd#更改开机默认启动目标](<../zh-cn/Systemd.html#%E6%9B%B4%E6%94%B9%E5%BC%80%E6%9C%BA%E9%BB%98%E8%AE%A4%E5%90%AF%E5%8A%A8%E7%9B%AE%E6%A0%87> "Systemd")
  * [The TTY demystified](<https://www.linusakesson.net/programming/tty/>)
  * [Wikipedia:Tty (unix)](<https://en.wikipedia.org/wiki/Tty_\(unix\)> "wikipedia:Tty \(unix\)")
