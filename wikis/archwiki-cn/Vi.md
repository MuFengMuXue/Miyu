**翻译状态：**

  * 本文（或部分内容）译自 [Vi](<https://wiki.archlinux.org/title/Vi> "arch:Vi")，最近一次同步于 2022-07-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Vi?diff=0&oldid=679836>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Vi_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自[维基百科](<https://en.wikipedia.org/wiki/Vi> "wikipedia:Vi")： 

    vi 是一款面向屏幕的文本编辑器，最初为 Unix 操作系统创建。《单一 Unix 规范》和 POSIX 描述（并标准化）了 vi 及其衍生程序的可移植行为子集，以及这些程序中支持的 ex 编辑器语言。

##  安装

vi 已不再提供。作为代替方案，你可以使用新一点的文本编辑器，例如 [vim](<https://archlinux.org/packages/?name=vim>)包 和 [neovim](<https://archlinux.org/packages/?name=neovim>)包。还有一个兼容包 [ex-vi-compat](<https://archlinux.org/packages/?name=ex-vi-compat>)包 同时提供了ex 和 vi（兼容模式下的 vim）两种[文本编辑器](<../zh-cn/List_of_applications/Documents.html#Vi-style_text_editors> "List of applications/Documents")。另外， [vi-vim-symlink](<https://aur.archlinux.org/packages/vi-vim-symlink/>)AUR 提供了从 vi 到 vim 的简单链接。 

##  Vi 风格的软件

Vi 的键绑定和模式已在其他各种软件中重新创建： 

  * [文本编辑器](<../zh-cn/List_of_applications/Documents.html#Vi-style_text_editors> "List of applications/Documents")，其中最受欢迎的是 [Vim](<../zh-cn/Vim.html> "Vim")
  * [文件管理器](<../zh-cn/List_of_applications/Utilities.html#File_managers> "List of applications/Utilities")，如 [ranger](<../zh-cn/Ranger.html> "Ranger") 和 [Vifm](<../zh-cn/Vifm.html> "Vifm")
  * [Readline](<../zh-cn/Readline.html#Editing_mode> "Readline") 输入库（由 [Bash](<../zh-cn/Bash.html> "Bash") 使用）
  * [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell")，如 [Zsh](<../zh-cn/Zsh.html#Key_bindings> "Zsh")
  * [网页浏览器](</wzh/index.php?title=Web_browser&action=edit&redlink=1> "Web browser（页面不存在）")，如 [Luakit](</wzh/index.php?title=Luakit&action=edit&redlink=1> "Luakit（页面不存在）")，[qutebrowser](</wzh/index.php?title=Qutebrowser&action=edit&redlink=1> "Qutebrowser（页面不存在）") 和 [vimb](<https://archlinux.org/packages/?name=vimb>)包；对于 [Firefox](<../zh-cn/Firefox.html> "Firefox") 和 [Chromium](<../zh-cn/Chromium.html> "Chromium")，有可用的[浏览器扩展](</wzh/index.php?title=Browser_extensions&action=edit&redlink=1> "Browser extensions（页面不存在）")。
  * 大多数[平铺窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html#%E5%B9%B3%E9%93%BA%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8> "平铺窗口管理器")都可以配置为进行 vi 样式控制

##  参见

  * [vi(1)](<https://man.archlinux.org/man/vi.1>)
