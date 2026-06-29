[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 尚有一些段落未翻译完全（在 [Talk:OCaml 打包准则#](<../zh-cn/Talk:OCaml_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html>) 中讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [OCaml package guidelines](<https://wiki.archlinux.org/title/OCaml_package_guidelines> "arch:OCaml package guidelines")，最近一次同步于 2025-07-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/OCaml_package_guidelines?diff=0&oldid=812144>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/OCaml_package_guidelines_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")**

* * *

[32 位](<../zh-cn/32_%E4%BD%8D%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "32位软件包打包准则") – [安全](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99/%E5%AE%89%E5%85%A8.html> "Arch 打包准则/安全") – [CLR](<../zh-cn/CLR_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CLR 软件打包准则") – [CMake](<../zh-cn/CMake_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CMake 软件打包准则") – [DKMS](<../zh-cn/DKMS_%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "DKMS 软件包打包准则") – [Eclipse](<../zh-cn/Eclipse_%E6%8F%92%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Eclipse 插件打包准则") – [Electron](<../zh-cn/Electron_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Electron 打包准则") – [Free Pascal](<../zh-cn/Free_Pascal_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Free Pascal 打包准则") – [GNOME](</wzh/index.php?title=GNOME_package_guidelines&action=edit&redlink=1> "GNOME package guidelines（页面不存在）") – [Go](<../zh-cn/Go_%E8%AF%AD%E8%A8%80%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Go 语言软件打包准则") – [Haskell](<../zh-cn/Haskell_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Haskell 打包准则") – [Java](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Java 打包准则") – [交叉编译工具](<../zh-cn/%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%E5%B7%A5%E5%85%B7%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "交叉编译工具打包准则") – [KDE](<../zh-cn/KDE_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "KDE 软件打包准则") – [Lisp](</wzh/index.php?title=Lisp_package_guidelines&action=edit&redlink=1> "Lisp package guidelines（页面不存在）") – [Meson](</wzh/index.php?title=Meson_package_guidelines&action=edit&redlink=1> "Meson package guidelines（页面不存在）") – [MinGW](</wzh/index.php?title=MinGW_package_guidelines&action=edit&redlink=1> "MinGW package guidelines（页面不存在）") – [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "内核模块打包指南") – [Node.js](<../zh-cn/Node.js_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Node.js 打包准则") – [Nonfree](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）") – OCaml – [Perl](</wzh/index.php?title=Perl_package_guidelines&action=edit&redlink=1> "Perl package guidelines（页面不存在）") – [PHP](<../zh-cn/PHP_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "PHP 打包准则") – [Python](<../zh-cn/Python_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Python 打包准则") – [R](<../zh-cn/R_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "R 软件打包准则") – [Ruby](</wzh/index.php?title=Ruby_package_guidelines&action=edit&redlink=1> "Ruby package guidelines（页面不存在）") – [Rust](<../zh-cn/Rust_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Rust 软件打包准则") – [Shell](</wzh/index.php?title=Shell_package_guidelines&action=edit&redlink=1> "Shell package guidelines（页面不存在）") – [VCS](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则") – [Web](</wzh/index.php?title=Web_application_package_guidelines&action=edit&redlink=1> "Web application package guidelines（页面不存在）") – [Wine](<../zh-cn/Wine_package_guidelines.html> "Wine package guidelines") – [字体](<../zh-cn/%E5%AD%97%E4%BD%93%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "字体打包指南")

为使用 [OCaml](<https://en.wikipedia.org/wiki/OCaml> "wikipedia:OCaml") 编写的软件创建 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")。 

##  命名

若是库则采用 `ocaml-_modulename_` 的格式，若是程序则采用程序名。不论如何，名字都应当是全小写的。 

##  文件的位置

###  库

OCaml 库应当安装到 `/usr/lib/ocaml`。到 `/usr/lib/ocaml/site-lib` 已经弃用。 

OCaml 库应当使用 [ocaml-findlib](<https://archlinux.org/packages/?name=ocaml-findlib>)包 来安装。`ocaml-findlib` 在包种包含了元信息来使库管理更加简单。这是一种惯例，现在很多 OCaml 都需要它。 

`ocaml-findlib` 从应被包含在源码包中的 `META` 的文件中取出必要的数据。If this file is not included, one should either be obtained from the corresponding Debian, Ubuntu, or Fedora package, or created for the package by the maintainer. A request to include the file should also be made to the upstream developers of the package. 

The `OCAMLFIND_DESTDIR` variable should be used when installing packages with `ocaml-findlib`. See the example PKGBUILD below for details. 

### OASIS

OCaml packages that install executables using OASIS ignore `DESTDIR`. This is a known limitation of OASIS ([issue #493](<https://github.com/ocaml/oasis/issues/493>)). One way to enable `DESTDIR`-like functionality is to run the `configure` script with the `--destdir` argument, like so: 
    
    build() {
        cd "${srcname}-${pkgver}"
        ./configure --prefix /usr --destdir "$pkgdir"
    
        # build commands
    }
    
## OCaml bytecode and levels

OCaml can run code on multiple "levels", the top level interprets OCaml Code without compiling, the bytecode level creates machine independent bytecode and the native level creates machine code binaries (just like C/C++). 

When building OCaml Packages you need to be aware if the build process is compiling native machine code, bytecode, or as in many cases both. This creates a number of situations which can cause problems with package options and the right dependencies. 

If bytecode is produced at all then the PKGBUILD must contain the following to protect the bytecode: 
    
    options=('!strip')
    
If the package does not contain bytecode and only distributes a binary, then `ocaml` is not needed as a dependency, but it of course is required as a makedepends since the `ocaml` package provides the OCaml compiler. If the package contains both native code and bytecode then `ocaml` should be a dependency and a makedepends. 

OCaml code is rarely (if ever) distributed as bytecode only and will almost always include native code: the only case where using _any_ as the _arch_ is advisable is when only un-compiled source code is distributed, usually with a library, though many libraries still distribute native code. 

The moral of the story here is to be aware of what it is you are distributing, chances are your package contains both native machine code and bytecode. 

##  使用 Dune 的 PKGBUILD 实例

[Dune](<https://dune.build/>) 是一种新的构建系统，现在已经越来越多的被用于 OCaml 项目中。 

One thing to be aware is that a single project can build several "packages" in the OPAM/findlib sense, each with its own directory in `/usr/lib/ocaml/`. See [ocaml-cairo](<https://archlinux.org/packages/?name=ocaml-cairo>)包 for an example. For release builds, all "packages" have to be explicitly listed. 
    
    # Contributor: Your Name <youremail@domain.com>
    
    pkgname=ocaml-<package name>
    pkgver=4.2
    pkgrel=1
    license=(_)_
    arch=('x86_64')
    pkgdesc="An OCaml Package"
    url=""
    depends=('ocaml')
    makedepends=('dune')
    source=()
    options=('!strip')
    sha256sums=()
    
    build() {
      cd "${pkgname}-${pkgver}"
      # The "-p" flag is necessary for release builds, see the Dune manpage. Dune will complain if you forget some packages.
      dune build -p package1,package1-extension,package2
    }
    
    package() {
       cd "${pkgname}-${pkgver}"
    	
       DESTDIR="${pkgdir}" dune install --prefix "/usr" --libdir "/usr/lib/ocaml" --docdir "/usr/share/doc"

##  使用 findlib 的 PKGBUILD 实例
    
    # Contributor: Your Name <youremail@domain.com>
    
    pkgname=ocaml-<package name>
    pkgver=4.2
    pkgrel=1
    license=(_)_
    arch=('x86_64')
    pkgdesc="An OCaml Package"
    url=""
    depends=('ocaml')
    makedepends=('ocaml-findlib')
    source=()
    options=('!strip')
    md5sums=()
    
    OCAMLFIND_DESTDIR="${pkgdir}$(ocamlfind printconf destdir)"
    
    build() {
      cd "${pkgname}-${pkgver}"
      mkdir -p "$OCAMLFIND_DESTDIR"
      ./configure --prefix=/usr
      make
    }
    
    package() {
      cd "${pkgname}-${pkgver}"
      env DESTDIR="${pkgdir}" \
        OCAMLFIND_DESTDIR="$OCAMLFIND_DESTDIR" \
        make install
    }

需要留意的是许多 OCaml 包都需要给 `make` 与 `make install` 一些额外信息。同时，请去除 `!strip` 选项，并在包不编译为字节码时指定架构。 
