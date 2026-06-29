**翻译状态：**

  * 本文（或部分内容）译自 [Mono](<https://wiki.archlinux.org/title/Mono> "arch:Mono")，最近一次同步于 2024-09-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Mono?diff=0&oldid=815835>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Mono_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自 [Wikipedia](<https://en.wikipedia.org/wiki/Mono_\(software\)> "wikipedia:Mono \(software\)")： 

    Mono is a [...] project to create a [.NET Framework](<https://en.wikipedia.org/wiki/.NET_Framework> "wikipedia:.NET Framework")-compatible set of tools including, among others, a [C#](<https://en.wikipedia.org/wiki/C_Sharp_\(programming_language\)> "wikipedia:C Sharp \(programming language\)") compiler and a [Common Language Runtime](<https://en.wikipedia.org/wiki/Common_Language_Runtime> "wikipedia:Common Language Runtime").

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mono](<https://archlinux.org/packages/?name=mono>)包 软件包。 

如果需要 VisualBasic.Net 支持，则必须使用 [mono-basic](<https://aur.archlinux.org/packages/mono-basic/>)AUR 安装 VisualBasic.Net 解释器。 

**注意：** 安装软件包后，[证书颁发机构](</wzh/index.php?title=%E8%AF%81%E4%B9%A6%E9%A2%81%E5%8F%91%E6%9C%BA%E6%9E%84&action=edit&redlink=1> "证书颁发机构（页面不存在）") 会存储在 `/usr/share/.mono/certs/Trust/` 中，但删除软件包并不会删除它们。[[1]](<https://bbs.archlinux.org/viewtopic.php?id=201926>)

##  运行 Mono 应用程序

您可以手动调用 `mono` 来执行 Mono 二进制文件： 
    
    $ mono programsname.exe
    
您也可以直接执行 Mono 二进制文件，就像本地二进制文件一样： 
    
    $ chmod 755 exefile.exe
    $ ./exefile.exe
    
##  测试 Mono

新建一个文件： 
    
    test.cs
    
    using System;
    
    public class Test {
     public static void Main(string[] args) {
      Console.WriteLine("Hello World!");
     }
    }
    
然后运行： 
    
    $ mcs test.cs
    $ mono test.exe
    Hello world!
    
##  开发

[OmniSharp](<https://www.omnisharp.net/#integrations>) 为多个编辑器提供 .NET/Mono 开发插件/集成，包括 [Vim](<../zh-cn/Vim.html> "Vim")、[Emacs](<../zh-cn/Emacs.html> "Emacs") 和 [Visual Studio Code](<../zh-cn/Visual_Studio_Code.html> "Visual Studio Code")。 

或者，您也可以安装 [rider](<https://aur.archlinux.org/packages/rider/>)AUR 集成开发环境。如果**不是** 从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装 Rider，则需要安装 [mono-msbuild](<https://archlinux.org/packages/?name=mono-msbuild>)包，因为最近的 Rider 版本[放弃了对 xbuild 的支持](<https://youtrack.jetbrains.com/issue/RIDER-50179/Mono-support-is-broken-on-Linux#focus=Comments-27-4408716.0-0>)，转而使用来自 net-core 的 MSBuild。 

如果需要 API 文档浏览器以及一些测试和开发工具，则必须安装 [mono-tools](<https://archlinux.org/packages/?name=mono-tools>)包。 

##  问题解决

###  当我尝试直接运行 Mono 二进制文件时，我遇到了一个错误： “cannot execute binary file”

Mono的 [binfmt_misc](<https://en.wikipedia.org/wiki/Binfmt_misc> "wikipedia:Binfmt misc") 处理程序尚未建立，[Mono Project website](<https://www.mono-project.com/Guide:Running_Mono_Applications#Registering_.exe_as_non-native_binaries_.28Linux_only.29>) 上有详细说明。 

要解决这个问题，[restart](<../zh-cn/Systemd.html> "Daemon") `systemd-binfmt` 服务。 

###  我收到一个 TLS 握手（或类似的基于证书的）错误

造成这种情况的原因可能是 Mono 证书存储区中的证书丢失，或者 Mono 证书存储区中仍然存在过期的破损证书。 

如果可能，请运行 `curl -vI` 或类似程序，在 Mono 外部复制失败请求，以确保系统证书存储处于良好状态。 

  * `cert-sync /etc/ssl/certs/ca-certificates.crt` 将 mono 存储与系统存储同步，并添加缺失的证书。
  * 要删除已损坏的证书（即，如果上述操作无效），请删除 `/usr/share/.mono` 目录，然后重新运行 `cert-sync /etc/ssl/certs/ca-certificates.crt` 。
  * 最后，旧版工具 `mozroots --import --ask-remove` 可绕过系统证书存储区，直接下载 Mozilla 的信任存储区。这同样无法删除损坏的证书，而且如果依赖于私有 CA，还可能导致其他问题。

`cert-sync`和 `mozroots` 都是 mono 软件包的一部分。 

##  参见

  * [Mono 官方网站](<https://www.mono-project.com>)
  * [Mono 手册](<https://mono-project.com/Monkeyguide>)
  * [Mono 的应用程序接口参考](<http://go-mono.org/docs>)
  * [ECMA-334: C# Language Specification](<https://www.ecma-international.org/publications-and-standards/standards/ecma-334/>)
  * [ECMA-335: Common Language Infrastructure (CLI)](<https://www.ecma-international.org/publications-and-standards/standards/ecma-335/>)
  * [运行 Mono 应用程序的说明](<https://www.mono-project.com/Guide:Running_Mono_Applications>)
