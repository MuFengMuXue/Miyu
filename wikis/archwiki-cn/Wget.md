**翻译状态：**

  * 本文（或部分内容）译自 [Wget](<https://wiki.archlinux.org/title/Wget> "arch:Wget")，最近一次同步于 2024-6-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Wget?diff=0&oldid=810890>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Wget_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GNU Wget](<https://www.gnu.org/software/wget/>) 是一款自由软件，用于使用[HTTP](</wzh/index.php?title=HTTP&action=edit&redlink=1> "HTTP（页面不存在）")、HTTPS、[FTP](<../zh-cn/Category:FTP.html> "FTP")和 FTPS _（FTPS 的支持自 1.18 版起）_ 来检索文件。它是一个非交互式命令行工具，因此从脚本中调用它很容易。 

##  安装

### wget 1.x

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [wget](<https://archlinux.org/packages/?name=wget>)包 软件包。[git](<../zh-cn/Git.html> "Git") 版本存在于 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") ，其名称为 [wget-git](<https://aur.archlinux.org/packages/wget-git/>)AUR。 

### wget2

wget2 是命令行语法与之几乎完全相同的另一个软件，它"是 GNU Wget 的后继者"，"从零开始设计和编写"。这个重写版本"可以多线程运行，并可用许多功能来实现快速操作。由于采用了 HTTP2、HTTP 压缩、并行连接和使用 If-Modified-Since HTTP 请求头技术，在许多情况下，Wget2 的下载速度比 Wget1.x 快得多"。 

要使用 wget2，请从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [wget2](<https://aur.archlinux.org/packages/wget2/>)AUR。需要注意的是，这需要对 [pandoc](</wzh/index.php?title=Pandoc&action=edit&redlink=1> "Pandoc（页面不存在）") 进行 makedepend，依赖度较高；您也可以[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中的 [wget2-no-docs](<https://aur.archlinux.org/packages/wget2-no-docs/>)AUR 来避免依赖。 

##  配置

可在 `/etc/wgetrc` 中配置。默认配置文件不仅文档详尽，而且很少需要修改。更多复杂选项，请参见 [wget(1) § OPTIONS](<https://man.archlinux.org/man/wget.1#OPTIONS>)。 

###  FTP 自动化

通常，[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 用于在网络之间安全地传输文件。不过，相比于通过 SSH 运行的 scp 和[rsync](<../zh-cn/Rsync.html> "Rsync")，FTP 占用的资源更少。FTP 并不安全，但当在受防火墙保护的环境中，在 CPU 紧张的系统上传输大量数据时，使用 FTP 可以被证明是有好处的。 
    
    wget ftp://root:somepassword@10.13.X.Y//ifs/home/test/big/"*.tar"
    
    3,562,035,200 74.4M/s   in 47s
    
在本例中，Wget 以每秒 74.4MB 的速度传输了一个 3.3GiB 的文件。 

简而言之，该程序 

  * 可编写脚本
  * 比 ssh 更快
  * 可替代字符串变量的语言易于使用
  * [globbing](<https://en.wikipedia.org/wiki/glob_\(programming\)> "wikipedia:glob \(programming\)")capable

###  代理

Wget 使用标准代理环境变量。请参阅[代理设置](</wzh/index.php?title=%E4%BB%A3%E7%90%86%E8%AE%BE%E7%BD%AE&action=edit&redlink=1> "代理设置（页面不存在）")。 

使用代理验证功能 
    
    $ wget --proxy-user "DOMAIN\USER" --proxy-password "PASSWORD" URL
    
不包括使用 HTML 验证表单的代理。 

###  pacman 集成

要让 [pacman](<../zh-cn/Pacman.html> "Pacman") 自动使用 Wget 和带有身份验证的代理，请将 Wget 命令写入 `/etc/pacman.conf` 中的 `[options]` 部分： 
    
    XferCommand = /usr/bin/wget --proxy-user "domain\user" --proxy-password="password" --passive-ftp --quiet --show-progress --continue --output-document=%o %u
    
**警告：** 请注意，以纯文本存储密码并不安全。可使用 `chmod 600 /etc/pacman.conf` 确保只有 root 才能读取该文件。

##  用法

本节将解释 Wget 的一些使用场景。 

###  基础用法

Wget 最基本、最常见的用途之一就是从互联网上下载文件。 
    
    $ wget <url>
    
当你已经知道要下载文件的 URL 时，这比通常在浏览器上下载文件并手动将其移动到正确的目录要快得多。不言而喻的是，你可找到一些方法来利用其最简单的用法进行自动下载，如果你想要。 

###  完整网站存档

Wget 可以将绝对链接改为相对链接，从而在存档完整网站的同时保留正确的链接目的地。 
    
    $ wget --recursive --no-parent --convert-links 'target-url-here'
    
如果是动态网站，还可以使用一些其他选项将其转换为静态 HTML。 

    $ wget --recursive --no-parent --page-requisites --adjust-extension --convert-links --backup-converted 'target-url-here'
    
_wget_ 还提供了绕过下载阻止机制的选项。 
    
    $ wget --recursive --no-parent --convert-links --random-wait --execute robots=off --user-agent "Mozilla/5.0" 'target-url-here'
    
And if third-party content is to be included in the download, `-H/--span-hosts` switch can be used alongside `-r/--recursive` to recurse to linked hosts. 
