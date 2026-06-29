[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Drupal](<../zh-cn/Talk:Drupal.html>)讨论)

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:Drupal#](<../zh-cn/Talk:Drupal.html>) 中讨论）

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 许多内容为空（在 [Talk:Drupal#](<../zh-cn/Talk:Drupal.html>) 中讨论）

_“Drupal 是一个自由开源的内容管理系统，以PHP语言写成。在网页编程界中，Drupal经常被视为一套内容管理框架，而不单纯作为一般意义上的内容系统。”_ \--- 摘自[维基百科](<https://zh.wikipedia.org/wiki/Drupal>)

这篇文章主要描述了怎样安装Drupal以及配置[Apache](</wzh/index.php?title=Apache&action=edit&redlink=1> "Apache（页面不存在）")，[MySQL](<../zh-cn/MySQL.html> "MySQL")和[PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")，[PHP](<../zh-cn/PHP.html> "PHP")，[Postfix](<../zh-cn/Postfix.html> "Postfix")，以便使它们构建一套完整的，可以正常工作的web服务系统。这篇文章假定你有一定的[LAMP](<../zh-cn/Category:%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8.html> "LAMP")（Apache，MySQL，PHP）和[LAPP](</wzh/index.php?title=LAPP&action=edit&redlink=1> "LAPP（页面不存在）")（Apache，PostgreSQL，PHP）的安装经验。 

#  安装

##  安装Drupal

###  从源安装

  1. [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [drupal](<https://archlinux.org/packages/?name=drupal>)包。
  2. 使用自己喜欢的编辑器，编辑文件`/etc/php/php.ini`
         
         # vim /etc/php/php.ini

找到下面一行："`;extension=json.so`"，如果有注释就去掉注释（第一个字符“;”），如果没有这行就在这个文件的`[PHP]`区块添加。  
对于Drupal 7来说，还需要启用数据库的PDO扩展，例如MySQL， `extension=pdo_mysql.so`。
  3. 打开文件`/etc/httpd/conf/httpd.conf`
         
         # vim /etc/httpd/conf/httpd.conf

找到以"`<Directory "/srv/http">`"（根据自己的Drupal安装目录而定）开始的部分，找到"`AllowOverride None`"，替换为"`AllowOverride All`"，这样可以启用Drupal的简洁连接（clear URL's）。
  4. 重启Apache 
         
         /etc/rc.d/httpd restart

###  手工安装

##  安装GD库

##  安装Postfix

#  提示和技巧

##  使用Cron配置任务计划

##  兼容Xampp

##  启用“上传进度条”

#  疑难排解

##  浏览器显示PHP代码

##  不能进入安装界面

##  安装时发生HTTP 500错误
