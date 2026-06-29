相关文章

  * [Help:Style/Formatting and punctuation](</wzh/index.php?title=Help:Style/Formatting_and_punctuation&action=edit&redlink=1> "Help:Style/Formatting and punctuation（页面不存在）")
  * [Help:Style/White space](</wzh/index.php?title=Help:Style/White_space&action=edit&redlink=1> "Help:Style/White space（页面不存在）")
  * [Help:编辑](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html> "Help:编辑")
  * [Help:阅读](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html> "Help:阅读")
  * [Help:讨论](<../zh-cn/Help:%E8%AE%A8%E8%AE%BA.html> "Help:讨论")
  * [Help:模板](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html> "Help:模板")
  * [Help:术语表](<../zh-cn/Help:%E6%9C%AF%E8%AF%AD%E8%A1%A8.html> "Help:术语表")

**翻译状态：**

  * 本文（或部分内容）译自 [Help:Style](<https://wiki.archlinux.org/title/Help:Style> "arch:Help:Style")，最近一次同步于 2021-09-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Help:Style?diff=0&oldid=691338>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Help:Style_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

这些风格约定鼓励简约、有条理和视觉一致的文章。请在编辑 ArchWiki 时尽量遵守本文的指导。 

##  文章页面

###  标题

  * 标题应该使用[整句大小写格式](<https://en.wikipedia.org/wiki/Sentence> "wikipedia:Sentence"), 例如应该使用 "Title for new page" 而不是 "Title for New Page"。如果单词是常见缩写的一部分，则应该使用大写，例如应该使用 "Advanced Linux Sound Architecture" 而不是 "Advanced Linux sound architecture".   
名称空间不是标题的一部分，应该使用"ArchWiki:Example article" 而不是 "ArchWiki:example article"。子页面名也应该首字母大写，应该使用 "My page/My subpage" 而不是"My page/my subpage".
  * 默认情况下文章使用英文的单数形式命名，如果文章代表一类问题，则使用复数形式。
  * 尽量使用全名而不是缩写。如果您认为它们都很常见，可创建一个从缩写到全名的[重定向](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html#%E9%87%8D%E5%AE%9A%E5%90%91> "Help:编辑")。不要用括号包含缩写。
  * 本地化页面也应该遵循 [Help:i18n#Page titles](<../zh-cn/Help:%E5%9B%BD%E9%99%85%E5%8C%96%E5%92%8C%E6%9C%AC%E5%9C%B0%E5%8C%96.html#Page_titles> "Help:I18n").
  * 参见[文章命名指导](<../zh-cn/Help:%E6%96%87%E7%AB%A0%E5%91%BD%E5%90%8D%E5%87%86%E5%88%99.html> "Help:文章命名准则")。

###  布局

ArchWiki 上的文章应该分为两部分：**前言** 和**主体** ，且主要遵循如下顺序： 

  * 前言：由分类、[i18n](<../zh-cn/Help:%E5%9B%BD%E9%99%85%E5%8C%96%E5%92%8C%E6%9C%AC%E5%9C%B0%E5%8C%96.html> "Help:I18n")、文章状态、概览和简介
  * 主体: 介绍、安装、配置、技巧、问题解决和更多内容

  * 文章各部分的排列顺序应该为:

  1. [#特殊字段](<#%E7%89%B9%E6%AE%8A%E5%AD%97%E6%AE%B5>) (可选)
  2. [#分类](<#%E5%88%86%E7%B1%BB>)
  3. [#跨语言链接](<#%E8%B7%A8%E8%AF%AD%E8%A8%80%E9%93%BE%E6%8E%A5>) (可选)
  4. [#文章状态模板](<#%E6%96%87%E7%AB%A0%E7%8A%B6%E6%80%81%E6%A8%A1%E6%9D%BF>) (可选)
  5. [#相关文章](<#%E7%9B%B8%E5%85%B3%E6%96%87%E7%AB%A0>) (可选)
  6. [#前言或介绍](<#%E5%89%8D%E8%A8%80%E6%88%96%E4%BB%8B%E7%BB%8D>)
  7. 目录 (自动生成)
  8. 文章特有的部分

####  特殊字段

  * [特殊字段](<https://www.mediawiki.org/wiki/Help:Magic_words> "mw:Help:Magic words")会修改文章的显示方式，但并不会添加内容。这些字段应该位于文章的最开始，尤其是这两个：`{{DISPLAYTITLE:title}}` 和[模板:小写标题](<../zh-cn/Template:%E5%B0%8F%E5%86%99%E6%A0%87%E9%A2%98.html> "Template:小写标题")。

####  分类

  * 每个文章至少应该属于一个分类。
  * 一个文章可以属于多个分类，只要分类间没有包含关系。
  * 分类必须放在文章的顶部，且在特殊字段之后。

**注意：** 这点和其它 MediaWiki 项目有时会不一样，后者经常把分类放在文章末尾。

  * 分类与正文第一段（包括跨语言链接）之间不要插入空格，否则会有多余的空白。
  * 参见[文章分类](<../zh-cn/Help:Category_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Help:Category \(简体中文\)")。

**提示：**

  * 由于分类页面中，MediaWiki会把相同首字母的页面归到一栏中，对于中文标题的页面，会把每个起始汉字归到一类，导致页面很混乱。因此在为名称由中文起始的页面，添加分类时请同时添加汉语拼音的首字母，如官方安装指南可以添加如下分类：`[[Category:简体中文|G]]`，这样该页面就会归类到字母G一栏的最上方。
  * **不要** 添加多个字母(如：`[[Category:简体中文|GFAZZN]]`)，否则会出现分类中中英文页面顺序混排的现象，使页面不便于查找。

####  跨语言链接

  * 如果文章有其他语言的翻译，必须在分类和正文第一段之间加上这些跨语言链接。它们将显示在页面的左边。
  * 跨语言链接和正文第一段之间不应该有空格，否则文章顶部会有多余的空白。
  * 除了在当前页面上添加其它跨语言链接，您还需要在其它语言的页面上添加当前页面的跨语言链接。
  * 每个语言的跨语言链接应只能有一个。
  * 不要加入当前语言的跨语言链接。
  * 跨语言链接需要根据其语言标签，来按字母表顺序排列，不要按语言本身的正式名称顺序排列。例如，`` 就该排在 `` 前面，哪怕 “Suomi” 就本来在 “Français” 之后。
  * 参见 [Help:i18n](<../zh-cn/Help:I18n_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Help:I18n \(简体中文\)") 和 [Wikipedia:Help:Interlanguage links](<https://en.wikipedia.org/wiki/Help:Interlanguage_links> "wikipedia:Help:Interlanguage links").

####  文章状态模板

  * [文章状态模板](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#Article_status_templates> "Help:Template")应放在分类(或跨语言链接)和相关文章之间。
  * 针对段落的标记，位置尽量靠近有问题的地方。
  * 每个状态模板都应该包含简要的说明。有必要时，可以在讨论页面加以讨论。

####  相关文章

  * 给出相关的文章列表
  * 放在分类、跨语言链接和文章状态模板之后。
  * 通过组合模板[模板:相关文章开始](<../zh-cn/Template:%E7%9B%B8%E5%85%B3%E6%96%87%E7%AB%A0%E5%BC%80%E5%A7%8B.html> "Template:相关文章开始"), [Template:Related](<../zh-cn/Template:%E7%9B%B8%E5%85%B3.html> "Template:Related") 和[模板:相关文章结束](<../zh-cn/Template:%E7%9B%B8%E5%85%B3%E6%96%87%E7%AB%A0%E7%BB%93%E6%9D%9F.html> "Template:相关文章结束")实现。详情参阅这几个模板的页面。
  * 可以使用 [Template:Related2](<../zh-cn/Template:%E7%9B%B8%E5%85%B32.html> "Template:Related2") 给出需要显示的标题翻译.
  * 如果文章较多，或者需要详细描述，请使用参阅段落。

####  前言或介绍

  * 描述文章的话题。  
不要自己给软件下评论，一般可以访问项目主页，使用作者自己的描述。[MediaTomb](</wzh/index.php?title=MediaTomb&action=edit&redlink=1> "MediaTomb（页面不存在）") 是一个范例。
  * 放在第一段前面
  * 不要另外加上 `==Introduction==` 或 `==Preface==` 说明：直接在第一段开始时写入即可。如果文章有足够多的段落，在前言和第一段直接会自动加入目录。
  * 参见 [Writing Article Introductions](</wzh/index.php?title=Writing_Article_Introductions&action=edit&redlink=1> "Writing Article Introductions（页面不存在）")。

####  标准段落

#####  "安装" 段落

  * _安装_ 段落介绍软件的安装方法，请参考 [#指南](<#%E6%8C%87%E5%8D%97>).
  * 标准的标题是 _安装_ ，尽量往前放.

#####  "已知问题" 段落

  * 已知的 bug 或者使用问题，暂时还没有解决方法(与[#"问题解决" 段落](<#"%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3"_%E6%AE%B5%E8%90%BD>)相反)。
  * 标准标题是**已知问题**.
  * 尽量避免明确的版本号，如果这个问题已经报告了 bug，请提供链接；如果没有报告，请报告它，这样会提高问题解决的概率。

#####  "提示与技巧" 段落

  * 高级技巧或使用软件的示例
  * 标准标题应是 _提示与技巧_
  * 用子段落分别介绍不同的技巧

#####  "问题解决" 段落

  * 常见问题的解决办法(与 [#"已知问题" 段落](<#"%E5%B7%B2%E7%9F%A5%E9%97%AE%E9%A2%98"_%E6%AE%B5%E8%90%BD>)不同)。
  * 标准标题是 _问题解决_ 。
  * 可以提供绕过已知 bug 的临时解决方法，但是请务必提供该 bug 的链接地址；如果还未得到报告，请自行报告 bug，这样可以让它更容易被修复。  
增加 bug 链接对读者和编辑有如下好处： 
    * 对读者来说，阅读该 Wiki 并非就到此为止了：他们还可以进一步访问链接，获取更多信息。
    * 对 Wiki 编辑来说，更好判断 bug 是否已经解决，容易维护；如果读者有得到新信息，他们也可以自主编辑。

#####  "参见" 段落

  * 列出参考文档和额外信息.
  * 应该是个列表，每行都以 `*` 开头。
  * 一般使用 "参见" 作为标题，应该避免使用"外部链接","更多资源",“参阅” 等。

###  段落标题

  * 段落标题应该从第二级开始(`==`), 因为第一级已保留给文章标题用。
  * 使用子标题时不要越级，就像二级标题下面必然是三级标题。
  * 不要在标题上添加超链接，它们会破坏样式的一致性。  
同理，请不要使用任何 html 或 wiki 标记代码，包括 [#代码格式](<#%E4%BB%A3%E7%A0%81%E6%A0%BC%E5%BC%8F>)。
  * 参见 [Effective Use of Headers](</wzh/index.php?title=Effective_Use_of_Headers&action=edit&redlink=1> "Effective Use of Headers（页面不存在）")。

###  格式

####  代码格式

  * 使用 [Template:ic](<../zh-cn/Template:Ic.html> "Template:Ic") 格式化要嵌入的代码片段、文件名、路径、命令名、配置参数、变量等。例如:   
在终端运行`sh ./hello_world.sh`
  * 对于单行的代码 (命令行或者代码输出) 可以可以直接在行首加入空格，参考[Help:Editing#Code](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html#Code> "Help:Editing"). 示例：

    $ sh ./hello_world.sh
    
    Hello World
    
  * 使用 `{{bc|code}}` 格式化多行代码(命令行的输入或输出内容、文件内容) 例如:

    #!/bin/sh
    
    # Demo
    echo "Hello World"

  * 如果代码不长，代替 `{{bc|code}}` (参见[编辑帮助](<../zh-cn/Help:Editing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Help:Editing \(简体中文\)"))。
  * 使用 `{{hc|input|output}}` 能同时显示命令行及其输出，例如:

    $ sh ./hello_world.sh
    
    Hello World

  * 需要显示文件内容时，可以使用 `{{hc|filename|content}}` 明确内容属于哪个文件，例如：

    ~/hello_world.sh
    
    #!/bin/sh
    
    # Demo
    echo "Hello World"

  * 大段的代码，例如配置文件，可以考虑用 `...` 略去无关的内容
  * 关于模板的一些格式上的特殊处理，比如`=` 或 `|`，请阅读 [Help:Template](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html> "Help:Template")。

###  命令行文字

  * 使用段落代码 ([Template:bc](<../zh-cn/Template:Bc.html> "Template:Bc")) 时，需要提示符标注执行权限;使用 [Template:ic](<../zh-cn/Template:Ic.html> "Template:Ic") 时不需要提示符，但是需要用文字明确指出需要的权限。
  * 使用 `$` 作为一般用户权限命令的提示符；使用 `#` 作为 root 命令的提示符。

**注意：** 因为 `#` 也经常表示文本文件中的注释符号，所以经常要澄清是运行命令还是编辑文件，以避免不必要的误解。

  * 引入命令的句子尽量以 `:` 结尾。
  * 建议使用 `# command` 而不是 `$ sudo command`。
  * 尽量少假设用户会使用 `[sudo](<../zh-cn/Sudo.html> "Sudo")` 或其它权限获取工具(例如 `gksu`、`kdesu`)。
  * 应该避免`# sudo command`，唯一的例外是用`sudo`的`-u`选项修改用户，这时提示符可以与其它命令一致，默认使用`$`。
  * 不要在一行命令的代码框里添加注释，例如`# pacman -S foo #Install package foo`就不好
  * 代码行不要过长，请尽量换行。

###  键盘按键

  * 表示按键的标准方法是使用 [Template:ic](<../zh-cn/Template:Ic.html> "Template:Ic") 模板。
  * 字母键应该小写：`a`. 大写字母用 `Shift+a`，不要使用 `Shift+A` 或 `A`。
  * 表示按键组合的正确方法是使用 `+` 号连接，不要增加额外空格，在一个模板中包含多个按键：`Ctrl+c`.   
下面格式都应该避免使用：`Ctrl + c`, `Ctrl`+`c`, `Ctrl-c`。
  * 特殊键的标准名称： 
    * `Shift` (不要用 `SHIFT`)
    * `Ctrl` (不要用 `CTRL` 或 `Control`)
    * `Alt` (不要用 `ALT`)
    * `Super` (不要用 `Windows` 或 `Mod`)
    * `Enter` (不要用 `ENTER` 或 `Return`)
    * `Esc` (不要用 `ESC` 或 `Escape`)
    * `Space` (不要用 `SPACE`)
    * `Backspace`
    * `Tab`
    * `Ins` (不要用 `INS` 或 `Insert`)
    * `Del` (不要用 `DEL` 或 `Delete`)
    * `Print Screen`
    * `Up` (不要使用 `↑` 或 `Up Arrow`) – 其它方向键类似
    * `PageUp`
    * `PageDown`
    * `Fn` (不要使用 `FN` 或 `fn`) – 不同笔记本上的功能按键请参考[这里](<https://en.wikipedia.org/wiki/Fn_key> "wikipedia:Fn key")。

###  注意、警告、提示

  * [注意](<../zh-cn/Template:%E6%B3%A8%E6%84%8F.html> "Template:注意")应该用在用户预料不到的地方。包括与文章关系不大的细节知识、软件包名称变动等。  
也可以用来强调容易被用户忽略的地方。
  * [警告](<../zh-cn/Template:%E8%AD%A6%E5%91%8A.html> "Template:警告")用来指出需要特别警惕的地方，比如不可逆转的修改、损害系统的可能性等。警告应该直接指出最坏的情况，并给出相应措施。不要滥用警告，如果不确定的时候，用注意即可。
  * [提示](<../zh-cn/Template:%E6%8F%90%E7%A4%BA.html> "Template:提示")用来给出一个可能会相当有用的小技巧，一般不是必须的，省略也无妨。
  * 如果多个注意、警告、技巧连用，最好组合到单一模板中，除非彼此毫无相干。例如:

**提示：**

  * Tip example #1.
  * Tip example #2.

####  表格

关于表格的语法，请参见 [MediaWiki 帮助文档](<https://www.mediawiki.org/wiki/Help:Tables/zh> "mw:Help:Tables/zh")。 

  * 表格通常需要包含 `wikitable` 类。
  * 对照表还应包含 `sortable` 类。
  * 在适当的地方使用表格标题和[表格模板](<../zh-cn/Help:Template_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E8%A1%A8%E6%A0%BC%E6%A8%A1%E6%9D%BF> "Help:Template \(简体中文\)")。
  * ~~表格标题的第一个字母应该大写，其余应该小写。~~ （汉字并无大小写之分，故本条可被忽略）
  * 表格说明应使用定义列表，并放在表格之前。

###  指南

  * 除非必要，请不要特别指定某编辑器(nano, vim, emacs, ...)。
  * 除非必要，请不要使用隐晦复杂的编辑命令，就像 `$ echo -e "clear\nreset" >> ~/.bash_logout` 应该写成这样：

    将下行附加到 `~/.bash_logout`:
    
    clear  
    reset

    合适的话可以增加一个到 [Help:Reading#Append, add, create, edit](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Append,_add,_create,_edit> "Help:Reading") 的链接。

####  官方软件包

  * 在示意要从官方软件仓库安装软件包时，请避免直接标出 pacman 命令。不仅简化内容(每个 Arch 用户都应该知道如何使用 [pacman](<../zh-cn/Pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Pacman \(简体中文\)"))而且避免了 `pacman -Sy package` 之类的键误，以及 `pacman -S package` 和 `pacman -Syu package` 孰好孰坏的无谓争论。同理，也不要引入 pacman 前端或图形界面等。  
相反，请像这样简单地示范：安装说明应该使用： `[[pacman (简体中文)|安装]] 软件包 {{Pkg|package}}`。
  * 如果安装的是一组软件包，则使用 : [安装](<../zh-cn/Pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Pacman \(简体中文\)")软件组 [foobar](<https://archlinux.org/groups/x86_64/foobar/>)包组.
  * 必须要用 [Template:Pkg](<../zh-cn/Template:%E5%8C%85.html> "Template:Pkg")/和[Template:Grp](<../zh-cn/Template:%E5%8C%85%E7%BB%84.html> "Template:Grp") 模板进行格式化，例如`{{Pkg|package}}`.
  * 不要特意指出软件包是在 [core]、[extra] 或 [community] 中的哪一个仓库，因为一个软件包可能会在不同仓库之间转移。此外如果软件包位于 [multilib] 仓库，请这样示范：  
[安装](<../zh-cn/Pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Pacman \(简体中文\)")[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")的 [package](<https://archlinux.org/packages/?name=package>)包 时，需要事先开启 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 仓库。  

####  AUR 软件包

  * 安装 AUR 软件包的语句安装`[[Arch 用户软件仓库|AUR]] 中的 {{AUR|package}}`。
  * 可以适当修改以适应具体文章，但是一定要明确指出软件包并非官方支持。
  * 千万不要直接示范如何安装 AUR 软件包：因为凡是安装非官方软件包的用户，都得事先充分阅读 [Arch 用户仓库](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "Arch 用户软件仓库")，并了解使用这些包会给系统带来的风险。
  * AUR 软件包的超链接化应该使用 [Template:AUR](<../zh-cn/Template:AUR.html> "Template:AUR") 模板，例如 `{{AUR|package}}`.

####  非官方软件仓库

  * 要使用非官方软件仓库时，请先将其加入[非官方软件仓库](<../zh-cn/Unofficial_user_repositories.html> "Unofficial user repositories")，然后提供一个链接，示例：  
从 `[[Unofficial user repositories#example|示例]]` 软件仓库安装 [package](<https://aur.archlinux.org/packages/package/>)AUR.   
不要在文章内直接给出启用软件仓库的详细信息。
  * 必须链接到[非官方软件仓库](<../zh-cn/Unofficial_user_repositories.html> "Unofficial user repositories")，而且请尽量使用段落链接：`[[Unofficial User Repositories#example|example]]`.

###  Systemd 单元操作

  * 不要用 _systemctl_ 命令直接进行 _start_ 、 _restart_ 或 _stop_ 的操作。正确的说明方法应该是列出需要的单元，以及它们的依赖、冲突关系，描述所要执行的操作。例如：

    要在开机时启动 GDM，请[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `gdm.service`.
    如果模板需要实例化： 

    要在无线时自动切换 _netctl_ 配置，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")一个带接口名称的 `netctl-auto@.service` 实例，例如 `netctl-auto@wlan0.service`.
    可以根据上下文调整语句，但是请确保有到 [systemd#Using units](<../zh-cn/Systemd.html#Using_units> "Systemd") 文章段落的链接，可以直接引用或通过[重定向](<https://wiki.archlinux.org/index.php?title=Special:WhatLinksHere/Systemd&hidelinks=1&hidetrans=1>)实现，例如 `[[start]]`, `[[enable]]` or `[[stop]]`.

### Shells

  * 除非必要，不要特别指定用户所用的 shell：撰写文章内容时请尽量做到与所用 shell 无关。

###  超链接

  * 尽可能在该页面和相关页面插入彼此的超链接，实现 wiki 脉络性最大化。
  * 像[系统调用](<https://zh.wikipedia.org/wiki/%E7%B3%BB%E7%BB%9F%E8%B0%83%E7%94%A8> "zhwp:系统调用")之类的文章 ArchWiki 却没有，大可直接用到维基百科页面的链接（使用 `zhwp:` 链接前缀）。
  * 链接到 wiki 中其它页面时，不要用完整地址，而是用 wiki 间链接语法：`[[Wiki Article]]`。 wiki 引擎可以跟踪 wiki 间链接，好让大家更容易维护。  
更多 wiki 间链接内容参见 [Help:编辑#链接](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html#%E9%93%BE%E6%8E%A5> "Help:编辑")。 
    * 链接到本页面段落时，不要隐藏井号，除了简化额外的格式，井号还明确告诉读者这是一个到本页面的链接。
  * 请避免使用隐含链接，例如应该使用“参阅 [systemd](<../zh-cn/Systemd.html> "Systemd")”而不是“参阅 [here](<../zh-cn/Systemd.html> "Systemd")”。
  * 仅在文件存在时才创建链接，不要链接到不存在的文件。
  * 除极个别情况外，页面不能是死亡页面(没有任何到其它页面的链接)或孤立页面(没有其它文章链接到它).
  * 添加内容时，首先请注意是不是已经有现成的文章描述了该详细内容，如果有，请插入它的链接而不是再三重复内容。
  * 如果上游的现有文档十分完善且维护程度良好，请只写 Arch 应特有的内容，并提供到前者文档的链接。
  * 如果某页面中文维基没有，请使用 `{{[link-en](<../zh-cn/Template:Link-en.html> "Template:Link-en")}}` 模板来链接到英文 ArchWiki，以便在中文页面被创建时自动链接到中文页面。
  * 需要链接到英文 ArchWiki 的时候，请使用链接前缀 `arch:`。

####  手册页面

  * 请用 [Template:man](<../zh-cn/Template:Man.html> "Template:Man") 引用[手册页面](<../zh-cn/Man_page.html> "Man page")。

###  代码规范

  * 添加命令或脚本时，请保持代码风格一致，也可以参考该程序语言的主流编码规范，并加以遵守。
  * 避免使用过时的语言功能和风格，例如推荐使用 `$()` 做脚本命令，而不是````.
  * 脚本尽可能短，只需表达需要的信息。尽量使用[伪变量](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Pseudo-variables_in_code_examples> "Help:Reading")而不是真实变量。不要添加参数解析或输出等无关功能。
  * 代码应该在文本解释不太清楚的时候使用，如果脚本确实有用但是不是必须，可以考虑使用 [gist](<https://gist.github.com>) 引用。
  * 明确标明是文件还是目录/文件夹，比如

  * "检查目录 `/sys/firmware/efi` 是否已被创建",不要写 "检查 `/sys/firmware/efi` 是否已被创建".
  * "将 _.conf_ 文件放入 `/etc/modules-load.d/`"，而不是 "将 _.conf_ 文件放入 `/etc/modules-load.d`".

  * 包含空格的参数应该用引号引用，使用 `cd "foo bar"` 而不是 `cd foo\ bar`.

###  支持的内核版本

  * Arch Wiki 支持的最老内核版本为 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 和[安装介质](<https://archlinux.org/download/>)中的内核版本。
  * 仅可以删除比两个版本更老的内核说明或适配信息。

###  不相关内容

  * 请不要署名，甚至把文章归功于自己：ArchWiki 是社区全体的劳动成果，文章的历史已能足够说明个人贡献。  
直接在 wiki 之外的地方专门撰文、并提供链接也不失为署名的好办法，可以通过 "参见" 段落实现。
  * 一般用户没有上传文件的权限，而且不能用图片。作为替代，可以靠外部链接或者用 ASCII 编辑器，如[Asciiflow](<http://www.asciiflow.com/>) 等绘制简单图形。原因： 
    * 维护性: Arch 是滚动更新的，图片会大幅度地提高维护文章的难度。
    * 必要性: Arch 之道注定了它并不会开发或维护 GUI，所以没有显示图片的必要。
    * 资源性: 允许自行上传图片，会需要更多的精力来删除重复和不合适的图片。
    * 可行性: 有一些用户的网速很慢，纯文字页面不光能加快其访问速度
    * 效率性: 图片会剧烈消耗服务器的带宽和存储空间。
    * 简约性: 且界面简约美观。

###  拼写

  * 尽量避免不必要的缩写词。
  * 专有名词拼写与项目官方主页里面的拼写保持一致。

###  措辞

  * 文章的措辞应做到十分正式、专业且精确。
  * 编写时，请注意不光说**怎么样** ，还要回答**为什么？** 解释远胜单纯的指导。
  * 不要加入个人评论，后者应该放到讨论页面，一般不要用第一人称。
  * 不要说现在，当前等等，请给出具体的时间。
  * 编辑内容时，保持和页面其它内容的一致性，用一样的人称描述。
  * 在多个选项间提供选择时，不要感性的建议一个或另一个，请可观的描述每一个选择的优点和缺点，让用户自行选择。
  * 翻译页面时，请尽量避免使用第二人称代词“你”或“您”。确实需要使用第二人称代词时，如果页面中现存的翻译已使用其中的一种，请与其保持一致，如果使用了多种，请考虑统一为其中的一种；如果页面中没有使用，则可以自行决定使用哪一种，但请确保在翻译中保持一致。

##  分类页面

  * 除了根分类外，每个[分类](<../zh-cn/Help:%E5%88%86%E7%B1%BB.html> "Help:Category")都应该有一个父分类。  
根分类是[Category:Archive](</wzh/index.php?title=Category:Archive&action=edit&redlink=1> "Category:Archive（页面不存在）"), [Category:DeveloperWiki](<../zh-cn/Category:%E5%BC%80%E5%8F%91%E8%80%85%E7%99%BE%E7%A7%91.html> "Category:DeveloperWiki"), [Category:Languages](</wzh/index.php?title=Category:Languages&action=edit&redlink=1> "Category:Languages（页面不存在）")，[Category:Maintenance](<../zh-cn/Category:%E7%BB%B4%E6%8A%A4.html> "Category:Maintenance") 和 [Category:Sandbox](</wzh/index.php?title=Category:Sandbox&action=edit&redlink=1> "Category:Sandbox（页面不存在）").
  * 分类可以属于多个父分类，只要父分类之间是平级的。
  * 避免循环关系: 两个分类不能互相包含。
  * 分类必须放到在分类页面的顶部。
  * 分类不能被重定向，除非是[重命名的分类](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#Rename_a_category> "Help:Procedures").

##  重定向页面

  * 建议创建缩写词到正式文章的重定向，比如创建 [ALSA](<../zh-cn/ALSA.html> "ALSA"), [daemon](<../zh-cn/Systemd.html> "Daemon") 或 [AIGLX](</wzh/index.php?title=AIGLX&action=edit&redlink=1> "AIGLX（页面不存在）"). 重定向可以简化链接： `[[Advanced Linux Sound Architecture|ALSA]]`, `[[daemons|daemon]]` 或 `[[Xorg#Composite|AIGLX]]`.
  * 重定向页面应该只包含重定向链接，除此之外一无所有。除非： 
    * 是[归档](<../Project:%E5%BD%92%E6%A1%A3.html> "Project:Archive")页面，虽然是重定向，需要属于分类 [Category:Archive](</wzh/index.php?title=Category:Archive&action=edit&redlink=1> "Category:Archive（页面不存在）").
    * 是[重命名分类](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#Rename_a_category> "Help:Procedures")可以包含一个 [Template:Archive](<../zh-cn/Template:%E5%BD%92%E6%A1%A3.html> "Template:Archive") 标记.
  * 只重定向到 Wiki 内部的页面，不要重定向到外部页面。
  * 参考 [Help:Editing#Redirects](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html#Redirects> "Help:Editing")

##  用户页面

  * [用户](<../Special:%E5%89%8D%E7%BC%80%E7%B4%A2%E5%BC%95/User:.html> "Special:前缀索引/User:")这一名字空间中的页面不能被分类。
  * [用户](<../Special:%E5%89%8D%E7%BC%80%E7%B4%A2%E5%BC%95/User:.html> "Special:前缀索引/User:")这一名字空间中的页面只能链接自“[用户](<../Special:%E5%89%8D%E7%BC%80%E7%B4%A2%E5%BC%95/User:.html> "Special:前缀索引/User:")”或者“[讨论](<../Special:%E5%89%8D%E7%BC%80%E7%B4%A2%E5%BC%95/Talk:.html> "Special:前缀索引/Talk:")”名字空间中的其他页面，除非管理员明确同意。

##  一般规则

###  编辑摘要

请阅读 [Wiki 贡献的基本原则](<../Project:%E8%B4%A1%E7%8C%AE.html#%E4%B8%89%E4%B8%AA%E5%9F%BA%E6%9C%AC%E5%8E%9F%E5%88%99> "Project:贡献"). 

###  HTML 标签

  * 尽量不要使用 HTML 标签：尽量使用 wiki 标记和模板，参见 [Help:编辑](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html> "Help:编辑")。
  * 使用 `<pre>code</pre>` 的地方都改成 `{{bc|code}}`。使用 `<tt>text</tt>` 或 `<code>text</code>` 的地方，都改用 `{{ic|text}}`。
  * 特别是避免 HTML 注释(`<!-- comment -->`): 一般使用 HTML 注释的文字都可以放到讨论页面。   
可以加入适当的 [Help:Template#Article status templates](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#Article_status_templates> "Help:Template")。
  * 仅在必要时才使用 `<br>`：要开启新段落时，用后面的空行实现。  
一个例外是作为一个列表的子项目时，或者在一个模板当中，这时必须使用`<br>`换行。
  * 大段代码可考虑使用 [<syntaxhighlight> 标签](<https://www.mediawiki.org/wiki/Extension:SyntaxHighlight/zh> "mw:Extension:SyntaxHighlight/zh")进行语法高亮

##  中文排版

  * 中文之间不要加空格（即使样式不同，比如包含链接）
  * 尽量避免中文斜体

###  中英文混排

  * 英文和数字使用半角字符
  * 中文文字之间不加空格
  * 中文文字与英文、阿拉伯数字及 @ # $ % ^ & * . ( ) 等符号之间加空格
  * 中文标点之间不加空格
  * 中文标点与前后字符（无论全角或半角）之间不加空格
  * 翻译时，正文的英文常见标点等需要换为中文标点
  * 当半角符号 / 表示“或者”之意时，与前后的字符之间均不加空格

##  术语

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 需要规范术语。 (在 [Help talk:风格](<../zh-cn/Help_talk:%E9%A3%8E%E6%A0%BC.html>) 中讨论)

为保持一致的翻译风格，在翻译时请遵守以下规范： 

  * _在正式的规范完成前，请暂时先按照现有的风格翻译。_

相关讨论： 

  * [Help_talk:Style_(简体中文)](</wzh/index.php?title=Help_talk:Style_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Help talk:Style \(简体中文\)（页面不存在）")
  * [ArchWiki_talk:Translation_Team_(简体中文)](</wzh/index.php?title=ArchWiki_talk:Translation_Team_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "ArchWiki talk:Translation Team \(简体中文\)（页面不存在）")
  * [Project:社群首页#Help:风格之关于统一翻译术语的新新提案](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#Help:%E9%A3%8E%E6%A0%BC%E4%B9%8B%E5%85%B3%E4%BA%8E%E7%BB%9F%E4%B8%80%E7%BF%BB%E8%AF%91%E6%9C%AF%E8%AF%AD%E7%9A%84%E6%96%B0%E6%96%B0%E6%8F%90%E6%A1%88> "Project:社群首页")
