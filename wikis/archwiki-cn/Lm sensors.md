相关文章

  * [风扇转速控制](<../zh-cn/%E9%A3%8E%E6%89%87%E8%BD%AC%E9%80%9F%E6%8E%A7%E5%88%B6.html> "风扇转速控制")
  * [hddtemp](<../zh-cn/Hddtemp.html> "Hddtemp")
  * [I2C](</wzh/index.php?title=I2C&action=edit&redlink=1> "I2C（页面不存在）")
  * [monitorix](</wzh/index.php?title=Monitorix&action=edit&redlink=1> "Monitorix（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [Lm sensors](<https://wiki.archlinux.org/title/Lm_sensors> "arch:Lm sensors")，最近一次同步于 2023-8-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lm_sensors?diff=0&oldid=786188>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lm_sensors_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[lm_sensors](<https://hwmon.wiki.kernel.org/lm_sensors>)（Linux monitoring sensors，Linux 监控传感器）是一个免费的开源应用程序，提供用于监控温度、电压和风扇的工具和驱动程序。本文档介绍如何安装、配置和使用 lm_sensors。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [lm_sensors](<https://archlinux.org/packages/?name=lm_sensors>)包 包。 

**注意：** 更多文档请访问 [GitHub 存储库](<https://github.com/groeck/lm-sensors/tree/master/doc>)。以后可能会安装这些，见 [FS#48354](<https://bugs.archlinux.org/task/48354>)。

##  配置

在 root 下使用 _sensors-detect_ 来检测并生成内核模块列表： 

**警告：** 不要使用默认选项以外的任何选项（只需点击 `Enter`），除非您确切地知道自己在做什么。见[#Laptop screen issues after running sensors-detect.](<#Laptop_screen_issues_after_running_sensors-detect.>)。
    
    # sensors-detect
    
它将询问探测各种硬件。默认答案是“safe（安全）”，因此只需对所有问题点击 `Enter` 通常不会造成任何问题。这将创建 `/etc/conf.d/lm_sensors` 配置文件，该文件由 `lm_sensors.service` 用于在启动时自动加载内核模块。 

检测完成后，将对探测进行总结。 

示例： 
    
    # sensors-detect
    
    This program will help you determine which kernel modules you need
    to load to use lm_sensors most effectively. It is generally safe
    and recommended to accept the default answers to all questions,
    unless you know what you're doing.
    
    Some south bridges, CPUs or memory controllers contain embedded sensors.
    Do you want to scan for them? This is totally safe. (YES/no): 
    Module cpuid loaded successfully.
    Silicon Integrated Systems SIS5595...                       No
    VIA VT82C686 Integrated Sensors...                          No
    VIA VT8231 Integrated Sensors...                            No
    AMD K8 thermal sensors...                                   No
    AMD Family 10h thermal sensors...                           No
    
    ...
    
    Now follows a summary of the probes I have just done.
    Just press ENTER to continue: 
    
    Driver `coretemp':
      * Chip `Intel digital thermal sensor' (confidence: 9)
    
    Driver `lm90':
      * Bus `SMBus nForce2 adapter at 4d00'
        Busdriver `i2c_nforce2', I2C address 0x4c
        Chip `Winbond W83L771AWG/ASG' (confidence: 6)
    
    Do you want to overwrite /etc/conf.d/lm_sensors? (YES/no): 
    ln -s '/usr/lib/systemd/system/lm_sensors.service' '/etc/systemd/system/multi-user.target.wants/lm_sensors.service'
    Unloading i2c-dev... OK
    Unloading cpuid... OK
    
**注意：** 当被问及即将生成 `/etc/conf.d/lm_sensors` 时，如果用户回答 **YES** ，则会自动启用 systemd 服务。回答 **YES** 也会自动启动该服务。

##  运行传感器

示例运行 `sensors`： 
    
    $ sensors
    
    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:       +35.0°C  (crit = +105.0°C)
    Core 1:       +32.0°C  (crit = +105.0°C)
    
    w83l771-i2c-0-4c
    Adapter: SMBus nForce2 adapter at 4d00
    temp1:        +28.0°C  (low  = -40.0°C, high = +70.0°C)
                           (crit = +85.0°C, hyst = +75.0°C)
    temp2:        +37.4°C  (low  = -40.0°C, high = +70.0°C)
                           (crit = +110.0°C, hyst = +100.0°C)
    
###  添加双列直插内存模块（DIMM）温度传感器

要查找 DIMM 的温度传感器，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [i2c-tools](<https://archlinux.org/packages/?name=i2c-tools>)包 包。安装后，加载 `i2c-dev` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。 
    
    # modprobe i2c_dev
    
要显示所有列，[在 root 下](<../zh-cn/%E5%BB%BA%E8%AE%AE%E9%98%85%E8%AF%BB.html#%E5%AE%89%E5%85%A8> "建议阅读")使用 _i2cdetect_ ： 
    
    # i2cdetect -l
    
    i2c-2	smbus     	SMBus PIIX4 adapter port 2 at 0b00	SMBus adapter
    i2c-2	smbus     	SMBus PIIX4 adapter port 1 at 0b20	SMBus adapter
    i2c-0	smbus     	SMBus PIIX4 adapter port 0 at 0b00	SMBus adapter

否则，其输出将显示如下： 
    
    i2c-2	unknown    	SMBus PIIX4 adapter port 2 at 0b00	N/A
    i2c-2	unknown    	SMBus PIIX4 adapter port 1 at 0b20	N/A
    i2c-0	unknown    	SMBus PIIX4 adapter port 0 at 0b00	N/A
    
在以下示例中，内存棒连接到总线 `SMBus 0`。 _i2cdetect_ 命令将显示连接到总线的设备。`-y **0**` 参数使用 `i2c-**0**` smbus。如果需要，检查其他总线。 
    
    # i2cdetect -y 0
    
    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- 0c -- -- -- 
    10: 10 -- -- -- -- -- -- -- 18 19 -- -- -- -- -- -- 
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- 36 -- -- -- -- -- -- -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 4f 
    50: 50 51 -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    70: -- -- -- -- -- -- -- 77

RAM SPD（ _s_ erial _p_ resence _d_ etect，串行存在检查）从同一总线上的地址 `0x50` 开始，RAM 温度传感器从 `0x18` 开始。在本例中，有2个 DIMM 可用。地址 `0x18` 和 `0x19` 是 DIMM 温度传感器。 

为了读取内存棒的温度，我们需要加载 `jc42` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。您需要告诉模块要使用哪些地址。此过程包括将 `_模块名_` 和 `_地址_` 写入 `_smbus_path_`。例如： 
    
    # modprobe jc42
    # echo jc42 0x18 > /sys/bus/i2c/devices/i2c-0/new_device
    # echo jc42 0x19 > /sys/bus/i2c/devices/i2c-0/new_device
    
之后，您的内存棒温度将可见： 
    
    $ sensors
    
    jc42-i2c-0-19
    Adapter: SMBus PIIX4 adapter port 0 at 0b00
    temp1:        +50.7°C  (low  =  +0.0°C)                  ALARM (HIGH, CRIT)
                           (high =  +0.0°C, hyst =  +0.0°C)
                           (crit =  +0.0°C, hyst =  +0.0°C)
    
    jc42-i2c-0-18
    Adapter: SMBus PIIX4 adapter port 0 at 0b00
    temp1:        +51.8°C  (low  =  +0.0°C)                  ALARM (HIGH, CRIT)
                           (high =  +0.0°C, hyst =  +0.0°C)
                           (crit =  +0.0°C, hyst =  +0.0°C)

###  从内存模块读取电涌保护器（SPD）值（可选）

要从内存模块中读取 SPD 计时值，请安装 [i2c-tools](<https://archlinux.org/packages/?name=i2c-tools>)包 包。安装后，加载 `at24` 或 `eeprom` （已弃用）[内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。 
    
    # modprobe at24
    
最后，使用 `decode-dimms` 查看内存信息。 

这里是一台机器的部分输出： 
    
    # decode-dimms
    
    Memory Serial Presence Detect Decoder
    By Philip Edelbrock, Christian Zuckschwerdt, Burkart Lingner,
    Jean Delvare, Trent Piepho and others
    
    Decoding EEPROM: /sys/bus/i2c/drivers/eeprom/0-0050
    Guessing DIMM is in                             bank 1
    
    ---=== SPD EEPROM Information ===---
    EEPROM CRC of bytes 0-116                       OK (0x583F)
    # of bytes written to SDRAM EEPROM              176
    Total number of bytes in EEPROM                 512
    Fundamental Memory type                         DDR3 SDRAM
    Module Type                                     UDIMM
    
    ---=== Memory Characteristics ===---
    Fine time base                                  2.500 ps
    Medium time base                                0.125 ns
    Maximum module speed                            1066MHz (PC3-8533)
    Size                                            2048 MB
    Banks x Rows x Columns x Bits                   8 x 14 x 10 x 64
    Ranks                                           2
    SDRAM Device Width                              8 bits
    tCL-tRCD-tRP-tRAS                               7-7-7-33
    Supported CAS Latencies (tCL)                   8T, 7T, 6T, 5T
    
    ---=== Timing Parameters ===---
    Minimum Write Recovery time (tWR)               15.000 ns
    Minimum Row Active to Row Active Delay (tRRD)   7.500 ns
    Minimum Active to Auto-Refresh Delay (tRC)      49.500 ns
    Minimum Recovery Delay (tRFC)                   110.000 ns
    Minimum Write to Read CMD Delay (tWTR)          7.500 ns
    Minimum Read to Pre-charge CMD Delay (tRTP)     7.500 ns
    Minimum Four Activate Window Delay (tFAW)       30.000 ns
    
    ---=== Optional Features ===---
    Operable voltages                               1.5V
    RZQ/6 supported?                                Yes
    RZQ/7 supported?                                Yes
    DLL-Off Mode supported?                         No
    Operating temperature range                     0-85C
    Refresh Rate in extended temp range             1X
    Auto Self-Refresh?                              Yes
    On-Die Thermal Sensor readout?                  No
    Partial Array Self-Refresh?                     No
    Thermal Sensor Accuracy                         Not implemented
    SDRAM Device Type                               Standard Monolithic
    
    ---=== Physical Characteristics ===---
    Module Height (mm)                              15
    Module Thickness (mm)                           1 front, 1 back
    Module Width (mm)                               133.5
    Module Reference Card                           B
    
    ---=== Manufacturer Data ===---
    Module Manufacturer                             Invalid
    Manufacturing Location Code                     0x02
    Part Number                                     OCZ3G1600LV2G     
    
    ...
    
##  使用传感器数据

###  图形前端

传感器数据有多种前端。 

  * **psensor** — GTK 应用程序，用于监测硬件传感器，包括温度和风扇速度。监控主板和 CPU（使用 lm-sensors）、Nvidia GPU（使用 XNVCtrl）和硬盘（使用 [hddtemp](<../zh-cn/Hddtemp.html> "Hddtemp") 或 libatasmart）。

     <https://wpitchoune.net/psensor/> || [psensor](<https://archlinux.org/packages/?name=psensor>)包

  * **xsensors** — lm-sensors 的 X11 界面。

     <https://github.com/Mystro256/xsensors> || [xsensors](<https://archlinux.org/packages/?name=xsensors>)包

  * **Netdata** — 基于 Web 的系统监视器（[netdata](</wzh/index.php?title=Netdata&action=edit&redlink=1> "Netdata（页面不存在）")）。

     <https://github.com/netdata/netdata> || [netdata](<https://archlinux.org/packages/?name=netdata>)包

  * **CoolerControl** — 监测和控制冷却设备的程序。

     <https://gitlab.com/coolercontrol/coolercontrol> || [coolercontrol](<https://aur.archlinux.org/packages/coolercontrol/>)AUR

特定于[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")的： 

  * **Freon (GNOME Shell extension)** — 用于在 [GNOME](<../zh-cn/GNOME.html> "GNOME") Shell 中显示 CPU 温度、磁盘温度、显卡温度、电压和风扇转速的扩展。

     <https://github.com/UshakovVasilii/gnome-shell-extension-freon> || [gnome-shell-extension-freon](<https://aur.archlinux.org/packages/gnome-shell-extension-freon/>)AUR

  * **GNOME Sensors Applet** — [GNOME](<../zh-cn/GNOME.html> "GNOME") 面板的小程序，用于显示硬件传感器的读数，包括 CPU 温度、风扇速度和电压读数。

     <http://sensors-applet.sourceforge.net/> || [sensors-applet](<https://archlinux.org/packages/?name=sensors-applet>)包

  * **lm-sensors (LXPanel plugin)** — 通过 lm-sensors 监测 [LXDE](<../zh-cn/LXDE.html> "LXDE") 中的温度/电压/风扇速度。

     <https://danamlund.dk/sensors_lxpanel_plugin/> || [sensors-lxpanel-plugin](<https://aur.archlinux.org/packages/sensors-lxpanel-plugin/>)AUR

  * **MATE Sensors Applet** — 在 [MATE](<../zh-cn/MATE.html> "MATE") 面板中显示硬件传感器的读数。

     <https://github.com/mate-desktop/mate-sensors-applet> || [mate-sensors-applet](<https://archlinux.org/packages/?name=mate-sensors-applet>)包

  * **Sensors (Xfce4 panel plugin)** — [Xfce](<../zh-cn/Xfce.html> "Xfce") 面板的硬件传感器插件

     <https://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin> || [xfce4-sensors-plugin](<https://archlinux.org/packages/?name=xfce4-sensors-plugin>)包

  * **Thermal Monitor (Plasma 5 applet)** — 用于监控 CPU、GPU 和其他可用温度传感器的 [KDE](<../zh-cn/KDE.html> "KDE") Plasma 小程序。

     <https://gitlab.com/agurenko/plasma-applet-thermal-monitor> || [plasma5-applets-thermal-monitor](<https://archlinux.org/packages/?name=plasma5-applets-thermal-monitor>)包

### sensord

有一个名为 _sensord_ 的可选守护程序（包含在 [lm_sensors](<https://archlinux.org/packages/?name=lm_sensors>)包 包中），它可以将数据记录到轮询数据库（round robin database，rrd）中，然后以图形方式进行可视化。有关详细信息，请参阅 [sensord(8)](<https://man.archlinux.org/man/sensord.8>) 手册页。 

##  提示和技巧

###  调整数值

在某些情况下，显示的数据可能不正确，或者用户可能希望重命名输出。用例包括： 

  * 由于错误的偏移导致温度值不正确（即报告的温度比实际温度高 20°C）。
  * 用户希望重命名某些传感器的输出。
  * 核心可能以不正确的顺序显示。

以上所有用例（以及更多用例）都可以通过重写包来进行调整。通过创建 `/etc/sensors.d/_foo_` ，包提供了 `/etc/sensors3.conf` 中的设置，其中任何数量的调整都将重写默认值。建议将 'foo' 重命名为主板品牌和型号，但此命名法是可选的。 

多个主板的自定义配置文件可以在 lm-sensors 包的 [configs](<https://github.com/lm-sensors/lm-sensors/tree/master/configs>) 目录中找到，并用作模板。 

**注意：** 不要直接编辑 `/etc/sensors3.conf`，因为包更新将覆盖任何更改，从而丢失这些更改。

####  示例 1. 调整温度偏移

这是 Zotac ION-ITX-A-U 主板上的一个真实例子。将堆芯温度值降低了20°C（过高），并根据英特尔规格进行了调整。 
    
    $ sensors
    
    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:       +57.0°C  (crit = +125.0°C)
    Core 1:       +55.0°C  (crit = +125.0°C)
    ...
    
使用 `-u` 开关来运行 `sensors`，以查看每个物理芯片有哪些可用选项（原始模式）。如果您看到的一些原始标签似乎是不可配置的，请查看 `/sys/class/hwmon` 目录树。这里提到的每个设备都有一个 `name` 文件，可以用来匹配它引用的设备。然后尝试该目录引用的标签。 
    
    $ sensors -u
    
    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:
      temp2_input: 57.000
      temp2_crit: 125.000
      temp2_crit_alarm: 0.000
    Core 1:
      temp3_input: 55.000
      temp3_crit: 125.000
      temp3_crit_alarm: 0.000
    ...
    
创建以下文件以覆盖默认值： 
    
    /etc/sensors.d/Zotac-IONITX-A-U
    
    chip "coretemp-isa-0000"
      label temp2 "Core 0"
      compute temp2 @-20,@-20
    
      label temp3 "Core 1"
      compute temp3 @-20,@-20
    
现在调用 `sensors` 显示调整后的值： 
    
    $ sensors
    
    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:       +37.0°C  (crit = +105.0°C)
    Core 1:       +35.0°C  (crit = +105.0°C)
    ...
    
####  示例 2. 重命名标签

这是华硕 A7M266 上的一个真实例子。用户希望温度标签`temp1` 和 `temp2`的名称更加详细： 
    
    $ sensors
    
    as99127f-i2c-0-2d
    Adapter: SMBus Via Pro adapter at e800
    ...
    temp1:        +35.0°C  (high =  +0.0°C, hyst = -128.0°C)
    temp2:        +47.5°C  (high = +100.0°C, hyst = +75.0°C)
    ...
    
创建以下文件以覆盖默认值： 
    
    /etc/sensors.d/Asus_A7M266
    
    chip "as99127f-*"
      label temp1 "Mobo Temp"
      label temp2 "CPU0 Temp"
    
现在调用 `sensors` 显示调整后的值： 
    
    $ sensors
    
    as99127f-i2c-0-2d
    Adapter: SMBus Via Pro adapter at e800
    ...
    Mobo Temp:        +35.0°C  (high =  +0.0°C, hyst = -128.0°C)
    CPU0 Temp:        +47.5°C  (high = +100.0°C, hyst = +75.0°C)
    ...
    
####  示例 3. 多 CPU 系统的核心重新编号

这是带有双至强 CPU 的惠普 Z600 工作站上的一个真实例子。物理核心的实际编号不正确：编号为 0、1、9、10，重复到第二个 CPU 中。大多数用户希望堆芯温度按顺序报告，即 0,1,2,3,4,5,6,7。 
    
    $ sensors
    
    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:       +65.0°C  (high = +85.0°C, crit = +95.0°C)
    Core 1:       +65.0°C  (high = +85.0°C, crit = +95.0°C)
    Core 9:       +66.0°C  (high = +85.0°C, crit = +95.0°C)
    Core 10:      +66.0°C  (high = +85.0°C, crit = +95.0°C)
    
    coretemp-isa-0004
    Adapter: ISA adapter
    Core 0:       +54.0°C  (high = +85.0°C, crit = +95.0°C)
    Core 1:       +56.0°C  (high = +85.0°C, crit = +95.0°C)
    Core 9:       +60.0°C  (high = +85.0°C, crit = +95.0°C)
    Core 10:      +61.0°C  (high = +85.0°C, crit = +95.0°C)
    ...
    
同样，使用 `-u` 开关来运行 `sensors`，以查看每个物理芯片有哪些可用选项： 
    
    $ sensors -u coretemp-isa-0000
    
    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:
      temp2_input: 61.000
      temp2_max: 85.000
      temp2_crit: 95.000
      temp2_crit_alarm: 0.000
    Core 1:
      temp3_input: 61.000
      temp3_max: 85.000
      temp3_crit: 95.000
      temp3_crit_alarm: 0.000
    Core 9:
      temp11_input: 62.000
      temp11_max: 85.000
      temp11_crit: 95.000
    Core 10:
      temp12_input: 63.000
      temp12_max: 85.000
      temp12_crit: 95.000
    
    $ sensors -u coretemp-isa-0004
    
    coretemp-isa-0004
    Adapter: ISA adapter
    Core 0:
      temp2_input: 53.000
      temp2_max: 85.000
      temp2_crit: 95.000
      temp2_crit_alarm: 0.000
    Core 1:
      temp3_input: 54.000
      temp3_max: 85.000
      temp3_crit: 95.000
      temp3_crit_alarm: 0.000
    Core 9:
      temp11_input: 59.000
      temp11_max: 85.000
      temp11_crit: 95.000
    Core 10:
      temp12_input: 59.000
      temp12_max: 85.000
      temp12_crit: 95.000
    ...
    
创建以下文件以覆盖默认值： 
    
    /etc/sensors.d/HP_Z600
    
    chip "coretemp-isa-0000"
      label temp2 "Core 0"
      label temp3 "Core 1"
      label temp11 "Core 2"
      label temp12 "Core 3"
    
    chip "coretemp-isa-0004"
      label temp2 "Core 4"
      label temp3 "Core 5"
      label temp11 "Core 6"
      label temp12 "Core 7"

现在调用 `sensors` 显示调整后的值： 
    
    $ sensors
    
    coretemp-isa-0000
    Adapter: ISA adapter
    Core0:        +64.0°C  (high = +85.0°C, crit = +95.0°C)
    Core1:        +63.0°C  (high = +85.0°C, crit = +95.0°C)
    Core2:        +65.0°C  (high = +85.0°C, crit = +95.0°C)
    Core3:        +66.0°C  (high = +85.0°C, crit = +95.0°C)
    
    coretemp-isa-0004
    Adapter: ISA adapter
    Core4:        +53.0°C  (high = +85.0°C, crit = +95.0°C)
    Core5:        +54.0°C  (high = +85.0°C, crit = +95.0°C)
    Core6:        +59.0°C  (high = +85.0°C, crit = +95.0°C)
    Core7:        +60.0°C  (high = +85.0°C, crit = +95.0°C)
    ...
    
###  自动化 lm_sensors 部署

希望在多台机器上部署 lm_sensors 的用户可以使用以下命令接受所有问题的默认设置： 
    
    # sensors-detect --auto
    
###  S.M.A.R.T. 驱动器温度

[从内核 5.6 开始](<https://hwmon.wiki.kernel.org/device_support_status>) `drivetemp` 模块将通过硬件监控系统报告 SATA/SAS 温度，但 `sensors-detect` 无法自动检测到这一点，因此该模块必须[手动加载](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E6%89%8B%E5%8A%A8%E5%8A%A0%E8%BD%BD%E6%A8%A1%E5%9D%97> "内核模块")。 
    
    # modprobe drivetemp
    
现在，您应该在 `sensors` 的输出中看到类似的条目： 
    
    sensors
    
    drivetemp-scsi-1-0
    Adapter: SCSI adapter
    temp1:        +33.0°C 
    
    drivetemp-scsi-2-0
    Adapter: SCSI adapter
    temp1:        +32.0°C  (low  =  +0.0°C, high = +70.0°C)
                           (crit low =  +0.0°C, crit = +70.0°C)
                           (lowest = +29.0°C, highest = +41.0°C)

您现在可以[在启动时加载模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E8%87%AA%E5%8A%A8%E5%8A%A0%E8%BD%BD%E6%A8%A1%E5%9D%97> "内核模块")。或者，手动将其添加到 `/etc/conf.d/lm-sensors` 的 `HWMON_MODULES` 行中。请注意，当 `sensors-detect` 被允许再次写入此文件时，它将不会自动添加。 

###  持久化设备名称

许多软件都希望在 `/sys/class/hwmon/hwmonX` 中找到传感器设备，但通常情况下，提供 hwmon 接口的设备超过 1-2 个的系统上就无法在 `/sys/class/hwmon/hwmonX` 中正常找到传感器设备了。软件可能应该解析 `hwmon?/name` 或使用 lmsensors 库，但遗憾的是，它们通常不会。一些软件（例如 [Monitorix](</wzh/index.php?title=Monitorix&action=edit&redlink=1> "Monitorix（页面不存在）")（英语：[Monitorix](<https://wiki.archlinux.org/title/Monitorix> "en:Monitorix")） 或它的某些模块，即 amdgpu）期望在其他地方使用持久名称。 

因此，以下类型的 udev 规则可能是有用的。并不是所有的软件都能使用它们（例如，KDE 系统监视器 - 不幸的是，这使得这些软件在许多系统上几乎毫无用处）。在许多情况下，只需在 udev 规则中匹配 hwmon 子系统和合适的名称就足够了，但并不总是如此！有关编写规则的更多信息，请参阅 [Udev](<../zh-cn/Udev.html> "Udev") 页面。 

不能在 `/sys` 层次下重命名或符号链接。 `SYMLINK+=` -语句也将不起作用。因此，我们需要使用 `RUN+=` 语句（注意，符号链接不必要像本例中那样位于 `/dev` 之下 - 既没有标准，也没有合适的位置）。 
    
    /udev/rules.d/99-persistent-hwmon-names
    
    # 我的主板传感器芯片：
    ACTION=="add", SUBSYSTEM=="hwmon", ATTRS{name}=="nct6687", RUN+="/bin/sh -c 'ln -s /sys$devpath /dev/nct6678'"
    # 提供传感器的 USB 设备:
    ACTION=="add", SUBSYSTEM=="hwmon", ATTRS{name}=="corsaircpro", RUN+="/bin/sh -c 'ln -s /sys$devpath /dev/corsaircpro'"
    # 我的 GPU：
    ACTION=="add", SUBSYSTEM=="hwmon", ATTRS{vendor}=="0x1002", ATTRS{device}=="0x73bf", RUN+="/bin/sh -c 'ln -s /sys$devpath /dev/rx6900xt'"
    
##  疑难解答

###  K10Temp 模块

一些 K10 处理器的温度传感器存在问题。有关更多信息，请参见[k10temp文档](<https://docs.kernel.org/hwmon/k10temp.html#description>)。 

在受影响的机器上，模块将报告“不可靠的 CPU 热传感器；监控已禁用（unreliable CPU thermal sensor; monitoring disabled）”。要强制监控，您可以运行以下命令： 
    
    # rmmod k10temp
    # modprobe k10temp force=1
    
确认传感器实际上是有效和可靠的。如果是，可以编辑 `/etc/modprobe.d/k10temp.conf` 并添加： 
    
    options k10temp force=1
    
这将允许模块在引导时加载。 

###  华硕 B450M-A/A320M-K/A320M-K-BR 主板

自2020年11月，这些主板使用的是不受 it87 内核驱动支持的 IT8655E 芯片 [[1]](<https://docs.kernel.org/hwmon/it87.html>)。不过，内核驱动的上游版本 [[2]](<https://github.com/bbqlinux/it87/blob/master/it87.c#L22>) 支持它。[DKMS](<../zh-cn/DKMS.html> "DKMS") 变体包含在 [it87-dkms-git](<https://aur.archlinux.org/packages/it87-dkms-git/>)AUR 中。 

###  使用 AM4 插槽的华硕 B450/X399/X470 主板

某些新近的华硕主板使用 ITE IT8665E 芯片，访问温度，风扇和电压传感器可能需要 `asus-wmi-sensors` 模块。从 5.17 开始它成为了主线内核的一部分：加载使用了 UEFI 接口的 `asus-wmi-sensors` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")，可能需要在某些主板上进行 BIOS 更新 [[3]](<https://github.com/electrified/asus-wmi-sensors#supported-hardware>)。 

或者，`it87` 模块直接从芯片读取值，安装 [it87-dkms-git](<https://aur.archlinux.org/packages/it87-dkms-git/>)AUR 并加载 `it87` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。 

###  华硕 H97/Z97/Z170/Z370i/X570/B550 主板

对于某些新近的华硕主板，风扇和电压传感器访问可能需要加载 `nct6775` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。 

你还可能需要添加以下[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")： 
    
    acpi_enforce_resources=lax
    
更多信息见 [https://bugzilla.kernel.org/show_bug.cgi?id=204807。](<https://bugzilla.kernel.org/show_bug.cgi?id=204807%E3%80%82>)

**注意：** 从内核 5.16 开始 [[4]](<https://bugzilla.kernel.org/show_bug.cgi?id=204807#c199>)，对于大多数主板来说，不再需要上述内核参数，应该避免使用。

###  华擎 Deskmini H470

Deskmini H470 的 STX 主板使用 NCT6683 芯片，为了访问温度、风扇和电压传感器，需要加载 `nct6683` 模块。 

为了获得 `nct6683` 模块的正确值，请创建一个模块配置文件： 
    
    /etc/modprobe.d/nct6683.conf
    
    options nct6683 force=1 
    
###  技嘉 B250/Z370/B450M/B560M/B660M/Z690 主板

自2019年5月，一些技嘉主板使用 ITE IT8686E, ITE8689 (用于 B560 and B660M) 或 ITE8689E (用于 Z690) 芯片，it87 内核驱动不支持这些芯片 [[5]](<https://docs.kernel.org/hwmon/it87.html>)。不过，内核驱动的上游版本 [[6]](<https://github.com/bbqlinux/it87/blob/master/it87.c#L24>) 支持它。[DKMS](<../zh-cn/DKMS.html> "DKMS") 变体包含在 [it87-dkms-git](<https://aur.archlinux.org/packages/it87-dkms-git/>)AUR 中。与 [#华硕 H97/Z97/Z170/Z370i/X570/B550 主板](<#%E5%8D%8E%E7%A1%95_H97/Z97/Z170/Z370i/X570/B550_%E4%B8%BB%E6%9D%BF>)一样，在尝试安装模块之前需要[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")： 
    
    acpi_enforce_resources=lax
    
此外，在加载模块时提供芯片的 id，如下所示： 
    
    # modprobe it87 force_id=0x8686
    或
    # modprobe it87 force_id=0x8689  # for B560
    # modprobe it87 force_id=0x8628  # for Z690
    
或者你可以在启动过程中通过创建以下两个文件[加载模块](<../zh-cn/Kernel_modules.html> "Kernel modules")： 
    
    /etc/modules-load.d/it87.conf
    
    it87
    
对于 Z690 
    
    /etc/modprobe.d/it87.conf
    
    options it87 force_id=0x8628
    
对于其它的 
    
    /etc/modprobe.d/it87.conf
    
    options it87 ignore_resource_conflict=1
    
一旦模块被加载，您就可以使用 _sensors_ 工具来探测芯片。 

现在，您还可以使用[风扇转速控制](<../zh-cn/%E9%A3%8E%E6%89%87%E8%BD%AC%E9%80%9F%E6%8E%A7%E5%88%B6.html> "风扇转速控制")来控制机箱风扇的转速级数。 

可选地,安装 [zenpower3-dkms](<https://aur.archlinux.org/packages/zenpower3-dkms/>)AUR 可以允许对主板的冷却系统进行更大的微调。不过，它会禁用默认的 k10temp 模块。 

###  技嘉 GA-J1900N-D3V

该主板使用 ITE IT8620E 芯片（也可用于读取电压、主板温度和风扇速度）。自2014年10月，lm_sensors 不支持芯片 ITE IT8620E 的驱动程序 [[7]](<https://hwmon.wiki.kernel.org/device_support_status_g_i>) [[8]](<https://marc.info/?l=lm-sensors&m=139496833404519>)。lm_sensors 的开发人员报告称，该芯片与用于硬件监控的 IT8728F 部分兼容。然而，自2016年8月，[[9]](<https://docs.kernel.org/hwmon/it87.html>) 列出了支持的 IT8620E。 

你以在运行时使用 modprobe 加载模块： 
    
    $ modprobe it87 force_id=0x8728
    
或者你可以在启动过程中通过创建以下两个文件[加载模块](<../zh-cn/Kernel_modules.html> "Kernel modules")： 
    
    /etc/modules-load.d/it87.conf
    
    it87
    
    /etc/modprobe.d/it87.conf
    
    options it87 force_id=0x8603

一旦模块被加载，您就可以使用 _sensors_ 工具来探测芯片。 

现在，您还可以使用[风扇转速控制](<../zh-cn/%E9%A3%8E%E6%89%87%E8%BD%AC%E9%80%9F%E6%8E%A7%E5%88%B6.html> "风扇转速控制")来控制机箱风扇的转速级数。 

###  运行 sensors-detect 后笔记本电脑出现屏幕问题

这是由于 lm-sensors 在探测传感器时干扰了屏幕的 Vcom 值造成的。论坛上已经讨论并解决了这个问题： <https://bbs.archlinux.org/viewtopic.php?id=193048> 。不过，在运行任何建议的命令之前，请确保仔细阅读帖子。 

###  在 AMD Navi 2 GPU 上的 i2c 总线错误

目前，在 AMD Navi 2 GPU 上内核处理 i2c 总线读取的方式中存在一个错误。该总线目前只能与 EEPROM 一起使用，尝试将其与其他设备一起使用会导致其故障。这可能会导致崩溃、黑屏，甚至导致显卡的异常行为，比如无法切换电源状态。如果您有基于 Navi 2 的显卡，目前建议不要扫描 i2c 总线。您可以在此处阅读更多信息： <https://gitlab.freedesktop.org/drm/amd/-/issues/1470>
