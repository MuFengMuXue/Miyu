**翻译状态：**

  * 本文（或部分内容）译自 [Xdg-menu](<https://wiki.archlinux.org/title/Xdg-menu> "arch:Xdg-menu")，最近一次同步于 2020-04-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xdg-menu?diff=0&oldid=604755>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xdg-menu_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

xdg-menu是一个用于为以下窗口管理器生成[XDG桌面菜单](<https://specifications.freedesktop.org/menu-spec/menu-spec-latest.html>)的工具： 

  * [awesome](<../zh-cn/Awesome.html> "Awesome")
  * [Blackbox](<../zh-cn/Blackbox.html> "Blackbox")
  * [Fluxbox](<../zh-cn/Fluxbox.html> "Fluxbox")
  * [FVWM](<https://wiki.archlinux.org/title/FVWM> "en:FVWM")
  * [IceWM](<../zh-cn/IceWM.html> "IceWM")
  * [Openbox](<../zh-cn/Openbox.html> "Openbox")
  * [twm](<../zh-cn/Twm.html> "Twm")
  * [Window Maker](<https://wiki.archlinux.org/title/Window_Maker> "en:Window Maker")

KDE, Gnome, Xfce，Enlightenment已经兼容XDG。 

##  安装

安装[archlinux-xdg-menu](<https://archlinux.org/packages/?name=archlinux-xdg-menu>)包包。 

##  菜单层级结构

  * 应用 
    * 辅助功能
    * 附件
    * 开发
    * 教育
    * 游戏
    * 图形
    * 互联网
    * 多媒体
    * 办公
    * 其他
    * 科学
    * 设置
    * 系统

##  配置

Xdg_menu依赖三类信息来生成菜单：一个根菜单（即通常通过命令行传入的 XML 菜单模板）、上次运行时缓存的信息，以及一系列配置文件。 

  * 你可以在`/etc/xdg/menus`中找到一些XML菜单模板.
  * 如果更改 xdg_menu 的代码以更改菜单布局，请确保删除`~/.xdg_menu_cache`中的所有内容，否则你可能将花费数小时试图弄明白为什么对Perl脚本所做的修改没有生效。
  * 各个应用程序的配置文件位于`/usr/share/applications`。

其他配置文件目录可以在`/usr/share`下找到。在大多数情况下，你无需改动这些文件。不过，如果你希望调整菜单的布局，可以通过修改菜单模板以进行小幅调整。若需大幅改动，则需要直接修改Xdg_menu的Perl脚本本身。 

如果你发现某些应用程序未显示在菜单中，或者其名称显示异常，那么你需要检查 `/usr/share/applications` 目录下的相应 `.desktop` 文件，并参考[桌面入口规范](<https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html>)。 

###  从其他目录添加桌面入口

默认情况下，Xdg-menu会加载那些将桌面入口（desktop entry）安装到`/usr/share/applications`的应用程序。若要将桌面入口安装在用户目录（例如`~/.local/share/applications`）中的应用程序也加入菜单的菜单中，需编辑`/etc/xdg/menus/arch applications.menu`文件，并为相关目录添加`<AppDir>`标签，如下所示： 
    
    /etc/xdg/menus/arch-applications.menu
    
    <Menu>
    
      <Name>Applications</Name>
      <Directory>Arch-Applications.directory</Directory>
      <DefaultAppDirs/>
      **< AppDir>/home/_username_ /.local/share/applications</AppDir>**
      <DefaultDirectoryDirs/>
      <DefaultMergeDirs/>
      ...
    
##  使用

### xdg_menu
    
    xdg_menu [--format <format>] [--desktop <desktop>] 
             [--charset <charset>] [--language <language>]  
    	 [--root-menu <root-menu>] [--die-on-error]
    	 [--fullmenu] [--help]
    		 
    	format - output format
    	         possible formats: twm, WindowMaker, fvwm2, icewm, ion3
    	                           blackbox, fluxbox, openbox, 
    				   xfce4, openbox3, openbox3-pipe, awesome
    				   readable
    		 default: WindowMaker
    		
     	fullmenu  - output a full menu and not only a submenu
    
    	desktop - desktop name for NotShowIn and OnlyShowIn
    		 default: the same as format
    			 
    	charset - output charset
    		 default: <locale>
    			 
    	language - output language
    		 default: <locale>
    			 
    	root-menu - location of root menu file
    		 default: /opt/gnome/etc/xdg/menus/applications.menu
    			 
    	die-on-error - abort execution on any error, 
    		 default: try to continue
    
    	verbose - print debugging information
    		 
    	help - print this text
    
### update-menus

**update-menus** 可根据 XDG 数据更新窗口管理器（WM）的菜单，并可配置为自动执行此操作。 

该脚本是xdg_menu的一个封装，依赖于 `/etc/update-menus.conf`配置文件 

要使用它，你需要安装 [archlinux-xdg-menu](<https://archlinux.org/packages/?name=archlinux-xdg-menu>)包 (其中包含xdg_menu) 

在`/etc/update-menus.conf` 文件中，你需要从支持的窗口管理器列表中选择需要为其生成菜单的WM。配置文件中允许使用#添加注释。 

所有生成的菜单都会存放在`/var/cache/xdg-menu/`目录下。有关具体窗口管理器的配置示例，请参阅本页的“[WM特定示例](<https://wiki.archlinux.org/title/Xdg-menu#Examples> "en:Xdg-menu")”部分。 

##  示例

###  Awesome窗口管理器

####  使用 xdg_menu ：
    
    $ xdg_menu --format awesome > ~/.config/awesome/xdg_menu.lua
    
编辑 rc.lua ，按如下方式更改 

  * 添加一行require语句，以加载你生成的xdg_menu.lua文件
  * 在你的awful.menu对象中添加一个菜单项，调用xgd_menu生成的应用程序菜单

    ...
    xdg_menu = require("xdg_menu")
    ...
    
    ...
    mymainmenu = awful.menu({ items = { { "awesome", myawesomemenu, beautiful.awesome_icon },
                                        { "Applications", xdg_menu },
                                        { "open terminal", terminal }
                                      }
                            })
    ...

### IceWM

##  使用 xdg_menu
    
    $ xdg_menu --format icewm --fullmenu --root-menu /etc/xdg/menus/arch-applications.menu >>~/.icewm/programs
    
####  使用 update-menus

  * 在 /etc/update-menus.conf 取消对icewm的注释
  * 使用root用户运行 update-menus 命令
  * 将 ~/.icewm/programs 符号链接到 /var/cache/xdg-menu/icewm/programs

### Ion3

####  使用 xdg_menu
    
    $ xdg_menu --format ion3  --root-menu /etc/xdg/menus/arch-applications.menu >~/.ion3/default-session--0/_xdg-menu.lua
    
之后，将 cfg_menus.lua 更改为包含 _xdg-menu.lua 文件，并将菜单添加到主菜单中。例如： 
    
    ...
    
    dopath("_xdg-menu")
    
    -- Main menu
    defmenu("mainmenu", {
        submenu("XDG Menu",         "<NAME-OF-FIRST-MENU-IN-_xdg-menu.lua-FILE>"),
        submenu("Programs",         "appmenu"),
        menuentry("Lock screen",    "ioncore.exec_on(_, 'xlock')"),
        menuentry("Help",           "mod_query.query_man(_)"),
        menuentry("About Ion",      "mod_query.show_about_ion(_)"),
        submenu("Styles",           "stylemenu"),
        submenu("Session",          "sessionmenu"),
    })
    
    ...
    
####  使用update-menus

  * 在 /etc/update-menus.conf 取消对ion3的注释
  * 使用root用户运行 update-menus 命令
  * 将 cfg_menus.lua 更改为包含 xdg-menu.lua 文件，并将菜单添加到主菜单中

例如: 
    
    ...
    
    dopath("/var/cache/xdg-menu/ion3/xdg-menu.lua")
    
    -- Main menu
    defmenu("mainmenu", {
        submenu("XDG Menu",         "<NAME-OF-FIRST-MENU-IN-xdg-menu.lua-FILE>"),
        submenu("Programs",         "appmenu"),
        menuentry("Lock screen",    "ioncore.exec_on(_, 'xlock')"),
        menuentry("Help",           "mod_query.query_man(_)"),
        menuentry("About Ion",      "mod_query.show_about_ion(_)"),
        submenu("Styles",           "stylemenu"),
        submenu("Session",          "sessionmenu"),
    })
    
    ...
    
### FluxBox

####  使用 xdg_menu
    
    $ xdg_menu --format fluxbox  --root-menu /etc/xdg/menus/arch-applications.menu >~/.fluxbox/my-menu
    
将菜单文件更改为包含生成的菜单。 

例如添加行: 
    
    [include] (my-menu)
    
####  使用 update-menus

  * 在 /etc/update-menu.conf 中取消对fluxbox的注释
  * 使用root用户运行 update-menus
  * 将菜单文件更改为包含生成的菜单

例如添加行: 
    
    [include] (/var/cache/xdg-menu/fluxbox/boxrc)
    
### OpenBox

####  使用 xdg_menu

生成菜单: 
    
    $ xdg_menu --format openbox3 --root-menu /etc/xdg/menus/arch-applications.menu > xdg-menu.xml
    
然后手动将其添加到 menu.xml 中。例如，将 xdg-menu.xml 放入 menu.xml 并添加： 
    
    <menu id="Applications" />

进入根菜单。 

####  作为管道菜单

使用 xdg_open 作为管道菜单，您可以获得额外的好处，即在安装新应用程序时，菜单会自动更新。 

在 menu.xml 中的根菜单标记之间添加以下内容: 
    
    <menu id="applications" label="Applications" execute="xdg_menu --format openbox3-pipe --root-menu /etc/xdg/menus/arch-applications.menu" />

一个非常基本的例子: 
    
    <?xml version="1.0" encoding="UTF-8"?>
    
    <openbox_menu xmlns="<http://openbox.org/3.4/menu>">
    
    <menu id="root-menu" label="Openbox 3">
      <menu id="applications" label="Applications" execute="xdg_menu --format openbox3-pipe --root-menu /etc/xdg/menus/arch-applications.menu" />
      <separator />
      <item label="Log Out">
        <action name="Exit">
          <prompt>yes</prompt>
        </action>
      </item>
    </menu>
    
    </openbox_menu>

####  使用 update-menus

  * 在 /etc/update-menu.conf 中取消对openbox的注释
  * 以root用户运行 update-menus
  * 将 menu.xml 文件更改为包含生成的菜单

例如，在根菜单中添加以下内容: 
    
    <menu id="xdg-menu" label="XDG Menu" execute="cat /var/cache/xdg-menu/openbox/menu.xml"/>

### Twm

####  使用 xdg_menu

使用 
    
    $ xdg_menu --format twm --root-menu /etc/xdg/menus/arch-applications.menu >my-twm-menu
    
并手动添加到 twmrc 中。对于具有m4预处理的twm衍生物，如vtwm或ctwm，可通过添加 
    
    sinclude(`/PATH/TO/my-twm-menu')
    
到 *twmrc. 

####  使用 update-menus

  * 在 /etc/update-menu.conf 中取消对twm的注释
  * 添加到 /etc/X11/twm/system.twmrc 文件应用程序菜单中 (添加以下这行:

     "apps"          f.menu "Applications"
    
)到菜单中 

  * 使用root用户运行 update-menus
  * 运行 twm -f /var/cache/xdg-menu/twm/twmrc

(您还需要将其他自定义项添加到 /etc/X11/twm/system.twmrc) 

### WindowMaker

####  使用 xdg_menu

使用 
    
    $ xdg_menu --format WindowMaker --root-menu /etc/xdg/menus/arch-applications.menu >my-wm-menu
    
然后添加 
    
    #include "my-wm-menu"
    
到你的 WindowMaker 菜单文件。 

您还可以使用WPrefs“应用程序菜单定义”，并将xdg命令作为参数添加到“生成的子菜单”对象中。 

####  使用 update-menus

  * 在 /etc/update-menus.conf 取消对 WindowMaker 的注释
  * 用root用户运行 update-menus
  * 添加

    #include "/var/cache/xdg-menu/WindowMaker/wmrc"
    
到你的菜单文件 

### Fvwm2

####  使用 xdg_menu

生成菜单 
    
    $ xdg_menu --format fvwm2 --root-menu /etc/xdg/menus/arch-applications.menu >fvwm2-menu
    
然后把菜单添加到根菜单 
    
    read fvwm2-menu
    
    AddToMenu MenuFvwmRoot  "Root Menu"             Title
    +                       "&0. XDG Menu"          Popup xdg_menu
    
####  使用 update-menus

  * 在 /etc/update-menus.conf 取消对 fvwm2 的注释
  * 使用root用户运行 update-menus
  * 修改你的 .fvwm2rc 以使其包含创建的菜单，示例:

    AddToMenu MenuFvwmRoot  "Root Menu"             Title
    +                       "&0. XDG Menu"          Popup xdg_menu
    
    read /var/cache/xdg-menu/fvwm2/fvwm2rc
    
### BlackBox

####  使用 xdg_menu
    
    $ xdg_menu --format blackbox  --root-menu /etc/xdg/menus/arch-applications.menu >my-menu
    
修改你的菜单文件以使其包含创建的菜单 

例如添加: 
    
    [include] (my-menu)
    
####  使用 update-menus

  * 在 /etc/update-menus.conf 取消 blackbox 的注释
  * 使用root用户运行 update-menus
  * 更改你的菜单文件以使其包含创建的菜单

例如添加: 
    
    [include] (/var/cache/xdg-menu/blackbox/boxrc)
    
##  另请参见

  * [Sawfish#Menus](</wzh/index.php?title=Sawfish&action=edit&redlink=1> "Sawfish（页面不存在）")
  * <https://github.com/gapan/xdgmenumaker>
