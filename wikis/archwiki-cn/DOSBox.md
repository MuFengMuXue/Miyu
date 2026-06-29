**翻译状态：**

  * 本文（或部分内容）译自 [DOSBox](<https://wiki.archlinux.org/title/DOSBox> "arch:DOSBox")，最近一次同步于 2022-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/DOSBox?diff=0&oldid=753632>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/DOSBox_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[DOSBox](<https://www.dosbox.com/>) 是一个x86 PC平台DOS模拟器，用于运行DOS游戏和DOS程序。 

##  安装

从[官方仓库](<../zh-cn/Official_repositories.html> "Official repositories") [安装](<../zh-cn/Pacman.html> "Pacman") [dosbox](<https://archlinux.org/packages/?name=dosbox>)包 或者从 AUR 安装其开发版本 [dosbox-svn](<https://aur.archlinux.org/packages/dosbox-svn/>)AUR 。您还可以选择其分支版本如： 

  * [dosbox-staging](<https://aur.archlinux.org/packages/dosbox-staging/>)AUR 旨在使代码库现代化
  * [dosbox-x](<https://aur.archlinux.org/packages/dosbox-x/>)AUR 更精确的模拟硬件

请注意原版 DOSBox 自2019年开始就没有发布过新的正式版，所以一些发行版会默认提供 dosbox-staging 。[[1]](<https://src.fedoraproject.org/rpms/dosbox>)

##  配置

无需初始化配置, 尽管DOSBox官方手册提供一个名为“dosbox.conf”的配置文件以供参阅。那个文件默认在你的`~/.dosbox`目录。 

你可以通过从`~/.dosbox`复制“dosbox.conf”，放在每个DOS程序所在目录，来创建一个新的配置文件。你也可以自动生成一个配置文件：只需在你希望的程序目录里不带任何参数运行`dosbox`： 
    
    $ dosbox
    
然后在DOS提示符中，输入： 
    
    Z:\> config -wc dosbox.conf
    
配置文件“dosbox.conf”会被保存到当前目录中。然后怎样配置随你便了。 

官方 DOSBox 百科[描述](<https://www.dosbox.com/wiki/Dosbox.conf>)了配置文件内容。 

##  使用

一种简单方法是将你的DOS游戏（或者其安装文件）放在一个目录里，然后运行 `dosbox`，将这个目录作为参数。例如： 
    
    $ dosbox ./game-folder/
    
你现在应该看到一个DOS提示符，你上面设定的那个目录已变成它的工作目录。然后你就可以运行你想运行的程序啦。 
    
    C:\> SETUP.EXE
    
##  提示

###  释放焦点

如果dosbox 抓取了你的鼠标输入，你可以按`CTRL+F10`来释放。 

###  在 DOS 游戏中播放音乐

有的游戏需要 [MIDI](<../zh-cn/MIDI.html> "MIDI") 合成器才能够正常播放音乐，但 DOSBox 并不提供对其的模拟。然而，DOSBox 可以使用现有的 MIDI 合成器，比如 [FluidSynth](<../zh-cn/FluidSynth.html> "FluidSynth") 和 [Timidity](</wzh/index.php?title=Timidity&action=edit&redlink=1> "Timidity（页面不存在）") 之类的软件合成器或者您自己的硬件合成器。 

##  另请参阅

  * <https://www.dosbox.com/> \- DOSBox官网。
  * <http://www.abandonia.com/> \- Abandonia: 大型老旧、废弃 DOS 游戏仓库。
  * <https://www.dosgames.com/> \- DosGames.com: 大型 DOS 游戏仓库。
