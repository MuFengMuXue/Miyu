相关文章

  * [Apache HTTP 服务器](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Apache HTTP 服务器")
  * [Nginx](<../zh-cn/Nginx.html> "Nginx")
  * [OpenSSL](<../zh-cn/OpenSSL.html> "OpenSSL")
  * [WebDAV](<../zh-cn/WebDAV.html> "WebDAV")

**翻译状态：**

  * 本文（或部分内容）译自 [Nextcloud](<https://wiki.archlinux.org/title/Nextcloud> "arch:Nextcloud")，最近一次同步于 2024-11-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Nextcloud?diff=0&oldid=819822>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Nextcloud_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

根据 [Wikipedia:Nextcloud](<https://en.wikipedia.org/wiki/Nextcloud> "wikipedia:Nextcloud"): 

Nextcloud 是一套客户机——服务器软件（依赖被称为 apps 的组件），能够实现诸如共享，协作以及沟通的需要,比如： 

  * 文件共享
  * 个人信息管理（[contacts](<https://apps.nextcloud.com/apps/contacts>),[calendar](<https://apps.nextcloud.com/apps/calendar>),[tasks](<https://apps.nextcloud.com/apps/tasks>))
  * 通讯（[mail](<https://apps.nextcloud.com/apps/mail>),[chat,video conferencing](<https://apps.nextcloud.com/apps/spreed>))
  * 合作编辑([text](<https://github.com/nextcloud/text>),Office integration)

Nextcloud 是开源的，并且它基于开放标准。数据主权是 Nextcloud 的一大优势，也就是说，你可以部署自己的 Nextcloud 实例来摆脱诸如 Dropbox、Office365 和 Google Drive 等专有（甚至不可信）的服务的束缚。 

Nextcloud可以按照你的需求部署在小至单板计算机（比如树莓派），大到有数百万用户的超大型数据中心中。Nextcloud 具有一套精心设计的授权方案以及可选的联邦方案（用于连接多个独立的实例），所以 Nextcloud 同样非常适合在企业环境下部署。 

Nextcloud 是 [ownCloud](<https://owncloud.com/>)的分支，有关其历史，请参看其[Wikipedia 页面](<https://en.wikipedia.org/wiki/Nextcloud#History> "w:Nextcloud")。 

##  安装概览

完全安装的 Nextcloud 应当（至少）包含以下组件： 

一个**web 服务器** ；与之配套的**应用服务器** ，用来运行 **Nextcloud** （即 PHP 代码）；一个供 Nextcloud 使用的**数据库** 。 

这篇文章将会讲解使用 [MariaDB](<../zh-cn/MariaDB.html> "MariaDB")/MySQL 或 [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL") 作为数据库和以下 web 服务器与应用服务器的组合： 

  * Nginx->uWSGI(plus uwsgi-plugin-php)

  * Nginx->FPM
  * Apache HTTP server(using mod_proxy_usgi)->uWSGI(plus uwsgi-plugin-php)
  * Apache HTTP server(using mod_proxy_fcgi)->FPM

Nextcloud 包符合 [Web 应用包指导规范](<https://wiki.archlinux.org/title/Web_application_package_guidelines> "en:Web application package guidelines")。它要求 Web 应用程序应当由专门的用户运行——在本例中为 `nextcloud`。这就是为什么要使用应用服务器。出于相同的理由，使用 [php-apache](<https://archlinux.org/packages/?name=php-apache>)直接在 Apache 中执行 Nextcloud 的 PHP 代码也是不可能的。 

##  安装

**注意：**[nextcloud](<https://archlinux.org/packages/?name=nextcloud>)包 提供了基于 [php](<https://archlinux.org/packages/?name=php>)包 或基于 [php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包 的安装（依赖元软件包 php-interpreter）。本文强烈建议使用 [php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包 包安装以保证安全（也能让你高枕无忧）。详情请看[迁移到 php-legacy](<https://wiki.archlinux.org/title/Nextcloud#Migrating_to_php-legacy> "arch:Nextcloud")。本文假定您使用了 [php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包 进行安装。

安装 [nextcloud](<https://archlinux.org/packages/?name=nextcloud>)包。当被问及时，选择 [php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包 作为你的php版本，这会拉取相当多的依赖。大多数[必要的 PHP 扩展](<https://docs.nextcloud.com/server/stable/admin_manual/installation/php_configuration.html>)都将以这种方式进行处理。此外，你必须安装 [php-legacy-gd](<https://archlinux.org/packages/?name=php-legacy-gd>)包（最好是作为依赖包安装，利用 pacman 的`--asdeps`选项实现）。 

同时建议你安装下面的软件包（同样使用`--asdeps`选项）： 

  * [php-legacy-sodium](<https://archlinux.org/packages/?name=php-legacy-sodium>)包 用于argon2散列算法

  * [php-legacy-imagick](<https://archlinux.org/packages/?name=php-legacy-imagick>)包和[librsvg](<https://archlinux.org/packages/?name=librsvg>)包 用于生成预览

其他可选依赖将在后面介绍，具体内容取决于你的安装配置（比如：你选择了什么样的数据库）。 

请注意，[php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包 自带一部分模块（即 _bcmath、exif、gmp、intl和sysvsem_ ），这些模块不必显式安装。 

##  配置

### PHP

本指南不会修改 PHP 的主配置文件`/etc/php-legacy/php.ini`,Nextcloud的 PHP 配置会放在单独的地方，不干扰其它使用 PHP 的应用程序。这些文件被放在： 

  * 一份`php.ini`的副本，存放在`/etc/webapps/nextcloud`（用于`occ`命令行工具以及后台作业）。这是一份初始`php.ini`的完整复制，由[php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包提供，Nextcloud 将对其进行一些修改，以供使用。

  * 应用程序服务器的相关配置。将在应用程序服务器的部分介绍这些内容。

将`/etc/php-legacy/php.ini`复制到`/etc/webapps/nextcloud`(当然，最好是从 _php-legacy_ 的tarball中解压一份php.ini， _php-legacy_ 包存放在`/var/cache/pacman/pkg`）。然后，虽然不是绝对必须的，但请纪律性修改文件的所有权：
    
    # cp /etc/php-legacy/php.ini /etc/webapps/nextcloud
    # chown nextcloud:nextcloud /etc/webapps/nextcloud/php.ini

[Nextcloud文档](<https://docs.nextcloud.com/server/stable/admin_manual/installation/php_configuration.html>)中列出的大部分所需的PHP模块已经在刚刚复制的PHP配置文件中启用。但还需手动启用以下扩展： 
    
    /etc/webapps/nextcloud/php.ini
    
    extension=exif
    extension=gd
    extension=iconv
    extension=intl
    extension=sysvsem
    ; bcmath and gmp for passwordless login
    extension=bcmath
    extension=gmp
    ; sodium for the argon2 hashing algorithm
    extension=sodium
    ; in case you installed php-legacy-imagick (as recommended)
    extension=imagick

根据你准备使用的数据库，启用相应的`pdo_xxxx`模块。请参阅：[数据库](<#%E6%95%B0%E6%8D%AE%E5%BA%93>)。 

将`date.timezone`设置为你的首选时区，例如： 
    
    /etc/webapps/nextcloud/php.ini
    
    date.timezone = Asia/Shanghai

将PHP的内存限制放宽到至少512MiB： 
    
    /etc/webapps/nextcloud/php.ini
    
    memory_limit = 512M

为了提高安全性，你也可以配置`open_basedir`，但这不是必要的。这限制了 Nextcloud 的 PHP 代码可以读取和写入文件的位置。经过验证的设置是： 
    
    /etc/webapps/nextcloud/php.ini
    
    open_basedir=/var/lib/nextcloud:/tmp:/usr/share/webapps/nextcloud:/etc/webapps/nextcloud:/dev/urandom:/usr/lib/php-legacy/modules:/var/log/nextcloud:/proc/meminfo:/proc/cpuinfo

根据你安装的其他扩展，你可能需要扩充此列表，例如，如果你选择了[Redis](</wzh/index.php?title=Redis&action=edit&redlink=1> "Redis（页面不存在）")，则需要扩展 /`run/redis`。 

配置 _opcache_ 是不必要的，因为这份`php.ini`只用于`occ`命令行工具和后台作业，这二者并不经常运行PHP进程。 

### Nextcloud

将以下条目加入nextcloud的配置文件中： 
    
    /etc/webapps/nextcloud/config/config.php
    
    'trusted_domains' =>
      array (
        0 => 'localhost',
        1 => 'cloud.mysite.com',
      ),    
    'overwrite.cli.url' => '<https://cloud.mysite.com/'>,
    'htaccess.RewriteBase' => '/',

将示例的主机名 _`cloud.mysite.com`_ 修改成你的。如果你的Nextcloud需要通过子文件夹访问（比如`https://www.mysite.com/nextcloud`）`overwrite.cli.url` 和 `htaccess.RewriteBase` 必须做出相应更改。 

###  系统和环境

确保Nextcloud使用刚刚编辑的`php.ini`作为`occ`工具的配置文件，设置`NEXTCLOUD_PHP_CONFIG`环境变量：
    
    $ export NEXTCLOUD_PHP_CONFIG=/etc/webapps/nextcloud/php.ini

同时将其加入`.bashrc`（或`.bash_profile`）使其永久生效。出于隐私和安全方面的考量，请为会话数据创建专用目录：
    
    # install --owner=nextcloud --group=nextcloud --mode=700 -d /var/lib/nextcloud/sessions

网页应用的配置文件在 `/etc/webapps/nextcloud/config/config.php`。 

**注意：** Nextcloud 应当把用户数据存放在 `/var/lib/nextcloud/data/`，因为该目录只能被 root 和应用本身访问。要安装使用这个网页应用的软件，请使用 `/var/lib/nextcloud/apps/`。

###  数据目录

默认情况下，Nextcloud 将用户数据存放在 `/var/lib/nextcloud/data/`，这个位置可以调节： 
    
    /etc/webapps/nextcloud/config/config.php
    
    $CONFIG = [
    /* [..] */
    'datadirectory' => '/var/lib/nextcloud/data',
    /* [..] */
    ]

**注意：** `nextcloud` 用户需要有对 `datadirectory` 的写入权限。

###  可写应用目录

`nextcloud` 不可写入默认应用目录 `/usr/share/webapps/nextcloud/apps/`，因为它是软件包的一部分。 

要从应用商店安装应用，使用一个独立的、可写的目录是可以的。它默认指向 `/var/lib/nextcloud/apps/`，并可以通过一个在网页应用根目录下的符号链接 (`/usr/share/webapps/nextcloud/wapps`) 来访问。 

这个目录是可调整的: 
    
    /etc/webapps/nextcloud/config/config.php
    
    $CONFIG = [
    /* [..] */
    'apps_paths' => [
            [
                    'path'=> '/usr/share/webapps/nextcloud/apps',
                    'url' => '/apps',
                    'writable' => false,
            ],
            [
                    'path'=> '/var/lib/nextcloud/apps',
                    'url' => '/wapps',
                    'writable' => true,
            ],
    ],
    /* [..] */
    ]

**注意：**

  * 声明为 `writable` 的 `apps_paths` 条目需要可由 `nextcloud` 用户写入。此外，需要在 `/usr/share/webapps/nextcloud/` 中创建指向该目录的符号链接。
  * 上面的语法使用 PHP 的[短数组语法](<https://wiki.php.net/rfc/short_list_syntax>)。这可以用大多数指南使用的语法编写：

    /etc/webapps/nextcloud/config/config.php
    
    $CONFIG = (
    /* [..] */
      'apps_paths' => array (
            0 => array (
                    'path' => '/usr/share/webapps/nextcloud/apps',
                    'url' => '/apps',
                    'writable' => false,
            ),
            1 => array (
                    'path' => '/var/lib/nextcloud/apps',
                    'url' => '/wapps',
                    'writable' => true,
            ),
      ),
    /* [..] */
    )

###  日志目录

默认情况下，日志生成在 `/var/log/nextcloud/nextcloud.log`，这个位置是可以调整的： 
    
    /etc/webapps/nextcloud/config/config.php
    
    $CONFIG = [
    /* [..] */
    'logfile' => '/var/log/nextcloud/nextcloud.log',
    ]
    /* [..] */

##  数据库

[MariaDB](<../zh-cn/MariaDB.html> "MariaDB")/MySQL是Nextcloud的推荐选择。 

Nextcloud数据库的相关资料大都与MariaDB / MySQL有关。Nextcloud开发人员承认，他们[不太了解其它数据库的专业知识](<https://github.com/nextcloud/server/issues/5912#issuecomment-318568370%7C>)。 

[PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")据说可以提供比MariaDB/MySQL更好的性能，并且方言更少。[SQLite](<../zh-cn/SQLite.html> "SQLite")主要支持测试/开发安装，不建议用于生产环境。[受支持的数据库列表](<https://docs.nextcloud.com/server/stable/admin_manual/configuration_database/linux_database_configuration.html>)中还包括了Oracle database，但本指南不对其作介绍。 

###  MariaDB / MySQL

自从2013年以来，[MariaDB](<../zh-cn/MariaDB.html> "MariaDB")一直作为Arch Linux中的MySQL默认实现。 

如果你想在安装Nextcloud的主机上同时运行数据库，请配置并启动MariaDB（如果你尚未这样做）。请查看[此文档](<https://wiki.archlinux.org/title/MariaDB> "en:MariaDB")获得更多信息。不要忘记使用`mariadb-install-db`命令初始化MariaDB。为了提高安全性，建议[将MariaDB配置为仅侦听本地Unix套接字](<../zh-cn/MariaDB.html#%E5%90%AF%E7%94%A8%E4%BB%85%E9%80%9A%E8%BF%87_Unix_%E5%A5%97%E6%8E%A5%E5%AD%97%E5%9C%A8%E6%9C%AC%E5%9C%B0%E5%90%AF%E7%94%A8%E8%AE%BF%E9%97%AE> "MariaDB")： 
    
    /etc/my.cnf.d/server.cnf
    
    [mysqld]
    skip_networking

Nextcloud的官方文档[推荐](<https://docs.nextcloud.com/server/stable/admin_manual/configuration_database/linux_database_configuration.html#database-read-committed-transaction-isolation-level>)将事务隔离级别设置为READ-COMMITTED。当你预计有大量并发事务从而造成负载过高时，这一点尤其重要。 
    
    /etc/my.cnf.d/server.cnf
    
    [mysqld]
    transaction_isolation=READ-COMMITTED

设置`binlog_format=ROW`的建议已经过时，MariaDB现行版本的默认设置“`MIXED`”的表现已经足够好。 

以数据库用户root身份启动命令行工具`mysql`。（默认密码为空，应当尽快修改）
    
    $ mysql -u root -p

为Nextcloud创建用户和与之配套的数据库：
    
    CREATE USER 'nextcloud'@'localhost' IDENTIFIED BY 'db-password';
    CREATE DATABASE IF NOT EXISTS nextcloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
    GRANT ALL PRIVILEGES on nextcloud.* to 'nextcloud'@'localhost';
    FLUSH privileges;

（用自行设置的Nextcloud数据库用户的密码替换dp-password字段。完成后使用\q命令退出。） 

**注意：** MariaDB对于UTF8编码的解释存在缺陷，这导致了MariaDB无法存储码位在0x10000及以上的字符（比如emoji）。MariaDB在5.5版本引入了一种新的编码来“修复”这个问题，它叫做utf8mb4.所以千万不要使用MariaDB的utf8编码，请使用utf8mb4。如果需要迁移，请参阅[此文档](<https://docs.nextcloud.com/server/stable/admin_manual/configuration_database/mysql_4byte_support.html>)。

在PHP中启用相应扩展： 
    
    /etc/webapps/nextcloud/php.ini
    
    extension=pdo_mysql

与[Nextcloud管理手册](<https://docs.nextcloud.com/server/stable/admin_manual/configuration_database/linux_database_configuration.html#configuring-a-mysql-or-mariadb-database>)中提供的信息不同，对MariaDB进行额外设置是不必要的。 

使用以下命令完成对数据库的安装： 
    
    $ occ maintenance:install \
        --database=mysql \
        --database-name=nextcloud \
        --database-host=localhost:/run/mysqld/mysqld.sock \
        --database-user=nextcloud \
        --database-pass=_db-password_ \
        --admin-pass=_admin-password_ \
        --admin-email=_admin-email_ \
        --data-dir=/var/lib/nextcloud/data
    
**提示：** 原文大概是为了美观对上面的这条命令进行了排版，在输入的时候不能直接复制此命令，否则会报错，去掉反斜杠，按照正常的命令输入即可。比如`occ maintenance:install --database=pgsql --database-name=nextcloud --database-host=/run/postgresql...`。详情请看下面给出的官方文档。

注意将`db-password`，`admin-password`，`admin-email`替换成自己设定的相对应的值。这个命令可以使Nextcloud与数据库运行在同一台主机上。关于更多选项，请查看[官方文档](<https://docs.nextcloud.com/server/latest/admin_manual/occ_command.html#command-line-installation>)（输入`occ help maintenance:install`）。查看[使用“occ”命令行工具](<#%E4%BD%BF%E7%94%A8%E2%80%9Cocc%E2%80%9D%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7>)来了解此工具的详细信息。 

### PostgreSQL

如果你想在安装Nextcloud的主机上同时运行数据库，请配置并启动PostgreSQL（如果你尚未这样做）。请查看[此文档](<https://wiki.archlinux.org/title/PostgreSQL> "en:PostgreSQL")获得更多信息。为了提高安全性，建议[将PostgreSQL配置为仅侦听本地Unix套接字](<https://wiki.archlinux.org/title/PostgreSQL#Configure_PostgreSQL_to_be_accessible_exclusively_through_UNIX_Sockets> "en:PostgreSQL")： 
    
    /var/lib/postgres/data/postgresql.conf
    
    listen_addresses = ''
    
特别的，请不要忘记使用`initdb`命令初始化数据库。接下来使用PostgreSQL的命令行工具`psql`创建一个名为`nextcloud`的用户，然后为其创建一个同样名为`nextcloud`的数据库： 
    
    [postgres]$ psql
    
    CREATE USER nextcloud WITH PASSWORD '_db-password_ ';
    CREATE DATABASE nextcloud TEMPLATE template0 ENCODING 'UNICODE';
    ALTER DATABASE nextcloud OWNER TO nextcloud;
    GRANT ALL PRIVILEGES ON DATABASE nextcloud TO nextcloud;
    \q
    
（用自行设置的Nextcloud数据库用户的密码替换`dp-password`字段。） 

下载PHP依赖包[php-legacy-pgsql](<https://archlinux.org/packages/?name=php-legacy-pgsql>)包（使用pacman --asdpes选项），然后启用相应的PHP扩展： 
    
    /etc/webapps/nextcloud/php.ini
    
    extension=pdo_pgsql
    
使用以下命令完成对数据库的安装： 
    
    $ occ maintenance:install \
        --database=pgsql \
        --database-name=nextcloud \
        --database-host=/run/postgresql \
        --database-user=nextcloud \
        --database-pass=_db-password_ \
        --admin-pass=_admin-password_ \
        --admin-email=_admin-email_ \
        --data-dir=/var/lib/nextcloud/data
    
注意将`db-password`，`admin-password`，`admin-email`替换成自己设定的相对应的值。这个命令可以使Nextcloud与数据库运行在同一台主机上。关于更多选项，请查看[官方文档](<https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/occ_command.html#command-line-installation>)（输入`occ help maintenance:install`）。查看[“occ”工具使用方法](<https://wiki.archlinux.org/title/Nextcloud#Using_the_"occ"_command_line_tool> "en:Nextcloud")来了解此工具的详细信息。 

##  应用服务器

[uwsgi](<https://archlinux.org/packages/?name=uwsgi>)包和[FPM](<https://cwiki.apache.org/confluence/display/HTTPD/PHP-FPM>)是两种常用的应用服务器，可用于处理PHP代码。其中FPM专门用于PHP，FPM与web服务器之间使用的通信协议是fastcgi。FPM的[文档](<https://www.php.net/manual/en/install.fpm.php>)仍有改进的空间。而uWSGI可以通过安装插件来支持包含PHP在内的一[部分语言](<https://uwsgi-docs.readthedocs.io/en/latest/LanguagesAndPlatforms.html>)，uWSGI与web服务器之间使用的通信协议是uwsgi（小写）。uWSGI有[大量的文档](<https://uwsgi-docs.readthedocs.io/en/latest/index.html>)可供查看，虽然大量的文档可能会导致阅读困难以及混乱。 

### uWSGI

[uWSGI](<https://wiki.archlinux.org/title/UWSGI> "en:UWSGI")有自己的文章。在那里可以找到很多有用的信息。最好作为依赖安装[uwsgi](<https://archlinux.org/packages/?name=uwsgi>)包和它的插件[uwsgi-plugin-php-legacy](<https://archlinux.org/packages/?name=uwsgi-plugin-php-legacy>)包,比如使用`--asdpes`选项。若要使用uWSGI运行Nextcloud代码，你必须为uWSGI创建一个专门的配置文件（`nextcloud.ini`）并且定义一个systemd服务。 

**警告：** 必须说明的一点：uWSGI最近维护得很少，其PHP插件更是维护甚少。这已经引发了一些问题，现在只能通过Arch Linux软件包的维护者修补uWSGI代码解决问题，即不能在上游解决。

#### nextcloud.ini

[Nextcloud](<https://archlinux.org/packages/?name=Nextcloud>)包已经包含了一个示例文件，该文件已经位于正确的位置`/etc/uwsgi/nextcloud.ini`。通常情况下你都必须根据你的需求调整此文件。你应该找到一份[具有大量注释的修改版本](<https://gist.githubusercontent.com/wolegis/fc0c01882b694777a6565aa1d0a4da47>)（与nextcloud自带的相比）。它提供了一个简洁的Nextcloud配置供个人使用（中等负载）。 

通常情况下，应当将启用的扩展，扩展的配置以及`open_basedir`与`/etc/webapps/nextcloud/php.ini`同步（opcache除外）。 

**提示：** 对`/etc/uwsgi/nextcloud.ini`的更改应该会变得更广泛。在软件包更新期间，将创建一个名为`nextcloud.ini.pacnew`的文件，以防止[nextcloud](<https://archlinux.org/packages/?name=nextcloud>)包提供的原始文件发生更改。为了更好的检查新文件的更改情况并将其应用到`/etc/uwsgi/nextcloud.ini`中去，可以采取以下方法： 

获取软件包提供`nextcloud.ini`的文件（例如直接从软件包中解压），存储一份它的副本，并将其命名为`nextcloud.ini.package`。 如果因[nextcloud](<https://archlinux.org/packages/?name=nextcloud>)包更新而产生了`nextcloud.ini.pacnew`文件，你可以通过下面的命令比对新旧文件的差异： 
    
    diff nextcloud.ini.package nextcloud.ini.pacnew

有选择性的应用更改到你自己的nextcloud.ini,这具体取决于它们是否适用于你的版本 

用`nextcloud.ini.pacnew`替换`nextcloud.ini.package`

####  uWSGI服务

[uwsgi](<https://archlinux.org/packages/?name=uwsgi>)包软件包提供了一个模板单元文件（`uwsgi@.service`）。实例ID（此处为 _nextcloud_ ）用于选择正确的配置文件。[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")`uwsgi@nextcloud.service`。 

如果你有多个（比如2个）像这样运行，这时可以考虑使用[emperor模式](<https://uwsgi-docs.readthedocs.io/en/latest/Emperor.html>)，这样更节约资源。 

### FPM

如果选择FPM作为你的应用服务器，下载[php-legacy-fpm](<https://archlinux.org/packages/?name=php-legacy-fpm>)包（最好作为依赖包安装 `--asdeps`） 

FPM的配置包含一份与它提供的全部应用相关的`php.ini`副本，一份专为每个应用（此处为Nextcloud）生成的pool file文件。最后，还需要调整systemd服务文件。 

#### php-fpm.ini

如前文所述，本指南将不会修改PHP主配置文件`/etc/php-legacy/php.ini`，而是创建并修改它的副本：
    
    # cp /etc/php-legacy/php.ini /etc/php-legacy/php-fpm.ini

确保该文件由root所有且仅能被root修改。（`-rw-r--r-- 1 root root ... php-fpm.ini`）。启用 op-cache（取消该行的注释）。 
    
    /etc/php-legacy/php-fpm.ini
    
    zend_extension=opcache

然后将下面的内容放到`[opcache]`行下面 
    
    /etc/php-legacy/php-fpm.ini
    
    opcache.enable = 1
    opcache.interned_strings_buffer = 16
    opcache.max_accelerated_files = 10000
    opcache.memory_consumption = 128
    opcache.save_comments = 1
    opcache.revalidate_freq = 1

**警告：** 不要尝试通过php_value[...]和php_flag[...]来把上面这些设置放到pool file中。否则FPM进程会在第一个请求处崩溃。

#### nextcloud.conf

下一步是创建pool file。它负责为Nextcloud应用程序生成专用的FPM进程。创建文件`/etc/php-legacy/php-fpm.d/nextcloud.conf`，你也许可以借鉴这个[预先配置好的版本](<https://gist.githubusercontent.com/wolegis/0d9c83acd0c8bf83bcfb3983931bc364>)。 

确保pool file由root所有且仅能被root修改。（`-rw-r--r-- 1 root root ... nextcloud.conf`）。取决于是否开启访问记录（预配置版本中已开启），应当为日志文件创建相应的目录（预配置版本中是`/var/log/php-fpm-legacy/access`）。按你的想法修改配置（特别是`pm...` ，`php_value[...]`以及`php_flag[...]`）。`php_value[...]`和`php_flag[...]`应当与文件`/etc/webapps/nextcloud/php.ini`中的相一致（而不是`/etc/php-legacy/php-fpm.ini`）。 

也可以通过修改`php-fpm.ini`文件来达到同样的目的，但是对`php-fpm.ini`的修改将对所有由FPM提供服务的应用生效。 

**提示：**[php-legacy-fpm](<https://archlinux.org/packages/?name=php-legacy-fpm>)包自带一个名为`www.conf`的pool file的文件，但是在本指南中不发挥任何作用。一个防止其生效的好方法是将其重命名为`www.conf.package`并创建一个仅包含注释行（以分号开头的行）的文件`www.conf`。使用这种方法可以将`www.conf`变成空操作文件。该文件同样不会因[php-legacy-fpm](<https://archlinux.org/packages/?name=php-legacy-fpm>)包的更新而被覆盖。在更新中，新文件被命名为`www.conf.pacnew`，你通过可以对比`www.conf.package`与`www.conf.pacnew`来检查新文件中是否有重大更改。如果发现了需要重新生成`nextcloud.conf`的更改，请在对`nextcloud.conf`操作完成后，将`www.conf.pacnew`重命名为`www.conf.package`。

####  systemd服务

FPM作为systemd的一个服务运行。你应该修改服务的配置来使其能够运行Nextcloud。最好的方法是通过[drop-in文件](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "Systemd")（： 
    
    /etc/systemd/system/php-fpm-legacy.service.d/override.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/php-fpm-legacy --nodaemonize --fpm-config /etc/php-legacy/php-fpm.conf --php-ini /etc/php-legacy/php-fpm.ini
    ReadWritePaths=/var/lib/nextcloud
    ReadWritePaths=/etc/webapps/nextcloud/config

  * 它将ExecStart行替换为上一节中提到的php-fpm.ini的启动命令。

  * 它将/var/lib/nextcloud和/etc/webapps/nextcloud/config目录（及其下所有内容全部置为可写。原始服务定义的ProtectSystem=full会默认将/usr,/boot和/etc作为只读目录对FPM进程开放。

不要忘记[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")和[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")php-fpm-legacy服务。 

####  保持/etc目录整洁

Nextcloud会默认创建uWSGI的配置文件`/etc/uwsgi/nextcloud.ini`.该文件对你没有任何作用（虽然也没有任何危害）如果你无论如何都不想它出现在你的目录中。将以下代码添加到`/etc/pacman.conf`中： 
    
    /etc/pacman.conf
    
    # uWSGI configuration that comes with Nextcloud is not needed
    NoExtract = etc/uwsgi/nextcloud.ini

##  Web服务器

有相当数量的web服务器可供选择。但你无论作何选择都要记住，Nextcloud应用必须用其自己的系统用户nextcloud运行。所以才需要将请求转发到上文提到的应用服务器中。 

### nginx

有关nginx的配置，显然已经超过了本文的覆盖范围。可以查看[相关文章](<../zh-cn/Nginx.html> "Nginx")了解更多信息。[Nextcloud的官方文档](<https://docs.nextcloud.com/server/latest/admin_manual/installation/nginx.html>)中也提供了详细配置文件可供参考。你可以自行决定如何将这些代码引入到你的nginx配置文件中。一种常见的方法是使用`/etc/nginx/sites-available`和`/etc/nginx/sites-enabled`目录来单独配置不同的服务器（也被称作虚拟主机）。请参看：[Nginx#管理服务器入口](<../zh-cn/Nginx.html#%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%A5%E5%8F%A3> "Nginx")。 

如果使用了nextcloud文档中提供的nginx配置，应将根目录更改为： 
    
    cloud.mysite.com.conf
    
    root /usr/share/webapps/nextcloud;

`upstream php-handler { ... }`的部分是不必要的。只需要在`location`中指定`fastcgi_pass unix:/run/php-fpm-legacy/nextcloud.sock;`当使用 _uWSGI_ 替代 _FPM_ 时，应将`location`替换成： 
    
    cloud.mysite.com.conf
    
    location ~ \.php(?:$|/) {
        include uwsgi_params;
        uwsgi_modifier1 14;
        # Avoid duplicate headers confusing OC checks
        uwsgi_hide_header X-Frame-Options;
        uwsgi_hide_header X-XSS-Protection;
        uwsgi_hide_header X-Content-Type-Options;
        uwsgi_hide_header X-Robots-Tag;
        uwsgi_hide_header X-Download-Options;
        uwsgi_hide_header X-Permitted-Cross-Domain-Policies;
        uwsgi_pass unix:/run/uwsgi/nextcloud.sock;
    
} 

你可能需要解决以下问题（部分）： 

  * 你的服务器名称，即你的Nextcloud能够访问的服务器部分的URL。
  * 用于签名的名称和用于SSL/TLS的密钥。
  * 访问记录存放的位置。
  * [Certbot](</wzh/index.php?title=Certbot&action=edit&redlink=1> "Certbot（页面不存在）")（或其他ACME客户端）用于存放域验证质询的位置。在这里，`alias`可能比`try_files`更合适。
  * 用于访问Nextcloud的路径（访问URL中服务器名称和端口的权限）。
  * 你正在使用的应用服务器（uWSGI或FPM），即nginx将以何种方式、向何处传递触发的PHP代码（见上文）。
  * 配置[OCSP装订](<https://en.wikipedia.org/wiki/OCSP_stapling> "w:OCSP stapling")。

Nginx无需安装任何其他模块，因为其本就支持这两种协议：FastCGI和uwsgi。 

###  Apache HTTP 服务器

[apache HTTP服务器](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Apache HTTP 服务器")中有许多有用的信息。Nextcloud的文档中同样有一些[配置样例](<https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#apache-web-server-configuration>)，你也可以从`/usr/share/doc/nextcloud/apache.example.conf`中找到它们。对mod_php的隐性依赖将不再可用，需要使用mod_proxy_fcgi或mod_proxy_uwsgi。 

你可以在本站中找到[使apache与FPM协同工作](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html#%E4%BD%BF%E7%94%A8_php-fpm_%E5%92%8C_mod_proxy_fcgi> "Apache HTTP 服务器")的方法。uWSGI的文档中有[使apache与uWSGI和mod_proxy_uwsgi协同工作以处理PHP代码](<https://uwsgi-docs.readthedocs.io/en/latest/Apache.html>)的方法。注意apache包含了`mod_proxy_fcgi`以及`mod_proxy_uswgi`两个插件。它们应按需开启。 

下面是运行Nextcloud所需的模块： 
    
    /etc/httpd/conf/httpd.conf
    
    # these are already loaded in a standard Apache installation
    LoadModule headers_module modules/mod_headers.so
    LoadModule env_module modules/mod_env.so
    LoadModule dir_module modules/mod_dir.so
    LoadModule mime_module modules/mod_mime.so
    LoadModule setenvif_module modules/mod_setenvif.so
    
    # these need to be uncommented explicitly
    LoadModule rewrite_module modules/mod_rewrite.so
    LoadModule ssl_module modules/mod_ssl.so
    LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
    LoadModule proxy_module modules/mod_proxy.so
    
    # either this one in case you use FPM
    LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so
    # or this one in case you opt for uWSGI
    LoadModule proxy_uwsgi_module modules/mod_proxy_uwsgi.so

取消注释下面的代码来引入TLS配置参数： 
    
    /etc/httpd/conf/httpd.conf
    
    Include conf/extra/httpd-ssl.conf

有关如何优化TLS配置的详细信息，参看[Mozilla SSL配置工具](<https://ssl-config.mozilla.org/#server=apache&config=intermediate>)。 

请参阅以下两个示例配置文件，具体取决于你希望如何访问Nextcloud： 

  * 通过主机名访问（例：`https://cloud.mysite.com/`)，把[这段代码](<https://gist.github.com/wolegis/1659786ded9128935f638ee2bf228906>)放入`/etc/httpd/conf/extra/httpd-vhosts.conf`中。
  * 通过子文件夹访问（例：`https://www.mysite.com/nextcloud/`），把[这段代码](<https://gist.github.com/wolegis/002e198c2db7980a84fd8d160c2bdb9a>)放入`/etc/httpd/conf/httpd.conf`中。

当然，你应该按照自己的实际情况来修改示例的配置文件。当你使用 _uWSGI_ 时，用`SetHandler "proxy:unix:/run/uwsgi/nextcloud.sock|uwsgi://nextcloud/"`替换`SetHandler`行。 

Nextcloud包自带一个`.htaccess`文件，它已经处理了很多重写和标题内容。运行 `occ maintenance:update:htaccess` 以适配此文件。`/etc/webapps/nextcloud/config/config.php`中的`htaccess.RewriteBase`参数对此至关重要。 

##  后台作业

Nextcloud要求按计划运行某些任务。请查看[相关文档](<https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/background_jobs_configuration.html>)来获取更多信息。实现这个目的最简单（也是最可靠）的方法是使用systemd的“服务”和已经内置在[nextcloud](<https://archlinux.org/packages/?name=nextcloud>)包中的计时器单元。为使作业使用正确的`php.ini`文件（而不是全局`php.ini`），服务单元需要进行一些调整。创建一个[附加配置片段（drop-in file）](<../zh-cn/Drop-in_file.html> "Drop-in file")并添加: 
    
    /etc/systemd/system/nextcloud-cron.service.d/override.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/php-legacy -c /etc/webapps/nextcloud/php.ini -f /usr/share/webapps/nextcloud/cron.php

之后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")`nextcloud-cron.timer`（不是`.service`） 

根据[文档](<https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/background_jobs_configuration.html#maintenance-window-start>)的建议，添加如下参数到nextcloud的配置文件中。 
    
    /etc/webapps/nextcloud/config/config.php
    
    ....
    'maintenance_window_start' => 0,
    ....

该值是UTC定义的整点时刻，每天从这一时刻开始的4小时，所有高耗时的作业将会被尽数处理，也就是说，请将它安排在主要工作时间以外。 

**警告：** 不要下载 [nextcloud-systemd-timers](<https://archlinux.org/packages/?name=nextcloud-systemd-timers>)包。该软件包已经过时且不再维护。

##  使用内存缓存（In-memory caching）

Nextcloud 的文档推荐使用存内对象缓存，这样可以显著提高性能。 

**注意：** 关注[这篇通知](<https://github.com/nextcloud/notify_push>)：Nextcloud服务以服务器推送取代了客户端轮询，这大大减少了同步延迟，这依赖于redis。

### APCu

安装[php-legacy-apcu](<https://archlinux.org/packages/?name=php-legacy-apcu>)包 （作为依赖`--asdeps`）。在相关配置文件中启用此扩展： 

  * `occ`命令和后台任务需要用到的 `/etc/webapps/nextcloud/php.ini`。
  * 下面的文件由你的应用服务器决定 
    * _uWSGI：_`/etc/uwsgi/nextcloud.ini`。
    * _FPM：_`/etc/php-legacy/php-fpm.d/nextcloud.conf`。

将以下代码添加到`/etc/webapps/nextcloud/php.ini`中： 
    
    /etc/webapps/nextcloud/php.ini
    
    extension=apcu
    apc.ttl=7200
    apc.enable_cli = 1

（最好是写在`Module Settings`部分的下面什么地方）。 

对于另外的那个文件，激活APCu的设置默认已经在其中，只需要取消注释即可。 另外两个与 APCu 相关的配置参数也已存在。不需要再修改（touch）`/etc/php-legacy/php.ini`或者`/etc/php-legacy/conf.d/apcu.ini`这两个文件。 

重启应用服务器（不是Web服务器，官方文档中强调了）。将下面的代码添加到Nextcloud配置文件中： 
    
    /etc/webapps/nextcloud/config/config.php
    
    'memcache.local' => '\OC\Memcache\APCu',

### Redis

下载[php-legacy-igbinary](<https://archlinux.org/packages/?name=php-legacy-igbinary>)包和[php-legacy-redis](<https://archlinux.org/packages/?name=php-legacy-redis>)包（作为依赖`--asdeps`）如果你在本地运行这个组件（与Nextcloud在同一台主机上）。 当然，你也可以选择将Redis服务器安装在其它机器上。详细信息参看： [Nextcloud官方文档](<https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/caching_configuration.html#id2>)

**注意：** “Redis”与“APCu”本地缓存并不冲突。事实上，Nextcloud的文档推荐同时配置这二者。

在有关文件中启用所需的`igbinary`和`redis`扩展： 

  * `occ`命令和后台任务需要用到的 `/etc/webapps/nextcloud/php.ini`。
  * 下面的文件由你的应用服务器决定 
    * _uWSGI：_`/etc/uwsgi/nextcloud.ini`。
    * _FPM：_`/etc/php-legacy/php-fpm.d/nextcloud.conf`。

找到文件中有关启用扩展的部分，然后添加上启动`igbinary`和`redis`的两行。 

**注意：** 应当在`extension=redis`之前加载`extension=igbinary`。否则`occ`会报这个错： _/usr/lib/php-legacy/modules/redis.so: undefined symbol: igbinary_serialize_ 。

如果你在上述的配置文件中指定了`open_basedir` 选项，并且通过本地Unix套接字在本地使用Redis服务，那么则必须扩展允许PHP读取和写入文件的目录列表。在上面提到的文件找到有关的行，然后在其中添加由Redis创建的包含本地Unix套接字的目录，例如：`/run/redis`。 

**注意：** 在[#Application server](<#Application_server>) 一节中提到的示例配置文件[nextcloud.ini](<https://gist.githubusercontent.com/wolegis/fc0c01882b694777a6565aa1d0a4da47>)和[nextcloud.conf](<https://gist.githubusercontent.com/wolegis/0d9c83acd0c8bf83bcfb3983931bc364>)中已经启用了`open_basedir`。所以说，如果你使用了这些配置文件，那么必须要调整它们。

将下面的内容添加到Nextcloud配置文件中： 
    
    /etc/webapps/nextcloud/config/config.php
    
    'memcache.local' => '\OC\Memcache\APCu',
    'memcache.distributed' => '\OC\Memcache\Redis',
    'memcache.locking' => '\OC\Memcache\Redis',
    'redis' => [
         'host'     => '/run/redis/redis.sock',
         'port'     => 0,
         'dbindex'  => 0,
         'password' => '',
         'timeout'  => 1.5,
    ],

相同的，应根据需要调整`/run/redis/redis.sock`。`dbindex`，`password`和`timeout`是可选的。 

如果 _Redis_ 运行在不同的机器上： 
    
    /etc/webapps/nextcloud/config/config.php
    
    'memcache.local' => '\OC\Memcache\APCu',
    'memcache.distributed' => '\OC\Memcache\Redis',
    'memcache.locking' => '\OC\Memcache\Redis',
    'redis' => [
         'host' => '_redis-host.mysite.com_ ',
         'port' => 6379,
    ],

你需要将` _redis-host.mysite.com_`替换成你自己的设置。 

##  提高安全性

请参看[Nextcloud官方文档](<https://docs.nextcloud.com/server/latest/admin_manual/installation/harden_server.html>)和本百科中的[安全](<../zh-cn/%E5%AE%89%E5%85%A8.html> "安全")条目。Nextcloud也提供了一个[安全性检测工具](<https://scan.nextcloud.com/>)。 

##  同步

**提示：** 不推荐使用自己的个人密码进行认证，而是使用所谓应用程序令牌作为认证工具，通过应用程序令牌，其它软件可以自动认证你的服务器。如此一来，如果你怀疑其中一个软件的凭据已经泄露，你只需要撤消这个受影响的应用程序令牌，而不是更改密码并将新密码重新配置到所有使用此密码的软件上。你可以使用 Nextcloud 的 Web 界面上的设置>设备及会话安全来生成新的令牌。

###  桌面

官方提供的客户端可以下载 [nextcloud-client](<https://archlinux.org/packages/?name=nextcloud-client>)包。[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中提供了它的替代版本：[nextcloud-client-git](<https://aur.archlinux.org/packages/nextcloud-client-git/>)AUR。注意：Nextcloud 不支持 [owncloud-client](<https://archlinux.org/packages/?name=owncloud-client>)包。 

桌面客户端基本上会将计算机的一个或多个目录与 Nextcloud 的文件服务中的目录同步。它可以很好地集成在桌面文件管理器中（KDE plasma 中是 Dolphin、Gnome 中是 Nautilus），在其上显示表示同步与共享状态的叠加层。文件的右键菜单都会多出一个 _Nextcloud_ 选项，可以通过此选项来使用 Nextcloud 的相关功能。[Nextcloud 的官方文档](<https://docs.nextcloud.com/desktop/latest/>)中专门介绍了其桌面客户端。 

如果 Nextcloud 客户端未能成功与文件管理器协同，请查看 [nextcloud-client](<https://archlinux.org/packages/?name=nextcloud-client>)包（`pacman -Qi nextcloud-client`）. 例如 Nautilus（Gnome）需要 [python-nautilus](<https://archlinux.org/packages/?name=python-nautilus>)包。使用（`pacman -S --asdeps`)作为依赖安装。 

**注意：** Nextcloud 的桌面客户端提供了一个可以指示同步状态的系统托盘图标[[1]](<https://docs.nextcloud.com/desktop/latest/visualtour.html>)。但 GNOME 没有提供开箱即用的系统托盘图标 API[[2]](<https://gitlab.archlinux.org/archlinux/packaging/packages/nextcloud-client/-/issues/5#note_180692>)。如果需要使用此功能，可以通过安装并启用 [gnome-shell-extension-appindicator](<https://archlinux.org/packages/?name=gnome-shell-extension-appindicator>)包。详情请看[GNOME#Extensions](<../zh-cn/GNOME.html#Extensions> "GNOME")。

### Thunderbird

102 版本以后的 [Thunderbird](<../zh-cn/Thunderbird.html> "Thunderbird") 完全支持 CalDAV 和 CardDAV——具有自动检测功能（即使不输入很长的URL也能访问日历和地址簿）。更多信息，请参阅 [Nextcloud 的官方文档](<https://docs.nextcloud.com/server/latest/user_manual/en/groupware/sync_thunderbird.html>)。 

###  以 davfs2 挂载

如果你想使用 WebDAV 挂载 Nextcloud，请下载 [davfs2](<https://archlinux.org/packages/?name=davfs2>)包（在 [davfs2](<../zh-cn/Davfs2.html> "Davfs2") 中有描述）。 

使用下面的命令挂载 Nextcloud： 
    
    # mount -t davfs https://_your_domain_ /nextcloud/remote.php/dav/files/_username_ / /path/to/mount
    
也可以在 `/etc/fstab` 创建条目： 
    
    /etc/fstab
    
    https://_your_domain_ /nextcloud/remote.php/dav/files/_username_ / /path/to/mount davfs rw,user,noauto 0 0
    
**提示：** 如果想要实现自动挂载目录，你可以将你的用户名（及密码，可选）存储在 [davfs2#Storing credentials](<../zh-cn/Davfs2.html#Storing_credentials> "Davfs2") 描述的文件中。

**注意：** 如果不能创建、复制文件及目录，参见 [davfs2#Creating/copying files not possible and/or freezes](<../zh-cn/Davfs2.html#Creating/copying_files_not_possible_and/or_freezes> "Davfs2")。

###  挂载到 GNOME Files (Nautilus)

你可以直接使用 Nautilus ('+ Other Locations')通过 WebDAV 来访问文件。使用 Nextcloud 服务器的 Web GUI 上显示的链接（例如：`https://cloud.mysite.com/remote.php/webdav/`）然后把 `davs` 替换成 `https`。当 Nautilus 尝试连接时会询问用户名和密码。 

**注意：** 确保你已经安装了 [gvfs-dnssd](<https://archlinux.org/packages/?name=gvfs-dnssd>)包，如果没有安装，也许会出现“Location is not mountable”错误。

### Android

从 [Google Play](<https://play.google.com/store/apps/details?id=com.nextcloud.client>) 或 [F-Droid](<https://f-droid.org/packages/com.nextcloud.client/>) 上下载Nextcloud的官方应用。 

启用日历及联系人同步（Android 4+）： 

  1. 下载[DAVx5](<https://www.davx5.com/>)（[Play Store](<https://play.google.com/store/apps/details?id=at.bitfire.davdroid>)，[F-Droid](<https://f-droid.org/app/at.bitfire.davdroid>)）。
  2. 创建一个新的 DAVdroid 账户，在 _账户_ 选项中设置你服务器的URL（例如：`https://cloud.mysite.com`）及登录账号和密码。

**注意：** 如前面的 [Nextcloud#Web](<#Web>) 服务器章节所示，如果你在 web 服务器上配置了适当的重定向，则不需要`/remote.php/{carddav,webdav}`这一部分。DAVdroid 会为自己找到正确的 URL。

### iOS

[App Store](<https://itunes.apple.com/us/app/nextcloud/id1125420102>) 有Nextcloud的官方应用。 

##  提示和技巧

###  使用“occ”命令行工具

`occ`是一个非常有用的管理工具。详情请参看[Nextcloud官方文档](<https://docs.nextcloud.com/server/latest/admin_manual/occ_command.html>)。你可以使用`occ`命令做许多操作，比如管理用户和配置应用。 

`/usr/bin/occ`是一个方便的基于原始occ工具`/usr/share/webapps/nextcloud/occ`的包装，它自动使用默认用户（ _nextcloud）_ 运行，使用默认的PHP可执行程序与配置文件。可以使用`NEXTCLOUD_USER`, `NEXTCLOUD_PHP`和`NEXTCLOUD_PHP_CONFIG`环境变量来指定使用别的用户、PHP可执行文件和PHP配置文件）。特别是对于使用了本内容[配置](<#%E9%85%8D%E7%BD%AE>)和[应用服务器](<#%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1%E5%99%A8>)配置自己的服务器的用户，使用`NEXTCLOUD_PHP_CONFIG`来指定自己的配置文件是必要的。即使用Next cloud指定的PHP配置文件。在本例中，将`export NEXTCLOUD_PHP_CONFIG=/etc/webapps/nextcloud/php.ini`行添加到你的`.bashrc`中。 

当使用[php](<https://archlinux.org/packages/?name=php>)包而非推荐的[php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包时你也需要设置`NEXTCLOUD_PHP`环境变量，即`export NEXTCLOUD_PHP=/usr/bin/php`也要被添加到.bashrc中。

**警告：** 当使用[php-legacy-apcu](<https://archlinux.org/packages/?name=php-legacy-apcu>)包进行缓存时，则需要在 `/etc/webapps/nextcloud/php.ini`中设置`apc.enable_cli=1`。否则`occ`命令将提示APCu的配置有误。

### Pacman hook

[nextcloud](<https://archlinux.org/packages/?name=nextcloud>)包自带一个[pacman hook](<../zh-cn/Pacman_hook.html> "Pacman hook")，它负责在软件包更新后自动升级Nextcloud数据库。查看 `/usr/share/doc/nextcloud/nextcloud.hook`这个文件。 

只可惜这个钩子在运行`occ upgrade`命令时无条件的使用全局的`php.ini`文件。也就是说，它并不使用[上文提及](<#%E4%BD%BF%E7%94%A8%E2%80%9Cocc%E2%80%9D%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7>)的账户下的环境变量`NEXTCLOUD_PHP_CONFIG`。 

一个可行的解决方案是在适当的地方复制hook文件：
    
    # mkdir -vp /etc/pacman.d/hooks
    # cp -a /usr/share/doc/nextcloud/nextcloud.hook /etc/pacman.d/hooks/10-nextcloud.hook

并且修改以`Exec`开始的行:
    
    /etc/pacman.d/hooks/10-nextcloud.hook
    
    Exec = /usr/bin/runuser -u nextcloud -- /usr/bin/php-legacy --php-ini /etc/webapps/nextcloud/php.ini /usr/share/webapps/nextcloud/occ upgrade

###  在子目录下运行Nextcloud

如果按照[Web服务器](<#Web%E6%9C%8D%E5%8A%A1%E5%99%A8>)一节中介绍的方法安装Nextcloud，最后需要一整个主机名才能访问Nextcloud服务。例如，`cloud.mysite.com`。如果你想通过子目录访问Nextcloud的话。例如，`www.mysite.com/nextcloud`。请尝试： 

  * Nginx：请查看[Nextcloud的官方文档](<https://docs.nextcloud.com/server/latest/admin_manual/installation/nginx.html#nextcloud-in-a-subdir-of-the-nginx-webroot>)，其中对这部分内容有完整介绍。

  * Apache：编辑`/etc/httpd/conf/extra/nextcloud.conf`文件，并注释掉`<VirtualHost *:80> ... </VirtualHost>`这部分内容。

**注意：** 别忘了编辑`.well-known`URLs，它用于服务发现。更多内容请参看官方文档：[Service discovery](<https://docs.nextcloud.com/server/latest/admin_manual/issues/general_troubleshooting.html#service-discovery>)

### Docker

要使用[Docker](<../zh-cn/Docker.html> "Docker")运行Nextcloud，请查看Docker Hub上的[Nextcloud仓库](<https://hub.docker.com/_/nextcloud>)。 

###  Office集成

对于Office集成，目前有三种解决方案： 

  * [Collabora Online](<https://www.collaboraoffice.com/collabora-online/>)
  * [ONLYOFFICE](<https://www.onlyoffice.com/>)
  * [MS Office Online Server](<https://docs.microsoft.com/en-us/officeonlineserver/office-online-server-overview>)

这三者的共同点是需要一个单独的服务器，并且你的Web服务器需要进行一些调整以将某些请求转发到Office服务。实际的集成由上面三者的Nextcloud app完成。 

需要注意的是，上面的三个产品都是面向商业客户的，也就是说你必须为其付费。只有Collabora有[面向开发者免费](<https://www.collaboraonline.com/code/>)的方案。ONLYOFFICE有对于[家庭部署](<https://www.onlyoffice.com/zh/docs-home-server.aspx>)的定价方案。 

有关安装、配置和如何集成的更多信息，参看： 

  * [Collabora online](<https://nextcloud.com/collaboraonline/>), [app](<https://apps.nextcloud.com/apps/richdocuments>)
  * [ONLYOFFICE](<https://api.onlyoffice.com/editors/nextcloud>), [app](<https://apps.nextcloud.com/apps/onlyoffice>)
  * [MS Office Online Server](<https://github.com/nextcloud/officeonline>), [app](<https://apps.nextcloud.com/apps/officeonline>)

###  禁用应用推荐

默认情况下，Nextcloud会向新用户推荐应用，这可能会导致大量通知。要禁用此功能，请使用`occ app:disable recommendations`。 

###  使用Calcardbackup备份日历和地址簿

可以配置[calcardbackup](<https://aur.archlinux.org/packages/calcardbackup/>)AUR，它可以定期备份日历和地址簿。根据喜好编辑`/etc/calcardbackup/calcardbackup.conf`文件，并且[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")和[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")`calcardbackup.timer`。 

##  故障排除

有关故障排除的详细信息，请参看本页面的[英文版本](<https://wiki.archlinux.org/title/Nextcloud#Troubleshooting> "en:Nextcloud")。 

##  参见

  * [Nextcloud Documentation Overview](<https://docs.nextcloud.com/>)
  * [Nextcloud Admin Manual](<https://docs.nextcloud.com/server/latest/admin_manual/>)
