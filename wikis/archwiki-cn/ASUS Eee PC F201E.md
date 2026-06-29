**翻译状态：**

  * 本文（或部分内容）译自 [ASUS Eee PC F201E](<https://wiki.archlinux.org/title/ASUS_Eee_PC_F201E> "arch:ASUS Eee PC F201E")，最近一次同步于 2020-05-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/ASUS_Eee_PC_F201E?diff=0&oldid=610398>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ASUS_Eee_PC_F201E_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Asus Eee PC F201E 是一款轻巧的笔记本/超极本，与 [X201E](<https://www.asus.com/Laptops/X201E/>) 相似。显然，它仅在德国出售。 

F201E 具有 11.6 英寸屏幕和 1.1 GHz Intel Celeron 847 处理器。它配备 4GB RAM，500GB 硬盘驱动器，集成 Intel HD 显卡，网络摄像头和 30 瓦 2 芯电池，最多可提供 5 小时的使用时间。 

##  硬件支持

###  图形

可以使用 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包。 

###  音频

使用标准 [ALSA](<../zh-cn/ALSA.html> "ALSA") 和 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 设置。 

####  没有耳机声音

如果耳机插孔不起作用，请确保已安装并启动 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")（通常从 X 会话启动，但在某些设置中可能需要手动启动）。 

##  参考

  * [Asus F201E 安装过程示例](<https://gist.github.com/yuvadm/509eda44bb2d25c11eeb>)
