**翻译状态：**

  * 本文（或部分内容）译自 [Fcitx](<https://wiki.archlinux.org/title/Fcitx> "arch:Fcitx")，最近一次同步于 2020-04-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Fcitx?diff=0&oldid=608582>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Fcitx_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [IBus](<../zh-cn/IBus.html> "IBus")
  * [Fcitx5](<../zh-cn/Fcitx_5.html> "Fcitx5")
  * [SCIM](</wzh/index.php?title=SCIM&action=edit&redlink=1> "SCIM（页面不存在）")
  * [UIM](</wzh/index.php?title=UIM&action=edit&redlink=1> "UIM（页面不存在）")

[Fcitx](<https://en.wikipedia.org/wiki/Fcitx> "wikipedia:Fcitx")，即小企鹅输入法，是一个以 GPL 许可发布的[输入法](<https://en.wikipedia.org/wiki/Input_method> "wikipedia:Input method")平台,可以通过安装引擎支持多种输入法，支持简入繁出，是在 Linux 操作系统中常用的中文输入法。它的优点是：短小精悍、与各种程序的兼容性比较好。 

**警告：** 本页面是关于上游仓库已归档、不支持 [Wayland](<../zh-cn/Wayland.html> "Wayland") 的 Fcitx 3.x-4.x 版本。推荐使用正被积极维护的、支持 Wayland 的 [Fcitx5](<../zh-cn/Fcitx_5.html> "Fcitx5")。在[社区](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA.html> "Arch Linux 中文社区")提问时，也请提前声明您使用的版本。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [fcitx](<https://aur.archlinux.org/packages/fcitx/>)AUR。 

###  输入法引擎

Fcitx 内置的输入法支持中文[拼音](<https://en.wikipedia.org/wiki/Pinyin> "wikipedia:Pinyin")和基于字符表的输入（例如[五笔](<https://en.wikipedia.org/wiki/Wubi_method> "wikipedia:Wubi method")）。根据语言的不同，可以选择其他输入法引擎。 

####  中文

在 Fcitx 支持的拼音输入法中，内置拼音响应速度最快。Fcitx 同样支持流行的第三方拼音输入法以提供更好的整句输入效果。 

  * [fcitx-sunpinyin](<https://aur.archlinux.org/packages/fcitx-sunpinyin/>)AUR 在输入速度和输入精度之间有较好的平衡。
  * [fcitx-libpinyin](<https://aur.archlinux.org/packages/fcitx-libpinyin/>)AUR 算法比 sunpinyin 先进。
  * [fcitx-rime](<https://aur.archlinux.org/packages/fcitx-rime/>)AUR, 即著名中文输入法 [Rime IME](</wzh/index.php?title=Rime_IME&action=edit&redlink=1> "Rime IME（页面不存在）")的 Fcitx 版本。但它不支持 Fcitx 本身的 [#特殊符号](<#%E7%89%B9%E6%AE%8A%E7%AC%A6%E5%8F%B7>)和 [#快速输入](<#%E5%BF%AB%E9%80%9F%E8%BE%93%E5%85%A5>)功能，自定义设置请参见[官方](<https://rime.im>)，
  * [fcitx-googlepinyin](<https://aur.archlinux.org/packages/fcitx-googlepinyin/>)AUR, Google 拼音输入法 for Android。
  * [fcitx-sogoupinyin](<https://aur.archlinux.org/packages/fcitx-sogoupinyin/>)AUR, 搜狗输入法for linux——支持全拼、简拼、模糊音、云输入、皮肤、中英混输入。[官方网址](<https://pinyin.sogou.com/linux/>)
  * [fcitx-cloudpinyin](<https://aur.archlinux.org/packages/fcitx-cloudpinyin/>)AUR 可以提供云拼音输入的支持，支持 Fcitx 下的所有拼音输入法，Fcitx-rime 除外。
  * [fcitx-chewing](<https://aur.archlinux.org/packages/fcitx-chewing/>)AUR 为 Fcitx 添加 chewing (繁体中文注音) 输入引擎支持。依赖 [libchewing](<https://archlinux.org/packages/?name=libchewing>)包。
  * [fcitx-baidupinyin](<https://aur.archlinux.org/packages/fcitx-baidupinyin/>)AUR, 百度拼音输入法的fcitx wrapper。
  * [fcitx-table-extra](<https://aur.archlinux.org/packages/fcitx-table-extra/>)AUR Fcitx 的一些额外码表支持，包括仓颉 3, 仓颉 5, 粤拼, 速成, 五笔, 郑码等等。

####  日文

  * [fcitx-mozc](<https://aur.archlinux.org/packages/fcitx-mozc/>)AUR, 为 Fcitx 添加 mozc (日语) 输入引擎支持，mozc 是 Google 日语输入法的开源版本。
  * [fcitx-kkc](<https://aur.archlinux.org/packages/fcitx-kkc/>)AUR, 一款新的基于 [libkkc](<https://archlinux.org/packages/?name=libkkc>)包 的日文假名与汉字输入引擎。
  * [fcitx-skk](<https://aur.archlinux.org/packages/fcitx-skk/>)AUR, 一款基于 [libskk](<https://archlinux.org/packages/?name=libskk>)包 的日文假名与汉字输入引擎。
  * [fcitx-anthy](<https://aur.archlinux.org/packages/fcitx-anthy/>)AUR, 为 Fcitx 添加 anthy (日语) 输入引擎支持。

####  其它语言

  * [fcitx-hangul](<https://aur.archlinux.org/packages/fcitx-hangul/>)AUR, 为 Fcitx 添加 hangul (韩语) 输入引擎支持。
  * [fcitx-m17n](<https://aur.archlinux.org/packages/fcitx-m17n/>)AUR, 为 Fcitx 添加 m17n (多国语言码表) 输入引擎支持。
  * [fcitx-unikey](<https://aur.archlinux.org/packages/fcitx-unikey/>)AUR, 为 Fcitx 添加 unikey (越南语) 输入引擎支持。
  * [fcitx-sayura](<https://aur.archlinux.org/packages/fcitx-sayura/>)AUR, 为 Fcitx 添加 sayura （僧伽罗语） 输入引擎支持。

###  输入法模块

Fcitx 提供对 Qt 提供了输入法模块，请根据需要安装 [fcitx-qt4](<https://aur.archlinux.org/packages/fcitx-qt4/>)AUR、[fcitx-qt5](<https://aur.archlinux.org/packages/fcitx-qt5/>)AUR 和 [fcitx-qt6](<https://aur.archlinux.org/packages/fcitx-qt6/>)AUR。如果没有安装对应的模块，一般还是可以在大部分程序中使用输入法的。不过很可能出现从无法光标跟随、无法显示预编辑字符串、无法输入甚至程序卡死等情况。 

某些程序不使用 Qt 的输入法模块，这些程序包括： 

  * 使用 Tk, motif, 甚至 xlib 的程序
  * Emacs、Opera、OpenOffice、LibreOffice、Skype、Wine、Java、Xterm、urxvt、WPS

###  其它

  * [fcitx-ui-light](<https://aur.archlinux.org/packages/fcitx-ui-light/>)AUR, Fcitx 的轻量 UI。
  * [fcitx-table-other](<https://aur.archlinux.org/packages/fcitx-table-other/>)AUR, Fcitx 的一些更奇怪的码表支持，包括 Latex, Emoji, 以及一大堆不明字符等等。

您还可以在 [Arch User Repository](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 找到更多以上软件包的 Git 版以及其它。 

##  使用

###  桌面环境下自动启动

如果您用 XDG 兼容的桌面环境，比如 [KDE](<../zh-cn/KDE.html> "KDE"), [GNOME](<../zh-cn/GNOME.html> "GNOME"), [Xfce](<../zh-cn/Xfce.html> "Xfce"), [LXDE](<../zh-cn/LXDE.html> "LXDE"), 那么当您安装好 Fcitx 并重新登录后，Fcitx 应该会自动启动。如果没有的话，可以打开控制台并运行`fcitx`。为检验 Fcitx 是否正常运行, 打开一个程序，比如 leafpad, 按 CTRL+Space 激活 Fcitx 并试着输入几个字。 

如果 Fcitx 没有随桌面环境自动启动，或者您想修改下 Fcitx 启动参数，请用桌面环境提供的自动启动工具配置，或者直接编辑用户目录`~/.config/autostart/` 下的 `fcitx-autostart.desktop` 文件以确认自动启动是否被禁用。如果用户目录下的文件并不存在，您可以复制自动启动文件 `/etc/xdg/autostart/fcitx-autostart.desktop` 到用户目录： 
    
    cp /etc/xdg/autostart/fcitx-autostart.desktop ~/.config/autostart/
    
如果您使用的桌面环境并不自动支持 XDG 自动启动, 请在您使用的启动脚本里面添加 `fcitx` 以实现自动启动。 

例如，你使用[i3](<../zh-cn/I3.html> "I3")或[sway](<../zh-cn/Sway.html> "Sway")窗口管理器，可以在配置文件中添加`exec --no-startup-id fcitx`来自动启动输入法。 

当 iBus 等其它输入法程序同时启动且开启了 Xim 支持时, 可能导致 Fcitx 无法启动，请确保已禁用了其它输入法程序的自动启动。 

###  设置输入法的环境变量

请按以下方式设置环境变量，如果没有这些环境变量，程序可能默认使用 XIM 协议。qt5 程序不支持 XIM 所以必须配置使用 IM 模块，其它程序也有可能出现问题。 

建议通过 `/etc/environment` 设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")，[pam-env](<../zh-cn/PAM.html> "PAM") 模块会在所有登录会话中读取此文件，包括 X11 会话和 Wayland 会话。详情请参考 `man 8 pam-env`。 
    
    /etc/environment
    
    GTK_IM_MODULE=fcitx
    QT_IM_MODULE=fcitx
    XMODIFIERS=@im=fcitx
    
**注意：** pam-env 已不再读取 `~/.pam_environment` 文件。

部分[登录管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "登录管理器")（如 [LightDM](<../zh-cn/LightDM.html> "LightDM")）也支持读取 `~/.xprofile`，可以这样设置： 
    
    ~/.xprofile
    
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS=@im=fcitx
    
重新登录后让环境变量生效。 

如果 _fcitx_ 没有自动启动，请将 `fcitx &` 加入 `~/.xinitrc`, 如果 `fcitx &` 不启动，在后面加一个延时 `sleep 2`。 

  * 请不要在 `.bashrc` 设置这些环境变量。`bashrc`只应用于交互性 bash 会话的初始化，并不应用于非交互性脚本或 X 会话的初始化。
  * 如果 Qt 使用 fcitx 有问题，请执行 qtconfig (qtconfig-qt4)，在输入法配置中将 fcitx 设置为 "Default Input Method"。

### Xim

要在 Gtk/Qt 程序中用 xim, 请将上面的变量改成如下的值： 
    
    GTK_IM_MODULE DEFAULT=xim
    QT_IM_MODULE  DEFAULT=xim
    
**警告：** 使用 xim, 很可能会遇到一些包括不能输入, 没有光标跟随, 重启输入法时应用程序卡死在内的无法由 Fcitx 解决的问题，且官方不支持解决。

重新登录后让环境变量生效。 

**注意：** Gtk2 从 2.24.20 开始，使用 `/usr/lib/gtk-2.0/2.10.0/immodules.cache` 作为缓存文件。如果设置了 `GTK_IM_MODULE_FILE` 环境变量或在安装后修改了配置，请清掉环境变量并使用 `/usr/bin/gtk-query-immodules-2.0 --update-cache` 更新缓存。Qt5 程序不支持 XIM 所以必须配置使用 IM 模块

##  配置

###  配置工具

Fcitx 提供了若干图形界面的配置程序：KDE 中的 [kcm-fcitx](<https://aur.archlinux.org/packages/kcm-fcitx/>)AUR, 基于 GTK+3 的 [fcitx-configtool](<https://aur.archlinux.org/packages/fcitx-configtool/>)AUR。 

安装完配置工具[fcitx-configtool](<https://aur.archlinux.org/packages/fcitx-configtool/>)AUR之后打开配置工具的方法是用终端运行fcitx-config-gtk3，打开这个配置工具之后还要添加中文输入法。对于新安装的英文系统，要取消只显示当前语言的输入法（Only Show Current Language），才能看到和添加中文输入法(Pinyin, Libpinyin等)。 

如果要手工编辑 fcitx 的配置文件，请确保系统中并没有在运行 fcitx ，否则手工编辑的配置内容可能丢失。 

###  替换自带的经典界面

Fcitx 支持使用 kimpanel 协议的界面，以提供更好的桌面整合体验。 

  * Gnome-Shell：安装 [gnome-shell-extension-kimpanel-git](<https://aur.archlinux.org/packages/gnome-shell-extension-kimpanel-git/>)AUR, 它提供了类似 ibus-gjs 的用户体验，其候选框界面将会采用 Gnome-Shell 的主题风格, 同时在状态栏中增加 Fcitx 的输入法状态图标。

###  输入法

您可以在配置界面工具中添加／移除启用的输入法。在输入法图标上右键可以打开配置。 

列表第一项将作为“未激活”状态使用，请将此项设为键盘布局输入法，比如“(键盘 - 英文)”，第一项后面的输入法都是活动输入法。。 

**警告：** 请必须将键盘布局输入法设为列表中第一项, 否则可能会无法禁用中文输入。

在 _全局配置_ 中， _触发输入法_ 快捷键仅在未激活输入法及最后一个活动输入法之间切换。 _切换输入法_ 快捷键默认仅在不同的活动输入法间切换，但是在高级设置中可以将非激活输入法加入切换选择。 _切换输入法_ 快捷键需要按顺序按下，例如 `ALT_SHIFT` 仅在先按 `alt` 再按 `shift` 后生效。 

###  扩充内置拼音词库

用户配置拼音词库在 `~/.config/fcitx/pinyin`, 其中 `pybase.mb` 为拼音单字库，`pyphrase.mb` 为拼音词库。如果这两文件并不存在，直接将您下载的词库放置到 `/usr/share/fcitx/pinyin`. 重启 Fcitx 即可。 

###  皮肤

下载皮肤并解压缩到下面任一目录，如果没有可以新建目录： 
    
    /usr/share/fcitx/skin   ##全局设置
    ~/.config/fcitx/skin    #特定用户设置
    
###  云拼音

安装后重启 Fcitx 即可，所选的云拼音输入结果会自动添加到当前输入法的词库中。提醒：建议在fcitx设置里面将“云拼音来源”由Google改为“百度”，Google国内访问不是很顺畅。 

启用云拼音后，从云拼音获得的候选词会默认添加到候选词列表中的第二个，显示位置可以通过云拼音的设置配置。如果云拼音的结果和本地输入法给出的结果一致，云拼音后选项会和本地产生的候选项自动合并，不会产生重复的候选项。 

若安装fcitx-cloudpinyin后，在配置程序里却没有看见云拼音，记得勾上“高级”复选框。这时云拼音会显示出来，再勾上云拼音。 

**注意：** 不推荐将云拼音候选词设为第一个候选词，因为当网络情况不好，没有及时返回云拼音结果，那么云拼音结果将默认降到第二候选词的位置，于是这个过程可能会涉及到默认候选词的改变。

##  提示与技巧

###  快捷键

部分常用默认快捷键： 

  * `Ctrl+Space` 激活输入法
  * 左`Shift` 临时切换到英文
  * `Ctrl+Shift` 输入法间切换
  * `-/=` 向前/向后翻页
  * `Shift+Space` 全角、半角切换

**注意：** 您可以在配置界面的全局配置中修改这些快捷键。

### Vim

如果您经常在 Vim 下使用 Fcitx, 可以安装 [vim-fcitx](<https://aur.archlinux.org/packages/vim-fcitx/>)AUR 插件，或者在 `~/.vimrc` 添加如下代码。以退出插入模式时，自动关闭 Fcitx, 反之则反： 
    
    "##### auto fcitx  ###########
    let g:input_toggle = 1
    function! Fcitx2en()
       let s:input_status = system("fcitx-remote")
       if s:input_status == 2
          let g:input_toggle = 1
          let l:a = system("fcitx-remote -c")
       endif
    endfunction
    
    function! Fcitx2zh()
       let s:input_status = system("fcitx-remote")
       if s:input_status != 2 && g:input_toggle == 1
          let l:a = system("fcitx-remote -o")
          let g:input_toggle = 0
       endif
    endfunction
    
    set ttimeoutlen=150
    "退出插入模式
    autocmd InsertLeave * call Fcitx2en()
    "进入插入模式
    autocmd InsertEnter * call Fcitx2zh()
    "##### auto fcitx end ######
    
**注意：** 由于要调用外部程序，这将明显拖慢会反复进出插入模式的映射。建议改写相关映射，用带 Python 支持的 Vim 加以配合 fcitx.vim 亦可改善效率。

###  剪贴板

[Fcitx 自带剪贴板](<https://www.csslayer.info/wordpress/fcitx-dev/fcitx-clipboard/>)，其快捷键为 `Ctrl + ;`, 小小功能拯救世界。 

###  特殊符号

创建 `~/.config/fcitx/data/pySym.mb`, 文件内容示范如下： 
    
     #第一个字符为“#”的行是注释
     #格式：编码 符号
     #编码只能为小写字母，经拼音解析后最长为10(如py为2，pinyin也为2)
     #数学符号
     sxfh ＋
     sxfh －
     sxfh ＜
     sxfh ＝
     sxfh ＞
     sxfh ±
     sxfh ×
     sxfh ÷
     sxfh ∈
     sxfh ∏
     sxfh ∑
     sxfh ∕
     sxfh √
     sxfh ∝
    
直接输入某编码，可以匹配出对应的特殊符号。 

**注意：** 编码只能用二十六个小写字母表示；以 v 开头，无效。

###  快速输入

确保在 `~/.config/fcitx/config` 里把 `SemiColonAction` 修改为 `QuickPhrase`。 

创建 `~/.config/fcitx/data/QuickPhrase.mb`, 文件内容示范如下： 
    
     #第一个字符为“#”的行是注释
     #格式：编码 符号
     dianhua 123456789
     youbian 123456
     dizhi 中华人民共和国北京市长安街一号
     aowu ┗<(=｀O′=)>┛ 
     mobai ｍ<(＿　＿)>ｍ 
     baobao <(=′▽')爻 (`▽｀=)> 
     baobao <(=*′д｀)爻(′д｀*=)> 
     qiangbi ▄︻┻┳═一…… ☆<(=￣□￣=!)>
     xiaoku 😂
     canyue 🌖
     xuehua ❄
    
按 `;` 并输入编码，可实现快速输入，自然也能用来当[颜文字库](<https://blog.felixc.at/2012/05/kitty-for-fcitx-quickphrase/>)和[emoji表情库](<https://github.com/levinit/fcitx-emoji>)。 

**注意：** 编码除了不得有空格，不得以 `;` 开头之外，没有其它限制。

### fcitx-remote

_fcitx-remote_ 是可以控制 fcitx 状态的命令行工具，位于 [fcitx](<https://aur.archlinux.org/packages/fcitx/>)AUR 安装包中。 

常见的应用包括用 `fcitx-remote -s _imname_`, 将输入法切换到 `_imname_`。要获得正确的 `_imname_`，执行 _fcitx-diagnose_ 并查看 "## Input Methods:" 对应的输出。 

###  通过 Fcitx 输入特殊字符

参见：[Fcitx5#通过 Fcitx5 输入特殊字符](<../zh-cn/Fcitx_5.html#%E9%80%9A%E8%BF%87_Fcitx5_%E8%BE%93%E5%85%A5%E7%89%B9%E6%AE%8A%E5%AD%97%E7%AC%A6> "Fcitx5")。该内容同样适用于 Fcitx 

##  故障排除

###  停用或修改 _Extra key for trigger input method_

设置位于 _全局配置_ 标签，默认是 _SHIFT_ , 也就是说两边的 shift 键都会修改输入法。这个设置可能在输入大写字母的时候引起误触，而且可能会在安装后恢复成默认值。要确保进行的修改没有被覆盖，请设置配置文件为只读：`# chattr +i ~/.config/fcitx/config`。 

###  首先诊断问题所在

当你遇到任何 fcitx 有关的问题，比如 ctrl+space 在有的程序中不能工作，首先应该用 `fcitx-diagnose` 命令诊断问题的原因。 `fcitx-diagnose` 会列出所有 fcitx 正常运行所需的前提条件，从输出结果中通常可以找到问题的原因。 在网上（比如在 irc 或者论坛里）询问别人关于 fcitx 配置的问题时，也请首先提供你的 `fcitx-diagnose` 输出结果（比如贴到 pastebin 服务），这将加速别人帮你找到问题所在。 

###  Emacs 无法使用输入法

emacs会找出一份字体列表发送给输入法,以便输入法绘制输入框。 那么会出现两种情况： 

  * 1.找不到字体

emacs 默认 fontset 会使用 "-*-*-*-r-normal--14-*-*-*-*-*-*-*" 字体 (terminus, 75dpi 等等，可以通过 `xlsfonts` 命令查看)。 

解决方法：安装[xorg-mkfontscale](<https://archlinux.org/packages/?name=xorg-mkfontscale>)包后**重启** , 它将创建字体文件索引。通过 `xlsfonts` 命令查看是否存在emacs默认字体，如果不存在可尝试安装类似字体后**重启** ，比如[ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包。 

  * 2.找到太多字体

找到太多字体会导致某些地方溢出，无法呼出输入法。终端下并不会遇到此现象。 将`LC_CTYPE` 设为 `zh_CN.UTF-8`，会减少找到的字体数目。 

解决方法：在.xprofile或.xinitrc中添加以下内容后**重新登录或者重启**
    
    export LC_CTYPE=zh_CN.UTF-8 
    
使用`locale`命令可查看是否成功更改。 

更详细的情况参见[Emacs 为什么要设置 LC_CTYPE](<https://www.csslayer.info/wordpress/fcitx-dev/%E4%B8%96%E7%BA%AA%E6%9C%AA%E8%A7%A3%E4%B9%8B%E8%B0%9C%E4%B9%8B-emacs-%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E8%AE%BE%E7%BD%AE-lc_ctype-%E6%89%8D%E8%83%BD%E7%94%A8%E8%BE%93%E5%85%A5%E6%B3%95%E7%BB%88/>)，[Yichao Yu给emacs写的Patch](<https://debbugs.gnu.org/cgi/bugreport.cgi?bug=10867>)。 

###  在 gnome-terminal中 `Ctrl + Space` 不能调出输入法

使用 GDM 3.16 启动 GNOME，可能在某些程序中无法使用 `Ctrl + Space` 调出输入法。解决方法是修改GSettings配置 
    
    gsettings set \
      org.gnome.settings-daemon.plugins.xsettings overrides \
      "{'Gtk/IMModule':<'fcitx'>}"
    
###  `Ctrl + ;` 会调出 Fcitx 的剪贴板

严格的说，这不是 BUG, Fcitx 的 `Ctrl + ;` 会覆盖很多用户自己的快捷键，特别是 Emacs 用户。有必要时，可以在配置界面中禁用剪贴板插件，或更改其激活快捷键。 

###  fcitx-sogoupinyin 卡死、联想失败

如果您遇到下列的问题： 

  * 输入类似“安装”、“暗影”等 "a" 开头的词语，出现卡死的情况。
  * 输入并不以拼音 "a" 开头的词语时，却出现“阿拉伯”、“阿里巴巴”等以 "a" 开头的错误联想词语等。

可以通过删除 `~/.config/fcitx/sogou` 下的所有内容的方式解决。 

**注意：** 此操作会清空用户词库。

###  在某些程序下输入法总是被切换到美语键盘

比如在 XMind 下，当 Enter 出新结点时，输入法就会被切换到美语键盘，不得不按 Ctrl-Space 以重新切回中文输入法。 

启动 Fcitx 的 Config, 在 Global Config 选项卡下的“Share State Among Window”选项里选中“PerProgram”或“All”即可解决。 

##  参见

  * [Fcitx GitHub](<https://github.com/fcitx/fcitx/>)
  * [Fcitx Google Code](<https://code.google.com/p/fcitx/>)
  * [Fcitx Wiki](<https://fcitx-im.org/>)
  * [猫颜文字 For Fcitx QuickPhrase](<https://blog.felixc.at/2012/05/kitty-for-fcitx-quickphrase/>)
  * [emoji常用表情-fcitx-emoji](<https://github.com/levinit/fcitx-emoji>)
  * [史前大坑 Fcitx 官方 Artwork 团队出品：Fcitx 输入法皮肤制作全教程](<https://forum.suse.org.cn/viewtopic.php?f=16&t=731>)
  * [rime 朙(ming)月拼音扩充词库](<https://archive.today/2014.10.06-110451/https://bintray.com/rime-aca/dictionaries/luna_pinyin.dict/view/general>)
  * [Fcitx not work in terminal, nautilus, gedit](<https://bugzilla.gnome.org/show_bug.cgi?id=747825#c6>)
