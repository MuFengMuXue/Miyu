**翻译状态：**

  * 本文（或部分内容）译自 [Cron](<https://wiki.archlinux.org/title/Cron> "arch:Cron")，最近一次同步于 2025-02-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Cron?diff=0&oldid=820492>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Cron_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [systemd/Timers](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/Timers")

摘自 [Wikipedia](<https://zh.wikipedia.org/wiki/Cron> "zhwp:Cron"): 

     _cron_ 是一个在 Unix 及类似操作系统上执行计划任务的程序。cron 使用户能够安排工作(命令或shell脚本)在特定时间、日期或间隔定期运行，通常用于系统的自动化维护或者管理。

##  安装

cron 有多个实现程序，但是基础系统默认使用 [systemd 的 Timers](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/Timers")，下面的实现都不被默认安装。参见 Gentoo wiki 的 [cron 指南](<https://www.gentoo.org/doc/en/cron-guide.xml>)，该指南提供了这些实现之间的比较。 

可用的包: 

  * [cronie](<https://archlinux.org/packages/?name=cronie>)包
  * [fcron](<https://archlinux.org/packages/?name=fcron>)包
  * [dcron](<https://aur.archlinux.org/packages/dcron/>)AUR
  * [vixie-cron](<https://aur.archlinux.org/packages/vixie-cron/>)AUR
  * [fcron-dev](<https://aur.archlinux.org/packages/fcron-dev/>)AUR
  * [scron-git](<https://aur.archlinux.org/packages/scron-git/>)AUR

##  配置

###  激活及开机启动

安装后，默认的守护进程不会启动。安装的软件包通常提供了可以用 [systemctl](<../zh-cn/Systemd.html#Using_units> "Systemd") 控制的服务文件。例如 _cronie_ 使用 `cronie.service`。 

`/etc/cron.daily/` 和类似的目录包含当前的任务，启动 cron 服务时会触发所有这类任务。 

**注意：** _cronie_ 提供了 `0anacron` 任务，每小时执行一次，它允许[延迟运行](<#%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E5%A4%84%E7%90%86>)其他某些任务，比如因为未开机而延迟的任务。

###  处理任务中的错误

cron 会记录 _stdout_ 和 _stderr_ 的输出并尝试通过 `sendmail` 命令发送邮件给用户。如果 Cronie 未找到 `/usr/bin/sendmail`，则会禁用邮件通知。要发送邮件到用户的 spool，需要在系统上运行一个 smtp 守护进程，例如 [opensmtpd](<https://archlinux.org/packages/?name=opensmtpd>)包。也可以安装提供 sendmail 命令的软件包，然后配置成通过外部邮件服务器发送邮件。或者使用 `-m` 选项将错误记录到日志并通过定制的脚本进行处理。 

**提示：** 通过 [Postfix/localmail](<../zh-cn/Postfix.html#%E7%B3%BB%E7%BB%9F%E6%9C%AC%E5%9C%B0%E7%94%A8%E6%88%B7%E9%82%AE%E4%BB%B6\(Local_mail\)> "Postfix") 可以发送邮件到本地系统。

  1. [编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") `cronie.service` 服务。
  2. 安装 [esmtp](<https://aur.archlinux.org/packages/esmtp/>)AUR, [mSMTP](</wzh/index.php?title=MSMTP&action=edit&redlink=1> "MSMTP（页面不存在）"), [opensmtpd](<https://archlinux.org/packages/?name=opensmtpd>)包, [sSMTP](</wzh/index.php?title=SSMTP&action=edit&redlink=1> "SSMTP（页面不存在）") 或编写自定义脚本。

####  使用 sSMTP 的例子

sSMTP 是一个仅包含发送功能的 sendmail 模拟器，可以从本地计算机向 smtp 服务器发送邮件。尽管目前已经没有活跃维护者，这个程序依然是发送邮件的最简单方式。不需要运行守护进程，配置可以简单到只需在一个配置文件中编辑三行即可（如果你的主机是受信任的，可以通过你的邮件服务提供商转发未经认证的邮件）。sSMTP 无法收取邮件、展开别名或管理队列。 

安装 [ssmtp](<https://aur.archlinux.org/packages/ssmtp/>)AUR，安装时会创建链接 `/usr/bin/sendmail` 指向 `/usr/bin/ssmtp`。安装后编辑 `/etc/ssmtp/ssmtp.conf` 配置文件。详情请参考 [sSMTP](</wzh/index.php?title=SSMTP&action=edit&redlink=1> "SSMTP（页面不存在）")，到 `/usr/bin/sendmail` 的软链接可以确保 [S-nail](</wzh/index.php?title=S-nail&action=edit&redlink=1> "S-nail（页面不存在）") 等提供 `/usr/bin/mail` 的程序可以无需修改直接使用。 

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `cronie.service` 以确保 cronie 能够检测到新配置的 `/usr/bin/sendmail` 命令。 

####  使用 mSMTP 的例子

安装 [msmtp-mta](<https://archlinux.org/packages/?name=msmtp-mta>)包, 安装时会创建链接 `/usr/bin/sendmail` 指向 `/usr/bin/msmtp`。[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `cronie.service` 以确保 cronie 能够检测到新配置的 `/usr/bin/sendmail` 命令。你必须提供一种方法让 `msmtp` 能够将你的用户名转换成电子邮件地址。 

然后要么在你的 crontab 中添加 `MAILTO` 行： 
    
    MAILTO=your@email.com
    
**要么** 创建 `/etc/msmtprc` 文件，并添加这一行： 
    
    aliases /etc/aliases
    
并创建 `/etc/aliases` 文件： 
    
    your_username: your@email.com
    # 可选：
    default: your@email.com
    
然后[修改](<../zh-cn/Systemd.html#Editing_provided_units> "Systemd") _cronie_ 的配置，将 _cronie_ 守护进程的 `ExecStart` 命令替换为 
    
    ExecStart=/usr/bin/crond -n -m '/usr/bin/msmtp -t'
    
####  使用 esmtp 的例子

安装 [esmtp](<https://aur.archlinux.org/packages/esmtp/>)AUR 和 [procmail](<https://aur.archlinux.org/packages/procmail/>)AUR。 

安装完成后，进行如下配置: 
    
    /etc/esmtprc
    
    identity _myself_ @myisp.com
           hostname mail.myisp.com:25
           username _"myself"_
           password _"secret"_
           starttls enabled
           default
    mda "/usr/bin/procmail -d %T"
    
Procmail 需要 root 权限才能在投递模式下工作，但如果你是以 root 身份运行 cronjobs，就不会有这个问题。 

要测试一切是否正常工作，请创建一个内容为 `"test message"` 的 `message.txt` 文件。 

在同一目录下运行： 
    
    $ sendmail _user_name_ < message.txt 
    
紧接着： 
    
    $ cat /var/spool/mail/_user_name_
    
现在您应该看到测试信息以及发送的时间和日期。 

所有作业的错误输出现在会被重定向到 `/var/spool/mail/_user_name_`。 

由于权限问题，很难创建和发送邮件给root用户（比如 `su -c ""`）。你可以要求 `esmtp` 将 root 的所有邮件转发给普通用户，方法是： 
    
    /etc/esmtprc
    
    force_mda="_user-name_ "

**注意：** 如果上述测试没有成功，您可以尝试在 `~/.esmtprc` 中创建一个具有相同内容的本地配置。 

运行下面的命令以确保它有正确的权限： 
    
    $ chmod 710 ~/.esmtprc
    
然后用 `message.txt` 文件重新运行一遍上面的测试。

####  使用 opensmtpd 的例子

安装 [opensmtpd](<https://archlinux.org/packages/?name=opensmtpd>)包。 

编辑 `/etc/smtpd/smtpd.conf`。下面的配置允许本地投递： 
    
    listen on localhost
    action "local" mbox alias <aliases>
    match for local action "local"
    
您现在可以进行测试。[运行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `smtpd.service`，然后执行： 
    
    $ echo test | sendmail user
    
_user_ 可以用任何 能够处理 mbox 格式的[邮件阅读器](<../zh-cn/Category:Email_clients.html> "Category:Email clients")来检查邮件，或者直接查看 `/var/spool/mail/_user_` 文件。如果一切都符合预期，您可以[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") openmtpd 使其开机运行。 

这种方法的好处是不需要向远程服务器发送本地 cron 通知。但缺点是需要运行一个新的守护进程。 

**注意：**

  * 在写这篇文章的时候，Arch 的 opensmtpd 包还没有在 `/var/spool/smtpd` 下创建好所有需要的目录，但是守护进程会在需要指定所有者和权限时发出警告。只需按照警告创建即可。
  * 尽管上文的配置中程序并不会接受远程连接，但使用[iptables](<../zh-cn/Iptables.html> "Iptables")或类似的方法来阻止端口 25 也是预防措施。

####  运行时间很长的 cron 任务

假设 cron 调用了这个脚本： 
    
    #!/bin/sh
    echo "我有一个可恢复错误！"
    sleep 1h
    
这时会发生以下事件： 

  1. cron 运行这个脚本
  2. 一旦 cron 检查到脚本有输出，就会启动你的邮件传输程序，并向通过管道其传递一些必要的头部内容。因为脚本还没有结束，还会有更多的输出，管道就没有关闭。
  3. 邮件传输程序打开到邮件服务器的链接，并等待后续的输出。
  4. 邮件服务器会在特定时间后关掉这个空闲的链接，你会受到类似这样的错误 : 
         
         smtpmsg='421 … Error: timeout exceeded' errormsg='the server did not accept the mail'（服务器没有接受邮件

要解决这个问题，你可以使用 [moreutils](<https://archlinux.org/packages/?name=moreutils>)包 中的 chronic 或 sponge 命令。 它们各自的手册页面中写道： 

[chronic(1)](<https://man.archlinux.org/man/chronic.1>)（时序）
    chronic 运行一个命令时，会缓存它的标准输出和标准错误输出，并只在命令失败（返回值非零或崩溃）的情况下才会一并输出。如果命令成功执行，任何无关的输出将被隐藏。
[sponge(1)](<https://man.archlinux.org/man/sponge.1>)（海绵）
    sponge 读取标准输入并将其写入指定的文件。不同于 shell 重定向，sponge 在打开输出文件之前会吸收所有的输入……如果没有指定输出文件，sponge 会输出到标准输出。

Chronic也会在打开标准输出之前缓冲命令输出。 

##  Crontab 格式

crontab 的基本格式是： 

_分_ _时_ _日_ _月_ _星期_ _命令_

  * _分_ 值从 0 到 59。
  * _时_ 值从 0 到 23。
  * _日_ 值从 1 到 31。
  * _月_ 值从 1 到 12。
  * _星期_ 值从 0 到 6, 0 代表星期日。

空格用来分开字段，要微调你的时间表，也可以用下面特殊字符来设定范围: 

符号 | 描述   
---|---  
***** | 通配符，表示所有支持的时间值   
**,** | 用逗号分隔多个时间   
**-** | 连接两个数值，给出一个范围   
**/** | 指定一个周期或频率   
  
例如，下面一行： 
    
    */5 9-16 * 1-5,9-12 1-5 ~/bin/i_love_cron.sh
    
将会在6月、7月和8月外的周一至周五，从早上 9 点到下午 4 点 55 分，每隔 5 分钟执行一次脚本 `i_love_cron.sh`。 

此外，crontab 还有一些特殊的关键字。 

Keyword | Description   
---|---  
**@reboot** | 启动时   
**@yearly** | 每年一次   
**@annually** | 同 @yearly   
**@monthly** | 每月一次   
**@weekly** | 每周一次   
**@daily** | 每天一次   
**@midnight** | 同 @daily   
**@hourly** | 每小时一次   
  
例如： 
    
    @reboot ~/bin/i_love_cron.sh
    
将在启动时执行脚本 `i_love_cron.sh`。 

更多信息参见: <https://www.adminschoice.com/crontab-quick-reference>

更多的例子和高级配置技巧可以在下面找到。 

##  基本命令

Crontabs 绝不应该被直接编辑；你应该使用 `crontab` 程序来处理你的 crontabs。 

要查看你的 crontabs： 
    
    $ crontab -l
    
要编辑你的 crontabs： 
    
    $ crontab -e
    
要移除你的 _所有_ crontabs： 
    
    $ crontab -r
    
如果你有一个保存好的 crontab ，而且你想要用它完全覆盖旧的 crontab： 
    
    $ crontab _saved_crontab_filename_
    
要从命令行([Wikipedia:stdin](<https://en.wikipedia.org/wiki/stdin> "wikipedia:stdin"))覆盖一个 crontab： 
    
    $ crontab - 
    
要编辑其他用户的 crontab： 
    
    # crontab -u _username_ -e
    
同一个格式（在命令后追加 `-u _username_`）也可以用来列出或删除 crontabs。 

##  范例

下面的条目: 
    
    01 * * * * /bin/echo Hello, world!
    
将会在每个月的每一天的每一个小时的第一分钟（例如，在12:01，1:01，2:01等）执行命令 `/bin/echo Hello, world!`

类似地, 
    
    */5 * * jan mon-fri /bin/echo Hello, world!
    
将会在一月的每个工作日每五分钟（例如，在12：00，12：05，12：10等）执行一次相同的命令。 

和前文 _Crontab 格式_ 一章相同，这一行（如 [crontab(5)](<https://man.archlinux.org/man/crontab.5>) 所述）： 
    
    *0,*5 9-16 * 1-5,9-12 1-5 /home/user/bin/i_love_cron.sh
    
将会在周内从早上 9 点到下午 4 点 55 分，每隔 5 分钟执行一次脚本 `i_love_cron.sh`，夏季除外（6月、7月和8月）。 

也可以像这样输入周期性设置： 
    
    # Chronological table of program loadings                                       
    # Edit with "crontab" for proper functionality, "man 5 crontab" for formatting
    # User: johndoe
    
    # mm  hh  DD  MM  W /path/progam [--option]...  ( W = weekday: 0-6 [Sun=0] )
      21  01  *   *   * /usr/bin/systemctl hibernate
      @weekly           $HOME/.local/bin/trash-empty

下面是一些不言自明的crontab语法例子： 
    
    30 4 echo "四点半了。"
    0 22 echo "晚上十点了。"
    30 15 25 12 echo "现在是圣诞节下午三点半。"
    30 3 * * * echo "每天早上三点半提醒我。"
    0 * * * * echo "新的一个小时到来了。"
    0 6 1,15 * * echo "每月1号和15号的早上六点。"
    0 6 * * 2,3,5 echo "周二三四的早上六点。"
    59 23 * * 1-5 echo "周内每天的最后一分钟。"
    0 */2 * * * echo "每两个小时。"
    0 20 * * 4 echo "周四的晚上八点。"
    0 20 * * Thu echo "周四的晚上八点。"
    */15 9-17 * * 2-5 echo "周内朝九晚五的每一刻钟。"
    @yearly echo "新年好！"
    
##  默认编辑器

要修改默认编辑器，请在 shell 初始化脚本中定义 `EDITOR` 环境变量，如[环境变量](<../zh-cn/Environment_variables.html> "Environment variables")所述。 

作为普通用户，需要使用 `su` 代替 `sudo` 来正确拉取环境变量： 
    
    $ su -c "crontab -e"
    
如果希望给这个命令取别名，因为 su 会在一个新启动的子 shell 中启动，为了防止一些以外的发生，需要用 `printf` 加一个任意字符串，来提醒你仍然在 root 下运行： 
    
    alias scron="su -c $(printf "%q " "crontab -e")"
    
##  运行基于 X.org 的应用程序

Cron 不在 [X.org](</wzh/index.php?title=X.org&action=edit&redlink=1> "X.org（页面不存在）") 下运行，因此它无法知道启动 X.org 应用程序所需的环境变量，因此必须显式定义。我们可以使用类似 [xuserrun-git](<https://aur.archlinux.org/packages/xuserrun-git/>)AUR 这样的程序来完成： 
    
    17 02 * ... /usr/bin/xuserrun /usr/bin/xclock
    
[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 是否仍然有效？ (在[Talk:Cron#cron x.org aplications](</wzh/index.php?title=Talk:Cron&action=edit&redlink=1> "Talk:Cron（页面不存在）")讨论)

或者可以手动定义它们（`echo $DISPLAY` 将给出当前的 DISPLAY 环境变量值）： 
    
    17 02 * ... env DISPLAY=:0 /usr/bin/xclock
    
如果需要在 cron 中运行 notify-send 进行桌面通知，因为 notify-send 通过 dbus 发送值。需要告诉 dbus 连接到正确的总线。 通过检查 DBUS_SESSION_BUS_ADDRESS 环境变量，并设置为相同的值，就可以找到地址。因此： 
    
    17 02 * ... env DBUS_SESSION_BUS_ADDRESS=your-address notify-send 'Foo bar'
    
如果是通过SSH完成的，需要给与权限： 
    
    # xhost +si:localuser:$(whoami)
    
##  异步任务处理

如果你经常关机，但又不想错过任务的执行，这里有一些解决方案（从最简单到最难）： 

### Cronie

[cronie](<https://archlinux.org/packages/?name=cronie>)包 内含 anacron。其项目主页介绍道： 

Cronie 包含了标准的 UNIX 守护进程 crond，它可以在预定的时间运行指定的程序和相关工具。 它基于最初的 cron，并增强了安全性和配置功能，比如可以使用 pam 和 SELinux。 

### Dcron

Vanilla [dcron](<https://aur.archlinux.org/packages/dcron/>)AUR 支持异步任务处理。只要用@hourly、@daily、@weekly或者@monthly加上任务名就可以了： 
    
    @hourly         ID=greatest_ever_job      echo This job is very useful.
    
### Cronwhip

[cronwhip](<https://aur.archlinux.org/packages/cronwhip/>)AUR 是一个自动运行遗漏的 cron 任务的脚本；它与以前的默认 cron 实现 _dcron_ 一起工作。 另见这个[论坛帖子](<https://bbs.archlinux.org/viewtopic.php?id=57973>)。 

### Anacron

Anacron 是 _dcron_ 的完全替代者，它可以异步处理任务。 

它由 [cronie](<https://archlinux.org/packages/?name=cronie>)包 提供，配置文件为 `/etc/anacrontab`。关于格式的信息可以在 [anacrontab(5)](<https://man.archlinux.org/man/anacrontab.5>) 中找到。运行 `anacron -T` 可以测试 `/etc/anacrontab` 的有效性。 

### Fcron

和 _anacron_ 一样，[fcron](<https://archlinux.org/packages/?name=fcron>)包 假设计算机并不总是在运行。但与 _anacron_ 不同的是，它可以在比一天更短的时间内安排这些事件，这对于经常暂停/休眠的系统（例如笔记本电脑）可能很有用。和 cronwhip 一样， fcron 也可以运行那些本应在计算机停机期间运行的作业。 

用 fcron 取代 [cronie](<https://archlinux.org/packages/?name=cronie>)包 时，spool 目录会变为 `/var/spool/fcron`，并使用 `fcrontab` 命令代替 _crontab_ 来编辑用户的 crontabs。这些 crontab 以二进制格式存储，其旁边的文本版本在 spool 目录中为 _foo_.orig。由于这种行为上的差异，任何手动编辑的用户 crontabs 可能需要进行调整。 

一个快速的脚本小程序，可以帮助您将传统的用户 crontabs 转换为 fcron 格式： 
    
    cd /var/spool/cron && (
     for ctab in *; do
      fcrontab ${ctab} -u ${ctab}
     done
    )
    
另见这个[论坛主题](<https://bbs.archlinux.org/viewtopic.php?id=140497>)。 

##  确保排他性

如果您有可能运行很久的任务（比如说变化很多或者网速突然变慢，备份可能会偶尔运行很长时间），那么 `flock`（[util-linux](<https://archlinux.org/packages/?name=util-linux>)包）可以确保 cron 任务在同一时间点只有一个运行。 
    
      5,35 * * * * /usr/bin/flock -n /tmp/lock.backup /root/make-backup.sh
    
## Cronie

cronie 的相关文件层次结构如下： 
    
       /etc/
         |----- cron.d/
                  | ----- 0hourly
         |----- cron.minutely/
         |----- cron.hourly/
                  | ----- 0anacron
         |----- anacrontab
         |----- cron.daily/
         |----- cron.monthly/
         |----- cron.weekly/
         |----- crontab
         |----- cron.deny
    
Cronie 提供了 _cron_ 和 _anacron_ 两种功能：只要系统在指定的时间可用， _cron_ 以固定的时间间隔（粒度为一分钟）运行工作，而 _anacron_ 则在以天为单位指定的时间间隔执行命令。与 cron 不同的是，它并不假设系统连续运行。当系统启动时， _anacron_ 就会检查是否有任何漏掉的任务，并进行相应的处理。 

_cron_ 任务可以在 `/etc/cron.d` 目录中类似 crontab 的文件中定义，或者在 `/etc/crontab` 文件中添加。注意后者在默认情况下并不存在，但如果存在就会被使用。按照 `/etc/cron.d/0hourly` 的内容，`/etc/cron.hourly` 中的任何可执行文件将每小时运行一次（默认为每小时的第1分钟），而在 `/etc/cron.minutely` 中的可执行文件将每分钟执行一次（如果 `/etc/cron.d/0minutely` 中有相应的指令）。这些可执行文件通常是 shell 脚本，也可以使用可执行文件的符号链接。 `/etc/cron.deny` 文件包括不允许使用 crontab 的用户列表，如果没有这个文件，只有 `/etc/cron.allow` 中列出的用户才能使用它。 

_Anacron_ 的工作原理类似，通过执行根据所需的作业频率放置在 `/etc/cron.daily`、`/etc/cron.weekly` 和 `/etc/cron.monthly`目录下的文件，cron 作业 `/etc/cron.hourly/0anacron` 确保 _anacron_ 每天运行一次，以执行其待办任务。 

**注意：**

  * Cronie 使用 `run-parts` 来执行不同目录下的脚本。文件名中不应该包含任何点号（.），因为 `run-parts` 在默认模式下会忽略它们（参见[run-parts(8)](<https://man.archlinux.org/man/run-parts.8>)）。名字必须只由大小写字母、数字、下划线和减号组成。
  * `systemctl status cronie` 的输出可能会显示诸如 `CAN'T OPEN (/etc/crontab): No such file or directory` 的内容。您可以忽略这些内容，因为这个文件 cronie 不是必须的。
  * Cronie 对 `/etc/cron.d/0hourly` 的权限要求很严格。如果 `/etc/cron.d/{hourly,weekly,daily}...` 中的任务损坏或权限不正确，`/etc/cron.d/0hourly` 中的所有任务都不会被运行（包括 anacron 启动器）。`pacman -Qkk cronie` 可以显示是否有这样的问题。

**提示：** 如果不需要某些命令的输出和电子邮件提醒，请在该 cron 任务的行末添加 `>/dev/null 2>&1`，将输出重定向到/dev/null： 
    
    0 1 5 10 * /path/to/script.sh >/dev/null 2>&1
    
您也可以在您的 crontab 文件中设置 `MAILTO=""` 变量来禁用全部电子邮件提醒。

## Dcron

cron守护进程会解析一个名为`crontab`的配置文件。系统中的每个用户都可以维护一个单独的crontab文件来单独调度命令。root 用户的 crontab 用于调度全系统的任务（用户可以选择使用 `/etc/crontab` 或 `/etc/cron.d` 目录，这取决于他们选择的 cron 实现）。 
    
    /var/spool/cron/root
    
    # Run command at a scheduled time
    # Edit this 'crontab -e' for error checking, man 1 crontab for acceptable format
    
    # <@freq>                       <tags and command>
    @hourly         ID=sys-hourly   /usr/sbin/run-cron /etc/cron.hourly
    @daily          ID=sys-daily    /usr/sbin/run-cron /etc/cron.daily
    @weekly         ID=sys-weekly   /usr/sbin/run-cron /etc/cron.weekly
    @monthly        ID=sys-monthly  /usr/sbin/run-cron /etc/cron.monthly
    
    # mm  hh  DD  MM  W /path/command (or tags) # W = week: 0-6, Sun=0
      21  01  *   *   * /usr/bin/systemctl suspend
    
下面几行是 crontab 条目的一种可接受格式，即以空格分隔的字段: 

  1. @period
  2. ID=jobname （这个是 dcron 独有的）
  3. command

crontab 条目的另一种标准格式是： 

  1. minute
  2. hour
  3. day
  4. month
  5. day of week
  6. command

crontab文件本身通常存储为 `/var/spool/cron/username`。例如，root 的 crontab 文件位于 `/var/spool/cron/root`。 

参见 crontab [man page](<../zh-cn/Man_page.html> "Man page") 获取更多信息和配置示例。 

##  另请参阅

  * [Gentoo Linux Cron 指南](<https://www.gentoo.org/doc/en/cron-guide.xml>)
  * [crontab.guru](<https://crontab.guru/>) \- cronjob 表达式在线编辑器
  * [cron-notify](<https://aur.archlinux.org/packages/cron-notify/>)AUR 是一个兼容 FreeDesktop.org 的通知服务，用于在执行命令前定期请求确认。命令在自定义配置文件中进行配置。
