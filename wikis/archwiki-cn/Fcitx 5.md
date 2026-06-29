相关文章

  * [Fcitx](<../zh-cn/Fcitx.html> "Fcitx")
  * [IBus](<../zh-cn/IBus.html> "IBus")
  * [中州韵输入法引擎](<../zh-cn/Rime.html> "Rime")

**注意：** 本页面**不是** 英文页面的翻译。请勿不加选择地将英文页面同步至本页面。

[Fcitx5](<https://fcitx-im.org/wiki/Fcitx_5>) 是一个[输入法](<../zh-cn/%E8%BE%93%E5%85%A5%E6%B3%95.html> "输入法")框架，它具有轻量级内核，并通过 addon 提供各种语言和输入法的支持。Fcitx5 接替 [Fcitx](<../zh-cn/Fcitx.html> "Fcitx")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 软件包。 

[fcitx5-im](<https://archlinux.org/groups/x86_64/fcitx5-im/>)包组 包组提供 [fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 本体、[#配置工具](<#%E9%85%8D%E7%BD%AE%E5%B7%A5%E5%85%B7>)和[#输入法模块](<#%E8%BE%93%E5%85%A5%E6%B3%95%E6%A8%A1%E5%9D%97>)。 

**注意：**[fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 仅提供基本框架，且仅支持英文。如果要输入其他语言（例如中文或日文），则需要安装输入法引擎（IME）。

###  中文

  * [fcitx5-chinese-addons](<https://archlinux.org/packages/?name=fcitx5-chinese-addons>)包 包含与中文相关的 addon，例如拼音、双拼和五笔。
  * [fcitx5-chewing](<https://archlinux.org/packages/?name=fcitx5-chewing>)包 是流行的繁体中文注音输入引擎，它基于 [libchewing](<https://archlinux.org/packages/?name=libchewing>)包。
  * [fcitx5-rime](<https://archlinux.org/packages/?name=fcitx5-rime>)包 使用 [Rime](<../zh-cn/Rime.html> "Rime") 引擎。
  * [fcitx5-table-extra](<https://archlinux.org/packages/?name=fcitx5-table-extra>)包 包含仓颉、呒虾米等输入法。
  * [fcitx5-mcbopomofo-git](<https://aur.archlinux.org/packages/fcitx5-mcbopomofo-git/>)AUR小麦注音的Linux版， [McBopomofo](<https://github.com/openvanilla/fcitx5-mcbopomofo>) 支持。
  * [rime-flypy](<https://aur.archlinux.org/packages/rime-flypy/>)AUR 小鹤音形支持。

###  日文

  * [fcitx5-anthy](<https://archlinux.org/packages/?name=fcitx5-anthy>)包 是流行的日文输入引擎。但是，它已不再受到积极开发。
  * [fcitx5-kkc](<https://archlinux.org/packages/?name=fcitx5-kkc>)包 是日文假名输入引擎，它基于 [libkkc](<https://archlinux.org/packages/?name=libkkc>)包。
  * [fcitx5-mozc](<https://archlinux.org/packages/?name=fcitx5-mozc>)包 基于 [Mozc](</wzh/index.php?title=Mozc&action=edit&redlink=1> "Mozc（页面不存在）")（英语：[Mozc](<https://wiki.archlinux.org/title/Mozc> "en:Mozc")）（Google 日文输入法的开源版本）。
  * [fcitx5-skk](<https://archlinux.org/packages/?name=fcitx5-skk>)包 是日文假名输入引擎，它基于 [libskk](<https://archlinux.org/packages/?name=libskk>)包。

###  其他语言

  * [fcitx5-hangul](<https://archlinux.org/packages/?name=fcitx5-hangul>)包 用于输入韩文，基于 [libhangul](<https://archlinux.org/packages/?name=libhangul>)包。
  * [fcitx5-unikey](<https://archlinux.org/packages/?name=fcitx5-unikey>)包 或 [fcitx5-bamboo-git](<https://aur.archlinux.org/packages/fcitx5-bamboo-git/>)AUR 可用于输入越南语字符。
  * [fcitx5-m17n](<https://archlinux.org/packages/?name=fcitx5-m17n>)包 或 [fcitx5-table-other](<https://archlinux.org/packages/?name=fcitx5-table-other>)包 可用于各种语言。使用后者输入 IPA（X-SAMPA）。

###  输入法模块

一些 GUI 工具包提供了输入法模块支持，这些模块在 [X11](<../zh-cn/Xorg.html> "X11") 下能提供更好的体验，但是在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 下则经常相反。因此 X11 桌面的用户建议安装，而 Wayland 桌面的用户则根据 Wayland 混成器的支持情况按需安装，详见 [#Wayland](<#Wayland>)。 

  * 对于 [Qt](<../zh-cn/Qt.html> "Qt")5/6 程序，安装 [fcitx5-qt](<https://archlinux.org/packages/?name=fcitx5-qt>)包。
  * 对于 [GTK](<../zh-cn/GTK.html> "GTK") 程序，安装 [fcitx5-gtk](<https://archlinux.org/packages/?name=fcitx5-gtk>)包。
  * 对于 Qt4 程序，安装 [fcitx5-qt4-git](<https://aur.archlinux.org/packages/fcitx5-qt4-git/>)AUR（通常不需要）。

##  配置

[X11](<../zh-cn/Xorg.html> "X11")（以及 Xwayland）和 [Wayland](<../zh-cn/Wayland.html> "Wayland") 环境的配置方式并不相同。 

Fcitx5 支持多种与要使用输入法的应用程序进行通信的方式： 

  * Wayland 输入法协议 
    * input-method-v1: 用于 [KDE](<../zh-cn/KDE.html> "KDE") 和 Wayfire 等 Wayland 混成器。
    * input-method-v2: 用于 [Sway](<../zh-cn/Sway.html> "Sway") 等 Wayland 混成器。
    * [GNOME Shell](<../zh-cn/GNOME_Shell.html> "GNOME Shell"): 用于与 [GNOME](<../zh-cn/GNOME.html> "GNOME") Wayland 桌面环境。它是通过 D-Bus 进行的。
  * 输入法模块。这些通常用于 X11 环境，或者尚未良好支持 Wayland 输入法协议的应用程序。它是通过 D-Bus 进行的。需要额外注意的是，当在原生 Wayland 模式下使用输入法模块时，为了将输入法窗口放置到正确的位置，输入法窗口是由使用输入法的应用程序自己绘制的，因此不同的应用程序的状况不太一样。比如 GTK3 的输入法窗口可能会闪烁，Qt 的输入法窗口可能无法显示部分 GTK 能显示的文字。 
    * fcitx: 用于 [GTK](<../zh-cn/GTK.html> "GTK")、[Qt](<../zh-cn/Qt.html> "Qt") 的输入法模块。
    * fcitx5: 同上，但是不兼容 [fcitx4](<../zh-cn/Fcitx.html> "Fcitx") 的输入法模块。不建议使用。
    * ibus: 兼容 [IBus](<../zh-cn/IBus.html> "IBus") 的协议。
  * XIM: 用于其它 X11 应用程序。有一些缺点，建议尽量不用。

### X11

X11 下，输入法可使用 [GTK](<../zh-cn/GTK.html> "GTK") 和 [Qt](<../zh-cn/Qt.html> "Qt") 的输入法模块通过 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 与输入法通信。某些非 [GTK](<../zh-cn/GTK.html> "GTK") 和 [Qt](<../zh-cn/Qt.html> "Qt") 的应用程序（或者框架）也实现了 fcitx 或者 ibus 的 D-Bus 通信协议。其它程序可以通过 X11 的 XIM 协议进行通信。 

为了告诉程序使用 fcitx5 输入法，需要设置相应的环境变量。编辑 `/etc/environment` 并添加以下几行，然后重新登录[[1]](<#cite_note-1>)： 
    
    GTK_IM_MODULE=fcitx
    QT_IM_MODULE=fcitx
    XMODIFIERS=@im=fcitx
    SDL_IM_MODULE=fcitx
    GLFW_IM_MODULE=ibus
    
如果使用 en_US.UTF-8 时，遇到 GTK2 无法激活 fcitx5，可专门为该 GTK2 应用程序设置输入法为 xim，如 
    
    $ env GTK_IM_MODULE=xim _< your_gtk2_application>_
    
请勿将 `GTK_IM_MODULE` 全局设置为 xim，因为它也会影响 GTK3 程序。XIM 有各种问题（比如输入法重启之后再无法输入），尽可能不要使用。 

**注意：**

  * SDL_IM_MODULE 是为了让一些使用特定版本 SDL2 库的游戏能正常使用输入法。
  * GLFW_IM_MODULE 是为了让 kitty 启用输入法支持。此环境变量的值为ibus为了保证所有的kitty均可启用该功能，在基于x11的桌面环境和窗口管理器中此属性设置为fcitx5或fcitx会导致无法启用输入法设置，wayland桌面不受此影响。
  * 按 fcitx5 上游推荐，环境变量的值设置为`fcitx`。部分并非由 Arch 从源码编译打包的应用程序因兼容性的需求而需要将之设置为`fcitx5`。

### Wayland

不同Wayland混成器的情况有所不同。 

####  共通设置

为了支持运行于Xwayland的GTK软件，在`~/.config/gtk-3.0/settings.ini`中添加：
    
    [Settings]
    gtk-im-module = fcitx
    
**警告：** 请勿设置`GTK_IM_MODULE`环境变量。

为了支持Qt5和运行于Xwayland的Qt软件，设置以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")： 
    
    QT_IM_MODULES=wayland;fcitx
    QT_IM_MODULE=fcitx

为了支持运行于Xwayland 的其他软件，设置环境变量`XMODIFIERS=@im=fcitx`。 

#### KDE Wayland

根据 [Fcitx 5 Wiki](<https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland#KDE_Plasma>)，Plasma 5.27+ 支持 Wayland text-input-v1、text-input-v2 和 text-input-v3，可被 Chromium、Qt 和 GTK 使用。 

要使用 Wayland 输入法协议，首先退出正在运行的 Fcitx 5 进程，前往 _系统设置_ > _输入与输出_ > _键盘_ > _虚拟键盘_ ，选择 _Fcitx 5 Wayland 启动器_ 。 

如果重新登录之后无法使用输入法，尝试运行：
    
    qdbus6 org.kde.KWin /VirtualKeyboard org.kde.kwin.VirtualKeyboard.enabled true
    
#### GNOME Wayland

安装 [gnome-shell-extension-kimpanel-git](<https://aur.archlinux.org/packages/gnome-shell-extension-kimpanel-git/>)AUR 并启用 Kimpanel GNOME Shell 拓展。 

根据 [Fcitx 5 Wiki](<https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland#GNOME>), GNOME 支持 Wayland text-input-v3 协议，大多数足够新的GUI库和软件应当能够开箱即用。 

根据 [Fcitx5 Wiki](<https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland#GNOME>), 在[GNOME](<../zh-cn/GNOME.html> "GNOME") Wayland 环境中的fcitx，可能出现弹出候选窗口无法在 gnome-shell UI 上显示。一个解决方案是使用[Kimpanel](<https://fcitx-im.org/wiki/Special:MyLanguage/Kimpanel>)扩展，此为[扩展连接](<https://extensions.gnome.org/extension/261/kimpanel/>)。 

#### Wayfire

启用 `input-method-v1` 插件。然后运行 Fcitx5 即可。 

Wayfire 支持 text-input-v1，但是不会显示输入法窗口[[2]](<#cite_note-2>)。低版本的 Chromium / Electron 在原生 Wayland 模式下会使用这个。 

####  Chromium 和基于 Chromium / Electron 的软件

除了各种基于 Chromium 内核的浏览器之外，这类软件还包括 VS Code、QQ、Discord、Element 等基于 Electron 的软件。请参阅 [Chromium#原生 Wayland 上运行](<../zh-cn/Chromium.html#%E5%8E%9F%E7%94%9F_Wayland_%E4%B8%8A%E8%BF%90%E8%A1%8C> "Chromium")。 

##### flatpak

flatpak 沙箱应用启动时不会读到`~/.config/gtk-3.0/settings.ini`，而是`~/.var/app/$APP_ID/config`（受 XDG_CONFIG_HOME 控制）[[2]](<https://github.com/flatpak/flatpak/issues/1147>)[[3]](<https://forum.endeavouros.com/t/how-to-consistent-flatpak-theming-in-kde-plasma/6385>)。 

你可以使用 [Flatseal](<https://flathub.org/apps/com.github.tchx84.Flatseal>) 为所有 flatpak 应用（global）设定 `GTK_IM_MODULE=fcitx` 环境变量，也可以添加允许读取 `xdg-config/gtk-3.0:ro`，这样就能读到主机配置文件了 [[4]](<https://github.com/pop-os/cosmic-comp/issues/488#issuecomment-2119339876>)。 

###  随桌面环境自动启动

**注意：**

  * 如果您使用的桌面环境是兼容 XDG 的（例如 [KDE](<../zh-cn/KDE.html> "KDE")、[GNOME](<../zh-cn/GNOME.html> "GNOME")、[Xfce](<../zh-cn/Xfce.html> "Xfce")、[LXDE](<../zh-cn/LXDE.html> "LXDE") 等），则**无需** 此步骤。
  * 如果使用 [i3](<../zh-cn/I3.html> "I3")、[awesome](<../zh-cn/Awesome.html> "Awesome") 等窗口管理器，需要在其脚本中添加 Fcitx5 以实现自启动。例如，如果您使用 i3 或 sway ,可以在配置文件中添加`exec --no-startup-id fcitx5 -d`
  * 如果使用 [dwm](<../zh-cn/Dwm.html> "Dwm")，则需要添加 [autostart](<https://dwm.suckless.org/patches/autostart>) 补丁。在 `~/.dwm/autostart.sh` 中添加`fcitx5 -d`
  * [KDE](<../zh-cn/KDE.html> "KDE") Wayland 用户请使用“虚拟键盘”设置，请勿使用此方法。

想要 [fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 开机自启，执行 
    
    $ cp /usr/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/
    
如果使用 [xinit](<../zh-cn/Xinit.html> "Xinit") 启动，则可以在`~/.xinitrc`中，在`exec`前添加`fcitx5 &`

###  词库

对于 Fcitx5 的中文输入法, 目前在仓库里提供了数个词库： 

  * [fcitx5-pinyin-zhwiki](<https://archlinux.org/packages/?name=fcitx5-pinyin-zhwiki>)包：felixonmars 根据中文维基百科创建的词库。适用于**拼音输入法**
  * [fcitx5-pinyin-sougou-dict-git](<https://aur.archlinux.org/packages/fcitx5-pinyin-sougou-dict-git/>)AUR、[fcitx5-pinyin-sougou-dict](<https://aur.archlinux.org/packages/fcitx5-pinyin-sougou-dict/>)AUR：适用于拼音输入法的搜狗词库
  * [rime-pinyin-zhwiki](<https://archlinux.org/packages/?name=rime-pinyin-zhwiki>)包：适用于 [Rime](<../zh-cn/Rime.html> "Rime") 输入法的词库
  * [rime-pinyin-moegirl](<https://aur.archlinux.org/packages/rime-pinyin-moegirl/>)AUR：适用于 [Rime](<../zh-cn/Rime.html> "Rime") 输入法的词库
  * [cedict](<https://github.com/cathaysia/fcitx5_dicts/releases/tag/0.0.1>):从 [cedict辞典](<https://www.mdbg.net/chinese/dictionary?page=cc-cedict>)导出的词库。
  * [fcitx5-pinyin-moegirl](<https://aur.archlinux.org/packages/fcitx5-pinyin-moegirl/>)AUR： outloudvi 根据萌娘百科创建的词库

**注意：**

  * 词典文件存在的目录为 ~/.local/share/fcitx5/pinyin/dictionaries
  * .dict类型的词典文件可以直接手动移动到词典目录，使用搜狗细胞词库下载的.scel文件无法被fcitx识别
  * 可在fcitx5-configtool中选择导入来自搜狗细胞词库文件，或使用scel2org5指令手动转换

###  自定义词库

一般而言,由于 [fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 支持[导入搜狗词库](<#%E5%AF%BC%E5%85%A5%E6%90%9C%E7%8B%97%E8%AF%8D%E5%BA%93>)，因此很大程度上不需要自定义词库，但是 [fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 依然提供了相关工具。 

  * 安装 [libime](<https://archlinux.org/packages/?name=libime>)包

原始词库文件是一个文本文件，其格式为： `汉字 拼音 频率`

在得到原始词库文件后，调用 `libime_pinyindict "词库文件.txt" "词库文件.dict" ` 即可。 

自定义词库文件放置在 `~/.local/share/fcitx5/pinyin/dictionaries`

**注意：** 以下内容或许能提供帮助： 

  * [汉字转拼音](<https://pypi.org/project/pypinyin/>)
  * [简繁转换](<https://pypi.org/project/OpenCC/>)

###  配置工具

[fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 的配置文件位于 `~/.config/fcitx5`，尽管您可以使用文本编辑器编辑配置文件，但是使用 GUI 配置显然更方便。安装 [fcitx5-configtool](<https://archlinux.org/packages/?name=fcitx5-configtool>)包 软件包并运行 `fcitx5-configtool`，或者从输入法托盘的菜单里选择“配置”。 

KDE 用户请安装 [fcitx5-configtool](<https://archlinux.org/packages/?name=fcitx5-configtool>)包 后在 KDE 的“设置”程序里找到并设置。 

###  主题和外观

####  主题

仓库内的主题数量有限，如果需要更多主题，可以去 [GitHub](<https://github.com/search?q=fcitx5+theme&type=Repositories>) 发现更多主题。 

  * [fcitx5-breeze](<https://archlinux.org/packages/?name=fcitx5-breeze>)包：提供了与KDE默认的Breeze主题匹配的外观。
  * [fcitx5-nord](<https://archlinux.org/packages/?name=fcitx5-nord>)包 ：[Nord颜色](<https://github.com/tonyfettes/fcitx5-nord>)的主题
  * [fcitx5-material-color](<https://archlinux.org/packages/?name=fcitx5-material-color>)包：提供了类似微软拼音的外观。
  * [fcitx5-solarized](<https://aur.archlinux.org/packages/fcitx5-solarized/>)AUR：[Solarized颜色](<https://ethanschoonover.com/solarized/>)主题
  * [fcitx5-skin-fluentdark-git](<https://aur.archlinux.org/packages/fcitx5-skin-fluentdark-git/>)AUR：具有模糊效果和阴影的 Fluent-Design 深色主题

然后前往 `Fcitx5设置 -> 配置附加组件 -> 经典用户界面 -> 主题` 设置主题。 

**注意：** 如果您在 GNOME 环境下使用了 [gnome-shell-extension-kimpanel-git](<https://aur.archlinux.org/packages/gnome-shell-extension-kimpanel-git/>)AUR，那么主题设置对于 Fcitx5 不起作用。[[5]](<https://yanqiyu.info/2020/11/06/fcitx5-fedora-updated/#60d50c0a87a8c64ae965e403>)

####  设置单行模式

在拼音输入法（或者 Rime 输入法）的设置中，启用“**在程序中显示预编辑文本** ”即可启用单行模式 

##  故障处理

###  诊断问题

当你遇到任何 Fcitx 5 有关的问题，比如 `Ctrl+Space` 快捷键在有的程序中不能工作，首先应该用 `fcitx5-diagnose` 命令诊断问题的原因。 `fcitx5-diagnose` 会列出所有 Fcitx 5 正常运行所需的前提条件，从输出结果中通常可以找到问题的原因。 

###  部分应用中 Fcitx 5 的单行默认无效

1\. 如果是 Firefox 等 gtk 应用中单行模式不生效，请安装 [fcitx5-gtk](<https://archlinux.org/packages/?name=fcitx5-gtk>)包

2\. 在 WPS 和 Sublime 中单行模式无效，这是 WPS 和 Sublime 自身的问题，而不是 [fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 的问题。[[6]](<https://github.com/fcitx/fcitx5/issues/60>)，请参阅 [WPS Office#Fcitx5 无法输入中文](<../zh-cn/WPS_Office.html#Fcitx5_%E6%97%A0%E6%B3%95%E8%BE%93%E5%85%A5%E4%B8%AD%E6%96%87> "WPS Office")。 

###  Fcitx5 在 JetBrains IDEs 不正常工作

请确保您的系统的 [locale](<../zh-cn/Locale.html> "Locale") 是正确的并已生成，因为不正确的 [locale](<../zh-cn/Locale.html> "Locale") 会导致Fcitx5 无法在 JetBrains 集成开发环境中正常工作。 

###  emoji 在候选框中显示为空白

首先确保电脑上已经安装了支持 emoji 的字体（例如 [noto-fonts-emoji](<https://archlinux.org/packages/?name=noto-fonts-emoji>)包）。然后对该 emoji 字体禁用反锯齿。编辑 [fontconfig](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html> "Fontconfig") 的配置文件并加入： 
    
    <match target="font">
      <test name="family" qual="first">
        <string>Noto Color Emoji</string>
      </test>
      <edit mode="assign" name="antialias">
        <bool>false</bool>
      </edit>
    </match>
    
###  RStudio 中无法调出输入法

运行以下命令： 
    
    $ strings /usr/lib/rstudio/lib/libQt5Core.so.5 | grep "Qt 5"
    
找出 Qt 库的版本，使用该版本重新编译 [fcitx5-qt](<https://archlinux.org/packages/?name=fcitx5-qt>)包 中的 `libfcitx5platforminputcontextplugin.so` ，再放到 `/usr/lib/rstudio/plugins/platforminputcontexts/` 目录中。 

如果使用的是 [rstudio-desktop-bin](<https://aur.archlinux.org/packages/rstudio-desktop-bin/>)AUR ，可直接安装 [rstudio-fcitx5](<https://aur.archlinux.org/packages/rstudio-fcitx5/>)AUR 。 

###  在 Steam 和 Dota2 中无法使用

事实上，Fcitx5 能够在 Steam 大屏模式和 Dota2 中使用。但是需要使用 `Ctrl+Space` 激活输入法而不是 `Ctrl+Shift`，参阅[[7]](<https://github.com/fcitx/fcitx5/issues/442>)。 

如果遇到问题, 请尝试[[8]](<https://github.com/ValveSoftware/steam-for-linux/issues/3255>)
    
    XMODIFIERS=@im=fcitx LANG=zh_CN.UTF-8 steam
    
###  输入法窗口在Wayland的Chromium中不显示

详见 [Chromium#原生 Wayland 上运行](<../zh-cn/Chromium.html#%E5%8E%9F%E7%94%9F_Wayland_%E4%B8%8A%E8%BF%90%E8%A1%8C> "Chromium"). 

###  在 kitty 中 Fcitx5 不可用

详见 [kitty#输入法兼容](<../zh-cn/Kitty.html#%E8%BE%93%E5%85%A5%E6%B3%95%E5%85%BC%E5%AE%B9> "Kitty")。 

###  Fcitx5 的 右Alt 在 Electron applications 不正常工作

如果应用程序使用的是非系统键盘（如 Discord、Element 等），则应用程序可能会在输入法处理 ISO_Level3_Shift 之前处理 ISO_Level3_Shift。这导致了一些输入法在个别应用各种中会发生错误。一个解决方法是添加另一个输入法组，将系统输入法布局设置成与键盘相对应的布局。例如，要在一个以英语为主要语言系统的QWERTY键盘上输入波兰字母 `ąćęłńóśźż` ，你可以用 Fcitx5 的GUI配置工具： 

  1. 点击 _添加组_ 加号按钮。
  2. 在下拉菜单中选择该组，然后添加输入法（键盘，例如“‘键盘 - 波兰语’”）。
  3. 使用“‘选择系统键盘布局’”选择与此输入法匹配的键盘布局，然后应用更改。

如果您需要其它解决方案，请参阅 Fcitx5 开发人员的评论。[[9]](<https://github.com/fcitx/fcitx5/issues/740>)

###  使用 Wayland 原生协议的软件不显示输入法窗口

#### Sway

请确保您在使用 Sway 1.10 或更高的版本。 

#### GNOME

安装 [gnome-shell-extension-kimpanel-git](<https://aur.archlinux.org/packages/gnome-shell-extension-kimpanel-git/>)AUR 插件。 

#### wayfire

请启用 `input-method-v1` 插件。 

由于目前 Qt（6.8.x）默认会使用 text-input-v1（而非 text-input-v3）协议，Qt 应用程序在通过 Wayland 协议使用输入法时看不到输入法窗口。一个绕过的办法是使用 `QT_IM_MODULE=fcitx`。（这样会导致 fcitx 主题不能自适应亮暗色。）另一个办法是设置 `QT_WAYLAND_TEXT_INPUT_PROTOCOL=zwp_text_input_v3` 让 Qt 使用 text-input-v3，但有可能会遇到 bug。 

###  Fcitx5 在一些应用程序中无法使用

如果你的 Fcitx5 在一些应用程序中无法使用（例如：[Anki](<https://wiki.archlinux.org/title/Anki> "en:Anki")Qt6）检查是否有 `~/.xprofile`文件。如果没有就创建一个包含[Fcitx5环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")的`~/.xprofile`文件。然后重启你的桌面会话。 

####  在 Wine 中无法使用输入法

对于运行于[Xorg](<../zh-cn/Xorg.html> "Xorg")或者Xwayland下的Wine，记得在[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")中加入 
    
    XMODIFIERS=@im=fcitx
    
运行于[Wayland](<../zh-cn/Wayland.html> "Wayland")原生模式下的Wine已经可以使用输入法，但可能不支持显示预编辑字符串。可按`Ctrl-Alt-P`快捷键来关闭预编辑功能，或者使用`FCITX_NO_PREEDIT_APPS`环境变量来对特定的程序禁用预编辑。 

##  提示和技巧

###  自定义繁简中文转换

一些IME认为默认使用简体中文，就导致了当输出一些繁体中文时字符显示的不正常，例如当输入“為什麼”时被替换成了“爲什麼”。若要修复这个问题，可以自定义`简体中文和繁体中文翻译`的用法 

为了配置转换功能，请将`简体中文转换为繁体中文的 OpenCC 属性值`设置为以下值之一： 

  * s2t - Simplified to Traditional (OpenCC) （这是默认值，也许不是你正在寻找的属性）
  * s2tw - Simplified to Traditional (Taiwan)
  * s2twp - Simplified to Traditional (Taiwan) 台湾惯用语
  * s2hk - Simplified to Traditional (Hong Kong)

若要设置反转，请将`繁体中文转换为简体中文的`设置为以下值之一： 

  * t2s - Traditional (OpenCC) to Simplified (OpenCC) （这是默认值，也许不是你正在寻找的属性）
  * tw2s - Traditional (Taiwan) to Simplified (OpenCC)
  * tw2sp - Traditional (Taiwan) to Simplified (OpenCC) 大陆习惯用语
  * t2hk - Traditional (OpenCC) to Hong Kong variant 香港变体
  * t2tw - Traditional (OpenCC) to Taiwan Standard 台湾标准
  * tw2t - Traditional (Taiwan) to Traditional (OpenCC)
  * hk2s - Traditional (Hong Kong) to Simplified (OpenCC)
  * hk2t - Traditional (Hong Kong) to Traditional Chinese (OpenCC)
  * t2jp - Traditional (Kyūjitai) to New Japanese Kanji (Shinjitai)
  * jp2t - New Japanese Kanji (Shinjitai) to Traditional (Kyūjitai)

最新列表在这：[OpenCC](<https://github.com/BYVoid/OpenCC>)。 

###  查看选中字符的 Unicode 编码

  * 如果你需要查看文本编辑器中选中文字的 Unicode 编码，那么直接选中文字，然后使用快捷键 `ctrl + alt + shift + u` 可以查看选中文字的编码。

  * 如果你需要查看非编辑区域（比如本 wiki）中文字的 Unicode 编码，那么需要首先将该段文字复制到剪贴板，然后点击任意一个可编辑区域（比如搜索框），然后使用快捷键 `ctrl + alt + shift + u` 可以查看剪贴板中文字的编码。

###  通过 Fcitx5 输入特殊字符

可以使用 Fcitx5 的 Unicode 输入功能来输入特殊字符： 

以 `①` 为例： 

将光标定位到任意一个输入框内，然后按下 `Ctrl + Alt + Shift + U`，然后输入 `circle one` 来搜索字符，你将会看到多种形式的 `①`。使用 `Alt+数字` 来选择。如果你知道要输入字符的 Unicode 编码，也可以直接按 `Ctrl + Shift + U` 然后输入编码。这些快捷键可以在设置中更改。 

如果你要经常输入某些特殊字符，可以考虑将其加入“快速输入”功能中。 

###  切换半角和全角标点

对于 [fcitx5-chinese-addons](<https://archlinux.org/packages/?name=fcitx5-chinese-addons>)包，默认情况下使用全角标点，可以使用`Ctrl+.`快捷键在全角和半角标点间切换。 

###  在 vim 中自动切换输入法

推荐使用 [fcitx.vim](<https://github.com/lilydjwg/fcitx.vim>) 插件。此插件会为不同缓冲区保持各自的插入模式输入法状态。 

有一个简单的方案，可以向 `~/.vimrc` 追加代码：[[3]](<#cite_note-3>)[[4]](<#cite_note-4>)
    
    let fcitx5state = system("fcitx5-remote")
    " 退出插入模式时禁用输入法，并保存状态
    autocmd InsertLeave * :silent let fcitx5state=system("fcitx5-remote")[0] | silent !call system("fcitx5-remote -c") 
    " 2 表示之前状态打开了输入法，则进入插入模式时启动输入法
    autocmd InsertEnter * :silent if fcitx5state == 2 | call system("fcitx5-remote -o") | endif
    
如果你使用的是新的 Vim9 语法，追加的代码应该是：
    
    # 仅在使用 vim9script 语法或带有 `vim9script` 的关键字后才会生效
    var fcitx5state = system("fcitx5-remote")
    autocmd InsertLeave * :silent fcitx5state = system("fcitx5-remote")[0] | silent !fcitx5-remote -c
    autocmd InsertEnter * :silent if fcitx5state == '2' | call system("fcitx5-remote -o") | endif
    
如果使用的是 [neovim](<https://archlinux.org/packages/?name=neovim>)包 ，则追加上述代码到 `~/.config/nvim/init.vim`。 

**注意：** 如果您在 vim.cmd 中添加此代码，可能需要将注释去掉。

###  拼音输入法

**注意：** 以下功能只对 [fcitx5-chinese-addons](<https://archlinux.org/packages/?name=fcitx5-chinese-addons>)包 中的拼音输入法有效，其他输入法请自行探索。

####  导入搜狗词库

  * 对于 KDE 用户来说，可以通过 `设置 -> 区域设置 -> 输入法 -> 拼音 -> 词典 -> 导入` 来导入搜狗词库

  * 对于使用 [fcitx5-configtool](<https://archlinux.org/packages/?name=fcitx5-configtool>)包 的用户来说，需要手动打开 “Fcitx5 配置” 这个软件，并在拼音输入法中手动配置。

既可以导入本地词库也可以**在线浏览词库并自动导入**

####  云拼音

在拼音输入法的设置页面，你可以启用云拼音。但是如果你需要更改云拼音默认的后端，则需要在 [fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 的全局设置里进行更改。提供的后端有 `Google`, `Baidu`, `GoogleCN`

####  笔画过滤

在设置的拼音输入法的“笔画过滤”后设置快捷键（默认为 ```） 然后在输入文字后，按下快捷键，输入法的候选框将会出现**笔画过滤** 字样，可以对词语进行笔画过滤，具体规则为：h 横、s 竖、p 撇、n 捺、z 折 

默认情况下，笔画过滤是对一个句子的第一个字进行筛选，但是使用**以词定字** 可以在一个句子之间的不同字之间进行切换。 

例如对词语“中华人民共和国”中的第三个字进行笔画筛选，你可以在启用笔画过滤后连续按两次 `]` 让 [fcitx5](<https://archlinux.org/packages/?name=fcitx5>)包 对其进行笔画过滤。 

**注意：** 默认情况下，**以词定字** 的快捷键为 `[` 和 `]`，该快捷键在**拼音输入法** 的设置中可以查看

####  将输入错误的单词从输入历史中删除

输入过程中有可能因为误操作写入错误单词, 此时可以通过`重新输入错误单词拼音 -> 使用忘记词汇快捷键(默认为 Ctrl + 7) -> 选择错误单词的对应数字`删除. 

快捷键可以由`Fcitx 配置 > "附加组件"标签页 > "输入法"部分 > "拼音"齿轮图标 > "忘记词汇" 快捷键`指定. 

####  输入自定义时间

在按照前文安装 [fcitx5-lua](<https://archlinux.org/packages/?name=fcitx5-lua>)包之后, 在输入`;`进入快速输入模式后可使用如下指令: 

  * `;fh`可输入特殊符号
  * `;sj`可输入当前时间, 格式默认提供3种: [15:52]，[15时52分]，[十五时五十三分]；如果输入`;sj`后按照`时:分`的格式输入，可以格式化指定时间。
  * `;rq`可输入当前日期, 格式默认提供3种: [2023-07-21]，[2023年7月21日]，[二〇二三年七月二十一日]；如果输入`;rq`后按照`年-月-日`的格式输入，可以格式化指定日期。

可通过修改`pinyin.lua`甚至`imeapi.lua`脚本扩展功能(注意备份).[[5]](<#cite_note-5>)

###  RIME/中州韵

**提示：** 所有更改皆需重新部署方可生效

####  导入词库

以导入词库[rime-pinyin-zhwiki](<https://archlinux.org/packages/?name=rime-pinyin-zhwiki>)包和[rime-pinyin-moegirl](<https://aur.archlinux.org/packages/rime-pinyin-moegirl/>)AUR为例. 

**提示：** 将自定义词库放入`~/.local/share/fcitx5/rime/`亦可,文件名(文件名.dict.yaml)应与词库名统一([词库格式](<https://github.com/rime/home/wiki/RimeWithSchemata#%E7%A2%BC%E8%A1%A8%E8%88%87%E8%A9%9E%E5%85%B8>))

1.更改`~/.local/share/fcitx5/rime/luna_pinyin.custom.yaml`文件(以`luna_pinyin`为例,其余输入方案修改方案名即可) 
    
    ~/.local/share/fcitx5/rime/luna_pinyin.custom.yaml
    
    # 文件中“patch:”应只存在一个,若已存在只需粘贴后面的代码
    # 此文件用于修改特定输入方案,把上方的luna_pinyin改为其它输入方案名即可完成对其它输入方案的修改
    patch:
        "translator/dictionary": extended #词典名字可自定义,与下方文件名保持一致即可
    
2.新建`~/.local/share/fcitx5/rime/extended.dict.yaml`文件 

**提示：** 导入自定义词库只需将词库名添加到“import_tables:”之后
    
    ~/.local/share/fcitx5/rime/extended.dict.yaml
    
    # 以下禁用了默认词库同时不启用默认的“八股文”词库及词频系统,如果您不希望候选词中的出现繁体字、方框字的话
    ---
    name: extended
    version: "2021.02.19"
    sort: by_weight
    use_preset_vocabulary: false #是否启用默认的“八股文”词库及词频系统,如需启用请设为 true 。
    import_tables:
      # - luna_pinyin #默认词库,如需启用请取消注释
      - zhwiki
      - moegirl
      # - 自定义词库名
    ...
    
####  模糊音设置

请根据需要注释(#)或删除不需要的模糊音,若需增加其它模糊音,请参考[明月拼音模糊音定制模板](<https://gist.github.com/2320943>)

若`luna_pinyin.custom.yaml`文件不存在 
    
    ~/.local/share/fcitx5/rime/luna_pinyin.custom.yaml
    
    patch:
        "speller/algebra":
            - derive/^([zcs])h/$1/ #zh,ch,sh->z,c,s
            - derive/^([zcs])([^h])/$1h$2/ #z,c,s->zh,ch,sh
            - derive/^n/l #n->l
            - derive/^l/n #l->n
            - derive/([ei])n$/$1ng/  # en -> eng, in -> ing
            - derive/([ei])ng$/$1n/ # eng->en, ing -> in
            - abbrev/^([a-z]).+$/$1/ #简拼支持
            - abbrev/^([zcs]h).+$/$1/ #模糊音的简拼支持
            delimiter: " '" #分隔符
    
如果文件存在,则粘贴`patch:`以下的部分到文件末尾(`luna_pinyin.custom.yaml`中有且只有一个`patch:`) 

####  特殊符号

**注意：** Fcitx5 已经内置了对特殊符号的支持。参阅[#通过 Fcitx5 输入特殊字符](<#%E9%80%9A%E8%BF%87_Fcitx5_%E8%BE%93%E5%85%A5%E7%89%B9%E6%AE%8A%E5%AD%97%E7%AC%A6>)

导入[rime-dict](<https://github.com/yangshann/rime-dict>)项目中`symbols.dict.yaml`词库即可在拼音中输入希腊字母、部分数学符号及Emoji表情 

示例: 

希腊字母:输入`alpha`即可输出`α`

数学符号:输入`jifen`即可输出`∫`

特殊符号:输入`cha`可输出`✕,✖`

序号:输入`qi`可输出`Ⅶ,⑦`

Emoji表情:输入`haha`可输出`😃,😆`

####  加载 librime-lua 插件

若想加载 librime-lua 插件，须在 fcitx 配置工具的 Rime 输入法设置中添加 `lua` 模块。 

##  参考来源

  1. [↑](<#cite_ref-1>) [[1]](<https://fcitx-im.org/wiki/Setup_Fcitx_5#Environment_variables>)
  2. [↑](<#cite_ref-2>) <https://github.com/WayfireWM/wayfire/issues/2315>
  3. [↑](<#cite_ref-3>) <https://www.zhihu.com/question/341748857/answer/1739052604>
  4. [↑](<#cite_ref-4>) <https://sur.moe/post/vim%E8%BE%93%E5%85%A5%E6%B3%95%E5%88%87%E6%8D%A2%E4%B8%8D%E4%BD%BF%E7%94%A8%E6%8F%92%E4%BB%B6/>
  5. [↑](<#cite_ref-5>) [fcitx5 使用自定义 lua 扩展输入当前日期和时间 - tedding's blog](<https://tedding.dev/2023/07/21/189774b2a10.html>)
