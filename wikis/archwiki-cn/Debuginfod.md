相关文章

  * [调试/获取跟踪数据](<../zh-cn/%E8%B0%83%E8%AF%95/%E8%8E%B7%E5%8F%96%E8%B7%9F%E8%B8%AA%E4%BF%A1%E6%81%AF.html> "调试/获取跟踪数据")

**翻译状态：**

  * 本文（或部分内容）译自 [Debuginfod](<https://wiki.archlinux.org/title/Debuginfod> "arch:Debuginfod")，最近一次同步于 2024-11-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Debuginfod?diff=0&oldid=806818>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Debuginfod_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Debuginfod](<https://sourceware.org/elfutils/Debuginfod.html>) 是一种通过 HTTP API 提供 debug 信息的服务。 

##  安装

[gdb](<https://archlinux.org/packages/?name=gdb>)包 会自动尝试从 `DEBUGINFOD_URLS` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")中指定的服务器下载调试文件（debug files），该变量是一串以空格分隔的 URL。 

[libelf](<https://archlinux.org/packages/?name=libelf>)包 是 [gdb](<https://archlinux.org/packages/?name=gdb>)包 的依赖项，附带了 `/etc/profile.d/debuginfod.sh` 和 `/etc/profile.d/debuginfod.csh` 脚本，这些脚本在登录时设置变量，因此无需安装额外的软件包。这些脚本解析 `/etc/debuginfod/` 中的 _.urls_ 文件，并将 `DEBUGINFOD_URLS` 环境变量默认设置为 `https://debuginfod.archlinux.org`。 

**提示：** 还可以使用 `https://debuginfod.elfutils.org/` 作为联合服务器并查询所有可用的 _debuginfod_ 服务器。

您可以选择性[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")提供 [debuginfod-find(1)](<https://man.archlinux.org/man/debuginfod-find.1>) 实用程序的 [debuginfod](<https://archlinux.org/packages/?name=debuginfod>)包 软件包，此包是 [delve](<https://archlinux.org/packages/?name=delve>)包 中的 debuginfod 支持所必需的。 

##  使用

**提示：** 关于 _debuginfod_ 配合 _gdb_ 一起使用，参考 [Debugging/Getting traces#Getting the trace](<../zh-cn/Debugging/Getting_traces.html#Getting_the_trace> "Debugging/Getting traces")。

###  手动下载

如果要手动检索 [zstd](<https://archlinux.org/packages/?name=zstd>)包 中某些源文件的调试符号, 可以使用 [debuginfod-find](<https://archlinux.org/packages/?name=debuginfod-find>)包: 
    
    $ debuginfod-find debuginfo /usr/bin/zstd
    
    /home/user/.cache/debuginfod_client/70e1b456c5813658df6436a3deb71812e75a0267/debuginfo
    
    $ debuginfod-find source /usr/bin/zstd /usr/src/debug/zstd-1.5.2/programs/fileio.c
    
    /home/user/.cache/debuginfod_client/70e1b456c5813658df6436a3deb71812e75a0267/source##usr##src##debug##zstd-1.5.2##programs##fileio.c

###  禁用

可以通过清除 `DEBUGINFOD_URLS` 来禁用 _debuginfod_ 客户端服务： 
    
    $ unset DEBUGINFOD_URLS
    
如果想使用本地缓存，而不尝试连接任何服务器，可以将 `DEBUGINFOD_URLS` 设置为非空字符串，例如 `/dev/null`。 

##  调试器支持

多种调试器支持使用 debuginfod 查找调试符号和源代码列表。 

软件包 | 状况 | 注意   
---|---|---  
[gdb](<https://archlinux.org/packages/?name=gdb>)包 | 支持 |   
[delve](<https://archlinux.org/packages/?name=delve>)包 | 支持 |   
KDE Crash Report | 支持 |   
[valgrind](<https://archlinux.org/packages/?name=valgrind>)包 | 支持 |   
  
##  缓存

_debuginfod_ 的缓存存储在 `$DEBUGINFOD_CACHE_PATH` （如果已设置）指定的位置。否则，如果设置了 `$XDG_CACHE_HOME`，它将使用 `$HOME/.cache/debuginfod_client/` 或 `$XDG_CACHE_HOME/debuginfod_client/`。缓存的大小可能增长得非常快，具体取决于您拥有的调试会话数量以及涉及的软件包。 

有 3 个参数可以配置缓存行为，如 [debuginfod(8) § CACHE](<https://man.archlinux.org/man/debuginfod.8#CACHE>) 手册中的描述: 

  * `cache_clean_interval_s`: 每次自动清理之间的间隔（默认为 86400，即 1 天）
  * `max_unused_age_s`: 未使用的数据保留多长时间（默认为 604800，即 1 周）
  * `cache_miss_s`: 记住失败的查询多长时间（默认为 600，即 10 分钟）

每个参数都由缓存文件夹中同名文件中的数字定义。 

如果你很少使用 _debuginfod_ ，可以手动删除缓存中的所有目录（保留参数文件）或完整的缓存目录。 

##  参见

  * [主页](<https://sourceware.org/elfutils/Debuginfod.html>)
  * [The elfutils debuginfod server, FOSDEM 2020](<https://www.youtube.com/watch?v=_iaK9L7akJU>)
