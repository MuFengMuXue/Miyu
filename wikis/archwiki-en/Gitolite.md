# Gitolite

Gitolite allows you to host Git repositories for multiple users easily and securely.

## Installation
Install the  package.

## Configuration
Installing gitolite automatically adds the gitolite user to the system, with home directory .

## Admin SSH access
To give yourself admin access, copy your SSH public key to , where  is your username.

 # install -o gitolite -g gitolite ~/.ssh/id_rsa.pub /var/lib/gitolite/username.pub

Then run the Gitolite setup script as the gitolite user:

 gitolite setup -pk /var/lib/gitolite/username.pub

This puts your public key into the gitolite-admin keydir and gives your username RW+ access to the gitolite-admin repository

You can now remove the copy of your SSH public key:

 # rm /var/lib/gitolite/username.pub

Now as your user you can check that everything went correctly

Do not add repositories or users directly as gitolite on the server! The server must be managed by cloning the special gitolite-admin repository:

 $ git clone gitolite@hostname:gitolite-admin

For reference see [https://github.com/sitaramc/gitolite/ Gitolite.

## Create a repository
To create a repository, first check out the  repository as a client.

 $ git clone gitolite@server:gitolite-admin

Append a new repository to :

 repo repository_name
     RW+     =   @all

Commit and push the changes and gitolite will automatically generate the necessary files on the server.

## Adding http(s) access via Apache (with basic authentication)
We need to create an suEXEC wrapper script. To satisfy suEXEC's security requirements, the script and the directory containing it must be owned by  and below  in the directory hierarchy. For this example, we create the directory as .
 # install -o gitolite -g gitolite -d /srv/http/git/cgi-bin

Create an suEXEC wrapper for the gitolite shell with the contents below. For this example, we create it as .

Make the wrapper executable and owned by .
 # chown gitolite:gitolite /srv/http/git/cgi-bin/gitolite-suexec-wrapper
 # chmod 0755 /srv/http/git/cgi-bin/gitolite-suexec-wrapper

Create an empty password database file, owned by
 # install -o gitolite -g http -m 0640 /dev/null /srv/http/git/htpasswd

Apache's basic authentication mechanism is separate from ssh, and therefore requires a separate set of credentials. Create your web users using .
 # htpasswd /srv/http/git/htpasswd username

Add the following to your Apache vhost configuration:

Restart .

Finally, in the gitolite-admin repository you cloned in the previous section, edit , add an  access rule to all repositories you want to make available via http, and push the changes.

## Add users
## ssh users
Ask each user who will get access to send you an SSH public key. Rename each public key to , where  is the user name which will be used in . Then move all new public keys to the  directory in the cloned  repository. You can also organize them into various sub-directories of  if you wish, since the entire tree is searched.

Finally commit and push the changes.

See the add/remove users in the official documentation for details.

To grant access rights to the new users, edit the configuration file ( in the  repository). See the .conf file in the official documentation for details.

## http(s) users
User management for http(s) is more suitable for single-user setups. To add a new user or to change an existing user's password:
 # htpasswd /srv/http/git/htpasswd username

## Troubleshooting
In case you cannot log in with the gitolite account, it may be caused by the account being locked, and depending of your ssh configuration.

If you have done some SSH hardening, it may be the cause of this behavior, as noted in SSH and locked users Article and Unix & Linux StackExchange - How to unlock account for public key ssh authorization, but not for password authorization.

To solve this, you have to allow PAM in  or unlock the account by:

 # usermod -p '*' gitolite
