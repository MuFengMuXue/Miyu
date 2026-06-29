**翻译状态：**

  * 本文（或部分内容）译自 [CURL](<https://wiki.archlinux.org/title/CURL> "arch:CURL")，最近一次同步于 2024-09-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/CURL?diff=0&oldid=816191>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/CURL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[cURL](<https://curl.haxx.se/>) 是一个命令行工具和库，用于使用 URL 传输数据。该命令支持多种不同的协议，包括 [HTTP](</wzh/index.php?title=HTTP&action=edit&redlink=1> "HTTP（页面不存在）")、HTTPS、[FTP](<../zh-cn/Category:FTP.html> "FTP")、[SCP](<../zh-cn/SCP_%E4%B8%8E_SFTP.html> "SCP") 和 SFTP。它还可以在没有用户交互的情况下工作，比如在脚本中。 

**注意：** 尽管表面上等同于 [wget](<../zh-cn/Wget.html> "Wget")，但事实并非如此。请参阅 [Can_I_do_recursive_fetches_with](<https://curl.se/docs/faq.html#Can_I_do_recursive_fetches_with>)、[运行与给定 wget 命令对应的 curl 命令](<https://superuser.com/a/972282>) 和 [What_is_curl_not](<https://curl.se/docs/faq.html#What_is_curl_not>)。

##  安装

**提示：** 一般情况下，cURL 已作为 [pacman](<https://archlinux.org/packages/?name=pacman>)包 等软件包的依赖而被安装。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [curl](<https://archlinux.org/packages/?name=curl>)包 软件包。 

##  用法

###  下载

cURL 的常见用例是将资源下载到指定文件： 
    
    $ curl --output _文件名_ _URL_
    
如果 URL 包含文件名，则可以直接将资源保存为该文件名： 
    
    $ curl --remote-name _URL_
    
同样，你也可以使用 `-J/--remote-header-name` 来接受来自 HTTP 服务器（来自 `Content-Disposition` 头信息）的文件名提示。当与 `-O/--remote-name` 结合使用时，如果 HTTP 服务器没有返回文件名提示，curl 将使用 URL 指定的文件名。 

您也可以省略输出选项，将资源打印到 stdout： 
    
    $ curl _URL_
    
### HTTP POST

您可以使用 cURL 发送 HTTP POST 请求： 
    
    $ curl --data _'request body'_ _URL_
    
如果命令行无法容纳 request body，cURL 可以从文件中读取 request body： 
    
    $ curl --data @_文件名_ _URL_
    
有时，您可能需要为 `Content-Type` 头指定一个自定义值（cURL 的默认值为 `application/x-www-form-urlencoded`）。您可以使用 `-H` 来实现这一功能。例如，如果您想发送一个带有 JSON body 的 POST request，可以使用： 
    
    $ curl --data _'json body'_ -H 'Content-Type: application/json' _URL_
    
请注意，curl 也有一个选项，可以以 json 格式写入 post 数据，并自动更改 header： `--json`: 
    
    $ curl --json '{"key":"value"}' _URL_
    
##  提示与技巧

###  跟踪重定向

跟踪重定向（如 HTTP 到 HTTPS 重定向）： 
    
    $ curl --location _URL_
    
###  显示下载错误

默认情况下，curl 会忽略错误（例如，在下载文件时，如果出现错误，curl 不会通知你，创建的文件将是空的），因此使用 `--fail` 可以让它显示错误信息： 
    
    $ curl --fail _URL_
    
###  压缩

如果你想[压缩](<https://everything.curl.dev/usingcurl/transfers/compression.html>)传输数据，（例如，在带宽比CPU更有限的情况下，curl 会下载压缩数据，然后在下载后解压缩）： 
    
    $ curl --compressed _URL_
    
###  进度条

当下载文件时，curl 可以选择普通的进度条（例如 `[##### ] 80%` ）。 
    
    $ curl --progress-bar _URL_
    
###  通配

也可以在 curl 中使用[通配](<https://everything.curl.dev/cmdline/urls/globbing.html>)： 
    
    $ curl "example.com/images/[1-9].png"
    $ curl "example.com/{first_page,second_page,third_page}"
    
##  配置文件

curl 也会在主目录和 `$XDG_CONFIG_HOME` 中搜索名为 `.curlrc` 的[配置文件](<https://everything.curl.dev/cmdline/configfile>)。默认情况下，你只需将想要使用的命令行参数放在 curl 中，例如 ： 
    
    $HOME/.curlrc
    
    # this is a comment, the next line would be the option for progressbar:
    -#
    # to make curl always compress:
    --compressed
    # or just
    compressed

##  参见

  * [Wikipedia:cURL](<https://en.wikipedia.org/wiki/cURL> "wikipedia:cURL")
  * [Everything curl](<https://everything.curl.dev/>) \- cURL 使用指南详解
  * [curl(1)](<https://man.archlinux.org/man/curl.1>)
