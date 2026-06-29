# Ruby on Rails

Ruby on Rails, often shortened to Rails or RoR, is an open source web application framework for the Ruby programming language. It is intended to be used with an Agile development methodology that is used by web developers for rapid development.

## Installation
Ruby on Rails requires Ruby to be installed, so read that article first for installation instructions. The  package is also required if using uglifier (Ruby wrapper for UglifyJS JavaScript compressor, optional)
The Rails framework is linked to a version of Ruby (or the system Ruby installation).
Ruby version(s) installed can be from system or from rbenv or from rvm (Ruby Version Manager).

## RubyGems
The following command will install Rails for the current user:

 $ gem install rails

Make sure you add the Ruby gem binary to PATH.

Building the documentation takes a while. If you want to skip it, append  to the install command.

 $ gem install rails --no-document

gem is a package manager for Ruby modules, somewhat like pacman is to Arch Linux. To update your gems, simply run:

 $ gem update

## Pacman
Install the  package. Alternatively, see Ruby#Managing RubyGems using pacman.

## Quarry binary repository
Install ruby-rails from the unofficial quarry repository.

## Configuration
Rails is bundled with a basic HTTP server called Puma. You can create a test application to test it. First, create an application with the rails command:

 $ rails new testapp_name

This creates a new folder inside your current working directory.

 $ cd testapp_name

Next start the web server. It listens on port 3000 by default:

 $ rails server

Now visit the testapp_name website on your local machine by opening http://localhost:3000 in your browser

A test-page should be shown greeting you "Welcome aboard".

## Application servers
There are several choices for Rails application servers, but there are some common “things to consider” regardless of the choice:

# One typically want to allow a program to continue after logoff for servers, such as  or systemd.
# For easily deploying app in production mode, you can try capistrano.
# One can always put a Web server like Nginx, Apache, or Lighttpd, in front of the application server for reverse proxy. For example, this is useful if serving multiple web applications on a single machine.

## Thin
Thin is a fast and very simple Ruby web server.

First install thin gem:
 $ gem install thin

Then start it using:
 $ thin start

## Unicorn
Unicorn is an application server that cannot talk directly to clients. Instead, a web server must sit between clients and Unicorn, proxying requests as needed. Unicorn is loosely based on Mongrel. It is used by Github, and it uses an architecture that tries hard to find the best child for handling a request. Explanation of differences between Unicorn and Mongrel.

Install the Unicorn gem:
 # gem install unicorn

Then create a configuration file for your application in . For example; here is a configuration example based on this tutorial for Redmine:

{{hc|/etc/unicorn/redmine.ru|
working_directory "/srv/http/redmine"
pid "/tmp/redmine.pid"

preload_app true
timeout 60
worker_processes 4
listen 4000
stderr_path('/var/log/unicorn.log')

GC.respond_to?(:copy_on_write_friendly=) and GC.copy_on_write_friendly = true

after_fork do |server, worker|
	#start the worker on port 4000, 4001, 4002 etc...
	addr = "0.0.0.0:#{4000 + worker.nr}"
	# infinite tries to start the worker
	server.listen(addr, :tries => -1, :delay => -1, :backlog => 128)

	#Drop privileges if running as root
	worker.user('nobody', 'nobody') if Process.euid == 0
end
}}

Start it using:
 # /usr/bin/unicorn -D -E production -c /etc/unicorn/redmine.ru
where  means “daemonize”.

## Apache/Nginx (using Phusion Passenger)
Phusion Passenger is a module available for Nginx and Apache HTTP Server, that greatly simplifies setting up a Rails server environment. Nginx does not support modules as Apache and has to be compiled with  in order to support Passenger; let Passenger compile it for you. As for Apache, let Passenger set up the module for you.

Two differents choices (one or the other, not both in same time):

# Install the  package.
# Installing the 'passenger' gem from any version of ruby (user setting):

If you are aiming to use Apache HTTP Server, install the  package (if passenger is not installed from gem), and run:
 # passenger-install-apache2-module

In case a rails application is deployed with a sub-URI, like http://example.com/yourapplication, some additional configuration is required, see the Passenger documentation.

For Nginx, install the  package (if passenger is not installed from gem), and run:
 # passenger-install-nginx-module

The installer will provide you with any additional information regarding the installation (such as installing additional libraries).

To serve an application with Nginx, configure it as follows:
{{bc|
server {
    server_name app.example.org;
    root path_to_app/public; # Be sure to point to 'public' folder!
    passenger_enabled on;
    rails_env development; # Rails environment.
}
}}

## Puma
Puma (Github Page) is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for Ruby/Rack applications, and is considered the replacement for Webrick and Mongrel. It was designed to be the go-to server for Rubinius, but also works well with JRuby and MRI. The reverse proxy server would act as a load balancer that routes all external requests to a pool of web apps.

For a webserver it is better to use a server user and group, check Users and groups#Example adding a user, below use  as user name and  as group name, also  as rails app name.

Start by copying your app to /var/www/my_app. And set new ownership with
 # cd /var/www/
 # chown -R rails:server my_app

and permission for user with
 # chmod -R 775 my_app

Then add  in the Gemfile and install with
 $ cd my_app
 $ bundle install

Create file , copy codes below and modify as you like:
{{bc|
# Change to match your CPU core count
# You can check available worker numbers with $ grep -c processor /proc/cpuinfo
# also see the comment in the nginx.conf
workers 2

# Min and Max threads per worker
#threads 1, 6

app_dir = File.expand_path("../..", __FILE__)
shared_dir = "#{app_dir}/shared"

# Default to production
#rails_env = ENV|| "production"
#environment rails_env

# Set up socket location
bind "unix://#{shared_dir}/sockets/puma.sock"

# Logging
#stdout_redirect "#{shared_dir}/log/puma.stdout.log", "#{shared_dir}/log/puma.stderr.log", true

# Set master PID and state locations
pidfile "#{shared_dir}/pids/puma.pid"
#state_path "#{shared_dir}/pids/puma.state"
#activate_control_app

#on_worker_boot do
#  require "active_record"
#  ActiveRecord::Base.connection.disconnect! rescue ActiveRecord::ConnectionNotEstablished
#  ActiveRecord::Base.establish_connection(YAML.load_file("#{app_dir}/config/database.yml")[rails_env)
#end}}

Start server with
 $ bundle exec puma -C config/puma.rb

You can also run it in background with parameter  and check with
 $ pgrep puma
when you want to  it.

## Databases
Most web applications will need to interact with some sort of database. ActiveRecord (the ORM used by Rails to provide database abstraction) supports several database vendors, the most popular of which are MySQL, SQLite, and PostgreSQL.
And then you will have next to configure the file "config/database.yml" for Rails application web site able to connect on your database.

## SQLite
SQLite is the default lightweight database for Ruby on Rails. To enable SQLite, simply install .

## PostgreSQL
Install and configure PostgreSQL.

Install for Rails:
 # gem install pg

Or add the gem inside your Gemfile of your project, then use bundle.

create a new Rails web site:
 # rails new my_web_site -d postgresql

## MySQL
First, install and configure a MySQL server. Please refer to MariaDB on how to do this.

A gem with some native extensions is required, probably best installed as root:
 # gem install mysql

You can generate a rails application configured for MySQL by using the  parameter:
 $ rails new testapp_name -d mysql

## Database Access Configuration
What ever Database (MySQL or Postgresql or SQlite (the default one) you use, you then need to edit . Rails uses different databases for development, testing, production and other environments. Here is an example development configuration for MySQL running on localhost:

  default:
    adapter: mysql (or postgresql or sqlite)
    username: my_user_name_access
    password: my_secret_password

For safety reasons, it is a good practice to not directly put password (who will be no more secret) as clear text in a text file.
Instead you can replace "my_secret_password' by "''" where MYSQL_PASSWD can be an environment variable exported from the user environment the server use (~/.profile or ~/.bashrc or ~/.zshrc depend of your choice and utility). Surrounding  by  searve in case of your password has some special chars like  or , etc...

## Create the databases from Rails
Note that you do not have to actually create the database using MySQL or Postgresql or Sqlite, as this can be done via Rails directly with:

For rails-4.X version:
 # rake db:create

For rails-5.X version:
 # rails db:create

If no errors are shown, then your database has been created and Rails can talk to your database.

## The Perfect Rails Setup
Phusion Passenger running multiple Ruby versions.

* Arch Linux: A simple, lightweight distribution. ;)
* Nginx: A fast and lightweight web server with a strong focus on high concurrency, performance and low memory usage.
* Passenger (a.k.a. mod_rails or mod_rack): Supports both Apache and Nginx web servers. It makes deployment of Ruby web applications, such as those built on Ruby on Rails web framework, a breeze.
* Ruby Version Manager (RVM): A command-line tool which allows you to easily install, manage, and work with multiple Ruby environments from interpreters to sets of gems. RVM lets you deploy each project with its own completely self-contained and dedicated environment —from the specific version of ruby, all the way down to the precise set of required gems to run your application—.
* SQLite: The default lightweight database for Ruby on Rails.

## Step 0: SQLite
Install .

## Step 1: RVM
Make a multi-user RVM installation as specified here.

In the 'adding users to the rvm group' step, do
 # usermod -a -G rvm http
 # usermod -a -G rvm nobody

 and  are the users related to Nginx and Passenger, respectively.

## Step 2: Rubies
Once you have a working RVM installation in your hands, it is time to install the latest Ruby interpreter

 $ rvm install 2.0.0

## Step 3: Nginx with Passenger support
Run the following to allow passenger install nginx:
 $ rvm use 2.0.0
 $ gem install passenger
 $ rvmsudo passenger-install-nginx-module

The passenger gem will be put into the default gemset.

This will download the sources of Nginx, compile and install it for you. It will guide you through all the process. Note that the default location for Nginx will be .

After completion, add the following two lines into the 'http block' at  that look like:

 http {
   ...
   passenger_root /usr/local/rvm/gems/ruby-2.0.0-p353/gems/passenger-3.0.9;
   passenger_ruby /usr/local/rvm/wrappers/ruby-2.0.0-p353/ruby;
   ...
 }

## Step 4: Gemsets and Apps
For each Rails application you should have a gemset. Suppose that you want to try RefineryCMS against BrowserCMS, two open-source Content Management Systems based on Rails.

Install RefineryCMS first:

 $ rvm use 2.0.0@refinery --create
 $ gem install rails -v 4.0.1
 $ gem install passenger
 $ gem install refinerycms refinerycms-i18n sqlite3

Deploy a RefineryCMS instance called refineria:

 $ cd /srv/http/
 $ rvmsudo refinerycms refineria

Install BrowserCMS in a different gemset:

 $ rvm use 2.0.0@browser --create
 $ gem install rails -v 4.0.1
 $ gem install passenger
 $ gem install browsercms sqlite3

Deploy a BrowserCMS instance called navegador:

 $ cd /srv/http/
 $ rvmsudo browsercms demo navegador
 $ cd /srv/http/navegador
 $ rvmsudo rake db:install

## Passenger for Nginx and Passenger Standalone
Observe that the passenger gem was installed three times and with different intentions; in the environments
* 2.0.0 => for Nginx,
* 2.0.0@refinery => Standalone
* 2.0.0@browser => Standalone

The strategy is to combine Passenger for Nginx with Passenger Standalone. One must first identify the Ruby environment (interpreter plus gemset) that one uses the most; in this setup the Ruby interpreter and the default gemset were selected. One then proceeds with setting up Passenger for Nginx to use that environment (step 3).
* Applications within the chosen environment can be served as in Apache/Nginx (using Phusion Passenger), page up in this article.
* All applications that are to use a different Ruby version and/or gemset can be served separately through Passenger Standalone and hook into the main web server via a reverse proxy configuration (step 6).

## Step 5: .rvmrc files and ownerships
This step is crucial for the correct behaviour of the setup. RVM seeks for .rvmrc files when changing folders; if it finds one, it reads it. In these files normally one stores a line like
 rvm @
so the specified environment is set at the entrance of applications' root folder.

Create /srv/http/refineria/.rvmrc doing
 # echo "rvm ree@refinery" > /srv/http/refineria/.rvmrc
, and /srv/http/navegador/.rvmrc with
 # echo "rvm 2.0.0@browser" > /srv/http/navegador/.rvmrc
You have to enter to both application root folders now, because every first time that RVM finds a .rvmrc it asks you if you trust the given file, consequently you must validate the two files you have just created.

These files aid the programs involved to find the correct gems.

Apart, if applications' files and folders are not owned by the right user you will face database write-access problems. The use of rvmsudo produces root-owned archives when generated by Rails; in the other hand, nobody is the user for Passenger —if you have not changed it—: who will use and should posses them. Fix this doing
 # chown -R nobody.nobody /srv/http/refineria /srv/http/navegador

## Step 6: Reverse proxies
You have to start the Passenger Standalone web servers for your applications. So, do
 $ cd /srv/http/refineria
 $ rvmsudo passenger start --socket tmp/sockets/passenger.socket -d
and
 $ cd /srv/http/navegador
 $ rvmsudo passenger start --socket tmp/sockets/passenger.socket -d
. The first time that you run a Passenger Standalone it will perform a minor installation.

Note that you are using unix domain sockets instead of the commonly-used TCP sockets; it turns out that unix domain are significantly faster than TCP sockets.

## Launch Passenger Standalone daemons at system start-up
Do you have a script? Please post it here.

The systemd script below was made for a Typo blog I host at /srv/http/typo. It is located at /etc/systemd/system/passenger_typo.service. I set the Environment= tags (see "man systemd.exec") from the output of "rvm env". The only exception was PATH=, which I had to combine from my regular PATH and the output of rvm env.

Note: If you do not set the "WorkingDirectory=" variable to your application folder, passenger will fail to find your app and will subsequently shut itself down.

## Step 7: Deployment
## With subdomains
Once again edit /opt/nginx/conf/nginx.conf to include some vital instructions:

{{bc|
## RefineryCMS ##

server {
    server_name refinery.domain.com;
    root /srv/http/refineria/public;
    location / {
        proxy_pass http://unix:/srv/http/refineria/tmp/sockets/passenger.socket;
        proxy_set_header Host $host;
    }
}

## BrowserCMS ##

server {
    server_name browser.domain.com;
    root /srv/http/navegador/public;
    location / {
        proxy_pass http://unix:/srv/http/navegador/tmp/sockets/passenger.socket;
        proxy_set_header Host $host;
    }
}
}}

## Without subdomains
If you for some reason do not want to host each application on its own subdomain but rather in a url like:  then you could do something like this in your config:

{{bc|
server {
    server_name site.com;
    #Base for the html files etc
    root /srv/http/;

    #First application you want hosted under domain site.com/railsapp
    location /railsapp {
        root /srv/http/railsapp/public;
        #you may need to change passenger_base_uri to be the uri you want to point at, ie:
        #passenger_base_uri /railsapp;
        #but probably only if you are using the other solution with passenger phusion
        proxy_pass http://unix:/srv/http/railsapp/tmp/sockets/passenger.socket;
        proxy_set_header Host $host;
    }

    #Second application you want hosted under domain site.com/anotherapp
    location /anotherapp {
        root /srv/http/anotherapp/public;
        #same thing about the passenger_base_uri here, but with value /anotherapp instead
        proxy_pass http://unix:/srv/http/anotherapp/tmp/sockets/passenger.socket;
        proxy_set_header Host $host;
    }
}
}}

At this point you are in conditions to start the  service and to access both CMSs through refinery.domain.com and browser.domain.com.
