**翻译状态：**

  * 本文（或部分内容）译自 [PHP package guidelines](<https://wiki.archlinux.org/title/PHP_package_guidelines> "arch:PHP package guidelines")，最近一次同步于 2020-05-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/PHP_package_guidelines?diff=0&oldid=614505>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PHP_package_guidelines_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")**

* * *

[32 位](<../zh-cn/32_%E4%BD%8D%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "32位软件包打包准则") – [安全](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99/%E5%AE%89%E5%85%A8.html> "Arch 打包准则/安全") – [CLR](<../zh-cn/CLR_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CLR 软件打包准则") – [CMake](<../zh-cn/CMake_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CMake 软件打包准则") – [DKMS](<../zh-cn/DKMS_%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "DKMS 软件包打包准则") – [Eclipse](<../zh-cn/Eclipse_%E6%8F%92%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Eclipse 插件打包准则") – [Electron](<../zh-cn/Electron_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Electron 打包准则") – [Free Pascal](<../zh-cn/Free_Pascal_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Free Pascal 打包准则") – [GNOME](</wzh/index.php?title=GNOME_package_guidelines&action=edit&redlink=1> "GNOME package guidelines（页面不存在）") – [Go](<../zh-cn/Go_%E8%AF%AD%E8%A8%80%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Go 语言软件打包准则") – [Haskell](<../zh-cn/Haskell_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Haskell 打包准则") – [Java](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Java 打包准则") – [交叉编译工具](<../zh-cn/%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%E5%B7%A5%E5%85%B7%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "交叉编译工具打包准则") – [KDE](<../zh-cn/KDE_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "KDE 软件打包准则") – [Lisp](</wzh/index.php?title=Lisp_package_guidelines&action=edit&redlink=1> "Lisp package guidelines（页面不存在）") – [Meson](</wzh/index.php?title=Meson_package_guidelines&action=edit&redlink=1> "Meson package guidelines（页面不存在）") – [MinGW](</wzh/index.php?title=MinGW_package_guidelines&action=edit&redlink=1> "MinGW package guidelines（页面不存在）") – [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "内核模块打包指南") – [Node.js](<../zh-cn/Node.js_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Node.js 打包准则") – [Nonfree](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）") – [OCaml](<../zh-cn/OCaml_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "OCaml 打包准则") – [Perl](</wzh/index.php?title=Perl_package_guidelines&action=edit&redlink=1> "Perl package guidelines（页面不存在）") – PHP – [Python](<../zh-cn/Python_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Python 打包准则") – [R](<../zh-cn/R_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "R 软件打包准则") – [Ruby](</wzh/index.php?title=Ruby_package_guidelines&action=edit&redlink=1> "Ruby package guidelines（页面不存在）") – [Rust](<../zh-cn/Rust_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Rust 软件打包准则") – [Shell](</wzh/index.php?title=Shell_package_guidelines&action=edit&redlink=1> "Shell package guidelines（页面不存在）") – [VCS](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则") – [Web](</wzh/index.php?title=Web_application_package_guidelines&action=edit&redlink=1> "Web application package guidelines（页面不存在）") – [Wine](<../zh-cn/Wine_package_guidelines.html> "Wine package guidelines") – [字体](<../zh-cn/%E5%AD%97%E4%BD%93%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "字体打包指南")

本文档介绍了为 PHP 库创建 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 的过程。本文档的目标读者是 PHP 库的打包人员。对于 PHP Web 应用程序，请参阅 [Web application package guidelines](</wzh/index.php?title=Web_application_package_guidelines&action=edit&redlink=1> "Web application package guidelines（页面不存在）")

##  软件包名称

对于模块，软件包名称应以 `php-` 开头，其余名称应通过将库名称转换为小写字母并用连字符分隔来从库名称构造。 例如，与 `File iterator` 相对应的软件包名称将是 `php-file-iterator`。 

##  打包文件的位置

PHP 软件包应将文件安装到 `/usr/share/php/` 中。此路径应位于 php.ini include_path 或 open_basedir 指令中，以便能够在 PHP Web 应用程序中包含库文件。 

##  体系架构

在大多数情况下，`arch` 数组应包含 `'any'` ，因为大多数 PHP 软件包都是与体系架构无关的。 
