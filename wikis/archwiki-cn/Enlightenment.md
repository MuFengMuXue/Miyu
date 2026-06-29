**翻译状态：**

  * 本文（或部分内容）译自 [Enlightenment](<https://wiki.archlinux.org/title/Enlightenment> "arch:Enlightenment")，最近一次同步于 2020-02-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Enlightenment?diff=0&oldid=585161>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Enlightenment_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")

## Enlightenment

这个软件包提供了 [Enlightenment](<https://www.enlightenment.org/>) 的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")及其构建库 EFL（Enlightenment Foundation Libraries）。后者提供了额外的桌面环境特性，如工具包、对象画布和抽象对象。Enlightenment 从 2005 年开始开发，2011 年 2 月发布 1.0 稳定版本。 

###  安装

可[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")同名软件包 [enlightenment](<https://archlinux.org/packages/?name=enlightenment>)包 。 

还可以安装 [terminology](<https://archlinux.org/packages/?name=terminology>)包，这是一个基于 EFL 的终端仿真器。 

####  从 AUR 安装

**警告：** 其中某些软件包使用不稳定的开发版代码，请风险自担。

开发版的软件包源码及其依赖的包构建文件可以通过安装 [enlightenment-git](<https://aur.archlinux.org/packages/enlightenment-git/>)AUR 获得。 以下是基于 EFL 的应用，大部分是开发版本，尚未正式发布： 

  * [ecrire-git](<https://aur.archlinux.org/packages/ecrire-git/>)AUR – Ecrire 文本编辑器
  * [edi](<https://aur.archlinux.org/packages/edi/>)AUR – 基于 EFL 的集成开发环境(IDE)
  * [eluminance-git](<https://aur.archlinux.org/packages/eluminance-git/>)AUR – Eluminance 图片浏览器
  * [enjoy-git](<https://aur.archlinux.org/packages/enjoy-git/>)AUR – Enjoy 音乐播放器
  * [eperiodique](<https://aur.archlinux.org/packages/eperiodique/>)AUR – [Eperiodique](<http://eperiodique.sourceforge.net/>) periodic 表格查看器
  * [ephoto](<https://archlinux.org/packages/?name=ephoto>)包 and [ephoto-git](<https://aur.archlinux.org/packages/ephoto-git/>)AUR – [Ephoto](<https://smhouston.us/ephoto/>)图片查看器
  * [epour](<https://aur.archlinux.org/packages/epour/>)AUR – 基于 EFL 的种子(torrent)客户端
  * [epymc-git](<https://aur.archlinux.org/packages/epymc-git/>)AUR – E Python 多媒体中心
  * [equate-git](<https://aur.archlinux.org/packages/equate-git/>)AUR – Equate 计算器
  * [eruler-git](<https://aur.archlinux.org/packages/eruler-git/>)AUR – Eruler 屏幕尺和测量工具
  * [efbb-git](<https://aur.archlinux.org/packages/efbb-git/>)AUR – Escape from Booty Bay 类似《愤怒的小鸟》的游戏
  * [elemines-git](<https://aur.archlinux.org/packages/elemines-git/>)AUR – [Elemines](<http://elemines.sourceforge.net/>) 《扫雷》类型的游戏
  * [rage](<https://archlinux.org/packages/?name=rage>)包 和 [rage-git](<https://aur.archlinux.org/packages/rage-git/>)AUR – Rage 视频播放器
  * [terminology-git](<https://aur.archlinux.org/packages/terminology-git/>)AUR – [terminology](<https://archlinux.org/packages/?name=terminology>)包 的当前 git 主分支版本

###  启动 Enlightenment

只需从喜欢的[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")中选择 _Enlightenment_ ，或配置好 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 即可从控制台启动。 

#### Entrance

**警告：** Entrance 仍旧处于高度实验性阶段，尚未被 systemd 完全支持 ，若要使用请自担风险。

Enlightenment 提供了一个名为 Entrance 的新显示管理器，由 [entrance-git](<https://aur.archlinux.org/packages/entrance-git/>)AUR 提供。Entrance 十分精巧，它用 `/etc/entrance.conf` 管理配置。可以通过 [systemd](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") 启用 `entrance.service` 服务来使用它。 

####  手动启动

如果更偏好手动启动 Enlightenment，请在控制台里输入并执行 `startx /usr/bin/enlightenment_start`。详见 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc")。 

要尝试使用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 混成器，请改为输入`enlightenment_start`。可能为此需要安装 [efl-git](<https://aur.archlinux.org/packages/efl-git/>)AUR 和 [enlightenment-git](<https://aur.archlinux.org/packages/enlightenment-git/>)AUR，因为这两个软件包虽然仍处于实验开发阶段，但功能和体验相对更完整。 

###  配置

Enlightenment 提供了一个精巧的配置系统，可以从主菜单中选择“设置”子菜单进入。 

####  网络

**ConnMan**

Enlightenment 首选的网络管理器是 [ConnMan](<../zh-cn/ConnMan.html> "ConnMan") ，包名： [connman](<https://archlinux.org/packages/?name=connman>)包 。配置方法参见：[ConnMan](<../zh-cn/ConnMan.html> "ConnMan")。 

为实现更多的配置，还可以安装 Econnman （AUR 中的 [econnman](<https://aur.archlinux.org/packages/econnman/>)AUR 或 [econnman-git](<https://aur.archlinux.org/packages/econnman-git/>)AUR）及其相关依赖包。 

**把 ConnMan 添加到书架**

  1. 设置 -> 扩展 -> 模块
  2. 系统
  3. 连接管理器（Connection Manager）
  4. 加载（选中并点击 _加载_ ）
  5. 在屏幕底部书架点击右键
  6. 进入书架 -> 内容
  7. 滚动项目列表找到 _ConnMan_
  8. 点击 _添加_

**NetworkManager**

你也可以使用 [networkmanager](<https://archlinux.org/packages/?name=networkmanager>)包 来管理网络连接。参见 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")。 

注意：这个小程序需要Appindicator支持才能在Enlightenment的[系统托盘](<#%E7%B3%BB%E7%BB%9F%E6%89%98%E7%9B%98>)中显示。可参考[NetworkManager#Appindicator](<../zh-cn/NetworkManager.html#Appindicator> "NetworkManager").作为使用该程序的一种选择，NetworkManager包含了CLI and TUI两种网络配置界面--参见[NetworkManager#nmcli examples](<../zh-cn/NetworkManager.html#nmcli_examples> "NetworkManager")。 

####  Polkit 代理

Enlightenment 没有提供[图形化的 Polkit 认证代理](<../zh-cn/Polkit.html#%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81%E7%BB%84%E4%BB%B6> "Polkit")。如果要执行某些需授权的操作（例如安装系统设备上的文件系统），你要安装一个认证代理并且使它自动启动。后者可以导航至 _**设置面板 > 应用 > 启动应用程序 > 系统**_设置项并激活它。AUR 中提供了一个基于 EFL 的认证代理，名为 [polkit-efl-git](<https://aur.archlinux.org/packages/polkit-efl-git/>)AUR。 

####  集成 GNOME 密钥环

在Enlightenment中可以使用gnome-keyring. 然而你需要做一点小的更改才能让它完全地工作。首先你需要设置Enlightenment去自动启动gnome-keyring，定位到 _Settings Panel > Apps > Startup Applications > System_ 并激活 _Certificate and Key Storage_ 、 _GPG Password Agent_ 、 _SSH Key Agent_ 以及 "Secret Storage Service"。 然后, 你应该编辑 `~/.pam_environment` 并添加下面的代码: 
    
           #Set gnome-keyring as the ssh authentication agent
           SSH_AUTH_SOCK=/run/user/${UID}/keyring/ssh
    
上述代码会覆盖 "enlightenment-start" 变量的自动启动配置，从 "ssh-agent" 切换到 gnome-keyring。 

更多信息请参考 [GNOME Keyring](<../zh-cn/GNOME_Keyring.html> "GNOME Keyring") 一文。 

####  系统托盘

**注意：** 从 Enlightenment 20 版开始，对 Xembed 的支持已被移除 [[1]](<https://twitter.com/_enlightenment_/status/538000507315314688>)。这意味着许多“传统的”托盘部件将无法显示在托盘。要使用这些托盘部件，需要另外安装一个独立的系统托盘程序（例如 [stalonetray](<https://archlinux.org/packages/?name=stalonetray>)包）

Enlightenment 支持系统托盘，但默认未启用。若要启用系统托盘，请打开 Enlightenment 主菜单，导航至 _**设置**_ 子菜单，点击 _**模块**_ 选项，向下滚动至 _**系统托盘**_ 选项并聚焦，点击 _**加载**_ 按钮。这样就加载了模块，可将其添加到书架中。在待添加系统托盘的书架上右击，聚焦于 _**书架**_ 子菜单，点击 _**内容**_ 选项，向下滚动到 _**系统托盘**_ 并聚焦，然后点击 _**添加**_ 按钮。 

####  通知

Enlightenment 的“通知”扩展模块提供了一个通知服务器。 

  * 通知可以按下述定义显示在屏幕任一角落
  * 可用的屏幕策略有：主屏幕、当前屏幕、所有屏幕和 Xinerama
  * 通知可以按紧急程度过滤（低、普通、紧急，及各种组合形式）
  * 可以设置默认通知消隐时间，也可以设置是否强制不自动消隐
  * 通知服务器可以设置是否忽略替换 ID 的请求

###  主题

下列更多主题用于定制 Enlightenment 外观： 

  * [enlightenment-themes.org](<https://www.enlightenment-themes.org/>)
  * [relighted.c0n.de](<https://relighted.c0n.de/#100>) 200 种不同颜色组合的默认主题
  * [git.enlightenment.org](<https://git.enlightenment.org>)（用 git 抓取喜欢的主题，运行 'make' 生成 .edj 后缀的主题文件）
  * [packages.bodhilinux.com](<http://packages.bodhilinux.com/bodhi/pool/b6main/b/>) 这里有一堆不错的主题（需从 .deb 包中释放出 .edj 文件，可以用 Arch Linux 的基础组件 bsdtar 释放）。在[他们的维基上](<https://web.archive.org/web/20140120083020/http://art.bodhilinux.com/doku.php?id=bodhi_e17_themes_v3>)还提供了一个很不错的分类
  * [exchange.enlightenment.org](<https://web.archive.org/web/20161025233126/https://exchange.enlightenment.org/theme>) (已封存)

你可以在主题设置对话框中安装这些 .edj 文件格式的主题，或者把它们放在 `~/.e/e/themes` 目录中。 

**注意：** Enlightenment 未提供稳定的主题 API，多年以来，甚至在 E17 发布后，很多主题 API 也已改变。未及时更新的主题很可能无法正常工作。

**提示：** 若要使 GTK 和 Qt 应用程序与 Enlightenment 默认主题相匹配，你可以下载一个类似 [E17 GTK 主题](<https://gnome-look.org/content/show.php/?content=163472>) 这样的主题包，放在 `~/.themes/` 中或者安装 [gtk-theme-e17gtk-git](<https://aur.archlinux.org/packages/gtk-theme-e17gtk-git/>)AUR 包，并在 Enlightenment 的设置中选中它，然后对其进行配置。这样可以使所有 GTK2 和 GTK3 应用匹配默认 Enlightenment 主题，然后，你可以配置 Qt 应用程序（或者配置 Qt 的默认设置），让其使用 Gtk+ 主题。这样 Qt 应用程序将模拟当前使用的 GTK 应用程序。这样就可以让绝大部分应用程序都使用 Enlightenment 的主题。参阅 [Qt 与 GTK 应用程序外观一致化](</wzh/index.php?title=Qt_%E4%B8%8E_GTK_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%A4%96%E8%A7%82%E4%B8%80%E8%87%B4%E5%8C%96&action=edit&redlink=1> "Qt 与 GTK 应用程序外观一致化（页面不存在）")。

####  GTK+

替换 GTK+ 主题的选项在 _**设置 > 全部 > 外观 > 应用程序主题**_。 

###  模块和小部件

模块
    小工具的后端支持代码在 Enlightenment 中使用的名称。
小工具
    前端或用户界面，应该有助于 Enlightenment 的用户完成某项任务。

很多模块提供了可以添加到桌面或面板上的小工具。某些模块 (如 CPUFreq) 只提供了单个的小工具；而一些模块 (如 Composite) 虽然不提供小工具，但提供了额外的功能。 注意某些小工具（如 Systray）只能被添加到面板上，而另一些小工具（如 Moon）只能在桌面上加载。 

####  "外部" 模块

**警告：** 这些第三方模块不被官方开发者支持。它们直接来自 git，因而可能随时出现工作异常。若要使用请自担风险。

除了这里列举的模块, 更多的模块可以从 [e-modules-extra-git](<https://aur.archlinux.org/packages/e-modules-extra-git/>)AUR 找到。 

**Scale Windows**

_Scale Windows_ 模块添加了额外的功能，但需要开启 compositing. 缩放窗口特效（Scale Windows）可以缩小所有打开的窗口并使它们全部进入预览视图。 这项功能与macOS中的"Mission Control"功能相类似. scale pager特效缩放所有桌面并将它们如壁纸一样显示，类似于插件 expo. 这两项功能都可以添加到桌面，或者与快捷键、鼠标以及屏幕边缘绑定起来。 

某些用户喜欢将标准的窗口选择快捷键 `ALT + Tab` 改变为使用缩放窗口特效（Scale Windows）去选择窗口。为了达到上述目的, 需要依次定位到 _Menu > Settings > Settings Panel > Input> Keys_. 在这里你可以设置任何你喜欢的快捷键。 

若需要将窗口选择键绑定功能替换为缩放窗口特效（Scale Windows）,滚动做面板直到 _ALT_ 节然后找到并选择 `ALT + Tab`。然后滚动右面版寻找 "Scale Windows" 并选择 _Select Next_ 或者 _Select Next (All)_ 并点击 _Apply_ 保存设置， _Select Next_ 选项仅能看到当前桌面的窗口， _Select Next (All)_ 选项可看到所有桌面上的窗口。 

这些可从[上游 git](<https://git.enlightenment.org/enlightenment/enlightenment-module-comp-scale>) 包获得。 

###  默认快捷键绑定

Enlightenment 的一些默认快捷键绑定  Shift + F10  | 垂直方向最大化   
---|---  
Ctrl + Menu  | 显示 "客户端"(窗口)菜单   
Alt + Escape  | 显示 "Everything 启动器" (应用、窗口等)   
Win + Left  | 左分屏最大化   
Win + Right  | 右分屏最大化   
Alt + Shift + F10  | 水平方向最大化   
Alt + Shift + Left  | 转到左侧的桌面   
Alt + Shift + Right  | 转到右侧的桌面   
Ctrl + Alt + D  | 显示桌面   
Ctrl + Alt + F  | 切换全屏   
Ctrl + Alt + I  | 切换图标模式   
Ctrl + Alt + K  | 杀死窗口   
Ctrl + Alt + L  | 锁定桌面   
Ctrl + Alt + N  | 最大化窗口   
Ctrl + Alt + R  | 向上卷起窗口   
Ctrl + Alt + W  | 窗口菜单   
Ctrl + Alt + X  | 关闭窗口   
Ctrl + Alt + Down  | 下移一层   
Ctrl + Alt + Up  | 上移一层   
Ctrl + Alt + Left  | 转到左侧的桌面   
Ctrl + Alt + Right  | 转到右侧的桌面   
Ctrl + Alt + Delete  | 结束会话对话框   
Ctrl + Alt + Insert  | 启动默认终端   
  
###  故障排除

如果 Enlightenment 出现了一些奇怪的行为, 可以尝试下面的步骤: 

  1. 尝试使用默认主题，看这些行为是否会出现；
  2. 禁用你安装的所有第三方模块；
  3. 备份 `~/.e` 文档并移除 `~/.e` (使用命令`mv ~/.e ~/.e.back`)；

若你确定自己发现了一个 Bug，请将它提交到 [directly 上游](<https://phab.enlightenment.org/maniphest/task/create/>)页面。 

####  混成

当需要在无法打开设置窗口的情况下重置设置的时候, 可以通过硬编码（hardcoded）快捷键 `Ctrl + Alt + Shift + Home` 重置混成器的设置。 

####  字体看不清楚

如果字体太小而无法阅读,首先确定你已经安装了正确的字体包。 安装[ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包 和[ttf-bitstream-vera](<https://archlinux.org/packages/?name=ttf-bitstream-vera>)包 字体包是一个不错的选择。 

你可以在 _Settings > Settings Panel > Look > Scaling_选项中设置缩放。 

####  背光总是较暗

你或许会发现在登出的情况下 Enlightenment 会常规性的将背光调低为30%，却只能在你登录到另一个新的Enlightenment session时才能恢复到100%。当使用Enlightenment和另一个桌面环境时，该问题特别明显；因为当使用该桌面环境时，背光不会自动恢复到正常水平。要修复该问题， 打开 _Settings Panel_ ，在 _Look_ 标签下, 勾选 _Composite_ 选项。勾选 _Don't fade backlight_ 前的方框并点击 _OK_. 

####  光标主题不一致

有时可能会发现桌面的光标主题与应用（如 [Firefox](<../zh-cn/Firefox.html> "Firefox")）中的光标主题不一致。 这是因为应用使用的是 X 光标主题，而 Enlightenment 有自己的光标主题设置。为了两者一致, 你可以设置 Enlightenment 总是使用 X 光标主题： 打开 Enlightenment的 _Settings Panel_ ，然后点击 _Input_ 标签。之后点击 _Mouse_ 选项。将其主题从 _Enlightenment_ 切换到 _X_ 然后点击 _OK_ 保存即可。 此时应该可以看到光标主题在每一个地方都是一致的了。 如果 X 光标主题并不总是一致的，可参考[光标主题](<../zh-cn/Cursor_themes.html#XDG_specification> "Cursor themes")

####  背景图片

你需要将想要设置为背景的图片拷贝到 `~/.e/e/backgrounds/` 目录下。 

在桌面的任意地方点击鼠标中键（MMB）或右键（RMB）访问“设置”选项，选择`/Desktop/Backgrounds/`

任何新拷贝到 `~/.e/e/backgrounds/` 文件夹下的图片都会使可供选择的背景列表自动更新。从下拉菜单中选择你想要设置的图片。在全局设置中的 _appropriate_ 选项卡内，可以调整背景图像的平铺、填充屏幕等。 

## Enlightenment DR16

Enlightenment, 开发版 16 第一次发布于2000年,在2009年到达了 1.0版. 初始情况下，DR16表示Enlightenment项目的0.16版。它就是现在Arch源的"Enlightenment16", 直到今天还在开发维护中, 通常由它的维护者 Kim 'kwo' Woelders提供更新。With compositing, shadows and transparencies, E16 kept all of the speed that presided over its foundation by original author Carsten "Rasterman" Haitzler but with up to date refinement. 

###  安装 E16

安装[enlightenment16](<https://aur.archlinux.org/packages/enlightenment16/>)AUR包. 

如需要深入的文档，可以参考`/usr/share/doc/e16/e16.html`. 

###  基本设置

E16的大多数设置文件保存在`~/.e16`目录中，并且是基于文本、可以编辑的。其中也包含了菜单（menus）。 

快捷键可以通过手动修改,也可以使用e16keyedit 软件修改；该软件可以在[sourceforge](<https://sourceforge.net/projects/enlightenment/>)页面找到。注意：默认情况下不会在`~/.e16`目录下创建键盘快捷键绑定文件。如果你想做修改的话，可以通过下面的命令将安装包自带的键盘快捷键绑定文件复制到你的home目录下： 
    
    $ cp /usr/share/e16/config/bindings.cfg ~/.e16
    
####  启动、重启、停止脚本

在你的`~/.e16`文件夹中创建 Init, a Start and a Stop 文件夹: 任何在这些文件夹中的 .sh 脚本 将会在启动时(位于Init文件夹)、每次重启时(位于Start文件夹)或者关机时(位于Stop文件夹)被执行; 假如你允许它们通过 MMB / settings / session / <enable scripts> button并 通过`chmod +x **yourscript.sh**`命令赋予它们可执行权限。经典的例子是启动pulseaudio或者你喜欢的网络管理程序。 

####  合成器（Compositor）

阴影、透明等等特效位于 Composite 项下的 MMB 或 RMB / 设置。 

##  参考资料

  * [Enlightenment 主页](<https://www.enlightenment.org/>)
  * [Enlightenment 开发者文档](<https://docs.enlightenment.org/>)
  * [E17-Stuff](<http://www.e17-stuff.org/>)
  * [DR16 下载资源](<https://sourceforge.net/projects/enlightenment/>)
  * [Enlightenment 用户邮件列表](<https://lists.sourceforge.net/lists/listinfo/enlightenment-users>)
  * [Enlightenment 开发者邮件列表](<https://lists.sourceforge.net/lists/listinfo/enlightenment-devel>)
  * <ircs://irc.libera.chat/e>

##  配置输入法

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 这篇文章或章节的内容已经过期。（在 [Talk:Enlightenment#](<../zh-cn/Talk:Enlightenment.html>) 中讨论）

**注意：** 英文版本节文字已删除。为方便中文用户，本节内容暂予保留

E17 内置了输入法支持的模块，支持的输入法有 iiimf 、scim 和 uim 。使用这些输入法的配置在 
    
    Settings -> Settings Panel -> Language -> Input Method Settings -> Advanced
    
System 配置中，使用者只需选择即可。使用其他输入法的用户可以在 Personal 配置中添加。 

### ibus

ibus 的配置参数为： 
    
    Input Method Parameters:
     Name              ibus
     Execute Command   /usr/bin/ibus-daemon --xim
     Setup Command     /usr/bin/ibus-setup
    
    Exported Environment Variables:
     GTK_IM_MODULE     ibus
     QT_IM_MODULE      ibus
     XMODIFIERS        @im=ibus
    