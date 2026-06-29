**翻译状态：**

  * 本文（或部分内容）译自 [Python package guidelines](<https://wiki.archlinux.org/title/Python_package_guidelines> "arch:Python package guidelines")，最近一次同步于 2026-01-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Python_package_guidelines?diff=0&oldid=850782>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Python_package_guidelines_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")**

* * *

[32 位](<../zh-cn/32_%E4%BD%8D%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "32位软件包打包准则") – [安全](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99/%E5%AE%89%E5%85%A8.html> "Arch 打包准则/安全") – [CLR](<../zh-cn/CLR_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CLR 软件打包准则") – [CMake](<../zh-cn/CMake_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "CMake 软件打包准则") – [DKMS](<../zh-cn/DKMS_%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "DKMS 软件包打包准则") – [Eclipse](<../zh-cn/Eclipse_%E6%8F%92%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Eclipse 插件打包准则") – [Electron](<../zh-cn/Electron_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Electron 打包准则") – [Free Pascal](<../zh-cn/Free_Pascal_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Free Pascal 打包准则") – [GNOME](</wzh/index.php?title=GNOME_package_guidelines&action=edit&redlink=1> "GNOME package guidelines（页面不存在）") – [Go](<../zh-cn/Go_%E8%AF%AD%E8%A8%80%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Go 语言软件打包准则") – [Haskell](<../zh-cn/Haskell_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Haskell 打包准则") – [Java](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Java 打包准则") – [交叉编译工具](<../zh-cn/%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%E5%B7%A5%E5%85%B7%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "交叉编译工具打包准则") – [KDE](<../zh-cn/KDE_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "KDE 软件打包准则") – [Lisp](</wzh/index.php?title=Lisp_package_guidelines&action=edit&redlink=1> "Lisp package guidelines（页面不存在）") – [Meson](</wzh/index.php?title=Meson_package_guidelines&action=edit&redlink=1> "Meson package guidelines（页面不存在）") – [MinGW](</wzh/index.php?title=MinGW_package_guidelines&action=edit&redlink=1> "MinGW package guidelines（页面不存在）") – [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "内核模块打包指南") – [Node.js](<../zh-cn/Node.js_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Node.js 打包准则") – [Nonfree](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）") – [OCaml](<../zh-cn/OCaml_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "OCaml 打包准则") – [Perl](</wzh/index.php?title=Perl_package_guidelines&action=edit&redlink=1> "Perl package guidelines（页面不存在）") – [PHP](<../zh-cn/PHP_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "PHP 打包准则") – Python – [R](<../zh-cn/R_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "R 软件打包准则") – [Ruby](</wzh/index.php?title=Ruby_package_guidelines&action=edit&redlink=1> "Ruby package guidelines（页面不存在）") – [Rust](<../zh-cn/Rust_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Rust 软件打包准则") – [Shell](</wzh/index.php?title=Shell_package_guidelines&action=edit&redlink=1> "Shell package guidelines（页面不存在）") – [VCS](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则") – [Web](</wzh/index.php?title=Web_application_package_guidelines&action=edit&redlink=1> "Web application package guidelines（页面不存在）") – [Wine](<../zh-cn/Wine_package_guidelines.html> "Wine package guidelines") – [字体](<../zh-cn/%E5%AD%97%E4%BD%93%E6%89%93%E5%8C%85%E6%8C%87%E5%8D%97.html> "字体打包指南")

本文档描述了使用 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 来为 [Python](<../zh-cn/Python.html> "Python") 程序进行打包时须遵守的标准和指引。 

##  包名

对于 [Python 3](<../zh-cn/Python.html#%E5%AE%89%E8%A3%85> "Python") 的**库** 模块，或与 Python 生态紧密耦合的**应用程序** （如 _pip_ 和 _tox_ ），使用 `python-_模块名或应用程序名_` 命名。对于其他**应用程序** ，则仅使用程序原名。 

**注意：** 包名应全为小写。

##  架构

参见 [PKGBUILD#arch](<../zh-cn/PKGBUILD.html#arch> "PKGBUILD")。 

包含 C 扩展的 Python 软件包与架构相关。反之则通常无关于架构。 

使用 [setuptools](<https://setuptools.pypa.io/>) 构建的软件包通过在 `setup.py` 中定义 `ext_modules` 关键字来声明其使用的 C 扩展。 

##  源代码

**注意：** 根据 [RFC0020](<https://rfc.archlinux.page/0020-sources-for-python-packaging/>)，默认应使用上游提供的源代码压缩包，而非 PyPI 提供的 sdist 压缩包。

PyPI 网站提供的下载链接包含不可预测的哈希值，每次更新软件包时需重新从 PyPI 获取。这导致其不适合直接用于 PKGBUILD。PyPI [提供](<https://github.com/pypa/pypi-legacy/issues/438#issuecomment-226940730>)了以下稳定方案：[PKGBUILD#source](<../zh-cn/PKGBUILD.html#source> "PKGBUILD") `source=()` 数组应使用以下 URL 模板： 

源代码包：
    `https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz`
纯 Python wheel 包
     `https://files.pythonhosted.org/packages/py2.py3/${_name::1}/$_name/${_name//-/_}-$pkgver-py2.py3-none-any.whl`（同时兼容 Python 2 和 Python 3）
     `https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/${_name//-/_}-$pkgver-py3-none-any.whl` （仅兼容 Python 3）
    注意分发包名称（distribution name，在 PyPI 注册的名称）可能包含连字符，但在 wheel 文件名中需转换为下划线。
架构相关的 wheel 包
    可通过追加下划线和架构名添加额外数组（如 `source_x86_64=('...')`）。另可使用 `_py=cp310` 避免重复 Python 版本：
    `https://files.pythonhosted.org/packages/$_py/${_name::1}/$_name/${_name//-/_}-$pkgver-$_py-${_py}m-manylinux1_x86_64.whl`

注意使用自定义变量 `**_name**` 代替 `pkgname`，因 Python 软件包通常带有 `python-` 前缀。该变量可通过以下方式定义： 
    
    _name=${pkgname#python-}
    
##  安装方式

Python 中的包通常使用 Python 专用的包管理器（如 [pip](<https://pip.pypa.io/>)）进行安装，这类工具会从在线仓库（通常是 [PyPI](<https://pypi.org/>) —— Python 软件包索引）获取软件包并追踪相关文件。 

然而，在使用 `PKGBUILD` 管理 Python 软件包时，需要将 Python 包“安装”到临时位置 `_$pkgdir_ /usr/lib/python _< Python 版本>_/site-packages/_$pkgname_`。 

对于使用[标准元数据（standard metadata）](<https://www.python.org/dev/peps/pep-0517/>)在 `pyproject.toml` 中指定了构建后端（build backend）的 Python 包，使用 [python-build](<https://archlinux.org/packages/?name=python-build>)包 和 [python-installer](<https://archlinux.org/packages/?name=python-installer>)包 是完成上述“安装”过程最容易的方式。 旧版本软件包可能未声明使用 setuptools，仅提供需手动调用的 `setup.py`。 

**注意：** 必须将元数据中的依赖关系声明在 `depends` 数组中，否则相关依赖不会被安装。

###  基于标准（PEP 517）的安装方式

**提示：** 当从上游提供的源代码 tarball 构建时，若项目依赖 git 生成版本字符串，在构建 wheel 前需根据使用的工具将特定的环境变量设为 `$pkgver`： 

  * [python-flit-core](<https://archlinux.org/packages/?name=python-flit-core>)包、[python-hatch-vcs](<https://archlinux.org/packages/?name=python-hatch-vcs>)包 或 [python-setuptools-scm](<https://archlinux.org/packages/?name=python-setuptools-scm>)包：`SETUPTOOLS_SCM_PRETEND_VERSION`
  * [python-pbr](<https://archlinux.org/packages/?name=python-pbr>)包：`PBR_VERSION`
  * [python-pdm-backend](<https://archlinux.org/packages/?name=python-pdm-backend>)包：`PDM_BUILD_SCM_VERSION`

基于标准的工作流程很简单：使用 [python-build](<https://archlinux.org/packages/?name=python-build>)包 构建一个 wheel，再使用 [python-installer](<https://archlinux.org/packages/?name=python-installer>)包 将其安装到 `$pkgdir`： 

**注意：** 除 [python-build](<https://archlinux.org/packages/?name=python-build>)包 和 [python-installer](<https://archlinux.org/packages/?name=python-installer>)包 外，还需将软件包使用的[构建后端（build backend）](<https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-a-build-backend>)添加至 `makedepends`。仓库中所有可用的构建后端均属于 [python-build-backend](<https://archlinux.org/groups/x86_64/python-build-backend/>)包组。请检查项目的 `pyproject.toml` 文件中 `build-system.build-backend` 配置项的值，该值即为此项目实际使用的构建后端，若未配置则默认使用 [python-setuptools](<https://archlinux.org/packages/?name=python-setuptools>)包。
    
    makedepends=(python-build python-installer python-wheel)
    
    build() {
        cd $_name-$pkgver
        python -m build --wheel --no-isolation
    }
    
    package() {
        cd $_name-$pkgver
        python -m installer --destdir="$pkgdir" dist/*.whl
    }

其中： 

  * `--wheel` 表示仅构建 wheel 文件，不生成源代码分发包
  * `--no-isolation` 表示使用系统已安装的包（含 `depends` 中声明的依赖）进行构建，默认会创建隔离的虚拟环境执行构建
  * `--destdir="$pkgdir"` 可防止直接尝试安装到宿主系统（而非软件包目录），避免权限错误
  * 可将 `--compile-bytecode=……` 或 `--no-compile-bytecode` 传递给 `installer`，但默认值较为合理，无需手动指定

**注意：** 不建议跳过 `build` 阶段而直接将 `.whl` 文件放入 `source` 数组，应优先采用源代码构建。仅在无法通过源码构建时（例如项目**仅** 提供 wheel 源）才应使用此方式。

**提示：** 若软件包为 [VCS 包](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则")（`python-……-git`），请在 `prepare` 函数中添加 `git -C "${srcdir}/${pkgname}" clean -dfx` 命令。此操作可清除旧版 wheel 及其他构建产物，避免后续问题。另请参阅 [setuptools](<https://github.com/pypa/setuptools/issues/1347>) 与 [Poetry](<https://github.com/python-poetry/poetry/issues/1329>) 的上游 issue。

###  使用 setuptools 或 distutils 的安装方式

若项目中不存在 `pyproject.toml` 文件，或该文件未包含 `[build-system]` 表，则说明项目使用遗留格式，即通过 _setup.py_ 文件调用 _setuptools_ 或 _distutils.core_ 的 `setup` 函数。 

此类软件包通常仍可使用上述 [python-build](<https://archlinux.org/packages/?name=python-build>)包 和 [python-installer](<https://archlinux.org/packages/?name=python-installer>)包 方法构建安装（推荐方式），但需在 `makedepends` 中添加 [python-setuptools](<https://archlinux.org/packages/?name=python-setuptools>)包。 

通过直接运行 _setup.py_ 的旧方式（见下）仍可构建安装，但此方法已弃用，仅建议在 PEP 517 兼容方式因故不可用时作为备选方案。 

需注意，使用此方法构建时会在 `package` 阶段输出以下警告： 
    
    SetuptoolsDeprecationWarning: setup.py install is deprecated.

另请注意，Python 3.12 及后续版本的标准库中已移除 _distutils_ 。对于仍使用 _setup.py_ 的项目，必须在 `makedepends` 中添加 [python-setuptools](<https://archlinux.org/packages/?name=python-setuptools>)包（该软件包提供了自带的 _distutils_ 实现）。 
    
    makedepends=('python-setuptools')
    
    build() {
        cd $_name-$pkgver
        python setup.py build
    }
    
    package() {
        cd $_name-$pkgver
        python setup.py install --root="$pkgdir" --optimize=1
    }

其中： 

  * `--root="$pkgdir"` 作用同前文 `--destdir`
  * `--optimize=1` 预生成优化字节码文件（ _.opt-1.pyc_ ）而非在宿主系统按需生成，以便由 [pacman](<../zh-cn/Pacman.html> "Pacman") 追踪这些文件
  * 添加 `--skip-build` 可以跳过不必要的重复构建步骤（如 `build()` 函数已执行过的构建过程）

若软件包使用 [python-setuptools-scm](<https://archlinux.org/packages/?name=python-setuptools-scm>)包，构建时可能报错如下： 
    
    LookupError: setuptools-scm was unable to detect version for /build/python-jsonschema/src/jsonschema-3.2.0.
    
    Make sure you're either building from a fully intact git repository or PyPI tarballs. Most other sources (such as GitHub's tarballs, a git checkout without the .git folder) don't contain the necessary metadata and will not work.

需将 `SETUPTOOLS_SCM_PRETEND_VERSION` 环境变量设为 `$pkgver` 以完成构建： 
    
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    
##  测试

**注意：**

  * 避免使用 `tox` 运行测试套件，因其明确设计用于依据从 PyPI 下载的可复现的、固定的配置环境测试，而**不会** 测试软件包实际安装后的版本，若使用则将使 _check_ 函数失去意义
  * 避免在 **checkdepends** 中添加用于代码检查（lint）、覆盖率或类型检查的 pytest 插件（详见 [#禁用 pytest 附加选项](<#%E7%A6%81%E7%94%A8_pytest_%E9%99%84%E5%8A%A0%E9%80%89%E9%A1%B9>)章节）。这些工具会增加引导难度且非发行版打包必需，因其不验证功能正确性
  * 在为测试配置自定义 `PYTHONPATH` 时，避免使用相对路径，否则可能导致问题出现。请使用绝对路径。

大多数提供测试套件的 Python 项目使用 unittest 运行器、nosetests 或 pytest（分别由 [python](<https://archlinux.org/packages/?name=python>)包、[python-nose](<https://archlinux.org/packages/?name=python-nose>)包 和 [python-pytest](<https://archlinux.org/packages/?name=python-pytest>)包 提供），通过检测特定格式的文件/目录名和类/函数名（如含 `test` 的命名）自动发现测试套件。通常直接运行 `nosetests` 或 `pytest` 即可执行测试套件。 
    
    check(){
        cd $_name-$pkgver
        
        # 使用内置的 unittest
        python -m unittest discover -vs .
    
        # 使用 nosetests
        nosetests
    
        # 使用 pytest
        pytest
    }
    
若存在已编译的 C 扩展模块，测试时需通过 `$PYTHONPATH` 指定与当前 Python 主次版本匹配的构建路径以正确加载模块。 
    
    check(){
        cd $_name-$pkgver
        local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
        
        # 使用内置的 unittest
        PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$python_version" python -m unittest discover -vs .
        
        # 使用 nosetests
        PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$python_version" nosetests
    
        # 使用 pytest
        PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$python_version" pytest
    }

##  提示和技巧

###  获取 Python 版本号

在准备、构建、测试或安装过程中，如需引用系统 Python 的主次版本号（如 `3.9` 或 `3.10`），请勿硬编码版本号，而应通过 Python 解释器动态获取并存储至局部变量： 
    
    check(){
      local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
      ...
    }

###  获取 site-packages 路径

在构建、测试或安装过程中，如需引用系统的 `site-packages` 目录，请勿硬编码路径，而应通过 Python 解释器动态获取并存储至局部变量： 
    
    check(){
      local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
      ...
    }

###  避免在 site-package 中放置测试目录

避免在 `site-packages/` 下直接安装名为 `tests/` 的目录（即 `/usr/lib/python _X_._Y_ /site-packages/tests/`），否则可能引发软件包冲突。某些使用 _setuptools_ 的 Python 项目存在错误配置，可能将其测试目录作为顶层 Python 包包含。若发现此类问题，请向项目提交 issue 请求修复，例如[此 issue](<https://github.com/Lightning-AI/lightning/issues/10335>)。 

###  禁用 pytest 附加选项

运行 pytest 时，通常应禁用额外插件。特别是代码检查（lint）和覆盖率（coverage）插件在打包场景中可能适得其反，因其行为变更可能导致测试失败。 

推荐通过命令行覆盖配置选项（而非修改 pytest 配置文件）来禁用 `addopts` 等参数，以减少维护成本。要清空所有附加选项，可使用： 
    
    pytest -o addopts=""
    
###  修复 meson-python 的可复现性问题

使用 [meson-python](<https://archlinux.org/packages/?name=meson-python>)包 作为 PEP 517 构建后端时，其随机生成的构建目录路径会导致[可复现性问题](<https://github.com/mesonbuild/meson-python/issues/703>)。可通过 `-Cbuild-dir` 参数硬编码构建目录来规避此问题： 
    
    python -m build --wheel --no-isolation -Cbuild-dir=build
    
###  使用已安装的软件包运行测试

有些软件包需要安装后才能正常测试。在这种情况下（例如 [python-narwhals](<https://archlinux.org/packages/?name=python-narwhals>)包），可以将构建的软件包安装到 _虚拟环境_ 下，并在该环境中运行测试： 
    
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    test-env/bin/python -P -m pytest
    