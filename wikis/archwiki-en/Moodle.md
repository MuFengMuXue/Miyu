# Moodle

Moodle is a free and open-source e-learning software platform, written in PHP.

This article describes how to set up the Moodle server.

## Installation
Installation quick guide:
: You will need a working web server (e.g. Apache HTTP Server), a database (e.g. MySQL or PostgreSQL) and have PHP configured.

Be aware a compatible PHP version is required.

There is also an AUR package  for the installation.

Either you can use this way:

Download the most current version of Moodle from https://download.moodle.org/ - this installation was done with 2.3.1+, and there may be minor changes to the install routine in later versions.

Unzip it into :

 # tar xzvf moodle-latest-23.tgz -C /srv/http

Make it read/writeable by Apache:

 # chown -R http:http /srv/http/moodle

## Configuration
## Preconfiguration
Some changes need to be made to the default setup so Moodle will work.

## File access
Add  to :

 open_basedir = /srv/http/:/home/:/tmp/:/usr/share/pear/:/srv/

This allows PHP to access the .BBS#80782

## Create the MoodleData Directory
This needs to be readable and writeable by Apache:

 # mkdir /srv/moodledata
 # chown http:http /srv/moodledata

## Configure PHP extension
Uncomment the following lines in  (remove the semicolon from the start of the line):

 extension=curl
 extension=gd
 extension=gettext
 extension=iconv
 extension=intl
 extension=mysqli
 extension=soap
 extension=xmlrpc
 extension=zip

## Restart Apache
You now need to restart Apache's  to make these changes current. Note that if you get any errors while installing Moodle, and make subsequent changes, you will need to restart Apache after each set of changes.

## MariaDB
If you are using MariaDB and the moodle installer complains about the wrong version of MySQL, edit  in

 $CFG->dbtype    = 'mariadb';
 $CFG->dblibrary = 'native';

You will also need to create some tables so that Moodle can connect to it and modify it:

 MariaDB> CREATE USER 'moodleuser'@'localhost' IDENTIFIED BY 'yourpassword';
 MariaDB[(none) > GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON moodle.* TO 'moodleuser'@'localhost';
 MariaDB> FLUSH PRIVILEGES;
 MariaDB[(none) > exit;

## Configure a cron job
Per maintenance requirements, you need to configure a cron job to run regularly on your site.

Check Cron page to install a cron implementation. After that, edit your  file and add the following:

 * * * * *    /usr/bin/php /path/to/moodle/admin/cli/cron.php >/dev/null

Change the path to your Moodle installation directory.

## Application configuration
Go to http://localhost/moodle/install.php - this starts the Moodle installer. There then follows a sequence of configuration screens, most of which should be left at the defaults:

*Select the language
*You should pass the first page of tests (PHP Settings).
*Leave the default locations as they are. An error here is likely to be a data directory problem - check the directory exists, that it has the right ownership and that  in  is set correctly.
*On the MySQL Screen, enter the user (root) and that user's password in the screen. If you get an error here, go to the  created when you set up the LAMP stack and check mysql is working, and also check the passwords.
*On the Environment screen, you should pass all the tests - if not the errors give you a clue what is missing - an uninstalled program or a failure to uncomment one of the lines in
*If you are English, you do not need to download language packs.
*If the  has failed - probably because of lack of write access to the moodle subdirectory - the most likely reason is the ownership of the  structure, which should be  - this was set earlier but you might have skipped that bit.
*The remainder of the install should be automatic. It takes 2 or 3 minutes on my computer to set up all the SQL Databases and so on.
*The final page allows you to set up the administrator user for Moodle. You need to enter a password, name and set the country as a bare minimum. Do not forget the password !

Happy Moodling !
