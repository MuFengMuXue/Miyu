**翻译状态：**

  * 本文（或部分内容）译自 [Haskell package guidelines](<https://wiki.archlinux.org/title/Haskell_package_guidelines> "arch:Haskell package guidelines")，最近一次同步于 2020-05-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Haskell_package_guidelines?diff=0&oldid=610337>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Haskell_package_guidelines_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")**

* * *

[32 位](<../zh-cn/32_%E4%BD%8D%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "32位软件包打包准则") – [安全](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99/%E5%AE%89%E5%85%A8.html> "Arch 打包准则/安全") – [CLR](<../zh-cn/CLR_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CLR 软件打包准则") – [CMake](<../zh-cn/CMake_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CMake 软件打包准则") – [DKMS](<../zh-cn/DKMS_%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "DKMS 软件包打包准则") – [Eclipse](<../zh-cn/Eclipse_%E6%8F%92%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Eclipse 插件打包准则") – [Electron](<../zh-cn/Electron_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Electron 打包准则") – [Free Pascal](<../zh-cn/Free_Pascal_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Free Pascal 打包准则") – [GNOME](</wzh/index.php?title=GNOME_package_guidelines&action=edit&redlink=1> "GNOME package guidelines（页面不存在）") – [Go](<../zh-cn/Go_%E8%AF%AD%E8%A8%80%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Go 语言软件打包准则") – Haskell – [Java](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Java 打包准则") – [交叉编译工具](<../zh-cn/%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%E5%B7%A5%E5%85%B7%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "交叉编译工具打包准则") – [KDE](<../zh-cn/KDE_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "KDE 软件打包准则") – [Lisp](</wzh/index.php?title=Lisp_package_guidelines&action=edit&redlink=1> "Lisp package guidelines（页面不存在）") – [Meson](</wzh/index.php?title=Meson_package_guidelines&action=edit&redlink=1> "Meson package guidelines（页面不存在）") – [MinGW](</wzh/index.php?title=MinGW_package_guidelines&action=edit&redlink=1> "MinGW package guidelines（页面不存在）") – [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "内核模块打包指南") – [Node.js](<../zh-cn/Node.js_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Node.js 打包准则") – [Nonfree](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）") – [OCaml](<../zh-cn/OCaml_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "OCaml 打包准则") – [Perl](</wzh/index.php?title=Perl_package_guidelines&action=edit&redlink=1> "Perl package guidelines（页面不存在）") – [PHP](<../zh-cn/PHP_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "PHP 打包准则") – [Python](<../zh-cn/Python_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Python 打包准则") – [R](<../zh-cn/R_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "R 软件打包准则") – [Ruby](</wzh/index.php?title=Ruby_package_guidelines&action=edit&redlink=1> "Ruby package guidelines（页面不存在）") – [Rust](<../zh-cn/Rust_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Rust 软件打包准则") – [Shell](</wzh/index.php?title=Shell_package_guidelines&action=edit&redlink=1> "Shell package guidelines（页面不存在）") – [VCS](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则") – [Web](</wzh/index.php?title=Web_application_package_guidelines&action=edit&redlink=1> "Web application package guidelines（页面不存在）") – [Wine](<../zh-cn/Wine_package_guidelines.html> "Wine package guidelines") – [字体](<../zh-cn/%E5%AD%97%E4%BD%93%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "字体打包指南")

本文档旨在涵盖在Arch上创建优质 [Haskell](</wzh/index.php?title=Haskell&action=edit&redlink=1> "Haskell（页面不存在）") [软件包](<../zh-cn/Creating_packages.html> "Creating packages")标准和准则。 

在撰写本文之前，请联系 [User:Felixonmars](</wzh/index.php?title=User:Felixonmars&action=edit&redlink=1> "User:Felixonmars（页面不存在）")

##  软件包命名

对于 Haskell 库，使用 `haskell-_libraryname_`，通常与 [hackage](<https://hackage.haskell.org/>) 相同。 

**注意：** 软件包名称应完全小写。

##  体系架构

参见 [PKGBUILD#arch](<../zh-cn/PKGBUILD.html#arch> "PKGBUILD")。 

每个 Haskell 库或程序都依赖于体系结构。 

##  来源

Haskell程序或库的首选来源是 [hackage](<https://hackage.haskell.org>)。[PKGBUILD#source](<../zh-cn/PKGBUILD.html#source> "PKGBUILD") `source=()` 数组应使用以下 URL 模板： 

    `https://hackage.haskell.org/packages/archive/$_hkgname/$pkgver/$_hkgname-$pkgver.tar.gz`

请注意，因为 Haskell 软件包通常以 haskell- 为前缀，所以使用自定义 _hkgname 变量而不是 pkgname 。通常可以如下定义此变量： 
    
    _hkgname=stm-delay
    
##  重建顺序

当 Haskell 库更改时，它的构建标志或被更新，所有依赖包都需要重建。 

##  PKGBUILD 库示例

打包 Haskell 库与打包 Haskell 程序不同，Arch Linux 中打包的库供打包的 Haskell 程序使用。 
    
    PKGBUILD
    
    # Contributor: Your Name <youremail@domain.com>
    _hkgname=stm-delay
    pkgname=haskell-stm-delay
    arch=('x86_64')
    url="https://hackage.haskell.org/package/$hkgname"
    depends=(ghc-libs)
    makedepends=(ghc)
    source=("https://hackage.haskell.org/packages/archive/$_hkgname/$pkgver/$_hkgname-$pkgver.tar.gz")
    
    build() {
      cd $_hkgname-$pkgver    
        
      runhaskell Setup configure -O --enable-shared --enable-executable-dynamic --disable-library-vanilla \
        --prefix=/usr --docdir=/usr/share/doc/$pkgname --enable-tests \
        --dynlibdir=/usr/lib --libsubdir=\$compiler/site-local/\$pkgid \
        --ghc-option=-optl-Wl\,-z\,relro\,-z\,now \
        --ghc-option='-pie'
    
      runhaskell Setup build
      runhaskell Setup register --gen-script
      runhaskell Setup unregister --gen-script
      sed -i -r -e "s|ghc-pkg.*update[^ ]* |&'--force' |" register.sh
      sed -i -r -e "s|ghc-pkg.*unregister[^ ]* |&'--force' |" unregister.sh
    }
    
    check() {
      cd $_hkgname-$pkgver
      runhaskell Setup test
    }
    
    package() {
      cd $_hkgname-$pkgver
    
      install -D -m744 register.sh "$pkgdir"/usr/share/haskell/register/$pkgname.sh
      install -D -m744 unregister.sh "$pkgdir"/usr/share/haskell/unregister/$pkgname.sh
      runhaskell Setup copy --destdir="$pkgdir"
      install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
      rm -f "${pkgdir}/usr/share/doc/${pkgname}/LICENSE"
    }
    