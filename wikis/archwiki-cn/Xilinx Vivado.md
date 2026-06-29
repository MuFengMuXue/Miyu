[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Xilinx Vivado](<../zh-cn/Talk:Xilinx_Vivado.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Xilinx_Vivado](<https://wiki.archlinux.org/title/Xilinx_Vivado> "arch:Xilinx Vivado")，最近一次同步于 2021-05-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xilinx_Vivado?diff=0&oldid=561915>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xilinx_Vivado_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Some content is not translated, appears abandoned.（在 [Talk:Xilinx Vivado#](<../zh-cn/Talk:Xilinx_Vivado.html>) 中讨论）

Arch Linux 并不受 Vivado 的正式支持，但是从 [Xilinx ISE WebPACK](</wzh/index.php?title=Xilinx_ISE_WebPACK&action=edit&redlink=1> "Xilinx ISE WebPACK（页面不存在）") 的使用体验上看，只需要一点修改便能正常使用所有功能。 

##  安装

可以从官方网址[[1]](<https://www.xilinx.com/products/design-tools/vivado.html>)下载Xilinx Vivado。我们建议您下载“Vivado HLx <year>.<version>: All OS installer Single-File Download”。别心急，因为这个文件(写作时最新版本为2020.3)有将近50GB。 

###  AUR包

[vivado](<https://aur.archlinux.org/packages/vivado/>)AUR [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 包可以由[pacman](<../zh-cn/Pacman.html> "Pacman")管理安装. 由于vivado安装程序需要登录后提交个人信息才能下载，因此需要像上面那样手动下载，并将其放置在与 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 相同的目录中. 该软件包只构建最新的主要版本(< 年份 >.< 版本 >) , 而不是较小的更新(< 年份 >.< 版本 >.<更新版本> ) 。如果需要，请手动安装 Vivado。 

###  手动安装

####  依赖

安装程序需要 ncurses5 库，并且不能使用官方仓库里的 ncurses6。您可以通过安装 [Arch User Repository](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 中的 [ncurses5-compat-libs](<https://aur.archlinux.org/packages/ncurses5-compat-libs/>)AUR 来解决这个问题。您可能需要安装 [libpng12](<https://archlinux.org/packages/?name=libpng12>)包 与 [lib32-libpng12](<https://archlinux.org/packages/?name=lib32-libpng12>)包 以便使用 Xilinx Document Navigator。 

SDK 2018.3（以及其他可能的版本）需要 gtk2 库。如果您打算使用 SDK，您可能需要安装 [gtk2](<https://archlinux.org/packages/?name=gtk2>)包.Vitis需要安装 [xorg-xlsclients](<https://archlinux.org/packages/?name=xorg-xlsclients>)包 来正常工作. 

可以使用[xilinx-vivado-dummy](<https://aur.archlinux.org/packages/xilinx-vivado-dummy/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 进行替代安装所有这些依赖项。 

在一些平铺式窗口管理器上 (例如 [dwm](<../zh-cn/Dwm.html> "Dwm") 和 [Xmonad](<../zh-cn/Xmonad.html> "Xmonad")), 您可能需要在启动 `xsetup` 之前设置这个环境变量(否则安装 GUI 将不呈现). 
    
    $ export _JAVA_AWT_WM_NONREPARENTING=1
    
您必须安装主程序包，并且还建议安装最新的更新补丁。 

默认的字体可能难以阅读，并导致一些 UI 元素被切断错误渲染。通过安装 [noto-fonts](<https://archlinux.org/packages/?name=noto-fonts>)包 来修复。 

####  PetaLinux Tools的依赖

在启动 petalinux-tools 之前，请安装: 

[git](<https://archlinux.org/packages/?name=git>)包 [diffstat](<https://archlinux.org/packages/?name=diffstat>)包 [unzip](<https://archlinux.org/packages/?name=unzip>)包 [texinfo](<https://archlinux.org/packages/?name=texinfo>)包 [python](<https://archlinux.org/packages/?name=python>)包 [chrpath](<https://archlinux.org/packages/?name=chrpath>)包 [wget](<https://archlinux.org/packages/?name=wget>)包 [xterm](<https://archlinux.org/packages/?name=xterm>)包 [sdl](<https://aur.archlinux.org/packages/sdl/>)AUR [rpcsvc-proto](<https://archlinux.org/packages/?name=rpcsvc-proto>)包 [socat](<https://archlinux.org/packages/?name=socat>)包 [cpio](<https://archlinux.org/packages/?name=cpio>)包 [inetutils](<https://archlinux.org/packages/?name=inetutils>)包 [python2](<https://archlinux.org/packages/?name=python2>)包 [net-tools](<https://archlinux.org/packages/?name=net-tools>)包 [tftp-hpa](<https://archlinux.org/packages/?name=tftp-hpa>)包 [python-virtualenv](<https://archlinux.org/packages/?name=python-virtualenv>)包 [xorg-server-xvfb](<https://archlinux.org/packages/?name=xorg-server-xvfb>)包 [bison](<https://archlinux.org/packages/?name=bison>)包 [flex](<https://archlinux.org/packages/?name=flex>)包 [gnupg](<https://archlinux.org/packages/?name=gnupg>)包 [ncurses](<https://archlinux.org/packages/?name=ncurses>)包 [autoconf](<https://archlinux.org/packages/?name=autoconf>)包 [libtool](<https://archlinux.org/packages/?name=libtool>)包 [tar](<https://archlinux.org/packages/?name=tar>)包 [gcc](<https://archlinux.org/packages/?name=gcc>)包 [sdl](<https://aur.archlinux.org/packages/sdl/>)AUR [sdl2](<https://archlinux.org/packages/?name=sdl2>)包 [glib2](<https://archlinux.org/packages/?name=glib2>)包 [screen](<https://archlinux.org/packages/?name=screen>)包 [pax](<https://archlinux.org/packages/?name=pax>)包 [pax-utils](<https://archlinux.org/packages/?name=pax-utils>)包 [libstdc++5](<https://aur.archlinux.org/packages/libstdc%2B%2B5/>)AUR [python-django](<https://archlinux.org/packages/?name=python-django>)包 [iproute2](<https://archlinux.org/packages/?name=iproute2>)包 [lib32-zlib](<https://archlinux.org/packages/?name=lib32-zlib>)包 [openssl](<https://archlinux.org/packages/?name=openssl>)包 [gawk](<https://archlinux.org/packages/?name=gawk>)包 [python-pexpect](<https://archlinux.org/packages/?name=python-pexpect>)包 [python-pip](<https://archlinux.org/packages/?name=python-pip>)包 [python-gitpython](<https://archlinux.org/packages/?name=python-gitpython>)包 [python-jinja](<https://archlinux.org/packages/?name=python-jinja>)包 [xz](<https://archlinux.org/packages/?name=xz>)包 [iputils](<https://archlinux.org/packages/?name=iputils>)包 [python-pylint](<https://archlinux.org/packages/?name=python-pylint>)包

和[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中的 

[pod2man](<https://aur.archlinux.org/packages/pod2man/>)AUR [libselinux](<https://aur.archlinux.org/packages/libselinux/>)AUR [debianutils](<https://aur.archlinux.org/packages/debianutils/>)AUR

启用 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 库 并安装[multilib-devel](<https://archlinux.org/groups/x86_64/multilib-devel/>)包组 包组 

启用 [tftp-hpa](<https://archlinux.org/packages/?name=tftp-hpa>)包
    
    $ sudo systemctl enable tftpd.service
    $ sudo systemctl start tftpd.service
    
####  Vivado 与 SDK

建议在默认位置 `/opt/Xilinx` 安装该套件，因为本页中的进一步说明将假定该套件安装在那里。 

**警告：** 2018.1及以后版本不再需要以下补丁。请直接解压后执行 xsetup 文件。

Once downloaded and unpacked the tarball, the install script must be patched to be able to properly detect the machine architecture. You can do it by going to the directory where installer is extracted and running: 
    
    $ sed -i.original 's/uname -i/uname -m/' xsetup
    
Install script will be patched and original will be backed up as `xsetup.original`, just in case you need to restore it later. Once patched, just run the script; it should work perfect and install the suite without a problem: 
    
    # ./xsetup
    
It is recommended to install the suite at the default location `/opt/Xilinx`, as further instructions in this page will assume the suite is installed there. 

####  更新补丁

**警告：** 2018.1 及以后版本不再需要以下补丁。

It is recommended to install the latest update patch, and repeat the process each time a new patch is released. Note that update patches cannot be applied to WebPACK installs. If you installed Vivado WebPACK, skip this section. 

To install the update, repeat the same hack used to install the suite. Once downloaded and unpacked, go to the directory containing the extracted tarball, patch the install script and run it: 
    
    $ sed -i.original 's/uname -i/uname -m/' xsetup
    # ./xsetup
    
####  证书

**警告：** 2018.1及以后的 Webpack 版本不再需要手动下载证书文件。

If you already have a license file, you can load it using Vivado License Manager. Unfortunately, if you want to obtain a WebPack license, further steps are needed. Vivado installs old stdc++ libraries, causing problems when spawning programs not included with Vivado Suite (like your default browser). To fix this, do the following steps: 
    
    # cd /opt/Xilinx/Vivado/2015.4/lib/lnx64.o/
    # mv libstdc++.so.6 libstdc++.so.6.orig
    # ln -s /usr/lib/libstdc++.so.6
    
Close any running Vivado Suite program, and launch license manager: 
    
    $ /opt/Xilinx/Vivado/2015.4/bin/vlm
    
If you try obtaining a WebPack license, your default browser should open, and the license should be generated normally. If Vivado License Manager fails to automatically load the generated license, download the .lic file, and manually load it. 

####  Digilent USB-JTAG 驱动

要使用来自 Vivado 的 Digilent Adept USB-JTAG 适配器(例如内置在 [ZedBoard](<https://www.zedboard.org>) 上的 JTAG 适配器) ，你需要安装 [Digilent Adept Runtime](<https://store.digilentinc.com/digilent-adept-2-download-only/>)。 

确保您已经从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装了 [fxload](<https://aur.archlinux.org/packages/fxload/>)AUR。 

要安装 Digilent Adept Runtime，建议从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装 [digilent.adept.runtime](<https://aur.archlinux.org/packages/digilent.adept.runtime/>)AUR 。 

此外，安装 [digilent.adept.utilities](<https://aur.archlinux.org/packages/digilent.adept.utilities/>)AUR 可以很好地配置你的开发板。 

####  桌面与应用程序菜单快捷方式

安装过程必须作为 root 用户运行，以便对/opt/Xilinx 进行写访问。如果需要应用程序菜单中的快捷方式，则必须将它们从根帐户移动到/usr/share。桌面快捷方式应该移动到用户桌面。 

以下命令假定只有 Xilinx 已经安装到根帐户，并且用户具有用户名. 

复制应用程序菜单快捷方式: 
    
    # mv /root/.local/share/applications/* /usr/share/applications/
    # mv /root/.local/share/desktop-directories/* /usr/share/desktop-directories/
    # mv /root/.config/menus/applications-merged/* /etc/xdg/menus/applications-merged/
    
复制桌面快捷方式: 
    
    # chown _username_ /root/Desktop/*
    # mv /root/Desktop/* /home/_username_ /Desktop/
    
####  Linux cable 驱动

以 root 权限运行以下脚本： 
    
    $ {vivado_install_dir}/data/xicom/cable_drivers/lin64/install_script/install_drivers/install_drivers
    
##  提示和技巧

###  启用屏幕缩放功能

启动 Vivado，然后按照以下方式启用屏幕缩放功能： 
    
    Tools -> Setting -> Display -> Scaling
    
###  禁用WebTalk

免费的WebPACK许可证不允许你禁用这一功能，该功能在生成比特流时将使用数据上传到赛灵思的服务器，但即使连接失败，综合仍会顺利完成。一个简单的方法是为Vivado工具设置一个无效的HTTPS代理，使其无法链接到服务器。 
    
    /opt/Xilinx/Vivado/<version>/bin/setupEnv.sh
    
    ...
    
    export HTTPS_PROXY=localhost

这个方法不会污染您的工作环境，只是在工具启动时配置的临时环境，它不会破坏其他任何东西。 

##  故障排除

### Synthesis segfaults

See <https://support.xilinx.com/s/feed/0D52E00006hpUycSAE?language=en_US>

You will need to recompile glibc (just take the PKGBUILD from the abs) with `--disable-lock-elision`. Instead of patching the system libc in /usr/lib, copy the newly compiled `libpthread-2.25.so` and `libc-2.25.so` to `/opt/Xilinx/Vivado/2016.4/ids_lite/ISE/lib/lin64` Do not forget to repeat this when glibc gets upgraded. 

### xsct segfault

xsct might crash with message: 
    
     Xilinx/SDK/2018.1/bin/xsct: line 141:  5611 Segmentation fault      (core dumped) "$RDI_BINROOT"/unwrapped/"$RDI_PLATFORM$RDI_OPT_EXT"/rlwrap -rc -f "$RDI_APPROOT"/scripts/xsdb/xsdb/cmdlist -H "$HOME"/.xsctcmdhistory "$RDI_BINROOT"/loader -exec rdi_xsct "${RDI_ARGS[@]}"
    
This is a problem with the rlwrap version bundled with vivado, probably due the lack of legacy vsyscall emulation in Arch Linux. To fix this issue either drop rlwrap altogether (losing history and autocompletion in xsct) or install [rlwrap](<https://archlinux.org/packages/?name=rlwrap>)包 from the official repo, and edit the corresponding line in the xsct startup script: 
    
    ../Xilinx/SDK/2018.1/bin/xsct
    
    # Use rlwrap to invoke XSCT
    /usr/bin/rlwrap -rc -f "$RDI_APPROOT"/scripts/xsdb/xsdb/cmdlist -H "$HOME"/.xsctcmdhistory "$RDI_BINROOT"/loader -exec rdi_xsct "${RDI_ARGS[@]}"
    # OR run xsct without rlwrap
    #"$RDI_BINROOT"/loader -exec rdi_xsct "${RDI_ARGS[@]}"

### Vivado HLS testbench error with GCC

Vivado requires an older version of glibc (2.26 as of vivado 2018.1). 

The solution proposed in [this thread](<https://forums.xilinx.com/t5/High-Level-Synthesis-HLS/Testbench-error-with-gcc/td-p/756773>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-19 ⓘ] from Xilinx forums suggests to update the fixed headers shipped by Xilinx. 

For vivado version 2016, run: 
    
     # /opt/Xilinx/Vivado_HLS/<version>/lnx64/tools/gcc/libexec/gcc/x86_64-unknown-linux-gnu/4.6.3/install-tools/mkheaders /opt/Xilinx/Vivado_HLS/<version>/lnx64/tools/gcc/
    
For vivado 2017 and newer, run: 
    
     # /opt/Xilinx/Vivado/2018.1/lnx64/tools/gcc/libexec/gcc/x86_64-unknown-linux-gnu/4.6.3/install-tools/mkheaders /opt/Xilinx/Vivado/2018.1/lnx64/tools/gcc
    
### Vivado Crashes with Wayland

If Vivado crashes and the error file contains something similar to this: 
    
    hs_err_pid*.log
    
    #
    # An unexpected error has occurred (11)
    #
    Stack:
    /opt/Xilinx/Vivado/2018.2/tps/lnx64/jre/lib/amd64/server/libjvm.so(+0x923da9) [0x7fced0c19da9]
    /opt/Xilinx/Vivado/2018.2/tps/lnx64/jre/lib/amd64/server/libjvm.so(JVM_handle_linux_signal+0xb6) [0x7fced0c203f6]
    /opt/Xilinx/Vivado/2018.2/tps/lnx64/jre/lib/amd64/server/libjvm.so(+0x9209d3) [0x7fced0c169d3]
    /usr/lib/libc.so.6(+0x368f0) [0x7fcf0ea408f0]
    /opt/Xilinx/Vivado/2018.2/tps/lnx64/jre/lib/amd64/libawt_xawt.so(+0x42028) [0x7fceb1a20028]
    /opt/Xilinx/Vivado/2018.2/tps/lnx64/jre/lib/amd64/libawt_xawt.so(+0x42288) [0x7fceb1a20288]
    /opt/Xilinx/Vivado/2018.2/tps/lnx64/jre/lib/amd64/libawt_xawt.so(Java_sun_awt_X11_XRobotPeer_getRGBPixelsImpl+0x17c) [0x7fceb1a1867c]
    [0x7fcec0cb94cf]

Switch to using Xorg instead of Wayland. The version of Java Vivado uses has compatibility problems with Wayland. 
