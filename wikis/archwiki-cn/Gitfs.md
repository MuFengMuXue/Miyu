**翻译状态：**

  * 本文（或部分内容）译自 [Gitfs](<https://wiki.archlinux.org/title/Gitfs> "arch:Gitfs")，最近一次同步于 2024-6-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gitfs?diff=0&oldid=811263>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gitfs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自 [gitfs](<https://www.presslabs.org/gitfs/docs/>): 

    gitfs 是一个与 git 完全集成的 FUSE 文件系统。你可以在本地挂载远程仓库的分支，随后对文件所做的任何修改都会自动提交到远程仓库。
    您可以挂载任何版本库，您所做的所有改动都会自动转化为提交。gitfs 还会通过模拟每次提交的快照，显示您当前工作分支的历史。
    gitfs 对于那些需要跟踪所有文件，但又无法将所有文件整理成文件提交的地方非常有用。一个用于 git 仓库的 FUSE 文件系统，带有本地缓存。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gitfs](<https://aur.archlinux.org/packages/gitfs/>)AUR。 

##  用法

例如，通过 gitfs，用户可以将远程 git 仓库挂载为[FUSE](</wzh/index.php?title=Fuse&action=edit&redlink=1> "Fuse（页面不存在）")文件系统： 
    
    $ gitfs https://example.com/repository.git _/mount/directory_
    
请参阅 [options](<https://www.presslabs.org/gitfs/docs/arguments/>) 文档。 

##  问题解决

###  对 /var/lib/gitfs 的写访问权限

`/var/lib/gitfs` 需要存在，但不是自动创建。此外，如果想以普通用户身份挂载 gitfs，请确保该用户可写： 
    
    # mkdir /var/lib/gitfs
    # chown username:users /var/lib/gitfs
    
###  对 pygit2 的写访问权限

如果以普通用户身份运行，首次运行时 gitfs 会尝试进行自我检查，但会失败。要解决这个问题，请以根用户身份运行一次。您不需要实际挂载任何东西。以 root 身份显示帮助信息即可： 
    
    # gitfs -h
    
###  与 ssh 密钥一起使用的选项

Gitfs（以及它所依赖的 pygit2）似乎正在进行大量开发，选项也在不断变化。 虽然[官方文档](<https://www.presslabs.org/gitfs/docs/arguments/>)说可以使用 `-o key=` 选项来更改密钥，但 AUR 的 0.4.1-1 版本却要求使用 `-o ssh_key=`。 注意，如果密钥受密码保护，gitfs 不会要求输入密码。它只会返回错误信息： 
    
    _pygit2.GitError: Failed to authenticate SSH session: Callback returned error
    
建议为此创建一个单独的密钥，方法是发出 
    
    ssh-keygen
    /home/user/.ssh/gitfs_rsa
    <empty passphrase>
    <empty passphrase again>
    
##  参见

  * [git worktree](<https://git-scm.com/docs/git-worktree>)
