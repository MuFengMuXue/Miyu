**翻译状态：**

  * 本文（或部分内容）译自 [Tomb](<https://wiki.archlinux.org/title/Tomb> "arch:Tomb")，最近一次同步于 2022-09-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/Tomb?diff=0&oldid=731141>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Tomb_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Data-at-rest encryption](<../zh-cn/Data-at-rest_encryption.html> "Data-at-rest encryption")
  * [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt")
  * [TrueCrypt](</wzh/index.php?title=TrueCrypt&action=edit&redlink=1> "TrueCrypt（页面不存在）")
  * [Tcplay](</wzh/index.php?title=Tcplay&action=edit&redlink=1> "Tcplay（页面不存在）")

根据[官方网站](<https://www.dyne.org/software/tomb/>): 

    Tomb 是 100% 免费和开源的软件，使强大的加密变得易于使用。
    一个 Tomb 就像一个锁定的文件夹，可以安全地传输和隐藏在文件系统中。
    密钥可以分开保存：例如，在您计算机上储存 Tomb 和在 U 盘上储存密钥。

Tomb 旨在成为一个非常简单易用的软件来管理称为 tombs 的“加密目录”。只有当您拥有密钥文件且知道密码时，才能打开 Tomb。它还具有高级功能，例如隐写术。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [tomb](<https://aur.archlinux.org/packages/tomb/>)AUR 或 [tomb-git](<https://aur.archlinux.org/packages/tomb-git/>)AUR。 

##  使用

Tomb 旨在作为单个非交互式脚本从控制台使用。它还提供**tomb-open** ，这是一个简单的交互式脚本，可帮助您创建 tomb、打开 tomb、从 USB 检索密钥。 

Tomb 是从终端命令行操作的，并且需要 root 访问权限（或者只是对脚本的 [sudo](<../zh-cn/Sudo.html> "Sudo") 访问权限）。 

要创建一个名为“secret”的 100MB tomb，请执行以下操作： 
    
    # tomb dig -s 100 secret.tomb
    # tomb forge secret.tomb.key
    # tomb lock secret.tomb -k secret.tomb.key
    
要打开它，请执行以下操作： 
    
    # tomb open secret.tomb -k secret.tomb.key
    
完成后： 
    
    # tomb close
    
有关更多信息，请参阅 `tomb -h` 和 `man tomb`。 

##  高级功能

  * 隐写术（将密钥隐藏在 jpeg/wav 文件中）
  * 绑定挂钩：您可以把它的一些子目录作为 "绑定" 挂到其他目录上。例如，假设你想对你的.Mail、.firefox 和 Documents 目录进行加密。那么，您可以创建一个包含这些子目录的 tomb（如果你愿意，也可以创建其他子目录），并在 tomb 中创建一个简单的配置文件；当您运行`tomb open`时，它会自动将这些目录绑定到正确的位置。这样，您就可以很容易地得到一个加密的 firefox 配置文件，或 maildir。
  * 后挂钩：当 tomb 打开或关闭时运行的命令。您可以为此实现很多事情：打开 tomb 内的文件，将您的计算机置于“偏执”状态（例如，禁用交换），等等。

##  参见

  * [手册页](<https://web.archive.org/web/20170904181039/http://tomb.dyne.org/manual.html>)
  * [首页](<https://www.dyne.org/software/tomb/>)
  * [快速开始](<https://github.com/dyne/Tomb/wiki/Quickstart>)
  * [高级功能](<https://github.com/dyne/Tomb/wiki/Advancedfeatures>)
