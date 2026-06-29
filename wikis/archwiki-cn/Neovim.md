相关文章

  * [Vim](<../zh-cn/Vim.html> "Vim")
  * [Emacs](<../zh-cn/Emacs.html> "Emacs")

**翻译状态：**

  * 本文（或部分内容）译自 [Neovim](<https://wiki.archlinux.org/title/Neovim> "arch:Neovim")，最近一次同步于 2024-02-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Neovim?diff=0&oldid=795753>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Neovim_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Neovim](<https://neovim.io/>) 是 [Vim](<../zh-cn/Vim.html> "Vim") 的分支，旨在改进代码库，从而使得 API 更容易实现，并改善用户体验和插件实现。Neovim 启发了 [Helix](<../zh-cn/Helix.html> "Helix") 等编辑器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [neovim](<https://archlinux.org/packages/?name=neovim>)包 或 [neovim-git](<https://aur.archlinux.org/packages/neovim-git/>)AUR（开发版本）软件包，两者强烈建议使用 [Lua](<../zh-cn/Lua.html> "Lua") 作为主要的配置语言。要使 Neovim 能够访问系统剪贴板，可能需要安装 [xclip](<https://archlinux.org/packages/?name=xclip>)包（X11）或 [wl-clipboard](<https://archlinux.org/packages/?name=wl-clipboard>)包（Wayland）。 

**注意：** 在 Neovim 中，一些功能委托给外部“providers”（提供者）。对于 Python 提供者，使用 [python-pynvim](<https://archlinux.org/packages/?name=python-pynvim>)包。 对于剪贴板提供者，参见 [provider-clipboard](<https://neovim.io/doc/user/provider.html#provider-clipboard>) 或 `:help provider-clipboard` Neovim 命令。

也可以安装 [GUI 和其他相关项目](<https://github.com/neovim/neovim/wiki/Related-projects>)，它们中的大多数都在[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")或 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中： 

  * **[neovim-qt](<https://archlinux.org/packages/?name=neovim-qt>) 包** — Fast, lightweight, and customizable Qt GUI. Provides a modern interface, including support for multiple tabs, split windows, and customizable themes.

     <https://github.com/equalsraf/neovim-qt> || [neovim-qt](<https://archlinux.org/packages/?name=neovim-qt>)包

  * **[neovim-gtk](<https://aur.archlinux.org/packages/neovim-gtk/>) AUR** — GTK GUI. Provides a modern, customizable interface, including support for split windows, multiple tabs, and customizable themes.

     <https://github.com/Lyude/neovim-gtk> || [neovim-gtk](<https://aur.archlinux.org/packages/neovim-gtk/>)AUR

  * **[uivonim-git](<https://aur.archlinux.org/packages/uivonim-git/>) AUR** — ([Inactive](<https://aur.archlinux.org/packages/uivonim-git#comment-888471>)) Simple and lightweight GTK GUI. Provides a minimalistic interface, including support for split windows and customizable themes.

     [uivonim-git](<https://aur.archlinux.org/packages/uivonim-git/>)AUR || [uivonim-git](<https://aur.archlinux.org/packages/uivonim-git/>)AUR

  * **[neovide](<https://archlinux.org/packages/?name=neovide>) 包** — Rust GUI.

     <https://github.com/neovide/neovide> || [neovide](<https://archlinux.org/packages/?name=neovide>)包

  * **[neoray-git](<https://aur.archlinux.org/packages/neoray-git/>) AUR** — Go GUI.

     <https://github.com/hismailbulut/neoray> || [neoray-git](<https://aur.archlinux.org/packages/neoray-git/>)AUR

  * **[gnvim](<https://aur.archlinux.org/packages/gnvim/>) AUR** — GTK GUI.

     <https://github.com/vhakulinen/gnvim> || [gnvim](<https://aur.archlinux.org/packages/gnvim/>)AUR

  * **[fvim](<https://aur.archlinux.org/packages/fvim/>) AUR** — F# GUI.

     <https://github.com/yatli/fvim> || [fvim](<https://aur.archlinux.org/packages/fvim/>)AUR

##  配置

Neovim 的用户配置位于 `$XDG_CONFIG_HOME/nvim/init.vim`（默认是 `~/.config/nvim/init.vim`）。全局配置文件位于 `$XDG_CONFIG_DIRS/nvim/sysinit.vim`（默认是 `/etc/xdg/nvim/sysinit.vim`）。如果不存在，则会载入 `/usr/share/nvim/sysinit.vim`，后者不建议由用户编辑。[[1]](<https://github.com/neovim/neovim/blob/master/runtime/doc/starting.txt#L439>) 默认情况下，前一个全局配置文件并不存在。如果你创建了前一个文件，那你可能也想在其中 source 后一个文件（如果你想获得它提供的功能：允许 Neovim 使用通过 pacman 安装的 Vim 包）。 

Neovim 兼容 Vim 大多数的选项，不过有一些选项特定于 Neovim。完整的 Neovim 选项列表参见 Neovim 的[帮助文件](<https://neovim.io/doc/user/options.html>)。 

Neovim 的数据目录位于 `~/.local/share/nvim/`，包含打开文件的交换文件、[ShaDa](<https://neovim.io/doc/user/starting.html#shada>)（共享数据）文件和插件的站点目录。 

从 Neovim 0.5 版本开始，可以使用 Lua 设置 Neovim（默认是 `~/.config/nvim/init.lua`），API 仍然很年轻，不过常见的配置开箱即用，无需过多配置。关于转换现有的配置的建议，参见 [[2]](<https://github.com/nanotee/nvim-lua-guide>)。当前，与 `init.vim` 相比，使用 `init.lua` 没有太多的优势，不过在使用得当时，Lua 可以小幅改善启动时间，并且由于配置简单，在使用以 Lua 编写的插件时会很有用。 

###  从 Vim 迁移

要将现有的 Vim 配置迁移到 Neovim，只需将 `~/.vimrc` 复制到 `~/.config/nvim/init.vim`。如果需要的话，将 `~/.vim/autoload/` 的内容复制到 `~/.local/share/nvim/site/autoload/`。 

###  在 Vim 和 Neovim 间共享配置

Neovim 将 `$XDG_CONFIG_HOME/nvim` 而不是 `~/.vim` 作为主要配置目录，并使用 `$XDG_CONFIG_HOME/nvim/init.vim` 而不是 `~/.vimrc` 作为主要配置文件。 

如果要继续使用 Vim，又希望在 Neovim 中 source 现有的 Vim 配置，参见 [nvim-from-vim](<https://neovim.io/doc/user/nvim.html#nvim-from-vim>) 或 `:help nvim-from-vim` Neovim 命令。 

####  加载插件

`/etc/xdg/nvim/sysinit.vim` 会自动 source 从[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")或 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中安装的 Vim 或 Neovim 插件，因此无需额外设置。大量的插件都可以在两个地方找到，但最好通过插件管理器添加插件，最常用的是 [vim-plug](<https://github.com/junegunn/vim-plug>)（可用于 Vim 和 Neovim）和 ~~[packer](<https://github.com/wbthomason/packer.nvim>)（使用 Lua 编写，只能用于 Neovim 0.5 或更新的版本）~~，[packer](<https://github.com/wbthomason/packer.nvim>)已停止维护，建议使用[lazy.nvim](<https://github.com/folke/lazy.nvim>)或[pckr.nvim](<https://github.com/lewis6991/pckr.nvim>)。这些插件管理器都可接受在 GitHub 分支到运行时命令这一范围内的深度配置。 

大多数为 Vim 编写的插件无需花费很多精力即可在 Neovim 上工作，不过不是每个为 Neovim 编写的插件都适用于 Vim，因此，如果你的目标是确保配置兼容两个版本，坚持使用 `init.vim` 或 `.vimrc`. 

##  提示与技巧

###  将 vi 和 vim 替换为 neovim

大部分情况下设置 `$VISUAL` 和 `$EDITOR` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")应该就足够了。 

一些应用程序可能硬编码 vi 或 vim 为默认编辑器，对于这种情况，安装 [neovim-symlinks](<https://aur.archlinux.org/packages/neovim-symlinks/>)AUR 或 [neovim-drop-in](<https://aur.archlinux.org/packages/neovim-drop-in/>)AUR。 

###  将 init.vim 设置为指向 .vimrc 的符号连接

因为 Neovim 与标准 Vim 大部分兼容，可以将 `nvim/init.vim` 设置为指向原来 `.vimrc` 的符号连接，从而保留旧的配置选项： 
    
    $ ln -s ~/.vimrc ~/.config/nvim/init.vim
    
如果想要某几行特定于每个版本，可以使用 `if` 块： 
    
    .vimrc
    
    if has('nvim')
        " 特定于 Neovim 的命令
    else
        " 特定于标准 Vim 的命令
    endif
    
###  真彩色支持

[这个项目](<https://github.com/CarloWood/neovim-true-color-scheme-editor>)的 `README` 文件解释了如何为语法高亮添加 24 位“真彩色”支持，以及如何使用取色器实时查看效果。包含作者为 C++ 提供的语法高亮（如果安装的话）。 

### Lastplace cursor support

如果你想保留光标的最后位置，[lastplace.lua](<https://github.com/neovim/neovim/issues/16339#issuecomment-1348133829>) 非常有用。只需将其放置在 `~/.config/nvim/plugin/` 或系统目录 `/usr/share/nvim/runtime/plugin/` 中即可。 

### Language Server Protocol

Neovim 内置 [Language Server Protocol（LSP）](<https://microsoft.github.io/language-server-protocol>)客户端，[nvim-lspconfig](<https://github.com/neovim/nvim-lspconfig>) 插件提供常见的配置。 

参见[语言服务器协议](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%8D%8F%E8%AE%AE.html> "语言服务器协议")。 

### Use as a pager

你可以用 `:Man` 命令打开手册页。要使用 Neovim 打开所有手册页，请将 `MANPAGER` [environment variable](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") 设置为 `nvim +Man!`. 

对其他帮助阅读程序的支持请安装 [nvimpager](<https://aur.archlinux.org/packages/nvimpager/>)AUR 或 [nvimpager-git](<https://aur.archlinux.org/packages/nvimpager-git/>)AUR 包并将 `PAGER` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable") 设置为 `nvimpager`. 

也可以试试 [page](<https://github.com/I60R/page>), 打包在 [page-git](<https://aur.archlinux.org/packages/page-git/>)AUR 中。 

##  问题解决

###  退出后光标没有恢复到之前的状态

如果退出 Neovim 后光标仍闪烁，参见 [neovim FAQ](<https://github.com/neovim/neovim/wiki/FAQ#cursor-style-isnt-restored-after-exiting-or-suspending-and-resuming-nvim>) 中的解决方案。 

##  参见

  * [GitHub 仓库](<https://github.com/neovim/neovim>)
  * [GitHub wiki](<https://github.com/neovim/neovim/wiki>)
