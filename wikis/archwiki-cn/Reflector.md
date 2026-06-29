[Reflector](<https://xyne.dev/projects/reflector/>) 是一个 Python 脚本；它可以从 [Arch Linux Mirror Status](<https://archlinux.org/mirrors/status/>) 页面获取最新的镜像列表，然后筛选出最新的镜像并按速度排序，最后将结果写入到 `/etc/pacman.d/mirrorlist` 文件。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [reflector](<https://archlinux.org/packages/?name=reflector>)包 软件包。 

##  用法

**警告：**

  * 在下面的例子中，会覆盖 `/etc/pacman.d/mirrorlist` 文件。进行操作前应该进行备份。
  * 在同步或更新 [pacman](<../zh-cn/Pacman.html> "Pacman") 前，需要确保 `/etc/pacman.d/mirrorlist` 文件没有包含你不信任的镜像。

要查看所有可用选项，运行以下命令： 
    
    $ reflector --help
    
###  示例

请见 [reflector(1) § EXAMPLES](<https://man.archlinux.org/man/reflector.1#EXAMPLES>)。覆盖 `/etc/pacman.d/mirrorlist` 的示例需要以 root 用户运行。 

**提示：** 要想包含全球服务器,向 country 选项传递一个空的字符串。举个例子,要想包含法国,德国和全球镜像,应该使用 `--country 'France,Germany,'`。[[1]](<https://bbs.archlinux.org/viewtopic.php?pid=1975404#p1975404>)

##  自动处理

### systemd service

Reflector 附带一个 `reflector.service`。这个服务会用 `/etc/xdg/reflector/reflector.conf` 中指定的参数运行 Reflector。此文件中的默认选项是一个很好的起点和示例。 

例如，从法国和德国的镜像中筛选出 5 个最新的并且支持 HTTPS 的镜像，然后将结果覆写到 `/etc/pacman.d/mirrorlist` 文件内；使用： 
    
    /etc/xdg/reflector/reflector.conf
    
    --save /etc/pacman.d/mirrorlist
    --country France,Germany
    --protocol https
    --latest 5
    
[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `reflector.service` 服务可以在引导时运行 Reflector 脚本。要立即运行，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")该服务。 

**注意：**`reflector.service` 依赖于一个通过 [network-online.target](</wzh/index.php?title=Network-online.target&action=edit&redlink=1> "Network-online.target（页面不存在）") 配置的网络等待服务。

### systemd timer

Reflector 提供一个 [systemd 定时器](<../zh-cn/Systemd_%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd 定时器")（`reflector.timer`），这样每周都会调用 `reflector.service` [服务](<#systemd_service>)。可以[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") `reflector.timer` 来调整时间表。 

首先像[服务](<#systemd_service>)一节那样编辑好配置文件。配置文件更新后，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")或[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `reflector.timer` 定时器。 

要提前刷新镜像列表，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `reflector.service` 服务。 

### pacman hook

[pacman-mirrorlist](<https://archlinux.org/packages/?name=pacman-mirrorlist>)包 不定期更新,只是因为一些地区添加或移除镜像调用 Reflector 与此无关。改为使用基于时间的自动化。如果你完全不想安装 `mirrorlist.pacnew`,在 `pacman.conf` 使用 `NoExtract`。 

##  参考

  * [Arch Linux 论坛上的 Reflector 帖子](<https://bbs.archlinux.org/viewtopic.php?id=115714>)
  * [包含变更日志的上游项目页面](<https://xyne.dev/projects/reflector/>)
