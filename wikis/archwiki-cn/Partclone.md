**翻译状态：**

  * 本文（或部分内容）译自 [Partclone](<https://wiki.archlinux.org/title/Partclone> "arch:Partclone")，最近一次同步于 2020-08-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Partclone?diff=0&oldid=738573>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Partclone_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Partclone](<https://partclone.org>) 与众所周知的 [Partimage](<https://www.partimage.org/Main_Page>) 一样可用于备份和还原分区，同时仅考虑已使用的块。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [partclone](<https://archlinux.org/packages/?name=partclone>)包 包。 

##  对一个 ext4 格式的分区使用 Partclone

###  不使用压缩

要备份而**不使用** 压缩： 
    
    # partclone.ext4 -c -s /dev/sda1 -o ~/image_sda1.pcl
    
还原它： 
    
    # partclone.ext4 -r -s ~/image_sda1.pcl -o /dev/sda1
    
###  使用压缩

要**进行** 压缩备份： 
    
    # partclone.ext4 -c -s /dev/sda1 | gzip -c > ~/image_sda1.pcl.gz
    
**注意：** 为获得最大压缩效果，请使用 `gzip -c9`，或者尝试使用其他[压缩工具](<../zh-cn/Archiving_and_compression.html#Compression_tools> "Archiving and compression")

还原它： 
    
    # zcat ~/image_sda1.pcl.gz | partclone.ext4 -r -o /dev/sda1
    