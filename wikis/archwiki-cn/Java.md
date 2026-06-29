**翻译状态：**

  * 本文（或部分内容）译自 [Java](<https://wiki.archlinux.org/title/Java> "arch:Java")，最近一次同步于 2025-10-1，若英文版本有所[更改](<https://wiki.archlinux.org/title/Java?diff=0&oldid=846989>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Java_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Java 打包准则](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Java 打包准则")
  * [Java 运行环境字体配置](<../zh-cn/Java_%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html> "Java 运行环境字体配置")

摘自维基百科中的 [Java](<https://en.wikipedia.org/wiki/Java_\(programming_language\)> "wikipedia:Java \(programming language\)") 词条: 

    Java是一种编程语言，最初由Sun Microsystems开发，并于1995年作为Sun Microsystems的Java平台的核心组件发布。它有很多语法来自C和C++，但对象模型更简洁，底层组件更少。Java的应用一般会编译成能在任何Java虚拟机([JVM](<https://en.wikipedia.org/wiki/Java_virtual_machine> "wikipedia:Java virtual machine"))而不是特定架构上运行的字节码。

[Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux") 官方支持开源的 [OpenJDK](<https://openjdk.java.net/>) [版本](<https://en.wikipedia.org/wiki/Java_version_history#Release_table> "wikipedia:Java version history") 8、11、17 和 21—— _长期支持_ (LTS) 版本，以及 25——最新发布的版本。所有这些JVM可以并存，并能够通过帮助脚本 _archlinux-java_ （随 [java-runtime-common](<https://archlinux.org/packages/?name=java-runtime-common>)包 包安装）切换。在 [AUR](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 中也有一些不受官方支持的Java环境。 

##  安装

**注意：**

  * Arch Linux 官方仅支持 [OpenJDK](<#OpenJDK>) 实现。
  * 安装完成后，Java 环境需要被 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell") (`$PATH` 变量) 识别。可以通过在命令行中使用 `source` 命令读取 `/etc/profile`，注销并重新登录 [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")，或者重启系统来做到这点。

两个 _常见的_ 包分别作为依赖被拉取，分别是 [java-runtime-common](<https://archlinux.org/packages/?name=java-runtime-common>)包（包含 _Java 运行环境_ 的公共文件）和 [java-environment-common](<https://archlinux.org/packages/?name=java-environment-common>)包（包含 _Java 开发工具包_ 的公共文件）。 

提供的 `/etc/profile.d/jre.sh` 和 `/etc/profile.d/jre.csh` 文件指向由 _archlinux-java_ 帮助脚本设置的链接 `/usr/lib/jvm/default/bin`。 

**提示：**`/usr/lib/jvm/default` 和 `/usr/lib/jvm/default-runtime` 符号链接应**始终** 使用 `archlinux-java` 进行编辑，该工具用于显示并指向一个可用的默认 Java 运行环境。

大多数 Java 安装的可执行文件通过直接链接在 `/usr/bin/` 中提供，而其他可执行文件则在 `$PATH` 指向的位置处。 

### OpenJDK

[OpenJDK](<https://en.wikipedia.org/wiki/OpenJDK> "wikipedia:OpenJDK")是 _Java平台标准版_ （Java SE）的开源实现，也是官方的参考实现。有几个OpenJDK构建的分发，如[Adoptium](<https://adoptium.net>)（以前称为AdoptOpenJDK）和[Amazon Corretto](<https://aws.amazon.com/corretto/>)。Arch Linux的OpenJDK包由[上游的OpenJDK源代码](<https://hg.openjdk.java.net/>)构建。 

Headless JRE
    Java的最小运行环境 - 执行非GUI的Java程序所需。
Full JRE
    完全的Java运行环境 - 执行Java GUI程序所需。
JDK
     [Java Development Kit](<https://en.wikipedia.org/wiki/Java_Development_Kit> "wikipedia:Java Development Kit") \- Java开发所需。

JDK、full JRE 和 headless JRE 互相冲突，因为较小的包是其子集： 

  * JDK 冲突并提供 full JRE，
  * full JRE 冲突并提供 headless JRE。

版本 | Headless JRE | Full JRE | JDK | 文献 | 源码   
---|---|---|---|---|---  
[OpenJDK 25](<https://openjdk.java.net/projects/jdk/23/>) | [jre-openjdk-headless](<https://archlinux.org/packages/?name=jre-openjdk-headless>)包 | [jre-openjdk](<https://archlinux.org/packages/?name=jre-openjdk>)包 | [jdk-openjdk](<https://archlinux.org/packages/?name=jdk-openjdk>)包 | [openjdk-doc](<https://archlinux.org/packages/?name=openjdk-doc>)包 |  [openjdk-src](<https://archlinux.org/packages/?name=openjdk-src>)包  
[OpenJDK 21](<https://openjdk.java.net/projects/jdk/21/>) | [jre21-openjdk-headless](<https://archlinux.org/packages/?name=jre21-openjdk-headless>)包 | [jre21-openjdk](<https://archlinux.org/packages/?name=jre21-openjdk>)包 | [jdk21-openjdk](<https://archlinux.org/packages/?name=jdk21-openjdk>)包 | [openjdk21-doc](<https://archlinux.org/packages/?name=openjdk21-doc>)包 |  [openjdk21-src](<https://archlinux.org/packages/?name=openjdk21-src>)包  
[OpenJDK 17](<https://openjdk.java.net/projects/jdk/17/>) | [jre17-openjdk-headless](<https://archlinux.org/packages/?name=jre17-openjdk-headless>)包 | [jre17-openjdk](<https://archlinux.org/packages/?name=jre17-openjdk>)包 | [jdk17-openjdk](<https://archlinux.org/packages/?name=jdk17-openjdk>)包 | [openjdk17-doc](<https://archlinux.org/packages/?name=openjdk17-doc>)包 |  [openjdk17-src](<https://archlinux.org/packages/?name=openjdk17-src>)包  
[OpenJDK 11](<https://openjdk.java.net/projects/jdk/11/>) | [jre11-openjdk-headless](<https://archlinux.org/packages/?name=jre11-openjdk-headless>)包 | [jre11-openjdk](<https://archlinux.org/packages/?name=jre11-openjdk>)包 | [jdk11-openjdk](<https://archlinux.org/packages/?name=jdk11-openjdk>)包 | [openjdk11-doc](<https://archlinux.org/packages/?name=openjdk11-doc>)包 |  [openjdk11-src](<https://archlinux.org/packages/?name=openjdk11-src>)包  
[OpenJDK 8](<https://openjdk.java.net/projects/jdk8/>) | [jre8-openjdk-headless](<https://archlinux.org/packages/?name=jre8-openjdk-headless>)包 | [jre8-openjdk](<https://archlinux.org/packages/?name=jre8-openjdk>)包 | [jdk8-openjdk](<https://archlinux.org/packages/?name=jdk8-openjdk>)包 | [openjdk8-doc](<https://archlinux.org/packages/?name=openjdk8-doc>)包 |  [openjdk8-src](<https://archlinux.org/packages/?name=openjdk8-src>)包  
  
**IcedTea-Web** — Java Web Start 和已弃用的 Java 浏览器插件。 

     <https://icedtea.classpath.org/download/icedtea-web-docs/1.8/html/en/icedtea-web.html> || [icedtea-web](<https://archlinux.org/packages/?name=icedtea-web>)包

**OpenJDK EA** — Oracle 最新的 OpenJDK 开发版Early-Access构建版本。 

     <https://jdk.java.net> || [java-openjdk-ea-bin](<https://aur.archlinux.org/packages/java-openjdk-ea-bin/>)AUR

**OpenJDK GA** — Oracle 最新的 OpenJDK 通用可用版本发布构建。 

     <https://jdk.java.net> || [java-openjdk-bin](<https://aur.archlinux.org/packages/java-openjdk-bin/>)AUR

**OpenJDK Wakefield** — JDK 在 Linux 上对 Wayland 桌面环境（WIP）支持。 

     <https://openjdk.org/projects/wakefield/> || [jdk-openjdk-wakefield](<https://aur.archlinux.org/packages/jdk-openjdk-wakefield/>)AUR

### OpenJFX

[OpenJFX](<https://wiki.openjdk.java.net/display/OpenJFX/Main>) 是 [JavaFX](<https://en.wikipedia.org/wiki/JavaFX> "wikipedia:JavaFX") 的开源实现。如果您使用的是 Oracle JDK，则[无需安装](<https://wiki.openjdk.java.net/display/OpenJFX/Repositories+and+Releases>)此软件包。此软件包只适用于 Java 的开源实现（OpenJDK 项目）及其衍生产品的用户。 

版本 | 运行环境与开发工具 | 文档 | 源码   
---|---|---|---  
[OpenJFX 26](<https://wiki.openjdk.java.net/display/OpenJFX/Main>) |  [java-openjfx](<https://aur.archlinux.org/packages/java-openjfx/>)AUR |  [java-openjfx-doc](<https://aur.archlinux.org/packages/java-openjfx-doc/>)AUR |  [java-openjfx-src](<https://aur.archlinux.org/packages/java-openjfx-src/>)AUR  
[OpenJFX 21](<https://wiki.openjdk.java.net/display/OpenJFX/Main>) | [java21-openjfx](<https://aur.archlinux.org/packages/java21-openjfx/>)AUR | [java21-openjfx-doc](<https://aur.archlinux.org/packages/java21-openjfx-doc/>)AUR |  [java21-openjfx-src](<https://aur.archlinux.org/packages/java21-openjfx-src/>)AUR  
[OpenJFX 17](<https://wiki.openjdk.java.net/display/OpenJFX/Main>) | [java17-openjfx](<https://aur.archlinux.org/packages/java17-openjfx/>)AUR | [java17-openjfx-doc](<https://aur.archlinux.org/packages/java17-openjfx-doc/>)AUR |  [java17-openjfx-src](<https://aur.archlinux.org/packages/java17-openjfx-src/>)AUR  
[OpenJFX 11](<https://wiki.openjdk.java.net/display/OpenJFX/Main>) | [java11-openjfx](<https://aur.archlinux.org/packages/java11-openjfx/>)AUR | [java11-openjfx-doc](<https://aur.archlinux.org/packages/java11-openjfx-doc/>)AUR |  [java11-openjfx-src](<https://aur.archlinux.org/packages/java11-openjfx-src/>)AUR  
[OpenJFX 8](<https://wiki.openjdk.java.net/display/OpenJFX/Main>) | [java8-openjfx](<https://aur.archlinux.org/packages/java8-openjfx/>)AUR | [java8-openjfx-doc](<https://aur.archlinux.org/packages/java8-openjfx-doc/>)AUR |  [java8-openjfx-src](<https://aur.archlinux.org/packages/java8-openjfx-src/>)AUR  
  
###  其他实现

  * **AWS Corretto** — Amazon Web Services 的 OpenJDK 发行版。

     <https://aws.amazon.com/corretto/> || [amazon-corretto-8](<https://aur.archlinux.org/packages/amazon-corretto-8/>)AUR [amazon-corretto-11](<https://aur.archlinux.org/packages/amazon-corretto-11/>)AUR [amazon-corretto-17](<https://aur.archlinux.org/packages/amazon-corretto-17/>)AUR [amazon-corretto-21-bin](<https://aur.archlinux.org/packages/amazon-corretto-21-bin/>)AUR

  * **Azul JDK** — Azul 的 JDK 实现。请注意，Azul Zulu Builds of OpenJDK 是开源的，而 Azul Zulu Prime Builds of OpenJDK 是商业产品，免费用于开发和评估。

     <https://www.azul.com/downloads/> ||
    Zulu: [zulu-8-bin](<https://aur.archlinux.org/packages/zulu-8-bin/>)AUR [zulu-11-bin](<https://aur.archlinux.org/packages/zulu-11-bin/>)AUR [zulu-17-bin](<https://aur.archlinux.org/packages/zulu-17-bin/>)AUR [zulu-21-bin](<https://aur.archlinux.org/packages/zulu-21-bin/>)AUR
    Zulu Prime: [zing-8-bin](<https://aur.archlinux.org/packages/zing-8-bin/>)AUR [jdk17-zulu-prime-bin](<https://aur.archlinux.org/packages/jdk17-zulu-prime-bin/>)AUR [zing-21-bin](<https://aur.archlinux.org/packages/zing-21-bin/>)AUR

  * **Eclipse Adoptium/Temurin** — Eclipse 的 JRE/JDK 实现，基于 Hotspot JVM（前身为 AdoptOpenJDK）。请注意，JRE 被称为 Eclipse Temurin。

     <https://adoptium.net/> || [jdk-temurin](<https://aur.archlinux.org/packages/jdk-temurin/>)AUR [jdk17-temurin](<https://aur.archlinux.org/packages/jdk17-temurin/>)AUR [jdk11-temurin](<https://aur.archlinux.org/packages/jdk11-temurin/>)AUR

  * **IBM Certified** — IBM Semeru Runtime Certified Edition。

     <https://www.ibm.com/semeru-runtimes/downloads> || [jdk11-j9-bin](<https://aur.archlinux.org/packages/jdk11-j9-bin/>)AUR

  * **IBM J9** — IBM 的 JRE 实现，使用 OpenJ9 贡献。

     <https://www.ibm.com/support/pages/java-sdk-downloads> || [jdk8-j9-bin](<https://aur.archlinux.org/packages/jdk8-j9-bin/>)AUR [jdk7-j9-bin](<https://aur.archlinux.org/packages/jdk7-j9-bin/>)AUR [jdk7r1-j9-bin](<https://aur.archlinux.org/packages/jdk7r1-j9-bin/>)AUR

  * **Liberica JDK** — BellSoft 的 Liberica JDK 实现。

     <https://bell-sw.com/libericajdk/> || [liberica-jre-8-full-bin](<https://aur.archlinux.org/packages/liberica-jre-8-full-bin/>)AUR [liberica-jdk-8-full-bin](<https://aur.archlinux.org/packages/liberica-jdk-8-full-bin/>)AUR [liberica-jre-11-bin](<https://aur.archlinux.org/packages/liberica-jre-11-bin/>)AUR [liberica-jre-11-full-bin](<https://aur.archlinux.org/packages/liberica-jre-11-full-bin/>)AUR [liberica-jdk-11-bin](<https://aur.archlinux.org/packages/liberica-jdk-11-bin/>)AUR [liberica-jdk-11-full-bin](<https://aur.archlinux.org/packages/liberica-jdk-11-full-bin/>)AUR [liberica-jdk-17-full-bin](<https://aur.archlinux.org/packages/liberica-jdk-17-full-bin/>)AUR [liberica-jdk-21-full-bin](<https://aur.archlinux.org/packages/liberica-jdk-21-full-bin/>)AUR

  * **Microsoft OpenJDK** — Microsoft 的 OpenJDK 发行版。

     <https://www.microsoft.com/openjdk/> || [microsoft-openjdk-11-bin](<https://aur.archlinux.org/packages/microsoft-openjdk-11-bin/>)AUR [microsoft-openjdk-17-bin](<https://aur.archlinux.org/packages/microsoft-openjdk-17-bin/>)AUR [microsoft-openjdk-21-bin](<https://aur.archlinux.org/packages/microsoft-openjdk-21-bin/>)AUR

  * **OpenJ9** — Eclipse 的 JRE/JDK 实现，基于 J9 JVM，由 IBM 贡献。

     <https://www.eclipse.org/openj9/> || [jdk-openj9-bin](<https://aur.archlinux.org/packages/jdk-openj9-bin/>)AUR [jdk17-openj9-bin](<https://aur.archlinux.org/packages/jdk17-openj9-bin/>)AUR [jdk11-openj9-bin](<https://aur.archlinux.org/packages/jdk11-openj9-bin/>)AUR [jdk8-openj9-bin](<https://aur.archlinux.org/packages/jdk8-openj9-bin/>)AUR

  * **Oracle JDK** — Oracle 的商业许可的 OpenJDK 构建。请注意，某些版本只能通过手动下载获得，这需要签署 OTN 协议并创建 Oracle 账户。

     <https://www.oracle.com/java/technologies/downloads/> ||
    JRE: [jre](<https://aur.archlinux.org/packages/jre/>)AUR [jre-lts](<https://aur.archlinux.org/packages/jre-lts/>)AUR [jre11](<https://aur.archlinux.org/packages/jre11/>)AUR [jre8](<https://aur.archlinux.org/packages/jre8/>)AUR [jre7](<https://aur.archlinux.org/packages/jre7/>)AUR
    JDK: [jdk](<https://aur.archlinux.org/packages/jdk/>)AUR [jdk-lts](<https://aur.archlinux.org/packages/jdk-lts/>)AUR [jdk11](<https://aur.archlinux.org/packages/jdk11/>)AUR [jdk8](<https://aur.archlinux.org/packages/jdk8/>)AUR [jdk7](<https://aur.archlinux.org/packages/jdk7/>)AUR

**注意：** Oracle JDK 的 32 位版本可以通过前缀 `bin32-` 找到，例如 [bin32-jre](<https://aur.archlinux.org/packages/bin32-jre/>)AUR。它们使用 [java32-runtime-common](<https://aur.archlinux.org/packages/java32-runtime-common/>)AUR，其功能与 [java-runtime-common](<https://archlinux.org/packages/?name=java-runtime-common>)包 相同，但添加了 `32` 的后缀，例如 `java32`。[java32-environment-common](<https://aur.archlinux.org/packages/java32-environment-common/>)AUR 也是同理，只有 32 位的 JDK 包使用它。

###  开发工具

对于集成开发环境，见[List of applications/Utilities#Integrated development environments](<../zh-cn/List_of_applications/Utilities.html#Integrated_development_environments> "List of applications/Utilities") 和 [Java IDEs](<../zh-cn/List_of_applications/Utilities.html#Java_IDEs> "List of applications/Utilities") 子分区。 

为了阻止逆向工程，可以使用[proguard](<https://aur.archlinux.org/packages/proguard/>)AUR等混淆器。 

####  反编译器

  * **CFR** — Java decompiler, supporting modern features of Java 9, 10 and beyond.

     <https://www.benf.org/other/cfr/> || [cfr](<https://archlinux.org/packages/?name=cfr>)包

  * **Fernflower** — Analytical decompiler for Java, developed as part of [IntelliJ IDEA](</wzh/index.php?title=IntelliJ_IDEA&action=edit&redlink=1> "IntelliJ IDEA（页面不存在）").

     <https://github.com/JetBrains/intellij-community/tree/master/plugins/java-decompiler/engine> || [fernflower-git](<https://aur.archlinux.org/packages/fernflower-git/>)AUR

  * **Vineflower** — Java decompiler forked from Fernflower, aiming to improve code quality. Also available as an [IntelliJ IDEA](</wzh/index.php?title=IntelliJ_IDEA&action=edit&redlink=1> "IntelliJ IDEA（页面不存在）") plugin.

     <https://github.com/Vineflower/vineflower> || [vineflower](<https://aur.archlinux.org/packages/vineflower/>)AUR

  * **Krakatau** — Java decompiler, assembler, and disassembler.

     <https://github.com/Storyyeller/Krakatau> || [krakatau-git](<https://aur.archlinux.org/packages/krakatau-git/>)AUR

  * **Procyon decompiler** — Experimental Java decompiler, inspired by ILSpy and Mono.Cecil.

     <https://bitbucket.org/mstrobel/procyon/wiki/Java%20Decompiler> || [procyon-decompiler](<https://archlinux.org/packages/?name=procyon-decompiler>)包

  * **Java Decompiler (JD-Core)** — Popular Java decompiler providing a GUI (see JD-GUI) and supporting Java 1-10.

     <https://java-decompiler.github.io/> || [jd-core-java](<https://aur.archlinux.org/packages/jd-core-java/>)AUR

  * **Jadx** — Android DEX to Java decompiler with an optional GUI (see Jadx-GUI).

     <https://github.com/skylot/jadx> || [jadx](<https://archlinux.org/packages/?name=jadx>)包

  * **[JAD](<https://en.wikipedia.org/wiki/JAD_\(software\)> "wikipedia:JAD \(software\)")** — Unmaintained Java decompiler (last release 2006).

     <https://varaneckas.com/jad> || [jad](<https://archlinux.org/packages/?name=jad>)包

####  GUI前端

  * **Bytecode Viewer** — Java reverse engineering suite, including a decompiler, editor and debugger; Frontend for CFR/Fernflower/Procyon.

     <https://bytecodeviewer.com> || [bytecode-viewer](<https://aur.archlinux.org/packages/bytecode-viewer/>)AUR

  * **Recaf** — An easy to use modern Java bytecode editor that abstracts away the complexities of Java programs; Frontend for CFR/Fernflower/Procyon.

     <https://www.coley.software/Recaf/> || [recaf-bin](<https://aur.archlinux.org/packages/recaf-bin/>)AUR

  * **Java Decompiler (JD-GUI)** — Popular Java decompiler providing a GUI and supporting Java 1-10; Frontend for JD-Core.

     <https://java-decompiler.github.io/> || [jd-gui](<https://aur.archlinux.org/packages/jd-gui/>)AUR

  * **Jadx-GUI** — Android APK DEX to Java decompiler with an optional GUI; Frontend for Jadx.

     <https://github.com/skylot/jadx> || [jadx](<https://archlinux.org/packages/?name=jadx>)包

  * **Luyten** — An Open Source Java Decompiler Gui; Frontend for Procyon.

     <https://github.com/deathmarine/Luyten> || [luyten](<https://aur.archlinux.org/packages/luyten/>)AUR== 在JVM间切换 ==

帮助脚本 _archlinux-java_ (软件包: [java-runtime-common](<https://archlinux.org/packages/?name=java-runtime-common>)包) 提供了如下功能: 
    
    archlinux-java <COMMAND>
    
    COMMAND:
    status          列出已安装的 Java 环境及当前启用的环境
    get             返回设置为默认的 Java 环境的短名称
    set <JAVA_ENV>  强制将 <JAVA_ENV> 设置为默认
    unset           取消当前默认的 Java 环境
    fix             修复无效/损坏的默认 Java 环境配置
    
###  列出兼容的安装了的Java环境
    
    $ archlinux-java status
    
例如: 
    
    $ archlinux-java status
    Available Java environments:
      java-11-openjdk (default)
      java-8-openjdk/jre
    
这里的`(default)`表示目前默认使用`java-11-openjdk`，Java和其他二进制文件的调用都将依赖于此Java安装。前面的输出中也显示，这里只安装了OpenJDK 8的JRE部分。 

###  改变默认Java环境
    
    # archlinux-java set <JAVA_ENV_NAME>
    
例如: 
    
    # archlinux-java set java-8-openjdk/jre
    
**提示：** 若要看到可用的`<JAVA_ENV_NAME>`名称，请使用`archlinux-java status`。

注意，`archlinux-java` 不会允许您设置无效的Java环境。在前面的例子中，只安装了[jre8-openjdk](<https://archlinux.org/packages/?name=jre8-openjdk>)包，而**没有** 安装[jdk8-openjdk](<https://archlinux.org/packages/?name=jdk8-openjdk>)包，所以设置`java-8-openjdk`将会失败： 
    
    # archlinux-java set java-8-openjdk
    
    '/usr/lib/jvm/java-8-openjdk' is not a valid Java environment path
    
###  取消设置的默认Java环境

无需取消Java环境的设置，因为提供环境的软件包通常会考虑到这一点。但若想这样做，只需使用`unset`命令： 
    
    # archlinux-java unset
    
###  解决默认Java环境的问题

如果设置了一个无效的Java环境链接，尝试调用`archlinux-java fix`命令以修复它。还要注意，如果没有设置默认的Java环境，它将寻找有效的环境并尝试设置。它会优先考虑官方支持的软件包"OpenJDK 8"。 
    
    # archlinux-java fix
    
###  运行非默认Java版本的程序

如果想用另一个版本的Java启动一个程序（例如系统同时安装了Java 18——默认版本——和11，而您要使用Java 11），可以用一个shell脚本包装应用程序，在本地改变Java的默认路径： 
    
    #!/bin/sh 
    
    export PATH="/usr/lib/jvm/java-11-openjdk/bin/:$PATH"
    exec /path/to/application "$@"
    
对于[systemd](<../zh-cn/Systemd.html> "Systemd")服务，您可以在[drop-in file](<../zh-cn/Drop-in_file.html> "Drop-in file")中附加`JAVA_HOME`到环境变量： 
    
    /etc/systemd/system/_unit_.d/override.conf
    
    [Service]
    Environment=JAVA_HOME=/usr/lib/jvm/java-11-openjdk

##  软件包支持 archlinux-java 的先决条件

**注意：** 这条信息同样适用于 `archlinux32-java` 的32位Java包，如果它们的包或者可执行名字里有 `32` ，都可适用。

这个分区的信息针对愿意提供包作为备份JVM给 [AUR](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 的贡献者，并且能够用 `archlinux-java` 集成Arch Linux JVM方案（即：与 `archlinux-java` 兼容）。如果要这样的话，这些包应该： 

  * 把所有文件放在 `/usr/lib/jvm/java-${JAVA_MAJOR_VERSION}-${VENDOR_NAME`}
  * 确认所有的 [java-runtime-common](<https://archlinux.org/packages/?name=java-runtime-common>)包 和 [java-environment-common](<https://archlinux.org/packages/?name=java-environment-common>)包 提供的可执行链接在相关包里都可用
  * 把所有链接从 `/usr/bin` 移动到可执行文件里，除非这些链接不属于 [java-runtime-common](<https://archlinux.org/packages/?name=java-runtime-common>)包 和 [java-environment-common](<https://archlinux.org/packages/?name=java-environment-common>)包
  * 用 `-${VENDOR_NAME}${JAVA_MAJOR_VERSION} ` 的格式给手册页添加后缀以防止冲突（查阅 [jre8-openjdk](<https://archlinux.org/packages/?name=jre8-openjdk>)包 文件列表，它的手册页用 `-openjdk8` 做后缀）
  * 不要定义任何[冲突](<../zh-cn/PKGBUILD.html#conflicts> "PKGBUILD")和[替代](<../zh-cn/PKGBUILD.html#replaces> "PKGBUILD")，用其他的JDK，`java-runtime`，`java-runtime-headless` 和 `java-environment`
  * 在 _安装函数_ 里使用 `archlinux-java` 脚本以将Java环境设置为默认**如果没有其他可用的Java环境准备设置的话** （即：这些包**不应该强制** 被装为默认）。查阅[官方支持的Java环境包源码](<https://gitlab.archlinux.org/archlinux/packaging/packages/java-openjdk>)做例子

同时也要注意： 

  * 包需要的**任何** Java环境都应声明依赖，和通常一样在 `java-runtime`、`java-runtime-headless` 或 `java-environment` 里声明。
  * 包如果需要**特定的Java提供商** ，应该在相关包里声明依赖。
  * OpenJDK 包现在应该声明 `provides="java-runtime-openjdk=${pkgver}"` 等。这能让第三方的包在没有特定版本要求的OpenJDK里声明依赖== 疑难解答 ==

### MySQL

由于JDBC-drivers经常使用URL中的端口来建立与数据库的连接，它被认为是 “远程”的（即MySQL不会按照其默认设置监听该端口），尽管它们可能运行在同一台主机上，因此，若要使用JDBC和MySQL，应按照[MariaDB#Grant remote access](<../zh-cn/MariaDB.html#Grant_remote_access> "MariaDB")中的说明，启用对MySQL的远程访问。 

### IntelliJ IDEA

如果在设置JDK的时候选择了系统的JDK，同时碰到了错误提示`The selected directory is not a valid home for JDK`，此时应重新安装另一个JDK包，并在IDEA设置中选择它。 

###  伪装成另一个窗口管理器

可以使用[suckless.org](<https://tools.suckless.org/x/wmname>)中的[wmname](<https://archlinux.org/packages/?name=wmname>)包来使JVM相信其正运行于其它窗口管理器。这也许能解决在[Awesome](<../zh-cn/Awesome.html> "Awesome")或[Dwm](<../zh-cn/Dwm.html> "Dwm")或[Ratpoison](<../zh-cn/Ratpoison.html> "Ratpoison")等窗口管理器中出现的Java GUI渲染问题。这种做法能够有效，是因为JVM包含了一个已知的、non-re-parenting窗口管理器的硬编码列表。为了达到最大的讽刺效果，一些用户喜欢伪装成`LG3D`，这是由Sun用Java编写的non-re-parenting窗口管理器[Project Looking Glass](<https://en.wikipedia.org/wiki/Project_Looking_Glass> "wikipedia:Project Looking Glass")。尝试设置`compiz`、`Metacity`或`LG3D`： 
    
    $ wmname _窗口管理器名称_
    
运行了这条命令后，必须重启有问题的程序。 

另外，可以使用[javaagent JavaMatePatch](<https://github.com/zheludkovm/JavaMatePatch>)，它是在[MATE](<../zh-cn/MATE.html> "MATE")中设置WM名称并解决Java Swing应用程序在全屏启动时工作不正常的bug的工具。在Java选项中添加`-javaagent:JavaMatePatch-1.0.0-SNAPSHOT.jar=_窗口管理器名称_`来使用它。 

###  字体难以辨认

除了下面[#更好的字体渲染](<#%E6%9B%B4%E5%A5%BD%E7%9A%84%E5%AD%97%E4%BD%93%E6%B8%B2%E6%9F%93>)中的建议，有些字体可能依然难以辨认。使用微软的字体或许能有所改善，安装[ttf-ms-fonts](<https://aur.archlinux.org/packages/ttf-ms-fonts/>)AUR即可。 

###  某些应用没有文字

如果某些应用完全没有文字，使用[FS#40871](<https://bugs.archlinux.org/task/40871>)中建议的[#提示和技巧](<#%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7>)下的选项可能会有所帮助。 

###  灰色窗口/应用不随窗口管理器调整大小/菜单自动关闭

标准的Java GUI工具包有一个non-re-parenting窗口管理器的硬编码列表，如果使用不在该列表中的窗口管理器，在运行某些Java应用时可能会有问题。最常见的问题之一是Java应用渲染成了一个灰色盒子而不是GUI。另一个问题是菜单能够响应点击，但马上又会关闭。 

以下内容也许有所帮助： 

  * 见[#伪装成另一个窗口管理器](<#%E4%BC%AA%E8%A3%85%E6%88%90%E5%8F%A6%E4%B8%80%E4%B8%AA%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8>)。
  * 设置`_JAVA_AWT_WM_NONREPARENTING=1` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。
  * 对于较新的版本，设置`AWT_TOOLKIT=MToolkit` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。
  * 对于[xmonad](<../zh-cn/Xmonad.html> "Xmonad")，使用[SetWMName](<https://wiki.haskell.org/Xmonad/Frequently_asked_questions#Using_SetWMName>)。然而，当同时使用`XMonad.Hooks.EwmhDesktops`时，其效果可能会被取消。这种情况下，在`LogHook`中添加`>> setWMName "LG3D"`可能会有帮助。

更多信息，请参阅[Java应用程序问题，Applet java控制台](<https://wiki.haskell.org/Xmonad/Frequently_asked_questions#Problems_with_Java_applications.2C_Applet_java_console>)。 

###  调试JavaFX应用时系统卡住

如果调试JavaFX应用时系统卡住了，可以尝试提供JVM选项`-Dsun.awt.disablegrab=true`。 

见[[1]](<https://bugs.java.com/bugdatabase/view_bug?bug_id=6714678>)。 

###  JavaFX's MediaPlayer constructor throws an exception

从JavaFX的声音模块中创建MediaPlayer类的实例可能会产生以下异常（Oracle JDK和OpenJDK都是如此）： 
    
    ... (i.e. FXMLLoader construction exceptions) ...
    Caused by: MediaException: UNKNOWN : com.sun.media.jfxmedia.MediaException: Could not create player! : com.sun.media.jfxmedia.MediaException: Could not create player!
     at javafx.scene.media.MediaException.exceptionToMediaException(MediaException.java:146)
     at javafx.scene.media.MediaPlayer.init(MediaPlayer.java:511)
     at javafx.scene.media.MediaPlayer.<init>(MediaPlayer.java:414)
     at <constructor call>
    ...
    
这是因为JavaFX和Arch Linux仓库中的[ffmpeg](<https://archlinux.org/packages/?name=ffmpeg>)包构建不兼容。 

安装[ffmpeg-compat-55](<https://aur.archlinux.org/packages/ffmpeg-compat-55/>)AUR以解决问题。如果[ffmpeg-compat-55](<https://aur.archlinux.org/packages/ffmpeg-compat-55/>)AUR无法构建，可以尝试安装[ffmpeg3.4](<https://aur.archlinux.org/packages/ffmpeg3.4/>)AUR。 

见[[2]](<https://www.reddit.com/r/archlinux/comments/70o8o6/using_a_javafx_mediaplayer_in_arch>)。 

###  Java程序无法打开外部链接

如果Java应用无法将链接打开到浏览器等应用，请安装[gvfs](<https://archlinux.org/packages/?name=gvfs>)包，因为`Desktop.Action.BROWSE`办法依赖于它。见[[3]](<https://bugs.launchpad.net/ubuntu/+source/openjdk-8/+bug/1574879/comments/2>)。 

如果应用程序打印错误消息`java.lang.UnsupportedOperationException: The BROWSE action is not supported on the current platform!`，这通常是此问题的明确指示。 

### Error initializing QuantumRenderer: no suitable pipeline found

可能的问题和解决方法： 

  * 没有GTK2。安装[gtk2](<https://archlinux.org/packages/?name=gtk2>)包。
  * 没有OpenJFX。安装[java-openjfx](<https://aur.archlinux.org/packages/java-openjfx/>)AUR。

##  提示和技巧

**注意：** 本节中的建议适用于所有使用明确安装（外部）的Java运行环境的应用程序。有些应用程序捆绑了自己（私有）的运行环境，或使用自己的GUI、字体渲染等机制，以下内容不一定完全适用于这种情况。

大多数Java应用的行为都可以通过向Java运行时提供预定义变量来控制。从[这个论坛帖子](<https://bbs.archlinux.org/viewtopic.php?id=72892>)来看，一种方法是在`~/.bash_profile`中添加以下一行 (或在`/etc/profile.d/jre.sh`添加来影响那些不通过`~/.bash_profile`运行的程序）： 
    
    export _JAVA_OPTIONS="-D**< option 1>** -D**< option 2>**..."
    
例如，使用系统抗锯齿字体并使swing使用GTK的外观与体验（look and feel）： 
    
    export _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel'
    
存在三个这样的变量，在下表中解释的选项优先考虑。 

JAVA_TOOL_OPTIONS  | 影响应用程序以及javac、jshell等工具。   
---|---  
JDK_JAVA_OPTIONS  | 影响通过java命令启动的一切应用程序，需要Java 9。   
（命令行选项）  | 在 "class name"参数前指定的参数是Java选项。   
_JAVA_OPTIONS  | 旧方法，影响应用程序和工具。   
  
###  更好的字体渲染

开源和闭源的Java实现都有不合适的抗锯齿字体实现。这可以通过以下办法来解决: `-Dawt.useSystemAAFontSettings=on`，`-Dswing.aatext=true`

详见[Java Runtime Environment fonts](<../zh-cn/Java_Runtime_Environment_fonts.html> "Java Runtime Environment fonts")。 

###  禁止命令行里的 'Picked up _JAVA_OPTIONS' 消息

设置 JDK_JAVA_OPTIONS 环境变量会使Java（openjdk）向stderr写出以下形式的信息：'Picked up JDK_JAVA_OPTIONS=...'。为了禁止终端中显示这些信息，可以在`~/.bashrc`中取消设置环境变量，并alias java，将这些选项传递为命令行参数： 
    
    _SILENT_JAVA_OPTIONS="$_JAVA_OPTIONS"
    unset _JAVA_OPTIONS
    alias java='java "$_SILENT_JAVA_OPTIONS"'
    
非交互式的Shell，如Java程序的启动脚本，（通常）不读取`~/.bashrc`，但仍从其父进程中继承了导出的变量（而父进程又在某个时间从读取了`~/.bash_profile`的登录Shell中继承了它）。 

至于这种情况，一般会在`~/.bashrc`的开头放一个声明，以避免读取文件。这样变量就会传递到通过桌面菜单启动的程序，如果是交互式Shell，则会使用alias来代替（这则不能用于脚本）。 

###  GTK LookAndFeel（外观与体验）

如果你的Java程序看起来很丑，你可能想为swing组件设置默认外观与体验： 
    
    swing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel
    
一些Java程序坚持用跨平台的金属风格外观与体验。在这些情况下，你可以通过设置下面的属性强制这些app用GTK外观和外观: 
    
    swing.crossplatformlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel
    
####  GTK3支持

在Java 9以前，GTK LookAndFeel是针对GTK2链接的，而许多较新的桌面应用程序使用GTK3。这种GTK版本之间的不兼容可能会破坏使用Java插件的GUI应用程序，因为在Java不支持在同一进程中混合使用GTK2和GTK3（如LibreOffice 5.0）。 

GTK LookAndFeel可以针对GTK`2`、`2.2`和`3`运行，默认为GTK3。可以通过设置以下属性来调整： 

`jdk.gtk.version=3`

### HiDPI

根据GUI框架的不同，[HiDPI#Java applications](<../zh-cn/HiDPI.html#Java_applications> "HiDPI")可以使用不同的方法启用。 
