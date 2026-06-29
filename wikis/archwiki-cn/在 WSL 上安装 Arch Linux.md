**翻译状态：**

  * 本文（或部分内容）译自 [Install Arch Linux on WSL](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_WSL> "arch:Install Arch Linux on WSL")，最近一次同步于 2025-08-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_WSL?diff=0&oldid=844836>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_WSL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

作为 [archlinux-wsl](<https://gitlab.archlinux.org/archlinux/archlinux-wsl>) 项目的一部分，Arch Linux 提供官方 [WSL（Windows Subsystem for Linux，适用于 Linux 的 Windows 子系统）](<https://learn.microsoft.com/en-us/windows/wsl/about>)镜像。 

镜像每月构建并发布一次，旨在通过最简且完整的系统在 WSL 上提供完整的 Arch Linux 体验。 

**注意：** 需要 **WSL 2** 。**不支持** WSL 1。以下内容均假定您使用最新稳定版的 WSL 2。

##  安装

###  安装 WSL

在 UEFI 设置中[启用虚拟化](<https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1>)，然后从 Microsoft Store [安装](<https://learn.microsoft.com/en-us/windows/wsl/install>) **Windows Subsystem for Linux（适用于 Linux 的 Windows 子系统）** 。 

**注意：** Microsoft Store 内的 WSL 是[默认版本](<https://devblogs.microsoft.com/commandline/the-windows-subsystem-for-linux-in-the-microsoft-store-is-now-generally-available-on-windows-10-and-11/>)。不要启用 "Windows Subsystem for Linux" 组件，也不要安装 WSL 内核或 WSLg 的 MSI 安装包，因为它们不再被需要。相比于 Windows 组件，使用 [Microsoft Store 版本](<https://aka.ms/wslstorepage>)的 WSL 可让您[更快地获取更新](<https://devblogs.microsoft.com/commandline/a-preview-of-wsl-in-the-microsoft-store-is-now-available/>)，[WSLg](<https://aka.ms/wslg>) 现也已被打包。

###  更新 WSL

要更新到最新稳定版的 WSL 和 WSLg，在具有管理员权限的 Windows 的命令行 Shell 中执行以下命令： 
    
    > wsl --update
    
要更新到最新的预发行版本，请换用以下命令： 
    
    > wsl --update --pre-release
    
###  在 WSL 上安装 Arch Linux

在[已安装了 WSL 2](<https://learn.microsoft.com/en-us/windows/wsl/install>) 的 Windows 系统上遵循以下安装方式之一： 

####  自动安装

在 Windows 的命令行 Shell 中执行该命令： 
    
    > wsl --install archlinux
    
然后您可以在开始菜单中通过 `archlinux` 应用程序在 WSL 中运行 Arch Linux，亦可在 Windows 的命令行 Shell 中执行 `wsl -d archlinux`。 

如果您不希望使用 WSL 的默认安装路径和发行版名称，可以使用以下命令： 
    
    > wsl --install -d archlinux --name _自定义名称_ --location _自定义路径_
    
其中 `--name` 用于设置名称，`--location` 用于设置安装路径，例如： 
    
    > wsl --install -d archlinux --name Arrrrch --location D:\WSLOS\Arch
    
执行 `wsl --help` 命令以查看 WSL 的更多操作。 

####  手动安装

下载[最新的 Arch Linux `.wsl` 镜像](<https://geo.mirror.pkgbuild.com/wsl/latest/archlinux.wsl>)，然后双击以进行安装或在 Windows 的命令行 Shell 中执行以下命令： 
    
    > wsl --install --from-file _WSL_image_
    
直接安装： 
    
    > wsl --install --from-file C:\Users\_用户名_ \Downloads\archlinux-2025.04.01.121271.wsl
    
导入式安装（可自定义位置）： 
    
    > wsl --import archlinux D:\WSL\Arch D:\Download\archlinux-2025.04.01.121271.wsl
    
**提示：** 这会以默认发行版名称 `archlinux` 安装 WSL 镜像，若您欲以不同名称导入，请添加 `--name _名称_` 选项。

然后您可以在开始菜单中通过 `archlinux` 应用程序在 WSL 中运行 Arch Linux，亦可在 Windows 的命令行 Shell 中执行 `wsl -d archlinux`。 

##  提示和技巧

###  设定默认用户

要设定 `root` 以外的默认用户，首先[确保该用户已被创建](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%B7%BB%E5%8A%A0%E7%99%BB%E5%BD%95%E7%94%A8%E6%88%B7> "用户和用户组")，然后将以下行添加到 `/etc/wsl.conf`： 
    
    [user]
    default=_username_
    
关闭会话前记得为 `root` 用户设置密码，如果您被“拒之门外”，请在 Windows 主机的 CMD 中执行： 
    
    > wsl -u root
    
此更改将在下次会话启动时生效，要终止当前会话，请在 Windows 的命令行 Shell 中执行以下命令： 
    
    > wsl --terminate archlinux
    
若您使用 WSL 2.4.10 或更新版本，则可以使用以下命令为您的发行版设定默认用户： 
    
    > wsl --manage archlinux --set-default-user _用户名_
    
此更改将在下次启动时生效。 

###  用 WSLg 运行图形界面应用程序

[WSLg（Windows Subsystem for Linux GUI）](<https://github.com/microsoft/wslg>)项目致力于[让 WSL 支持 Linux 音频（PulseAudio）和图形界面（X11 和 Wayland）](<https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps>)。 

WSLg 默认启用，您可在 [WSL 配置文件](<https://learn.microsoft.com/en-us/windows/wsl/wsl-config>)中将 `wsl2.guiApplications` 设为 `false` 以将其关闭。 

####  硬件加速渲染

欲在 WSL 中启用 [GPU 视频加速渲染](<https://devblogs.microsoft.com/commandline/d3d12-gpu-video-acceleration-in-the-windows-subsystem-for-linux-now-available/>)，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")以下软件包： 

  * [mesa](<https://archlinux.org/packages/?name=mesa>)包 \- 包含 OpenGL 所需的 `d3d12` Gallium 驱动
  * [vulkan-dzn](<https://archlinux.org/packages/?name=vulkan-dzn>)包 \- 包含实验性的 `dzn`（亦作 `microsoft-experimental`）Vulkan 驱动

还需要安装 [vulkan-icd-loader](<https://archlinux.org/packages/?name=vulkan-icd-loader>)包（要运行 32 位应用程序则亦需安装 [lib32-vulkan-icd-loader](<https://archlinux.org/packages/?name=lib32-vulkan-icd-loader>)包）。 
    
    ~/.bashrc
    
    export GALLIUM_DRIVER=d3d12
    	
    export LIBVA_DRIVER_NAME=d3d12
    	
若 openGL 依然在英特尔 GPU 上使用 llvmpipe 软件渲染，则需要为 libedit 创建符号链接： 
    
    # ln -s /usr/lib/libedit.so /usr/lib/libedit.so.2
    
更多信息参见 [Issue 996](<https://github.com/microsoft/wslg/issues/996>) 和 [Gentoo:Gentoo in WSL#OpenGL falling back to llvmpipe software renderer on Intel GPUs](<https://wiki.gentoo.org/wiki/Gentoo_in_WSL#OpenGL_falling_back_to_llvmpipe_software_renderer_on_Intel_GPUs> "gentoo:Gentoo in WSL")。 

###  WSL 互操作

WSL 支持[与 Windows 互操作](<https://github.com/ubuntu/WSL/blob/main/docs/tutorials/interop.md>)，这让您可以从 WSL 运行 Windows 二进制程序。 

其默认启用，您可在 `/etc/wsl.conf` 中将 `interop.enabled` 设定为 `false` 以将其禁用[[1]](<https://learn.microsoft.com/en-us/windows/wsl/wsl-config#interop-settings>)。 

有一些工具能让您在 WSL 内使用 Windows 服务和功能。 

####  从 Windows 桥接 SSH 代理服务

[wsl2-ssh-agent](<https://github.com/mame/wsl2-ssh-agent>) 工具允许您在 WSL 内使用 Windows [SSH 代理](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html#SSH_%E4%BB%A3%E7%90%86> "SSH 密钥")。 

当您使用需要物理安全密钥甚至是 [Windows Hello](<https://www.microsoft.com/windows/tips/windows-hello>) 的 `*-sk` SSH 密钥时，这会很有用。 

安装 [wsl2-ssh-agent](<https://aur.archlinux.org/packages/wsl2-ssh-agent/>)AUR 并将以下行添加到您的 `~/.bashrc`： 
    
    eval "$(/usr/sbin/wsl2-ssh-agent)"
    
重启 shell，`SSH_AUTH_SOCK` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")应该已正确设置。 

####  使用 Windows Hello 进行 PAM 认证

[WSL-Hello-Sudo](<https://github.com/nullpo-head/WSL-Hello-sudo>) 是一个使用 [Windows Hello](<https://www.microsoft.com/windows/tips/windows-hello>) 进行用户身份认证的 [PAM](<../zh-cn/PAM.html> "PAM") 插件。 

安装 [wsl-hello-sudo-bin](<https://aur.archlinux.org/packages/wsl-hello-sudo-bin/>)AUR 并运行 `/opt/wsl-hello-sudo/install.sh`。安装程序会复制一个 Windows 可执行程序到您选定的目录并存储用于身份认证的证书。 

**提示：**[WSL-Hello-Sudo](<https://github.com/nullpo-head/WSL-Hello-sudo>) 已经 4 年没有更新了，因此 [wsl-hello-sudo-bin](<https://aur.archlinux.org/packages/wsl-hello-sudo-bin/>)AUR 打包了一个[分支](<https://github.com/lzlrd/wsl-hello-sudo>)，合并了一些依赖更新。

欲使用 Windows Hello 进行认证，将 `auth sufficient pam_wsl_hello.so` 行添加到 `/etc/pam.d` 中相应组件的配置文件，例如 Sudo： 
    
    /etc/pam.d/sudo
    
    #%PAM-1.0
    auth            sufficient      pam_wsl_hello.so
    auth            include         system-auth
    account         include         system-auth
    session         include         system-auth
    
###  向 WSL 连接设备

WSL 2 是一个 [Hyper-V](</wzh/index.php?title=Hyper-V&action=edit&redlink=1> "Hyper-V（页面不存在）") 虚拟机，这使得设备可以从主机（Windows）直连到客户机（WSL 2）。 

####  挂载磁盘

WSL 2 支持附加并挂载 Windows 可用的磁盘。 

欲如此做，首先请用以下 PowerShell 命令获取磁盘的 `DeviceID`： 
    
    > GET-CimInstance -query "SELECT * from Win32_DiskDrive"
    
找到欲挂载的磁盘后，请在 Windows 上执行以下命令（需要管理员权限）： 
    
    > wsl --mount _DeviceID_ --bare
    
**警告：** 这会使相应磁盘在 Windows 上下线，挂载前确保您已关闭所有正在使用该驱动器的应用程序。

附加后，您应当可以用 `lsblk` 看到该磁盘。 

要取消挂载，请运行： 
    
    > wsl --unmount _DeviceID_
    
欲获取更多信息，请参阅[官方文档](<https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk>)（中文文档[在此](<https://learn.microsoft.com/zh-cn/windows/wsl/wsl2-mount-disk>)）。 

####  连接 USB 设备

[usbipd-win](<https://github.com/dorssel/usbipd-win>) 项目可以将本地连接的 USB 共享到其他设备，包括 WSL 2。 

首先请在 Windows 上安装该软件。您可以选择运行[最新发布](<https://github.com/dorssel/usbipd-win/releases/latest>)的安装程序（ _.msi_ ）或使用 [Windows 包管理器](<https://learn.microsoft.com/en-us/windows/package-manager/winget/>)： 
    
    > winget install usbipd
    
安装完成后，请在 Windows 上执行以下命令，找到欲共享的 USB 设备，特别留意其 bus ID： 
    
    > usbipd list
    
执行以下命令以准备欲共享的 USB 设备（需要管理员权限）： 
    
    > usbipd bind --busid _busid_
    
**警告：** 确保您已关闭了所有使用该 USB 设备的应用程序。

然后执行以下命令将 USB 设备连接到 WSL 2： 
    
    > usbipd attach --wsl --busid _busid_
    
连接后，您应当可以用 `lsusb` 看到该设备。 

要与 USB 设备断开连接，请执行： 
    
    > usbipd detach --busid _busid_
    
欲获取更多信息，请参阅[官方文档](<https://learn.microsoft.com/en-us/windows/wsl/connect-usb>)。 

###  修改区域设置

WSL 默认会尝试将区域设置调整为与 Windows 相匹配。欲手动设置，请执行以下命令： 
    
    ln -sf /etc/locale.conf /etc/default/locale
    
然后像正常安装一样[设定区域](<../zh-cn/Locale.html> "Locale")。 

##  疑难解答

###  systemd 支持

Arch Linux WSL 镜像支持 [systemd](<../zh-cn/Systemd.html> "Systemd")。 

然而，有一些[已知问题](<https://gitlab.archlinux.org/archlinux/archlinux-wsl#known-issues>)可能需要额外操作才能使 systemd 正常工作。 

###  Docker 容器运行出错

从 WSL 运行 [Docker](<../zh-cn/Docker.html> "Docker") 容器可能会出现如下报错： 
    
    Error response from daemon: path / is mounted on / but it is not a shared or slave mount
    Error: failed to start containers
    
有可能是 `docker run` 之类的命令一直挂起而不输出。 

因为 Docker 需要根目录（`/`）被挂载为可共享。 

欲修复，请运行： 
    
    # mount --make-rshared /
    
欲持久化该更改，您可以[创建一个 systemd 服务](<https://github.com/microsoft/WSL/issues/11715#issuecomment-2798498272>)，使其在启动时就执行命令： 
    
    /etc/systemd/system/mount-root-rshared.service
    
    [Unit]
    Description=Remount / with shared propagation
    Requires=-.mount
    After=-.mount
    
    [Service]
    Type=oneshot
    ExecStart=/bin/mount --make-rshared /
    
    [Install]
    WantedBy=local-fs.target

然后[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `mount-root-rshared.service`。 

关于该选项的更多信息，请参阅 [mount(8) § Shared subtree operations](<https://man.archlinux.org/man/mount.8#Shared_subtree_operations>)。 

##  参见

  * [Wikipedia:Windows Subsystem for Linux](<https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux> "wikipedia:Windows Subsystem for Linux")
  * [Gentoo:Gentoo in WSL](<https://wiki.gentoo.org/wiki/Gentoo_in_WSL> "gentoo:Gentoo in WSL")
  * [官方文档（英文）](<https://learn.microsoft.com/en-us/windows/wsl>)
  * [官方文档（中文）](<https://learn.microsoft.com/zh-cn/windows/wsl>)
  * [WSLg GitHub Wiki](<https://github.com/microsoft/WSLg/wiki>)
