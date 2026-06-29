**翻译状态：**

  * 本文（或部分内容）译自 [Archinstall](<https://wiki.archlinux.org/title/Archinstall> "arch:Archinstall")，最近一次同步于 2024-12-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Archinstall?diff=0&oldid=823647>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Archinstall_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[archinstall](<https://archinstall.archlinux.page/>) 是一个用于自动化 [Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux") 安装过程的帮助库。它和其它的预配置安装程序一起打包，作为“向导”安装程序。 

本文不讨论将 archinstall 作为 Python 库使用的情况。这种情况请参看[官方文档](<https://archinstall.archlinux.page/installing/python.html>)。 

**警告：**

  * _archinstall_ 以纯文本形式存储所有用户和（辅助）磁盘加密的密码。[[1]](<https://github.com/archlinux/archinstall/issues/1111>)
  * _archinstall_ 的默认配置与[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")不同。如使用 archinstall 安装系统出现问题的话，请在反馈中注明，并提供 `/var/log/archinstall/install.log`。
  * 如果选择单独的 `/home` 分区， _archinstall_ 创建的根分区会小于[推荐的 23-32 GiB](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")。

##  运行安装程序

首先，按照[安装指南#安装前的准备](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#%E5%AE%89%E8%A3%85%E5%89%8D%E7%9A%84%E5%87%86%E5%A4%87> "安装指南")中的[启动到 Live 环境](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#%E5%90%AF%E5%8A%A8%E5%88%B0_Live_%E7%8E%AF%E5%A2%83> "安装指南")操作。[archinstall](<https://archlinux.org/packages/?name=archinstall>)包 包是 live 镜像的一部分，因此可以直接运行： 
    
    # archinstall
    
向导安装程序将执行多个步骤，并要求用户输入，参见[官方文档](<https://archinstall.archlinux.page/installing/guided.html>)。 

**警告：** 将 root 密码留空会禁用 root 账户，使用 [sudo](<../zh-cn/Sudo.html> "Sudo") 来提升权限。这可能会导致你将自己锁定在系统之外，因此可能不需要这样做。请参阅[Sudo#禁止 root 登录](<../zh-cn/Sudo.html#%E7%A6%81%E6%AD%A2root%E7%99%BB%E5%BD%95> "Sudo")。

**注意：** 本安装程序可使用 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 配置目标系统的有线网络，或把[ISO](<https://en.wikipedia.org/wiki/Optical_disc_image> "wikipedia:Optical disc image")中的网络配置复制到目标系统中。也就是说，如果你使用 [iwd#iwctl](<../zh-cn/Iwd.html#iwctl> "Iwd") 配置无线网络的话，包括网络登录密码在内的配置信息会被复制到目标系统中。与此同时，安装程序也会将安装介质里的有线网络配置复制到目标系统中。

附加软件包也可以通过在 `Write additional packages to install` 选项后输入软件包名称安装。建议在此处或安装完成后的 chroot 环境中安装必需的驱动软件包，以免安装成功后无法正常进入系统。 

安装完成后会提示是否进入 chroot 环境，通过 chroot 可以在进入系统前进行额外的配置。 

###  配置文件

archinstall 包含一些[配置文件](<https://gitlab.archlinux.org/archlinux/archinstall/-/tree/master/archinstall/default_profiles>)，也就是在基本系统安装完成后，安装的一系列软件包，以及一些预配置文件。 

**警告：** 配置文件是专门为 _archinstall_ 编写的，不受软件包维护者支持。在使用前请仔细查看每个配置文件的细节。

##  参见

  * [python-archinstall: guided](<https://archinstall.archlinux.page/installing/guided.html>)
