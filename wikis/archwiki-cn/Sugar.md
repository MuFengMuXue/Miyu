相关文章

  * [Desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment")

作为 [OLPC](<https://en.wikipedia.org/wiki/One_Laptop_per_Child> "wikipedia:One Laptop per Child") 倡议的产物，[Sugar](<https://en.wikipedia.org/wiki/Sugar_\(software\)> "wikipedia:Sugar \(software\)") 是一个类似于 [KDE](<../zh-cn/KDE.html> "KDE") 和 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的桌面环境，但面向儿童和教育。 

Sugar 有一个特殊的[分类法](<https://wiki.sugarlabs.org/go/Taxonomy>)来命名其系统的各个部分。图形界面本身构成了 **Glucose** （葡萄糖）组。这是安装 Sugar 时理应符合预期的核心系统。但要真正使用这个桌面环境，您需要 activities（一些应用程序）。基础的 activities 是 **Fructose** （果糖）的一部分。然后，**Sucrose** 由 Glucose 和 Fructose 组成，代表应该作为基本 Sugar 桌面环境分发的内容。额外的 activities 是 **Honey** （蜜糖）的一部分。请注意，Ribose（底层操作系统）在这里被 Arch 取代。 

##  安装

  * 对于核心系统 (_Glucose_)，安装 [sugar](<https://archlinux.org/packages/?name=sugar>)包。它提供了图形界面和桌面会话，但它本身并不是很有用。
  * [sugar-fructose](<https://archlinux.org/groups/x86_64/sugar-fructose/>)包组 软件包组包含了基本 activities (_Fructose_)，包括网络浏览器、文本编辑器、媒体播放器和终端模拟器。
  * [sugar-runner](<https://archlinux.org/packages/?name=sugar-runner>)包 软件包提供了一个帮助脚本，可以在另一个桌面环境中启动 Sugar，或者直接从命令行启动。

###  从 Activity 库安装

[Sugar Activity Library](<https://wiki.sugarlabs.org/go/Activity_Library>) 提供了许多 [Activity Bundles](<https://wiki.sugarlabs.org/go/Development_Team/Almanac/Activity_Bundles>)，打包为带有“.xo”扩展名的 zip 文件。这些包可以从 Sugar 下载并安装到用户的目录中，但是安装并不能确保满足依赖关系。因此，不推荐此安装 activities 的方法，因为它们可能由于缺少依赖项而无法启动。常用依赖： 

  * 对于web activities，从官方存储库安装 [webkit2gtk](<https://archlinux.org/packages/?name=webkit2gtk>)包。
  * 对于基于 GTK 2 的 activities，从 AUR 安装 [sugar-toolkit-gtk2](<https://aur.archlinux.org/packages/sugar-toolkit-gtk2/>)AUR。

为了检查 activities 无法启动的原因，请查看位于 `~/.sugar/default/logs/[app_id]-1.log` 的log文件。 

##  启动 Sugar

Sugar 可以使用 [display manager](<../zh-cn/Display_manager.html> "Display manager") 以图形方式启动，也可以从控制台手动启动。 

**图形方式**

从显示管理器的会话菜单中选择 _Sugar_ 。 

**手动**

如果 [sugar-runner](<https://archlinux.org/packages/?name=sugar-runner>)包 已安装，Sugar 可以使用 `sugar-runner` 命令启动。 

另一种方法是将 `exec sugar` 添加到 `~/.xinitrc` 文件中。然后，可以使用 `startx` 命令启动 Sugar（有关详细信息，请参阅 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc")）。设置好`~/.xinitrc`文件后，也可以安排为 [Start X at login](</wzh/index.php?title=Start_X_at_login&action=edit&redlink=1> "Start X at login（页面不存在）")。 

##  另请参见

  * [Sugar 官网](<https://sugarlabs.org/>)
  * [Activities for Sugar](<https://activities.sugarlabs.org/>)
