# Node.js

Node.js is a JavaScript runtime environment combined with useful libraries. Node.js uses Google V8 engine to execute code outside of the web browser. Due to its event-driven, non-blocking I/O model, it is suitable for real-time web applications.

## Installation
Install the  package. There are long-term support (LTS) releases, too:

* —version 24.x
* —version 22.x
* —version 20.x

## Node version manager
It is not uncommon to need or desire to work in different versions of Node.js. A preferred method among Node.js users is to use Node Version Manager (), which allows for cheap and easy alternative installs. You can set nvm up by adding this to your Command-line shell#Configuration files:

 . /usr/share/nvm/init-nvm.sh

Usage is well documented on the project's GitHub but is as simple as:

 $ nvm install 8.0
 Downloading and installing node v8.0.0...
 $ nvm use 8.0
 Now using node v8.0.0 (npm v5.0.0)

If you want to run  automatically every time there is a  file on the directory, add [https://stackoverflow.com/a/50378304 this in shell initialization files.

## Node packaged modules
npm is the official package manager for Node.js. It can be installed with the  package.

## Managing packages with npm
## Installing packages
Any package can be installed using:

 $ npm install packageName

This command installs the package in the current directory under  and executables under .

For a system-wide installation global switch  can be used:

 # npm -g install packageName

By default this command installs the package under  and requires root privileges to do so. (If using a secure umask like , you will need to set up a permissive sudo umask for the package to be usable.)

## Allow user-wide installations
To allow global package installations for the current user, set the  environment variable. This is used by both npm and yarn.

Re-login or source to update changes.

You can also specify the  parameter for . However, this is not recommended, since you will need to add it every time you install a global package.

 $ npm -g install packageName --prefix ~/.local

Another option is to set  field in . This achieves the same effect as using  in one's :

 $ npm set prefix="$HOME/.local"

## Updating packages
Updating packages is as simple as

 $ npm update packageName

For the case of globally installed packages ()

 # npm update -g packageName

## Updating all packages
However, sometimes you may just wish to update all packages, either locally or globally. Leaving off the packageName  will attempt to update all packages

 $ npm update

or add the  flag to update globally installed packages

 # npm update -g

## Removing packages
To remove a package installed with the  switch simply use:

 # npm -g uninstall packageName

to remove a local package drop the switch and run:

 $ npm uninstall packageName

## Listing packages
To show a tree view of the installed globally packages use:

 $ npm -g list

This tree is often quite deep. To only display the top level packages use:

 $ npm -g list --depth=0

To display obsolete packages that may need to be updated:

 $ npm -g outdated

## Managing packages with pacman
Some Node.js packages can be found in Arch User Repository (AUR) with the name .

See the Node.js package guidelines for best practices in packaging Node.js packages for AUR.

## Troubleshooting
## npm help does not display documentation
Using  may not display the documentation for topic.  Instead, use .  For example:

 $ npm help install
 Top hits for "install"
 ...
 $ man npm-install
 ... shows the documentation for the npm install subcommand

This is a bug with Arch's npm package.

## node-gyp errors
In case of errors like ,  option might help:

 # npm install --unsafe-perm -g node-inspector

## Cannot find module ... errors
Since npm 5.x.x. package-lock.json file is generated along with the package.json file. Conflictions may arise when the two files refer to different package versions. A temporary method to solving this problem has been:

 $ rm package-lock.json
 $ npm install

However, fixes were made after npm 5.1.0 or above. For further information, see:
missing dependencies
