# Wordpress

WordPress is a free and open source content management system (CMS) created by Matt Mullenweg and first released in 2003. WordPress has a vast and vibrant community that provides tens of thousands of free plugins and themes to allow the user to easily customize the appearance and function of their WordPress CMS. WordPress is licensed under the GPLv2.

The biggest feature of WordPress is its ease in configuration and administration. Setting up a WordPress site takes five minutes. The WordPress administration panel allows users to easily configure almost every aspect of their website including fetching and installing plugins and themes. WordPress provides effortless automatic updates.

## Installation
WordPress requires Apache HTTP Server, PHP and MariaDB to be installed and configured. See the respective pages for information. During PHP configuration, be aware that some WordPress features require PHP extensions that may not be turned on by default.

Install the  package.

## Configuration
The configuration method used here assumes you are using WordPress on a local network.

## Host config
Make sure your  file is setup correctly. This will be important when accessing your WordPress CMS from a local network. Your  file should look something like the following,

## Configure Apache
You will need to create a configuration file for Apache to find your WordPress install. Create the following file and edit it your favorite text editor:

Change  in the first line to whatever you want. For example,  would require that you navigate to  to see your WordPress website.

Also change the paths to your WordPress install folder in case you did a manual install. Do not forget to append the parent directory to the  variable as well as shown below.

Next edit the Apache HTTP Server configuration file and add the following:

Since the WordPress index is written in PHP add the following line within the  block:

Now restart  (Apache).

## Configure Nginx
Example server block configuration from https://www.nginx.com/resources/wiki/start/topics/recipes/wordpress/:

 # Upstream to abstract backend connection(s) for php
 upstream php {
        server unix:/tmp/php-cgi.socket;
        server 127.0.0.1:9000;
 }

 server {
        ## Your website name goes here.
        server_name domain.tld;
        ## Your only path reference.
        root /var/www/wordpress;
        ## This should be in your http block and if it is, it's not needed here.
        index index.php;

        location = /favicon.ico {
                log_not_found off;
                access_log off;
        }

        location = /robots.txt {
                allow all;
                log_not_found off;
                access_log off;
        }

        location / {
                # This is cool because no php is touched for static content.
                # include the "?$args" part so non-default permalinks doesn't break when using query string
                try_files $uri $uri/ /index.php?$args;
        }

        location ~ \.php$ {
                #NOTE: You should have "cgi.fix_pathinfo = 0;" in php.ini
                include fastcgi_params;
                fastcgi_intercept_errors on;
                fastcgi_pass php;
                #The following parameter can be also included in fastcgi_params file
                fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        }

        location ~* \.(js|css|png|jpg|jpeg|gif|ico)$ {
                expires max;
                log_not_found off;
        }
 }

## Configure MariaDB
MariaDB can be configured using a plethora of tools, but the most common are the command-line or phpMyAdmin.

## Using MariaDB command-line tool
First, login as root. You will be asked for your MariaDB root password:

 $ mysql -u root -p

Then create a user and database:

See WordPress.org for details.

## Using phpMyAdmin
See phpMyAdmin to install and configure phpMyAdmin.

In your web browser, navigate to your phpMyAdmin host and perform the following
steps:

# Login to phpMyAdmin.
# Click "user" and then click "Add user".
# Give the pop up window a name and a password.
# Select "Create database with same name and grant all privileges".
# Click the "Add user" button to create the user.

## WordPress installation
Once you have set up your http server, php, and mariadb, it is time to install and configure WordPress itself.

The WordPress installation procedure will use the URL in the address field of your web browser as the default website URL. If you have navigated to http://localhost/wordpress, your website will be accessible from your local network, but it will be broken in appearance and function.

# Navigate to .
# Click the "Create a Configuration File" button.
# Click the "Let's go!" button.
# Fill in you database information created in the previous section
# Click "Submit".

If you installed , then this setup procedure will not have the correct permissions to create the  file used by WordPress. You will have to do this step yourself as root using information WordPress will provide.

A page will appear saying WordPress can not write the  file. Copy the text in the edit box and open  as  in your text editor. Paste the copied text into the editor and save the file.

After that, you will have to change permissions of the  and all the files inside it to user  and group  by using chown so that the webserver can access it:

 # chown http:http -R /usr/share/webapps/wordpress/

Finally, Click "Run the install" and WordPress will populate the database with your information. Once complete, you will be shown "Success!" page. Click the login button to finish your installation.

Now would be a good time to access your website from all your devices to be sure your WordPress installation is setup correctly.

## Usage
## Installing a theme
## Finding new themes
There are tens of thousands of themes available for WordPress. Searching on google for a good theme can be like wading through a river filled with trash. Good places for looking for themes include:

* [https://wordpress.org/themes/ Official WordPress theme website
* Smashing Magazine
* The Theme Factory
* Woo Themes

## Install using the admin panel
Before installing a theme using the admin panel, you will need to setup an FTP server on your WordPress host. To maintain a high level of protection, you might set up a user on your system specifically for WordPress, give it the home directory of , disallow anonymous login, and allow no more users to log in than for WordPress (and obviously others as required by your setup).

Once the FTP server is setup, login to your WordPress installation and click "Appearance->Install Themes->Upload". From there select your zip file that contains your theme and click "Install Now". You will be presented with a box asking for FTP information, enter it and click "Proceed".  You might need to update file ownership and rights if WordPress reports that it is unable to write to the directory. If you have been following along closely, you should now have an installed theme. Activate it if you wish.

## Install manually
Download the archive and extract into the  folder:

 $ cd /path/to/wordpress/root/directory
 $ cd wp-content/themes

Get the theme archive and extract:

 $ wget http://www.example.com/MyTheme.zip
 $ unzip MyTheme.zip

Remove the archive (optional):

 $ rm MyTheme.zip

Be sure to follow any additional instructions as provided by the theme author.

Select your new theme from the theme chooser (Appearance > Themes).

## Installing a plugin
The steps for installing a plugin are the same as they are for installing a theme. Just click the "Plugins" link in the left navigation bar and follow the steps.

## Updating
Every now and then when you log into wordpress there will be a notification informing you of updates. If you have correctly installed and configured an FTP client, and have the correct filesystem permissions to write in the WordPress install path then you should be able to perform updates at the click of a button. Just follow the steps.

Alternatively, you can use SSH to update your installation with the SSH SFTP Updater Support plugin.

## Troubleshooting
## Appearance is broken (no styling)
Your WordPress website will appear to have no styling to it when viewing it in a web browser (desktop or mobile) that does not have its hostnames mapped to ip addresses correctly.

This occurs because you used a url with the hostname of your server, instead of an ip address, when doing the initial setup and WordPress has used this as the default website URL.

To fix this, you will either need to edit your /etc/hosts file or setup a proxy server. See Squid.

Another option is changing a value in the database table of your WordPress, specifically the wp_options table. The fix is to change the siteurl option to point directly to the domain name and not "localhost".

## Plugins are unable to install: Could not create directory
Your WordPress site need appropriate permissions to your local files. It does not have the permissions to create files/directory. Apache with Arch uses the user `http`.

To give the appropriate permissions run the following command:

 # chown -R http:http your-wordpress-directory/wp-content

In addition, if you use a setup with php-fpm (as of version 7.4), you need to override the php-fpm systemd unit file, as php-fpm is hardened, making /usr read-only. Edit  and add the following lines to the file:

## Cannot save plugins to localhost
WordPress uses by default only a ftp server to download plugins. In order to also download them locally append the following config:

## There has been an error cropping your image.
Wordpress needs `php-gd` to modify images. Install , then enable the extension by uncommenting the following line in :

 extension=gd

## Call to undefined function mysql_connect()
You can usually see this error if you are using mysql/mariadb with php>=7.0.0 and have debug enabled in wordpress config.

This issue can be solved by uncommenting the following line in :

  extension=mysqli

## 502 Gateway Error after starting nginx
This can be caused due to the php upstream defined as  in the nginx configuration file not being installed and configured.

Install the  package. Open the following file and go to the line:

Change it to:

Enable and Restart .

Restart .

## Tips and tricks
## WP-CLI
WP-CLI is the command-line interface for WordPress. You can update plugins, configure multisite installations and much more, without using a web browser.
