[![](../File:User-trash-full.svg.png)](<../File:User-trash-full.svg.png>)**本文已被弃用。**

**本文所述教程或工具由于已经过时而被弃用，请使用其他替代方案：** 暂无替代方案 (在[Talk:Capi4hylafax](<../zh-cn/Talk:Capi4hylafax.html>)讨论)

**Capi4hylafax** 是一个用于 [Hylafax](</wzh/index.php?title=Hylafax&action=edit&redlink=1> "Hylafax（页面不存在）") 的 CAPI 插件，用于在 CAPI 2.0 设备上启用 ISDN 传真。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [capi4hylafax](<https://archlinux.org/packages/?name=capi4hylafax>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 包。 

##  配置

以 root 用户身份运行 _faxsetup_ 以根据需要调整 hylafax。根据需要进一步调整 `/var/spool/hylafax/etc/config/config.faxCAPI`。 

**警告：** 甚至不要尝试为 CAPI 2.0 设备运行 _faxaddmodem_ ！

_c2faxaddmodem_ 是配置 ISDN 卡的不错的工具。 

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `hylafax.service` 和 `c2faxrecv.service`。 

确保您的设备对 `uucp` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")具有正确的权限。 

将以下行添加到 `/var/spool/hylafax/etc/config`： 
    
    SendFaxCmd: /usr/bin/c2faxsend
    
**注意：** 如果您需要多个 ISDN 控制器，请阅读 capi4hylafax 手册。

有关提示和技巧，请参见 [Hylafax](</wzh/index.php?title=Hylafax&action=edit&redlink=1> "Hylafax（页面不存在）")。 
