**翻译状态：**

  * 本文（或部分内容）译自 [Powertop](<https://wiki.archlinux.org/title/Powertop> "arch:Powertop")，最近一次同步于 2024-06-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/Powertop?diff=0&oldid=806842>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Powertop_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [电源管理](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86.html> "电源管理")
  * [Laptop Mode Tools](<../zh-cn/Laptop_Mode_Tools.html> "Laptop Mode Tools")
  * [TLP](<../zh-cn/TLP.html> "TLP")

[Powertop](<https://github.com/fenrus75/powertop>) 是一个 Intel 提供的在用户空间、内核和硬件层面的节电工具。它可以监视进程，并显示哪些进程利用 CPU 并从空闲状态唤醒它，从而识别具有特殊高功率需求的应用程序。 

##  安装

安装 [powertop](<https://archlinux.org/packages/?name=powertop>)包 或最新开发版本 [powertop-git](<https://aur.archlinux.org/packages/powertop-git/>)AUR。 

##  使用

Powertop 的交互模式可以通过以下方式调用： 
    
    # powertop
    
在交互模式下，您可以在 **Tunables** 和 **WakeUp** 选项卡中修改建议的设置，并可以在 **Overview** 选项卡中监视它们对功耗的影响。但是，任何设置都不会保留，重启后会丢失。 

###  生成报告

Powertop 可以生成 CSV 或 HTML 格式的报告。HTML 导出的是一个交互式文档，显示推荐的设置。在生成报告之前，请确保重启以恢复为系统默认设置！ 

您也可以通过遵循以下步骤来提取推荐的参数： 

  1. 使用 Powertop 生成参数报告：
         
         # powertop --html=powerreport.html

  2. 在您喜欢的网页浏览器中打开报告。报告的 **Tuning** 标签现在显示了工具建议节省电量应用的实际参数。提取命令： 
         
         $ awk -F '</?td ?>' '/tune/ { print $4 }' powerreport.html

较新版本的 Powertop 包括了 `--auto-tune-dump` 选项，它将输出 Powertop 的 `--auto-tune` 将运行的命令。如果您不想运行 Powertop 的所有建议，这在脚本中非常有用。 

###  保存设置

有两种方法保存其设置，使其在重启后依然应用先前的设置。 

  * **推荐：** 使用 [Kernel modules](<../zh-cn/Kernel_modules.html> "Kernel modules")、 [Udev](<../zh-cn/Udev.html> "Udev") 和[sysctl](<../zh-cn/Sysctl.html> "Sysctl")来使其在系统启动时应用设置。相关细节请看[Power management](<../zh-cn/Power_management.html> "Power management")。您也可以使用 [powertop-to-tmpfile](<https://aur.archlinux.org/packages/powertop-to-tmpfile/>)AUR 辅助工具，通过 [systemd-tmpfiles](<../zh-cn/Systemd.html#systemd-tmpfiles_-_%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6> "Systemd") 应用设置。
  * 使用 Powertop 的 `--auto-tune` 参数，该参数会使得所有的可调整项变成 GOOD,为使其在系统启动时就生效，可使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务使其开启自启动。添加该文件并[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动")该服务：

    /etc/systemd/system/powertop.service
    
    [Unit]
    Description=Powertop tunings
    
    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=/usr/bin/powertop --auto-tune
    
    [Install]
    WantedBy=multi-user.target

您也可以将这一行添加到 `[Service]` 部分，以防止在启动时已经连接到您的系统的鼠标断开连接。 
    
    ExecStartPost=/bin/sh -c 'for f in $(grep -l "Mouse" /sys/bus/usb/devices/*/product | sed "s/product/power\\/control/"); do echo on >| "$f"; done'
    
##  疑难解决

### Error: Cannot load from file

如果在启动 powertop 时遇到如下错误，可能是因为 powertop 没有收集到足够的数据，请在电池供电的情况下多运行一段时间，收集更多的数据。 
    
    Loaded 39 prior measurements
    Cannot load from file /var/cache/powertop/saved_parameters.powertop
    Cannot load from file /var/cache/powertop/saved_parameters.powertop
    
###  校准测量数据

如果测量结果不准确，可能需要先校准 powertop: 运行 powertop 时增加 `--calibrate` 参数. 

**注意：** 校准时会开关背光、wifi 等功能，在校准时不要触碰机器。
    
    # powertop --calibrate
    
##  参见

  * [Project repository](<https://github.com/fenrus75/powertop>)
  * [Wikipedia article](<https://en.wikipedia.org/wiki/Powertop> "wikipedia:Powertop")
