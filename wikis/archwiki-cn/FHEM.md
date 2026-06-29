**翻译状态：**

  * 本文（或部分内容）译自 [FHEM](<https://wiki.archlinux.org/title/FHEM> "arch:FHEM")，最近一次同步于 2020-07-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/FHEM?diff=0&oldid=625481>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/FHEM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[FHEM](<https://fhem.de>) (TM) 是在 GPL 下分发的 Perl 服务器，用于使房屋自动化。它可以用于自动执行家庭中的一些常见任务，例如开关灯/百叶窗/暖气等，并记录温度/湿度/功耗等。 

##  安装

安装 [fhem](<https://aur.archlinux.org/packages/fhem/>)AUR 软件包。 

##  配置

从版本 5.7 开始，FHEM 软件包对其文件使用不同的目录布局： 

  * `/usr/share/fhem` Perl 模块和静态内容
  * `/var/lib/fhem` 日志和状态文件，动态内容
  * `/etc/fhem.cfg` 主配置文件

如果您有旧版配置，请通过将这些行放入 `/etc/fhem.cfg` 来调整路径 

如果您想从 Web 前端编辑配置，请确保 `fhem` 用户对 `/etc/fhem.cfg` 具有写权限。 
    
    /etc/fhem.cfg
    
    attr global logfile /var/lib/fhem/fhem-%Y-%m.log
    attr global modpath /usr/share/fhem
    attr global statefile /var/lib/fhem/fhem.save
    
    [...]
    
    define Logfile FileLog /var/lib/fhem/fhem-%Y-%m.log fakelog
    
    define autocreate autocreate
    attr autocreate filelog /var/lib/fhem/%NAME-%Y.log
    
    define eventTypes eventTypes /var/lib/fhem/eventTypes.txt
    
请访问 [FHEM 参考文档](<https://fhem.de/commandref.html>)以获取更多信息。 

##  启动

只需[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `fhem.service`。 
