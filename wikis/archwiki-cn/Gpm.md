**翻译状态：**

  * 本文（或部分内容）译自 [General purpose mouse](<https://wiki.archlinux.org/title/General_purpose_mouse> "arch:General purpose mouse")，最近一次同步于 2024-08-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/General_purpose_mouse?diff=0&oldid=765317>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/General_purpose_mouse_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

GPM（General Purpose Mouse，通用鼠标）是为 Linux 虚拟控制台（TTY）提供鼠标支持的守护进程。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gpm](<https://archlinux.org/packages/?name=gpm>)包 软件包。有关笔记本电脑上的触摸板支持，请参阅[笔记本电脑#触摸板](<../zh-cn/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91.html#%E8%A7%A6%E6%91%B8%E6%9D%BF> "笔记本电脑")。 

##  配置

`-m` 参数用于声明要使用的鼠标。`-t` 参数用于定义鼠标类型。要获取 `-t` 选项的可用类型列表，请使用 `-t help` 运行 `gpm`。 
    
    # gpm -m /dev/input/mice -t help
    
[gpm](<https://archlinux.org/packages/?name=gpm>)包 软件包需要使用一些参数启动。这些参数可以通过[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")文件 `/etc/conf.d/gpm` 记录，也可以在直接运行 _gpm_ 时使用。`gpm.service` 默认包含 USB 鼠标的参数（`ExecStart=/usr/bin/gpm -m /dev/input/mice -t imps2`）。 

显然，如果需要为其他鼠标类型使用该服务，应该对其进行编辑，最好以 [systemd 友好的方式](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")。 

  * PS/2 鼠标：
        
        -m /dev/psaux -t ps2

  * IBM Trackpoint（“小红点”）：
        
        -m /dev/input/mice -t ps2

**注意：** 如果鼠标只有 2 个按钮（无中键），则将 `-2` 传递给 `GPM_ARGS`，第二个按钮将执行粘贴功能。

找到合适的配置后，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `gpm.service`。 

更多信息见 [gpm(8)](<https://man.archlinux.org/man/gpm.8>)。 

###  QEMU 或 VirtualBox

QEMU 和 VirtualBox 默认模拟的鼠标在使用 _gpm_ 和 X 时存在严重的定位和点击问题。鼠标的定位与主机失去同步，因此无法在不反复退出并重新进入窗口的情况下悬停于某些区域。点击的位置与光标显示的位置不符。 

QEMU 和 VirtualBox 通过提供 USB 平板设备的模拟来解决此问题，该模拟提供了绝对定位功能。（[libvirt](<https://archlinux.org/packages/?name=libvirt>)包 自动使用这种方式。） 

然而， _gpm_ 只知道如何以相对定位模式使用模拟的鼠标，因此这些问题依然存在。尝试通过 `-t` 使用其他类型也均无法正确工作。 

[gpm-vm](<https://aur.archlinux.org/packages/gpm-vm/>)AUR 包含了一个已有数年的[拉取请求](<https://github.com/telmich/gpm/pull/23>)，用于添加 VirtualBox 的 USB 平板支持（在 QEMU 下也能工作），并修改了 `gpm.service` 文件以默认启用它。 

你可能需要更改所使用的事件。给 _gpm_ 原始的 `-m /dev/input/mice` 不会起作用。默认情况下： 
    
    /etc/gpm-vm.conf
    
    event="/dev/input/event2"

你可以通过安装 [evtest](<https://archlinux.org/packages/?name=evtest>)包 并运行以下命令来确定要使用的事件： 
    
    # evtest
    
    ...
    /dev/input/event2:      QEMU QEMU USB Tablet
    ...
    
如果需要给 _gpm_ 添加额外的选项，可以在 `/etc/gpm-vm.conf` 中设置 `additional_args`。 

一旦找到合适的配置，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `gpm.service`。 

##  参见

  * [Gentoo:GPM](<https://wiki.gentoo.org/wiki/GPM> "gentoo:GPM")
  * [consolation](<https://aur.archlinux.org/packages/consolation/>)AUR 基于 libinput 的替代品
