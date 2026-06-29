[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 因心理原因未更新，且需要重写 (在[Talk:Scx-scheds](<../zh-cn/Talk:Scx-scheds.html>)讨论)

[scx-scheds](<https://archlinux.org/packages/?name=scx-scheds>)包 是 scheds-ext 的程序实现，**scheds-ext** （Scheduler Extensions）是 Linux 的一个可拓展调度器框架，允许在不修改内核代码的情况下通过 **[BPF](<https://zh.wikipedia.org/wiki/BPF> "zhwp:BPF")** （Berkeley Packet Filter）或 eBPF 来实现自定义调度策略，具有少量的性能提升效果。 

##  安装

需要先检查内核是否支持 bpf，使用 [root](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "Root") 权限执行指令： 
    
    # zcat /proc/config.gz | grep -i BPF

通常情况下会输出这些内容： 
    
    # zcat /proc/config.gz | grep -i BPF
    
    CONFIG_BPF=y
    CONFIG_HAVE_EBPF_JIT=y
    CONFIG_ARCH_WANT_DEFAULT_BPF_JIT=y
    .....

如果得到如上结果，代表内核支持 BPF。 [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [scx-scheds](<https://archlinux.org/packages/?name=scx-scheds>)包 与 [bpf](<https://archlinux.org/packages/?name=bpf>)包。 

##  部署

scx-scheds 安装后会提供两个 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务 `scx_loader.service` 和 `scx.service`：`scx.service` 是 scx 调度程序，`scx_loader.service` 则是通过 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 来实现 scheds-ext 框架加载器和管理器的实用程序。 

**警告：** 现在不再推荐使用 `scx.service`，推荐使用 `scx_loader.service` ，且不要同时运行，否则它们不会执行任何东西。

**警告：** 在使用 scheds-ext 框架的任何一个调度器时强烈建议[禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用")并[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止")使用 [ananicy-cpp-git](<https://aur.archlinux.org/packages/ananicy-cpp-git/>)AUR 等相关的包，因为 [anaicy-cpp-git](<https://aur.archlinux.org/packages/anaicy-cpp-git/>)AUR 等相关的包会干扰系统优先级导致 scheds-ext watchdog 超时，使调度程序被“杀死”。

**提示：** 内核的 [Lockdown](<../zh-cn/%E5%AE%89%E5%85%A8.html#Kernel_lockdown_mode> "安全") 模式设置为 `integrity` 并不会影响 `scx-scheds` 调度程序及 [dae](<../zh-cn/%E5%BB%BA%E8%AE%AE%E9%98%85%E8%AF%BB/%E4%B8%AD%E5%9B%BD%E7%94%A8%E6%88%B7%E7%9A%84%E6%8E%A8%E8%8D%90%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88.html#%E4%BB%A3%E7%90%86> "建议阅读/中国用户的推荐解决方案") 代理程序的正常运行。

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") scx_loader 服务。 

[scx-scheds](<https://archlinux.org/packages/?name=scx-scheds>)包 在安装后会生成一个默认配置文件位于 `/etc/default/scx` ，用于 `scx.service`。 

**注意：**`scx_loader.service` 不会使用 `/etc/default/scx` 配置文件。

###  配置 scx 服务

在 `scx.service` 中分为两个部分： `SCX_SCHEDULER` 和 `SCX_FLAGS` 。 
    
    /etc/default/scx
    
    # List of scx_schedulers: scx_bpfland scx_central scx_flash scx_lavd scx_layered scx_nest scx_qmap scx_rlfifo scx_rustland scx_rusty scx_simple scx_userland scx_p2dq scx_tickless
    SCX_SCHEDULER=scx_bpfland
    
    # Set custom flags for each scheduler, below is an example of how to use
    #SCX_FLAGS='-p -m performance'
    
`SCX_SCHEDULER` 为 scx 调度器，总共 14 个调度器，主要调度器有 4 个：`scx_bpfland`、`scx_rusty`、`scx_flash` 和 `scx_lavd` 。 

`SCX_FLAGS` 是调度器的启动参数，例如： 
    
    SCX_FLAGS='-p -m performance'

`-p` 参数表示**启用每颗CPU的任务优先级划分** 。`-m` 表示使用模式 performance 代表 gaming 或 lowlatency（低延迟）。 

适用环境：`scx_rustland` 旨在优先处理交互式工作负载，而不是后台 CPU 密集型工作负载，如游戏，实时直播和视频会议等，但不适用于生产环境；`scx_lavd` 使用了 **LAVD** （延迟关键性感知虚拟截止时间）调度算法，旨在提高 Linux 在游戏上的性能提升，虽然仍在开发，但已经能用于生产环境；`scx_bpfland` 是 `scx_rustland` 的改进版本，完全能用于平常使用和生产环境；`scx_rusty` 为一个多域、BPF/用户空间混合调度器，可以适应不同架构和工作负载，可以投入生产环境，但需要调整。 

###  配置 scx_loader 服务

**注意：** scx_loader 服务的配置文件是不会自动生成的，需要用户手动配置。

scx_loader 的配置文件有两个：`/etc/scx_loader.toml` 和 `/etc/scx_loader/config.toml` 。 

文件结构为：
    
    /etc/scx_loader/config.toml 
    
    default_sched = "scx_bpfland"
    default_mode = "Auto"
    
    [scheds.scx_bpfland]
    auto_mode = ["-m","performance"]

`default_sched` 意思是默认使用的调度器。`scx` 和 `scx_loader` 的默认调度器都是 `scx_bpfland`，如果字段为空则什么都不启用。 `default_mode` 指默认启动模式，主要参数有： `"Auto"`、`"LowLatency"`、`"PowerSave"`、`"Gaming"` 和 `"Server"`。如果没有参数则为默认模式，即 `"Auto"` 。 `[scheds.scx_name]` 指对调度器的自定义标志，把 `scx_name` 修改为实际的调度程序。参数标志有： `auto_mode`、`gaming_mode`、`lowlatency_mode`、`powersave_mode` 和 `server_mode`；每个字段是一个字符串且每个字符串表示一个参数标志。如果没有参数标志则使用默认。 

**注意：**`server_mode` 仅 `scx_bpfland` 可用

参考样例：
    
    /etc/scx_loader.toml 
    
    default_sched = "scx_bpfland"
    default_mode = "LowLatency"
    
    [scheds.scx_bpfland]
    auto_mode = []
    gaming_mode = ["-m", "performance"]
    lowlatency_mode = ["-k", "-s", "5000", "-l", "5000"]
    powersave_mode = ["-m", "powersave"]

**提示：** 如无微调设置需求，仅需设置 `default_sched` 与 `default_mode` 项，因其它项具有默认值。

###  参数标签

#### scx_bpfland

  * Gaming Mode : `-m performance`
  * Low Latency Mode : `-s 5000 -S 500 -l 5000`
  * PowerSave Mode : `-m powersave`

#### scx_rusty

没有自定义参数标志，使用默认参数标志。 

#### scx_lavd

  * Gaming Mode：`--performance`
  * Low Latency Mode：`--performance`
  * AutoPower Mode：`--autopower`
  * PowerSave Mode：`--powersave`

#### scx_flash

没有自定义参数标签，使用默认参数标签。 

###  启动和检查

通过 [systemd](<../zh-cn/Systemd.html> "Systemd") [启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")后，使用 [root](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "Root") 权限进行检查。通过命令检查是否启用以及查看调度器：
    
    # cat /sys/kernel/sched_ext/state /sys/kernel/sched_ext/*/ops 2>/dev/null

###  回退模式

如果配置文件中未定义特定参数标志， `scx_loader` 会自动使用默认的参数标志。 

##  参见

  * [CachyOS sched-ext教程](<https://wiki.cachyos.org/configuration/sched-ext/>)
  * [sched-ext配置](<https://github.com/sched-ext/scx/blob/main/rust/scx_loader/configuration.md>)
  * [crates的scx_bpfland](<https://crates.org.cn/crates/scx_bpfland>)
  * [crates的scx_rusty](<https://crates.org.cn/crates/scx_rusty>)
  * [crates的scx_rustland](<https://crates.org.cn/crates/scx_rustland>)
  * [crates的scx_lavd](<https://crates.org.cn/crates/scx_lavd>)
