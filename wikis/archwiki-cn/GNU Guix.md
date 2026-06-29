**翻译状态：**

  * 本文（或部分内容）译自 [Guix](<https://wiki.archlinux.org/title/Guix> "arch:Guix")，最近一次同步于 2025-01-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Guix?diff=0&oldid=821116>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Guix_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GNU Guix](<https://guix.gnu.org>) 是一个提供事务性、可复现性以及按用户管理的软件包管理器。 

虽然 _Guix_ 可以独立使用，并提供一个完整的 [GNU](<../zh-cn/GNU.html> "GNU") 发行版以及内核，但你也可以将 _Guix_ 软件包管理器安装在 [Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux") 上，从而在使用更传统且成熟的类 Unix 系统作为基础的同时，让用户能够使用 _Guix_ 。 

有关 _Guix_ 提供的按用户管理的软件包命令的详细信息，请参阅 [Guix 手册](<https://guix.gnu.org/manual/en/>)。 

**注意：** _Guix_ 并不是 [Arch Linux 的官方包管理器](<../zh-cn/Pacman.html> "Pacman")。

##  安装

在 Arch Linux 上，你可以使用 AUR 或按照《Guix Manual》中的说明手动安装 Guix。 使用 AUR 安装的好处是，pacman 可以识别软件包和 `/usr` 文件树中的额外文件。但与其他 AUR 软件包不同的是，卸载软件包并不会解除整个 Guix 安装。 由于 Guix 本身就是一个软件包管理器，而且它还可以自我更新，因此您仍需手动卸载通过 Guix 安装的文件（无论您安装的是 AUR 软件包还是手动安装）。 因此，更新一次 Guix 后，AUR 的优势就会变成劣势，因为 `/usr` 文件树中会出现许多不必要的文件，这些文件是 Guix AUR 软件包的一部分，但 Guix 不再使用它们。因此，请考虑使用手动安装。 

###  手动安装

关于手动安装，请参阅 Guix 手册[安装章节](<https://guix.gnu.org/manual/zh-cn/html_node/An-Zhuang-.html>)。 最简单的方法是使用其中链接的 shell 安装脚本。安装程序也可以从 AUR 安装，如 [guix-installer](<https://aur.archlinux.org/packages/guix-installer/>)AUR。 

截至 2021 年 12 月，该脚本会将文件安装到以下位置： 

  * `/gnu/store`、`/var/guix`（Guix store）
  * `/usr/local/share/info`、`/usr/local/bin`，（仅符号链接）
  * `/root/.config/guix`（指向当前配置文件的符号链接）
  * `/etc/guix/acl`，（替代服务器的密钥）
  * `/etc/profile.d/guix.sh`，（设置环境变量，将当前的 Guix 配置文件放在 PATH 的首位）
  * `/etc/bash_completion.d/guix`、`/usr/share/zsh/site-functions/_guix`、`/usr/share/fish/vendor_completions.d/guix.fish`（[Bash](<../zh-cn/Bash.html> "Bash")、[Zsh](<../zh-cn/Zsh.html> "Zsh") 和 [Fish](<../zh-cn/Fish.html> "Fish") 的 shell 补全）

此外，它还安装并启用了名为 `guix-daemon.service` 的 systemd 服务，并创建了用户 `guixbuilder01`...`guixbuilder10` 和组 `guixbuild`。 

现在启动一个新的登录 shell（或者重启机器），就可以开始使用 Guix 了： 
    
    $ guix install glibc-locales
    
###  AUR 软件包安装

**注意：**

  * 目前，如果 `/bin/sh` 不是指向 bash 的链接，编译检查就会失败，这在默认的 Arch 安装中不是问题。
  * 自 13.05.2018 起，如果 [BUILDDIR 环境变量](<../zh-cn/Makepkg.html#%E4%BD%BF%E7%94%A8%E5%86%85%E5%AD%98%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E8%BF%9B%E8%A1%8C%E7%BC%96%E8%AF%91> "Makepkg")指向 tmpfs 挂载，则在 makepkg 编译过程中 _guix-environment-container_ 测试会失败。

GNU Guix 可在 AUR 中以 [guix](<https://aur.archlinux.org/packages/guix/>)AUR 的形式获取。如 `PKGBUILD` 所述，需要先添加 Guix 发行者的 PGP 密钥。 

Guix 通过使用无特权的构建用户账户来运行构建过程，从而提高了构建的可重复性（reproducible）。因此，如果想同时编译 `_n_` 个软件包（例如同时为多个用户提供服务），就应该创建 `_n_` 个编译用户账户，因为 Guix 应该能够同时编译。下面的命令是按照 [Guix 手册](<https://www.gnu.org/software/guix/manual/html_node/Build-Environment-Setup.html#Build-Environment-Setup>)中描述的方法执行的： 
    
    # groupadd --system guixbuild
    # uncomment and type e.g.  10  for   _n_ below  -->  have ten users  
    # for i in `seq -w 1 _n_ `;
      do
        useradd -g guixbuild -G guixbuild           \
                -d /var/empty -s `which nologin`    \
                -c "Guix build user $i" --system    \
                guixbuilder$i;
      done
    
[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `guix-daemon.service`。 

您可能希望授权 Guix 使用[Guix 官方替代服务器](<https://ci.guix.gnu.org>)（'替代'）下载和使用二进制软件包： 
    
    # guix archive --authorize < /usr/share/guix/ci.guix.gnu.org.pub
    
##  在 /tmp 外构建软件包

如果 `/tmp` 没有提供足够的空间，可能需要扩展单元文件，以使用不同的 `TMPDIR` 进行构建（详情请参见 [Guix 手册](<https://www.gnu.org/software/guix/manual/html_node/Build-Environment-Setup.html#Build-Environment-Setup>)）。要使用 `_/tmpdir_` 代替 `/tmp` 进行编译，[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `guix-daemon.service` 添加以下几行： 
    
    [Service]
    Environment=TMPDIR=_/tmpdir_

##  卸载 Guix

停止并禁用 `guix-daemon.service`，必要时停止并禁用 `gnu-store.mount`。 如果将 Guix 作为 AUR 软件包安装，则使用[pacman](<../zh-cn/Pacman.html> "Pacman")移除 Guix。 

如果存在，移除 `/etc/systemd/system/guix-daemon.service`，`/etc/systemd/system/guix-daemon.service.d`，`/etc/systemd/system/guix-daemon.service.wants`，和`/etc/profile.d/guix.sh`。 

现在移除所有 Guix 构建用户及其组： 
    
    # for i in `seq -w 1 _n_ `; do userdel guixbuilder$i; done
    # groupdel guixbuild
    
然后删除 Guix store `/gnu` 以及 `/var/guix` 和 `/var/log/guix`。 删除 `/usr/local/share/info` 和 `/usr/local/bin` 中的过期符号链接。 同时删除 `/etc/guix/acl` 和 Guix 特有的 shell 完成文件。 

##  参见

  * [官方主页](<https://guix.gnu.org/>)
  * [中文社区](<https://guixcn.codeberg.page/>)及 [Codeberg 主页](<https://codeberg.org/guixcn>)
  * [官方 Codeberg](<https://codeberg.org/guix>)
  * [Hilton Chain 关于 Guix 的一些文章](<https://ultrarare.space/search/?keyword=Guix>)
  * 视频 [Linux 头脑风暴第十二期，GNU GuixLinux 探秘-哔哩哔哩](<https://bilibili.com/video/BV1DT4y1N7Hz>)
