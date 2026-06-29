**翻译状态：**

  * 本文（或部分内容）译自 [Thunar](<https://wiki.archlinux.org/title/Thunar> "arch:Thunar")，最近一次同步于 2024-09-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Thunar?diff=0&oldid=816873>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Thunar_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Xfce](<../zh-cn/Xfce.html> "Xfce")
  * [File manager functionality](<../zh-cn/File_manager_functionality.html> "File manager functionality")
  * [arch:GNOME Files](<https://wiki.archlinux.org/title/GNOME_Files> "arch:GNOME Files")
  * [PCManFM](<../zh-cn/PCManFM.html> "PCManFM")
  * [arch:Nemo](<https://wiki.archlinux.org/title/Nemo> "arch:Nemo")

来自项目[官网](<https://docs.xfce.org/xfce/thunar/start>): 

    Thunar 是一个用于 Xfce 桌面环境的现代化的文件管理器。Thunar 的设计初衷就是快速且易于使用。其界面简洁直观,默认不包含令人误解或无用的选项。Thunar 快速且响应迅速，具有良好的启动时间和文件夹加载时间。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [thunar](<https://archlinux.org/packages/?name=thunar>)包 软件包。Thunar [xfce4](<https://archlinux.org/groups/x86_64/xfce4/>)包组 软件包组的一部分,也是 [Xfce](<../zh-cn/Xfce.html> "Xfce") 桌面环境的默认文件管理器。 

###  插件与附件

  * **Gnome 虚拟文件系统** — 安装后显示垃圾桶，可移动介质，和远程文件系统（`mtp`/`smb`）。详情请见 [File manager functionality#Mounting](<../zh-cn/File_manager_functionality.html#Mounting> "File manager functionality")。

     <https://wiki.gnome.org/Projects/gvfs> || [gvfs](<https://archlinux.org/packages/?name=gvfs>)包

  * **Thuanr 归档插件** — 让你能够使用上下文菜单创建和解压归档文件的插件。它并不会直接创建或解压归档,而是作为其他程序的前端,例如 File Roller ([file-roller](<https://archlinux.org/packages/?name=file-roller>)包), Ark ([ark](<https://archlinux.org/packages/?name=ark>)包), Xarchiver ([xarchiver](<https://archlinux.org/packages/?name=xarchiver>)包) 或 Engrampa ([engrampa](<https://archlinux.org/packages/?name=engrampa>)包)。是软件包组 [xfce4-goodies](<https://archlinux.org/groups/x86_64/xfce4-goodies/>)包组 的一部分。

     <https://goodies.xfce.org/projects/thunar-plugins/thunar-archive-plugin> || [thunar-archive-plugin](<https://archlinux.org/packages/?name=thunar-archive-plugin>)包

  * **Thunar 媒体标签插件** — 让你能够预览媒体文件详细信息的插件。它还带有批量重命名和编辑媒体标签的功能。它支持 ID3 (MP3 文件格式系统) 和 Ogg/Vorbis 标签。是软件包组 [xfce4-goodies](<https://archlinux.org/groups/x86_64/xfce4-goodies/>)包组 的一部分。

     <https://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin> || [thunar-media-tags-plugin](<https://archlinux.org/packages/?name=thunar-media-tags-plugin>)包

  * **Thunar 共享插件** — 让你能够无需 root 权限,通过 Thunar ,使用 Samba 快速分享文件夹的插件。另见[如何配置方向](<../zh-cn/Samba.html#Enable_Usershares> "Samba")。

     <https://goodies.xfce.org/projects/thunar-plugins/thunar-shares-plugin> || [thunar-shares-plugin](<https://archlinux.org/packages/?name=thunar-shares-plugin>)包

  * **[Thunar 卷管理器](<#Thunar_%E5%8D%B7%E7%AE%A1%E7%90%86%E5%99%A8>)** — 在 Thunar 中自动管理可移动设备。是软件包组 [xfce4-goodies](<https://archlinux.org/groups/x86_64/xfce4-goodies/>)包组 的一部分。

     <https://goodies.xfce.org/projects/thunar-plugins/thunar-volman> || [thunar-volman](<https://archlinux.org/packages/?name=thunar-volman>)包

  * **Tumbler** — 生成缩略图的外部程序。还可以安装 [ffmpegthumbnailer](<https://archlinux.org/packages/?name=ffmpegthumbnailer>)包 来启用视频缩略图。

     <https://gitlab.xfce.org/xfce/tumbler> || [tumbler](<https://archlinux.org/packages/?name=tumbler>)包

  * **libgsf** — GNOME 结构化文件库是一个用于读写结构化文件格式的实用程序库。如果你需要 odf 缩略图的支持就安装。

     <https://directory.fsf.org/wiki/Libgsf> || [libgsf](<https://archlinux.org/packages/?name=libgsf>)包

  * **RAW thumbnailer** — 一个轻量快速的原始图像缩略图生成器,用于显示原始图像缩略图。

     <https://code.google.com/archive/p/raw-thumbnailer/> || [raw-thumbnailer](<https://aur.archlinux.org/packages/raw-thumbnailer/>)AUR

  * **Extra thumbnailers** — 为 Tumbler 定制的缩略图生成器。

     <https://docs.xfce.org/xfce/tumbler/available_plugins/> || [tumbler-extra-thumbnailers](<https://aur.archlinux.org/packages/tumbler-extra-thumbnailers/>)AUR

  * **Folder thumbnailer** — 通过 Tumbler 支持自定义文件夹缩略图。

     <https://github.com/j-james/thunar-folder-thumbnails> || [tumbler-folder-thumbnailer](<https://aur.archlinux.org/packages/tumbler-folder-thumbnailer/>)AUR

  * **STL thumbnailer** — 为 Tumbler 生成 STL 缩略图的支持。

     <https://github.com/j-james/thunar-stl-thumbnails> || [tumbler-stl-thumbnailer](<https://aur.archlinux.org/packages/tumbler-stl-thumbnailer/>)AUR

  * **webp-pixbuf-loader** — [gdk-pixbuf2](<https://archlinux.org/packages/?name=gdk-pixbuf2>)包 的可选依赖，为默认的缩略图生成器提供了生成 webp 缩略图的支持。

     <https://github.com/aruiz/webp-pixbuf-loader> || [webp-pixbuf-loader](<https://archlinux.org/packages/?name=webp-pixbuf-loader>)包

##  配置

要配置按键绑定，请编辑 `~/.config/Thunar/accels.scm` 文件。要配置 Thunar 的隐藏变量，请使用 `xfconf-query -c thunar -l -v`。 

##  Thunar 卷管理器

若已安装 [gvfs](<https://archlinux.org/packages/?name=gvfs>)包 和 [thunar-volman](<https://archlinux.org/packages/?name=thunar-volman>)包，可配置 Thunar 在介质连接时自动执行命令。对于可移动设备,通常遵循 [MTP](<../zh-cn/%E5%AA%92%E4%BD%93%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE.html> "MTP"),需要额外安装 [gvfs-mtp](<https://archlinux.org/packages/?name=gvfs-mtp>)包 软件包。 

**提示：** 要想让 Thunar 处理自动挂载,必须在[守护进程模式](<#%E4%BB%A5%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B%E6%A8%A1%E5%BC%8F%E5%90%AF%E5%8A%A8>)中启动。

###  配置

它还可以配置为在连接相机和音频播放器时执行某些操作。 在安装插件之后: 

  1. 启动 Thunar 然后前往 _Edit > Preference_
  2. 在 'Advanced' 标签页下,勾选 'Enable Volume Management'
  3. 点击配置并勾选下列项目: 
     * Mount removable drives when hot-plugged.
     * Mount removable media when inserted.
  4. 再做出你想要的设置(请见下面的例子)

这是一个自动用 Amarok 播放音频 CD 的设置例子。 
    
     Multimedia - Audio CDs: amarok --cdplay %d
    
##  自定义动作

本节介绍有用的自定义操作,可以通过 `Edit -> Configure custom actions` 访问,存储在 `~/.config/Thunar/uca.xml`。[thunar wiki](<https://docs.xfce.org/xfce/thunar/custom-actions>) 中列出了更多例子。此外,[这篇](<https://duncanlock.net/blog/2013/06/28/useful-thunar-custom-actions/>)博客文章提供了全面的自定义操作集合。 

###  在此处打开终端

“在此处打开终端” 是安装时的唯一操作。为 [exo](<https://archlinux.org/packages/?name=exo>)包 配置要使用的终端： 
    
    ~/.config/xfce4/helpers.rc
    
    TerminalEmulator=_terminal_

Name | Command | File patterns | Appears if selection contains   
---|---|---|---  
Open Terminal Here  | `exo-open --working-directory %f --launch TerminalEmulator` | * | Directories   
  
###  搜索文件的目录

要想使用这个动作,你需要安装 [catfish](<https://archlinux.org/packages/?name=catfish>)包。对于想要有预构建的索引数据库的用户, 可以安装[plocate](<https://archlinux.org/packages/?name=plocate>)包 和 [zeitgeist](<https://archlinux.org/packages/?name=zeitgeist>)包 可选依赖。 

Name | Command | File patterns | Appears if selection contains   
---|---|---|---  
Search  | `catfish --path=%f` | * | Directories   
  
###  扫描病毒

要想使用这个动作,你需要安装 [clamav](<https://archlinux.org/packages/?name=clamav>)包 和 [clamtk](<https://archlinux.org/packages/?name=clamtk>)包。 

Name | Command | File patterns | Appears if selection contains   
---|---|---|---  
Scan for virus  | `clamtk %F` | * | Select all   
  
###  链接到 Dropbox

Name | Command | File patterns | Appears if selection contains   
---|---|---|---  
Link to Dropbox  | `ln -s %f /path/to/DropboxFolder` | * | Directories, other files   
  
请注意当使用许多自定义操作将文件和文件夹符号链接到特定位置时,将它们放到上下文菜单中的 `发送到` 目录可以避免上下文菜单变得臃肿。这很容易实现,需要在 `~/.local/share/Thunar/sendto` 中为每个动作创建一个 .desktop 文件。假设我们要将上述 Dropbox 符号链接操作放入 "发送到",创建一个带有下列内容的 `dropbox_folder.desktop` 。新应用的动作会在 Thunar 重启后激活。 
    
    [Desktop Entry]
    Type=Application
    Version=1.0
    Encoding=UTF-8
    Exec=ln -s %f /path/to/DropboxFolder
    Icon=/usr/share/icons/dropbox.png
    Name=Dropbox
    
##  提示与技巧

###  使用 Thunar 浏览远程位置

因为 Xfce 4.8 (Thunar 1.2) 可以直接在 Thunar 浏览远程位置 (例如 FTP 服务器或 Samba 共享)。要想启用这个功能，确保 [gvfs](<https://archlinux.org/packages/?name=gvfs>)包 和 [sshfs](<https://archlinux.org/packages/?name=sshfs>)包（若需要 SMB/CIFS 支持，还需要 [gvfs-smb](<https://archlinux.org/packages/?name=gvfs-smb>)包）软件包已安装。Thunar 侧边栏可以看到 '网络' 项目,可以在位置对话框中使用以下 URI 方案打开远程位置 (用 `Ctrl+l` 打开):smb://, ftp://, ssh://, sftp://, davs:// 后跟服务器主机名或 IP 地址。 

没有用于 [NFS](<../zh-cn/NFS.html> "NFS") 共享的 URI 方案,但是如果你正确设置你的 [fstab](<../zh-cn/Fstab.html> "Fstab") ,Thunar 可以发出 `mount` 命令。 
    
    /etc/fstab
    
    # nas1 server
    nas1:/c/home		/media/nas1/home	nfs	noauto,user,_netdev,bg  0 0

这里要注意的是 `noauto` 选项,它会在你点击挂载前阻止共享被自动挂载,`user` 选项是被允许挂载和卸载共享的用户,`_netdev` 选项使网络连接成为先决条件,最后 `bg` 选项使挂载操作在后台进行,如果你的服务器需要一些启动时间,这么做将使你在它工作前不必处理超时消息并重新单击。 

**提示：**

  * 如果你想要持久存储远程文件系统位置的密码,你必须安装 [GNOME Keyring](<https://wiki.archlinux.org/title/GNOME/Keyring> "arch:GNOME/Keyring")。
  * 为了让 Thunar 显示任意非 root 用户的新设备,可能需要将挂载点设置为 `/media` 的子目录。

###  以守护进程模式启动

Thunar 可以以守护进程模式运行。这有许多优势,包括加快 Thunar 的启动速度,Thunar 在后台运行而且在需要时只打开一个窗口(例如当闪存驱动器插入时),和让 Thunar 处理可移动介质的自动挂载。 

确保命令 `thunar --daemon` 在登录时自动运行。详情请见 [Xfce](<../zh-cn/Xfce.html> "Xfce") 和[自动运行](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "Autostarting")。 

###  缓慢的冷启动问题的解决方案

一些人还有 Thunar 在首次启动时耗时过长的问题。这是因为 gvfs 检查网络,阻止 Thunar 启动直到它完成该操作。要想改善此行为,编辑 `/usr/share/gvfs/mounts/network.mount` ,将 `AutoMount=true` 修改为 `AutoMount=false`。 

###  在侧窗格中隐藏快捷方式

在侧窗格中有一个隐藏菜单用于隐藏快捷方式。 

在侧窗格中没有快捷方式的地方右键,例如在 DEVICES 标签上。然后会弹出一个菜单,你可以将不想显示出的项目取消勾选。 

###  在 Thunar 中分配键盘快捷键

请见 [GTK#键盘快捷键](<../zh-cn/GTK.html#%E9%94%AE%E7%9B%98%E5%BF%AB%E6%8D%B7%E9%94%AE> "GTK")。 

###  显示在 fstab 中定义的分区

默认情况下 Thunar 不会在设备中显示 `/etc/fstab` 中定义的任何分区,除了 root 分区。 

我们可以通过向 [fstab](<../zh-cn/Fstab.html> "Fstab") 中为想要显示出的分区添加 `x-gvfs-show` 选项。 

##  故障排除

###  大型外部驱动器的自动挂载

如果安装了 thunar-volman 和 gvfs,但 Thunar 拒绝挂载大型可移动介质(大小 > 1TB),试着安装一个不同的自动挂载器例如 [udevil](<https://aur.archlinux.org/packages/udevil/>)AUR 或 [udiskie](<https://archlinux.org/packages/?name=udiskie>)包。更推荐后者因为它使用 udisks2 而且它与 gvfs 兼容。要想启动带有 udisks2 支持的 udiskie,将下列内容添加到你的自动启动文件: 
    
    udiskie -2 &
    
###  Tumblerd 挂起,占用过多 CPU

Tumblerd 在监视文件系统并在需要制作缩略图时通知系统的服务时可能会陷入循环,请见 [bug 报告](<https://bugzilla.xfce.org/show_bug.cgi?id=7384>)。下面的脚本是一个阻止这种情况发生的临时解决方案。复制,将它粘贴到一个 _.sh_ 文件,将它保存的你的家目录的某个位置,将文件标记为可运行,然后在将它设置为在系统启动时自动运行。 
    
    #!/bin/bash
    period=20
    tumblerpath="/usr/lib/*/tumbler-1/tumblerd" # The * here should find the right one, whether 32 and 64-bit
    cpu_threshold=50
    mem_threshold=20
    max_strikes=2                               # max number of above cpu/mem-threshold's in a row
    log="/tmp/tumblerd-watcher.log"
    
    if [[ -n "${log}" ]]; then
        cat /dev/null > "${log}"
        exec >"${log}" 2>&1
    fi
    
    strikes=0
    while sleep "${period}"; do
        while read pid; do
    	cpu_usage=$(ps --no-headers -o pcpu -f "${pid}"|cut -f1 -d.)
    	mem_usage=$(ps --no-headers -o pmem -f "${pid}"|cut -f1 -d.)
    
    	if [[ $cpu_usage -gt $cpu_threshold ]] || [[ $mem_usage -gt $mem_threshold ]]; then
    	    echo "$(date +"%F %T") PID: $pid CPU: $cpu_usage/$cpu_threshold %cpu MEM: $mem_usage/$mem_threshold STRIKES: ${strikes} NPROCS: $(pgrep -c -f ${tumblerpath})"
    	    (( strikes++ ))
    	    if [[ ${strikes} -ge ${max_strikes} ]]; then
    		kill "${pid}"
    		echo "$(date +"%F %T") PID: $pid KILLED; NPROCS: $(pgrep -c -f ${tumblerpath})"
    		strikes=0
    	    fi
    	else
    	    strikes=0
    	fi
        done < <(pgrep -f ${tumblerpath})
    done
    
###  垃圾桶/网络 图标随机消失

确保所有 Thunar 示例在 _gvfs_ **之后** 启动。[[1]](<https://bugs.launchpad.net/ubuntu/+source/thunar/+bug/1057610>)对于 `thunar --daemon`, 你可以将它包装成等待直到 GVFS 启动: 

**注意：** 在 `$PATH` 中 `/usr/local/bin` 应该在 `/usr/bin` 的前面。
    
    /usr/local/bin/Thunar
    
    #!/bin/bash
    if [[ $1 == --daemon ]]; then
      until pgrep gvfs >/dev/null; do
        sleep 1
      done
      exec /usr/bin/Thunar "$@"
    else
      exec /usr/bin/Thunar "$@"
    fi
    
###  未经身份验证挂载文件系统

请见 [File manager functionality#Troubleshooting](<../zh-cn/File_manager_functionality.html#Troubleshooting> "File manager functionality")。 

###  Thunar 新窗口或标签打开速度太慢

可能是因为你在设置为 `XDG_TEMPLATES_DIR` 的目录中有太多文件。请见 [XDG 用户路径](<../zh-cn/XDG_user_directories.html> "XDG user directories")。 

解决方案是将 `XDG_TEMPLATES_DIR` 中文件移到其他地方,或者将 `XDG_TEMPLATES_DIR` 设置为其他目录。 

##  另见

  * [Thunar](<https://docs.xfce.org/xfce/thunar/start>) 项目页面
  * [Thunar 卷管理器](<https://goodies.xfce.org/projects/thunar-plugins/thunar-volman>)项目页面
  * 这个插件[列表](<https://docs.xfce.org/xfce/thunar/start#thunar_plugins>)
  * 一些设置,比如在标题中显示完整路径,可以通过 `xfconf-query` 启用。详情请见[这个列表](<https://docs.xfce.org/xfce/thunar/hidden-settings>)。
