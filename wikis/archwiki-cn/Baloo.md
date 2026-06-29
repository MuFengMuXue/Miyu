**翻译状态：**

  * 本文（或部分内容）译自 [Baloo](<https://wiki.archlinux.org/title/Baloo> "arch:Baloo")，最近一次同步于 2022-04-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Baloo?diff=0&oldid=727350>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Baloo_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Baloo](<https://community.kde.org/Baloo>) 是 [KDE](<../zh-cn/KDE.html> "KDE") Plasma 的文件索引与搜索框架。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [baloo](<https://archlinux.org/packages/?name=baloo>)包 软件包。 

##  用法与配置

为了在 Plasma 桌面上使用 Baloo 进行搜索，启动 krunner （默认快捷键 `ALT+F2`）并键入查询。若要在 Dophin（文件管理器）内搜索，按`CTRL+F`。 

在默认情况下，桌面搜索的 KCM 仅显示两个选项：一个将文件夹放入黑名单的面板以及一种一次点击来禁用它的方法。 

或者您可以编辑 `~/.config/baloofilerc` 文件[[1]](<https://community.kde.org/Baloo/Configuration>)。另外您也可以使用 `balooctl` 进程。运行 `balooctl stop` 和 `balooctl disable`。 

将文件夹添加到黑名单或完全禁用了Baloo之后，`baloo_file_cleaner` 进程将会自动删除所有不需要的索引文件。这些文件存储于 `~/.local/share/baloo/` 目录下。 

##  命令行用法
    
    $ baloosearch _query_
    
Support for range queries: 
    
    $ baloosearch "width>=6000 width<7000"
    
Groups and OR/AND operators: 
    
    $ baloosearch "tag:coolpicture OR (width>=6000 width<7000)"
    
For a list of all supported filter properties available, see ([info](<https://api.kde.org/frameworks/baloo/html/searching.html>)). 

Note that text search index breaks down all metadata (including filenames) into "words", and does all its searches over it from the beginning of the word only. What this means is that while `baloosearch "tutorial"` would match `my_great_tutorial.txt`, `baloosearch "utorial"` would not match it. To see what "words" baloo stored in the index for a particular file do: 
    
    $ balooshow -x _filename_
    
##  索引可移动设备或远程设备

默认情况下，所有可移动设备都在黑名单内，只需在 KCM 面板中将其移除即可。 

##  禁用索引器

To disable the Baloo file indexer: 
    
    $ balooctl suspend
    $ balooctl disable
    
The indexer will be disabled on next login. 

Alternatively, disable _Enable File Search_ in _System settings_ under _Search > File search_. 

To permanently delete the index database, run: 
    
    $ balooctl purge
    
This will also resolve the following error message in file dialogs and other applications ([KDE bug 437176](<https://bugs.kde.org/show_bug.cgi?id=437176>)): 
    
    kf.kio.core: "Could not enter folder tags:/."
    
##  疑难解答

### Inotify folder watch limit error

If you get the following error: 
    
    KDE Baloo Filewatch service reached the inotify folder watch limit. File changes may be ignored.
    
Then you will need to increase the inotify folder watch limit: 
    
    # echo 524288 > /proc/sys/fs/inotify/max_user_watches
    
To make changes permanent, create a [sysctl](<../zh-cn/Sysctl.html> "Sysctl") configuration file: 
    
    /etc/sysctl.d/40-max-user-watches.conf
    
    fs.inotify.max_user_watches=524288

### Plasma Vault Files are indexed and available even when vault is closed

This is a major security [bug](<https://bugs.kde.org/show_bug.cgi?id=390830>) not yet fixed. Any file inside vault is by default indexed and available through file manager search, Krunner and Kickoff. 

One workaround is to **stop** folder(s) from being indexed by Baloo. The relevant options are available in _System Settings > Search > File Search > Folder specific configuration > Add folder configuration > Stop indexing a folder_. After adding the desired folder, the existing Baloo data needs to be removed and freshly indexed again: 
    
    $ balooctl disable
    $ balooctl purge
    $ balooctl enable
    $ balooctl check
    