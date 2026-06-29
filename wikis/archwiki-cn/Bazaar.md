**翻译状态：**

  * 本文（或部分内容）译自 [Bazaar](<https://wiki.archlinux.org/title/Bazaar> "arch:Bazaar")，最近一次同步于 2020-05-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Bazaar?diff=0&oldid=614273>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Bazaar_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Bazaar](<https://bazaar.canonical.com/>) 是一个版本控制系统，可以帮助您跟踪一段时间内的项目历史记录并与他人轻松地进行协作。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [bzr](<https://aur.archlinux.org/packages/bzr/>)AUR 包。 

##  使用

请参阅 [bzr(1)](<https://linux.die.net/man/1/bzr>)。 

###  使用 xinetd 设置 Bazaar 服务器

根据需要添加 `_bzr-usr_` [用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户")。 

创建一个存储库： 
    
    $ bzr init /home/bzr/repo.bzr
    $ chown -R _bzr_usr_ /home/bzr/repo.bzr
    
添加 _xinetd_ 的配置： 
    
    service bzr
    {
    	flags			= REUSE
    	socket_type		= stream
    	wait			= no
    	user			= _bzr_usr_
    	server			= /usr/bin/bzr
    	server_args		= serve --inet --directory=/home/bzr/repo.bzr
    	env			= HOME=/home/bzr
    	log_on_failure		+= USERID
    	disable			= no
    	cps			= 50 10
    	instances		= 60
    }
