相关文章

  * [PhpPgAdmin](<../zh-cn/PhpPgAdmin.html> "PhpPgAdmin")

**翻译状态：**

  * 本文（或部分内容）译自 [PostgreSQL](<https://wiki.archlinux.org/title/PostgreSQL> "arch:PostgreSQL")，最近一次同步于 2025-08-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/PostgreSQL?diff=0&oldid=834074>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PostgreSQL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

PostgreSQL是一个开源的，社区驱动的，符合标准的 对象-关系型 数据库系统。 

##  安装

**警告：** 在升级到新版本的 PostgreSQL 包前，请先查看 [#升级 PostgreSQL](<#%E5%8D%87%E7%BA%A7_PostgreSQL>) 一节中的必要步骤。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [postgresql](<https://archlinux.org/packages/?name=postgresql>)包 包。这同时会创建一个名为 _postgres_ 的系统用户。 

你现在可以通过[提权工具](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%AE%89%E5%85%A8.html#%E6%8F%90%E6%9D%83> "应用程序列表/安全")来切换到 _postgres_ 用户下。 

##  初始化配置

在 PostgreSQL 可以正常使用之前，数据库集群必须被初始化： 
    
    [postgres]$ initdb -D /var/lib/postgres/data
    
其中 `-D` 提供了数据库集群的默认数据存放位置（如果需要修改目录位置，可以参考[#修改默认数据目录](<#%E4%BF%AE%E6%94%B9%E9%BB%98%E8%AE%A4%E6%95%B0%E6%8D%AE%E7%9B%AE%E5%BD%95>)）。`initdb` 也支持多种其它的命令行参数： 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** PostgreSQL 还支持 ICU 区域设置。[[1]](<https://www.postgresql.org/docs/current/locale.html#id-1.6.11.3.7>) (在 [Talk:PostgreSQL](<../zh-cn/Talk:PostgreSQL.html>) 中讨论)

  * 默认情况下，[数据库集群的区域设置和编码](<https://www.postgresql.org/docs/current/static/locale.html>)是从当前环境中派生的（使用 [$LANG](<../zh-cn/Locale.html#LANG:_default_locale> "Locale") 值）。如果这不是你想要的，你可以使用 `--locale=_locale_`（其中 _locale_ 是从系统的[可用区域设置](<../zh-cn/Locale.html#Generating_locales> "Locale")中选择的）和 `--encoding=_encoding_`（必须与选择的区域设置匹配）来覆盖默认值。（一旦数据库启动，你可以使用 `[postgres]$ psql -l` 检查使用了哪些值。）

**注意：** 使用除 `C.UTF-8`、`C`、`POSIX` 或 `ucs_basic` 以外的区域设置可能会导致 排序规则版本不匹配，如果提供区域设置的库（[glibc](<https://archlinux.org/packages/?name=glibc>)包 或 [icu](<https://archlinux.org/packages/?name=icu>)包）更新，则需要重新索引。

  * 如果数据目录所在的文件系统没有数据校验和功能，你可能会想要启用 PostgreSQL 自带的[校验和](<https://www.postgresql.org/docs/current/checksums.html>)功能来提高数据完整性保障 - 使用 `--data-checksums` 参数即可。相关细节可参考 [#Enable data checksumming](<#Enable_data_checksumming>)。（一旦数据库启动，你可以使用 `[postgres]$ psql --tuples-only -c "SHOW data_checksums"` 检查是否启用了该功能。）

**注意：**`/var/lib/postgres/data/` 目录设置了 `C`（`No_COW`）[file attribute](</wzh/index.php?title=File_attribute&action=edit&redlink=1> "File attribute（页面不存在）")。[[2]](<https://gitlab.archlinux.org/archlinux/packaging/packages/postgresql/-/blob/main/postgresql.tmpfiles#L3>) 这会在 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 中 [禁用校验和](<https://unix.stackexchange.com/a/316797>)。

  * 默认使用 _trust_ 认证方法，这意味着主机上的任何人都可以以任何数据库用户身份连接。你可以使用 `--auth-local=peer --auth-host=scram-sha-256` 来使用更安全的认证方法。
  * `-c`/`--set` 选项可用于设置任何 `postgresql.conf` 参数，避免手动编辑 `postgresql.conf` 的需要。
  * 更多选项，请参阅 `initdb --help` 和[官方文档](<https://www.postgresql.org/docs/current/creating-cluster.html>)。

示例： 
    
    [postgres]$ initdb --locale=C.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data --data-checksums
    
屏幕上应该会出现许多行，其中几行以 `... ok` 结尾： 
    
    The files belonging to this database system will be owned by user "postgres".
    This user must also own the server process.
    
    The database cluster will be initialized with locale "C.UTF-8".
    The default text search configuration will be set to "english".
    
    Data page checksums are enabled.
    
    creating directory /var/lib/postgres/data ... ok
    creating subdirectories ... ok
    selecting dynamic shared memory implementation ... posix
    selecting default max_connections ... 100
    selecting default shared_buffers ... 128MB
    selecting default time zone ... UTC
    creating configuration files ... ok
    running bootstrap script ... ok
    performing post-bootstrap initialization ... ok
    syncing data to disk ... ok
    
    initdb: warning: enabling "trust" authentication for local connections
    initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
    
    Success. You can now start the database server using:
    
        pg_ctl -D /var/lib/postgres/data -l logfile start
    
如果你看到的是这些行，那么初始化过程成功了。使用 `exit` 返回到普通用户。 

**警告：**

  * 欲了解更多 _initdb_ 警告，请参阅 [#默认限制数据库超级用户的访问权限](<#%E9%BB%98%E8%AE%A4%E9%99%90%E5%88%B6%E6%95%B0%E6%8D%AE%E5%BA%93%E8%B6%85%E7%BA%A7%E7%94%A8%E6%88%B7%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90>)。
  * 如果数据库位于 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 文件系统上，你应该在创建数据库前禁用数据库目录的 [写时复制](<../zh-cn/Btrfs.html#%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6_\(CoW\)> "Btrfs")。
  * 如果数据库位于 [ZFS](<../zh-cn/ZFS.html> "ZFS") 文件系统上，你应该在创建数据库前先查阅 [ZFS#Databases](<../zh-cn/ZFS.html#Databases> "ZFS")。

**提示：** 如果你将根目录更改为 `/var/lib/postgres` 以外的路径，你将需要 [编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") 服务文件。如果根目录在 `home` 下，请确保将 `ProtectHome` 设置为 false。

最后，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `postgresql.service` 服务。 

##  创建第一个数据库/用户

**提示：** 如果你创建一个与你的 Linux 用户名相同的 PostgreSQL 角色/用户，它将允许你在访问 PostgreSQL 数据库 shell 时无需指定登录用户（这非常方便）。

以 postgres 用户身份，使用 [createuser](<https://www.postgresql.org/docs/current/static/app-createuser.html>) 命令添加一个新的数据库角色/用户： 
    
    [postgres]$ createuser --interactive
    
使用 [createdb](<https://www.postgresql.org/docs/current/static/app-createdb.html>) 命令，创建一个上述用户可以读写的新数据库（如果数据库用户与你的 Linux 用户名相同，请从你的登录 shell 执行此命令，否则请在以下命令中添加 `-O _database-username_`）： 
    
    $ createdb myDatabaseName
    
**提示：** 如果你没有授予新用户数据库创建权限，请在上述命令中添加 `-U postgres`。

##  熟悉 PostgreSQL

###  连接数据库 shell

以 postgres 用户身份登录。启动主数据库 shell [psql](<https://www.postgresql.org/docs/current/static/app-psql.html>)，在这里你可以创建/删除数据库和表、配置权限以及运行原始 SQL 命令。使用 `-d` 选项连接到你创建的数据库（如果不指定数据库，`psql` 会尝试连接与你用户名同名的数据库）。 
    
    [postgres]$ psql -d _myDatabaseName_
    
一些有用的命令： 

  * 获取帮助

    => \help
    
  * 列出所有数据库

    => \l
    
  * 连接到特定数据库

    => \c _database_
    
  * 列出所有用户以及他们的权限

    => \du
    
  * 展示当前数据库中所有的表相关的汇总信息

    => \dt
    
  * 退出 `psql`

    => \q 或是 Ctrl+d
    
当然也有更多元命令，但这些应该能够帮助您开始。要查看所有元命令： 
    
    => \?
    
##  可选配置

PostgreSQL 数据库服务器的配置文件是 `postgresql.conf`。该文件位于服务器的数据目录中，通常为 `/var/lib/postgres/data`。该目录还包含其他主要配置文件，包括定义认证设置的 `pg_hba.conf`，适用于[本地用户](<#%E9%BB%98%E8%AE%A4%E9%99%90%E5%88%B6%E6%95%B0%E6%8D%AE%E5%BA%93%E8%B6%85%E7%BA%A7%E7%94%A8%E6%88%B7%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90>)和[其他主机用户](<#%E9%85%8D%E7%BD%AE_PostgreSQL_%E4%BB%A5%E5%85%81%E8%AE%B8%E8%BF%9C%E7%A8%8B%E4%B8%BB%E6%9C%BA%E8%AE%BF%E9%97%AE>)。 

**注意：** 默认情况下，普通用户无法浏览或搜索此目录。这就是为什么 `find` 和 `locate` 无法找到配置文件的原因。

###  默认限制数据库超级用户的访问权限

默认情况下，`pg_hba.conf` 允许任何本地用户以任何数据库用户身份连接，包括数据库超级用户。 这可能不是您想要的，因此为了限制对 _postgres_ 用户的全局访问，请更改以下行： 
    
    /var/lib/postgres/data/pg_hba.conf
    
    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    
    # "local" 仅用于 Unix 域套接字连接
    local   all             all                                     trust

改为： 
    
    /var/lib/postgres/data/pg_hba.conf
    
    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    
    # "local" 仅用于 Unix 域套接字连接
    local   all             postgres                                peer

您可以根据需要或软件要求稍后添加其他行。 

###  要求登录密码

编辑 `/var/lib/postgres/data/pg_hba.conf` 并将每个用户（或 `all` 以影响所有用户）的认证方法设置为 `scram-sha-256`： 
    
    /var/lib/postgres/data/pg_hba.conf
    
    # TYPE  DATABASE        USER            ADDRESS                 METHOD 
    
    # "local" 仅用于 Unix 域套接字连接
    local   all             _user_                                    scram-sha-256

**注意：** 更改 `pg_hba.conf` 中的认证方法不会更新数据库中存储的哈希密码 [[3]](<https://stackoverflow.com/a/64317399>)。要从 `md5` 迁移到 `scram-sha-256`，您需要为每个数据库用户设置新密码。

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `postgresql.service`，然后使用 `ALTER USER _user_ WITH ENCRYPTED PASSWORD '_password_ ';` 重新添加每个用户的密码。 

###  配置 PostgreSQL 仅通过 UNIX 套接字访问

在[最初创建集群](<#%E5%88%9D%E5%A7%8B%E5%8C%96%E9%85%8D%E7%BD%AE>)时，将 `-c listen_addresses=''` 附加到 _initdb_ 命令中。 

对于现有集群，编辑 `postgresql.conf` 并在连接和认证部分设置： 
    
    /var/lib/postgres/data/postgresql.conf
    
    listen_addresses = ''

这将完全禁用网络监听。 之后，您应该[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `postgresql.service` 以使更改生效。 

###  配置 PostgreSQL 以允许远程主机访问

在连接和认证部分，根据需要设置 `listen_addresses` 行： 
    
    /var/lib/postgres/data/postgresql.conf
    
    listen_addresses = 'localhost,_my_local_ip_address'_

您可以使用 `'*'` 来监听所有可用地址。 

**注意：** PostgreSQL 默认使用 TCP 端口 `5432` 进行远程连接。确保此端口在您的[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")中打开并能够接收传入连接。您也可以在配置文件中更改此端口，位于 `listen_addresses` 下方。

然后在认证配置中添加如下行： 
    
    /var/lib/postgres/data/pg_hba.conf
    
    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    # IPv4 本地连接：
    host    all             all             _ip_address_ /32           scram-sha-256

其中 `_ip_address_` 是远程客户端的 IP 地址。 

请参阅 [pg_hba.conf](<https://www.postgresql.org/docs/current/static/auth-pg-hba-conf.html>) 的文档。 

**注意：**

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** [官方文档](<https://www.postgresql.org/docs/current/auth-password.html>)指出 `md5` 使用挑战-响应认证，这"防止了密码嗅探"。也许不应将其视为与明文发送密码一样不安全。（在 [Talk:PostgreSQL](<../zh-cn/Talk:PostgreSQL.html>) 中讨论）

如果未通过 SSL 安全连接发送，无论是发送明文密码还是 md5 哈希值都不安全。请参阅 [使用 SSL 保护 TCP/IP 连接](<https://www.postgresql.org/docs/current/static/ssl-tcp.html>) 以了解如何配置 PostgreSQL 使用 SSL。

之后，您应该[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `postgresql.service` 以使更改生效。 

要进行故障排除，请查看服务器日志文件： 
    
    # journalctl -u postgresql.service
    
###  配置 PostgreSQL 使用 PAM 认证

PostgreSQL 提供了多种认证方法。如果您希望允许用户使用其系统密码进行认证，则需要执行额外的步骤。首先，您需要为连接启用 [PAM](<../zh-cn/PAM.html> "PAM")。 

例如，与上述相同的配置，但启用了 PAM： 
    
    /var/lib/postgres/data/pg_hba.conf
    
    # IPv4 本地连接：
    host   all   all   _my_remote_client_ip_address_ /32   pam

然而，PostgreSQL 服务器在没有 root 权限的情况下运行，无法访问 `/etc/shadow`。我们可以通过允许 postgres 组访问此文件来解决此问题： 
    
    # setfacl -m g:postgres:r /etc/shadow
    
###  修改默认数据目录

默认设置下，新创建的数据库会被存放于 `/var/lib/postgres/data` 目录下。如果要更改目录位置，可以参考下列步骤： 

创建一个新文件夹，并将其所有者设为 postgres 用户： 
    
    # mkdir -p /pathto/pgroot/data
    # chown -R postgres:postgres /pathto/pgroot
    
切换到 postgres 用户，然后初始化新集群： 
    
    [postgres]$ initdb -D /pathto/pgroot/data
    
通过[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `postgresql.service` 来[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")，以覆盖 `Environment` 和 `PIDFile` 设置。例如： 
    
    /etc/systemd/system/postgresql.service.d/PGROOT.conf
    
    [Service]
    Environment=PGROOT=_/pathto/pgroot_
    PIDFile=_/pathto/pgroot/_ data/postmaster.pid

如果您想使用 `/home` 目录作为默认目录或用于表空间，需要在此文件中额外添加一行： 
    
    ProtectHome=false
    
###  将新数据库的默认编码更改为 UTF-8

**注意：** 如果您在运行 `initdb` 时使用了 `-E UTF8` 或在使用 UTF-8 区域设置时，这些步骤不是必需的。

在创建新数据库时（例如使用 `createdb blog`），PostgreSQL 实际上会复制一个模板数据库。有两个预定义的模板：`template0` 是原始的，而 `template1` 是供管理员更改的现场模板，默认情况下使用。要更改新数据库的编码，其中一个选项是更改现场 `template1`。为此，登录到 PostgreSQL shell（`psql`）并执行以下操作： 

首先，我们需要删除 `template1`。模板无法直接删除，因此我们首先将其修改为普通数据库： 
    
    UPDATE pg_database SET datistemplate = FALSE WHERE datname = 'template1';
    
现在我们可以删除它： 
    
    DROP DATABASE template1;
    
下一步是从 `template0` 创建一个新数据库，并使用新的默认编码： 
    
    CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UNICODE';
    
现在将 `template1` 修改为实际模板： 
    
    UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template1';
    
可选地，如果您不希望任何人连接到此模板，请将 `datallowconn` 设置为 `FALSE`： 
    
    UPDATE pg_database SET datallowconn = FALSE WHERE datname = 'template1';
    
**注意：** 最后一步在使用 `pg_upgrade` 升级时可能会产生问题。

现在您可以创建一个新数据库： 
    
    [postgres]$ createdb blog
    
如果您重新登录到 `psql` 并检查数据库，您应该看到新数据库的正确编码： 
    
    \l
    
                                  List of databases
      Name    |  Owner   | Encoding  | Collation | Ctype |   Access privileges
    -----------+----------+-----------+-----------+-------+----------------------
    blog      | postgres | UTF8      | C         | C     |
    postgres  | postgres | SQL_ASCII | C         | C     |
    template0 | postgres | SQL_ASCII | C         | C     | =c/postgres
                                                         : postgres=CTc/postgres
    template1 | postgres | UTF8      | C         | C     |
    
###  启用数据校验和

如果您的数据库文件位于没有校验和的文件系统上，其数据可能会因位衰减和硬件故障而遭受静默数据损坏。虽然这些事件很少见，但如果您关心数据完整性，您可能希望启用 [PostgreSQL 的内置数据校验和](<https://www.postgresql.org/docs/current/checksums.html>)。此功能必须在集群级别启用，而不是按数据库或按表启用。 

**注意：** 此功能有一些注意事项： 

  * 存在 [最小的性能影响](<https://web.archive.org/web/20170218093959/https://blog.endpoint.com/2015/12/postgres-checksum-performance-impact.html>)，尤其是在从磁盘读取大型数据集时。内存操作不受影响。
  * PostgreSQL 无法修复损坏的数据 - 它只会中止从损坏页面读取的事务，以防止进一步的损坏或无效的执行结果。
  * 校验和仅覆盖磁盘数据（行）页面，不包括元数据或控制结构。内存页面不进行校验和。纠错存储和 ECC 内存仍然有益。

  * 要在集群创建期间启用校验和，请将 `--data-checksums` 参数添加到 `initdb`。
  * 要验证是否启用了校验和，请运行 `[postgres]$ psql --tuples-only -c "SHOW data_checksums"`（应打印 `off` 或 `on`）。
  * 要在现有集群上切换校验和：

  1. [停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `postgresql.service`。
  2. 运行 `[postgres]$ pg_checksums --pgdata /var/lib/postgres/data --enable`（或 `--disable` 如果您不再需要校验和）。启用校验和将重写所有数据库页面，对于大型数据库实例，这将需要一些时间。
  3. [启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `postgresql.service`。

##  图形化管理工具

  * **[phpPgAdmin](<../zh-cn/PhpPgAdmin.html> "PhpPgAdmin")** — 基于 Web 的 PostgreSQL 管理工具。

     <https://github.com/phppgadmin/phppgadmin> || [phppgadmin](<https://aur.archlinux.org/packages/phppgadmin/>)AUR

  * **pgAdmin-desktop** — pgAdmin 的桌面用户界面，一个全面的 PostgreSQL 设计和管理的图形用户界面。

     <https://www.pgadmin.org/> || [pgadmin4-desktop](<https://aur.archlinux.org/packages/pgadmin4-desktop/>)AUR

  * **pgAdmin** — 全面的 PostgreSQL 设计和管理图形用户界面。

     <https://www.pgadmin.org/> || [pgadmin4](<https://archlinux.org/packages/?name=pgadmin4>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

  * **pgModeler** — PostgreSQL 的图形化模式设计工具。

     <https://pgmodeler.io/> || [pgmodeler](<https://aur.archlinux.org/packages/pgmodeler/>)AUR

  * **Postbird** — 跨平台的 PostgreSQL 图形用户界面客户端，使用 JavaScript 编写，基于 Electron 运行。

     <https://github.com/paxa/postbird> || [postbird-bin](<https://aur.archlinux.org/packages/postbird-bin/>)AUR

  * **rainfrog** — Postgres 的数据库管理 TUI。

     <https://github.com/achristmascarl/rainfrog> || [rainfrog](<https://archlinux.org/packages/?name=rainfrog>)包

  * **pgweb** — 跨平台的 PostgreSQL 数据库 Web 客户端。

     <https://sosedoff.github.io/pgweb> || [pgweb-bin](<https://aur.archlinux.org/packages/pgweb-bin/>)AUR

支持多种数据库管理系统的工具，请参见 [List of applications/Documents#Database tools](<../zh-cn/List_of_applications/Documents.html#Database_tools> "List of applications/Documents")。 

##  设置备份

建议为包含重要数据的数据库设置备份。请参阅 PostgreSQL 文档中的 [备份与恢复](<https://www.postgresql.org/docs/current/backup.html>) 章节。PostgreSQL 维基中还有一个 [备份工具列表](<https://wiki.postgresql.org/wiki/Ecosystem:Backup>)，尽管它可能不是最新的或完整的。请记住，除非您定期执行测试恢复，否则不能信任备份系统！ 

##  升级 PostgreSQL

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** How to upgrade when using third party extensions? (在 [Talk:PostgreSQL#pg_upgrade problem if extensions (like postgis) are used](</wzh/index.php?title=Talk:PostgreSQL&action=edit&redlink=1> "Talk:PostgreSQL（页面不存在）") 中讨论)

升级 PostgreSQL 大版本（例如从 14.x 升级到 15.y）需要一些额外的维护工作。 

**注意：** 应遵循 PostgreSQL 官方的 [升级文档](<https://www.postgresql.org/docs/current/static/upgrading.html>)。

**警告：** 以下指令可能导致数据丢失。不要盲目运行下面的命令，确保你理解它们在做什么。[请先备份](<#%E8%AE%BE%E7%BD%AE%E5%A4%87%E4%BB%BD>)。

通过以下命令获取当前使用的数据库版本： 
    
    # cat /var/lib/postgres/data/PG_VERSION
    
为了避免意外升级到不兼容的数据库版本，建议 [跳过更新](<../zh-cn/Pacman.html#%E5%9C%A8%E5%8D%87%E7%BA%A7%E6%97%B6%E8%B7%B3%E8%BF%87%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman") PostgreSQL 包。 

小版本升级是安全的。然而，如果你意外升级到一个不同的大版本，你可能无法访问任何数据。请务必查看 [PostgreSQL 主页](<https://www.postgresql.org/>) 以确认每个升级所需的步骤。有关为什么会出现这种情况的更多信息，请参阅 [版本策略](<https://www.postgresql.org/support/versioning>)。 

**注意：** 如果你使用了扩展，请查看 [#PostgreSQL database unable to start after package update when using extensions](<#PostgreSQL_database_unable_to_start_after_package_update_when_using_extensions>) 和 [#Failing to start a PostgreSQL server with the older version of the database while upgrading to the newer version with extensions](<#Failing_to_start_a_PostgreSQL_server_with_the_older_version_of_the_database_while_upgrading_to_the_newer_version_with_extensions>)。

有两种主要的方法可以升级你的 PostgreSQL 数据库。请阅读官方文档以获取详细信息。 

### pg_upgrade

`pg_upgrade` 工具尝试在集群之间复制尽可能多的兼容数据，并升级其他所有内容。尽管它需要访问源和目标 PostgreSQL 版本的二进制文件，但它通常是升级大多数实例的最快方法。请阅读 [pg_upgrade(1)](<https://man.archlinux.org/man/pg_upgrade.1>) 手册页以了解它执行的操作。对于非平凡的实例（例如带有流复制或日志传送的实例），请先阅读 [上游文档](<https://www.postgresql.org/docs/current/pgupgrade.html>)。 

对于希望使用 `pg_upgrade` 的用户，有一个 [postgresql-old-upgrade](<https://archlinux.org/packages/?name=postgresql-old-upgrade>)包 包，它将始终运行比实际 PostgreSQL 包低一个主要版本的版本。这可以与新版本的 PostgreSQL 一起安装。要从旧版本的 PostgreSQL 升级，可以使用 AUR 包，例如 [postgresql-12-upgrade](<https://aur.archlinux.org/packages/postgresql-12-upgrade/>)AUR。（你必须使用与你升级到的 PostgreSQL 版本打包的 `pg_upgrade` 版本。） 

请注意，数据库集群目录不会随版本变化而变化，因此在运行 `pg_upgrade` 之前，有必要重命名现有的数据目录并迁移到一个新目录。必须使用与旧集群相同的参数初始化新的数据库集群。 

当你准备好开始升级时： 

  1. 当旧数据库集群仍在运行时，收集用于创建它的 `initdb` 参数。请参阅 [#初始化配置](<#%E5%88%9D%E5%A7%8B%E5%8C%96%E9%85%8D%E7%BD%AE>) 以获取更多信息。
  2. [停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop") `postgresql.service`。检查 [单元状态](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "单元状态") 以 **确保 PostgreSQL 已正确停止** 。如果停止失败，`pg_upgrade` 将失败并显示 `The source cluster was not shut down cleanly`。
  3. [升级](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E6%9B%B4%E6%96%B0%E7%B3%BB%E7%BB%9F> "升级") [postgresql](<https://archlinux.org/packages/?name=postgresql>)包, [postgresql-libs](<https://archlinux.org/packages/?name=postgresql-libs>)包, 和 [postgresql-old-upgrade](<https://archlinux.org/packages/?name=postgresql-old-upgrade>)包。
  4. 确保 `/var/lib/postgres/olddata` 不存在。如果你在上次升级后没有删除它，请现在删除。
  5. 重命名旧集群目录，然后创建一个新的集群和临时工作目录：
         
         # mv /var/lib/postgres/data /var/lib/postgres/olddata
         # mkdir /var/lib/postgres/data /var/lib/postgres/tmp
         # chown postgres:postgres /var/lib/postgres/data /var/lib/postgres/tmp
         [postgres]$ cd /var/lib/postgres/tmp
         
  6. 使用与旧集群相同的 `initdb` 参数初始化新集群：
         
         [postgres]$ initdb -D /var/lib/postgres/data --locale=C.UTF-8 --encoding=UTF8 --data-checksums

  7. 升级集群，将下面的 `_PG_VERSION_` 替换为旧的 PostgreSQL 版本号（例如 `15`）：
         
         [postgres]$ pg_upgrade -b /opt/pgsql-_PG_VERSION_ /bin -B /usr/bin -d /var/lib/postgres/olddata -D /var/lib/postgres/data

**提示：** 在支持 reflinks 的文件系统（例如 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 和 [XFS](<../zh-cn/XFS.html> "XFS")）上，可以附加 `--clone` 选项以加快文件复制速度。

如有必要，调整新集群的配置文件（例如 `pg_hba.conf` 和 `postgresql.conf`）以匹配旧集群。
  8. 再次[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")`postgresql.service` 。
  9. **可选：** 运行 `[postgres]$ vacuumdb --all --analyze-in-stages` 以重新计算查询分析器统计信息，这 [应该会在升级后不久提高查询性能](<https://www.cybertec-postgresql.com/en/postgresql-analyze-and-optimizer-statistics/>)。（添加 `--jobs=_NUMBER_OF_CPU_CORES_` 参数可能会提高此命令的性能。）
  10. **可选：** 备份 `/var/lib/postgres/olddata` 目录，以防你需要恢复之前的 PostgreSQL 版本。
  11. 删除包含旧集群数据的 `/var/lib/postgres/olddata` 目录。
  12. 删除 `/var/lib/postgres/tmp` 目录。
  13. 如果你使用 [pgbackrest](<https://archlinux.org/packages/?name=pgbackrest>)包，请运行 [stanza-upgrade](<https://pgbackrest.org/command.html#command-stanza-upgrade>) 命令。

###  手动转储和重新加载

你也可以这样做（在升级并安装 [postgresql-old-upgrade](<https://archlinux.org/packages/?name=postgresql-old-upgrade>)包 之后）。 

**注意：**

  * 以下是升级自 PostgreSQL 14 的命令。你可以在 `/opt/` 中找到适用于你 PostgreSQL 集群版本的类似命令，前提是你安装了相应版本的 [postgresql-old-upgrade](<https://archlinux.org/packages/?name=postgresql-old-upgrade>)包 包。
  * 如果你自定义了 `pg_hba.conf` 文件，你可能需要临时修改它以允许从本地系统完全访问旧数据库集群。升级完成后，将你的自定义设置应用到新数据库集群并 [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `postgresql.service`。

[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop") `postgresql.service`
    
    # mv /var/lib/postgres/data /var/lib/postgres/olddata
    # mkdir /var/lib/postgres/data
    # chown postgres:postgres /var/lib/postgres/data
    [postgres]$ initdb -D /var/lib/postgres/data --locale=C.UTF-8 --encoding=UTF8 --data-checksums
    [postgres]$ /opt/pgsql-14/bin/pg_ctl -D /var/lib/postgres/olddata/ start
    # cp /usr/lib/postgresql/postgis-3.so /opt/pgsql-14/lib/ # 仅当安装了 postgis 时
    [postgres]$ pg_dumpall -h /tmp -f /tmp/old_backup.sql
    [postgres]$ /opt/pgsql-14/bin/pg_ctl -D /var/lib/postgres/olddata/ stop
    
[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `postgresql.service`
    
    [postgres]$ psql -f /tmp/old_backup.sql postgres
    
##  故障排除

###  提高小事务的性能

如果你在本地机器上使用 PostgresSQL 进行开发，并且感觉速度较慢，可以尝试在配置中关闭 [synchronous_commit](<https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-SYNCHRONOUS-COMMIT>)。但请注意 [注意事项](<https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-SYNCHRONOUS-COMMIT>)。 

**警告：** 这是一个非常粗糙的解决方案，可能会破坏数据库或导致数据丢失，因此请务必备份。

###  使用扩展时包更新后 PostgreSQL 数据库无法启动

这种情况通常是因为现有扩展包没有针对新版本编译（尽管扩展包本身可能是最新的），解决方案是[重新构建](</wzh/index.php?title=Arch_build_system&action=edit&redlink=1> "Arch build system（页面不存在）")扩展包，可以手动操作或等待扩展包更新。 

###  升级带有扩展的数据库版本时无法启动旧版本 PostgreSQL 服务器

这是因为 [postgresql-old-upgrade](<https://archlinux.org/packages/?name=postgresql-old-upgrade>)包 提供的旧版本 postgres 在其 lib 目录中没有所需的扩展（ _.so_ 文件）。目前的解决方案比较粗糙，可能会引发很多问题，因此请务必先备份数据库。基本思路是将所需的扩展 _.so_ 文件从 `/usr/lib/postgresql/` 复制到 `/opt/pgsql-_XX_ /lib/`（记得将 XX 替换为 [postgresql-old-upgrade](<https://archlinux.org/packages/?name=postgresql-old-upgrade>)包 的主版本号）。 

例如，对于 timescaledb： 
    
    # cp /usr/lib/postgresql/timescaledb*.so /opt/pgsql-13/lib/
    
**警告：** 虽然复制 _.so_ 文件对我来说已经足够，但可能需要将更多文件复制到 `/opt/pgsql-_XX_ /` 下的正确目录中。

要了解需要复制的确切文件，可以使用以下命令检查扩展包的内容： 
    
    $ pacman -Ql _package_name_
    
**警告：** 这是一个非常粗糙的解决方案，可能会破坏数据库或导致数据丢失，因此请务必备份。

###  警告：数据库 "postgres" 的排序规则版本不匹配

你可能会看到类似这样的信息： 
    
    WARNING:  database "postgres" has a collation version mismatch
    DETAIL:  The database was created using collation version X.YY, but the operating system provides version X.ZZ.
    HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE postgres REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
    
这意味着排序规则提供库（[glibc](<https://archlinux.org/packages/?name=glibc>)包 或 [icu](<https://archlinux.org/packages/?name=icu>)包）已更新，可能使某些索引失效。因此需要重新索引这些数据库。 

可以通过以下命令操作： 
    
    [postgres]$ psql -c 'REINDEX DATABASE' postgres
    [postgres]$ psql -c 'ALTER DATABASE postgres REFRESH COLLATION VERSION'
    
对于其他数据库，只需将上述命令中的 _postgres_ 替换为相应的数据库名称并重复执行。

**提示：** 使用 `C.UTF-8`、`C`、`POSIX` 或 `ucs_basic` 区域设置创建数据库集群可以避免此问题。
