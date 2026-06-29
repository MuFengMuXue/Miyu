**翻译状态：**

  * 本文（或部分内容）译自 [Xiaomi RedmiBook Pro 15 2022 Ryzen](<https://wiki.archlinux.org/title/Xiaomi_RedmiBook_Pro_15_2022_Ryzen> "arch:Xiaomi RedmiBook Pro 15 2022 Ryzen")，最近一次同步于 2025-06-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xiaomi_RedmiBook_Pro_15_2022_Ryzen?diff=0&oldid=838407>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xiaomi_RedmiBook_Pro_15_2022_Ryzen_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

硬件 | PCI/USB ID | 是否正常工作   
---|---|---  
Touchpad | `27C6:01E0` | 是   
Keyboard |  | 是   
GPU (AMD) | `1002:1681` | 是   
Wireless | `10ec:b852` | 是   
Bluetooth | `0cb8:c559` | 是   
Webcam | `2b7e:b557` | 是   
Audio | `1002:1640` | 是   
SD-card reader | `10ec:525a` | 是   
Fingerprint reader | `27c6:589a` | Untested   
  
This laptop has two variants, one with dedicated NVIDIA graphics and one without. 

## Installation

See [#Firmware](<#Firmware>). 

## Accessibility

The appearance of the UEFI is pretty simple and not very colorful, so it might work well with OCR software. 

**注意：** Blind users should request the help of a sighted person to change UEFI settings

## Firmware

This UEFI setup interface has very limited options available. You can disable/enable [Secure Boot](<../zh-cn/Secure_Boot.html> "Secure Boot"), set/unset password, change the size of shared VRAM, change boot order, or change the date/time. But that is about what all you can do in it. Pressing `F12` during booting to select the boot device. 

**注意：** This device does not have a BIOS speaker.

[fwupd](<../zh-cn/Fwupd.html> "Fwupd") does not support this device yet. 

### Secure Boot

在启动画面按 `F2` 键进入 UEFI 设置界面，按如下方式禁用[UEFI/安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "UEFI/安全启动")。 

  * 安全 → 设置密码，设置一个临时的密码
  * 安全 → 禁用安全启动
  * 再次设置密码，但在提示新密码时可以使用空白密码，这样即可以在不使用密码的同时禁用安全启动。

##  话筒检测问题

此笔记本使用了深蕾科技(SenaryTech) SN6140 声卡芯片。外部话筒插入 3.5mm 接口时，有可能没有被检测到。 

它只会在插入的耳麦(4段式 TRRS 插头)的话筒阻抗较小时发生。比如我的安克声阔 (Anker Soundcore) Q35 耳机自带的话筒线的阻抗大约为 1000Ω，而我的其他两个耳机的阻抗约为 2000Ω。 这很可能芯片在探测插入的是四段式 OMTP/CTIA (俗称诺基亚/苹果式或国标/美标) 耳麦还是普通的3段式耳机时存在 bug。由于耳机喇叭的阻抗一般都比话筒的小得多，声卡可能依靠探测它们的阻抗来区分二者，但是遇到阻抗较小的话筒时就将它判断错误了。 

明白了这个原因，你就可以从下面几种方法里面选择一种来解决或绕过这个问题了。（或者换一个其他的话筒） 

###  改变阻抗

改变话筒的阻抗就可以使它被识别到，例如将它串联一个合适阻值的电阻。当然这需要你手动更改电路的能力。 

###  使用 `hda-verb` 命令来重新配置声卡芯片

使用这种方法，你可以正常地插入耳麦，也不需要手动改变电路。然而，我不知道这些命令实际上都对声卡做了什么事情，请确保自己足够自信和勇于冒险再尝试。 

安装 [alsa-tools](<https://archlinux.org/packages/?name=alsa-tools>)包。 

**警告：** 所有这些命令都是我根据这两行源码 <https://github.com/torvalds/linux/blob/f7301f856d351f068f807d0a3d442b85b2c6a01d/sound/pci/hda/patch_conexant.c#L173> 和自己的实验得出的，因为我找不到 SN6140 或相近型号的芯片的数据手册或文档。

首先，检查和保存你的(大概是)[话筒偏置电流检查阈值寄存器](<https://github.com/torvalds/linux/blob/master/sound/pci/hda/patch_conexant.c#L173>)的初始值。这里 `/dev/snd/hwC1D0` 是我的设备路径，`0xb20` 是查询动词 (hda verb)，对应于设置动词 `0x320` 的。`0` 是无用但必须写出的参数。 
    
    # hda-verb /dev/snd/hwC1D0 0x1c 0xb20 0
    nid = 0x1c, verb = 0xb20, param = 0x0
    value = 0x10
    
这里 `0x10` 就是阈值寄存器的初始值。现在我们来更改一下： 
    
    # hda-verb /dev/snd/hwC1D0 0x1c 0x320 0x08
    
这句命令将改寄存器设置为 `0x08`。在我的系统上它大约使检测阈值降低了500Ω，你的效果可能略有区别。你也可以其他可能有用的值例如 `0x0`、`0x18`、`0x20` 或 `0x30`。它们似乎有不同的改变阈值的功效，但我完全不明白为什么这样会有用。 

使用这些值你的话筒应该就可以正常识别和使用了。它似乎在重启后仍然有效，甚至重启到 Windows 后似乎仍然有效（可以在那边修复同样的问题）。如果你感到长期使用被更改的值不太舒服，也可以在使话筒用完毕后将它复原到初始值： 
    
    # hda-verb /dev/snd/hwC1D0 0x1c 0x320 0x10
    
如果你的初始值不同，可将 `0x10` 换成你保存的初始值。 

###  使用两段式插入法

在插入耳麦的插头时，请缓慢插入并盯着音频输入设备的列表看（比如 KDE 的声音设置界面）。如果你在某个特定位置暂停，就可以看到它正确识别到了话筒，然后你就可以继续插入，话筒就可以正常使用了。这种方法避免了运行未知命令可能带来的后果，但是需要每次插入时都使用这样的奇怪插入方法。 

## Fingerprint reader

The fingerprint reader requires a proprietary driver from [an unknown third-party](<https://github.com/vrolife/modern_laptop/tree/main/drivers/fingerprint>). The author explains that "The driver is developed with an internal async framework, which is not well-prepared to be open-sourced. So only the binary is released for the time being." 

##  增加内置键盘映射的键码

默认情况下，键盘右上角的小爱键没有映射。如果你想把它映射为 Insert 键，可以安装[redmibook-hwdb-git](<https://aur.archlinux.org/packages/redmibook-hwdb-git/>)AUR来使用[一个自定义的硬件数据库规则补丁](<https://github.com/oldherl/redmibook-hwdb>)。 

回车键和右 Ctrl 键的修正已经进入 [systemd](<https://archlinux.org/packages/?name=systemd>)包 v257-rc1 及后续版本，无需另外配置。 

##  另见

  * 一个第三方仓库，提供了一些 Redmibook 的 Linux 支持: <https://github.com/vrolife/modern_laptop/>
  * 小米网站上的驱动下载 (仅限 Windows 系统): <https://www.mi.com/service/notebook/drivers/A39S>
  * 此笔记本的一个 [Hardware probe](<../zh-cn/Hardware_probe.html> "Hardware probe")，注意它的蓝牙/无线网卡和 SSD 都被用户替换掉了。<https://linux-hardware.org/?probe=3428364c49>
