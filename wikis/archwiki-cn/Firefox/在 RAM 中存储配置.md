**翻译状态：**

  * 本文（或部分内容）译自 [Firefox/Profile on RAM](<https://wiki.archlinux.org/title/Firefox/Profile_on_RAM> "arch:Firefox/Profile on RAM")，最近一次同步于 2025-01-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Firefox/Profile_on_RAM?diff=0&oldid=824212>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Firefox_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Profile_on_RAM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

假设有多余的内存可用，将 [Firefox](<../../zh-cn/Firefox.html> "Firefox") 的缓存或完整配置文件放入 RAM 中可以带来显著的优势。若选择部分迁移，不仅其本身会带来优势，还比默认配置响应更快。其优势包括但不限于： 

  * 减少磁盘读写操作；
  * 提高响应速度；
  * 可在 Firefox 中几乎即时地执行许多操作（如快速搜索和历史记录查询）。

这可以使用 [tmpfs](<../../zh-cn/Tmpfs.html> "Tmpfs") 实现。 

由于放入 RAM 中的数据无法在系统关闭后继续保存，如果需要持久化数据（如迁移配置文件时），需要借助脚本在系统关闭前将数据同步回磁盘。而仅迁移缓存快速但覆盖面较小，可以稍微提升用户体验，同时在每次重启时清空 Firefox 缓存。 

**注意：** 缓存存储在与 Firefox 默认配置文件文件夹（`/home/$USER/.mozilla/firefox/`）**不同** 的位置：`/home/$USER/.cache/mozilla/firefox/<profile>`。这与其它浏览器（如 Chromium）的处理方式相似。因此，章节 [#使用工具将配置文件迁移到 RAM](<#%E4%BD%BF%E7%94%A8%E5%B7%A5%E5%85%B7%E5%B0%86%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E8%BF%81%E7%A7%BB%E5%88%B0_RAM>) 和 [#手动将配置文件迁移到 RAM](<#%E6%89%8B%E5%8A%A8%E5%B0%86%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E8%BF%81%E7%A7%BB%E5%88%B0_RAM>) **不涉及** 缓存的迁移和同步，而仅限于配置文件的调整。有关更多细节，请参阅 [Profile-sync-daemon](<../../zh-cn/Profile-sync-daemon.html> "Profile-sync-daemon") 的第一条“注意”。[Anything-sync-daemon](<../../zh-cn/Anything-sync-daemon.html> "Anything-sync-daemon") 可以用于实现与选项 2 类似的缓存文件夹操作。

##  仅将缓存迁移到 RAM

参见 [Firefox/微调#关闭磁盘缓存](<../../zh-cn/Firefox/%E5%BE%AE%E8%B0%83.html#%E5%85%B3%E9%97%AD%E7%A3%81%E7%9B%98%E7%BC%93%E5%AD%98> "Firefox/微调")。 

##  使用工具将配置文件迁移到 RAM

将浏览器配置文件重新定位到 [tmpfs](<../../zh-cn/Tmpfs.html> "Tmpfs")，可全局提升浏览器的响应速度，并减少驱动器的 I/O 操作，其中[固态硬盘受益最大](<../../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html#%E6%98%BE%E7%A4%BA%E7%A3%81%E7%9B%98%E5%86%99%E4%BF%A1%E6%81%AF> "性能优化")。 

使用一个主动管理脚本可以实现最大程度的可靠性和易用性。在 AUR 中有多个可用的脚本。 

### Profile-sync-daemon

参见 [Profile-sync-daemon](<../../zh-cn/Profile-sync-daemon.html> "Profile-sync-daemon") 页面以获取更多信息。 

### firefox-sync

[firefox-sync](<https://aur.archlinux.org/packages/firefox-sync/>)AUR 对于仅使用单个配置文件的用户来说已经足够，它使用类似于下文 [#脚本](<#%E8%84%9A%E6%9C%AC>)中的脚本和 systemd 服务。 

根据 [#开始之前](<#%E5%BC%80%E5%A7%8B%E4%B9%8B%E5%89%8D>)中的建议，确认并备份当前的 Firefox 配置文件。 

使用[附加配置片段](<../../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")将配置文件作为参数传递： `-p _profile_id_.default`。 

**警告：** 该操作可能会删除配置文件，请备份以准备在启动服务后立即从备份中恢复。

然后[启动/启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `firefox-sync.service` [用户单元](<../../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

##  手动将配置文件迁移到 RAM

###  开始之前

请务必在可能影响 Firefox 配置文件之前将其备份，以便快速恢复。首先，通过访问 `about:profiles` 页面，查看正在使用的配置文件目录。使用 `tar` 进行备份（替换 **`xyz.default`** 为正在使用的配置文件目录）： 
    
    $ tar zcvfp ~/firefox_profile_backup.tar.gz ~/.mozilla/firefox/**xyz.default**
    
###  脚本

此脚本改编自 [verot.net 的 Speed up Firefox with tmpfs](<https://www.verot.net/firefox_tmpfs.htm>)。 

脚本首先会将 Firefox 的配置文件移动到一个新的静态位置，在 `/dev/shm` 中创建一个子目录，在原位置使用软链接指向它，然后将配置文件的内容填充到该目录中。和之前一样，并且直到本文结束，替换所有粗体 **`xyz.default`** 字符串为 Firefox 配置文件目录。唯一必须更改的值仍然是 **`xyz.default`** 。 

在安装 [rsync](<../../zh-cn/Rsync.html> "Rsync") 后，[创建](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")： 
    
    ~/.local/bin/firefox-sync.sh
    
    #!/bin/sh
    
    static=_static-$1_
    link=_$1_
    volatile=_/dev/shm/firefox-$1-$USER_
    
    IFS=
    set -efu
    
    cd ~/.mozilla/firefox
    
    if [ ! -r $volatile ]; then
    	mkdir -m0700 $volatile
    fi
    
    if [ "$(readlink $link)" != "$volatile" ]; then
    	mv $link $static
    	ln -s $volatile $link
    fi
    
    if [ -e $link/.unpacked ]; then
    	rsync -av --delete --exclude .unpacked ./$link/ ./$static/
    else
    	rsync -av ./$static/ ./$link/
    	touch $link/.unpacked
    fi

将脚本设为[可执行](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")，然后运行以下命令以关闭 Firefox 并测试脚本： 
    
    $ killall firefox firefox-bin
    $ ls ~/.mozilla/firefox/
    $ ~/.local/bin/firefox-sync.sh **xyz.default**
    
再次运行 Firefox 并评估结果。脚本第二次运行时，会将 RAM 配置文件复制回磁盘来保留它。 

###  自动化

鉴于忘记同步配置文件可导致的灾难性后果，自动化此过程会是一个合乎逻辑的选择。 

#### systemd

[创建](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")以下脚本： 
    
    ~/.config/systemd/user/firefox-profile@.service
    
    [Unit]
    Description=Firefox profile memory cache
    
    [Install]
    WantedBy=default.target
    
    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=%h/.local/bin/firefox-sync.sh %i
    ExecStop=%h/.local/bin/firefox-sync.sh %i

然后，运行 [daemon-reload](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload") 并[启用/启动](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `firefox-profile@**xyz.default**.service` [用户单元](<../../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

####  cron 定时任务

使用 `crontab` 操作用户的 [cron](<../../zh-cn/Cron.html> "Cron") 表： 
    
    $ crontab -e
    
添加一行每隔 30 分钟运行脚本： 
    
    */30 * * * * ~/.local/bin/firefox-sync.sh **xyz.default**
    
或者添加以下内容，每隔 2 小时运行一次： 
    
    0 */2 * * * ~/.local/bin/firefox-sync.sh **xyz.default**
    
####  登录/注销时进行同步

若使用 [bash](<../../zh-cn/Bash.html> "Bash")，在登录/注销文件中运行 [#脚本](<#%E8%84%9A%E6%9C%AC>)： 
    
    $ echo 'bash -c "~/.local/bin/firefox-sync.sh **xyz.default** > /dev/null &"' | tee -a ~/.bash_logout ~/.bash_login
    
**注意：** 如果同时存在 `~/.bash_profile` 和 `~/.bash_login` 并且两者都可读，bash 只会读取前者，因此可能需要使用 `~/.bash_profile` 替代 `~/.bash_login`。

对于 [zsh](<../../zh-cn/Zsh.html> "Zsh")，使用 `~/.zlogin` 和 `~/.zlogout` 代替： 
    
    $ echo 'bash -c "~/.local/bin/firefox-sync.sh **xyz.default** > /dev/null &"' | tee -a ~/.zlog{in,out}
    
##  参见

  * [tmpfs](<../../zh-cn/Tmpfs.html> "Tmpfs")
