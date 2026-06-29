[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Haveged](<../zh-cn/Talk:Haveged.html>)讨论)

相关文章

  * [Rng-tools](</wzh/index.php?title=Rng-tools&action=edit&redlink=1> "Rng-tools（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [Haveged](<https://wiki.archlinux.org/title/Haveged> "arch:Haveged")，最近一次同步于 2014-12-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Haveged?diff=0&oldid=349739>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Haveged_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[haveged ](<https://www.issihosts.com/haveged/>) 项目的目的是提供一个简单易用的不可预测[随机数生成器](<../zh-cn/Random_number_generation.html> "Random number generation")，基于 HAVEGE 算法。Haveged 可以解决在某些情况下，系统熵过低的问题。 

**警告：** 此程序无法保证熵的质量([[1]](<https://lwn.net/Articles/525459/>)，[[2]](<https://security.stackexchange.com/questions/34523/is-it-appropriate-to-use-haveged-as-a-source-of-entropy-on-virtual-machines>)). 如果对安全要求较高，请考虑使用硬件随机数生成器 [rng-tools](<https://archlinux.org/packages/?name=rng-tools>)包.

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install")软件包 [haveged](<https://archlinux.org/packages/?name=haveged>)包. 

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")和[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")服务 `haveged.service`。 

##  检查当前的熵

要检查是否需要 Haveged, 使用下面命令查看当前收集到的熵: 
    
    # cat /proc/sys/kernel/random/entropy_avail
    
如果结果比较低 (<1000)，建议安装 haveged. 否则加密程序会等待系统有足够的熵。例如如果使用[软件热点](<../zh-cn/Software_access_point.html> "Software access point")，网速会比较慢。 

安装 haveged 之后，可以再次查看系统熵看下有无提升。 

##  其它选择

Unless you have a specific reason to not trust any hardware random number generator on your system, you should try to use them with the [rng-tools](</wzh/index.php?title=Rng-tools&action=edit&redlink=1> "Rng-tools（页面不存在）") first and if it turns out not to be enough (or if you do not have a hardware random number generator available), then use Haveged. 

## Virtual machines

As discussed at [Is it appropriate to use haveged as a source of entropy on virtual machines?](<https://security.stackexchange.com/questions/34523/is-it-appropriate-to-use-haveged-as-a-source-of-entropy-on-virtual-machines>), it can be contested whether haveged provides quality entropy within a virtual environment. Haveged relies on the rdtsc instruction, which may be virtualized within a virtual machine resulting in lower quantity entropy. On some hypervisors, it is possible to disable the virtualization of rdtsc, which would in theory allow haveged to provide higher quality entropy. 

To disable the virtualization of the rdtsc instruction in VMware ESXi, add the setting `monitor_control.virtual_rdtsc = "FALSE"` to the virtual machine’s .vmx configuration file. VMware recommends the setting for use when performing measurements that require a precise source of real time in the virtual machine. [[3]](<https://www.vmware.com/files/pdf/Timekeeping-In-VirtualMachines.pdf>)

##  参阅

  * [http://www.issihosts.com/haveged](<https://www.issihosts.com/haveged>)
  * [如何通过 haveged 增加系统的熵](<https://www.digitalocean.com/community/tutorials/how-to-setup-additional-entropy-for-cloud-servers-using-haveged>)
