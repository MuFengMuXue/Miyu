**翻译状态：**

  * 本文（或部分内容）译自 [GNU Radio](<https://wiki.archlinux.org/title/GNU_Radio> "arch:GNU Radio")，最近一次同步于 2024-08-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/GNU_Radio?diff=0&oldid=749904>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GNU_Radio_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [DVB-T](</wzh/index.php?title=DVB-T&action=edit&redlink=1> "DVB-T（页面不存在）")
  * [RTL-SDR](</wzh/index.php?title=RTL-SDR&action=edit&redlink=1> "RTL-SDR（页面不存在）")

[GNU Radio](<https://wiki.gnuradio.org/index.php/Main_Page>) 是一个提供了信号处理模块来实现软件无线电的开源且免费的SDK。它可以与低成本易获取的射频硬件来组成软件定义无线电（software-defined radios），同时在没有硬件的情况下也可以作为模拟环境来使用，这个套件被广泛的应用于爱好者，学术与商业环境中来协助无线通讯研究与设置无线电系统。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gnuradio](<https://archlinux.org/packages/?name=gnuradio>)包 可获取最新稳定版 GNU Radio。 

最新的安装包为 [gnuradio-git](<https://aur.archlinux.org/packages/gnuradio-git/>)AUR，在某种特定情况中 VOLK 需要分别从 [libvolk-git](<https://aur.archlinux.org/packages/libvolk-git/>)AUR 中构建。 

如果需要 `gnuradio-companion`，只需要安装 [gnuradio-companion](<https://archlinux.org/packages/?name=gnuradio-companion>)包，这个包将会安装包括 GNU Radio 和它的一些依赖包。 

另外一个热门包是 [gnuradio-osmosdr](<https://archlinux.org/packages/?name=gnuradio-osmosdr>)包，这个包提供了很多常见的 SDR 设备的 GRC 源模块（Funcube Dongle、[RTL-SDR](</wzh/index.php?title=RTL-SDR&action=edit&redlink=1> "RTL-SDR（页面不存在）")（英语：[RTL-SDR](<https://wiki.archlinux.org/title/RTL-SDR> "en:RTL-SDR")）、USRP、OsmoSDR、BladeRF 和 HackRF）。 

##  疑难解答

###  TypeError: in method 'source_sptr_set_gain_mode', argument 2 of type 'bool'

如果使用（osmocom）RTL-SDR 源，你可能会看到这个错误。解决方法是将 Gain Mode 手动设置成 `True` 或 `False`。 
