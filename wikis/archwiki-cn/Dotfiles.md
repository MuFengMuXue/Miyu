**翻译状态：**

  * 本文（或部分内容）译自 [Dotfiles](<https://wiki.archlinux.org/title/Dotfiles> "arch:Dotfiles")，最近一次同步于 2025-1-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dotfiles?diff=0&oldid=825943>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dotfiles_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [XDG 基本目录](<../zh-cn/XDG_%E5%9F%BA%E6%9C%AC%E7%9B%AE%E5%BD%95.html> "XDG 基本目录")
  * [X 资源](<../zh-cn/X_%E8%B5%84%E6%BA%90.html> "X 资源")

用户对于程序的配置通常存储在所谓的[点文件](<https://en.wikipedia.org/wiki/dotfile> "wikipedia:dotfile")（以 `.` 开头的文件）中。通常的做法是用[版本控制系统](<../zh-cn/Category:%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F.html> "版本控制系统")（如 [Git](<../zh-cn/Git.html> "Git") ）来管理点文件，以跟踪其变化，并在不同的主机上同步。有许多管理点文件的方法。例如，直接跟踪主目录中的点文件；或者将其放在子文件夹中，用 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell") 脚本或[专用工具](<#%E5%B7%A5%E5%85%B7>)进行管理。除了说明如何管理你的点文件之外，本文章还包含了一个来自 Arch Linux 用户的[点文件配置库](<#%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93>)列表。 

##  使用 Git 跟踪点文件

直接使用 Git 跟踪点文件的好处是它只涉及[Git](<../zh-cn/Git.html> "Git")而不涉及符号链接。坏处则是对于[特定主机的配置](<#%E7%89%B9%E5%AE%9A%E9%85%8D%E7%BD%AE>)通常需要多个[分支](<../zh-cn/Git.html#Branching> "Git")来合并。 

实现这一需求最简单的方式是直接在 home 目录初始化一个 [Git](<../zh-cn/Git.html> "Git") 仓库，并在[gitignore(5)](<https://man.archlinux.org/man/gitignore.5>)文件中使用`*`匹配所有文件来忽视它们。 但是两个弊端也随之而来：一是当你的 home 目录下有其他 Git 仓库时，就会难以应对（比如说你如果你忘记初始化而直接对点文件仓库进行操作的时候）。二是你很难确定当前目录下的那些文件是没有被跟踪的（因为他们已经被忽略了)。 

为避免上述两个弊端，一个很受欢迎的替代方法是“裸仓库别名法”，它的原文链接在此：[Ask Hacker News: What do you use to manage your dotfiles?](<https://news.ycombinator.com/item?id=11071754>)，它只要3个命令就可轻松完成设置： 
    
    $ git init --bare ~/.dotfiles
    $ alias dotfiles='/usr/bin/git --git-dir="$HOME/.dotfiles/" --work-tree="$HOME"'
    $ dotfiles config status.showUntrackedFiles no
    
**注意：** 通常情况下， 点文件都是默认权限，但如果某些配置一定要配置特定权限，请另寻他法。（git 不支持存储权限信息）([Discussion](</wzh/index.php?title=Talk:Dotfiles&action=edit&redlink=1> "Talk:Dotfiles（页面不存在）"))

你可以采用下面的命令在新系统中复制点文件： 
    
    $ git clone --bare <git-repo-url> $HOME/.dotfiles
    $ alias dotfiles='/usr/bin/git --git-dir="$HOME/.dotfiles/" --work-tree="$HOME"'
    $ dotfiles checkout
    $ dotfiles config --local status.showUntrackedFiles no
    
  * 如果这时有一些点文件已经被覆盖了，你可能会遇到类似下面这样的错误：

    $ dotfiles checkout
    error: The following untracked working tree files would be overwritten by checkout:
        .bashrc
        .gitignore
    Please move or remove them before you can switch branches.
    Aborting
    
    你应该使用 `$ dotfiles checkout -f`重写已经存在的文件，或是用下面更安全的脚本方法备份所有文件，记得使用`checkout`：
    
    mkdir -p .dotfiles-backup && \
    dotfiles checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | \
    xargs -I{} mv {} .dotfiles-backup/{}
    
在这之后你可以用 alias命令 去管理点文件。如果你使用的是 Bash，只需要安装 [bash-complete-alias](<https://aur.archlinux.org/packages/bash-complete-alias/>)AUR 后就可以使用补全功能，最后将别名和下面的一行命令放在你的`~/.bashrc`中。 
    
    $ complete -F _complete_alias dotfiles
    
另一种在bash中使用补全功能的方法，在你的`~/.bashrc`中加入下面的命令（擅自[[1]](<https://askubuntu.com/a/642778>)）： 
    
    source /usr/share/bash-completion/completions/git
    __git_complete config __git_main
    
**提示：** 关于避免以外提交敏感信息的方式，请看 [Git#Filtering confidential information](<../zh-cn/Git.html#Filtering_confidential_information> "Git").

##  特定设备相关的配置

你可能有很多台设备, 在这些设备之间同步点文件是一个很常见的问题，我们将其称之为特定设备相关的配置。 

有了 [Git](<../zh-cn/Git.html> "Git") 工具的帮助，我们可以通过以下方式解决这个问题：我们可以维护一个包含通用配置文件的主分支，同时为设备间不同的特定配置文件创建单独的分支。维护时将通用配置文件的变动提交到前者，而将与设备相关的配置文件提交到后者。也就是说，每个设备的专用分支都是在保持通用分支更新的基础上单独建立的。 

某些配置文件中，比如在 [shell configuration files](<../zh-cn/Command-line_shell.html#Configuration_files> "Command-line shell") 中，可以使用条件逻辑判断不同的设备。比如，[Bash](<../zh-cn/Bash.html> "Bash") 脚本 (即`.bashrc`) 中可以根据不同的主机名（或者其他特征如类型、自定义变量等等）应用不同的配置。 
    
    if [[ "$(hostname)" == "archlaptop" ]]; then
        # laptop specific commands here
    else
        # desktop or server machine commands
    fi
    
同样也可以用 [.Xresources](</wzh/index.php?title=.Xresources&action=edit&redlink=1> ".Xresources（页面不存在）").[[2]](<https://jnrowe.github.io/articles/tips/Sharing_Xresources_between_systems.html>) 实现类似功能。 

如果你觉得设置 Git 分支太麻烦，也可以使用支持文件分组的[工具](<#%E5%B7%A5%E5%85%B7>)，或者使用处理工具使管理更加灵活。 

##  工具

文件分组
    也就是将配置文件归纳成组的方法。
处理
    一些工具对配置文件进行处理，使其能够根据主机情况进行定制。
名称 | 包 | 语言 | 文件分组 | 处理   
---|---|---|---|---  
[dotbot](<https://github.com/anishathalye/dotbot>) |  [dotbot](<https://aur.archlinux.org/packages/dotbot/>)AUR | Python  | 配置文件  | 无   
[chezmoi](<https://github.com/twpayne/chezmoi>) | [chezmoi](<https://archlinux.org/packages/?name=chezmoi>)包 | Go | 基于目录 | Go 模板   
[dot-templater](<https://github.com/kesslern/dot-templater>) | [dot-templater-git](<https://aur.archlinux.org/packages/dot-templater-git/>)AUR | Rust | 基于目录 | 特定语法   
[toml-bombadil](<https://github.com/oknozor/toml-bombadil>) |  [toml-bombadil](<https://archlinux.org/packages/?name=toml-bombadil>) | Rust  | 基于目录  | tera   
[dotdrop](<https://deadc0de.re/dotdrop/>) | [dotdrop](<https://aur.archlinux.org/packages/dotdrop/>)AUR | Python | 配置文件 | Jinja2   
[dotfiles](<https://github.com/jbernard/dotfiles>) | [dotfiles](<https://aur.archlinux.org/packages/dotfiles/>)AUR | Python | [无](<https://github.com/jbernard/dotfiles/pull/24>) | 无   
[dotter](<https://github.com/SuperCuber/dotter>) | [dotter-rs](<https://aur.archlinux.org/packages/dotter-rs/>)AUR | Rust | 配置文件 | Handlebars   
[dt-cli](<https://dt.cli.rs>) | [dt-cli](<https://aur.archlinux.org/packages/dt-cli/>)AUR | Rust | 配置文件 | Handlebars   
[GNU Stow](<https://www.gnu.org/software/stow/>) | [stow](<https://archlinux.org/packages/?name=stow>)包 | Perl | 基于目录[[3]](<http://brandon.invergo.net/news/2012-05-26-using-gnu-stow-to-manage-your-dotfiles.html>) | 无   
[Mackup](<https://github.com/lra/mackup>) | [mackup](<https://aur.archlinux.org/packages/mackup/>)AUR | Python | 自动按应用 | 无   
[mir.qualia](<https://github.com/darkfeline/mir.qualia>) | [mir.qualia](<https://aur.archlinux.org/packages/mir.qualia/>)AUR | Python | 无 | 自定义块   
[rcm](<https://github.com/thoughtbot/rcm>) | [rcm](<https://aur.archlinux.org/packages/rcm/>)AUR | Shell | 基于目录（按主机或标签） | 无   
[yas-bdsm](<https://github.com/sebastiancarlos/yas-bdsm>) | \-  | Shell  | 基于目录  | 无   
  
###  Git 的替代品

如果你不喜欢 [Git](<../zh-cn/Git.html> "Git") ，可以尝试下列工具，它们或多或少可以看作是版本控制系统。 

名称 | 包 | 语言 | 文件分组 | 处理   
---|---|---|---|---  
[dotbare](<https://github.com/kazhala/dotbare>) | [dotbare](<https://aur.archlinux.org/packages/dotbare/>)AUR | Shell ([fzf](<https://archlinux.org/packages/?name=fzf>)包) | repository-wise | 无   
[dotgit](<https://github.com/kobus-v-schoor/dotgit>) | [dotgit](<https://aur.archlinux.org/packages/dotgit/>)AUR | Python | 基于文件名称 | 无   
[homeshick](<https://github.com/andsens/homeshick>) | [homeshick-git](<https://aur.archlinux.org/packages/homeshick-git/>)AUR | Bash | repository-wise | 无   
[homesick](<https://github.com/technicalpickles/homesick>) | – | Ruby | repository-wise | 无   
[Pearl](<https://github.com/pearl-core/pearl>) | [pearl-git](<https://aur.archlinux.org/packages/pearl-git/>)AUR | Python | repository-wise | 无   
[vcsh](<https://github.com/RichiH/vcsh>) | [vcsh](<https://archlinux.org/packages/?name=vcsh>)包 | Shell | repository-wise | 无   
[yadm](<https://yadm.io>)(1) | [yadm](<https://archlinux.org/packages/?name=yadm>)包 | Python | 基于文件名称  
(按类/操作系统/发行版/主机名称/用户)[[4]](<https://yadm.io/docs/alternates>) | 内置模板/Jinja2/ESH[[5]](<https://yadm.io/docs/templates>)  
（可选）   
[dfm](<https://github.com/justone/dotfiles>) |  [dfm](<https://aur.archlinux.org/packages/dfm/>)AUR | Perl  | repository-wise  | 无   
  
  1. 支持以 [GPG](<../zh-cn/GnuPG.html> "GPG") 或 OpenSSL 对文件加密。 [[6]](<https://yadm.io/docs/encryption>)

##  用户仓库

**提示：** 中文社区有人整理了来自中文社区用户的 dotfiles 集锦：[archlinuxcn-dotfiles-collection](<https://github.com/zjuyk/archlinuxcn-dotfiles-collection>)。

**注意：** 这个表格用于提供点文件的参考和例子，如果你想将自己的点文件提交到此，请确保它们整洁、注释完善且不过时。

**警告：** 这些点文件未经Arch Linux维护团队验证，请自行承担使用风险。

作者 | Shell | WM / DE | 编辑器 | 终端 | 终端复用 | 音频 | 资源监视 | 邮件 | IRC | 文件管理 | RSS 阅读   
---|---|---|---|---|---|---|---|---|---|---|---  
[adamperkowski](<https://github.com/adamperkowski/dwm>) | Zsh  | dwm  | Neovim  | Kitty  | tmux  | mpv  | 自定义  |  |  [weechat](<https://github.com/benmezger/dotfiles/blob/main/dot_weechat/>) |  |   
[alfunx](<https://github.com/alfunx/.dotfiles>) | zsh | awesome | vim | kitty | tmux | ncmpcpp/mpd | htop/lain | thunderbird |  |  |   
[Ambrevar](<https://gitlab.com/Ambrevar/dotfiles>) | Eshell | EXWM | Emacs | Emacs (Eshell) | Emacs TRAMP + dtach | EMMS | conky/dzen | mu4e | Circe |  |   
[ananthu](<https://github.com/ask1234560/dotfiles_bspwm>) | zsh | bspwm | neovim | alacritty |  | mpv | htop, polybar | neomutt | weechat | ranger |   
[awal](<https://github.com/awalGarg/dotfiles>) | fish | i3 | vim | st | tmux |  | i3status |  | The Lounge |  |   
[ayekat](<https://github.com/ayekat/localdir>) | zsh | karuiwm | vim | rxvt-unicode | tmux | ncmpcpp/mpd | karuibar | mutt | irssi |  |   
[bachoseven](<https://github.com/BachoSeven/dotfiles>) | zsh | [dwm](<https://github.com/BachoSeven/dwm>) | neovim | [st](<https://github.com/BachoSeven/st>) |  | ncmpcpp | bottom | neomutt | weechat | lf |   
[bamos](<https://github.com/bamos/dotfiles>) | zsh | i3/xmonad | vim/emacs | rxvt-unicode | tmux | mpv/cmus | conky/xmobar | mutt | ERC |  |   
[brisbin33](<https://github.com/pbrisbin/dotfiles>) | [zsh](<https://github.com/pbrisbin/oh-my-zsh>) | [xmonad](<https://github.com/pbrisbin/xmonad-config>) | [vim](<https://github.com/pbrisbin/vim-config>) | rxvt-unicode | screen |  | dzen | [mutt](<https://github.com/pbrisbin/mutt-config>) | [irssi](<https://github.com/pbrisbin/irssi-config>) |  |   
[BVollmerhaus](<https://gitlab.com/BVollmerhaus/dotfiles>) | [fish](<https://gitlab.com/BVollmerhaus/dotfiles/-/tree/master/config/fish>) | [i3-gaps](<https://gitlab.com/BVollmerhaus/dotfiles/blob/master/config/i3/config>) | [kakoune](<https://gitlab.com/BVollmerhaus/dotfiles/blob/master/config/kak/kakrc>) | [kitty](<https://gitlab.com/BVollmerhaus/dotfiles/-/blob/master/config/kitty/kitty.conf>) |  |  | [polybar](<https://gitlab.com/BVollmerhaus/dotfiles/blob/master/config/polybar/config>) |  |  | [ranger](<https://gitlab.com/BVollmerhaus/dotfiles/-/tree/master/config/ranger>) |   
[christian-heusel](<https://github.com/christian-heusel/dotfiles>) |  [Zsh](<https://github.com/pbrisbin/oh-my-zsh>) | i3  | Neovim  | st / terminator  | byobu / tmux  |  | htop  | neomutt/thunderbird  | weechat  | nemo / rangern  |   
[cinelli](<https://github.com/cinelli/dotfiles>) | zsh | dwm | vim | termite-git |  | pianobar | htop | mutt-kz | weechat |  |   
[dikiaap](<https://github.com/dikiaap/dotfiles>) | zsh | i3-gaps | neovim | alacritty | tmux |  | i3blocks |  |  | nnn |   
[Earnestly](<https://github.com/Earnestly/dotfiles>) | zsh | i3/orbment | vim/emacs | termite | tmux | mpd | conky | mutt | weechat |  |   
[ErikBjare](<https://github.com/ErikBjare/dotfiles>) | zsh | xmonad/xfce4 | vim | terminator | tmux |  | xfce4-panel |  | weechat |  |   
[falconindy](<https://github.com/falconindy/dotfiles>) | bash | i3 | vim | rxvt-unicode |  | ncmpcpp | conky | mutt |  |  |   
[filiparag](<https://github.com/filiparag/dotfiles>) | fish | bspwm | vim | alacritty | tmux | mpv, [playerctl](<https://github.com/altdesktop/playerctl>) | htop, polybar | [mail-notification](<https://www.nongnu.org/mailnotify/>) |  |  [pcmanfm](<https://wiki.lxde.org/en/PCManFM>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ] |   
[gardenapple](<https://git.sr.ht/~gardenapple/dotfiles>) | zsh | sway | neovim | kitty |  |  | htop | [aerc](<https://aerc-mail.org/>) |  |  |   
[graysky](<https://github.com/graysky2/configs/tree/master/dotfiles>) | zsh | xfce4 | vim | terminal |  | ncmpcpp | custom | thunderbird |  |  |   
[hugdru](<https://github.com/hugdru/dotfiles>) | zsh | awesome | neovim | rxvt-unicode | tmux |  |  | thunderbird | weechat |  |   
[insanum](<https://github.com/insanum/dotfiles>) | bash | herbstluftwm | vim | evilvte | tmux |  | dzen | mutt-kz |  |  |   
[isti115](<https://github.com/isti115/dotfiles>) |  [pwsh](<https://github.com/Isti115/dotfiles/blob/master/.config/powershell/Microsoft.PowerShell_profile.ps1>) |  [sway](<https://github.com/Isti115/dotfiles/blob/master/.config/sway/config>) |  [neovim](<https://github.com/Isti115/dotfiles/tree/master/.config/nvim>) |  [alacritty](<https://github.com/Isti115/dotfiles/blob/master/.config/alacritty/alacritty.yml>) | tmux  |  [mpv](<https://github.com/Isti115/dotfiles/tree/master/.config/mpv>) / playerctl  |  [waybar](<https://github.com/Isti115/dotfiles/tree/master/.config/waybar>) / htop / ytop  |  |  |  [ranger](<https://github.com/Isti115/dotfiles/tree/master/.config/ranger>) |   
[jasonwryan](<https://hg.sr.ht/~jasonwryan/shiv>) | bash/zsh | dwm | vim | rxvt-unicode | tmux | ncmpcpp | custom | mutt | irssi |  |   
[jdevlieghere](<https://github.com/JDevlieghere/dotfiles/>) | zsh | xmonad | vim | terminal | tmux |  | htop | mutt | weechat |  |   
[jelly](<https://github.com/jelly/Dotfiles>) | zsh | i3 | vim | termite | tmux | ncmpcpp |  | mutt-kz-git | weechat |  |   
[JonasDe](<https://github.com/JonasDe/dotfiles>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ] | zsh | i3 | vim | rxvt-unicode | tmux |  |  |  |  |  |   
[Jorengarenar](<https://github.com/Jorengarenar/dotfiles>) |  [sh](<https://github.com/Jorengarenar/dotfiles/tree/master/shell>)/[Bash](<https://github.com/Jorengarenar/dotfiles/blob/master/bashrc>) | [i3](<https://github.com/Jorengarenar/dotfiles/tree/master/i3>) | [Vim](<https://github.com/Jorengarenar/dotfiles/tree/master/vim>) | [xterm](<https://github.com/Jorengarenar/dotfiles/blob/master/X11/Xresources>) |  [tmux](<https://github.com/Jorengarenar/dotfiles/blob/master/tmux.conf>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ] | [mpv](<https://github.com/Jorengarenar/dotfiles/tree/master/mpv>) | [htop](<https://github.com/Jorengarenar/dotfiles/blob/master/htoprc>) | [aerc](<https://github.com/Jorengarenar/dotfiles/tree/master/aerc>) | [WeeChat](<https://github.com/Jorengarenar/dotfiles/tree/master/weechat>) | [ranger](<https://github.com/Jorengarenar/dotfiles/blob/master/ranger.conf>) | QuiteRSS   
[MarkusZoppelt](<https://github.com/markuszoppelt/dotfiles>) | zsh | gnome | vim | terminal | tmux |  |  |  |  |  |   
[maximbaz](<https://github.com/maximbaz/dotfiles>) | zsh | sway | kakoune | kitty |  |  | waybar | neomutt |  | nnn |   
[mehalter](<https://git.mehalter.com/mehalter/dotfiles>) | zsh | i3-gaps | neovim | termite | tmux | cmus | gotop | neomutt | weechat | ranger |   
[meskarune](<https://github.com/meskarune/.dotfiles>) | bash | herbstluftwm | vim | rxvt-unicode | screen |  | conky |  | weechat |  |   
[neersighted](<https://github.com/neersighted/dotfiles>) | fish | i3 | neovim | alacritty | tmux | ncmpcpp |  |  |  |  |   
[nimaipatel](<https://github.com/nimaipatel/dotfiles>) | fish | awesome | neovim | alacritty |  | ncmpcpp |  |  |  |  |   
[oibind](<https://github.com/oibind/dotfiles>) | fish | awesome | neovim | st | tmux |  | htop-vim |  | weechat | lf |   
[OK100](<https://github.com/ok100/configs>) | bash | dwm | vim | rxvt-unicode |  | cmus | conky, dzen | mutt | weechat |  |   
[orhun](<https://github.com/orhun/dotfiles>) | bash | i3-gaps | vsc | alacritty |  |  | i3status |  | weechat | tere |   
[pablox-cl](<https://github.com/pablox-cl/dotfiles>) | zsh (zplug) | gnome3 | neovim | kitty |  |  |  |  |  |  |   
[peterzuger](<https://gitlab.com/peterzuger/dotfiles>) | zsh | i3-gaps | emacs | rxvt-unicode | screen | moc | htop |  |  |  |   
[potamides](<https://github.com/potamides/dotfiles>) | bash | awesome | neovim | termite | tmux | ncmpcpp | conky,htop | mutt | weechat | ranger |   
[reisub0](<https://github.com/reisub0/dot>) | fish | qtile | neovim | kitty |  | mpd | conky |  |  |  |   
[Scrumplex](<https://git.sr.ht/~scrumplex/dotfiles>) | fish | sway | neovim | kitty |  | ncmpcpp / pipewire | waybar | aerc |  | ranger |   
[sistematico](<https://github.com/sistematico/majestic>) | zsh/fish/bash | [i3-gaps](<https://github.com/Airblader/i3>) | vim/nano | termite | tmux | ncmpcpp | polybar | mutt | weechat |  |   
[sitilge](<https://git.sitilge.id.lv/sitilge/dotfiles>) | zsh | sway | neovim | alacritty |  |  | htop | thunderbird |  |  |   
[thecashewtrader](<https://git.sr.ht/~thecashewtrader/dotfiles>) | Eshell | EXWM | Emacs | Emacs (VTerm) | Emacs | Bongo | htop | mu4e | ERC | Dired | Elfeed   
[thiagowfx](<https://github.com/thiagowfx/.dotfiles>) | bash/zsh | i3 | vim | alacritty | tmux | playerctl | i3status |  |  | ranger |   
[tuurep](<https://github.com/tuurep/dotfiles>) | bash | openbox | neovim | alacritty | tmux |  | polybar |  |  |  |   
[vodik](<https://github.com/vodik/dotfiles>) | zsh | xmonad | vim | termite-git | tmux | ncmpcpp | custom | mutt | weechat |  |   
[w0ng](<https://github.com/w0ng/dotfiles>) | zsh | dwm | vim | rxvt-unicode | tmux | ncmpcpp | custom | mutt | irssi |  |   
[whitelynx](<https://github.com/whitelynx/dotfiles>) | fish | i3 | neovim | kitty |  |  | i3pystatus |  |  |  |   
[whynothugo](<https://git.sr.ht/~whynothugo/dotfiles>) | zsh | sway | neovim | alacritty |  | mpv | waybar, top | neomutt |  | nemo |   
[wryonik](<https://github.com/wryonik/dotfiles>) | zsh | i3-gaps-rounded | vim | terminator |  | cmus | htop, i3blocks, gotop |  |  | ranger, nautilus |   
  
##  另见

  * [gregswiki:DotFiles](<https://mywiki.wooledge.org/DotFiles> "gregswiki:DotFiles")
  * [XMonad Config Archive](<https://wiki.haskell.org/Xmonad/Config_archive>)
  * [dotshare.it](<http://dotshare.it>)
  * [dotfiles.github.io](<https://dotfiles.github.io/>)
  * [terminal.sexy](<https://terminal.sexy/>) \- Terminal color scheme designer
