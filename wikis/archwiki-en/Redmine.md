# Redmine

Redmine is a free and open source, web-based project management and issue tracking tool. It handles multiple projects and subprojects.  It features per project wikis and forums, time tracking, and flexible role based access control. It includes a calendar and Gantt charts to aid visual representation of projects and their deadlines. Redmine integrates with various version control systems and includes a repository browser and diff viewer.

Redmine is written using the Ruby on Rails framework. It is cross-platform and cross-database and supports 34 languages.

## Installation
This document will guide you through the suggested installation process of Redmine.

If for some reason you want to setup redmine manually, it is recommended to follow the official Installation Guide.

Although it is possible to run Redmine on its own for testing purposes, for production use it requires an SQL database as well as a web server.
As database it is recommended to use MariaDB or PostgreSQL.
The supported web servers are

* Ruby on Rails#Apache/Nginx (using Phusion Passenger)
* Ruby on Rails#Puma
* Ruby on Rails#Unicorn

## Installation
## Build and Installation
Install the  package.

In the following we assume user under which the redmine will be running is . The ruby commands are thus explicitly executed under this specific user's control.

## Database Configuration
Now, we will need to create the database that the Redmine will use to store your data. For now on, the database and its user will be named . But this names can be changed to anything else.

## Database Creation
To create the database, the user and set privileges:

For PostgreSQL:

## Database Access Configuration
Now you need to configure Redmine to access the database we just created. To do that you have to copy  to :

 # cd /usr/share/webapps/redmine/config
 # cp database.yml.example database.yml

And then edit this file in order to configure your database settings for "production" environment (you can configure for the "development" and "test" environments too, just change the appropriate sections).

Example for MariaDB and MySQL database:

Example for PostgreSQL database:

Example for an SQL Server database:

## Ruby gems
Redmine requires some RubyGems, however  comes prepackaged with all requirements.

## Session Store Secret Generation
Now you must generate a random key that will be used by Rails to encode cookies that stores session data thus preventing their tampering:

 # bundle exec rake generate_secret_token

## Database Structure Creation
With the database created and the access configured for Redmine, now it is time to create the database structure. This is done by running the following command under the application root directory:

 # cd /usr/share/webapps/redmine
 # chown -R http:http db # migration requires write access to db/schema.rb
 RAILS_ENV=production bundle exec rake db:migrate

These command will create tables by running all migrations one by one then create the set of the permissions and the application administrator account, named admin.

## Database Population with Default Data
Now you may want to insert the default configuration data in database, like basic types of  task, task states, groups, etc. To do so execute the following:

 [http$ RAILS_ENV=production bundle exec rake redmine:load_default_data

Redmine will prompt for the data set language that should be loaded; you can also define the REDMINE_LANG environment variable before running the command to a value which will be automatically and silently picked up by the task:

 RAILS_ENV=production REDMINE_LANG=de bundle exec rake redmine:load_default_data

## File System Permissions
The user account running the application must have write permission on the following subdirectories:

* files: storage of attachments.
* log: application log file production.log.
* tmp and tmp/pdf: used to generate PDF documents among other things (create these ones if not present).

The  comes preconfigured with permissions for user . In case you like to use a different user you need to change the ownership, e.g.

 # chown -R redmine:redmine files/ log/ tmp/

## Test the installation
To test your new installation using WEBrick web server run the following in the Redmine folder:

 [http$ ruby bin/rails server webrick -e production

Once WEBrick has started, point your browser to http://localhost:3000/. You should now see the application welcome page. Use default administrator account to log in: ''admin/admin''. You can go to Administration menu and choose Settings to modify most of the application settings.

## Configure the production server
## Puma / Unicorn
Puma and Unicorn are web servers based on Mongrel. For its increased speed and smaller memory footprint Puma is recommended. Both are very simple to setup, but for production use should be used in combination with a reverse proxy (Apache, Nginx, lighttpd, etc.).

 # gem install puma
 /opt/ruby2.6/bin/puma

For production, puma can be started as a systemd service:

Do a complete daemon-reload, then start/enable .

## Phusion Passenger
For Apache and Nginx, it is recommended to use [https://www.phusionpassenger.com/ Phusion Passenger. Passenger is a module available for Nginx and Apache HTTP Server.

Start by installing the 'passenger' gem:
 # gem install passenger

Now you have to look at your passenger gem installation directory to continue. If you do not known where it is, type:
 # gem env

And look at the  to find where the gems are installed. If you followed this guide and installed RVM, you can have more than one path, look at the one you are using.

For this guide so far, the gem path is .
 # cd /usr/local/rvm/gems/ruby-2.0.0-p247@global/gems/passenger-4.0.23

If you are aiming to use Apache HTTP Server, run:
 # passenger-install-apache2-module

In case a rails application is deployed with a sub-URI, like http://example.com/yourapplication, some additional configuration is required, see the Passenger documentation

For Nginx:
 # passenger-install-nginx-module

And finally, the installer will provide you with further information regarding the installation (such as installing additional libraries). So, to setup your server, simply follow the output from the passenger installer.

## Updating
Backup the files used in Redmine:
 # tar czvf ~/redmine_files.tar.gz -C /usr/share/webapps/redmine/ files

Backup the plugins installed in Redmine:
 # tar czvf ~/redmine_plugins.tar.gz -C /usr/share/webapps/redmine/ plugins

Backup the database:
 # mysqldump -u root -p  | gzip > ~/redmine_db.sql.gz

Update the  package as normal.

Update the gems requirements:
 #  bundle update

For a clean gems environment, you may want to remove all the gems and reinstall them. To go through this, do:
 # for x in `gem list --no-versions`; do gem uninstall $x -a -x -I; done

If you did the last step and removed all the gems, now you will need to reinstall them all:
 # gem install bundler
 # bundle install --without development test

Copy the saved files:
 # tar xzvf ~/redmine_files.tar.gz -C /usr/share/webapps/redmine/

Copy the installed plugins:
 # tar xzvf ~/redmine_plugins.tar.gz -C /usr/share/webapps/redmine/

Regenerate the secret token:
 # cd /usr/share/webapps/redmine
 # bundle exec rake generate_secret_token

Check for any themes that you may have installed in the  directory. You can copy them over but checking for updated version is ideal.

Update the database. This step is the one that could change the contents of your database. Go to your new redmine directory, then migrate your database:
 # RAILS_ENV=production REDMINE_LANG=pt-BR bundle exec rake db:migrate

If you have installed any plugins, you should also run their database migrations:
 # RAILS_ENV=production REDMINE_LANG=pt-BR bundle exec rake redmine:plugins:migrate

Now, it is time to clean the cache and the existing sessions:
 # RAILS_ENV=production bundle exec rake tmp:cache:clear tmp:sessions:clear

Restart the application server (e.g. puma, thin, passenger, etc). And finally go to "Admin -> Roles & permissions" to check/set permissions for the new features, if any.

## Troubleshooting
## Runtime error complaining that RMagick was configured with older version
If you get the following runtime error after upgrading ImageMagick  then you only need to reinstall (or rebuild as shown above if it is the case).

## Error when installing gems: Cannot load such file -- mysql2/mysql2
If you see an error like , you are having a problem with the installation of the database gem. Probably a misconfiguration in the Database Access Configuration step.
In this case you should verify the  file.

If this does not work, you can manually install the database gem by:

 # gem install mysql2

As a last resort, you can try to comment the line of the database gem and add a new one as below:

## Checkout SVN Source
Get the Redmine source (Download instructions). Here is method of installing Redmine directly from subversion in /srv/http/redmine/
 # useradd -d /srv/http/redmine -s /bin/false redmine
 # mkdir -p /srv/http/redmine
 # svn checkout https://svn.redmine.org/redmine/branches/2.1-stable /srv/http/redmine
 # chown -R redmine: /srv/http/redmine

## Automating The Update Process
Example of an after-update script:

 #!/usr/bin/bash
 export RAILS_ENV=production
 grep -E "^gem 'thin'" Gemfile || echo "gem 'thin'" >> Gemfile
 bundle update && bundle exec rake generate_secret_token db:migrate redmine:plugins:migrate tmp:cache:clear tmp:sessions:clear

## Creating a Systemd Unit
If you want to automatically run your application server when system starts, you need to create a systemd unit file.
