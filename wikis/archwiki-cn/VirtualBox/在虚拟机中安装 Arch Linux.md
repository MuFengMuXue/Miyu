[![](../../File:Tango-preferences-desktop-locale.png)](<../../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** Partial translation（在 [Talk:VirtualBox/在虚拟机中安装 Arch Linux#](<../../zh-cn/Talk:VirtualBox/%E5%9C%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E5%AE%89%E8%A3%85_Arch_Linux.html>) 中讨论）

相关文章

  * [VirtualBox](<../../zh-cn/VirtualBox.html> "VirtualBox")

本文介绍如何在 [VirtualBox](<../../zh-cn/VirtualBox.html> "VirtualBox") 中安装 Arch linux。 

在虚拟机的虚拟光驱里加载 Arch Linux 的[安装镜像](<https://archlinux.org/download/>)，然后按照[安装指南](<../../zh-cn/Installation_guide.html> "Installation guide")里的步骤继续即可。 

##  安装

###  以 EFI 模式安装（可选）

如果你想在 VirtualBox 里以 EFI 模式安装 Arch Linux，这需要在虚拟机的设置窗口里，先从左侧选择 _System_ ，再从右侧选择 _Motherboard_ 标签页，最后勾选 _Enable EFI (special OSes only)_ 选项。从安装镜像的启动菜单里选好 Arch Linux 的内核之后，这时启动过程要卡顿一两分钟，之后就能正常进入系统，稍安勿躁。 

等系统和[启动引导程序](<../../zh-cn/Boot_loaders.html> "Boot loaders")安装成功之后，VirtualBox 会首先尝试从 [ESP](<../../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "ESP") 加载 `/EFI/BOOT/BOOTX64.EFI`。如果这个首选的文件加载失败，VirtualBox 会从 ESP 根目录尝试加载 EFI shell 脚本 `startup.nsh`。这样来说，为了能顺利进入系统，你需要从下面几种方案选一个： 

  * 每次都从 EFI shell [手动选择启动引导程序](<../../zh-cn/Unified_Extensible_Firmware_Interface.html#UEFI_Shell> "Unified Extensible Firmware Interface")
  * 把启动引导程序的 .EFI 文件移动到默认位置：`/EFI/BOOT/BOOTX64.EFI`
  * 自己编写 ESP 分区的 `/startup.nsh` 脚本，用这个脚本加载想使用的引导程序（例如 `\EFI\grub\grubx64.efi`）
  * 从 ESP 分区的 [startup.nsh 脚本](</wzh/index.php?title=EFISTUB&action=edit&redlink=1> "EFISTUB（页面不存在）")直接启动到 Linux

虽然 VirtualBox 支持按 F2 进入自带的 VirtualBox Boot Manager 来管理 EFI 启动过程，但这部分功能还不完整而且有 bug。它还不能持久保存交互式设置的 EFI 变量。也就是说，开机时按下 F12 之后手动添加的、或者用 [efibootmgr](<https://archlinux.org/packages/?name=efibootmgr>)包 添加的 EFI 项目，重启后依然可以生效，但关机之后就会失效。 

另见：[UEFI VirtualBox installation boot problems](<https://bbs.archlinux.org/viewtopic.php?id=158003>). 

###  安装客体机插件

VirtualBox [客体机插件](<https://www.virtualbox.org/manual/ch04.html>)为客体系统提供了必要的驱动与应用软件，其作用包括改善图像分辨率与鼠标支持等。在客体机的 Arch Linux 系统里： 

  * 若需要支持 X，安装 [virtualbox-guest-utils](<https://archlinux.org/packages/?name=virtualbox-guest-utils>)包
  * 若不需支持 X，安装 [virtualbox-guest-utils-nox](<https://archlinux.org/packages/?name=virtualbox-guest-utils-nox>)包

**注意：**

  * 另一个安装方案是从宿主机（如果也是 Arch 系统）安装 [virtualbox-guest-iso](<https://archlinux.org/packages/?name=virtualbox-guest-iso>)包，这个软件包里有供客体机安装插件的 ISO 文件。装好这个包之后，启动客体机，点击菜单项目 Devices -> Insert Guest Additions CD Image 即可加载安装镜像。
  * 若要手动重新编译客体机的 VirtualBox 内核模块，以 root 权限运行 `rcvboxadd setup` 即可。

客体机里运行的插件和主体机上的 VirtualBox 程序版本需要匹配。否则某些功能（比如剪贴板互通）可能会失效。如果你在客体机里升级系统（比如运行了 `pacman -Syu`），那么宿主机上的 VirtualBox 也要跟进更新到最新版。VirtualBox GUI 菜单里的 "Check for updates" 功能未必够用，可以去官网 [VirtualBox.org](<https://www.virtualbox.org/>) 再看看。 

###  加载 VirtualBox 内核模块

若要开机自动加载模块，[启用](<../../zh-cn/Systemd.html> "Systemd") `vboxservice.service` 服务即可。该服务还能起到将客户机时间与宿主机同步的功能。 

若要手动加载模块，使用这个命令： 
    
    # modprobe -a vboxguest vboxsf vboxvideo
    
###  启动 VirtualBox 客体机服务

安装并加载了 VirtualBox 内核模块之后，如果你在虚拟机系统里使用 [X](<../../zh-cn/Xorg.html> "Xorg")，那么推荐启动这样一个客体机服务：服务的程序名字叫 `VBoxClient`，它与 X 窗口系统沟通来实现其功能。具体功能包括： 

  * 在宿主机与客体机之间互通剪贴板，实现鼠标拖拽文件
  * 无缝窗口模式
  * 宿主机的虚拟机窗口缩放之后，使客体机的显示分辨率与之自动匹配
  * 检查宿主机的 VirtualBox 的版本

上述功能由专门的命令行参数来各自启用： 
    
    $ VBoxClient --clipboard --draganddrop --seamless --display --checkhostversion
    
为了方便，`VBoxClient-all` 这个 shell 脚本能取代上面这一整行命令。 

[virtualbox-guest-utils](<https://archlinux.org/packages/?name=virtualbox-guest-utils>)包 包提供了 XDG 自启动项目 `/etc/xdg/autostart/vboxclient.desktop`，这会在登录 X 时自动运行 `VBoxClient-all`。然而，如果你在用的[桌面环境](<../../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")或[窗口管理器](<../../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")不支持 XDG 自启动，那么你就需要手动配置。详见[自动启动#桌面环境](<../../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83> "自动启动")。 

至此，你的 Arch Linux 应该能在虚拟机里正常运行了。需要指出的是，某些功能（如剪贴板互通）在 VirtualBox 里是默认禁用的。这需要在各个虚拟机的设置选项里手动开启（ _Settings > General > Advanced > Shared Clipboard_）。 

###  显卡加速

从 VirtualBox 选项里可以开启显卡加速。已知 [GDM](<../../zh-cn/GDM.html> "GDM") 显示管理器从 3.16 版本起会导致显卡加速失效。[[1]](<https://bugzilla.gnome.org/show_bug.cgi?id=749390>) 如果你遇到类似问题，可以换另一种显示管理器（比如 [LightDM](<../../zh-cn/LightDM.html> "LightDM")）试试看。[[2]](<https://bbs.archlinux.org/viewtopic.php?id=200025>) [[3]](<https://bbs.archlinux.org/viewtopic.php?pid=1607593#p1607593>)

###  启用共享目录

共享目录的设置在宿主机这边操作。启动 VirtualBox 的图形管理界面，在虚拟机的设置界面的 _Shared Folders_ 标签页可以找到相关设置。可以设置的项目包括：目录在宿主机的位置 _Folder Path_ ，客户机挂载点的名字 _Folder name_ ，还有 _Read-only_ ， _Auto-mount_ , _Make permanent_ 等杂项。还有一种管理方法是使用 `VBoxManage`。详情可以参阅 [VirtualBox 手册](<https://www.virtualbox.org/manual/ch04.html#sharedfolders>)。 

无论用哪一种方法来挂载共享目录，首先都要做些准备工作。 

为了避免出现 `/sbin/mount.vboxsf: mounting failed with the error: No such device` 这种错误，首先要确保 `vboxsf` 内核模块已经加载。只要按照前面的步骤在加载客体机里加载内核模块，这一步应该没问题。 

为了让挂载之后的目录能让 root 之外的用户也直接读写，还要： 

  * 安装 [virtualbox-guest-utils](<https://archlinux.org/packages/?name=virtualbox-guest-utils>)包 软件包时会创建用户组 `vboxsf`（在前面的步骤就装过了）
  * 你的用户需要加入到 `vboxsf` [用户组](<../../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups")

####  手动挂载

在 Arch Linux 客体系统里挂载共享目录的命令是： 
    
    # mount -t vboxsf _< 共享目录的名字>_ _< 客户机系统的挂载点>_
    
这个命令可以查看 vboxsf 的挂载参数： 
    
    # mount.vboxsf
    
假如用户不在 `vboxsf` 组里，用这个命令可以把挂载点的读写权限授权给他： 
    
    # mount -t vboxsf -o uid=1000,gid=1000 home /mnt/
    
其中 _uid_ 和 _gid_ 的值要与接受授权的用户的值相对应。用 `id` 命令可以为该用户找到这两个值。 

####  自动挂载

**注意：** 自动挂载需要启用 `vboxservice` 服务才能生效

为使用自动挂载功能，首先需要在 GUI 的管理界面里勾选自动挂载，或者为命令行工具 `VBoxManage sharedfolder` 加上参数 `--automount`。 

此时，共享目录应该已经在 `/media/sf__< 共享目录的名字>_` 挂载上了。如果用户没有读写权限，确认一下该目录的权限是否是 755。如果是 750 的话，确保该目录属于 `vboxsf` 组。 

可以用软链接把共享目录链接到方便的位置，这样就不必进入那么远的目录了： 
    
    $ ln -s /media/sf__共享目录的名字_ ~/_my_documents_
    
####  按配置于启动时挂载

[fstab](<../../zh-cn/Fstab.html> "Fstab") 可以用来挂载目录。然而，为了避免 Systemd 启动可能带来的问题，要在 `/etc/fstab` 配置里为共享目录加上挂载选项 `noauto,x-systemd.automount`。这样，共享目录会在开机后初次访问时挂载，而不是在系统启动过程里挂载。这可以避免 Systemd 在客体机插件加载之前就按 fstab 挂载目录而导致的出错。 
    
    _sharedFolderName_  _/path/to/mntPtOnGuestMachine_  vboxsf  uid=_user_ ,gid=_group_ ,rw,dmode=700,fmode=600,noauto,x-systemd.automount 
    
  * `_sharedFolderName_`: 在虚拟机设置界面 _Settings > SharedFolders > Edit > FolderName_ 里所设置的值。这个值和宿主机里实际的目录名可以不相同。要查看虚拟机的设置，在宿主机的 VirtualBox GUI 管理界面选中虚拟机，然后点击工具栏的 _Settings_ 按钮，再从弹出的对话框里选择 _Shared Folders_ 。
  * `_/path/to/mntPtOnGuestMachine_`: 如果这个路径在虚拟机里还不存在，那么需要在挂载之前手动创建（用 [mkdir](<../../zh-cn/Core_utilities.html#Essentials> "Core utilities") 就可以）。
  * `dmode`/`fmode` 分别用来指定挂载共享目录之后，下面的子目录与文件的属性。

`mount.vboxsf` 尚不支持 `nofail` 挂载参数： 
    
    _desktop_  _/media/desktop_  vboxsf  uid=_user_ ,gid=_group_ ,rw,dmode=700,fmode=600,nofail  0  0
    
###  从宿主机 SSH 登录客体机

在虚拟机设置的 Network 标签页 -> 右侧打开 Advanced 折叠 -> 单击 Port Forwarding 按钮，可以设置端口。 

假如我们设置了将宿主机的 3022 端口转发到客体机的 22 端口。然后在宿主机执行： 
    
    user@host$ ssh -p 3022 $USER@localhost
    
即可 SSH 登录客体机。 

####  用 SSHFS 来实现共享目录

配置好了端口转发，再装上 [SSHFS](<../../zh-cn/SSHFS.html> "SSHFS")，只要在宿主机运行这个命令就可以把客体机的目录挂载到宿主机： 
    
    user@host$ sshfs -p 3022 $USER@localhost:$HOME ~/shared_folder
    
这样也能实现互传文件。 

##  故障排除

###  访客操作系统中访问串口

请参阅[使用终端仿真器程序连接串口的操作方式](</wzh/index.php?title=%E4%BD%BF%E7%94%A8%E7%BB%88%E7%AB%AF%E4%BB%BF%E7%9C%9F%E5%99%A8%E7%A8%8B%E5%BA%8F%E8%BF%9E%E6%8E%A5%E4%B8%B2%E5%8F%A3%E7%9A%84%E6%93%8D%E4%BD%9C%E6%96%B9%E5%BC%8F&action=edit&redlink=1> "使用终端仿真器程序连接串口的操作方式（页面不存在）"). 

###  安装过程中TTY文本太小

在主机上的VirtualBox管理器中，将显示比例设置为2.00或3.00。 

###  启动 Xorg 之后虚拟机卡死

出现这一问题的原因是驱动程序缺失或有错。例如：[[4]](<https://bbs.archlinux.org/viewtopic.php?pid=1167838>) 或 [[5]](<https://bbs.archlinux.org/viewtopic.php?id=156079>)。试试从菜单项 _Settings > Display_ 里关闭 3D 加速，并确认要用的 [Xorg](<../../zh-cn/Xorg.html> "Xorg") 驱动都已装好。 

###  全屏模式只能看到黑屏

在某些窗口管理器（[i3](<../../zh-cn/I3.html> "I3"), [awesome](<../../zh-cn/Awesome.html> "Awesome")）下运行 VirtualBox 时，由于顶层状态栏（overlay bar）的问题，VirtualBox 的全屏模式会出现问题。试试在菜单项 "Guest Settings > User Interface > Mini ToolBar" 里禁用 "Show in Full-screen/Seamless" 有可能绕过这一问题。详情可见[上游的问题汇报](<https://www.virtualbox.org/ticket/14323>)。 

如果屏幕是在某个大小之后开始黑屏，例如大于 2048 像素宽度时，请尝试增加 _Settings > Display > Screen > Video Memory_。 

###  Linux 客体机的声音缓慢 / 扭曲

在 VirtualBox 里运行时，Linux 内核的 AC97 声卡驱动偶尔会猜错时钟频率设定。这就会造成声音播放速度太慢 / 太快。在 `/etc/modprobe.d` 目录里创建一个内容如下的文件即可解决： 
    
    options snd-intel8x0 ac97_clock=48000
    
###  Linux 宿主机存在音频卡顿/延迟

在某些情况下，音频可能会出现延迟性能问题（例如在在线视频流媒体中音频与视频不同步）。一个可能的解决方法是在VirtualBox中使用Intel HD音频控制器，并通过在客户操作系统的`/etc/modprobe.d/` 目录下的文件中添加以下行来禁用其节能功能： 
    
    options snd_hda_intel power_save=0 power_save_controller=N
    
###  Arch: pacstrap 脚本出错

如果在安装 Arch 系统时，**还没有** 启动至新安装到虚拟盘的系统，就用 `pactrap` 直接安装客体机插件，需要以 root 身份运行一次 `umount -l /mnt/dev` 然后再次运行 `pactrap`。否则新装的系统就不可用。 

###  Windows 宿主机: VERR_ACCESS_DENIED

为了能在 Windows 宿主机上读取 RAW 格式的 VMDK 镜像，VirtualBox GUI 需要以管理员权限启动。 

###  在Arch Linux客户机中没有硬件3D加速

[virtualbox-guest-utils](<https://archlinux.org/packages/?name=virtualbox-guest-utils>)包 包的版本5.2.16-2缺少文件`VBoxEGL.so`. 这导致Arch Linux虚拟机无法正常使用3D加速。请参阅 [FS#49752](<https://bugs.archlinux.org/task/49752>). 

为了解决这个问题，请按照[FS#49752#comment152254](<https://bugs.archlinux.org/task/49752#comment152254>)中提供的补丁集进行修复。需要对补丁集进行一些修复，以使其适用于版本5.2.16-2。 

###  Plasma将客户机的分辨率重置为800×600

See [KDE#Cannot change screen resolution when running in a virtual machine](<../../zh-cn/KDE.html#Cannot_change_screen_resolution_when_running_in_a_virtual_machine> "KDE"). 

###  在Plasma-X11最小安装中出现黑屏

如果您使用的是 **plasma-desktop** 最小安装，而不是 **plasma** (包含Wayland支持), 那么在启动Plasma-X11会话后，可能会出现黑屏但有光标的情况。 

要解决此问题，请在VirtualBox窗口中多次调整虚拟机窗口大小，然后通过以下方式手动设置分辨率。 

View -> Virtual Screen 1 -> Resize to 1024x768 (or other resolution you like) 

然后[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [kscreen](<https://archlinux.org/packages/?name=kscreen>)包. 

Open in KDE launcher **System Settings - > Startup and Shutdown -> Background Services**, stop and unselect **KScreen2** and save settings. Issue should go away forever 
