**Resources**

[[]][Home](https://git-scm.com)

[[]][Package information](https://packages.gentoo.org/packages/dev-vcs/git)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Git_(software) "wikipedia:Git (software)")

[[]][GitWeb](https://git.kernel.org/cgit/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/git)

**Git** is a widely used, open source, distributed [version control system](https://wiki.gentoo.org/wiki/Version_control_systems "Version control systems"), mainly written in [C](https://wiki.gentoo.org/wiki/C "C").

Git was created by Linus Torvalds for use developing the [Linux kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") and other open source projects, with the stated goals of being distributed, fast, and to guarantee that output exactly matches input. It was first released in 2005, and has since become the most widely used distributed version control system.

This article will cover getting started with Git, and general usage.

** Tip**\
The [git] repositories for Gentoo developers can be found here: [https://gitweb.gentoo.org/](https://gitweb.gentoo.org/)

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Local]](#Local)
    -   [[2.2] [Bash completion]](#Bash_completion)
    -   [[2.3] [Zsh completion]](#Zsh_completion)
    -   [[2.4] [Status in bash prompt]](#Status_in_bash_prompt)
    -   [[2.5] [Server]](#Server)
        -   [[2.5.1] [Initial setup]](#Initial_setup)
    -   [[2.6] [SSH keys]](#SSH_keys)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Creating a patch]](#Creating_a_patch)
    -   [[3.2] [Bisecting with live ebuilds]](#Bisecting_with_live_ebuilds)
    -   [[3.3] [Create a repository and make the initial commit]](#Create_a_repository_and_make_the_initial_commit)
    -   [[3.4] [Common commands]](#Common_commands)
    -   [[3.5] [Repository management via GUI]](#Repository_management_via_GUI)
    -   [[3.6] [Serving and managing repositories via builtin web interface]](#Serving_and_managing_repositories_via_builtin_web_interface)
        -   [[3.6.1] [Help]](#Help)
        -   [[3.6.2] [Configuration]](#Configuration_2)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [dev-vcs/git](https://packages.gentoo.org/packages/dev-vcs/git) [[]] [Stupid content tracker: distributed VCS designed for speed and efficiency]

  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+curl`](https://packages.gentoo.org/useflags/+curl)                       Support fetching and pushing (requires webdav too) over http:// and https:// protocols
  [`+gpg`](https://packages.gentoo.org/useflags/+gpg)                         Pull in gnupg for signing \-- without gnupg, attempts at signing will fail at runtime!
  [`+iconv`](https://packages.gentoo.org/useflags/+iconv)                     Enable support for the iconv character set conversion library
  [`+nls`](https://packages.gentoo.org/useflags/+nls)                         Add Native Language Support (using gettext - GNU locale utilities)
  [`+pcre`](https://packages.gentoo.org/useflags/+pcre)                       Add support for Perl Compatible Regular Expressions
  [`+perl`](https://packages.gentoo.org/useflags/+perl)                       Adds Perl bindings and tools such as git-send-email
  [`+safe-directory`](https://packages.gentoo.org/useflags/+safe-directory)   Respect the safe.directory setting
  [`+webdav`](https://packages.gentoo.org/useflags/+webdav)                   Adds support for push\'ing to HTTP/HTTPS repositories via DAV
  [`cgi`](https://packages.gentoo.org/useflags/cgi)                           Install gitweb too
  [`cvs`](https://packages.gentoo.org/useflags/cvs)                           Enable CVS (Concurrent Versions System) integration
  [`doc`](https://packages.gentoo.org/useflags/doc)                           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`highlight`](https://packages.gentoo.org/useflags/highlight)               GitWeb support for app-text/highlight
  [`keyring`](https://packages.gentoo.org/useflags/keyring)                   Enable support for freedesktop.org Secret Service API password store
  [`perforce`](https://packages.gentoo.org/useflags/perforce)                 Add support for Perforce version control system (requires manual installation of Perforce client)
  [`rust`](https://packages.gentoo.org/useflags/rust)                         Build components using Rust, starting with 2.52 with varint. This will become mandatory upstream with Git 3.0.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`subversion`](https://packages.gentoo.org/useflags/subversion)             Include git-svn for dev-vcs/subversion support
  [`test`](https://packages.gentoo.org/useflags/test)                         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tk`](https://packages.gentoo.org/useflags/tk)                             Include the \'gitk\' and \'git gui\' tools
  [`xinetd`](https://packages.gentoo.org/useflags/xinetd)                     Add support for the xinetd super-server
  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-23 17:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]]:

`root `[`#`]`emerge --ask dev-vcs/git`

### [Additional software]

There are a number of additional applications that are associated with Git and are of note:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                  Description                                                   Notes
  [[[app-vim/fugitive]](https://packages.gentoo.org/packages/app-vim/fugitive)[]]   Git wrapper plugin for vim.
  [[[dev-vcs/git-cola]](https://packages.gentoo.org/packages/dev-vcs/git-cola)[]]   \"Sleek and powerful\" graphical user interface for Git.      As of v4.0.1, [git-cola] cannot open a fully history clone of [gentoo.git](https://gitweb.gentoo.org/repo/gentoo.git) without serious application freezes. Try a shallow clone if experiencing freezing.
  [[[dev-vcs/git-flow]](https://packages.gentoo.org/packages/dev-vcs/git-flow)[]]   Git extensions to provide high-level repository operations.
  [[[dev-vcs/gitg]](https://packages.gentoo.org/packages/dev-vcs/gitg)[]]               Git repository viewer for GNOME.
  [[[dev-vcs/qgit]](https://packages.gentoo.org/packages/dev-vcs/qgit)[]]               Qt-based GUI for git repositories.                            As of v2.10, [qgit] has no issues opening a full history clone of [gentoo.git](https://gitweb.gentoo.org/repo/gentoo.git).
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is a partial selection of packages available in the Gentoo repository, see the [dev-vcs](https://packages.gentoo.org/categories/dev-vcs) category on the Gentoo Packages site, or use [eix](https://wiki.gentoo.org/wiki/Eix "Eix") ([eix \--category dev-vcs]), to see packages from the *dev-vcs* category that may be of interest.

There is additional software in the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository, such as the *gitui* and *lazygit* GUIs.

## [Configuration]

Before contributing to a project, it is imperative to establish a user name and email for each user. Substitute the bracketed \"Larry\" references (brackets and everything in-between, but leave the quotes) in the next example for a personal user name and e-mail address:

`user `[`$`]`git config --global user.email "<larry@gentoo.org>" `

`user `[`$`]`git config --global user.name "<Larry the cow>" `

** Note**\
To prevent email spam, it is possible to set a blank email address as follows:

`user `[`$`]`git config --global user.email ""`

### [Local]

If there will be just one user of the project, or when creating something which will be shared in a distributed way, start on the local workstation.

If the intent is to have a central server which everyone uses as the \"official\" server (e.g. GitHub) then it might be easier to create an empty repository there.

The next list of commands will describe how to create a repository on a workstation:

`user `[`$`]`cd ~/src `

`user `[`$`]`mkdir hello `

`user `[`$`]`cd hello `

`user `[`$`]`touch readme.txt `

`user `[`$`]`git init `

The local repository has now been created.

** Note**\
The actual repository resides the [.git] folder, so don\'t delete it or the parent [hello] folder, which would mean losing everything.

Let\'s make some edits:

`user `[`$`]`echo "Hello, world!" >> readme.txt `

The new [readme.txt] file must be added (staged) before it can be included in the git repository. Use the next commands to stage the file and to make the commit:

`user `[`$`]`git add readme.txt `

`user `[`$`]`git commit -m "Added text to readme.txt" `

One of many nice features of git - on commit message writing screen (for example in Vim) [you can see the diff](https://stackoverflow.com/a/46160765/1879101)

[FILE] **`~/.gitconfig`**

    [commit]
        verbose = true

### [Bash completion]

To setup [bash completion](https://wiki.gentoo.org/wiki/Bash#Tab_completion "Bash") ([see here](https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Bash) for more info):

[FILE] **`~/.config/bashrc`**

    .  /usr/share/bash-completion/completions/git

### [Zsh completion]

[Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh") will prefer completions that come later on `fpath`. Since both [[[app-shells/zsh]](https://packages.gentoo.org/packages/app-shells/zsh)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] install a completion script [\_git], and Git\'s comes later on `fpath`, default installations of both will use Git\'s packaged Zsh completion.

If you prefer to use Zsh\'s packaged completion script, adjust `fpath` so that the containing directory is earlier on `fpath`:

[FILE] **`~/.zshrc`**

    # Assuming normal options
    fpath=(/usr/share/zsh/5.9/functions/Completion/Unix/_git $fpath)

### [Status in bash prompt]

It is possible to configure the [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") prompt to show information such as the name of the current branch, flag of uncommited changes, number of commits that were not pushed, etc., all without additional software^[\[1\]](#cite_note-1)^:

[FILE] **`~/.config/bashrc`**

    source /usr/share/git/git-prompt.sh
    export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w\[\033[01;33m\]$(__git_ps1)\[\033[01;34m\] \$\[\033[00m\] '
    export GIT_PS1_SHOWDIRTYSTATE=1

Similar code works for [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh"), also.

To see numbers like `[master ↑·2|●1✚ 1]`, and with time: use [https://github.com/magicmonty/bash-git-prompt](https://github.com/magicmonty/bash-git-prompt).

### [Server]

This section will cover setting up a Git server for remote project management through SSH.

** Note**\
The Git server is only necessary if the intent is to have an *unauthenticated read-only server* for people to get code from. See here: [https://git-scm.com/book/en/Git-on-the-Server-Git-Daemon](https://git-scm.com/book/en/Git-on-the-Server-Git-Daemon). If not sure then skip this section.

#### [Initial setup]

Start by creating the required group, user, and home directory. The user uses the `git-shell` to prevent normal shell access.

`root `[`#`]`groupadd git `

`root `[`#`]`useradd -m -g git -d /var/git -s /usr/bin/git-shell git`

Edit [/etc/conf.d/git-daemon] to change user from *\"nobody\"* to *\"git\"* and start the daemon:

[FILE] **`/etc/conf.d/git-daemon`**

    GIT_USER="git"
    GIT_GROUP="git"

If desired to accept git push and allow access all direct, it needs two options \--enable=receive-pack and \--export-all in GITDAEMON_OPTS , e.g.:

[FILE] **`/etc/conf.d/git-daemon`**

    GITDAEMON_OPTS="--syslog --export-all --enable=receive-pack --base-path=/var/git"

Start the daemon:

`root `[`#`]`/etc/init.d/git-daemon start`

### [SSH keys]

[SSH](https://wiki.gentoo.org/wiki/SSH "SSH") is the preferred method to handle the secure communications between client and server.

** Tip**\
For more information and instructions on how to enable, create, and share keys, please see the [SSH - Passwordless Authentication](https://wiki.gentoo.org/wiki/SSH#Passwordless_authentication_to_a_remote_SSH_server "SSH") wiki page.

## [Usage]

### [Creating a patch]

See [Creating a patch](https://wiki.gentoo.org/wiki/Creating_a_patch "Creating a patch").

### [Bisecting with live ebuilds]

See [Bisecting with live ebuilds](https://wiki.gentoo.org/wiki/Bisecting_with_live_ebuilds "Bisecting with live ebuilds").

### [Create a repository and make the initial commit]

On the server:

Become the *git* user to make sure all objects are owned by this user:

`root `[`#`]`su git`

** Note**\
If the following message appears:

`root `[`#`]`su git`

    fatal: Interactive git shell is not enabled.
    hint: ~/git-shell-commands should exist and have read and execute access.

Then temporarily set the login shell to [/bin/bash] ([usermod -s /bin/bash git]) and set it back after creating the bare repository ([usermod -s /usr/bin/git-shell git]). This may be also necessary when setting ssh access (see also [this post](https://serverfault.com/questions/285324/git-shell-not-enabled)).

Create a bare repository:

`git `[`$`]`cd /var/git `

`git `[`$`]`mkdir /var/git/newproject.git `

`git `[`$`]`cd /var/git/newproject.git `

`git `[`$`]`git init --bare `

On a client station:

`git `[`$`]`mkdir ~/newproject `

`git `[`$`]`cd ~/newproject `

`git `[`$`]`git init `

`git `[`$`]`touch test `

`git `[`$`]`git add test `

`git `[`$`]`git config --global user.email "larry@gentoo.org" `

`git `[`$`]`git config --global user.name "larry_the_cow" `

`git `[`$`]`git commit -m 'initial commit' `

`git `[`$`]`git remote add origin git@example.com:/var/git/newproject.git `

`git `[`$`]`git push origin master `

Writing to config this way will create [\~/.gitconfig], but it can be moved to [\~/.config/git/config], to house the git config under git.

** Note**\
If the SSH server is not running with the default port, adding the remote should look like this, with the appropriate port (in this case `59876`) following the host name:

`user `[`$`]`git remote add origin ssh://git@example.com:59876/var/git/newproject.git`

### [Common commands]

Clone a repository:

`user `[`$`]`git clone git@example.com:/newproject.git`

`user `[`$`]`git clone git://example.com:/newproject.git`

** Note**\
The following syntaxes apply in the example above:

`user `[`$`]`ssh://[user@]host.xz[:port]/path/to/repo.git/`

`user `[`$`]`git://host.xz[:port]/path/to/repo.git/`

For more, see [man git-pull(1)]

### [Repository management via GUI]

If [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] was built with [[[tk]](https://packages.gentoo.org/useflags/tk)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], Git will provide a tk GUI. Launch it from a directory containing a Git repository, using:

`user ~/repository.git $``gitk `

### [Serving and managing repositories via builtin web interface]

Git comes with a built-in web interface called [[gitweb](http://git-scm.com/docs/gitweb)]. It can run on a variety of web servers:

-   [lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") - No configuration necessary.
-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") - Some configuration necessary.
-   [nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") - A small, robust, and high-performance HTTP server and reverse proxy.

In order to use [gitweb], be sure one of the three web servers has been installed and [git] has been built with the `cgi` USE flag.

There is a simple setup script that will create a working default configuration, start a web server (the default configuration is for [lighttpd]) and open the URL in a browser. Navigate to the repositories directory. Once inside, type:

`user ~/repository.git $``git instaweb `

If [git instaweb] opens a 404 error, enable the `cgi` USE flag and rebuild [git].

#### [Help]

Find out more about the options using the the built-in help output:

`user ~/repository.git $``git help instaweb `

For additional help, consider reading the contextual man page:

`user ~/repository.git $``man git instaweb `

#### [Configuration]

Per-project configuration can be set in the repositories [.git/config] file:

`user ~/repository.git $``vim .git/config `

Values in this file should be in an [ini-style format](https://en.wikipedia.org/wiki/INI_file):

[FILE] **`.git/config`Setting lighttpd values for instaweb in a repository\'s configuration**

    [instaweb]
            ; local = true
            httpd = lighttpd
            port = 8080
            browser = elinks
            modulePath = /usr/lib64/lighttpd/

Adjust the values as needed. If the `local = true` line is uncommented (remove the `;`), [instaweb] will only be reachable from the localhost.

## [See also]

-   [Cgit](https://wiki.gentoo.org/wiki/Cgit "Cgit") --- a hyperfast web frontend for git repositories written in C
-   [Git/Tweaks](https://wiki.gentoo.org/wiki/Git/Tweaks "Git/Tweaks") --- aims to document some neat bonus features and config options available in git.
-   [Tracking changes to \"/etc\" with git for backup](https://wiki.gentoo.org/wiki/Tracking_changes_to_%22/etc%22_with_git_for_backup "Tracking changes to "/etc" with git for backup") --- Tracking the [/etc] directory with [git]
-   [CVS](https://wiki.gentoo.org/wiki/CVS "CVS")
-   [Kernel git-bisect](https://wiki.gentoo.org/wiki/Kernel_git-bisect "Kernel git-bisect") --- a [Git] tool to find the commit that caused problems between versions.
-   [Portage with Git](https://wiki.gentoo.org/wiki/Portage_with_Git "Portage with Git") --- use [Git] to synchronize the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository")

## [External resources]

-   [git flow documentation](https://jeffkreeftmeijer.com/2010/why-arent-you-using-git-flow/) --- Client side scripts to make git repository management a snap.
-   [The Official Git Handbook](https://git-scm.com/book/) --- Hosted at the official git website.
-   [Git -- The simple guide](https://rogerdudler.github.io/git-guide/)
-   [Git from the inside out](https://codewords.recurse.com/issues/two/git-from-the-inside-out) --- A well written publication from the Recurse Center. This article addresses what happens beneath the surface when using git.
-   [Lesser known git commands](https://hackernoon.com/lesser-known-git-commands-151a1918a60) --- A blog entry on helpful commands that go unnoticed.
-   [https://git-send-email.io](https://git-send-email.io) --- git collaboration over email.

1.  [[[↑](#cite_ref-1)] [[https://gist.github.com/d4rk5eed/d1651aa46e42d91ef96f](https://gist.github.com/d4rk5eed/d1651aa46e42d91ef96f)]]