Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Dispatch-conf/es "Dispatch-conf (94% translated)")
-   [français](https://wiki.gentoo.org/wiki/Dispatch-conf/fr "dispatch-conf/fr (85% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Dispatch-conf/hu "Dispatch-conf (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Dispatch-conf/ja "dispatch-conf (100% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf]\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")][Project](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/portage)

[[]][GitWeb](https://gitweb.gentoo.org/proj/portage.git)

[[]][GitHub](https://github.com/gentoo/portage)

[[]][Bugs (upstream)](https://bugs.gentoo.org)

[[]]This article has some todo items:\

-   how to revert a change
-   how backups are made
-   is archive-dir still an option ? it isn\'t in the config file by default

**[dispatch-conf]** is a utility included with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), used to safely and conveniently manage configuration files after package updates. It is an important tool to manage the issue of transitioning configuration across package updates, without the user needing to manually migrate changes.

[dispatch-conf] allows system administrators to review configuration file changes made by Portage, to gracefully manage changes to the structure of the configuration of an updated package, in a standard way. Portage will indicate when config files need updating, and running [dispatch-conf] will propose to either use the new configuration as-is, reject changes, or selectively merge modifications. [dispatch-conf] will automatically update config files that the user has never modified, or that differ from the current version only in CVS cruft, comments, or white space.

[dispatch-conf] keeps a history of changes and permits rollback to previous versions, so any mistakes can be reverted. Changes made to config files will be saved in the archive directory. Alternatively it can integrate with [rcs] to allow for version-controlled configuration file management.

[dispatch-conf] will check all directories in the `CONFIG_PROTECT` environment variable for changes. Any config files found in paths in the `CONFIG_PROTECT_MASK` environment variable will not be protected and will **automatically be overwritten**.

** Important**\
Before running dispatch-conf for the first time, the settings in [/etc/dispatch-conf.conf] should be edited, and the archive directory specified in [/etc/dispatch-conf.conf] will need to be created ([/etc/config-archive] by default).

## Contents

-   [[1] [The configuration management problem with updates]](#The_configuration_management_problem_with_updates)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [RCS (revision control system) integration]](#RCS_.28revision_control_system.29_integration)
    -   [[2.3] [Changing diff or merge tools]](#Changing_diff_or_merge_tools)
        -   [[2.3.1] [Color diff output]](#Color_diff_output)
        -   [[2.3.2] [Use (g)vimdiff to merge changes]](#Use_.28g.29vimdiff_to_merge_changes)
        -   [[2.3.3] [Using imediff to merge changes]](#Using_imediff_to_merge_changes)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Keep configuration changes in a git repository]](#Keep_configuration_changes_in_a_git_repository)
-   [[5] [See also]](#See_also)

## [The configuration management problem with updates]

Configuration migration is a general problem with any software update process: some version changes will modify behavior, such that the previous configuration parameters become no longer pertinent to the new version. New configuration options may be added, removed, their meaning may be changed or the names or the format of each directive may change.

Each software project manages this in its own way. Some projects have robust configuration version tracking and can automatically transfer configuration from one version to another; some projects may have issues between major versions, or if updating from much older versions; for some projects, updating while trying to preserve previous configurations may cause issues or even be impossible.

There is a long-standing Unix convention of using plain text files, often with a semi-standard syntax, for storing configuration. Major updates could require manual migration of these files, or risk them becoming outdated. This may seem cumbersome today, but it remains a very robust way to manage configuration, and avoids ambiguity of how the configuration directives may change between versions, which is important for many - sometimes critical - services such as Internet servers.

## [Configuration]

### [Files]

The [dispatch-conf] configuration file is [/etc/dispatch-conf.conf]. The directory referenced by the `archive-dir` variable in this file may need to be created.

### [][RCS (revision control system) integration]

** Warning**\
When configured to use RCS, read and execute permissions of archived files may be inherited from a file\'s first check-in. If the permissions of the working file have since changed, the permissions from the first check in may be kept - this could inadvertently cause security issues. Access to RCS files can be controlled by setting the permissions of the parent directory.

When [dispatch-conf] is configured to integrate with [rcs], it will store all changes in [/etc/config-archive].

Install revision control system:

`root `[`#`]`emerge --ask dev-vcs/rcs`

This process of configuration is as simple as editing the configuration file to include the following:

[FILE] **`/etc/dispatch-conf.conf`**

    use-rcs=yes

Administrators can then view the differences using the [rcs] utilities like [rlog] as well as roll-back changes using [co]. The [rcs] utilities work with file locking itself, so the moment it is needed for administrative tasks, understand that:

-   [dispatch-conf] only stores the changes made when the package suggests to alter the file. Changes made afterwards are *not* registered yet
-   when checking out a file, [rcs] will want to write the file to the file system, so make sure to backup existing files first, or work with standard output (see later)
-   to check in a file, a lock must first be taken on said file. Also, make sure not to remove the working file

To view the commit history on [/etc/conf.d/udev]:

`user `[`$`]`rlog /etc/config-archive/etc/conf.d/udev,v`

    RCS file: /etc/config-archive/etc/conf.d/udev,v
    Working file: udev
    head: 1.1
    branch:
    locks: strict
    access list:
    symbolic names:
    keyword substitution: kv
    total revisions: 2;     selected revisions: 2
    description:
    Archived config file.
    ----------------------------
    revision 1.1
    date: 2011/06/15 18:14:59;  author: root;  state: Exp;
    branches:  1.1.1;
    dispatch-conf update.
    ----------------------------
    revision 1.1.1.1
    date: 2011/06/15 18:14:59;  author: root;  state: Exp;  lines: +3 -2
    dispatch-conf update.
    =============================================================================

To roll back to a particular version, a simple way to do so is to check out a previous version:

`root `[`#`]`cp udev udev.orig `

`root `[`#`]`co -p -r1.1.1.1 /etc/config-archive/etc/conf.d/udev,v > udev `

    etc/config-archive/etc/conf.d/udev,v  -->  standard output
    revision 1.1.1.

After making final changes (it is possible to use the backup [udev.orig] to merge any changes made later), check in the file again:

`root `[`#`]`co -p -l /etc/config-archive/etc/conf.d/udev,v`

Edit the file, and finally check in the changes:

`root `[`#`]`ci -l /etc/config-archive/etc/conf.d/udev,v`

    /etc/config-archive/etc/conf.d/udev,v  <--  udev
    new revision: 1.2; previous revision: 1.1
    enter log message, terminated with single '.' or end of file:
    >> Merged changes for persistant rules
    >> .
    done

### [Changing diff or merge tools]

#### [Color diff output]

Reading changes in all grey text can be a bit annoying. Fortunately, modern versions of [[[sys-apps/diffutils]](https://packages.gentoo.org/packages/sys-apps/diffutils)[]] have a `--color` switch, which displays the different types of changes in different colors. Configuration is simple - change the diff line in the config file to:

[FILE] **`/etc/dispatch-conf.conf`**

    diff="diff --color=always -Nu '%s' '%s'"

Alternatively, the package [[[app-misc/colordiff]](https://packages.gentoo.org/packages/app-misc/colordiff)[]] can be used. Install colordiff with:

`root `[`#`]`emerge --ask app-misc/colordiff`

Then change the config to use it:

[FILE] **`/etc/dispatch-conf.conf`**

    diff="colordiff -Nu '%s' '%s'"

#### [][Use (g)vimdiff to merge changes]

It is possible to use [vimdiff]/[gvimdiff] instead of the default method of merging files. To do this, modify the [/etc/dispatch-conf.conf] configuration file by changing the merge line:

[FILE] **`/etc/dispatch-conf.conf`**

    merge="vimdiff -c'saveas %s' -c next -c'setlocal noma readonly' -c prev %s %s"

[vimdiff] (for [gvimdiff] use `-f` option moreover) can also be used to merge changes.

\
And for **neovim**:

[FILE] **`/etc/dispatch-conf.conf`**

    merge="nvim -d -c'saveas %s' -c next -c'setlocal noma readonly' -c prev %s %s"

** Note**\
The left pane will hold the original config file saved as the merge output, so make changes in the left pane and save that pane. To help remember the right hand pane (containing the new config file) will be marked unmodifiable and read-only.

Some useful commands related to merge with [vimdiff]:

    "]c" : jump to next change
    "[c" : jump to previous change
    "CTRL-W <Right>" or "CTRL-W <Left>" : go to the other window
    "do" (diff obtain): get the text of the highlighted block from the other window
    "dp" (diff put) : put the text of the highlighted block to the other window
    "zo" : open fold under the cursor
    "zc" : close fold under the cursor
    "zr" : open all folds
    ":wqa" : write and exit

See the [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") documentation for further help.

#### [Using imediff to merge changes]

Another merge alternative is [[[dev-util/imediff]](https://packages.gentoo.org/packages/dev-util/imediff)[]]. This simple tool allows using just a few keys to toggle between options. Primarily, this is done through the [a] or [b] keys. Also, the [e] key will open the user\'s favorite editor set by the `EDITOR` shell variable for manual merging.

To use with dispatch-conf, first install imediff:

`root `[`#`]`emerge --ask dev-util/imediff`

Then, configure [/etc/dispatch-conf.conf]:

[FILE] **`/etc/dispatch-conf.conf`**

    # imediff-1.X
    merge="imediff2 -c -N --output='%s' '%s' '%s'"
    # imediff-3.X
    merge="imediff --output='%s' '%s' '%s'"

## [Usage]

### [Invocation]

[dispatch-conf] should be run as root, as configuration files are usually owned by root:

`root `[`#`]`dispatch-conf`

The [AMD64 Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Tools#dispatch-conf "Handbook:AMD64/Portage/Tools") and the [[[dispatch-conf(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/dispatch-conf.1.html)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page contain further information on usage:

`user `[`$`]`man 1 dispatch-conf`

## [Tips]

### [Keep configuration changes in a git repository]

On installation, [etckeeper](https://wiki.gentoo.org/wiki/Etckeeper "Etckeeper") will hook into dispatch-conf to make backups of configuration files upon each invocation.

## [See also]

-   [cfg-update](https://wiki.gentoo.org/wiki/Cfg-update "Cfg-update") --- a utility used on Gentoo to manage configuration file updates.