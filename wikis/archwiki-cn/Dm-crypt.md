**翻译状态：**

  * 本文（或部分内容）译自 [Dm-crypt](<https://wiki.archlinux.org/title/Dm-crypt> "arch:Dm-crypt")，最近一次同步于 2025-07-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dm-crypt?diff=0&oldid=838291>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dm-crypt_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [静态数据加密](<../zh-cn/Data-at-rest_encryption.html> "Data-at-rest encryption")
  * [移除系统加密](</wzh/index.php?title=Removing_system_encryption&action=edit&redlink=1> "Removing system encryption（页面不存在）")

dm-crypt 是 Linux 内核的设备映射器（[device mapper](<https://en.wikipedia.org/wiki/device_mapper> "wikipedia:device mapper")）的加密模块（crypto target）。根据[Wikipedia:dm-crypt](<https://en.wikipedia.org/wiki/dm-crypt> "wikipedia:dm-crypt")词条的定义： 

    它是 Linux 内核中的透明磁盘加密子系统... 该模块通过设备映射器框架实现，可堆叠在其他设备映射器转换层之上。因此能够加密整个磁盘（包括可移动介质）、分区、软件 RAID 卷、逻辑卷以及文件。加密后的存储单元表现为块设备，可用于承载文件系统、作为交换空间或 LVM 物理卷。

##  用法

[/准备磁盘](<../zh-cn/Dm-crypt/%E5%87%86%E5%A4%87%E7%A3%81%E7%9B%98.html> "Dm-crypt/准备磁盘")
    处理诸如[安全擦除硬盘驱动器数据](<../zh-cn/Dm-crypt/%E5%87%86%E5%A4%87%E7%A3%81%E7%9B%98.html#%E5%AE%89%E5%85%A8%E6%93%A6%E9%99%A4%E7%A1%AC%E7%9B%98%E9%A9%B1%E5%8A%A8%E5%99%A8%E6%95%B0%E6%8D%AE> "Dm-crypt/准备磁盘")和[分区](<../zh-cn/Dm-crypt/%E5%87%86%E5%A4%87%E7%A3%81%E7%9B%98.html#%E5%88%86%E5%8C%BA> "Dm-crypt/准备磁盘")的 dm-crypt 特定点等操作。
[/设备加密](<../zh-cn/Dm-crypt/%E8%AE%BE%E5%A4%87%E5%8A%A0%E5%AF%86.html> "Dm-crypt/设备加密")
    介绍如何通过 [cryptsetup](<../zh-cn/Dm-crypt/%E8%AE%BE%E5%A4%87%E5%8A%A0%E5%AF%86.html#Cryptsetup_%E7%94%A8%E6%B3%95> "Dm-crypt/设备加密") 命令手动使用 dm-crypt 加密系统。 它涵盖了[使用 dm-crypt 的加密选项](<../zh-cn/Dm-crypt/%E8%AE%BE%E5%A4%87%E5%8A%A0%E5%AF%86.html#%E4%BD%BF%E7%94%A8_dm-crypt_%E7%9A%84%E5%8A%A0%E5%AF%86%E9%80%89%E9%A1%B9> "Dm-crypt/设备加密")的示例，处理[密钥文件](<../zh-cn/Dm-crypt/%E8%AE%BE%E5%A4%87%E5%8A%A0%E5%AF%86.html#%E5%AF%86%E9%92%A5%E6%96%87%E4%BB%B6> "Dm-crypt/设备加密")的创建，用于[密钥管理](<../zh-cn/Dm-crypt/%E8%AE%BE%E5%A4%87%E5%8A%A0%E5%AF%86.html#%E5%AF%86%E9%92%A5%E7%AE%A1%E7%90%86> "Dm-crypt/设备加密")以及[备份与恢复](<../zh-cn/Dm-crypt/%E8%AE%BE%E5%A4%87%E5%8A%A0%E5%AF%86.html#%E5%A4%87%E4%BB%BD%E4%B8%8E%E6%81%A2%E5%A4%8D> "Dm-crypt/设备加密")的 LUKS 特定命令。
[/系统配置](<../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html> "Dm-crypt/系统配置")
    说明在加密系统时如何配置[mkinitcpio](<../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#mkinitcpio> "Dm-crypt/系统配置")、[内核参数](<../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0> "Dm-crypt/系统配置")和[crypttab](<../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#crypttab> "Dm-crypt/系统配置")文件。
[/交换分区加密](<../zh-cn/Dm-crypt/%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA%E5%8A%A0%E5%AF%86.html> "Dm-crypt/交换分区加密")
    介绍如何在需要时向加密系统添加交换分区。交换分区也必须加密，以保护系统交换出的任何数据。本部分详细介绍了[无需休眠支持](<../zh-cn/Dm-crypt/%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA%E5%8A%A0%E5%AF%86.html#%E6%97%A0%E9%9C%80%E4%BC%91%E7%9C%A0%E6%94%AF%E6%8C%81> "Dm-crypt/交换分区加密")和[需要休眠支持](<../zh-cn/Dm-crypt/%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA%E5%8A%A0%E5%AF%86.html#%E9%9C%80%E8%A6%81%E4%BC%91%E7%9C%A0%E6%94%AF%E6%8C%81> "Dm-crypt/交换分区加密")的方法。
[/特殊应用](<../zh-cn/Dm-crypt/%E7%89%B9%E6%AE%8A%E5%BA%94%E7%94%A8.html> "Dm-crypt/特殊应用")
    处理一些特殊的操作，如[保护未加密的boot分区](<../zh-cn/Dm-crypt/%E7%89%B9%E6%AE%8A%E5%BA%94%E7%94%A8.html#%E4%BF%9D%E6%8A%A4%E6%9C%AA%E5%8A%A0%E5%AF%86%E7%9A%84boot%E5%88%86%E5%8C%BA> "Dm-crypt/特殊应用")，[使用GPG、LUKS、OpenSSL加密的密钥文件](<../zh-cn/Dm-crypt/%E7%89%B9%E6%AE%8A%E5%BA%94%E7%94%A8.html#%E4%BD%BF%E7%94%A8GPG%E3%80%81LUKS%E3%80%81OpenSSL%E5%8A%A0%E5%AF%86%E7%9A%84%E5%AF%86%E9%92%A5%E6%96%87%E4%BB%B6> "Dm-crypt/特殊应用")，[通过网络启动和解锁](<../zh-cn/Dm-crypt/%E7%89%B9%E6%AE%8A%E5%BA%94%E7%94%A8.html#%E8%BF%9C%E7%A8%8B%E8%A7%A3%E9%94%81%E5%88%86%E5%8C%BA> "Dm-crypt/特殊应用")，[为SSD设置discard/TRIM](<../zh-cn/Dm-crypt/%E7%89%B9%E6%AE%8A%E5%BA%94%E7%94%A8.html#%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98%E7%9A%84Discard/TRIM%E6%94%AF%E6%8C%81> "Dm-crypt/特殊应用")，[使用encrypt钩子解密多个设备](<../zh-cn/Dm-crypt/%E7%89%B9%E6%AE%8A%E5%BA%94%E7%94%A8.html#%E4%BD%BF%E7%94%A8encrypt%E9%92%A9%E5%AD%90%E8%A7%A3%E5%AF%86%E5%A4%9A%E4%B8%AA%E8%AE%BE%E5%A4%87> "Dm-crypt/特殊应用")。
[/登录时挂载](</wzh/index.php?title=Dm-crypt/%E7%99%BB%E5%BD%95%E6%97%B6%E6%8C%82%E8%BD%BD&action=edit&redlink=1> "Dm-crypt/登录时挂载（页面不存在）")（英语：[Dm-crypt/Mounting_at_login](<https://wiki.archlinux.org/title/Dm-crypt/Mounting_at_login> "en:Dm-crypt/Mounting at login")）

##  示例方案

[/加密非根文件系统](<../zh-cn/Dm-crypt/%E5%8A%A0%E5%AF%86%E9%9D%9Eroot%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "Dm-crypt/加密非root文件系统")
    如果你需要加密一个不用于启动系统的设备，比如一个[分区（英文）](<../zh-cn/Dm-crypt/Encrypting_a_non-root_file_system.html#Partition> "Dm-crypt/Encrypting a non-root file system")或一个[文件容器（英文）](<../zh-cn/Dm-crypt/Encrypting_a_non-root_file_system.html#File_container> "Dm-crypt/Encrypting a non-root file system")。
[/加密整个系统](<../zh-cn/Dm-crypt/%E5%8A%A0%E5%AF%86%E6%95%B4%E4%B8%AA%E7%B3%BB%E7%BB%9F.html> "Dm-crypt/加密整个系统")
    如果您想加密整个系统，特别是根分区。本文涵盖了使用带有**LUKS** 扩展的**dm-crypt** 、**plain** 模式加密以及加密和**LVM** 的情况。

##  另请参见

  * [dm-crypt](<https://gitlab.com/cryptsetup/cryptsetup/wikis/DMCrypt>) \- 项目主页
  * [cryptsetup](<https://gitlab.com/cryptsetup/cryptsetup>) \- LUKS主页、[FAQ](<https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions>)，这是最重要的参考资料。
