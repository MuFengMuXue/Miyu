# RVM

RVM (Ruby enVironment Manager) is a command line tool which allows us to easily install, manage and work with multiple Ruby environments from interpreters to sets of gems.

There exists a similar application that you may also want to consider: rbenv.

## Installation
The install process is very easy. You have two choices, one system-wide, another as a user. The first is for production servers, or if you are alone on your machine, you will need root privileges. The second is recommended for multiple users on the same machine (like a development test box). If you do not know which to choose then start with a single user installation.

The upstream instructions for installing RVM should just work. The install script is aware enough to tell you what packages you need to install on Arch Linux to make different rubies work. This usually involves gcc and some other stuff needed to compile ruby.

As an observation, installing RVM with gem is not recommended anymore. This article uses the recommended documentation with minor tweaks to make it work on Arch Linux.

## Pre-requisites
Before starting, you will need to install the following packages , , , ,  and  if not installed yet.

## Single-user installation
For most purposes, the recommended installation method is single-user, which is a self-contained RVM installation in a user's home directory.

Use the script that rvm docs recommends to install. Make sure to run this script as the user for whom you want RVM installed (i.e. your normal user that you use for development).

To check the script before running it, do:

 $ curl -L get.rvm.io > rvm-install

Inspect the file, and then run it with:

 $ bash

Group memberships are only evaluated at login time. Log the users out, then back in. You too: close out your current shell or terminal session and open a new one. You may attempt reloading your  with the following command:

 $ source ~/.bash_profile

However, closing out your current shell or terminal and opening a new one is the preferred way for initial installations. Alternatively, you can use the  command and check with  to see whether the shell has picked up the new group membership of your user

RVM will be automatically configured for every user on the system (in opposite to the single-user installation); this is accomplished by loading  on login. Arch Linux defaults to parsing  which contains the logic to load all files residing in the  directory.

Before installing gems with multi-user rvm, make sure that  does not have the line . If it does you need to comment it out otherwise the gems will install to the wrong place.

Only use the sudo command during the install process. In multi-user configurations, any operations which require sudo access must use the rvmsudo command which preserves the RVM environment and passes this on to sudo. There are very few cases where rvmsudo is required once the core install is completed, except for when updating RVM itself. There is never a reason to use sudo post-install. rvmsudo should only be needed for updating with

 $ rvmsudo rvm get head

## A cautionary action
In order to prevent the installation breakage by this cause, create the following drop-in file using the  command as root:

Where  would be —for example— ruby-1.9.2-p290.

## Post Installation
After the installation, check everything worked with this command:

 $ type rvm | head -n1

The response should be:

 $ rvm is a function

If you receive rvm: not found, you may need to source your  (or wherever you put the line above):

 $ . ~/.bash_profile

If you receive "rvm is hashed", you need to source  in  or similar:

 $ source $HOME/.rvm/scripts/rvm

Check if the rvm function is working:

 $ rvm notes

Finally, see if there are any dependency requirements for your installation by running:

 $ rvm requirements

(Follow the returned instructions if any.)

Very important: whenever you upgrade RVM in the future, you should always run rvm notes and rvm requirements as this is usually where you will find details on any major changes and/or additional requirements to ensure your installation stays working.

## Some extras
You may put in your  the following lines to get some useful features:

Or if you are running as a single user:

## Using RVM
The RVM documentation is quite comprehensive and explanatory. However, here are some RVM usage examples to get you started.

## Rubies
## Installing environments
To see what Ruby environments are available to install, run:

 $ rvm list known

To install one, run:

 $ rvm install

For example, to install Ruby 1.9.2 one would run the following command:

 $ rvm install 1.9.2

This should download, configure and install Ruby 1.9.2 in the place you installed RVM. For example, if you did a single user install, it will be in .

You can define a default ruby interpreter by doing:

 $ rvm use  --default

If not, the default environment will be the system ruby in  —if you have installed one using pacman— or none.

## Switching environments
To switch from one environment to another simply run:

 $ rvm use

For example to switch to Ruby 1.8.7 one would run the following command:

 $ rvm 1.8.7

(As you see, the flag use is not really necessary.)

You should get a message telling you the switch worked. It can be confirmed by running:

 $ ruby --version

Note that this environment will only be used in the current shell. You can open another shell and select a different environment for that one in parallel.

In case you have set a default interpreter as explained above, you can do the switch with:

 $ rvm default

## System ruby
If you wish the ruby interpreter that is outside RVM (i.e. the one installed in /usr by the standard Arch Linux package), you can switch to it using:

 $ rvm system

## Listing environments
To see all installed Ruby environments, run the following command:

 $ rvm list

If you have installed a few rubies, this might generate a list like so:

 rvm Rubies
 => ruby-1.8.7-p249 [ x86_64 ]
    ruby-1.9.2-head [ x86_64 ]
 System Ruby
    system [ x86_64 ]

The ASCII arrow indicates which environment is currently enabled. In this case, it is Ruby 1.8.7. This could be confirmed by running:

 $ ruby --version
 ruby 1.8.7 (2010-01-10 patchlevel 249) === Gemsets ===

RVM has a valued feature called gemsets which enables you to store different sets of gems in compartmentalized independent ruby setups. This means that ruby, gems and irb are all separate and self-contained from the system and each other.

## Creating
Gemsets must be created before being used. To create a new gemset for the current ruby, do this:

 $ rvm use
 $ rvm gemset create

Alternatively, if you prefer the shorthand syntax offered by rvm use, employ the --create option like so:

 $ rvm use @ --create

You can also specify a default gemset for a given ruby interpreter, by doing:

 $ rvm use @ --default

## Using
{{Tip|Remove gems that reside in system prior to the RVM installation with:
{{bc|$ gem  list --local --no-version | awk '{print "gem uninstall " $1}' | bash}}
and check what's left:

}}

To use a gemset:

 $ rvm gemset use

You can switch to a gemset as you start to use a ruby, by appending @ to the end of the ruby selector string:

 $ rvm use @

## Notes
When you install a ruby environment, it comes with two gemsets out of the box, their names are default and global. You will usually find in the latter some pre-installed common gems, while the former always starts empty.

A little bit about where the default and global gemsets differ: When you do not use a gemset at all, you get the gems in the default set. If you use a specific gemset (say @testing), it will inherit gems from that ruby's @global. The global gemset is to allow you to share gems to all your gemsets.

## Gems
Within a gemset, you can utilize usual RubyGems commands
 $ gem install
to add,
 $ gem uninstall
to remove gems, and
 $ gem list
to view installed ones.

If you are deploying to a server, or you do not want to wait around for rdoc and ri to install for each gem, you can disable them for gem installs and updates. Just add these two lines to your  or :

 install: --no-document
 update: --no-document

## Listing
To see the name of the current gemset:

 $ rvm gemset name

To list all named gemsets for the current ruby interpreter:

 $ rvm gemset list

To list all named gemsets for all interpreters:

 $ rvm gemset list_all

## Deleting
This action removes the current gemset:

 $ rvm gemset use
 $ rvm gemset delete

By default, rvm deletes gemsets from the currently selected Ruby interpreter. To delete a gemset from a different interpreter, say 1.9.2, run your command this way:

 $ rvm 1.9.2 do gemset delete

## Emptying
This action removes all gems installed in the gemset:

 $ rvm gemset use
 $ rvm gemset empty

## RVM
## Updating
To upgrade to the most recent release version:

 $ rvm get latest

Upgrading to the latest repository source version (the most bugfixes):

 $ rvm get head

Remember to use rvmsudo for multi-user setups. Update often!

## Uninstalling
Executing

 $ rvm implode

is going to wipe out the RVM installation —cleanly—.

## Troubleshooting
Unfortunately, some ruby patchlevels just do not play nicely with Arch Linux, and many times RVM does not choose the latest patchlevel version to install. So, you will need to manually check on the ruby website, and force RVM to install it.

## "data definition has no type or storage class"
This appears to be specific to 1.8.7, but if you get this error while compiling the following steps will fix your problem:

 $ cd src/ruby-1.8.7-p334/ext/dl
 $ rm callback.func
 $ touch callback.func
 $ ruby mkcallback.rb >> callback.func
 $ rm cbtable.func
 $ touch cbtable.func
 $ ruby mkcbtable.rb >> cbtable.func

Naturally, substitute the actual build path to your source, which will be something like .

## RVM uses wrong OpenSSL version
Ruby versions older than 2.4 require OpenSSL 1.0 but RVM will try to build them with OpenSSL 1.1. You know this is the case if you find this line in the  file:

 /usr/include/openssl/asn1_mac.h:10:2: error: #error "This file is obsolete; please update your software."

First install  if not already installed.

You can point it to the correct version like this:

 $ rvm remove
 $ PKG_CONFIG_PATH=/usr/lib/openssl-1.0/pkgconfig:/usr/lib/pkgconfig rvm install

if the above does not work, try changing the last command to:

 PKG_CONFIG_PATH=/usr/lib/openssl-1.0/pkgconfig \
 CFLAGS+=" -I/usr/include/openssl-1.0" \
 LDFLAGS+=" -L/usr/lib/openssl-1.0 -lssl" \
 rvm install

Alternatively you could also use RVM to install OpenSSL:

 $ rvm pkg install openssl
 $ rvm remove X.Y.Z
 $ rvm install X.Y.Z -C --with-openssl-dir=$HOME/.rvm/usr
