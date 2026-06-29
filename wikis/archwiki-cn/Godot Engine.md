**翻译状态：**

  * 本文（或部分内容）译自 [Godot Engine](<https://wiki.archlinux.org/title/Godot_Engine> "arch:Godot Engine")，最近一次同步于 2024-12-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Godot_Engine?diff=0&oldid=815971>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Godot_Engine_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Godot Engine](<https://godotengine.org>) 是一个开源游戏引擎。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [godot](<https://archlinux.org/packages/?name=godot>)包 软件包，或安装 [godot-git](<https://aur.archlinux.org/packages/godot-git/>)AUR 以获取开发版本。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")用于支持 C# 编程的 [godot-mono](<https://archlinux.org/packages/?name=godot-mono>)包 软件包。 

###  旧版本

**注意：** 不建议用于新项目。只适用于传统项目，并考虑将其移植到最新版本。

要使用第 3 版引擎，请安装 [godot3](<https://aur.archlinux.org/packages/godot3/>)AUR 软件包。 

要使用第 2 版引擎，请安装 [godot2](<https://aur.archlinux.org/packages/godot2/>)AUR 软件包。 

###  Mono 版本

如果想使用 C# 作为脚本语言，请安装 mono 版本 [godot-mono-bin](<https://aur.archlinux.org/packages/godot-mono-bin/>)AUR 或 [godot-mono-git](<https://aur.archlinux.org/packages/godot-mono-git/>)AUR。 

###  导出模板

要导出项目，您需要预编译的二进制文件。如果使用的是 Git 版本，则需要按照 [wiki](<https://godot.readthedocs.io/en/stable/development/compiling/introduction_to_the_buildsystem.html#export-templates>) 上针对不同平台的自行编译说明，或者使用 [godot-export-templates-git](<https://aur.archlinux.org/packages/godot-export-templates-git/>)AUR。如果使用的是稳定版，则可以安装 Godot 提供的导出模板。点击右上角的引擎设置图标，然后点击 "Install export templates" 并提供下载的模板即可安装。 

##  问题解决

###  Wayland 中的 UI 冻结

Godot 使用 Xwayland 在 Wayland 上运行，如果不在单窗口模式下运行，就会出现各种用户界面问题。[[1]](<https://github.com/godotengine/godot/issues/78487>) 要解决这个问题，可以使用 `godot --single-window` 启动 Godot，然后打开一个项目，并在编辑器设置中启用单窗口模式。 

该问题已在 Godot 4.1.1 中得到解决。[[2]](<https://github.com/godotengine/godot/pull/79143#issuecomment-1629271532>) 这个问题似乎在 Godot 4.2 中再次出现 [[3]](<https://github.com/godotengine/godot/issues/86061>)

在 Godot 4.3 中，Wayland 可以原生使用。[[4]](<https://godotengine.org/article/dev-snapshot-godot-4-3-dev-3/#wayland-support-for-linux>) 有两种方法可以做到这一点： 

  * 设置命令行参数 `--display-driver wayland`。
  * 启用位于 `run/platforms/linuxbsd/prefer_wayland` 的编辑器设置。

##  参见

  * [Wiki 上的 Godot (游戏引擎)](<https://en.wikipedia.org/wiki/Godot_\(game_engine\)> "wikipedia:Godot \(game engine\)")
  * [Godot 文档](<https://godot.readthedocs.io/en/stable/>)
    * [简体中文版](<https://docs.godotengine.org/zh-cn/4.x/>)
  * [Godot 源代码](<https://github.com/godotengine/godot>)
  * [Godot: the Game-Changer for GameDevs](<https://willnationsdev.wordpress.com/2017/07/21/godot-the-game-changer-for-gamedevs/>) \- 简介及与其他引擎的比较
  * [awesome-godot](<https://github.com/godotengine/awesome-godot>) \- 用于 Godot 的免费/自由插件、脚本和附加组件
  * [/r/godot](<https://www.reddit.com/r/godot/>) reddit.com 上的社区
  * [Godot 引擎资源教程](<https://www.youtube.com/user/Link4ns/playlists>)
  * [Gamesfromscratch 的视频教程](<https://www.youtube.com/playlist?list=PLS9MbmO_ssyAXRl-_ktrebQBFxjSQt7UX>)
  * [KidsCanCode 的视频教程](<https://www.youtube.com/channel/UCNaPQ5uLX5iIEHUCLmfAgKg/playlists>)
  * [Andreas Esau 的视频教程](<https://www.youtube.com/user/ndee85/playlists>)
  * [Heartbeast 的视频教程](<https://www.youtube.com/playlist?list=PL9FzW-m48fn1iR6WL4mjXtGi8P4TaPIAp>)
  * [GDQuest 的视频教程](<https://www.youtube.com/channel/UCxboW7x0jZqFdvMdCFKTMsQ/playlists>)
  * [Jose Moreno 的视频教程](<https://www.youtube.com/playlist?list=PLjuYP3iuWoM2hLxtTfvsQA6FzOhRIUMOf>)
