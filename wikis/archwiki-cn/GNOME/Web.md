**翻译状态：**

  * 本文（或部分内容）译自 [GNOME/Web](<https://wiki.archlinux.org/title/GNOME/Web> "arch:GNOME/Web")，最近一次同步于 2022-08-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/GNOME/Web?diff=0&oldid=735113>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GNOME_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Web_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Web是[GNOME](<../../zh-cn/GNOME.html> "GNOME")的默认网络浏览器。Web 提供了一个简单而简约的界面来访问互联网。虽然它主要是为 GNOME 开发的，但 Web 在其他[桌面环境](<../../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")中也能正常工作。 

**注意：** 在3.4版本之前，Web 被称为 [Epiphany](<https://wiki.gnome.org/Apps/Web>)。该应用程序被赋予新的描述性名称，每种支持的语言都有一个。 _Epiphany_ 这个名字仍然用在许多地方，如可执行文件名、一些软件包名、一些桌面条目和一些 GSettings 纲要。

##  安装

Web 能以 [epiphany](<https://archlinux.org/packages/?name=epiphany>)包 包[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。如果您想保存登录密码，请安装[gnome-keyring](<https://archlinux.org/packages/?name=gnome-keyring>)包。 

##  配置

###  广告屏蔽

它是默认启用的，您可以通过解除勾选在 _首选项_ 中的 _阻止广告_ 禁用它。EasyList 是默认的阻止列表。所有列表都会定期刷新。 

要获取当前启用的过滤器列表： 
    
    $ gsettings get org.gnome.Epiphany content-filters
    
可以按照 <https://gitlab.com/eyeo/filterlists/contentblockerlists> 中的示例使用 JSON 格式的资源修改过滤器： 
    
    $ gsettings set org.gnome.Epiphany content-filters "['https://gitlab.com/eyeo/filterlists/contentblockerlists/-/raw/master/easylist_min_content_blocker.json', 'https://gitlab.com/eyeo/filterlists/contentblockerlists/-/raw/master/easylist+easylistchina-minified.json']"
    
**提示：**[dconf-editor](<https://archlinux.org/packages/?name=dconf-editor>)包 可用作 GUI 替代品。

###  跟踪预防

Web 包括“智能跟踪器预防”，可以在“首选项”中启用。 

###  火狐同步

Web 允许使用[火狐同步](<https://www.mozilla.org/en-US/firefox/sync/>)来同步书签、历史记录、密码和打开的标签。它可以在“导入和导出”下拉菜单中进行配置。 

###  Web 应用

Web 可以从网站创建 Web 应用程序并将它们添加到桌面菜单。要配置和删除它们，请在地址栏中输入 `about:applications`。 

###  自定义样式表

Web 支持自定义样式表，您可以在**首选项** 中的**外观** 下启用。 

使用下面的示例根据 Adwaita 深色变体设置新的标签页布局和颜色： 
    
    ~/.config/epiphany/user-stylesheet.css
    
    #overview {
      background-color: #2E3436 !important;
      max-width: 100% !important;
      max-height: 100% !important;
      position: fixed !important;
    }
    
    #overview .overview-title {
      color: white !important;
    }
    
###  字体

Web 不会检查 GNOME 字体设置，但会检查 [Font configuration](<../../zh-cn/Font_configuration.html> "Font configuration")。 

###  视频

有关所需的插件安装，请参阅 [GStreamer](<../../zh-cn/GStreamer.html> "GStreamer")。 

要启用硬件加速视频解码，请参阅 [GStreamer#Hardware video acceleration](<../../zh-cn/GStreamer.html#Hardware_video_acceleration> "GStreamer") 和 [#Hardware 加速合成](<#Hardware_%E5%8A%A0%E9%80%9F%E5%90%88%E6%88%90>)[[损坏的链接](<../../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]。 

###  硬件加速合成

默认情况下，仅在需要（按需）显示 3D 变换时才使用硬件加速合成。 

强制启用硬件加速合成： 
    
    $ gsettings set org.gnome.Epiphany.web:/ hardware-acceleration-policy 'always'
    
###  代理配置

Web 不尊重 socks_proxy，相反，您可以将 http_proxy 设置为 `socks:// URL` ： 
    
    export http_proxy=socks://127.0.0.1:1080
    
更多信息：[代理服务器#环境变量](<../../zh-cn/Proxy_server.html#Environment_variables> "Proxy server")

##  参见

  * [应用程序/网络 - GNOME Wiki！](<https://wiki.gnome.org/Apps/Web>)
