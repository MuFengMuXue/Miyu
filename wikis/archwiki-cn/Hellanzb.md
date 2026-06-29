[![](../File:User-trash-full.svg.png)](<../File:User-trash-full.svg.png>)**本文已被弃用。**

**本文所述教程或工具由于已经过时而被弃用，请使用其他替代方案：** 参见[应用程序列表/互联网#新闻组新闻阅读器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E6%96%B0%E9%97%BB%E7%BB%84%E6%96%B0%E9%97%BB%E9%98%85%E8%AF%BB%E5%99%A8> "应用程序列表/互联网")。 (在[Talk:Hellanzb](<../zh-cn/Talk:Hellanzb.html>)讨论)

[Hellanzb](<https://github.com/pjenvey/hellanzb>) 是用 Python 编写的基于控制台的 Usenet 二进制下载器。它可以在守护程序模式下运行，并且可以使用多个 GUI 或 PHP 前端。 

**注意：** 尽管开发人员和测试团队认为最新版本（0.13）稳定，但 hellanzb 不再处于活动开发中。

##  主要功能

  * 自动下载放置在用户指定的监视目录中的 nzb 文件。
  * Par1/2 验证和修复损坏的文件。
  * 取消完全下载。
  * 下载完成后，删除不需要的文件。

##  安装

Hellanzb 在 [AUR](<../zh-cn/AUR_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "AUR \(简体中文\)") 软件包 [hellanzb-git](<https://aur.archlinux.org/packages/hellanzb-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 中可用。 

##  配置

Hellanzb 可以在两种模式下运行： 

  * 从 CLI
  * 作为守护程序

### hellanzb.conf

用户 `.config` 目录中必须存在一个名为 `hellanzb.conf` 的配置文件，hellanzb 才能正常运行。提供了一个示例配置文件。 
    
    mkdir -p ~/.config
    cp /etc/hellanzb.conf.sample ~/.config/hellanzb.conf
    
###  /etc/conf.d/hellanzb

在守护程序模式下运行时，需要修改 `/etc/conf.d/hellanzb` 文件以配置将要运行 hellanzb 的用户 
    
    HELLANZB_USER="username"
    HELLANZB_CONF="/home/${HELLANZB_USER}/.config/hellanzb.conf"
    