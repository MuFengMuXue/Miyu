**翻译状态：**

  * 本文（或部分内容）译自 [R package guidelines](<https://wiki.archlinux.org/title/R_package_guidelines> "arch:R package guidelines")，最近一次同步于 2024-5-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/R_package_guidelines?diff=0&oldid=808148>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/R_package_guidelines_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")**

* * *

[32 位](<../zh-cn/32_%E4%BD%8D%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "32位软件包打包准则") – [安全](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99/%E5%AE%89%E5%85%A8.html> "Arch 打包准则/安全") – [CLR](<../zh-cn/CLR_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CLR 软件打包准则") – [CMake](<../zh-cn/CMake_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CMake 软件打包准则") – [DKMS](<../zh-cn/DKMS_%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "DKMS 软件包打包准则") – [Eclipse](<../zh-cn/Eclipse_%E6%8F%92%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Eclipse 插件打包准则") – [Electron](<../zh-cn/Electron_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Electron 打包准则") – [Free Pascal](<../zh-cn/Free_Pascal_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Free Pascal 打包准则") – [GNOME](</wzh/index.php?title=GNOME_package_guidelines&action=edit&redlink=1> "GNOME package guidelines（页面不存在）") – [Go](<../zh-cn/Go_%E8%AF%AD%E8%A8%80%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Go 语言软件打包准则") – [Haskell](<../zh-cn/Haskell_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Haskell 打包准则") – [Java](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Java 打包准则") – [交叉编译工具](<../zh-cn/%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%E5%B7%A5%E5%85%B7%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "交叉编译工具打包准则") – [KDE](<../zh-cn/KDE_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "KDE 软件打包准则") – [Lisp](</wzh/index.php?title=Lisp_package_guidelines&action=edit&redlink=1> "Lisp package guidelines（页面不存在）") – [Meson](</wzh/index.php?title=Meson_package_guidelines&action=edit&redlink=1> "Meson package guidelines（页面不存在）") – [MinGW](</wzh/index.php?title=MinGW_package_guidelines&action=edit&redlink=1> "MinGW package guidelines（页面不存在）") – [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "内核模块打包指南") – [Node.js](<../zh-cn/Node.js_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Node.js 打包准则") – [Nonfree](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）") – [OCaml](<../zh-cn/OCaml_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "OCaml 打包准则") – [Perl](</wzh/index.php?title=Perl_package_guidelines&action=edit&redlink=1> "Perl package guidelines（页面不存在）") – [PHP](<../zh-cn/PHP_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "PHP 打包准则") – [Python](<../zh-cn/Python_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Python 打包准则") – R – [Ruby](</wzh/index.php?title=Ruby_package_guidelines&action=edit&redlink=1> "Ruby package guidelines（页面不存在）") – [Rust](<../zh-cn/Rust_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Rust 软件打包准则") – [Shell](</wzh/index.php?title=Shell_package_guidelines&action=edit&redlink=1> "Shell package guidelines（页面不存在）") – [VCS](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则") – [Web](</wzh/index.php?title=Web_application_package_guidelines&action=edit&redlink=1> "Web application package guidelines（页面不存在）") – [Wine](<../zh-cn/Wine_package_guidelines.html> "Wine package guidelines") – [字体](<../zh-cn/%E5%AD%97%E4%BD%93%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "字体打包指南")

本文档涵盖了为 [R](</wzh/index.php?title=R&action=edit&redlink=1> "R（页面不存在）") 软件包编写 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 的标准和指南。大多数信息可以通过查看软件包的 `DESCRIPTION` 文件获得。在 R 中运行 `tools::CRAN_package_db()` 可以获得大部分信息。您还可以访问 [CRAN](<https://cran.r-project.org/src/contrib/PACKAGES>)、[Bioconductor link1](<https://bioconductor.org/packages/release/bioc/src/contrib/PACKAGES>)与[Bioconductor link2](<https://bioconductor.org/packages/release/data/annotation/src/contrib/PACKAGES>)，了解所有 R 软件包的信息。 

##  软件包命名

软件包应命名为 `r-pkgname`，其中 pkgname 取自 `DESCRIPTION` 文件中的`Package`字段。软件包名称应小写。 

##  软件包版本号

从`Version`字段中获取。R 允许软件包在版本号中使用冒号和连字符，但在 PKGBUILD 中不允许。将其转换为句号或下划线。 

## Arch

请参见 [PKGBUILD#arch](<../zh-cn/PKGBUILD.html#arch> "PKGBUILD")。如果软件包的 CRAN 网页上有 `NeedsCompilation: yes`，那么它很可能是特定架构的。否则，很可能不是，参见 [PKGBUILD#arch](<../zh-cn/PKGBUILD.html#arch> "PKGBUILD")。 

##  依赖

在软件包 `DESCRIPTION` 文件的`Depends`、`Imports`或 `LinkingTo` 字段中列出的 R 软件包应列在[依赖项](<../zh-cn/PKGBUILD.html#depends> "PKGBUILD")下。 

`Suggests` 中列出的 R 软件包应列为 [optdepends](</wzh/index.php?title=Optdepends&action=edit&redlink=1> "Optdepends（页面不存在）")。 

有些软件包需要外部工具，这些工具列在 `SystemRequirements` 下。 

某些软件包需要[依赖](<../zh-cn/PKGBUILD.html#depends> "PKGBUILD") [gcc-fortran](<https://archlinux.org/packages/?name=gcc-fortran>)包，但它并不总是列在 `DESCRIPTION` 文件中。 

##  来源

CRAN 上的所有 R 软件包都可以在网站 `https://cran.r-project.org/src/contrib/_cranname_ __cranversion_.tar.gz` 上找到，其中 `_cranname_` 是 CRAN 上软件包的名称，` _cranversion_` 是 cran 的版本。 

Bioconductor 上可用的 R 软件包可从网站 `https://bioconductor.org/packages/release/bioc/src/contrib/_bcname_ __bcname_.tar.gz` 或 `https://bioconductor.org/packages/release/data/annotation/src/contrib/_bcname_ __bcname_.tar.gz` 上获取，其中 `_bcname_` 是 Bioconductor 上软件包的名称，` _bcver_` 是版本。 

##  构建与打包

R 内置支持构建软件包。下面是三个软件源的 `PKGBUILD` 模板： MRAN、CRAN 和 Bioconductor。MRAN 是 CRAN 的快照镜像，使用该模板即使软件包过期也能构建。 

### MRAN
    
    _cranname=
    _cranver=
    _updatedate=YYYY-MM-DD
    pkgname=r-${_cranname,,}
    pkgver=${_cranver//[:-]/.}
    pkgrel=1
    pkgdesc=""
    arch=()
    url="https://cran.r-project.org/package=${_cranname}"
    license=()
    depends=(r)
    makedepends=()
    optdepends=()
    source=("https://cran.microsoft.com/snapshot/${_updatedate}/src/contrib/${_cranname}_${_cranver}.tar.gz")
    sha256sums=(_)_
    
    build() {
      R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
    }
    
    package() {
      install -dm0755 "${pkgdir}/usr/lib/R/library"
    
      cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
    }
    
### CRAN
    
    _cranname=
    _cranver=
    pkgname=r-${_cranname,,}
    pkgver=${_cranver//[:-]/.}
    pkgrel=1
    pkgdesc=""
    arch=()
    url="https://cran.r-project.org/package=${_cranname}"
    license=()
    depends=(r)
    makedepends=()
    optdepends=()
    source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
    sha256sums=(_)_
    
    build() {
      R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
    }
    
    package() {
      install -dm0755 "${pkgdir}/usr/lib/R/library"
    
      cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
    }
    
### Bioconductor
    
    _bcname=
    _bcver=
    pkgname=r-${_bcname,,}
    pkgver=${_bcver//[:-]/.}
    pkgrel=1
    pkgdesc=""
    arch=()
    url="https://bioconductor.org/packages/${_bcname}"
    license=()
    depends=(r)
    makedepends=()
    optdepends=()
    source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_bcname}_${_bcver}.tar.gz")
    # or
    # source=("https://bioconductor.org/packages/release/data/annotation/src/contrib/${_bcname}_${_bcver}.tar.gz")
    sha256sums=(_)_
    
    build() {
      R CMD INSTALL ${_bcname}_${_bcver}.tar.gz -l "${srcdir}"
    }
    
    package() {
      install -dm0755 "${pkgdir}/usr/lib/R/library"
      
      cp -a --no-preserve=ownership "${_bcname}" "${pkgdir}/usr/lib/R/library"
    }
    
##  技巧与窍门

###  Bioconductor 存储库

欲轻松访问bioconductor软件包，可以添加 [bioarchlinux](<../zh-cn/Unofficial_user_repositories.html#bioarchlinux> "Unofficial user repositories") 软件源。 
