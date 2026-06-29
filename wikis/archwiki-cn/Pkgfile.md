**翻译状态：**

  * 本文（或部分内容）译自 [Pkgfile](<https://wiki.archlinux.org/title/Pkgfile> "arch:Pkgfile")，最近一次同步于 2025-02-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Pkgfile?diff=0&oldid=804428>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Pkgfile_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

工具 **pkgfile** 是检查[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")中软件包文件的工具。 

**提示：**[pacman](<https://archlinux.org/packages/?name=pacman>)包 [有内置的类似功能](<../zh-cn/Pacman.html#%E6%9F%A5%E8%AF%A2%E4%B8%80%E4%B8%AA%E5%8C%85%E5%90%AB%E5%85%B7%E4%BD%93%E6%96%87%E4%BB%B6%E7%9A%84%E5%8C%85%E5%90%8D> "Pacman")。

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")软件包 [pkgfile](<https://archlinux.org/packages/?name=pkgfile>)包，或者安装开发版本的软件包 [pkgfile-git](<https://aur.archlinux.org/packages/pkgfile-git/>)AUR。 

然后，pkgfile 数据库可以用以下方式同步: 
    
    # pkgfile -u
    
##  使用

查找文件 “makepkg” 属于哪个软件包: 
    
    $ pkgfile makepkg
    
    core/pacman

列出 [archlinux-keyring](<https://archlinux.org/packages/?name=archlinux-keyring>)包 包含的所有文件： 
    
    $ pkgfile -l archlinux-keyring
    
    core/archlinux-keyring usr/
    core/archlinux-keyring usr/share/
    core/archlinux-keyring usr/share/pacman/
    core/archlinux-keyring usr/share/pacman/keyrings/
    core/archlinux-keyring usr/share/pacman/keyrings/archlinux-revoked
    core/archlinux-keyring usr/share/pacman/keyrings/archlinux-trusted
    core/archlinux-keyring usr/share/pacman/keyrings/archlinux.gpg

这个结果与 `pacman -Ql` 类似(参考[pacman#查询包数据库](<../zh-cn/Pacman.html#%E6%9F%A5%E8%AF%A2%E5%8C%85%E6%95%B0%E6%8D%AE%E5%BA%93> "Pacman"))，只不过这个命令查询的是远程仓库中的软件包。 

##  “Command not found” 钩子

详见 [Bash#找不到命令](<../zh-cn/Bash.html#%E6%89%BE%E4%B8%8D%E5%88%B0%E5%91%BD%E4%BB%A4> "Bash")、[Zsh#pkgfile“未找到命令”处理程序](<../zh-cn/Zsh.html#pkgfile%E2%80%9C%E6%9C%AA%E6%89%BE%E5%88%B0%E5%91%BD%E4%BB%A4%E2%80%9D%E5%A4%84%E7%90%86%E7%A8%8B%E5%BA%8F> "Zsh")与 [Fish#"command not found" 事件函数](<../zh-cn/Fish.html#"command_not_found"_%E4%BA%8B%E4%BB%B6%E5%87%BD%E6%95%B0> "Fish")。 

##  自动更新

**pkgfile** 提供了 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务和[定时器](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/Timers")，可以自动同步 pkgfile 数据库。要自动启动，请[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `pkgfile-update.timer`. 

默认情况下 pkgfile 每天更新一次，可以通过[编辑单元文件](<../zh-cn/Systemd.html#Editing_provided_units> "Systemd")进行配置。 
