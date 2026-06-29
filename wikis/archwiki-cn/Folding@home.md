**翻译状态：**

  * 本文（或部分内容）译自 [Folding@home](<https://wiki.archlinux.org/title/Folding@home> "arch:Folding@home")，最近一次同步于 2020-05-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/Folding@home?diff=0&oldid=611430>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Folding@home_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Help Stanford University scientists studying Alzheimer's, Huntington's, Parkinson's, and many cancers by simply running a piece of software on your computer. The problems we are trying to solve require so many calculations, we ask people to donate their unused computer power to crunch some of the numbers. In just 5 minutes... Add your computer to over 333,684 others around the world to form the world's largest distributed supercomputer. 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [foldingathome](<https://aur.archlinux.org/packages/foldingathome/>)AUR 包。为了使用您的 GPU 进行计算（强烈推荐），您需要 [ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包 和适合您的 GPU 的 [OpenCL](<../zh-cn/GPGPU.html#OpenCL> "GPGPU") 包。 Nvidia 用户也可以使用 [CUDA](<../zh-cn/GPGPU.html#CUDA> "CUDA")。 

##  配置

运行 `FAHClient --configure`，以 root 身份生成 `/etc/foldingathome/config.xml` 配置文件。(Arch Linux 团队编号是 45032) 此外，您可以手动编辑 `/etc/foldingathome/config.xml`。有了配置文件后，您就可以启动守护进程，检查它的状态，并使守护进程在启动时自动启动。 
    
    $ cd /etc/foldingathome
    # FAHClient --configure
    
然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `foldingathome.service` systemd 单元。Nvidia 用户也应该[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `foldingathome-nvidia.service` systemd 单元。 

###  图形化运行

您可以通过打开网页浏览器并访问 <http://localhost:7396/> 来管理守护进程。另外，您也可以安装 [fahcontrol](<https://aur.archlinux.org/packages/fahcontrol/>)AUR 并使用 FAHControl 程序。 

守护进程也可以被远程控制。这样做的说明在 `/etc/foldingathome/config.xml` 中列出。如果有必要，请记得打开防火墙端口。 

###  终端中运行

foldingathome 的行为可以通过编辑 `/opt/fah/config.xml` 来定制。可以指定的一些选项如下： 

  * 密码，用于识别你的身份。虽然不需要，但它提供了一定程度的安全性。详情请参见 [[1]](<https://foldingathome.org/support/faq/points/passkey/>)

    <passkey v='passkey'/>
    
  * CPU 或 GPU 的并行

    <slot id='0' type='CPU'/>
    
###  在限制权限的情况下运行 f@h

更新版的 [foldingathome](<https://aur.archlinux.org/packages/foldingathome/>)AUR 包（>7.6.9）已经以有限用户的身份运行。它还安装了一个您可以使用的 systemd 用户脚本，没有 root 权限的用户都可以启用它（您仍然需要 video 组权限才能使用 GPU）。 

##  监测工作单位的计算情况

有几种方法可以在命令行和 GUI 中监控 FAH 客户端的进度。 

Folding@home 会将其日志文件写入数据目录。通过检查最后几行，你可以检查它的进度，例如 `tail -10 /var/log/foldingathome/log.txt`。 

folding at home 发行的 [FAHCONTROL](<https://aur.archlinux.org/packages/FAHCONTROL/>)AUR 软件为您提供了高效的控制本地主机和远程主机的方法。只需用相应的“添加”按钮添加另一个客户端，然后输入名称、IP地址、端口和密码（如果你设置了的话），点击保存即可。这时软件应该会尝试建立与远程主机的连接，并在单独的客户端选项卡中显示进度。 

要检查 NVidia GPU 的使用率，你可以使用 [nvtop-git](<https://aur.archlinux.org/packages/nvtop-git/>)AUR。它还可以报告核心温度和电源使用情况。 

##  问题解决

如果您的 GPU 被支持但仍未使用，请编辑 `/etc/foldingathome/config.xml` 文件，尝试自动配置 GPU： 
    
    <gpu v='true'/>
    
##  参见

  * [Folding@home 主页](<https://foldingathome.org/>)
  * [Folding@home FAQ](<https://foldingathome.org/support/faq/>)
  * [Folding@home 配置指南](<https://foldingathome.org/support/faq/installation-guides/configuration-guide/>)
  * [Arch Folding@home 团队页面](<https://stats.foldingathome.org/team/45032>)
  * 更多有关 Arch 团队的统计 [extremeoverclocking.com](<https://folding.extremeoverclocking.com/team_summary.php?s=&t=45032>)
