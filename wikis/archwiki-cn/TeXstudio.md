**翻译状态：**

  * 本文（或部分内容）译自 [TeXstudio](<https://wiki.archlinux.org/title/TeXstudio> "arch:TeXstudio")，最近一次同步于 2024-08-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/TeXstudio?diff=0&oldid=815310>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/TeXstudio_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

是一款免费的 [LaTeX](<../zh-cn/TeX_Live.html> "LaTeX") [编辑器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#TeX_%E7%BC%96%E8%BE%91%E5%99%A8> "应用程序列表/文档")。它提供多种功能，可轻松输入特殊字符、编辑表格、预览数学模式片段和语言检查。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [texstudio](<https://archlinux.org/packages/?name=texstudio>)包 软件包。 

###  语言检查

如果想启用语言检查功能，请安装 [hunspell](<https://archlinux.org/packages/?name=hunspell>)包 和至少[一个对应的词典](<https://archlinux.org/packages/?q=hunspell->)。TeXstudio 中的语言选择将与所安装的 hunspell 词典相匹配。如果没有安装词典，则无法在应用程序中选择语言。 

您也可以安装 [languagetool](<https://archlinux.org/packages/?name=languagetool>)包 来进行更高级的语言检查，或者连接到远程 [LanguageTool](<https://languagetool.org>) 服务器。无论如何，您都需要为所需语言安装 hunspell 词典，否则即使语言工具包或服务器支持该词典，TeXstudio 也不会让您选择该词典。 
