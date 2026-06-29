相关文章

  * [Project:翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")
  * [国际社区](<../zh-cn/%E5%9B%BD%E9%99%85%E7%A4%BE%E5%8C%BA.html> "国际社区")

**翻译状态：**

  * 本文（或部分内容）译自 [Help:I18n](<https://wiki.archlinux.org/title/Help:I18n> "arch:Help:I18n")，最近一次同步于 2022-10-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Help:I18n?diff=0&oldid=750932>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Help:I18n_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

注意：本页面为英文版 ArchWiki 之翻译，所述内容适用于英文版 ArchWiki，并不一定适用于本中文维基，其中的链接也可能并不指向正确的地方。

本文是 ArchWiki [国际化和本地化](<https://en.wikipedia.org/wiki/Internationalization_and_localization> "wikipedia:Internationalization and localization")的全面指引。 

##  准则

###  文章标题

非英文文章的标题应该命名为**“Title in English (Language)”** ，其中**“Language”** 是文章所用语言的本地化拼写，括弧前有一个空格。例如：[Installation guide (简体中文)](</wzh/index.php?title=Installation_guide_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Installation guide \(简体中文\)（页面不存在）")。英文标题不能包含语言标签。 

使用子页面时，语言标签应该放到每层标题末尾，所以不应该使用 **Title (Language)/Sub-page** ，而应该使用 **Title (Language)/Sub-page (Language)** ，例如 [systemd (简体中文)/User (简体中文)](</wzh/index.php?title=Systemd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/User_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Systemd \(简体中文\)/User \(简体中文\)（页面不存在）")。在每层标题上使用语言标签可以链接到正确的上层页面，特别是最后一个标签会自动添加到跨语言链接中，而且它使自动处理工具检测页面语言更加实用和安全。**Title/Sub-page (Language)** 是过去接受的格式，现在已经过时，但某些页面可能仍在使用。 

[所有语言的根类别](</wzh/index.php?title=Category:Languages&action=edit&redlink=1> "Category:Languages（页面不存在）")是唯一的例外，因为不需要在后缀重复语言名称。 

合理性： 

  * 英文标题方便管理；[管理员](</wzh/index.php?title=Project:Administrators&action=edit&redlink=1> "Project:Administrators（页面不存在）")都会英语，但不一定会多种语言。浏览[最近更改](<../Special:%E6%9C%80%E8%BF%91%E6%9B%B4%E6%94%B9.html> "Special:最近更改")和其他特殊页面时，管理员能够不借助翻译就知道编辑的文章。

  * 标准化的文章标题简化了跨语言链接。

###  本地化标题重定向

可以并且需要创建本地化标题, 但是必须重定向至如上所述的英文命名的文章。重定向文章的标题并不需要包含语言标签。例如：[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")重定向至 [Installation guide (简体中文)](</wzh/index.php?title=Installation_guide_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Installation guide \(简体中文\)（页面不存在）")。请注意，这不适用于[分类页面](<../zh-cn/Help:%E5%88%86%E7%B1%BB.html> "Help:Category")，因为分类不支持重定向（将一个页面分类到重定向分类下，并不会导致该页面显示在重定向的目标分类下）。 

合理性： 

  * 本地化的标题有利于不同语言用户的浏览。内部和外部搜索都能够使用这些重定向。
  * 合理使用重定使内部链接更方便。

###  跨语言链接

如果文章有多个语言的版本，请在文章顶部加入跨语言链接。 
    
    [[de:Title]]
    [[en:Title]]
    [[zh-hans:Title]]
    
**注意：** 跨语言链接会自动加入文章标题中规定的后缀所以 [主页](</wzh/index.php?title=%E4%B8%BB%E9%A1%B5&action=edit&redlink=1> "主页（页面不存在）") 对应的跨语言链接是 ` 对应的跨语言链接是 {{ic|<nowiki>[[zh-hans:Help:Style (简体中文)/Formatting and punctuation]]`。

可用的语言标签参见 [#语言列表](<#%E8%AF%AD%E8%A8%80%E5%88%97%E8%A1%A8>)。使用指南参见 [Help:Style (简体中文)#跨语言链接](<../zh-cn/Help:Style_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E8%B7%A8%E8%AF%AD%E8%A8%80%E9%93%BE%E6%8E%A5> "Help:Style \(简体中文\)")

合理性： 

  * 在文档开头增加跨语言链接有利于不同语言的用户立即确定文档是否被翻译。而且翻译人员也能够立即确定文章是否需要翻译。

####  查找带有某个跨语言链接的页面

要查找带有某文章跨语言链接的页面，请使用: 

[https://wiki.archlinux.org/api.php?action=query&list=langbacklinks&lbllimit=500&lblprop=lltitle&lbllang=en&lbltitle=Main%20page](<https://wiki.archlinux.org/api.php?action=query&list=langbacklinks&lbllimit=500&lblprop=lltitle&lbllang=en&lbltitle=Main%20page>)

这个查询将搜索 `[[en:Main page]]` 的链入页面，其它语言可以修改 `lbllang` 和 `lbltitle`。 

如果要查找带某个语言的跨语言链接列表，请忽略 `lbltitle` 关键字： 

[https://wiki.archlinux.org/api.php?action=query&list=langbacklinks&lbllimit=500&lblprop=lltitle&lbllang=de](<https://wiki.archlinux.org/api.php?action=query&list=langbacklinks&lbllimit=500&lblprop=lltitle&lbllang=de>)

此示例将查找所有德语（`de`）跨语言链接的页面。修改 `lbllang` 可以查到相应的语言。 

**注意：** 这个查询可能查找不到使用跨语言链接的重定向页面（被[重定向页面](<../zh-cn/Help:Style_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E9%87%8D%E5%AE%9A%E5%90%91%E9%A1%B5%E9%9D%A2> "Help:Style \(简体中文\)")所管理）：[一个这样的查询](<https://wiki.archlinux.org/index.php?title=Special%3ASearch&profile=advanced&limit=500&offset=0&search=%22redirect%20%5B%5Bde%3A%22&fulltext=Search&ns0=1&ns1=1&ns2=1&ns3=1&ns4=1&ns5=1&ns6=1&ns7=1&ns8=1&ns9=1&ns10=1&ns11=1&ns12=1&ns13=1&ns14=1&ns15=1&redirs=1&profile=advanced>)应该可以正常运行（如果你得到 0 个结果表示一切正常）。

请注意，API 查询总是有限制的，因此，如果一种语言的反向链接超过500个，则有必要继续搜索，并将出现在列表底部的 `lblcontinue` 属性添加到查询字符串中。 

##  语言列表

参见英文版 [en:Help:I18n#Languages](<https://wiki.archlinux.org/title/Help:I18n#Languages> "en:Help:I18n"). 

表头说明： 

英语名称 | 中文名称   
---|---  
**English name** | 英文名称   
**Localized name** | 本地名称   
**Subtag** | 子标签   
**Root category** | 根类型   
**External wiki** | 外部 wiki   
  
MediaWiki 后端处理子标签时不区分大小写。按照约定，ArchWiki 上的跨语言链接应使用子标签的小写形式。关于子标签的更多信息，请查看： 

  * <https://www.iana.org/assignments/language-subtag-registry>
  * <https://tools.ietf.org/rfc/bcp/bcp47.txt>
  * <https://r12a.github.io/app-subtags/>

###  添加本地跨语言链接

如果想在 wiki.archlinux.org 为一个新语言启用跨语言链接，请在 [Help talk:I18n](</wzh/index.php?title=Help_talk:I18n&action=edit&redlink=1> "Help talk:I18n（页面不存在）") 提出申请。注意最少翻译一定的文章之后，管理员才会同意请求。请尽量采用外部 Wiki。下面的清单总结了添加新语言所需的步骤。 

  1. 在 [Help talk:I18n](</wzh/index.php?title=Help_talk:I18n&action=edit&redlink=1> "Help talk:I18n（页面不存在）") 通知有关新语言的信息。确保包含填写[语言](<../zh-cn/Help:%E5%9B%BD%E9%99%85%E5%8C%96%E5%92%8C%E6%9C%AC%E5%9C%B0%E5%8C%96.html#Languages> "Help:I18n")表的所需信息。
  2. 在 [Category:Languages](</wzh/index.php?title=Category:Languages&action=edit&redlink=1> "Category:Languages（页面不存在）") 下创建一个基础语言类别，并将翻译好的文章添加到它或一个子类别中。
  3. 一个维护者应该更新[#语言列表](<#%E8%AF%AD%E8%A8%80%E5%88%97%E8%A1%A8>)。
  4. 至少要翻译 [Main Page](<../zh-cn/Main_Page.html> "Main Page")、[Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux")、[Installation guide](<../zh-cn/Installation_guide.html> "Installation guide") 和 [General recommendations](<../zh-cn/General_recommendations.html> "General recommendations")。
  5. [初始化](</wzh/index.php?title=Project:Bots&action=edit&redlink=1> "Project:Bots（页面不存在）")一个[内容表](<../zh-cn/Table_of_contents.html> "Table of contents")的翻译：然后它将被一个机器人保持更新，见下文。
  6. 一个管理员应该考虑这个请求；然后一个维护者应该相应地更新[#语言](<#%E8%AF%AD%E8%A8%80>)表。
  7. 开发人员应更新各自的 [ArchWiki:Bots](</wzh/index.php?title=Project:Bots&action=edit&redlink=1> "Project:Bots（页面不存在）")，以支持新的语言。

###  添加外部跨语言链接

如果使用了外部 Wiki，请在 [Help talk:I18n](</wzh/index.php?title=Help_talk:I18n&action=edit&redlink=1> "Help talk:I18n（页面不存在）") 提出申请或直接联系[管理员](</wzh/index.php?title=Project:Administrators&action=edit&redlink=1> "Project:Administrators（页面不存在）")：跨语言链接将会尽快被设置！ 

###  将本地语言移到外部wiki

我们鼓励将翻译转移到独立的 Wiki 进行维护，管理员会提供尽可能的帮助。转移过程中，会先建立临时跨语言链接，一个文件一个文件转移到外部 Wiki。两种可能的转移方式： 

  * 首先将**所有** 文章转移到外部 wiki。完成之后，更新跨语言链接指向新站点，将所有目标标题修改为新标题。最后删除所有本站中该语言的文章，或者在[维护团队](<../Project:Maintenance_Team_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Project:Maintenance Team \(简体中文\)")的授权下，用跨语言链接将它们重定向至外部 wiki。
  * 设置临时跨语言链接（例如 `[[ja-temp:Title]]`），并使用它们将各种文章“一个个地”移动到外部Wiki。移动完成后，将常规的跨语言链接（即 `[[ja：Title]]`）指向外部wiki，并使用新的目标标题对其进行更新。接下来，删除本地重定向，或者在[维护团队](<../Project:Maintenance_Team_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Project:Maintenance Team \(简体中文\)")的授权下，更新它们以使用常规的跨语言链接。最后，禁用临时跨语言链接。
