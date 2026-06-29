**翻译状态：**

  * 本文（或部分内容）译自 [su](<https://wiki.archlinux.org/title/su> "arch:su")，最近一次同步于 2022-07-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/su?diff=0&oldid=729288>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/su_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Users and groups](<../zh-cn/Users_and_groups.html> "Users and groups")
  * [sudo](<../zh-cn/Sudo.html> "Sudo")
  * [List of applications/Security#Privilege elevation](<../zh-cn/List_of_applications/Security.html#Privilege_elevation> "List of applications/Security")

[su](<https://en.wikipedia.org/wiki/Su_\(Unix\)> "wikipedia:Su \(Unix\)") [核心应用程序](<../zh-cn/Core_utilities.html> "Core utilities")（替代用户）用来假设系统中另一个用户的身份，默认为root。 

参阅 [PAM](<../zh-cn/PAM.html> "PAM") 可以找到配置 **su** 其他特性的方法。 

##  安装

_su_ 是 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 包的一部分。 

##  用法

要切换到其他用户身份，将要切换的用户名传递给 su，像这样： 
    
    $ su _username_
    
默认情况下，当以普通用户身份运行时，系统会提示您输入要成为的用户的密码。以root身份运行 _su_ 时，不需要密码。 

如果没有传入用户名，su 默认切换为 root 用户，要求输入的密码也应该是 root 用户的密码。 

更多信息，请参阅[su(1)](<https://man.archlinux.org/man/su.1>)

##  提示和技巧

###  “登录至”其他用户

su 的默认行为是保持在当前目录中并保持原始用户的环境变量（而不是切换到新用户的环境变量）。 

这一特性的优劣需要注意以下重要的对比因素： 

  * 系统管理员可以使用普通用户的 shell 而不是自己的。特别是在有些时候，解决用户问题的最有效的方法，就是登录到该用户的帐户以重现问题或进行调试。

  * 但是通常情况下，root 用户不能登录普通用户的 shell 并使用该用户的环境变量进行操作，而是用自己的环境变量操作，这在很多情况下是不可取的，甚至是危险的。在无意中使用普通用户的 shell 时，root 可能会安装程序，或对系统进行其他更改，而这些更改与使用 root 帐户时所做的结果不同。例如，可能会安装某个程序，使得普通用户能够意外地损坏系统或未经授权访问某些数据。

因此，建议系统管理员以及被授权使用 su 的任何其他用户（建议只有极少数用户），始终保持用 `-l` 或 `--login` 选项运行 su 命令的习惯。它有两个作用： 

  1. 通过 _登录至_ 目标用户，从当前工作目录切换到目标用户的主目录（比如切换到 root 用户就是 `/root`）。
  2. 根据目标用户的首选设置（比如 `~/.bashrc` 或是 [bash](</wzh/index.php?title=Bash_%EF%BC%88%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%EF%BC%89&action=edit&redlink=1> "Bash （简体中文）（页面不存在）") shell 的其他配置文件） 切换到目标用户的环境变量。也就是说，当前工作目录和环境将会切换到和目标用户登录新会话时一样的目录和环境（而不是仅接管现有用户的会话）。

因此，管理员通常应该这样使用 su： 
    
    $ su -l
    
添加用户名 root 结果一样： 
    
    $ su -l root
    
对于任何其他用户（如名为 archie 的用户），同样可以做到： 
    
    # su -l archie
    
你可能希望在 `~/.bashrc` 里为这个规则添加一个 alias： 
    
    alias su="su -l"
    
**提示：** 有时你会遇到使用 `su -` 而不是 `su -l` 或 `su --login` 来登录用户。不提倡这种简写是因为 `-` 操作会遇到解析限制，参阅 [su(1) § DESCRIPTION](<https://man.archlinux.org/man/su.1#DESCRIPTION>)。

###  su 和 wheel 用户组

BSD su 默认仅允许 `wheel` [用户组](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups")成员切换至 root 身份。而 GNU su 默认没有这一特性，可以使用 [PAM](<../zh-cn/PAM.html> "PAM") 来模拟这一特性。将 `/etc/pam.d/su` 和 `/etc/pam.d/su-l` 中相应的行取消注释： 
    
    auth required pam_wheel.so use_uid
    