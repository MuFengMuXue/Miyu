[![](../File:User-trash-full.svg.png)](<../File:User-trash-full.svg.png>)**本文已被弃用。**

**本文所述教程或工具由于已经过时而被弃用，请使用其他替代方案：** [Thunderbird](<../zh-cn/Thunderbird.html> "Thunderbird") 等，参见[应用程序列表/互联网#Email 客户端](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#Email_%E5%AE%A2%E6%88%B7%E7%AB%AF> "应用程序列表/互联网")。 (在[Talk:NBSMTP](<../zh-cn/Talk:NBSMTP.html>)讨论)

来自 nbSMTP manpage： 

    nbSMTP is a lightweight SMTP client. It simply takes a message from STDIN and sends it to a relayhost. A relayhost is meant to be a full SMTP server and it will really send the message.

##  安装

安装 [nbsmtp](<https://aur.archlinux.org/packages/nbsmtp/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 包。 

##  转发到 Gmail 邮件服务器

要配置 nbSMTP，您将必须编辑其配置文件（`~/.nbsmtprc`) 并输入您的帐户设置： 
    
    ~/.nbsmtprc
    
    relayhost=smtp.gmail.com
    port=587
    use_starttls=True
    fromaddr=myusername@gmail.com
    auth_user=myusername@gmail.com
    auth_pass=myultrasecretpassword

请谨慎此文件的权限，建议运行以下命令： 
    
    chmod 600 ~/.nbsmtprc
    
要测试配置，请创建一个文件（`testemail`）： 
    
    testemail
    
    To: myusername@gmail.com
    From: myusername@gmail.com
    Subject: nbsmtp test
    hello email world

然后运行： 
    
    /usr/bin/nbsmtp < testemail
    