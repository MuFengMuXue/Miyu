**翻译状态：**

  * 本文（或部分内容）译自 [Help:Template](<https://wiki.archlinux.org/title/Help:Template> "arch:Help:Template")，最近一次同步于 2023-01-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Help:Template?diff=0&oldid=761958>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Help:Template_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [帮助:编辑](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html> "Help:编辑")
  * [帮助:阅读](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html> "Help:阅读")
  * [帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")

模板是一段预先定义的 [wikitext](<https://en.wikipedia.org/wiki/Wikitext> "wikipedia:Wikitext")，可以直接插入到文章当中，主要用来加入格式化的内容。 

本文描述并说明 Arch Wiki 的模板规则，关于中文 Wiki 的额外要求，请访问 [Help:翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译"). 

##  使用

要使用一个模板，在文章中加入如下内容: 
    
    {{模板名称}}

大部分模板都可以附加额外参数，例如 [Template:注意](<../zh-cn/Template:%E6%B3%A8%E6%84%8F.html> "Template:注意"): 
    
    {{注意|这是一段应该注意的文字。}}

将显示为: 

**注意：** 这是一段应该注意的文字。

有些模板使用带名称的参数，例如[模板:hc](<../zh-cn/Template:Hc.html> "Template:Hc"): 
    
    {{hc|head=/etc/rc.local|output=exit 0}}

将显示为: 
    
    /etc/rc.local
    
    exit 0

一般格式为: 
    
    {{模板名称|参数1|参数m2|...|参数N}}

每个模板的页面都包含具体的使用方法。 

###  样式

  * 模板的大小写应该与模板页面的示例一致，例如应该使用 `{{Pkg|...` 和 `{{ic|...` 而不是 `{{pkg|...` 和 `{{Ic|...`。
  * 模板名的前后不应该有空格，: 应该用`{{模板名称|...` 而不是 `{{ 模板名称 |...`。
  * 不应对模板进行分类。

###  转义特殊字符

有些字符在模板中使用会扰乱输出，常见的如 "=" (等号) 和 "|" (管道字符). 可以用下面方法处理： 

**提示：**

  * 管道字符 "|" 可以通过 [magic word](<https://www.mediawiki.org/wiki/Help:Magic_words#Other> "mw:Help:Magic words") `{{!}}` 显示。
  * 等号 "=" 可以通过 magic word `{{=}}` 显示。

####  使用命名和位置编号参数

如果问题是 = 引起，可以通过命名或位置编号参数解决。 例如：`{{提示|1=https://archlinux.org/?foo=bar}}`

显示为：

**提示：**<https://archlinux.org/?foo=bar>

此方法非常适合这些情况使用： 

  * 变量定义
  * URL中带有查询参数的[站外链接](<../zh-cn/Help:Editing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%AB%99%E5%A4%96%E9%93%BE%E6%8E%A5> "Help:Editing \(简体中文\)")
  * 命令行字符串和命令
  * 多行代码

参数前后的多个空行会被自动移除，要保留空行，请使用 `<nowiki/>` 标签。 

例如: 
    
    {{Tip|1=<nowiki/>
    * https://archlinux.org/?foo=bar
    * https://archlinux.org/?foo=baz
    }}
    
将显示为: 

**提示：**

  * <https://archlinux.org/?foo=bar>
  * <https://archlinux.org/?foo=baz>

#####  多个参数

  * 使用位置编号参数`1`和`2`

    {{hc|1=$ echo "="|2==}}
    
效果：
    
    $ echo "="
    
    =

  * 使用命名参数`head`和`output`

    {{hc|head=$ echo "="|output==}}
    
效果：
    
    $ echo "="
    
    =

####  nowiki 标签

如果要支持 = 之外的字符，例如 "}", 请用 `<nowiki>` 包裹完整参数，但是这时他所有 Wiki 语法都会失效，例如链接和其他模板等都只会显示原始文本。示例： 
    
    {{提示|<nowiki>= | }} https://archlinux.org/ {{ic|foo}}</nowiki>}}
    
**提示：** = | }} https://archlinux.org/ {{ic|foo}}

当然，在 `<nowiki>` 标签中只包含特定部分(甚至单个字符)仍然有效，但为了可读性，建议只在链接或其他模板必须正常显示时才使用这种方法。例如: 
    
    {{提示|<nowiki>= | }}</nowiki> https://archlinux.org/ {{ic|foo}}}}
    
**提示：** = | }} <https://archlinux.org/> `foo`

####  将字符替换为 HTML 实体

此方法支持所有字符，但是不利于后续维护，所以仅当上面方法不适用时再使用。示例： 
    
    {{提示|&#61; &#124; &#123;&#123; &#125;&#125;}}
    
**提示：** = | {{ }}

##  创建

**注意：**

  * [模板命名空间是半保护的](<../Special:%E7%BE%A4%E7%BB%84%E6%9D%83%E9%99%90.html#Namespace_restrictions> "Special:群组权限")。只有[自动确认的用户](<https://wiki.archlinux.org/title/ArchWiki:Access_levels_and_roles#Access_levels>)才能创建或编辑模板。
  * 创建新模板前先在[帮助讨论:模板](</wzh/index.php?title=Help_talk:%E6%A8%A1%E6%9D%BF&action=edit&redlink=1> "Help talk:模板（页面不存在）") 进行讨论。
  * 请仅创建多次使用的模板。如果某个特殊的模板仅在有限的几个文章中使用，请不要创建它。
  * 请创建精简的模板，不要忘了 [Arch 之道](<../zh-cn/Arch_Linux.html> "Arch Linux"): 大道至简！

创建模板时，在本中文维基中，模板和模板的文档是分开创建的。模板页面的内容像这样： 
    
    <includeonly>此处是模板代码...</includeonly><noinclude>{{documentation}}
    <!-- 请将分类/语言链接放在文档页面 --></noinclude>
    
模板文档应该位于模板的`/doc`子页面。模板内通过 noinclude 标签调用`{{[Documentation](<../zh-cn/Template:Documentation.html> "Template:Documentation")}}`后，（预览或者保存后）按模板上的“创建”链接会自动加载所需的文档模板。详情参见[模板:模板](<../zh-cn/Template:%E6%A8%A1%E6%9D%BF.html> "Template:模板")。 

要开始创建过程，请先访问 `Template:Template name`(将`Template name`替换为要创建的模板名), 然后[帮助:编辑](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html> "Help:编辑")添加相关内容。 

**注意：**`<includeonly>` 和 `<noinclude>`标签之外的文本也会出现在模板调用的结果中。`<includeonly>` 的意思仅仅是不要在模板自己的页面中出现。因此，**不要在开始标签前、结束标签后换行** ，以避免额外的空行出现在使用模板的页面中。

##  模板列表

下列模板可直接于ArchWiki的页面中使用。点击链接可以查看详细使用方法。完整列表位于[Special:AllPages/Template:](<../Special:%E6%89%80%E6%9C%89%E9%A1%B5%E9%9D%A2/Template:.html> "Special:所有页面/Template:")、[Special:PrefixIndex/Template:](<../Special:%E5%89%8D%E7%BC%80%E7%B4%A2%E5%BC%95/Template:.html> "Special:前缀索引/Template:")或[Special:MostLinkedTemplates](<../Special:%E6%9C%80%E5%A4%9A%E9%93%BE%E6%8E%A5%E6%A8%A1%E6%9D%BF.html> "Special:最多链接模板")。 

**警告：** 请不要直接修改已经存在的模板。如果需要编辑未保护的模板，请将内容复制到[Template:Sandbox](<../zh-cn/Template:%E6%A8%A1%E6%9D%BF/Sandbox.html> "Template:Sandbox")进行编辑和测试，正常工作后再复制回去。强烈推荐（受保护模板必须）先在讨论页提出修改建议。

###  沙盒

  * [Template:Sandbox](<../zh-cn/Template:%E6%A8%A1%E6%9D%BF/Sandbox.html> "Template:Sandbox")
  * [Template:Lorem Ipsum](<../zh-cn/Template:Lorem_Ipsum.html> "Template:Lorem Ipsum")

###  文章状态模板

请将下列模板加入文章或段落的开头，详情参阅 [Help:风格#文章状态模板](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html#%E6%96%87%E7%AB%A0%E7%8A%B6%E6%80%81%E6%A8%A1%E6%9D%BF> "Help:风格"). 

译者还应检查 [ArchWiki:Translation Team](<../Project:Translation_Team.html> "Project:Translation Team") 中的模板指南。 

下列模板都通过 [Wiki 维护分类](<../zh-cn/Category:%E7%BB%B4%E6%8A%A4.html> "Category:Maintenance")统一管理，[ArchWiki:Statistics#Maintenance statistics](<https://wiki.archlinux.org/title/ArchWiki:Statistics#Maintenance_statistics>) 包含相关模板使用情况的统计。 

名称 | 适用情形 | 参数   
---|---|---  
[Template:Style](<../zh-cn/Template:%E9%A3%8E%E6%A0%BC.html> "Template:Style") | 内容存在语句、wiki 语法或样式问题.  |  `1`——原因, `2`——讨论页面(可选), `section`——讨论话题(可选)   
[Template:Accuracy](<../zh-cn/Template:%E5%87%86%E7%A1%AE%E6%80%A7.html> "Template:Accuracy") | 不正确、错误或容易引起误解的内容.   
[Template:Expansion](<../zh-cn/Template:%E6%89%A9%E5%85%85.html> "Template:Expansion") | 不全的内容.   
[Template:Out of date](<../zh-cn/Template:Out_of_date.html> "Template:Out of date") | 已经过时的内容.   
[Template:Remove](<../zh-cn/Template:%E7%A7%BB%E9%99%A4.html> "Template:Remove") | 不相关、无帮助内容.   
[Template:Archive](<../zh-cn/Template:%E5%BD%92%E6%A1%A3.html> "Template:Archive") | 已经过时的页面.   
[Template:Laptop style](<../zh-cn/Template:Laptop_style.html> "Template:Laptop style") |  [Laptop](<../zh-cn/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91.html> "Laptop") pages not following the [Help:Laptop page guidelines|Laptop page guidelines](<https://wiki.archlinux.org/title/Help:Laptop_page_guidelines>).   
[Template:Translateme](<../zh-cn/Template:%E9%9C%80%E8%A6%81%E7%BF%BB%E8%AF%91.html> "Template:Translateme") | 翻译不完全的内容.   
[Template:Bad translation](<../zh-cn/Template:Bad_translation.html> "Template:Bad translation") | 有问题的翻译   
[Template:TranslationStatus](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html> "Template:TranslationStatus") | 翻译状态  |  `1`——英文页面标题, `2`——翻译日期, `3`——英文页面版本号   
[Template:Merge](<../zh-cn/Template:%E5%90%88%E5%B9%B6.html> "Template:Merge") | 文章内容和其他页面重叠  |  `1`——目标页面, `2`——原因, `3`——讨论页面(可选), `section`——讨论话题(可选)   
[Template:Move](<../zh-cn/Template:%E7%A7%BB%E5%8A%A8.html> "Template:Move") | 文章应该改名.   
[Template:Redirect](<../zh-cn/Template:%E9%87%8D%E5%AE%9A%E5%90%91.html> "Template:Redirect") | 文章应该重定向到其它页面.   
[Template:Unsupported](<../zh-cn/Template:%E4%B8%8D%E5%8F%97%E6%94%AF%E6%8C%81.html> "Template:Unsupported") | 和 Arch Linux 无关的用户页面. |  `1`——最后审阅的日期   
  
用于非英语页面： 

  * [Template:Bad translation](<../zh-cn/Template:Bad_translation.html> "Template:Bad translation")
  * [Template:Translateme (简体中文)](<../zh-cn/Template:Translateme_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Template:Translateme \(简体中文\)") （[模板:需要翻译](<../zh-cn/Template:%E9%9C%80%E8%A6%81%E7%BF%BB%E8%AF%91.html> "Template:需要翻译")）
  * [Template:TranslationStatus (简体中文)](<../zh-cn/Template:TranslationStatus_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Template:TranslationStatus \(简体中文\)") （[Template:翻译状态](<../zh-cn/Template:%E7%BF%BB%E8%AF%91%E7%8A%B6%E6%80%81.html> "Template:翻译状态")）

###  相关文章模板

  * [Template:Related articles start](<../zh-cn/Template:Related_articles_start.html> "Template:Related articles start")
  * [Template:Related](<../zh-cn/Template:%E7%9B%B8%E5%85%B3.html> "Template:Related")
  * [Template:Related articles end](<../zh-cn/Template:Related_articles_end.html> "Template:Related articles end")

###  代码排版模板

  * [Template:ic](<../zh-cn/Template:Ic.html> "Template:Ic")
  * [Template:bc](<../zh-cn/Template:Bc.html> "Template:Bc")
  * [Template:hc](<../zh-cn/Template:Hc.html> "Template:Hc")
  * [Template:Text art](<../zh-cn/Template:Text_art.html> "Template:Text art")

###  提示模板

  * [Template:Note (简体中文)](<../zh-cn/Template:Note_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Template:Note \(简体中文\)") （[Template:注意](<../zh-cn/Template:%E6%B3%A8%E6%84%8F.html> "Template:注意")）
  * [Template:Tip (简体中文)](<../zh-cn/Template:Tip_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Template:Tip \(简体中文\)") （[Template:提示](<../zh-cn/Template:%E6%8F%90%E7%A4%BA.html> "Template:提示")）
  * [Template:Warning (简体中文)](<../zh-cn/Template:Warning_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Template:Warning \(简体中文\)") （[Template:警告](<../zh-cn/Template:%E8%AD%A6%E5%91%8A.html> "Template:警告")）

仅用于讨论页的草稿： 

  * [Template:Comment](<../zh-cn/Template:Comment.html> "Template:Comment")

###  杂项

  * [Template:App](<../zh-cn/Template:%E5%BA%94%E7%94%A8.html> "Template:App")
  * [Template:Broken package link](<../zh-cn/Template:Broken_package_link.html> "Template:Broken package link")
  * [Template:Broken section link](<../zh-cn/Template:Broken_section_link.html> "Template:Broken section link")
  * [Template:Bug](<../zh-cn/Template:Bug.html> "Template:Bug")
  * [Template:Committed identity](<../zh-cn/Template:Committed_identity.html> "Template:Committed identity")
  * [Template:Dead link](<../zh-cn/Template:Dead_link.html> "Template:Dead link")
  * [Template:Lowercase title](<../zh-cn/Template:Lowercase_title.html> "Template:Lowercase title")
  * [Template:man](<../zh-cn/Template:Man.html> "Template:Man")
  * [Template:Unsigned](<../zh-cn/Template:Unsigned.html> "Template:Unsigned")

###  软件包模板

  * [Template:Pkg](<../zh-cn/Template:%E5%8C%85.html> "Template:Pkg")
  * [Template:Grp](<../zh-cn/Template:%E5%8C%85%E7%BB%84.html> "Template:Grp")
  * [Template:AUR](<../zh-cn/Template:AUR.html> "Template:AUR")
  * [Template:Cnrepo](<../zh-cn/Template:Cnrepo.html> "Template:Cnrepo")

###  表格模板

文字对齐： 

模板名 | 对齐 | Wiki标记 | 效果   
---|---|---|---  
[Template:C](<../zh-cn/Template:C.html> "Template:C") | 居中 | `{{C|text}}` | text   
[Template:L](<../zh-cn/Template:L.html> "Template:L") | 靠左 | `{{L|text}}` | text   
  
单元格背景： 

模板名 | 颜色 | Wiki标记 | 效果   
---|---|---|---  
[Template:R](<../zh-cn/Template:%E7%BA%A2.html> "Template:R") | red | `{{R|text}}` | text   
[Template:O](<../zh-cn/Template:O.html> "Template:O") | orange | `{{O|text}}` | text   
[Template:Y](<../zh-cn/Template:Y.html> "Template:Y") | yellow | `{{Y|text}}` | text   
[Template:G](<../zh-cn/Template:%E7%BB%BF.html> "Template:G") | green | `{{G|text}}` | text   
[Template:B](<../zh-cn/Template:%E8%93%9D.html> "Template:B") | blue | `{{B|text}}` | text   
[Template:V](<../zh-cn/Template:V.html> "Template:V") | violet | `{{V|text}}` | text   
[Template:Grey](<../zh-cn/Template:%E7%81%B0.html> "Template:Grey") | grey | `{{Grey|text}}` | text   
  
常见文字： 

模板名 | Wiki标记 | 效果   
---|---|---  
[Template:是](<../zh-cn/Template:%E6%98%AF.html> "Template:是") | `{{是}}` | 是   
`{{是|https://wiki.archlinux.org/}}` |  [是](<https://wiki.archlinux.org/>)  
[Template:否](<../zh-cn/Template:%E5%90%A6.html> "Template:否") | `{{否}}` | 否   
`{{否|https://wiki.archlinux.org/}}` |  [否](<https://wiki.archlinux.org/>)  
[Template:-](<../zh-cn/Template:-.html> "Template:-") | `{{-}}` | –   
  
**提示：** 将单元格属性前置即可让属性和表格模板并用，例如：`| colspan=2 {{是}}`。

###  分类模板

  * [Template:Cat main](<../zh-cn/Template:Cat_main.html> "Template:Cat main")

##  参见

  * [Template:Template](<../zh-cn/Template:%E6%A8%A1%E6%9D%BF.html> "Template:Template")
  * [MetaWikimedia:Help:Template/zh](<https://meta.wikimedia.org/wiki/Help:Template/zh> "metawikimedia:Help:Template/zh")
