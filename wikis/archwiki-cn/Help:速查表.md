**翻译状态：**

  * 本文（或部分内容）译自 [Help:Cheatsheet](<https://wiki.archlinux.org/title/Help:Cheatsheet> "arch:Help:Cheatsheet")，最近一次同步于 2016-03-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Help:Cheatsheet?diff=0&oldid=393588>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Help:Cheatsheet_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

查看完整的编辑命令列表，参见 [Help:编辑](<../zh-cn/Help:%E7%BC%96%E8%BE%91.html> "Help:编辑")。想尝试编辑，使用[沙盒](<../Project:%E6%B2%99%E7%9B%92.html> "Project:沙盒")。 

**在文字中任何地方可以使用 (wikitext)**  
---  
描述  | 输入  | 显示   
斜体文字  |  `''italic''` |  _italic_  
粗体文字  |  `'''bold'''` |  **bold**  
粗斜体文字  |  `'''''bold & italic'''''` |  _**bold & italic**_  
链接到另一个 ArchWiki 页面  |  `[[Name of page]]`  
`[[Name of page|要显示的文字]]`  
`[[Name of page#Section]]` |  [要显示的文字](</wzh/index.php?title=Name_of_page&action=edit&redlink=1> "Name of page（页面不存在）")  
[Name of page#Section](</wzh/index.php?title=Name_of_page&action=edit&redlink=1> "Name of page（页面不存在）")  
链接到同页面的段落  |  `[[#Section]]` |  [#Section](<#Section>)  
外部链接  |  `[https://www.google.com/ Google search engine]` |  [Google search engine](<https://www.google.com/>)  
添加页面到分类中 _分类应该放在页面的**开始** 。_ |  `[[Category:Category name]]` | 分类名称在页面预览或保存时会显示在页面下面的一个条形区域中。   
签名  _当在_ 讨论页 _中张贴时签名。_ _在内容页面编辑时不要签名。_ _参见[mw:Help:Signatures](<https://www.mediawiki.org/wiki/Help:Signatures> "mw:Help:Signatures")._ |  `~~~~` |  [Username](<../Special:%E6%88%91%E7%9A%84%E7%94%A8%E6%88%B7%E9%A1%B5.html> "Special:我的用户页"), 04:39, 1 2月 2026 (UTC)   
**在文字中任何地方可以使用 (HTML)**  
描述  | 输入  | 显示   
删除线  |  `<s>strikethrough</s>` |  ~~strikethrough~~  
下划线  |  `<u>underline</u>` |  _underline_  
下标和上标  |  `正常<sub>下标</sub> <sup>上标</sup>` |  正常下标 上标  
**只有在行首可以使用**  
描述  | 输入  | 显示   
代码  _使用一个或多个空格开始代码行。警告，不会自动换行！_ _另见[Help:Style (简体中文)#代码格式](<../zh-cn/Help:Style_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E4%BB%A3%E7%A0%81%E6%A0%BC%E5%BC%8F> "Help:Style \(简体中文\)")._ |  `$ echo Hello World` | 
    
    $ echo Hello World  
  
重定向到另一个页面 _重定向必须放在第一行的行首。_ |  `#redirect [[Target page]]` |  ↳ [Target page](</wzh/index.php?title=Target_page&action=edit&redlink=1> "Target page（页面不存在）")  
章节标题  _如果有4个或更多标题，目录会自动出现。_ _=Level 1= 不应该使用。_ _另见[Effective Use of Headers](</wzh/index.php?title=Effective_Use_of_Headers&action=edit&redlink=1> "Effective Use of Headers（页面不存在）")._ |  `== Level 2 ==`  
`=== Level 3 ===`  
`==== Level 4 ====`  
`===== Level 5 =====`  
`====== Level 6 ======`  
| 

## Level 2

### Level 3

#### Level 4

##### Level 5

###### Level 6  
  
水平线  |  `----` | 

* * *  
  
项目符号列表  |  `* One`  
`* Two`  
`** Two point one`  
`* Three` | 

  * One
  * Two 
    * Two point one
  * Three

编号列表  |  `# One`  
`# Two`  
`## Two point one`  
`# Three`  
| 

  1. One
  2. Two 
     1. Two point one
  3. Three

定义列表  |  `; Term one: Definition one`  
`; Term two: Definition two`  
| 

Term one
    Definition one
Term two
    Definition two  
缩进文本 _这通常用在讨论页中回复时使用，保证会话容易浏览。_ |  `no indent (normal)`  
`:first indent`  
`::second indent`  
`:::third indent` |  no indent (normal)  

    first indent 

    second indent 

    third indent  
**模板**  
描述  | 输入  | 显示   
行内代码 _Use[Template:ic](<../zh-cn/Template:Ic.html> "Template:Ic")._ |  `{{ic|code}}` |  `code`  
Character escape _See[Help:Template#Escape template-breaking characters](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#Escape_template-breaking_characters> "Help:Template")._ |  `{{ic|1=echo =}}` |  `echo =`  
Block code _Use[Template:bc](<../zh-cn/Template:Bc.html> "Template:Bc")._ | 
    
    {{bc|
    block
    code
    }}
    
| 
    
    block
    code
      
Block code with header _Use[Template:hc](<../zh-cn/Template:Hc.html> "Template:Hc")._ | 
    
    {{hc|header|
    block
    }}
    
| 
    
    header
    
    block
      
Note _Use[Template:Note](<../zh-cn/Template:%E6%B3%A8%E6%84%8F.html> "Template:Note")._ |  `{{Note|This text should be noted.}}` |  **注意：** This text should be noted.  
Warning _Use[Template:Warning](<../zh-cn/Template:%E8%AD%A6%E5%91%8A.html> "Template:Warning")._ |  `{{Warning|This text should be heeded.}}` |  **警告：** This text should be heeded.  
Man page _Use[Template:man](<../zh-cn/Template:Man.html> "Template:Man")._ |  `{{man|7|ascii}}` |  [ascii(7)](<https://man.archlinux.org/man/ascii.7>)  
软件包 _Use[Template:Pkg](<../zh-cn/Template:%E5%8C%85.html> "Template:Pkg")._ |  `{{Pkg|linux}}` |  [linux](<https://archlinux.org/packages/?name=linux>)包  
AUR 软件包 _Use[Template:AUR](<../zh-cn/Template:AUR.html> "Template:AUR")._ |  `{{AUR|linux-git}}` |  [linux-git](<https://aur.archlinux.org/packages/linux-git/>)AUR  
中文社区仓库软件包 _使用[Template:Cnrepo](<../zh-cn/Template:Cnrepo.html> "Template:Cnrepo")。_ |  `{{cnrepo|linux-lily}}` |  [linux-lily](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/linux-lily>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")
