**翻译状态：**

  * 本文（或部分内容）译自 [7-Zip](<https://wiki.archlinux.org/title/7-Zip> "arch:7-Zip")，最近一次同步于 2024-12-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/7-Zip?diff=0&oldid=824084>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/7-Zip_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [归档与压缩](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html> "归档与压缩")

[7-Zip](<https://www.7-zip.org/>) 是一款高压缩比的文件压缩工具。它曾经由 _p7zip_ 包提供。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [7zip](<https://archlinux.org/packages/?name=7zip>)包 软件包。 

程序可通过以下命令运行： 
    
    $ 7z
    
替代方案：[bsdtar(1)](<https://man.archlinux.org/man/bsdtar.1>) 提供了 7z 归档支持，它包含在 [libarchive](<https://archlinux.org/packages/?name=libarchive>)包 包中。 

##  示例

**警告：** 7z 格式不会保存文件的所有者/组，因此不应用于备份目的。

添加文件或目录至已有的归档（或创建一个新的归档）： 
    
    $ 7z a _归档名_ _文件名_
    
也可以使用 `-p` 设置密码，并使用 `-mhe=on` 隐藏归档的目录结构： 

**警告：** 使用 `-p` 要求在命令行中输入密码。从 24.09 版本开始，在 `Enter password:` 后输入的内容不再隐藏，输入的内容可见，并且不会要求确认密码。
    
    $ 7z a _归档名_ _文件名_ -p -mhe=on
    
更新归档内已有的文件或添加新文件： 
    
    $ 7z u _归档名_ _文件名_
    
列出归档的内容： 
    
    $ 7z l _归档名_
    
从归档中解压所有文件到当前文件夹中，不保留存档内的目录结构： 
    
    $ 7z e _归档名_
    
如果需要保留归档内的目录结构，使用： 
    
    $ 7z x _归档名_
    
解压到新的目录中： 
    
    $ 7z x -o _文件夹路径_ _归档名_
    
校验归档完整性： 
    
    $ 7z t _归档名_
    
##  二进制文件 7z、7za 与 7zr 的区别

软件包中包含了三个二进制文件： 

  * `7z` 使用插件来处理归档文件。
  * `7za` 是一个独立的可执行文件，支持的归档格式比 7z 少。
  * `7zr` 是一个独立的可执行文件。它是 7za 的“轻量版”，仅支持 7z 格式的归档文件。与 7za 不同的是，它无法处理加密的归档文件。

##  参见

  * [zhwp:7-Zip](<https://zh.wikipedia.org/wiki/7-Zip> "zhwp:7-Zip")
  * [7-Zip 主页](<https://www.7-zip.org/>)（英文）
  * [官方手册](<https://7-zip.opensource.jp/chm/cmdline/index.htm>)（英文）
