**翻译状态：**

  * 本文（或部分内容）译自 [Nix](<https://wiki.archlinux.org/title/Nix> "arch:Nix")，最近一次同步于 2026-04-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Nix?diff=0&oldid=871900>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Nix_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Nix](<https://en.wikipedia.org/wiki/Nix_package_manager> "wikipedia:Nix package manager") 是一个纯函数式包管理器，旨在使包管理[可重现、声明式且可靠](<https://nixos.org>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nix](<https://archlinux.org/packages/?name=nix>)包。 

##  配置

要使 Nix 守护程序在系统启动时启动，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `nix-daemon.service`。 

将需要运行 Nix 的用户添加到 `nix-users` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")中以获取与守护程序套接字连接的权限。重启会话以使更改生效。 

添加一个[频道](<https://nixos.wiki/wiki/Nix_channels>)并更新它。 
    
    $ nix-channel --add https://nixos.org/channels/nixpkgs-unstable
    $ nix-channel --update
    
##  使用

**注意：** 如果您从 [官方仓库](<#%E5%8E%9F%E7%94%9F%E5%AE%89%E8%A3%85>) 安装了 Nix，您必须手动将 `~/.nix-profile/bin` 目录添加到您的 PATH 中。

在 shell 配置完成后，以下内容应该将 _hello_ 安装到您已经更新过的 PATH 中： 
    
    $ nix-env -iA nixpkgs.hello
    
二进制文件本身将位于 `/nix/store/[hash]-hello-[version]/bin/hello`。 

运行 `hello` 并确保它在正确的 PATH 中。如果它工作正常，您可以卸载它： 
    
    $ nix-env --uninstall hello
    
或者您可以检查已安装的程序列表： 
    
    $ nix-env --query
    
您还可以列出迭代版本： 
    
    $ nix-env --list-generations
    
更多详细信息请参阅 [nix-env(1)](<https://man.archlinux.org/man/nix-env.1>) 手册。 

##  提示与技巧

###  最大任务数

nix 默认只同时进行一个构建。以下内容将可以使 nix 同时进行与 CPU 数量相同的构建： 
    
    /etc/nix/nix.conf
    
    max-jobs = auto

###  图形加速

要运行 OpenGL 和 Vulkan 应用程序，请使用 [NixGL](<https://github.com/guibou/nixGL>)。 

###  桌面集成

要将 Nix 应用程序与您的桌面环境集成，请将 `~/.nix-profile/share` 目录添加到您的 `$XDG_DATA_DIRS` 中，例如使用 `export XDG_DATA_DIRS=$HOME/.nix-profile/share:$XDG_DATA_DIRS`。 

###  Zsh 集成用于 nix-shell

`nix-shell` 默认启动 [Bash](<../zh-cn/Bash.html> "Bash")。[zsh-nix-shell](<https://aur.archlinux.org/packages/zsh-nix-shell/>)AUR 允许您在 `nix-shell` 环境中使用 [Zsh](<../zh-cn/Zsh.html> "Zsh") 作为默认 shell。一些提示插件如 [zsh-theme-powerlevel10k](<https://aur.archlinux.org/packages/zsh-theme-powerlevel10k/>)AUR 和 [zsh-pure-prompt](<https://aur.archlinux.org/packages/zsh-pure-prompt/>)AUR 提供了 `nix-shell` 指示器。 

##  命令补全

### Zsh

[nix-zsh-completions](<https://aur.archlinux.org/packages/nix-zsh-completions/>)AUR 提供了 Zsh 对 nix 命令的补全，如 `nix-env` 和 `nix-shell`。 

##  故障排查

###  打开的文件太多

一些构建可能会遇到类似如下的问题： 
    
    error: opening directory '/nix/store/...': Too many open files
    
[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `nix-daemon.service` 并增大文件限制： 
    
    [Service]
    LimitNOFILE=65536
    
###  关于 root 用户更新频道的警告

如果在使用 Nix 时出现以下错误： 
    
    warning: Nix search path entry '/nix/var/nix/profiles/per-user/root/channels' does not exist, ignoring
    
root 用户需要更新他们的频道： 
    
    # nix-channel --update
    
###  沙盒构建问题

####  其他沙盒问题
    
    error: while setting up the build environment: mounting /proc: Operation not permitted
    error: program '/usr/bin/nix-env' failed with exit code 1
    
    1: package 'utils' in options("defaultPackages") was not found
    2: package 'stats' in options("defaultPackages") was not found
    Error: .onLoad failed in loadNamespace() for 'utils', details:
     call: system(paste(which, shQuote(names[i])), intern = TRUE, ignore.stderr = TRUE)
     error: cannot popen '/nix/store/fnkvlbls29d01jcx3wsdnhykyrl7087r-which-2.21/bin/which 'uname' 2>/dev/null', probable reason 'Cannot allocate memory'
    
这是已知的上游问题：[#2311](<https://github.com/NixOS/nix/issues/2311>)、[#3000](<https://github.com/NixOS/nix/issues/3000>) 和 [#4636](<https://github.com/NixOS/nix/issues/4636>)。 

**警告：** 通常不建议禁用沙盒，因为这会污染构建环境，且可能导致更多的构建错误。`nixpkgs` 中的所有内容都指望在启用沙盒的情况下构建。

最常见的解决方法是在配置文件中禁用沙盒： 
    
    /etc/nix/nix.conf
    
    # 禁用沙盒
    sandbox = false

然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `nix-daemon` 服务。 

###  区域设置警告

[Nixos wiki](<https://wiki.nixos.org/wiki/Locales>) 建议运行 `export LOCALE_ARCHIVE=/usr/lib/locale/locale-archive`。或者，导出环境变量 `LC_ALL=C`。 

##  参见

  * [上游 Wiki](<https://wiki.nixos.org/wiki/Nix>)
  * [Nix 包管理器指南](<https://nixos.org/nix/manual/>)
