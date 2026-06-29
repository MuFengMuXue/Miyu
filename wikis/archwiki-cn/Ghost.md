[![](../File:User-trash-full.svg.png)](<../File:User-trash-full.svg.png>)**本文已被弃用。**

**本文所述教程或工具由于已经过时而被弃用，请使用其他替代方案：** [Wordpress](<../zh-cn/Wordpress.html> "Wordpress") 等，参见[应用程序列表/互联网#博客引擎](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E5%8D%9A%E5%AE%A2%E5%BC%95%E6%93%8E> "应用程序列表/互联网") (在[Talk:Ghost](<../zh-cn/Talk:Ghost.html>)讨论)

[Ghost](<https://ghost.org/>) 是一个免费的开源博客平台，使用 JavaScript 编写，并根据 MIT 许可证进行分发，旨在简化单个博客作者和在线出版物的在线发布过程。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ghost-web](<https://aur.archlinux.org/packages/ghost-web/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]，并修改 `/etc/webapps/ghost/config.js` 。然后[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `ghost.service` 。 如果对它感到满意，请在系统引导时[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")它以自动启动。 

请访问 <http://127.0.0.1:2368/ghost> 进行最终配置。 
