**翻译状态：**

  * 本文（或部分内容）译自 [Ranger](<https://wiki.archlinux.org/title/Ranger> "arch:Ranger")，最近一次同步于 2025-05-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ranger?diff=0&oldid=827453>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ranger_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [文件管理器功能](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")
  * [lf](<../zh-cn/Lf.html> "Lf")
  * [Midnight Commander](<../zh-cn/Midnight_Commander.html> "Midnight Commander")
  * [nnn](<../zh-cn/Nnn.html> "Nnn")
  * [vifm](<../zh-cn/Vifm.html> "Vifm")

[ranger](<https://ranger.github.io/>) 是一个基于文本的文件管理器，以 Python 编写。不同层级的目录分别在一个面板的三列中进行展示。可以通过快捷键、书签、鼠标以及历史命令在它们之间移动。当选中文件或目录时，会自动预览文件或目录。 

主要特性有：[vi](<../zh-cn/Vi.html> "Vi") 风格的快捷键、书签、选择、标签、选项卡、命令历史、创建符号链接、多种终端模式以及任务视图。ranger 可以定制命令和快捷键，包括绑定到外部脚本，ranger 还有自己的[文件打开工具](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "默认应用程序")——[rifle(1)](<https://man.archlinux.org/man/rifle.1>)。 

最接近的竞争者是 [lf](<../zh-cn/Lf.html> "Lf")、[Vifm](<../zh-cn/Vifm.html> "Vifm") 和 [yazi](<https://archlinux.org/packages/?name=yazi>)包。 

##  安装

安装 [ranger](<https://archlinux.org/packages/?name=ranger>)包 包，或其开发版本 [ranger-git](<https://aur.archlinux.org/packages/ranger-git/>)AUR。 

##  用法

在[终端](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E7%BB%88%E7%AB%AF> "应用程序列表/工具")里执行 `ranger` 以启动 ranger。 

快捷键 | 命令   
---|---  
`?` | 打开帮助手册或列出快捷键、命令以及设置项   
`l`, `Enter` | 打开文件   
`j`, `k` | 选择当前目录中的文件   
`h`, `l` | 在目录树中上移和下移   
`q` | 退出   
  
##  定制

第一次启动时，ranger 会创建一个目录 `~/.config/ranger/`。可以使用以下命令复制默认配置文件到这个目录： 
    
    $ ranger --copy-config=all
    
此外，设定 `RANGER_LOAD_DEFAULT_RC=false` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")可以避免在加载本地配置时同时加载全局配置。 

了解一些基本的 python 知识可能对定制 ranger 会有帮助。 

  * `rc.conf` \- 选项设置和快捷键
  * `commands.py` \- 能通过 `:` 执行的命令
  * `rifle.conf` \- 指定不同类型的文件的默认打开程序。

`rc.conf` 只需要包含与默认配置文件不同的部分，因为它们都会被加载。对于 `commands.py`，如果你没有包含整个文件，把下面这一行加入到文件起始处： 
    
    from ranger.api.commands import *
    
更多配置选项请参考 [ranger(1)](<https://man.archlinux.org/man/ranger.1>)。 

###  移动到回收站

如果想添加一个把文件移动到目录 `~/.local/share/Trash/files/` 的快捷键 `DD`，将相关配置修改为以下配置： 
    
    ~/.config/ranger/rc.conf
    
    ...
    map DD shell mv %s /home/${USER}/.local/share/Trash/files/
    ...
    
或使用 [glib2](<https://archlinux.org/packages/?name=glib2>)包 软件包提供的 GIO 命令： 
    
    map DD shell gio trash %s
    
一般的图形文件管理器都支持查看或清空回收站，此外还可以使用 `gio list trash://` 命令查看，用 `gio trash --empty` 命令清空回收站。 

###  命令定义

继续上面的例子，增加如下代码将会定义一个清空垃圾箱 `~/.Trash` 的命令。 
    
    ~/.config/ranger/commands.py
    
    ...
    
    class empty(Command):
        """:empty
    
        Empties the trash directory ~/.Trash
        """
    
        def execute(self):
            self.fm.run("rm -rf /home/myname/.Trash/")
    
输入 `:empty` 与 `Enter` 来执行命令， 如果希望的话，也可以使用 tab 补全。 

**提示：** 你可以在[官方 wiki](<https://github.com/ranger/ranger/wiki/Custom-Commands>) 中找到很多有用的命令。

###  配色方案

Ranger 配备了四个配色方案：`默认 (default)`、`丛林 (jungle)`、`积雪 (snow)`和`烈日 (solarized)`。 下列命令可自定义配色： 
    
     set colorscheme _scheme_
    
自定义配色方案放在 `~/.config/ranger/colorschemes`。 

###  文件预览色彩高亮

安装 [python-pygments](<https://archlinux.org/packages/?name=python-pygments>)包，将 `/usr/share/doc/ranger/config/scope.sh` 复制到 `~/.config/ranger/scope.sh` 并在 ranger 配置文件中将 `PYGMENTIZE_STYLE` 设定为您想要的值。通过 `pygmentize -L style` 获得支持的主题的完整列表。 

###  文件关联

Ranger 使用自己的文件打开程序，名为`rifle`，它的配置文件为 `~/.config/ranger/rifle.conf`。如果该文件不存在，可运行 `ranger --copy-config=rifle` 生成。例如，如下的代码指定 [kile](<https://archlinux.org/packages/?name=kile>)包 为打开 tex 文件的默认程序。 
    
    ext tex = kile "$@"
    
使用 [xdg-utils](<https://archlinux.org/packages/?name=xdg-utils>)包 来打开所有文件，设置 `$EDITOR` 和 `$PAGER`: 
    
    else = xdg-open "$1"
    label editor = "$EDITOR" -- "$@"
    label pager  = "$PAGER" -- "$@"
    
##  提示与技巧

###  存档相关

可以使用 [atool](<https://archlinux.org/packages/?name=atool>)包 或 [p7zip](<https://archlinux.org/packages/?name=p7zip>)包 来进行存档操作。 

####  解压缩

下面的命令实现了解压当前目录下选中的项目： 
    
    import os
    from ranger.core.loader import CommandLoader
    
    class extract_here(Command):
        def execute(self):
            """ extract selected files to current directory."""
            cwd = self.fm.thisdir
            marked_files = tuple(cwd.get_selection())
    
            def refresh(_):
                cwd = self.fm.get_directory(original_path)
                cwd.load_content()
    
            one_file = marked_files[0]
            cwd = self.fm.thisdir
            original_path = cwd.path
            au_flags = ['-x', cwd.path]
            au_flags += self.line.split()[1:]
            au_flags += ['-e']
    
            self.fm.copy_buffer.clear()
            self.fm.cut_buffer = False
            if len(marked_files) == 1:
                descr = "extracting: " + os.path.basename(one_file.path)
            else:
                descr = "extracting files from: " + os.path.basename(
                    one_file.dirname)
            obj = CommandLoader(args=['aunpack'] + au_flags
                                + [f.path for f in marked_files], descr=descr,
                                read=True)
    
            obj.signal_bind('after', refresh)
            self.fm.loader.add(obj)
    
对于使用 7z 的用户, 可以在添加以下命令后, 选中压缩包然后执行 ":extract" 或通过绑定的快捷键来解压 
    
    class extract(Command):
        """:extract <paths>
        
        Extract archives using 7z
        """
        def execute(self):
            import os
            fail=[]
            for i in self.fm.thistab.get_selection():
                ExtractProg='7z x'
                if i.path.endswith('.zip'):
                    # zip encoding issue
                    ExtractProg='unzip -O gbk'
                elif i.path.endswith('.tar.gz'):
                    ExtractProg='tar xvf'
                elif i.path.endswith('.tar.xz'):
                    ExtractProg='tar xJvf'
                elif i.path.endswith('.tar.bz2'):
                    ExtractProg='tar xjvf'
                if os.system('{0} "{1}"'.format(ExtractProg, i.path)):
                    fail.append(i.path)
            if len(fail) > 0:
                self.fm.notify("Fail to extract: {0}".format(' '.join(fail)), duration=10, bad=True)
            self.fm.redraw_window()

PS: 如果需要解压 ZIP 压缩包还需要安装 [unzip-iconv](<https://aur.archlinux.org/packages/unzip-iconv/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found](为了解决中文乱码问题) 

####  压缩

以下命令允许用户将当前目录下选中的文件通过":compress <package name>"命令压缩。它还支持通过当前目录名和为扩展名追加几种可能性来建议名称。 
    
    import os
    from ranger.core.loader import CommandLoader
    
    class compress(Command):
        def execute(self):
            """ Compress marked files to current directory """
            cwd = self.fm.thisdir
            marked_files = cwd.get_selection()
    
            if not marked_files:
                return
    
            def refresh(_):
                cwd = self.fm.get_directory(original_path)
                cwd.load_content()
    
            original_path = cwd.path
            parts = self.line.split()
            au_flags = parts[1:]
    
            descr = "compressing files in: " + os.path.basename(parts[1])
            obj = CommandLoader(args=['apack'] + au_flags + \
                    [os.path.relpath(f.path, cwd.path) for f in marked_files], descr=descr)
    
            obj.signal_bind('after', refresh)
            self.fm.loader.add(obj)
    
        def tab(self):
            """ Complete with current folder name """
    
            extension = ['.zip', '.tar.gz', '.rar', '.7z']
            return ['compress ' + os.path.basename(self.fm.thisdir.path) + ext for ext in extension]

###  外部驱动器

外部驱动器可通过 [udev](<../zh-cn/Udev.html> "Udev") 或 [udisks](<../zh-cn/Udisks.html> "Udisks") 自动挂载。跳转到共有挂载点 `/media` 和 `/run/media/$USER` 的快捷键分别为 `gm` 和 `gi`。 

###  隐藏文件

使用以下命令切换隐藏文件的可见性： 
    
    :set show_hidden!
    
显示隐藏的文件： 
    
    :set show_hidden true
    
要固定该设置，请将该设置添加到配置文件： 
    
    rc.conf
    
    set show_hidden true
    
此外，可使用 `zh` 快捷键切换隐藏文件的可见性。 

###  镜像挂载

以下命令假设你正在使用 [CDemu](<../zh-cn/CDemu.html> "CDemu") 作为你的镜像挂载器，挂载虚拟驱动器到指定位置（如 `/media/virtualrom`），类似于 [autofs](<../zh-cn/Autofs.html> "Autofs") 文件系统，**不要忘记根据你的系统设置修改挂载路径** 。 

为从 ranger 把镜像挂载到 cdemud 虚拟驱动器，需要选中镜像文件然后在终端输入 ':mount'。根据您的设置，挂载可能会需要一些时间。以下命令使用的自定义加载器会等待加载过程结束然后通过后台在第 9 标签打开挂载了的镜像. 
    
    import os, time
    from ranger.core.loader import Loadable
    from ranger.ext.signals import SignalDispatcher
    from ranger.ext.shell_escape import *
    
    class MountLoader(Loadable, SignalDispatcher):
        """
        Wait until a directory is mounted
        """
        def __init__(self, path):
            SignalDispatcher.__init__(self)
            descr = "Waiting for dir '" + path + "' to be mounted"
            Loadable.__init__(self, self.generate(), descr)
            self.path = path
    
        def generate(self):
            available = False
            while not available:
                try:
                    if os.path.ismount(self.path):
                        available = True
                except:
                    pass
                yield
                time.sleep(0.03)
            self.signal_emit('after')
    
    class mount(Command):
        def execute(self):
            selected_files = self.fm.env.cwd.get_selection()
    
            if not selected_files:
                return
    
            space = ' '
            self.fm.execute_command("cdemu -b system unload 0")
            self.fm.execute_command("cdemu -b system load 0 " + \
                    space.join([shell_escape(f.path) for f in selected_files]))
    
            mountpath = "/media/virtualrom/"
    
            def mount_finished(path):
                currenttab = self.fm.current_tab
                self.fm.tab_open(9, mountpath)
                self.fm.tab_open(currenttab)
    
            obj = MountLoader(mountpath)
            obj.signal_bind('after', mount_finished)
            self.fm.loader.add(obj)

###  PDF文件预览

默认情况下，`ranger` 会以文本的形式预览PDF文件。然后，你可以通过先将PDF文件转换为图片，再以图片的方式预览PDF文件。`ranger` 将图片预览保存在 `~/.cache/ranger/` 目录下。你需要手动创建这个目录，或者在`~/.config/ranger/rc.conf` 将 `preview_images` 设置为 `true` 来让 `ranger` 在下一次启动时自动创建这个目录。然而，请注意你并不需要将 `preview_images` 一直设置为 `true` 来以图片的方式预览 PDF 文件，只要有 `~/.cache/ranger` 就可以了。 

为了启用这个功能，你可以在 `/usr/share/doc/ranger/config/scope.sh` 去掉相应行的注释，或者在你本地文件 `~/.config/ranger/scope.sh` 中增加/取消注释这些行。 

###  在当前目录打开新标签

你可能已经注意到有两个快捷键能够以家目录为默认目录创建新的标签 (`gn` 和 `Ctrl+n`)。不妨重新绑定 `Ctrl+n`: 
    
    rc.conf
    
    map <c-n>  eval fm.tab_new('%d')
    
###  Shell 提示

####  目录同步

_ranger_ 提供了一个 shell [function](<../zh-cn/Bash/%E5%87%BD%E6%95%B0.html> "Bash/Functions") `/usr/share/doc/ranger/examples/shell_automatic_cd.sh`. 执行 `ranger_cd` 会自动切换到最后一次浏览的目录. 

如果你的ranger是从一个终端模拟器启动的(比如`$TERMCMD -e ranger`, 其中 TERMCMD 是某个X终端), 你将无法使用 `ranger_cd`. 请创建以下可执行脚本： 
    
    ranger-launcher.sh
    
    #!/bin/sh
    export RANGERCD=true
    $TERMCMD
    
并在你的shell配置文件追加以下内容: 
    
    ._shell_ rc
    
    $RANGERCD && unset RANGERCD && ranger_cd
    
只在设置了`RANGERCD`变量的情况下才会启动`ranger_cd`. 其中`unset RANGERCD`是必要的, 否则在终端中启动一个subshell将会重新启动`ranger`. 

####  阻止嵌套 ranger 实例

使用快捷键 `S` 以在当前目录启动一个 shell，当您退出 shell 时则会回到 ranger。 

然而，您可能会忘记您处于 ranger 启动的 shell 中，导致在需要使用 ranger 时又在 ranger shell 中启动了新的 ranger 实例，造成嵌套。 

欲阻止该行为，您可以在您的 [shell 的配置文件](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "命令行解释器")添加以下函数： 
    
    ranger() {
        if [ -z "$RANGER_LEVEL" ]; then
            /usr/bin/ranger "$@"
        else
            exit
        fi
    }
    
##  参见

  * [BBS thread](<https://bbs.archlinux.org/viewtopic.php?id=93025>)
  * [DotShare.it configurations](<http://dotshare.it/category/fms/ranger/>)
  * [GitHub](<https://github.com/hut/ranger>)
  * [Installing and using ranger](<https://www.digitalocean.com/community/tutorials/installing-and-using-ranger-a-terminal-file-manager-on-a-ubuntu-vps>)
  * [Mailing list](<https://lists.nongnu.org/mailman/listinfo/ranger-users>)
  * [Official website](<https://nongnu.org/ranger>)
  * [Ranger tutorial](<http://bloerg.net/posts/ranger-file-manager/>)
