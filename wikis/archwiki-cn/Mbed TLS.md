**翻译状态：**

  * 本文（或部分内容）译自 [mbed TLS](<https://wiki.archlinux.org/title/mbed_TLS> "arch:mbed TLS")，最近一次同步于 2020-08-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/mbed_TLS?diff=0&oldid=632660>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/mbed_TLS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

根据 [Wikipedia](<https://en.wikipedia.org/wiki/mbed_TLS> "wikipedia:mbed TLS"): 

     **mbed TLS** （以前的 **PolarSSL** ）是 TLS 和 SSL 协议以及相应的加密算法和所需支持代码的实现。它具有 Apache License 版本 2.0 和 GPLv2 的双重许可。网站上的声明是 mbed TLS 旨在“易于理解，使用，集成和扩展”。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mbedtls](<https://archlinux.org/packages/?name=mbedtls>)包 软件包。 

##  用法

命令名称以“mbedtls_”开头，关于用法示例，请参见[知识库](<https://tls.mbed.org/kb>)。 

###  生成 RSA 私钥
    
    $ mbedtls_gen_key rsa_keysize=_keysize_ filename=_filename_
    
###  生成证书签名请求
    
    $ mbedtls_cert_req filename=_private_key_ subject_name=_subject_ output_file=_filename_
    
[相关方法](<https://tls.mbed.org/kb/how-to/generate-a-certificate-request-csr>)

###  生成自签名证书
    
    $ mbedtls_cert_write selfsign=1 issuer_key=_private_key_ issuer_name=_subject_ not_before=_YYYYMMDDHHMMSS_ not_after=_YYYYMMDDHHMMSS_ is_ca=1 max_pathlen=0 output_file=_file_
    
[相关方法](<https://tls.mbed.org/kb/how-to/generate-a-self-signed-certificate>)

##  参见

  * [官方网站](<https://tls.mbed.org/>)
  * [API 文档](<https://tls.mbed.org/api/>)
