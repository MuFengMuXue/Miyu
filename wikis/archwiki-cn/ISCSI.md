**翻译状态：**

  * 本文（或部分内容）译自 [iSCSI](<https://wiki.archlinux.org/title/iSCSI> "arch:iSCSI")，最近一次同步于 2022-07-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/iSCSI?diff=0&oldid=737073>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/iSCSI_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

使用 [iSCSI](<https://en.wikipedia.org/wiki/iSCSI> "wikipedia:iSCSI") 您可以通过基于 IP 的网络访问存储。 

导出的存储实体是 **target** 导入的实体是 **initiator** 。 

从 Linux 2.6.38 开始，[LIO](<../zh-cn/ISCSI_Target.html> "ISCSI Target") 是内核内 iSCSI 目标。 [SCST](<https://scst.sourceforge.net/>) 是另一个包含内核的候选对象。[[1]](<https://lwn.net/Articles/424004/>)

当前的启动器是 [Open-iSCSI](<../zh-cn/Open-iSCSI.html> "Open-iSCSI")。 

可以[通过 iSCSI 引导 Arch Linux](</wzh/index.php?title=ISCSI/Boot&action=edit&redlink=1> "ISCSI/Boot（页面不存在）")。 

##  参见

  * [Gentoo:iSCSI](<https://wiki.gentoo.org/wiki/iSCSI> "gentoo:iSCSI")
