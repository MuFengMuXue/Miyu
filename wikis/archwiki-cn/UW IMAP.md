相关文章

  * [邮件服务器](<../zh-cn/%E9%82%AE%E4%BB%B6%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "邮件服务器")

**翻译状态：**

  * 本文（或部分内容）译自 [UW IMAP](<https://wiki.archlinux.org/title/UW_IMAP> "arch:UW IMAP")，最近一次同步于 2024-8-5，若英文版本有所[更改](<https://wiki.archlinux.org/title/UW_IMAP?diff=0&oldid=813896>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/UW_IMAP_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自 [Wikipedia](<https://en.wikipedia.org/wiki/UW_IMAP> "wikipedia:UW IMAP")： 

     **UW IMAP** 是 University of Washington 开发的 IMAP 协议的参考服务器实现。

虽然多年来它一直没有得到积极开发，但作为基本的 IMAPS 服务器，它仍然可运行良好。(有关其他 IMAP 服务器，请参阅[邮件服务器#软件](<../zh-cn/%E9%82%AE%E4%BB%B6%E6%9C%8D%E5%8A%A1%E5%99%A8.html#%E8%BD%AF%E4%BB%B6> "邮件服务器")）。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [c-client](<https://aur.archlinux.org/packages/c-client/>)AUR。它不使用配置文件。 

**注意：** _c-client_ 是一个包含 UW IMAP 及其客户端的拆分软件包，你可以根据自己的需要同时或只安装其中一个软件包。

##  配置

虽然它最初是与 [inetd](<https://en.wikipedia.org/wiki/inetd> "wikipedia:inetd") 一起使用的，但在现代 Arch 系统上，更好的解决方案是使用 systemd socket 文件： 
    
    /etc/systemd/system/imaps.socket
    
    [Unit]
    Description=IMAP Server Activation Socket
    Documentation=https://www.washington.edu/imap/
    
    [Socket]
    ListenStream=0.0.0.0:993
    Accept=true
    
    [Install]
    WantedBy=sockets.target
    
此外，还需要创建相应的 .service 文件： 
    
    /etc/systemd/system/imaps@.service
    
    [Unit]
    Description=IMAP Server
    
    [Service]
    ExecStart=-/usr/bin/imapd
    StandardInput=socket
    
UW-IMAPD 使用 [PAM](<../zh-cn/PAM.html> "PAM")，因此还需要创建一个 PAM 授权文件。本例将使用标准系统密码进行身份验证： 
    
    /etc/pam.d/imap
    
    auth		required	pam_unix.so
    account		required	pam_unix.so
    session		required	pam_unix.so
    
[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `imaps.socket` 并进行测试。 

## SSL

如果尚未创建通用 SSL 证书和密钥，则会在 `/etc/ssl/certs/imapd.pem` 中创建。可以[替换](</wzh/index.php?title=Transport_Layer_Security&action=edit&redlink=1> "Transport Layer Security（页面不存在）")特定服务器的签名证书。 

**警告：** 自签名证书（如自动生成的证书）容易受到 [MITM 攻击](<https://en.wikipedia.org/wiki/%E4%B8%AD%E9%97%B4%E4%BA%BA%E6%94%BB%E5%87%BB> "wikipedia:中间人攻击")，请确保在生产服务器上使用签名证书。
