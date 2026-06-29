# PHP

PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML.

## Installation
Install the  package.

Due to application software that cannot use the latest PHP version, you may install  alongside. That package provides the oldest still supported (at least Security Support) PHP branch and must be configured within the applications that require it.

You can find older and pinned versions of PHP in the Arch User Repository (AUR):

* ,
* ,
* ,
* ,
* ,
* .

Those are binary builds using the openSUSE Build Service.

## Running
While PHP can be run standalone, it is typically used with web servers. That requires installing additional packages and editing configuration files. For common setups, see the following:

* Apache HTTP Server#PHP
* nginx#PHP implementation
* lighttpd#PHP
* Hiawatha#CGI

To run PHP scripts as plain CGI, you need the  package.

## Configuration
The main PHP configuration file is well-documented and located at .

* It is recommended to set your timezone (list of timezones) in  like so:

 date.timezone = Europe/Berlin

* If you want to display errors to debug your PHP code, change  to  in :

 display_errors = On

* The open_basedir directive limits the paths that can be accessed by PHP, thus increasing security at the expense of potentially interfering with normal program execution. Starting with PHP 7.0, it is no longer set by default to more closely match upstream so users who wish to use it must configure it manually. All symbolic links are resolved, so it is not possible to avoid this restriction with a symlink. The default Arch packages for certain webapps like  &  installs the webapps under  and creates a symlink pointing to the actual configuration files for those webapps under . So, if you are setting up , make sure both those folders listed are in the . This will obviously be different for webapps installed in other locations. Example:

 open_basedir = /srv/http/:/var/www/:/home/:/tmp/:/var/tmp/:/var/cache/:/usr/share/pear/:/usr/share/webapps/:/etc/webapps/

## Extensions
A number of commonly used PHP extensions can also be found in the official repositories:

 $ pacman -Ss php-

Existing extensions are located in  directory.

For example, to enable  extension create file  with line:

 extension=iconv

Extensions for current and older versions of PHP are also available in the AUR under prefixes like php- and php56-, e.g. , , .

## gd
For  uncomment the line in :

 extension=gd

## Imagemagick
Install the  package and install one of the listed PHP extension library.

Install , it will create the file  to configure the extension.

If you want imagemagick to have SVG support, e.g. for nextcloud, then install  as a dependency.

## PECL
Make sure the  package has been installed:

 # pecl install imagick

Create a  and enable the extension:

## Multithreading
If you wish to have POSIX multi-threading you will need the parallel extension. To install the extension using  you are required to use a compiled version of PHP with the thread safety support flag . Currently the most clean way to do this would be to rebuild the original package with the flag.  Instruction can be found on the PHP pthreads extension page.

## PCNTL
PCNTL allows you to create process directly into the server side machine. While this may seen as something you would want, it also gives PHP the power to mess things up really badly. So it is a PHP extension that cannot be loaded like other more convenient extension. This is because of the great power it gives to PHP. To enable it PCNTL has to be compiled into PHP.

The php package on Arch Linux is currently built with "--enable-pcntl", so that it should be available by default.

## MySQL/MariaDB
Install and configure MySQL/MariaDB as described in MariaDB.

Uncomment the following lines in :

 extension=pdo_mysql
 extension=mysqli

You can add minor privileged MySQL users for your web scripts. You might also want to edit  and add in mysqld section  line so the MySQL server is only accessible by the localhost, as per MariaDB#Enable access locally only via Unix sockets. You have to restart MySQL for changes to take effect.

## Redis
Install and configure Redis, then install .

Uncomment the line of the package, e.g. .
Also ensure that the igbinary extension is enabled (also uncommented) in

## PostgreSQL
Install and configure PostgreSQL, then install the  package and uncomment the following lines in :

 extension=pdo_pgsql
 extension=pgsql

## Sqlite
Install and configure SQLite, then install the  package and uncomment the following lines in :

 extension=pdo_sqlite
 extension=sqlite3

## XDebug
XDebug allows you to easily debug (using modified var_dump function), profile, or trace PHP code.

Install  and uncomment the following line in :

 zend_extension=xdebug.so

You can configure what XDebug does by adding a xdebug.mode line to the same file. By default, it is set to .

## Snuffleupagus
Install , uncomment the two lines in , and put the path to the  file in the second line:

 extension=snuffleupagus.so
 sp.configuration_file=/etc/php/conf.d/snuffleupagus.rules

## Caching
There are two kinds of caching in PHP: opcode/bytecode caching and userland/user data caching. Both allow for substantial gains in applications speed, and therefore should be enabled wherever possible.

* Zend OPCache provides only opcode caching.
* APCu provides only userland caching.

## OPcache
OPcache comes bundled with the standard PHP distribution and is enabled by default since version 8.5 (November 2025).
A list of its options and suggested settings can be found in its official entry on the PHP website.

## APCu
APCu can be installed with the  package. You can then enable it by uncommenting the following line in , or adding it to your PHP configuration file:

 extension=apcu

Its author recommends a few suggested settings, among which:

*  and  are not really required as they represent the default values;
*  on the other hand seems rather beneficial;
* finally, , which although not recommended by the manual may be required by some software such as ownCloud.

## Development tools
*
*
*
*
*
*

## Commandline tools
## Composer
Composer is a dependency manager for PHP.
It can be installed with the  package.

## Allow user-wide installations
To allow global package installations for the current user (e.g. ), you may want to specify a default location by using an environment variable:

 PATH="$HOME/.config/composer/vendor/bin:$PATH"

## Usage with php-legacy
Some applications may require , but by default,  runs with the latest version of PHP. Thus, in order to use the legacy version instead, one must replace  with  in their scripts, makefiles and other applicable locations. An example of this is when building Nextcloud apps.

## Others
*
*
*
*
*
*
*
*
*
*

## Troubleshooting
## PHP Fatal error: Class 'ZipArchive' not found
Ensure the zip extension is enabled.

## /etc/php/php.ini not parsed
If your  is not parsed, the ini file is named after the sapi it is using. For instance, if you are using uwsgi, the file would be called . If you are using cli, it is .

## PHP Warning: PHP Startup: '''': Unable to initialize module
When running , this error indicates that the aforementioned module is out of date. This will rarely happen in Arch Linux, since maintainers make sure core PHP and all modules be only available in compatible versions.

This might happen in conjunction with a module compiled from the AUR. You usually could confirm this by looking at the dates of the files .

To fix, find a compatible update for your module, probably by looking up the AUR using its common name.

If it applies, flag the outdated AUR package as outdated.

## Permission denied issues when using php-fpm
There is a default AppArmor php-fpm profile which prohibits php-fpm from accessing files outside system paths. You may need to manually allow access to your custom web path by creating :
