**翻译状态：**

  * 本文（或部分内容）译自 [Mathematica](<https://wiki.archlinux.org/title/Mathematica> "arch:Mathematica")，最近一次同步于 2024-05-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/Mathematica?diff=0&oldid=794976>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Mathematica_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [应用程序列表/科学](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E7%A7%91%E5%AD%A6.html> "应用程序列表/科学")
  * [SageMath](<../zh-cn/SageMath.html> "SageMath")
  * [Matlab](<../zh-cn/MATLAB.html> "Matlab")

[Mathematica](<https://en.wikipedia.org/wiki/Wolfram_Mathematica> "wikipedia:Wolfram Mathematica") 是用于科学，工程和数学领域的商业软件。在这里我们说明如何安装它。 

##  安装

由于 Mathematica 是专有软件，升级可能会产生成本，因此本节列出了不同可用版本的说明。 

### Mathematica 6

####  挂载 iso 文件

挂载 Mathematica `.iso` 的一种方式是创建 `/media/iso` 目录用于挂载，并在 [fstab](<../zh-cn/Fstab.html> "Fstab") 中增加这几行： 
    
    /_location/of/mathematica.iso_ /media/iso iso9660 exec,ro,user,noauto,loop=/dev/loop0   0 0
    
然后就可以这样挂载它： 
    
    # mount /media/iso
    
####  运行安装程序

运行 _MathInstaller_ ： 
    
    # cd Unix/Installer
    # sh ./MathInstaller
    
**注意：** 如果没有把 "sh" 放在前面，那么会得到一个关于解释器出错 (bad interpreter) 的错误信息。

####  字体

向 FontPath 里添加包含 Type1 和 BDF 字体的目录。 

### Mathematica 7

Mathematica 7 安装起来非常方便。 
    
    #tar xf Mathematica-7.0.1.tar.gz
    #cd Unix/Installer
    #./MathInstaller
    
按照指示完成即可。 

KDE 用户注意，Mathematica 的图标可能会出现在 _Lost & Found_ 分类里面。解决方法是以 root 用户身份运行下列命令： 
    
    # ln -s /etc/xdg/menus/applications-merged /etc/xdg/menus/kde-applications-merged
    
### Mathematica 8

Mathematica 8 的一个问题是执行 WolframAlpha[ ] 函数时会出现崩溃，这个崩溃可以重现。Mathematica 的默认配置为，在设置如何连接到互联网以获取数据时，检测系统的代理设置。但是在调用库函数时存在一个 bug，最终会使 Mathematica 崩溃。解决方法是通过将 Mathematica 配置为“直接连接”到互联网来完全避免此库调用 (_Edit > Preferences > Internet Connectivity > Proxy Settings_)。这个错误已经报告给 Wolfram。 

### Mathematica 10

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mathematica](<https://aur.archlinux.org/packages/mathematica/>)AUR （需要旧版本）。需要 `Mathematica_10.XX.YY_LINUX.sh` 安装脚本，从 Wolfram.com 或某大学的站点上下载。同时你还需要一个激活密钥。 

### Mathematica 11

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mathematica](<https://aur.archlinux.org/packages/mathematica/>)AUR。从 Wolfram Research 获取 `Mathematica_11.XX.YY_LINUX.sh` 和激活密钥，并将其保存到软件包构建目录。成功地安装可能也会抛出一些不严重的错误：xdg-icon-resource, mkdir, xdg-desktop-menu 等。详细信息请见[mathematica PKGBUILD file](<https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=mathematica>)。 

Mathematica 11 在 [$UserDocumentsDirectory](<https://reference.wolfram.com/language/ref/$UserDocumentsDirectory.html>) 自动创建 'Wolfram Mathematica' 文件夹，Mathematica 根据 [XDG user directories](<../zh-cn/XDG_user_directories.html> "XDG user directories") 自动设置了这个变量。、 

### Mathematica 12

  1. [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [avahi](<https://archlinux.org/packages/?name=avahi>)包 和 [inetutils](<https://archlinux.org/packages/?name=inetutils>)包。
  2. [启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")服务`avahi-daemon.service`。
  3. 检查`hostnamectl`是否包括静态或临时主机名。
  4. 从 [Wolfram](<https://account.wolfram.com/products/downloads/mathematica>) 获取安装脚本，文件名为`Mathematica_12.XX.YY_LINUX.sh`。
  5. 确保 `Mathematica_12.XX.YY_LINUX.sh ` 具有[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")权限。
  6. 以root身份运行安装脚本。若以普通身份运行，安装脚本将请求另一个安装目录。

    # ./Mathematica_12.XX.YY_LINUX.sh
    
### Mathematica 13

安装步骤与Mathematica 12相同。 

##  故障排除

###  "Missing symbols" 错误

如果出现字体渲染问题，某些符号无法显示（比如 `/` 显示为正方形），请尝试[这种](<https://mathematica.stackexchange.com/questions/1158/invisible-conjugate-glyph-in-the-linux-frontend>)方案。其中还说明了 Mathematica 版本 9 修复了这个问题。 

尝试让应用程序使用抗锯齿。 对于 KDE 用户： _System Settings > Application Appearance > Fonts > Use anti-aliasing (Enabled)_

###  HiDPI / Retina 屏幕

如果你有一块 [HiDPI](<../zh-cn/HiDPI.html> "HiDPI") 屏幕，比如 Apple Retina 屏幕，而且 Mathematica 里面的文字非常小，这样就能解决： 

  * 打开 _Edit > Preferences_
  * 在 _Advanced_ 选项卡里单击 _Open Option Inspector_
  * 在右侧的树状列表中找到 _Formatting Options > Font Options > Font Properties_
  * 改变 _"ScreenResolution"_ 的值到它原来的两倍大小，比如将 72 改为 144。你也可以用 `xdpyinfo | grep resolution` 来获得一个更精确的数字（也要变成原来的两倍大小）。

###  与系统库冲突导致的问题

Mathematica 软件包包含了一系列其自有的库，存放在 `<INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64` 里面。它们可能会导致一些兼容性问题，并且可能需要将某些库回退到系统现有版本。 

####  Symbol lookup error: /usr/lib/libfontconfig.so.1: undefined symbol: FT_Done_MM_Var

强制 Mathematica 使用系统自有的 freetype 库。 
    
    # cd <INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64
    # mv libfreetype.so.6 libfreetype.so.6.old
    
####  Mathematica/11.3/SystemFiles/Libraries/Linux-x86-64/libz.so.1: version `ZLIB_1.2.9' not found (required by /usr/lib/libpng16.so.16)

强制 Mathematica 使用系统自有的 zlib 库。 
    
    # cd <INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64
    # mv libz.so.1 libz.so.1.old
    
##  参阅

  * [Official site](<https://www.wolfram.com/mathematica/>)
  * [Official Support](<https://www.wolfram.com/support/>)
