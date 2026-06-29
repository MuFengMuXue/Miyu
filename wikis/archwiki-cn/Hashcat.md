**翻译状态：**

  * 本文（或部分内容）译自 [Hashcat](<https://wiki.archlinux.org/title/Hashcat> "arch:Hashcat")，最近一次同步于 2020-04-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Hashcat?diff=0&oldid=608841>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Hashcat_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Hashcat](<https://en.wikipedia.org/wiki/Hashcat> "wikipedia:Hashcat") 是功能强大的密码恢复工具，支持 200 多种 hash 算法。它使用 OpenCL 来增强性能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [hashcat](<https://archlinux.org/packages/?name=hashcat>)包 包。 

如果没有 [OpenCL](<../zh-cn/GPGPU.html#OpenCL> "OpenCL")，Hashcat 将无法运行，因此您需要为 CPU 或 GPU 安装 [GPGPU#OpenCL](<../zh-cn/GPGPU.html#OpenCL> "GPGPU") 软件包。 

##  用法

对于来自 _hash_file_ 与 _hash_type_ 获得密码使用 _dictionary_file_ ： 
    
    hashcat -m _hash_type_ _hash_file_ _dictionary_file_
    
在 [Hashcat wiki](<https://hashcat.net/wiki/>) 上可以找到更多示例和用法详细信息。 

##  参见

  * [官方网站](<https://hashcat.net/hashcat/>)
