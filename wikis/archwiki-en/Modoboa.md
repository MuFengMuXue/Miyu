# Modoboa

Modoboa is a mail hosting and management platform including a modern and simplified Web User Interface designed to work with Postfix and Dovecot.

For context, please see List of applications/Internet#Mail servers

When setting up this program is seems like the aur repo is a basic way to install the dependencies but lacks a lot of the system setup that you currently have to do manually. Here is a few details on how to setup modoboa as a system service.

## Installation
To install modoboa through pip please create a . You can also make a  user if you want to encapsulate the program.

Find a place to put modoboa then run:
 mkdir modoboa
 cd /modoboa
 virtualenv env
 . env/bin/activate.fish

Then once you are in the virtual environment install modoboa:

 pip install modoboa

If you feel inclined you can read the documentation. Additionally here is a link to the github for reference:
Modoboa-Github.

Once installing  you will have access to two command line utilities:

*
*

## Databases
Modoboa requires one of these databases:

* PostgreSQL
* MariaDB or MySQL
* SQLite

Please follow the installation process for whichever database you want to use and set it up before continuing.

## Using PostgreSQL
If you use PostgreSQL you must install the python dependency pip install psycopg[binary>3.1

Then create a user and datbase for modoboa to use:
 sudo -l -u postgres createuser --no-createdb modoboa
 sudo -l -u postgres createdb --owner=modoboa modoboa
## Using MySQL or MariaDB
For MySQL or MariaDB you must install the python dependency pip install mysqlclient

Once installed create an associated user:
 CREATE DATABASE modoboa;
 CREATE USER 'modoboa'@'localhost' IDENTIFIED  BY 'my-strong-password-here';
 GRANT ALL PRIVILEGES ON modoboa.* TO 'modoboa'@'localhost';

## Using SQLite
No required dependencies besides installing SQLite.

## Making a Modoboa Instance
To start with Modoboa, until the aur repo is fixed follow the instructions above on installing a virtual environment and pip install modoboa. Then you can proceed to creating the Django project.

## Building your Instance
Now deploy your modoboa. Once you have everything installed you can create an instance of the Django web-server using the command . This will create a Django project in the directory  in your working directory.

By default without introducing any database arguments Modoboa, it will prompt you for which database you want to use through an interactive console. If you use the SQLite method it will create a database in your working directory under the name .

 modoboa-admin.py deploy instance --collectstatic --domain
The interactive prompt will ask you which database you want and to start you can just use sqlite3 while you are setting up your system:
 Configuring database connection: default
 Database type (mysql, postgres or sqlite3): sqlite3

## Specifying a Sqlite Location
Alternatively, you can specify the location of your SQLite database.

 modoboa-admin.py deploy instance --collectstatic --domain  --dburl default:sqlite:////full/path/to/your/database/file.sqlite

## Other Databases
If you are going to use an alternative database use this syntax  for the connection string. Here is a filled out example,
 modoboa-admin.py deploy instance_name --collectstatic --domain example.com --dburl default:postgres://user:pass@[localhost/modoboa

For more information on running the different databases see
 modoboa-admin.py help deploy

Or read the documentation

## Running the Django Instance
Before you can run modoboa you need to setup your webserver because it is dependent on your domain.

Once you have used  to create a  directory, you can  into the directory and there will be a  file which would be familiar to anyone who uses Django.

To view the various services in the django project you can run in the  directory:

 python manage.py

## Setting up Nginx
In this example we will use Gunicorn to run a unix socket for the modoboa webserver.
While in the virtual environment for modoboa, please install gunicorn to host the webserver. You can also use uwsgi.

 pip install gunicorn

Then we can setup a Nginx config accordingly. Make your configuration file however you do it. I have a  directory that I place config files then system link them to  which is included in the .

I placed the the following in

 upstream modoboa {
      server      unix:/var/run/gunicorn/modoboa.sock fail_timeout=0;
}

 server {
      server_name domain.com;
      root ;

      access_log  /var/log/nginx/modoboa.access.log;
      error_log /var/log/nginx/modoboa.error.log;

      location /sitestatic/ {
              autoindex on;
      }

      location /media/ {
              autoindex on;
      }

      location / {
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_set_header Host $http_host;
              proxy_redirect off;
              proxy_set_header X-Forwarded-Protocol ssl;
              proxy_pass http://modoboa;
      }
 }

Now for ssl you need to install  and the nginx plugin .
Then run
 sudo certbot --nginx run
To enable tls.
