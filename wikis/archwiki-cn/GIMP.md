**翻译状态：**

  * 本文（或部分内容）译自 [GIMP](<https://wiki.archlinux.org/title/GIMP> "arch:GIMP")，最近一次同步于 2024-09-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/GIMP?diff=0&oldid=754115>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GIMP_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [GIMP/CMYK support](</wzh/index.php?title=GIMP/CMYK_support&action=edit&redlink=1> "GIMP/CMYK support（页面不存在）")
  * [应用程序列表/多媒体#光栅图形编辑器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html#%E5%85%89%E6%A0%85%E5%9B%BE%E5%BD%A2%E7%BC%96%E8%BE%91%E5%99%A8> "应用程序列表/多媒体")

[GIMP](<https://en.wikipedia.org/wiki/GIMP> "wikipedia:GIMP") 是一款功能强大的位图图像编辑程序，常用于照片处理、图像处理以及常规的平面设计工作。它可以作为简单的绘画程序使用，也可以作为专业级的照片处理程序，还可以作为在线批量处理系统，包括可批量作业的图像渲染工具及图像格式转换工具等。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gimp](<https://archlinux.org/packages/?name=gimp>)包 软件包。 

##  提示和技巧

###  照片添加文字说明

要给图像加标题说明，请输入所需的文字后，选中文字所在的图层，然后按照以下步骤操作： 

  1. 点击菜单 _图层_ > _文字到路径_
  2. 点击菜单 _选择_ > _从路径_
  3. 点击菜单 _选择_ > _反转_
  4. 点击菜单 _编辑_ > _勾画路径_

###  画一个圆

GIMP中画圆请按以下步骤操作: 

  1. 选择 _椭圆工具_ 然后按住 `Shift` 键不松手在图像上拖动鼠标
  2. 点击菜单 _编辑_ > _以前/背景色填充_
  3. 点击菜单 _选择_ > _收缩_
  4. 按键盘上的 `Delete` 键

**提示：** _增长_ 和 _边界_ 可以达到相同效果

###  Photoshop用户习惯

GIMP 的可配置性很强，可以自定义快捷键，甚至用户界面，这个功能会极大方便那些习惯使用 [Photoshop](<https://en.wikipedia.org/wiki/Adobe_Photoshop> "wikipedia:Adobe Photoshop") 的用户。 

具体来说，可以在 GIMP 上安装 [GimpPs](<https://github.com/doctormo/GimpPs>) 主题，该主题旨在让 GIMP 的外观更接近 Photoshop。 

另外，如果你只是想使用快捷键配置，可在主题的 `menurc` 文件中找到相关配置信息，然后将其添加到本地的配置文件 `~/.config/GIMP/2.10/menurc` 中。 

另一个类似的项目也可参阅：[PhotoGIMP](<https://github.com/Diolinux/PhotoGIMP>)。 

##  插件

GIMP 拥有庞大的[插件系统](<https://docs.gimp.org/en/gimp-scripting.html>)和一个用于编写 _Script-Fu_ （[GIMP 文档：Script-Fu 相关概念](<https://docs.gimp.org/en/gimp-concepts-script-fu.html>)）脚本的 [Scheme](<../zh-cn/Scheme.html> "Scheme") 解释器。 

大多数插件通过[官方仓库](<https://archlinux.org/packages/?sort=&q=gimp-plugin>)（如 [gimp-plugin-gmic](<https://archlinux.org/packages/?name=gimp-plugin-gmic>)包）和 [AUR](<https://aur.archlinux.org/packages?K=gimp-plugin>) 分发，其中一部分以 [gimp](<https://archlinux.org/packages/?name=gimp>)包 软件包的可选依赖列出。 

**注意：** Python-Fu 插件在由官方仓库分发的 GIMP 版本上无法使用，因其需要 [python2](<https://aur.archlinux.org/packages/python2/>)AUR（生命周期已于 2020 年结束）。要恢复其功能，可使用 [python2-gimp](<https://aur.archlinux.org/packages/python2-gimp/>)AUR。

###  手动安装

若插件并非由仓库分发，可使用 `gimptool` 编译并安装。 

从源代码安装一个插件： 
    
    $ gimptool --install source.c

安装一个预编译插件： 
    
    $ gimptool --install-bin executable

安装一个 Script-Fu 脚本： 
    
    $ gimptool --install-script script.scm

更多选项参见 `gimptool --help` 的输出。 

###  打包

插件包的文件应在 `/usr/lib/gimp/2.0/plug-ins/` 目录下与所属插件同名的目录内。 

##  故障排除

###  绿色文字

如果启用了抗锯齿功能后，你在字母周围看到有绿色，请在 `~/.config/GIMP/2.10/fonts.conf` 中添加以下内容： 
    
    ~/.config/GIMP/2.10/fonts.conf
    
    <?xml version='1.0'?>
    <!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
    <fontconfig>
      <match target="font">
        <edit name="rgba" mode="assign">
          <const>none</const>
        </edit>
      </match>
    </fontconfig>

###  隐藏Noto字体

如果你已经安装了 [noto-fonts](<https://archlinux.org/packages/?name=noto-fonts>)包 字体，并且希望把此字体从 GIMP 的字体列表中移除，请在 `~/.config/GIMP/2.10/fonts.conf` 中添加以下内容： 
    
    ~/.config/GIMP/2.10/fonts.conf
    
    <?xml version='1.0'?>
    <!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
    <fontconfig>
      <rejectfont>
        <glob>/usr/share/fonts/noto</glob>
      </rejectfont>
    </fontconfig>

更多信息请参考 [fonts-conf(5)](<https://man.archlinux.org/man/fonts-conf.5>) 和[字体白名单与黑名单配置](<../zh-cn/Font_configuration.html#Whitelisting_and_blacklisting_fonts> "Font configuration")。 

###  PDF文件

GIMP 需要使用 [poppler-glib](<https://archlinux.org/packages/?name=poppler-glib>)包 库来打开 PDF 文件，否则会无法识别这些文件。 

由于 GIMP 从一开始就对 PDF 文件进行光栅化，所以在编辑 PDF 文件时，它不会利用 PDF 的固有功能。其它程序（比如 [LibreOffice Draw](<../zh-cn/LibreOffice.html> "LibreOffice")）在编辑 PDF 文件方面可能表现更好。 

##  参阅

  * [官方网站](<https://www.gimp.org>)
  * [debian:GIMP](<https://wiki.debian.org/GIMP> "debian:GIMP")
  * [GIMP 论坛](<https://gimp-forum.net>)
