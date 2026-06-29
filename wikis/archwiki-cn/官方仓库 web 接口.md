**翻译状态：**

  * 本文（或部分内容）译自 [Official repositories web interface](<https://wiki.archlinux.org/title/Official_repositories_web_interface> "arch:Official repositories web interface")，最近一次同步于 2023-05-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Official_repositories_web_interface?diff=0&oldid=779250>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Official_repositories_web_interface_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Aurweb RPC interface](</wzh/index.php?title=Aurweb_RPC_interface&action=edit&redlink=1> "Aurweb RPC interface（页面不存在）")

本文提供了官方仓库网页界面的文档，通过该界面可以查询官方仓库并获取 JSON 格式的结果。 

##  软件包信息

基础链接: `https://www.archlinux.org/packages/`

###  软件包细节

链接格式: `/_仓库_ /_架构_ /_软件包_ /json`

例子: <https://archlinux.org/packages/core/x86_64/coreutils/json/>

###  文件列表

链接格式: `/_仓库_ /_架构_ /_软件包_ /files/json`

例子: <https://archlinux.org/packages/core/x86_64/coreutils/files/json/>

##  软件包搜索

该界面支持除了`sort`以外的和[HTML Search Form](<https://archlinux.org/packages/>)一样的查询格式。 

基础链接: `https://www.archlinux.org/packages/search/json`

###  通过名称或描述搜索

参数: `q`

例子: <https://archlinux.org/packages/search/json/?q=pacman>

###  通过准确的名称搜索

参数: `name`

例子: <https://archlinux.org/packages/search/json/?name=coreutils>

###  通过描述搜索

参数: `desc`

例子: <https://archlinux.org/packages/search/json/?desc=pacman>

###  通过仓库筛选

可以多次使用这个参数以在多个仓库中搜索(但是请注意,如果完全省略它会在所有仓库中搜索)。 

参数: `repo`

可用值: `Core`, `Core-Testing`, `Extra`, `Extra-Testing`, `Multilib`, `Multilib-Testing`

例子: [https://archlinux.org/packages/search/json/?q=cursor&repo=Core&repo=Extra](<https://archlinux.org/packages/search/json/?q=cursor&repo=Core&repo=Extra>)

###  通过架构筛选

可以多次使用这个参数以在多个架构的软件包中搜索(但是请注意,如果完全省略它会在所有架构的软件包中搜索)。 

参数: `arch`

可用值: `any`, `x86_64`

例子: [https://archlinux.org/packages/search/json/?q=cursor&arch=any&arch=x86_64](<https://archlinux.org/packages/search/json/?q=cursor&arch=any&arch=x86_64>)

###  通过维护者搜索

参数: `maintainer`

例子: [https://archlinux.org/packages/search/json/?repo=Extra&maintainer=orphan](<https://archlinux.org/packages/search/json/?repo=Extra&maintainer=orphan>)

###  通过打包者搜索

参数: `packager`

###  通过标记状态搜索

参数: `flagged`

可用值: `Flagged`, `Not+Flagged`

例子: [https://archlinux.org/packages/search/json/?arch=x86_64&flagged=Flagged](<https://archlinux.org/packages/search/json/?arch=x86_64&flagged=Flagged>)

##  参见

  * [Forum thread](<https://bbs.archlinux.org/viewtopic.php?id=170892>)
  * Initial feature request: [FS#13026](<https://bugs.archlinux.org/task/13026>)
  * [Kittypack: A silly little tool to poke archlinux.org/packages for info](<https://github.com/MrElendig/kittypack>)
