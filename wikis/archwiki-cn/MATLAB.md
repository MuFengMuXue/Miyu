**翻译状态：**

  * 本文（或部分内容）译自 [Matlab](<https://wiki.archlinux.org/title/Matlab> "arch:Matlab")，最近一次同步于 2020-9-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Matlab?diff=0&oldid=636207>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Matlab_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Octave](<../zh-cn/Octave.html> "Octave")
  * [Sage-mathematics](</wzh/index.php?title=Sage-mathematics&action=edit&redlink=1> "Sage-mathematics（页面不存在）")
  * [Mathematica](<../zh-cn/Mathematica.html> "Mathematica")

引自[官方网站](<https://www.mathworks.com/products/matlab/>): 

    MATLAB是数百万工程师和科学家都在使用的编程和数值计算平台，支持数据分析、算法开发和建模。

##  概览

MATLAB是MathWorks公司开发的专有软件。获取，安装和激活Matlab需要许可证。MATLAB一年发布两次新版本，发布名称由`R`,发布年份和`a`或`b`构成。从R2012b开始，只有64位Linux才可使用Matlab。Arch Linux 不受官方支持。参见[系统要求](<https://cn.mathworks.com/support/sysreq.html>)

##  安装

在安装 MATLAB 前需要获取一份完整的软件副本。对于许可证持有者，MATLAB 软件可以通过 DVD 或者 [MathWorks 网站](<https://www.mathworks.com>)获取。 除了软件本身，安装还需要一份文件安装密钥。要安装 MATLAB，你既可以通过 [matlab](<https://aur.archlinux.org/packages/matlab/>)AUR 软件包也可以直接使用 MATLAB 安装软件。通过 [matlab](<https://aur.archlinux.org/packages/matlab/>)AUR 软件包安装的优势是它可以管理依赖和某些微妙的安装过程，而直接从安装软件安装则可由普通用户安装到他们的家目录从而不需要 root 权限，并且适用于任何版本的 MATLAB ([matlab](<https://aur.archlinux.org/packages/matlab/>)AUR 软件包只适用于 MATLAB 2010b 及以后的版本). 

###  从 MATLAB 安装软件安装

MATLAB 安装软件是独立的，它不需要任何额外的依赖来静默安装。要通过图形界面安装， [Xorg](<../zh-cn/Xorg.html> "Xorg") 图形显示是必要的。 [Wayland](<../zh-cn/Wayland.html> "Wayland") 目前不受支持。安装过程由 `install` 脚本处理。你可以以 root 用户运行此脚本来安装 MATLAB 到整个系统，或者以你自己运行来仅为你安装。 

MATLAB 2016a 及更早不兼容 [ncurses](<https://archlinux.org/packages/?name=ncurses>)包 6，因此你必须安装 [ncurses5-compat-libs](<https://aur.archlinux.org/packages/ncurses5-compat-libs/>)AUR 。 要了解更多信息，查看 [#启动时出现段错误](<#%E5%90%AF%E5%8A%A8%E6%97%B6%E5%87%BA%E7%8E%B0%E6%AE%B5%E9%94%99%E8%AF%AF>)。 

在安装过程中，你会被询问是否创建符号链接。如果你选择不创建，你可以手动创建一个 `/usr/local/bin` 使得 MATALB 更容易从终端启动： 
    
    # ln -s /{MATLAB}/bin/matlab /usr/local/bin
    
或者你也可以将 MATLAB 的安装路径加入 `PATH` 环境变量。 

####  桌面入口

你可以选择创建一个 [desktop entry](</wzh/index.php?title=Desktop_entry&action=edit&redlink=1> "Desktop entry（页面不存在）")。 MATLAB 文件的 MIME 类型是 `text/x-matlab`. 

这样启动 `matlab`： 

  * `-desktop` 从而不使用终端。
  * `-nosplash` 从而取消启动画面。

要想让图标正确显示， `StartupWMClass` 需要在桌面入口中设置。要找到它，执行 `xprop | grep WM_CLASS` 然后选择 MATLAB 窗口 

桌面入口示例 (将 **R2019a** 替换为你的 MATLAB 版本): 
    
    /usr/share/applications/matlab.desktop
    
    [Desktop Entry]
    Version=**R2019a**
    Type=Application
    Terminal=false
    MimeType=text/x-matlab
    Exec=/usr/local/MATLAB/**R2019a** /bin/matlab -desktop
    Name=MATLAB
    Icon=matlab
    Categories=Development;Math;Science
    Comment=Scientific computing environment
    StartupNotify=true

若需设置环境变量，可以在 `Exec` 中预先准备 `env`。例如, 到系统的 libfreetype: 
    
    Exec=env LD_PRELOAD=/usr/lib/libfreetype.so.6 matlab
    
你可能想要使用系统的 `libstdc++`. 

###  从 AUR 软件包安装

专用 MATLAB 软件的EULA是有限制的。[matlab](<https://aur.archlinux.org/packages/matlab/>)AUR 被设计成使 MATLAB 和 Arch 集成。 该软件包应当在目标系统上被编译，并且应当在安装后删除该软件包和 [Pacman](<../zh-cn/Pacman.html> "Pacman") 缓存。分发该软件包显然违反了EULA。 

[matlab](<https://aur.archlinux.org/packages/matlab/>)AUR 默认安装最新版的64位 MATLAB。也可以安装更旧的版本，例如 [matlab-r2015b](<https://aur.archlinux.org/packages/matlab-r2015b/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]。[matlab](<https://aur.archlinux.org/packages/matlab/>)AUR 需要在它的安装路径中有 MATLAB 安装软件和文件密钥。 要想从 AUR 安装 MATLAB， 从 AUR 下载 PKGBUILD。下载包含 MATLAB 安装器的 zip 文件，然后执行以下命令来下载必要文件： 
    
    bsdtar xC matlab -f matlab_R2019a_glnxa64.zip
    ./matlab/install
    
确保勾选你需要的所有工具包，然后等待下载。不要关闭安装窗口。你可以这样找到下载位置： 
    
    sudo find /tmp -name "tmw*"
    
or 
    
    cd /tmp
    ls | grep tmw
    
将下载文件合并到安装器： 
    
    rsync -a /tmp/tmwXXXXXXXX/archives matlab
    
然后打包： 
    
    tar -cvf matlab.tar -C matlab/ .
    
下载 .lic 文件：访问[你的 Mathworks 账户](<https://mathworks.com/mwaccount/>)并点击你想要使用的许可证号。前往 Install and Activate 标签，选择 "Activate to Retrieve License File"。按照指导下载许可证文件并将将其命名为 `matlab.lic`。另，会显示文件安装密钥 (FIK) -把它复制粘贴进一个空文件，命名为 `matlab.fik`. 

把以上文件复制进包含 PKGBUILD 文件的路径。然后修改 PKGBUILD 来安装你需要的工具包，开始安装： 
    
    makepkg -sri
    
要了解更多细节，参考 PKGBUILD 文件 

##  配置

### Java

The MATLAB software is bundled with a JVM and therefore it is not necessary to install [Java](<../zh-cn/Java.html> "Java"). The JVM version supported by MATLAB is listed in [System Requirements & Platform Availability](<https://ww2.mathworks.cn/support/compilers.html>) or simply type `version -java` in MATLAB. One could set the `MATLAB_JAVA` environment variable to use custom JVM, for example, to specify the [jre8-openjdk](<https://archlinux.org/packages/?name=jre8-openjdk>)包 JRE, launch MATLAB with: 
    
    $ env MATLAB_JAVA=/usr/lib/jvm/java-8-openjdk/jre matlab
    
###  OpenGL加速

MATLAB can take advantage of hardware based 2D and 3D OpenGL acceleration. Support for hardware acceleration needs to be configured outside of MATLAB. Appropriate [video drivers](</wzh/index.php?title=Video_drivers&action=edit&redlink=1> "Video drivers（页面不存在）") need to be installed along with the OpenGL utility library [glu](<https://archlinux.org/packages/?name=glu>)包 package. If X11 forwarding is being used, the video drivers need to be installed on both the client and server. To check if MATLAB is making use of hardware based OpenGL acceleration run: 
    
    $ matlab -nodesktop -nosplash -r "opengl info; exit" | grep Software
    
If "software rendering" is not "false", then there is a problem with your hardware acceleration. If this is the case make sure OpenGL is configured correctly on the system. This can be done with the `glxinfo` program from the [mesa-utils](<https://archlinux.org/packages/?name=mesa-utils>)包 package: 
    
    $ glxinfo | grep "direct rendering"
    
If "direct rendering" is not "yes", then there is likely a problem with your system configuration. 

If glxinfo works but not matlab, you can try to run: 
    
    $ export LD_PRELOAD=/usr/lib/libstdc++.so; export LD_LIBRARY_PATH=/usr/lib/xorg/modules/dri/; matlab -nodesktop -nosplash -r "opengl info; exit" | grep Software
    
If its works, you can edit Matlab launcher script to add: 
    
    export LD_PRELOAD=/usr/lib/libstdc++.so
    export LD_LIBRARY_PATH=/usr/lib/xorg/modules/dri/
    
If you experience a low-level graphics error, you can use a software implementation of OpenGL or use an older driver. According to [this](<../zh-cn/Intel_graphics.html#Old_OpenGL_driver_\(i965\)> "Intel graphics") entry in the ArchWiki, in Mesa 20.0 the new Iris driver was promoted to be the default for Gen8+. You may disable it and revert to use the old i965 driver by setting the `MESA_LOADER_DRIVER_OVERRIDE=i965` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable") before starting Matlab or any OpenGL application. Alternatively, you can run Matlab with the following command: 
    
    $ env MESA_LOADER_DRIVER_OVERRIDE=i965 matlab -desktop
    
If it works, you can edit the Matlab launcher script to add: 
    
    export MESA_LOADER_DRIVER_OVERRIDE=i965
    
###  音频

To confirm that MATLAB is able to use the default soundcard to present sounds run: 
    
    $ matlab -nodesktop -nosplash -r "load handel; sound(y, Fs); pause(length(y)/Fs); exit" > /dev/null
    
This should play an except from Handel's "Hallelujah Chorus." If this fails make sure [ALSA](<../zh-cn/ALSA.html> "ALSA") is properly configured. This can be done with the `speaker-test` program from the [alsa-utils](<https://archlinux.org/packages/?name=alsa-utils>)包 package from the [official repositories](<../zh-cn/Official_repositories.html> "Official repositories"): 
    
    $ speaker-test
    
If you do not hear anything, then there is likely a problem with your system configuration. 

###  GPU计算

MATLAB can take advantage of [CUDA enabled GPUs](<https://www.mathworks.co.uk/discovery/matlab-gpu.html>) to speed up applications. In order to take advantage of a supported GPU install the [nvidia](<https://archlinux.org/packages/?name=nvidia>)包, [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包, [ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包, [opencl-nvidia](<https://archlinux.org/packages/?name=opencl-nvidia>)包, and [cuda](<https://archlinux.org/packages/?name=cuda>)包 packages from the [official repositories](<../zh-cn/Official_repositories.html> "Official repositories"). To check if MATLAB is able to utilize the GPU run: 
    
    $ matlab -nodesktop -nosplash -r "x=rand(10, 'single'); g=gpuArray(x); Success=isequal(gather(g), x), exit"  | sed -ne '/Success =/,$p'
    
###  安装额外的编译器

In order to access the full functionality of MATLAB (e.g., to use Simulink, Builder JA, and MEX-file compilation), supported versions of the `gcc`, `g++`, `gfortran`, and `jdk` compilers must be installed. Details about the supported compilers for the [current release](<https://www.mathworks.com/support/compilers/current_release/index.html?sec=glnxa64>) and [previous releases](<https://www.mathworks.com/support/sysreq/previous_releases.html>) are available online. Many of the supported `gcc`, `g++`, `jdk` compiler versions for past MATLAB releases are available from the [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") (e.g., [gcc43](<https://aur.archlinux.org/packages/gcc43/>)AUR, [gcc44](<https://aur.archlinux.org/packages/gcc44/>)AUR, [gcc47](<https://aur.archlinux.org/packages/gcc47/>)AUR, [gcc49](<https://aur.archlinux.org/packages/gcc49/>)AURand [jdk7](<https://aur.archlinux.org/packages/jdk7/>)AUR), while past versions of the `gfortran` compilers are not packaged. 

To use previous versions of the the `gcc`, `g++`, and `gfortran` compilers with MEX files, edit `${MATLAB}/bin/mexopts.sh` and replace all occurrences of `CC='gcc'` with `CC='gcc-4.X'`, `CXX='g++'` with `CXX='g++-4.X'`, and `FC='gfortran'` with `FC='gfortran-4.X'`, where `X` is the compiler version appropriate for the particular MATLAB release. 

**注意：** Newer versions of Matlab (at least 2017a) does not seem to respect the `${MATLAB}/bin/mexopts.sh` customization. Instead it uses `${MATLAB}/bin/glnxa64/mexopts/LANG_glnxa64.xml` file.

**注意：** Though, it's no officially supported, one could still use higher version of compiler, and ignore the warnings.

###  Matlab的帮助查看器的配置

The help browser uses valuable slots in the dynamic thread vector and causes competition with core functionality provided by libraries like the BLAS that also depend on the dynamic thread vector. The help browser can be configured to use fewer slots in the dynamic thread vector with 
    
    >> webutils.htmlrenderer('basic');
    
This is a persistent change and to reverse it use 
    
    >> webutils.htmlrenderer('default');
    
### Garbled Interface
    
    export J2D_D3D=false
    export MATLAB_JAVA=/usr/lib/jvm/java-7-openjdk/jre
    
### Serial port access

Matlab uses a bundled rxtx library to access serial ports. The built-in version requires the user to have write access directly to /var/run which is no good idea. The easiest way to fix this properly is to install the [java-rxtx](<https://archlinux.org/packages/?name=java-rxtx>)包 package first. Follow the instructions shown while installing this package to get your user into the right groups. Then run the following commands to make Matlab use the system rxtx version: 
    
    cd {MATLAB}/java/jarext
    mv RXTXcomm.jar RXTXcomm.jar.off
    ln -s /usr/share/java/rxtx/RXTXcomm.jar .
    
    cd {MATLAB}/bin/glnx64
    mv librxtxSerial.so librxtxSerial.so.off
    ln -s /usr/lib/librxtxSerial.so .
    
### HiDPI and 4k

See [HiDPI#MATLAB](<../zh-cn/HiDPI.html#MATLAB> "HiDPI")

##  故障排除

###  帮助浏览器和动态脚本黑屏

安装 [libselinux](<https://aur.archlinux.org/packages/libselinux/>)AUR. 

###  静态线程本地存储错误

MATLAB has a number of libraries that have been compiled with static thread local storage (TLS) including the help broswer `doc` and the BLAS libraries. For example, 
    
    >> doc('help');
    >> ones(10)*randn(10);
    Error using  * 
    BLAS loading error:
    dlopen: cannot load any more object with static TLS
    
is related to the bugs: 

  * [961964](<https://www.mathworks.de/support/bugreports/961964>) for which patched libraries are available from [MathWorks](<http://www.mathworks.de/support/bugreports/license/accept_license/5730?fname=attachment_961964_12b_13a_13b_14a_glnxa64_2014-01-30.zip&geck_id=961964>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-08-02 ⓘ]
  * [1003952](<https://www.mathworks.com/support/bugreports/1003952>) for which workarounds exist

A more general solution of recompiling `glibc` has also been suggested. [[1]](<https://stackoverflow.com/a/19468365>)

###  Matlab在显示图像时崩溃

To identify this error, start MATLAB with 
    
    LIBGL_DEBUG=verbose matlab
    
from the terminal and try to collect OpenGL information with `opengl info` from the MATLAB command prompt. If it crashes again and there is an output line like 
    
    libGL error: dlopen /usr/lib/xorg/modules/dri/swrast_dri.so failed 
    (/usr/local/MATLAB/R2011b/bin/glnxa64/../../sys/os/glnxa64/libstdc++.so.6: 
    version `GLIBCXX_3.4.15' not found (required by /usr/lib/xorg/modules/dri/swrast_dri.so))
    
then the problem is that MATLAB uses its own GNU C++ library, which is an older version than the up-to-date version on your Arch Linux system. Make MATLAB use the current C++ library for your system by 
    
    cd /usr/local/MATLAB/R(your release)/sys/os/glnxa64
    sudo unlink libstdc++.so.6
    sudo ln -s /usr/lib/libstdc++.so.6
    
If MATLAB still crashes or corrupts graphics (during startup or when plotting), make sure Java's 2D OpenGL rendering is disabled. The environment variable `_JAVA_OPTIONS` should not contain `-Dsun.java2d.opengl=true`. 

###  Blank/grey UI when using WM (non-reparenting window manager)

This is a common issue in a number of window managers. (DWM, Awesome, bspwm) Java does not play well with these window managers. There are two methods. 

First try setting the environment variable by running 
    
    $ export _JAVA_AWT_WM_NONREPARENTING=1
    
If Matlab works afterwards, export the variable in your `.xinitrc`. 

If it does not resolve, you have to fool Java into thinking the WM is named LG3D. (It's an old, depreciated WM that Java applications ironically support) Clean the previous environment variable, install the [wmname](<https://archlinux.org/packages/?name=wmname>)包 utility, and run. 
    
    wmname LG3D
    
Try running Matlab. If it works, put the fix in your starting script. (`.xinitrc`, `bspwmrc` and similar should be OK) Do note that other applications (such as `neofetch`, or `tdrop`) will think your WM is named LG3D, so you will have to configure them accordingly. Another solution is to run the command only before launching Matlab, and fixing the name after you are done with Matlab. 

If it does not work, try the combination of both. (The second line works in bspwm) If it still does not work, try googling similar issues with java in general. 

###  文本乱码或不可见

Set the environment variable `J2D_D3D` to `false`[[2]](<https://stackoverflow.com/questions/22737535/swing-rendering-appears-broken-in-jdk-1-8-correct-in-jdk-1-7>). 

In newer versions of MATLAB (R2015b) [[3]](<https://www.reddit.com/r/archlinux/comments/3yaga8/matlab_installer_bonked/>) this also requires setting `MATLAB_JAVA` to something openjdk based. Example: 
    
    export J2D_D3D=false
    ./bin/glnxa64/install_unix -javadir /usr/lib/jvm/java-7-openjdk/jre
    
###  菜单和输入窗口的文字显示异常

If you notice that the menus or the input fields are corrupted or not appearing correctly then you can try to activate the _"**Use antialiasing to smooth desktop fonts** "_ option in Matlab preferences, it seems to solve the problem. Go to _**Preferences - > Matlab -> Fonts**_ and activate it. You will need to restart Matlab in order to take affect. 

###  安装依赖缺失

As one installs Matlab, it might complain that it cannot find a package, for the most part just look at the package name and then install it with [Pacman](<../zh-cn/Pacman.html> "Pacman"), or in the case of x86_64 there are some libraries only in [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR"). 

### Installation error: archive is not a ZIP archive

During the installation you can get: 
    
    The following error was detected while installing _package_name_ : archive is not a ZIP archive 
    Would you like to retry installing _package_name_? If you press No, the installer will exit without completing the installation. More information can be found at /tmp/mathworks_root.log
    
Matlab downloads all packages to `/tmp/` directory which resides in RAM and is maximum size of half of available memory. In this case it is not enough for installation files and Matlab 2019a installer will warn you about this. If it did not, or if you ignored the warning, you will have got the above error. 

You can either [resize tmpfs](<../zh-cn/Tmpfs.html#Examples> "Tmpfs") (3,5 GB is not enough, 6 GB works), or remove packages from base install and add them later with built-in Matlab add-on installer. 

###  安装时library错误

  * Make sure that the symlink `bin/glnx64/libstdc++.so.6` is pointing to the correct version of `libstdc++.so.xx` (which is also in the same directory and has numbers where 'xx' is). By default, it may be pointing to an older (and nonexistent) version (different value for 'xx').

  * Make sure the device you are installing from is not mounted as `noexec`

  * If you downloaded the files from Mathworks' website, make sure they are not on an NTFS or FAT partition, because that can mess up the symlinks. Ext4 or Ext3 should work.

###  启动时出现段错误

If Matlab (R2016a or earlier) stops working after upgrading [ncurses](<https://archlinux.org/packages/?name=ncurses>)包 to v6.x, [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") the [ncurses5-compat-libs](<https://aur.archlinux.org/packages/ncurses5-compat-libs/>)AUR package. See [BBS#202575](<https://bbs.archlinux.org/viewtopic.php?id=202575>). 

In newer versions (e.g. R2017b), the issue could also be due to a font display failing to load. Try moving the libfreetype.so.6 font display file in $MATLAB/bin/glnxa64/ to an 'exclude' directory; see [BBS#231299](<https://bbs.archlinux.org/viewtopic.php?id=231299>). 

###  与Intel显卡有关的错误

Some users have reported issues with DRI3 enabled on Intel Graphics chips. A possible workaround is to disable DRI3 and run MATLAB with hardware rendering on DRI2; to do so, launch MATLAB with the environment variable LIBGL_DRI3_DISABLE set to 1: 
    
    LIBGL_DRI3_DISABLE=1 /{MATLAB}/bin/matlab
    
If the previous workaround does not work, the issue can be circumvented by selecting software rendering with the MATLAB command (beware, performance may be very poor when doing e.g. big or complex 3D plots): 
    
    opengl('save','software')
    
See [[4]](<https://bugzilla.redhat.com/show_bug.cgi?id=1357571>) and [[5]](<https://bugs.freedesktop.org/show_bug.cgi?id=96671>) for more. 

###  附加组件管理器无法使用

Addon manager requires the [libselinux](<https://aur.archlinux.org/packages/libselinux/>)AUR package to work. (in Matlab 2017b) 

Since upgrade from pango-1.40.5 to pango-1.40.6, the MATLABWindow application (responsible for Add-On Manager, Simulation Data Inspector and perhaps something else) cannot be started. [FS#54257](<https://bugs.archlinux.org/task/54257>) A workaround is to point MATLAB shipping glib libraries to those glib libraries from your system. There are 5 of those libraries in `matlabroot/R2017b/cefclient/sys/os/glnxa64`, namely, as of R2017b: 
    
    libgio-2.0.so
    libglib-2.0.so
    libgmodule-2.0.so
    libgobject-2.0.so
    libgthread-2.0.so
    
Make it so that these symlinks are pointing to your system glib libraries instead of versions located in `matlabroot/R2017b/cefclient/sys/os/glnxa64`. On a standard arch install the local files reside in `/usr/lib/`. 

Relinking of "libfreetype.so.6" is also necessary to open these interfaces. This is found in `matlabroot/R2017b/bin/glnxa64/`. 

If the window opens but is blank, consider switching the html renderer to: " webutils.htmlrenderer('basic');" as described in [#Matlab的帮助查看器的配置](<#Matlab%E7%9A%84%E5%B8%AE%E5%8A%A9%E6%9F%A5%E7%9C%8B%E5%99%A8%E7%9A%84%E9%85%8D%E7%BD%AE>). 

###  LiveScript错误

If you get the error when attempting to load or create a LiveScript: 
    
     Viewing matlab live script files is not currently supported by this operating system configuration
    
The steps in [#附加组件管理器无法使用](<#%E9%99%84%E5%8A%A0%E7%BB%84%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8>) may resolve the issue. 

###  Using webcam/video device

Make sure the correct support package addons are installed (webcam or OS Generic Video Interface for example). If running matlab as a user, make sure your user has write permissions to wherever the support packages are being downloaded and installed. 

At least Matlab 2016b does not recognize webcams or imaq adapters correctly without gstreamer0.10. The gstreamer0.10 can be found in the aur and installed as a work around. 

Since MATLAB R2017a, Image Acqusition Toolbox is using GStreamer library version 1.0. It previously used version 0.10. 

In general, USB Webcam Support Package does a better job working with UVC and built-in cameras than OS Generic Video Interface Support Package. 

**Warning:** As of 2018-08-15 updating gst from 1.14.0 to 1.14.2 breaks video device operation (MATLAB does not see the video device anymore). Downgrading fixes this. 

###  关闭帮助窗口时Matlab数秒无响应

Since upgrade of glibc from 2.24 to 2.25, MATLAB (at least R2017a) hangs when closing Help Browser. The issue is related to the particular version of jxbrowser-chromium shipped with MATLAB. This issue is still present with glibc 2.26 and MATLAB R2017b. 

To fix this issue, download the [latest jxbrowser](<https://www.teamdev.com/jxbrowser>) and replace the following jars from MATLAB: 
    
    matlabroot/java/jarext/jxbrowser-chromium/jxbrowser-chromium.jar
    matlabroot/java/jarext/jxbrowser-chromium/jxbrowser-linux64.jar
    
MATLAB should automatically unpack those jars into `matlabroot/sys/jxbrowser-chromium/glnxa64/chromium` when first opening Help Browser. Remove `matlabroot/sys/jxbrowser-chromium/glnxa64/chromium` directory to make sure MATLAB uses the latest jxbrowser. 

Unfortunately, this workaround does not work in R2017b anymore. Going deeper into investigation of this issue, it is related to a crash of one of jxbrowser-chromium processes. The parent process of jxbrowser-chromium then sits there and waits for response from a process that is already dead. This causes MATLAB main window to freeze. You can easily unfreeze MATLAB by manually killing all leftover jxbrowser-chromium processes. 

I have come up with this simple script that uses inotify and waits for user to close Help browser in MATLAB. It triggers when user closes Help browser and sends kill signal to all leftover jxbrowser-chromium processes: 
    
    #!/bin/sh
    
    if [ -z "$1" ]; then
    	REL=R2017b
    else
    	REL=$1
    fi
    
    JXPATH="/path/to/MATLAB/$REL/sys/jxbrowser-chromium/glnxa64/chromium"
    CMD="inotifywait -m -e CLOSE $JXPATH/resources.pak"
    
    #Exit if the daemon is already active
    if ! pgrep -f "$CMD" > /dev/null; then
    	#Wait for user to close Help Browser, then killall leftover jxbrowser processes
    	$CMD |
    	while read line
    	do
    		killall "$JXPATH/jxbrowser-chromium"
    	done
    else
    	exit
    fi

I run this script as part of my MATLAB start script like that: 
    
    ~/bin/unfreeze_matlab.sh R2017b &
    
To make sure that this background job is killed when I exit MATLAB, I use this in the beginning of MATLAB start script: 
    
    trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
    
###  一些下拉菜单无法被选中

In some interfaces - such as Simulation Data Inspector or Simulink Test Manager - nothing happens when choosing an item in dropdown menu (for example, when trying to change a number of subplots in Simulation Data Inspector). To work around this issue, hold down the Shift key while clicking the item in dropdown menu. 

###  因许可证问题造成的无法启动Matlab

In case MATLAB will not start from a [desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment") by the call of its [desktop file](</wzh/index.php?title=Desktop_file&action=edit&redlink=1> "Desktop file（页面不存在）") one should see the output as you start it from the terminal. For a _Licensing error_ such as: 
    
    # matlab
    
    MATLAB is selecting SOFTWARE OPENGL rendering.
    License checkout failed.
    License Manager Error -9
    This error may occur when: 
    -The hostid of this computer does not match the hostid in the license file. 
    -A Designated Computer installation is in use by another user. 
    If no other user is currently running MATLAB, you may need to activate.
    
    Troubleshoot this issue by visiting: 
    <https://www.mathworks.com/support/lme/R2017a/9>
    
    Diagnostic Information:
    Feature: MATLAB 
    License path: /home/<USER>/.matlab/R2017a_licenses/license_<NUM>_R2017a.lic:/home/<USER>/.matlab/R2017a_licenses/lice
    nse_Darkness_<NUM>_R2017a.lic:/opt/MATLAB/R2017a/licenses/license.dat:/opt/MATLAB/R2017a/licenses/*
    .lic 
    Licensing error: -9,57.
    
a re-activation might solve the problem. 

###  启动Matlab时显示"Failure loading desktop class"并崩溃

In case MATLAB will not start and starting it from command line gives you the following error: 
    
    $ matlab
    
    Fatal Internal Error: Internal Error: Failure occurs during desktop startup. Details: Failure loading desktop class.
    
and you have the option [`-Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel`](<../zh-cn/Java.html#GTK_LookAndFeel> "Java") set in your `_JAVA_OPTIONS` environment variable, start MATLAB with 
    
    $ _JAVA_OPTIONS= matlab
    
If this works, add the line 
    
    export _JAVA_OPTIONS=
    
to your MATLAB launcher script. Optionally re-add other Java options. 

### Unable to type in text fields of interfaces based on MATLABWindow

Since R2018a, it is not possible to type text in interfaces based on MATLABWindow - like Signal Editor, Add-Ons Explorer and others. MATLABWindow and MATLAB's webwindow infrastructure is based on Chromium Embedded Framework, and it looks like a known and long standing bug: <https://bitbucket.org/chromiumembedded/cef/issues/2026/multiple-major-keyboard-focus-issues-on>

One possible workaround is to switch focus from the MATLABWindow to another window and then switch back - so that you can type. 

To elaborate more on this workaround (since the problem is still there in R2018b), here is what i did in my Openbox config (note that the A-Middle keybinding already exist in default config): 
    
        <mousebind button="A-Middle" action="Press">
           <action name="Unfocus"/>
           <action name="Focus"/>
         </mousebind>
    
Now, whenever it is not possible to type in a text field, I press Alt+Mouse middle mouse and then I can type again. 

###  安装程序显示 "Unable to launch the MATLABWindow application" 并崩溃

In MATLAB version R2018b (and later), the installer crashes as follows: 
    
     $ ./install 
    
    terminate called after throwing an instance of 'std::runtime_error'
      what():  Failed to launch web window with error: Unable to launch the MATLABWindow application. The exit code was: 127
    [1]    1409378 IOT instruction (core dumped)  ./install
    
To find out why `MATLABWindow` is crashing, run it manually to get detailed information. 
    
     $ ./bin/glnxa64/MATLABWindow 
    
    bin/glnxa64/MATLABWindow: symbol lookup error: /usr/lib/libcairo.so.2: undefined symbol: FT_Get_Color_Glyph_Layer
    
`FT_Get_Color_Glyph_Layer` is a symbol of [freetype2](<https://archlinux.org/packages/?name=freetype2>)包, which indicates a library incompatibility between the MATLAB application and the Arch Linux packages. [[6]](<https://ww2.mathworks.cn/matlabcentral/answers/364551-why-is-matlab-unable-to-run-the-matlabwindow-application-on-linux>)

To fix this, put aside MATLAB's `libfreetype.so*`. 
    
    $ rm ./bin/glnxa64/libfreetype.so.6*
    
You can also use `LD_PRELOAD` environment variable to force MATLAB use Arch Linux's libfreetype without removing the lib file. 
    
    $ export LD_PRELOAD=/lib64/libfreetype.so
    $ ./install
    
Similarly, if the error is caused by `undefined symbol: g_log_structured...`, put aside MATLAB's `libglib-2.0.so*`. If the error is caused by `path to/libstdc++.so.6: version `CXXABI_1.3.9' not found (required by _somelibrary_)`, put aside MATLAB's `libstdc++.so.6`. 

### Add-on manager does not start in R2020a

In MATLAB version R2020a Update 5 (and possibly older), the Add-on manager does not start. Instead, the following error is shown 
    
     Error using matlab.internal.cef.webwindow (line 385)
     MATLABWindow application failed to launch. Unable to launch the MATLABWindow application
     
     Error in matlab.internal.webwindow/createImplementation (line 288)
                     implObj = matlab.internal.cef.webwindow(varargin{:});
     
     Error in matlab.internal.webwindow (line 144)
                 obj.impl = obj.createImplementation(varargin{:});
     
     Error in matlab.internal.addons.AddOnsWindow/launch (line 51)
                     obj.webwindow = matlab.internal.webwindow(char(url), obj.debugPort, obj.normalWindowPosition);
     
     Error in matlab.internal.addons.Explorer/loadUrlForNavigateToMessage (line 125)
                     obj.addOnsWindowInstance.launch(url, obj.windowStateUtil.getExplorerWindowMaximizedSetting);
     
     Error in matlab.internal.addons.Explorer/show (line 56)
                     obj.loadUrlForNavigateToMessage(url);
     
     Error in matlab.internal.addons.launchers.showExplorer (line 128)
             matlab.internal.addons.Explorer.getInstance.show(navigationData);
    
The problem is solved by removing (or hiding) the `libgl*` and `libgio*` libraries of MATLAB, as suggested for an older issue [[7]](<https://it.mathworks.com/matlabcentral/answers/397138-why-do-i-get-a-matlabwindow-application-failed-to-launch-error-when-launching-live-editor-app-des#answer_316968>)
    
    $ cd {MATLAB INSALLATION FOLDER}/cefclient/sys/os/glnxa64/
    $ mkdir exclude
    $ mv libglib-2.0.so* libgio-2.0.so* exclude/
    
##  在systemd-nspawn容器中运行

Matlab can be run within a systemd-nspawn container to maintain a static system and avoid the library issues that often plague matlab installs after significant updates to libraries in Arch. Refer to [Systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn") for detailed information on setting up such containers. 

The following lists instruction to get a MATLAB 2017b install running in a minimal debian 9 environment. It assumes matlab is already installed as normal in "/usr/local/MATLAB/R2017b". 

Use [Xhost](<../zh-cn/Xhost.html> "Xhost") to allow the nspawn environment to use the existing X server instance. 

Create a minimal debian environment in a folder ("deb9" here) with: 
    
    $ debootstrap --arch=amd64 stretch deb9
    
Set a password for the root user and then boot the environment with: 
    
    $ systemd-nspawn --bind-ro=/dev/dri --bind=/tmp/.X11-unix --bind=/usr/local/MATLAB/ -b -D deb9
    
Install the following packages to have the requisite libraries in the nspawn environment for MATLAB. "mesa-utils" and "usbutils" can be installed to debug graphics acceleration and usb interfaces for I/O with MATLAB. 
    
    $ apt-get install xorg build-essential libgtk2.0-0 libnss3 libasound2 
    
Install the MATLAB-support (from contrib source) package in the environment for some convenient integration. 
    
    $ apt-get install matlab-support
    
Set the $DISPLAY variable to use your existing X server instance. 
    
    $ export DISPLAY=:0
    
MATLAB can be launched from within the environment normally by using the binary at $MATLABROOT/bin. 
