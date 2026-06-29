预加载的主要作用是让把文件放入RAM中，或者让文件保持在RAM中。这样做的好处是让应用预加载从而更快的打开，因为从内存读取要比从硬盘读取速度更快。虽然这样会使用一部分内存，但不会比应用打开后所需的内存多。所以，预加载最好用于大型的，经常打开的应用，比如 Firefox 和 LibreOffice。 

## Go-preload

[gopreload-git](<https://aur.archlinux.org/packages/gopreload-git/>)AUR 是个轻量级的守护进程，来自 [Gentoo forum](<https://forums.gentoo.org/viewtopic-t-622085-highlight-preload.html>)。为了使它发光发热，得启动后先在一个终端里为每个你想要preload的程序运行以下命令： 
    
    # gopreload-prepare _program_
    
对于普通用户，给予 `/usr/share/gopreload/enabled` 和 `/usr/share/gopreload/disabled` 的所有权： 
    
    # chown username:users /usr/share/gopreload/enabled /usr/share/gopreload/disabled
    
接着为每个你想要preload的程序“gopreload”： 
    
    $ gopreload-prepare _program_
    
接着，按照提示，当程序完全加载好时回车。这样就会在 `/usr/share/gopreload/enabled` 添加preload所需的列表。如果要在启动时加载列表中所有的程序，[启用](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")该systemd服务 `gopreload.service`. 

想要禁用一个程序的加载，在 `/usr/share/gopreload/enabled` 中移除你想要的程序或把那个程序移到文件 `/usr/share/gopreload/disabled` 里。 

建议在系统升级后运行gopreload prepare以刷新文件列表。 运行以下脚本文件可以非常方便地做到这一点： 
    
    # gopreload-batch-refresh.sh
    
只需要在不使用系统时运行它。 

###  配置

配置文件位于 `/etc/gopreload.conf`

## preload

**preload** 是由Behdad Esfahbod编写的程序，它作为一个[守护进程](<../zh-cn/Systemd.html> "Daemons")运行，并使用马尔可夫链统计程序的使用情况；在计算机空闲时，使用频率较高的程序的文件会加载到内存中。这会加快程序的启动时间，因为需要从磁盘读取的数据更少。 

###  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading")包[preload](<https://aur.archlinux.org/packages/preload/>)AUR。您现在可以[开启](<../zh-cn/Systemd.html> "Daemons")[systemd](<../zh-cn/Systemd.html> "Systemd")服务`preload`，然后也可以启用这个服务以便在开机时启动。 

###  配置

配置文件位于`/etc/preload.conf`，它包含适合普通用户的默认设置。`cycle`选项允许您配置调用preload的频率，以更新其要缓存的应用程序和库的信息。 

##  参阅

  * [wikipedia:Preload_(software)](<https://en.wikipedia.org/wiki/Preload_\(software\)> "wikipedia:Preload \(software\)")
  * [Improving performance](<../zh-cn/Improving_performance.html> "Improving performance")
