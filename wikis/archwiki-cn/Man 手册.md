**翻译状态：**

  * 本文（或部分内容）译自 [Man page](<https://wiki.archlinux.org/title/Man_page> "arch:Man page")，最近一次同步于 2025-07-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Man_page?diff=0&oldid=841430>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Man_page_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [在终端输出彩色#man](<../zh-cn/%E5%9C%A8%E7%BB%88%E7%AB%AF%E8%BE%93%E5%87%BA%E5%BD%A9%E8%89%B2.html#man> "在终端输出彩色")

[man 手册页](<https://en.wikipedia.org/wiki/Man_page> "wikipedia:Man page")，指 "manual pages"，是类 UNIX 系统的标准手册工具，包括[Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux")。这个命令常常被显示为 [man(1)](<https://man.archlinux.org/man/man.1>)。 

man手册页被设计成独立的文档，不能引用其它手册页面，于是这限制了它们在讨论相似话题时指向其它的手册页面。这与支持超链接的 [Info 文档](<../zh-cn/GNU.html#Texinfo> "GNU")形成鲜明对比，[GNU](<../zh-cn/GNU.html> "GNU")正在将 man 手册替换成 info 文档。 

##  安装

[man-db](<https://archlinux.org/packages/?name=man-db>)包 提供了 _man_ 命令，[less](<../zh-cn/Core_utilities.html#Essentials> "Core utilities") 是 _man_ 的默认分页器。[mandoc](<https://archlinux.org/packages/?name=mandoc>)包 同样可供使用。 

[man-pages](<https://archlinux.org/packages/?name=man-pages>)包 既提供Linux和POSIX.1的man页面。[[1]](<https://gitlab.archlinux.org/archlinux/packaging/packages/man-pages/-/blob/main/PKGBUILD#L64-67>)

中文用户可以选择安装中文版本，其余语言版本见[英文wiki](<https://wiki.archlinux.org/title/Man_page#Installation> "en:Man page"): 

  * [man-pages-zh_cn](<https://archlinux.org/packages/?name=man-pages-zh_cn>)包 简体中文版本
  * [man-pages-zh_tw](<https://archlinux.org/packages/?name=man-pages-zh_tw>)包 繁体中文版本

你也可以搜索所有可用的本地man页面在[官方仓库](<https://archlinux.org/packages/?sort=&q=man-pages>)和[AUR](<https://aur.archlinux.org/packages?K=man-pages>)

##  阅读手册页

通过以下命令阅读man手册页： 
    
    $ man _手册名_
    
man手册页分为很多[段落](<https://en.wikipedia.org/wiki/Man_page#Manual_sections> "wikipedia:Man page")。每个段落有一段介绍，像[intro(1)](<https://man.archlinux.org/man/intro.1>), [intro(2)](<https://man.archlinux.org/man/intro.2>)等等。完整的列表可以参考:[man-pages(7) § Sections of the manual pages](<https://man.archlinux.org/man/man-pages.7#Sections_of_the_manual_pages>) . 

man手册页通过名称和所属分类标识。有些不同分类的man手册页名字可能相同，比如 [man(1)](<https://man.archlinux.org/man/man.1>) 和 [man(7)](<https://man.archlinux.org/man/man.7>)，这时需要额外指明分类以访问需要的手册。例如： 
    
    $ man 5 passwd
    
会显示有关文件`/etc/passwd`，而非命令 `passwd`，的内容。 

相同地，我们也可以使用man页面后用一'.'分开，并追加一段落号: 
    
    $ man passwd.5
    
##  搜索手册页

如果用户压根儿不知道要查阅的手册的名称，该怎么办呢？没事，通过 `-k` 或者 `--apropos` 参数就可以按给定关键词搜索相关手册。例如，要查阅有关密码的手册（“password”）： 

关键词搜索特性是从一个专用的缓存生成的。默认情况下你没有这个缓存，所以无论你搜什么，都会提示你 _nothing appropriate_ 。你可以通过下面的命令来生成这个缓存： 
    
    # mandb
    
每当你安装新的manpage之后都需要运行这个命令，缓存才会更新。 

现在你可以开始搜索了。例如，要查阅有关密码的手册（“password”）,可以使用下面的命令: 
    
    $ man -k password
    $ man --apropos password
    $ apropos password
    
关键字可以使用正则表达式。 

如果你想全文搜索的话，你可以用`-K`选项： 
    
    $ man -K password
    
通过`whatis`命令，可以只显示需要的man手册页的简要信息。如果只是想获取对命令 ls 的简要说明，使用以下命令： 
    
    $ whatis ls
    
    ls (1p)              - list directory contents
    ls (1)               - list directory contents
    
##  页面宽度

man页面宽度由环境变量`MANWIDTH` 来控制。 

如果终端中的列数很小（比如窗口宽度很小），换行可能会出现错误。这会很影响你阅读。你可以通过设置在`man`调用时设置`MANWIDTH`来修复。如[Bash](<../zh-cn/Bash.html> "Bash")：
    
    ~/.bashrc
    
    man() {
        local width=$(tput cols)
        [ $width -gt $MANWIDTH ] && width=$MANWIDTH
        env MANWIDTH=$width \
        man "$@"
    }
    
##  阅读本地man页面

你可以通过以下软件来查看man面： 

  * **[Emacs](<../zh-cn/Emacs.html> "Emacs")** — The extensible and self-documenting editor can also be used to read man pages with the built-in M-x `man` command.

     <https://www.gnu.org/software/emacs/> || [emacs](<https://archlinux.org/packages/?name=emacs>)包

  * **GNOME Help** — Help viewer for [GNOME](<../zh-cn/GNOME.html> "GNOME"). Part of [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组. It can show man pages via `yelp man:<name>` or the undocumented `Ctrl+L` keybinding from an existing window.

     <https://apps.gnome.org/Yelp/> || [yelp](<https://archlinux.org/packages/?name=yelp>)包

  * **KHelpCenter** — Application to show [KDE](<../zh-cn/KDE.html> "KDE") Applications' documentation. Part of [kde-system](<https://archlinux.org/groups/x86_64/kde-system/>)包组. Man pages are in _UNIX manual pages_ or by running `khelpcenter man:<name>`.

     <https://apps.kde.org/khelpcenter/> || [khelpcenter](<https://archlinux.org/packages/?name=khelpcenter>)包

  * **[Konqueror](<https://en.wikipedia.org/wiki/Konqueror> "wikipedia:Konqueror")** — KDE file manager and web browser. It can show man pages via `man:<name>`.

     <https://konqueror.org/> || [konqueror](<https://archlinux.org/packages/?name=konqueror>)包

  * **[neovim](<../zh-cn/Neovim.html> "Neovim")** — The editor can be used to read man pages using the built-in `:Man _name_` command, or configured as a man pager with `export MANPAGER='nvim +Man!'`. Supports highlighting and navigation between command-line flags, keywords, and other man pages. Automatically generates an outline using section headers, command-line flags, and keywords as entries (available via `gO`).

     <https://neovim.io/> || [neovim](<https://archlinux.org/packages/?name=neovim>)包

  * **xman** — Provides a categorized look at man pages.

     <https://xorg.freedesktop.org/> || [xorg-xman](<https://archlinux.org/packages/?name=xorg-xman>)包

使用如 [lynx](<https://archlinux.org/packages/?name=lynx>)包 and [firefox](<https://archlinux.org/packages/?name=firefox>)包 等浏览器来查看man页面可以使用户获得如阅读`info`页面的超链接优势，你可以使用以下替代方案： 

###  转换为 HTML

#### mandoc

安装 [mandoc](<https://archlinux.org/packages/?name=mandoc>)包来转换页面，如 `free(1)`: 
    
    $ mandoc -Thtml -Ostyle=style.css /usr/share/man/man1/free.1.gz > free.html
    
然后在你的浏览器中打开`free.html`

### man2html

首先，安装软件包[man2html](<https://archlinux.org/packages/?name=man2html>)包。 

然后使用它转换man手册页： 
    
    $ man free | man2html -compress -cgiurl man$section/$title.$section$subsection.html > ~/man/free.html
    
此外，`man2html`还可以把man页转换为便于打印的文本文件： 
    
    $ man free | man2html -bare > ~/free.txt
    
### man -H

[man-db](<https://archlinux.org/packages/?name=man-db>)包提供的man也具有浏览器阅读功能： 
    
    $ man -H free
    
由`BROWSER`环境变量决定使用的浏览器。也可以使用 `man -Hlynx`（H后无空格）这样的形式手动设置浏览器。 

#### roffit

安装 [roffit](<https://aur.archlinux.org/packages/roffit/>)AUR。 

转化一个man页面： 
    
    $ gunzip -c /usr/share/man/man1/free.1.gz | roffit > free.html
    
###  转换为 PDF

man pages 是可以打印的，遵循 [troff(1)](<https://man.archlinux.org/man/troff.1>) 格式，本来就是一种打印设置语言。因此，你可以很容易地通过**groff** 将man页面转换为输出设备支持的任意格式，这也被[man-db](<https://archlinux.org/packages/?name=man-db>)包 所使用。通过[groff(1)](<https://man.archlinux.org/man/groff.1>) (如果你使用[mandoc](<https://archlinux.org/packages/?name=mandoc>)包，请使用[mandoc(1)](<https://man.archlinux.org/man/mandoc.1>)）的`-T`选项来列出所有输出设备。 

如下命令将会为你导出PDF文件： 

$ man -Tpdf ''manpage'' > ''filename'' 

注意，这里只能使用Times字体的硬编码大小，一些man页面是特地为终端查看而设计的，并且不会在PDF或PS格式中正确被渲染。 

### Qman

这是一个提供查看man页面的界面的替代软件，它支持像超链接和历史记录等现代的功能，安装[qman-git](<https://aur.archlinux.org/packages/qman-git/>)AUR。然后你可以使用`qman`来代替`man`了： 
    
    $ qman ls    # 显示ls的man页面
    $ qman -k ls # 'ls'上执行apropos命令
    
查看这个项目的 [GitHub页面](<https://github.com/plp13/qman>)以了解更多 

###  可选配置

_Qman_ 的配置文件在 `~/.config/qman.conf` (用户的) or `/etc/xdg/qman.conf` (全局的). 

如果你正在使用一个支持256色和Unicode的现代终端，你可能想要使用一个[自定义配置](<https://github.com/plp13/qman/blob/main/config/themes/modernity.conf>)来为这个软件提供一个更现代化的界面 

默认的 _Qman_ 是通过`xdg-open`来打开超链接和电子邮件链接。你可以通过在你的配置文件中添加如下行来更改： 
    
    [misc]
    browser_path=/path/to/your/browser
    mailer_path=/path/to/your/email/client
    
###  使用在线手册页

**警告：** 一些发行版与Arch Linux不同的man页面，这可能是补丁后或过时版本的页面

许多网站提供在线man手册页，详细列表参见： 

  * [Arch Linux manual pages](<https://man.archlinux.org>)—contains man pages from Arch Linux packages. Used for [man page links](<../zh-cn/Template:Man.html> "Template:Man") from the wiki. You can also use the `!archman` bang with search engines like [DuckDuckGo](<https://duckduckgo.com/bangs>) or [Brave](<https://search.brave.com/bangs>) to search through the Arch manual pages directly.
  * [man7.org](<https://man7.org/linux/man-pages/index.html>)—The Linux man-pages project. Upstream of the [man-pages](<https://archlinux.org/packages/?name=man-pages>)包 package. The online pages currently show an outdated version of man-pages ([5.13](<https://man7.org/linux/man-pages/changelog.html>), released in 2021).
  * [manned.org](<https://manned.org/>)—collection from various Linux distributions, BSD, etc., with multiple package versions
  * [linux.die.net](<https://linux.die.net/man/>)
  * [man.cx](<https://man.cx/>)—Man pages extracted from Debian testing.
  * [Debian man pages](<https://manpages.debian.org/>)
  * [Ubuntu man pages](<https://manpages.ubuntu.com/>)
  * [DragonFlyBSD man pages](<https://leaf.dragonflybsd.org/cgi/web-man>)
  * [FreeBSD man pages](<https://www.freebsd.org/cgi/man.cgi>)
  * [NetBSD man pages](<https://man.netbsd.org/>)
  * [OpenBSD man pages](<https://man.openbsd.org>)
  * [Plan 9 Manual — Volume 1](<https://man.cat-v.org/plan_9/>)
  * [Inferno Manual — Volume 1](<https://man.cat-v.org/inferno/>)
  * [The UNIX and Linux forums man page repository](<https://www.unix.com/man-page-repository.php>)

注意， [man-pages](<https://archlinux.org/packages/?name=man-pages>)包提供的是POSIX.1-2017 (见[[2]](<https://gitlab.archlinux.org/archlinux/packaging/packages/man-pages/-/blob/main/PKGBUILD#L64-67>))的man页面，一个官方的在线参考也存在于： 

##  值得注意的man页面

这列举了一些可能帮助你更深度理解很多事情的页面，但这并不是很详尽。它们中的一些可能给你一个很好的参考（如ASCII表） 

  * [ascii(7)](<https://man.archlinux.org/man/ascii.7>)
  * [boot(7)](<https://man.archlinux.org/man/boot.7>)
  * [charsets(7)](<https://man.archlinux.org/man/charsets.7>)
  * [chmod(1)](<https://man.archlinux.org/man/chmod.1>)
  * [credentials(7)](<https://man.archlinux.org/man/credentials.7>)
  * [fstab(5)](<https://man.archlinux.org/man/fstab.5>)
  * [file-hierarchy(7)](<https://man.archlinux.org/man/file-hierarchy.7>)
  * [systemd(1)](<https://man.archlinux.org/man/systemd.1>)
  * [locale(1p)](<https://man.archlinux.org/man/locale.1p>), [locale(5)](<https://man.archlinux.org/man/locale.5>), [locale(7)](<https://man.archlinux.org/man/locale.7>)
  * [printf(3)](<https://man.archlinux.org/man/printf.3>)
  * [proc(5)](<https://man.archlinux.org/man/proc.5>)
  * [regex(7)](<https://man.archlinux.org/man/regex.7>)
  * [signal(7)](<https://man.archlinux.org/man/signal.7>)
  * [term(5)](<https://man.archlinux.org/man/term.5>), [term(7)](<https://man.archlinux.org/man/term.7>)
  * [termcap(5)](<https://man.archlinux.org/man/termcap.5>)
  * [terminfo(5)](<https://man.archlinux.org/man/terminfo.5>)
  * [utf-8(7)](<https://man.archlinux.org/man/utf-8.7>)

你也可以看：[category 7 (miscellaneous) pages](<https://man7.org/linux/man-pages/dir_section_7.html>): 
    
    $ man -s 7 -k ".*" 
    
Arch Linux 的特定页面： 

  * [alpm-hooks(5)](<https://man.archlinux.org/man/alpm-hooks.5>)
  * [libalpm(3)](<https://man.archlinux.org/man/libalpm.3>)
  * [makepkg(8)](<https://man.archlinux.org/man/makepkg.8>)
  * [makepkg.conf(5)](<https://man.archlinux.org/man/makepkg.conf.5>)
  * [makepkg-template(1)](<https://man.archlinux.org/man/makepkg-template.1>)
  * [mkinitcpio(8)](<https://man.archlinux.org/man/mkinitcpio.8>)
  * [pacman(8)](<https://man.archlinux.org/man/pacman.8>)
  * [pacman.conf(5)](<https://man.archlinux.org/man/pacman.conf.5>)
  * [pacman-conf(8)](<https://man.archlinux.org/man/pacman-conf.8>)
  * [pacman-key(8)](<https://man.archlinux.org/man/pacman-key.8>)

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Add a section on writing man pages, including conversion tools like [pandoc-cli](<https://archlinux.org/packages/?name=pandoc-cli>)包, [ruby-ronn-ng](<https://archlinux.org/packages/?name=ruby-ronn-ng>)包, [asciidoc](<https://archlinux.org/packages/?name=asciidoc>)包, [help2man](<https://archlinux.org/packages/?name=help2man>)包, [go-md2man](<https://archlinux.org/packages/?name=go-md2man>)包, [txt2man](<https://archlinux.org/packages/?name=txt2man>)包, [scdoc](<https://archlinux.org/packages/?name=scdoc>)包, [info2man](<https://aur.archlinux.org/packages/info2man/>)AUR, [pod2man](<https://aur.archlinux.org/packages/pod2man/>)AUR, [ruby-md2man](<https://aur.archlinux.org/packages/ruby-md2man/>)AUR, etc. (在 [Talk:Man 手册](<../zh-cn/Talk:Man_%E6%89%8B%E5%86%8C.html>) 中讨论)
