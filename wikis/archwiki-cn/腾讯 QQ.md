QQ 是腾讯公司开发的即时通讯软件，为 ICQ 的仿制品，是中国最流行的 IM 软件之一。本页面列出了在 Arch Linux 上使用 QQ 的各种解决方案。 

##  原生 Linux 版本

使用 Electron 技术的 Linux QQ 对应的软件包为 [linuxqq](<https://aur.archlinux.org/packages/linuxqq/>)AUR。 

**注意：** 官方版本提供的是普通 QQ，TIM 没有官方版本。如果要使用 TIM，请使用 [wine 方案](<#Wine>)。

###  带有 bubblewrap 沙盒的版本

此外还有 [linuxqq-nt-bwrap](<https://aur.archlinux.org/packages/linuxqq-nt-bwrap/>)AUR 可选，带有 bubblewrap 沙盒和一些调整。 

  * 要传递给 **bwrap** 的自定义参数应该写在 `~/.config/qq-bwrap-flags.conf`，可在此文件中设置自定义挂载目录。
  * 要传递给 **electron** 的自定义参数应该写在 `~/.config/qq-electron-flags.conf`。

##  虚拟机

您可以在虚拟机中运行一个完整的 Windows 系统，并在此中运行 QQ。相比于其他的方案，这种方案出错的几率是最小的，缺点是占用的资源较多。 

**提示：**

  * 根据[许可条款](<https://www.microsoft.com/en-us/Useterms/OEM/Windows/10Mobile/UseTerms_OEM_Windows_10Mobile_ChineseSimplified.htm>)，在每个虚拟设备上运行 Windows 都需要单独的授权。
  * 如果您使用 VirtualBox，建议您开启**[无缝模式](<https://www.virtualbox.org/manual/ch04.html#seamlesswindows>)** ，这个功能能让您在宿主机的桌面下无缝操作虚拟机中的窗口。

## Wine

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 在qqlinux原生版本更新之后大部分wine-qq上游并没有继续维护了,基本上都因为qq版本过旧无法运行。 (在[Talk:腾讯 QQ](<../zh-cn/Talk:%E8%85%BE%E8%AE%AF_QQ.html>)讨论)

[Wine](<../zh-cn/Wine.html> "Wine") 是类 UNIX 系统下运行微软 Windows 程序的"兼容层"，可以用它模拟 Windows 环境来运行 QQ/TIM。 

**警告：** Wine QQ/TIM 在平铺式窗口管理器下的样式可能会大规模失控，需要进行[额外的配置](<#%E5%B9%B3%E9%93%BA%E5%BC%8F%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E4%B8%8B%E7%9A%84%E9%85%8D%E7%BD%AE>)。

###  Ukylin Wine（优麒麟Wine）

[ukylin-wine](<https://aur.archlinux.org/packages/ukylin-wine/>)AUR 是基于 Wine 开发的一款软件，用于在 Linux 系统上兼容运行 Windows 软件。其对微信和QQ/TIM进行了大量的修复以确保软件稳定。如果您在使用 TIM 时遇到了不停的卡顿（包括但不限于群详情页、右键菜单和表情面板），不妨尝试使用 ukylin-wine 替换其他版本的 wine 来启动 TIM。 

例：替换 Spark-TIM 启动脚本中的 APPRUN_CMD 
    
    /opt/apps/com.qq.tim.spark/files/run.sh:14
    
    export APPRUN_CMD="ukylin-wine"
    
### Crossover

可以使用 [CrossOver](<../zh-cn/CrossOver.html> "CrossOver") 运行 QQ 和 TIM。更多详情可以参阅 [CrossOver 的兼容性列表](<https://www.codeweavers.com/compatibility>)。 

###  手动 Wine 方案

#### TIM

安装 [wine](<https://archlinux.org/packages/?name=wine>)包、[wine-gecko](<https://archlinux.org/packages/?name=wine-gecko>)包 和 [wine-mono](<https://archlinux.org/packages/?name=wine-mono>)包。 

执行 `winetricks riched20`，也可使用 `winecfg` 设置函数库顶替。 

可能需要配置中文字体显示，见[#字体配置](<#%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE>)。 

安装 TIM。 

#####  生成图标

安装的 TIM 可能没有在程序列表中生成图标。若要自行添加图标，新建 `tim.desktop` 文件，写入以下内容： 
    
    tim.desktop
    
    [Desktop Entry]
    Encoding=UTF-8
    Version=1
    Name=TIM
    Comment=Tencent TIM
    Exec=wine '~/.wine/drive_c/Program Files/Tencent/TIM/Bin/TIM.exe'
    Icon=~/.wine/drive_c/Program Files/Tencent/TIM/TIMUninst.ico
    Terminal=false
    Type=Application
    Categories=Network;

将 `tim.desktop` 移动到 `~/.local/share/applications` 或 `/usr/share/applications`文件夹下即可。 

##  第三方客户端

**注意：** 请尽量使用含 wine 在内的方案或来自腾讯官方的客户端。第三方客户端尽管不存在官方客户端的一系列问题，但随时可能因为种种原因而失效。

###  Icalingua++

[Icalingua++](<https://github.com/Icalingua-plus-plus/Icalingua-plus-plus>) 是 Icalingua 的分支，为已经删除的 Icalingua 提供有限的更新。此项目希望为 Linux 打造一个会话前端框架，通过实现 Adapter 后端接口来适配各种聊天平台。目前已经拥有基于 oicq 以及 Icalingua 自有协议的后端。 

要使用 Icalingua++ ，可以从 AUR 源安装[icalingua++](<https://aur.archlinux.org/packages/icalingua%2B%2B/>)AUR。 

##  疑难解答

###  原生版本(Linux QQ)

####  无法使用通知功能

如果在 QQ 中无法使用桌面环境的通知功能，可以尝试安装[XDG桌面门户](<../zh-cn/XDG_%E6%A1%8C%E9%9D%A2%E9%97%A8%E6%88%B7.html> "XDG桌面门户")中对应的桌面后端。也可能是在设置-消息通知中关闭了通知，但Linux版本没有此设置，需要在Windows或macOS上的QQ中修改。 

####  打开窗口/设置/接受消息闪退

你可以尝试以下命令: 

`sudo rm -rf ~/.config/QQ/crash_files/ && sudo chattr +i ~/.config/QQ/crash_files/`

####  每次登录都需要重新扫码

如果即使在登录时勾选了无需在手机端确认，下次登录时还需要扫码，这可能是因为其是根据网卡mac地址来判断是否为同一设备，你可以尝试禁用虚拟网卡(例如:Docker网卡,VMWare网卡)来解决这个问题。 

###  wine版

####  无法调用输入法

如果在 QQ 中使用输入法无反应，可考虑在 QQ 的启动脚本中配置有关环境变量，示例如下（将 fcitx 改成你用的输入法）。 
    
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS=@im=fcitx
    
[com.qq.im.deepin](<https://aur.archlinux.org/packages/com.qq.im.deepin/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]等默认脚本中可能存在将输入法配置为 ibus 的行，如果你要使用其它输入法，需将这些行删去。 

####  字体配置

如果中文的显示遇到问题，可以尝试先执行 `winetricks fakechinese`。 

另请参阅[字体](<../zh-cn/Wine.html#%E5%AD%97%E4%BD%93> "Wine")和[字体配置#不支持 Fontconfig 的程序](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html#%E4%B8%8D%E6%94%AF%E6%8C%81_Fontconfig_%E7%9A%84%E7%A8%8B%E5%BA%8F> "字体配置")。 

#####  字体替换不完全/显示宋体发虚

先使用 fakechinese 替换完字体后，再参考 [https://bbs.deepin.org/zh/post/213530](<https://web.archive.org/web/20221106064119/https://bbs.deepin.org/en/post/213530>) 和 [https://bbs.deepin.org/post/213153](<https://web.archive.org/web/20221106064052/https://bbs.deepin.org/en/post/213153>) 使用伪装的宋体。 

####  文件被占用

杀死 QQ 或 TIM 的进程即可。 在退出 QQ/TIM 之后，某些相关进程仍然在后台运行。也可以使用如下脚本来启动 QQ/TIM，它会首先查找已有的进程，杀死该进程后启动新的 QQ/TIM。 
    
    start-tim.sh
    
    #!/bin/sh
    # script to start TIM
    # kill TIM before start TIM
    for pid in `pgrep TIM.exe`; do
    	if [ -n ${pid} ]; then
    		kill ${pid}
    	fi
    done
    # start TIM
    wine '~/.wine/drive_c/Program Files/Tencent/TIM/Bin/TIM.exe'
    
上面的例子适用于 TIM，稍作修改之后即可应用于 QQ。 

####  xfce4（xfwm4）下无法输入表情

打开设置管理器-窗口管理器微调-焦点，取消勾选激活焦点防窃取和遵照标准的 ICCCM 焦点提示即可。 

原因是表情窗口获取焦点时会发生不兼容现象。 

####  在非中文 locale 下无法输入中文

修改 `.desktop` 文件的 `Exec`，这个文件一般位于 `/usr/share/applications/` 或者 `~/.local/share/applications/`。 

在 `Exec` 行中加入 `env LC_ALL=zh_CN.UTF-8`。 例如，原来的 `Exec` 为： 
    
    Exec=".wine/drive_c/Program Files/QQ/Bin/QQ.exe"
    
则应改为： 
    
    Exec=env LC_ALL=zh_CN.UTF-8 wine ".wine/drive_c/Program Files/QQ/Bin/QQ.exe"
    
####  deepinwine方案在非中文 locale 下字体显示为黑框且能够调用输入法但是无法输入字符

首先查看是否安装有中文locale。在 `/etc/locale.gen` 中启用zh_CN.UTF-8 UTF-8(删除#符号)。而后运行命令 `locale-gen`。 

安装了中文locale后，修改deepinwine的启动脚本，其位于 `/opt/deepinwine/tools/` 。其中有三个脚本，分别为 `run.sh`， `run_v2.sh`， `run_v3.sh`。将三个脚本中的 
    
    WINE_CMD="deepin-wine"
    
都修改为 
    
    WINE_CMD="LC_ALL=zh_CN.UTF-8 deepinwine"
    
也可以根据对应deepinwine容器的启动脚本（一般路径为 `/usr/share/applications/*.desktop` ）中的Exec行确定要修改的脚本。 

####  HiDPI 支持

在 HiDPI 显示器上，QQ/TIM 的界面可能会过小。在较新版本的 QQ/TIM 中已经加入了对 HiDPI 的支持。只需手动调整 Wine 的 DPI 即可。 

执行 `winecfg`，在打开的窗口中切换到**显示** 选项卡并调整 DPI。 

**注意：** 如果您使用的不是默认的 Wine 容器（例如使用了deepin QQ/TIM），那么需要在执行 `winecfg` 时指定`WINEPREFIX` 变量。例如`env WINEPREFIX=$HOME/.deepinwine/Deepin-QQ deepin-wine winecfg` 或是 `env WINEPREFIX=$HOME/.deepinwine/Deepin-TIM deepin-wine winecfg`。

####  平铺式窗口管理器下的配置

###### Awesome

Wine QQ/TM 在平铺式窗口管理器下可能会失控，需要进行一些配置。 

下面的配置有这些作用： 

  * 将所有 TM 的窗口设置为浮动。

  * 清除不需要的窗口边框、避免菜单弹出时焦点移动到菜单上。

  * 在使用标签式会话窗口时，增加[使用 Alt+数字来切换标签页](<https://blog.lilydjwg.me/2013/11/15/switch-tabs-with-alt-num-in-wined-tm-exe-in-awesome.41729.html>)的快捷键，需要安装 [xdotool](</wzh/index.php?title=Xdotool&action=edit&redlink=1> "Xdotool（页面不存在）")。

  * 自动关闭弹出的新闻窗口。

将以下内容添加到 [Awesome](<../zh-cn/Awesome.html> "Awesome") 配置： 
    
    function myfocus_filter(c)
      if awful.client.focus.filter(c) then
        -- This works with tooltips and some popup-menus
        if c.class == 'Wine' and c.above == true then
          return nil
        elseif c.class == 'Wine'
          and c.type == 'dialog'
          and c.skip_taskbar == true
          and c.size_hints.max_width and c.size_hints.max_width < 160
          then
          -- for popup item menus of Photoshop CS5
          return nil
        else
          return c
        end
      end
    end
    
    awful.rules.rules = {
      -- All clients will match this rule.
      {
        rule = { },
        properties = {
          -- 这里使用我们自己的函数
          focus = myfocus_filter,
          -- 以下是默认的部分
          border_width = beautiful.border_width,
          border_color = beautiful.border_normal,
          keys = clientkeys,
          buttons = clientbuttons,
        }
      }, {
        rule_any = { 
          instance = {'TM.exe', 'QQ.exe'},
        },
        properties = {
          -- This, together with myfocus_filter, make the popup menus flicker taskbars less
          -- Non-focusable menus may cause TM2013preview1 to not highlight menu
          -- items on hover and crash.
          focusable = true,
          floating = true,
          -- 去掉边框
          border_width = 0,
        }
      }, {
        -- 其它规则
      }
    }
    
    alt_switch_keys = awful.util.table.join(
        -- it's easier for a vimer to manage this than figuring out a nice way to loop and concat
        awful.key({'Mod1'}, 1, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+1') end),
        awful.key({'Mod1'}, 2, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+2') end),
        awful.key({'Mod1'}, 3, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+3') end),
        awful.key({'Mod1'}, 4, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+4') end),
        awful.key({'Mod1'}, 5, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+5') end),
        awful.key({'Mod1'}, 6, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+6') end),
        awful.key({'Mod1'}, 7, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+7') end),
        awful.key({'Mod1'}, 8, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+8') end),
        awful.key({'Mod1'}, 9, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+9') end)
    )
    function bind_alt_switch_tab_keys(client)
        client:keys(awful.util.table.join(client:keys(), alt_switch_keys))
        end -- }}}
        
        client.connect_signal("manage", function (c, startup)
      -- 其它配置
    
      if c.instance == 'TM.exe' then
        -- 添加 Alt+n 支持
        bind_alt_switch_tab_keys(c)
        -- 关闭各类新闻通知小窗口
        if c.name and c.name:match('^腾讯') and c.above then
          c:kill()
        end
      end
    
      -- 其它配置
    end)
    
也可以看看完整 [Awesome 配置](<https://github.com/lilydjwg/myawesomerc>)。 

###### i3

原生配置下，启动 `qq` 时会自动最大化，且边框不美观，可在 [i3](<../zh-cn/I3.html> "I3") 的 `config` 设置如下两条规则以改善： 
    
    for_window [instance="QQ.exe"] floating enable
    for_window [instance="QQ.exe"] border none
    
在i3status中，tim托盘可能无法正常显示。推荐您使用[i3status-rust](<https://github.com/greshake/i3status-rust>)作为替代。可以安装包： 
    
    [i3status-rust-git](<https://aur.archlinux.org/packages/i3status-rust-git/>)AUR
    [i3status-rust](<https://archlinux.org/packages/?name=i3status-rust>)包
    
##  参阅

  * [openSUSE wiki](<https://zh.opensuse.org/SDB:QQ>)
  * [Web 端的 QQ 群空间](<http://qun.qzone.qq.com/>)当所使用 QQ 客户端不支持群空间时，可以此用该服务代替。
  * [IM QQ-QQ 手机版](<https://im.qq.com/mobileqq/>)移动端也未尝不也是一种代替方案。
  * [hillwoodroc/winetricks-zh](<https://github.com/hillwoodroc/winetricks-zh>) hillwoodroc/winetricks-zh
