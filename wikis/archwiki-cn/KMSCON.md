**翻译状态：**

  * 本文（或部分内容）译自 [KMSCON](<https://wiki.archlinux.org/title/KMSCON> "arch:KMSCON")，最近一次同步于 2023-03-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/KMSCON?diff=0&oldid=769075>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/KMSCON_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Kernel mode setting](<../zh-cn/Kernel_mode_setting.html> "Kernel mode setting")
  * [systemd](<../zh-cn/Systemd.html> "Systemd")

Kmscon 是一个简单的、基于 Linux [内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")的终端模拟器，尝试用用户空间终端代替内核的虚拟终端（VT）。[[1]](<#cite_note-1>)

##  特性

KMSCON 能作为 Linux 内核内置终端的一个完整替代，它具有以下功能： 

  * 完整的 vt220 to vt510 实现。
  * 完整的国际化支持： 
    * Kmscon 支持打印全部 Unicode 字符，包括中日韩文字。
    * Kmscon 通过 libxkbcommon 对国际键盘布局提供支持，所以人们可以使用 X 支持的所有键盘布局。
  * 硬件加速渲染。
  * 支持 [multi-seat](<https://www.freedesktop.org/wiki/Software/systemd/multiseat/>)。

**注意：** 要允许 root 用户通过 kmscon 登录，你需要移除或注释 `/etc/pam.d/login` 中相应行来停用 `pam_securetty` 模块。 

##  安装

虽然名字里带有 KMS，kmscon 并非硬性依赖 [KMS](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "KMS")。Kmscon 支持的视频后端如下：drm3d（Linux DRM 硬解后端）、fbdev（Linux fbdev 视频后端）。请确保你的系统支持其中之一。 

安装 [kmscon](<https://archlinux.org/packages/?name=kmscon>)包，或者安装最新开发版 [kmscon-git](<https://aur.archlinux.org/packages/kmscon-git/>)AUR。 

在 tty1 上一般有特殊的 systemd 配置。出于保守的策略，你可以继续在 tty1 上使用传统的 getty 而只在其他虚拟终端上运行 kmscon ，或者你可以用 kmscon 替换 getty。 

要在 tty1 上启用 kmscon： 
    
    # systemctl disable getty@tty1.service
    # systemctl enable kmsconvt@tty1.service
    
重新启动即可生效。 

要在所有的虚拟终端上启用 kmscon : 
    
    # ln -s /usr/lib/systemd/system/kmsconvt\@.service /etc/systemd/system/autovt\@.service
    
这使 [systemd](<https://archlinux.org/packages/?name=systemd>)包 在每个虚拟终端上启动 kmscon 而不是 agetty，同时使 _systemd-logind_ 使用 `kmsconvt@.service` 而不是 `getty@.service` 打开新的虚拟终端。不过使用 `getty@.service` 的 systemd 单元不受影响。 

如果 _kmscon_ 无法启动，它会尝试启动 `getty@.service` ，此外没有虚拟终端可用时这个单元不会启动。 

**警告：** 如果你在所有的终端替换了 getty ，请在重新启动之前确认 _kmscon_ 可用 ！不然你只能用 Live CD 一类的介质恢复系统了。

##  中日韩文字支持

Kmscon 通过默认的字体引擎 [pango](<https://archlinux.org/packages/?name=pango>)包 支持渲染中日韩文字。但是， 必须为 [fontconfig](<https://archlinux.org/packages/?name=fontconfig>)包 设置**全局** 配置，来将等宽字体映射到合适的中日韩字体上。我们为中文用户提供如下配置模板。此模板可以满足中文字体渲染要求： 
    
    /etc/fonts/conf.d/99-kmscon.conf
    
    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
    <fontconfig>
    <match>
            <test name="family"><string>monospace</string></test>
            <edit name="family" mode="prepend" binding="strong">
                    <string>DejaVu Sans Mono</string>
                    <string>WenQuanYi Micro Hei Mono</string>
            </edit>
    </match>
    </fontconfig>
    
还可以将以下行加入 `/etc/kmscon/kmscon.conf` 来配置 kmscon 全局使用这些字体： 
    
    /etc/kmscon/kmscon.conf
    
    font-name=DejaVu Sans Mono, WenQuanYi Micro Hei Mono
    font-size=14
    
你需要安装 [ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包 和 [wqy-microhei](<https://archlinux.org/packages/?name=wqy-microhei>)包，它们都可以在官方仓库中找到。 

##  疑难解答

###  在切换 Xorg 和 kmscon 时遇到问题

如果你在切换 [Xorg](<../zh-cn/Xorg.html> "Xorg") 和 kmscon 时遇到问题，试着把 `hwaccel` 添加到 `/etc/kmscon/kmscon.conf` 中。 这个文件和目录不在包内，因此你需要手动创建它们，或者你可以[编辑 systemd 单元文件](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")。 
    
    ExecStart=/usr/bin/kmscon "--vt=%I" --seats=seat0 --no-switchvt --font-name Terminus --font-size 12 **--hwaccel** --drm
    
###  无法控制声音

在版本 7 中，如果你不能控制声音，把你的用户添加到 `audio` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")中。不过要注意这么做的[缺点](<../zh-cn/ALSA.html#%E5%AE%89%E8%A3%85> "Alsa")。 

###  Vim 无法清空终端输出

Vim 可能会在启动时不清除终端输出，这时仍然可以编辑文件，但只有更改文本后才能看到文本。解决方法是，尝试设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `TERM = vt220`。 另外，其它类似于 vim 的编辑器（例如 [vi](<https://archlinux.org/packages/?name=vi>)包 或 [Neovim](<../zh-cn/Neovim.html> "Neovim")）可能会正常工作。 

###  自动登录

你可以在 `/etc/kmscon/kmscon.conf`中添加以下内容来自动登录用户（不需要输入密码）： 
    
    # 你可以按需修改以下命令
    
    # 例：以 root 用户直接登录（非 systemd 会话）
    login=/bin/bash --login
    
    # 例：以指定用户直接登录（正常 systemd 会话）
    login=/usr/bin/machinectl -q shell 你的用户名@
    
###  HiDPI 支持

使用 `Ctrl++`、`Ctrl+Shift+=`、`Ctrl+-` 快捷键可以实时更改字体大小。也可以在 `/etc/kmscon/kmscon.conf` 里设置 font-dpi 和 font-size 选项，例如 `font-dpi=288`。288 = 96 * 3，也就是三倍大小。96 是默认值。 

##  参考资料

  1. [↑](<#cite_ref-1>) 来自[该项目代码库](<https://cgit.freedesktop.org/~dvdhrm/kmscon/tree/README>)的介绍
