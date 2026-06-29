# Mercurial

Mercurial (commonly referred to as hg) is a distributed version control system written in Python and is similar in many ways to Git, Bazaar and Darcs.

## Installation
Install the  package.

## Graphical front-ends
See also Mercurial graphical user interfaces.

*
*

## Configuration
At the minimum you should configure your username or mercurial will most likely give you an error when trying to commit. Do this by editing  or  and adding the following:

To use the graphical browser hgk aka. , add the following to  (see forum thread):

You will need to install  before running  to avoid the rather cryptic error message:

 /usr/bin/env: wish: No such file or directory

## Usage
All mercurial commands are initiated with the hg prefix. To see a list of some of the common commands, run
 $ hg help

Each command has a help page that can be read using
 $ hg help subcommand

You can either work with a pre-existing repository (collection of code or files), or create your own to share.

To work with a pre-existing repository, you must clone it to a directory of your choice:

 $ mkdir mercurial
 $ cd mercurial
 $ hg clone https://repo.mercurial-scm.org/hello

To create you own, change to the directory you wish to share and initiate a mercurial project

 $ cd myfiles
 $ hg init myfiles

## Dotfiles Repository
If you intend on creating a repository of all your  files, you simply initiate the project in your home folder:

 $ hg init

It is then just a case of adding the specific files you wish to track:

 $ hg add |file1 file2 file3

You can then create a  to ensure that only the files you wish to include in the repository are tracked by mercurial.

## Tips and tricks
## Progress bar
If you are going to be working with large repositories, you may want to enable the progress extension by adding it to your  file:

This will show progress bars on operations longer than 3 seconds.  If you would like the progress bar to show sooner, you can append the following to your configuration file:
