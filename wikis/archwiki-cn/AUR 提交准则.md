**翻译状态：**

  * 本文（或部分内容）译自 [AUR submission guidelines](<https://wiki.archlinux.org/title/AUR_submission_guidelines> "arch:AUR submission guidelines")，最近一次同步于 2025-01-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/AUR_submission_guidelines?diff=0&oldid=822050>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/AUR_submission_guidelines_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")
  * [软件包维护者指导原则](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85%E6%8C%87%E5%AF%BC%E5%8E%9F%E5%88%99.html> "软件包维护者指导原则")

用户可以通过 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") **分享** [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 脚本。AUR 中不包含任何二进制包，仅包含用户上传的 `PKGBUILD`，供其他用户下载使用。这些 `PKGBUILD` 都是非官方的，没有经过完整审查，使用风险自担。 

##  提交软件包

**警告：** 在提交前请先熟悉 [Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")及所有的“相关文章”。请**仔细检查** 上传的内容是否有误，**违反相应规则** 的软件包可能会**不经警告被直接删除** 。

如果在反复阅读该章节后仍不清楚软件包或构建/提交流程是否正确，可以将自己的 `PKGBUILD` 贴到 [AUR 邮件列表](<https://lists.archlinux.org/mailman3/lists/aur-general.lists.archlinux.org/>)、[论坛 AUR 版](<https://bbs.archlinux.org/viewforum.php?id=4>)、[中文论坛 AUR/ABS/PKGBUILD 版](<https://bbs.archlinuxcn.org/viewforum.php?id=29>)或 [IRC 频道](<../zh-cn/Arch_%E7%9A%84_IRC_%E9%A2%91%E9%81%93.html> "Arch 的 IRC 频道")，让大家帮您检查。 

###  提交软件包的规则

提交软件包时请遵循下列的规则: 

  * 任何提交的 `PKGBUILD` 都不能编译**已经** 位于**官方** 二进制软件包**仓库** 的程序。可通过[官方软件包数据库](<https://archlinux.org/packages/>)进行查找，如果在其中发现了任意版本的程序，就**不要** 进行提交。如果认为官方仓库的软件包已过期，请标记它。如果它有问题或者缺少功能，请反馈[反馈 bug 报告](<../zh-cn/%E6%BC%8F%E6%B4%9E%E6%8A%A5%E5%91%8A%E5%87%86%E5%88%99.html> "漏洞报告准则")。

     **唯一的例外** 是和官方打包版本相比增加或开启了**新的功能** 或者使用了不同的**补丁** 。这时需要修改 `pkgname` 来表示新增的功能。例如加入了边栏支持的 GNU screen（`screen`）应该命名为 `screen-sidebar`。此外还需要同时添加 `conflicts=('screen')` 以避免与官方仓库中的包冲突。

  * **检查 AUR** 中是否**已有** 相同软件包。如果已经有人维护某软件包，可以以评论的形式将更改报告给维护人员。如果软件包无人维护或维护者无反馈，可以按需将其认领并更新。不要创建重复的包。

  * 确保您的软件包**有人需要** 。在提交前请仔细想想：有人会用这个软件包吗？它非常特别吗？如果不是只有少数人觉得它有用，就提交它。

    AUR 和官方软件仓库是用于放置通用软件和软件相关的内容的，包括：可执行文件、配置文件、软件的在线/离线文档和软件直接使用的媒体数据。

  * 不支持 `x86_64` 架构的软件包[不允许上传到 AUR](<https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/GMYC74CRSFH7GGNENEUOODZUPWHOMX7A/>)。

  * 不要在 AUR `PKGBUILD` 中使用 `replaces`，除非这个软件包将要被重命名（例如当 _Ethereal_ 变成 _Wireshark_ 时）。如果这个软件包是**已经存在的软件包的另一版本** ，使用 `conflicts` （或者如果这个软件包被其他软件需要时，使用 `provides`）。两者的主要区别是：在 pacman 同步（-Sy）之后，如果遇到与 `replaces` 匹配并已经安装的软件包时，pacman 会立刻想去替换它。而 `conflicts` 则在安装软件包时进行替换。

  * 请为那些由版本控制系统构建，而不属于任何特定版本的软件包的包名添加合适的后缀，如 `-git`。具体细则见 [VCS 软件打包准则#软件包命名](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%91%BD%E5%90%8D> "VCS 软件打包准则")。

  * 当源码可获得时，那些**预构建**[可以直接部署](<https://en.wikipedia.org/wiki/Deliverable> "wikipedia:Deliverable")的二进制包应该加上 `-bin` 后缀， [Java](<../zh-cn/Java_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#%E5%9C%A8_Arch_Linux_%E4%B8%AD%E6%89%93_Java_%E5%8C%85> "Java 打包准则") 除外。除此之外，AUR 不应当包含 `makepkg` 创建的二进制包，也不应当包含文件列表。

  * 从特定版本的源码构建的包不应该添加后缀。

  * 请按照以下格式在 `PKGBUILD` 最上端加入包含当前**维护者** 和过去的**贡献者** 的信息**注释** ，记得对邮件地址进行必要的处理以避免被垃圾邮件骚扰。然后移除所有不必要的行。例如：

**注意：** 对邮件地址进行混淆会导致别人更难联系上你。

    如果您从其它人接手了一个 `PKGBUILD`，像这样把您的名字和邮件地址加到最上面。
    
    # Maintainer: Your Name <address at domain dot tld>
    
    如果在您之前有其他的维护者，请将它们添加到贡献者中。如果你不是初始上传者，也请将其加入贡献者中。如果您是协同维护者，也请加上现在的其他维护者。
    
    # Maintainer: Your name <address at domain dot tld>
    # Maintainer: Other maintainer's name <address at domain dot tld>
    # Contributor: Previous maintainer's name <address at domain dot tld>
    # Contributor: Original submitter's name <address at domain dot tld>
    
  * 为仓库添加 `LICENSE` 文件，建议使用 [0BSD 许可证](<https://spdx.org/licenses/0BSD.html>)。你可以直接[从 RFC 0040 复制许可证文本](<https://rfc.archlinux.page/0040-license-package-sources/#license-text>)。缺少许可证或使用与 0BSD 不同许可证的软件包[不允许](<https://rfc.archlinux.page/0040-license-package-sources/#aur>)被加入到官方软件源中。

###  认证

要向 AUR 写入软件包，用户需要创建一个 [SSH 密钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html> "SSH 密钥")。将公钥导入到用户账户的 _My Account_ 一节，然后为 `aur.archlinux.org` 主机配置对应的私钥，例如： 
    
    ~/.ssh/config
    
    Host aur.archlinux.org
      IdentityFile ~/.ssh/aur
      User aur

你应当为 AUR [生成新的密钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html#%E7%94%9F%E6%88%90%E5%AF%86%E9%92%A5%E5%AF%B9> "SSH 密钥")，而不是直接使用旧的，以在出问题时直接弃用密钥： 
    
    $ ssh-keygen -f ~/.ssh/aur
    
**提示：** 在输入公钥时可以通过换行的方式设置添加多个公钥。

###  创建软件包仓库

如果您正在[创建新的软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")，请通过[克隆](<../zh-cn/Git.html#%E8%8E%B7%E5%8F%96_Git_%E4%BB%93%E5%BA%93> "Git")所需的 [pkgbase](<../zh-cn/PKGBUILD.html#pkgbase> "PKGBUILD") 的方式建立一个远程 AUR 仓库和本地 [Git](<../zh-cn/Git.html> "Git") 仓库。如果软件包还不存在，则会出现以下预料之中的警告： 
    
    $ git -c init.defaultBranch=master clone ssh://aur@aur.archlinux.org/_pkgbase_.git
    
    Cloning into '_pkgbase_ '...
    warning: You appear to have cloned an empty repository.
    Checking connectivity... done.

**注意：** 如果 `_pkgbase_` 与[被删除](<#%E8%AF%B7%E6%B1%82>)的软件包相同，那克隆下来的仓库会不为空。

如果您已经有一个软件包了，但不是 Git 仓库的话，需要进行[初始化](<../zh-cn/Git.html#%E8%8E%B7%E5%8F%96_Git_%E4%BB%93%E5%BA%93> "Git")： 
    
    $ git -c init.defaultBranch=master init
    
并添加远程 AUR 地址： 
    
    $ git remote add _label_ ssh://aur@aur.archlinux.org/_pkgbase_.git
    
然后向远程仓库[拉取](<../zh-cn/Git.html#Working_with_remotes> "Git")以在 AUR 进行初始化。 

**提示：** 使用[拉取和变基](<https://git-scm.com/docs/git-pull#git-pull---rebasefalsetruemergespreserveinteractive>)来解决 `_pkgbase_` 匹配到已删除软件包的冲突问题。

###  提交和更新软件包

**警告：** 不想以全局身份提交？记得通过 `git config user.name [...]` 和 `git config user.email [...]` 编辑自己的本地身份！

**警告：** 你的提交会以[全局 Git 名称和邮件地址](<../zh-cn/Git.html#%E9%85%8D%E7%BD%AE> "Git")进行署名，且在推送后很难对提交进行修改（[FS#45425](<https://bugs.archlinux.org/task/45425>)）。如果你想以不同的身份推送到 AUR，可以使用 `git config user.name "..."` 和 `git config user.email "..."` 对单个包进行修改。

当释出新版本的软件时，更新 [pkgver](<../zh-cn/PKGBUILD.html#pkgver> "PKGBUILD") 或者 [pkgrel](<../zh-cn/PKGBUILD.html#pkgrel> "PKGBUILD") 变量来提示所有的用户更新。如果仅仅是对 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 的小修改（例如修正笔误），请不要更新这些变量。 

不要仅仅为了更新 `pkgver` 就更新 [VCS 软件包](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则")。当上游有新的提交时，他们不会被视为过时。只有当有其他变化，比如打包流程发生变化时，才应该进行更新。 

无论何时 `PKGBUILD` 的元数据发生变动（例如更新了 `pkgver()`），都需要重新生成 [.SRCINFO](<../zh-cn/.SRCINFO.html> ".SRCINFO")。否则 AUR 不会显示更新后的版本号。 

要上传或者更新一个软件包， _至少_ 要[添加](<../zh-cn/Git.html#%E8%AE%B0%E5%BD%95%E6%9B%B4%E6%94%B9> "Git") `PKGBUILD` 和 `.SRCINFO` 和其它所有新增的或者修改过的辅助文件（例如 [_.install_](<../zh-cn/PKGBUILD.html#install> "PKGBUILD") 文件或者如[软件包补丁](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E8%A1%A5%E4%B8%81.html> "软件包补丁")之类的[本地源码文件](<../zh-cn/PKGBUILD.html#source> "PKGBUILD")），写上有意义的提交信息并[提交](<../zh-cn/Git.html#%E8%AE%B0%E5%BD%95%E6%9B%B4%E6%94%B9> "Git")，最后[推送](<../zh-cn/Git.html#%E8%BF%9C%E7%A8%8B%E5%88%86%E6%94%AF> "Git")这些变动到 AUR 上。 

例如: 
    
    $ makepkg --printsrcinfo > .SRCINFO
    $ git add PKGBUILD .SRCINFO
    $ git commit -m "_useful commit message_ "
    $ git push
    
**注意：**

  * 如果您忘记在最后一次提交中包含 `.SRCINFO`，您可以通过 `git commit --amend` [修改最后一次提交](<https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend>)来使得 AUR 接受您的推送。
  * AUR 只允许推送到 `master` 分支。如果本地分支的名称不同，需要将其[重命名](<https://git-scm.com/docs/git-branch>)后再次推送。

**提示：** 为了保持工作目录和提交尽可能的干净，可以创建 [gitignore(5)](<https://man.archlinux.org/man/gitignore.5>) 文件来排除所有文件，然后再按需添加文件。

##  维护软件包

  * 阅读其他用户的反馈，并试着听从建议改进软件包，这是个学习的过程！
  * 升级软件包后，不要在评论中加入版本更新信息，这些信息会冲淡更重要的用户评论。
  * 不要提交软件包后就放任不管！检查更新并改进 `PKGBUILD` 是维护者的责任。
  * 发觉自己不再想维护某个软件包？可以通过 AUR 网页界面 `disown` 一个软件包并/或是在 AUR 邮件列表发条消息。如果这个包的所有维护者都 disown，那么它就会变成一个[“orphaned”](<https://aur.archlinux.org/packages?submit=Orphans>)软件包。
  * 自动化对维护人员来说很有用，但它不能取代[人工干预](<https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/AYISVT7SOB444HXHIF2CKA2TIHBESH2D/>)（例如：项目可能会修改许可证、添加或删除依赖关系，以及其它的显著更改）。自动更新 `PKGBUILD` 的风险将由您自行承担，任何出现问题的账户与他们提交的软件包都可能被无事前通知地删除。

##  请求

删除、合并、取消维护权限请求可以通过右侧“Package actions”的“File Request”链接执行。这会给当前的维护者和 [aur-requests 邮件列表](<https://lists.archlinux.org/mailman3/lists/aur-requests.lists.archlinux.org/>)自动发送邮件通知，之后[软件包维护者](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85.html> "软件包维护者")会接受或拒绝请求。 

###  删除

你可以请求 _unlist_ AUR 中的一个 `pkgbase`。提交时请附上原因说明（务必用英语），也可以是其它有用的细节（比方说其它包提供了相同的东西，或者如果你就是这个包的维护者，需要重命名且软件包所有者同意，等等）。 

**注意：**

  * 只在软件包的评论区解释原因并不够。当软件包维护者采取行动前，aur-request 邮件列表是唯一能取得这些信息的地方。
  * 删除请求可能被否决。如果你是这个包的维护者，我们可能会建议你 disown 这个软件包，以便其他维护者认领。
  * 在软件包被“删除”后，其 [Git](<../zh-cn/Git.html> "Git") 仓库仍可被[克隆](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html#%E8%8E%B7%E5%8F%96%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%9E%84%E5%BB%BA%E6%89%80%E9%9C%80%E6%96%87%E4%BB%B6> "AUR")。

###  合并

合并请求会删除 `pkgbase`，并将现有的投票数、评论转移到另一个 `pkgbase` 中。需要用到目标软件包的名称。 

这个操作适用于上游进行了[重命名项目](<https://lists.archlinux.org/archives/list/aur-requests@lists.archlinux.org/thread/CLPVKIYDKRCBOEITSWAG4FO5RBKTKGYG/#U73UG4AP6WMUIR23F7OA4ZKNILT6HZNU>)等情况。 

**注意：**

  * 这和 `git merge` 或者 GitLab 的 merge request 没有任何关系。
  * 由于投票和评论会转移到已经存在的目标中，如果一个包本身没有投票或评论，那么其效果与[#删除](<#%E5%88%A0%E9%99%A4>)并[链接到新包](<https://lists.archlinux.org/archives/list/aur-requests@lists.archlinux.org/thread/KSXL52EYMKTZXVO3WHWAUFEJI6DQAXV2/#KSXL52EYMKTZXVO3WHWAUFEJI6DQAXV2>)完全相同。

###  撤销所有权（orphan）

要求撤销当前维护者对 `pkgbase` 的所有权。如果现有维护者在两周之内没有响应，请求就会通过。另外，如果一个软件被标记为过期超过 180 天，请求会被自动通过。 
