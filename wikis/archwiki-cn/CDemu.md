**翻译状态：**

  * 本文（或部分内容）译自 [CDemu](<https://wiki.archlinux.org/title/CDemu> "arch:CDemu")，最近一次同步于 2022-12-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/CDemu?diff=0&oldid=743326>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/CDemu_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[CDemu](<http://cdemu.sourceforge.net/>) 是一个虚拟光驱，可以挂载.bin/.cue, .nrg, 或 .ccd 等非ISO-9660格式光盘镜像。`mount` 只能挂载包含单一文件系统的 iso。而许多 cd 都带有复杂的信息，比如混合数据和音轨。CDemu 能获得这些CD镜像完整、原始的内容。 

CDemu 利用vhba内核模块模拟出一个SCSI CD/DVD设备，由后台运行的cdemud守护进程(`cdemud`)与该模块通信。镜像分析代码被抽象到一个库中(`libmirage`)，需要支持新的镜像格式时，也便于扩充。守护进程响应来自客户端的[dbus](<../zh-cn/D-Bus.html> "Dbus")命令。CDemu软件包提供了两种可选的客户端：基于命令行的(`cdemu-client`)和[GNOME](<../zh-cn/GNOME.html> "GNOME")的panel applet——(`gcdemu`). 

##  安装

CDemu 可以通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")中的软件包 [cdemu-client](<https://archlinux.org/packages/?name=cdemu-client>)包 获得。如果使用自定义内核，不要使用正常的 `vhba` 内核软件包 [vhba-module](<https://archlinux.org/packages/?name=vhba-module>)包, 必须使用 [DKMS](<../zh-cn/DKMS.html> "DKMS") 版本的软件包 [vhba-module-dkms](<https://archlinux.org/packages/?name=vhba-module-dkms>)包. 

启动 Systemd 服务: 
    
    # systemctl enable cdemu-daemon.service
    
systemd 不会自动加载 CD/DVD 驱动，需要手动加载： 
    
     # modprobe -a sg sr_mod vhba
    
###  图形界面

[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中包含了多个图形界面： 

  * GTK/Gnome [gcdemu](<https://aur.archlinux.org/packages/gcdemu/>)AUR: 提供 GNOME 面板程序。
  * KDE [kde-cdemu-manager](<https://aur.archlinux.org/packages/kde-cdemu-manager/>)AUR: 独立程序，与 Dolphin 的动作菜单交互，可以在镜像文件上右键。

##  示例

将单个镜像加载为第一个设备： 
    
    $ cdemu load 0 ~/image.mds
    
将多文件镜像加载为第一个设备： 
    
    $ cdemu load 0 ~/session1.toc ~/session2.toc ~/session3.toc
    
设定字符编码: 
    
    $ cdemu load 0 ~/image.cue --encoding=windows-1250
    
挂载加密镜像: 
    
    $ cdemu load 0 ~/image.daa --password=seeninplain
    
卸载第一个设备: 
    
    $ cdemu unload 0
    
显示设备状态: 
    
    $ cdemu status
    
显示设备挂载信息: 
    
    $ cdemu device-mapping
    
Setting daemon debug mask for the first device: 
    
    $ cdemu daemon-debug-mask 0 0x01
    
Obtaining library debug mask for the first device: 
    
    $ cdemu library-debug-mask 0
    
Disabling DPM emulation on all devices: 
    
    $ cdemu dpm-emulation all 0
    
Enabling transfer rate emulation on first device: 
    
    $ cdemu tr-emulation 0 1
    
Changing device ID of first device: 
    
    $ cdemu device-id 0 "MyVendor" "MyProduct" "1.0.0" "Test device ID"
    
Enumerating supported parsers: 
    
    $ cdemu enum-supported-parsers
    
Enumerating supported fragments: 
    
    $ cdemu enum-supported-fragments
    
Enumerating supported daemon debug masks: 
    
    $ cdemu enum-daemon-debug-masks
    
Enumerating supported library debug masks: 
    
    $ cdemu enum-library-debug-masks
    
Displaying daemon and library version: 
    
    $ cdemu version
    