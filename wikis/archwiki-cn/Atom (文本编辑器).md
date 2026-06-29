[![](../File:User-trash-full.svg.png)](<../File:User-trash-full.svg.png>)**本文已被弃用。**

**本文所述教程或工具由于已经过时而被弃用，请使用其他替代方案：** 其他[文本编辑器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8> "文本编辑器") (在[Talk:Atom (文本编辑器)](<../zh-cn/Talk:Atom_\(%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8\).html>)讨论)

[Atom](<https://atom.io/>) 是一个由 GitHub 开发的开源文本编辑器，采用 MIT 证书授权方式。它主要用 CoffeeScript 和 Javascript 编写，并使用 Node.js 作为运行时环境。超过4,000个插件和1,000种主题使它具有很强的扩展性。它使用其内建的 apm 软件包管理器管理软件包和主题。 

##  安装

以下软件包都可用于安装Atom: 

  * [atom](<https://aur.archlinux.org/packages/atom/>)AUR
  * [atom-editor-git](<https://aur.archlinux.org/packages/atom-editor-git/>)AUR

##  插件

它的插件可以在Atom软件中或者使用apm命令完成安装，正确的apm命令语法是： 
    
    $ apm install _package_name1_ _package_name2_ _package_name3_ ...
    
一些包已经被预装到Atom中，未预装包中值得注意的有： 

  * [build](<https://atom.io/packages/build>) 使Atom可以编译源代码。
  * [git-plus](<https://atom.io/packages/git-plus>) 允许开发者在Atom中管理Git库。
  * [markdown-writer](<https://atom.io/packages/markdown-writer>) 将Atom变为一个有效的Markdown编辑器。
  * [script](<https://atom.io/packages/script>) 使Atom可以基于文件名运行脚本。

##  问题处理

###  环境变量设置未被使用

你可能会遇到一些因为软件包使用环境变量而引起的问题，像[go-plus](<https://atom.io/packages/go-plus>) (`$GOPATH not found`)。而且，问题只有在通过文件管理器打开Atom时才会出现（这是由DBUS引发的，因而不会使用在 `.bashrc` 中定义的环境变量）。 

你可以通过[Systemd/用户#环境变量](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F> "Systemd/用户")为DBUS-spawned进程创建可用的环境变量 

关于这个问题的更多内容，请参考 [Environment variables#Per user](<../zh-cn/Environment_variables.html#Per_user> "Environment variables"). 

###  无法删除文件

[Electron](<https://electron.atom.io/>) 程序默认使用 `gvfs-trash` 删除文件，不使用 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的用户可以使用 `ELECTRON_TRASH` 环境变量设置删除工具。 

例如要在 [Plasma](<../zh-cn/KDE.html> "Plasma") 中删除文件: 
    
    $ ELECTRON_TRASH=kioclient5 atom
    
目前 Electron 支持 `kioclient5`, `kioclient`, `trash-cli` 和 `gvfs-trash` (默认)。 更多信息请参考 [Github 页面](<https://github.com/electron/electron/pull/7178>). 

###  启动时黑屏

在某些显卡，例如 [VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") 客户系统中，只有使用 `--disable-gpu` 禁用硬件加速的显卡，或者编辑配置文件 `.atom/config.cson` 并在`editor`中增加或更改 `useHardwareAcceleration: false`，Atom 才会渲染窗口。 

###  无拼写检查

请确保 hunspell 和[需要的字典](<https://archlinux.org/packages/?sort=&q=hunspell&maintainer=&flagged=>)已经安装. 
