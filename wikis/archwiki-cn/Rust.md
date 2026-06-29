相关文章

  * [Rust 软件打包准则](<../zh-cn/Rust_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Rust 软件打包准则")

**翻译状态：**

  * 本文（或部分内容）译自 [Rust](<https://wiki.archlinux.org/title/Rust> "arch:Rust")，最近一次同步于 2025-10-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Rust?diff=0&oldid=846429>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Rust_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

根据[维基百科](<https://zh.wikipedia.org/wiki/Rust_\(%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80\)> "zhwp:Rust \(编程语言\)")： 

     [Rust](<https://rust-lang.org>) 是由 Mozilla 主导开发的通用、编译型编程语言。设计准则为“安全、并发、实用”，支持函数式、并发式、过程式以及面向对象的程序设计风格。Rust 的设计目标之一，是要使设计大型的互联网客户端和服务器的任务变得更容易。因此更加强调安全性、存储器配置、以及并发处理等方面的特性。

##  语言核心

###  Rust 核心库

[Rust 核心库](<https://doc.rust-lang.org/core/>)是 Rust 标准库的基础，无需依赖。它直接与 LLVM 原语对接，使 Rust 可以与平台和硬件无关。正是这种与 [LLVM](<../zh-cn/LLVM.html> "LLVM") 的集成，使 Rust 比 [Clang](<../zh-cn/Clang.html> "Clang") 编译的同样功能的 C 语言程序性能更高，使得用 libcore 设计的 Rust 软件比 C 语言的更底层。为嵌入式平台设计软件的开发者可通过 `#![no_std]` 放弃使用标准库，只使用语言自带的核心库，以获得更小的二进制文件和更好的性能。然而，由于大多数库都需要标准库，使用 `#![no_std]` 意味着来自 Rust 社区的软件支持会受限。 

###  Rust 标准库

[Rust 标准库](<https://doc.rust-lang.org/std/index.html>)提供了方便的高级抽象，用于开发大多数可移植的 Rust 软件。标准库包含 `Vec` 和 `String` 类型、大量的语言原语方法、大量的标准宏、I/O 和多线程支持、使用 `Box` 实现的堆分配，以及更多核心库不具有的高级特性。 

###  发布周期

与 [Firefox](<../zh-cn/Firefox.html> "Firefox") 类似，Rust 使用每六周的发布周期。在每个新版本中，核心库和标准库都会得到改进，以支持更多的平台、提高性能，以及为稳定版本增加新特性。 

##  安装

安装 Rust 主要有两种方式： 

  * 直接安装。如果你只使用 Rust 来运行或安装软件，推荐使用此方式。
  * Rustup 安装。如果你打算进行 Rust 编程，推荐使用此方式。

###  直接安装

要从 Arch Linux 官方软件库中[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")最新的稳定版 Rust，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [rust](<https://archlinux.org/packages/?name=rust>)包。这将安装 `rustc` 编译器和 [Cargo](<#Cargo>)。 

除此之外还有开发版的 Rust 编译器 [rust-nightly-bin](<https://aur.archlinux.org/packages/rust-nightly-bin/>)AUR 和 [rust-git](<https://aur.archlinux.org/packages/rust-git/>)AUR 可用，分别用于预编译的通用二进制文件、编译器与系统库的构建。 

###  通过 rustup 安装

为开发软件，官方推荐的 Rust 安装方法是使用 [rustup 工具链管理器](<https://www.rustup.rs/>)安装。 

使用 rustup 工具链管理器而不是仓库中独立的 Rust 软件包的优点，主要是能为多个目标平台（Windows、macOS、Android）和架构（x86、x86_64、arm）安装多个工具链（稳定版、测试版、开发版）。需要注意的是，安装 rustup 并不会自动安装 Rust 工具链，使用任何方法更新 rustup 也不会自动提供 Rust 的最新工具链版本。有关工具链的更多信息，请参见[#用法](<#%E7%94%A8%E6%B3%95>)或 [rustup 工具链文档](<https://rust-lang.github.io/rustup/concepts/toolchains.html>)。 

Rustup 的安装有两种方式，一种是通过 Arch Linux 自带的 pacman，另一种是通过 Rust 官方安装脚本。 

####  Arch Linux 软件包

[rustup](<https://archlinux.org/packages/?name=rustup>)包 在 Arch Linux 软件仓库中可用。注意，以这种方式安装时，`rustup self update` 将**不** 起作用，只能使用 pacman 更新 rustup。然而，这一变化并不适用于其他 rustup 功能，例如用于更新 Rust 工具链的 `rustup update`。 

使用此软件包的优点是 Rust 可执行文件都在 `/usr/bin` 目录内，而不是 `~/.cargo/bin`，因此避免了在 `PATH` 中添加其他目录的麻烦。 

**注意：**[rustup](<https://archlinux.org/packages/?name=rustup>)包 软件包默认不会安装工具链。它提供了 `/usr/bin/rustup` 与 `/usr/bin/rustc`、`/usr/bin/cargo` 等普通二进制文件之间的符号链接。如上所述，要使上述 Rust 命令能工作，用户仍需手动安装工具链。

为安装工具链，需要指定使用的版本号或使用稳定版（`stable`）、测试版（`beta`）、开发版（`nightly`）： 
    
    $ rustup default stable

####  构建 Rust 时更新 LLVM

由于 Rust 采用引导策略进行构建，因此在构建前必须先安装一个已经可用的 Rust 软件包。当构建使用的 [llvm](<https://archlinux.org/packages/?name=llvm>)包 版本**高于** 官方仓库中的版本时，需要提供用于构建仓库中 Rust 版本的旧版 [llvm-libs](<https://archlinux.org/packages/?name=llvm-libs>)包 动态链接库才能进行构建。 

示例：官方仓库提供 llvm-18.1.8，需要针对 llvm-19.1.6 构建。 

引导步骤需要来自 llvm-libs-18.1.8 的 `/usr/lib/libLLVM.so.18.1` 文件。该文件可以通过手动放置到构建根目录，或通过安装诸如 [llvm15-libs](<https://archlinux.org/packages/?name=llvm15-libs>)包 之类的软件包来提供。 

####  上游安装脚本

Rustup 也可通过 [rustup 官方网页](<https://rustup.rs/>)下载并手动安装。 

使用下面命令下载：`curl --proto '=https' --tlsv1.3 -sSf https://sh.rustup.rs -o rust.sh`，查看脚本：`less ./rust.sh`，运行脚本以安装 rustup：`./rust.sh`。此脚本仅对当前登录 Shell 的[配置文件](<../zh-cn/Bash.html#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "Bash")进行 PATH 修改。在注销并重新登录之前需要`source ~/.cargo/env`。在此之后升级 rustup 需执行 `rustup self update`。 

该脚本自动安装并激活默认工具链（[rust](<https://archlinux.org/packages/?name=rust>)包 所使用的工具链），因此无需手动安装工具链即可使用 Rust。 

**警告：** 正如 Rust 文档所建议的，执行 `curl _some-url_ | sh` 会带来安全风险，因为它执行的是未知的、甚至可能在下载过程中被破坏的代码。因此建议在执行脚本之前，手动下载并检查。

**注意：** 在运行 `rustup` 时请确保 `~/.cargo/bin` 在 `PATH` 内。

####  用法

可能需要手动安装工具链，例如稳定版（`stable`）、测试版（`beta`）、开发版（`nightly`）或特定版本（`1.58.0`）。如果想要使用或测试另一个工具链，也需要如下操作： 
    
    $ rustup toolchain install _toolchain_
    
现在可通过 `rustup run _toolchain_ _command_ ` 来执行 Rust 命令。然而，如果要直接使用这些命令，则需要激活该工具链： 
    
    $ rustup default _toolchain_
    
使用 `rustc -V` 检查目前安装的 Rust 版本: 
    
    $ rustc -V 
    
    rustc 1.58.0 (02072b482 2022-01-11)
    
**注意：** Rust 自身并不会进行链接操作，因此需要确保已安装链接器。可使用 [gcc](<https://archlinux.org/packages/?name=gcc>)包，否则 Rust 会提示以下错误：` error: linker `cc` not found.`

**注意：**

Rustup 不会自动更新提供的工具链。如果用户希望使用最新版本的 Rust、crates 以及其他相关包，他们可能需要偶尔使用 ` rustup update` 来更新他们的工具链。有关更多信息，请参见 [官方 rustup 文档](<https://rust-lang.github.io/rustup/basics.html>)。 

###  测试安装结果

通过构建一个小程序来测试 Rust 是否已正确安装，源码如下所示： 
    
    ~/hello.rs
    
    fn main() {
        println!("Hello, World!");
    }
    
可使用 `rustc` 编译，然后运行： 
    
    $ rustc hello.rs && ./hello
    
    Hello, World!
    
##  交叉编译

###  使用 rustup

使用 rustup 可轻松地交叉编译。rustup 支持许多交叉编译目标，完整列表可通过执行 `rustup target list` 查看。 

例如，使用 Windows 稳定通道安装 Rust，使用 GNU 编译器，需要执行以下命令： 
    
    $ rustup toolchain install stable-x86_64-pc-windows-gnu
    
此操作只会为目标架构安装 Rust 及其工具，但在交叉编译时可能还需要其他工具。 

### Windows

本节中，`$ARCH` 是目标架构（`x86_64` 或 `i686`）。以下内容将解释如何使用 rustup 进行交叉编译。 

  1. [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mingw-w64-gcc](<https://archlinux.org/packages/?name=mingw-w64-gcc>)包
  2. 为目标架构安装 Rust 标准库：`rustup target add $ARCH-pc-windows-gnu`
  3. 最后，为了使 cargo 能找到 MinGW-w64 gcc/ar，需要在 `~/.cargo/config.toml` 中添加如下内容：

    ~/.cargo/config.toml
    
    [target.$ARCH-pc-windows-gnu]
    linker = "/usr/bin/$ARCH-w64-mingw32-gcc"
    ar = "/usr/bin/$ARCH-w64-mingw32-ar"
    
最后，通过向 cargo 传递 `--target $ARCH-pc-windows-gnu` 参数，即可为 Windows 交叉编译： 
    
    $ # Build
    $ cargo build --release --target "$ARCH-pc-windows-gnu"
    $ # Run unit tests under wine
    $ cargo test --target "$ARCH-pc-windows-gnu"
    
目前无法使用 MinGW 6 和通过 rustup 安装的工具链构建可执行文件。要修复此问题，请执行 
    
    for lib in crt2.o dllcrt2.o libmsvcrt.a; do cp -v /usr/x86_64-w64-mingw32/lib/$lib $HOME/.rustup/toolchains/$CHANNEL-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-pc-windows-gnu/lib/; done
    
其中 `CHANNEL` 为更新通道：稳定版（`stable`）、测试版（`beta`）或开发版（`nightly`）。 

###  非官方软件包

非官方仓库 [archlinuxcn](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Archlinuxcn") 有 rust-nightly 和 i686, ARM, ARMv7, Windows 32 & 64 的 Rust 标准库，因此只需安装对应的标准库即可享受交叉编译。然而，ARM 工具链只能自行寻找。对于 32 位 Windows 目标，需要获取 [mingw-w64-gcc](<https://archlinux.org/packages/?name=mingw-w64-gcc>)包 提供的 libgcc_s_dw2-1.dll 来编译运行。 

## Cargo

[Cargo](<https://crates.io/>)，Rust 的包管理器，是 [rust](<https://archlinux.org/packages/?name=rust>)包 的一部分。作为 [rust-nightly-bin](<https://aur.archlinux.org/packages/rust-nightly-bin/>)AUR 的一部分，Cargo 开发版（nightly）在 AUR 上可用。如果使用 [rustup](<https://archlinux.org/packages/?name=rustup>)包 则无需再安装 Cargo。 

Cargo 使 Rust 项目能声明各种依赖关系，并确保始终能得到可重现构建。推荐阅读[官方指南](<https://doc.crates.io/guide.html>)。 

###  用法

使用 Cargo 创建新项目： 
    
    $ cargo new hello_world 
    
此操作将创建包含默认 Cargo.toml 文件的目录，该文件用于构建可执行文件。 

**注意：** Cargo 将 `Cargo.toml` 作为包含编译项目所需所有元数据的列表。 
    
    Cargo.toml
    
    [package]
    name = "hello_world"
    version = "0.1.0"
    edition = "2021"
    
    [dependencies]

###  为本机 CPU 平台优化

通过在 `~/.cargo/config.toml` 中添加一个标志，Cargo 将始终为本机 CPU 进行编译优化。请注意，由此产生的二进制文件无法在其他计算机上运行。如果未来更换 CPU，您甚至可能无法在自己的系统上运行这些二进制文件。 

找出安装时默认使用的目标平台： 
    
    $ rustup toolchain list
    
    stable-x86_64-unknown-linux-gnu (default)
    
这说明目前在 `x86_64-unknown-linux-gnu` 平台上使用稳定版（`stable`） Rust。 

将 Cargo 设置为始终为本机 CPU 进行编译优化： 
    
    ~/.cargo/config.toml
    
    [target.x86_64-unknown-linux-gnu]
    rustflags = ["-C", "target-cpu=native"]
    
### sccache

使用 [sccache](<https://github.com/mozilla/sccache>)（[sccache](<https://archlinux.org/packages/?name=sccache>)包）可以大大减少编译时间。这将在本地维护编译器的工作缓存，从而无需重新编译自上次编译以来不变的代码。 

为启用 sccache，可使用 `RUSTC_WRAPPER` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")： 
    
    $ export RUSTC_WRAPPER=sccache
    $ cargo build
    
或者 
    
    $ RUSTC_WRAPPER=sccache cargo build
    
或者也可以将以下内容添加到 `~/.cargo/config.toml`： 
    
    ~/.cargo/config.toml
    
    [build]
    rustc-wrapper = "sccache"
    
##  IDE 支持

###  工具

Rust 项目的推荐工具请参阅 <https://www.rust-lang.org/zh-CN/tools> 。 

#### rust-analyzer

[rust-analyzer](<https://rust-analyzer.github.io/>) 是官方的 Rust 语言服务器协议（LSP）实现，已取代 [RLS](<https://github.com/rust-lang/rls>)。 

安装 [rust-analyzer](<https://archlinux.org/packages/?name=rust-analyzer>)包 软件包即可使用，最新 Git 版本可通过安装 [rust-analyzer-git](<https://aur.archlinux.org/packages/rust-analyzer-git/>)AUR 获取。另外，如果已安装 [rustup](<https://archlinux.org/packages/?name=rustup>)包，可使用以下命令安装 rust-analyzer： 
    
    $ rustup component add rust-analyzer
    
rust-analyzer 需要标准库的源代码。如果源代码不存在，rust-analyzer 将尝试使用 rustup 自动安装。要使用 rustup 手动安装源代码，请执行以下命令： 
    
    $ rustup component add rust-src
    
#### Clippy

[Clippy](<https://github.com/rust-lang/rust-clippy>) 借助编译器插件支持实现了许多额外提示，能检测出更多错误和非惯用的 Rust 语法。[rust](<https://archlinux.org/packages/?name=rust>)包 软件包中包含了 Clippy。 

使用 rustup 安装 Clippy： 
    
    $ rustup component add clippy
    
#### Rustfmt

[Rustfmt](<https://github.com/rust-lang/rustfmt>) 是一个根据官方代码风格规范来格式化 Rust 代码的工具。 

[rust](<https://archlinux.org/packages/?name=rust>)包 软件包中包含了 Rustfmt。执行以下命令，用 rustup 来安装 Rustfmt： 
    
    $ rustup component add rustfmt
    
###  编辑器

#### Emacs

[Emacs](<../zh-cn/Emacs.html> "Emacs") 对 Rust 的支持可通过官方的 [rust-mode](<https://github.com/rust-lang/rust-mode>) 插件获取。 

Emacs 支持使用 [Eglot](<https://www.gnu.org/software/emacs/manual/eglot.html>)[GNU 文档](<https://www.gnu.org/manual/manual.html>) 、[lsp-bridge](<https://github.com/manateelazycat/lsp-bridge>) 等包连接 [rust-analyzer](<#rust-analyzer>)。 

#### GNOME Builder

GNOME Builder 对 Rust 的支持通过语言服务器协议（LSP）实现。默认使用 [rust-analyzer](<#rust-analyzer>)，需要同时安装 Rust 源代码。 

#### Helix

[Helix](<../zh-cn/Helix.html> "Helix") 编辑器使用 Rust 编写，包含了 Rust 语言服务器协议（LSP）。Helix 的灵感来自 Neovim 和 Kakoune。 

#### Kate

Kate 对 Rust 的支持通过语言服务器协议（LSP）实现。默认使用 [rust-analyzer](<#rust-analyzer>)，需要同时安装 Rust 源代码。 

#### IntelliJ IDEA

[IntelliJ IDEA](<https://www.jetbrains.com/idea/>) 有 [Rust 插件](<https://github.com/intellij-rust/intellij-rust>)。此插件同样适用于 CLion。 

如果使用 rustup，请使用 rustup 下载源代码（`rustup component add rust-src`），然后将工具链所在位置指定为 `~/.rustup/toolchains/<your toolchain>/bin`。 

如果使用 Arch Linux 官方软件库中的 Rust，请将工具链所在位置指定为 `/usr/bin`，将标准库所在位置指定为 `/usr/lib/rustlib/src/rust/library/`。 

#### Jetbrains RustRover

[Jetbrains](<https://www.jetbrains.com/zh-cn/idea/>) 也正在开发一款专为 Rust 设计的编辑器。可以在其[官方网站](<https://www.jetbrains.com/zh-cn/rust/>)或 AUR （[rustrover](<https://aur.archlinux.org/packages/rustrover/>)AUR 和 [rustrover-eap](<https://aur.archlinux.org/packages/rustrover-eap/>)AUR） 中找到并下载。 

#### Visual Studio Code

[Visual Studio Code](<../zh-cn/Visual_Studio_Code.html> "Visual Studio Code") 对 Rust 的支持可通过 [rust-analyzer](<#rust-analyzer>) 与 [rust-lang.rust-analyzer](<https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer>) 扩展获取。 

#### Vim

[Vim](<../zh-cn/Vim.html> "Vim") 对 Rust 的支持可通过官方的 [rust.vim](<https://github.com/rust-lang/rust.vim>) 插件获取，支持文件检测、语法高亮、格式化和 [Syntastic](<https://github.com/vim-syntastic/syntastic>) 语法检查插件。许多代码补全引擎都支持 Rust，例如 [coc](<https://github.com/neoclide/coc.nvim>)（通过 [coc-rust-analyzer](<https://github.com/fannheyward/coc-rust-analyzer>) 插件）和 [YouCompleteMe](<https://github.com/ycm-core/YouCompleteMe>)。 

##  另见

  * [Rust 编程语言官网](<https://www.rust-lang.org/zh-CN/>)
  * [Rust 文档](<https://www.rust-lang.org/zh-CN/learn>)
  * [标准库 API](<https://rustwiki.org/zh-CN/std/>)
  * [Rust 官方文档中文教程](<https://rustwiki.org/>)
  * [《Rust 程序设计语言》](<https://rustwiki.org/zh-CN/book/>)
  * [《通过例子学 Rust》](<https://rustwiki.org/zh-CN/rust-by-example/>)
  * [《Rust 参考手册》](<https://rustwiki.org/zh-CN/reference/>)
  * [Rust 维基百科词条](<https://zh.wikipedia.org/wiki/Rust> "zhwp:Rust")
  * [Rust 语言术语中英文对照表](<https://rustwiki.org/wiki/translate/english-chinese-glossary-of-rust/>)
  * [Rust Telegram 中文讨论群](<https://t.me/rust_zh>)

  * [带少量注释的 Rust 示例](<https://doc.rust-lang.org/stable/rust-by-example/>)（英文）
  * [Cargo 可用的库（单元包/crate）](<https://crates.io/>)（英文）
  * [Rust 本周动态](<https://this-week-in-rust.org/>)（英文）
  * [Rust 编程语言博客](<https://blog.rust-lang.org/>)（英文）
  * [Rust 用户论坛](<https://users.rust-lang.org/>)（英文）
  * [Rust 内部人员论坛](<https://internals.rust-lang.org/>)（英文）
