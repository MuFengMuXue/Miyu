# Apache HTTP Server/mod fcgid

mod_fcgid is a FastCGI module for Apache with a GPL license.

 2.4 now provides an official module, mod_proxy_fcgi. See configuration example for php-fpm and Apache HTTP Server#Using php-fpm and mod_proxy_fcgi.

## Installation
Install the  package.

## Usage
First you need to load the fastcgi module. Make sure that the following present and uncommented:

Then you need to tell Apache when to use FastCGI.

For example you can ask Apache to treat all .fcgi files as fastcgi applications:

Remember that standard CGI restrictions apply, files must be in an ExecCGI enabled directory to execute.

## Troubleshooting
It does not work? Apache error log () should help you find the problem.
