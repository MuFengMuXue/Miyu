相关文章

  * [Pdepend](</wzh/index.php?title=Pdepend&action=edit&redlink=1> "Pdepend（页面不存在）")
  * [Php-codesniffer-drupal](</wzh/index.php?title=Php-codesniffer-drupal&action=edit&redlink=1> "Php-codesniffer-drupal（页面不存在）")
  * [PhpMetrics](</wzh/index.php?title=PhpMetrics&action=edit&redlink=1> "PhpMetrics（页面不存在）")
  * [PHPLOC](</wzh/index.php?title=PHPLOC&action=edit&redlink=1> "PHPLOC（页面不存在）")
  * [PhpDox](</wzh/index.php?title=PhpDox&action=edit&redlink=1> "PhpDox（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [PHP](<https://wiki.archlinux.org/title/PHP> "arch:PHP")，最近一次同步于 2025-01-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/PHP?diff=0&oldid=822622>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PHP_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[PHP](<https://secure.php.net/>)是一种广泛使用的通用脚本语言，特别适合于 Web 开发，可嵌入到 HTML 中。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [php](<https://archlinux.org/packages/?name=php>)包。 

由于某些应用程序无法使用最新版本的 PHP，您可以并行安装 [php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包。该软件包提供了最老的仍在[积极支持](<https://www.php.net/supported-versions.php>)的 PHP 分支，并且必须在需要它的应用程序中进行配置。有关详细说明，请参阅 [Nextcloud#Migrating to php-legacy](<../zh-cn/Nextcloud.html#Migrating_to_php-legacy> "Nextcloud")。 

您可以在 AUR 中找到较旧和固定版本的 PHP，包括 [php56](<https://aur.archlinux.org/packages/php56/>)AUR、[php74](<https://aur.archlinux.org/packages/php74/>)AUR、[php80](<https://aur.archlinux.org/packages/php80/>)AUR、[php81](<https://aur.archlinux.org/packages/php81/>)AUR 和 [php82](<https://aur.archlinux.org/packages/php82/>)AUR。这些是使用 [openSUSE Build Service](<https://build.opensuse.org/project/show/home:el:archphp>) 构建的二进制版本。 

##  运行

虽然PHP可以独立运行，但它通常与Web服务器一起使用。这需要安装额外的软件包并编辑配置文件。常见的设置请参考以下内容： 

  * [Apache HTTP Server#PHP](<../zh-cn/Apache_HTTP_Server.html#PHP> "Apache HTTP Server")
  * [nginx#PHP implementation](<../zh-cn/Nginx.html#PHP_implementation> "Nginx")
  * [lighttpd#PHP](<../zh-cn/Lighttpd.html#PHP> "Lighttpd")
  * [Hiawatha#CGI](</wzh/index.php?title=Hiawatha&action=edit&redlink=1> "Hiawatha（页面不存在）")

要想像纯CGI那样运行PHP,需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [php-cgi](<https://archlinux.org/packages/?name=php-cgi>)包 。 

##  配置

主要的PHP配置文件位于 `/etc/php/php.ini`，并且有详细的文档说明。 

  * 建议在`/etc/php/php.ini` 中设置所在时区([list of timezones](<https://secure.php.net/manual/en/timezones.php>)) 。如下:

    date.timezone = Europe/Berlin
    
  * 如果你想调试PHP时显示错误，在`/etc/php/php.ini`中将`display_errors` 设为 `On`：

    display_errors=On
    
  * [open_basedir](<https://php.net/open-basedir>) 限制 PHP 可以访问的目录，可以增加安全性，但是会影响程序的正常执行。从 PHP 7.0 开始，和上游一样默认不再设置，要使用的用户请手动设置。符号链接会被解析，所以无法通过符号链接跳过限制。某些软件的 Arch 软件包，例如 `nextcloud` 和 `phpmyadmin` 安装在 `/usr/share/webapps`，然后在 `/etc/webapps` 中创建了配置文件的符号链接。设置 `open_basedir` 时请加入这两个目录。例如：

    open_basedir = /srv/http/:/var/www/:/home/:/tmp/:/var/tmp/:/var/cache/:/usr/share/pear/:/usr/share/webapps/:/etc/webapps/
    
##  扩展

一些常用的PHP扩展也可以在官方库发现： 
    
    $ pacman -Ss php-
    
**提示：** 不要编辑`/etc/php/php.ini`，扩展的启停可在 `/etc/php/conf.d` 中设置，如： (e.g. `/etc/php/conf.d/imagick.ini`)

已经安装的扩展位于 `/usr/lib/php/modules` 目录。 

例如要启用 `ext-iconv` 扩展，在 `/etc/php/conf.d/extensions.ini` 中配置: 
    
    extension=iconv
    
要安装 PHP 的扩展，可以在 AUR 中搜索 php-* 或 php56-*, 例如 [php-imagick](<https://archlinux.org/packages/?name=php-imagick>)包, [php-redis](<https://archlinux.org/packages/?name=php-redis>)包 [php56-mcrypt](<https://aur.archlinux.org/packages/php56-mcrypt/>)AUR。 

### gd

欲使用 [php-gd](<https://archlinux.org/packages/?name=php-gd>)包 在 `/etc/php/php.ini`中取消下列内容的注释: 
    
    extension=gd
    
### imagemagick

安装[php-imagick](<https://archlinux.org/packages/?name=php-imagick>)包。这个软件包会创建 `/etc/php/conf.d/imagick.ini` 配置文件。 

要让 imagemagick 支持 SVG,需要安装 [librsvg](<https://archlinux.org/packages/?name=librsvg>)包。 

###  多线程

要使用 POSIX 多线程，需要 parallel 扩展 。用 `pecl` 安装 parallel (<https://pecl.php.net/package/parallel>) 扩展，需要 PHP 在编译时启用线程安全选项`--enable-maintainer-zts`. 当前最简单的方式是用需要的选项重新编译. 

可在 [PHP pthreads extension](</wzh/index.php?title=PHP_pthreads_extension&action=edit&redlink=1> "PHP pthreads extension（页面不存在）") 页面找到指令介绍。 

### PCNTL

利用 PCNTL 可以在服务器上直接创建进程。虽然这可能是你想要的，但是这样也会让 PHP 有能力把机器搞的一团糟。所以 PHP 不能和其他扩展一样加载，要启用此扩展，需要重新编译PHP。ArchLinux 的 PHP 已经加入 "--enable-pcntl"选项，默认已经启用。 

###  MySQL/MariaDB

根据 [MariaDB](<../zh-cn/MariaDB.html> "MariaDB") 页面安装并配置 MySQL/MariaDB. 

取消 `/etc/php/php.ini` 中[下面行](<https://secure.php.net/manual/en/mysqlinfo.api.choosing.php>)前面的注释 : 
    
    extension=pdo_mysql.so
    extension=mysqli.so
    
**警告：** PHP 7.0 中 [删除了](<https://secure.php.net/manual/en/migration70.removed-exts-sapis.php>) `mysql.so`。

可以给网络脚本最低的 MySQL 用户权限，可以编辑 `/etc/my.cnf.d/server.cnf`，在 'mysqld _段落添加`skip-networking`，这样 MyQSL 服务器就仅允许通过 localhost 本地访问。请参考 [MariaDB#Enable access locally only via Unix sockets](<../zh-cn/MariaDB.html#Enable_access_locally_only_via_Unix_sockets> "MariaDB")。设置之后需要重启 MySQL。_

### Redis

安装并配置 [Redis](</wzh/index.php?title=Redis&action=edit&redlink=1> "Redis（页面不存在）")，然后安装 [php-redis](<https://archlinux.org/packages/?name=php-redis>)包. 

在 `/etc/php/conf.d/redis.ini` 中取消 redis 扩展的注释。同时在 `/etc/php/conf.d/igbinary.ini` 中启用(取消注释) igbinary 扩展。 

### PostgreSQL

安装并配置 [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")，然后安装 [php-pgsql](<https://archlinux.org/packages/?name=php-pgsql>)包 软件包并取消 `/etc/php/php.ini` 中下面几行的注释: 
    
    extension=pdo_pgsql
    extension=pgsql
    
### Sqlite

安装并配置 [SQLite](<../zh-cn/SQLite.html> "SQLite")，然后安装 [php-sqlite](<https://archlinux.org/packages/?name=php-sqlite>)包 软件包并取消 `/etc/php/php.ini` 中下面几行的注释: 
    
    extension=pdo_sqlite
    extension=sqlite3
    
### XDebug

用 XDebug 可以很容易的通过修改的 var_dump() 函数进行调试、评测、追踪。 

安装 [xdebug](<https://archlinux.org/packages/?name=xdebug>)包 并取消 `/etc/php/conf.d/xdebug.ini` 中如下行前面的注释： 
    
    zend_extension=xdebug.so
    
你可以通过在同一文件中添加 [xdebug.mode](<https://xdebug.org/docs/install#mode>) 行来配置 XDebug 的行为。默认情况下，它设置为 `xdebug.mode=develop`。 

对于 Xdebug 3，默认端口是 9003，要更改它，请设置 `xdebug.remote_port=9000`。 

### Snuffleupagus

安装 [php-snuffleupagus](<https://archlinux.org/packages/?name=php-snuffleupagus>)包，取消 `/etc/php/conf.d/snuffleupagus.ini` 中的两行注释，并将 `snuffleupagus.rules` 文件的路径放在第二行： 
    
    extension=snuffleupagus.so
    sp.configuration_file=/etc/php/conf.d/snuffleupagus.rules
    
##  缓存

PHP有两种缓存： _opcode_ /_bytecode_ 缓存和 _userland_ /_user data_ 缓存，这两种缓存都大幅度提升性能，因此最好开启。 

  * [Zend OPCache](<https://en.wikipedia.org/wiki/Zend_Opcache> "wikipedia:Zend Opcache")仅提供 _opcode_ 缓存。
  * [APCu](<https://github.com/krakjoe/apcu/>)仅提供 _userland_ 缓存

### OPCache

OPCache随PHP发布，因此在[PHP configuration file](<#%E9%85%8D%E7%BD%AE>)中开启或添加此行即可： 
    
    /etc/php/php.ini
    
    zend_extension=opcache

你可在[官网](<https://secure.php.net/manual/en/book.opcache.php>) 找到其他设置以及建议设置。 

**警告：** 如果你使用[推荐设置](<https://secure.php.net/manual/en/opcache.installation.php#opcache.installation.recommended>)，要确保你一仔细看过[说明](<https://secure.php.net/manual/en/opcache.installation.php#114567>)，某些情况下可能导致如下错误：`zend_mm_heap corrupted`。

### APCu

通过 [php-apcu](<https://archlinux.org/packages/?name=php-apcu>)包 软件包安装 APCu, 然后在 `/etc/php/conf.d/apcu.ini` 中取消下面行的注释： 
    
    extension=apcu.so
    
作者 [建议进行一些设置](<https://github.com/krakjoe/apcu/blob/master/INSTALL>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ]: 

  * `apc.enabled=1` 和 `apc.shm_size=32M` 并不是必须的，因为这已经是 [默认值](<https://secure.php.net/manual/en/apcu.configuration.php>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ];
  * `apc.ttl=7200` 看上去 [很有效](<https://secure.php.net/manual/en/apc.configuration.php#ini.apcu.ttl>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ];
  * 最后, `apc.enable_cli=1`, 虽然手册上 [不建议启用](<https://secure.php.net/manual/en/apcu.configuration.php#ini.apcu.enable-cli>)，有些软件比如 [ownCloud](<https://github.com/owncloud/core/issues/17329#issuecomment-119248944>) 需要这个选项.

**提示：** 可以将设置加入 APCu 自己的 `/etc/php/conf.d/apcu.ini` 或直接加到住配置文件，只需要注意不要同时加入。

##  开发工具

  * **[Visual Studio Code](<../zh-cn/Visual_Studio_Code.html> "Visual Studio Code")** — 支持 PHP 等多种语言的开发编辑器。

     <https://code.visualstudio.com/> || [visual-studio-code-bin](<https://aur.archlinux.org/packages/visual-studio-code-bin/>)AUR

  * **Aptana Studio** — 用于PHP和网页开发的IDE。没有PHP调试器。

     <http://www.aptana.com/products/studio3.html> || [aptana-studio](<https://aur.archlinux.org/packages/aptana-studio/>)AUR

  * **[Eclipse](<../zh-cn/Eclipse.html> "Eclipse") PDT** — Eclipse的PHP变种。

     <https://www.eclipse.org/pdt/> || [eclipse-php-bin](<https://aur.archlinux.org/packages/eclipse-php-bin/>)AUR

  * **Komodo** — 集成了PHP+HTML+JavaScript的IDE。

     <http://komodoide.com/> || [komodo-ide](<https://aur.archlinux.org/packages/komodo-ide/>)AUR, 仅编辑器：[komodo-edit](<https://aur.archlinux.org/packages/komodo-edit/>)AUR

  * **[NetBeans](</wzh/index.php?title=NetBeans&action=edit&redlink=1> "NetBeans（页面不存在）")** — 用于多种语言的IDE，包括PHP。包含调试、重构、代码模板、自动补全、XML特性、网页设计和其他开发功能。

     <https://netbeans.org/> || [netbeans](<https://archlinux.org/packages/?name=netbeans>)包

  * **[JetBrains PhpStorm](<https://en.wikipedia.org/wiki/PhpStorm> "wikipedia:PhpStorm")** — 商业的、跨平台PHP IDE，基于JetBrains的IntelliJ IDEA平台。可以从JetBrains获取免费的教育许可。[[1]](<https://www.jetbrains.com/student/>)

     <https://www.jetbrains.com/phpstorm/> || [phpstorm](<https://aur.archlinux.org/packages/phpstorm/>)AUR, 30天试用：[phpstorm-eap](<https://aur.archlinux.org/packages/phpstorm-eap/>)AUR

##  命令行工具

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 使用 [Template:App](<../zh-cn/Template:%E5%BA%94%E7%94%A8.html> "Template:App")。（在[Talk:PHP](<../zh-cn/Talk:PHP.html>)讨论）

### Composer

[Composer](<https://getcomposer.org/>) 是 PHP 的依赖管理工具。 可以通过 [composer](<https://archlinux.org/packages/?name=composer>)包 包进行安装。 

要允许当前[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户")全局安装包（例如 `$ composer global require "package/name"`），您可能需要通过使用[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")指定默认位置： 
    
    PATH="$HOME/.config/composer/vendor/bin:$PATH"
    
####  与 php-legacy 一起使用

某些应用程序可能需要 [php-legacy](<https://archlinux.org/packages/?name=php-legacy>)包，但默认情况下，`composer` 使用最新版本的 PHP 运行。因此，为了使用旧版 PHP，必须在脚本、Makefile 和其他适用位置中将 `composer` 替换为 `php-legacy /usr/bin/composer`。例如，在构建 [Nextcloud](<../zh-cn/Nextcloud.html> "Nextcloud") 应用时就需要这样做。 

### Box

[Box](<https://box-project.github.io/box2/>) 是一个用于构建和管理 Phars 的应用程序。 可以通过 [php-box](<https://aur.archlinux.org/packages/php-box/>)AUR 包进行安装。 

### PDepend

[PHP Depend](<https://pdepend.org/>) (pdepend) 是一个用于 PHP 的软件度量工具。 可以通过 [pdepend](<https://aur.archlinux.org/packages/pdepend/>)AUR 包进行安装。 

### PHP Coding Standards Fixer

[PHP Coding Standards Fixer](<https://github.com/FriendsOfPHP/PHP-CS-Fixer>) 是一个用于修复代码以符合 PSR-1 和 PSR-2 编码标准的工具。 可以通过 [php-cs-fixer](<https://aur.archlinux.org/packages/php-cs-fixer/>)AUR 包进行安装。 

### PHP-CodeSniffer

[PHP CodeSniffer](<https://pear.php.net/package/PHP_CodeSniffer/>) 可以对 PHP、JavaScript 和 CSS 文件进行标记化，并检测违反定义的编码标准的行为。 可以通过 [php-codesniffer](<https://aur.archlinux.org/packages/php-codesniffer/>)AUR 包进行安装。 

### phpcov

[phpcov](<https://github.com/sebastianbergmann/phpcov>) 是 PHP_CodeCoverage 库的命令行前端。 可以通过 [phpcov](<https://aur.archlinux.org/packages/phpcov/>)AUR 包进行安装。 

### phpDox

[phpDox](<http://phpdox.de/>) 是 PHP 项目的文档生成器。这包括但不限于 API 文档。 可以通过 [phpdox](<https://aur.archlinux.org/packages/phpdox/>)AUR 包进行安装。 

### PHPLoc

[PHPLoc](<https://github.com/sebastianbergmann/phploc/>) 是一个用于快速测量 PHP 项目大小的工具。 可以通过 [phploc](<https://aur.archlinux.org/packages/phploc/>)AUR 包进行安装。 

### PhpMetrics

[PhpMetrics](<https://www.phpmetrics.org/>) 提供了关于 PHP 项目的各种度量。 可以通过 [phpmetrics](<https://aur.archlinux.org/packages/phpmetrics/>)AUR 包进行安装。 

### PHPUnit

[PHPUnit](<https://phpunit.de>) 是一个面向程序员的 PHP 测试框架。 可以通过 [phpunit](<https://aur.archlinux.org/packages/phpunit/>)AUR 包进行安装。 

### Producer

[Producer](<http://getproducer.org/>) 是一个命令行质量保证工具，用于验证并发布您的 PHP 库包。 可以通过 [producer](<https://aur.archlinux.org/packages/producer/>)AUR 包进行安装。 

##  故障排除

###  PHP Fatal error: Class 'ZipArchive' not found

确保启用了 zip 扩展。 
    
    /etc/php/php.ini
    
    extension=zip

###  /etc/php/php.ini 未被解析

如果你的 `php.ini` 未被解析，ini 文件的名称会根据所使用的 SAPI 命名。例如，如果你使用的是 uwsgi，文件将被称为 `/etc/php/php-uwsgi.ini`。如果你使用的是 cli，文件则是 `/etc/php/php-cli.ini`。 

###  PHP Warning: PHP Startup: _< module>_: Unable to initialize module

当运行 `php` 时，此错误表明上述模块已过时。在 Arch Linux 中这种情况很少发生，因为维护者确保核心 PHP 和所有模块仅在兼容的版本中可用。 

这种情况可能与从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 编译的模块一起发生。你通常可以通过查看 `/usr/lib/php/modules/` 目录中的文件日期来确认这一点。 

要修复此问题，请为你的模块找到一个兼容的更新，通常可以通过使用其常用名称在 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中查找。 

如果适用，请将过时的 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 包标记为 _outdated_ 。 

##  参见

  * [PHP 官方网站](<https://www.php.net/>)
  * [Arch Linux PHP 传统分支公告](<https://archlinux.org/news/php-82-update-and-introduction-of-legacy-branch/>)
