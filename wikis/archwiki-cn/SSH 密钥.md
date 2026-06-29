**翻译状态：**

  * 本文（或部分内容）译自 [SSH keys](<https://wiki.archlinux.org/title/SSH_keys> "arch:SSH keys")，最近一次同步于 2025-01-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/SSH_keys?diff=0&oldid=824942>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SSH_keys_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** The intro and _Background_ section ignore the server perspective. (在 [Talk:SSH 密钥](<../zh-cn/Talk:SSH_%E5%AF%86%E9%92%A5.html>) 中讨论)

对于使用[公钥加密](<https://zh.wikipedia.org/wiki/%E5%85%AC%E5%BC%80%E5%AF%86%E9%92%A5%E5%8A%A0%E5%AF%86> "zhwp:公开密钥加密")与[质询-应答式认证](<https://en.wikipedia.org/wiki/Challenge-response_authentication> "wikipedia:Challenge-response authentication")的 SSH 服务器，SSH 密钥可以作为证明身份的方法。基于密钥的认证主要优点在于，与密码认证相比，它不易遭受[暴力破解攻击](<https://zh.wikipedia.org/wiki/%E8%9B%AE%E5%8A%9B%E6%94%BB%E5%87%BB> "zhwp:蛮力攻击")，且在服务器被攻破的情况下也不会泄露您的有效凭证（详细信息请参考 [RFC 4251 9.4.4](<https://tools.ietf.org/html/rfc4251#section-9.4.4> "rfc:4251")）。 

不仅如此，SSH 密钥认证也会比传统的密码认证更加方便。当与被称作 SSH agent 的程序共用时，SSH 密钥可以让您无需记住或输入每个系统的密码，就能够连接到一个或多个服务器。 

基于密钥的认证并非没有缺点，可能也并非适用于一切环境，但在很多情况下可以提供一些有力的优势。对 SSH 密钥如何工作的概略理解会帮助您决定如何以及何时使用它们，以满足您的需求。 

本文假定您已经对于[安全外壳协议](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "安全外壳协议")有了基本理解，并[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")了 [openssh](<https://archlinux.org/packages/?name=openssh>)包 软件包。 

##  背景

SSH 密钥都是成对生成的，其一称为公钥，另一则称为私钥。私钥只由您所知，必须安全保管。相对地，公钥可以向您想连接的任何 SSH 服务器自由地共享。 

如果一个 SSH 服务器在文件中存有您的公钥，并收到了您的连接请求，就会使用您的公钥构建一个质询问题并发送给您。这一质询问题是一条加密信息，必须得到正确应答，服务器才能允许您访问。这条编码信息特别安全是在于，只有私钥持有者才能理解它。公钥可以用来加密信息，但不能用来解密同一条信息。只有您，私钥的持有者，能够正确理解这一质询问题并产生合适的应答。 

这一[质询-应答](<https://en.wikipedia.org/wiki/Challenge-response_authentication> "wikipedia:Challenge-response authentication")过程发生在后台，对用户不可见。只要您持有私钥（一般存放在 `~/.ssh/` 目录下），您的 SSH 客户端就应当能够向服务器回复正确的应答。 

私钥是受保护的秘密，因此建议以加密形式将其存储在磁盘上。当需要被加密的私钥时，为了解密它，需要先输入密码。虽然这在表面上可能像是您在向 SSH 服务器提供登录密码，但该密码只用于解密本地系统上的私钥。该密码并未通过网络传输。 

##  生成密钥对

通过运行 `ssh-keygen` 命令可以生成密钥对，具体“ _一般被认为充足_ ”且应当兼容于几乎所有客户端和服务器的选项请参考 [ssh-keygen(1)](<https://man.archlinux.org/man/ssh-keygen.1>)： 
    
    $ ssh-keygen
    
    Generating public/private ed25519 key pair.
    Enter file in which to save the key (/home/_username_ /.ssh/id_ed25519):
    Created directory '/home/_username_ /.ssh'.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/_username_ /.ssh/id_ed25519
    Your public key has been saved in /home/_username_ /.ssh/id_ed25519.pub
    The key fingerprint is:
    SHA256:RLy4JBv7jMK5qYhRKwHB3af0rpMKYwE2PBhALCBV3G8 _username_ @_hostname_
    The key's randomart image is:
    +--[ED25519 256]--+
    |%oooo. ..        |
    |== ..o.o.        |
    |==  . +o..       |
    |+ o o.ooE        |
    |...  *.oS        |
    | o..o ..         |
    |o=.. +o          |
    |+o*..+o          |
    |+.o+. .          |
    +----[SHA256]-----+
    
[randomart 图像](<https://www.cs.berkeley.edu/~dawnsong/papers/randomart.pdf>)作为一种简便的密钥指纹视觉辨识方式在 [OpenSSH 5.1](<https://www.openssh.com/txt/release-5.1>) 中引入。 

**注意：** 可以使用 `-a` 开关来指定密码加密的 KDF rounds 数量。

也可以用 `-C` 开关对公钥添加可选的注释栏，从而更容易在 `~/.ssh/known_hosts`、`~/.ssh/authorized_keys` 以及 `ssh-add -L` 输出等处进行辨识。例如： 
    
    $ ssh-keygen -C "$(whoami)@$(uname -n)-$(date -I)"
    
会添加一条注释，说明是哪个用户何时在哪台机器上创建的密钥。 

###  选择认证密钥类别

OpenSSH（对于认证密钥）支持数种签名算法，按照所采用的数学性质可分为两类： 

  1. [Ed25519](<https://zh.wikipedia.org/wiki/Curve25519> "zhwp:Curve25519") 以及 [ECDSA](<https://zh.wikipedia.org/wiki/%E6%A4%AD%E5%9C%86%E6%9B%B2%E7%BA%BF%E6%95%B0%E5%AD%97%E7%AD%BE%E5%90%8D%E7%AE%97%E6%B3%95> "zhwp:椭圆曲线数字签名算法")，依赖于椭圆曲线[离散对数](<https://zh.wikipedia.org/wiki/%E7%A6%BB%E6%95%A3%E5%AF%B9%E6%95%B0> "zhwp:离散对数")问题（ECDLP）；（[例子](<https://www.certicom.com/content/certicom/en/52-the-elliptic-curve-discrete-logarithm-problem.html>)）
  2. [RSA](<https://zh.wikipedia.org/wiki/RSA%E5%8A%A0%E5%AF%86%E7%AE%97%E6%B3%95> "zhwp:RSA加密算法")，依赖于对两个大质数之积进行分解的[实际困难度](<https://zh.wikipedia.org/wiki/%E6%95%B4%E6%95%B0%E5%88%86%E8%A7%A3#.E9.9A.BE.E5.BA.A6.E4.B8.8E.E5.A4.8D.E6.9D.82.E5.BA.A6> "zhwp:整数分解")。

[椭圆曲线密码学](<https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography>)（ECC）算法是对于公钥密码体制的[较新发展](<https://zh.wikipedia.org/wiki/%E6%A4%AD%E5%9C%86%E6%9B%B2%E7%BA%BF%E5%AF%86%E7%A0%81%E5%AD%A6#.E6.AD.B7.E5.8F.B2> "zhwp:椭圆曲线密码学")。其主要优势之一是[以较小密钥提供同等安全性](<https://zh.wikipedia.org/wiki/%E6%A4%AD%E5%9C%86%E6%9B%B2%E7%BA%BF%E5%AF%86%E7%A0%81%E5%AD%A6#Rationale> "zhwp:椭圆曲线密码学")的能力，使得计算密集操作更少（ _也就是_ 密钥创建、加密及解密更快）且存储及传输的要求更低。 

由于安全问题，DSA 密钥已被[废弃](<https://archlinux.org/news/openssh-70p1-deprecates-ssh-dss-keys/>)，且 SSH 实现正逐渐将其移除。OpenSSH 9.8 构建默认不带 DSA 密钥支持，Dropbear 2022.83 禁用了 DSA 密钥支持，libssh 0.11.0 完全移除了 DSA 密钥支持。因此[密码体制](<https://zh.wikipedia.org/wiki/%E5%AF%86%E7%A0%81%E4%BD%93%E5%88%B6> "zhwp:密码体制")的选择范围就限定在了 RSA 或两种 ECC 之一当中。 

[#RSA](<#RSA>) 密钥会提供最大的可移植性，而 [#Ed25519](<#Ed25519>) 会提供最佳的安全性，但需要新版本的客户端与服务器[[1]](<https://web.archive.org/web/20191222003107/https://www.gentoo.org/support/news-items/2015-08-13-openssh-weak-keys.html>)。. [#ECDSA](<#ECDSA>) 兼容性可能比 Ed25519 更好（虽然还是不如 RSA），但存在对于其安全性的怀疑（见下文）。 

默认的 Ed25519 会提供最佳安全性和不错的性能。ECDSA 比 Ed25519 更慢，但比 RSA 快，在安全性上存在些疑问（具体参见下文）。RSA 密钥提供了对旧服务器的最佳兼容性，但需要更大的密钥才能提供足够的安全性。 

**注意：** 这些密钥只用于认证您的身份；选择更强的密钥并不会在通过 SSH 传输数据时加重 CPU 负担。

**提示：** 为防止 SSH 密钥从设备上外泄，可以将密钥储存在 [FIDO/U2F 实体认证器](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "通用第二因素")或[可信平台模块](<../zh-cn/%E5%8F%AF%E4%BF%A1%E5%B9%B3%E5%8F%B0%E6%A8%A1%E5%9D%97.html> "可信平台模块")中。 

  * 在生成密钥时，可以使用特殊的“安全密钥”类型将 Ed25519 或 ECDSA 密钥储存在 FIDO/U2F 实体认证器上。具体信息请参考 [#FIDO/U2F](<#FIDO/U2F>)。
  * 可信平台模块支持 ECDSA 和 RSA，因此可以将 SSH 密钥封装在 TPM 内。具体信息请参考 [可信平台模块#SSH](<../zh-cn/%E5%8F%AF%E4%BF%A1%E5%B9%B3%E5%8F%B0%E6%A8%A1%E5%9D%97.html#SSH> "可信平台模块")。

#### Ed25519

[Ed25519](<https://ed25519.cr.yp.to/>) 在2014年1月被引入 [OpenSSH 6.5](<https://www.openssh.com/txt/release-6.5>)：“ _Ed25519 是一种能够提供比 ECDSA 及 DSA 更佳安全性及良好性能的椭圆曲线签名体系_ ”。其主要长处在于速度、时间恒定运行时（从而能够对抗侧信道攻击）以及无需晦暗不明的硬编码常数。[[2]](<https://git.libssh.org/projects/libssh.git/tree/doc/curve25519-sha256@libssh.org.txt>) 关于其工作方式，参见由一位 Mozilla 开发者撰写的[博客文章](<https://blog.mozilla.org/warner/2011/11/29/ed25519-keys/>)。 

它已经在[众多应用及库中](<https://zh.wikipedia.org/wiki/EdDSA#.E8.BD.AF.E4.BB.B6> "zhwp:EdDSA")得到实现，并且在 OpenSSH 中是[默认的密钥交换算法](<https://www.libssh.org/2013/11/03/openssh-introduces-curve25519-sha256libssh-org-key-exchange/>)（与密钥 _签名_ 不同）。 

Ed25519 密钥对生成方法如下： 

[ssh-keygen(1)](<https://man.archlinux.org/man/ssh-keygen.1>) 默认使用 Ed25519，因此不需要使用 `-t ed25519` 选项进行指定。使用以下命令生成密钥： 
    
    $ ssh-keygen
    
所有 Ed25519 密钥都是 256 位，故无需设置密钥尺寸。 

注意较老的 SSH 客户端与服务器可能不支持这些密钥。 

#### ECDSA

椭圆曲线数字签名算法（ECDSA）是 [OpenSSH 5.7](<https://www.openssh.com/txt/release-5.7>)（2011-01-24）到 OpenSSH 6.5（2014-01-30）间的首选认证（密钥交换）算法。 

对于它的担忧有两种： 

  1. _政治上的担忧_ ：在 NSA（美国国家安全局）被曝在软件、硬件组件及发布的标准中蓄意植入后门之后，由 NIST（美国国家标准技术研究所）产生的曲线的可信性[受到了质疑](<https://crypto.stackexchange.com/questions/10263/should-we-trust-the-nist-recommended-ecc-parameters>)；密码领域的知名人士对于 NIST 曲线的设计方式[表示](<https://www.schneier.com/blog/archives/2013/09/the_nsa_is_brea.html#c1675929>) [了](<https://safecurves.cr.yp.to/rigid.html>) [怀疑](<https://www.hyperelliptic.org/tanja/vortraege/20130531.pdf>)，并且之前已经有主动的污染[被](<https://www.schneier.com/blog/archives/2007/11/the_strange_sto.html>) [证实](<https://www.scientificamerican.com/article/nsa-nist-encryption-scandal/>)。
  2. _技术上的担忧_ ：对于[正确实现该标准的困难](<https://blog.cr.yp.to/20140323-ecdsa.html>)以及在实现不够谨慎情况下降低安全性的[迟缓与设计缺陷](<https://www.gossamer-threads.com/lists/openssh/dev/57162#57162>)。

[libssh curve25519 介绍](<https://git.libssh.org/projects/libssh.git/tree/doc/curve25519-sha256@libssh.org.txt#n4>)当中很好地总结了上述担忧。尽管政治上的担忧仍受到争议，但有[明确的共识](<https://news.ycombinator.com/item?id=7597653>)认为 [#Ed25519](<#Ed25519>) 技术上更优越，因此应当优先采用。 

可以使用以下方法生成 ECDSA 密钥对： 
    
    $ ssh-keygen -t ecdsa
    
ECDSA 密钥支持三种椭圆曲线大小：256，384 和 521 位，默认使用 256 位。如果想要生成更安全的 ECDSA 密钥对，可以使用 `-b` 选项进行指定： 
    
    $ ssh-keygen -t ecdsa -b 384
    
#### RSA

RSA 提供所有算法当中最佳的兼容性，但提供充足安全性所需的密钥尺寸较大。最低密钥大小为 1024 位，默认为 3072（具体请参考 [ssh-keygen(1)](<https://man.archlinux.org/man/ssh-keygen.1>)），最大为 16384。 

使用以下命令生成 RSA 密钥对： 
    
    $ ssh-keygen -t rsa
    
如果您想生成较强的 RSA 密钥对（ _例如_ 为了防范先进或未知攻击以及较高级的攻击者），只需为 `-b` 选项指定比默认更高的位值： 
    
    $ ssh-keygen -t rsa -b 4096
    
需要明白的是，使用更长的密钥存在收益递减。[[3]](<https://security.stackexchange.com/a/25377>)[[4]](<https://www.gnupg.org/faq/gnupg-faq.html#no_default_of_rsa4096>) GnuPG 常见问答记载：“ _如果你需要的安全性比 RSA-2048 所提供的更强，应该做的是改用椭圆曲线密码学——而不是接着使用 RSA_ 。”[[5]](<https://www.gnupg.org/faq/gnupg-faq.html#please_use_ecc>)

另一方面，最新版本的 [NSA Fact Sheet Suite B Cryptography](<https://web.archive.org/web/20160305203915/https://www.nsa.gov/ia/programs/suiteb_cryptography/index.shtml>) 建议对于 RSA 使用最少 3072 位的模，同时“ _为即将到来的抗量子算法迁移（做准备）_ ”。[[6]](<https://www.keylength.com/en/6/>)

####  FIDO/U2F

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：**[OpenSSH 8.2 版本](<https://www.openssh.com/txt/release-8.2>)添加了 FIDO2 resident 密钥支持，可以将 SSH 密钥存放在实体令牌上。 (在 [Talk:SSH 密钥](<../zh-cn/Talk:SSH_%E5%AF%86%E9%92%A5.html>) 中讨论)

[OpenSSH 8.2 版本](<https://www.openssh.com/txt/release-8.2>)添加了 FIDO/[U2F](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "U2F") [实体认证器](<https://zh.wikipedia.org/wiki/%E5%AE%89%E5%85%A8%E4%BB%A4%E7%89%8C> "zhwp:安全令牌")支持，可以使用上文描述的两种椭圆曲线签名方案。这使得可以将连接的实体令牌作为多重验证方案与私钥搭配使用。 

实体令牌需要用到 [libfido2](<https://archlinux.org/packages/?name=libfido2>)包。 

**注意：**

  * 客户端和服务器都需要支持 `ed25519-sk` 和 `ecdsa-sk` 密钥类型。
  * OpenSSH 使用中间件库来与实体令牌通信，其带有支持 USB 令牌的内部中间件。如果要使用其它中间件，可以通过[sshd_config(5) § SecurityKeyProvider](<https://man.archlinux.org/man/sshd_config.5#SecurityKeyProvider>) 配置项或为 `ssh-keygen` 和 `ssh-add` 配置 `SSH_SK_PROVIDER` 环境变量来实现。

连接兼容的 FIDO 密钥后，使用以下命令生成密钥对： 
    
    $ ssh-keygen -t ed25519-sk
    
这一步通常需要输入 PIN 码并/或触摸令牌进行确认。除非在生成时使用了 `-O no-touch-required` 命令行选项或服务器指定了 [sshd(8) § no-touch-required](<https://man.archlinux.org/man/sshd.8#no-touch-required>) `authorized_keys` 选项，否则连接服务器时通常需要触摸令牌进行确认。 

要生成不需要触摸确认的密钥，需在生成密钥对时使用 `no-touch-required` 选项，例如： 
    
    $ ssh-keygen -O no-touch-required -t ed25519-sk
    
**注意：** 并不是所有实体令牌都支持该选项。如果你使用的是 YubiKey，需要 5.2.3 固件版本才能使用 ed25519-sk 类型密钥。[[7]](<https://www.yubico.com/blog/whats-new-in-yubikey-firmware-5-2-3/>)

另外，`sshd` 默认会拒绝 `no-touch-required` 密钥。为使用通过该选项生成的密钥，需在 `authorized_keys` 文件内对每个密钥单独进行启用： 
    
    no-touch-required sk-ssh-ed25519@openssh.com AAAAInN... user@example.com
    
或是在 `/etc/ssh/sshd_config` 中对整个系统进行启用： 
    
    PubkeyAuthOptions none
    
**提示：**[GitHub](<https://github.com/orgs/community/discussions/10593>) 和 [GitLab](<https://gitlab.com/gitlab-org/gitlab/-/issues/367682>) 不支持 `no-touch-required`。

基于 ECDSA 的密钥对可通过 `ecdsa-sk` 密钥类型生成，但同样会有 [#ECDSA](<#ECDSA>) 一节提到的问题： 
    
    $ ssh-keygen -t ecdsa-sk
    
###  选择密钥存储位置以及密码短语

运行 `ssh-keygen` 时，它会询问您希望的私钥文件名称及位置。默认情况下，密钥保存到 `~/.ssh` 目录下，并根据所使用的加密类型命名。为使下文中的示例代码正确工作，建议您接受默认的名称和位置。 

当系统向您询问密码短语时，如果您在乎私钥的安全性，请选择难以猜到的密码。更长、更随机的密码一般会更强，当私钥落入贼人之手时更不容易被破解掉。 

在没有密码短语的情况下生成私钥也是可能的。虽然也许很方便，但您需要明白随之而来的风险。在没有密码短语的情况下，您的私钥会以未加密形式存储在硬盘上。任何能接触到您私钥文件的人之后都能够在您使用基于密钥认证连接的任何 SSH 服务器面前冒用您的身份。更进一步，没有密码短语，您也必须信任 root 用户，因为他可以绕过文件权限并能够随时访问您未加密的私钥文件。 

**注意：** 从前，私钥密码都是以一种不安全的方式编码的：仅一遍 MD5 散列。OpenSSH 6.5 及之后版本支持一种新的、更安全的格式来编码您的私钥。从 [OpenSSH 7.8 版本](<https://www.openssh.com/txt/release-7.8>)开始默认使用该格式。Ed25519 密钥一直采用新的编码格式。只需按下节所述更改密钥的密码短语即可升级到新格式。

####  不修改密钥对的情况下修改密码短语

如果不希望使用原本选择的 SSH 密钥密码短语或者必须更换，可以使用 `ssh-keygen` 命令来修改密码短语，而无需改动实际密钥。此法也可用于将密码编码格式改为新标准。 
    
    $ ssh-keygen -f ~/.ssh/id_rsa -p
    
####  管理多组密钥对

如果你有多个 SSH 身份，可以在配置文件中通过 `Host` 和 `IdentityFile` 为不同的主机和远程用户使用不同的密钥： 
    
    ~/.ssh/config
    
    Host SERVER1
       IdentitiesOnly yes
       IdentityFile ~/.ssh/id_rsa_IDENTITY1
    
    Host SERVER2 SERVER3
       IdentitiesOnly yes
       IdentityFile ~/.ssh/id_ed25519_IDENTITY2

对于这些选项的完整描述见 [ssh_config(5)](<https://man.archlinux.org/man/ssh_config.5>)。 

####  在硬件令牌上存储 SSH 密钥

SSH 密钥也可以存储在智能卡或 USB 令牌等安全令牌上。这样做的好处是私钥安全地存储在令牌上，而不是存储在磁盘中。当使用安全令牌时，敏感的私钥也从来不会存在于 PC 的内存当中；密码学操作在令牌自身上进行。密码学令牌还有一点好处是，它不与单台电脑绑定；可以将其从一台电脑上轻松取下，四处携带之后在其他电脑上使用。 

硬件令牌的例子可参考： 

  * [#FIDO/U2F](<#FIDO/U2F>)
  * [YubiKey#SSH notes](<../zh-cn/YubiKey.html#SSH_notes> "YubiKey") 用于 FIDO/U2F keys 的原生 OpenSSH 支持
  * [YubiKey#SSH keys](<../zh-cn/YubiKey.html#SSH_keys> "YubiKey")
  * [可信平台模块#SSH](<../zh-cn/%E5%8F%AF%E4%BF%A1%E5%B9%B3%E5%8F%B0%E6%A8%A1%E5%9D%97.html#SSH> "可信平台模块")

##  将公钥复制到远程服务器上

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 在[强制公钥认证](<../zh-cn/OpenSSH.html#%E5%BC%BA%E5%88%B6%E5%85%AC%E9%92%A5%E9%AA%8C%E8%AF%81> "OpenSSH")的情况下如何实现？ (在 [Talk:SSH 密钥](<../zh-cn/Talk:SSH_%E5%AF%86%E9%92%A5.html>) 中讨论)

创建好密钥对之后，您需要将公钥上传到远程服务器上，以便用于 SSH 密钥认证登录。公钥和私钥的文件名相同，只不过公钥文件带有扩展名 `.pub` 而私钥文件名则没有。千万不要将私钥上传，私钥应该保存在本地。 

###  简易方式

如果您的公钥文件为 `~/.ssh/id_rsa.pub`，只需要输入命令： 
    
    $ ssh-copy-id remote-server.org
    
如果您的远程服务器用户名与本地的不同，您需要在远程主机名前以 `@` 隔开指定用户名： 
    
    $ ssh-copy-id username@remote-server.org
    
如果您的公钥文件名不是默认的 `~/.ssh/id_rsa.pub`，会出现报错 `/usr/bin/ssh-copy-id: ERROR: No identities found`。这种情况下，您需要显式提供公钥的位置： 
    
    $ ssh-copy-id -i ~/.ssh/id_ed25519.pub username@remote-server.org
    
如果远程服务器监听端口不是默认的 22，请在主机参数中指明： 
    
    $ ssh-copy-id -i ~/.ssh/id_ed25519.pub -p 221 username@remote-server.org
    
###  手动方式

对于 OpenSSH，默认需要将公钥添加到 `~/.ssh/authorized_keys`。先从复制公钥到远程服务器开始。 
    
    $ scp ~/.ssh/id_ecdsa.pub username@remote-server.org:
    
以上示例通过 `scp` 将公钥（`id_ecdsa.pub`）复制到您在远程服务器上的主目录。别忘了加上服务器地址末尾的 `:`。并请注意，您的公钥名称可能与此例所示不同。 

在远程服务器上，如果还没有 `~/.ssh` 目录，您需要创建一个；然后将您的公钥追加到 `authorized_keys` 文件内。 
    
    $ ssh username@remote-server.org
    username@remote-server.org's password:
    $ install -dm700 ~/.ssh
    $ cat ~/id_ecdsa.pub >> ~/.ssh/authorized_keys
    $ rm ~/id_ecdsa.pub
    $ chmod 600 ~/.ssh/authorized_keys
    
上面最后两个命令将公钥文件从服务器上删除，并设置 `authorized_keys` 文件的权限，这样只有作为文件拥有者的您能够读取及写入。 

##  SSH 代理

如果您的私钥使用密码短语来加密了的话，每一次试图连接到使用公钥认证的 SSH 服务器的时候，您都必须输入密码短语。每次唤起 `ssh` 或 `scp` 时都需要密码短语来解密您的私钥以便认证能够继续。 

而 SSH 代理程序能够将您的已解密的私钥缓存起来，并代表您将其提供给 SSH 客户端。这样子，您就只需要将私钥加入 SSH 代理缓存的时候输入一次密码短语就可以了。在经常使用 SSH 连接时，将会提供不少便利。 

SSH 代理一般会设置成在登录会话的时候自动启动，并在整个会话中保持运行。有多种代理、前端及配置都能够达成这一效果。本节概述了多种不同的解决方案，能够适应以满足您的特定需求。 

### ssh-agent

`ssh-agent` 是 OpenSSH 自带的默认代理。它可以直接使用，或者作为下文所述的几种前端解决方案的后端。`ssh-agent` 运行时会自动 fork 到后台，然后打印出其所需的环境变量，例如： 
    
    $ ssh-agent
    
    SSH_AUTH_SOCK=/tmp/ssh-vEGjCM2147/agent.2147; export SSH_AUTH_SOCK;
    SSH_AGENT_PID=2148; export SSH_AGENT_PID;
    echo Agent pid 2148;

要使用这些环境变量，请使用 `eval` 命令来运行它。如果使用的是 `fish` shell，需要转而使用 `ssh-agent -c`。 
    
    $ eval $(ssh-agent)
    
    Agent pid 2157
    
`ssh-agent` 运行起来之后，您还需要将您的私钥加入它的缓存。 
    
    $ ssh-add ~/.ssh/id_ed25519
    
    Enter passphrase for /home/user/.ssh/id_ed25519:
    Identity added: /home/user/.ssh/id_ed25519 (/home/user/.ssh/id_ed25519)
    
如果您的私钥已加密，`ssh-add` 会提示您输入密码短语。一旦您的私钥被成功添加到代理，您不需要再输入密码短语就能够建立 SSH 连接了。 

**提示：** 要让包括 `git` 在内的所有 `ssh` 客户端在第一次使用时就把密钥存储在代理中，请将配置 `AddKeysToAgent yes` 添加到 `~/.ssh/config`。其他可能的值有 `confirm`、`ask` 和 `no`（默认）。

为了自动启动代理并确保同一时间只有一个 `ssh-agent` 进程在运行，添加以下内容到您的 `~/.bashrc`： 
    
    if ! pgrep -u "$USER" ssh-agent > /dev/null; then
        ssh-agent -t 1h > "$XDG_RUNTIME_DIR/ssh-agent.env"
    fi
    if [[ ! -f "$SSH_AUTH_SOCK" ]]; then
        source "$XDG_RUNTIME_DIR/ssh-agent.env" >/dev/null
    fi
    
如果还没有 `ssh-agent` 进程在运行的话，该脚本会自动启动一个，并保存其输出。如果已经有一个在运行了，就会读取缓存的 `ssh-agent` 输出并执行之，从而设置必要的环境变量。解密密钥的存活时间设置为1小时。 

本节后面会介绍几种 `ssh-agent` 的前端及其它代理，也能够避免这一问题。 

####  用 systemd user 启动 ssh-agent

如果想要在登录时运行 SSH agent 而不论 X 是否在运行的话，从 9.4p1-3 版本开始 [openssh](<https://archlinux.org/packages/?name=openssh>)包 提供了 `ssh-agent.service`，可以作为[用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")。 

然后将[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html#%E6%8C%89%E7%94%A8%E6%88%B7> "环境变量") `SSH_AUTH_SOCK` 设为 `$XDG_RUNTIME_DIR/ssh-agent.socket`。 

**注意：** 如果您使用 GNOME，该环境变量默认会被覆盖。见 [GNOME/Keyring#禁用钥匙环的守护进程组件](<../zh-cn/GNOME/Keyring.html#%E7%A6%81%E7%94%A8%E9%92%A5%E5%8C%99%E7%8E%AF%E7%9A%84%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B%E7%BB%84%E4%BB%B6> "GNOME/Keyring")。

####  转发 ssh-agent

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** This is not specific to ssh-agent, e.g. gpg-agent uses the same environment variable: [GnuPG#Forwarding gpg-agent and ssh-agent to remote](<../zh-cn/GnuPG.html#Forwarding_gpg-agent_and_ssh-agent_to_remote> "GnuPG")（在[Talk:SSH 密钥](<../zh-cn/Talk:SSH_%E5%AF%86%E9%92%A5.html>)讨论）

When [forwarding](<../zh-cn/OpenSSH.html#Agent_forwarding> "OpenSSH") a local `ssh-agent` to remote (e.g., through command-line argument `ssh -A remote` or through `ForwardAgent yes` in the configuration file), it is important for the remote machine not to overwrite the environment variable `SSH_AUTH_SOCK`. So if the remote machine uses a [systemd unit](<#Start_ssh-agent_with_systemd_user>) shown previously to start the agent, `SSH_AUTH_SOCK` must not be set in the environment when a user is logged in through SSH. Otherwise, the forwarding may fail, and you may see errors (for example: `The agent has no identities`) when checking the existing keys with `ssh-add -l` on the remote machine. 

For example, if using bash, the `.bashrc` could be something like: 
    
    ~/.bashrc
    
    ...
    if [[ -z "${SSH_CONNECTION}" ]]; then
        export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
    fi
    ...

In this way, `SSH_AUTH_SOCK` is only set when the current session is **not** a SSH login. And when this is a SSH session, `SSH_AUTH_SOCK` on the remote machine is then set by the local machine to make the forwarding work. 

####  作为包装程序运行 ssh-agent

[加州大学伯克利分校实验室的这份 ssh-agent 教程](<https://upc.lbl.gov/docs/user/sshagent.shtml>)还介绍了一种随每个 X 会话启动 `ssh-agent` 的方法。基本用法是，如果您使用命令 `startx` 正常启动 X，您可以改成像这样在前面加上 `ssh-agent`： 
    
    $ ssh-agent startx
    
您也可以在 `.bash_aliases` 或等同文件中设置别名，就不用再费心了： 
    
    alias startx='ssh-agent startx'
    
这样做可以避免多个会话中存在多余的 `ssh-agent` 进程。整个 X 会话中只会有一个 `ssh-agent` 在运行。 

**注意：**`ssh-askpass` 需要 `DISPLAY` 或 `WAYLAND_DISPLAY` 环境变量才能正常工作，所以你可能会需要在 `~/.xinitrc` 中运行 `ssh-agent` 以配置 `DISPLAY` 选项，而不是使用 `ssh-agent startx`（如将 `exec ssh-agent dbus-launch i3` 添加到 `~/.xinitrc`）。或者也可以将 `eval $(ssh-agent)` 添加到 `~/.xinitrc` 以使用 `ssh-agent` 作为包装程序运行。

见[下文有关协同使用 x11-ssh-askpass 与 ssh-add 的说明](<#Calling_x11-ssh-askpass_with_ssh-add>)了解如何立即将密钥添加到 agent。 

### OpenPGP card ssh-agent

This ssh-agent specializes on [OpenPGP](</wzh/index.php?title=OpenPGP&action=edit&redlink=1> "OpenPGP（页面不存在）") card integration. It uses private keys that are stored in [OpenPGP](</wzh/index.php?title=OpenPGP&action=edit&redlink=1> "OpenPGP（页面不存在）") card authentication slots. 

**注意：** When also using [GnuPG](<../zh-cn/GnuPG.html> "GnuPG") while running this agent, it is required to [use it with pcscd](<../zh-cn/GnuPG.html#GnuPG_with_pcscd_\(PCSC_Lite\)> "GnuPG") and configure [shared access with pcscd](<../zh-cn/GnuPG.html#Shared_access_with_pcscd> "GnuPG").

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [openpgp-card-ssh-agent](<https://archlinux.org/packages/?name=openpgp-card-ssh-agent>)包 and [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") and [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") the `openpgp-card-ssh-agent.socket` user unit. 

Afterwards add the relevant environment variable for this agent: 
    
    export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/openpgp-card/ssh-agent.sock"
    
#### User PIN handling

The user PIN for the [OpenPGP](</wzh/index.php?title=OpenPGP&action=edit&redlink=1> "OpenPGP（页面不存在）") card is persisted via an [org.freedesktop.secrets](<https://archlinux.org/packages/?q=org.freedesktop.secrets>) provider (such as [GNOME Keyring](<../zh-cn/GNOME_Keyring.html> "GNOME Keyring"), [KeePassXC](</wzh/index.php?title=KeePass&action=edit&redlink=1> "KeePass（页面不存在）") or [KDE Wallet](<../zh-cn/KDE_Wallet.html> "KDE Wallet")) by default. The PIN storage backend is [configurable and extendable](<https://codeberg.org/openpgp-card/state>). 

The user PIN needs to be persisted only once for each [OpenPGP](</wzh/index.php?title=OpenPGP&action=edit&redlink=1> "OpenPGP（页面不存在）") card. Prior to the first SSH connection with this agent, list the available SSH public keys and add their respective card identifiers: 
    
    $ ssh-add -L
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJUz6VnFprMe33G88Pq8NLw3wnIKOsBg0CDrwFeUVrU6 **FFFE:01234567**
    $ ssh-add -s **FFFE:01234567**
    Enter passphrase for PKCS#11:
    
**注意：** The prompt mentions _PKCS#11_ as it is a hardcoded message in [ssh-add(1)](<https://man.archlinux.org/man/ssh-add.1>). However, in this context the OpenPGP card user PIN must be entered.

### GnuPG Agent

[gpg-agent](<../zh-cn/GnuPG.html#gpg-agent> "Gpg-agent") 模拟了 OpenSSH 的代理协议，必要配置请参考 [GnuPG#SSH 代理](<../zh-cn/GnuPG.html#SSH_%E4%BB%A3%E7%90%86> "GnuPG")。 

### Keychain

[Keychain](<https://www.funtoo.org/Keychain>) 是一个用来方便管理 SSH 密钥对的程序，它能尽最大努力去减少对用户的打扰。实际上，它就是一个 shell 脚本，驱动 _ssh-agent_ 或者 _gpg-add_ 来工作。一个值得注意的特性是，Keychain 在多个会话中重复使用同一个 _ssh-agent_ 进程。这意味着您只需要在机器启动时输入一次密码短语即可。 

####  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [keychain](<https://archlinux.org/packages/?name=keychain>)包 软件包。 

####  配置

**警告：** 直至 2015-09-26 为止，`-Q, --quick` 选项存在预期之外的副作用，导致 _keychain_ 在重新登录时切换到新产生的 _ssh-agent_ （至少在使用 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的系统上如此），使您不得不重新添加所有先前注册的密钥。

将类似以下的行加入到您 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell") 的配置文件中， _例如_ 若您使用[Bash](<../zh-cn/Bash.html> "Bash")： 
    
    ~/.bashrc
    
    eval $(keychain --eval --quiet id_ed25519 id_rsa ~/.keys/my_custom_key)
    
**注意：** 之所以使用 `~/.bashrc` 而非上游建议的 `~/.bash_profile`，是因为在 Arch 上登录与非登录 shell 都会使用它，因此同样适用于文字与图形环境。关于二者之间差异的更多信息见[Bash#调用](<../zh-cn/Bash.html#%E8%B0%83%E7%94%A8> "Bash")。

上例当中， 

  * `--eval` 开关可以输出供 `eval` 命令执行的行；这样可以设置必要的环境变量，让 SSH 客户端能够找到您的 agent。
  * `--quiet` 会把输出限制为只包含警告、错误及用户提示。

如例子所示，可在命令行中指定多个密钥。Keychain 默认会在 `~/.ssh/` 目录中寻找密钥对，但对于位于非标准位置的密钥可以使用绝对路径。也可使用 `--confhost` 选项告知 keychain 在 `~/.ssh/config` 中寻找为特定主机定义的 `IdentityFile` 设置，并使用这些路径来定位密钥。 

关于如何为其他 shell 设置 _keychain_ 的详情请参考 `keychain --help` 或 [keychain(1)](<https://man.archlinux.org/man/keychain.1>)。 

要测试 Keychain，只需打开一个终端模拟器，或注销当前会话再重新登录。它应该会使用 `$SSH_ASKPASS` 中设置的程序或在终端上提示您输入指定私钥的密码短语（如果有）。 

因为 Keychain 重新使用之前的登录中的 _ssh-agent_ 进程，所以您再次登录或打开新终端时应该就无需输入密码短语了。每当您重启机器时，您才会被要求再次输入密码短语。 

####  提示

  * _keychain_ 需要公钥文件存放在相应私钥的同一目录下，并带有 `.pub` 扩展名。如私钥为符号链接，公钥需要与符号链接一起存放或与符号链接目标在同一目录下（该功能需要系统上有 `readlink` 命令）。

  * 要禁用图形提示，以始终在终端中输入密码短语，请使用 `--nogui` 选项。举例来说，这样可以从密码管理器中复制粘贴长密码。

  * 如果您想要等到需要时再提示解锁密钥，而不是一开始就提示，请使用 `--noask` 选项。

**注意：** Keychain 能够以同样的方式管理 [GPG](<../zh-cn/GnuPG.html> "GPG") 密钥。它默认只会尝试启动 _ssh-agent_ ，但使用 `--agents` 选项可以改变这一行为， _例如_ `--agents ssh,gpg`。详细信息请参考 [keychain(1)](<https://man.archlinux.org/man/keychain.1>)。

**注意：**

  * Keychain 能够以同样的方式管理 [GPG](<../zh-cn/GnuPG.html> "GPG") 密钥。它默认只会尝试启动 _ssh-agent_ ，但使用 `--agents` 选项可以改变这一行为， _例如_ `--agents ssh,gpg`。详细信息请参考 [keychain(1)](<https://man.archlinux.org/man/keychain.1>)。
  * 根据 [keychain issue 148](<https://github.com/funtoo/keychain/issues/148>)，在使用 Wayland 时可能需要添加 `--inherit any-once` 参数。

### x11-ssh-askpass

The [x11-ssh-askpass](<https://archlinux.org/packages/?name=x11-ssh-askpass>)包 package provides a graphical dialog for entering your passhrase when running an X session. _x11-ssh-askpass_ depends only on the [libx11](<https://archlinux.org/packages/?name=libx11>)包 and [libxt](<https://archlinux.org/packages/?name=libxt>)包 libraries, and the appearance of _x11-ssh-askpass_ is customizable. While it can be invoked by the _ssh-add_ program, which will then load your decrypted keys into [ssh-agent](<#ssh-agent>), the following instructions will, instead, configure _x11-ssh-askpass_ to be invoked by the aforementioned [Keychain](<#Keychain>) script. 

Install the [keychain](<https://archlinux.org/packages/?name=keychain>)包 and [x11-ssh-askpass](<https://archlinux.org/packages/?name=x11-ssh-askpass>)包 packages. 

Edit your `~/.xinitrc` file to include the following lines, replacing the name and location of your private key if necessary. Be sure to place these commands **before** the line which invokes your window manager. 
    
    ~/.xinitrc
    
    keychain ~/.ssh/id_ecdsa
    [ -f ~/.keychain/$HOSTNAME-sh ] && . ~/.keychain/$HOSTNAME-sh 2>/dev/null
    [ -f ~/.keychain/$HOSTNAME-sh-gpg ] && . ~/.keychain/$HOSTNAME-sh-gpg 2>/dev/null
    ...
    exec openbox-session

In the above example, the first line invokes _keychain_ and passes the name and location of your private key. If this is not the first time _keychain_ was invoked, the following two lines load the contents of `$HOSTNAME-sh` and `$HOSTNAME-sh-gpg`, if they exist. These files store the environment variables of the previous instance of _keychain_. 

#### Calling x11-ssh-askpass with ssh-add

The _ssh-add_ manual page specifies that, in addition to needing the `DISPLAY` or `WAYLAND_DISPLAY` variable defined, you also need `SSH_ASKPASS` set to the name of your askpass program (in this case _x11-ssh-askpass_). It bears keeping in mind that the default Arch Linux installation places the _x11-ssh-askpass_ binary in `/usr/lib/ssh/`, which will not be in most people's `PATH`. This is a little annoying, not only when declaring the `SSH_ASKPASS` variable, but also when theming. You have to specify the full path everywhere. Both inconveniences can be solved simultaneously by symlinking: 
    
    $ ln -sv /usr/lib/ssh/x11-ssh-askpass ~/bin/ssh-askpass
    
This is assuming that `~/bin` is in your `PATH`. So now in your `.xinitrc`, before calling your window manager, one just needs to export the `SSH_ASKPASS` environment variable: 
    
    $ export SSH_ASKPASS=ssh-askpass
    
and your [X resources](<../zh-cn/X_resources.html> "X resources") will contain something like: 
    
    ssh-askpass*background: #000000
    
Doing it this way works well with [the above method on using _ssh-agent_ as a wrapper program](<#ssh-agent_as_a_wrapper_program>). You start X with `ssh-agent startx` and then add _ssh-add_ to your window manager's list of start-up programs. 

#### Theming

The appearance of the _x11-ssh-askpass_ dialog can be customized by setting its associated [X resources](<../zh-cn/X_resources.html> "X resources"). Some examples are the .ad files at <https://github.com/sigmavirus24/x11-ssh-askpass>. See [x11-ssh-askpass(1)](<https://man.archlinux.org/man/x11-ssh-askpass.1>) for full details. 

#### Alternative passphrase dialogs

There are other passphrase dialog programs which can be used instead of _x11-ssh-askpass_. The following list provides some alternative solutions. 

  * [seahorse](<https://archlinux.org/packages/?name=seahorse>)包 (provides `/usr/lib/seahorse/ssh-askpass`) uses the [GTK](<../zh-cn/GTK.html> "GTK") library. .
  * [gnome-ssh-askpass3](<https://aur.archlinux.org/packages/gnome-ssh-askpass3/>)AUR uses the [GTK](<../zh-cn/GTK.html> "GTK") library.
  * [ksshaskpass](<https://archlinux.org/packages/?name=ksshaskpass>)包 uses the [KDE Wallet](<../zh-cn/KDE_Wallet.html> "KDE Wallet").
  * [openssh-askpass](<https://aur.archlinux.org/packages/openssh-askpass/>)AUR uses the [Qt5](<../zh-cn/Qt.html> "Qt") library.
  * [lxqt-openssh-askpass](<https://archlinux.org/packages/?name=lxqt-openssh-askpass>)包

### pam_ssh

[pam_ssh](<http://pam-ssh.sourceforge.net/>) 项目为 SSH 私钥提供了一个[可插拔认证模块](<https://zh.wikipedia.org/wiki/%E5%8F%AF%E6%8F%92%E6%8B%94%E8%AE%A4%E8%AF%81%E6%A8%A1%E5%9D%97> "zhwp:可插拔认证模块")（PAM），该模块可以为 SSH 连接提供类似单点登录验证的特性。在认证完成后，pam_ssh 模块会让 ssh-agent 在整个会话期间缓存您已解密的私钥。 

要在 tty 模式下使用单点登录特性，需要安装非官方的 [pam_ssh](<https://aur.archlinux.org/packages/pam_ssh/>)AUR 包。 

**注意：** pam_ssh 2.0 要求所有用于认证的私钥文件必须保存在 `~/.ssh/login-keys.d/` 下。

可以为您的私钥文件创建一个软链接，并放到 `~/.ssh/login-keys.d/`。将以下案例中的 `id_rsa` 替换为你的私钥的名称： 
    
    $ mkdir ~/.ssh/login-keys.d/
    $ cd ~/.ssh/login-keys.d/
    $ ln -s ../id_rsa
    
编辑 `/etc/pam.d/login`，将下面例子中高亮加粗的那几行加进去。请注意配置内容的顺序会影响到登录行为，应当按照例子中的来。 

**警告：** PAM 配置错误会导致系统中的所有用户被锁定。因此，在进行任何更改前，你需要大致了解 PAM 配置的工作方式，并确保具有备用的 PAM 配置文件访问手段（如 Arch Live CD），以确保被锁定后仍能撤回更改。可以参阅 IBM developerWorks 的 [这篇文章](<https://developer.ibm.com/tutorials/l-pam/>) 详细了解一下 PAM 的配置细节。
    
    /etc/pam.d/login
    
    #%PAM-1.0
    
    auth       required     pam_securetty.so
    auth       requisite    pam_nologin.so
    auth       include      system-local-login
    **auth       optional     pam_ssh.so        try_first_pass**
    account    include      system-local-login
    session    include      system-local-login
    **session    optional     pam_ssh.so**

在上面的例子中，登录认证在起始阶段正常进行，并要求用户输入登录密码。附加到认证栈末尾的额外 `auth` 认证规则会让 pam_ssh 尝试解密 `~/.ssh/login-keys.d` 目录下的所有私钥。`try_first_pass` 选项会被传递给 pam_ssh 模块，要求它尝试使用用户之前输入的密码解密 SSH 私钥。如果用户密码与私钥密码一致，用户就无需再次输入相同的密码。如果两者不同，pam_ssh 模块会在用户输入登录密码后要求输入私钥密码。`optional` 选项可以保证在没有私钥时用户也能正常登录系统。这样，没有 SSH 私钥的用户对 pam_ssh 是无感的。 

如果你使用 X11 显示管理器（如 [SLiM](<../zh-cn/SLiM.html> "SLiM") 或 [XDM](<../zh-cn/XDM.html> "XDM")）等其它方式进行登录，必须仿照如上配置编辑 PAM 配置文件。提供 PAM 支持的软件包通常会将默认配置文件放置在 `/etc/pam.d/` 目录下。 

Further details on how to use pam_ssh and a list of its options can be found in the [pam_ssh(8)](<https://linux.die.net/man/8/pam_ssh>) man page. 

####  使用不同密码解锁 SSH 密钥

If you want to unlock the SSH keys or not depending on whether you use your key's passphrase or the (different!) login password, you can modify `/etc/pam.d/system-auth` to 
    
    /etc/pam.d/system-auth
    
    #%PAM-1.0
    
    **auth      [success=1 new_authtok_reqd=1 ignore=ignore default=ignore]  pam_unix.so     try_first_pass nullok**
    **auth      required  pam_ssh.so      use_first_pass**
    auth      optional  pam_permit.so
    auth      required  pam_env.so
    
    account   required  pam_unix.so
    account   optional  pam_permit.so
    account   required  pam_time.so
    
    password  required  pam_unix.so     try_first_pass nullok sha512 shadow
    password  optional  pam_permit.so
    
    session   required  pam_limits.so
    session   required  pam_unix.so
    session   optional  pam_permit.so
    **session   optional  pam_ssh.so**

For an explanation, see [[8]](<https://unix.stackexchange.com/a/239486>). 

####  pam_ssh 已知问题

pam_ssh 项目并不活跃，其提供的文档也比较少。你需要注意该软件未提及的一些使用限制，比如： 

  * 2.0 版本前的 pam_ssh 不支持 ECDSA（椭圆曲线）SSH 密钥，需要使用旧版本的必须使用 RSA 密钥。

  * pam_ssh 调用的 `ssh-agent` 进程仅限于当前用户登录，无法在多次登录间持久化。如果你在登录期间保留了一个 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 会话，会发现重新连接 screen 会话后无法与 ssh-agent 进行通信。这是因为 GNU Screen 环境和其子进程仍在引用调用 screen 时存在的 ssh-agent，但其已随上次登出被关闭。上文提到的 [Keychain](<#Keychain>) 前端可以在多次登录间保留 ssh-agent 进程，从而避免该问题。

### pam_exec-ssh

As an alternative to [pam_ssh](<#pam_ssh>) you can use [pam_exec-ssh-git](<https://aur.archlinux.org/packages/pam_exec-ssh-git/>)AUR. It is a shell script that uses pam_exec. Help for configuration can be found [upstream](<https://github.com/x70b1/pam_exec-ssh>). 

### GNOME Keyring

[GNOME Keyring](<../zh-cn/GNOME_Keyring.html> "GNOME Keyring") 可用作 ssh-agent 的封装，并提供图形界面和/或密钥自动解锁功能。详情请参考 [GNOME Keyring#SSH密钥](<../zh-cn/GNOME_Keyring.html#SSH%E5%AF%86%E9%92%A5> "GNOME Keyring")。 

###  使用 Kwallet 存储 SSH 密钥

For instructions on how to use kwallet to store your SSH keys, see [KDE Wallet#Using the KDE Wallet to store ssh key passphrases](<../zh-cn/KDE_Wallet.html#Using_the_KDE_Wallet_to_store_ssh_key_passphrases> "KDE Wallet"). 

###  KeePass2 搭配 KeeAgent 插件

[KeeAgent](<https://lechnology.com/software/keeagent/>) is a plugin for [KeePass](</wzh/index.php?title=KeePass&action=edit&redlink=1> "KeePass（页面不存在）") that allows SSH keys stored in a KeePass database to be used for SSH authentication by other programs. 

  * Supports both PuTTY and OpenSSH private key formats.
  * Works with native SSH agent on Linux/Mac and with PuTTY on Windows.

See [KeePass#Plugin installation in KeePass](</wzh/index.php?title=KeePass&action=edit&redlink=1> "KeePass（页面不存在）") or [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [keepass-plugin-keeagent](<https://archlinux.org/packages/?name=keepass-plugin-keeagent>)包 package. 

This agent can be used directly, by matching KeeAgent socket: `KeePass -> Tools -> Options -> KeeAgent -> Agent mode socket file -> %XDG_RUNTIME_DIR%/keeagent.socket`\- and environment variable: `export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR"'/keeagent.socket'`. 

### KeePassXC

The KeePassXC fork of KeePass [can act as a client for an existing SSH agent](<https://keepassxc.org/docs/#faq-ssh-agent-how>). SSH keys stored in its database can be automatically (or manually) added to the agent. It is also compatible with KeeAgent's database format. 

##  疑难排解

###  密钥被服务器忽略

如果您的 SSH 服务器忽略了您的 SSH 密钥对，您需要检查一下相关文件的权限是否正确。 

    本地机器上：
    
    $ chmod 700 ~/.ssh
    $ chmod 600 ~/.ssh/_key_
    
    服务器上：
    
    $ chmod 700 ~/.ssh
    $ chmod 600 ~/.ssh/authorized_keys
    
如果这样还不能解决您的问题，您可以试试将 `/etc/ssh/sshd_config` 中的 `StrictModes` 设为 `no`。如果使用 `StrictModes off` 就能够顺利认证的话，说明相关文件的权限还没有改对。 

  * 确保 `~/.ssh/authorized_keys` 中的密钥正确并只有一行。
  * 确保远程设备支持使用的密钥类型：有些服务器不支持 ECDSA 密钥，可以试试 RSA 密钥，具体请参考 [#生成密钥对](<#%E7%94%9F%E6%88%90%E5%AF%86%E9%92%A5%E5%AF%B9>)。
  * 你可能会想在连接时启用调试模式并监控输出：

    # /usr/bin/sshd -d
    
  * 如果你的密钥使用其它名字（如 `id_rsa_server`），需要使用 `-i` 选项进行连接：

    $ ssh -i id_rsa_server user@server
    
###  代理拒绝操作

If your private key requires a password (or, for instance, you have a hardware key with a PIN) but ssh-agent is not provided with one, `ssh` will fail: 
    
    sign_and_send_pubkey: signing failed for ECDSA-SK _user_ @_host_ from agent: agent refused operation
    
One potential cause for this is ssh-agent being unable to prompt for a password. Ensure that ssh-agent has access to either a display server (via the `DISPLAY` environment variable) or a TTY. 

Another cause, if using a hardware authenticator, could be the key malfunctioning or being unplugged. 

There is currently an open [bug](<https://bugzilla.mindrot.org/show_bug.cgi?id=3572>) that triggers with the "agent refused operation" error when using authenticator keys like ED25519-sk and ECDSA-SK that were created with the option `-O verify-required`. To avoid this issue, use the `-o IdentityAgent=none -o IdentitiesOnly=yes` option for the `ssh` command or add it to your `ssh_config` file for the relevant hosts: 
    
    Host myserver.tld
        IdentityAgent none
        IdentitiesOnly yes
    
##  参考

  * OpenSSH 密钥管理：[第一部分](<https://www.funtoo.org/OpenSSH_Key_Management,_Part_1>)，[第二部分](<https://www.funtoo.org/OpenSSH_Key_Management,_Part_2>)，[第三部分](<https://www.funtoo.org/OpenSSH_Key_Management,_Part_3>)
  * [Secure Secure Shell](<https://stribika.github.io/2015/01/04/secure-secure-shell.html>)
