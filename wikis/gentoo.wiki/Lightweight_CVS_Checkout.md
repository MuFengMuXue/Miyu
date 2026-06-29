**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

Gentoo developers willing to work with the ebuilds often check out the complete gentoo-x86 CVS repository. This page describes a method of creating and maintaining a *lightweight CVS checkout* backed up by regular (rsync or git) Gentoo repository.

## Contents

-   [[1] [Why lightweight checkout?]](#Why_lightweight_checkout.3F)
-   [[2] [How to create a lightweight checkout?]](#How_to_create_a_lightweight_checkout.3F)
    -   [[2.1] [Before starting]](#Before_starting)
    -   [[2.2] [Automated script]](#Automated_script)
    -   [[2.3] [Manual method]](#Manual_method)
-   [[3] [Working with a partial checkout]](#Working_with_a_partial_checkout)

## [][Why lightweight checkout?]

Unlike standard CVS checkout which involves fetching all the files from the gentoo-x86 repository, the lightweight method allows you to get only the files you are working on. The remaining files are obtained from a regular repository --- obtained through rsync, git, webrsync...

The advantages of this method are:

-   bandwidth and space efficiency --- only needed files are fetched and stored,
-   improved performance --- only modified files need to be recached, the supplied md5-cache is used for the remaining ebuilds,
-   improved maintainability --- there\'s no longer need to keep all ebuilds up-to-date in the CVS checkout. Instead, just remove them when done and let the regularly synced repository supply them.

The disadvantages of this method are:

-   necessity of manually fetching additional files as they are worked on,
-   inability to run tree-wide repoman scans without merging two repositories.

## [][How to create a lightweight checkout?]

### [Before starting]

Ensure that you have a Gentoo repository synced via method other than CVS. If you used to sync against CVS, please switch your Package Manager to use rsync, git or another supported method instead.

### [Automated script]

The repository can be easily created using *lcvs-init* script from [lightweight-cvs-toolkit](https://bitbucket.org/mgorny/lightweight-cvs-toolkit).

`user `[`$`]`git clone `[`https://bitbucket.org/mgorny/lightweight-cvs-toolkit.git`](https://bitbucket.org/mgorny/lightweight-cvs-toolkit.git)

`user `[`$`]`cd lightweight-cvs-toolkit`

`user `[`$`]`./lcvs-init /home/myuser/gentoo-x86 myuser`

The script takes three parameters:

1.  location where the repository should be created,
2.  CVS username (optional, defaults to current user\'s username),
3.  Repository name (optional, defaults to *gentoo-cvs*).

Before creating the repository, the script will check system sanity, output the resulting configuration and ask the user for confirmation.

### [Manual method]

Then create a new CVS checkout using the *-l* option (local) to disable recursive fetching:

`user `[`$`]`cvs -dmyuser@cvs.gentoo.org:/var/cvsroot co -l gentoo-x86`

(change *myuser* to your Gentoo username)

It is also convenient to fetch (non-recursively) directories for all ebuild categories. For example:

`user `[`$`]`cd gentoo-x86`

`user `[`$`]`cvs up -dl $(</usr/portage/profiles/categories)`

Afterwards, the metadata for repository should be fetched and layout.conf file updated to state a new repository name, and name *gentoo* as its master repository. This will allow the checkout to be used as a regular overlay on top of the rsync/git repository.

`user `[`$`]`cvs up -dP metadata`

`user `[`$`]`vim metadata/layout.conf`

[FILE] **`metadata/layout.conf`Additions to layout.conf**

    repo-name = gentoo-cvs
    masters = gentoo

It is recommended to consistently use the name *gentoo-cvs* since that provides a convenient way of locating the CVS checkout for scripts.

** Note**\
The *repo-name* in *metadata/layout.conf* overrides *profiles/repo_name*. This way, it is possible to conveniently change the repository name without introducing any changes in *profiles* directory --- that could be accidentally committed along with profile changes.

At this point the repository is ready. It is also a good idea to create a git repository on top of it and store the current state. This can be used to conveniently remove checked out ebuild later and restore the repository to vanilla state.

`user `[`$`]`git init`

`user `[`$`]`git add -A`

`user `[`$`]`git commit -m "Initialize CVS checkout"`

Finally, add the repository to repos.conf:

[FILE] **`/etc/portage/repos.conf/cvs.conf`Configuration for repos.conf**

    [gentoo-cvs]
    location = /home/myuser/gentoo-x86
    # ensure it overrides any overlay
    priority = 1000

** Warning**\
Do not add a *sync-uri* or otherwise *emerge \--sync* will update *all* ebuilds in the repository, converting it to a regular checkout.

## [Working with a partial checkout]

Since partial checkout doesn\'t have any ebuilds, eclasses, licenses or profiles by default (inherits them all from *gentoo* implicitly), the files being worked need to be fetched manually. *cvs up -dP* can be used for this. For example, if you want to work on dev-foo/bar, you\'d do:

`user `[`$`]`cd ~/gentoo-x86`

`user `[`$`]`cd dev-foo`

`user `[`$`]`cvs up -dP bar`

** Note**\
You normally don\'t have to check eclasses, licenses or profiles out, since they are inherited from the rsync/git *gentoo* repository.

You can also pass multiple directories to *cvs up*:

`user `[`$`]`cd ~/gentoo-x86`

`user `[`$`]`cvs up -dP dev-foo/bar dev-bar/baz profiles`

When done working with the files, it is useful to remove them. Otherwise, the old versions will confuse your Package Manager in the future.

`user `[`$`]`rm -r dev-foo/bar dev-bar/baz profiles`

If you used git during the repository creation (both methods above do), you can also let it clean any new files:

`user `[`$`]`git clean -df`