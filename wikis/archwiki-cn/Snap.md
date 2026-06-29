**翻译状态：**

  * 本文（或部分内容）译自 [Snap](<https://wiki.archlinux.org/title/Snap> "arch:Snap")，最近一次同步于 2024-08-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Snap?diff=0&oldid=815046>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Snap_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Flatpak](<../zh-cn/Flatpak.html> "Flatpak")
  * [AppArmor](<../zh-cn/AppArmor.html> "AppArmor")

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:Snap#](<../zh-cn/Talk:Snap.html>) 中讨论）

[Snap](<https://snapcraft.io/>) 是一个软件部署和包管理系统。这些包被称为“Snap 软件包”（“snaps”），可以通过“snapd”来管理“Snap 软件包”。它适用于一系列 Linux 发行版，因此允许与发行版无关的上游软件开发。Snap 的开发商 Canonical 管理 [Snap Store](<https://snapcraft.io/store>) 服务。用户可以通过该服务安装 Snap 软件包。 

[snapd](<https://github.com/snapcore/snapd>) 是一个用于管理 Snap 软件包的 REST API 守护进程。用户可以通过使用 _snap_ 客户端与它进行交互，该客户端是 snapd 包的一部分。 

用户可以使用 [AppArmor](<../zh-cn/AppArmor.html> "AppArmor") 限制 Snap 软件包。现在内核中默认启用了该功能。请查阅相关维基页面，了解在系统中启用 [AppArmor](<../zh-cn/AppArmor.html> "AppArmor") 的步骤。 

**警告：**

  * 如果您的系统中未启用AppArmor，则所有快照都将以 _devel_ 模式运行，这意味着它们将与从Arch Linux存储库安装的应用程序一样，可以不受限制地访问您的系统。
  * 运行不受信任的代码永远是不安全的，沙盒也无法改变这一点。

##  安装

安装 [snapd](<https://aur.archlinux.org/packages/snapd/>)AUR 包组。 

**提示：**`snapd` 在 `/etc/profile.d/snapd.sh` 中安装了一个脚本，记录了snapd软件包和桌面软件的二进制安装文件路径。重启后才会使改变生效。

如果你在你的系统中启用了 [AppArmor](<../zh-cn/AppArmor.html> "AppArmor")，snapd 是支持这种安全模型的，请根据 [AppArmor#Installation](<../zh-cn/AppArmor.html#Installation> "AppArmor") 进行安装。 

如果你在使用 _AppArmor_ ，请确保启用并打开了`apparmor.service`和`snapd.apparmor.service`服务。 

##  配置

请启用/开启`snapd.socket`服务以使`snapd`守护线程正常运行，这样才能正常使用 _snap_ 。 

##  使用

_用snap_ 工具来管理snap软件包。 

###  查找软件包

用下面的命令可以在Ubuntu Store中查询你想要安装的snap软件包： 
    
    $ snap find _searchterm_
    
###  安装软件包

一但你找到想要安装的snap软件包了，用下面的命令来安装： 
    
    # snap install _snapname_
    
这将需要root权限。目前还不能为每个用户安装snap。为了使其可以被系统使用，snap会把下载的内容放到`/var/lib/snapd/snaps`目录并挂载到`/var/lib/snapd/snap/_snapname_`。 

同时这也会为每个snap软件包创建挂载单元，并将它们作为符号链接添加到` /etc/systemd/system/multi-user.target.wants/`下 ，以便在系统启动时使所有snap软件包可用。完成后，可以使用下面的命令在已安装snap软件包的列表中找到这个snap软件包以及其版本号、修订号和开发者： 
    
    $ snap list
    
你也可以用下面的命令从本地侧载snap软件包： 
    
    # snap install --dangerous _/path/to/snap_
    
### Updating

使用以下命令来更新 snap 软脚包： 
    
    # snap refresh
    
snap 的 `refresh.timer` 会自动更新 snap 软件包。 

使用以下命令来查看下次或上次的更新时间： 
    
    # snap refresh --time
    
要设置不同的更新时间，例如每天两次： 
    
    # snap set core refresh.timer=0:00~24:00/2
    
请阅读 [system options documentation page](<https://forum.snapcraft.io/t/system-options/87>) 来详细了解如个自定义更新时间。 

###  移除软件包

下面的命令可以用来移除snap软件包： 
    
    # snap remove _snapname_
    
##  提示与技巧

###  旧版 Snap 包

某些 Snap 包（例如 Julia 和 Pycharm）使用旧版隔离模式。然而，旧版隔离模式需要 `/snap` 目录，但该目录不符合 FHS 标准。[snapd](<https://aur.archlinux.org/packages/snapd/>)AUR 软件包默认不提供此目录，但用户可以手动创建 `/var/lib/snapd/snap` 与 `/snap` 之间的符号链接，以允许安装旧版 Snap 软件包： 
    
    # ln -s /var/lib/snapd/snap /snap
    
###  隔离机制

当使用 [AppArmor](<../zh-cn/AppArmor.html> "AppArmor") 时， _snapd_ 会为 Snap 软件包生成与 Ubuntu 上相同的配置文件。[AppArmor](<../zh-cn/AppArmor.html> "AppArmor") 解析器会忽略主线内核尚未支持的规则。 

要验证基本隔离机制是否正常工作，请先安装 _hello-world_ snap 包。然后运行以下命令： 
    
    $ hello-world.evil
    
    Hello Evil World!
    This example demonstrates the app confinement
    You should see a permission denied error next
    /snap/hello-world/27/bin/evil: 9: /snap/hello-world/27/bin/evil: cannot create /var/tmp/myevil.txt: Permission denied
    
AppArmor 应该会拒绝此次访问并将其记录到日志中： 
    
    # dmesg
    
    ...
    [  +0.000003] audit: type=1327 audit(1540469583.966:257): proctitle=2F62696E2F7368002F736E61702F68656C6C6F2D776F726C642F32372F62696E2F6576696C
    [ +12.268939] audit: type=1400 audit(1540469596.236:258): apparmor="DENIED" operation="open" profile="snap.hello-world.evil" name="/var/tmp/myevil.txt" pid=10835 comm="evil" requested_mask="wc" denied_mask="wc" fsuid=1000 ouid=1000
    [  +0.000006] audit: type=1300 audit(1540469596.236:258): arch=c000003e syscall=2 success=no exit=-13 a0=55d991ba6bc8 a1=241 a2=1b6 a3=55d991ba6be0 items=0 ppid=31349 pid=10835 auid=1000 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=pts2 ses=3 comm="evil" exe="/bin/dash" subj==snap.hello-world.evil (enforce)
    ...

如果您没有看到拒绝访问的记录，请验证配置文件是否已加载： 
    
    # aa-status | grep snap.hello-world
    
       snap.hello-world.env
       snap.hello-world.evil
       snap.hello-world.hello-world
       snap.hello-world.sh
    
此外，您可以根据 snapd 检查系统中可用的沙箱功能： 
    
    $ snap debug sandbox-features
    
    apparmor:             kernel:caps kernel:domain kernel:file kernel:mount kernel:namespaces kernel:network_v8 kernel:policy kernel:ptrace kernel:query kernel:rlimit kernel:signal parser:unsafe policy:default support-level:partial
    confinement-options:  devmode
    dbus:                 mediated-bus-access
    kmod:                 mediated-modprobe
    mount:                freezer-cgroup-v1 layouts mount-namespace per-snap-persistency per-snap-profiles per-snap-updates per-snap-user-profiles stale-base-invalidation
    seccomp:              bpf-argument-filtering kernel:allow kernel:errno kernel:kill_process kernel:kill_thread kernel:log kernel:trace kernel:trap
    
### Hide the snap folder

See [XDG Base Directory#Hiding unwanted directories](<../zh-cn/XDG_Base_Directory.html#Hiding_unwanted_directories> "XDG Base Directory") to hide the `snap` folder. 

### Sudo

With `secure_path` being enabled in sudo by default, the `/var/lib/snapd/snap/bin` directory is no longer present in the default `$PATH` environment variable of the process started by sudo. Commands such as `sudo lxc list` will fail, as the `lxc` symbolic link can no longer be found by the shell process. 

This can be addressed on per user basis by adding the following snippet to `/etc/sudoers.d/90_snap`: 
    
    # Add snap binaries installation dir to PATH
    Defaults:<your-user-name> secure_path="/usr/local/sbin:/usr/local/bin:/usr/bin:/var/lib/snapd/snap/bin"
    
Where `<your-user-name>` must be replaced with the desired `$USER`. 

## Troubleshooting

### Text unreadable

If you are seeing squares instead of readable characters, you need to clear the font cache: 
    
    # rm -f /var/cache/fontconfig/*
    $ rm -f ~/.cache/fontconfig/*
    # fc-cache -r -v
    
Snapctl also stores internal caches for each individual snap, which need to be [cleared seperately](<https://askubuntu.com/a/1228809>). First, find them by running: 
    
    $ find ~/snap/ -wholename '*/.cache/fontconfig'
    
    ... /home/darth_vader/snap/mailspring/common/.cache/fontconfig
    ... /home/darth_vader/snap/authy/common/.cache/fontconfig
    ... /home/darth_vader/snap/icedrive/common/.cache/fontconfig
    ... /home/darth_vader/snap/discord/common/.cache/fontconfig
    ... /home/darth_vader/snap/bitwarden/common/.cache/fontconfig
    
Then either remove them individually or use [this simple loop](<https://gist.github.com/Techcable/a9382ad83f1b651a0e9c25e9c6f26f88>). 

Finally, Restart your session. 

### Error: cannot mount squashfs

Snap packages use the [SquashFS](</wzh/index.php?title=SquashFS&action=edit&redlink=1> "SquashFS（页面不存在）") file system. In the event of an error similar to the following: 
    
    error: system does not fully support snapd: cannot mount squashfs image using "squashfs"
    
you may verify that the SquashFS kernel module is loaded with 
    
    $ lsmod
    
    Module                  Size  Used by
    **squashfs               xxxxx  x**
    ...
    
**提示：** If you have recently [installed](<#Installation>) the snapd package to your system, you may need to reboot Arch Linux before [installing Snap packages](<#Installing>). 

###  Error: /user.slice/user-1000.slice/session-1.scope is not a snap cgroup

You need to set your **DBUS_SESSION_BUS_ADDRESS** environment variable like so: 
    
    export DBUS_SESSION_BUS_ADDRESS="unix:path=$XDG_RUNTIME_DIR/bus"
    
To make this change permanent and also available in your GUI session, consider adding this line to your **~/.xprofile** file. 

For more information and full discussion about this issue, please [read here](<https://forum.snapcraft.io/t/cannot-launch-snap-applications-with-cgroup-v2/27700/19>)

## Graphical management

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** snap plugin for [gnome-software](<https://archlinux.org/packages/?name=gnome-software>)包 is not built by default（在 [Talk:Snap#Snap support in Gnome Software 3.38](</wzh/index.php?title=Talk:Snap&action=edit&redlink=1> "Talk:Snap（页面不存在）") 中讨论）

Both Gnome Software Center and KDE Discover can provide native snap support. For KDE Discover install [discover-snap](<https://aur.archlinux.org/packages/discover-snap/>)AUR package. 

The [Snap Store](<https://snapcraft.io/snap-store>) can be installed via snap 
    
    # snap install snap-store
    
## Support

Arch Linux related mailing lists and other official Arch Linux support channels are not an appropriate place to request help with snaps on Arch Linux. An appropriate place to ask for support is the [Snapcraft forum](<https://forum.snapcraft.io>). 

## See also

  * [Official site](<https://snapcraft.io/>)
  * [GitHub repository](<https://github.com/snapcore/snapd>)
  * [ArsTechnica article](<https://arstechnica.com/information-technology/2016/06/goodbye-apt-and-yum-ubuntus-snap-apps-are-coming-to-distros-everywhere/>) (2016-06) about Ubuntu snaps becoming available for Arch and other distributions
