**翻译状态：**

  * 本文（或部分内容）译自 [Bubblewrap](<https://wiki.archlinux.org/title/Bubblewrap> "arch:Bubblewrap")，最近一次同步于 2026-03-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Bubblewrap?diff=0&oldid=868210>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Bubblewrap_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Bubblewrap/示例](<../zh-cn/Bubblewrap/%E7%A4%BA%E4%BE%8B.html> "Bubblewrap/示例")
  * [Firejail](<../zh-cn/Firejail.html> "Firejail")
  * [Security](<../zh-cn/%E5%AE%89%E5%85%A8.html> "Security")

[Bubblewrap](<https://github.com/containers/bubblewrap>) 是一款轻量化的沙箱应用，常为 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak") 和其他容器工具所用。安装和运行 bubblewrap 所需的资源非常少。虽然软件包名称是 bubblewrap，实际的命令行接口却是 [bwrap(1)](<https://man.archlinux.org/man/bwrap.1>)。Bubblewrap 所值得注意的特性包括支持 cgroup、IPC（进程间通信）、mount、network、PID、user、UTS [namespaces](<https://en.wikipedia.org/wiki/Linux_namespaces> "wikipedia:Linux namespaces") 和 [seccomp](<https://en.wikipedia.org/wiki/Seccomp> "wikipedia:Seccomp") 过滤。注意 bubblewrap 在沙箱内会丢弃所有的 [capabilities](<../zh-cn/Capabilities.html> "Capabilities")，因此子任务的权限不能超过其父任务。但 bubblewrap 对文件路径的黑白名单缺乏明确支持。 

**警告：** Bubblewrap 是一种能提供 namespaces 和 seccomp 过滤等沙箱化技术的工具。默认情况下，不提供能够隔离所用技术的缺陷的完整沙箱环境。运行不受信任的代码永远是危险的，沙箱化技术也不会改变这一事实。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [bubblewrap](<https://archlinux.org/packages/?name=bubblewrap>)包。 

**注意：**

  * 有关 Arch Linux 内核所支持的 [user_namespaces(7)](<https://man.archlinux.org/man/user_namespaces.7>) 的更多信息，参见[安全#沙盒程序](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E6%B2%99%E7%9B%92%E7%A8%8B%E5%BA%8F> "安全")。
  * [linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 用户请忽略上述两个软件包并请考虑安装 [bubblewrap-suid](<https://archlinux.org/packages/?name=bubblewrap-suid>)包。更多相关信息请参阅 [FS#63316](<https://bugs.archlinux.org/task/63316>)。

##  配置

可通过直接在命令行中调用或是作为组成[复杂包装器](<https://github.com/containers/bubblewrap/blob/main/demos/flatpak-run.sh>)的一部分 [shell 脚本](<https://github.com/containers/bubblewrap/blob/main/demos/bubblewrap-shell.sh>)中使用 bubblewrap。与一些自动在沙箱内将 `/var` 和 `/etc` 设置为只读的应用程序（例如 [Firejail](<../zh-cn/Firejail.html> "Firejail")）不同，bubblewrap 不会做这样的操作假设。应该由用户根据想要沙箱化运行的程序来决定需要传入何种配置选项。以 setuid 权限运行的 bubblewrap 不会自动创建用户命名空间（user namespaces），但可以接受典型的环境变量，如 `$HOME` 和 `$USER`。 

强烈建议安装 [strace](<https://archlinux.org/packages/?name=strace>)包 软件包用于了解要以沙箱运行的程序的所需文件。 

##  bubblewrap 配置管理器

除了手动配置，也可以使用配置管理器并通过更简单的操作来自动化配置 bubblewrap。 

  * **[Bubblejail](</wzh/index.php?title=Bubblejail&action=edit&redlink=1> "Bubblejail（页面不存在）")** — 基于 bubblewrap 的沙箱，有基于资源的权限模型（提供了用于权限配置的图形界面）。

     <https://github.com/igo95862/bubblejail> || [bubblejail](<https://aur.archlinux.org/packages/bubblejail/>)AUR

  * [portable](<https://aur.archlinux.org/packages/portable/>)AUR：简单易用的沙箱化框架，包括 D-Bus 代理过滤、数据隔离、访问控制以及其他功能。

##  使用示例

参阅 [Bubblewrap 示例](<../zh-cn/Bubblewrap/%E7%A4%BA%E4%BE%8B.html> "Bubblewrap/示例")以了解如何使用 bubblewrap。 除此以外，许多项目已证实 bubblewrap 可用于通常应用程序： 

  * [bwscripts](<https://github.com/valoq/bwscripts/>)
  * [StandingPad's Bubblewrap scripts](<https://github.com/StandingPadAnimations/sandboxing-scripts>)

### No-op

无操作调用（No-op invocation）bubblewrap 的示例如下： 
    
    $ bwrap --dev-bind / / bash
    
上述命令会创建一个大多数情况下与沙箱外部表现完全一致的 [Bash](<../zh-cn/Bash.html> "Bash") 进程。如果沙箱化的程序出现异常行为，可以通过上述的无操作调用启动，然后逐步调整至更安全的配置。 

**注意：** 如果执行对象的拥有者（owner）和用户组（group）与执行者不一致，这个操作会把所有的拥有者（owner）和用户组（group）更改为 `nobody`，因此运行某些程序如 `sudo`，将不能正常工作。

### Bash

创建一个简单的 [Bash](<../zh-cn/Bash.html> "Bash") 沙箱： 

  * 确定可用的内核命名空间（kernel namespaces）:

    $ ls /proc/self/ns
    
    cgroup  ipc  mnt  net  pid  user uts
    
**注意：**`user` 的存在意味着内核已经通过 `CONFIG_USER_NS=y` 暴露出对用户命名空间（user namespaces）的支持。

  * 将宿主的整个 `/` 目录以只读模式绑定到沙箱内的 `/`。
  * 创建一个新的用户命名空间（user namespace）并将[用户标识符](<https://en.wikipedia.org/wiki/User_identifier> "wikipedia:User identifier")设为 `256`，[用户组标识符](<https://en.wikipedia.org/wiki/Group_identifier> "wikipedia:Group identifier")设为 `512`。

    $ bwrap --ro-bind / / --unshare-user --uid 256 --gid 512 bash
    
    bash-4.4$ id
    uid=256 gid=512 groups=512,65534(nobody)
    bash-4.4$ ls -l /usr/bin/bash
    -rwxr-xr-x 1 nobody nobody 811752 2017-01-01 04:20 /usr/bin/bash

###  桌面项

在[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")中使用 bubblewrap： 

  * 将宿主的整个 `/` 目录以读写模式绑定到沙箱内的 `/`。
  * 将沙箱内的 `/var` 和 `/etc` 目录重新以只读模式绑定。
  * 挂载一个新的 devtmpfs 文件系统到沙箱内的 `/dev`。
  * 在沙箱化的 `/run` 目录中创建一个 tmpfs 文件系统。
  * 创建一个新的网络命名空间（network namespace）以禁用网络访问。

    [Desktop Entry]
    Name=nano Editor
    Exec=bwrap --bind / / --ro-bind /var /var --ro-bind /etc /etc --dev /dev --tmpfs /run --unshare-net st -e nano -o . %f
    Type=Application
    MimeType=text/plain;
    
**注意：** 为写入到 `/dev/pty`，`--dev /dev`是必需的。

  * MuPDF 的桌面项示例（配合一个 `mupdf.sh` 的 shell 包装器）：

    [Desktop Entry]
    Name=MuPDF
    Exec=mupdf.sh %f
    Icon=application-pdf.svg
    Type=Application
    MimeType=application/pdf;application/x-pdf;
    
**注意：** 请确保 `mupdf.sh` 位于 PATH 中，例如 `PATH=$PATH:$HOME/bwrap`

###  隔离文件系统

**警告：** Bubblewrap 用户需自行负责定期更新文件系统树。

要进一步隐藏文件系统的内容（例如 `/var`、`/usr/bin` 和 `/usr/lib` 中的文件），甚至是用沙箱保护软件的安装，pacman 可以将软件包安装到隔离的文件系统中。 

为能让 pacman 将软件安装到文件系统树中，需要先安装 [fakeroot](<https://archlinux.org/packages/?name=fakeroot>)包 和 [fakechroot](<https://archlinux.org/packages/?name=fakechroot>)包。 

假设用户想用 pacman 将 `xterm` 软件包安装到一个隔离的文件系统树中，用户应该先准备好文件系统树，就像下面的示例那样： 
    
    $ MYPACKAGE=xterm
    $ mkdir -p ~/sandboxes/${MYPACKAGE}/files/var/lib/pacman
    $ mkdir -p ~/sandboxes/${MYPACKAGE}/files/etc
    $ cp /etc/pacman.conf ~/sandboxes/${MYPACKAGE}/files/etc/pacman.conf
    
可能需要编辑 `~/sandboxes/${MYPACKAGE}/files/etc/pacman.conf` 并调整 pacman 的配置文件： 

  * 移除任何不需要的自定义仓库以及仅被宿主系统需要的 `IgnorePkg`、`IgnoreGroup`、`NoUpgrade` 和 `NoExtract` 设置。
  * 可能需要移除 `CheckSpace` 选项，这样 pacman 就不会在检查磁盘空间的时候抱怨找不到根文件系统。

然后将 `base` 包组和 fakeroot 安装到隔离的文件系统树中： 
    
    $ fakechroot fakeroot pacman -Syu \
        --root ~/sandboxes/${MYPACKAGE}/files \
        --dbpath ~/sandboxes/${MYPACKAGE}/files/var/lib/pacman \
        --config ~/sandboxes/${MYPACKAGE}/files/etc/pacman.conf \
        base fakeroot
    
因为接下来要以相同的选项重复调用 bubblewrap，可以设置一个别名（alias）： 
    
    $ alias bw-install='bwrap                        \
         --bind ~/sandboxes/${MYPACKAGE}/files/ /    \
         --ro-bind /etc/resolv.conf /etc/resolv.conf \
         --tmpfs /tmp                                \
         --proc /proc                                \
         --dev /dev                                  \
         --chdir /                                   '
    
[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `~/sandboxes/${MYPACKAGE}/files/etc/locale.gen` 并运行下面的命令以设置 [locale](<../zh-cn/Locale.html> "Locale")： 
    
    $ bw-install locale-gen
    
然后设置 pacman 的 keyring： 
    
    $ bw-install fakeroot pacman-key --init
    $ bw-install fakeroot pacman-key --populate
    
现在就可以安装所需的 `xterm` 软件包了： 
    
    $ bw-install fakeroot pacman -S ${MYPACKAGE}
    
如果 pacman 在这一步执行失败，尝试再次运行用于 populate keyring 的命令。 

成功后，用户现在拥有一个包含 `xterm` 的隔离的文件系统树。之后可以再次使用 `bw-install`（上面的例子中配置好的别名）来更新文件系统树。 

接下来就可以使用 bubblewrap 来运行软件了。本例中的 `_command_` 应该替换成 `xterm`。 
    
    $ bwrap                                          \
         --ro-bind ~/sandboxes/${MYPACKAGE}/files/ / \
         --ro-bind /etc/resolv.conf /etc/resolv.conf \
         --tmpfs /tmp                                \
         --proc /proc                                \
         --dev /dev                                  \
         --chdir /                                   \
         _command_
    
注意，一些文件会在软件包中共享。用户可以将一个已存在的父文件系统树中的所有文件硬链接到一个新的文件系统树中来重用这些文件： 
    
    $ cp -al ~/sandboxes/${MYPARENTPACKAGE} ~/sandboxes/${MYPACKAGE}
    
然后像平时那样从 `bw-install fakechroot fakeroot pacman ...` 开始调用 pacman 进行安装。 

##  疑难解答

###  使用 X11

绑定挂载宿主的 X11 socket 到另一个 X11 socket 可能无法工作： 
    
    --bind /tmp/.X11-unix/X0 /tmp/.X11-unix/X8 --setenv DISPLAY :8
    
一种解决方法是将宿主的 X11 socket 绑定挂载到沙箱中的同一个 socket： 
    
    --bind /tmp/.X11-unix/X0 /tmp/.X11-unix/X0 --setenv DISPLAY :0
    
###  沙箱化 X11

虽然 bwrap 为沙箱化的应用程序提供了一些非常不错的隔离功能，但对于应用程序来说，只要能访问 X11 socket，就仍然有能够逃离沙箱隔离的方法。 

X11 下的应用程序之间没有互相隔离，这会让恶意软件能够监听输入、注入按键或记录其他应用程序的图像。 

一种应对方式是换用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 混成器，该混成器不能从沙箱中访问 X 服务。Wayland 实现了不允许应用程序交互的特性。 

而如果要继续使用 X11，应该使用 [xpra](</wzh/index.php?title=Xpra&action=edit&redlink=1> "Xpra（页面不存在）") 或 [xephyr](<../zh-cn/Xephyr.html> "Xephyr")。这些工具能够创建一个次要且仅用于运行被沙箱化的应用程序的 X11 实例，该实例会在用户目前使用的环境中的一个窗口中显示。以这种方式运行的应用程序窗口无法与其自身 X11 实例以外的环境交互。上述方式同样可与 bwrap 共同使用。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：**[Bubblewrap 示例](<../zh-cn/Bubblewrap/%E7%A4%BA%E4%BE%8B.html> "Bubblewrap/示例")中的所有示例都仅仅只是 bind-mount 了 X11 socket。需要一些做了隔离的示例。 (在 [Talk:Bubblewrap](<../zh-cn/Talk:Bubblewrap.html>) 中讨论)

要测试 X11 是否被隔离，运行 `xinput test _id_`（使用 `xinput list` 查找所需的 _id_ ）。 在没有额外隔离的情况下运行 X11 时，上述命令会显示任何能访问 X11 且够抓取键盘输入的其他应用程序，这种情况下恶意软件将能够记录按键。 

###  使用 portals

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[XDG Desktop Portal](<../zh-cn/XDG_Desktop_Portal.html> "XDG Desktop Portal")。**

**附注：** 有独立页面。（在 [Talk:Bubblewrap](<../zh-cn/Talk:Bubblewrap.html>) 中讨论）

**警告：** 这其实是利用一些方法“欺骗”了 `xdg-desktop-portal`，让它认为被沙箱化的程序是一个 Flatpak 程序。再次提醒，运行不受信任的代码永远是危险的，就算是通过 Portals 在沙箱中运行也是。

[通过一些解决方法](<https://github.com/flatpak/xdg-desktop-portal/pull/741#issuecomment-1084218429>)，或许可以利用 [XDG Desktop Portals](<../zh-cn/XDG_Desktop_Portal.html> "XDG Desktop Portal") 来沙箱化一些应用程序。 这么做的优点是，使用文件系统 portals，能够在不给予应用程序对于家目录（home directory）的访问权限的情况下，让应用程序依然可以访问文件。 然而[出于安全原因](<https://github.com/flatpak/xdg-desktop-portal/pull/741#issuecomment-1081909119>)，使用 portals 需要欺骗 `xdg-desktop-portal`，让它认为被沙箱化的程序是 Flatpak 的一部分。这可以通过在沙箱的根文件系统中添加一个 `.flatpak-info` 文件来实现。 

此外，用户还应该运行 `xdg-dbus-proxy` 以更好地颗粒化控制 portals 的访问权限。此命令应该在沙箱环境下运行，因此也需要一个 `.flatpak-info` 文件。但 proxy 至少需要能够有 `org.freedesktop.portal.Flatpak` 的 talk 访问权限。更多 portals 请访问 [Flatpak 文档](<https://docs.flatpak.org/en/latest/portal-api-reference.html>)。 

常见的案例是允许一个被完全限制 home 目录访问权限的程序仅仅能够访问用户在文件选择器中选择的文件和目录。用以下参数启动 `xdg-dbus-proxy` 可以实现这个目的： 
    
    --talk=org.freedesktop.portal.Documents
    --talk=org.freedesktop.portal.Flatpak
    --talk=org.freedesktop.portal.Desktop
    --talk=org.freedesktop.portal.FileChooser
    
完整示例如下： 
    
    APP_NAME=app.application.Name
    APP_FOLDER="$XDG_RUNTIME_DIR/app/$APP_NAME"
    mkdir -p "$APP_FOLDER"
    set_up_dbus_proxy() {
     bwrap \
       --new-session \
       --symlink /usr/lib64 /lib64 \
       --ro-bind /usr/lib /usr/lib \
       --ro-bind /usr/lib64 /usr/lib64 \
       --ro-bind /usr/bin /usr/bin \
       --bind "$XDG_RUNTIME_DIR" "$XDG_RUNTIME_DIR" \
       --ro-bind-data 3 "/.flatpak-info" \
       --die-with-parent \
       -- \
       env -i xdg-dbus-proxy \
       "$DBUS_SESSION_BUS_ADDRESS" \
       "$APP_FOLDER/bus" \
       --filter \
       --log \
       --talk=org.freedesktop.portal.Flatpak \
       --call="org.freedesktop.portal.Desktop=org.freedesktop.portal.Settings.Read@/org/freedesktop/portal/desktop" \
       --broadcast="org.freedesktop.portal.Desktop=org.freedesktop.portal.Settings.SettingChanged@/org/freedesktop/portal/desktop" 3<<EOF
    [Application]
    name=$APP_NAME
    EOF
    }
    
    set_up_dbus_proxy &
    sleep 0.1
    
    bwrap \
      ...
      --ro-bind-data 3 /.flatpak-info \
      ...
      3<<EOF
    [Application]
    name=$APP_NAME
    EOF
    
###  从被隔离的（wrapped）应用中打开 URL

当被隔离的 IRC 或电子邮件客户端尝试打开一个 URL，通常会尝试启动一个浏览器进程，而被启动的浏览器进程会与被隔离的应用程序一样运行在同一个沙箱中，而一个被良好隔离的应用程序很有可能没法正常工作。[Firejail](<../zh-cn/Firejail.html> "Firejail") 所用的处理方式是[给予被隔离的应用程序所有浏览器也拥有的权限](<https://github.com/netblue30/firejail/blob/b1479a3730a361221c271226cc56d0724ee109c4/etc/thunderbird.profile#L31-L33>)，然而这也意味着分配大量的权限。 

对于这个问题，更好的解决方法是将打开 URL 的请求发送到沙箱外。参照下列示例使用 `snapd-xdg-open`： 

  1. 安装 [snapd-xdg-open-git](<https://aur.archlinux.org/packages/snapd-xdg-open-git/>)AUR
  2. 在 `bwrap` 命令行中添加：

    $ bwrap ... \
      --ro-bind /run/user/$UID/bus /run/user/$UID/bus \
      --ro-bind /usr/lib/snapd-xdg-open/xdg-open /usr/bin/xdg-open \
      --ro-bind /usr/lib/snapd-xdg-open/xdg-open /usr/bin/chromium \
      ...
    
对于不使用 XDG 惯例的应用程序而言，绑定 `/usr/bin/chromium` 是必需的，比如 Mozilla Thunderbird。 

### New session

一个关于 TIOCSTI 的安全问题（CVE-2017-5226）会引起沙箱逃逸。 为防止这个问题，bubblewrap 已引入一个新选项“--new-session”，该选项会调用 setsid()。 然而，这个选项在一些情况下会引起行为问题（behavioural issues）从而难以使用。 例如，这个选项会让 shell 的作业控制（job control）无法应用于 bwrap 命令。 

如果应用程序开发人员有其他方式解决上述漏洞（CVE-2017-5226），可以不用这个选项（比如 [Flatpak 所处理的用于 SECCOMP 的方式](<https://github.com/flatpak/flatpak/commit/902fb713990a8f968ea4350c7c2a27ff46f1a6c4>)），但除此以外建议尽量使用“--new-session”选项。 

###  嵌套的命名空间

特定应用程序如 [Chromium](<../zh-cn/Chromium.html> "Chromium") 已经使用 suid 帮助文件实现了其自身的沙箱环境。这个机制会在以 bubblewrap 容器中运行这些软件时被阻止。 

一种解决方法是让应用程序使用 bubblewrap 创建的命名空间。比如可以使用 [zypak](<https://aur.archlinux.org/packages/zypak/>)AUR，同时它也是 Flatpak 所使用的方式，用于在额外的命名空间中运行基于 electron 的应用程序。[这个链接](<https://github.com/valoq/bwscripts/blob/master/profiles/signal-desktop>)中有关于如何使用 zypak 运行 Chromium 或 [Electron](</wzh/index.php?title=Electron&action=edit&redlink=1> "Electron（页面不存在）") 的示例代码。 

###  没有声音输出

对于直接使用 [ALSA](<../zh-cn/ALSA.html> "ALSA") 声音系统的程序，如果没有声音输出，请添加如下选项： 
    
    --dev-bind /dev/snd /dev/snd
    
即可获得声音输出。 

##  另请参见

  * [GitHub repository](<https://github.com/containers/bubblewrap>)
  * [Seccomp BPF (SECure COMPuting with filters)](<https://docs.kernel.org/userspace-api/seccomp_filter.html>)
  * [Additional bubblewrap examples](<https://github.com/valoq/bwscripts>)
