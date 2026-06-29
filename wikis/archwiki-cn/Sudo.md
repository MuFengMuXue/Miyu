**翻译状态：**

  * 本文（或部分内容）译自 [Sudo](<https://wiki.archlinux.org/title/Sudo> "arch:Sudo")，最近一次同步于 2025-01-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/Sudo?diff=0&oldid=824232>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Sudo_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [用户和用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户和用户组")
  * [su](<../zh-cn/Su.html> "Su")
  * [doas](<../zh-cn/Doas.html> "Doas")

[Sudo](<https://www.sudo.ws/sudo/>) 使得系统管理员可以授权特定用户或用户组作为 root 或其他用户执行命令，同时还能够对命令及其参数提供审核跟踪。 

Sudo 是对于使用 [su](<../zh-cn/Su.html> "Su") 以 root 用户身份执行命令的一个替代。与 [su](<../zh-cn/Su.html> "Su") 启动 root shell 并允许用户执行之后的所有命令不同，sudo 仅对单个命令临时授予权限。通过仅在需要时授权，sudo 可以减少因输错命令或命令存在问题导致系统损坏的可能性。 

sudo 也能以其他用户身份执行命令，并且会将用户执行的命令及失败的权限申请记录到 [journal](<../zh-cn/Systemd/Journal.html> "Journal")，以供后续安全审计使用。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sudo](<https://archlinux.org/packages/?name=sudo>)包 软件包。 

##  使用

在正确配置之前，普通用户无法使用 `sudo`。参见[#配置](<#%E9%85%8D%E7%BD%AE>)。 

要使用 _sudo_ ，只需在命令和其参数前加上 `sudo` 和空格： 
    
    $ sudo _cmd_
    
例如，要使用 pacman： 
    
    $ sudo pacman -Syu
    
参见 [sudo(8)](<https://man.archlinux.org/man/sudo.8>)。 

### Login shell

并不是所有命令都可以在前面加上 _sudo_ 就能以其它用户身份执行。特别是在使用[重定向](<https://zh.wikipedia.org/wiki/%E9%87%8D%E5%AE%9A%E5%90%91_\(%E8%AE%A1%E7%AE%97%E6%9C%BA\)> "zhwp:重定向 \(计算机\)")和[命令替换](<https://zh.wikipedia.org/wiki/%E5%91%BD%E4%BB%A4%E6%9B%BF%E6%8D%A2> "zhwp:命令替换")时，必须通过 `sudo -iu _user_`（目标用户是 root 时可以省略 `-u _user_`）使用 login shell。 

以下为例，其可以在完整的 shell 环境中执行，但无法直接附加 _sudo_ 执行： 
    
    $ sudo wpa_supplicant -B -i _interface_ -c **<(**wpa_passphrase _MYSSID passphrase_**)**
    
    Successfully initialized wpa_supplicant
    Failed to open config file '/dev/fd/63', error: No such file or directory
    Failed to read or parse configuration '/dev/fd/63'
    
##  配置

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Create an intro discussing `Defaults`, perhaps with a table that lists common settings (在 [Talk:Sudo](<../zh-cn/Talk:Sudo.html>) 中讨论)

###  默认框架

[sudoers(5) § SUDOERS OPTIONS](<https://man.archlinux.org/man/sudoers.5#SUDOERS_OPTIONS>) 在 `/etc/sudoers` 文件中列出了所有可以被 `Defaults` 命令使用的选项。 

查看 [[1]](<https://gist.github.com/AladW/7eca9799b9ea624eca31>) 获得格式优化后的 `sudoers` 选项列表（解析自 1.8.7 源码）。 

查看 [sudoers(5)](<https://man.archlinux.org/man/sudoers.5>) 获得更多信息，例如密码超时设置。 

###  查看当前设置

命令 `sudo -ll` 可以显示当前的 sudo 配置; 命令 `sudo -lU _user_` 可以查看某个特定用户的设置。 

###  使用 visudo

sudo 的配置文件是 `/etc/sudoers`，**必须** 使用 [visudo(8)](<https://man.archlinux.org/man/visudo.8>) 编辑该文件。 _visudo_ 会锁定 `sudoers` 文件，将修改保存到临时文件中，并在将其复制到 `/etc/sudoers` 前检查语法问题。 

**警告：**

  * 必须确保 `sudoers` 没有语法问题！任何错误都会导致 sudo 不可用。**必须** 使用 _visudo_ 编辑该文件防止出错。
  * [visudo(8)](<https://man.archlinux.org/man/visudo.8>) 警告说，将 _visudo_ 配置为尊重用户编辑器的环境变量设置可能会是一个安全漏洞，因为它允许拥有 _visudo_ 权限的用户通过将环境变量设置为其他内容从而以根用户身份运行任意命令而不被日志所记录。 

_visudo_ 调用的默认编辑器是 _vi_ 。[sudo](<https://archlinux.org/packages/?name=sudo>)包 包在编译时启用了 `--with-env-editor`，会采用[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `SUDO_EDITOR`，`VISUAL` 和 `EDITOR` 的设置。如果设置了`VISUAL`，就不会使用 `EDITOR`。 

要在当前 shell 会话中使用 [nano](<../zh-cn/Nano.html> "Nano") 作为 _visudo_ 编辑器，可以设置 `EDITOR=nano` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")；如果要临时使用[其他编辑器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8> "文本编辑器")，在调用 _visudo_ 前设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")即可。 
    
    # EDITOR=nano visudo
    
你还可以编辑 `/etc/sudoers` 的副本，然后使用 `visudo -c _/copy/of/sudoers_` 进行检查。该操作可以避免 _visudo_ 锁定文件。 

要永久设置编辑器，请参考[定义本地环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html#%E6%8C%89%E7%94%A8%E6%88%B7> "环境变量")。要仅修改 _visudo_ 的系统级编辑器设置，可以在 `/etc/sudoers` 中添加以下内容（假设你要使用 [nano](<../zh-cn/Nano.html> "Nano") 作为默认编辑器）： 
    
    # Set default EDITOR to restricted version of nano, and do not allow visudo to use EDITOR/VISUAL.
    Defaults      editor=/usr/bin/rnano, !env_editor
    
###  设置示例

要允许指定用户在命令前添加 `sudo` 时获得完全 root 权限，在配置文件中加入该行： 
    
    用户名   ALL=(ALL:ALL) ALL
    
要限定主机名为 `HOST_NAME` 的设备上的指定用户可以执行任意命令： 
    
    用户名   HOST_NAME=(ALL:ALL) ALL
    
要允许 [wheel](</wzh/index.php?title=Wheel&action=edit&redlink=1> "Wheel（页面不存在）") 用户组成员使用sudo： 
    
    %wheel      ALL=(ALL:ALL) ALL
    
**提示：** 创建新的管理员经常被描述为为 `wheel` 组启用 sudo 访问并将管理员加入其中，这是因为默认 Polkit 就认为 wheel 组中的成员是管理员。如果用户不是 `wheel` 组的成员，使用 Polkit 的软件可能会要求验证 root 密码而非用户密码。

禁用询问用户 `USER_NAME` 的密码： 

**警告：** 任何以您的用户名运行的程序都可以无需密码就执行 sudo。
    
    Defaults:USER_NAME      !authenticate
    
仅允许主机 `HOST_NAME` 上的用户 `USER_NAME` 执行特定命令： 
    
    USER_NAME HOST_NAME=/usr/bin/halt,/usr/bin/poweroff,/usr/bin/reboot,/usr/bin/pacman -Syu
    
**注意：** 最后的设置会覆盖前面的设置，所以限定多的配置应该放到配置文件的后面。如果用户位于 `%wheel` 用户组内，就需要将该行放于对应组配置之后。

仅允许主机 `HOST_NAME` 上的用户 `USER_NAME` 执行特定命令，但不用输入密码： 
    
    USER_NAME HOST_NAME= NOPASSWD: /usr/bin/halt,/usr/bin/poweroff,/usr/bin/reboot,/usr/bin/pacman -Syu
    
更详细的 `sudoers` 范例请参考 `/usr/share/doc/sudo/examples/sudoers`。此外，更多信息参见 [sudoers(5)](<https://man.archlinux.org/man/sudoers.5>)。 

###  sudoers 文件默认权限

`sudoers` 文件的属主和属组 ID 必须都是 0，文件权限位是 0440（-r--r-----）。如果你不小心改变了默认权限，应当立即恢复它们，否则 sudo 将会出错： 
    
    # chown -c root:root /etc/sudoers
    # chmod -c 0440 /etc/sudoers
    
##  使用技巧

###  禁用密码输入超时

比较常见的烦人问题是有个后台终端上长时间运行的进程，该进程以正常权限运行，只有在需要时才提升权限。这时就会出现 sudo 密码输入提示，该提示很容易会被忽略并导致超时，此时进程就会死亡，已完成的工作也会丢失，或者最多只是被缓存。常见的建议是启用无密码 sudo 或延长 sudo 记住密码的超时时间。这两种方法都会带来负面的安全影响。这里的解决方案应是将**输入提示** 超时禁用，且不会造成任何合理的安全影响： 
    
    Defaults passwd_timeout=0
    
###  bash 自动补全支持

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** 没理由不使用 [bash-completion](<https://archlinux.org/packages/?name=bash-completion>)包。 (在 [Talk:Sudo](<../zh-cn/Talk:Sudo.html>) 讨论)

要为 sudo 命令提供完整的 bash 自动补全功能，请安装 [bash-completion](<https://archlinux.org/packages/?name=bash-completion>)包 软件包。如果由于某些原因无法安装该包，则可在 [.bashrc](</wzh/index.php?title=.bashrc&action=edit&redlink=1> ".bashrc（页面不存在）") 中添加以下内容，以获得部分 sudo 命令的自动补全功能： 
    
    complete -cf sudo
    
### Passing aliases

The following is only relevant if the bash completion is not available (either full or reduced as described above): Aliases in [Zsh](<../zh-cn/Zsh.html> "Zsh") and [Bash](<../zh-cn/Bash.html> "Bash") are normally only expanded for the first word in a command. This means that your aliases will not normally get expanded when running the `sudo` command. One way to make the next word expand is to make an alias for sudo ending with a space. Add the following to your [shell's configuration file](<../zh-cn/Command-line_shell.html#Configuration_files> "Command-line shell"): 
    
    alias sudo='sudo '
    
[zshmisc(1) § ALIASING](<https://man.archlinux.org/man/zshmisc.1#ALIASING>) describes how this works: 

    If the replacement text ends with a space, the next word in the shell input is always eligible for purposes of alias expansions.

As well as [bash(1) § ALIASES](<https://man.archlinux.org/man/bash.1#ALIASES>): 

    If the last character of the alias value is a blank, then the next command word following the alias is also checked for alias expansion.

### Add terminal bell to the password prompt

To draw attention to a sudo prompt in a background terminal, users can simply make it echo a [bell character](<https://en.wikipedia.org/wiki/Bell_character> "wikipedia:Bell character"): 
    
    Defaults passprompt="^G[sudo] password for %p: "
    
Note the `^G` is a literal bell character. E.g. in [vim](<../zh-cn/Vim.html> "Vim"), insert using the sequence `Ctrl+v` `Ctrl+g`. If `Ctrl+v` is mapped, e.g. for pasting, one can [usually](<https://unix.stackexchange.com/a/366875>) use `Ctrl+q` instead. In [nano](<../zh-cn/Nano.html> "Nano"), `Alt+v` `Ctrl+g`. 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Is it possible to preserve the localized prompt while using bell? The same question for the case when SUDO_PROMPT is used. Is there an alternative, for example by using "-B" option as default? (在 [Talk:Sudo](<../zh-cn/Talk:Sudo.html>) 中讨论)

Another option is to set the `SUDO_PROMPT` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable"). For example, add the following to your shell configuration file: 
    
    export SUDO_PROMPT=$'\a[sudo] password for %p: '
    
###  禁用单终端 sudo

**警告：** 这将使所有进程都能使用你的 sudo 会话。

如果觉得每开一个终端使用 sudo 都要输密码很烦，可以将 `timestamp_type` 设为 `global`： 
    
    Defaults timestamp_type=global
    
###  减少要求输入密码的次数

如果觉得每 5 分钟（默认值）都要重新输密码很烦，可以将 `timestamp_timeout` 改成更长的值（单位为分钟）： 
    
    Defaults timestamp_timeout=10
    
如果在较长的脚本中使用 sudo 命令，且不想在超时后等待用户输入，则可以通过循环运行 `sudo -v` 来刷新超时（而 `sudo -K` 则会立即取消超时）。 

###  环境变量

如果你使用了大量环境变量，或者你通过 `export http_proxy="..."` 配置了代理设置，除非执行 sudo 时使用了 `-E`/`--preserve-env` 选项，否则这些变量不会被传递到根用户下。 
    
    $ sudo -E pacman -Syu
    
推荐方法是将要传递的环境变量添加到 `env_keep` 中： 
    
    /etc/sudoers
    
    Defaults env_keep += "ftp_proxy http_proxy https_proxy no_proxy"

###  使用 root 密码

通过将 `targetpw`（目标用户，默认为 root）或 `rootpw` 添加到 `/etc/sudoers` 的 Defaults 一行中，可以让 sudo 询问 root 账户的密码，而不是用户密码： 
    
    Defaults targetpw
    
为避免向用户暴露 root 账户密码，可以将该设置限定到特定组： 
    
    Defaults:%wheel targetpw
    %wheel ALL=(ALL) ALL
    
###  禁止 root 登录

用户也许希望禁止使用 root 登录。没有了 root 用户，黑客就必须要知道 sudoer 的用户名和密码，具体实例请参考 [OpenSSH#拒绝](<../zh-cn/OpenSSH.html#%E6%8B%92%E7%BB%9D> "OpenSSH")。 

**警告：**

  * 注意，禁用 root 登陆后有可能会把你自己锁在系统外。默认情况下没有安装 sudo，其默认配置也不允许无密码使用 root 权限和使用用户密码获取 root 权限。在禁用 root **之前** ，务必确保已正确配置至少一个用户的权限！
  * 如果你在 sudoers 中配置了默认使用 rootpw，就不要执行下列任一命令禁用 root 登陆：
  * 如果你已经被锁在系统外了，请参考[重置 root 密码](<../zh-cn/%E9%87%8D%E7%BD%AE_root_%E5%AF%86%E7%A0%81.html> "重置 root 密码")。

使用 `passwd` 命令锁住 root 用户： 
    
    # passwd -l root
    
使用以下命令解锁 root 用户： 
    
    $ sudo passwd -u root
    
或者，编辑 `/etc/shadow` 文件，将 root 的加密口令列替换为 `!*`： 
    
    root:!*:12345::::::
    
要再次允许 root 登陆，重新设置其密码即可： 
    
    $ sudo passwd root
    
[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** In most cases when a user ends up in an emergency shell they are using the initramfs, will not use the following configuration, unless added to the `FILES` in [mkinitcpio's configuration](<../zh-cn/Mkinitcpio.html#Configuration> "Mkinitcpio").（在 [Talk:Sudo](<../zh-cn/Talk:Sudo.html>) 中讨论）

In case of system emergency, the recovery prompt is going to ask your for a root password, making it impossible to log into recovery shell. To automatically unlock the root account in case of emergency add `SYSTEMD_SULOGIN_FORCE=1` environment variable to `rescue.service` using a [drop-in file](<../zh-cn/Drop-in_file.html> "Drop-in file"): 
    
    /etc/systemd/system/rescue.service.d/SYSTEMD_SULOGIN_FORCE.conf
    
    [Service]
    Environment=SYSTEMD_SULOGIN_FORCE=1

**提示：** 要在禁用 _root_ 账号后使用 root 交互终端，请使用 `sudo -i`。

#### kdesu

[KDE](<../zh-cn/KDE.html> "KDE") 下可能会使用 kdesu 以 root 权限执行图形程序。默认情况下，即使 root 账户被禁用，kdesu 仍可能会尝试使用 su 切换 root。可以配置 kdesu 以使用sudo，创建或编辑 `~/.config/kdesurc`，加入： 
    
    [super-user-command]
    super-user-command=sudo
    
或者使用下面命令： 
    
    $ kwriteconfig6 --file kdesurc --group super-user-command --key super-user-command sudo
    
###  示例：通过 sudo 强化安全

假设你创建了 3 个用户：admin，devel 和 archie。用户“admin”用于 journalctl，systemctl，mount，kill 和 iptable；“devel”用于安装软件包和编辑配置文件；“archie”是用户登录使用的账户。为了允许“archie”进行重启，关机和使用 netctl，需要进行以下步骤： 

编辑 `/etc/pam.d/su` 和 `/etc/pam.d/su-l`。Require user be in the wheel group, but do not put anyone in it. 
    
    #%PAM-1.0
    auth            sufficient      pam_rootok.so
    # Uncomment the following line to implicitly trust users in the "wheel" group.
    #auth           sufficient      pam_wheel.so trust use_uid
    # Uncomment the following line to require a user to be in the "wheel" group.
    auth            required        pam_wheel.so use_uid
    auth            required        pam_unix.so
    account         required        pam_unix.so
    session         required        pam_unix.so
    
仅允许 'ssh' 用户组下的用户通过 SSH 登录，只有“archie”在该组内： 
    
    # groupadd -r ssh
    # gpasswd -a archie ssh
    # echo 'AllowGroups ssh' >> /etc/ssh/sshd_config
    
[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `sshd.service`。 

将用户添加到其它组中： 
    
    # for g in power network ;do ;gpasswd -a archie $g ;done
    # for g in network power storage ;do ;gpasswd -a admin $g ;done
    
设置配置文件的权限，以使 devel 能够进行编辑： 
    
    # chown -R devel:root /etc/{http,openvpn,cups,zsh,vim,screenrc}
    
    Cmnd_Alias  POWER       =   /usr/bin/shutdown -h now, /usr/bin/halt, /usr/bin/poweroff, /usr/bin/reboot
    Cmnd_Alias  STORAGE     =   /usr/bin/mount -o nosuid\,nodev\,noexec, /usr/bin/umount
    Cmnd_Alias  SYSTEMD     =   /usr/bin/journalctl, /usr/bin/systemctl
    Cmnd_Alias  KILL        =   /usr/bin/kill, /usr/bin/killall
    Cmnd_Alias  PKGMAN      =   /usr/bin/pacman
    Cmnd_Alias  NETWORK     =   /usr/bin/netctl
    Cmnd_Alias  FIREWALL    =   /usr/bin/iptables, /usr/bin/ip6tables
    Cmnd_Alias  SHELL       =   /usr/bin/zsh, /usr/bin/bash
    %power      ALL         =   (root)  NOPASSWD: POWER
    %network    ALL         =   (root)  NETWORK
    %storage    ALL         =   (root)  STORAGE
    root        ALL         =   (ALL)   ALL
    admin       ALL         =   (root)  SYSTEMD, KILL, FIREWALL
    devel	    ALL         =   (root)  PKGMAN
    archie	    ALL         =   (devel) SHELL, (admin) SHELL 
    
完成配置后，就基本不需要以 root 身份登录了。 

“archie”可以连接到家里的 Wi-Fi： 
    
    $ sudo netctl start home
    $ sudo poweroff
    
“archie”无法以其他用户身份使用 netctl： 
    
    $ sudo -u admin -- netctl start home
    
如果“archie”需要使用 journalctl 或杀死其它进程，可以切换到对应用户： 
    
    $ sudo -i -u devel
    $ sudo -i -u admin
    
但“archie”无法切换到根用户： 
    
    $ sudo -i -u root
    
如果“archie”想以 admin 身份启动 gnu-screen 会话，可以参考以下操作： 
    
    $ sudo -i -u admin
    [admin]$ chown admin:tty `echo $TTY`
    [admin]$ screen
    
###  让 sudo 使用 /etc/sudoers.d 中的文件

_sudo_ 可以解析 `/etc/sudoers.d/` 目录中的文件，这样就不需要编辑 `/etc/sudoers`，可以单独将配置写入到新文件中，然后放入到该目录。该方式的优点包括： 

  * 不需要编辑 `sudoers.pacnew` 文件；
  * 如果新配置有问题，可以删除这个文件而不用编辑 `/etc/sudoers`（但注意下方警告）。

该目录下的文件格式与 `/etc/sudoers` 一致。如需直接编辑这些文件，可以使用 `visudo -f /etc/sudoers.d/_somefile_`，具体请参考 [sudoers(5) § Including other files from within sudoers](<https://man.archlinux.org/man/sudoers.5#Including_other_files_from_within_sudoers>)。 

`/etc/sudoers.d/` 目录中的文件是按字母顺序加载的，`.` 或 `~` 开头的文件会被跳过。为避免排序问题，文件名应以两位数字开头，例如：`01_foo`。 

**注意：** 注意文件中各项的排序，确保不会被互相覆盖。

**警告：**`/etc/sudoers.d/` 中的文件和 `/etc/sudoers` 一样，格式错误将导致 `sudo` 无法正常运行。因此，强烈建议同样使用 `visudo`。

###  编辑文件

`sudo` 提供了 `sudoedit` 命令（与 `sudo -e` 等效），能以当前用户身份及配置运行编辑器时修改仅 root 有权编辑的文件。 

要编辑文件，需将 `SUDO_EDITOR` 设为编辑器名称，并将文件名传递给 `sudoedit`，例如： 
    
    $ SUDO_EDITOR=vim sudoedit /etc/file
    
设置编辑器的方式请参考[#使用 visudo](<#%E4%BD%BF%E7%94%A8_visudo>) 和 [sudo(8) § e](<https://man.archlinux.org/man/sudo.8#e>)，但需要注意[潜在的安全问题](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E7%94%A8_sudo_%E6%9B%BF%E4%BB%A3_su> "安全")。 

如果一次性向 `sudo` 传入多个文件名，则会在编辑器中同时打开所有文件： 
    
    $ SUDO_EDITOR=vimdiff sudoedit /etc/file /etc/file.pacnew
    
###  启用嘲讽

通过 `visudo` 在 `sudoers` 文件中添加下行可以启用嘲讽彩蛋： 
    
    /etc/sudoers
    
    Defaults insults

在用户输错密码时，会将 `Sorry, try again.` 替换成各种嘲讽。 

###  启用密码输入反馈

默认情况下，输入密码是不会有视觉反馈的，目的是增强安全性。如果你想启用视觉反馈，可以添加下行进行启用： 
    
    /etc/sudoers
    
    Defaults pwfeedback

###  彩色密码提示

在 shell 初始化文件中设置 `SUDO_PROMPT` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")和 [tput(1)](<https://man.archlinux.org/man/tput.1>) 可以自定义彩色和/或粗体密码提示。 

以将 `Password: ` 显示为红色粗体为例： 
    
    export SUDO_PROMPT="$(tput setaf 1 bold)Password:$(tput sgr0) "
    
也可以使用不同颜色来显示默认消息： 
    
    export SUDO_PROMPT="$(tput setab 1 setaf 7 bold)[sudo]$(tput sgr0) $(tput setaf 6)password for$(tput sgr0) $(tput setaf 5)%p$(tput sgr0): "
    
详细信息请参考[在终端输出彩色](<../zh-cn/%E5%9C%A8%E7%BB%88%E7%AB%AF%E8%BE%93%E5%87%BA%E5%BD%A9%E8%89%B2.html> "在终端输出彩色")和 [Bash/Prompt customization](</wzh/index.php?title=Bash/Prompt_customization&action=edit&redlink=1> "Bash/Prompt customization（页面不存在）")。 

###  使用 U2F

将 U2F 与 sudo 搭配使用，可以通过物理触碰进行批准，还能基本消除公众场合下被[肩窥](<https://en.wikipedia.org/wiki/Shoulder_surfing_\(computer_security\)> "wikipedia:Shoulder surfing \(computer security\)")的风险。 

具体信息请参考[通用第二因素#无密码 sudo](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html#%E6%97%A0%E5%AF%86%E7%A0%81_sudo> "通用第二因素")。 

###  写入到受保护文件

在使用 sudo 时，无法使用 `>`/`>>` 写入到受保护文件，这时候可以使用 [tee](</wzh/index.php?title=Tee&action=edit&redlink=1> "Tee（页面不存在）")： 
    
    $ _input stream_ | sudo tee _--option_ _protected_file_1 protected_file_2..._
    
####  Vim 环境内

A similar concept is useful when you forgot to start [Vim](<../zh-cn/Vim.html> "Vim") with sudo when editing a file owned by an other user. In this case you can do the following inside [Vim](<../zh-cn/Vim.html> "Vim") to save the file: 
    
    :w !sudo tee %
    
You can add this to your `~/.vimrc` to make this trick easy-to-use with `:w!!` mapping in command mode: 
    
    ~/.vimrc
    
    " Allow saving of files as sudo when I forgot to start vim using sudo
     cmap w!! w !sudo tee > /dev/null %

The `> /dev/null` part explicitly throws away the standard output since we do not need to pass anything to another piped command. 

More detailed explanation of how and why this works can be found in [How does the vim “write with sudo” trick work?](<https://stackoverflow.com/questions/2600783/how-does-the-vim-write-with-sudo-trick-work>) article on StackOverflow. 

##  疑难解答

###  SSH TTY 问题

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[#配置](<#%E9%85%8D%E7%BD%AE>)。**

**附注：** 请提供模板的second参数以more detailed indications。（在 [Talk:Sudo](<../zh-cn/Talk:Sudo.html>) 中讨论）

远程执行命令时，SSH 默认不会分配 tty。没有分配 tty，sudo 就无法在获取密码时关闭回显。使用 SSH 的 `-t` 选项可以强制分配 tty。 

`Defaults` 的 `requiretty` 选项可以仅允许有 tty 的用户才能使用 sudo： 
    
    # Disable "ssh hostname sudo <cmd>", because it will show the password in clear text. You have to run "ssh -t hostname sudo <cmd>".
    #
    #Defaults    requiretty
    
###  权限 Umask

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[#配置](<#%E9%85%8D%E7%BD%AE>)。**

**附注：** 请提供模板的second参数以more detailed indications。（在 [Talk:Sudo](<../zh-cn/Talk:Sudo.html>) 中讨论）

Sudo 会统一用户的 [umask](<../zh-cn/Umask.html> "Umask") 值和它自己的 umask（默认是 0022）。这会防止 sudo 创建的文件权限比该用户 umask 允许的更广。在没有使用自定义 umask 时，该配置比较合理，但可能导致 sudo 创建的文件权限与 root 下直接创建的权限不同。如果这导致了问题，sudo 提供了一个方法来修复 umask，即使想要的 umask 比用户指定的 umask 权限还要多。添加下面内容（使用 `visudo`）会覆盖 sudo 的默认行为： 
    
    Defaults umask = 0022
    Defaults umask_override
    
这会将 sudo 的 umask 设置为 root 的默认 umask（0022），覆盖掉默认行为，无论用户的 umask 设置成什么都会使用这里设定的值。 
