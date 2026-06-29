# Diaspora

Diaspora is the privacy aware, personally controlled, do-it-all, open source social network.

## Prerequisites
* Since Diaspora can run on MySQL and PostgreSQL you need to decide which one you want to use. Install one of them and set it up.
* Diaspora starts a so called appserver, on port 3000 by default, which serves the dynamic contents. You need a reverse proxy to handle the static content and that forwards requests it cannot handle to the appserver. Typical tools for that are Apache HTTP Server or Nginx.

## Installation
Install  or .

Now edit   and fill out the needed values. Then edit  and change at least the url setting to the URL your installation will be reachable under (the one served by your reverse proxy). You can change the port the appserver will listen on under the server section. By default Diaspora requires a SSL setup, you can disable that with the require_ssl setting.

Ensure your database is running and then switch to the diaspora user:

 $ su - diaspora

Create the database and initialize the schema:

 $ bin/bundle exec rake db:create db:migrate

If the user you specified in the  file cannot create databases leave the  out and create a database named diaspora_production by hand.

You can now switch back to your regular user and start .

The static content your reverse proxy needs to serve will be available under .

## Updating
Updating is very analogous. Obtain the newest version of the package and build it, just like in the installation instructions. Watch for .pacnew files and review the changes. Also read the changelog over at Diaspora. Then again ensure the database is running and switch to the diaspora user:

 $ su - diaspora

And update the database schema:

 $ RAILS_ENV=production bin/bundle exec rake db:migrate

Exit and restart diaspora systemd service.

If you notice missing icons or layout issues after restarting the service, switch to the diaspora user again and run:

 $ RAILS_ENV=production bin/bundle exec rake assets:precompile

Once more, exit and restart diaspora systemd service.

## Add yourself as an admin
Switch to the diaspora user and start the Rails console:

 $ su - diaspora
 $ bin/bundle exec rails console production

Then run the following command, replacing user with your username (only lowercase characters):

 Role.add_admin User.where(username: "user").first.person

You can exit the Rails console by pressing .

## Troubleshooting
## GDM login screen with Diaspora
GDM will insert the user diaspora in its login window because it currently considers the id range 500-1000 as normal users while Arch considers this range for system users as defined in /etc/login.defs. GDM does that probably to keep legacy normal users working.
To exclude this user from the login window, add this 'Exclude' line in your  file:

 greeter
 Exclude=diaspora
