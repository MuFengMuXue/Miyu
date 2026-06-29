**翻译状态：**

  * 本文（或部分内容）译自 [Aria2](<https://wiki.archlinux.org/title/Aria2> "arch:Aria2")，最近一次同步于 2024-09-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Aria2?diff=0&oldid=809521>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Aria2_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自 aria2 [主页](<https://aria2.github.io/>): 

    aria2 是一个轻量级多协议多源命令行下载工具，支持 [HTTP](</wzh/index.php?title=HTTP&action=edit&redlink=1> "HTTP（页面不存在）")/[HTTPS](</wzh/index.php?title=HTTPS&action=edit&redlink=1> "HTTPS（页面不存在）")， [FTP](<../zh-cn/Category:FTP.html> "FTP")，[BitTorrent](<../zh-cn/Category:BitTorrent.html> "BitTorrent") 和 [Metalink](<https://en.wikipedia.org/wiki/Metalink> "wikipedia:Metalink")。用户可以通过内置的 [JSON-RPC](<https://en.wikipedia.org/wiki/JSON-RPC> "wikipedia:JSON-RPC") 和 [XML-RPC](<https://en.wikipedia.org/wiki/XML-RPC> "wikipedia:XML-RPC") 接口操作 aria2。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [aria2](<https://archlinux.org/packages/?name=aria2>)包 软件包。 

要以[守护进程](<../zh-cn/Systemd.html> "Daemon")运行 aria2，你可以写一个 [systemd 用户单元](<#%E4%BD%9C%E4%B8%BA%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B%E4%BD%BF%E7%94%A8_aria2>)。 

##  配置

### aria2.conf

aria2 默认从 `$XDG_CONFIG_HOME/aria2/aria2.conf` 中寻找全局配置，该行为可以通过 `--conf-path` 选项改变： 

  * 下面的示例用配置文件 `/file/aria2.rapidshare` 中的选项下载 `aria2.example.rar`：

    $ aria2c --conf-path=/file/aria2.rapidshare http://rapidshare.com/files/12345678/aria2.example.rar
    
如果存在 `$XDG_CONFIG_HOME/aria2/aria2.conf`，但希望使用 `/file/aria2.rapidshare` 中的选项，需要在命令中加入 `--no-conf` 选项： 

  * 若不使用默认的配置文件，只使用 `/file/aria2.rapidshare` 中的选项下载 `aria2.example.rar`：

    $ aria2c --no-conf --conf-path=/file/aria2.rapidshare http://rapidshare.com/files/12345678/aria2.example.rar
    
如果不存在 `$XDG_CONFIG_HOME/aria2/aria2.conf`，并且你想要简化配置管理： 
    
    $ touch $XDG_CONFIG_HOME/aria2/aria2.conf
    
###  示例 aria2.conf
    
    continue
    dir=${HOME}/Desktop
    file-allocation=none
    input-file=${HOME}/.aria2/input.conf
    log-level=warn
    max-connection-per-server=4
    min-split-size=5M
    on-download-complete=exit

这与执行下面的命令等价： 
    
    $ aria2c --dir=${HOME}/Desktop --file-allocation=none --input-file=${HOME}/.aria2/input.conf --on-download-complete=exit --log-level=warn FILE
    
**注意：** 上面示例 aria.conf 可能错误地使用了 $HOME 变量，一些用户报告说，使用花括号语法会在 aria2 的工作目录下创建名叫 ${HOME} 的文件夹。因为 bash 会把 $HOME 当成环境变量，这样的文件夹很难访问。目前建议在 aria2.conf 中使用绝对路径。

####  选项细节

  * `continue`: 如果存在下载任务对应的控制文件，自动继续未完成的下载任务。
  * `dir=${HOME}/Desktop`: 在 `~/Desktop` 中存储下载文件。
  * `file-allocation=none`: 不要在下载开始前预分配磁盘空间（默认值：prealloc1
  * `input-file=${HOME}/.aria2/input.conf`: 从 `~/.aria2/input.conf` 中的 URI 下载文件，URI 以 TAB 分割。
  * `log-level=warn`: 设置日志级别，只输出警告和错误。（默认值：debug）
  * `max-connection-per-server=4`: 设置每个服务器的最大链接数为 4。（默认值：1）
  * `min-split-size=5M`: 只在文件大小超过 2*5MB = 10MB 时分割文件。（默认值： 20M）
  * `on-download-complete=exit`: 当下载任务完成时，运行 `exit` 命令并退出 shell。

#####  示例输入文件 #1

从两个分别的地址下载 `aria2-1.10.0.tar.bz2` 到 `~/Desktop`，并合并为 `aria2-1.10.0.tar.bz2`
    
    http://aria2.net/files/stable/aria2-1.10.0/aria2-1.10.0.tar.bz2    http://sourceforge.net/projects/aria2/files/stable/aria2-1.10.0/aria2-1.10.0.tar.bz2
    
#####  示例输入文件 #2

下载 `aria2-1.9.5.tar.bz2`，命名为 `aria2.old.tar.bz2 `，保存到 `/file/old`
    
    http://aria2.net/files/stable/aria2-1.9.5/aria2-1.9.5.tar.bz2
      dir=/file/old
      out=aria2.old.tar.bz2
      
下载 `aria2-1.10.0.tar.bz2`，命名为 `aria2.new.tar.bz2`，保存到 `~/Desktop`
    
    http://aria2.net/files/stable/aria2-1.10.0/aria2-1.10.0.tar.bz2
      out=aria2.new.tar.bz2
    
####  备注

1 `--file-allocation=falloc`: 推荐在新的文件系统，比如 [ext4](<../zh-cn/Ext4.html> "Ext4") （具有 extents 支持的）、[btrfs](<../zh-cn/Btrfs.html> "Btrfs") 或者 [XFS](<../zh-cn/XFS.html> "XFS") 上，使用这个选项，因为它们几乎可以瞬间分配 GB 级别的大文件。不要在传统的文件系统，比如 [ext3](</wzh/index.php?title=Ext3&action=edit&redlink=1> "Ext3（页面不存在）") 上，使用 falloc，因为预分配会消耗与正常分配相同的时间，还会阻塞 aria2 下载。 

**提示：** 要查看完整的配置选项，参见 `aria2c --help=#all` 和 [aria2c(1) § OPTIONS](<https://man.archlinux.org/man/aria2c.1#OPTIONS>)。

###  示例 aria2.rapidshare
    
    http-user=USER_NAME
    http-passwd=PASSWORD
    allow-overwrite=true
    dir=/file/Downloads
    file-allocation=falloc
    enable-http-pipelining=true
    input-file=/file/input.rapidshare
    log-level=error
    max-connection-per-server=2
    summary-interval=120

####  选项细节

  * `http-user=USER_NAME`: 设置 HTTP [用户名](<https://en.wikipedia.org/wiki/User_\(computing\)> "wikipedia:User \(computing\)")为 USER_NAME。这会影响所有的 [URI](<https://en.wikipedia.org/wiki/Uniform_Resource_Identifier> "wikipedia:Uniform Resource Identifier")。
  * `http-passwd=PASSWORD`: 设置 HTTP [密码](<https://en.wikipedia.org/wiki/Password> "wikipedia:Password")为 PASSWORD。这会影响所有的 URI。
  * `allow-overwrite=true`: 如果控制文件不存在，重新下载。（默认值：false）
  * `dir=/file/Downloads`: 存储下载文件到 `/file/Downloads`。
  * `file-allocation=falloc`: 在下载开始前，调用 [posix_fallocate(3)](<https://man.archlinux.org/man/posix_fallocate.3>) 分配磁盘空间。（默认值：prealloc）
  * `enable-http-pipelining=true`: 启用 [HTTP/1.1 流水线](<https://en.wikipedia.org/wiki/HTTP_Pipelining> "wikipedia:HTTP Pipelining")来降低网络延迟的影响，并减少数据用量。（默认值：false）
  * `input-file=/file/input.rapidshare`: 从 `/file/input.rapidshare` 中的 URI 下载文件，URI 以 TAB 分割。
  * `log-level=error`: 设置日志级别，只输出错误。（默认值：debug）
  * `max-connection-per-server=2`: 设置每台服务器每个文件的最大链接数为 2。（默认值：1）
  * `summary-interval=120`: 每 120 秒输出下载进度汇总。（默认值：60）2

####  备注

  * 因为 `aria2.rapidshare` 包含用户名和密码，建议将该文件权限设置为 600 或类似的权限。

    $ cd /file
    $ chmod 600 /file/aria2.rapidshare
    $ ls -l
    total 128M
    -rw------- 1 arch users  167 Aug 20 00:00 aria2.rapidshare
    
2 `summary-interval=0`: 不显示下载进度汇总，可以提高总体性能。日志仍然会按照 `log-level` 选项的配置输出。 

**提示：** 示例的配置文件可以用于[Hotfile](<http://www.hotfile.com/>)，[DepositFiles](<https://depositfiles.com/>) 等网站。

**注意：** 命令行选项永远优先于配置文件中的选项。

###  示例 aria2.bittorrent
    
    bt-seed-unverified
    max-overall-upload-limit=1M
    max-upload-limit=128K
    seed-ratio=5.0
    seed-time=240

####  选项细节

  * `bt-seed-unverified=false`: 在做种前不检查文件哈希。（默认值：true）
  * `max-overall-upload-limit=1M`: 设置全局最大上传速度为 1MB/sec。（默认值：0）
  * `max-upload-limit=128K`: 设置每个种子的最大上传速度为 128K/sec。（默认值：0）
  * `seed-ratio=5.0`: 下载完成后持续做种直到分享率达到 5.0。（默认值：1.0）
  * `seed-time=240`: 下载完成后做种 240 分钟。

**注意：** 如果同时设置了 `seed-ratio` 和 `seed-time`，当至少一个条件满足时就会停止做种。

###  示例 aria2.daemon

这个配置可以用于以服务启动的 aria2。可以与下面的前端一起使用。注意 rpc-user 与 rpc-pass 选项已经被弃用，但许多前端还不支持新的认证系统。记得修改用户名、密码和下载目录。 
    
    continue
    daemon=true
    dir=/home/aria2/Downloads
    file-allocation=falloc
    log-level=warn
    max-connection-per-server=4
    max-concurrent-downloads=3
    max-overall-download-limit=0
    min-split-size=5M
    enable-http-pipelining=true
    
    enable-rpc=true
    rpc-listen-all=true
    rpc-user=rpcuser
    rpc-passwd=rpcpass

##  前端

**注意：** 前端的设置不会影响 `aria2` 本身的配置，不确定不同的前端是否会在提供了自定义配置时，复用 `aria2` 的配置。用户应当确认选择的工具能效实现，并能持久保存配置。（比如 uGet 提供了自己的 `aria2` 命令行，并且会在重启间保存配置）。

### Web UIs

**注意：** 这些前端需要 `aria2c` 以 `--enable-rpc` 选项启动。它们应该在你本地的设备，而不是远程服务器上运行。

  * **WebUI** — Aria2 的 HTML 前端。

     <https://github.com/ziahamza/webui-aria2> || [webui-aria2-git](<https://aur.archlinux.org/packages/webui-aria2-git/>)AUR

  * **aria2rpc** — 用于连接远程 `aria2c` 实例的命令行工具。如果安装了 `aria2c`，该程序可以在 `/usr/share/doc/aria2/xmlrpc/aria2rpc` 下找到。

     <https://github.com/tatsuhiro-t/aria2/blob/master/doc/xmlrpc/aria2rpc> || [aria2](<https://archlinux.org/packages/?name=aria2>)包

  * **AriaNg** — 纯 HTML & JavaScript 实现的aria2前端，也提供桌面客户端。

     <https://github.com/mayswind/AriaNg> || [ariang-git](<https://aur.archlinux.org/packages/ariang-git/>)AUR, [ariang-native-electron-git](<https://aur.archlinux.org/packages/ariang-native-electron-git/>)AUR

###  其他 UIs

**注意：** 这些前端**不需要** `aria2c` 以 `--enable-rpc` 选项启动。

  * **aria2fe** — 一个命令行下载工具 aria2 的 GUI。

     <https://sourceforge.net/projects/aria2fe/> || [aria2fe](<https://aur.archlinux.org/packages/aria2fe/>)AUR

  * **Persepolis** — Aria2 下载管理器的图形前端，具有许多功能，支持 HTTP 和 FTP。

     <https://github.com/persepolisdm/> || [persepolis](<https://archlinux.org/packages/?name=persepolis>)包

  * **uGet** — 功能丰富的 GTK/CLI 下载管理器，可以通过内置的插件，使用 aria2 作为后端。

     <https://ugetdm.com> || [uget](<https://archlinux.org/packages/?name=uget>)包

  * **Motrix** — 基于 aria2 的全功能下载管理器，支持 HTTP、FTP、BitTorrent 和 Magnet。

     <https://github.com/agalwood/Motrix> || [motrix](<https://aur.archlinux.org/packages/motrix/>)AUR

##  提示与技巧

###  下载但不安装软件包

只需要用下面的命令： 
    
    # pacman -Sp _packages_ | aria2c -i -
    
`pacman -Sp` 在标准输出里打印软件包的 URL，而不是下载它们，然后用 `|` 管道传给下一个命令。最后，`aria2c -i -` 里的 `-i` 意味着下载文件的 URL 应该从文件里指定。但如果传入了 `-`，就从 stdin 里读取 URL。 

### pacman XferCommand

参见 [Pacman/提示和技巧#aria2](<../zh-cn/Pacman/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#aria2> "Pacman/提示和技巧"). 

###  改变 User Agent

一些站点会根据你的 User Agent 过滤请求，由于 aria2 并不出名，使用主流下载器或浏览器的 User Agent 可能会更好。只需要像这样使用 `-U` 选项： 
    
    $ aria2c -UWget http://some-url-to-download/file.xyz
    
你可以任意指定 User Agent，比如 **-UMozilla/5.0** 等。 

###  在 makepkg 中使用 aria2

你可以使用 aria2 代替 [curl](<https://archlinux.org/packages/?name=curl>)包 来下载源文件，只需要像下面一样更改 `DLAGENTS` 变量： 
    
    /etc/makepkg.conf
    
    [...]
    DLAGENTS=('ftp::/usr/bin/aria2c -UWget -s4 -x4 %u -o %o --follow-metalink=mem'
              'http::/usr/bin/aria2c -UWget -s4 -x4 %u -o %o --follow-metalink=mem'
              'https::/usr/bin/aria2c -UWget -s4 -x4 %u -o %o --follow-metalink=mem'
              'rsync::/usr/bin/rsync --no-motd -z %u %o'
              'scp::/usr/bin/scp -C %u %o')
    [...]

**注意：** 用 `-UWget` 选项改变 user agent 为 Wget，可以防止下载文件时，站点根据不同的 user agent 提供不同的响应。由于 aria2 不是著名的下载器，可能会被站点识别为浏览器而不是下载器，所以使用 Wget 的 user agent 可以在大多数情况下解决问题。使用`--follow-metalink=mem`选项来避免将metalink下载为单独的文件导致校验检查失败。

###  作为守护进程使用 aria2

要使用 aria2 作为守护进程，你可以[写一个systemd用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")。比如： 
    
    ~/.config/systemd/user/aria2cd.service
    
    [Unit]
    Description=aria2 Daemon
    
    [Service]
    ExecStart=/usr/bin/aria2c --conf-path=_/path/to/conf_
    
    [Install]
    WantedBy=default.target

[#示例 aria2.daemon](<#%E7%A4%BA%E4%BE%8B_aria2.daemon>) 展示了配置文件示例。 

###  使用 aria2 做种

要做种下载好的种子，使用 `--check-integrity` 选项： 
    
    $ aria2c --check-integrity=true --seed-ratio=0.0 --dir="/path/to/iso" "/path/to/torrent/archlinux-2020.03.01-x86_64.iso.torrent"
    
指定 `--seed-ratio=0.0` 选项可以永久做种。 

##  另请参见

  * [aria2 手册](<https://aria2.github.io/manual/en/html/index.html>) \- 官方网站
  * [aria2 用例](<https://aria2.github.io/manual/en/html/aria2c.html#example>) \- 官方网站
