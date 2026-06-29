相关文章

  * [phpMyAdmin](<../zh-cn/PhpMyAdmin.html> "PhpMyAdmin")
  * [Adminer](<../zh-cn/Adminer.html> "Adminer")
  * [JDBC and MySQL](</wzh/index.php?title=JDBC_and_MySQL&action=edit&redlink=1> "JDBC and MySQL（页面不存在）")
  * [Open Database Connectivity](</wzh/index.php?title=Open_Database_Connectivity&action=edit&redlink=1> "Open Database Connectivity（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [MariaDB](<https://wiki.archlinux.org/title/MariaDB> "arch:MariaDB")，最近一次同步于 2025-01-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/MariaDB?diff=0&oldid=816531>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MariaDB_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[MariaDB](<https://en.wikipedia.org/wiki/MariaDB> "wikipedia:MariaDB") 是一个可靠的、高性能的、功能全面的数据库，旨在为用户提供长期免费、向下兼容能直接替代[MySQL](<../zh-cn/MySQL.html> "MySQL")的数据库服务。自2013年起，MariaDB就被Arch Linux当作官方默认的MySQL实现[[1]](<https://archlinux.org/news/mariadb-replaces-mysql-in-repositories/>)。 

##  安装

[MariaDB](<https://mariadb.com/>) 是 Arch Linux 中 MySQL 的[默认实现](<https://archlinux.org/news/mariadb-replaces-mysql-in-repositories/>)，由 [mariadb](<https://archlinux.org/packages/?name=mariadb>)包 软件包提供。 

**提示：**

  * 如果数据库 (位于 `/var/lib/mysql`) 运行在 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 分区之上, 你应当在创建数据库之前禁用 [Copy-on-Write](<../zh-cn/Btrfs.html#Copy-on-Write_\(CoW\)> "Btrfs") 特性。
  * 如果数据库运行在 [ZFS](<../zh-cn/ZFS.html> "ZFS") 分区之上, 你应该在创建数据库之前参阅 [ZFS#Databases](<../zh-cn/ZFS.html#Databases> "ZFS") 。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mariadb](<https://archlinux.org/packages/?name=mariadb>)包 软件包之后，你必须在启动 `mariadb.service` **之前** 运行下面这条命令： 
    
    # mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
    
然后 [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") 或者 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `mariadb.service`。 

**提示：** 如果数据目录使用的不是 `/var/lib/mysql`，需要在 `/etc/my.cnf.d/server.cnf` 文件的 `[mysqld]` 部分设置 `datadir=<数据目录>`

**注意：** 在继续之前，建议 [提高 MariaDB 安装的初始安全性](<#Improve_initial_security>)。

为了简化管理，你可能需要安装一个[前端工具](<../zh-cn/MySQL.html#Graphical_tools> "MySQL")。 

##  配置

默认情况下，`root` 用户和运行服务器的用户都可以管理数据库。 

要管理服务器，可以以运行服务器的用户身份运行 _mariadb_ ： 
    
    [mysql]$ mariadb
    
或者以 root 身份运行： 
    
    # mariadb
    
###  添加用户

以下是创建一个密码为'some_pass'的'monty'用户的示例，并赋予 mydb 完全操作权限： 
    
    $ mariadb -u root -p
    
    MariaDB> CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass';
    MariaDB> GRANT ALL PRIVILEGES ON mydb.* TO 'monty'@'localhost';
    MariaDB> quit

###  配置文件

_MariaDB_ 配置选项会按照以下顺序读取配置文件（根据 `mysqld --help --verbose | head -10` 的输出）： 
    
    /etc/my.cnf /etc/my.cnf.d/ ~/.my.cnf
    
在 `/etc/my.cnf.d/` 中创建一个以 _.cnf_ 为扩展名的配置文件，以确保升级时保留您的配置。 

根据您想要进行的更改范围（系统范围、仅用户...），使用相应的文件。有关更多信息，请参阅知识库中的[此条目]([https://mariadb.com/kb/en/library/configuring-mariadb-with-option-files/)。](<https://mariadb.com/kb/en/library/configuring-mariadb-with-option-files/\)%E3%80%82>)

###  启用自动补全

**注意：** 启用这项功能会增加客户端启动时间。

MySQL 默认禁用客户端自动补全功能。要在整个系统中启用它，编辑 `/etc/my.cnf.d/client.cnf`，并在 `client-mariadb` 下添加 `auto-rehash`。注意：不要将其放在 `mysqld` 下。下次运行 MariaDB 客户端时，补全功能将启用。 

###  使用 UTF8MB4

**警告：** 在更改字符集之前**务必** 先创建备份！

**注意：**[mariadb](<https://archlinux.org/packages/?name=mariadb>)包 包已经使用 `utf8mb4` 作为字符集，并使用 `utf8mb4_unicode_ci` 作为校对规则。使用默认（字符集）设置的用户可以跳过本节。 

  * 推荐使用 UTF8MB4 而不是 UTF-8，因为它允许完整的 Unicode 支持 [[2]](<https://mathiasbynens.be/notes/mysql-utf8mb4>) [[3]](<https://stackoverflow.com/questions/30074492/what-is-the-difference-between-utf8mb4-and-utf8-charsets-in-mysql>)。

将以下内容[追加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append")到 `/etc/my.cnf.d/my.cnf` 文件中： 
    
    [client]
    default-character-set = utf8mb4
    
    [mariadb]
    collation_server = utf8mb4_unicode_ci
    character_set_server = utf8mb4
    
    [mariadb-client]
    default-character-set = utf8mb4

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `mariadb.service` 以应用更改。更改字符集不会改变现有表格格式，只会影响新创建的表格以及检索数据的协议交互。 

参见[#Maintenance](<#Maintenance>) 以优化和检查数据库健康状况。 

###  使用内存作为临时文件存放点

MySQL 存储临时文件的目录名是 _tmpdir_ 。 

创建一个临时目录： 
    
    # mkdir -pv /var/lib/mysqltmp
    # chown mysql:mysql /var/lib/mysqltmp
    
通过命令找出 `mysql` 的 id 和 gid： 
    
    $ id mysql
    uid=27(mysql) gid=27(mysql) groups=27(mysql)
    
添加 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") 到 `/etc/fstab` 中： 
    
     tmpfs   /var/lib/mysqltmp   tmpfs   rw,gid=27,uid=27,size=100M,mode=0750,noatime   0 0
    
将以下配置添加到 `/etc/mysql/my.cnf` 的 `mysqld` 组下： 
    
     tmpdir      = /var/lib/mysqltmp
    
[Stop](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop") `mariadb.service`, [mount](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount") `/var/lib/mysqltmp/` 并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `mariadb.service`. 

###  时区表

尽管时区表在安装过程中已创建，但它们不会自动填充。如果您计划在 SQL 查询中使用 CONVERT_TZ()，则需要填充这些表。 

要填充所有时区的时区表： 
    
    $ mariadb-tzinfo-to-sql /usr/share/zoneinfo | mariadb -u root -p mysql
    
可选地，您可以使用特定的时区文件填充表： 
    
    $ mariadb-tzinfo-to-sql _timezone_file_ _timezone_name_ | mariadb -u root -p mysql
    
##  安全

###  提高初始的安全性

使用 `mariadb-secure-installation` 命令会交互式地引导您完成一些推荐的安全措施，比如移除匿名账户和测试数据库，从而提高初始安全性。 
    
    # mariadb-secure-installation
    
**警告：** 运行之后，请注意TCP端口3306仍将保持打开状态，但会拒绝连接并显示错误消息。要防止MySQL监听外部接口，请参阅[#仅在回环地址上监听](<#%E4%BB%85%E5%9C%A8%E5%9B%9E%E7%8E%AF%E5%9C%B0%E5%9D%80%E4%B8%8A%E7%9B%91%E5%90%AC>)和[#仅通过Unix套接字本地访问](<#%E4%BB%85%E9%80%9A%E8%BF%87Unix%E5%A5%97%E6%8E%A5%E5%AD%97%E6%9C%AC%E5%9C%B0%E8%AE%BF%E9%97%AE>)的部分。

###  只监听本地回环地址

默认情况下, MariaDB 会监听 0.0.0.0 这个地址, 它包括了所有的网络接口。 为了限制 MariaDB 只监听回环地址， 请在 `/etc/my.cnf.d/server.cnf`文件中添加如下行: 
    
    [mariadb]
    bind-address = localhost
    
这将绑定到地址 127.0.0.1 和 ::1，并使 MariaDB 能够接收 IPv4 和 IPv6 的连接。 

###  启用仅通过 Unix 套接字在本地启用访问

默认情况下，MariaDB 可通过 Unix sockets 和网络访问。如果只需要在本地主机上使用 MariaDB，则可以通过不在 TCP 端口 3306 上监听，而是仅在 Unix sockets 上监听来提高安全性。要实现这一点，请在`/etc/my.cnf.d/server.cnf`文件中添加以下行： 
    
    [mariadb]
    skip-networking
    
您仍然可以像以前一样在本地登录，但只能使用 Unix 套接字。 

###  授权远程访问

**警告：** 这不被视为最佳实践，因为可能会引起安全问题。如果你想要从网络内/外的另一台主机上管理 MariaDB 服务器，请考虑使用[安全外壳协议（Secure Shell）](</wzh/index.php?title=%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE%EF%BC%88Secure_Shell%EF%BC%89&action=edit&redlink=1> "安全外壳协议（Secure Shell）（页面不存在）"),[虚拟网络计算机（VNC）](</wzh/index.php?title=%E8%99%9A%E6%8B%9F%E7%BD%91%E7%BB%9C%E8%AE%A1%E7%AE%97%E6%9C%BA%EF%BC%88VNC%EF%BC%89&action=edit&redlink=1> "虚拟网络计算机（VNC）（页面不存在）")或[虚拟专用网络（VPN）](</wzh/index.php?title=%E8%99%9A%E6%8B%9F%E4%B8%93%E7%94%A8%E7%BD%91%E7%BB%9C%EF%BC%88VPN%EF%BC%89&action=edit&redlink=1> "虚拟专用网络（VPN）（页面不存在）")。

要允许远程访问MariaDB服务器，请确保MariaDB[已启用网络](<#Enable_access_locally_only_via_Unix_sockets>)并[正在适当的接口上进行侦听](<#Listen_only_on_the_loopback_address>). 

授予任何MariaDB用户远程访问权限（以root用户为例）： 
    
    # mariadb -u root -p
    
检查当前具有远程访问权限特权的用户： 
    
    SELECT User, Host FROM mysql.user WHERE Host <> 'localhost';
    
现在为您的用户（这里是 root）授予远程访问权限： 
    
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.1.%' IDENTIFIED BY 'my_optional_remote_password' WITH GRANT OPTION;
    
如果愿意，您可以将“%”通配符更改为特定的主机。密码可以与用户的主密码不同。 

###  配置主目录访问

**注意：** 出于安全考虑，systemd 的 .service 文件通过 `ProtectHome=true` 禁止 MariaDB 访问 `/home`、`/root` 和 `/run/user` 目录内的文件。`datadir` 必须要放在以上文件夹之外，并且由 `mysql` 用户和用户组 [所有](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%89%80%E6%9C%89%E8%80%85> "Chown")。 如果要改变这个设置，可以根据以下链接创建一个替代的 service 文件：[[4]](<https://mariadb.com/kb/en/mariadb/systemd/>)

##  维护

###  大版本升级时升级数据库

在 [mariadb](<https://archlinux.org/packages/?name=mariadb>)包 大版本发布时（例如从 mariadb-10.3.10-1 升级到 mariadb-10.9.4-1），建议升级系统数据库以启用新服务器功能： 
    
    # mariadb-upgrade -u root -p
    
要从 10.3.x 更新到 10.9.x： 

  * 停止 10.3.x 服务器
  * 升级软件包
  * 运行新软件包中的 `mariadb-upgrade` 以针对新运行的守护进程

如果（新）守护进程未启动，请参考 [#无法运行 mariadb-upgrade 因为 MariaDB 无法启动](<#%E6%97%A0%E6%B3%95%E8%BF%90%E8%A1%8C_mariadb-upgrade_%E5%9B%A0%E4%B8%BA_MariaDB_%E6%97%A0%E6%B3%95%E5%90%AF%E5%8A%A8>)。 

###  检查、优化和修复数据库

[mariadb-clients](<https://archlinux.org/packages/?name=mariadb-clients>)包 提供了 _mariadb-check_ ，可用于从 shell 中检查、修复和优化数据库中的表。更多信息请参见 [mariadb-check(1)](<https://man.archlinux.org/man/mariadb-check.1>)。以下是一些常用命令： 

要检查所有数据库中的所有表： 

##  备份

有各种各样的[工具和策略](<https://mariadb.com/kb/en/mariadb/documentation/backing-up-and-restoring/>)可以备份你的数据库。 

如果你正在使用默认的 InnoDB 存储引擎，[建议](<https://mariadb.com/kb/en/mariadb/documentation/clients-and-utilities/backup-restore-and-import/mysqldump/#examples>)的在线备份所有数据库并为[时序恢复](<https://dev.mysql.com/doc/refman/5.6/en/point-in-time-recovery.html>)（也称为“向前滚动”，当你需要恢复旧备份并重放自那个备份以来发生的更改时）的方法是执行以下命令： 
    
    $ mariadb-dump --single-transaction --flush-logs --events --routines --master-data=2 --all-databases -u root -p > all_databases.sql
    
这将提示输入 **MariaDB** 的 root 用户密码，该密码是在数据库[配置](<#Configuration>)期间定义的。 

[强烈建议不在命令行中指定密码](<https://dev.mysql.com/doc/refman/5.6/en/password-security-user.html>)，因为这会使密码通过 `ps aux` 或其他技术暴露给其他用户发现。相反，上述命令会提示输入指定用户的密码，并将其隐藏起来。 

###  压缩

由于 SQL 表可能会变得非常大，建议将上述命令的输出通过[压缩工具](<../zh-cn/Archiving_and_compression.html#Compression_only> "Archiving and compression")如 [xz(1)](<https://man.archlinux.org/man/xz.1>) 进行压缩： 
    
    $ mariadb-dump --single-transaction --flush-logs --events --routines --master-data=2 --all-databases -u root -p | xz -z > all_databases.sql.xz
    
解压缩创建的备份并将其重新加载到服务器中可以通过以下命令完成： 
    
    $ xzcat all_databases.sql.xz | mariadb -u root -p
    
这将重新创建并重新填充之前备份的所有数据库（参见[这个](<https://stackoverflow.com/questions/23180963/restore-all-mysql-database-from-a-all-database-sql-gz-file#comment35453351_23180977>)或[这个](<https://www.linuxquestions.org/questions/linux-server-73/how-to-restore-mysqldump-all-databases-backup-892922/>)）。 

###  非交互式

如果你想为 [cron](<../zh-cn/Cron.html> "Cron") 作业或 [systemd 定时器](</wzh/index.php?title=Systemd/cron_functionality&action=edit&redlink=1> "Systemd/cron functionality（页面不存在）")设置非交互式备份脚本，请参阅[选项文件](<https://mariadb.com/kb/en/configuring-mariadb-with-option-files/>)和[这个示例](<https://stackoverflow.com/a/9293090>)以了解 _mariadb-dump_ 。 

基本上，你应该在相关的[配置文件](<#Configuration_files>)中添加以下部分： 
    
    [mariadb-dump]
    user=mysqluser
    password=secret

在这里提及用户是可选的，但这样做可以让你不必在命令行中提及它。如果你想为所有工具（包括 `mariadb-client`）设置此选项，请使用 `[client]` 组。 

####  示例脚本

数据库可以转储到文件中以便轻松备份。以下 shell 脚本将为你完成此操作，在与脚本相同的目录中创建一个 `db_backup.xz` 文件，其中包含你的数据库转储： 
    
    #!/bin/sh
    
    THISDIR=$(dirname $(readlink -f "$0"))
    
    mariadb-dump --single-transaction --flush-logs --events --routines --master-data=2 --all-databases \
     | xz -z > $THISDIR/db_backup.xz
    echo 'purge master logs before date_sub(now(), interval 7 day);' | mariadb
    
另请参阅 [MariaDB](<https://mariadb.com/kb/en/mariadb/documentation/clients-and-utilities/backup-restore-and-import/mysqldump>) 手册中的官方 `mariadb-dump` 页面。 

###  Holland 备份

一个名为 [Holland Backup](<https://hollandbackup.org/>) 的基于 Python 的软件包可以自动化所有备份工作。它支持直接使用 mysqldump、LVM 快照到 tar 文件（mysqllvm）、带有 mysqldump 的 LVM 快照（mysqldump-lvm）以及 [xtrabackup](<https://archlinux.org/packages/?name=xtrabackup>)包 方法来提取数据。Holland 框架支持多种选项，并且高度可配置，几乎可以应对任何备份情况。 

主要的 [holland](<https://aur.archlinux.org/packages/holland/>)AUR 和 [holland-common](<https://aur.archlinux.org/packages/holland-common/>)AUR 包提供了核心框架；必须安装其中一个子包（[holland-mysqldump](<https://aur.archlinux.org/packages/holland-mysqldump/>)AUR、[holland-mysqllvm](<https://aur.archlinux.org/packages/holland-mysqllvm/>)AUR 和/或 [holland-xtrabackup](<https://aur.archlinux.org/packages/holland-xtrabackup/>)AUR）以进行完整操作。每种方法的示例配置位于 `/usr/share/doc/holland/examples/` 目录中，可以复制到 `/etc/holland/backupsets/`，也可以使用 `holland mk-config` 命令为指定的提供者生成基本配置。 

##  故障排除

###  执行 mysql_upgrade 后 MySQL 不能启动

试试安全模式下运行的 MySQL： 
    
    # mariadbd-safe --datadir=/var/lib/mysql/
    
然后再运行: 
    
    # mariadb-upgrade -u root -p
    
###  重置 root 密码

  1. 停止 `mariadb.service`.
  2. 用安全方式启动服务：
         
         # mariadbd-safe --skip-grant-tables --skip-networking &

  3. 连接服务器: 
         
         # mariadb -u root

  4. 修改 root 密码: 
         
         MariaDB [mysql]> FLUSH PRIVILEGES;
         MariaDB [mysql]> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
         MariaDB [mysql]> exit
         
  5. 停掉 mariadbd* 进程: 
         
         # kill $(cat /var/lib/mysql/$HOSTNAME.pid)

  6. 启动 `mariadb.service`.

###  检查并修复所有数据表

检查并自动修复所有数据库中的所有表，[查看更多](<https://dev.mysql.com/doc/refman/5.7/en/mysqlcheck.html>)： 
    
    # mariadb-check -A --auto-repair -u root -p
    
###  优化所有数据表

强制优化所有数据表，自动修复可能出现的数据表错误 
    
    # mariadb-check -A --auto-repair -f -o -u root -p
    
### OS error 22 when running on ZFS

如果您正在使用 [ZFS](<../zh-cn/ZFS.html> "ZFS") 并且遇见了如下错误 
    
    InnoDB: Operating system error number 22 in a file operation.
    
那么就需要修改 `/etc/mysql/my.cnf` 中的设置来禁用 aio_writes 
    
    [mariadb]
    ...
    innodb_use_native_aio = 0
    
###  无法通过命令行登录, 但是 phpmyadmin 正常工作

当使用了超长 (>80) 的密码后，这个问题有可能发生。 `mariadb` 的命令行不能在 readline 模式中处理那么多的字符。 所以如果打算使用推荐的密码输入方式： 
    
    $ mariadb -u user -p
    Password:
    
不妨考虑更换一个长度短一点的密码。 

**注意：** 您依然可以通过在命令行参数中指定密码来登录 
    
    $ mysql -u <user> -p"some-very-strong-password"
    
**警告：** 但这样做很危险，因为您的密码很可能会泄漏到某个地方，例如，日志。只有当遇到紧急情况才能考虑这么做，并且事后不要忘记更改密码。

###  MySQL 日志文件占用太多空间

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** /etc/my.cnf.d/my.cnf 不再存在 (在[Talk:MariaDB#"MariaDB 二进制日志占用大量磁盘空间"中的错误](</wzh/index.php?title=Talk:MariaDB&action=edit&redlink=1> "Talk:MariaDB（页面不存在）")讨论)

默认情况下，mariadbd 会在 `/var/lib/mysql/mysql-bin._XXXXXX_` 创建二进制日志文件，文件名中的数字递增。这些日志对于复制主服务器或数据恢复非常有用，但这些二进制日志可能会迅速占用大量磁盘空间。如果您不打算使用复制或数据恢复功能，可以通过在 `/etc/my.cnf.d/my.cnf` 中注释掉以下两行来禁用二进制日志记录，然后重启： 
    
    #log-bin=mysql-bin
    #binlog_format=mixed
    
或者，如果您希望保留这些日志但控制其大小并删除旧日志，可以设置以下限制然后重启： 
    
    log-bin=mysql-bin
    expire_logs_days = 10
    max_binlog_size  = 100M
    
另外，MariaDB 提供了一个命令来手动删除比特定日志更早的日志。例如，您可能会看到一个名为 `mysql-bin._000023_` 的文件，并希望删除比它更早的所有日志。只要 log-bin=mysql-bin 设置生效，您可以运行： 
    
    # mariadb -u root -p"PASSWORD" -e "PURGE BINARY LOGS TO 'mysql-bin._000023_ ;"
    
**警告：** 使用这些方法中的任何一种都可能会降低在尝试修复数据库表（例如数据库损坏）时成功恢复数据的机会。

###  OpenRC 无法启动 MariaDB

要使用 [OpenRC](<../zh-cn/OpenRC.html> "OpenRC") 启动 MariaDB，您需要在 MySQL 配置文件 `/etc/my.cnf.d/my.cnf` 的 `[mariadb]` 部分添加以下行： 
    
    user = mysql
    basedir = /usr
    datadir = /var/lib/mysql
    pid-file = /run/mysqld/mysql.pid
    
您现在应该能够使用以下命令启动 MariaDB： 
    
    # rc-service mysql start
    
###  更改 max_open_files/table_open_cache 的限制警告

通过创建 [systemd drop-in](<../zh-cn/Systemd.html#Drop-in_files> "Systemd") 来增加文件描述符的数量，例如： 
    
    /etc/systemd/system/mariadb.service.d/limit_nofile.conf
    
    [Service]
    LimitNOFILE=8192

###  10.4 到 10.5 升级崩溃："InnoDB: Upgrade after a crash is not supported. The redo log was created with MariaDB 10.4.x"

在 MariaDB 10.5 之前，redo log 被不必要地分割成多个文件。[[5]](<https://mariadb.com/kb/en/upgrading-from-mariadb-104-to-mariadb-105/>)

千万不要删除旧的二进制日志 `/var/lib/mysql/ib_logfile*`。 

要解决此问题，请安装 MariaDB 10.4。启动它并让它进行干净的关闭。之后，您可以再次升级到 10.5。如果指定了其他版本的 MariaDB，同样适用。 

###  Table 'mysql.xxx' does not exist in engine

症状：运行 _mariadb-upgrade_ 或 _mariadb-check_ 时，返回一个或多个类似以下的错误： 
    
    Table 'mysql.xxx' does not exist in engine
    
其中 "xxx" 通常是 mysql 数据库中的系统表。 

修复步骤： 

  1. 在 MariaDB `${DATADIR}</nowiki>` 之外创建备份目录，例如在 `$HOME/mariadb_backup`。
  2. 将问题文件从 `${DATADIR}/mysql/xxx.{frm,ibd}</nowiki>` 复制到备份目录。`xxx.ibd` 可能不存在。
  3. 在 `mariadb` 提示符下使用 _DROP TABLE mysql.xxx_ 删除表。
  4. 运行 _mariadb-check_ 。成功后，应重新创建 `xxx.frm` 和 `xxx.ibd` 文件。
  5. 如有必要，重新运行 _mariadb-upgrade_ 。您可能需要使用 _\--force_ 选项。

##  更多资源

  * [MariaDB 官方网站](<https://mariadb.org/>)
  * [MariaDB 知识库](<https://mariadb.com/kb/en/>)
  * [MySQL 性能调优脚本与技巧](<https://www.askapache.com/mysql/performance-tuning-mysql/>)
