**翻译状态：**

  * 本文（或部分内容）译自 [Arch User Repository](<https://wiki.archlinux.org/title/Arch_User_Repository> "arch:Arch User Repository")，最近一次同步于 2026-01-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_User_Repository?diff=0&oldid=857520>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_User_Repository_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [AUR 扫除日](<../zh-cn/AUR_%E6%89%AB%E9%99%A4%E6%97%A5.html> "AUR 扫除日")
  * [AUR 助手](<../zh-cn/AUR_%E5%8A%A9%E6%89%8B.html> "AUR 助手")
  * [AUR 提交准则](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html> "AUR 提交准则")
  * [Aurweb RPC 界面](</wzh/index.php?title=Aurweb_RPC_%E7%95%8C%E9%9D%A2&action=edit&redlink=1> "Aurweb RPC 界面（页面不存在）")
  * [创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")
  * [官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")
  * [软件包维护者指导原则](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85%E6%8C%87%E5%AF%BC%E5%8E%9F%E5%88%99.html> "软件包维护者指导原则")
  * [非官方用户仓库](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html> "非官方用户仓库")
  * [.SRCINFO](<../zh-cn/.SRCINFO.html> ".SRCINFO")

[_Arch 用户软件仓库_](<https://aur.archlinux.org>)（Arch User Repository，AUR）是为 [Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux") 用户而建，由社区主导的软件仓库。AUR 中的软件包以软件包描述文件（[PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")）的形式提供，用户自己通过 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 生成包，再由 [pacman](<../zh-cn/Pacman.html#%E5%85%B6%E5%AE%83%E5%91%BD%E4%BB%A4> "Pacman") 安装。创建 AUR 的初衷是供社区管理和分享新的软件包，并由官方定期从中挑选软件包进入 [extra](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Extra") 仓库。本文介绍用户访问和使用 AUR 的方法。 

许多官方仓库软件包都来自 AUR。通过 AUR，大家可以相互分享新的软件包生成脚本（[PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 和其他相关文件）。用户还可以为软件包[投票](<#%E7%BB%99%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%8A%95%E7%A5%A8>)。如果一个软件包投票足够多，没有许可证问题且打包质量好，那么它就很有希望被收录进官方 _extra_ 仓库（以后就可以直接通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 或 [Arch 构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统")安装了）。 

**警告：** AUR 中的软件包是由其他用户编写的，这些 `PKGBUILD` 完全是非官方的，未经彻底审查。使用这些文件的风险由您自行承担。

**注意：** 如果你计划要使用 AUR 仓库，**强烈建议** 关注 [AUR 常规邮件列表](<https://lists.archlinux.org/mailman3/lists/aur-general.lists.archlinux.org/>)，该列表被用于发布安全警告。[[1]](<https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/FFCMZGL4UQODYKZGUY7KTN3UBF3XN66P/>) [[2]](<https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/7EZTJXLIAQLARQNTMEW2HBWZYE626IFJ/>)

##  入门

用户可以从 [AUR 网站](<https://aur.archlinux.org>)下载 `PKGBUILD` 文件。这些 `PKGBUILD` 可以通过 _makepkg_ 生成软件包，最后由 _pacman_ 进行安装。 

  * 确保已经[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")了 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包。
  * 浏览 [#常见问题](<#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98>)一节，以获得对最常见问题的解答。
  * 在从 AUR 构建软件包之前，您可能希望调整 `/etc/makepkg.conf` 以优化系统的构建过程。通过调整 `MAKEFLAGS` 变量、使用多核进行压缩或使用不同的压缩算法，可以在多核处理器的系统上显著缩短包构建时间。用户还可以通过 `CFLAGS` 变量启用特定于硬件的编译器优化。详情参见 [makepkg](<../zh-cn/Makepkg.html#%E4%BC%98%E5%8C%96> "Makepkg")。

如果您设置了 [AUR SSH 身份验证](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html#%E8%AE%A4%E8%AF%81> "AUR 提交准则")，也可以通过 SSH 连接到 AUR：运行 `ssh aur@aur.archlinux.org help` 以获得可用指令的列表。 

##  安装与更新软件包

从 AUR 安装软件包并不困难。基本步骤如下： 

  1. 从 AUR 下载 `PKGBUILD` 和其他构建文件（比如 [systemd](<../zh-cn/Systemd.html> "Systemd") 单元文件和补丁，通常不是实际代码）。
  2. 验证 `PKGBUILD` 和其它相关文件，确保其中不含有恶意代码。
  3. 在保存文件的目录下运行 `makepkg`。这将下载代码，编译并打包。
  4. 运行 `pacman -U _package_file_` 将软件包安装到您的系统上。

###  准备

首先，确保[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")了 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包，该[元软件包](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "元软件包")提供了 [make](<https://archlinux.org/packages/?name=make>)包 等用于从源码进行编译的工具： 

**注意：** AUR 中的软件包会假定构建环境里已安装了 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包。

然后，选择一个合适的构建目录。该目录仅用作生成软件包或从源码构建时的工作目录，因此任何空白目录都可以。下面的示例中使用 `~/builds` 作为编译目录。 

###  获取软件包构建所需文件

通过在 [AUR 主页](<https://aur.archlinux.org/>)中搜索，找到要安装的软件包。点击搜索结果中的软件名称，进入软件包信息页。阅读描述并确认是否为目标软件，并检查软件的更新时间和评论。 

确认无误后，有几种方法可以获取包的构建文件： 

  * 克隆其 [git](<../zh-cn/Git.html> "Git") 存储库，在其 AUR 页面的“包详细信息”中标记为“Git Clone URL”。这是首选方法，其优点是您可以通过 `git pull` 轻松获取包的更新。

    $ git clone https://aur.archlinux.org/_package_name_.git

  * 通过单击其 AUR 页面右侧“Package Actions”下的“Download snapshot”链接或在终端中下载快照：

    $ curl -L -O https://aur.archlinux.org/cgit/aur.git/snapshot/_package_name_.tar.gz

**注意：** 快照文件是被压缩的，必须被解压（最好在为 AUR 构建预留的目录中）：`tar -xvf _package_name_.tar.gz`

  * 使用 [GitHub 上的 archlinux/aur](<https://github.com/archlinux/aur>) 只读镜像，每个包都位于一个分支中。建议只克隆一个分支（整个存储库太大，速度会很慢）。您可以使用以下两种方法之一执行此操作： 
    * 使用 `git clone --single-branch`：
          
          $ git clone --branch _package_name_ --single-branch https://github.com/archlinux/aur.git

    * [部分克隆](<../zh-cn/Git.html#%E9%83%A8%E5%88%86%E6%8E%A5%E6%94%B6> "Git")这个仓库 (`git clone --depth=1`) 和选择性[添加分支](<../zh-cn/Git.html#%E8%8E%B7%E5%8F%96%E5%85%B6%E4%BB%96%E5%88%86%E6%94%AF> "Git")：

    $ git clone --depth=1 https://github.com/archlinux/aur.git; cd aur  
    $ git remote set-branches --add origin _package_name_  
     $ git fetch  
    $ git switch _package_name_

###  如果需要，获取 PGP 公钥

检查 _.sig_ 或 _.asc_ 形式的签名文件是否是 `PKGBUILD` 源数组的一部分，如果是，则获取 PKGBUILD [validpgpkeys](<../zh-cn/PKGBUILD.html#validpgpkeys> "PKGBUILD") 数组中列出的公钥之一。更多信息请参考 [makepkg#验证签名](<../zh-cn/Makepkg.html#%E9%AA%8C%E8%AF%81%E7%AD%BE%E5%90%8D> "Makepkg")。 

###  构建软件包

切换到含有软件包的 `PKGBUILD` 文件的目录： 
    
    $ cd _package_name_
    
**警告：** 请仔细检查 git 代码库中的 `PKGBUILD`、所有 _.install_ 文件以及其它文件，确认是否带有恶意或危险命令。如有任何怀疑，请不要构建软件包，并到论坛或邮件列表中[寻求帮助](<../zh-cn/%E5%B8%B8%E8%A7%84%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html#%E9%A2%9D%E5%A4%96%E6%94%AF%E6%8F%B4> "常规故障排除")。过去已有发现数例含恶意代码的软件包。[[3]](<https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/FFCMZGL4UQODYKZGUY7KTN3UBF3XN66P/>) [[4]](<https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/7EZTJXLIAQLARQNTMEW2HBWZYE626IFJ/>)

查看所有提供的文件中的内容。例如使用 _less_ 查看 `PKGBUILD`： 
    
    $ less PKGBUILD
    
**提示：** 如果您正在更新软件包，您可能需要查看最后一次提交以来的变动。 

  * 您可以使用 `git show` 来查看最后一次提交之后的变动。
  * 您也可以使用 _vimdiff_ ：`git difftool @~..@ --tool=vimdiff`。使用 _vimdiff_ 的好处是可以查看到所有文件，以及对出现变更部分的提示。

接下来开始生成软件包。检查文件后，以普通用户权限执行 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") ，下面是一些有用的参数： 

  * `-s`/`--syncdeps` 会在构建之前使用 [pacman](<../zh-cn/Pacman.html> "Pacman") 自动解析和安装任何依赖项。如果包依赖于其他 AUR 包，则您应先手动安装它们。
  * `-i`/`--install` 会在构建成功后安装软件包。这使您可以跳过通常需手动完成的下一步。
  * `-r`/`--rmdeps` 会在构建后删除不需要的构建时依赖项。但是，下次更新包时可能需要重新安装这些依赖项。
  * `-c`/`--clean` 会在构建后清理临时构建文件，因为它们不再需要。这些文件通常仅在调试构建过程时才需要。

**提示：** 使用 ` git clean -dfx` 可以删除所有不被 git 跟踪的文件，从而删除所有以前构建的包文件。

###  安装包

现在可以使用 pacman 安装该软件包： 
    
    # pacman -U _package_name_ -_version_ -_architecture_.pkg.tar.zst
    
**注意：**

  * 如果您在 `makepkg.conf` 中更改了 `PKGEXT`，则包文件的名称可能会略有不同。
  * 以上示例只是对构建过程的简要总结。**特别** 推荐阅读 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 和 [Arch 构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统")文章以了解更多详情。

**提示：** 在不进行构建的情况下，您可以用 `makepkg --packagelist` 来获取生成的软件包文件名列表。

###  升级包

在包含包的 `PKGBUILD` 的目录中，您必须首先使用命令更新文件： 
    
    $ git pull
    
然后按照之前的构建和安装说明进行操作。 

###  更新包

Pacman 不支持 AUR，因此更新您安装的所有包是 _您的职责_ ，而不是 pacman 的。如果官方仓库中的包更新了，您需要重新构建依赖于那些库的 AUR 包。`checkrebuild` 和 [rebuild-detector](<https://archlinux.org/packages/?name=rebuild-detector>)包 提供的 `rebuild-detector` [钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")可用于查找需重新构建的软件包。 

##  账户状态

###  封禁（Suspension）

作为[软件包维护者](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85.html> "软件包维护者")时，可以对用户配置“封禁”字段，从而挂起目标用户。**当用户被封禁时，他们不能：**

  * 登录 <https://aur.archlinux.org>
  * 接收通知
  * 与 git 界面交互

###  非活动（Inactivity）

当编辑自己的账户或作为 _软件包维护者_ 编辑其他用户的账户时，可以设置“非活动”字段。使用非活动账户有两个原因： 

  * 在其账户页面上显示某人被标记为非活动的日期
  * 根据他们对新提案的不活动情况，生成当前的活跃 _软件包维护者_ 计数

##  反馈

###  在软件包上添加评论

[AUR 网页界面](<https://aur.archlinux.org>)中有一个评论工具，允许用户就改进提出建议和反馈给 `PKGBUILD` 贡献者。 

**提示：** 避免将补丁或 `PKGBUILD` 粘贴到评论部分：它们很快就会过时，最终会不必要地占用大量空间。请将这些文件通过电子邮件发送给维护者，甚至可以使用 [pastebin](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8.html#Pastebin_%E6%9C%8D%E5%8A%A1> "Pastebin")。

[Python-Markdown](<https://python-markdown.github.io/>) 提供了基本的 [Markdown](<https://en.wikipedia.org/wiki/Markdown> "wikipedia:Markdown") 语法来格式化评论。 

**注意：**

  * 此实现与官方[语法规则](<https://daringfireball.net/projects/markdown/syntax>)或许会有一些[差异](<https://python-markdown.github.io/#differences>)。
  * 对软件包 [Git](<../zh-cn/Git.html> "Git") 存储库的提交哈希值，以及对 [Flyspray](<../zh-cn/Flyspray.html> "Flyspray") 工单的引用会被自动转换为链接。
  * 长评论默认折叠，可按需展开。

###  给软件包投票

**所有的** Arch 用户都可以通过 AUR 界面为喜欢的软件包**投票** 。所有软件包都有机会被包维护者接手，并收录至 [extra](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Extra") 仓库。投票数是该选拔过程的重要依据之一，因此请尽可能地投票！ 

注册 [AUR 网站](<https://aur.archlinux.org/>)账户，在浏览软件包时会看到投票选项。注册后，还可以通过 [aur-auto-vote-git](<https://aur.archlinux.org/packages/aur-auto-vote-git/>)AUR 在命令行中投票。 

此外，如果你设置了 [AUR SSH 身份认证](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html#%E8%AE%A4%E8%AF%81> "AUR 提交准则")，可以使用 ssh 密钥直接通过命令行投票，不再需要保存或者输入 AUR 密码： 
    
    $ ssh aur@aur.archlinux.org vote _package_name_
    
###  将软件包标记为过期

首先，点击软件包页面的“Flag Out-of-date”（中文版为“标记为过期”），并说明过期的原因，最好包含新版本的发布说明或 [tarball](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html#%E4%BB%85%E5%BD%92%E6%A1%A3> "归档与压缩") 的链接。 

可以通过邮件通知维护人员。如果 _两周_ 后还是没有得到答复，可以发出 _遗弃_ （orphan）请求。更多信息请参考 [AUR 提交准则#请求](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html#%E8%AF%B7%E6%B1%82> "AUR 提交准则")。 

**注意：**[VCS 软件包](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则") 在 `pkgver` 变化时并不会过时，所以不要标记它们，且维护者也只会取消标记并无视请求。AUR 维护者不应该仅为升高 `pkgver` 就进行提交。

##  调试包构建过程

  1. 在构建任何东西之前，通过[更新](<../zh-cn/Pacman.html#%E5%8D%87%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman")确保您的构建环境是最新的。
  2. 确保您已安装 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包。
  3. 对 `makepkg` 搭配使用 `-s` 选项，以在开始构建过程之前检查并安装所有依赖项。
  4. 试试默认的 [makepkg 配置](<https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/blob/main/makepkg.conf>)。
  5. 常见问题请参阅 [Makepkg#问题处理](<../zh-cn/Makepkg.html#%E9%97%AE%E9%A2%98%E5%A4%84%E7%90%86> "Makepkg")。

如果您在构建包时遇到问题，请先阅读其 `PKGBUILD` 及其 AUR 页面上的评论。 

可能 `PKGBUILD` 本身就有配置问题。如果您无法自行解决，请将其报告给维护者（例如，通过[在 AUR 页面的评论中发布您遇到的错误](<#%E5%9C%A8%E8%BD%AF%E4%BB%B6%E5%8C%85%E4%B8%8A%E6%B7%BB%E5%8A%A0%E8%AF%84%E8%AE%BA>)）。您也可以在 [AUR 问题、讨论和 PKGBUILD 请求论坛](<https://bbs.archlinux.org/viewforum.php?id=38>)寻求帮助。 

问题原因可能并不简单，可能会涉及自定义到 `CFLAGS`、`LDFLAGS` 和 `MAKEFLAGS`。为排除由您的特定系统配置引起的问题，请在[干净的 chroot](<../zh-cn/%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%B9%B2%E5%87%80%E7%9A%84_chroot.html> "创建一个干净的 chroot") 中构建包。如果在纯净 chroot 中构建仍然失败，则问题很可能出在 `PKGBUILD`。 

请参阅[创建软件包#检查包的逻辑性](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html#%E6%A3%80%E6%9F%A5%E5%8C%85%E7%9A%84%E9%80%BB%E8%BE%91%E6%80%A7> "创建软件包")以获得关于使用 [namcap](<../zh-cn/Namcap.html> "Namcap") 的信息。如果您希望审核 `PKGBUILD`，请将其发布到 [aur-general 邮件列表](<https://lists.archlinux.org/mailman3/lists/aur-general.lists.archlinux.org/>)以获得[软件包维护者](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85.html> "软件包维护者")和其他 AUR 成员的反馈，或发布到[创建和修改包论坛](<https://bbs.archlinux.org/viewforum.php?id=4>)。您还可以在 [Libera Chat](<https://libera.chat>) 上的 [#archlinux-aur](<ircs://irc.libera.chat/archlinux-aur>) [IRC 频道](<../zh-cn/Arch_%E7%9A%84_IRC_%E9%A2%91%E9%81%93.html> "Arch 的 IRC 频道")中寻求帮助。 

##  提交

用户可以使用 AUR 分享 `PKGBUILD`。参见 [AUR 提交准则](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html> "AUR 提交准则")以获得更多细节。 

##  Web 接口翻译

参阅 AUR 源码中的 [i18n.md](<https://gitlab.archlinux.org/archlinux/aurweb/-/blob/master/doc/i18n.md>) 获得关于创建和维护 [AUR Web 界面](<https://aur.archlinux.org>)翻译的详细信息。 

##  历史

最初，人们仅将 `PKGBUILD`、所需的补充文件和构建好的包上传到 `ftp://ftp.archlinux.org/incoming` 服务器。包及相关文件会暂存在此，直至一位“受信用户”（现已更名为[软件包维护者](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85.html> "软件包维护者")）看到这个程序并接管维护。 

然后，受信用户仓库诞生了。社区中，特定的个人被授权托管他们自己的仓库，以供他人使用。在更灵活、更易用的目标下，AUR 在这个基础上扩展壮大。事实上，AUR 维护者曾一直被称作受信用户（Trusted user，TU），直到更名为软件包维护者。 

在 2015 年 6 月 8 日到 8 月 8 日期间，AUR 从 3.5.1 版本迭代到 4.0.0，引入了通过 Git 仓库发布 `PKGBUILD` 的功能。 已存在的包会被丢弃，除非维护者手动地将它们移植到新的基础架构上。 

###  AUR3 包的 Git 仓库

Github 上的 [AUR 存档](<https://github.com/aur-archive>)中有一个包含移植时 AUR 3 的所有包的仓库。 

或者，采用等价的 [aur-mirror](<https://github.com/felixonmars/aur3-mirror/>) 仓库。 

##  常见问题

###  什么样的软件包能被放到 AUR？

AUR 中的软件包仅是编译脚本，即为 [pacman](<../zh-cn/Pacman.html> "Pacman") 构建二进制文件的蓝图。只要你遵循了打包内容的许可条例，基本上符合[规则](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html#%E6%8F%90%E4%BA%A4%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%9A%84%E8%A7%84%E5%88%99> "AUR 提交准则")的软件包都可以提交。有时候，下载的链接具有 "you may not link" 条款（即不可分发），这时就不能提供下载链接，而是要用程序名称代替，用户需要用其它方式提前获取受限制的源代码。有疑问请及时询问。 

###  怎么可以为 AUR 中的包投票？

见 [#给软件包投票](<#%E7%BB%99%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%8A%95%E7%A5%A8>)。 

###  软件包维护者是什么？

参见 [Arch 术语#软件包维护者](<../zh-cn/Arch_%E6%9C%AF%E8%AF%AD.html#%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85> "Arch 术语")。 

###  Arch User Repository 和 extra 仓库有何区别？

Arch User Repository 是储存所有用户提交的 `PKGBUILD` 的地方，软件包需通过 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 手动生成。吸引足够多的社区关注及有软件包维护者支持的 `PKGBUILD` 会被收录进 [extra](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Extra") 仓库（由软件包维护者维护），以二进制软件包形式提供，可以由 [pacman](<../zh-cn/Pacman.html> "Pacman") 安装。 

###  AUR 中的软件包过期了，我该怎么做？

参见 [#将软件包标记为过期](<#%E5%B0%86%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%A0%87%E8%AE%B0%E4%B8%BA%E8%BF%87%E6%9C%9F>)。 

同时，你可以在本地编辑 `PKGBUILD` 来自行更新软件包。有时更新不需要修改构建流程，只用按需更新 `pkgver` 或 `source` 数组即可。 

###  `makepkg` 无法构建某个软件包，我该怎么办？

您很可能忘了点啥，参见 [#调试包构建过程](<#%E8%B0%83%E8%AF%95%E5%8C%85%E6%9E%84%E5%BB%BA%E8%BF%87%E7%A8%8B>)。 

###  ERROR: One or more PGP signatures could not be verified! 我该怎么办？

最有可能的情况是您没有所需的公钥来验证下载的文件。详情参见 [Makepkg#验证签名](<../zh-cn/Makepkg.html#%E9%AA%8C%E8%AF%81%E7%AD%BE%E5%90%8D> "Makepkg")。 

###  如何编写 PKGBUILD？

查阅 [AUR 提交准则#提交软件包的规则](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html#%E6%8F%90%E4%BA%A4%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%9A%84%E8%A7%84%E5%88%99> "AUR 提交准则") 和 [创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")。 

###  我想提交一个 PKGBUILD，希望别人帮忙检查错误。

您可以通过多种渠道提交您的材料供审核；请看 [#调试包构建过程](<#%E8%B0%83%E8%AF%95%E5%8C%85%E6%9E%84%E5%BB%BA%E8%BF%87%E7%A8%8B>)。 

###  PKGBUILD（AUR 软件包）怎样才能被收录到 extra 软件仓库？

一般至少需要 10 票，并且要有软件包维护者愿意维护，否则即便有上千票也不会收录。当然，如果某个软件包维护者愿意维护一个软件包的话，投票数往往不是决定因素。 

一些流行的软件包未被收录的原因一般是： 

  * Arch Linux 的软件仓库中已经有了别的版本。
  * 没有再发布的授权许可。
  * 那个软件包的功能只和 AUR 相关（例如，是个 [AUR helper](<../zh-cn/AUR_helper.html> "AUR helper")）

另见[包进入 extra 仓库的规则](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85%E6%8C%87%E5%AF%BC%E5%8E%9F%E5%88%99.html#%E8%BD%AF%E4%BB%B6%E5%8C%85%E8%BF%9B%E5%85%A5_extra_%E4%BB%93%E5%BA%93%E7%9A%84%E8%A7%84%E5%88%99> "软件包维护者指导原则")。 

###  如何加速编译？

参见 [Makepkg#减少编译时间](<../zh-cn/Makepkg.html#%E5%87%8F%E5%B0%91%E7%BC%96%E8%AF%91%E6%97%B6%E9%97%B4> "Makepkg")。 

###  foo 和 foo-git 的区别是什么？

很多 AUR 软件包都包含稳定版本和开发版本。开发版本一般都会有代表[版本控制系统](<../zh-cn/Category:%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F.html> "版本控制系统")的[后缀](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#%E5%8C%85%E5%90%8D> "VCS 软件打包准则")。开发版本并不是为日常使用而设计的，不过可能包含新功能或者 bug 修复。由于执行 `makepkg` 时会从软件源获取最新的代码，因此 AUR 上的 `pkgver()` 并不代表上游的最新更改。这些软件包很可能会跳过对 [VCS 源代码](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#VCS_%E6%BA%90%E4%BB%A3%E7%A0%81> "VCS 软件打包准则")的完整性效验。 

同时请参阅 [系统维护#使用经测试的软件包](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E4%BD%BF%E7%94%A8%E7%BB%8F%E6%B5%8B%E8%AF%95%E7%9A%84%E8%BD%AF%E4%BB%B6%E5%8C%85> "系统维护")。 

###  为啥某个软件包从 AUR 消失了？

可能是有软件包维护者认领了这个软件包，并把它收入到 [extra](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Extra") 仓库中了。 

软件包也可能因为不满足[提交软件包的规则](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html#%E6%8F%90%E4%BA%A4%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%9A%84%E8%A7%84%E5%88%99> "AUR 提交准则")而被删除，您可以在 [aur-requests 存档](<https://lists.archlinux.org/archives/list/aur-requests@lists.archlinux.org/>)中找到删除原因。 

**注意：** 通常被删除软件包的 git 仓库仍被保留，细节请参考 [AUR 提交准则#请求](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html#%E8%AF%B7%E6%B1%82> "AUR 提交准则")。

###  我要怎么找出从 AUR 里消失的软件包？

最简单的办法是检查软件包 AUR 页面的 HTTP 状态： 
    
    $ comm -23 <(pacman -Qqm | sort) <(curl <https://aur.archlinux.org/packages.gz> | gzip -cd | sort)
    
###  如何得到包含所有 AUR 包的列表？

  * <https://aur.archlinux.org/packages.gz>
  * 使用来自 [python3-aur](<https://aur.archlinux.org/packages/python3-aur/>)AUR 的 `aurpkglist`。
  * [新的 AUR 元数据存档](<https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/D4YC6Y7L4T5VSEONUCLHOX2R4NJKNIDP/>)

##  另请参阅

  * [AUR 网页界面](<https://aur.archlinux.org>)
  * [AUR 邮件列表](<https://lists.archlinux.org/mailman3/lists/aur-general.lists.archlinux.org/>)
