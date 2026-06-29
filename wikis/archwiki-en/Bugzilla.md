# Bugzilla

Bugzilla is server software designed to help you manage software development.

## Installation
Install the  package.

## Configuration
## Module dependencies
Perform a module check first:

 # cd /srv/http/bugzilla
 # ./checksetup.pl --check-modules

Check the output for which modules are required and which are optional. The shell commands to install missing modules will also be shown.

Install all required and optional modules using:

 # perl install-module.pl --all

## Final module check
What follows is some more configuration to let BugZilla connect to MySQL and create initial tables in it.

Run  again, this time without the  switch:

 # ./checksetup.pl

A file called  is generated if everything is okay. Then, modify some of the file's parameters:

 $webservergroup = 'http';
 $db_driver = 'DATABASE_TO_USE_HERE';
 $db_name = 'DATABASE_NAME_HERE';
 $db_user = 'DATABASE_USER_HERE';
 $db_pass = 'YOUR_PASSWORD_HERE';

## Apache
Finally, configure Apache HTTP Server to run BugZilla using mod_cgi (can also be configured using mod_perl; refer to this for details).

First uncomment the following line in :

 LoadModule cgi_module modules/mod_cgi.so

Then add the following lines to :

   AddHandler cgi-script .cgi
   Options +ExecCGI
   DirectoryIndex index.cgi
   AllowOverride All

Now restart Apache and required modules.

Access  using your web browser.
