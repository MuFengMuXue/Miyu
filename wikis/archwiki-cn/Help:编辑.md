**翻译状态：**

  * 本文（或部分内容）译自 [Help:Editing](<https://wiki.archlinux.org/title/Help:Editing> "arch:Help:Editing")，最近一次同步于 2022-11-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Help:Editing?diff=0&oldid=749846>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Help:Editing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Project:关于](<../Project:%E5%85%B3%E4%BA%8E.html> "Project:关于")
  * [Help:速查表](<../zh-cn/Help:%E9%80%9F%E6%9F%A5%E8%A1%A8.html> "Help:速查表")
  * [Help:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")
  * [Help:阅读](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html> "Help:阅读")
  * [Help:模板](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html> "Help:模板")
  * [Help:讨论](<../zh-cn/Help:%E8%AE%A8%E8%AE%BA.html> "Help:讨论")
  * [Help:术语表](<../zh-cn/Help:%E6%9C%AF%E8%AF%AD%E8%A1%A8.html> "Help:术语表")
  * [Project:沙盒](<../Project:%E6%B2%99%E7%9B%92.html> "Project:沙盒")
  * [ArchWiki:Bots](</wzh/index.php?title=Project:Bots&action=edit&redlink=1> "Project:Bots（页面不存在）")

ArchWiki 使用的 [MediaWiki](<https://www.mediawiki.org/wiki/MediaWiki> "mw:MediaWiki") 是一个用 PHP 写成的软件包，最早用于维基百科。更深入的帮助请查看 [MediaWiki 帮助](<https://www.mediawiki.org/wiki/Help:Contents> "mw:Help:Contents")（英文）和[中文维基百科的帮助](<https://zh.wikipedia.org/wiki/Help:%E7%9B%AE%E5%BD%95> "zhwp:Help:目录")。 

本文仅介绍编辑和创建页面的方法和页面语法，在编辑或创建页面之前，请阅读 [Project:贡献](<../Project:%E8%B4%A1%E7%8C%AE.html> "Project:贡献")、[Help:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")和 [Help:阅读](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html> "Help:阅读")，了解一下现有文章的语言、布局和风格，在后续的编辑中请尽量保持统一。请使用[沙盒](<../Project:%E6%B2%99%E7%9B%92.html> "Project:沙盒")进行编辑尝试。[Help:速查表](<../zh-cn/Help:%E9%80%9F%E6%9F%A5%E8%A1%A8.html> "Help:速查表")有一个关于 wiki 标记语言的概览，[Help:术语表](<../zh-cn/Help:%E6%9C%AF%E8%AF%AD%E8%A1%A8.html> "Help:术语表")中记载了本 wiki 中一些常用术语的翻译及使用概况。 

##  创建账号

[创建账号](<../Special:%E5%88%9B%E5%BB%BA%E8%B4%A6%E6%88%B7.html> "Special:创建账户")后方可编辑本中文 Wiki 内容，要编辑英文 Wiki 内容，请先[创建英文 ArchWiki 账号](<https://wiki.archlinux.org/title/Special:CreateAccount> "arch:Special:CreateAccount")。要回答英文账号创建时的问题，需要一个Arch Linux 环境或者 [pacman-static](<https://aur.archlinux.org/packages/pacman-static/>)AUR 或者 [Docker](<../zh-cn/Docker.html> "Docker") 镜像。我们也鼓励非 Arch 用户参与 wiki 贡献，请[下载](<https://archlinux.org/download/>)最新的安装环境，在 Live 系统中就可以获得问题的答案。创建账号后，[登录](<../Special:%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95.html> "Special:用户登录")系统。 

**注意：**[单点登录](<https://en.wikipedia.org/wiki/Single_sign-on> "wikipedia:Single sign-on")（基于[accounts.archlinux.org](<https://accounts.archlinux.org/>)的）[尚未实装](<https://gitlab.archlinux.org/archlinux/infrastructure/-/issues/38>)。

##  编辑

要开始编辑一个页面，点击页面顶端或者章节旁边的**编辑** 链接，可进行[所见即所得编辑](<https://www.mediawiki.org/wiki/Help:VisualEditor/User_guide> "mw:Help:VisualEditor/User guide")。也可以点击页面顶端的**编辑源代码** 标签。用户也可以通过点击章节头部的**编辑源代码** 链接编辑文章的特定部分。点击后将会显示**编辑源代码** 页面，包含如下元素： 

  * 编辑工具栏 (可选)
  * 编辑框
  * 编辑总结
  * “保存本页”，“显示预览”，“显示更改”和“取消”链接
  * _保存更改_ 或 _保存页面_ , _显示预览_ , _显示更改_ 和 _取消_ 链接

编辑框包含页面或章节最新版本的 **wiki文字** (服务器可以生成实际页面的源代码) 。进行编辑： 

  1. 按需编辑 wiki 内容(详情参见下面的[#格式](<#%E6%A0%BC%E5%BC%8F>)).
  2. 在**[摘要](<https://meta.wikimedia.org/wiki/Help:Edit_summary> "metawikimedia:Help:Edit summary")** 框中解释所作修改（例如: "错字更正" 或是 "新增关于 xyz 的信息"）。

**注意：** 所有的编辑都应该附有描述性的摘要，以方便其他用户的审查。更多信息参见[三个基本原则](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E4%B8%89%E4%B8%AA%E5%9F%BA%E6%9C%AC%E5%8E%9F%E5%88%99> "Project:Contributing \(简体中文\)")。

  3. 使用 **显示预览** 按钮在保存前检查页面的排版与格式。
  4. 如果修改没有太多实质性内容，请通过点击 **这是小编辑** 将编辑标记为 _[小修改](<https://en.wikipedia.org/wiki/Wikipedia:Minor_edit> "wikipedia:Wikipedia:Minor edit")_ 。
  5. 通过 **保存更改** 按钮保存。如果不满意，可以点击 **取消**(或继续完善)。

**注意：** 文章**不应该** 署名，因为它们是**合作** 成果；一个编辑者不应在众人的劳动成果上署名。

###  撤销编辑

如果页面编辑错误，可以采用如下步骤将文章回溯到上一个版本。要撤销单个编辑： 

  1. 点击要修改页面顶部的**查看历史** 标签(在**编辑** 标签旁边)，将显示版本列表。
  2. 点击错误修改右边的**撤销** 链接，将显示编辑预览，左侧显示当前版本，右侧显示要保存的版本。
  3. 记录撤销的原因
  4. 如果满足要求，点击页面底部的**保存更改** 按钮。

Wiki 页面将回到原始状态。 

有时需要同时撤销多个编辑，要回溯到以前的版本： 

  1. 点击要修改页面顶部的 **查看历史** 标签(在 **编辑** 标签旁边)，将显示版本列表。
  2. 通过点击相应的时间戳查看需要的版本（即最后的**好** 版本），将显示那个版本。
  3. 记录时间戳和回退到之前状态的原因。
  4. 如果满足要求，点击页面底部的 **编辑** 标签，将显示警告：**警告：您正在编辑该页面的旧版本。** 如果您发布该更改，该版本后的所有更改都会丢失。。只需要点击 **保存更改** 就可以回到这个版本。

**注意：** 请避免同时进行撤销和编辑！先撤销，然后进行修改；不要编辑版本预览。

如果是撤销编辑，请尽量写一个详细和丰富的编辑说明。 

##  创建页面

创建新页面前，请考虑如下内容： 

  1. 您的话题是否和 Arch Linux 相关？无关和没什么帮助的文章将被删除。
  2. 别人是否对您的话题感兴趣? 不仅考虑您想写什么，还要考虑别人想读什么。个人信息应该放在你的 _用户_ 页面。
  3. 您的话题是否值得增加单独页面？在 wiki 中查找相似文章，如果已经存在，可以考虑完善它或者新增一个章节。
  4. 您是否愿意贡献足够的内容？请避免仅添加话题，除非计划很快就会扩展和完善它。

创建新页面要求选择一个描述性的**标题** 和合适的**分类** 。 

请阅读[文章命名指导](<../zh-cn/Help:Article_naming_guidelines.html> "Help:Article naming guidelines")和[选择短文件名](<../zh-cn/Help:Article_naming_guidelines.html> "Help:Article naming guidelines")获取文章命名经验。 

  1. 标题应该包含大小写：使用 _Title for New Page_ ；而不是 _Title for new page_ 。
  2. 不要包含 "Arch Linux" 之类的修饰。这是 Arch Linux wiki；所有的文章都与 Arch Linux 相关(例如使用 Installing Openbox; 而不是 Installing Openbox in Arch Linux)。

访问[目录列表](<../zh-cn/Table_of_Contents.html> "Table of Contents")选择一个合适的类别。 文章可以属于多个类别。 

要在某个分类中添加新文章，(例如添加 "My New Page" 到 "Some Category")，您只需要： 

  1. 通过浏览 [https://wiki.archlinuxcn.org/wiki/My_new_page](<../zh-cn/My_new_page.html>) 创建一个页面(别忘了替换 "My_new_page"!)
  2. 在您**页面的顶端** 添加`[[Category:Some Category]]`

**注意：****不要创建无分类的页面!** 任何页面都必须属于至少一个分类。如果找不到合适的分类，请考虑创建一个分类。简体中文文章应该添加[[Category:简体中文]] 

这些页面目前还是[孤立页面](<../Special:%E5%AD%A4%E7%AB%8B%E9%A1%B5%E9%9D%A2.html> "Special:孤立页面")，请花些时间将其与其它页面链接起来，这样用户更容易找到它，并贡献内容。 

若您创建的新页面是 ArchWiki 上其他语言的本地化版本，那么请遵循下面的步骤： 

**注意：** ArchWiki 上面的非英文文章统一遵循了 **英文名_(语言)** 的命名规范（例如 Main_page_(简体中文)）

  1. 翻译文章标题（如果文章标题不需要翻译则跳过本条）
  2. 使用翻译后的文章标题在本站创建页面，标题中去掉 ArchWiki 中的语言信息（例如：为 Main_page_(简体中文) 创建本地化的标题应为**首页** 而不是**首页_(简体中文)** 或**首页_(繁体中文)** ）。
  3. 在本站创建重定向，将 ArchWiki 上的原标题重定向至上一步中创建的页面。（例如：将 Main_page_(简体中文) 重定向到**首页** ）。

部分情况下可以创建 _子页面_ ，也就是某个页面下的页面。子页面的标题格式一般是父页面标题+斜杠（“/”）+子页面标题。子页面功能一般可以用于在自己的用户页下创建页面草稿，比如[https://wiki.archlinuxcn.org/wiki/User:Myself/My_new_subpage](<../Special:%E6%88%91%E7%9A%84%E7%94%A8%E6%88%B7%E9%A1%B5/My_new_subpage.html> "Special:我的用户页/My new subpage")。 

##  格式

大部分的文字显示格式都可以用 wiki 内置的标记语法（称为wikitext）来实现，你不需要学习使用 HTML。常用的工作可以通过模板实现，[模板](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html> "Help:Template")页面包含模板使用的相关信息。[速查表](<../zh-cn/Help:%E9%80%9F%E6%9F%A5%E8%A1%A8.html> "Help:速查表")整理了常用的格式选项。 

###  标题与子标题

标题和子标题是提高文章的组织结构的常用方法。如果讨论了两个或两个以上的主题，可以在文章内为每个章节添加一个标题。请阅读[有效使用标题](<https://wiki.archlinux.org/title/Effective_Use_of_Headers> "en:Effective Use of Headers")获取更多信息。 

标题创建： 
    
    ==一级标题==
    ===二级标题===
    ====三级标题====
    =====四级标题=====
    
  1. 标题的大小写遵照句子规范**而不是** 标题规范，使用 _My new heading_ 而不是 _My New Heading_ 。
  2. 不应该跳过标题级别，也就是说，没有在二级标题之内就不要使用三级标题。

如果一篇文章使用四个以上的标题，系统会自动生成内容列表 (TOC)。如果不想使用内容列表，你可以在页面中添加 __NOTOC__。 请试着在[沙盒](<../Project:%E6%B2%99%E7%9B%92.html> "Sandbox")内建立几个标题，然后看看他们对内容列表的影响。 

###  换行

重要格式提示： 布局中单个换行是没有效果的，所以 
    
    这句话
    被分成
    三行。
    
...将显示为： 

这句话 被分成 三行。 

空行将新起一个段落，例如： 
    
    这是第一段。
    
    这是第二段。
    
...将显示为： 

这是第一段。 

这是第二段。 

HTML `<br>` 也可以实现手动换行，但是应该避免这么做。手动换行还会在其他格式元素中使用， 例如列表（后面会详细讲解列表）： 
    
    * 这个点 <br> 扩展到多行
    * 这个点
    结束列表
    
...将显示为： 

  * 这个点   
扩展到多行
  * 这个点

结束列表 

###  粗体与斜体

文字放在数个单引号 (') 之间将表现出 **Bold - 粗体** 和 _italics - 斜体_ 的效果: 

  * `''italics - 斜体''` 显示为 _italics - 斜体_. (前后加上两个单引号)
  * `'''bold - 粗体'''` 显示为 **bold - 粗体**. (前后加上三个单引号)
  * `'''''bolded italics - 粗体斜体字'''''` 显示为 _**bolded italics - 粗体斜体字**_. (前后加上 2 + 3 = 五个单引号)

**注意：** 中文的斜体字很不美观，字形非常贴近后面的文字，影响阅读，翻译时请尽量用双引号或者粗体替换。在有合适的字体时（如 [ttf-lxgw-wenkai](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/ttf-lxgw-wenkai>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")），本维基上的斜体中文会显示为 _楷体或者仿宋体_ 。

###  删除线

用删除线表示文字已经没有作用或者无关。 

例如： 
    
    <s>删除的文字</s>

...显示为 

~~删除的文字~~

###  要点列表

请使用星号 (`*`)插入一个新要点。插入星号越多，缩进越多。 

例如： 
    
    *第一条
    *第二条
    **第二条的子项
    *有趣吗？
    
显示为: 

  * 第一条
  * 第二条 
    * 第二条的子项
  * 有趣吗？

###  编号列表

要建立编号列表，请使用数字符号或是井字号 (`#`)。多个井字号 `#` 将增加缩进层次。 

例如: 
    
    # 第一条
    # 第二条 
    ## 子条目
    # 第三条 
    
...将显示为： 

  1. 第一条
  2. 第二条 
     1. 子条目
  3. 第三条

编号列表可以和要点列表混合使用，例如： 
    
    # 第一条
    # 第二条 
    #* 子条目
    # 第三条 
    
...将显示为： 

  1. 第一条
  2. 第二条 
     * 子条目
  3. 第三条

###  定义列表

可以通过在行首使用分号(`;`) + 定义名称 + 冒号(`:`) + 定义说明 生成定义列表。 

例如： 
    
    ; Apple: Fruit with red or yellow or green skin and sweet to tart crisp whitish flesh
    ; Banana: Elongated crescent-shaped yellow fruit with soft sweet flesh
    
...将显示为： 

Apple
    Fruit with red or yellow or green skin and sweet to tart crisp whitish flesh
Banana
    Elongated crescent-shaped yellow fruit with soft sweet flesh

可以使用多个冒号将定义分成多行。 

例如： 
    
    ; Term: First line of definition
    : Second line of definition
    : Third line of definition
    
...将显示为： 

Term
    First line of definition
    Second line of definition
    Third line of definition

###  缩进

要缩进文字，请在行首插入冒号 (`:`) 。插入冒号越多，文字就缩进越多。新行(按下 **Enter** 或是 **Return** 后) 将结束整段文字的缩进。 

例如： 
    
    这行靠最左对齐。
    :这行稍微缩进。
    ::这行缩进更多
    
显示为： 

这行靠最左对齐。 

    这行稍微缩进。 

    这行缩进更多。

在内容页面中，仅在必须时再使用缩进。在讨论页中，请用缩进区分回复。例如： 
    
    话题话题话题话题话题--~~~~
    :回复1--~~~~
    ::回复1回复1--~~~~
    ::回复1回复2--~~~~
    :回复2--~~~~
    ::回复2回复1--~~~~
    :::回复2回复1回复1--~~~~
    ::回复2回复2--~~~~
    
即，要回复某条，就相对于被回复的层数再缩进一层。对于缩进非常多的情况，其他wiki会相应再使用一些模板标识，但本wiki暂无。 

###  代码

在 wiki 页面使用代码格式非常简单：你只需要在每一行文字前加上一个空格。然而请注意行宽，因为代码**不会** 自动断行。 

注意，如果空格之后有冒号，需要将空格写作 `&#32;`，以避免被 wiki [自动转换](<https://meta.wikimedia.org/wiki/Help:Newlines_and_spaces#Non-breaking_spaces> "metawikimedia:Help:Newlines and spaces")成[不换行空格（nbsp）](<https://zh.wikipedia.org/wiki/%E4%B8%8D%E6%8D%A2%E8%A1%8C%E7%A9%BA%E6%A0%BC> "zhwp:不换行空格")。例如以下代码并不能直接复制后运行： 
    
    $ fc-list : file
    
而这样则可以： 
    
    $ fc-list : file
    
也可以使用 `<syntaxhighlight>` 标签来通过站点的Pygments软件高亮代码，详见 [SyntaxHighlight 扩展页面](<https://www.mediawiki.org/wiki/Extension:SyntaxHighlight/zh> "mw:Extension:SyntaxHighlight/zh")。使用可视化编辑器则可以直接从工具栏调整格式或者插入代码块。 

另请参见[代码格式模板](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#%E4%BB%A3%E7%A0%81%E6%8E%92%E7%89%88%E6%A8%A1%E6%9D%BF> "Help:模板")。 

###  表格

有效使用表格可以帮助组织和汇总大量数据。高级表格语法和格式请查看 [Help:Table](<https://en.wikipedia.org/wiki/Help:Table> "wikipedia:Help:Table"). 

例如： 
    
    {| border="1"
    |+ 表格数据
    ! 水果!! 颜色
    |-
    | 苹果 || 红色
    |-
    | 橘子 || 橙色
    |-
    | 香蕉|| 黄色
    |}
    
...将被显示为： 

表格数据  水果 | 颜色   
---|---  
苹果 | 红   
橘子 | 橙   
香蕉 | 黄   
      
    {| class="wikitable" border="1" cellpadding="5" cellspacing="0"
    ! RAID 级别 !! 数据 !! 使用!! 读 !! 写!! 稀疏!! 最大!! 最小
    |-
    | 0 || 否 || 100% || 好 || 好|| No || 1 || 16
    |-
    | 1 || 是|| 50% || 非常高 || 非常高 || No || 2 || 2
    |}

显示为: 

RAID 级别 | 数据 | 使用 | 读 | 写 | 稀疏 | 最大 | 最小   
---|---|---|---|---|---|---|---  
0 | 否 | 100% | 好 | 好 | No | 1 | 16   
1 | 是 | 50% | 非常高 | 非常高 | No | 2 | 2   
  
###  链接

链接是用帮助使用者浏览网站的关键。编辑者应该确保每篇文章都包含到其它文章的链接（避免[断链页面](<../Special:%E6%96%AD%E9%93%BE%E9%A1%B5%E9%9D%A2.html> "Special:断链页面")）并被其它文章引用。[链入页面](<../Special:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2.html> "Special:链入页面")可以用来显示链入的页面。参考 [Help:Style/Formatting and punctuation#First instances](</wzh/index.php?title=Help:Style/Formatting_and_punctuation&action=edit&redlink=1> "Help:Style/Formatting and punctuation（页面不存在）"). 

####  内部链接

你可以大量应用内部链接交叉引用 Wiki 页面。链接目标可以是已经存在的标题，或是之后应该存在的标题。 

在同一 wiki 内，要链接一个页面，只需要用双中括号包含要链接页面的标题。 

例如，如果你想要设定个链接到文章 [pacman](<../zh-cn/Pacman.html> "Pacman")，只需要： 
    
    [[pacman]]
    
如果希望使用页面标题以外的文字作为链接的标题，可以通过在链接和要使用的名字间插入 "|" 分隔符实现(在英文键盘上，使用`Shift` \+ `\`打出 "|")。 

例如 
    
    查看 [[Arch Linux (简体中文)|这篇]]  文章...
    
...将显示为： 

    查看[这篇](<../zh-cn/Arch_Linux_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Arch Linux \(简体中文\)")文章...

如果希望在链接的页面名称后面加上复数 (或是任何后缀文字)，可以把要加的文字直接放在包着链接页面的中括号后面。 

例如： 
    
    makepkg is used in conjunction with [[PKGBUILD]]s.
    
...将显示为： 
    
    makepkg is used in conjunction with [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")s.
    
#####  到文档章节的链接

要链接到文章的某个章节，只需要添加 `#` 加章节标题。 

例如： 
    
    [[ArchWiki Tutorial (简体中文)#到文档章节的链接]]
    
...将显示为： 

    [ArchWiki Tutorial (简体中文)#到文档章节的链接](</wzh/index.php?title=ArchWiki_Tutorial_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "ArchWiki Tutorial \(简体中文\)（页面不存在）")

**提示：**

  1. 如果链接到同页面的章节，可以省略文档名(例如, `[[#到文档章节的链接]]`)。
  2. 如果有相同名称的章节，又想链接到第二个该名称的章节，可以在章节名后添加下划线加数字，例如： [[ArchWiki Tutorial (简体中文)#到文档章节的链接_2]]。

**注意：** 如果目标页面不存在，将显示为 [red link](</wzh/index.php?title=Red_link&action=edit&redlink=1> "Red link（页面不存在）")，根据 [Help:Style#Hypertext metaphor](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html#Hypertext_metaphor> "Help:Style")，请尽量避免这种情况。

####  多国语言链接

请访问[跨语言链接](<../zh-cn/Help:I18n_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E8%B7%A8%E8%AF%AD%E8%A8%80%E9%93%BE%E6%8E%A5> "Help:I18n \(简体中文\)")。 

####  跨 Wiki 链接

**跨 Wiki 链接** 可以链接到其他 Wiki 文章，例如 Wikipedia。这种链接的语法格式为双中括号 Wiki 名称加冒号加要链接的文章。 

要链接到文章 [Wikipedia:Arch Linux](<https://en.wikipedia.org/wiki/Arch_Linux> "wikipedia:Arch Linux")，可以使用： 
    
    [[Wikipedia:Arch Linux]]
    
通过管道可以用新的名字显示链接。例如到 [Arch Linux Wikipedia article](<https://en.wikipedia.org/wiki/Arch_Linux> "wikipedia:Arch Linux") 的链接: 
    
    [[Wikipedia:Arch Linux|Arch Linux Wikipedia article]]
    
**注意：** 用管道链接设定新名字的方式只应该用于缩短长地址。

参见： [Wikipedia:InterWikimedia links](<https://en.wikipedia.org/wiki/InterWikimedia_links> "wikipedia:InterWikimedia links")

####  站外链接

要链接到外部网站，请直接写出目标网页的完整 URL。 
    
    https://archlinux.org/
    
在很多时候，我们都会给链接的 URL 设定含意比较清楚的名称。 把链接的 URL 放在中括号内，然后在 URL 后加上一个**空格** (_不是_ pipe)。要显示， [Arch Linux](<https://archlinux.org/>) ，可以使用: 
    
    [https://archlinux.org/ Arch Linux]
    
**注意：** 如果链接到其它 ArchWiki 或 Wikipedia 页面，请**使用[#内部链接](<#%E5%86%85%E9%83%A8%E9%93%BE%E6%8E%A5>) 或 [#跨 Wiki 链接](<#%E8%B7%A8_Wiki_%E9%93%BE%E6%8E%A5>) 而不是外部链接!**也就是说，如果链接以 <https://wiki.archlinux.org/> 开始，**请使用内部链接；** 如果以 <https://en.wikipedia.org/> 开始，**使用跨 wiki 链接!**

###  重定向

要把一个页面自动跳转到另一个，请使用 `#REDIRECT` 这个指令，同时把新转过去的网页名称放在括号内。 

例如，你可以设定把 "Cats" 这个页面自动转向 "Cat"： 
    
    #REDIRECT [[Cat]]
    
这样，不管使用者在搜索里输入的是哪一个，他们都会进入 "Cat" 这个页面。 

重定向之后的文字都不会被显示，然而类别标签仍然会起作用，以保证重定向会包含在类别列表中。 

  * 不应该重定向到其它网站
  * [分类页面](<../zh-cn/Help:%E5%88%86%E7%B1%BB.html> "Help:Category")不支持重定向.
  * 重定向是服务器内部解析，不会影响页面的打开速度。

###  Wiki 变量、特殊字符和模板 (templates)

MediaWiki 识别一些改变标准行为的特殊字符串。例如，在文章任意位置加入 `__NOTOC__` 将不会生成内容列表。而 `__TOC__` 将改变内容列表的位置。详情参见 [mw:Help:Magic words](<https://www.mediawiki.org/wiki/Help:Magic_words> "mw:Help:Magic words")。 

模板和变量为事先定义的 wiki 文字，加入文章后会增加格式化的内容。 

变量由系统定义，用来显示当前页面的信息、wiki 或者日期。例如，使用 `{{SITENAME}}` 显示 Wiki 网站的名字（本 Wiki 为 _**Arch Linux 中文维基**_ ）。要为页面设置新标题，可以使用变量：`{{DISPLAYTITLE:新标题}}` (仅允许大小写更改)。 

模板则为用户定义。**任意** 页面的内容都可以被其它页面引用，只需要在文章中加入 `{{命名空间:页面名称}}` 。但是除 **Template** 命名空间之外，这个功能很少被使用。(如果忽略命名空间，默认为 _Template_ 。) 例如, [Template:注意](<../zh-cn/Template:%E6%B3%A8%E6%84%8F.html> "Template:注意"),可以通过在文章中加入如下内容引用： 
    
    {{注意|这是个注释。}}

...将显示为： 

**注意：** 这是个注释。

更多信息请查看 [Help:模板](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html> "Help:模板")。 

##  使用机器人编辑

如果您的编辑需要进行大量或重复的修改，则可以考虑使用机器人编辑。 

###  注册机器人账户

  1. 登录主账户。
  2. 访问 [Special:创建账户](<../Special:%E5%88%9B%E5%BB%BA%E8%B4%A6%E6%88%B7.html> "Special:创建账户")。
  3. 以主账户用户名+“.bot”为用户名注册。

###  使用机器人账户编辑

这部分请参考 [Wikipedia:制作机器人](<https://zh.wikipedia.org/wiki/Wikipedia:%E8%A3%BD%E4%BD%9C%E6%A9%9F%E5%99%A8%E4%BA%BA> "zhwp:Wikipedia:制作机器人")。 
