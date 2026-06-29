[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Uvesafb](<../zh-cn/Talk:Uvesafb.html>)讨论)

相关文章

  * [Kernel modules](<../zh-cn/Kernel_modules.html> "Kernel modules")
  * [Kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters")
  * [sysctl](<../zh-cn/Sysctl.html> "Sysctl")

**翻译状态：**

  * 本文（或部分内容）译自 [Uvesafb](<https://wiki.archlinux.org/title/Uvesafb> "arch:Uvesafb")，最近一次同步于 2015-02-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Uvesafb?diff=0&oldid=359183>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Uvesafb_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last updated in 2015（在 [Talk:Uvesafb#](<../zh-cn/Talk:Uvesafb.html>) 中讨论）

与其他 framebuffer 驱动不同，uvesafb 需要一个叫做 v86d 的用户空间虚拟化守护进程。在 x86 机器上模拟 x86 代码看起来很愚蠢，但若是想在其他架构上使用 framebuffer 代码这就显得很重要了 (尤其是非 x86 架构). 一个新的 framebuffer 驱动已添加到 2.6.24 版的内核中。它比标准的 vesafb 有更多的特性，包括: 

  1. 延迟后适当间隔和硬件悬停。
  2. 支持自定义分辨率，就像使用系统 BIOS 一样。

vesafb 支持的硬件它应该都支持。 

##  安装

从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") [安装](<../zh-cn/Pacman.html> "Pacman") [v86d](<https://aur.archlinux.org/packages/v86d/>)AUR. 

##  准备系统

记得从引导器配置中删除一切与 framebuffer 有关的内核启动参数以防止 vesafb framebuffer 加载。 
    
    $ grep vga /proc/cmdline
    $ grep -ir vga /etc/modprobe.d/
    
应该不会返回错误。如果你在别处还有 `vga=` 选项，记得移除。 

### GRUB

**注意：** 这可能不起作用。

编辑 `/etc/default/grub`, 注释掉 `GRUB_GFXPAYLOAD_LINUX=keep` 行。 

然后用标准脚本生成 `grub.cfg`: 
    
    # grub-mkconfig -o /boot/grub/grub.cfg
    
### GRUB legacy

从 `/boot/grub/menu.lst` 的 kernel 行移除所有对 `vga=xxx` 的引用以便 uvesafb 正常工作。 

### Systemd

使用 systemd 的话，往 `/etc/mkinitcpio.conf` 的 HOOKS 部分添加 v86d. 这能让 uvesafb 在启动时接管工作。 
    
    HOOKS="base udev v86d ..."
    
##  配置 uvesafb

###  规定分辨率

uvesafb 的配置在 `/usr/lib/modprobe.d/uvesafb.conf`: 
    
    # This file sets the parameters for uvesafb module.
    # The following format should be used:
    # options uvesafb mode_option=<xres>x<yres>[-<bpp>][@<refresh>] scroll=<ywrap|ypan|redraw> ...
    #
    # For more details see:
    # <https://www.kernel.org/doc/html/latest/fb/uvesafb.html>
    #
    options uvesafb mode_option=1280x800-32 scroll=ywrap
    
`mode_option` 的文献可见于 [[1]](<https://www.kernel.org/doc/html/latest/fb/modedb.html>)。 

为避免你的设置在升级时被覆盖，把下面的文件复制到 `/etc/modprobe.d/uvesafb.conf`: 
    
    # cp /usr/lib/modprobe.d/uvesafb.conf /etc/modprobe.d/uvesafb.conf
    
然后往 `/etc/mkinitcpio.conf` 的 FILES 部分添加你的配置文件，比如: 
    
    FILES="/etc/modprobe.d/uvesafb.conf"
    
为使变更生效，你需要重新生成 _initramfs_ 镜像。 
    
    # mkinitcpio -p linux
    
重启后变更生效。 

###  调整分辨率

通过以下命令可得到可用分辨率: 
    
    $ cat /sys/bus/platform/drivers/uvesafb/uvesafb.0/vbe_modes
    
可根据得到的条目来修改 `/usr/lib/modprobe.d/uvesafb.conf`. 

###  检查当前分辨率

下面的任一命令都可以用来检查当前 framebuffer 分辨率: 
    
    $ cat /sys/devices/virtual/graphics/fbcon/subsystem/fb0/virtual_size
    
    $ cat /sys/class/graphics/fb0/virtual_size
    
##  Uvesafb 内核参数

如果你编译了个人定制内核，你也可以把 uvesafb 编译进内核，之后比如通过 `/etc/rc.local` 运行 v86d。这种情况下，该选项能够以 video=uvesafb:<options> 格式传递[内核参数](<../zh-cn/Kernel_parameters.html> "Kernel parameters")。请注意当你如下把 uvesafb 和 915resolution 结合起来时，这个方案是无效的。 

##  Uvesafb 和 915resolution

接下来我们要处理一个更复杂的情形。许多为笔记本设计的 Intel 图形芯片组被报告说有一个易出 bug 的 BIOS，它甚至无法支持宽屏的原生主分辨率！为此创造了 915resolution, 用于在启动时给 BIOS 打补丁以让 X server 支持宽屏的分辨率。 目前，X server 能在没有 915resolution 的情况下完成这些。然而，915resolution 能与 uvesafb 结合来获得一个支持宽屏的 framebuffer, 根本就不需要启动 X 了。这种情况下，运行完 915resolution 之后我们需要加载 uvesafb 来让它工作在正常的分辨率之下。 

### 915resolution-static

在这种情形中，915resolution 需要被静态编译 (因为它要包含在 initramfs 中，因此不能有任何到外部库文件的连接). 所以你**不能** 使用 [community] 源中的 915resolution 软件包，应该转而使用 AUR 中的 [915resolution-static](<https://aur.archlinux.org/packages/915resolution-static/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]. 它静态编译了 915resolution 并提供了一个它的钩子，所以你在加载 uvesafb 之前就能运行 915resolution 并获得正确的分辨率。所以通过 makepkg 和 [pacman](<../zh-cn/Pacman.html> "Pacman") 安装 915resolution-static . 

###  分辨率

你需要编辑 915resolution 钩子以确定你要替换的 BIOS 模式和你想要的分辨率。你可以用如下命令得到 915resolution 所有选项的信息: 
    
    $ 915resolution -h
    
编辑 `/lib/initcpio/hooks/915resolution` 并修改 915resolution 的选项: 
    
    run_hook ()
    {
       msg -n ":: Patching the VBIOS..."
       /usr/sbin/915resolution 5c 1280 800
       msg "done."
    }
    
默认的 5c 用来替换成你要的 BIOS 模式的代码。使用命令 `915resolution -l` 来得到所有可用 BIOS 图形模式的代码。 

**注意：** 你可能会选择你 _并不需要_ 的代码 (framebuffer 或是 X 也都不需要), 因为 915resolution 会把它替换成用户选定的模式。上例中，`1280 800` 是新的所需分辨率。

###  钩子阵列

添加 915resolution 钩子并在其后添加 v86d 钩子到 `/etc/mkinitcpio.conf` 的 HOOKS 部分。务必位于 keymap 之前，以便从悬停和文件系统中恢复。 
    
    HOOKS="base udev 915resolution v86d ..."
    
之后用 mkinitcpio 重新生成 initramfs (替换成你自己的预设文件): 
    
    mkinitcpio -p linux
    
##  疑难问题

###  Uvesafb 无法保留内存

检查你是否忘记删除了 `vga=xxx` 内核参数 -- 它把 UVESA framebuffer 覆盖为标准 VESA. 

###  Error: "pci_root PNP0A08:00 address space collision + Uvesafb cannot reserve memory"

这发生在 Acer Aspire One 751h 上使用 2.6.34-ARCH 内核时; 这是否在其他系统上也有我们不得而知。即使用另一份 uvesafb 设置调制 framebuffer, uvesafb 也不能保留必要的内存区域。 

你可以通过在引导器配置里加上如下内核参数来解决。 
    
    pci=nocrs
    
##  另见

  * [Uvesafb Kernel Page](<https://www.kernel.org/doc/html/latest/fb/uvesafb.html>)
  * [Gentoo's uvesafb Page](<https://web.archive.org/web/20121118062504/http://dev.gentoo.org:80/~spock/projects/uvesafb/>)
  * [VESA mode numbers](<http://infosnews.5cz.de/VESA_BIOS_Extensions.html#VBE_mode_numbers>)
