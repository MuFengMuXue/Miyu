**翻译状态：**

  * 本文（或部分内容）译自 [Eclipse plugin package guidelines](<https://wiki.archlinux.org/title/Eclipse_plugin_package_guidelines> "arch:Eclipse plugin package guidelines")，最近一次同步于 2015-03-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Eclipse_plugin_package_guidelines?diff=0&oldid=365147>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Eclipse_plugin_package_guidelines_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")**

* * *

[32 位](<../zh-cn/32_%E4%BD%8D%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "32位软件包打包准则") – [安全](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99/%E5%AE%89%E5%85%A8.html> "Arch 打包准则/安全") – [CLR](<../zh-cn/CLR_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CLR 软件打包准则") – [CMake](<../zh-cn/CMake_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CMake 软件打包准则") – [DKMS](<../zh-cn/DKMS_%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "DKMS 软件包打包准则") – Eclipse – [Electron](<../zh-cn/Electron_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Electron 打包准则") – [Free Pascal](<../zh-cn/Free_Pascal_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Free Pascal 打包准则") – [GNOME](</wzh/index.php?title=GNOME_package_guidelines&action=edit&redlink=1> "GNOME package guidelines（页面不存在）") – [Go](<../zh-cn/Go_%E8%AF%AD%E8%A8%80%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Go 语言软件打包准则") – [Haskell](<../zh-cn/Haskell_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Haskell 打包准则") – [Java](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Java 打包准则") – [交叉编译工具](<../zh-cn/%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%E5%B7%A5%E5%85%B7%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "交叉编译工具打包准则") – [KDE](<../zh-cn/KDE_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "KDE 软件打包准则") – [Lisp](</wzh/index.php?title=Lisp_package_guidelines&action=edit&redlink=1> "Lisp package guidelines（页面不存在）") – [Meson](</wzh/index.php?title=Meson_package_guidelines&action=edit&redlink=1> "Meson package guidelines（页面不存在）") – [MinGW](</wzh/index.php?title=MinGW_package_guidelines&action=edit&redlink=1> "MinGW package guidelines（页面不存在）") – [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "内核模块打包指南") – [Node.js](<../zh-cn/Node.js_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Node.js 打包准则") – [Nonfree](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）") – [OCaml](<../zh-cn/OCaml_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "OCaml 打包准则") – [Perl](</wzh/index.php?title=Perl_package_guidelines&action=edit&redlink=1> "Perl package guidelines（页面不存在）") – [PHP](<../zh-cn/PHP_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "PHP 打包准则") – [Python](<../zh-cn/Python_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Python 打包准则") – [R](<../zh-cn/R_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "R 软件打包准则") – [Ruby](</wzh/index.php?title=Ruby_package_guidelines&action=edit&redlink=1> "Ruby package guidelines（页面不存在）") – [Rust](<../zh-cn/Rust_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Rust 软件打包准则") – [Shell](</wzh/index.php?title=Shell_package_guidelines&action=edit&redlink=1> "Shell package guidelines（页面不存在）") – [VCS](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则") – [Web](</wzh/index.php?title=Web_application_package_guidelines&action=edit&redlink=1> "Web application package guidelines（页面不存在）") – [Wine](<../zh-cn/Wine_package_guidelines.html> "Wine package guidelines") – [字体](<../zh-cn/%E5%AD%97%E4%BD%93%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "字体打包指南")

有许多安装有效 [Eclipse](<../zh-cn/Eclipse.html> "Eclipse") 插件的方法。尤其是在 Eclipse 3.4 里引入 _dropins_ 文件夹之后。但其中一些比较凌乱，而且具有标准化和一致的封装方法对于一个干净的系统结构是非常重要的。然而，如果没有一个对 Eclipse 插件如何工作一清二楚的打包者的话，要实现这一切并不简单。本文试图定义一个标准且精简的 Eclipse 插件 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 的结构，如此来在不用麻烦打包者全部重新打包的情况下保持一个干净的文件系统结构。 

##  Eclipse 插件结构以及安装

一般的 Eclipse 插件包含两个目录，`features` 和 `plugins`, 自从 Eclipse 3.3 起它们只能放在 `/usr/share/eclipse/`. 这两个文件夹的内容可以与其他插件的混合，如此会导致混乱并且结构难以管理，也很难来一目了然地区分哪个软件包包含哪些文件。 

这种安装方法依然被 Eclipse 3.4 支持，然而我们更推荐使用 `/usr/share/eclipse/dropins/` 目录。该文件夹内可包含不限数目的子目录，每个子目录包含自己的 `features` 和 `plugins` 子目录。这也能保持一个干净而精简的系统结构，并应当成为打包的标准。 

##  打包

###  PKGBUILD 样例

这里是一个样例，稍后我们将介绍如何自定义修改。 
    
    PKGBUILD-eclipse.proto
    
    pkgname=eclipse-mylyn
    pkgver=3.0.3
    pkgrel=1
    pkgdesc="A task-focused interface for Eclipse"
    arch=('i686' 'x86_64')
    url="http://www.eclipse.org/mylyn/"
    license=('EPL')
    depends=('eclipse')
    optdepends=('bugzilla: ticketing support')
    source=(http://download.eclipse.org/tools/mylyn/update/mylyn-${pkgver}-e3.4.zip)
    md5sums=('e98cd7ab3c5d5aeb7c32845844f85c22')
    
    prepare() {
      # remove features and plug-ins containing sources
      rm features/*.source_*
      rm plugins/*.source_*
      # remove gz files
      rm plugins/*.pack.gz
    }
    
    package() {
      _dest=${pkgdir}/usr/share/eclipse/dropins/${pkgname/eclipse-}/eclipse
    
      # Features
      find features -type f | while read _feature ; do
        if [[ ${_feature} =~ (.*\.jar$) ]] ; then
          install -dm755 ${_dest}/${_feature%*.jar}
          cd ${_dest}/${_feature/.jar}
          # extract features (otherwise they are not visible in about dialog)
          jar xf ${srcdir}/${_feature} || return 1
        else
          install -Dm644 ${_feature} ${_dest}/${_feature}
        fi
      done
    
      # Plugins
      find plugins -type f | while read _plugin ; do
        install -Dm644 "${_plugin}" "${_dest}/${_plugin}"
      done
    }
    
###  如何自定义

需要修改的，最主要的变量就是 `pkgname`. 如果你要打包一个一般的插件，那么你只需要做这些: 大部分插件以 zip 文件发布，其中只含有 `features` 和 `plugins` 子目录。所以，如果你要打包 `foo` 插件并且源文件只包含 `features` 和 `plugins`, 只需把 `pkgname` 改成 `eclipse-foo`, 这样就完成了。 

请仔细阅读，获取 PKGBUILD 的内部结构，这能帮助你理解在其他情况下如何设置编译。 

###  深入分析 PKGBUILD

####  包的命名

包应该命名为 `eclipse-_pluginname_`, 如此能被识别为 Eclipse 相关软件包并且能轻松使用 shell 替代来提取出如 `${pkgname/eclipse-}` 的插件名称，而不用使用不需要的 `${_realname}` 变量。插件名对于清理安装时临时文件并避免冲突是必需的。 

####  文件

#####  解压

一些插件需要的功能要从 jar 文件中提取。已包含于 JRE 的 `jar` 工具,就是用来干这个的。然而，`jar` 并不能解压到当前目录以外的地方: 这意味着，创建每个目录之后，在解压之前需要 `cd` 进入该目录。`${_dest}` 变量被用在这样的背景下，以提高文本可读性和PKGBUILD整洁性。 

#####  地址

如同我们所说，源文档提供两个目录 `features` 和 `plugins`, 每个打包为 jar 文件。更好的嵌入式结构应该如下: 
    
    /usr/share/eclipse/dropins/pluginname/eclipse/features/feature1/...
    /usr/share/eclipse/dropins/pluginname/eclipse/features/feature2/...
    /usr/share/eclipse/dropins/pluginname/eclipse/plugins/plugin1.jar
    /usr/share/eclipse/dropins/pluginname/eclipse/plugins/plugin2.jar
    
这种结构支持把不同插件需要的不同版本的库混起来，同时很清楚它是属于那个包的。这也能避免当不同插件提供了相同库时的冲突。唯一的选择是把每个包和它的库一起它所需的一切乱七八糟的东西分离，并且你也别想这样就能起效，因为有些包需要旧版的库才能工作。 必须要从 jar 里解压出来因为 Eclipse 不会自动检测它们，不然的话整个安装的插件都不会工作。这归因于 Eclipse 认为更新站点和本地安装是不同的 (别问为什么，它就这样). 

####  build() 函数

首先要注意的就是 `cd ${srcdir}` 命令。通常源压缩文档直接在 `${srcdir}` 下解压出 `features` 和 `plugins` 文件夹，但并不是所有的都这样。总之，对大多数 _(事实上)_ 非标准的插件这是需要改变的唯一路线。 

某些特性也随源码发布。对一个普通的释出版来说源码并不需要，可以删除。更多的特性包含 `*.pack.gz` 文件，与 jar 文档相比内容相同。所以这些文件也能删除。 

接下来是 `features` 部分。它为每个 jar 文件创建必要的目录并解压到对应的目录去。同样，`plugins` 部分把 jar 安装到文件夹里去。一个 while 循环用于防止生成名字奇怪的文件。 
