**翻译状态：**

  * 本文（或部分内容）译自 [Arch Testing Team](<https://wiki.archlinux.org/title/Arch_Testing_Team> "arch:Arch Testing Team")，最近一次同步于 2024-04-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_Testing_Team?diff=0&oldid=802505>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_Testing_Team_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Arch 测试团队是 Arch 社区中的一个小组，负责确保提交到 [testing](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Testing") 存储库的软件包正常运行。这包括确保软件包安装正确，不会导致所依赖的软件包损坏等。 

Arch 测试员在证明其正确性之后[签名](</wzh/index.php?title=DeveloperWiki:CoreSignoffs&action=edit&redlink=1> "DeveloperWiki:CoreSignoffs（页面不存在）")软件包，以便可以将它们从 _testing_ 存储库移至 _core_ 存储库或 _extra_ 存储库。 

##  贡献

您可以通过[电子邮件](<mailto:bluewind@xinu.at>)与 [arch-testing-accounts@archlinux.org](<mailto:arch-testing-accounts@archlinux.org>) 联系并申请[测试者帐户](<https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/message/PXN2EZNSKUA6R45EMUC7WJ5CN5WNBYZD/>)，从而申请成为正式的 Arch 测试者。并至少需要在邮件中指明你想使用的用户名。 

如果您将得到一个测试帐户，您应该能够登录到 [archweb](<https://archlinux.org/devel>)，看到 _signoffs_ 标签就可以了。该 _signoffs_ 标签将包含当前处于测试仓库包的至少两个列表，并需要 _signoffs_ （即，证实一个包的正确性）。 

然后，您可以在本地测试列出的软件包，并通过单击每个软件包的 _signoff_ 按钮对它们进行签名（如果正确）。 

**提示：** 您可以通过使用 [arch-signoff](<https://archlinux.org/packages/?name=arch-signoff>)包 软件包中的 [signoff(1)](<https://man.archlinux.org/man/signoff.1>) 从命令行签名软件包来简化过程。

##  准则

为了测试 Arch 软件包，请牢记以下几个方面： 

  * 如果要测试依赖于内核模块的内核或软件包，**则应重新启动计算机并确保其正确启动**
  * 尽管不禁止在虚拟化软件上进行测试，但是它可能不如在裸机安装中测试软件包有用。这特别适用于易受不同硬件类型影响的软件包，例如内核软件包。
  * 如果要测试库，则可能要执行使用该库的二进制文件。使用 ldd 确保加载了共享库文件。
  * 同样，如果有一个附带可执行软件包的软件包，则鼓励测试其基本功能。
  * 如果在测试软件包时发现错误，请在 [bugtracker](<https://bugs.archlinux.org/>) 上添加详细的错误报告： 
    * 软件包名称，版本和 pkgrel
    * 软件包的哪个组件是错误的组件（例如，二进制文件之一或配置文件）
    * 错误的根源（例如，在安装或使用过程中等）
    * 任何相关的错误消息/日志
    * 确保该错误使用 _Packages: Testing_ 类别提交

##  协调

**注意：** 希望使用 _testing_ 存储库的人能经常检查 [arch-dev-public](<https://lists.archlinux.org/mailman3/lists/arch-dev-public.lists.archlinux.org/>) 邮件列表，以了解影响测试用户的任何已宣布的更改或注意事项。

您可以在 [#archlinux-testing](<ircs://irc.libera.chat/archlinux-testing>) IRC 频道上与其他测试人员协调。 

您可以在 [arch-commits](<https://lists.archlinux.org/mailman3/lists/arch-commits.lists.archlinux.org/>) 邮件列表上查看打包程序活动的更新（高流量）。 
