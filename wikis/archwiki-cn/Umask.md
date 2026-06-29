**翻译状态：**

  * 本文（或部分内容）译自 [Umask](<https://wiki.archlinux.org/title/Umask> "arch:Umask")，最近一次同步于 2025-11-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Umask?diff=0&oldid=839281>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Umask_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [File permissions and attributes](<../zh-cn/File_permissions_and_attributes.html> "File permissions and attributes")

[掩码](<https://en.wikipedia.org/wiki/umask> "wikipedia:umask")工具用于控制文件创建模式掩码，它决定新创建文件的文件权限位的初始值。这个工具的行为是由 [POSIX](<https://en.wikipedia.org/wiki/POSIX> "wikipedia:POSIX") 标准化，并在 [POSIX 开发者手册](<https://pubs.opengroup.org/onlinepubs/9799919799/utilities/umask.html>)中描述。因为 _掩码值_ 会影响当前的 shell 执行环境，所以它通常作为 shell 的内置命令实现。 

##  模式掩码的含义

模式掩码包含在新创建的文件上不应该设置的权限位，因此它是在新创建的文件上设置的权限位的[逻辑非](<https://en.wikipedia.org/wiki/Logical_complement> "wikipedia:Logical complement")。如果掩码值中的某些位被设置为`1`，新创建文件的相应权限将被禁用。因此，掩码值就像一个过滤器，可以剥离权限位，有助于设置文件的默认访问权限。 

在新创建的文件上设置权限位的结果是用位法[实质非蕴涵](<https://en.wikipedia.org/wiki/Material_nonimplication> "wikipedia:Material nonimplication")（也称为否定）计算的，可以用逻辑符号表示。 
    
    R: (D & (~M))
    
也就是说，产生的权限 `R` 是默认权限 `D` 的[位与](<https://en.wikipedia.org/wiki/Logical_conjunction> "wikipedia:Logical conjunction")和文件创建模式屏蔽 `M` 的[位非](<https://en.wikipedia.org/wiki/Bitwise_negation> "wikipedia:Bitwise negation")的结果。 

**注意：**

  * 目录的默认创建权限为`777`。
  * 因为 Linux 不允许以执行权限创建文件，文件的默认创建权限为`666`。
  * 在Linux下，只使用掩码值的文件权限位--见 [umask(2)](<https://man.archlinux.org/man/umask.2>)。掩码值中的 _suid_ 、 _sgid_ 和 _sticky_ 位被忽略。

例如，让我们假设文件创建模式掩码为`027`。这里，每个数字的位数表示为： 

  * `0`代表未在新创建的文件上设置的 _用户_ 权限位
  * `2`代表新创建文件未设置的 _组_ 权限位
  * `7`代表新创建文件未设置的 _其他_ 权限位

根据下表提供的信息，这意味着对于一个新创建的文件，例如由`User1`用户和`Group1`组所拥有，`User1`对新创建的文件拥有所有可能的权限（八进制值`7`）。`Group1`组的其他用户没有写权限（八进制值`5`），而其他用户对新创建的文件没有任何权限（八进制值`0`）。因此，在本例中采取`027`掩码值，文件将以`750`的权限创建。 

八进制 | 二进制 | 含义   
---|---|---  
`0` | `000` | 无权限   
`1` | `001` | 只执行   
`2` | `010` | 只写   
`3` | `011` | 可写和执行   
`4` | `100` | 只读   
`5` | `101` | 可读和执行   
`6` | `110` | 可读和写   
`7` | `111` | 可读，写和执行   
  
##  显示当前掩码值

要显示当前掩码值，只需调用 `umask`，不需要指定任何参数。默认的输出方式取决于实现，但通常为八进制。 
    
    $umask
    
    0027
    
当使用POSIX标准化的 `-S` 选项时，掩码值将使用符号表示来显示。然而，**符号表示值总是用八进制值的逻辑补码** ，即在新创建的文件上要设置的权限位： 
    
    $ umask -S
    
    u=rwx,g=rx,o=

##  设置掩码值

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** Arch 不使用 `/etc/profile` 设置默认的 umask, 参见 [the news](<https://archlinux.org/news/changes-to-default-password-hashing-algorithm-and-umask-settings/>). This section needs to be updated accordingly. (在[Talk:Umask](<../zh-cn/Talk:Umask.html>)讨论)

**注意：** 可以根据具体情况设置掩码值。例如，桌面用户可能会发现对其主文件夹的限制权限已足够（`useradd -m` 默认创建具有 `700` 权限的目录），因为其他人无法访问其中的所有文件。如果这不切实际（例如，在使用 [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server") 时），并且公共文件存储在私有文件中，那么请考虑限制掩码值。

可以通过 _umask_ 命令设置掩码值。指定模式掩码的字符串遵循与 [chmod](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%9D%83%E9%99%90> "Chmod") 的模式参数相同的语法规则（详见 [POSIX 开发者手册](<https://pubs.opengroup.org/onlinepubs/9799919799/utilities/chmod.html#tag_20_17_13>)）。 

全系统的掩码值可以在 `/etc/profile` (e.g. `/etc/profile.d/umask.sh`) 或默认的 shell [配置文件](<../zh-cn/Command-line_shell.html#Configuration_files> "Command-line shell")中设置，比如 `/etc/bash.bashrc`。大多数 Linux发行版，[包括 Arch](<https://gitlab.archlinux.org/archlinux/packaging/packages/shadow/-/blob/main/0003-Add-Arch-Linux-defaults-for-login.defs.patch>)，都在 `/etc/login.defs` 将掩码值的默认值设置为`022` 。也可以用 `pam_umask.so`设置掩码值，但它可能被 `/etc/profile` 或类似文件覆盖。 

如果需要设置不同的值，可以直接编辑该文件，从而影响所有用户，或者从 shell 的用户配置文件中调用 `umask`，例如 `~/.bashrc`，只修改你的掩码值，但这些修改只在下次登录后生效。要想只在当前会话中改变掩码值，只需运行 `umask` 并输入你想要的值。例如，运行 `umask 077` 会给你新文件的读写权限，以及新文件夹的读写和执行权限。 

如 [pam_umask(8) § DESCRIPTION](<https://man.archlinux.org/man/pam_umask.8#DESCRIPTION>) 中提到的, `umask=value` 也可以被用在 `/etc/passwd` 中的 [Users and groups#User database](<../zh-cn/Users_and_groups.html#User_database> "Users and groups") 部分。参见 [setting UMASK in GECOS field](<https://bbs.archlinux.org/viewtopic.php?pid=1857211#p1857211>) 的讨论。 

###  设置 KDE / Plasma 的掩码值

通过 `/etc/profile` 设置掩码值对 KDE / Plasma 会话不再有效，因为这些会话是以 systemd [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")的形式启动。 

掩码值可以通过 `pam_umask.so` 或 systemd 的[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")设置。 
    
    /etc/systemd/system/user@.service.d/override.conf
    
    [Service]
    UMask=0002

使用 `pam_umask.so` 可以在一个环境为文本控制台和图形 KDE 会话设置全系统的掩码值。在 `/etc/profile` 或 systemd 配置中的任何改动都可以省略。因此，需要在 `/etc/pam.d/login` 和 `/etc/pam.d/systemd-user` 都包含的配置文件中启用 `pam_umask.so`。 

在 `/etc/pam.d/system-login` 中添加以下一行： 
    
    # session    optional   pam_umask.so         umask=022
    
### Site-specific

[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Textedit") `/etc/login.defs` 并更新 `UMASK` 值。例如： 
    
    /etc/login.defs
    
    UMASK 077

##  参见

  * POSIX 开发者手册: 
    * [掩码值](<https://pubs.opengroup.org/onlinepubs/9799919799/utilities/umask.html>)(可在 [umask(1p)](<https://man.archlinux.org/man/umask.1p>) 阅读)
    * [chmod（扩展说明）](<https://pubs.opengroup.org/onlinepubs/9799919799/utilities/chmod.html#tag_20_17_13>)(可在 [chmod(1p)](<https://man.archlinux.org/man/chmod.1p>) 阅读)
  * [027 掩码值：安全和简单的折中方案](<https://blogs.gentoo.org/mgorny/2011/10/18/027-umask-a-compromise-between-security-and-simplicity/>)
