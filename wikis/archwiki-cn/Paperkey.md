**翻译状态：**

  * 本文（或部分内容）译自 [Paperkey](<https://wiki.archlinux.org/title/Paperkey> "arch:Paperkey")，最近一次同步于 2023-08-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Paperkey?diff=0&oldid=756936>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Paperkey_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [GnuPG](<../zh-cn/GnuPG.html> "GnuPG")

[Paperkey](<https://www.jabberwocky.com/software/paperkey/>) 是一个在纸上导出 GnuPG 密钥的命令行工具。它通过从私钥中删除公钥部分来减小导出密钥的大小。Paperkey 还在密钥中包含 CRC-24 校验和，以允许用户检查其私钥是否已正确恢复。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading")软件包 [paperkey](<https://archlinux.org/packages/?name=paperkey>)包。 

##  用法

###  备份

**警告：** 恢复纸质密钥备份时，您需要有可用的公钥！由于使公钥公开是安全的，故请考虑将其上传到[公钥服务器](<../zh-cn/GnuPG.html#%E4%BD%BF%E7%94%A8%E5%85%AC%E9%92%A5%E6%9C%8D%E5%8A%A1%E5%99%A8> "GnuPG")。

要创建 GnuPG 密钥的备份，请将私钥通过管道符传输到 paperkey： 
    
    $ gpg --export-secret-key _key-id_ | paperkey --output _secret-key-paper_.asc
    
###  恢复私钥

要恢复密钥，您需要有一个包含 paperkey 数据和公钥的文件。然后运行以下命令将私钥导入 `~/.gnupg`： 
    
    $ paperkey --pubring _public-key_.gpg --secrets _secret-key-paper_.asc | gpg --import
    
或者，将私钥恢复到一个文件： 
    
    $ paperkey --pubring _public-key_.gpg --secrets _secret-key-paper_.asc --output _secret-key_.gpg
    
####  Error: unable to parse OpenPGP packets (is this armored data?)

如果在恢复密钥时收到此错误，则需要先解除（dearmor）公钥： 
    
    $ gpg --dearmor _public-key_.asc
    
##  提示和技巧

###  直接打印私钥

如果没有说明 `--output` 参数，paperkey 会将其输出打印到 `stdout`。可以直接打印密钥而无需中间文件，这可能会产生安全隐患。为此，请安装 [CUPS](<../zh-cn/CUPS.html> "CUPS")，并通过管道符传输到 `lpr`： 
    
    $ gpg --export-secret-key _key-id_ | paperkey | lpr
    
###  将私钥转换成二维码

默认情况下，paperkey 会将密钥输出为可读的文本格式。虽然这种格式保证了有能力读取和恢复已打印出的信息，但它不是很方便。`--output-type raw` 选项告诉 paperkey 要输出原始（raw）密钥数据。这允许了其他编码方式的使用，包括计算机可读的编码，例如[二维码](<https://en.wikipedia.org/wiki/QR_code> "wikipedia:QR code")。 

[qrencode](<https://archlinux.org/packages/?name=qrencode>)包 程序可以这样使用： 
    
    $ gpg --export-secret-key _key-id_ | paperkey --output-type raw | qrencode --8bit --output _secret-key.qr.png_
    
可以使用 `--level H` 选项将[纠错级别](<https://www.qrcode.com/en/about/error_correction.html>)提升到最大值。这可以恢复约 30% 的丢失数据，但代价是减少了[二维码的容量](<https://www.qrcode.com/en/about/version.html>)。如果密钥不适合（高纠错级别的）二维码，也可以使用较低的 `Q` 和 `M` 纠错级别，恢复率分别约为 25% 和 15%。默认纠错级别为 `L`，允许恢复约 7% 的丢失数据。 

###  从二维码恢复私钥

使用 [zbar](<https://archlinux.org/packages/?name=zbar>)包，可以使用[相机](<../zh-cn/%E7%BD%91%E7%BB%9C%E6%91%84%E5%83%8F%E6%9C%BA%E9%85%8D%E7%BD%AE.html> "网络摄像机配置")恢复密钥： 
    
    $ zbarcam -1 --raw -Sbinary | paperkey --pubring _public-key_.gpg | gpg --import
    
相同的选项也适用于 `zbarimg`： 
    
    $ zbarimg -1 --raw -q -Sbinary _secret-key.qr.png_ | paperkey --pubring _public-key_.gpg | gpg --import
    
**提示：** 使用 `-q` 选项运行 zbarimg 会在打印解码数据后禁止打印其状态文本。不使用该选项，传递到 paperkey 中的数据可能会被污染。

如果您使用的是扫描的图像，则可能必须通过此命令对其进行模糊处理。 
    
    $ convert secret-key.qr.png -blur 0 secret-key-blurred.qr.png
    