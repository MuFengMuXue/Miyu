**翻译状态：**

  * 本文（或部分内容）译自 [Go](<https://wiki.archlinux.org/title/Go> "arch:Go")，最近一次同步于 2023-08-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Go?diff=0&oldid=784596>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Go_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Go 语言软件打包准则](<../zh-cn/Go_%E8%AF%AD%E8%A8%80%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Go 语言软件打包准则")

[Go](<https://go.dev/>) 是一门受 Google 支持的开源编程语言。根据 [Go 文档](<https://go.dev/doc/>)： 

    Go 表达力强、简洁、干净、高效。它的并发机制使编写能够最大限度地利用多核和联网计算机的程序变得简单，而它新颖的类型系统则使得灵活和模块化程序构造变得可能。Go 可以快速编译成机器代码，同时还具有垃圾回收的便利性和运行时反射的强大功能。它是快速、静态类型的编译语言，同时感觉就像是动态类型的解释型语言。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [go](<https://archlinux.org/packages/?name=go>)包 软件包，这包含标准 Go 编译器和其他开发工具。可在 [_go_ 命令文档（英文）](<https://pkg.go.dev/cmd/go>)中查看包含的子命令。 

###  其他编译器

[go](<https://archlinux.org/packages/?name=go>)包 软件包包含标准 Go 编译器（名为 _gc_ ）。还可使用下面这些编译器替代。 

#### gccgo

[gcc-go](<https://archlinux.org/packages/?name=gcc-go>)包 软件包提供了 [GCC](<../zh-cn/GNU_Compiler_Collection.html> "GCC") 的一个前端 [gccgo](<https://go.dev/doc/install/gccgo>)。在某些情况下， _gccgo_ 生成的二进制文件可能比 _gc_ 更快，而且可以为更多操作系统和架构生成二进制文件。[实践中，对于几乎所有的负载， _gc_ 生成的二进制文件都比 _gccgo_ 更快。](<https://meltware.com/2019/01/16/gccgo-benchmarks-2019.html>)

#### TinyGo

[TinyGo](<https://tinygo.org/>) 是一个基于 [LLVM](<../zh-cn/LLVM.html> "LLVM") 的编译器，旨在为嵌入式系统和 WebAssembly 生成非常小的二进制文件。其由 [tinygo](<https://archlinux.org/packages/?name=tinygo>)包 软件包提供。 

###  工具

这些软件包提供 Go 开发者工具： 

  * **Go tools** — 主要用于 Go 程序静态分析的各种工具和 Go 软件包。

     <https://cs.opensource.google/go/x/tools> || [go-tools](<https://archlinux.org/packages/?name=go-tools>)包

  * **gopls** — 官方 Go 语言服务器。

     <https://pkg.go.dev/golang.org/x/tools/gopls> || [gopls](<https://archlinux.org/packages/?name=gopls>)包

  * **Delve** — Go 编程语言的调试器。

     <https://github.com/go-delve/delve> || [delve](<https://archlinux.org/packages/?name=delve>)包

  * **go-bindata** — 一款可从任意文件生成 Go 代码的小工具。可用于在 Go 程序中嵌入二进制数据。

     <https://github.com/shuLhan/go-bindata> || [go-bindata](<https://aur.archlinux.org/packages/go-bindata/>)AUR, [go-bindata-hashicorp](<https://archlinux.org/packages/?name=go-bindata-hashicorp>)包

  * **GoReleaser** — Go 项目的发布自动化工具。

     <https://goreleaser.com/> || [goreleaser](<https://archlinux.org/packages/?name=goreleaser>)包

  * **gox** — Go 交叉编译工具，可并行为多个平台编译。

     <https://github.com/mitchellh/gox> || [gox](<https://archlinux.org/packages/?name=gox>)包

  * **ko** — Go 应用程序容器镜像生成器。

     <https://github.com/ko-build/ko> || [ko](<https://archlinux.org/packages/?name=ko>)包

  * **revive** — 一个快速、可配置、可扩展、灵活、美观的 Go linter。

     <https://revive.run/> || [revive](<https://archlinux.org/packages/?name=revive>)包

  * **Staticcheck** — 先进的 Go 编程语言 linter。

     <https://staticcheck.io/> || [staticcheck](<https://archlinux.org/packages/?name=staticcheck>)包

  * **Yaegi** — Go 解释器。包括 _yaegi_ 命令行解释器/REPL。

     <https://github.com/traefik/yaegi> || [yaegi](<https://archlinux.org/packages/?name=yaegi>)包

###  安装目录

`go install` 命令会将 Go 可执行文件安装到 `GOBIN` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")定义的目录或 `GOPATH` 环境变量第一个条目的 `bin` 子目录。默认情况下是 `~/go/bin`。 

**提示：** 运行 `go env` 来查看所有 Go 变量。

为方便起见，可将 bin 子目录添加到 `PATH` 中： 
    
    $ export PATH="$PATH:$(go env GOBIN):$(go env GOPATH)/bin"
    
更多信息，请参见[如何编写 Go 代码（英文）](<https://go.dev/doc/code>)和 `go help gopath`。 

##  提示和技巧

###  编译源代码

可以编写一个 Hello World 程序，如下所示： 
    
    hello.go
    
    package main
    
    import "fmt"
    
    func main() {
        fmt.Println("Hello, Arch!")
    }
    
接着通过 _go_ 工具运行它： 
    
    $ go run hello.go
    
    Hello, Arch!
    
使用标准编译器编译（等价于 `go build -compiler=gc hello.go`）： 
    
    $ go build hello.go
    
使用 _gccgo_ 编译（等价于 `go build -compiler=gccgo hello.go`）： 
    
    $ gccgo hello.go -o hello
    
使用 _tinygo_ 编译： 
    
    $ tinygo build -o hello ./hello.go
    
###  交叉编译到其他平台

标准编译器可以很容易地交叉编译到[很多平台](<https://go.dev/doc/install/source#introduction>)。过程根据源代码是否通过 [cgo](<https://pkg.go.dev/cmd/cgo>) 调用 C 代码而不同。 

####  不使用 cgo

如果构建不需要 cgo，则只需将目标操作系统和架构指定为 `go build` 的[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")： 
    
    $ GOOS=linux GOARCH=arm64 go build .
    
有关 `GOOS` 和 `GOARCH` 的有效组合，请参阅[官方文档（英文）](<https://go.dev/doc/install/source#environment>)。 

####  使用 cgo

如果构建需要 cgo，则必须通过 `CC` 或 `CXX` 环境变量提供 C/C++ 交叉编译器的路径。 

假设要为 `GOOS=linux` 和 `GOARCH=arm64` 交叉编译。 

首先要安装 [aarch64-linux-gnu-gcc](<https://archlinux.org/packages/?name=aarch64-linux-gnu-gcc>)包 交叉编译器。 

这是一个需要 `cgo` 的简单示例程序，以便测试交叉编译过程： 
    
    hello.go
    
    package main
    
    // #include <stdio.h>
    // void hello() { puts("Hello, Arch!"); }
    import "C"
    
    func main() {
        C.hello()
    }
    
然后，可以这样交叉编译： 
    
    $ GOOS=linux GOARCH=arm64 CGO_ENABLED=1 CC=/usr/bin/aarch64-linux-gnu-gcc go build hello.go
    
可以检查生成的二进制文件的架构确实是 aarch64： 
    
    $ file hello
    hello: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, BuildID[sha1]=b1d92ae8840a019f36cc2aee4606b6ae4a581bf1, for GNU/Linux 3.7.0, not stripped
    
如果将 `hello` 复制到合适的主机，则可以运行： 
    
    [alarm@rpi3 ~]$ uname -a
    Linux alarm 5.3.8-1-ARCH #1 SMP Tue Oct 29 19:31:23 MDT 2019 aarch64 GNU/Linux
    [alarm@arpi3 ~]$ ./hello
    Hello, Arch!
    
##  故障排除

###  JetBrains Go 插件

如果使用 JetBrains IDE，而 Go 插件找不到 Go SDK 路径，则可能是使用了不兼容的软件包。移除 _gcc-go_ 软件包并替换为 _go_ 。如果已设置 `GOPATH`，那 IDE 现在应该可以找到位于 `/usr/lib/go` 的 Go SDK。 

##  参见

  * [官方网站（英文）](<https://go.dev/>)
  * [维基百科文章（英文）](<https://en.wikipedia.org/wiki/Go_\(programming_language\)> "wikipedia:Go \(programming language\)")
  * [程序样例（包含简短的描述）（英文）](<https://gobyexample.com/>)
  * [交互式 Go 训练教程（英文）](<https://go.dev/tour>)
  * [Go 交叉编译（英文）](<https://rakyll.org/cross-compilation/>)
  * [Go IDE 和插件（英文）](<https://github.com/golang/go/wiki/IDEsAndTextEditorPlugins>)
