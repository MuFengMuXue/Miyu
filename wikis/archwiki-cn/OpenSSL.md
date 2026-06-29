相关文章

  * [Transport Layer Security](</wzh/index.php?title=Transport_Layer_Security&action=edit&redlink=1> "Transport Layer Security（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [OpenSSL](<https://wiki.archlinux.org/title/OpenSSL> "arch:OpenSSL")，最近一次同步于 2023-06-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/OpenSSL?diff=0&oldid=780045>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/OpenSSL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请完成翻译。大部分内容尚未翻译。（在 [Talk:OpenSSL#](<../zh-cn/Talk:OpenSSL.html>) 中讨论）

[OpenSSL](<https://www.openssl.org>)是 SSL 和 [TLS](</wzh/index.php?title=TLS&action=edit&redlink=1> "TLS（页面不存在）") 协议的开源实现，旨在尽可能灵活。OpenSSL 支持各种平台，包括 BSD、Linux、OpenVMS、Solaris 和 Windows。 

**警告：** 2015 年 5 月发布的对 OpenSSL 协议使用情况的合作研究显示 SSL 连接存在重大风险 “Logjam”。可在 <https://weakdh.org/> 查看结果，在 <https://weakdh.org/sysadmin.html> 查看建议的服务端配置。

##  安装

Arch Linux 默认安装 [openssl](<https://archlinux.org/packages/?name=openssl>)包（作为 [coreutils](<https://archlinux.org/packages/?name=coreutils>)包 的依赖）。 

有许多 OpenSSL 库绑定可供开发者使用： 

  * [python-pyopenssl](<https://archlinux.org/packages/?name=python-pyopenssl>)包
  * [perl-net-ssleay](<https://archlinux.org/packages/?name=perl-net-ssleay>)包
  * [lua-sec](<https://archlinux.org/packages/?name=lua-sec>)包、[lua52-sec](<https://archlinux.org/packages/?name=lua52-sec>)包 和 [lua51-sec](<https://archlinux.org/packages/?name=lua51-sec>)包
  * [haskell-hsopenssl](<https://archlinux.org/packages/?name=haskell-hsopenssl>)包
  * [haskell-openssl-streams](<https://archlinux.org/packages/?name=haskell-openssl-streams>)包

##  配置

在 Arch Linux 中 `OPENSSLDIR` 为 `/etc/ssl`。 

OpenSSL 配置文件通常位于 `/etc/ssl/openssl.cnf`，乍一看可能很复杂。注意在赋值中可以展开变量，这与 Shell 脚本的工作方式很相似。配置文件格式的详细解释，请见 [config(5ssl)](<https://man.archlinux.org/man/config.5ssl>)。 

###  req 部分

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[#生成证书签名请求](<#%E7%94%9F%E6%88%90%E8%AF%81%E4%B9%A6%E7%AD%BE%E5%90%8D%E8%AF%B7%E6%B1%82>)。**

**附注：** 主题相同。（在 [[[en:Talk:OpenSSL#Plan](<https://wiki.archlinux.org/title/Talk:OpenSSL#Plan>)]] 中讨论）

与生成密钥、请求和自签名证书有关的设置。 

The req section is responsible for the DN prompts. A general misconception is the _Common Name_ (CN) prompt, which suggests that it should have the user's proper name as a value. End-user certificates need to have the **machine hostname** as CN, whereas CA should _not_ have a valid TLD, so that there is no chance that, between the possible combinations of certified end-users' CN and the CA certificate's, there is a match that could be misinterpreted by some software as meaning that the end-user certificate is self-signed. 某些 CA 证书甚至没有 CN，例如 [Equifax](<https://www.equifax.com>)： 
    
    $ openssl x509 -subject -noout < /etc/ssl/certs/Equifax_Secure_CA.pem
    
    subject= /C=US/O=Equifax/OU=Equifax Secure Certificate Authority

##  用法

请先阅读 [Transport Layer Security#Obtaining a certificate](</wzh/index.php?title=Transport_Layer_Security&action=edit&redlink=1> "Transport Layer Security（页面不存在）")。 

###  生成 Curve25519 私钥
    
    $ openssl genpkey -algorithm x25519 -out _文件名_
    
###  生成 ECDSA 私钥
    
    $ openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out _文件名_
    
###  生成 RSA 私钥

使用（根据 [openssl(1ssl)](<https://man.archlinux.org/man/openssl.1ssl>)，代替 _genrsa_ 的）[genpkey(1ssl)](<https://man.archlinux.org/man/genpkey.1ssl>)： 
    
    $ openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:_私钥大小_ -out _文件名_
    
如果需要加密密钥，使用 `-aes-256-cbc` 选项。 

###  生成证书签名请求

使用 [req(1ssl)](<https://man.archlinux.org/man/req.1ssl>)： 
    
    $ openssl req -new -sha256 -key _私钥_ -out _文件名_
    
###  显示证书签名请求

证书签名请求以编码形式存储。要以人类可读的形式查看请求： 
    
    $ openssl req -noout -text -in _文件名_
    
###  生成自签名证书

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** This produces a certificate for the (root) Certificate Authority, which you are acting as. Most web browsers do not seem to accept CA certificates, deeming it necessary to request another certificate and sign it with the CA cert and CA key. The "Generate a certificate issued by own CA" procedure in [this forum post](<https://bbs.archlinux.org/viewtopic.php?pid=1776753#p1776753>) is what seems to satisfy browsers. (在 [Talk:OpenSSL](<../zh-cn/Talk:OpenSSL.html>) 中讨论)
    
    $ openssl req -key _private_key_ -x509 -new -days _days_ -out _filename_
    
### Generate a self-signed certificate with private key in a single command

You can combine the above command in OpenSSL into a single command which might be convenient in some cases: 
    
    $ openssl req -x509 -newkey rsa:4096 -days _days_ -keyout _key_filename_ -out _cert_filename_
    
###  Generate Diffie–Hellman parameters

See [Diffie–Hellman key exchange](<https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange> "wikipedia:Diffie–Hellman key exchange") for more information. 

Current [best practice](<https://wiki.mozilla.org/Security/Server_Side_TLS> "mozillawiki:Security/Server Side TLS") is to use one of the standard DH groups from [RFC:7919](<https://tools.ietf.org/html/rfc7919> "rfc:7919"), eg. [ffdhe2048](<https://ssl-config.mozilla.org/ffdhe2048.txt>). 

Alternatively you can generate a random group of your own: 
    
    $ openssl dhparam -out _filename_ _2048_
    
**提示：** To speed up generating, especially when not on high-end hardware, add the `-dsaparam` option [[1]](<https://security.stackexchange.com/questions/95178/diffie-hellman-parameters-still-calculating-after-24-hours/95184#95184>).

###  显示证书信息
    
    $ openssl x509 -text -in _证书文件名_
    
###  显示证书指纹
    
    $ openssl x509 -noout -in _证书文件名_ -fingerprint _-digest_
    
`_-digest_` is optional and one of `-md5`, `-sha1`, `-sha256`, or `-sha512`. See "-digest" in [x509(1ssl) § Input, Output, and General Purpose Options](<https://man.archlinux.org/man/x509.1ssl#Input,_Output,_and_General_Purpose_Options>) for when the digest is unspecified. 

###  转换证书格式

Use `openssl x509` to convert certificates from binary (DER) format to PEM format (the text format with `BEGIN CERTIFICATE` headers)： 
    
    $ openssl x509 -inform DER < _myCA_.crt > _myCA_pem_.crt
    
### Use third-party providers

OpenSSL 3 introduced providers as a new concept for OpenSSL plugability. It is possible to use algorithms not included in OpenSSL without having to recompile it. For example, to test the [NIST Post-Quantum Cryptography](<https://csrc.nist.gov/projects/post-quantum-cryptography>) algorithms, you can install the [Open Quantum Safe](<https://openquantumsafe.org/>) provider [oqsprovider](<https://aur.archlinux.org/packages/oqsprovider/>)AUR. As an example, you can generate a quantum-safe self-signed certificate with private key using one of the variants of the [Dilithium](<https://pq-crystals.org/dilithium/index.shtml>) signature algorithm: 
    
    $ openssl req -provider oqsprovider -x509 -newkey dilithium3 -days _days_ -keyout _key_ -out _cert_
    
## Troubleshooting

###  "bad decrypt" while decrypting

OpenSSL 1.1.0 changed the default digest algorithm for the dgst and enc commands from MD5 to SHA256. [[2]](<https://www.openssl.org/news/changelog.html#x6>)

Therefore if a file has been encrypted using OpenSSL 1.0.2 or older, trying to decrypt it with an up to date version may result in an error like: 
    
    error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:crypto/evp/evp_enc.c:540
    
Supplying the `-md md5` option should solve the issue: 
    
    $ openssl enc -d -md md5 -in encrypted -out decrypted
    
###  Python 3.10 and "ca md too weak" errors

In Python 3.10 by default there is a hardcoded list of allowed OpenSSL ciphers. Some of the less secure, like MD5, have been disabled at the `ssl` module level, ignoring the system-wide configuration of OpenSSL. It results sometimes in strange errors on older certificates, sometimes even when establishing `https` connections, like: 
    
    requests.exceptions.SSLError: HTTPSConnectionPool(host='a.kind.of.example.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(398, '[SSL: CA_MD_TOO_WEAK] ca md too weak (_ssl.c:3862)')))
    
To make Python follow the system configuration, you may have to rebuild it, adding `--with-ssl-default-suites=openssl` parameter to `./configure`. The issue has been also reported as [FS#73549](<https://bugs.archlinux.org/task/73549>). 

## See also

  * [维基百科的 OpenSSL 页面](<https://zh.wikipedia.org/wiki/OpenSSL> "zhwp:OpenSSL")，包含背景信息。
  * [OpenSSL](<https://www.openssl.org>) 项目页面。
  * [FreeBSD Handbook](<https://www.freebsd.org/doc/en/books/handbook/openssl.html>)
  * [Step-by-step guide to create a signed SSL certificate](<https://www.akadia.com/services/ssh_test_certificate.html>)
  * [OpenSSL Certificate Authority](<https://jamielinux.com/docs/openssl-certificate-authority/>): A guide demonstrating how to act as your own certificate authority.
  * [Bulletproof SSL and TLS](<https://www.feistyduck.com/books/bulletproof-ssl-and-tls/bulletproof-ssl-and-tls-introduction.pdf>) by Ivan Ristić, a more formal introduction to SSL/TLS
