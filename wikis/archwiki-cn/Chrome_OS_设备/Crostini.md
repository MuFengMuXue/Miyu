[Crostini](<https://chromium.googlesource.com/chromiumos/docs/+/master/containers_and_vms.md>) 是Google的总括术语，用于表示“使 Linux 应用程序易于使用，并与 ChromeOS 良好集成”。 

本文讲述了如何通过 Crostini 在 Chromebook 上的容器内安装 Arch Linux ，而无需启用开发者模式，使得应用程序与其他 Chrome/Android 应用程序能够一起运行。 

亮点： 

  * 官方支持，无需启用开发者模式- 让 ChromeOS 更安全、无需刷 BIOS 等。
  * 更长的电池寿命-享受 Chrome 的电池寿命的同时享用 Linux 功能。
  * 支持音频和 OpenGL，但对麦克风和 USB 设备的支持仍在跟进中。

##  介绍

###  启用 Linux 支持

在“设置”下查找 "Linux" 并启用。 这将安装一个 Debian Linux 容器，然后将其替换为 Arch Linux 容器。 

    “设置 > Linux（测试版） > 启用“

Crostini 仍在向 Chromebook 推广。 如果您没有看到启用 Linux 的选项，则可能需要切换到 Beta （测试）或 Developer （开发）频道（如果尚未将其部署到笔记本电脑的稳定频道中）。 通过“设置>关于 ChromeOS>频道>Dev/Beta”来完成。 

###  用Arch Linux替换默认的Debian Linux容器

以下说明基于 <https://www.reddit.com/r/Crostini/wiki/howto/run-arch-linux>

0\. 删除Debian容器（可选） 

如果您有没有用Debian了，你可以通过停止并重新创建termina虚拟机节省一定的存储空间（这是做的最简单的方法，简单地破坏与容器` lxc destroy penguin`会留下未使用空间）。 请注意，这还将删除您可能在终端下拥有的任何其他容器。 
    
    vmc destroy termina
    vmc start termina
    
1\. 安装Arch Linux容器 

**提示：** 在中国大陆有[山大镜像](<https://mirrors.sdu.edu.cn/help/lxc-images>)可选。

在Chrome中打开一个新的终端（Ctrl + Alt + T）。 然后连接到终端并创建一个Arch Linux容器： 
    
    vmc container termina arch <https://us.lxd.images.canonical.com/> archlinux/current
    
完成后将显示以下错误： 
    
    "Error: routine at frontends/vmc.rs:403 `container_setup_user(vm_name,user_id_hash,container_name,username)` failed: timeout while waiting for signal"
    
这是预期的行为，请继续以下步骤。 

2\. 连接到termina vm并检查是否存在arch容器（可能需要几分钟才能显示在列表中）: 
    
    vsh termina
    lxc list
    
3\. 在arch容器上启动bash shell： 
    
    lxc exec arch -- bash
    
4\. 根据您在容器上的gmail用户名，为默认用户设置密码。 默认情况下，gmail用户未设置密码，因此我们需要进行设置： 
    
    passwd $(grep 1000:1000 /etc/passwd|cut -d':' -f1)
    
您可能还需要添加[sudo](<../../zh-cn/Sudo.html> "Sudo")并将用户添加到wheel组。 
    
    pacman -S sudo
    visudo
    
**提示：** 因为众所周知的原因，在中国可能需要换源才能安装成功。 取消/etc/pacman.d/mirrorlist.pacnew文件中China源的注释，大概在80+行

取消注释此行： 
    
    # %wheel ALL=(ALL) ALL
    
将您的用户添加到wheel组以允许sudo命令 
    
    usermod -aG wheel $(grep 1000:1000 /etc/passwd|cut -d':' -f1)
    
退出容器： 
    
    exit
    
5\. 使用刚刚配置的普通用户帐户登录到容器： 
    
    lxc console arch
    
6\. 验证容器中的网络。 命令 
    
    ip -4 a show dev eth0
    
应该返回分配了IP地址的非空输出。 如果不为空，请继续执行步骤7，否则，您将面临[#容器中没有网络](<#%E5%AE%B9%E5%99%A8%E4%B8%AD%E6%B2%A1%E6%9C%89%E7%BD%91%E7%BB%9C>)故障排除部分中描述的问题-请按照此处列出的说明解决该问题。 

7\. 安装Crostini容器工具，用于GUI应用程序的Wayland，用于X11应用程序的XWayland。 

安装[cros-container-guest-tools-git](<https://aur.archlinux.org/packages/cros-container-guest-tools-git/>)AUR包. 另外，安装 [wayland](<https://archlinux.org/packages/?name=wayland>)包和 [xorg-xwayland](<https://archlinux.org/packages/?name=xorg-xwayland>)包才能使用GUI工具。 

**注意：** 如果安装时提示如下error可以执行 `sudo pacman -S base-devel` 安装基本打包工具 

==> ERROR: Cannot find the strip binary required for object file stripping. 

Error downloading sources: cros-container-guest-tools-git

8\. 启用并启动服务（针对Wayland GUI、X11 GUI、Wayland GUI低密度和X11 GUI低密度）： 
    
    $ systemctl --user enable sommelier@0
    $ systemctl --user enable sommelier-x@0
    $ systemctl --user enable sommelier@1
    $ systemctl --user enable sommelier-x@1
    $ systemctl --user start sommelier@0
    $ systemctl --user start sommelier-x@0
    $ systemctl --user start sommelier@1
    $ systemctl --user start sommelier-x@1
    
运行以下命令，确保这些服务运行成功： 
    
    systemctl --user status sommelier@0
    systemctl --user status sommelier@1
    systemctl --user status sommelier-x@0
    systemctl --user status sommelier-x@1
    
现在，在Arch Linux中安装应用程序后，它们会自动显示并可以从ChromeOS启动。 

9\. 将默认的Debian容器替换为Arch Linux。 

Exit from the container shell back to the termina shell pressing **< ctrl>+a q** (or just close existing and open new termina shell as shown in step 2). The default Debian container is named penguin. Renaming the "arch" container created above to it will cause chrome to launch Linux apps from the arch container. Skip the third line if you have already removed the Debian container. 

按下**< ctrl>+a q**（或如步骤2所示，仅关闭现有容器并打开新的termina外壳），从容器外壳退出并回到termina外壳。 默认的Debian容器名为penguin。 将上面创建的“ arch”容器重命名为它会导致chrome从arch容器启动Linux应用。 如果您已经删除了Debian容器，请跳过第三行。 
    
    lxc stop --force arch
    lxc stop --force penguin
    lxc rename penguin debian
    lxc rename arch penguin
    lxc start penguin
    
10\. 重新启动Linux子系统以应用更改。 在容器shell内重新启动后 
    
    systemctl --failed
    systemctl --user --failed
    
应同时报告“0已加载的单位列表”和 
    
    ip -4 a show dev eth0
    
应该报告分配给容器的IP地址 

##  疑难解答

###  容器中无网络

据多方报告，systemd-244.1 的 systemd-networkd 和 systemd-resolved 服务在无特权的 LXC 容器上不能正常工作，导致 Crostini 容器无网络。推荐的解决方案是完全禁用以上两个服务，改为使用 [dhclient](</wzh/index.php?title=Dhclient&action=edit&redlink=1> "Dhclient（页面不存在）") 服务进行网络配置： 
    
    sudo dhcpcd eth0
    sudo pacman -S dhclient
    sudo systemctl disable systemd-networkd
    sudo systemctl disable systemd-resolved
    sudo unlink /etc/resolv.conf
    sudo touch /etc/resolv.conf
    sudo systemctl enable dhclient@eth0
    sudo systemctl start dhclient@eth0
    
如果您相比建议的解决方案更喜欢 [NetworkManager](<../../zh-cn/NetworkManager.html> "NetworkManager") 和 [dhcpcd](<../../zh-cn/Dhcpcd.html> "Dhcpcd")，也可以用来解决该问题。 

###  应用无法在Chrome OS（无限转圈）中打开

我发现启动控制台（lxc console penguin）会话会阻止应用程序在Chrome操作系统中启动。启动将导致无限转圈。在这种情况下，我必须停止再启动容器以使Chrome操作系统启动程序工作 
    
    lxc stop penguin
    lxc start penguin
    
我没有使用lxc控制台会话，而是使用从ChromeOS启动的常规Linux终端GUI来防止这个问题。 

###  音频播放

Crostini从Chrome OS 74开始支持音频播放。安装了 [cros-container-guest-tools-git](<https://aur.archlinux.org/packages/cros-container-guest-tools-git/>)AUR后，ALSA和PulseAudio播放均应立即可用。 截至2019年8月21日，不支持音频输入。 

###  视频播放

[mpv](<../../zh-cn/Mpv.html> "Mpv")可以使用软件渲染播放视频，而无需任何附加配置，但这对于像H265这样的现代视频编解码器来说，是一种CPU消耗和滞后的体验。对于硬件加速播放，需要GPU加速。考虑到Crostini的GPU加速是基于[3D GPU project](<https://virgil3d.github.io/>)的，因此没有执行真正的GPU设备传递，并且没有VA-API或VPDAU之类的硬件特定API。但是，可以使用OpenGL加速，即这是[mpv]媒体播放器的mpv.conf配置示例，它启用了从Chrome OS 77开始的Google Pixelbook上的加速视频和音频播放： 
    
    vo=gpu
    ao=alsa

###  GPU加速

在谷歌Pixelbook上，GPU加速与Arch开箱即用的Chrome OS 77协同工作。最近发布的ChromeOS也不需要启用任何标志： 
    
    $ glxinfo -B
    
    name of display: :0
    display: :0  screen: 0
    direct rendering: Yes
    Extended renderer info (GLX_MESA_query_renderer):
        Vendor: Red Hat (0x1af4)
        Device: virgl (0x1010)
        Version: 19.1.4
    --> Accelerated: yes <--
        Video memory: 0MB
        Unified memory: no
        Preferred profile: core (0x1)
        Max core profile version: 4.3
        Max compat profile version: 3.1
        Max GLES1 profile version: 1.1
        Max GLES[23] profile version: 3.2
    OpenGL vendor string: Red Hat
    OpenGL renderer string: virgl
    OpenGL core profile version string: 4.3 (Core Profile) Mesa 19.1.4
    OpenGL core profile shading language version string: 4.30
    OpenGL core profile context flags: (none)
    OpenGL core profile profile mask: core profile
    
    OpenGL version string: 3.1 Mesa 19.1.4
    OpenGL shading language version string: 1.40
    OpenGL context flags: (none)
    
    OpenGL ES profile version string: OpenGL ES 3.2 Mesa 19.1.4
    OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.20

###  全屏视频、游戏和鼠标捕捉

目前，Crostini从Chrome OS 79（当前在开发人员通道中）开始对鼠标捕获开始了有限的支持。 您必须启用标记chrome://flags/#exo-pointer-lock 才能捕获鼠标。 与鼠标捕获有关的已关闭问题是https://bugs.chromium.org/p/chromium/issues/detail?id=927521 

##  有用的链接

  1. [Running Custom Containers Under Chrome OS](<https://chromium.googlesource.com/chromiumos/docs/+/master/containers_and_vms.md>)
  2. [/r/Crostini](<https://www.reddit.com/r/Crostini/>)
  3. [Powerline Web Fonts for Chromebook](<https://github.com/wernight/powerline-web-fonts>)
