[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Pass](<../zh-cn/Talk:Pass.html>)讨论)

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** Partial translation, abandoned since creation 2020-05-14.（在 [Talk:Pass#](<../zh-cn/Talk:Pass.html>) 中讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [Pass](<https://wiki.archlinux.org/title/Pass> "arch:Pass")，最近一次同步于 2020-05-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Pass?diff=0&oldid=612862>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Pass_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[官网](<https://www.passwordstore.org/>)提到: 

    密码管理应该要简易且遵照Unix哲学。Pass将你的密码保存在由gpg加密的文件中，并以相关的网站和资源的名称来命名文件。这些加密文件会被组织成合理的文件体系，你可以从一台装置复制到另一台装置，并用命令行程序来管理和操作它们。

Pass是一款简易的命令行密码管理器，本质上，它其实是利用[GnuPG](</wzh/index.php?title=GnuPG_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "GnuPG \(简体中文\)（页面不存在）")、[tree](<https://archlinux.org/packages/?name=tree>)包、和[Git](<../zh-cn/Git_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Git \(简体中文\)")的脚本。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [pass](<https://archlinux.org/packages/?name=pass>)包 软件包. 

另外还有图形[Qt](<../zh-cn/Qt_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Qt \(简体中文\)")界面软件包可供安装：[qtpass](<https://archlinux.org/packages/?name=qtpass>)包

##  基本用法

**注意：** 在使用Pass前，请先配置好[GnuPG](</wzh/index.php?title=GnuPG_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "GnuPG \(简体中文\)（页面不存在）")。Pass所使用的密钥信任程度(trust level)必须为"ultimate"。

初始化： 
    
    $ pass init _< gpg-id or email>_
    
若要创建一组新密码，提供一个文件名，注意文件名需要能体现出文件层次，如： _archlinux.org/wiki/username_ 。 
    
    $ pass insert archlinux.org/wiki/username
    
以文件组织的方式查看储存的密码： 
    
    $ pass
    
    Password Store
    └── archlinux.org
        └── wiki
            └── username
    
生成一组随机的新密码，执行如下命令，其中，正整数` _n_`代表想要的密码长度。 
    
    $ pass generate archlinux.org/wiki/username _n_
    
若要取得一组密码，执行如下命令，并在弹出窗口输入你的gpg密码短语(passphrase)，如使用以上范例： 
    
    $ pass archlinux.org/wiki/username
    
若您是Xorg用户并安装了[xclip](<https://archlinux.org/packages/?name=xclip>)包，您可以直接将取得的密码暂时的复制到剪贴板(clipboard)上；若您是Wayland用户，[pass-git](<https://aur.archlinux.org/packages/pass-git/>)AUR 则会使用 [wl-clipboard](<https://archlinux.org/packages/?name=wl-clipboard>)包，如使用以上范例： 
    
    $ pass -c archlinux.org/wiki/username
    
**注意：** 如果您喜欢以点击鼠标滚轮的方式来贴上密码，您可以在自己的 `~/.shellrc` 中添加：`export PASSWORD_STORE_X_SELECTION=primary`

pass 也有附加的功能可与[dmenu](<https://archlinux.org/packages/?name=dmenu>)包相结合，让用户可以轻松的搜索和复制粘贴。若要使用它，安装如下可选依赖[dmenu](<https://archlinux.org/packages/?name=dmenu>)包后，执行： 
    
    $ passmenu
    
当您选择一组密码时，dmenu将会复制密码到剪贴版上。[dmenu(1)](<https://man.archlinux.org/man/dmenu.1>) 有更多相关的自定义选项。为了更快的取得密码，您可以把这个命令绑定在一组系统快捷键上。 

##  信息格式

由`pass insert`新建的信息文件预设只会包含您的密码，有时这仍旧不太足够，因为一些应用可能会要求取得您的其他信息如：用户名、网站地址等。这时，您可以用以下命令，编辑一个已存在的信息文件： 
    
    $ pass edit _password_name_
    
如下是由[官网](<https://www.passwordstore.org>)推荐的信息排版格式。使用这种格式时，选项`-c`或`--clip`仅会复制第一行的密码。 
    
    YwrZSNH35z164ym9pI
    URL: *.amazon.com/*
    Username: AmazonianChicken@example.com
    Secret Question 1: What is your childhood best friend's most bizarre superhero fantasy? Oh god, Amazon, it's too awful to say...
    Phone Support PIN #: 84719
    
##  迁移到pass

在[这里](<https://www.zx2c4.com/projects/password-store/>)可以找到相当多脚本可将其他应用的密码导入pass。 

##  扩充

自版本1.7起，pass开始支援由社区开发的扩充，这些扩充包含一些新的命令，用以延伸pass的功能。 

  * [pass-tomb](<https://github.com/roddhjav/pass-tomb>) ([pass-tomb](<https://aur.archlinux.org/packages/pass-tomb/>)AUR)

可将信息文件以[tomb](<../zh-cn/Tomb.html> "Tomb")加密 

  * [pass-otp](<https://github.com/tadfisher/pass-otp>) ([pass-otp](<https://archlinux.org/packages/?name=pass-otp>)包)

一次性密码(OTP)支援 

  * [pass-import](<https://github.com/roddhjav/pass-import>) ([pass-import](<https://aur.archlinux.org/packages/pass-import/>)AUR)

从其他管理器导入密码的综合工具 

  * [pass-update](<https://github.com/roddhjav/pass-update>) ([pass-update](<https://aur.archlinux.org/packages/pass-update/>)AUR)

一种更新密码的快捷方式 

  * [pass-audit](<https://github.com/roddhjav/pass-audit>) ([pass-audit](<https://aur.archlinux.org/packages/pass-audit/>)AUR)

一款用以审查密码安全性的扩充 

##  进阶用法

可使用[环境变量](</wzh/index.php?title=Environment_variables_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Environment variables \(简体中文\)（页面不存在）")修改pass设定中执行存取和git命令的地方： 
    
    PASSWORD_STORE_DIR=/path/to/store
    
若想进一步了解怎么修改变量使pass支持存取多个密码仓库，参阅[此处](<https://lists.zx2c4.com/pipermail/password-store/2016-November/002463.html>)

以下的`pw()`别名范例将信息文件中第一行复制到剪贴板上，五秒后再复制第二行，再五秒后复制一组一次性密码(OTP)。如果信息文件中的第一行为密码(password)，第二行为用户名(username)，并包含一组[一次性密码(OTP)URI](<https://github.com/google/google-authenticator/wiki/Key-Uri-Format>)，此范例可按照 _username > password > otp code_的顺序将三者贴入空白栏位中(如浏览器的登入注册表)。 
    
    pw() {
    export PASSWORD_STORE_CLIP_TIME=8
    export PASSWORD_STORE_X_SELECTION=primary
    pass -c2 $1; sleep 5; pass -c $1; sleep 5; pass otp -c $1; exit
    }
    
##  Multiple pass Contexts (e.g. Teaming)

One can use aliases to set up different pass contexts, which helps when collaborating with different teams. We have gotten this working in bash as follows: 

Add aliases to your `_~/.bashrc_`: 
    
     alias passred="PASSWORD_STORE_DIR=~/.pass/red pass"
     alias passblue="PASSWORD_STORE_DIR=~/.pass/blue pass"
    
Add these for bash-completion to your `_~/.bash_completion_` and make sure [bash-completion](<https://archlinux.org/packages/?name=bash-completion>)包 is installed: 
    
     source /usr/share/bash-completion/completions/pass
     _passred(){
         PASSWORD_STORE_DIR=~/.pass/red/ _pass
     }
     complete -o filenames -o nospace -F _passred passred
     _passblue(){
         PASSWORD_STORE_DIR=~/.pass/blue/ _pass
     }
     complete -o filenames -o nospace -F _passblue passblue
    
Now you can initialize into `_~/.pass/red_` and `_~/.pass/blue_` and have two pass contexts with the `_passred_` and `_passblue_` aliases. You can generalize this further into as many contexts as you like. 

## Git integration

### Git helper usage

You can use `pass` as a credentials helper for `git`. [Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [pass-git-helper](<https://aur.archlinux.org/packages/pass-git-helper/>)AUR or [pass-git-helper-git](<https://aur.archlinux.org/packages/pass-git-helper-git/>)AUR package. Detail are described in the [github README file](<https://github.com/languitar/pass-git-helper>). 

####  `git` Configuration

Install `pass-git-helper` as a git credentials helper by calling: 
    
    git config --global credential.helper /usr/bin/pass-git-helper
    
#### Mapping File

Create the file `~/.config/pass-git-helper/git-pass-mapping.ini`. It is used to map git remote hosts to your `pass` database. The format is something like this: 
    
    [github.com]
    target=dev/github
    
    [*.fooo-bar.*]
    target=dev/fooo-bar

You can use wildcards in the host part, as shown in the example. 

#### Password Store Layout

As usual with pass, the helper assumes that the password is contained in the first line of the passwordstore entry. Additionally, if a second line is present, this line is interpreted as the username. 

For this to work, you have to use `pass insert --multiline` to create a multi line password store entry. 

###  Central Git server for pass in combination with GnuPG (SSH example)

You are able to setup a password management system by setting up a central Git server for Pass. This allows you to synchronize your central password repository through multiple client environments. 

#### Install a bare Git repository for Pass on the server

On the server run `git init --bare ~/.password-store` to create a bare repository you can push to. 

#### Import authorized public SSH keys

See [SSH keys#Copying the public key to the remote server](<../zh-cn/SSH_keys.html#Copying_the_public_key_to_the_remote_server> "SSH keys")

#### On the client

This section assumes you have configured GnuPG and have a key pair to encrypt passwords. On your local client ensure you have a local password store on the client, then enable management of local changes through Git, add your remote Git repository, and push your local Pass history. 
    
    # Create local password store
    pass init <gpg key id>
    # Enable management of local changes through Git
    pass git init
    # Add the the remote git repository as 'origin'
    pass git remote add origin user@server:~/.password-store
    # Push your local Pass history
    pass git push -u --all

Now you can use the standard Git commands, prefixed by `pass`. For example: `pass git push`, or `pass git pull`. Pass will automatically create commits when you use it to modify your password store. 

## Troubleshooting

### Encryption failed: Unusable public key

The following error can occur when attempting to insert a new entry: 
    
    $ pass insert archlinux.org/wiki/username
    Enter password for archlinux.org/wiki/username:
    Retype password for archlinux.org/wiki/username:
    gpg: XXXXXXXXX: There is no assurance this key belongs to the named user
    gpg: [stdin]: encryption failed: Unusable public key
    Password encryption aborted.
    
This occurs if the trust level of the GnuPG key is set to anything other than "ultimate." Edit the key used for `pass` to set its trust level to "ultimate." 

## See also

  * [A more comprehensive pass tutorial](<https://blog.sanctum.geek.nz/linux-crypto-passwords/>)
  * [Pass home page](<https://www.passwordstore.org/>)
  * [List of Compatible clients and possibilities for migration to Pass](<https://www.passwordstore.org/#other>)
