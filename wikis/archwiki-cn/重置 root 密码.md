**翻译状态：**

  * 本文（或部分内容）译自 [Reset lost root password](<https://wiki.archlinux.org/title/Reset_lost_root_password> "arch:Reset lost root password")，最近一次同步于 2025-01-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/Reset_lost_root_password?diff=0&oldid=807035>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Reset_lost_root_password_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本指南介绍了在遗忘 [root](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "根用户") 密码后，重置密码的几种方法。 

**警告：** 攻击者可以使用以下部分方法攻入系统。除非使用[静态数据加密](<../zh-cn/%E9%9D%99%E6%80%81%E6%95%B0%E6%8D%AE%E5%8A%A0%E5%AF%86.html> "静态数据加密")，否则无论系统和密码有多安全可靠，只要攻击者可以物理接触设备，就能启动到其它系统并导出数据。

##  使用 sudo

如果你安装了 [sudo](<../zh-cn/Sudo.html> "Sudo")，并对 `wheel` 用户组或其它你记得密码的用户授予了权限，那可以使用 `sudo passwd root` 命令修改 root 密码。 

##  使用 debug shell

  1. 将 `systemd.debug_shell` 附加到[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。
  2. 系统将会正常启动，但同时会启动 `debug-shell.service` 服务，并在 `tty9` 开启一个 root shell（`/bin/sh`），按下 `Ctrl+Alt+F9` 可以进行访问。
  3. 使用 [passwd](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86> "Passwd") 命令为 root 用户创建新密码。
  4. 完成后，[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `debug-shell.service`。

##  用 Bash 作为 Init

  1. 将 `init=/bin/bash` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")附加到启动加载器的启动项。
  2. 根文件系统应该是只读挂载，需要以可读写模式重新挂载：`mount -n -o remount,rw /`
  3. 用 [passwd](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86> "Passwd") 创建新的管理员密码。
  4. 通过 `reboot -f` 重启，不要再次忘记你的密码。

**注意：** 使用此法时有的键盘不能被初始系统正确加载，可能无法在 bash 提示符后进行输入。如果出现这种情况，你只能使用其他方法。

##  使用 LiveCD

通过 [LiveCD](<../zh-cn/U_%E7%9B%98%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8.html> "U 盘安装介质") 可以使用好几种方法：chroot 并使用 `passwd` 命令，或者编辑密码文件直接删掉密码项。除使用 chroot 时架构必须与已安装的系统匹配外，可以使用任何 Linux 的 LiveCD。这里仅介绍 chroot 方式，因为这个方法更不容易出错。 

### Change Root

  1. 启动 LiveCD, [挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")主系统的根文件系统。
  2. 然后通过下列命令重置密码（不会出现要求输入旧密码的提示）：

    passwd --root _根文件系统挂载点_ _用户名_
    
  1. 卸载根文件系统。
  2. 重启并输入你的新密码。

##  参阅

  * [如何用 Knoppix 重置忘记的密码](<https://www.howtoforge.com/how-to-reset-a-forgotten-root-password-with-knoppix-p2>)
  * [启动早期 Debug Shell](<https://systemd.io/DEBUGGING/#early-debug-shell>)
