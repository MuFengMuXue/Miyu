本文介绍翻译的基本流程，[中文翻译组页面](<../Project:Translation_Team.html> "Project:Translation Team")包含了当前的页面认领列表。 

##  如何开始翻译一篇新页面

  * 创建中文标题的页面，将英文页面的内容复制于其中

**警告：** 如果不准备翻译页面的大部分内容，请尽量不要新建简体中文页面。检查英文页面的更新需要花费不少精力，没有翻译的页面会增加维护负担。管理员在清理历史页面的时候，可能会将长期未翻译的页面改为到英文页面的重定向。

  1. 如果还不知道如何编辑 wiki，请阅读[编辑帮助](<../zh-cn/Help:Editing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Help:Editing \(简体中文\)")。
  2. 阅读 [i18n 帮助](<../zh-cn/Help:I18n_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Help:I18n \(简体中文\)")，文章给出了 ArchWiki 国际化和本地化的指南。
  3. [登录](<../Special:%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95.html> "Special:用户登录")以进行编辑。
  4. 选择要翻译的页面，例如从[随机页面](<../Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2.html> "Special:随机页面")或[页面维护列表](<#%E9%A1%B5%E9%9D%A2%E7%BB%B4%E6%8A%A4%E5%88%97%E8%A1%A8>)中选择一个未翻译完成的页面。假设要翻译 [ArchWiki:Translation Team](<../Project:Translation_Team.html> "Project:Translation Team")。
  5. 进入选择的英文页面，点击页面顶部的**编辑** 。
  6. 添加要翻译文件的语言间链接, 简体中文的话加入 [[zh-hans:Some Page]]，其它语言参见 [Help:i18n#Interlanguage links](<../zh-cn/Help:%E5%9B%BD%E9%99%85%E5%8C%96%E5%92%8C%E6%9C%AC%E5%9C%B0%E5%8C%96.html#Interlanguage_links> "Help:I18n"))。
  7. 复制所有页面代码。
  8. 预览页面 (新加了语言链接)
  9. 访问页面左边新添加的语言链接，应该会进到 [ArchWiki Translation Team](</wzh/index.php?title=ArchWiki_Translation_Team&action=edit&redlink=1> "ArchWiki Translation Team（页面不存在）")（打开新标签页，不要关闭预览的页面）
  10. 从 2022-11-28 开始，跨语言链接会跳转到单独的[Arch Linux 中文维基](<https://wiki.archlinuxcn.org>)，请在 Arch Linux中文维基网站中新建帐号。
  11. 因为页面不存在，点击**创建** 。
  12. 将显示一个编辑器 - 粘贴复制的英文页面。
  13. 将文章分类修改为本地化版本，例如将 `[[Category:Networking]]` 修改为 `[[Category:网络]]`，参阅 [Help:Category (简体中文)](<../zh-cn/Help:Category_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Help:Category \(简体中文\)") 和[目录](<../zh-cn/%E7%9B%AE%E5%BD%95.html> "目录").
  14. 修改语言间链接，仅保留到英文页面的跨语言链接（将 `zh-hans` 修改为 `en`，并删除其它跨语言链接）。
  15. 翻译页面，进行保存，还需要使用合适的[编辑摘要](<../zh-cn/Help:Style_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BC%96%E8%BE%91%E6%91%98%E8%A6%81> "Help:Style \(简体中文\)")，例如 `translate [[ArchWiki Translation Team]]`。碰到不好翻译的段落，可以保留英文。尽量不要让原文和不太确认的翻译同时存在，会让页面看上去比较杂乱。
  16. 在翻译页面的底部，列出了该页面所包含的类别。检查所有这些类别是否存在，即，链接不应为红色。否则，请点击红色链接，然后创建所有缺少的类别 - 类别的创建方式与常规页面相同。
  17. 返回预览的页面并保存页面。
  18. 将 [Template:翻译状态](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html> "Template:翻译状态")添加到已翻译的页面。有关使用方法，请参见 [Template:翻译状态#用法](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html#%E7%94%A8%E6%B3%95> "Template:翻译状态")。
  19. （可选）创建另一个页面，例如 [ArchWiki Translation Team](</wzh/index.php?title=ArchWiki_Translation_Team&action=edit&redlink=1> "ArchWiki Translation Team（页面不存在）") 翻译后的标题将是 [ArchWiki 翻译团队](<../zh-cn/ArchWiki_%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "ArchWiki 翻译团队")，输入 `#redirect [[ArchWiki Translation Team]]` 作为其唯一内容并保存。
  20. 开始逐个段落地翻译，并适时保存以防丢失

您可以使用工具栏上的“翻译”小工具，使用机器翻译的结果来协助。使用 `{{[link-en](<../zh-cn/Template:Link-en.html> "Template:Link-en")}}` 模板来为尚未创建的页面链接到英文版本。 

##  如何更新已翻译的页面

  * 点击[Template:翻译状态](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html> "Template:翻译状态")中的链接，查看 ArchWiki 更新的内容
  * 将更新整合到现有的页面中 
    * 注意页面内容可能不完全来源于翻译，请保留本地有用的内容
  * 如果所有更新均已完成，记得更新[Template:翻译状态](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html> "Template:翻译状态")中的 ArchWiki 页面 id，记录更新的进度

##  查找未翻译完成的页面

[这个特殊页面](<https://wiki.archlinuxcn.org/wzh/index.php?title=Special:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2/Template:%E9%9C%80%E8%A6%81%E7%BF%BB%E8%AF%91&limit=100>)包含了需要完善翻译的中文页面。完善翻译的基本步骤： 

  1. 选择自己比较熟悉的文章进行翻译
  2. 先检查英文页面的对应段落，更新成最新的英文后再翻译，避免翻译过时的内容，减少信息遗漏。
  3. 翻译完成后删除页面中的`{{[需要翻译](<../zh-cn/Template:%E9%9C%80%E8%A6%81%E7%BF%BB%E8%AF%91.html> "Template:需要翻译")}}`模板
  4. 给翻译完成的页面加上`{{[翻译状态](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html> "Template:翻译状态")}}`模板，请参见 [#创建翻译](<#%E5%88%9B%E5%BB%BA%E7%BF%BB%E8%AF%91>)。

##  更新过期页面

如果发现有 Wiki 页面过期或错误： 

  * 小的改动，有时间可以立即进行修改同步，[维护者](<../Project:Translation_Team.html> "Project:Translation Team")并不控制页面的编辑权限，越多的人参与维护越好。如果改动较大，请先联系维护者，避免重复劳动。
  * 没有时间查看更改，请给页面加上 `{{Bad translation|翻译已经过期，请阅读英文页面中的内容。}}` 模板，这样其他贡献者更容易发现需要更新的页面，而读者看到过期标记就可以直接查看英文页面，以免被错误内容误导，白白耽误时间。
  * 没有时间翻译，请将过期的中文部分删去，从英文页面中复制更改的部分到中文页面的相应部分，去掉`{{Bad translation|翻译已经过期，请阅读英文页面中的内容。}}`模板(如果页面上有的话)并加上`{{translateme (简体中文)}}`模板，这样其他贡献者就更容易发现需要翻译的页面，而读者也不会被过期的内容误导。

如果发现有页面未翻译： 

  * 有时间的话，请将页面中的英文部分翻译为中文，并去掉`{{translateme (简体中文)}}`模板。
  * 没有时间翻译，请为页面添加`{{translateme (简体中文)}}`模板，这样其他的贡献者就能更容易发现需要翻译的页面。

**注意：** 在修改页面上的模板时，请同时更新[Project:翻译团队#页面维护列表](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html#%E9%A1%B5%E9%9D%A2%E7%BB%B4%E6%8A%A4%E5%88%97%E8%A1%A8> "Project:翻译团队")的翻译状态。

##  模板

下表列出了应翻译的英文[模板](<../zh-cn/Help:Template_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Help:Template \(简体中文\)")及其等效的简体中文模板。 

英文模板 | 简体中文模板   
---|---  
文章模板   
[Template:Related articles start](<../zh-cn/Template:Related_articles_start.html> "Template:Related articles start") |  [模板:相关文章开始](<../zh-cn/Template:%E7%9B%B8%E5%85%B3%E6%96%87%E7%AB%A0%E5%BC%80%E5%A7%8B.html> "Template:相关文章开始")  
[Template:Unsupported](<../zh-cn/Template:%E4%B8%8D%E5%8F%97%E6%94%AF%E6%8C%81.html> "Template:Unsupported") |  [Template:Unsupported](<../zh-cn/Template:%E4%B8%8D%E5%8F%97%E6%94%AF%E6%8C%81.html> "Template:Unsupported")  
[Template:Yes](<../zh-cn/Template:%E6%98%AF.html> "Template:Yes") |  [模板:是](<../zh-cn/Template:%E6%98%AF.html> "Template:是")  
[Template:No](<../zh-cn/Template:%E5%90%A6.html> "Template:No") |  [模板:否](<../zh-cn/Template:%E5%90%A6.html> "Template:否")  
[Template:Tip](<../zh-cn/Template:%E6%8F%90%E7%A4%BA.html> "Template:Tip") |  [模板:提示](<../zh-cn/Template:%E6%8F%90%E7%A4%BA.html> "Template:提示")  
[Template:Note](<../zh-cn/Template:%E6%B3%A8%E6%84%8F.html> "Template:Note") |  [模板:注意](<../zh-cn/Template:%E6%B3%A8%E6%84%8F.html> "Template:注意")  
[Template:Warning](<../zh-cn/Template:%E8%AD%A6%E5%91%8A.html> "Template:Warning") |  [模板:警告](<../zh-cn/Template:%E8%AD%A6%E5%91%8A.html> "Template:警告")  
[Template:Dead link](<../zh-cn/Template:Dead_link.html> "Template:Dead link") |  [模板:失效的链接](<../zh-cn/Template:%E5%A4%B1%E6%95%88%E7%9A%84%E9%93%BE%E6%8E%A5.html> "Template:失效的链接")  
[Template:Broken package link](<../zh-cn/Template:Broken_package_link.html> "Template:Broken package link") |  [模板:损坏的软件包链接](<../zh-cn/Template:%E6%8D%9F%E5%9D%8F%E7%9A%84%E8%BD%AF%E4%BB%B6%E5%8C%85%E9%93%BE%E6%8E%A5.html> "Template:损坏的软件包链接")  
[Template:Broken section link](<../zh-cn/Template:Broken_section_link.html> "Template:Broken section link") |  [模板:损坏的章节链接](<../zh-cn/Template:%E6%8D%9F%E5%9D%8F%E7%9A%84%E7%AB%A0%E8%8A%82%E9%93%BE%E6%8E%A5.html> "Template:损坏的章节链接")  
翻译状态模板   
[Template:Bad translation](<../zh-cn/Template:Bad_translation.html> "Template:Bad translation") |  [模板:糟糕的翻译](<../zh-cn/Template:%E7%B3%9F%E7%B3%95%E7%9A%84%E7%BF%BB%E8%AF%91.html> "Template:糟糕的翻译")  
[Template:Translateme](<../zh-cn/Template:%E9%9C%80%E8%A6%81%E7%BF%BB%E8%AF%91.html> "Template:Translateme") |  [Template:Translateme](<../zh-cn/Template:%E9%9C%80%E8%A6%81%E7%BF%BB%E8%AF%91.html> "Template:Translateme")  
[Template:TranslationStatus](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html> "Template:TranslationStatus") |  [Template:TranslationStatus](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html> "Template:TranslationStatus")  
导航模板   
[Template:Laptops table header](</wzh/index.php?title=Template:Laptops_table_header&action=edit&redlink=1> "Template:Laptops table header（页面不存在）") |  [模板:笔记本电脑表头](<../zh-cn/Template:%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91%E8%A1%A8%E5%A4%B4.html> "Template:笔记本电脑表头")  
[Template:Laptops navigation](</wzh/index.php?title=Template:Laptops_navigation&action=edit&redlink=1> "Template:Laptops navigation（页面不存在）") |  [模板:笔记本电脑导航](<../zh-cn/Template:%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91%E5%AF%BC%E8%88%AA.html> "Template:笔记本电脑导航")  
[Template:List of applications navigation](<../zh-cn/Template:List_of_applications_navigation.html> "Template:List of applications navigation") |  [模板:应用程序列表导航](<../zh-cn/Template:%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8%E5%AF%BC%E8%88%AA.html> "Template:应用程序列表导航")  
[Template:Package guidelines](<../zh-cn/Template:Package_guidelines.html> "Template:Package guidelines") |  [模板:打包准则](<../zh-cn/Template:%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Template:打包准则")  
特殊模板   
[Template:Cat main](<../zh-cn/Template:Cat_main.html> "Template:Cat main") |  [Template:Cat main](<../zh-cn/Template:Cat_main.html> "Template:Cat main")  
[Template:Template](<../zh-cn/Template:%E6%A8%A1%E6%9D%BF.html> "Template:Template") |  [Template:模板](<../zh-cn/Template:%E6%A8%A1%E6%9D%BF.html> "Template:模板")  
[Template:META Error](<../zh-cn/Template:META_Error.html> "Template:META Error") |  [Template:META Error](<../zh-cn/Template:META_Error.html> "Template:META Error")  
[Template:META Unexplained Status Template](<../zh-cn/Template:META_Unexplained_Status_Template.html> "Template:META Unexplained Status Template") |  [Template:META Unexplained Status Template](<../zh-cn/Template:META_Unexplained_Status_Template.html> "Template:META Unexplained Status Template")  
[Template:Comment](<../zh-cn/Template:Comment.html> "Template:Comment") |  [Template:Comment](<../zh-cn/Template:Comment.html> "Template:Comment")  
[Template:Committed identity](<../zh-cn/Template:Committed_identity.html> "Template:Committed identity") |  [Template:Committed identity](<../zh-cn/Template:Committed_identity.html> "Template:Committed identity")  
[Template:Unsigned](<../zh-cn/Template:Unsigned.html> "Template:Unsigned") |  [Template:Unsigned](<../zh-cn/Template:Unsigned.html> "Template:Unsigned")  
  
###  翻译状态模板

Arch 作为滚动发行版，软件变化比较快，对应的文档变化也比较快。许多翻译的文章由于缺乏更新，会产生命令运行出错或不起作用等问题。而由于这些过期页面没有及时标记出来，所以用户无法及时获得更新。[翻译状态模板](<../zh-cn/Template:TranslationStatus_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Template:TranslationStatus \(简体中文\)")就是为了解决这个问题而创建。 

此模板可以起到如下作用： 

  * 为用户提供翻译状况，包括翻译时间、英文页面的最后版本等
  * 用户可以点击查看翻译后，英文页面的改动，这样英文不是很好的用户可以只查看很小一部分英文内容，并判断出是否影响操作。
  * 翻译人员可以跟踪页面状况，通过[模板的反向链接](<../Special:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2/Template:TranslationStatus_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Special:链入页面/Template:TranslationStatus \(简体中文\)")可以查找到所有标记页面，查看需要更新翻译的部分。

[模板页面](<../zh-cn/Template:TranslationStatus_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Template:TranslationStatus \(简体中文\)")有详细的使用方法。 

###  翻译中应省略的模板

当页面或段落标记有 [Template:Accuracy](<../zh-cn/Template:%E5%87%86%E7%A1%AE%E6%80%A7.html> "Template:Accuracy")，[Template:Style](<../zh-cn/Template:%E9%A3%8E%E6%A0%BC.html> "Template:Style")，[Template:Archive](<../zh-cn/Template:%E5%BD%92%E6%A1%A3.html> "Template:Archive")，[Template:Remove](<../zh-cn/Template:%E7%A7%BB%E9%99%A4.html> "Template:Remove") 或 [Template:Out of date](<../zh-cn/Template:Out_of_date.html> "Template:Out of date") 时——在解决问题并且删除模板之前，不要翻译有问题的页面/段落。 

如果看到 [Template:Expansion](<../zh-cn/Template:%E6%89%A9%E5%85%85.html> "Template:Expansion")，[Template:Merge](<../zh-cn/Template:%E5%90%88%E5%B9%B6.html> "Template:Merge")，[Template:Move](<../zh-cn/Template:%E7%A7%BB%E5%8A%A8.html> "Template:Move") 或 [Template:Redirect](<../zh-cn/Template:%E9%87%8D%E5%AE%9A%E5%90%91.html> "Template:Redirect")，则可以安全地翻译页面，但不要将这些模板复制到翻译的文章中。 

如果看到 [Template:Broken package link](<../zh-cn/Template:Broken_package_link.html> "Template:Broken package link")，[Template:Broken section link](<../zh-cn/Template:Broken_section_link.html> "Template:Broken section link") 或 [Template:Dead link](<../zh-cn/Template:Dead_link.html> "Template:Dead link")，请不要将这些模板复制到翻译的文章中。要么在原始文本中将其修复，然后复制并在要翻译时翻译修复的链接，要么在翻译时忽略与它们有关的整个句子或部分。 
