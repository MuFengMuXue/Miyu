**翻译状态：**

  * 本文（或部分内容）译自 [ASUS Linux](<https://wiki.archlinux.org/title/ASUS_Linux> "arch:ASUS Linux")，最近一次同步于 2024-07-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/ASUS_Linux?diff=0&oldid=797392>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ASUS_Linux_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [asusctl](</wzh/index.php?title=Asusctl&action=edit&redlink=1> "Asusctl（页面不存在）")
  * [supergfxctl](<../zh-cn/Supergfxctl.html> "Supergfxctl")

ASUS Linux 是一套旨在提升在华硕笔记本上运行 Linux 的使用体验的工具，包括性能提升和功能驱动。它由 [asusctl](</wzh/index.php?title=Asusctl&action=edit&redlink=1> "Asusctl（页面不存在）") 和 [supergfxctl](<../zh-cn/Supergfxctl.html> "Supergfxctl") 两部分组成，前者与内核模块 `asus-wmi` 通信以控制 BIOS 级别的功能，后者用于在双显卡机型上控制独立显卡。 

该项目由 [Luke Jones](<https://gitlab.com/flukejones>) 维护，托管在 [GitLab](<https://gitlab.com/asus-linux>) 上。 

##  软件

ASUS Linux 提供了许多软件包，详细请看下方子标题。 

**注意：**

  * 您可以在此定制仓库找到已编译的二进制软件包: [非官方用户仓库#g14](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#g14> "非官方用户仓库"), 由 [Luke Jones](<https://gitlab.com/flukejones>) 提供。
  * 官方建议使用此仓库安装 asus-linux 组件。此仓库由 asus-linux 开发者提供和维护。详见 <https://asus-linux.org/guides/arch-guide/>
  * 尽管该项目使用 G14 的名字，这**并不代表** 其仅适用于华硕幻14设备。事实上，它几乎支持所有华硕 ROG 和 TUF 笔记本。

### asusctl

[asusctl](<https://aur.archlinux.org/packages/asusctl/>)AUR 是用于华硕 ROG 和 TUF 笔记本的命令行工具，拥有包括但不限于以下功能： 

  * 集成显卡 MUX 控制
  * 键盘 RGB 控制 （不及 AURA/奥创中心）
  * 风扇曲线调控
  * 电池充电上限
  * 屏幕快显
  * AniMe Matrix 光显矩阵屏

使用方法详见 [asusctl](</wzh/index.php?title=Asusctl&action=edit&redlink=1> "Asusctl（页面不存在）")。 

### supergfxctl

[supergfxctl](<https://aur.archlinux.org/packages/supergfxctl/>)AUR 是在华硕混合显卡笔记本上管理显卡切换功能的命令行工具，尤其是独立显卡 MUX 控制。 

使用方法详见 [supergfxctl](<../zh-cn/Supergfxctl.html> "Supergfxctl")。 

### rog-control-center

[rog-control-center](<https://aur.archlinux.org/packages/rog-control-center/>)AUR 是 _asusctl_ 和 _supergfxctl_ 的图形化前端，不过功能有限。 

###  定制内核

ASUS Linux 项目还维护了一套针对华硕移动端特化的内核补丁，并将其整合到一个定制内核当中。一般来说，您并不需要使用此内核，但在某些极端情况下（通常是最新的笔记本），您必须使用此内核才能使用您笔记本的一些特殊功能。 

要使用定制内核，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [linux-g14](<https://aur.archlinux.org/packages/linux-g14/>)AUR 和 [linux-g14-headers](<https://aur.archlinux.org/packages/linux-g14-headers/>)AUR。 

**注意：**

  * 如果您添加了 [G14 非官方仓库](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#g14> "非官方用户仓库")，您可以直接使用 [pacman](<../zh-cn/Pacman.html> "Pacman") 安装上述 AUR 软件包。
  * 如果您正在尝试从原版内核切换为定制内核，您还必须将所有内核模块升级为 [DKMS](<../zh-cn/DKMS.html> "DKMS") 版本。

##  参见

  * 项目主页 - <https://asus-linux.org/>
  * 项目 GitLab 页 - <https://gitlab.com/asus-linux>
