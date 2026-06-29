**翻译状态：**

  * 本文（或部分内容）译自 [Dvorak](<https://wiki.archlinux.org/title/Dvorak> "arch:Dvorak")，最近一次同步于 2022-11-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dvorak?diff=0&oldid=716243>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dvorak_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

From [Wikipedia](<https://en.wikipedia.org/wiki/Dvorak_Simplified_Keyboard> "wikipedia:Dvorak Simplified Keyboard"): 

    Dvorak 是被 August Dvorak 和 William Dealey 于 1936 申请专利的键盘布局， 和事实标准的 QWERTY 布局有很大不同. Dvorak 的支持者声称这种布局需要更少的手指运动，可以间很少错误率、增加打字速度、减少重复导致的疲劳或就是比 QWERTY 用得舒服。

本文是一个快速参考手册，可以设置你的键盘映射从qwerty转换到Dvorak. 

##  设置 Dvorak 键盘布局

设置方法请阅读[终端设置](<../zh-cn/Keyboard_configuration_in_console.html> "Keyboard configuration in console")和 [Xorg 设置](</wzh/index.php?title=Keyboard_configuration_in_Xorg&action=edit&redlink=1> "Keyboard configuration in Xorg（页面不存在）")。 

虚拟终端中的 dvorak 和区域键盘被合并成一个键盘映射。但是 Xorg 将 dvorak 作为区域键盘的变体。 

虚拟终端中的 `us` Dvorak 键盘映射为： 

  * `dvorak`, 标准
  * `dvorak-l`, 左手布局
  * `dvorak-r`, 右手布局
  * `dvorak-programmer`, 程序员 Dvorak

Xorg 的 `us` Dvorak 键盘映射为： 

  * `dvorak`, 标准
  * `dvorak-l`, 左手布局
  * `dvorak-r`, 右手布局
  * `dvp`, 程序员 Dvorak
  * `dvorak-intl`, 国际 Dvorak
  * `dvorak-classic`
  * `dvorak-alt-intl`

下面布局可以同时在终端和 Xorg 中使用： 

  * `dvorak`, 标准 Dvorak
  * `dvorak-l`, 左手布局
  * `dvorak-r`, 右手布局

**注意：** 终端有单独的键盘映射，但是 Xorg 有 `us` 布局变体，需要传递给 `XkbVariant` 变量，参考 [Keyboard configuration in Xorg#Setting keyboard layout](</wzh/index.php?title=Keyboard_configuration_in_Xorg&action=edit&redlink=1> "Keyboard configuration in Xorg（页面不存在）")。

##  国际用户

### Franch

法文变体为 [Bépo](</wzh/index.php?title=B%C3%A9po&action=edit&redlink=1> "Bépo（页面不存在）")，有单独的文章介绍。 

### Swedish

Swedish 用户可以选择使用 swedish "dvorak 版本"，被称为 svorak，要将 X 切换到 svorak，并不需要从 www.aoeu.info 下载额外文件。 

### Spanish

要使用西班牙 dvorak 变体，使用 `dvorak-es` 替换 `dvorak`。 

在 Xorg 中将 `XkbLayout` 设置为 `es`， `XkbVariant` 设置为 `dvorak`. 

### United Kingdom

In console, specify `dvorak-ukp` (available from [dvorak-ukp](<https://aur.archlinux.org/packages/dvorak-ukp/>)AUR) instead of `dvorak` to use the United Kingdom dvorak variant with ISO/IEC 9995-1 punctuation. 

In Xorg, specify `gb` as `XkbLayout` and `dvorakukp` as `XkbVariant`. 

##  特定程序的重新绑定

下面是一些以键盘为中心程序的重新绑定方式，因为 Dvorak 使用了更多的右侧键盘，这里使用 `htns` 作为主要按键. 

### Vim
    
    ~/.vimrc
    
    noremap h <left>
    noremap t <down>
    noremap n <up>   
    noremap s <right>
    
    noremap l n
    noremap L N
    
**注意：** 这里 n 表示 _n search repeat command_ ，而不是 _按键 n_. See `:help n`

如果追求极限配置，请参考 [Vim Wiki](<https://vim.fandom.com/wiki/Using_Vim_with_the_Dvorak_keyboard_layout>). 

### Mutt
    
    ~/.config/mutt/muttrc
    
    bind index t next-entry
    bind index n previous-entry
    bind index s display-message
    
    bind index G last-entry
    bind index gg first-entry
    
    bind pager,attach h exit
    bind pager t next-line
    bind pager n previous-line
    bind pager s view-attachments
    
    bind browser h goto-parent
    bind pager,browser gg top-page
    bind pager,browser G bottom-page
    
### Less
    
    ~/.lesskey
    
    t         forw-line
    n         back-line
    l         repeat-search 
    L         reverse-search
    
需要运行 `lesskey` 之后才能生效。 

### Zathura
    
    ~/.config/zathura/zathurarc
    
    map h scroll left
    map t scroll down
    map n scroll up
    map s scroll right
    
    map l search forward
    map L search backward
    
### Qutebrowser
    
    ~/.config/qutebrowser/config.py
    
    config.bind('h', 'scroll left')
    config.bind('t', 'scroll down')
    config.bind('n', 'scroll up')
    config.bind('s', 'scroll right')
    
    config.bind('H', 'back')
    config.bind('T', 'tab-prev')
    config.bind('N', 'tab-next')
    config.bind('S', 'forward')
    
    config.bind('l', 'search-next')
    config.bind('L', 'search-prev')
    
    config.bind('e', 'hint all')
    
##  打字练习软件

  * GUI: [ktouch](<https://archlinux.org/packages/?name=ktouch>)包 (包含了英语、法语、德语和西班牙语的 Dvorak 课程)
  * GUI: [klavaro](<https://archlinux.org/packages/?name=klavaro>)包 Dvorak 课程: (BG; BR; DE_neo2; EO; FR; FR_bépo; TR; UK; US; US_BR; US_ES; US_SE)
