# XWiki

XWiki is an open-source enterprise-ready wiki written in Java, with a focus on extensibility.

## Installation
Feel free to follow along on the XWiki Installation Guide.  These instructions assume you will be using Tomcat and PostgreSQL. It should not be too difficult to apply these guidelines to other combinations.

* Install PostgreSQL.
* For easier PostgreSQL administration, install phpPgAdmin.
* Install tomcat. (Do not forget .)
* Download the XWiki WAR file.
* Rename the WAR file to .
* Move the WAR file into the  directory.
* Tomcat should automatically extract the WAR file. If not, restart Tomcat.
* At this point, you may find that a  directory has appeared in . Delete it.
* As root:

* Inside the  directory:
** Open the  file and alter the  field to read .
** Open the  file and:
*** Comment-out the section entitled "Configuration for the default database".
*** Uncomment the section entitled "PostgreSQL Configuration".
*** Modify the database name (in ), username, and password as desired.
* Create a role and database in PostgreSQL to match the hibernate configuration.
* Install  from the Arch User Repository.
* As root:

* Restart .
* Launch the XWiki application by clicking on  in Tomcat Manager.
* The XWiki is started with XWiki Wizard Guide to finish your configuration.

## Nginx proxy configuration - Solution 1
The official Nginx guide for XWiki is not correct. There is an alternative solution which works for XWiki.

* Configure nginx site  configuration file.
{{hc|/etc/nginx/sites-available/xwiki|
server {
  listen 80 default_server;
  server_name xwiki.;
  return 301 https://$host$request_uri;
}

server {
  listen ssl;
  listen 443 ssl;

  server_name xwiki.;

  # SSL Certificate section
  ssl_certificate ...
  ssl_certificate_key ...

  location = / {
    return 301 https://$host/xwiki;
  }

  location /xwiki {
    proxy_set_header   X-Real-IP $remote_addr;
    proxy_set_header   Host      $host;
    proxy_http_version 1.1;
    proxy_set_header   Upgrade $http_upgrade;
    proxy_set_header   Connection 'upgrade';
    proxy_cache_bypass $http_upgrade;
    proxy_set_header   X-Forwarded-Host $host;
    proxy_set_header   X-Forwarded-Server $host;
    proxy_set_header   X-Real-IP $remote_addr;
    proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header   X-Forwarded-Proto $scheme;
    proxy_pass         http://127.0.0.1:8080/xwiki;
  }
}
}}
* Activate a server block in  directory .
* Restart Nginx.

## Nginx proxy configuration - Solution 2
I found that instructing nginx to proxy to  did not work: the generated URLs were incorrect. Contrary to what is indicated in the [https://www.xwiki.org/xwiki/bin/view/Documentation/AdminGuide/Configuration/#HReverseproxysetup XWiki documentation, I could not make the URLs correct through the use of HTTP headers.

The only solution I'm aware of so far is to create a new  element in Tomcat's  file:
* Duplicate the existing  element and alter the  attribute to read .
* Alter the  attribute to read .
* Move the  application from  to .
* Restart Tomcat
* Add  as an alias to localhost in  (add it to the end of the 127.0.0.1 line).
* Instruct Nginx to proxy to  instead.
