[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Add more useful information. (在 [Talk:Qv2ray](<../zh-cn/Talk:Qv2ray.html>) 中讨论)

相关文章

  * [V2Ray](<../zh-cn/V2Ray.html> "V2Ray")

[Qv2ray](<https://qv2ray.net/lang/zh>) 是一个使用 [Qt](<../zh-cn/Qt.html> "Qt") 编写的跨平台的 [V2Ray](<../zh-cn/V2Ray.html> "V2Ray") 图形前端，可以在图形化界面中方便地配置代理。 

##  安装

**注意：** Shadowsocks-NET/Qv2ray 不与 Qv2ray/Qv2ray 的插件、配置文件兼容 [[1]](<https://github.com/Shadowsocks-NET/Qv2ray#compatibility>)。

###  Qv2ray/Qv2ray

[Qv2ray/Qv2ray](<https://github.com/Qv2ray/Qv2ray>) 是 Qv2ray 的原始版本。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [qv2ray](<https://aur.archlinux.org/packages/qv2ray/>)AUR 软件包。对于开发版本，安装 [qv2ray-dev-git](<https://aur.archlinux.org/packages/qv2ray-dev-git/>)AUR 软件包，也可以在 [archlinuxcn](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Archlinuxcn") 储存库中找到。 

**注意：** 此版本已[停止维护](<https://qv2ray.net/Deprecation-Notice>)。

###  Shadowsocks-NET/Qv2ray

[Shadowsocks-NET/Qv2ray](<https://github.com/Shadowsocks-NET/Qv2ray>) 是新的原创 Qv2ray 项目。 

安装 [qv2ray-v3](<https://aur.archlinux.org/packages/qv2ray-v3/>)AUR 软件包。对于开发版本，安装 [qv2ray-git](<https://aur.archlinux.org/packages/qv2ray-git/>)AUR 软件包。对于[预构建二进制每日版本](<https://github.com/Shadowsocks-NET/QvStaticBuild>)，安装 [qv2ray-static-nightly-bin](<https://aur.archlinux.org/packages/qv2ray-static-nightly-bin/>)AUR 软件包。 

**注意：** 此版本尚处于开发阶段，存在缺陷如[显示连接后无法上网](<https://github.com/Shadowsocks-NET/Qv2ray/issues/29>) 和功能缺失如[无多语言支持](<https://github.com/Shadowsocks-NET/Qv2ray/issues/15>)。

###  插件

参见[使用插件](<https://qv2ray.net/lang/zh/plugins/usage.html>)。 

**注意：** Qv2ray 本身并不包含 V2Ray 核心。如果不使用插件，就需要手动[安装 V2Ray](<../zh-cn/V2Ray.html#%E5%AE%89%E8%A3%85> "V2Ray")，否则 Qv2ray 将无法使用。若使用插件，Qv2ray 可以在不依赖 V2Ray 核心的情况下运行 [[2]](<https://qv2ray.net/lang/zh/plugins/usage.html#%E4%BB%80%E4%B9%88%E6%98%AF%E6%8F%92%E4%BB%B6>).

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Use [Template:App](<../zh-cn/Template:%E5%BA%94%E7%94%A8.html> "Template:App").（在[Talk:Qv2ray](<../zh-cn/Talk:Qv2ray.html>)讨论）

对于 Qv2ray/Qv2ray： 

  * 安装 [qv2ray-plugin-ssr-git](<https://aur.archlinux.org/packages/qv2ray-plugin-ssr-git/>)AUR 以支持 ShadowsocksR 协议。
  * 安装 [qv2ray-plugin-trojan](<https://aur.archlinux.org/packages/qv2ray-plugin-trojan/>)AUR 以支持 Trojan-GFW 协议。
  * 安装 [qv2ray-plugin-trojan-go-git](<https://aur.archlinux.org/packages/qv2ray-plugin-trojan-go-git/>)AUR 以支持 Trojan-Go 协议。
  * 安装 [qv2ray-plugin-naiveproxy-git](<https://aur.archlinux.org/packages/qv2ray-plugin-naiveproxy-git/>)AUR 以支持 NaiveProxy 协议。
  * 安装 [qv2ray-plugin-command](<https://aur.archlinux.org/packages/qv2ray-plugin-command/>)AUR 以进行自动化。

上述插件也可以在 _archlinuxcn_ 储存库找到，可以安装 _qv2ray-plugin_ 组以获得上述所有插件。 

**注意：**[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中尚没有[适用于 Shadowsocks-NET/Qv2ray 的插件](<https://github.com/Shadowsocks-NET/Qv2ray#plugins-at-a-glance>)的包。

##  配置

见 [Qv2ray 手册](<https://qv2ray.net/lang/zh/manual/>)。 

打开 Qv2ray 中的 _首选项_ 进行配置。Qv2ray 配置文件位于 `~/.config/qv2ray/` 目录。 

**注意：** 若要从 Qv2ray/Qv2ray 迁移到 Shadowsocks-NET/Qv2ray，请删除旧配置并重新进行配置 [[3]](<https://github.com/Shadowsocks-NET/Qv2ray/issues/6>)。

##  使用

见[导入节点到 Qv2ray](<https://qv2ray.net/lang/zh/getting-started/step3.html>) 和[配置浏览器/软件以使用 Qv2ray](<https://qv2ray.net/lang/zh/getting-started/step4.html>)。也可以看看 [Shadowsocks#为其它程序配置代理](<../zh-cn/Shadowsocks.html#%E4%B8%BA%E5%85%B6%E5%AE%83%E7%A8%8B%E5%BA%8F%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86> "Shadowsocks")。 

##  疑难解答

见[常见问题](<https://qv2ray.net/lang/zh/faq>)。 

##  参阅

  * [Qv2ray 官方网站 & 文档](<https://qv2ray.net/lang/zh>)
