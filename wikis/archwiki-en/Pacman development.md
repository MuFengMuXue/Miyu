# Pacman development

Interested in Pacman Development? This page should help you get started.

Remember that if you think something belongs on this page, add it! The current pacman developers are not likely to know what people need to know and should be on this page.

## References and links
* Pacman Homepage
* Latest NEWS/ChangeLog
* Pacman on GitLab
* Mailing List Archives
* HACKING
* Submitting Patches
* Translation Help
* IRC: #archlinux-pacman

## Developer repositories
A handful of the "regulars" have their own repositories with work in progress, working and feature branches, etc. Several are listed here, but feel free to add more that you may know about.

* Allan McRae: https://gitlab.archlinux.org/allan/pacman
* Andrew Gregory: https://github.com/andrewgregory/pacman

## Git tips
Before using these tips, it is highly recommended to read the Git article.

Clone git repo - only needed once:

 $ git clone https://gitlab.archlinux.org/pacman/pacman.git

Enable useful hooks:

 $ mv .git/hooks/applypatch-msg.sample .git/hooks/applypatch-msg
 $ mv .git/hooks/commit-msg.sample .git/hooks/commit-msg
 $ mv .git/hooks/pre-commit.sample .git/hooks/pre-commit
 $ mv .git/hooks/pre-rebase.sample .git/hooks/pre-rebase

or

 $ rename .sample "" .git/hooks/*.sample

Always do your work on a new local branch to save yourself headaches.

Make patch to master branch:

 $ git format-patch master

Amend patch (do not use it after a push):

 $ git commit -a --amend -s

Update master branch:

 $ git checkout master
 $ git pull

Merge changes on master with "branch":

 $ git rebase master branch

Get maint branch:

 $ git checkout -b maint origin/maint

Add a remote repository:

 $ git remote add toofishes git://code.toofishes.net/dan/pacman.git

Get toofishes working branch:

 $ git branch -r
 $ git checkout -b toofishes-working toofishes/working
