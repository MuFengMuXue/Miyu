**翻译状态：**

  * 本文（或部分内容）译自 [Howdy](<https://wiki.archlinux.org/title/Howdy> "arch:Howdy")，最近一次同步于 2023-11-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Howdy?diff=0&oldid=786460>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Howdy_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Howdy](<https://github.com/boltgolt/howdy>) 是 Linux 上一个类似 Windows Hello，通过电脑的红外传感器识别人脸，解锁电脑的程序。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [howdy-git](<https://aur.archlinux.org/packages/howdy-git/>)AUR 软件包。或者您也可以从[archlinuxcn](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Archlinuxcn")仓库安装[howdy](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/howdy>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")([howdy](<https://archlinux.org/packages/?name=howdy>)包已无法在最新的archlinux上正常使用，因此推荐安装[howdy-git](<https://aur.archlinux.org/packages/howdy-git/>)AUR)。 

**注意：** 在该软件包的使用过程中会从 GitHub 的 raw 服务器下载文件，而中国大陆用户连接该服务器网络不通畅，请确保你的网络能正常连接。

##  配置

###  把 Howdy 设置为当需要时才使用

为了让 Howdy 能够对用户进行身份验证，您需要在使用了 Howdy 的 [PAM](<../zh-cn/PAM.html> "PAM") 配置文件中做一些小改动。请把以下内容添加到对应的配置文件中： 
    
    auth sufficient pam_python.so /lib/security/howdy/pam.py
    
注意：当使用 Howdy 3.0.0 BETA 及以上版本时([howdy-git](<https://aur.archlinux.org/packages/howdy-git/>)AUR)，这一行应该为： 
    
    auth sufficient /lib/security/pam_howdy.so
    
为 `howdy/pam.py` (或 `pam_howdy.so`) 添加 _sufficient_ 的控制标记后，将只提示进行人脸身份验证。如果您无法中断（`Ctrl+C`）面部识别过程（比如在解锁屏幕和Polkit验证窗口中），那您将无法使用密码进行验证。想要既能人脸识别，又能用密码验证，请把以下内容添加到 `/etc/pam.d/` 下对应的 PAM 配置文件的**最顶部** 。 
    
    auth sufficient pam_unix.so try_first_pass likeauth nullok
    
###  添加正确的红外传感器

可以在诸如 [cheese](<https://archlinux.org/packages/?name=cheese>)包、[fswebcam](<https://aur.archlinux.org/packages/fswebcam/>)AUR 或者 [v4l-utils](<https://archlinux.org/packages/?name=v4l-utils>)包 的程序里找到并确定能连接到红外传感器的正确 `/dev/videoX` 文件， 

以内置于 [v4l-utils](<https://archlinux.org/packages/?name=v4l-utils>)包 软件包的工具为例： 
    
    $ v4l2-ctl --list-devices
    Integrated_Webcam_HD: Integrate (usb-0000:00:14.0-11):
            /dev/video0
            /dev/video1
    
    EyeChip: Tobii Video (usb-0000:00:14.0-3.4.3):
            /dev/video4
            /dev/video5
    
    HD Webcam C525 (usb-0000:00:14.0-3.4.4):
            /dev/video2
            /dev/video3
    
在上述例子中，有不止一个网络摄像头，而且每一个摄像头都有好几个不同的 `/dev/videoX` 路径，一般来说选第一或第二个路径会比较好。 

如果摄像头或红外传感器不止一个，使用 `/dev/videoX` 可能会随着时间的推移而变得不稳定，因为它们的路径可能会随着某些设备的拆卸和装入而改变。这时可以用由 Video 4 Linux[wikipedia:Video4Linux](<https://en.wikipedia.org/wiki/Video4Linux> "wikipedia:Video4Linux") 提供的，更加稳定的 `/dev/v4l/by-id/` 路径。 
    
    $ ls -l /dev/v4l/by-id
    total 0
    lrwxrwxrwx 1 root root 12 Dec  3 15:01 usb-046d_HD_Webcam_C525_BE4703F0-video-index0 -> ../../video2
    lrwxrwxrwx 1 root root 12 Dec  3 15:01 usb-046d_HD_Webcam_C525_BE4703F0-video-index1 -> ../../video3
    lrwxrwxrwx 1 root root 12 Dec  3 14:47 usb-CNFGH19N306021000582_Integrated_Webcam_HD-video-index0 -> ../../video0
    lrwxrwxrwx 1 root root 12 Dec  3 14:47 usb-CNFGH19N306021000582_Integrated_Webcam_HD-video-index1 -> ../../video1
    lrwxrwxrwx 1 root root 12 Dec  3 14:47 usb-Tobii_Technology_AB_EyeChip_IS404-100109244721-video-index0 -> ../../video4
    lrwxrwxrwx 1 root root 12 Dec  3 14:47 usb-Tobii_Technology_AB_EyeChip_IS404-100109244721-video-index1 -> ../../video5
    
先验证这些 `v4l` 路径不随设备的拆卸和装入而改变，然后重列设备目录（re-listing the directory）。 

找到正确的文件名后，您就可以用自己喜欢的编辑器编辑 `/lib/security/howdy/config.ini` 文件，也可以以 root 用户权限使用 `howdy config` 命令来编辑。 

设定 `EDITOR` 变量来自定义 `howdy config` 使用的编辑器： 
    
    # EDITOR=_editor_ howdy config
    
###  向 Howdy 添加面部数据

要想添加面部模型，运行 `sudo howdy add`。 

###  加固 Howdy

有些版本的 Howdy 会在识别用户时拍照，然后保存到 `/lib/security/howdy/snapshots`。这某种程度来说是一个安全漏洞。攻击者能够轻易找到某次成功登录的照片并用它来冒充您进行登录，从而达到提权的目的。当然，攻击者还可以使用目标用户的任何其他照片，但是 Howdy 简化了该过程。 

为了避免这样的攻击，以及突然发现磁盘空间骤减，可以在 `/lib/security/howdy/config.ini` 中取消拍照： 
    
    [snapshots]
    save_failed = false
    save_successful = false
    
##  疑难杂症

###  红外发射器不工作

已启用红外摄像头而红外发射器不工作，没准是因为你选错了文件。打个比方，可能 `/dev/video0` 和 `/dev/video2` 都能识别你的脸部，但是只有 `/dev/video2` 会启用红外发射器，所以要试试所有的 `/dev/video _X_` 路径，看看有没有哪个能正常工作。 

如果还不行，试着跟从 [linux-enable-ir-emitter](<https://github.com/EmixamPP/linux-enable-ir-emitter>) 的指导启用红外发射器。 

**注意：** 由于上游代码的原因，[linux-able-ir-emitter](<https://aur.archlinux.org/packages/linux-able-ir-emitter/>)AUR包的最新版本通过在安装完成后会运行自己的脚本来生成 Systemd 服务文件。这种行为可能不是您想要的，因为它的自定义脚本会修改文件系统根目录。目前已知在版本 `3.2.0-2` 之前，该软件包都带有 Systemd 服务文件，所以您可能需要选择适合自己的版本。

###  测试红外摄像头

提前确认红外摄像头能正常运作是个挺不错的主意，用 [gstreamer](<https://archlinux.org/packages/?name=gstreamer>)包 软件包的以下命令十连拍来测试设备（别忘了用你的红外摄像机的位置替代下面的 `_IR camera_` ）： 
    
    gst-launch-1.0 v4l2src device=_IR camera_ num-buffers=10 ! image/jpeg ! multifilesink location="frame-%02d.jpg"
    
###  Howdy 无法正常运转

用 root 权限运行 `howdy test` 来确保 Howdy 正常工作，如果看起来一切正常，就检查 PAM 配置并确认其正在工作。例如 SDDM [[1]](<https://github.com/sddm/sddm/issues/284>) 的某些程序不能在 PAM 下正常工作，会造成一些出乎意料的结果。 

如果您安装的是2.x版本，您也可以尝试使用beta版本[howdy-beta-git](<https://aur.archlinux.org/packages/howdy-beta-git/>)AUR，参见[[2]](<https://github.com/boltgolt/howdy/issues/795>)[[3]](<https://zhuanlan.zhihu.com/p/662513757>)。 

###  输入设备识别错误

例如 Thinkpad T480 的某些红外传感器需要在配置文件中定义框架高度和宽度： 
    
    frame_width = 400
    frame_height = 400

获取传感器输出的高度和宽度： `v4l2-ctl --list-devices --all`
