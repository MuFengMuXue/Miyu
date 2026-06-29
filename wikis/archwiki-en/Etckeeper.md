# Etckeeper

Etckeeper is a collection of tools to keep track of  in a repository (Git, Mercurial, Bazaar or Darcs are supported). A pacman hook auto-commits changes before a system-upgrade and file permissions are tracked, which version control does not normally support, but is important for files like :/etc/shadow.

## Installation
Install the  package.

## Configuration
The preferred version control system (default is git) and other options are to be configured in .

Etckeeper supports using pacman as a  and  in .

## Usage
After configuration the repository for the  path has to be initialized:
 # etckeeper init

And perform a first commit to keep track of the changes, this is a necessary step for etckeeper to be able to work automatically:
 # etckeeper commit "first commit"

As of etckeeper version 1.18.3-1, pre-install and post-install pacman hooks are executed automatically on package installation, update and removal. A manual #Wrapper script is not required anymore.

To track other changes to the  path, you need to either commit changes manually (see the  man page for commands) or use one of the stopgap solutions below.

git can not store file permissions directly so it is handled by etckeeper and you need to run the etckeeper init again to restore them after a checkout.
Alternatively, you can use Systemd#systemd-tmpfiles - temporary files to preserve the permissions.

## systemd
Service and timer units are included in the package. Simply enable .

See Systemd/Timers for more information and Systemd#Editing provided units if you wish to edit the provided units.

## Cron
There is a cron script in the source distribution.
You can use this script to automatically commit changes on a schedule.

For example, to make it run daily:

# Have cron installed and enabled.
# Put script as .
# Make it executable for root.

See cron for more information.

## Incron
To automatically create commits on every file modification inside , use . It utilizes native filesystem signalling through .

After installing incron and initializing etckeeper, add root to the users allowed to run incron scripts:

 # echo root >> /etc/incron.allow

Then edit the incrontab with:

 # incrontab -e

Add in the text:

 # /etc IN_MODIFY /bin/etckeeper commit "Where [message could be something like  where $# is a special incrontab wildcard expanded to the name of the file modified.

Do note that Incron is not capable of watching subdirectories. Only files within the path will be monitored. If you need subdirectories monitored, you must give them their own entry. However, commits when top-level files are modified will still commit all changes.

See: === Automatic push to remote repo ===

Whilst having a local backup in  is a good first step, etckeeper can automatically push your changes on each commit to a remote repository such as Github.

First, add your remote Github repository:

 # etckeeper vcs remote add backup https://github.com/user/repo.git

Next, one of two hooks must be used or configured to push:

## Using etckeeper provided hook
Edit the  option in , with the name of
the remote repository you want etckeeper to push to. For example:

 PUSH_REMOTE="backup"

Multiple remote repositories can be added separated with spaces.

## Through a custom hook
Create an executable file :

 #!/bin/sh
 set -e

 if [ "$VCS" = git  && [ -d .git ]; then
   cd /etc/
   git push backup master
 fi

## Wrapper script
If you want to track changes of a frequently executed command (e.g. ), a simple wrapper script can help to automate it. For example, create:

and make it executable. Alternatively, you may call the Etckeeper commands via a bash alias or function, see Bash#Aliases for more information.

## Reflector
To automatically commit the change after each Reflector invocation, make the  depend on a systemd service.

and this drop-in file:

Make  executable and do a daemon-reload.

Now, whenever  triggers the changes will immediately be saved, without interfering with unrelated configuration changes.

## Testing
Restart , then examine:

 # etckeeper vcs diff
 # etckeeper vcs show HEAD

 should show you that  has updated your mirrorlist -- it will have at least bumped the timestamp.
