**翻译状态：**

  * 本文（或部分内容）译自 [ImageMagick](<https://wiki.archlinux.org/title/ImageMagick> "arch:ImageMagick")，最近一次同步于 2025-02-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/ImageMagick?diff=0&oldid=826199>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ImageMagick_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

根据[英文维基百科](<https://en.wikipedia.org/wiki/ImageMagick> "wikipedia:ImageMagick")： 

    ImageMagick is a free and open-source software suite for displaying, converting, and editing raster image and vector image files. It can read and write over 200 image file formats.

    （译文）ImageMagick 是一款自由及开放源代码的软件套件，用于显示、转换及编辑位图图像和矢量图像文件。它能够读写超过 200 种不同的图像文件格式。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [imagemagick](<https://archlinux.org/packages/?name=imagemagick>)包。或者通过 [graphicsmagick](<https://archlinux.org/packages/?name=graphicsmagick>)包 安装 [GraphicsMagick](<https://en.wikipedia.org/wiki/GraphicsMagick> "wikipedia:GraphicsMagick")⸺ImageMagick 的分支，强调 API 和命令行界面的稳定性。 

##  使用方法

参见 [ImageMagick(1)](<https://man.archlinux.org/man/ImageMagick.1>)，或使用 [gm(1)](<https://man.archlinux.org/man/gm.1>) 查看 GraphicsMagick 的手册页。 

**提示：** 安装软件包后，可在本地访问官方 HTML 文档： 

  * ImageMagick 的文档路径为 `/usr/share/doc/ImageMagick-7/www/index.html`
  * GraphicsMagick 的文档路径为 `/usr/share/doc/GraphicsMagick/www/index.html`

###  常见操作

**注意：** 参数前的符号非常重要。用“+”代替“-”可以执行相反操作。

####  格式转换

ImageMagick 通过文件扩展名确定格式。例如，要将给定的 _.png_ 图像转换为 _.jpg_ 格式，需要使用： 
    
    $ magick 图像.png 图像.jpg
    
####  拼接

将多张图片拼接为一张： 
    
    $ magick -append 输入1.png 输入2.png ... 输出.png
    
####  裁剪与切除

对多张图像进行裁剪并转换格式： 
    
    $ mogrify -crop _宽_ x _高_ +_X_ +_Y_ -format jpg *.png
    
其中 _宽_ 和 _高_ 表示裁剪后的输出图像尺寸， _X_ 和 _Y_ 表示相对于输入图像的偏移量。 

也可使用 `-chop`，通过 -gravity 参数切除指定单侧边框，这种方式无需复杂坐标计算，操作更简便： 
    
    $ magick 红色边框.gif -gravity South -chop 0x10 切除底部.gif
    
####  限制文件大小

在指定文件大小下获得合理画质： 
    
    $ magick 图像.jpg -define jpeg:extent=3000KB 压缩图像.jpg
    
这有助于缩短传输时间。注意 `-quality` 参数（如以下用法：） 
    
    $ magick 图像.jpg -quality 85% 压缩图像.jpg
    
当画质与文件大小的对应关系不明确时难以使用。 

###  截屏

使用 [import(1)](<https://man.archlinux.org/man/import.1>) 命令便捷截取当前系统屏幕： 
    
    $ import -window root screenshot.jpg
    
若不带 `-window` 参数运行 `import`，可交互式地选择窗口或其它任意区域。使用 `-pause` 参数设置延时，在此期间可执行操作（例如最小化某些窗口）。 

**注意：** 若需使用 **graphicsmagick** 的等效功能，只需在命令前添加 "gm"，例如 `$ gm import -window root screenshot.jpg`。

####  在 X11 中进行多屏幕截屏

若使用双屏模式（twinview）或双头输出（dualhead），可分别截取两个屏幕后再使用 imagemagick 拼接： 
    
    $ import -window root -display :0.0 -screen /tmp/0.png
    $ import -window root -display :0.1 -screen /tmp/1.png
    $ convert +append /tmp/0.png /tmp/1.png 截屏.png
    $ rm /tmp/{0,1}.png
    
####  使用 Xinerama 时截取单个物理屏幕

使用 Xinerama 进行的多显示器配置仅存在单个虚拟屏幕。当物理屏幕高度不一致时，截图会产生无效区域。此时可单独截取每个物理屏幕（需确保 X 服务器提供 Xinerama 信息）： 
    
    #!/bin/sh
    xdpyinfo -ext XINERAMA | sed '/^  head #/!d;s///' |
    while IFS=' :x@,' read i w h x y; do
            import -window root -crop ${w}x$h+$x+$y 显示屏$i.png
    done
    
####  对活动（焦点所在）窗口截屏

以下脚本可截取当前活动窗口，适用于支持 EWMH（NetWM）的 X 窗口管理器。为了避免覆盖之前的截图，此处将当前日期用作文件名。 
    
    #!/bin/sh
    activeWinLine=$(xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)")
    activeWinId=${activeWinLine:40}
    import -window "$activeWinId" /tmp/$(date +%F_%H%M%S_%N).png
    
另外，无论是否支持 EWMH，以下方法应该都可行： 
    
    $ import -window "$(xdotool getwindowfocus -f)" /tmp/$(date +%F_%H%M%S_%N).png
    
**注意：** 如果某些程序（例如 [zathura](</wzh/index.php?title=Zathura&action=edit&redlink=1> "Zathura（页面不存在）")（英语：[zathura](<https://wiki.archlinux.org/title/zathura> "en:zathura")））的截图显示为空白，请尝试在 `xdotool` 命令后添加 `-frame` 或移除 `-f`。

###  加密图像数据

加密方法： 
    
    $ echo [_密码词组_](<https://zh.wikipedia.org/wiki/%E5%AF%86%E7%A0%81%E8%AF%8D%E7%BB%84> "zhwp:密码词组") | magick _图像.jpg_ -encipher - -depth 8 png24:_图像.png_
    
解密方法： 
    
    $ echo _密码词组_ | magick _图像.png_ -decipher - _图像.jpg_
    
有关此类命令可能遇到的各种问题及优化建议（如加密后文件格式的指定），参见官方文档 [Encrypting Image Data](<https://usage.imagemagick.org/transform/#encipher>)。 

一些图像格式的元数据支持 `cipher` 标签，可用于检测图像是否加密，但该标签可能被 EXIF 编辑工具移除或伪造。 
    
    $ identify -verbose image.png
    
通用的检测方法可通过分析像素分量分布实现：若其熵值超过特定阈值，数据可视为随机（即可能经过加密）。但需注意[菱形平方算法](<https://en.wikipedia.org/wiki/Diamond-square_algorithm> "wikipedia:Diamond-square algorithm")生成的图像也会产生类似特征，属于典型误判案例。 

##  用图像创建 PDF

参见 [PDF、PS 与 DjVu#用图像创建 PDF](<../zh-cn/PDF%E3%80%81PS_%E4%B8%8E_DjVu.html#%E7%94%A8%E5%9B%BE%E5%83%8F%E5%88%9B%E5%BB%BA_PDF> "PDF、PS 与 DjVu")。有关背景信息，参见[此 Stack Exchange 帖子](<https://unix.stackexchange.com/questions/42856/how-can-i-convert-a-png-to-a-pdf-in-high-quality-so-its-not-blurry-or-fuzzy>)。 

##  另见

  * [ImageMagick 官网](<https://www.imagemagick.org/>)，提供了广泛的参数列表、[示例](<https://usage.imagemagick.org/>)和[展示](<https://imagemagick.org/script/examples.php>)
  * [应用程序列表/多媒体#图像处理](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html#%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86> "应用程序列表/多媒体")
  * [Fred's ImageMagick Scripts](<http://www.fmwconcepts.com/imagemagick/index.php>)，包含大量的 ImageMagick 脚本
