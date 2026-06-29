**翻译状态：**

  * 本文（或部分内容）译自 [Java Runtime Environment fonts](<https://wiki.archlinux.org/title/Java_Runtime_Environment_fonts> "arch:Java Runtime Environment fonts")，最近一次同步于 2019-3-8，若英文版本有所[更改](<https://wiki.archlinux.org/title/Java_Runtime_Environment_fonts?diff=0&oldid=568119>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Java_Runtime_Environment_fonts_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Fonts](<../zh-cn/%E5%AD%97%E4%BD%93.html> "Fonts")
  * [Font configuration](<../zh-cn/Font_configuration.html> "Font configuration")
  * [MS Fonts](<../zh-cn/MS_Fonts.html> "MS Fonts")
  * [X Logical Font Description](</wzh/index.php?title=X_Logical_Font_Description&action=edit&redlink=1> "X Logical Font Description（页面不存在）")

可能一部分人认为Java应用程序中的默认字体和字体的显示模式不大理想。下面有几种方法可以改进Oracle Java Runtime Environment (JRE)中的字体显示。这些方法可以单独使用，但是经过许多用户实践发现将它们组合使用可以获得更好的效果。 

Java对于TrueType格式字体的支持似乎是最好的。 

##  抗锯齿

###  基础设置

Linux上的Oracle Java 1.6和OpenJDK提供了字体的[抗锯齿](<https://en.wikipedia.org/wiki/Font_rasterization> "wikipedia:Font rasterization")功能。使用这个功能，请将以下内容添加到`/etc/environment`: 
    
    _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=_setting_ '
    
`_setting_` 是下面内容的其中一项: 

设置值  | 描述   
---|---  
`off`, `false`, `default` | 不开启抗锯齿   
`on` | 全效抗锯齿   
`gasp` | 使用字体文件自带的配置信息   
`lcd`, `lcd_hrgb` | 为流行的显示器调整过的抗锯齿   
`lcd_hbgr`, `lcd_vrgb`, `lcd_vbgr` | 替代显示器的设置   
  
`gasp` 和`lcd` 设置在大部分情况下表现良好。 

选择使用GTK的显示风格，请将下面的内容添加到.bashrc： 
    
    _JAVA_OPTIONS='-Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel'
    
**注意：**

  * 所描述的Java选项仅适用于使用Java绘制GUI的应用程序，如Jdownloader，而不适用于仅使用Java作为后端的应用程序，如Openoffice.org和Matlab。
  * “TrueType” 字体包含一个网格显示拟合和扫描转换过程的表(Grid-fitting And Scan-conversion Procedure “GASP”)，其中包含了字体作者对不同大小字体显示的建议。一些字号可以完全抗锯齿，一些只有部分提示，还有一些显示为位图。对于一些字号，上面的方法会组合使用。

在运行之前，在命令行中指定其他的变量，可以尝试别的配置: 
    
    _JAVA_OPTIONS=_options_ _executable_ 
    
你需要重新登录使配置生效。 

###  OpenJDK 补丁

即使通过Java选项强制执行了抗锯齿，得到的抗锯齿效果也可能不如本机应用程序。可以通过OpenJDK的一个补丁来弥补，[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")提供了这个补丁: 

  * 修补后的 **OpenJDK7** 可用 [jre7-openjdk-infinality](<https://aur.archlinux.org/packages/jre7-openjdk-infinality/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] (`

**模板错误：** 您在尝试使用 = 标志吗？ 有关解决方法，请访问 [Help:Template#Escape template-breaking characters](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#Escape_template-breaking_characters> "Help:Template")。

`)
  * 修补后的 **OpenJDK8** 可用 [jre8-openjdk-infinality](<https://aur.archlinux.org/packages/jre8-openjdk-infinality/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

修补后的版本从fontconfig获得FreeType类型字体的渲染和加载标志，而不是使用OpenJDK的方法。虽然这是一个[Infinality](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html> "Infinality")包，但是补丁本身实际上并不依赖于[fontconfig-Infinality](<https://aur.archlinux.org/packages/fontconfig-Infinality/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]，因为只使用了普通的[fontconfig](<https://archlinux.org/packages/?name=fontconfig>)包 api。 

##  选择字体

###  TrueType 字体

使一些应用程序知道所需字体的目录路径，那么这些Java应用程序就会使用特定的TrueType字体。TrueType字体安装在`/usr/share/fonts/TTF`目录中。将以下内容添加到`/etc/environment`以启用这些字体。 
    
    JAVA_FONTS=/usr/share/fonts/TTF
    
你需要重新登录使配置生效。 

###  修复乱码 (For JRE8)

将字体文件放在下面的目录下。如果目录不存在，则创建该目录。 
    
    /usr/lib/jvm/java-8-openjdk/jre/lib/fonts/fallback/
    