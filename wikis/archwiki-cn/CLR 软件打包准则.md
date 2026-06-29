**翻译状态：**

  * 本文（或部分内容）译自 [CLR package guidelines](<https://wiki.archlinux.org/title/CLR_package_guidelines> "arch:CLR package guidelines")，最近一次同步于 2020-05-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/CLR_package_guidelines?diff=0&oldid=610310>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/CLR_package_guidelines_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")**

* * *

[32 位](<../zh-cn/32_%E4%BD%8D%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "32位软件包打包准则") – [安全](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99/%E5%AE%89%E5%85%A8.html> "Arch 打包准则/安全") – CLR – [CMake](<../zh-cn/CMake_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CMake 软件打包准则") – [DKMS](<../zh-cn/DKMS_%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "DKMS 软件包打包准则") – [Eclipse](<../zh-cn/Eclipse_%E6%8F%92%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Eclipse 插件打包准则") – [Electron](<../zh-cn/Electron_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Electron 打包准则") – [Free Pascal](<../zh-cn/Free_Pascal_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Free Pascal 打包准则") – [GNOME](</wzh/index.php?title=GNOME_package_guidelines&action=edit&redlink=1> "GNOME package guidelines（页面不存在）") – [Go](<../zh-cn/Go_%E8%AF%AD%E8%A8%80%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Go 语言软件打包准则") – [Haskell](<../zh-cn/Haskell_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Haskell 打包准则") – [Java](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Java 打包准则") – [交叉编译工具](<../zh-cn/%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%E5%B7%A5%E5%85%B7%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "交叉编译工具打包准则") – [KDE](<../zh-cn/KDE_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "KDE 软件打包准则") – [Lisp](</wzh/index.php?title=Lisp_package_guidelines&action=edit&redlink=1> "Lisp package guidelines（页面不存在）") – [Meson](</wzh/index.php?title=Meson_package_guidelines&action=edit&redlink=1> "Meson package guidelines（页面不存在）") – [MinGW](</wzh/index.php?title=MinGW_package_guidelines&action=edit&redlink=1> "MinGW package guidelines（页面不存在）") – [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "内核模块打包指南") – [Node.js](<../zh-cn/Node.js_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Node.js 打包准则") – [Nonfree](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）") – [OCaml](<../zh-cn/OCaml_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "OCaml 打包准则") – [Perl](</wzh/index.php?title=Perl_package_guidelines&action=edit&redlink=1> "Perl package guidelines（页面不存在）") – [PHP](<../zh-cn/PHP_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "PHP 打包准则") – [Python](<../zh-cn/Python_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Python 打包准则") – [R](<../zh-cn/R_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "R 软件打包准则") – [Ruby](</wzh/index.php?title=Ruby_package_guidelines&action=edit&redlink=1> "Ruby package guidelines（页面不存在）") – [Rust](<../zh-cn/Rust_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Rust 软件打包准则") – [Shell](</wzh/index.php?title=Shell_package_guidelines&action=edit&redlink=1> "Shell package guidelines（页面不存在）") – [VCS](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则") – [Web](</wzh/index.php?title=Web_application_package_guidelines&action=edit&redlink=1> "Web application package guidelines（页面不存在）") – [Wine](<../zh-cn/Wine_package_guidelines.html> "Wine package guidelines") – [字体](<../zh-cn/%E5%AD%97%E4%BD%93%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "字体打包指南")

本文档定义了在 Arch Linux 下打包 Common Language Runtime （.NET）项目的标准。当前，只有 [Mono](<../zh-cn/Mono.html> "Mono") 能够为多个系统提供可用的，高效的 CLR runtime，并且该标准将反映其用法。请注意，许多 CLR 程序是在考虑到 Microsoft .NET 的情况下开发的，因此，由于 P/Invoke 调用和 Microsoft 数字版权管理（DRM）API 等 .NET 专有的因素，它们可能在 Mono 下运行，也可能无法在 Mono 下运行。因此不会为 Arch Linux 提供可用的软件包。但是，如果与 1.5.6 版（？）或更高版本的 [Wine](<../zh-cn/Wine.html> "Wine") 结合使用，则您的程序包可能有机会在其下运行。如果是这种情况，请参阅 [Wine PKGBUILD Guidelines](</wzh/index.php?title=Wine_PKGBUILD_Guidelines&action=edit&redlink=1> "Wine PKGBUILD Guidelines（页面不存在）") 以获取更多信息。 

##  打包注意

  * 始终将 [mono](<https://archlinux.org/packages/?name=mono>)包 添加到 `depends`
  * 始终设置 `arch` 为 `any`。Mono 尚不支持编译（运行）64-bit 程序集。
  * 始终添加 `!strip` 到 `options`
  * 如果程序包是一个库（DLL），则要将该程序包用作依赖项，请考虑将其安装到 Mono 的全局程序集缓存（GAC）中。
  * 如果程序集是预编译的，并且带有程序调试数据库文件（Foo.dll.pdb），请考虑将其转换为：{ic|pdb2mdb Foo.dll}}
  * 如果要执行该程序包（EXE），请确保安装到 `/usr/bin` ，使用 shell 脚本以运行它，类似于以下程序：

    #!/bin/sh
    mono foo.exe "$@"
    
###  签名的程序集

如果要将软件包安装到 GAC 中，请确保它具有签名的密钥文件。如果没有，您可以生成一个这样的：`sn -k 1024 Foo.snk`。随后，嵌入密钥文件到组件的最简单方法是拆卸它，是这样的：`monodis Foo.dll --output=Foo.il`。然后，像这样重新组装它：`ilasm /dll /key:Foo.snk Foo.il`

##  PKGBUILD 示例

以下示例将尝试涵盖一些最常见的约定和构建系统。 

### xbuild

####  未签名的 DLL
    
    # Maintainer: yourname <yourmail>
    pkgname=foo
    pkgver=1.0
    pkgrel=1
    pkgdesc="Fantabulous library for .Net"
    arch=('any')
    url="http://www.foo.bar"
    license=('GPL')
    depends=('mono')
    options=('!strip')
    source=("http://www.foo.bar/foobar.tar.gz")
    md5sums=('4736ac4f34fd9a41fa0197eac23bbc24')
    
    build() {
      cd "${srcdir}/foobar"
    
      xbuild Foo.sln
    
      # if the package is unsigned, do the following:
      cd "/bin/x86/Debug"
      monodis Foo.dll --output=Foo.il
      sn -k 1024 Foo.snk
      ilasm /dll /key:Foo.snk Foo.il
    }
    
    package() {
      cd "${srcdir}/foobar/bin/x86/Debug"
    
      install -Dm644 Foo.dll "$pkgdir/usr/lib/foobar/Foo.dll"
      install -Dm644 Foo.dll.mdb "$pkgdir/usr/lib/foobar/Foo.dll.mdb"
      
      # Register assembly into Mono's GAC
      gacutil -i Foo.dll -root "$pkgdir/usr/lib"
    }
    