**翻译状态：**

  * 本文（或部分内容）译自 [fprint](<https://wiki.archlinux.org/title/fprint> "arch:fprint")，最近一次同步于 2025-08-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/fprint?diff=0&oldid=845532>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/fprint_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[fprint](<https://fprint.freedesktop.org/>) 旨在填补开源桌面环境在生物特征认证方面的空白，尤其是通过为指纹扫描仪提供标准支持来增强安全性。该项目的核心是 **libefprint** 库，它作为一个中间件层，为指纹识别硬件提供统一的接口，让各个桌面环境和应用软件能够便捷地利用指纹识别功能。 

该项目是在一些支持内置指纹识别器的笔记本中使用 PAM 登录。此教程还将介绍如何使用常规密码作为备用登录的方法（由于某些原因，不建议仅使用指纹模块进行验证登录）。 

##  使用前提

**注意：** 兼容设备列表并没有定期更新，也不完整。在使用[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")软件包之前，即使设备没有出现在该兼容清单列表中，仍然可以尝试使用本页教程测试指纹识别设备是否可用。

通过查看[兼容设备清单](<https://fprint.freedesktop.org/supported-devices.html>)和[不兼容设备清单](<https://gitlab.freedesktop.org/libfprint/wiki/-/wikis/Unsupported-Devices>)来确定是否支持指纹识别设备。 使用下面命令检测是否识别指纹设备信息: 
    
    $ lsusb
    
命令 _lsusb_ 在软件包[usbutils](<https://archlinux.org/packages/?name=usbutils>)包中提供。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [fprintd](<https://archlinux.org/packages/?name=fprintd>)包 软件包。 可能也需要软件包[imagemagick](<https://archlinux.org/packages/?name=imagemagick>)包. 

某些设备需要使用 [libfprint](<https://archlinux.org/packages/?name=libfprint>)包 的分支版本，但这些分支目前还没有合并到上游 _libfprint_ ,清单如下： 

  * **libfprint-tod** — 用于基于传感器的设备。

     <https://gitlab.freedesktop.org/3v1n0/libfprint/-/tree/tod> || [libfprint-tod-git](<https://aur.archlinux.org/packages/libfprint-tod-git/>)AUR

  * **libfprint-elanmoc2** — 用于ELAN `04f3:0c4c`,其版本在等待[合并](<https://gitlab.freedesktop.org/Depau/libfprint/-/merge_requests/1>)中。

     <https://gitlab.freedesktop.org/Depau/libfprint/-/tree/elanmoc2> || [libfprint-elanmoc2-git](<https://aur.archlinux.org/packages/libfprint-elanmoc2-git/>)AUR

  * **libfprint-elanmoc2-newdrvs** — 针对`04f3:0c4c`或`04f3:0c00`**实验性** 的功能，其版本也在等待[合并](<https://gitlab.freedesktop.org/geodic/libfprint/-/tree/elanmoc2>)。

     <https://gitlab.freedesktop.org/geodic/libfprint/-/tree/elanmoc2> || [libfprint-elanmoc2-newdrvs-git](<https://aur.archlinux.org/packages/libfprint-elanmoc2-newdrvs-git/>)AUR

清单并非包含所有，更完整的分支清单需在[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中查找。 

##  配置

###  登录配置

**注意：**

  * 如果桌面管理器为 [GDM](<../zh-cn/GDM.html> "GDM") ，指纹选项已经在账户的登录菜单中可用（请将用户加入到 `input` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84> "用户和用户组") 中）。可以跳过此章节！
  * 如果桌面管理器为 [SDDM](<../zh-cn/SDDM.html> "SDDM"), 请查看 [使用指纹识别器](<../zh-cn/SDDM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E4%BD%BF%E7%94%A8%E6%8C%87%E7%BA%B9%E8%AF%86%E5%88%AB%E5%99%A8> "SDDM \(简体中文\)")。

将`pam_fprintd.so`模块添加在`/etc/pam.d/system-local-login`文件 auth 字段的开头位置。 
    
    /etc/pam.d/system-local-login
    
    **auth      sufficient pam_fprintd.so**
    auth      include   system-login
    ...
    
这里首先会尝试使用指纹认证登录，如果验证失败或找不到用户指纹数据，则进行密码认证登录。 

**警告：** 此设置是su和sudo的安全漏洞，因为它允许后台进程在不提示用户的情况下获取权限。请参阅：[CVE-2024-37408](<https://nvd.nist.gov/vuln/detail/cve-2024-37408>)

将此项放在`auth fully pam_fprintd.so`之前，以便在指纹无法显示提示时使用sudo/su禁止指纹。 
    
    # 不允许在没有tty的情况下在sudo/su中使用指纹
    
    auth       [success=1 default=ignore]  pam_succeed_if.so    service in sudo:su:su-l tty in :unknown
    
也可以用相同的方式修改 `/etc/pam.d/{login,su,sudo,gdm,lightdm}` 中的其他文件， 如 `/etc/pam.d/polkit-1` 用于基于 [polkit](<../zh-cn/Polkit.html> "Polkit") 身份验证（GNOME和其他桌面环境）。如果 `/etc/pam.d/polkit-1` 不存在，请从`/usr/lib/pam.d/polkit-1`复制。 

KDE已经在`/etc/pam.d/KDE fingerprint`中配置了指纹身份验证，因此不需要编辑该文件。对于最低限度的工作设置，它首先要求您的指纹，如果在KDE Plasma上失败，则需要密码验证，只需将以下行更改为`/etc/pam.d/system-auth`即可： 
    
    -auth      [success=**3** default=ignore]   pam_systemd_home.so
    **auth       [success=2 default=ignore]   pam_fprintd.so**
    auth       [success=1 default=bad]     pam_unix.so          try_first_pass nullok
    
当完成录入指纹后，如果将 `pam_fprintd.so` 以 _sufficient_ 作为条件添加到 `/etc/pam.d/` 中的配置文件中时，只会进行指纹身份验证，此时因无法按 `Ctrl+c` 中断指纹身份验证（由于缺少shell环境），导致无法使用密码进行认证。如果想在图形界面中使用密码或指纹认证其中一项完成认证，请在相关文件的开头位置添加下列内容： 
    
    **auth		sufficient  	pam_unix.so try_first_pass likeauth nullok**
    auth		sufficient  	pam_fprintd.so
    ...
    
这里首先会提示输入密码，如果在空白字段上按 `Enter` 将跳过密码认证，继续进行指纹认证。 

如果需要同时使用输入指纹和密码，可以使用 [pam-fprint-grosshack](<https://aur.archlinux.org/packages/pam-fprint-grosshack/>)AUR。对于某些不允许空白密码输入的图形程序，例如 Gnome 的内置 polkit 代理，可能需要这样做。若要使用此包，请将以下行添加到所需任何文件的开头位置： 
    
    **auth		sufficient  	pam_fprintd_grosshack.so**
    **auth		sufficient  	pam_unix.so try_first_pass nullok**
    ...
    
###  录入指纹

需要运行 [Polkit 身份认证组件](<../zh-cn/Polkit.html#%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81%E7%BB%84%E4%BB%B6> "Polkit")才能录入。 

开始录入指纹，请运行： 
    
    $ fprintd-enroll
    
或为所有手指录入指纹： 
    
    $ fprintd-delete "$USER"
    $ for finger in {left,right}thumb,{index,middle,ring,littlefinger}; do fprintd-enroll -f "$finger" "$USER"; done
    
运行后将要求扫描给定的手指。用右手食指滑动“五次”。之后，在 `/var/lib/fprint/` 中创建指纹数据。 

也可以直接指定用户录入指纹： 
    
    # fprintd-enroll _user_
    
###  验证指纹

如果您需要验证录入的指纹能否正确识别，请运行以下命令： 
    
    $ fprintd-verify
    
###  删除指纹

如果不满意已录入的指纹数据，可以使用下面命令进行删除，例如需要删除左手拇指指纹数据： 
    
    $ fprintd-delete -f _left-thumb_
    
有关更多信息，请参阅 [fprintd(1)](<https://man.archlinux.org/man/fprintd.1>). 

###  限制用户录入指纹

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[polkit_(简体中文)](</wzh/index.php?title=Polkit_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Polkit \(简体中文\)（页面不存在）")。**

**附注：** 部分内容重复（在 [Talk:Fprint](<../zh-cn/Talk:Fprint.html>) 中讨论）

默认情况下，允许每个用户注册新指纹，而无需提示输入密码或指纹。可以使用 [polkit](<../zh-cn/Polkit.html> "Polkit") 规则更改此行为。 

有两个位置包含 polkit 配置文件 

  * `/etc/polkit-1/rules.d/`
  * `/usr/share/polkit-1/rules.d/`

**注意：****不推荐** 直接修改 `/usr/share/polkit-1/rules.d/` 目录下的文件，因为该目录下的文件在程序更新时将会被覆盖，应该复制文件到 `/etc/polkit-1/rules.d/` 目录。

在以下示例中，只有 root 可以录入指纹： 
    
    /etc/polkit-1/rules.d/50-net.reactivated.fprint.device.enroll.rules
    
    polkit.addRule(function (action, subject) {
      if (action.id == "net.reactivated.fprint.device.enroll") {
        return subject.user == "root" ? polkit.Result.YES : polkit.Result.NO
      }
    })

##  故障排除

###  指纹设备无法使用

如果在[兼容设备清单](<https://fprint.freedesktop.org/supported-devices.html>)没有找到您的设备, 请通过[journalctl](<../zh-cn/Systemd/Journal.html> "Systemd/Journal")查看`fprintd.service`的日志信息。 

可能会可能到如下日志条目： 
    
    fprintd[2936592]: Corrupted message received
    fprintd[2936592]: Ignoring device due to initialization error: unsupported firmware version
    
这时请确保设备的固件是最新的 [Fwupd](<../zh-cn/Fwupd.html> "Fwupd")。 

###  系统休眠后gdm在显示登录提示时挂起

这个问题在[libfprint](<https://gitlab.freedesktop.org/libfprint/libfprint/-/issues/426>)仓库中有描述。开发人员的答案是: 

    我现在的猜测是，我们正在断开USB蓝牙设备的连接，而它正在初始化。然后，当蓝牙usb设备试图加载固件时，一切都被卡住了（这有一个10秒的超时，解释了我们看到的不到10秒的挂起）。像这样断开USB蓝牙设备的连接预计会在rfkill开关切换时发生，所以这是正常的。只是设备突然断开连接的情况似乎没有得到正确处理并超时。

建议的修复方案是将禁用该驱动模块，添加内核模块配置文件： 
    
    /etc/modprobe.d/bluetooth-blacklist.conf
    
    blacklist btusb

或者直接执行： 
    
    # rmmod btusb
    
完成上面操作后，系统将不会尝试初始化该设备。 

###  挂起设备时出现意外错误

这个问题在[libfprint](<https://gitlab.freedesktop.org/libfprint/libfprint/-/issues/538>)仓库中有描述： 

    Set your laptop to not suspend to RAM but to do s2idle. You might need to switch the BIOS into "Windows mode"。

BIOS中设置成"Windows mode" 

###  指纹认证在polkit代理不工作

如果在录入指纹的时候提示类似下面信息： 
    
    Using device /net/reactivated/Fprint/Device/0
    Enrolling right-index-finger finger.
    EnrollStart failed: GDBus.Error:net.reactivated.Fprint.Error.PermissionDenied: Not Authorized:
    net.reactivated.fprint.device.enroll
    
这是因为[polkit](<../zh-cn/Polkit.html> "Polkit")策略的限制，可以尝试在`/usr/share/polkit-1/rules.d/`添加一条策略`reactivated.fprint.device.verify.rules`，以下实例中允许`users`用户组可以使用指纹识别器： 
    
    /etc/polkit-1/rules.d/reactivated.fprint.device.verify.rules
    
    polkit.addRule(function (action, subject) {
      if (action.id == "net.reactivated.fprint.device.enroll"
        && subject.isInGroup("users")) {
        return polkit.Result.YES
      }
    })

###  调试模式

使用下面环境变量来获取运行时详细日志。 
    
    # G_MESSAGES_DEBUG=all /usr/lib/fprintd -t
    
###  fprintd在从睡眠唤醒前启动

创建并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")一个fprintd.service 守护进程，将 `3-3` 替换成实际指纹Bus ID，可通过命令 `lsusb -t` 获取。 
    
    /etc/systemd/system/fingerprint.service
    
    [Unit]
    Description=Kill fprintd before sleep
    Before=sleep.target
    
    [Service]
    ExecStart=killall fprintd
    
    [Install]
    WantedBy=sleep.target

###  能录入指纹却无法验证

某些指纹识别设备扫描的图像太小，数据不足以支撑 fprint 正常工作。一种常见的解决方法是滑动而不是触摸传感器，但生成好图像的速度可能会有所不同。有些设备需要较慢的滑动速度，有些则需要较快的滑动速度。好的图像示例请参考github[[1]](<#cite_note-1>)。 

如果想练习不同速度以查看哪种速度生成更好的图像，请尝试使用脚本examples/img-capture[[2]](<#cite_note-2>)来导出图像，并与上面的示例进行比较（需要从源代码编译libfprint）。 

相关讨论见gitlab[[3]](<#cite_note-3>)。 

###  用户无法录入指纹

如果运行报错 

`EnrollStart failed: GDBus.Error:net.reactivated.Fprint.Error.PermissionDenied: Not Authorized: net.reactivated.fprint.device.enroll`

最简单的方式是用root身份执行该命令： 

`sudo fprintd-enroll "$(whoami)"`

这里需要提供用户，否则该指纹将会录入到root账户上。 

如果录入指纹时提示 "enroll-duplicate" 的报错，则表明该手指指纹已被注册到其他用户了。要么更换其他手指，要么使用`fprintd delete`从用户中删除该指纹。 

##  参见

  1. [↑](<#cite_ref-1>) <https://github.com/iafilatov/libfprint?tab=readme-ov-file>
  2. [↑](<#cite_ref-2>) <https://gitlab.freedesktop.org/libfprint/libfprint/-/blob/master/examples/img-capture.c>
  3. [↑](<#cite_ref-3>) <https://gitlab.freedesktop.org/libfprint/libfprint/-/issues/174>
