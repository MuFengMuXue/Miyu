**翻译状态：**

  * 本文（或部分内容）译自 [GNOME Keyring](<https://wiki.archlinux.org/title/GNOME_Keyring> "arch:GNOME Keyring")，最近一次同步于 2020-04-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/GNOME_Keyring?diff=0&oldid=607364>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GNOME_Keyring_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GNOME Keyring](<https://wiki.gnome.org/Projects/GnomeKeyring>) 是 GNOME 提供的一组工具，能够存储秘密、密码、密钥、认证并提供给其它程序使用。 

##  安装

如果使用的是GNOME, [gnome-keyring](<https://archlinux.org/packages/?name=gnome-keyring>)包 作为 [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组 组的一个包自动安装。在其他情况下，请[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gnome-keyring](<https://archlinux.org/packages/?name=gnome-keyring>)包 包。安装[libsecret](<https://archlinux.org/packages/?name=libsecret>)包来让应用程序使用 keyrings。不推荐安装[libgnome-keyring](<https://archlinux.org/packages/?name=libgnome-keyring>)包，除非有一些应用程序一定要用它。 

与GNOME keyring相关的其他工具包括： 

  * **secret-tool** — 通过命令行访问GNOME keyring (以及其他任何实现了[DBus Secret Service API](<https://specifications.freedesktop.org/secret-service/>)的服务) 。

     <https://wiki.gnome.org/Projects/Libsecret> || [libsecret](<https://archlinux.org/packages/?name=libsecret>)包

  * **gnome-keyring-query** — 提供一个用于从GNOME Keyring的密码库查询密码的命令行工具， 但是用的是不推荐的[libgnome-keyring](<https://archlinux.org/packages/?name=libgnome-keyring>)包包。

    || [gnome-keyring-query](<https://aur.archlinux.org/packages/gnome-keyring-query/>)AUR

  * **gkeyring** — 从命令行查询密码，用的是不推荐的[libgnome-keyring](<https://archlinux.org/packages/?name=libgnome-keyring>)包包。

     <https://github.com/kparal/gkeyring> || [gkeyring](<https://aur.archlinux.org/packages/gkeyring/>)AUR[[损坏的链接](<../../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found], [gkeyring-git](<https://aur.archlinux.org/packages/gkeyring-git/>)AUR[[损坏的链接](<../../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

##  用GUI管理

你可以通过Seahorse来管理GNOME Keyring的内容。[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [seahorse](<https://archlinux.org/packages/?name=seahorse>)包 包。 

留空或者更改GNOME keyring的密码是允许的。在seahorse里，在 "View" 下拉菜单里，选择 "By Keyring"。在Passwords标签页里，右键单击 "Passwords: login" 然后选择 "Change password." 输入旧密码然后留空新密码，你会收到警告说正在使用未加密的储存方式，如果确定请点击"Use Unsafe Storage." 

##  在GNOME外部使用钥匙环

###  没有可视化管理软件的情况下

####  自动登录

如果你在用自动登录，则需要把 login keyring 的密码设成空。 

**注意：** 所有密码会明文保存。

####  控制台登录

用控制台（tty）登录的时候，可以用 [PAM](<../../zh-cn/PAM.html> "PAM") 或 [xinitrc](<../../zh-cn/Xinit.html#xinitrc> "Xinitrc") 启动密钥环守护进程。如果用 PAM 的话它会在登录时自动解锁密钥环。 

#####  用PAM的方法

编辑 `/etc/pam.d/login` 文件，在 `auth` 部分的末尾添加 `auth optional pam_gnome_keyring.so`，在 `session` 末尾添加 `session optional pam_gnome_keyring.so auto_start`。 
    
    /etc/pam.d/login
    
    #%PAM-1.0
     
    auth       required     pam_securetty.so
    auth       requisite    pam_nologin.so
    auth       include      system-local-login
    **auth       optional     pam_gnome_keyring.so**
    account    include      system-local-login
    session    include      system-local-login
    **session    optional     pam_gnome_keyring.so auto_start**

如果用的是 [SDDM](<../../zh-cn/SDDM.html> "SDDM"), 编辑 `/etc/pam.d/sddm`. 

对 [GDM](<../../zh-cn/GDM.html> "GDM"), 在 `/etc/pam.d/passwd` 文件的最后添加 `password optional pam_gnome_keyring.so`： 
    
    /etc/pam.d/passwd
    
    #%PAM-1.0
    
    #password	required	pam_cracklib.so difok=2 minlen=8 dcredit=2 ocredit=2 retry=3
    #password	required	pam_unix.so sha512 shadow use_authtok
    password	required	pam_unix.so sha512 shadow nullok
    **password	optional	pam_gnome_keyring.so**

**注意：**

  * 为了自动解锁，密钥环的密码需要和帐户登录密码一样。
  * 依然需要按下面的章节的指示用 `~/.xinitrc` 设置环境变量。

#####  用xinitrc启动

把下面的代码添加到 `~/.xinitrc` 里： 
    
    ~/.xinitrc
    
    eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
    export SSH_AUTH_SOCK

如果用的是 Xfce，参考 [Xfce#SSH agents](<../../zh-cn/Xfce.html#SSH_agents> "Xfce")。 

###  使用显示管理器

如果用显示管理器（display manager），基本上不需要进行配置。下面这些显示管理器会在登录时自动解锁密钥环： 

  * [GDM](<../../zh-cn/GDM.html> "GDM")
  * [LightDM](<../../zh-cn/LightDM.html> "LightDM")
  * [LXDM](<../../zh-cn/LXDM.html> "LXDM")
  * [SDDM](<../../zh-cn/SDDM.html> "SDDM")

对于 GDM 和 LightDM, 密钥环[必须](<https://wiki.gnome.org/Projects/GnomeKeyring/Pam>)被命名为 _login_ 来实现自动解锁。 

如果要让在终端运行的程序也能访问密钥环（比如SSH），请添加下面的内容到 `~/.bash_profile`、`~/.zshenv`或者类似的环境变量声明文件里: 
    
    ~/.bash_profile
    
    if [ -n "$DESKTOP_SESSION" ];then
        eval $(gnome-keyring-daemon --start)
        export SSH_AUTH_SOCK
    fi
    
    ~/.config/fish/config.fish
    
    if test -n "$DESKTOP_SESSION"
        set (gnome-keyring-daemon --start | string split "=")
    end

##  SSH密钥

添加密钥: 
    
    $ ssh-add ~/.ssh/id_rsa
    Enter passphrase for /home/mith/.ssh/id_rsa:
    
列出自动加载的密钥: 
    
    $ ssh-add -L
    
禁用全部密钥: 
    
    $ ssh-add -D
    
导入密钥之后，ssh连接远程服务器的时候，会弹出一个对话框要你输入这个密钥的密码。如果你勾上登录时自动解锁密钥，那以后ssh用密钥的时候就不需要再输密码。 

或者如果要永久储存密码到密钥环里的话，用 [seahorse](<https://archlinux.org/packages/?name=seahorse>)包 提供的 `ssh-askpass` 命令： 
    
    /usr/lib/seahorse/ssh-askpass _my_key_
    
**注意：** 你需要把对应的 `.pub` （公钥文件）放到和私钥相同的目录里 (例子里公钥是`~/.ssh/id_rsa.pub`)，而且公钥文件的全名应该是私钥文件的名字加上扩展名 `.pub`。

### Start SSH and Secrets components of keyring daemon

如果你用显示管理器或者PAM启动了 Gnome Keyring 但是你的桌面不是 Gnome, Unity or Mate，SSH 和 Secrets 组件可能不会自动启动。所以你需要把 `gnome-keyring-ssh.desktop` 和 `gnome-keyring-secrets.desktop` 从 `/etc/xdg/autostart/` 里复制到 `~/.config/autostart/`，而且删除文件里面的 `OnlyShowIn`。下面是例子 
    
    $ cp /etc/xdg/autostart/{gnome-keyring-secrets.desktop,gnome-keyring-ssh.desktop} ~/.config/autostart/
    $ sed -i '/^OnlyShowIn.*$/d' ~/.config/autostart/gnome-keyring-secrets.desktop
    $ sed -i '/^OnlyShowIn.*$/d' ~/.config/autostart/gnome-keyring-ssh.desktop
    
###  禁用钥匙环的守护进程组件

如果你想要用别的 SSH 客户端，比如[ssh-agent](<../../zh-cn/SSH_keys.html#ssh-agent> "SSH keys")、[gpg-agent](<../../zh-cn/GnuPG.html#gpg-agent> "GnuPG")，你需要禁用 GNOME Keyring的 `ssh` 组件。如果只想对某个用户做这种更改，复制 `/etc/xdg/autostart/gnome-keyring-ssh.desktop` 到 `~/.config/autostart` 然后往 `~/.config/autostart/gnome-keyring-ssh.desktop`里面添加 `Hidden=true`。然后重新登录。 

**注意：** 如果你用的是基于 [Wayland](<../../zh-cn/Wayland.html> "Wayland") 的 [GNOME](<../../zh-cn/GNOME.html> "GNOME") 3.24 或者更老的版本，gnome-shell 会让 `SSH_AUTH_SOCK` 指向 gnome-keyring（无论它有没有运行）。为了阻止这个，你需要在 gnome-shell 启动之前设置 `GSM_SKIP_SSH_AGENT_WORKAROUND` 环境变量，比如把 `GSM_SKIP_SSH_AGENT_WORKAROUND DEFAULT=1` 添加到 `~/.pam_environment`。

##  提示与小技巧

###  软件中的插件

  * [Chromium](<../../zh-cn/Chromium.html#Force_a_password_store> "Chromium")

###  去除密码
    
    gnome-keyring-daemon -r -d
    
这个命令会启动新的 gnome keyring 守护进程并把之前运行的 gnome keyring 都关掉。 

###  Git的插件

如果你用 HTTPS 来 push [Git](<../../zh-cn/Git.html> "Git")，GNOME keyring 很有用。 

[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [libsecret](<https://archlinux.org/packages/?name=libsecret>)包。 

配置 Git 使用 gnome kerying： 
    
    $ git config --global credential.helper /usr/lib/git-core/git-credential-libsecret
    
下一次 _git push_ 的时候如果你没有解锁密钥环，它会提示你解锁。 

###  GnuPG的插件

某些使用 GnuPG 的程序要求指定 `pinentry-program`。 在 `~/.gnupg/gpg-agent.conf` 里添加以下内容来让 Gnome 3 pinentry for Gnome Keyring 去管理密码弹窗（passphrase prompts）。 
    
    ~/.gnupg/gpg-agent.conf
    
    pinentry-program /usr/bin/pinentry-gnome3

或者可以使用 [force loopback for GPG](<../../zh-cn/GnuPG.html#Unattended_passphrase> "GnuPG") 来实现在应用内输入密码。 

##  故障排除

###  密码没被记住

如果你每次登录的时候都收到密码提示框，并且你发现你的密码没有被自动保持你可能需要创建或设置一个默认钥匙环 

确保 [seahorse](<https://archlinux.org/packages/?name=seahorse>)包 包已经[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")了, 打开它 (系统设置中的"密码和密钥") 并且选中“视图” > “根据钥匙环”。 如果在左边的一竖排中没看到钥匙环 (一个锁一样的图标)， 打开“文件” > “新建” > “密码钥匙环”，然后取一个名字，你可能会被要求输入一个密码。如果你没有给钥匙环密码，钥匙环将会自动解锁，即使使用自动登录，密码也不会被安全保存。最后，右键你创建的钥匙环并选择“设为默认”。 

###  重置密钥环

如果出现报错 "The password you use to login to your computer no longer matches that of your login keyring", 可能要重置密钥环。在 seahorse 中右键点击 “默认密钥”，并选择修改密码。 

也可以删除 `~/.local/share/keyrings/` 中的 "login.keyring" and "user.keystore"，密钥环里的所有密码都会丢失，删除后重新登录。 

##  参见

  * [GNOME wiki](<https://wiki.gnome.org/action/show/Projects/GnomeKeyring>)
