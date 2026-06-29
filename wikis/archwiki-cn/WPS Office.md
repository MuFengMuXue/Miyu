**翻译状态：**

  * 本文（或部分内容）译自 [WPS Office](<https://wiki.archlinux.org/title/WPS_Office> "arch:WPS Office")，最近一次同步于 2024-05-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/WPS_Office?diff=0&oldid=793147>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/WPS_Office_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[WPS Office for Linux](<http://linux.wps.cn/>) 是金山公司推出的、运行于 Linux 平台上的全功能办公软件。与 Microsoft Office 高度兼容，且更加尊重 Linux 用户特定的使用习惯，并自带方正字体集。 

##  安装

WPS Office for Linux 根据不同的需求被打包成了： 

软件包名称  | 说明   
---|---  
[wps-office-cn](<https://aur.archlinux.org/packages/wps-office-cn/>)AUR | WPS   
[wps-office](<https://aur.archlinux.org/packages/wps-office/>)AUR | WPS 国际版   
[wps-office-365](<https://aur.archlinux.org/packages/wps-office-365/>)AUR | WPS 365   
[wps-office-365-edu](<https://aur.archlinux.org/packages/wps-office-365-edu/>)AUR | WPS 365 教育版   
  
中文使用者还需要安装中文语言包：[wps-office-mui-zh-cn](<https://aur.archlinux.org/packages/wps-office-mui-zh-cn/>)AUR。其他各种语言的语言包在 [AUR](<https://aur.archlinux.org/packages?O=0&K=wps-office-mui>) 可以找到。 

此外可选安装 WPS 需要的字体（符号字体和方正字体，请自行分辨）：[ttf-wps-fonts](<https://aur.archlinux.org/packages/ttf-wps-fonts/>)AUR 或 [ttf-wps-win10](<https://aur.archlinux.org/packages/ttf-wps-win10/>)AUR 或 [wps-office-fonts](<https://aur.archlinux.org/packages/wps-office-fonts/>)AUR 或 [wps-office-365-edu-fonts](<https://aur.archlinux.org/packages/wps-office-365-edu-fonts/>)AUR（针对[wps-office-365-edu](<https://aur.archlinux.org/packages/wps-office-365-edu/>)AUR）。 

**注意：** 请留意自带字体的版权状况，可阅读 [WPS Office 软件个人版最终用户许可协议](<https://privacy.wps.cn/policies/eula/personal-wps-office>) 第九条特别提示条款。

软件套装中的程序可以通过如下命令启动： 

命令  | 程序   
---|---  
`wps` | WPS 文字   
`et` | WPS 表格   
`wpp` | WPS 演示   
`wpspdf` | WPS PDF   
  
##  提示与技巧

###  修改 WPS 文件图标以及文件关联

安装 WPS 后，您所用 icon-theme 中的 DOC、XLS、PPT 等文件会被替换成 WPS Office 所自带的 WPS 文字、ET 表格、WPP 演示等图标。如果您并不需要，可自行修改相关的 mime 配置文件： 
    
    /usr/share/mime/packages/wps-office-{wpp,wps,et}.xml
    /usr/share/mime/packages/freedesktop.org.xml #(属于软件包shared-mime-info)
    
以及 desktop 文件： 
    
    /usr/share/applications/wps-office-{wpp,wps,et}.desktop
    
处理策略：WPS 自己的格式由 `wps-office-{wpp,wps,et}.xml` 定义，其他的用 `freedesktop.org.xml` 定义。同时修改 `desktop` 文件的 `MimeType` 项。 

在 PKGBUILD 文件中的 `package` 函数添加以下语句： 
    
    ##et wpp wps 支持的MimeType
        _etMT="MimeType=application\/wps-office.et;application\/wps-office.ett;application\/vnd.ms-excel;\
    application\/vnd.openxmlformats-officedocument.spreadsheetml.template;\
    application\/vnd.openxmlformats-officedocument.spreadsheetml.sheet;"
        _wppMT="MimeType=application\/wps-office.dps;application\/wps-office.dpt;application\/vnd.ms-powerpoint;\
    application\/vnd.openxmlformats-officedocument.presentationml.presentation;\
    application\/vnd.openxmlformats-officedocument.presentationml.slideshow;\
    application\/vnd.openxmlformats-officedocument.presentationml.template;"
        _wpsMT="MimeType=application\/wps-office.wps;application\/wps-office.wpt;\
    application\/msword;application\/rtf;application\/msword-template;\
    application\/vnd.openxmlformats-officedocument.wordprocessingml.template;\
    application\/vnd.openxmlformats-officedocument.wordprocessingml.document;"
    
        ##mime
        sed -i '3,31d' $pkgdir/usr/share/mime/packages/wps-office-et.xml
        sed -i '3,36d' $pkgdir/usr/share/mime/packages/wps-office-wpp.xml
        sed -i '3,30d' $pkgdir/usr/share/mime/packages/wps-office-wps.xml
    
        ##desktop
        #_et
        sed -i "s/^MimeType.*$/$_etMT/" $pkgdir/usr/share/applications/wps-office-et.desktop
        #_wpp
        sed -i "s/^MimeType.*$/$_wppMT/" $pkgdir/usr/share/applications/wps-office-wpp.desktop
        #_wps
        sed -i "s/^MimeType.*$/$_wpsMT/" $pkgdir/usr/share/applications/wps-office-wps.desktop

###  使用 GTK+ UI

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 不适用于最新版本 (在[Talk:WPS Office](<../zh-cn/Talk:WPS_Office.html>)讨论)

WPS 默认的 UI 为 Qt，事实上其捆绑的 Qt 为 4.7.4，从而因为版本不符，无法正常加载 qtcurve 之类的主题。但我们可以改为 [GTK+](<../zh-cn/Qt.html#Qt5> "Qt")，直接加上参数 `-style=gtk+` 即可。 

**注意：** 使用使用 [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR 提供的 Qt 配置工具 _qtconfig-qt4_ ，将GUI Style更改为GTK+也有效果

####  修改启动 desktop 文件

修改 `/usr/share/applications/` 下以 wps-office 开头的 desktop 文件： 

**提示：** 如果你使用的 flatpak 安装的应用，请查看 `/var/lib/flatpak/exports/share/applications` 目录

找到 Exec 行，在 %f 前添加启动参数： 
    
    -style=gtk+
    
为避免软件更新后，修改被覆盖，可以选择拷贝所有需要修改的 desktop 文件到 `~/.local/share/applications/` 后，再做修改。 

**注意：** 在修改 desktop 后请运行 `update-desktop-database ~/.local/share/applications/` 命令刷新菜单缓存（该命令的参数是存放已修改过的 desktop 文件的目录）

####  修改启动脚本

修改 /usr/bin/ 目录下的 et、wpp、wps 启动脚本文件 

删除该行（如果有的话）： 
    
    gOptExt=
    
然后添加： 
    
    gOptExt="-style=gtk+"
    export GTK2_RC_FILES=/usr/share/themes/Adwaita/gtk-2.0/gtkrc
    
**注意：** 在 export 参数中可以导入其他支持GTK2的主题，对于应用界面将会呈现不一样的效果

**注意：** 对于 金山 PDF （WPS PDF） 应用，可能存在启动脚本缺失的情况，请参考下节解决方案

#####  手动修复 金山 PDF 启动脚本

金山 PDF 提供的启动脚本缺失了对 GTK 的自定义配置 可以在其启动脚本 /usr/bin/wpspdf 开始位置添加： 
    
    gOptExt="-style=gtk+"
    export GTK2_RC_FILES=/usr/share/themes/Adwaita/gtk-2.0/gtkrc
    
并在其后的 run 函数中添加 `${gOptExt}`，修改后的 run 函数如下： 
    
    function run()
    {
    	if [ -e "${gInstallPath}/office6/${gApp}" ] ; then
    		{ ${gInstallPath}/office6/${gApp} ${gOptExt} "$@"; } >/dev/null 2>&1
    	else
    		echo "${gApp} does not exist!"
    	fi
    }
    
**注意：** 由于每次升级可能导致文件修改遗失，可以考虑将 et、wpp、wps 文件复制到其他目录（例如：`~/.local/bin/`），并将其添加到 [Environment variables](<../zh-cn/Environment_variables.html> "Environment variables")

##  疑难解答

###  Zip 模板压缩包乱码

解压时用参数 `-O gb18030` 即可。 

###  公式无法正常显示

大部分数学公式的正常显示需要以下字体： 
    
    symbol.ttf webdings.ttf wingding.ttf wingdng2.ttf wingdng3.ttf monotypesorts.ttf MTExtra.ttf
    
[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中的 [ttf-wps-fonts](<https://aur.archlinux.org/packages/ttf-wps-fonts/>)AUR 包含了除monotypesorts.ttf之外的字体，直接安装即可。 

###  KDE中Microsoft Office文件格式被识别为Zip

在安装完成wps之后，系统的Microsoft Office文件格式会被识别为zip，无法与wps关联，可以通过删除/usr/share/mime/packages/下的mime文件即可修改格式识别： 
    
    sudo rm /usr/share/mime/packages/wps-office-*.xml
    sudo update-mime-database /usr/share/mime
    
###  Fcitx5 无法输入中文

该问题在国内版 [wps-office-cn](<https://aur.archlinux.org/packages/wps-office-cn/>)AUR 11.1.0.9604-1 版本更新后部分用户出现，于 [wps-office-cn](<https://aur.archlinux.org/packages/wps-office-cn/>)AUR 11.1.0.9615-1 版本修复，但是部分用户仍然需要修改环境变量（例如 `.xprofile` 文件）[[1]](<https://github.com/fcitx/fcitx5/issues/83>)： 
    
    export QT_IM_MODULE=fcitx5
    
目前可用的方法为：直接在wps启动脚本中添加export变量导出。启动脚本位于/usr/bin目录下，打开相应程序对应的启动脚本。在gOpt一行下添加 
    
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx5
    export XMODIFIERS=@im=fcitx
    
保存退出。这样就可以成功在WPS中使用fcitx5了。 

###  无法将界面切换为中文（12.1.x版本后出现）

12.1.x版本后的WPS在界面中去掉了切换语言的选项，如果需要切换为中文或其他语言，可以在wps的配置文件中指定languages选项。 

**首先，确保已经安装了中文语言包：**[wps-office-mui-zh-cn](<https://aur.archlinux.org/packages/wps-office-mui-zh-cn/>)AUR

然后，使用编辑器打开`$XDG_CONFIG_HOME/Kingsoft/Office.conf`文件添加以下内容，重启后即可显示中文： 
    
    [General]
    languages=zh_CN
    
###  GNOME桌面环境中使用暗色主题时不正常显示

在暗色主题下，WPS 的字体跟随系统主题，导致字体颜色与背景为同色，无法看清（例如WPS表格筛选窗口内的文字）。 

关于此问题可参考上面的章节：[使用_GTK+_UI](<#%E4%BD%BF%E7%94%A8_GTK+_UI>)。**对于12.1.0.x版本后的WPS，可以参考上一节通过在.desktop文件的Exec选项中单独设置XDG_CONFIG_HOME解决。**

###  KDE下dpi不对称导致的字体模糊

wps office默认设置dpi为96。但是当kde DPI非96时，会强制修改wps的dpi导致字体模糊 

此时只需要在wps（包括wps,wps文字，wps表格，wps演示，wpsPDF）的desktop文件中第四行的Exec添加QT_SCREEN_SCALE_FACTORS=1 即可。如： 
    
    Exec= env QT_SCREEN_SCALE_FACTORS=1 /usr/bin/wps %U
    Exec= env QT_SCREEN_SCALE_FACTORS=1 /usr/bin/wpp %F
    
###  wpspdf 无法打开 PDF 文件

wpspdf 依赖于 libtiff5.so.5 以支撑其 PDF 功能。而系统更新后，Arch Linux 提供的是 libtiff.so.6 或更新版本，导致其无法正常工作。解决方案： 

安装 [libtiff5](<https://aur.archlinux.org/packages/libtiff5/>)AUR。 

###  字体太粗

**注意：** 该问题在国内版12.1.0.17885-1版本中已解决，但截至2024年12月17日，在国际版中尚未解决。

版本 11.1.0.11704-1 与 freetype2 版本 2.13.1 和 2.13.2 兼容性不佳。通常，如果所选字体没有粗体版本，freetype2 会通过算法生成伪粗体（fakebold），但在这种情况下，wps-office 也自行将字体设为粗体，结果是文本看起来特别粗，标题、粗体文本几乎不可用。 

解决方案为安装[freetype2-wps](<https://aur.archlinux.org/packages/freetype2-wps/>)AUR，重启WPS即可生效。 

另一种办法是在wps的desktop文件中添加旧的freetype2库文件位置的环境变量，详见 [[2]](<https://aur.archlinux.org/packages/wps-office-cn#comment-937115>)。 

##  参见

  * [How to associate all Microsoft office files to WPS office applications?](<https://archived.forum.manjaro.org/t/how-to-associate-all-microsoft-office-files-to-wps-office-applications/33528/6>)
