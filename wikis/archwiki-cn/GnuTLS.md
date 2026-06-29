**翻译状态：**

  * 本文（或部分内容）译自 [GnuTLS](<https://wiki.archlinux.org/title/GnuTLS> "arch:GnuTLS")，最近一次同步于 2020-05-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/GnuTLS?diff=0&oldid=614711>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GnuTLS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 翻译已过期 (在[Talk:GnuTLS](<../zh-cn/Talk:GnuTLS.html>)讨论)

根据 [Wikipedia](<https://en.wikipedia.org/wiki/GnuTLS> "wikipedia:GnuTLS"): 

     **GnuTLS** (the **GNU Transport Layer Security Library**) is a free software implementation of the TLS, SSL and DTLS protocols. It offers an application programming interface (API) for applications to enable secure communication over the network transport layer, as well as interfaces to access X.509, PKCS #12, OpenPGP and other structures.

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gnutls](<https://archlinux.org/packages/?name=gnutls>)包 包。 

要与 [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server") 集成，请安装 [mod_gnutls](</wzh/index.php?title=Mod_gnutls&action=edit&redlink=1> "Mod gnutls（页面不存在）")。 

##  用法

有关以下各节中使用的命令，请参见 [certtool(1)](<https://man.archlinux.org/man/certtool.1>)；有关 API 文档，请参见[信息](<https://www.gnutls.org/manual/html_node/index.html>)文档。 

###  生成 RSA 私钥
    
    $ certtool -p --rsa --bits=_keysize_
    
###  生成证书签名请求
    
    $ certtool -q --load-privkey _private_key_ --outfile _file_
    
###  生成自签名证书
    
    $ certtool -s --load-privkey _private_key_ --outfile _file_
    
##  另请参见

  * [官方网站](<https://www.gnutls.org/>)
