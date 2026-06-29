相关文章

  * [应用程序列表/科学](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E7%A7%91%E5%AD%A6.html> "应用程序列表/科学")

摘自 [QGIS Documentation](<https://docs.qgis.org/3.34/zh-Hans/docs/index.html>)： 

    QGIS旨在成为一个用户友好的地理信息系统，提供常用的功能和特性。该项目的最初目标是提供一个GIS数据查看器。QGIS在其发展过程中已经达到了这样一个阶段：它被用于日常GIS数据查看需求、数据捕获、高级GIS分析以及以复杂的地图、地图册和报告的形式呈现。QGIS支持大量的栅格和矢量数据格式，使用插件架构可以轻松添加新的格式支持。

##  安装

可以选择[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")不同版本： 

  * 稳定版 [qgis](<https://archlinux.org/packages/?name=qgis>)包

  * LTR 版（Long Term Release） [qgis-ltr](<https://aur.archlinux.org/packages/qgis-ltr/>)AUR

  * 测试版 [qgis-git](<https://aur.archlinux.org/packages/qgis-git/>)AUR。

##  配置

QGIS是高度可配置的。通过**设置** 菜单，提供了以下不同工具： 

  * 样式管理器: 创建和管理符号, 样式和颜色渐变。

  * 自定义投影: 创建您自己的 _坐标参照系_ 。

  * 键盘快捷键: 定义您自己的一组 _键盘快捷键_ 。此外, 工程属性 可以在每个QGIS会话期间替换它们 (可在 _工程_ 菜单下访问)。

  * 界面自定义: 配置应用程序界面, 隐藏您可能不需要的对话框或工具.

  * 选项: 设置全局选项以应用于软件的不同领域. 这些首选项保存在当前用户配置设置中, 并在使用此配置文件打开新工程时默认应用.

参见[官方文档](<https://docs.qgis.org/3.34/zh-Hans/docs/user_manual/introduction/qgis_configuration.html>)。 

**提示：** 插件可以在选项对话框中嵌入它们的设置。

##  问题解决

###  打开文件数量限制

如果您正在打开一个大型QGIS项目，并且您确定所有图层都是有效的，但是有些图层被标记为坏的，那么您可能遇到了此问题。Linux（以及其他类似的操作系统）有按进程打开文件的限制。每个进程的资源是受限的，且可以被继承。`ulimit`命令是一个内置的 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell") 命令，它仅为当前 shell 进程更改限制，新的限制将被每一个子进程继承。 

输入以下命令，你可以看到所有当前的ulimit信息： 
    
    ulimit -aS
    
在终端输入以下命令，你可以看到当前每个进程所允许打开的文件数量： 
    
    ulimit -Sn
    
要更改**现有会话** 的限制，您可以使用以下命令： 
    
     ulimit -Sn #number_of_allowed_open_files
     ulimit -Sn
     qgis
    
或者，您可以使用更新的 _prlimit_ 工具。更多信息请参见: [[1]](<https://manpages.ubuntu.com/manpages/latest/man1/prlimit.1.html>)

####  永久修改

在大多数 Linux 系统中，资源限制是在登录时通过 `pam_limits` 模块设定的，该模块依据的设置保存在文件 `/etc/security/limits.d/*.conf` 或者 `/etc/security/limits.conf` 中。如果你拥有 **root** 权限（也可以通过 [sudo](<../zh-cn/Sudo.html> "Sudo")）则可以编辑这些文件，但是你需要注销并重新登录使得变更生效。 

更多信息，参见[[2]](<https://www.cyberciti.biz/faq/linux-increase-the-maximum-number-of-open-files/>)、[[3]](<https://linuxaria.com/article/open-files-in-linux>)。 

###  启动时报错

####  启动时报错：**ModuleNotFoundError: No module named 'osgeo'**

启动时 Python 报错：**ModuleNotFoundError: No module named 'osgeo'** 、**NameError: name 'gdal' is not defined** 、**NameError: name 'ogr' is not defined** 、**NameError: name 'osr' is not defined** ，安装 [python-gdal](<https://archlinux.org/packages/?name=python-gdal>)包 即可。 

####  Python 报错：**无法加载插件 _xxx_ 因在调用其 _xxx_ 方法时发生错误**

Python 报错：**无法加载插件 _xxx_ 因在调用其 _xxx_ 方法时发生错误**、**ModuleNotFoundError: No module named '_xxx_ ' **，安装需要的 [Python](<../zh-cn/Python.html> "Python") 模块即可 

##  参见

  * [QGIS 官方网站](<https://www.qgis.org/>)

  * [QGIS 中文文档](<https://docs.qgis.org/3.34/zh-Hans/docs/index.html>)
