**翻译状态：**

  * 本文（或部分内容）译自 [Help:Category](<https://wiki.archlinux.org/title/Help:Category> "arch:Help:Category")，最近一次同步于 2021-03-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Help:Category?diff=0&oldid=486114>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Help:Category_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

每篇文章都应该有分类，分类在 Arch Wiki 的页面底部显示。一篇文章可以同时属于多个分类。本指南介绍如何设置页面分类，如何创建缺失的分类以及如何将修改页面的分类。 分类的使用规则请参考 [Help:Style (简体中文)](<../zh-cn/Help:Style_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Help:Style \(简体中文\)")。 

本文中使用的文章和分类都是示例，不是真实存在的页面。 

**注意：** 本文所说内容同时适用于页面和分类，分类本身也可能属于更大的分类。

##  设置页面分类

点击页面上面的“编辑”按钮，添加如下文字： 
    
    [[Category: Some Category]]
    
请尽可能使用已有的分类，可以在 [Table of contents](<../zh-cn/Table_of_contents.html> "Table of contents") 查看所有的已有分类。只有一篇新文章实在找不到合适的分类再创建新的分类，务必使用不存在的分类保存页面，然后按照[#创建新分类页面](<#%E5%88%9B%E5%BB%BA%E6%96%B0%E5%88%86%E7%B1%BB%E9%A1%B5%E9%9D%A2>)进行操作。 

##  创建新分类页面

保存后，可以在页面底部看到`"[[Category: Some Category (English)]]"`链接。如果分类还不存在，将显示为红色高亮。点击红色链接，进入新创建的页面。 

设置其父分类： 
    
    [[Category:Parent Category]]
    
最后保存分类页面。 

如果新分类需要一个还不存在的父分类，请在新分类的对话页中打开一个讨论，而不是自己创建一个全新的分类树。 

##  修改页面分类

要修改分类，只需编辑 `[[Category:Some category]]` 这一行。 

例如要将 "ArchWiki Tutorial (Magyar)" 移到到新分类，编辑页面，将 
    
     [[Category:帮助]]
    
修改为: 
    
     [[Category:Help (Magyar)]]
    
点击编辑框下方的保存按钮保存更改。 

##  i18n 分类名

分类标题遵循 [Help:i18n (简体中文)#文章标题](<../zh-cn/Help:I18n_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E6%96%87%E7%AB%A0%E6%A0%87%E9%A2%98> "Help:I18n \(简体中文\)")中描述的相同规则，但请注意它们不能利用 [Help:i18n (简体中文)#本地化标题重定向](<../zh-cn/Help:I18n_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E6%9C%AC%E5%9C%B0%E5%8C%96%E6%A0%87%E9%A2%98%E9%87%8D%E5%AE%9A%E5%90%91> "Help:I18n \(简体中文\)")仅仅是因为 MediaWiki 不支持。‏‎ 

##  分类列表

  * 查看[目录表](<../zh-cn/Table_of_contents.html> "Table of contents").
  * 全部分类列表：[Special:Categories](<../Special:%E9%A1%B5%E9%9D%A2%E5%88%86%E7%B1%BB.html> "Special:页面分类").
  * 未分类的分类： [Special:Uncategorizedcategories](<../Special:%E6%9C%AA%E5%BD%92%E7%B1%BB%E5%88%86%E7%B1%BB.html> "Special:未归类分类").
  * 未分类文章：[Special:Uncategorizedpages](<../Special:%E6%9C%AA%E5%BD%92%E7%B1%BB%E9%A1%B5%E9%9D%A2.html> "Special:未归类页面").
  * 空分类：[Special:Unusedcategories](<../Special:%E6%9C%AA%E4%BD%BF%E7%94%A8%E5%88%86%E7%B1%BB.html> "Special:未使用分类").
