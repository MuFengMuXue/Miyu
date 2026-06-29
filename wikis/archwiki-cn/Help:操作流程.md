本文是对文章执行复杂修改或其他维护操作时使用的一系列检查列表。 

##  在同一页面中移动段

此举应在单个编辑中进行，该编辑不会更改其他任何内容： 

  1. 在编辑器中打开文章。
  2. 剪切要被移动的段。**不要** 立即保存页面，即不要于两份编辑中执行移动操作——第一份剪切第二份再粘贴，否则在第二份编辑中会显示您似乎是该段的作者，特别是编辑摘要同时不明确时。
  3. 在新位置粘贴该段。
  4. 如果需要，调整标题等级，但**不要** 对内容进行其他更改，否则此次编辑所做增改不明确。
  5. 保存页面并规范书写编辑摘要。
  6. 现在您可以按照需求对内容进行正常的修改。

##  分割段到新的子页面

此过程在将文章中已经变得太长的段移动到该文章的子页面时很有用。 

  1. 在编辑器中打开原始文章指定段。
  2. 复制整个段内容。
  3. 在另一个编辑器中打开目标子页面。
  4. 将复制的内容粘贴到目标编辑器中， _不要_ 修改。
  5. 要保存目标子页面并书写编辑摘，例如 `content split from [[Origin article#Section]]`;确保包含指向原始页面的链接，否则看起来您是内容的作者。
  6. 在原始编辑器中，将拆分的内容替换为指向目标子页面的链接，或者保留段标题，或者在相关文章框添加链接。
  7. 保存带有编辑摘要的原始页面，例如 `content moved to [[Destination subpage]]`。
  8. 在编辑器中重新打开目标子页面。
  9. 像原始文章一样对目标子页面进行分类。
  10. 在顶部添加指向原始文章的链接，例如 `See [[Origin article]] for the main article`。
  11. 调整新子页面标题的层级，从第二层开始。

**提示：** 这一步可以通过 [Wiki Monkey](</wzh/index.php?title=Wiki_Monkey&action=edit&redlink=1> "Wiki Monkey（页面不存在）") 的插件自动完成。

  12. 书写适当的编辑摘要然后保存目标子页面。

更高级的附加步骤： 

  * 检查并修复指向原始页面和目标页面中的段以及链接到原始页面中的任何损坏链接。

**提示：** 这一步可以通过[Wiki Monkey](</wzh/index.php?title=Wiki_Monkey&action=edit&redlink=1> "Wiki Monkey（页面不存在）")插件自动完成。

##  在将页面重定向到另一个页面后处理讨论页面

如果页面 _A_ 已经[重定向](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html#%E9%87%8D%E5%AE%9A%E5%90%91> "Help:编辑")到页面 _B_ ，例如在将 _A_ 的内容合并到页面 _B_ 之后，并且其讨论页' 'Talk:A _存在：_

  * 如果 _Talk:B_ 不存在，**移动** 整个 _Talk:A_ 到 _Talk:B_ ，让 MediaWiki 自动将 _Talk:A_ 重定向到 _ЕTalk:B_ 。
  * 如果 _Talk:B_ 存在： 
    1. 若存在，则将依然相关的讨论从 _Talk:A_ [移动](<#%E5%B0%86%E8%AE%A8%E8%AE%BA%E7%A7%BB%E8%87%B3%E5%8F%A6%E4%B8%80%E4%B8%AA%E8%AE%A8%E8%AE%BA%E9%A1%B5>)到 _Talk:B_
    2. 确保 _Talk:A_ 中留下的讨论（如果有） [已关闭](<../zh-cn/Help:%E8%AE%A8%E8%AE%BA.html#%E5%85%B3%E9%97%AD%E4%B8%80%E4%B8%AA%E8%AE%A8%E8%AE%BA> "Help:讨论")。 
       * 如果 _Talk:A_ 主持的讨论的关闭时间少于[帮助:讨论#关闭一个讨论](<../zh-cn/Help:%E8%AE%A8%E8%AE%BA.html#%E5%85%B3%E9%97%AD%E4%B8%80%E4%B8%AA%E8%AE%A8%E8%AE%BA> "Help:讨论")中指定的时间，则使用[模板：重定向](</wzh/index.php?title=%E6%A8%A1%E6%9D%BF%EF%BC%9A%E9%87%8D%E5%AE%9A%E5%90%91&action=edit&redlink=1> "模板：重定向（页面不存在）")标记 _Talk:A_ ，以便页面将在关闭时段后重定向到“Talk:B”。
       * 否则，立即将 _Talk:A_ 重定向到 _Talk:B_ 。

##  修复双重重定向

  1. 阅读[此节](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html#%E9%87%8D%E5%AE%9A%E5%90%91> "Help:编辑")了解什么是重定向。
  2. 查看 [Special:双重重定向](<../Special:%E5%8F%8C%E9%87%8D%E9%87%8D%E5%AE%9A%E5%90%91.html> "Special:双重重定向")看看是否存在已知页面。
  3. 例如，如果您看到 `Pastebin Clients (Edit) → Common Applications → List of applications`，则表示 [Pastebin Clients](</wzh/index.php?title=Pastebin_Clients&action=edit&redlink=1> "Pastebin Clients（页面不存在）") 重定向到 [Common Applications](<../zh-cn/Common_Applications.html> "Common Applications")，并且 [Common Applications](<../zh-cn/Common_Applications.html> "Common Applications") 重定向到 [List of applications](<../zh-cn/List_of_applications.html> "List of applications")。因此，[Pastebin Clients](</wzh/index.php?title=Pastebin_Clients&action=edit&redlink=1> "Pastebin Clients（页面不存在）") 是双重重定向。
  4. 要修复它，编辑 [Pastebin Clients](</wzh/index.php?title=Pastebin_Clients&action=edit&redlink=1> "Pastebin Clients（页面不存在）") 并将 `#REDIRECT [[Common Applications]]` 更改为 `#REDIRECT [[List of applications]]` 跳过中间跳转。
  5. 输入编辑摘要，例如 `Fixed double redirect` 并保存。

**提示：** 这个任务 [User:lilydjwg](<../User:Lilydjwg.html> "User:Lilydjwg") 会不定期通过脚本自动完成。如果长时间有双重重定向没有被修复，可以去 [User talk:lilydjwg](<../User_talk:Lilydjwg.html> "User talk:Lilydjwg") 留言。

##  修复损坏的包链接

本维基包含许多在[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")或 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中找不到的包的损坏链接，这是包被合并、拆分或从存储库中删除的结果。 

要修复损坏的包链接，请**不要** 仅从 wiki 中删除对包的引用，先做一些研究： 

  * 搜索包数据库 (`pacman -Ss`) 和 [AUR](<https://aur.archlinux.org/packages/>)，包可能被合并/重命名。
  * 如果要查找特定文件，例如作为软件包一部分的二进制文件，[pkgfile](<../zh-cn/Pkgfile.html> "Pkgfile") 可能会解决问题。
  * 如果不确定，请使用适当的 [status template](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#Article_status_templates> "Help:Template") 标记页面或段，而不是完全删除对包的引用。

为了帮助手动更新，每个“损坏的包链接”模板都提供了一个提示： 

  * “无效的模板参数数量” –所有 [AUR](<../zh-cn/Template:AUR.html> "Template:AUR")、[Grp](<../zh-cn/Template:%E5%8C%85%E7%BB%84.html> "Template:Grp") 和 [Pkg](<../zh-cn/Template:%E5%8C%85.html> "Template:Pkg") 模板都只采用一个参数，但 wikitext 指定了更多（或没有）。在大多数情况下，过多的参数应该移动到周围的文本中，或者如果已经存在则删除。
  * "替换为 _[其他包]_ " –包被重命名或合并到另一个包中，这在 [ 替换](<../zh-cn/PKGBUILD.html#replaces> "PKGBUILD") 中指定了旧包名称数组。在大多数情况下，应该简单地用新包替换旧包，并相应更新周围的文本。
  * “找不到包” –以上均不适用时的默认提示。

在 [分类:包含损坏的软件包链接的页面](</wzh/index.php?title=Category:%E5%8C%85%E5%90%AB%E6%8D%9F%E5%9D%8F%E7%9A%84%E8%BD%AF%E4%BB%B6%E5%8C%85%E9%93%BE%E6%8E%A5%E7%9A%84%E9%A1%B5%E9%9D%A2&action=edit&redlink=1> "Category:包含损坏的软件包链接的页面（页面不存在）")中跟踪所有包含损坏包链接的页面。 

##  修复损坏的段链接

页面有时可能包含损坏的段链接，这是段被重命名、合并、移动或从页面中删除的结果。 

要修复损坏的段链接，请**不要** 简单地从 wiki 中删除对段链接的引用，先做一些研究： 

  * 查看该段所在页面的历史记录，该段可能被重命名/合并/移动/删除。
  * 如果不确定，请使用适当的 [status template](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#Article_status_templates> "Help:Template") 标记该段，而不是完全删除对该段的引用。

在 [Category:Pages with broken section links](</wzh/index.php?title=Category:Pages_with_broken_section_links&action=edit&redlink=1> "Category:Pages with broken section links（页面不存在）") 中跟踪所有带有损坏段链接的页面。 

##  创建一个新页面及其翻译

请参阅[帮助:翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")。 

##  将讨论移至另一个讨论页

  1. 将讨论文本复制到目标讨论页面，确保在新标题和粘贴的文本之间添加如下注释：  
`''[Moved from [[Origin talk page#Heading]]。 -- ~~~~]''`
  2. 在原始讨论页中删除标题并将内容替换为如下注释：  
`''[Moved to [[Destination talk page#Heading]]。 -- ~~~~]''`

##  重命名一个类别

  1. 以与移动普通页面相同的方式移动类别页面，确保创建从旧标题到新标题的重定向。这只会重命名类别页面本身，不会重新分类类别的成员。
  2. 重新分类旧类别所有成员，令其使用新类别。 

**提示：** 这可以通过 [wiki-scripts](<../Project:%E6%9C%BA%E5%99%A8%E4%BA%BA.html#wiki-scripts> "Project:机器人") 的 [recategorize-over-redirect.py](<https://github.com/lahwaacz/wiki-scripts/blob/master/recategorize-over-redirect.py>)自动完成，它依赖于来自旧类别的重定向来检测新名称，因此它不限于大小写或类似启发式的变化。

  3. 更新所有跨语言链接。 

**提示：** 这可以使用 [wiki-scripts](<../Project:%E6%9C%BA%E5%99%A8%E4%BA%BA.html#wiki-scripts> "Project:机器人") 的 [interlanguage.py](<https://github.com/lahwaacz/wiki-scripts/blob/master/interlanguage.py>) 或 [自动完成的机器人插件](<../Project:%E6%9C%BA%E5%99%A8%E4%BA%BA.html#Wiki_Monkey> "Project:机器人")。

  4. 更新旧类别的所有反向链接以引用新类别。 

**提示：** 这可以通过在旧类别的 [Special:链入页面](<../Special:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2.html> "Special:链入页面")页面上运行 Wiki Monkey 的“正则表达式替换”插件自动完成，替换为 `(\[\[| \{\{Related2?\|):[_]*[Cc]ategory[_]*:[_]*[Oo]ld[_]name[_]*(#|\||\]\]| \}\})` -> `$1:Category:New name$2`（假设旧的类别名称是“Category:Old name”）。

  5. 用 [Template:弃用](<../zh-cn/Template:%E5%BC%83%E7%94%A8.html> "Template:弃用")标记旧类别，而不破坏重定向（旧类别可能仍然从[目录](<../zh-cn/%E7%9B%AE%E5%BD%95.html> "目录")链接）。 

**提示：** 如果该类别没有相关历史记录，管理员可以在确保步骤 2-4 已经实际执行之后将其删除。

##  删除整个页面

  * 新但不合适的页面： 
    * 如果由于垃圾邮件或其他明显恶意内容（由管理员进行评估）而导致不当，则立即 [删除](<https://www.mediawiki.org/wiki/Help:Sysop_deleting_and_undeleting> "mw:Help:Sysop deleting and undeleting")；
    * 在其他情况下，例如与 Arch 无关，文章应当： 
      * 标记[模板:合并](<../zh-cn/Template:%E5%90%88%E5%B9%B6.html> "Template:合并")；或者
      * 标记[模板:重定向](<../zh-cn/Template:%E9%87%8D%E5%AE%9A%E5%90%91.html> "Template:重定向")；或者
      * 使用[模板:移动](<../zh-cn/Template:%E7%A7%BB%E5%8A%A8.html> "Template:移动")标记为作为其作者用户页面的子页面移动（或立即移动）。
  * 旧文章过时： 
    1. 用以下选项之一标记，按优先顺序排列： 
       * [模板:合并](<../zh-cn/Template:%E5%90%88%E5%B9%B6.html> "Template:合并")；
       * [模板:重定向](<../zh-cn/Template:%E9%87%8D%E5%AE%9A%E5%90%91.html> "Template:重定向")；
       * [模板:弃用](<../zh-cn/Template:%E5%BC%83%E7%94%A8.html> "Template:弃用")；
    2. 至少等待 7 天；
    3. 在没有反对讨论的情况下，或者当这些讨论最终解决有利于删除时，执行建议的行动； 
       * 重定向时，请考虑遵循[#在将页面重定向到另一个页面后处理讨论页面](<#%E5%9C%A8%E5%B0%86%E9%A1%B5%E9%9D%A2%E9%87%8D%E5%AE%9A%E5%90%91%E5%88%B0%E5%8F%A6%E4%B8%80%E4%B8%AA%E9%A1%B5%E9%9D%A2%E5%90%8E%E5%A4%84%E7%90%86%E8%AE%A8%E8%AE%BA%E9%A1%B5%E9%9D%A2>)和[#修复双重重定向](<#%E4%BF%AE%E5%A4%8D%E5%8F%8C%E9%87%8D%E9%87%8D%E5%AE%9A%E5%90%91>)；

**注意：** 本维基不使用 ArchWiki 的[归档](<../Project:%E5%BD%92%E6%A1%A3.html> "Project:归档")操作，取而代之的是[弃用](<../zh-cn/Template:%E5%BC%83%E7%94%A8.html> "Template:弃用")。

##  巡查

每个人都可以检查[最近更改](<../Special:%E6%9C%80%E8%BF%91%E6%9B%B4%E6%94%B9.html> "Special:最近更改")。[维护团队](<../Project:%E7%BB%B4%E6%8A%A4%E5%9B%A2%E9%98%9F.html> "Project:维护团队")成员也可以将编辑和页面标记为 [已巡查](<../Special:%E6%97%A5%E5%BF%97/patrol.html> "Special:日志/patrol")。这段主要是关于每个人都可以做的事情。 

请记住，巡视最近的变化显然需要更持久的承诺，而修复其他事情则更灵活，只要您有时间就可以完成。 

###  最近更改巡查

您可以通过两种主要方式查看最近更改： 

  * 定期访问 [Special:最近更改](<../Special:%E6%9C%80%E8%BF%91%E6%9B%B4%E6%94%B9.html> "Special:最近更改")，检查最近提交的所有编辑。
  * 订阅 [Special:最近更改 Atom 提要](<https://wiki.archlinuxcn.org/wzh/api.php?hidebots=1&urlversion=1&days=7&limit=50&action=feedrecentchanges&feedformat=atom>) 并在找到时间后立即检查编辑。

对于同一页面的每次编辑或一组编辑，您应该根据您的经验和知识评估它是否有问题，同时考虑[最常见问题](<#%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4>)。 

  * 如果您认为编辑需要一个可以立即执行的快速修复，那就去做吧。这尤其适用于较小的样式问题、拼写错误和语法修复。
  * 如果编辑有问题但您无法修复，您应该查看它是否已被适当的[模板](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#%E6%96%87%E7%AB%A0%E7%8A%B6%E6%80%81%E6%A8%A1%E6%9D%BF> "Help:模板")标记： 
    * 如果没有，请将适当的模板添加到描述问题的适当段。
    * 如果已经有编辑讨论，请查看是否可以在随附的注释或讨论中添加有用的详细信息。

**提示：** 采取以下步骤使巡逻更容易： 

  * 在“首选项 > 最近更改 > 高级选项”下启用“在最近更改和监视列表中按页面分组更改”设置。
  * 要使用提要阅读器关注您观看的文章，请使用[监视列表](<../Special:%E7%9B%91%E8%A7%86%E5%88%97%E8%A1%A8.html> "Special:监视列表")页面左栏中的 Atom 链接。

####  机器人编辑

默认情况下，MediaWiki 在最近的更改中不显示[机器人](</wzh/index.php?title=Project:Bots&action=edit&redlink=1> "Project:Bots（页面不存在）")编辑。可能需要检查其中一个机器人何时修改了页面，因为它可能表明需要进行更改。 

###  故障排除

**注意：** 您可以“始终”向[维护团队](<../Project:%E7%BB%B4%E6%8A%A4%E5%9B%A2%E9%98%9F.html> "Project:维护团队")寻求帮助。

####  滥用

幸运的是，垃圾邮件和其他违反[行为准则](<../zh-cn/%E8%A1%8C%E4%B8%BA%E5%87%86%E5%88%99.html> "行为准则")的事情并不常见，但仍会偶尔发生。 

[最重要的任务](<../Project:%E8%B4%A1%E7%8C%AE.html#%E6%9C%80%E9%87%8D%E8%A6%81%E7%9A%84%E4%BB%BB%E5%8A%A1> "Project:贡献")也在这里申请。确保立即打击滥用行为： 

  1. 首先，**撤消** 所有的破坏。
  2. 联系[维护团队](<../Project:%E7%BB%B4%E6%8A%A4%E5%9B%A2%E9%98%9F.html> "Project:维护团队")。您也可以加入 [本维基的编辑事务交流群](<../Project:Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BA%A4%E6%B5%81%E7%BE%A4%E6%8C%87%E5%BC%95.html#archlinux-cn-wiki> "Project:Arch Linux 中文社区交流群指引")并提及管理员，他们通常都是频道操作员。

如果有一波滥用行为并且消除破坏需要太长时间，请先报告。 

####  内容相关

  * 删除有用内容：撤消或联系作者。
  * 不明原因修改或删除内容：联系作者，无反应撤消。
  * 没有充分解释的重大修改（通常在单个大容量编辑中）：联系作者。

####  风格相关

  * 文章中的签名，赞赏，个人意见：撤消或移至讨论页面。
  * 从第 1 级开始标记标题：将所有段上移 1 级。
  * 未分类的新文章：添加类别并修复标题。
  * 模板使用不当：根据[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")修复。
  * 增加安装说明：撤销或遵守[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")。

###  MediaWiki 巡查功能

**注意：** 此功能只能由[维护团队](<../Project:%E7%BB%B4%E6%8A%A4%E5%9B%A2%E9%98%9F.html> "Project:维护团队")成员使用。

将更改标记为已巡查是一种非常有用的方法，可以避免在不必要时执行两次操作。我们鼓励维护团队的每个成员都使用此功能来节省其他人的时间。 

有时，特别是当某人对某个主题没有经验时，不清楚是否应该将编辑标记为已巡查。不将编辑标记为已巡查意味着维护团队的其他成员更有可能查看更改。以下是一些可能有助于巡查更多更改的提示： 

  * 拼写错误、语法或语言修复通常很容易验证。如果可能，请先修复它们。
  * 如果有意义，可以将讨论页的添加标记为已巡查（适合主题，例如在有关 archiso 的页面上讨论游戏是不合适的）。
  * 用户页面可以包含任何内容，只要它不违反任何规则。不幸的是，它们基本上不受大多数​​风格指南的约束。
  * 如果提交了大量翻译，则可能较难检查翻译。可以使用 [DeepL](<https://www.deepl.com/en/translator>) 等机器翻译工具来辅助检查翻译是否大致正确。检查非常新用户的翻译有助于发现低质量的编辑和破坏行为。
  * 错误发生。如果用户注意到他们的错误并撤消自己的编辑，则可以将两者都标记为已巡查。
  * 将由维护团队成员恢复的编辑标记为已巡查，因为恢复编辑的人可能只是忘记了它。
  * 新页面可能不完整和/或有样式问题。如果它适合 Arch Linux 中文维基，则将其标记为已巡逻。考虑监视此页面，并确保在它被遗弃时照顾它。

所有这些点都意味着更改不得违反 [Project:贡献](<../Project:%E8%B4%A1%E7%8C%AE.html> "Project:贡献")中描述的行为准则或规则。 

###  其他

还有其他一些事情需要注意： 

  * 检查新创建的帐户列表，查看其中是否有任何已编辑。应始终检查由非常新的编辑者所做的编辑，因为编辑者可能还不熟悉所有指南。
  * 确保任何添加到讨论页的内容都是[署名的](<../zh-cn/Template:Unsigned.html> "Template:Unsigned")。 
    * 有时，用户不知道讨论页上的“添加主题”按钮。确保将新的讨论放在底部并具有适当的段名称。
    * 如果编辑摘要看起来像 _[→某章节: 新章节](<#Other>)_ ，则用户在讨论页使用了“添加话题”按钮。
    * 如果用户一直手动添加新段，请随时提醒他们有更方便的“添加话题”按钮。
  * 应始终调查差异很大的空白和编辑。
  * 新页面也值得一看，改进它们并修复样式问题是一个很好的榜样，可以帮助作者。
  * 确保修改表格的编辑不会通过插入杂散行/列来破坏它们。
  * 没有适当的编辑摘要的编辑需要特别注意。如果用户没有正确使用编辑摘要，还有 [Template:Editsum](</wzh/index.php?title=Template:Editsum&action=edit&redlink=1> "Template:Editsum（页面不存在）")。
  * 撤消是常见现象，但仍应检查。

##  请求解决

参见 [ArchWiki talk:Requests](</wzh/index.php?title=ArchWiki_talk:Requests&action=edit&redlink=1> "ArchWiki talk:Requests（页面不存在）")。 

  * 如果您认为可以修复请求，只需执行并删除适当的模板。另请参阅 [#故障排除](<#%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4>)。
  * 如果您觉得最好联系有问题的编辑的作者，在他的讨论页中给他们写一条消息，或者给他们发送电子邮件，以请求解释或进一步讨论。

**提示：**

  * 更喜欢尝试修复最旧的请求。
  * 更喜欢修复与内容相关的问题，而不是与样式相关的问题。
  * 您可以考虑使用编辑器助手（例如 [Wiki Monkey](</wzh/index.php?title=Wiki_Monkey&action=edit&redlink=1> "Wiki Monkey（页面不存在）") 的 _Editor_ 配置）以自动解决一些常见的样式问题。
