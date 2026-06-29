**翻译状态：**

  * 本文（或部分内容）译自 [Arch Security Team](<https://wiki.archlinux.org/title/Arch_Security_Team> "arch:Arch Security Team")，最近一次同步于 2020-05-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_Security_Team?diff=0&oldid=610296>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_Security_Team_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Arch 安全团队是一组志愿者，其目标是使用Arch Linux软件包跟踪安全问题。所有问题都在 [Arch Linux security tracker](<https://security.archlinux.org/>)上进行跟踪。该团队以前称为 _Arch CVE Monitoring Team_. 

##  任务

Arch 安全团队的任务是为提高 Arch Linux 的安全性做出贡献。 

团队最重要的职责是查找和跟踪分配了[常见漏洞和披露](<https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures> "wikipedia:Common Vulnerabilities and Exposures")（CVE）的问题。CVE 是公共的，由 _CVE-YYYY-number_ 形式的唯一 ID 标识。 

他们发布了 ASA（ _Arch Linux Security Advisory_ ），这是向 Arch 用户分发的特定于 Arch 的警告。ASA 已在跟踪器中安排进行同行评审，并且在发布之前需要团队成员的两次确认。 

在 [Arch Linux security tracker](<https://security.archlinux.org/>) 使用的是安全团队跟踪包，增加的 CVE 和生成文本咨询的平台。 

**注意：**

  * 一个 _Arch Linux Vulnerability Group_ (AVG) 是一组涉及相同内的一组包的 CVE 的 _pkgbase_ 。
  * 符合咨询条件的软件包必须是 _core_ ， _extra_ ， _community_ 或 _multilib_ 存储库的一部分。

##  贡献

为了参与漏洞的识别，建议： 

  * 遵循 [#archlinux-security](<ircs://irc.libera.chat/archlinux-security>) IRC 频道。它是报告和讨论 CVE，受影响的软件包以及第一个固定软件包版本的主要沟通媒介。
  * 为了及早收到有关新问题的警告，可以监视建议的 [#邮件列表](<#%E9%82%AE%E4%BB%B6%E5%88%97%E8%A1%A8>)以获取新的 CVE，并根据需要监视其他来源。
  * 我们鼓励志愿者查看咨询中的错误，问题或评论，并在 IRC 频道中进行报告。
  * 订阅邮件列表 [arch-security](<https://lists.archlinux.org/mailman3/lists/arch-security.lists.archlinux.org/>) 和 [oss-security](<https://oss-security.openwall.org/wiki/mailing-lists/oss-security>)。
  * 将代码提交给 [arch-security-tracker (GitHub)](<https://github.com/archlinux/arch-security-tracker>) 项目是为团队做出贡献的好方法。
  * 鼓励依赖 Arch Linux 软件包系统信息库的派生发行版做出贡献。这有助于所有用户的安全。

##  程序

在 Arch Linux 官方存储库中的软件包中发现安全漏洞时，应遵循以下步骤： 

###  信息共享和调查阶段

  * 通过您首选的渠道与 Arch 安全团队成员接触，以确保该问题已引起团队注意。
  * 为了证实该漏洞，请针对当前程序包版本（包括可能的补丁程序）验证 CVE 报告，并通过搜索引擎收集有关此问题的尽可能多的信息。如果您需要帮助调查安全问题，请在 IRC 频道上寻求建议或支持。

###  上游情况和错误报告

可能出现两种情况： 

  * 如果上游发布了可解决此问题的新版本，则安全团队成员应将该软件包标记为过期。 
    * 如果经过长时间的延迟仍未更新软件包，则应提交有关该漏洞的错误报告。
    * 如果这是一个关键的安全问题，则必须在将软件包标记为过期后立即提交错误报告。
  * 如果没有上游发行，则必须提交错误报告，其中包括用于缓解问题的补丁。错误报告中必须提供以下信息： 
    * 有关安全问题及其影响的描述
    * 链接到 CVE-ID 和（上游）报告
    * 如果没有可用的版本，请链接到可缓解此问题的上游修补程序（或附件）

###  跟踪和发布

团队成员必须执行以下任务： 

  * 团队成员将在 [security tracker](<https://security.archlinux.org/>) 上创建建议，并添加 CVE 进行跟踪。
  * 具有访问 [arch-security](<https://lists.archlinux.org/mailman3/lists/arch-security.lists.archlinux.org/>) 权限的团队成员将从跟踪器生成 ASA 并将其发布。

**注意：** 如果要报告私有错误，请联系 [security@archlinux.org](<https://lists.archlinux.org/archives/list/arch-security@lists.archlinux.org/message/VBW3INY5FOVDNM4XYXOF3OVHERNAS7WG/>)。请注意，私有错误报告的地址是 _security_ ，而不是 _arch-security_ 。私有错误是一个过于敏感的问题，无法发布到任何人都可以阅读和利用的地方，例如 Arch Linux 基础架构中的漏洞。

##  资源

### RSS

National Vulnerability Database (NVD)
    所有 CVE 漏洞：<https://nvd.nist.gov/download/nvd-rss.xml>
    所有经过全面分析的 CVE 漏洞：<https://nvd.nist.gov/download/nvd-rss-analyzed.xml>

###  邮件列表

oss-sec：有关自由软件安全性的主要列表，如果您想了解安全新闻，则此处会包含很多 CVE 属性。
    信息：<https://oss-security.openwall.org/wiki/mailing-lists/oss-security>
    订阅：oss-security-subscribe(at)lists.openwall.com
    存档：<https://www.openwall.com/lists/oss-security/>

完整的披露审核邮件列表（杂乱）。
    信息：<https://www.securityfocus.com/archive/1/description>
    订阅：bugtraq-subscribe(at)securityfocus.com

Full Disclosure：另一个全披露的邮件列表（杂乱）。
    信息：<https://nmap.org/mailman/listinfo/fulldisclosure>
    订阅：full-disclosure-request(at)seclists.org

还可以考虑遵循特定软件包的邮件列表，例如 LibreOffice, X.org, Puppetlabs, ISC等。 

###  其他发行版

其他发行版的资源（查找CVE，补丁，注释等）： 

Red Hat 和 Fedora
    
    咨询提要：<https://bodhi.fedoraproject.org/rss/updates/?type=security>
    CVE 跟踪器：<https://access.redhat.com/security/cve/><CVE-ID>
    错误跟踪器：<https://bugzilla.redhat.com/show_bug.cgi?id=><CVE-ID>

Ubuntu
    
    咨询供稿：<https://usn.ubuntu.com/usn/atom.xml>
    CVE 跟踪器：<https://people.canonical.com/~ubuntu-security/cve/?cve=><CVE-ID>
    数据库：<https://code.launchpad.net/~ubuntu-security/ubuntu-cve-tracker/master>

Debian
    
    CVE 跟踪器：<https://security-tracker.debian.org/tracker/><CVE-ID>/
    补丁追踪器：<https://tracker.debian.org/pkg/patch>
    数据库：<https://salsa.debian.org/security-tracker-team/security-tracker/tree/master/data>

OpenSUSE
    
    CVE 跟踪器：<https://www.suse.com/security/cve/><CVE-ID>/

###  其他

CVE 的 Mitre 和 NVD 链接
    
     <https://cve.mitre.org/cgi-bin/cvename.cgi?name=><CVE-ID>
     <https://web.nvd.nist.gov/view/vuln/detail?vulnId=><CVE-ID>

NVD 和 Mitre 不一定在归属后立即填写其 CVE 条目，因此与 Arch 并不总相关。CVE-ID 和“创建日期条目”字段没有特殊含义。CVE 由 CVE 编号颁发机构（CNA）归属，每个 CNA 在需要/提出要求时从 Mitre 获取 CVE 块，因此 CVE ID 未链接到归属日期。“创建日期条目”字段通常仅指示将 CVE 块分配给 CNA 的时间，仅此而已。 

Linux Weekly News：LWN 每天为各种发行版提供安全更新通知。
    <https://lwn.net/headlines/newrss>

###  更多

有关更多资源，请参见 OpenWall 的[开源软件安全性 Wiki](<https://oss-security.openwall.org/wiki/>). 

##  团队成员

Arch 安全团队的当前成员是： 

  * [Levente Polyak](</wzh/index.php?title=User:Anthraxx&action=edit&redlink=1> "User:Anthraxx（页面不存在）")
  * [Remi Gacogne](</wzh/index.php?title=User:Rgacogne&action=edit&redlink=1> "User:Rgacogne（页面不存在）")
  * [Christian Rebischke](</wzh/index.php?title=User:Shibumi&action=edit&redlink=1> "User:Shibumi（页面不存在）")
  * [Jelle van der Waa](</wzh/index.php?title=User:Jelly&action=edit&redlink=1> "User:Jelly（页面不存在）")
  * [Santiago Torres-Arias](</wzh/index.php?title=User:Sangy&action=edit&redlink=1> "User:Sangy（页面不存在）")
  * [Jonathan Roemer](</wzh/index.php?title=User:Pid1&action=edit&redlink=1> "User:Pid1（页面不存在）")
  * [Morten Linderud](</wzh/index.php?title=User:Foxboron&action=edit&redlink=1> "User:Foxboron（页面不存在）")

**注意：** 在 [IRC 频道](<../zh-cn/IRC_channels.html> "IRC channels")中运行 `!pingsec <msg>`，以突出显示当前所有安全团队成员。
