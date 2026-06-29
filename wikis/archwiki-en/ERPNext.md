# ERPNext

ERPNext is an open source ERP software licensed under GPL3 which is accessed via the web browser. Functionalities are separated into logical sections which makes it convenient to only choose those capabilities which are needed. This enables many different use cases.

There is plenty of documentation. Moreover, a forum serves as a gathering point for discussions among users.

In contrast to its alternative Odoo, it is completely open source and does not have a proprietary version.

## Installation
The MariaDB database must be started before installing the package .

Internally, the software is unusual to install because it uses its own installer .

You may want to use an HTTP server like Nginx or Apache to run ERPNext behind a reverse proxy.

## Dependencies
The installer uses a virtual environment for Python. Therefore, Python dependencies are not required system-wide.

## Bug (Access to database denied)
During the setup, a database needs to be created. This happens with the own user. For the database creation, the user "root" is needed. By default, it has set an empty password but is accessed via the user "root". As this is not possible in the installation, the user "root" needs to be set a password.

## Update
Updating requires manual action because the installation will fail if the software's database named "erpnext" already exists.

Save your database and delete it.

 # mariadb-dump -p -u root erpnext > /tmp/erpnext.sql
 # mariadb -e "DROP DATABASE erpnext;" -p -u root

Save your files and encryption key.

 # cp -r /usr/share/webapps/erpnext/sites/erpnext/private/ /tmp/erpnext-private/
 # cp -r /usr/share/webapps/erpnext/sites/erpnext/public/ /tmp/erpnext-public/
 # grep -Eo "^+\"encryption_key\": +$" /usr/share/webapps/erpnext/sites/erpnext/site_config.json > /tmp/erpnext-encryption_key.txt

Uninstall  and remove its lingering files.

 # rm -r /usr/share/webapps/erpnext/

Afterwards, install the package .

Now, restore your old database and files and remove the backups.

 # mariadb -e "DROP DATABASE erpnext;" -p -u root
 # mariadb -e "CREATE DATABASE erpnext;" -p -u root
 # mariadb -p -u root erpnext < /tmp/erpnext.sql
 # cp -r /tmp/erpnext-private/* /usr/share/webapps/erpnext/sites/erpnext/private/
 # cp -r /tmp/erpnext-public/* /usr/share/webapps/erpnext/sites/erpnext/public/
 # readonly encryption_key="$(cat /tmp/erpnext-encryption_key.txt)"
 # perl -0e "s|\"db_type\": \"mariadb\"|\"db_type\": \"mariadb\",\n${encryption_key//\"/\\\"}|g" -i -p /usr/share/webapps/erpnext/sites/erpnext/site_config.json
 # rm /tmp/erpnext.sql
 # rm -r /tmp/erpnext-private/
 # rm -r /tmp/erpnext-public/
 # rm /tmp/erpnext-encryption_key.txt

Upgrade the database.

 # tmux new-session -s erpnext "erpnext"
 # cd /usr/share/webapps/erpnext/
 erpnext$ bench migrate
 # tmux send-keys -t erpnext C-c

Ultimately, assure the correct ownership.

  # chown -R erpnext:erpnext /usr/share/webapps/erpnext/

## Removal
As the software creates files on its own pacman cannot keep track of all files. For a complete removal, run:

 # rm -r /usr/share/webapps/erpnext/

## Backup
Create a backup of the database, see MariaDB#Backup. Additionally, save your files which are located in  and .

## Usage
Start the executable . The root password is required to access the user "erpnext". The server runs and can be accessed via http://localhost:8000.
