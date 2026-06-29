[![](../File:User-trash-full.svg.png)](<../File:User-trash-full.svg.png>)**本文已被弃用。**

**本文所述教程或工具由于已经过时而被弃用，请使用其他替代方案：** [SSHFS](<../zh-cn/SSHFS.html> "SSHFS")、[rclone](<https://archlinux.org/packages/?name=rclone>)包 等 (在[Talk:Shfs](<../zh-cn/Talk:Shfs.html>)讨论)

[Shfs](<http://shfs.sourceforge.net/>)是一个简单易用的Linux内核模块。该模块可以让你通过ssh连接挂载远程文件系统。使用shfs访问远程文件就和访问本地文件一样，但其访问权限由ssh安全传输功能进行管理。 

**注意：** 由于shfs自2004年后就再也没有更新过，目前基于FUSE的[SSHFS](<../zh-cn/SSHFS.html> "SSHFS")应用更加广泛。

##  安装

[安装](<../zh-cn/Help:Reading_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading \(简体中文\)")[shfs-utils](<https://archlinux.org/packages/?name=shfs-utils>)包软件包。 

**警告：** 要使用shfs，需要在客户端而不是服务器端进行安装及配置。服务器端只需要运行ssh服务即可。

##  配置

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Do not simply recommend setting the SUID bit on a binary since this can have severe security implications（在 [Talk:Shfs](<../zh-cn/Talk:Shfs.html>) 中讨论）

如果想作为普通用户使用shfs挂载功能，你需要使用`chmod +s /usr/bin/shfsmount`和`chmod + /usr/bin/shfsumount`两条命令。为了更方便地使用shfs，可以在`/etc/fstab`中增加挂载项，例如： 
    
    remoteuser@Server:/data   /mnt/data   shfs    rw,noauto,uid=localuser,persistent   0       0
    remoteuser@Server:/crap   /mnt/crap   shfs    rw,noauto,uid=localuser,persistent   0       0
    remoteuser@Server:/backup /mnt/backup shfs    rw,noauto,uid=localuser,persistent   0       0
    remoteuser@Server:/home   /mnt/home   shfs    rw,noauto,uid=localuser,persistent   0       0
    
使用[SSH keys](</wzh/index.php?title=SSH_keys_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "SSH keys \(简体中文\)（页面不存在）")可以免去输入密码的步骤。 

你可能需要在挂载项中添加端口号（`port=<端口号>`） 

###  添加fstab挂载项

如要在fstab添加shfs卷，在`/etc/fstab`中按以下格式增加内容： 
    
    userid@remoteMachine:/remoteDirectory /home/userid/remoteDirectory shfs rw,user,noauto 0 0
    
##  参考

  * [SSHFS (简体中文)](</wzh/index.php?title=SSHFS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "SSHFS \(简体中文\)（页面不存在）")
  * [Ubuntu Forums](<https://ubuntuforums.org/archive/index.php/t-30332.html>)
  * [Reference](<http://shfs.sourceforge.net/>)
  * [Another reference](<https://www.openssh.com/>)
