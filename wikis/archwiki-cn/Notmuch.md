相关文章

  * [mutt](<../zh-cn/Mutt.html> "Mutt")

**翻译状态：**

  * 本文（或部分内容）译自 [Notmuch](<https://wiki.archlinux.org/title/Notmuch> "arch:Notmuch")，最近一次同步于 2024-8-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Notmuch?diff=0&oldid=813291>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Notmuch_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Notmuch](<https://notmuchmail.org/>) 是一个邮件索引器。从本质上讲，它是 _xapian_ 之上的一个非常小的前端。 与 [Sup](<../zh-cn/Sup.html> "Sup") 一样，它只专注于一件事：为电子邮件建立索引。Notmuch 可用作电子邮件阅读器，也可简单地用作其他 MUA（如 [mutt](<../zh-cn/Mutt.html> "Mutt")）的索引器和搜索工具。 

##  概述

Notmuch 由 C 语言编写，速度比 sup-mail 快一个数量级。 Notmuch 可以在索引过程中终止，下次运行时会继续上次的工作。 与 sup-mail 一样，它也不提供永久删除不需要的电子邮件的方法（不过，请参阅[#永久删除电子邮件](<#%E6%B0%B8%E4%B9%85%E5%88%A0%E9%99%A4%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6>)）。 它不能获取或发送邮件，也不能存储你的电子邮件地址，你需要使用 [OfflineIMAP](</wzh/index.php?title=OfflineIMAP&action=edit&redlink=1> "OfflineIMAP（页面不存在）")、[msmtp](</wzh/index.php?title=Msmtp&action=edit&redlink=1> "Msmtp（页面不存在）") 和 _abook_ 等程序来完成这些任务。 

安装 [notmuch](<https://archlinux.org/packages/?name=notmuch>)包 软件包。它提供了 [python](<../zh-cn/Python.html> "Python")、[vim](<../zh-cn/Vim.html> "Vim") 和 [emacs](<../zh-cn/Emacs.html> "Emacs") 绑定。 

##  初次使用

安装完成后，您可以运行以下程序进入交互式设置： 
    
     notmuch setup
    
程序会提示你输入邮箱地址、主邮箱地址和副邮箱地址。你也可以直接编辑配置文件，该文件默认创建在 `$HOME/.notmuch-config`。 

邮件目录的后续重新索引通过 
    
     notmuch new
    
##  前端

有[一系列使用 notmuch 的方法](<https://notmuchmail.org/frontends/>)，包括 CLI 或 Unix `$EDITORS`： 

### Emacs

notmuch 的默认前端是 Emacs。它是由开发 notmuch 的同一批人开发的。 

### Vim

[notmuch-vim](<https://archlinux.org/packages/?name=notmuch-vim>)包 软件包中包含一个 Vim 界面。要启动它，请键入： 
    
    vim -c NotMuch
    
### alot

alot 是用 Python 编写的 notmuch 独立 CLI 界面。它以 [alot](<https://archlinux.org/packages/?name=alot>)包 和 [alot-git](<https://aur.archlinux.org/packages/alot-git/>)AUR 的形式提供。 

Alot 使用 [mailcap](<https://en.wikipedia.org/wiki/Mailcap> "wikipedia:Mailcap") 来处理不同类型的文件。目前包括 HTML 邮件，这意味着您需要配置一个 `~/.mailcap` 文件才能查看 HTML 邮件。至少要在 `~/.mailcap` 中加入这一行： 
    
     text/html; w3m -dump -o -document_charset=%{charset} %s; nametemplate=%s.html; copiousoutput
    
此处使用 [w3m](<https://archlinux.org/packages/?name=w3m>)包，也可使用其他基于文本的客户端，如 [links](<https://archlinux.org/packages/?name=links>)包 或 [lynx](<https://archlinux.org/packages/?name=lynx>)包，但它们的参数可能有所不同。 

当然，还可以配置更多的文件处理程序。 

### bower

[bower](<https://github.com/wangp/bower>) 是另一个 CLI 界面，使用 [Mercury](<https://mercurylang.org/>) 编写。可通过 [bower-mail](<https://aur.archlinux.org/packages/bower-mail/>)AUR 获取。 

### Neomutt

[Neomutt](<https://neomutt.org/>) \- 另一个包含许多功能补丁的 mutt fork，其中包括 [Notmuch](<https://neomutt.org/feature/notmuch>) 集成补丁。安装 [neomutt](<https://archlinux.org/packages/?name=neomutt>)包 或 [neomutt-git](<https://aur.archlinux.org/packages/neomutt-git/>)AUR 软件包。 

### astroid

[Astroid](<https://github.com/astroidmail/astroid>) 是一款使用 C++ 和 GTK 编写的图形化 MUA 和 notmuch 界面。可通过 [astroid](<https://archlinux.org/packages/?name=astroid>)包 或 [astroid-git](<https://aur.archlinux.org/packages/astroid-git/>)AUR 安装。GUI 设计非常快速，可预览 HTML 和附件，并可通过键盘导航。它可以进行大量配置，你可以使用自己喜欢的嵌入式编辑器，也可以从外部启动它。查看 [Tour](<https://github.com/astroidmail/astroid/wiki>) 了解如何使用 astroid 以及完整设置的说明，或查看 [README](<https://github.com/astroidmail/astroid>) 了解更多信息。 

##  与 mutt 集成

如果你使用 [mutt](<../zh-cn/Mutt.html> "Mutt") 作为你的 MUA，那么 notmuch 就是你索引和搜索邮件的绝佳辅助工具。[notmuch-mutt](<https://archlinux.org/packages/?name=notmuch-mutt>)包 软件包提供了将 notmuch 与 mutt 集成的脚本。 

安装 [notmuch-mutt](<https://archlinux.org/packages/?name=notmuch-mutt>)包 软件包并配置 notmuch 后，在使用 notmuch 从 mutt 进行搜索前，只需添加按键绑定以从 mutt 调用 `notmuch-mutt` perl 脚本。notmuch contrib source 建议在 `.muttrc` 中添加以下内容： 
    
    macro index <F8> \
    "<enter-command>set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key<enter>\
    <shell-escape>notmuch-mutt -r --prompt search<enter>\
    <change-folder-readonly>`echo ${XDG_CACHE_HOME:-$HOME/.cache}/notmuch/mutt/results`<enter>\
    <enter-command>set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key<enter>" \
    "notmuch: search mail"
    
    macro index <F9> \
    "<enter-command>set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key<enter>\
    <pipe-message>notmuch-mutt -r thread<enter>\
    <change-folder-readonly>`echo ${XDG_CACHE_HOME:-$HOME/.cache}/notmuch/mutt/results`<enter>\
    <enter-command>set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key<enter>" \
    "notmuch: reconstruct thread"
    
    macro index <F6> \
    "<enter-command>set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key<enter>\
    <pipe-message>notmuch-mutt tag -- -inbox<enter>\
    <enter-command>set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key<enter>" \
    "notmuch: remove message from inbox"
    
上文使用 `F8` 以使用 notmuch 搜索收件箱，使用 `F9` 从搜索结果创建线程，使用 `F6` 标记搜索结果。 

##  与 NeoMutt 集成

如果使用 [neomutt](<https://archlinux.org/packages/?name=neomutt>)包，则不需要 [notmuch-mutt](<https://archlinux.org/packages/?name=notmuch-mutt>)包 软件包。取而代之的是，创建一个包含一些基本（虚拟）邮箱的 `~/.mailboxes`。虚拟邮箱并非实际文件夹，而是 notmuch 查询特定标记的结果： 
    
    ~/.mailboxes
    
    virtual-mailboxes "inbox" "notmuch://?query=tag:inbox"
    virtual-mailboxes "archive" "notmuch://?query=tag:archive"
    virtual-mailboxes "sent" "notmuch://?query=tag:sent"
    virtual-mailboxes "newsletters" "notmuch://?query=tag:newsletters"

接下来，启用虚拟 spoolfile 并将其作为来源，让 mutt 知晓虚拟邮箱： 
    
    ~/.muttrc
    
    set virtual_spoolfile=yes
    set folder=_notmuch-root-folder_
    source ~/.mailboxes

此时，mutt 仍然会把你的邮箱列为空邮箱，因为你的邮件还没有被标记，所以查询的邮件也不是很多。要填满虚拟邮箱，首先需要标记邮件目录中的邮件。一个非常简单的方法是创建一个 shell 脚本，如下所示： 
    
    ~/.scripts/notmuch-hook.sh
    
    #!/bin/sh
    notmuch new
    # retag all "new" messages "inbox" and "unread"
    notmuch tag +inbox +unread -new -- tag:new
    # tag all messages from "me" as sent and remove tags inbox and unread
    notmuch tag -new -inbox +sent -- from:me@example.org or from:me@myself.com
    # tag newsletters, but dont show them in inbox
    notmuch tag +newsletters +unread -new -- from:newsletter@example.org or subject:'newsletter*'

将 shell 脚本设置为[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")并运行它： 
    
     ~/.scripts/notmuch-hook.sh
    
为使上述示例有效，请确保 notmuch 将新信息标记为 'new'： 
    
    ~/.notmuch-config
    
    [new]
    tags=new

最后，您的钩子脚本需要在新邮件到达时重新运行。如果使用 [offlineimap](<https://archlinux.org/packages/?name=offlineimap>)包 将 IMAP 同步到本地 maildir，则需要创建一个同步后钩子： 
    
    ~/.offlineimaprc
    
    [Account myaccount]
    postsynchook = ~/.scripts/notmuch-hook.sh

一些有用的按键绑定： 
    
    ~/.muttrc
    
    macro index A "<modify-labels>+archive -unread -inbox\\n" "Archive message"
    macro index c "<change-vfolder>?" "Change to vfolder overview"
    macro index \\\\ "<vfolder-from-query>" "Search mailbox"

##  永久删除电子邮件

一种方法是为希望从磁盘中删除的邮件保留一个标签，例如 "已删除"。然后，你可以将搜索标签与 `xargs` 结合起来，永久删除它们： 
    
     notmuch search --output=files --format=text0 tag:killed | xargs -r0 rm
     notmuch new
    
将此钩子放入 notmuch 的 `pre-new` 钩子中，就能确保在更新数据库前删除文件。 

##  参见

  * [notmuch 官方网站](<https://notmuchmail.org/>)
  * [notmuch 仓库](<https://git.notmuchmail.org/git/notmuch>)
  * [muchsync](<https://www.muchsync.org/>) \- 跨设备同步 Notmuch 邮件
  * [lieer](<http://lieer.gaute.vetsj.com/>) \- 快速获取和发送电子邮件，并在 notmuch 和 GMail 之间实现双向标签同步
