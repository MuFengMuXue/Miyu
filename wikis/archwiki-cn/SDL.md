**翻译状态：**

  * 本文（或部分内容）译自 [SDL](<https://wiki.archlinux.org/title/SDL> "arch:SDL")，最近一次同步于 2025-01-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/SDL?diff=0&oldid=826089>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SDL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**SDL** （Simple DirectMedia Layer）是一个跨平台软件开发库，旨在为计算机多媒体硬件组件提供一个硬件抽象层。软件开发者可用它编写高性能计算机游戏和其他多媒体应用程序。SDL 常常被误解为一个游戏引擎。不过，此库适合直接用于构建游戏，或被构建在其之上的引擎间接使用。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sdl3](<https://archlinux.org/packages/?name=sdl3>)包 软件包。 

如果您需要 [sdl2](<https://aur.archlinux.org/packages/sdl2/>)AUR 或 [sdl12-compat](<https://archlinux.org/packages/?name=sdl12-compat>)包，请相应安装，不过建议迁移到 SDL3。 

SDL2 应用程序也可以使用 [sdl2-compat](<https://archlinux.org/packages/?name=sdl2-compat>)包。SDL2 兼容层在幕后使用 SDL3。 

与 SDL3 类似，SDL2 也是模块化的，不过模块都在不同的软件包中。SDL 2 的模块包包括 [sdl2_image](<https://archlinux.org/packages/?name=sdl2_image>)包、[sdl2_mixer](<https://archlinux.org/packages/?name=sdl2_mixer>)包、[sdl2_ttf](<https://archlinux.org/packages/?name=sdl2_ttf>)包 等，SDL1.2 的模块包包括 [sdl_image](<https://archlinux.org/packages/?name=sdl_image>)包、[sdl_mixer](<https://archlinux.org/packages/?name=sdl_mixer>)包、[sdl_ttf](<https://archlinux.org/packages/?name=sdl_ttf>)包 等。 

##  文档

官方 [SDL Wiki](<https://wiki.libsdl.org/SDL3/FrontPage>) 提供了使用 SDL3 库所需的各种资源和文档。 

官方还提供了[关于将程序从 SDL2 迁移到 SDL3 的文档](<https://github.com/libsdl-org/SDL/blob/main/docs/README-migration.md>)。 

此外，[SDL3 Examples](<https://examples.libsdl.org/SDL3/>) 还提供了一些小型示例程序。 

##  参见

  * [SDL 发布](<https://github.com/libsdl-org/SDL/releases/latest>)
  * [SDL 论坛](<https://discourse.libsdl.org/>)
  * [SDL 主页](<https://www.libsdl.org/>)
  * [SDL 邮件列表](<https://www.libsdl.org/mailing-list.php>)
  * [SDL 语言绑定](<https://www.libsdl.org/languages.php>)
  * [SDL Github](<https://github.com/libsdl-org>)
  * [Wikipedia:Simple DirectMedia Layer](<https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer> "wikipedia:Simple DirectMedia Layer")
