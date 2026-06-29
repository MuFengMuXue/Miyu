**翻译状态：**

  * 本文（或部分内容）译自 [Ryzen](<https://wiki.archlinux.org/title/Ryzen> "arch:Ryzen")，最近一次同步于 2025-04-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ryzen?diff=0&oldid=824521>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ryzen_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Ryzen](<https://en.wikipedia.org/wiki/Ryzen> "w:Ryzen") 是 Advanced Micro Devices (AMD) 制造的微处理器品牌。本文涵盖了不同代 CPU 的系统配置和故障排除信息。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 添加关于 `amd_pstate` 的内容，或至少链接到 [CPU frequency scaling#Scaling drivers](<../zh-cn/CPU_frequency_scaling.html#Scaling_drivers> "CPU frequency scaling")。 (在 [Talk:AMD Ryzen](<../zh-cn/Talk:AMD_Ryzen.html>) 中讨论)

相关文章

  * [性能优化](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html> "性能优化")
  * [性能优化/启动过程](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96/%E5%90%AF%E5%8A%A8%E8%BF%87%E7%A8%8B.html> "性能优化/启动过程")
  * [内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")
  * [微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")

##  启用微码支持

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [amd-ucode](<https://archlinux.org/packages/?name=amd-ucode>)包 包以启用微码更新，并在[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")页面的帮助下启用它。这些更新提供了对系统稳定性至关重要的 Bug 修复。尽管它是专有产权的，仍然**强烈建议** 使用。 

##  微调 Ryzen

###  监视电压、电源和温度

[lm_sensors](<https://archlinux.org/packages/?name=lm_sensors>)包 可以开箱即用来监视温度。但是电量消耗及电压等更详细的信息需要 [zenpower3-dkms](<https://aur.archlinux.org/packages/zenpower3-dkms/>)AUR。也有图形用户界面的工具，如 [zenmonitor](<https://aur.archlinux.org/packages/zenmonitor/>)AUR 和对于 Zen 3 CPU 的 [zenmonitor3-git](<https://aur.archlinux.org/packages/zenmonitor3-git/>)AUR。 

###  电源管理、降压和超频

  * **RyzenAdj** — RyzenAdj 是一个用来调节 Ryzen 移动处理器电源管理设置的命令行工具。

     <https://github.com/FlyGoat/RyzenAdj> || [ryzenadj-git](<https://aur.archlinux.org/packages/ryzenadj-git/>)AUR

  * **amdctl** — amdctl 是一个 AMD CPU 的降、超（升）频率和电压的命令行工具，目前支持 AMD CPU 的 10h, 11h, 12h, 15h, 16h, 17h 和 19h 家族。

     <https://github.com/kevinlekiller/amdctl/> || [amdctl](<https://aur.archlinux.org/packages/amdctl/>)AUR

  * **ZenStates-Linux** — ZenStates 是一个调节时钟频率和电压的命令行工具。一个详细的设置例子可以在 [Level1Techs 论坛](<https://forum.level1techs.com/t/overclock-your-ryzen-cpu-from-linux/126025>) 找到。

     <https://github.com/r4m0n/ZenStates-Linux> || [zenstates-git](<https://aur.archlinux.org/packages/zenstates-git/>)AUR

  * **ryzen_smu** — Ryzen SMU 是一个 Linux 内核驱动程序，它可以让用户访问某些 AMD Ryzen 处理器的 SMU（系统管理单元）。[这](<https://github.com/svenlange2/Ryzen-5800x3d-linux-undervolting/>) 是一个给 5800x3D 降压的例子。

     <https://gitlab.com/leogx9r/ryzen_smu> || [ryzen_smu-dkms-git](<https://aur.archlinux.org/packages/ryzen_smu-dkms-git/>)AUR

##  编译内核

关于启用 Ryzen 支持，参考 [Gentoo:Ryzen#Kernel](<https://wiki.gentoo.org/wiki/Ryzen#Kernel> "gentoo:Ryzen")。[官方支持的内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E5%AE%98%E6%96%B9%E6%94%AF%E6%8C%81%E7%9A%84%E5%86%85%E6%A0%B8> "内核")中已默认包含了所需的配置。 

##  疑难解答

###  随机重启

如果你遇到了随机重启的问题，请参考 [Gentoo:Ryzen#Random_reboots_with_mce_events](<https://wiki.gentoo.org/wiki/Ryzen#Random_reboots_with_mce_events> "gentoo:Ryzen")。Ryzen 5000 系列，特别是 5950X 和 5900X 这两款高端型号，在 Linux 下似乎有一些轻微的不稳定问题，可能与 5.11+ 的内核有关，如[这个内核 bug](<https://bugzilla.kernel.org/show_bug.cgi?id=212087>) 所示。根据网上的报告，似乎 Windows 默认会让 CPU 运行在更高的电压和更低的峰值频率，而 Linux 内核则相反，这取决于你的硅片抽签结果，可能会导致一些随机的应用程序崩溃或硬件错误，从而导致重启。你可以通过 dmesg 日志来识别这些问题，例如： 
    
    kernel: mce: [Hardware Error]: Machine check events logged
    kernel: mce: [Hardware Error]: CPU 22: Machine Check: 0 Bank 1: bc800800060c0859
    kernel: mce: [Hardware Error]: TSC 0 ADDR 7ea8f5b00 MISC d012000000000000 IPID 100b000000000 
    kernel: mce: [Hardware Error]: PROCESSOR 2:a20f10 TIME 1636645367 SOCKET 0 APIC d microcode a201016
    
CPU ID 和处理器编号可能会不同。要解决这个问题，你需要给你的 CPU 提供更高的电压，以便它在高频运行时保持稳定。最简单的方法是使用 AMD 曲线优化器，这是一个可以通过你的主板 UEFI 访问的功能。进入 UEFI 并设置一个正向的 4 点偏移，这会增加你的 CPU 在高负载时的电压。这会限制超频的潜力，因为需要更好的散热，但它会运行得更稳定。更多细节请查看[这个论坛帖子](<https://community.amd.com/t5/processors/ryzen-5900x-system-constantly-crashing-restarting-whea-logger-id/td-p/423321/page/84>)。当我对我的 5950X 这样做时，我的处理器稳定了，频率和电压的范围也更接近 Windows 下的情况。 

###  系统挂起

在类似 [#随机重启](<#%E9%9A%8F%E6%9C%BA%E9%87%8D%E5%90%AF>)的情况下，系统可能会在重负载或特定的低负载下挂起，即使在应用了修复措施后也是如此。重置按钮或强制关机不起作用，外设电源关闭，视频输出可能会停止，拔掉电源是唯一的方法。 

将频率降低到非超频标准并增加 CPU 或 RAM 的电压可能会有所帮助，但可能无法解决问题。一个潜在的解决方法是更新 UEFI（也被误称为“BIOS 更新”），然后应用 PBO+4 曲线以提高高频下的稳定性。根据硅片抽签结果，某些 CPU 可能需要 +6 或更高的偏移量。 

###  屏幕撕裂（APU）

如果你正在使用 [Xorg](<../zh-cn/Xorg.html> "Xorg") 并遇到了屏幕撕裂的问题，请查看：[AMDGPU#无撕裂渲染](<../zh-cn/AMDGPU.html#%E6%97%A0%E6%92%95%E8%A3%82%E6%B8%B2%E6%9F%93> "AMDGPU")。 

###  软锁冻结

这个 bug 已经很有名了，目前正在 [bugzilla](<https://bugzilla.kernel.org/show_bug.cgi?id=196683>) 和 [launchpad](<https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1690085>) 上讨论。虽然解决方案并不是在所有情况下都一样，但[这个](<https://bugs.launchpad.net/linux/+bug/1690085/comments/69>)帮助了一些用户。把这个命令 `echo rcu_nocbs=0-$(($(nproc)-1))` 的输出作为一个内核参数添加，其中命令 `nproc` 只是打印出你的 CPU 的线程数。要应用这个选项，你需要一个带 `CONFIG_RCU_NOCB_CPU` 选项编译过的内核（比如 [linux](<https://archlinux.org/packages/?name=linux>)包）。 

导致冻结的另一个原因是电源管理中的 c-states。最大的省电状态 c6 可能会导致问题。在一些情况下，添加内核参数 `processor.max_cstate=5` 会有帮助，但其他用户报告说这个选项没有应用，c6 状态仍然被进入。对他们来说，这个包 [disable-c6-systemd](<https://aur.archlinux.org/packages/disable-c6-systemd/>)AUR 会有帮助。在使用它之前，需要运行 `modprobe msr` 来激活那个内核模块。 

一些带有 Ryzen CPU 的笔记本电脑，比如 HP Envy x360 15-bq100na，可能会遇到 CPU 软锁定，导致系统冻结。可以通过添加内核参数 `idle=nomwait` 来避免。 

在一些情况下，内核参数 `pci=nomsi` 可以修复问题。 

在其他一些情况下，问题只是硬件不好，保修换一个新的 CPU 可能就能解决你的问题。 

###  关机、重启、挂起时卡住

**注意：** 通过更新 UEFI（也被误称为“BIOS 更新”）获取的较新 AGESA 固件可能已经修复了这个问题。

这似乎与 C6 c-state 有关，它在 Linux 中似乎并不受到很好的支持（如果有的话）。 

要解决这个问题，进入 UEFI 设置并搜索一个标记为类似于“电源空闲控制”的选项。将其值更改为“典型空闲电流”。请注意，这些名称取决于主板制造商对它们的命名，因此在您的特定情况下可能会有所不同。 

其他不太理想的解决方案包括在 UEFI 设置中禁用 c-states 或在内核命令行参数中添加 `processor.max_cstate=1`。 

##  另见

  * [Gentoo:Ryzen](<https://wiki.gentoo.org/wiki/Ryzen> "gentoo:Ryzen")
