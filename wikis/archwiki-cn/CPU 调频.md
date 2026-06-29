**翻译状态：**

  * 本文（或部分内容）译自 [CPU frequency scaling](<https://wiki.archlinux.org/title/CPU_frequency_scaling> "arch:CPU frequency scaling")，最近一次同步于 2023-03-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/CPU_frequency_scaling?diff=0&oldid=769309>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/CPU_frequency_scaling_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Power saving](</wzh/index.php?title=Power_saving&action=edit&redlink=1> "Power saving（页面不存在）")
  * [Laptop Mode Tools](<../zh-cn/Laptop_Mode_Tools.html> "Laptop Mode Tools")
  * [Undervolting CPU](</wzh/index.php?title=Undervolting_CPU&action=edit&redlink=1> "Undervolting CPU（页面不存在）")

[CPU 调频](<https://docs.kernel.org/admin-guide/pm/cpufreq.html>)为操作系统提供了动态调整 CPU 频率的能力，实现节能或提升性能。系统负载、ACPI 事件或者用户空间程序都可以触发 CPU 频率的调整。 

Linux 内核通过 _cpufreq_ 子系统实现此功能，包含以下两个抽象层： 

  * [#调速器](<#%E8%B0%83%E9%80%9F%E5%99%A8>)基于系统需求计算所需的 CPU 频率。
  * [#调频驱动](<#%E8%B0%83%E9%A2%91%E9%A9%B1%E5%8A%A8>)直接与 CPU 交互，按照调速器的请求调整频率。

系统会自动选择默认的调频驱动程序和调速器，但是为您仍然可以使用[cpupower](<#cpupower>)、 [acpid](<../zh-cn/Acpid.html> "Acpid")、 [Laptop Mode Tools](<../zh-cn/Laptop_Mode_Tools.html> "Laptop Mode Tools") 或桌面环境提供的 GUI 工具等用户空间应用程序来进行高级配置。 

##  用户空间工具

### thermald

[thermald](<https://archlinux.org/packages/?name=thermald>)包 是一个防止 Intel 平台过热的 [Linux 守护进程](<https://01.org/linux-thermal-daemon>)。此守护进程会监控平台温度，并通过控制 P-states、T-states 和 Intel power clamp 驱动主动控制温度水平。thermald 也适用于较老的 Intel CPU。如果最新版本的驱动程序不可用，那么守护进程会还原为 x86 MSR (Model Specific Register)，由 Linux“cpufreq 子系统”来控制系统冷却。 

默认情况下，它利用 CPU 中的数字温度传感器读取 CPU 温度，在硬件采取激进的降温措施之前将 CPU 的温度控制在允许的范围内。如果 sysfs 中存在表面温度传感器，那么它会尝试将表面温度保持在 45℃ 以下。 

在使用 Tiger Lake 架构处理器的笔记本电脑（例如 [Dell Latitude 3420](</wzh/index.php?title=Dell_Latitude_3420&action=edit&redlink=1> "Dell Latitude 3420（页面不存在）")）上，此守护程序据说可以[解锁更多性能](<https://www.phoronix.com/review/intel-thermald-tgl>)。 

对应的 systemd 服务是 `thermald.service`，您应该[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")此服务。 

### i7z

[i7z](<https://archlinux.org/packages/?name=i7z>)包 是 i7 CPU （也同样适用于 i3、i5、i9 CPU）的报告工具。可以在终端下输入 `i7z` 或者使用图形化工具 `i7z-gui` 来运行该工具。 

### turbostat

[turbostat](<https://archlinux.org/packages/?name=turbostat>)包 可以显示现代 Intel 和 AMD CPU 的频率、功耗、空闲状态和其他统计数据。 

### cpupower

[cpupower](<https://archlinux.org/packages/?name=cpupower>)包 是一组为辅助 CPU 调频而设计的用户空间工具。该软件包并非必须，但强烈建议安装，因为它提供了方便的命令行实用程序，并且内置 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务，可在启动时更改调频器。 

_cpupower_ 的配置文件位于 `/etc/default/cpupower`。此配置文件由 `/usr/lib/systemd/scripts/cpupower` 中的 bash 脚本读取，而该脚本由 _systemd_ 通过 `cpupower.service` 激活。若要在启动时启用 _cpupower_ ，请执行： 
    
    # systemctl enable cpupower.service
    
### cpupower-gui

[cpupower-gui](<https://aur.archlinux.org/packages/cpupower-gui/>)AUR 是一个图形实用程序，旨在帮助 CPU 调频。该 GUI 基于 [GTK](<../zh-cn/GTK.html> "GTK")，提供与 _cpupower_ 相同的选项。 _cpupower-gui_ 可以更改每个内核的最大 / 最小 CPU 频率和调速器。该应用程序通过 [polkit](<../zh-cn/Polkit.html> "Polkit") 获得权限，并允许 `wheel` 用户组中的任何登录用户更改频率和调速器。 

### gnome-shell-extension-cpupower

[gnome-shell-extension-cpupower-git](<https://aur.archlinux.org/packages/gnome-shell-extension-cpupower-git/>)AUR是一个[GNOME](<../zh-cn/GNOME.html> "GNOME") shell扩展，可以改变 CPU 的最小/最大的频率，并启用/禁用调频。 

### auto-cpufreq

[auto-cpufreq](<https://aur.archlinux.org/packages/auto-cpufreq/>)AUR 是一个用于Linux的自动CPU速度和功率优化器，它基于对笔记本电脑的电池状态、CPU使用率、CPU温度和系统负载的主动监测。 

### power-profiles-daemon

[power-profiles-daemon](<https://archlinux.org/packages/?name=power-profiles-daemon>)包 中的 _powerprofilesctl_ 命令行工具通过 `power-profiles-daemon.service` 处理电源配置文件（如平衡、省电、性能）。GNOME 和 KDE 也提供了切换配置文件的[图形界面](<https://gitlab.freedesktop.org/hadess/power-profiles-daemon#how-to-use>)；见下文： 

  * [GNOME#Power modes](<../zh-cn/GNOME.html#Power_modes> "GNOME")
  * [KDE#Power management](<../zh-cn/KDE.html#Power_management> "KDE")

关于使用方法、用例以及与类似项目的比较，请参见该项目的 [README](<https://gitlab.freedesktop.org/hadess/power-profiles-daemon#power-profiles-daemon>)。 

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `power-profiles-daemon.service` 。注意，当 _powerprofilesctl_ 启动时，它也会尝试启动该服务（见`dbus.service`的[单元状态](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")）。 

**注意：** _power-profiles-daemon_ 与其他电源管理服务比如 [TLP](<../zh-cn/TLP.html> "TLP")， [tuned](<https://aur.archlinux.org/packages/tuned/>)AUR和 [system76-power](<https://aur.archlinux.org/packages/system76-power/>)AUR[冲突](<https://gitlab.freedesktop.org/hadess/power-profiles-daemon/-/blob/main/data/power-profiles-daemon.service.in#L3>)。要在不[卸载](<../zh-cn/Pacman.html#%E5%88%A0%E9%99%A4%E8%BD%AF%E4%BB%B6%E5%8C%85> "卸载") _power-profiles-daemon_ 的情况下使用上述服务之一（由于它可能存在依赖关系），可以通过 [mask](</wzh/index.php?title=Mask&action=edit&redlink=1> "Mask（页面不存在）") 来禁用 `power-profiles-daemon.service`（另见 [[1]](<https://github.com/linrunner/TLP/issues/564>)，[[2]](<https://linrunner.de/tlp/installation/arch.html#service-units>)）。

##  调频驱动

调频驱动实现了 CPU 特有的设置调速器指定频率的细节。严格来说，ACPI 标准要求电源性能状态（P-state）从P0开始性能逐渐降低。这种功能在英特尔称为 SpeedStep，在AMD称为 PowerNow! 

但在实践中，处理器提供了指定特定频率的方法，而不是局限于调频驱动程序处理的固定 P 状态。 

**注意：**

  * 原生 CPU 模块将会自动加载。
  * 对于现代 Intel CPU，将使用 `intel_pstate` 功率驱动程序，而非下列其他驱动程序。此驱动程序的优先级高于其他驱动程序，并编入内核（而非编译为模块）。此驱动程序将自动用于 Sandy Bridge（以及更新的 CPU）。`intel_pstate` 可能会忽略 BIOS P-State 设置，或者通过 `intel_cpufreq` 运行于 "被动模式"。如果使用时遇到问题，可以在内核行加入 `intel_pstate=disable`，这样系统会使用 `acpi_cpufreq` 驱动。
  * 在支持的 CPU 上(Zen 2 及之后型号)，在[内核参数](<../zh-cn/Kernel_parameter.html> "Kernel parameter") 中加入 `amd_pstate=passive` 可以手动启动 `amd_pstate` 。如果内核参数不起作用，可能需要进入主板设置程序中将CPPC和全局C状态控制(global c-state control)打开。主板中的大部分选项默认设置可能是自动（Auto），这往往意味着禁用，必须要手动改成启用（Enabled）才能生效。

_cpupower_ 需要相应模块来了解本地 CPU 的限制信息： 

模块 | 描述   
---|---  
intel_pstate | 此驱动程序通过内置调频器，实现面向 Intel Core（SandyBridge 和更新的型号）处理器的调频驱动。   
intel_cpufreq | 从内核 5.7 开始，intel_pstate 调频驱动程序为不支持 硬件P 状态管理(HWP) 的 CPU 选择“被动模式”又名 intel_cpufreq，即第 5 代或更早的 Intel Core i处理器。   
amd_pstate | 此驱动程序为 AMD Ryzen（某些 Zen 2 和更新版本）处理器实现了带有内部调速器的调频驱动程序。   
acpi_cpufreq | 此 CPUFreq 驱动程序可充分利用 ACPI Processor Performance States。此驱动程序也支持 Intel Enhanced SpeedStep（之前由 speedstep-centrino 模块（已废弃）提供支持）。   
speedstep_lib | 此 CPUFreq 驱动程序面向支持 Intel SpeedStep 的 CPU（主要包括 Atom 和早于 Pentinum 3 的 CPU）。   
powernow_k8 | 面向 K8/K10 Athlon 64/Opteron/Phenom 的 CPUFreq 驱动程序。从 Linux 3.7 开始，对于此系列中的较现代 CPU，将自动使用“acpi_cpufreq”。   
pcc_cpufreq | 此驱动程序支持 HP 和 Microsoft 提出的 Processor Clocking Control 接口，在某些 ProLiant 服务器上比较有用。   
p4_clockmod | 面向 Intel Pentium 4/Xeon/Celeron 处理器的 CPUFreq 驱动程序，可通过跳频来降低 CPU 温度。（您最好使用 SpeedStep 驱动程序。）   
  
查看所有可用的模块，运行以下命令： 
    
    $ ls /usr/lib/modules/$(uname -r)/kernel/drivers/cpufreq/
    
加载合适的模块 (see [Kernel modules](<../zh-cn/Kernel_modules.html> "Kernel modules") for details)。一旦合适的 cpufreq 驱动模块被加载成功，就可以通过以下命令查询到 CPU 的信息： 
    
    $ cpupower frequency-info
    
###  设置最大和最小频率

在罕见的情况下，可能有必要手动设置最大和最小频率。 

运行以下命令设置最大时钟频率（ _clock_freq_ 为时钟频率，单位为：GHz, MHz）： 
    
    # cpupower frequency-set -u _clock_freq_
    
运行以下命令设置最小时钟频率： 
    
    # cpupower frequency-set -d _clock_freq_
    
运行以下命令设置运行于指定频率： 
    
    # cpupower frequency-set -f _clock_freq_
    
**注意：**

  * 仅设置某一核心，添加参数 `-c _core_number_`。
  * The governor，频率的最大值和最小值可以在 `/etc/default/cpupower` 中设置。

或者，也可以手动设置频率： 
    
    # echo _value_ | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq
    
可以在 `/sys/devices/system/cpu/cpu*/cpufreq/scaling_available_frequencies` 或者类似的地方找到取值。 参考 [[3]](<https://web.archive.org/web/20201029114421/https://software.intel.com/sites/default/files/comment/1716807/how-to-change-frequency-on-linux-pub.txt>)

###  配置超频

在合适的散热条件下，某些处理器支持在短时间内将其频率提高到高于正常最大值的频率。 在 Intel 处理器上，这称为[英特尔睿频加速（英语：Intel Turbo Boost）](<https://en.wikipedia.org/wiki/Intel_Turbo_Boost> "wikipedia:Intel Turbo Boost"), 在 AMD 处理器上叫做 [Turbo-Core（别名：AMD Core Performance Boost ，缩写CPB）](<https://en.wikipedia.org/wiki/AMD_Turbo_Core> "wikipedia:AMD Turbo Core")。 

####  通过 sysfs 配置 (intel_pstate)

intel_pstate 有一个特定于驱动程序的接口，用于禁止处理器进入 turbo P-States： 
    
    # echo 1 > /sys/devices/system/cpu/intel_pstate/no_turbo
    
####  通过 sysfs 配置 (Other scaling drivers)

对于 intel_pstate 以外的缩放驱动程序，如果驱动程序支持超频，系统中应该可以找到 sysfs 属性`/sys/devices/system/cpu/cpufreq/boost`，并可用于禁用/启用超频： 
    
    # echo 0 > /sys/devices/system/cpu/cpufreq/boost
    
####  通过 x86_energy_perf_policy 配置

在 Intel 处理器上，[x86_energy_perf_policy](<https://archlinux.org/packages/?name=x86_energy_perf_policy>)包 也可用于配置 Turbo Boost： 
    
    # x86_energy_perf_policy --turbo-enable 0
    
##  调速器

调速器（见下表）是预设的 CPU 电源方案，有些是设置为固定频率，有些会根据算法计算出需要的频率。在同一时刻只会有一个会调速器被激活。详见[内核文档](<https://docs.kernel.org/admin-guide/pm/cpufreq.html#generic-scaling-governors>)。 

**注意：** Each governor is compatible with any scaling driver. However, the `intel_pstate` scaling driver in active mode will bypass the generic CPUFreq governors, providing its own scaling algorithms: `powersave` and `performance`. Although they share names with generic governors, their algorithms work differently: both `intel_pstate` governors provide dynamic scaling similar to the `schedutil` or `ondemand` generic governors. The `performance` algorithm [should give better power saving functionality than the old ondemand governor](<https://www.phoronix.com/scan.php?page=news_item&px=MTM3NDQ>).

调速器 | 描述   
---|---  
performance | 运行于最大频率, 数值通过 `/sys/devices/system/cpu/cpu _X_ /cpufreq/scaling_max_freq`.   
powersave | 运行于最小频率，数值值通过 `/sys/devices/system/cpu/cpu _X_ /cpufreq/scaling_min_freq` 查看。   
userspace | 运行于用户指定的频率，通过 `/sys/devices/system/cpu/cpu _X_ /cpufreq/scaling_setspeed` 配置。   
ondemand | 按需快速动态调整CPU频率， 一有cpu计算量的任务，就会立即达到最大频率运行，空闲时间增加就降低频率   
conservative | 按需快速动态调整CPU频率， 比 ondemand 的调整更保守   
schedutil | 基于调度程序调整 CPU 频率 [[4]](<https://lwn.net/Articles/682391/>), [[5]](<https://lore.kernel.org/lkml/1614814.usHvZ58O6A@vostro.rjw.lan/>).   
  
根据实际硬件，以下的调速器可能被默认启用： 

  * `powersave` ：Intel 使用 `intel_pstate` 驱动的 CPU(Sandy Bridge 和更新的CPU)。
  * `powersave` (for Linux < 5.10) or `schedutil` (since Linux 5.10) for CPUs using the `acpi_cpufreq` driver.

**警告：** 修改默认调速器时，请使用 CPU 监控工具监控温度、电压等指标。

如果需要指定特定的调速器，运行以下命令： 
    
    # cpupower frequency-set -g _governor_
    
**注意：**

  * 仅设置某一核心，请在命令的最后跟随以下参数 `-c _core_number_`。
  * 激活某一调速器，需要特定的 [内核模块](<../zh-cn/Kernel_modules.html> "Kernel modules") （名为 `cpufreq__governor_`）正确载入。在 3.4 内核上，这些模块应该已经自动加载。

也可以这样实现： 
    
    # echo _governor_ | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
    
**提示：** 如果需要实时监测 CPU 的频率，运行以下命令： 
    
     $ watch cat /sys/devices/system/cpu/cpu[0-9]*/cpufreq/scaling_cur_freq
    
###  调节 ondemand 调速器

详见[内核文档](<https://docs.kernel.org/admin-guide/pm/cpufreq.html#ondemand>)。 

####  开关阈值

设置到其他值（增加）的步长，执行以下命令： 
    
    # echo -n _percent_ > /sys/devices/system/cpu/cpufreq/_governor_ /up_threshold
    
设置到其他值（减小）的步长，执行以下命令： 
    
    # echo -n _percent_ > /sys/devices/system/cpu/cpufreq/_governor_ /down_threshold
    
####  采样率

采样率决定调速器多久进行一次检查并调整CPU频率。 设置`sampling_down_factor`大于1将通过降低负载评估的消耗，并将CPU保持在最高运行频率而提高性能。`sampling_down_factor` 的可选数值是 1 到 100000。这个可调参数对低CPU频率/负载没有效果。 

要获取这个值 (default = 1)，运行： 
    
    $ cat /sys/devices/system/cpu/cpufreq/ondemand/sampling_down_factor
    
要设置这个值，运行： 
    
    # echo -n <value> > /sys/devices/system/cpu/cpufreq/ondemand/sampling_down_factor
    
####  保存设置

要在重启后自动启用设置，通常使用[内核模式选项](<../zh-cn/Kernel_modules.html> "Kernel modules")和 [systemd#systemd-tmpfiles - temporary files](<../zh-cn/Systemd.html#systemd-tmpfiles_-_temporary_files> "Systemd")。 

例如要将 up_threshold 设置为 10: 
    
    /etc/tmpfiles.d/ondemand.conf
    
    w- /sys/devices/system/cpu/cpufreq/ondemand/up_threshold - - - - 10

如果某些特殊情况下会出现时序问题，可以使用 [udev](<../zh-cn/Udev.html> "Udev")。创建如下 udev 规则： 
    
    $ udevadm info -a /sys/devices/cpu
    
    ...
        KERNEL=="cpu"
        SUBSYSTEM=="event_source"
    ...
    
    /etc/udev/rules.d/cpu.rules
    
    KERNEL=="cpu", SUBSYSTEM=="event_source", ACTION=="add", RUN+="/bin/sh -c 'echo performance | tee /sys/devices/system/cpu/cpufreq/policy*/scaling_governor'"
    
    $ udevadm test /sys/devices/cpu
    
    ...
    Reading rules file: /usr/lib/udev/rules.d/99-systemd.rules
    Reading rules file: /etc/udev/rules.d/cpu.rules
    ...	
    
要在 _initramfs_ 中启用设置，请参考下面例子：[udev#Debug output](<../zh-cn/Udev.html#Debug_output> "Udev"). 

**提示：**

  * Since Linux 5.9, it is possible to set the `cpufreq.default_governor` kernel option.[[6]](<https://kernelnewbies.org/Linux_5.9#CPU_Frequency_scaling>)
  * Alternatively, configure the [cpupower](<#cpupower>) utility and enable its systemd service.

## Intel performance and energy bias hint

The [Intel performance and energy bias hint (EPB)](<https://docs.kernel.org/admin-guide/pm/intel_epb.html>) is an interface provided by Intel CPUs to allow for user space to specify the desired power-performance tradeoff, on a scale of 0 (highest performance) to 15 (highest energy savings). The EPB register is another layer of performance management functioning independently from frequency scaling. It influences how aggressive P-state and C-state selection will be, and informs internal model-specific decision making that affects energy consumption. 

Common values and their aliases, as recognized by sysfs and x86_energy_perf_policy are: 

EPB value  | String   
---|---  
0  | performance   
4  | balance-performance   
6  | normal, default   
8  | balance-power   
15  | power   
  
### Setting via sysfs

The EPB can be set using a sysfs attribute: 
    
    # echo _epb_ | tee /sys/devices/system/cpu/cpu*/power/energy_perf_bias
    
### Setting via x86_energy_perf_policy

With [x86_energy_perf_policy](<https://archlinux.org/packages/?name=x86_energy_perf_policy>)包: 
    
    # x86_energy_perf_policy _epb_
    
### Setting via cpupower

With [cpupower](<https://archlinux.org/packages/?name=cpupower>)包: 
    
    # cpupower set -b _epb_value_
    
**警告：** cpupower does not support the string aliases. If given a string, it will silently set the EPB to 0, corresponding to max performance.

##  与 ACPI 事件交互

用户可以把调速器配置为基于不同的ACPI事件自动切换的形式。例如接入外接电源，或是合上屏幕时。以下是一个简明的例子，但可能有必须通读一遍文章[acpid](<../zh-cn/Acpid.html> "Acpid"). 

事件是在`/etc/acpi/handler.sh`中定义的。如果[acpid](<https://archlinux.org/packages/?name=acpid>)包软件包已经安装，这个文件应该已经存在并且设置为可执行。例如，当外接电源拔除时将调速器从`performance`改为`conservative`，而当电源再次接入时将它改回来： 
    
    /etc/acpi/handler.sh
    
    [...]
    
     ac_adapter)
         case "$2" in
             AC*)
                 case "$4" in
                     00000000)
                         echo "conservative" >/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor    
                         echo -n $minspeed >$setspeed
                         #/etc/laptop-mode/laptop-mode start
                     ;;
                     00000001)
                         echo "performance" >/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
                         echo -n $maxspeed >$setspeed
                         #/etc/laptop-mode/laptop-mode stop
                     ;;
                 esac
             ;;
             *) logger "ACPI action undefined: $2" ;;
         esac
     ;;
    
    [...]
    
##  疑难解答

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Unverifiable and vague statements, lots of "some"s and "maybe"s. Troubleshooting items need to address concrete problems.（在 [Talk:CPU 调频](<../zh-cn/Talk:CPU_%E8%B0%83%E9%A2%91.html>) 中讨论）

  * 一些应用程序，如[ntop](</wzh/index.php?title=Ntop&action=edit&redlink=1> "Ntop（页面不存在）")，对自动频率调整不能很好地响应。在ntop的案例中它可能导致分段错误和大量信息丢失，因为在大量网络数据包突然到达被监控的网络接口时，`on-demand`调速器不能迅速反应，以致当前处理速度满足不了处理这些数据包所需的速度。

  * 一些CPU在默认的`on-demand`调速器配置下可能受到比较严重的性能损失（例如flash视频不能平滑地播放，或窗口动画停顿）。为了解决这些问题，完全禁用掉频率调整不如采取更积极的措施——降低每个CPU的 _up_threshold_ [sysctl](<../zh-cn/Sysctl.html> "Sysctl")变量值。阅读[#调节 ondemand 调速器](<#%E8%B0%83%E8%8A%82_ondemand_%E8%B0%83%E9%80%9F%E5%99%A8>)章节以获得更多信息。

  * 有时on-demand调速器可能达不到最高频率而只能达到次级频率。这个问题可以通过把max_freq值设置得稍微高于最大频率的方式来解决。例如，如果CPU的频率范围是2.00 GHz到3.00 GHz，把max_freq设置为3.01 GHz就是一个不错的主意。

  * [ALSA](<../zh-cn/ALSA.html> "ALSA")驱动和有些声音芯片配合工作时，可能导致在调速器改变频率时声音跳跃。改回non-changing调速器应该能够解决这个问题。

###  BIOS频率限制

一些CPU/BIOS配置可能导致达不到最高频率或根本无法调高频率。这很可能是因为BIOS告诉操作系统限制频率，结果在`/sys/devices/system/cpu/cpu0/cpufreq/bios_limit`中设置了一个过低的值。 

这种情况下需要在BIOS设置中修改指定的配置（频率，发热管理等）。这通常是由于有问题的/过旧的BIOS导致，也可能BIOS有特别的原因要求必须这样。 

可能的原因有（假设你的机器是一台笔记本）电池被移除（或快要完全损坏），所以你只能用外接电源。这种情况下如果电源适配器提供的电能太弱，就会满足不了整个系统在峰值所需的电能，而且又没有电池辅助供电，就可能导致数据丢失，数据损坏或最坏的情况下损坏硬件！ 

不是所有的BIOS都会在这种情况下限制CPU频率，但如IBM/联想 Thinkpad就会。参考thinkwiki以获取更多信息[thinkpad related info on this topic](<https://www.thinkwiki.org/wiki/Problem_with_CPU_frequency_scaling>). 

如果你检查后发现并没有不正确的BIOS设置，而且你也十分清楚自己在做什么以及可能导致的结果，你还可以选择让内核忽略BIOS限制。 

**警告：** 请确保你读了并且完全明白上面一节内容。CPU频率限制是你BIOS的一个安全特性，通常情况下你不应该越过它。

一个特殊的参数需要传递给处理器模块。 

临时尝试这办法时可以修改`/sys/module/processor/parameters/ignore_ppc`值从`0`到`1`。 

要固化这个修改请参考[Kernel module](<../zh-cn/Kernel_module.html#Manual_module_handling> "Kernel module")或继续阅读本文。 添加`processor.ignore_ppc=1`到内核启动参数或创建 
    
    /etc/modprobe.d/ignore_ppc.conf
    
    # 如果你的机器受到错误的BIOS频率限制，这应该会有帮助
    options processor ignore_ppc=1

##  参阅

  * [Linux CPUFreq - kernel documentation](<https://docs.kernel.org/cpu-freq/index.html>)
  * [Reddit post talking about pstate](<https://www.reddit.com/r/linux/comments/1hdogn/acpi_cpufreq_or_intel_pstates/>)
  * [Processor boosting control](<https://docs.kernel.org/admin-guide/pm/cpufreq.html#frequency-boost-support>)
  * [intel_pstate kernel documentation](<https://docs.kernel.org/admin-guide/pm/intel_pstate.html>)
  * [amd-pstate kernel documentation](<https://docs.kernel.org/admin-guide/pm/amd-pstate.html>)
  * [intel_pstate/intel_cpufreq documentation kernel 5.7+](<https://linrunner.de/tlp/settings/processor.html>)
