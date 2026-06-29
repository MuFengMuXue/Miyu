**翻译状态：**

  * 本文（或部分内容）译自 [Deepin-wine](<https://wiki.archlinux.org/title/Deepin-wine> "arch:Deepin-wine")，最近一次同步于 2022-12-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Deepin-wine?diff=0&oldid=745777>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Deepin-wine_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 需要添加更多关于使用 deepin-wine 和 [与Wine相比的特殊功能](</wzh/index.php?title=Talk:Deepin-wine&action=edit&redlink=1> "Talk:Deepin-wine（页面不存在）"). (在 [Talk:Deepin-wine](<../zh-cn/Talk:Deepin-wine.html>) 中讨论)

相关文章

  * [Wine](<../zh-cn/Wine.html> "Wine")
  * [微信](<../zh-cn/%E5%BE%AE%E4%BF%A1.html> "微信")
  * [腾讯QQ](<../zh-cn/%E8%85%BE%E8%AE%AF_QQ.html> "腾讯QQ")

Deepin-wine是由[武汉深之度科技有限公司](<https://www.deepin.org/zh/aboutus/>)开发的基于[Wine](<../zh-cn/Wine.html> "Wine")的兼容层, 它附属于 [deepin](<https://www.deepin.org/zh/aboutus/>) Linux. 

Deepin-wine 的应用程序几乎是开箱即用的，漏洞（相较于wine）会更少。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")以下包之一: 

  * **Deepin-wine5** — Deepin-wine5.

     <https://www.deepin.org> || [deepin-wine5](<https://aur.archlinux.org/packages/deepin-wine5/>)AUR

  * **Deepin-wine5 stable** — Deepin-wine5 stable.

     <https://www.deepin.org> || [deepin-wine5-stable](<https://aur.archlinux.org/packages/deepin-wine5-stable/>)AUR

  * **Deepin-wine6 stable** — Deepin-wine6 stable.

     <https://www.deepin.org> || [deepin-wine6-stable](<https://aur.archlinux.org/packages/deepin-wine6-stable/>)AUR

  * **Deepin-wine8 stable** — Deepin-wine8 stable.

     <https://www.deepin.org> || [deepin-wine8-stable](<https://aur.archlinux.org/packages/deepin-wine8-stable/>)AUR

##  Deepin-wine应用程序列表

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 需要安装的额外包. (在 [Talk:Deepin-wine](<../zh-cn/Talk:Deepin-wine.html>) 中讨论)

  * **Deepin-wine DingTalk** — DingTalk Client on Deepin-wine.

     <https://www.dingtalk.com/> || [deepin.com.dingtalk.com](<https://aur.archlinux.org/packages/deepin.com.dingtalk.com/>)AUR

  * **[Deepin-wine QQ Light](<../zh-cn/Tencent_QQ.html#Deepin_QQ/TIM> "Tencent QQ")** — [QQ Light](<../zh-cn/QQ_Light.html> "QQ Light") on Deepin-wine.

     <https://im.qq.com/> || [deepin.com.qq.im.light](<https://aur.archlinux.org/packages/deepin.com.qq.im.light/>)AUR

  * **[Deepin-wine TIM](<../zh-cn/Tencent_QQ.html#Deepin_QQ/TIM> "Tencent QQ")** — [TIM](<../zh-cn/%E8%85%BE%E8%AE%AF_QQ.html> "TIM") on Deepin-wine.

     <https://office.qq.com/>, <https://tim.qq.com/> || [com.qq.office.deepin](<https://aur.archlinux.org/packages/com.qq.office.deepin/>)AUR, [deepin-wine-tim](<https://aur.archlinux.org/packages/deepin-wine-tim/>)AUR, or from Spark Store: [com.qq.tim.spark](<https://aur.archlinux.org/packages/com.qq.tim.spark/>)AUR

  * **[Deepin-wine WeChat](<../zh-cn/%E5%BE%AE%E4%BF%A1.html#Deepin-wine_WeChat> "WeChat")** — [WeChat](<../zh-cn/%E5%BE%AE%E4%BF%A1.html> "WeChat") on Deepin-wine.

     <https://pc.weixin.qq.com/> || [com.qq.weixin.deepin](<https://aur.archlinux.org/packages/com.qq.weixin.deepin/>)AUR, or from Spark Store: [com.qq.weixin.spark](<https://aur.archlinux.org/packages/com.qq.weixin.spark/>)AUR

  * **[Deepin-wine Weixin Work](<../zh-cn/%E5%BE%AE%E4%BF%A1.html#Deepin-wine_WeChat> "WeChat")** — [Weixin Work](</wzh/index.php?title=Weixin_Work&action=edit&redlink=1> "Weixin Work（页面不存在）") on Deepin-wine.

     <https://work.weixin.qq.com/> || [com.qq.weixin.work.deepin](<https://aur.archlinux.org/packages/com.qq.weixin.work.deepin/>)AUR

##  故障排除

###  Deepin-wine应用程序启动失败

在不基于[GNOME](<../zh-cn/GNOME.html> "GNOME")的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")中，例如[KDE](<../zh-cn/KDE.html> "KDE")，Deepin-wine应用程序将不会启动。 

要想解决这个问题，你需要安装 [xsettingsd](<https://archlinux.org/packages/?name=xsettingsd>)包, 然后设置 `/usr/bin/xsettingsd` 到自启动项 , 参考[自动启动#桌面环境](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83> "自动启动"). 

重新登录后即可解决。 

##  参考

  * [deepin Wiki](<https://wiki.deepin.org/zh/%E5%BE%85%E5%88%86%E7%B1%BB/Deepin-wine>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ]
  * [此项目用于将 Deepin-wine 移植到 Ubuntu/Debian](<https://github.com/wszqkzqk/deepin-wine-ubuntu>)
