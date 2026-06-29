**翻译状态：**

  * 本文（或部分内容）译自 [ClamAV](<https://wiki.archlinux.org/title/ClamAV> "arch:ClamAV")，最近一次同步于 2025-05-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/ClamAV?diff=0&oldid=831607>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ClamAV_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Clam AntiVirus](<https://www.clamav.net>) 是一款 UNIX 下开源的 (GPL) 反病毒工具包。它提供了包括一个灵活且可扩展的多线程守护进程，一个命令行扫描程序及用于自动更新数据库的高级工具在内的多个实用程序。ClamAV 主要用被在文件和邮件服务器上，它通过内置的特征库来检测恶意软件，且不能被当作传统的终端安全套件来使用。 

由于多重原因，Linux 反恶意软件产品的现状并不理想： 

  1. 使用有限：和 Windows 相比，Linux 的用户和终端数较少，导致公司不愿为 Linux 平台开发产品。
  2. 安于现状：很多人认为 Linux 本身就是安全的，导致缺乏恶意软件防护的意识。这也导致主动防御机制上的空缺。
  3. 缺乏功能：现有工具往往缺乏 Windows 反恶意软件产品中常见的一些高级功能，因此在 Linux 上的效果较差。

由于基于 Linux 的服务器和物联网设备数量不断增加，Linux 上的恶意软件数量也在不断增加，可能的攻击面也在不断扩大，因此这种情况尤为糟糕。 

ClamAV 是当前 Linux 上为数不多的，且积极开发中的反恶意软件解决方案之一。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [clamav](<https://archlinux.org/packages/?name=clamav>)包 软件包。 

该操作将安装以下工具： 
    
    clamd：ClamAV 守护进程
    clamonacc：访问实时保护
    clamdscan：一个简易的扫描客户端
    clamdtop：针对 clamd 的资源监控界面
    freshclam：特征库更新守护进程
    clamconf：用于创建和检查配置文件的工具
    
所有 ClamAV 相关的工具、服务和守护进程都通过套接字与 clamd 进行通信。 

默认情况下，这是通过一个名为“LocalSocket”的本地套接字完成的。 

ClamAV 还提供了通过使用网络套接字进行远程通信的功能，该套接字名为“TCPSocket”。 

**警告：** 在 LocalSocket 改为使用 TCPSocket 时，请注意与 clamd 端口安全相关的警告。通常来说会使用本地 unix 套接字，但请注意该端口未经验证或保护。 

更多信息请参考： 

<https://blog.clamav.net/2016/06/regarding-use-of-clamav-daemons-tcp.html>

<https://docs.clamav.net/manual/Usage/Scanning.html#clamd-v0101> (Daemon and then ClamD section)

另一个需要注意的问题是，在使用 LocalSocket 时，clamd 需要在一个有权限扫描受监控文件的用户下运行。 

##  配置

正常情况下应已有默认配置文件，否则可以通过 clamconf 手动进行生成： 
    
    # clamconf -g freshclam.conf > freshclam.conf
    # clamconf -g clamd.conf > clamd.conf
    # clamconf -g clamav-milter.conf > clamav-milter.conf
    
下列文件中包含了对应的配置项： 

  * freshclam：`/etc/clamav/freshclam.conf`
  * clamd：`/etc/clamav/clamd.conf`
  * clamd 邮件过滤：`/etc/clamav/clamav-milter.conf`

另外，你可以通过执行 `clamconf` 来检查配置文件是否可用。 

默认安装方式将创建正常的默认配置，如 clamav 用户/用户组和所需的 clamd 配置。 

还可以设置其它建议配置： 
    
    /etc/clamav/clamd.conf
    
    # Log time with each message.
    # Default: no
    LogTime yes
    
    # Log additional information about the infected file, such as its
    # size and hash, together with the virus name.
    ExtendedDetectionInfo yes
    
    # Run as another user (clamd must be started by root for this option to work)
    # Default: don't drop privileges
    User clamav
    
    # Maximum depth directories are scanned at.
    # Default: 15
    MaxDirectoryRecursion 20
    
    DetectPUA yes
    HeuristicAlerts yes
    ScanPE yes
    ScanELF yes
    ScanOLE2 yes
    ScanPDF yes
    ScanSWF yes
    ScanXMLDOCS yes
    ScanHWP3 yes
    ScanOneNote yes
    ScanMail yes
    ScanHTML yes
    ScanArchive yes
    Bytecode yes
    AlertBrokenExecutables yes
    AlertBrokenMedia yes
    AlertEncrypted yes
    AlertEncryptedArchive yes
    AlertEncryptedDoc yes
    AlertOLE2Macros yes
    AlertPartitionIntersection yes
    
###  启用实时保护（访问时扫描，OnAccessScan）

访问时扫描是一个实时保护守护进程，会在读取/写入或执行文件时对其进行扫描。它可被配置为在检测到问题时发出提示或进行屏蔽。 

可以通过编辑 `/etc/clamav/clamd.conf` 来配置访问时扫描；使用该访问时扫描需要进行以下更改： 
    
    /etc/clamav/clamd.conf
    
    # Exclude the UID of the scanner itself from checking, to prevent loops
    OnAccessExcludeUname clamav
    
建议进行以下更改将将访问时扫描器设为仅提醒模式： 
    
    /etc/clamav/clamd.conf
    
    # Set the mount point where to recursively perform the scan,
    # this could be every path or multiple path (one line for path)
    OnAccessMountPath /
    
    # Alternatively, add some directories instead of mount points
    # OnAccessIncludePath /home
    
    # Prevention doesn't work with OnAccessMountPath.
    # It works with OnAccessIncludePath, as long as /usr and /etc are not included.
    # Including /var while activating prevention is also not recommended, because
    # this would slow down package installation by a factor of 1000.
    OnAccessPrevention no
    
    # Perform scans on newly created, moved, or renamed files
    OnAccessExtraScanning yes
    
    # Optionallyexclude root-owned processes
    # OnAccessExcludeRootUID true
    
####  为警报弹出通知提醒

目前为止，ClamAV 会静默记录所有检测结果，但不会通知用户。可以通过下面的操作在检测到问题时提醒用户。 

首先，在 clamd 配置中添加一行： 
    
    /etc/clamav/clamd.conf
    
    VirusEvent /etc/clamav/virus-event.bash
    
接下来，允许 _clamav_ 用户通过 [sudo](<../zh-cn/Sudo.html> "Sudo") 以任何带有自定义环境变量的用户身份运行 _notify-send_ ： 
    
    /etc/sudoers.d/clamav
    
    clamav ALL = (ALL) NOPASSWD: SETENV: /usr/bin/notify-send

然后创建 `/etc/clamav/virus-event.bash` 文件，添加以下内容并将其设为[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")： 
    
    /etc/clamav/virus-event.bash
    
    #!/bin/bash
    PATH=/usr/bin
    ALERT="Signature detected by clamav: $CLAM_VIRUSEVENT_VIRUSNAME in $CLAM_VIRUSEVENT_FILENAME"
    
    # Send an alert to all graphical users.
    for ADDRESS in /run/user/*; do
        USERID=${ADDRESS#/run/user/}
        /usr/bin/sudo -u "#$USERID" DBUS_SESSION_BUS_ADDRESS="unix:path=$ADDRESS/bus" PATH=${PATH} \
            /usr/bin/notify-send -w -u critical -i dialog-warning "Virus found!" "$ALERT"
    done
    
该文件使你可以自定义 clamd 访问时扫描服务检测到问题时弹出的消息内容。 

默认情况下， _clamonacc_ 会将刚访问的文件名称传递给 _clamav_ 进行扫描。问题是，如果 _clamav_ 用户无法访问对应的文件，就不能使用该方式进行扫描。作为替代，可以让 _clamonacc_ （其始终以根用户权限运行）传递文件描述符。参考以下内容[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `clamav-clamonacc.service`： 
    
    [Service]
    ExecStart=
    ExecStart=/usr/sbin/clamonacc -F **--fdpass** --log=/var/log/clamav/clamonacc.log
    
最后，[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")或[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `clamav-clamonacc.service` 和 `clamav-daemon.service`。 

参考：[#启动 ClamAV + OnAccessScanning 守护进程](<#%E5%90%AF%E5%8A%A8_ClamAV_+_OnAccessScanning_%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B>)

如果 [AppArmor](<../zh-cn/AppArmor.html> "AppArmor") 拒绝了 _clamd_ ，可以将其设为 complain 模式： 
    
    # aa-complain clamd
    
##  更新病毒库

通过下列命令更新病毒库: 
    
    # freshclam
    
如果你处于代理后，需编辑 `/etc/clamav/freshclam.conf` 并更新 HTTPProxyServer，HTTPProxyPort，HTTPProxyUsername 和 HTTPProxyPassword 的信息。 

病毒库保存在下列文件中： 
    
    /var/lib/clamav/daily.cld
    /var/lib/clamav/main.cld
    /var/lib/clamav/bytecode.cvd
    
For automatic updates first create and set the requires freshclam.log file: 
    
    touch /var/log/clamav/freshclam.log
    chmod 600 /var/log/clamav/freshclam.log
    chown clamav /var/log/clamav/freshclam.log
    
[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `clamav-freshclam.service` 或 `clamav-freshclam-once.timer` 来保持病毒库为最新。 

`clamav-freshclam.service` 将启动 `freshclam` 为守护进程模式，默认每天进行 12 次检查（每 2 小时一次）。检查频率可以在 `/etc/clamav/freshclam.conf` 中进行修改。 

`clamav-freshclam-once.timer` 将启动 `freshclam` 为每天检查一次。检查频率可在 `/usr/lib/systemd/system/clamav-freshclam-once.timer` 中进行修改。 

**注意：**

  * 以守护进程模式启动的 freshclam 在每次启动服务时会进行检查。
  * 每小时检查超过 1 次将被 CDN 屏蔽 24 小时。
  * `.timer` 单元将遵循计划配置，与设备重启或服务重启无关。
  * 可参考 [#添加更多病毒库/特征库](<#%E6%B7%BB%E5%8A%A0%E6%9B%B4%E5%A4%9A%E7%97%85%E6%AF%92%E5%BA%93/%E7%89%B9%E5%BE%81%E5%BA%93>) 一节添加病毒特征数据库

##  启动 ClamAV + OnAccessScanning 守护进程

该操作将把所有病毒特征加载到内存中。以 2024 年 2 月为例，这些特征共将占用至少 1.6GB 内存空间。在定期更新特征时，将短时占用多一倍的内存空间。 

**注意：**

  * 在首次启动服务前需要先运行 `freshclam`，否则将出现报错，并无法正常启动 ClamAV。
  * 如果你只需要使用独立扫描器进行扫描，就无需启动守护进程。更多信息可参考下方的[扫描病毒](<#%E6%89%AB%E6%8F%8F%E7%97%85%E6%AF%92>)部分。
  * 如果没有启用访问时扫描，那守护进程不会进行任何操作，详细信息请参考 [#启用实时保护（访问时扫描，OnAccessScan）](<#%E5%90%AF%E7%94%A8%E5%AE%9E%E6%97%B6%E4%BF%9D%E6%8A%A4%EF%BC%88%E8%AE%BF%E9%97%AE%E6%97%B6%E6%89%AB%E6%8F%8F%EF%BC%8COnAccessScan%EF%BC%89>)

对应的服务是 `clamav-daemon.service`。[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")它并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")使它自动在启动时运行。 

另外请[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `clamav-clamonacc.service` 以开启实时访问保护。 

##  测试

为了确保 ClamAV 和定义安装正确，请使用 _clamscan_ 扫描 [EICAR 测试文件](<https://www.eicar.org/download-anti-malware-testfile/>)（无病毒代码的无害签名）。 
    
    $ curl <https://secure.eicar.org/eicar.com.txt> | clamscan -
    
输出**必须** 包括 
    
    stdin: Win.Test.EICAR_HDB-1 FOUND
    
###  实时防护

您可以下载 eicar 文件并保存在您配置 clamonacc 监控的目录中。例如： 
    
    $ cd /home/user/Downloads/
    $ wget <https://secure.eicar.org/eicar.com.txt>
    $ cat eicar.com.txt
    
##  添加更多病毒库/特征库

ClamAV 可以使用来自其他存储库或安全厂商的病毒/特征库。 

可通过安装 [clamav-unofficial-sigs](<https://aur.archlinux.org/packages/clamav-unofficial-sigs/>)AUR（参见 [GitHub 描述](<https://github.com/extremeshok/clamav-unofficial-sigs#description>)）或是 [python-fangfrisch](<https://aur.archlinux.org/packages/python-fangfrisch/>)AUR（参见[线上文档](<https://rseichter.github.io/fangfrisch/>)）来添加最重要的部分。两者都会添加来自如 MalwarePatrol，SecuriteInfo，Yara，Linux Malware Detect 等著名供应商的特征/病毒库。 

**注意：** 必须[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `clamav-freshclam.service` 才能从 ClamAV 镜像更新官方特征信息。

###  选项 #1：配置 Fangfrisch

[Fangfrisch](<https://rseichter.github.io/fangfrisch/>) 在设计上目标成为更安全，灵活和方便的 clamav-unofficial-sigs 替代品，且[无需太多配置](<https://rseichter.github.io/fangfrisch/#_configuration>)（`/etc/fangfrisch/fangfrisch.conf`）。 

最重要的是，与 clamav-unofficial-sigs 不同，Fangfrisch 用不需要以 root 权限运行 

通过以下命令创建库结构： 
    
    # sudo -u clamav /usr/bin/fangfrisch --conf /etc/fangfrisch/fangfrisch.conf initdb
    
[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `fangfrisch.timer`（系统层级）。 

###  选项 #2：配置 clamav-unofficial-sigs

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `clamav-unofficial-sigs.timer`。 

这将根据 `/etc/clamav-unofficial-sigs` 目录下的配置文件信息定期更新非官方特征信息。 

可通过如下方法手动更新特征： 
    
    # clamav-unofficial-sigs.sh
    
可参考 `/etc/clamav-unofficial-sigs/user.conf` 来修改默认设置。 

####  MalwarePatrol 病毒库

如果你想使用 MalwarePatrol 病毒库，需要先在 <https://malwareblocklist.org> 注册账号（需付费）。 

在 `/etc/clamav-unofficial-sigs/user.conf` 中，修改以下内容来启用该功能： 
    
    malwarepatrol_receipt_code="YOUR-RECEIPT-NUMBER" # 输入收据编号
    malwarepatrol_product_code="8" # 免费账号设为 8，高级客户设为 15
    malwarepatrol_list="clamav_basic" # clamav_basic 或是 clamav_ext
    malwarepatrol_free="yes" # 免费账号设为 yes，高级客户设为 no 
    
来源：<https://www.malwarepatrol.net/clamav-configuration-guide/>

##  扫描病毒

有两种方法进行按需扫描： 

###  使用独立扫描器

`clamscan` 可用以扫描文件, 用户目录亦或是整个系统： 
    
    $ clamscan myfile
    $ clamscan --recursive --infected /home/archie
    # clamscan --recursive --infected --exclude-dir='^/sys|^/dev' /
    
  * 如果希望 `clamscan` 删除感染的文件，请使用 `--remove` 参数。
  * 使用 `-l _path/to/file_` 参数可以将 `clamscan` 的日志写入 log 文件。

如果希望 `clamscan` 删除感染的文件，请使用 `--remove` 参数，也可以使用 `--move=/dir` 来隔离文件。 

你可能会想要 `clamscan` 扫描大文件，在这一情况下，可将 {{ic|1=--max-filesize=4000M} 和 `--max-scansize=4000M` 添加到命令中。'4000M' 指的是最大值，可按需降低。 

`-l /path/to/file` 选项将把 `clamscan` 的日志输出为文本文件，方便定位受感染文件。 

###  使用守护进程

`clamdscan` 与上一选项类似，但使用了守护进程，因此必须要守护进程运行中才能使用。由于守护进程会读取 `/etc/clamav/clamd.conf` 中指定的配置，大多数选项都将被忽略。 

##  使用 milter

Milter 会检查 sendmail 服务器中的邮件是否含有病毒。根据需要编辑 `/etc/clamav/clamav-milter.conf`，例如： 
    
    /etc/clamav/clamav-milter.conf
    
    MilterSocket /tmp/clamav-milter.socket
    MilterSocketMode 660
    FixStaleSocket yes
    User clamav
    MilterSocketGroup clamav
    PidFile /run/clamav/clamav-milter.pid
    TemporaryDirectory /tmp
    ClamdSocket unix:/run/clamav/clamd.ctl
    LogSyslog yes
    LogInfected Basic

创建 `/etc/systemd/system/clamav-milter.service`： 
    
    /etc/systemd/system/clamav-milter.service
    
    [Unit]
    Description='ClamAV Milter'
    After=clamav-daemon.service
    Restart=Always
    
    [Service]
    Type=forking
    ExecStart=/usr/bin/clamav-milter --config-file /etc/clamav/clamav-milter.conf
    
    [Install]
    WantedBy=multi-user.target

如需使用如 [logrotate](</wzh/index.php?title=Logrotate&action=edit&redlink=1> "Logrotate（页面不存在）") 等自动化程序停止服务，可能会需要不同的 `Restart=` 配置。 

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `clamav-milter.service`。 

对于 [Postfix](<../zh-cn/Postfix.html> "Postfix")，将以下内容添加到 `/etc/postfix/main.cf`： 
    
    /etc/postfix/main.cf
    
    smtpd_milters = unix:/tmp/clamav-milter.socket
    milter_default_action = tempfail

检查 [journalctl](<../zh-cn/Systemd/Journal.html> "Journalctl") 来确认 postfix 对 `clamav-milter.socket` 的访问权限是否正常。如有问题，请将 postfix 添加到 `clamav` 组中。 

##  小贴士

###  使用多线程运行

####  使用 clamscan

通过命令行使用 `clamscan` 扫描文件或文件夹时只会使用单 CPU 线程。如果不考虑时间或者希望电脑不卡，就没什么大问题。但如果你要扫描大型目录，或者需要快速扫描 U 盘，就最好使用全部 CPU 核心来加速进程。 

`clamscan` 设计上为单线程，因此可以使用 `xargs` 进行多线程扫描： 
    
    $ find /home/archie -type f -print0 | xargs -0 -P $(nproc) clamscan
    
在这一例子中，`xargs` 的 `-P` 参数同时调用了尽可能多的 CPU 核心（数量由 `nproc` 提供）。`--max-lines` 和 `--max-args` 参数可以更精细地调整线程间的负载分配。 

因为每个进程都是独立的，且都会单独加载特征文件，所以该操作会消耗大量内存。单个线程会消耗大概 1G 或以上的内存，且可能会由于内存不足（OOM）导致系统卡住。可以考虑使用 clamdscan。 

####  使用 clamdscan

如果你已经启动了 `clamd` 守护进程，可以使用 `clamdscan`（参考 [#启动 ClamAV + OnAccessScanning 守护进程](<#%E5%90%AF%E5%8A%A8_ClamAV_+_OnAccessScanning_%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B>)）： 
    
    $ clamdscan --multiscan --fdpass /home/archie
    
其中 `--multiscan` 参数会让 `clamd` 使用可用线程并行扫描文件夹中的内容。由于守护进程是以 `clamav` 用户和用户组身份运行的，因此必须使用 `--fdpass` 参数将文件描述符权限传递给 `clamd`。 

`clamdscan` 的可用线程数是由 `/etc/clamav/clamd.conf` 中的 `MaxThreads` 参数决定的（默认为 10）[clamd.conf(5)](<https://man.archlinux.org/man/clamd.conf.5>)。只有在指定了 `--multiscan` 选项时，`clamdscan` 才会使用多线程扫描，否则将保持使用单线程。 

####  启用 TCPSocket

如果你在 `/etc/clamav/clamd.conf` 中启用了 TCPSocket，需要一并[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `clamav-daemon.socket`（参考 [FS#57669](<https://bugs.archlinux.org/task/57669>)），将 [systemd](<../zh-cn/Systemd.html> "Systemd") socket 文件中的配置改为对应的 IP 地址和端口： 
    
    /etc/systemd/system/clamav-daemon.socket.d/override.conf
    
    [Socket]
    ListenStream=
    ListenStream=/run/clamav/clamd.ctl
    ListenStream=127.0.0.1:3310

最后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `clamav-daemon.socket`，就能看到 Clamd 绑定到了 TCP 3310 端口： 
    
    # ss -tulpn | grep clamd
    
    tcp   LISTEN 0      4096       127.0.0.1:3310      0.0.0.0:*    users:(("clamd",pid=599,fd=4),("systemd",pid=1,fd=44))

##  疑难解答

**注意：** 确保运行 `clamscan` 的用户拥有病毒库文件（`/var/lib/clamav/*.c?d`）的读取权限。

### Error: Clamd was NOT notified

如果你在运行 freshclam 命令之后出现下列信息： 
    
    WARNING: Clamd was NOT notified: Cannot connect to clamd through 
    /var/lib/clamav/clamd.sock connect(): No such file or directory
    
为 clamav 添加一个 sock 文件： 

**警告：** 参考 [#安装](<#%E5%AE%89%E8%A3%85>) 中的警告了解 clamd 端口安全的相关信息：
    
    # touch /run/clamav/clamd.ctl
    # chown clamav:clamav /run/clamav/clamd.ctl
    
然后， 编辑 `/etc/clamav/clamd.conf`，去掉该行注释: 
    
    LocalSocket /run/clamav/clamd.ctl
    
保存文件并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `clamav-daemon.service`。 

### Error: No supported database files found

当启动守护进程时出现下列错误信息： 
    
    LibClamAV Error: cli_loaddb(): No supported database files found
    in /var/lib/clamav ERROR: Not supported data format
    
这意味着 `/etc/clamav/clamd.conf` 中的 `DatabaseDirectory` 设置与 `/etc/clamav/freshclam.conf` 中的 `DatabaseDirectory` 设置不匹配。`/etc/clamav/freshclam.conf` 指向了 `/var/lib/clamav`，而 `/etc/clamav/clamd.conf` 指向了 `/usr/share/clamav`（默认）或其它目录。你需要编辑 `/etc/clamav/clamd.conf`，将其中的 `DatabaseDirectory` 改为与 `/etc/clamav/freshclam.conf` 一致，之后就能正常启动 _clamav_ 了。 

###  Error: Can't create temporary directory

如果提示如下错误并给出包含 UID 和 GID 的提示， 
    
    # can't create temporary directory
    
请修改权限： 
    
    # chown UID:GID /var/lib/clamav && chmod 755 /var/lib/clamav
    
##  参考

  * [Wikipedia:ClamAV](<https://en.wikipedia.org/wiki/ClamAV> "wikipedia:ClamAV")
