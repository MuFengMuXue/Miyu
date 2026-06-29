**翻译状态：**

  * 本文（或部分内容）译自 [SQLite](<https://wiki.archlinux.org/title/SQLite> "arch:SQLite")，最近一次同步于 2025-08-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/SQLite?diff=0&oldid=795524>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SQLite_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自[项目主页](<https://www.sqlite.org/>)： 

    SQLite 是一个实现自包含、无服务器、零配置、事务性 SQL 数据库引擎的软件库。SQLite 是世界上部署最广泛的 SQL 数据库引擎。SQLite的源代码在公共领域。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sqlite](<https://archlinux.org/packages/?name=sqlite>)包 包。 

相关的包包括： 

  * [sqlite-doc](<https://archlinux.org/packages/?name=sqlite-doc>)包 – 该网站绝大多数由静态 HTML 文件构成，包括所有 SQL 语法和 C/C++ 接口规范以及其他杂项文档 [[1]](<https://www.sqlite.org/docs.html>)
  * [sqlite-analyzer](<https://archlinux.org/packages/?name=sqlite-analyzer>)包 – `sqlite3_analyzer` 是一个命令行实用程序，用于测量和显示 SQLite 数据库文件中各个表和索引使用的空间大小和效率 [[2]](<https://www.sqlite.org/sqlanalyze.html>)
  * [sqlite-tcl](<https://archlinux.org/packages/?name=sqlite-tcl>)包 – SQLite 库的 Tcl 接口 [[3]](<https://www.sqlite.org/tclsqlite.html>)
  * [php-sqlite](<https://archlinux.org/packages/?name=php-sqlite>)包 – PHP 的 sqlite3 模块（别忘了在 `/etc/php/php.ini` 中启用它）
  * [ruby-sqlite3](<https://archlinux.org/packages/?name=ruby-sqlite3>)包 – SQLite3 嵌入式数据库的 Ruby 绑定
  * [gambas3-gb-db-sqlite3](<https://archlinux.org/packages/?name=gambas3-gb-db-sqlite3>)包 – Gambas3 Sqlite3 数据库存取组件

##  使用 sqlite3 命令行 shell

SQLite 库包含一个名为 sqlite3 的简单命令行实用程序，允许用户手动输入和执行 SQLite 数据库的 SQL 命令。 

###  创建数据库
    
    $ sqlite3 _数据库名_
    
###  创建表
    
    sqlite> create table tblone(one varchar(10), two smallint);
    
###  插入数据
    
    sqlite> insert into tblone values('helloworld',20);
    sqlite> insert into tblone values('archlinux', 30);
    
###  搜索数据库
    
    sqlite> select * from tblone;
    
    helloworld|20
    archlinux|30
    
参见 [sqlite 文档（英文）](<https://www.sqlite.org/docs.html>)。 

##  软件

  * **DB Browser for SQLite** — 高质量、可视化、开源的工具，用于创建、设计和编辑与 SQLite 兼容的数据库文件。

     <https://sqlitebrowser.org/> || [sqlitebrowser](<https://archlinux.org/packages/?name=sqlitebrowser>)包

  * **Sqliteman** — 简单的 sqlite3 浏览器与编辑器。

     <http://sqliteman.yarpen.cz/>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-05-06 ⓘ] || [sqliteman](<https://aur.archlinux.org/packages/sqliteman/>)AUR

  * **litecli** — 用于SQLite的命令行界面，具有自动补全和语法高亮功能。

     <https://litecli.com/> || [litecli](<https://aur.archlinux.org/packages/litecli/>)AUR

对于支持多个数据库管理系统的工具，参见[应用程序列表/文档#数据库工具](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#%E6%95%B0%E6%8D%AE%E5%BA%93%E5%B7%A5%E5%85%B7> "应用程序列表/文档")。 

##  在 shell 脚本中使用 sqlite

参见论坛[帖子](<https://bbs.archlinux.org/viewtopic.php?id=109802>)。 

##  另见

  * [SQLite 主页](<https://www.sqlite.org>)
  * [SQLite Hammer](<https://web.archive.org/web/20160429004604/http://hubpages.com/technology/sqlitehammer>)
  * [Using SQLite - Oreilly Book](<https://www.oreilly.com/library/view/using-sqlite/9781449394592>)
  * [SQLite - Apress Book](<https://www.amazon.com/Definitive-Guide-SQLite-Mike-Owens/dp/1590596730>)
