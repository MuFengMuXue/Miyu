# Git

:"I've met people who thought git is a front-end to GitHub. They were wrong, git is a front-end to the AUR." — Linus T.

Git is the version control system (VCS) designed and developed by Linus Torvalds, the creator of the Linux kernel. Git is now used to maintain AUR packages, as well as many other projects, including sources for the Linux kernel.

## Installation
Install the  package. For the development version, install the  package. Check the optional dependencies when using tools such as git svn, git gui and gitk.

## Graphical front-ends
See also git GUI Clients.

*
*
*
*
*
*
*
*
*
:
*
*
*
*
*
*
*
*
*
*
*
*

## Configuration
In order to use Git you need to set at least a name and email:

 $ git config --global user.name  "John Doe"
 $ git config --global user.email "johndoe@example.com"

See Getting Started - First-Time Git Setup.

See #Tips and tricks for more settings.

## Usage
A Git repository is contained in a  directory, which holds the revision history and other metadata. The directory tracked by the repository, by default the parent directory, is called the working directory. Changes in the working tree need to be staged before they can be recorded (committed) to the repository. Git also lets you restore, previously committed, working tree files.

See Getting Started.

## Getting a Git repository
See Getting a Git Repository - Git Basics

## Recording changes
See Recording Changes to the Repository - Git Basics

## Viewing change history
See Viewing the Commit History - Git Basics

## Undoing things
See Undoing Things - Git Basics

## Working with remotes
See Working with Remotes - Git Basics

## Branching
See Branching in a Nutshell - Git Branching

## Basic branching and merging
See Basic Branching and Merging - Git Branching

## Branch management
See Branch Management - Git Branching

## Branching workflows
See Branching Workflows - Git Branching

## Remote branches
See Remote Branches - Git Branching

## Rebasing
See Rebasing - Git Branching

## Collaboration
## Distributed workflows
See Distributed Workflows - Distributed Git

## Contributing to a project
See Contributing to a Project - Distributed Git

## Maintaining a project
See Maintaining a Project - Distributed Git

## Git tools
## Revision selection
See Revision Selection - Git Tools

## Interactive staging
See Interactive Staging - Git Tools

## Stashing and cleaning
See Stashing and Cleaning - Git Tools

## Signing your work
See Signing Your Work - Git Tools

## Searching
See Searching - Git Tools

## Rewriting history
See Rewriting History - Git Tools

## Reset demystified
See Reset Demystified - Git Tools

## Advanced merging
See Advanced Merging - Git Tools

## Rerere
See Rerere - Git Tools

## Debugging with Git
See Debugging with Git - Git Tools

## Submodules
See Submodules - Git Tools

## Bundling
See Bundling - Git Tools

## Replace
See Replace - Git Tools

## Credential storage
See Credential Storage - Git Tools

## Tips and tricks
## Using git-config
Git reads its configuration from four INI-type configuration files:

*  for system-wide defaults
*  and  (since 1.7.12) for user-specific configuration
*  for repository-specific configuration

These files can be edited directly, but the usual method is to use git config, as shown in the examples below.

List the currently set variables:

 $ git config list {--local,--global,--system}

Set the default editor from vim to nano:

 $ git config --global core.editor "nano -w"

Set the default push action:

 $ git config --global push.default simple

Set a different tool for git difftool (meld by default):

 $ git config --global diff.tool vimdiff

See  and Git Configuration for more information.

## Inclusion of separate configuration files
Since v1.7.10 in 2012, Git is able to build a configuration file that is split into multiple configuration files using the  keyword inside the  file.

## Adopting a good etiquette
* When considering contributing to an existing project, read and understand its license, as it may excessively limit your ability to change the code. Some licenses can generate disputes over the ownership of the code.
* Think about the project's community and how well you can fit into it. To get a feeling of the direction of the project, read any documentation and even the log of the repository.
* When requesting to pull a commit, or submit a patch, keep it small and well documented; this will help the maintainers understand your changes and decide whether to merge them or ask you to make some amendments.
* If a contribution is rejected, do not get discouraged, it is their project after all. If it is important, discuss the reasoning for the contribution as clearly and as patiently as possible: with such an approach a resolution may eventually be possible.

## Speeding up authentication
You may wish to avoid the hassle of authenticating interactively at every push to the Git server.

* If you are authenticating with SSH keys, use an SSH agent. See also OpenSSH#Speeding up SSH and OpenSSH#Keep alive.
* If you are authenticating with username and password, switch to SSH keys if the server supports SSH, otherwise use git-credential-libsecret credential helper, or try git-credential-cache or git-credential-store.

## Using git-credential-libsecret as credential-helper
Git may fetch your credentials from an org.freedesktop.secrets compatible keyring like GNOME Keyring, KeePassXC or KDE Wallet. Therefore set up one compatible keyring and check if a keyring is registered to dbus using:

 $ dbus-send --session --print-reply --dest=org.freedesktop.DBus / \
     org.freedesktop.DBus.GetConnectionUnixProcessID \
     string:org.freedesktop.secrets

then run

 $ git config --global credential.helper /usr/lib/git-core/git-credential-libsecret

to set up git.

## Using git-credential-netrc as credential-helper
Git can read the netrc file to access credentials. First, direct Git to the netrc helper script:

 $ git config --global credential.helper /usr/share/git/credential/netrc/git-credential-netrc.perl

Then, create a  file:

The credential helper also supports gpg-encrypted files () if you like to keep your secrets safe.

## Protocol defaults
If you are running a multiplexed SSH connection as shown above, Git over SSH might be faster than HTTPS. Also, some servers (like the AUR) only allow pushing via SSH. For example, the following configuration will set Git over SSH for any repository hosted on the AUR.

## Bash completion
In order to enable Bash completion, source  in a Bash startup file. Alternatively, install .

## Git prompt
The Git package comes with a prompt script. To enable it, source the  and set a custom prompt with the  parameter:

* For Bash:
* For Zsh:

Note that the command substitution must be escaped, see Bash/Prompt customization#Embedding commands for details. See Command-line shell#Configuration files for persistent configuration.

When changing to a directory of a Git repository, the prompt will change to show the branch name. Extra details can be set to be shown by the prompt by setting the corresponding environment variable:

{| class="wikitable"
 |+
 ! Shell variable !! Information
 |-
 | GIT_PS1_SHOWDIRTYSTATE     ||  for staged,  if unstaged.
 |-
 | GIT_PS1_SHOWSTASHSTATE     ||  if something is stashed.
 |-
 | GIT_PS1_SHOWUNTRACKEDFILES ||  if there are untracked files.
 |-
 | GIT_PS1_SHOWUPSTREAM       || ,  behind, ahead, or diverged from upstream.
 |-
 | GIT_PS1_STATESEPARATOR     || separator between branch name and state symbols
 |-
 | GIT_PS1_DESCRIBE_STYLE     || show commit relative to tag or branch, when detached HEAD
 |-
 | GIT_PS1_SHOWCOLORHINTS     || display in color
 |}

The full documentation for the environment variables is available in the comments of the script.

Alternatively, you can use one of git shell prompt customization packages from AUR such as  or .

## Visual representation
To get an idea of the amount of work done:

 $ git diff --stat

git log with forking representation:

 $ git log --graph --oneline --decorate

git log graph alias (i.e. git graph will show a decorated version):

 $ git config --global alias.graph 'log --graph --oneline --decorate'

## Commit tips
Reset to previous commit (very dangerous, erases all tracked files to the specified commit):

 $ git reset --hard HEAD~

If a repository address gets changed, its remote location will need to be updated:

 $ git remote set-url origin git@address:user/repo.git

Alternatively, edit  with the new location.

Signed-off-by line append (a name-email signature is added to the commit which is required by some projects):

 $ git commit -s

Signed-off-by automatically append to patches (when using ):

 $ git config --local format.signoff true

Commit specific parts of files that have changed. This is useful if there are a large number of changes made that would be best split into several commits:

 $ git add -p

## Signing commits
Git allows commits and tags to be signed using GnuPG, see Signing Your Work.

To configure Git to automatically sign commits:

 $ git config --global commit.gpgSign true

## Working with a non-master branch
Occasionally a maintainer will ask that work be done on a branch. These branches are often called  or . Begin by cloning the repository.

To enter another branch beside master (git clone only shows master branch but others still exist,  to show):

 $ git checkout -b branch origin/branch

Now edit normally; however to keep the repository tree in sync be sure to use both:

 $ git pull --all
 $ git push --all

## Directly sending patches to a mailing list
If you want to send patches directly to a mailing list, you have to install the following packages:  and .

Make sure you have configured your username and e-mail address, see #Configuration.

Configure your e-mail settings:

 $ git config --global sendemail.smtpserver smtp.example.com
 $ git config --global sendemail.smtpserverport 465
 $ git config --global sendemail.smtpencryption ssl
 $ git config --global sendemail.smtpuser foobar@example.com

Now you should be able to send the patch to the mailing list (see also OpenEmbedded: Sending the Patches via Email and git-send-email.io):

 $ git add filename
 $ git commit -s
 $ git send-email --to=pacman-contrib@lists.archlinux.org --confirm=always -M -1

## Working with a large git repository
When working with a large remote repository, a significant amount of data has to be fetched. The following examples use the Linux kernel to illustrate how to work with such codebases.

## Fetching the entire repository
The easiest solution is to get the entire repository:

 $ git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git

You can update your repository by .

## Partially fetching the repository
To limit your local repository to a smaller subset of the origin, say after v4.14 to bisect a bug, use a shallow clone:

 $ git clone --shallow-exclude v4.13 git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git

You will get v4.14 and later, but not v4.13 and older.

If you only want the latest snapshot, ignoring all history (If a tarball is available and it suffices, choose that; downloading from a git repository needs more bandwidth.), you can get it with:

 $ git clone --depth 1 git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git

You can later obtain older commits, as the two following examples show:

 $ git fetch --tags --shallow-exclude v4.1
 $ git fetch --tags --shallow-since 2016-01-01

## Using Scalar
Scalar, formerly Virtual File System for Git (VFS for Git), allows to access git repositories without a local instance.

See .

## Getting other branches
Your local repository tracks, in the above example, only the mainline kernel, i.e. in which the latest development is done. Suppose you want the latest LTS, for example the up-to-date 4.14 branch. You can get it by:

 $ git remote set-branches --add origin linux-4.14.y
 $ git fetch --shallow-exclude v4.14
 $ git branch --track linux-4.14.y origin/linux-4.14.y

The last line is not mandatory, but probably wanted.
(To know the name of the branch you want, there is no general rule. You can guess one by seeing the "ref" link in the gitweb interface.)

For the snapshot of linux-4.14.y, do

 $ git checkout linux-4.14.y

Or to extract it in another directory,

 $ mkdir /path/to/src-4.14; cd /path/to/src-4.14
 $ git clone --no-local --depth 1 -b linux-4.14.y ../linux-stable

As usual, do  to update your snapshot.

## Filtering confidential information
Occasionally, software may keep plain-text passwords in configuration files, as opposed to hooking into a keyring. In these cases, git clean-filters may be handy to avoid accidentally committing confidential information. E. g., the following file assigns a filter to the file “some-dotfile”:

Whenever the file “some-dotfile” is checked into git, git will invoke the filter “remove-pass” on the file before checking it in. The filter must be defined in the git-configuration file, e. g.:

## HTML help files
The  documentation is also available in HTML form by installing . After installing, the HTML docs can be accessed by passing the  flag. For example:

 $ git help -w merge

The HTML documentation can be loaded by default by setting a  option:

 $ git config --global help.format html

## Extensions
## Helpers and utilities
*  - If you're using oh-my-zsh, you may also enable git-extras plugin
*
*

## Support of large file synchronization
*

## Manage multiple Git repositories
*
*
*
*
*
*
