**翻译状态：**

  * 本文（或部分内容）译自 [KDE Wallet](<https://wiki.archlinux.org/title/KDE_Wallet> "arch:KDE Wallet")，最近一次同步于 2025-02-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/KDE_Wallet?diff=0&oldid=819887>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/KDE_Wallet_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[KDE Wallet Manager](<https://utils.kde.org/projects/kwalletmanager/>) 是一个用于管理 [KDE](<../zh-cn/KDE.html> "KDE") Plasma 上的密码的工具。KWallet子系统提供了访问和管理兼容KWallet的应用所保存的密码的功能，同时你也可以用它来保存你自己的密码。 

A wallet (in the KDE's terminology, sometimes called vault or keyring) is an encrypted volume protected by a user-defined password where user and/or software can store secrets (often, credentials when the user checked _"Remember the account"_ in an application). Those vaults can be created and used manually by the user or created and used automatically in the background by some software that integrates with the wallet subsystem (_e.g._ mail applications or games). Vaults are often decrypted automatically at the user login using a PAM module (see below). 

Tips: 

  * If you only need to have a wallet available for applications using it, it is suggested to use the default name (_i.e._ `kdewallet`) and the same password as the user (for PAM).

  * Wallets are stored as encrypted files using the `.kwl` extension in the `~/.local/share/kwalletd` directory by default.

**注意：** Since KDE Frameworks 5.97.0 KDE Wallet supports org.freedesktop.secrets DBus API and can now be used by libsecret for storing and retrieving passwords and other secrets using the Secret Service API.

##  安装

KDE Wallet is often shipped with the KDE Plasma desktop environment. The wallet subsystem can be manually installed with the [kwallet](<https://archlinux.org/packages/?name=kwallet>)包 package. 

Optionally install the [kwalletmanager](<https://archlinux.org/packages/?name=kwalletmanager>)包 package for the wallet management tool. This tool can be used to graphically create and manage a KDE Wallet. 

##  配置

###  登录时自动解锁 Kwallet

To unlock KDE Wallet automatically on login, install [kwallet-pam](<https://archlinux.org/packages/?name=kwallet-pam>)包 for the PAM compatible module. The chosen KWallet password must be the same as the current user password.

**注意：**

  * [kwallet-pam](<https://archlinux.org/packages/?name=kwallet-pam>)包 与 [GnuPG](<../zh-cn/GnuPG.html> "GnuPG") keys 不兼容，所以 KDE Wallet 必须使用 `blowfish` 加密方式。
  * 所选择的 KWallet 密码必须与当前 [用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "User") 的密码相同。
  * KWallet 在账户使用自动登录的时候不会自动解锁。
  * 要自动解锁的 wallet 必须要命名为 `kdewallet` (这是默认的名字)。任何其他名字的 wallet 都不会自动解锁。
  * 如果桌面环境用的是 [KDE](<../zh-cn/KDE.html> "KDE"), 建议关闭 KDE Wallet settings 里的 _Close when last application stops using it_ 选项来防止 wallet 在每次被使用（比如获取[WiFi](</wzh/index.php?title=WiFi&action=edit&redlink=1> "WiFi（页面不存在）")密码）之后被关闭。
  * 可能需要先把默认创建的 wallet 删除——即删除所有已经储存的密码条目。
  * 如果 kwallet Migration Assistant在每次登录之后都要求输入密码，请重命名或删除 `~/.kde4/share/apps/kwallet` 文件夹.

**提示：** 替代选项是使用 KWalletManager 然后设置一个空的 Kwallet 密码, 这样就可以避免需要输入密码来解锁 wallet。只要在 _Change Password.._ 的时候把两个框都留空就可以了。但是这样的话无法阻止对 wallet 的未授权访问。 因此非常建议打开 _Access Control_ 里的 _Prompt when an application accesses a wallet_ 选项来避免未授权访问。

###  配置 PAM

下面的几行必须存在于你使用的 Display Manager 的配置文件里： 
    
    auth            optional        pam_kwallet5.so
    session         optional        pam_kwallet5.so auto_start

根据你的情况来编辑 [PAM](<../zh-cn/PAM.html> "PAM") 的配置： 

  * [SDDM](<../zh-cn/SDDM.html> "SDDM")：不需要进行修改，因为 `/etc/pam.d/sddm` 里已经写好了。
  * For [LightDM](<../zh-cn/LightDM.html> "LightDM") no further edits should be needed because the lines are already present in `/etc/pam.d/lightdm` and `/etc/pam.d/lightdm-autologin`.
  * [GDM](<../zh-cn/GDM.html> "GDM")： 修改 `/etc/pam.d/gdm-password`。
  * For [greetd](<../zh-cn/Greetd.html> "Greetd") edit `/etc/pam.d/greetd` accordingly.
  * For unlocking on tty login (no display manager, or like [greetd-tuigreet](<https://archlinux.org/packages/?name=greetd-tuigreet>)包), edit `/etc/pam.d/login` accordingly. You will need to specify the **force_run** parameter.

    /etc/pam.d/login
    
    auth            optional        pam_kwallet5.so
    session         optional        pam_kwallet5.so auto_start **force_run**
    
    /etc/pam.d/greetd
    
    #%PAM-1.0
    
    auth       required     pam_securetty.so
    auth       requisite    pam_nologin.so
    auth       include      system-local-login
    **auth       optional     pam_kwallet5.so**
    account    include      system-local-login
    session    include      system-local-login
    **session    optional     pam_kwallet5.so auto_start force_run**

##  提示与技巧

###  使用 KDE Wallet 存储 ssh key passphrases

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ksshaskpass](<https://archlinux.org/packages/?name=ksshaskpass>)包。 

Set the `SSH_ASKPASS` environment variable to `ksshaskpass` and `SSH_ASKPASS_REQUIRE` to `prefer` (prefer to use the askpass program instead of the TTY). To set it automatically on each login, create the following [environment.d(5)](<https://man.archlinux.org/man/environment.d.5>) file:
    
    ~/.config/environment.d/ssh_askpass.conf
    
    SSH_ASKPASS=/usr/bin/ksshaskpass
    SSH_ASKPASS_REQUIRE=prefer

Restart your session (i.e. relogin) so that the environment variables take effect. 

The first time you try to use an SSH key, you will get asked for its passphrase. Make sure to check the ''Remember password'' checkbox. Next time, the passphrase will be read from KDE Wallet. 

### Using the KDE Wallet to store Git credentials

[Git](<../zh-cn/Git.html> "Git") can delegate credential handling to a credential helper. By using [ksshaskpass](<https://archlinux.org/packages/?name=ksshaskpass>)包 as a credential helper, the HTTP/HTTPS and SMTP passwords can be safely stored in the KDE Wallet. 

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [ksshaskpass](<https://archlinux.org/packages/?name=ksshaskpass>)包 package. 

Configure Git by setting the `GIT_ASKPASS` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable"):
    
    ~/.config/environment.d/git_askpass.conf
    
    GIT_ASKPASS=/usr/bin/ksshaskpass

**提示：** If the `SSH_ASKPASS` environment variable [is set to ksshaskpass](<#Using_the_KDE_Wallet_to_store_ssh_key_passphrases>), then additionally setting `GIT_ASKPASS` is not required.

See [gitcredentials(7)](<https://man.archlinux.org/man/gitcredentials.7>) for alternatives and more details. 

### Store GPG key passphrases

Native KDE windows can be used to prompt for GPG key passphrases and save them in KDE Wallet. 

[Configure](<../zh-cn/GnuPG.html#pinentry> "GnuPG") `gpg-agent` to use `/usr/bin/pinentry-qt`. 

Enable the Secret Service interface. There are two ways to do this: 

  * Go to _System Settings > KDE Wallet_ and enable _Use KWallet for the Secret Service interface_.
  * Edit the KDE Wallet configuration file:

    ~/.config/kwalletrc
    
    [org.freedesktop.secrets]
    apiEnabled=true

Close the wallet and reopen it to affect these changes. You can do this using [kwalletmanager](<https://archlinux.org/packages/?name=kwalletmanager>)包 or by issuing commands to Qt D-Bus directly: 
    
    $ qdbus org.kde.kwalletd6 /modules/kwalletd6 closeAllWallets
    $ qdbus org.kde.kwalletd6 /modules/kwalletd6 open _kdewallet_ 0 $0
    
###  Chrome 和 Chromium 的 KDE Wallet 支持

Chrome/Chromium/Opera 内置了 wallet 支持。在运行 Chromium 的时候加上 `--password-store=kwallet` 或者 `--password-store=detect` 参数来启用它。如果需要永久启用这个参数，参考[Chromium#Making flags persistent](<../zh-cn/Chromium.html#Making_flags_persistent> "Chromium").。(设置 CHROMIUM_USER_FLAGS 是无效的。) 

### Query passwords from the terminal

Instead of storing passwords in plain text files, you can manually add new entries in your wallet and retrieve them with _kwallet-query_. 

For example, if you want to log into the Docker Hub registry with Podman, which supports getting the passwords from stdin with the `--password-stdin` flag, you can use the following command to login: 
    
    $ kwallet-query -r folder_entry wallet_name -f folder_name | podman login docker.io -u dockerhub_username --password-stdin
    
This way, your password is not stored in any text file and neither is it stored in the terminal history file. 

In order to run `kwallet-query` outside of a graphical session (for instance as part of an unattended backup script), set the `QT_QPA_PLATFORM=offscreen` environment variable: 
    
    $ QT_QPA_PLATFORM=offscreen kwallet-query -r folder_entry wallet_name -f folder_name
    
### Unlocking KWallet automatically in a window manager

To unlock KWallet protected by the login password, it is necessary to start `/usr/lib/pam_kwallet_init` in the [autostart](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#On_window_manager_startup> "Autostarting") portion of your window manager's configuration file in addition to configuring [PAM](<../zh-cn/PAM.html> "PAM"). 

###  禁用 KWallet

你可以使用以下方法来永久禁用KWallet：
    
    ~/.config/kwalletrc
    
    [Wallet]
    **Enabled=false**

### Automatic D-Bus activation

Most applications use `org.freedesktop.secrets.service` [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") service. KWallet does not provide a service file for it out of the box. 

You can achieve automatic activation by creating such service file:
    
    ~/.local/share/dbus-1/services/org.freedesktop.secrets.service
    
    [D-BUS Service]
    Name=org.freedesktop.secrets
    Exec=/usr/bin/kwalletd6

##  另见

  * [Wikipedia:KWallet](<https://en.wikipedia.org/wiki/KWallet> "w:KWallet")
  * [Unlocking KWallet with PAM](<https://www.dennogumi.org/2014/04/unlocking-kwallet-with-pam/>)
  * [org.freedesktop.secrets DBus API initial support](<https://invent.kde.org/frameworks/kwallet/-/merge_requests/11>)
