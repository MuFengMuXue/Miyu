**翻译状态：**

  * 本文（或部分内容）译自 [Xcompmgr](<https://wiki.archlinux.org/title/Xcompmgr> "arch:Xcompmgr")，最近一次同步于 2015-06-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xcompmgr?diff=0&oldid=376307>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xcompmgr_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Composite](</wzh/index.php?title=Composite&action=edit&redlink=1> "Composite（页面不存在）")
  * [Compiz](<../zh-cn/Compiz.html> "Compiz")
  * [Window manager](<../zh-cn/Window_manager.html> "Window manager")

**Xcompmgr** 是一个简单的混合窗口管理器，可以实现阴影、原生窗口透明（配合`transset`工具）等特效。Xcompmgr设计初衷只是实现混合窗口管理器的概念，所以比起同类混合窗口管理器如 [Compiz Fusion](<../zh-cn/Compiz.html> "Compiz")，Xcompmgr轻量许多。 

Xcompmgr不替代任何窗口管理器，所以对于[Openbox](<../zh-cn/Openbox.html> "Openbox")和[Fluxbox](<../zh-cn/Fluxbox.html> "Fluxbox")这类缺乏特效的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")来讲，配合Xcompmgr能得到更华丽的视觉效果。 

##  安装

在安装 Xcompmgr 前，请先确认您已经正确安装并配置了 [Xorg](<../zh-cn/Xorg.html> "Xorg")。如果你使用了自定义配置，请打开X服务器中的 [Composite](</wzh/index.php?title=Composite&action=edit&redlink=1> "Composite（页面不存在）") 拓展。 

您可以直接从[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")中安装[xcompmgr](<https://archlinux.org/packages/?name=xcompmgr>)包以及透明度设置工具[transset-df](<https://aur.archlinux.org/packages/transset-df/>)AUR。 

##  配置

运行 `xcompmgr`： 
    
    $ xcompmgr -c
    
如果要在每次 Xorg 启动时运行，添加以下内容到[xprofile](<../zh-cn/Xprofile.html> "Xprofile")： 
    
    xcompmgr -c &
    
用户可以通过命令行参数调整阴影、消隐等效果，以下是一个常用的配置： 
    
    xcompmgr -c -C -t-5 -l-5 -r4.2 -o.55 &
    
查看命令行帮助： 
    
    $ xcompmgr --help
    
###  窗口透明度

`transset-df` 工具用来设置单个窗口的透明度，透明特效可能会降低系统性能。 

先启动要设置透明度的程序，然后运行： 
    
    transset-df n
    
.. 此处 `n` 是0到1之间的数字，0表示完全透明（不可见），1表示不透明。例如：`transset .25` 代表75%的透明度。 

运行后，鼠标会变成十字形。点击要设置的窗口，即可应用透明度设置。 

##  小提示

###  方便开关xcompmgr的脚本

把这个脚本放在合适的应用程序目录，可以方便地启动、关闭xcompmgr。 
    
    #!/bin/bash
    #
    # Start a composition manager.
    # (xcompmgr in this case)
    
    comphelp() {
      echo "Composition Manager:"
      echo "   (re)start: COMP"
      echo "   stop:      COMP -s"
      echo "   query:     COMP -q"
      echo "              returns 0 if composition manager is running, else 1"
      exit
    }
    
    checkcomp() {
      pgrep xcompmgr &>/dev/null
    }
    
    stopcomp() {
      checkcomp && killall xcompmgr
    }
    
    startcomp() {
      stopcomp
    # Example settings only. Replace with your own.
      xcompmgr -CcfF -I-.015 -O-.03 -D6 -t-1 -l-3 -r4.2 -o.5 &
      exit
    }
    
    case "$1" in
        "") startcomp ;;
      "-q") checkcomp ;;
      "-s") stopcomp; exit ;;
         *) comphelp ;;
    esac
    
###  仅用一个快捷键就切换 xcompmgr

利用上面脚本的状态部分，将下面脚本设置为某个快捷键的脚本： 
    
    #!/bin/bash
    
    if pgrep xcompmgr &>/dev/null; then
           echo "Turning xcompmgr ON"
           xcompmgr -c -C -t-5 -l-5 -r4.2 -o.55 &
    else
           echo "Turning xcompmgr OFF"
           pkill xcompmgr &
    fi
    
    exit 0
    
##  疑难解答

###  Mozilla Firefox 打开 Flash 时崩溃

新建可执行文件`/etc/profile.d/flash.sh`，文件内容如下： 
    
    export XLIB_SKIP_ARGB_VISUALS=1
    
这将关闭混合特效。 

###  登录后变成浅灰色背景 （如Openbox）

安装[hsetroot](<https://archlinux.org/packages/?name=hsetroot>)包，在运行xcompmgr之前，执行`hsetroot -solid "#000000"`（将000000替换成你想要的颜色代码）。 

###  在 awesome 窗口管理器中出现 BadPicture request

如果你在 [awesome](<../zh-cn/Awesome.html> "Awesome") 得到以下错误信息： 
    
     error 163: BadPicture request 149 minor 8 serial 34943
     error 163: BadPicture request 149 minor 8 serial 34988
     error 163: BadPicture request 149 minor 8 serial 35033
    
只需要安装软件包 [feh](<../zh-cn/Feh.html> "Feh") 然后重启 [awesome](<../zh-cn/Awesome.html> "Awesome")。 

### Screen not updating in awesome after resolution change

When using an external monitor, you may encounter problems when automatically changing display resolutions: a part of the screen becomes "stuck" and no longer updates itself. This problem occurs because of the initial resolution change (happening before Xcompmgr starts) as well as [awesome](<../zh-cn/Awesome.html> "Awesome") setting the background via [feh](<../zh-cn/Feh.html> "Feh"). 

To fix it, you need to [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [hsetroot](<https://archlinux.org/packages/?name=hsetroot>)包 and put the following line in `.xinitrc`, just before `xcompmgr`: 
    
    hsetroot -solid "#000066"
    
(you can replace _#000066_ with your color of choice). 
