[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** No updates since 2020-08, English page has seen a large update since.（在 [Talk:Linux-ck#](<../zh-cn/Talk:Linux-ck.html>) 中讨论）

相关文章

  * [Unofficial user repositories/Repo-ck](</wzh/index.php?title=Unofficial_user_repositories/Repo-ck&action=edit&redlink=1> "Unofficial user repositories/Repo-ck（页面不存在）")
  * [Kernel](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel")
  * [Modprobed-db](</wzh/index.php?title=Modprobed-db&action=edit&redlink=1> "Modprobed-db（页面不存在）")

##  一般包细节

[Linux-ck](<https://aur.archlinux.org/packages/Linux-ck/>)AUR 是 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 和[用户预编译包](</wzh/index.php?title=Unofficial_user_repositories/Repo-ck&action=edit&redlink=1> "Unofficial user repositories/Repo-ck（页面不存在）")中都可用的软件包，它允许用户运行用 Con Kolivas 的 ck 补丁集[[1]](<http://ck.kolivas.org/patches/>)修补的内核和标头设置，包括名为 MuQSS 的 CPU 调度程序（ _Multiple Queue Skiplist Scheduler_ ，发音为 _mux_ ，代替了他先前的著作 Brain Fuck Scheduler（BFS）。许多 Arch Linux 用户选择此内核是因为其在任何负载情况下均具有出色的桌面交互性和响应能力。 

CK 补丁集旨在用于台式机/笔记本电脑，但不适用于服务器。它提供了低延迟环境，并且非常适合 16 个或更少的 CPU。为了能够引导到内核，必须适当配置[启动加载器](</wzh/index.php?title=%E5%90%AF%E5%8A%A8%E5%8A%A0%E8%BD%BD%E5%99%A8&action=edit&redlink=1> "启动加载器（页面不存在）")。 

###  发行周期

Linux-ck 大致遵循官方 Arch 内核的发布周期，但不仅如此。以下是新软件包发布的要求： 

  * CK 补丁集与当前内核版本兼容

###  长期支持 (Long-Term Support) (LTS) CK 版本

除了 [linux-ck](<https://aur.archlinux.org/packages/linux-ck/>)AUR 软件包之外，还有 LTS 内核版本，其中包括上述补丁集和先前提到的修改： 

  * [linux-lts-ck](<https://aur.archlinux.org/packages/linux-lts-ck/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] \- 使用 CK 补丁集修补的当前 Arch Linux LTS 内核

**注意：** 该软件包由 vishwin 维护，因此预编译版本将不会出现在非官方的ck仓库中。

##  关于 MuQSS 的更多信息

请参阅 CK 发布的 [LKML 公告](<https://lore.kernel.org/lkml/6544690.h1r1hWEHvO@hex/>)。 

###  检查是否启用了 MuQSS

启用 MuQSS 时，此启动消息应出现在内核环形缓冲区中： 
    
    # dmesg | grep -i muqss
    ...
    MuQSS CPU scheduler v0.120 by Con Kolivas.
    
###  应用了 MuQSS 补丁的内核和 systemd

认为 MuQSS 不支持 _cgroups_ 是一个常见的错误。它支持但不支持所有 cgroup 功能（例如，CPU 限制将不起作用）。 

##  在 Linux-ck 中使用树外模块

使用 [DKMS](<../zh-cn/DKMS.html> "DKMS") 可以轻松地编译和管理许多树外模块（broadcom-wl，nvidia，virtualbox 等）。 

##  另请参见

  * [Con Kolivas 的内核补丁仓库](<http://ck.kolivas.org/patches/>)
  * [Con Kolivas 的博客](<https://ck-hack.blogspot.it/>)
  * [Con Kolivas 在 Linux 内核邮件列表上的第一个 BFS 公告](<https://lore.kernel.org/lkml/20090906205952.GA6516@elte.hu/>)
  * [Wikipedia 的 Con Kolivas 页面](<https://en.wikipedia.org/wiki/Con_Kolivas> "wikipedia:Con Kolivas")
  * [Wikipedia 的 BFS 文章](<https://en.wikipedia.org/wiki/Brain_Fuck_Scheduler> "wikipedia:Brain Fuck Scheduler")
  * [Arch ck Linux 论坛支持主题](<https://bbs.archlinux.org/viewtopic.php?pid=1869636>)
