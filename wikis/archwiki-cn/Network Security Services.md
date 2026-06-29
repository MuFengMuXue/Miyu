[Network Security Services](<https://en.wikipedia.org/wiki/Network_Security_Services> "wikipedia:Network Security Services")(_NSS_)是一组旨在支持跨平台开发具有安全功能的客户端和服务器应用程序的库。 

使用NSS构建的应用程序可以支持[SSL](<https://en.wikipedia.org/wiki/SSL> "wikipedia:SSL") v2和v3、[TLS](</wzh/index.php?title=TLS&action=edit&redlink=1> "TLS（页面不存在）")、[PKCS #5](<https://en.wikipedia.org/wiki/PKCS_5> "wikipedia:PKCS 5")、[PKCS #7](<https://en.wikipedia.org/wiki/PKCS_7> "wikipedia:PKCS 7")、[PKCS #11](<https://en.wikipedia.org/wiki/PKCS_11> "wikipedia:PKCS 11")、[PKCS #12](<https://en.wikipedia.org/wiki/PKCS_12> "wikipedia:PKCS 12")、[S/MIME](<https://en.wikipedia.org/wiki/S/MIME> "wikipedia:S/MIME")、[X.509](<https://en.wikipedia.org/wiki/X.509> "wikipedia:X.509") v3证书以及其他安全标准。 

许多软件包都需要NSS，包括，例如，[Chromium](<../zh-cn/Chromium.html> "Chromium")和[Firefox](<../zh-cn/Firefox.html> "Firefox")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nss](<https://archlinux.org/packages/?name=nss>)包包。 

##  用法

使用NSS提供的 _certutil_ 工具来管理你的证书。 

###  列出证书数据库

要获得所有证书的列表。 
    
    $ certutil -d sql:$HOME/.pki/nssdb -L
    
要获得证书的详细信息。 
    
    $ certutil -d sql:$HOME/.pki/nssdb -L -n _certificate_nickname_
    
###  生成一个RSA私钥
    
    $ certutil -G -d _database_directory_ -g _keysize_ -n _nickname_
    
###  生成一个证书签名请求
    
    $ certutil -S -s _subject_ -n _nickname_ -x -t C,C,C -o _file_
    
###  生成一个自签名的证书
    
    $ certutil -S -s _subject_ -n _nickname_ -x -t C,C,C -o _file_
    
###  导入证书

要添加一个证书，请指定`-A`选项。 
    
    $ certutil -d sql:$HOME/.pki/nssdb -A -t "'TRUSTARGS'" -n _certificate_nickname_ -i _/path/to/cert/filename_
    
`TRUSTARGS`是由零个或多个字母组成的三个字符串，用逗号分隔，例如，`"TCu,Cu,Tuw"`。它们定义了证书在SSL、电子邮件和对象签名中应如何被信任，在[certutil documentation](<https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Tools/certutil>)或[Meena's blog post](<https://meenavyas.medium.com/about-trust-flags-of-certificates-in-nss-database-that-can-be-modified-by-certutil-67e4f33a6d0f>)中对信任标志进行了解释。 

要为SSL客户认证添加个人证书和私钥，请使用以下命令。 
    
    $ pk12util -d sql:$HOME/.pki/nssdb -i _/path/to/PKCS12/cert/filename.p12_
    
这将导入一个存储在PKCS #12文件中的个人证书和私钥。个人证书的`TRUSTARGS`将被设置为`"u,u,u"`。 

###  编辑证书

使用`-M`选项调用 _certutil_ 来编辑证书。例如，要编辑`TRUSTARGS`。 
    
    $ certutil -d sql:$HOME/.pki/nssdb -M -t "'TRUSTARGS'" -n _certificate_nickname_
    
###  删除证书

使用`-D`选项来删除证书。 
    
    $ certutil -d sql:$HOME/.pki/nssdb -D -n _certificate_nickname_
    
###  添加一个受信任的CA证书

[chromium](<https://archlinux.org/packages/?name=chromium>)包、[firefox](<https://archlinux.org/packages/?name=firefox>)包、[thunderbird](<https://archlinux.org/packages/?name=thunderbird>)包、[evolution](<https://archlinux.org/packages/?name=evolution>)包和[seamonkey](<https://archlinux.org/packages/?name=seamonkey>)包使用NSS检索可信的CA证书。 

[nss](<https://archlinux.org/packages/?name=nss>)包已经集成[p11-kit](<https://archlinux.org/packages/?name=p11-kit>)包，它将使用system-wide自动安装所有证书。但如果你更喜欢分发 "纯净" NSS，可以将证书安装到你自己的浏览器配置文件中。 
    
    certutil -d _database_ -A -i _myCA.cert_ -n "Honest Achmed's CA" -t C, 。
    
[chromium](<https://archlinux.org/packages/?name=chromium>)包和[evolution](<https://archlinux.org/packages/?name=evolution>)包使用一个位于`-d "sql:$HOME/.pki/nssdb"`的 "共享式" 数据库。 

对于[firefox](<https://archlinux.org/packages/?name=firefox>)包、[thunderbird](<https://archlinux.org/packages/?name=thunderbird>)包和[seamonkey](<https://archlinux.org/packages/?name=seamonkey>)包，要制定浏览器专用的配置文件目录（例如`-d ~/.mozilla/firefox/ov6jazas.default`）。 

##  参见

  * [网络安全服务 - Mozilla](<https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS>)
  * [使用证书数据库工具--Mozilla](<https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/tools/NSS_Tools_certutil#Using_the_Certificate_Database_Tool>)
  * [管理NSS数据库中的证书信任标志 - Meena Vyas, Oracle](<https://blogs.oracle.com/meena/about-trust-flags-of-certificates-in-nss-database-that-can-be-modified-by-certutil>)
