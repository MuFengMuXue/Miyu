**翻译状态：**

  * 本文（或部分内容）译自 [MySQL](<https://wiki.archlinux.org/title/MySQL> "arch:MySQL")，最近一次同步于 2020-06-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/MySQL?diff=0&oldid=621588>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MySQL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[MySQL](<https://en.wikipedia.org/wiki/MySQL> "wikipedia:MySQL") 是 一个广泛使用的多线程，多用户 SQL 数据库，由 Oracle 公司开发。 

##  安装

Arch Linux 默认推荐使用 [MariaDB](<../zh-cn/MariaDB.html> "MariaDB")，这是 MySQL 的一个社区维护分支，旨在实现“无缝替换”。Oracle 的 MySQL [已被移至](<https://archlinux.org/news/mariadb-replaces-mysql-in-repositories/>) [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")（Arch User Repository）包名为[mysql](<https://aur.archlinux.org/packages/mysql/>)AUR。另一个旨在完全兼容的分支是 [Percona Server](<https://en.wikipedia.org/wiki/Percona_Server_for_MySQL> "wikipedia:Percona Server for MySQL")，可从 [percona-server](<https://archlinux.org/packages/?name=percona-server>)包 获得。 

Percona 也有 Oracle 的 [InnoDB](<https://en.wikipedia.org/wiki/InnoDB> "wikipedia:InnoDB") 存储引擎的分支，称为 [XtraDB](<https://en.wikipedia.org/wiki/XtraDB> "wikipedia:XtraDB")。木卡 [MariaDB](<../zh-cn/MariaDB.html> "MariaDB") 和 Percona Server 都使用此分支。 

##  图形工具

  * **[phpMyAdmin](<../zh-cn/PhpMyAdmin.html> "PhpMyAdmin")** — MySQL Web 界面，用 PHP 编写。

     <https://www.phpmyadmin.net> || [phpmyadmin](<https://archlinux.org/packages/?name=phpmyadmin>)包

  * **[MySQL Workbench](<https://en.wikipedia.org/wiki/MySQL_Workbench> "wikipedia:MySQL Workbench")** — 适用于数据库架构师，开发人员和 DBA 的统一可视工具。 由 Oracle 开发，不能保证与[MariaDB](<../zh-cn/MariaDB.html> "MariaDB")一起使用。

     <https://www.mysql.com/products/workbench/> || [mysql-workbench](<https://archlinux.org/packages/?name=mysql-workbench>)包

有关支持多个 DBMS 的工具，请参阅[应用程序列表/文档#数据库工具](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#%E6%95%B0%E6%8D%AE%E5%BA%93%E5%B7%A5%E5%85%B7> "应用程序列表/文档")。 

##  控制台工具

  * **MyCLI** — MySQL 的终端客户端，具有自动完成功能和语法突出显示功能。

     <https://www.mycli.net> || [mycli](<https://aur.archlinux.org/packages/mycli/>)AUR

##  程序访问

  * [JDBC and MySQL](<https://wiki.archlinux.org/title/JDBC_and_MySQL> "en:JDBC and MySQL")
  * [PHP#MySQL/MariaDB](<../zh-cn/PHP.html#MySQL/MariaDB> "PHP")
  * [Python](<../zh-cn/Python.html> "Python")
    * [python-mysqlclient](<https://archlinux.org/packages/?name=python-mysqlclient>)包
    * [python-mysql-connector](<https://archlinux.org/packages/?name=python-mysql-connector>)包
  * [C++](<../zh-cn/C.html> "C++")
    * [mysql++](<https://archlinux.org/packages/?name=mysql%2B%2B>)包
  * [Ruby](<https://wiki.archlinux.org/title/Ruby> "en:Ruby")
    * [ruby-mysql2](<https://aur.archlinux.org/packages/ruby-mysql2/>)AUR
  * [Perl](<https://wiki.archlinux.org/title/Perl> "en:Perl")
    * [perl-dbd-mysql](<https://archlinux.org/packages/?name=perl-dbd-mysql>)包
