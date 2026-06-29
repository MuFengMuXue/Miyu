Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Equery/de "Equery (8% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Equery/es "Equery (48% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Equery/it "Equery (47% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Equery/hu "equery (63% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Equery/pt-br "Equery (48% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Equery/ru "Equery (63% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Equery/zh-cn "Equery (48% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Equery/ja "Equery (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Equery/ko "Equery/ko (47% translated)")

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")][Project](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")

[[]][Package information](https://packages.gentoo.org/packages/app-portage/gentoolkit)

[[]][GitWeb](https://gitweb.gentoo.org/proj/gentoolkit.git)

[[]][Bugs (upstream)](https://bugs.gentoo.org/)

**equery** is a tool to make several common [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") operations simpler. Among other operations, it can display package dependencies, metadata, and installed files.

[equery] is part of [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit"). See [man equery] for full information on all available modules and options along with some useful examples.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Finding the package that a file came from with belongs (b)]](#Finding_the_package_that_a_file_came_from_with_belongs_.28b.29)
    -   [[2.3] [Verifying package integrity with check (k)]](#Verifying_package_integrity_with_check_.28k.29)
    -   [[2.4] [Listing all packages depending on a package with depends (d)]](#Listing_all_packages_depending_on_a_package_with_depends_.28d.29)
    -   [[2.5] [Getting dependency graphs with depgraph (g)]](#Getting_dependency_graphs_with_depgraph_.28g.29)
    -   [[2.6] [Listing files installed by a package with files (f)]](#Listing_files_installed_by_a_package_with_files_.28f.29)
    -   [[2.7] [Looking for packages that have a specific USE flag with hasuse (h)]](#Looking_for_packages_that_have_a_specific_USE_flag_with_hasuse_.28h.29)
    -   [[2.8] [Display keywords for specified package (y)]](#Display_keywords_for_specified_package_.28y.29)
    -   [[2.9] [Listing packages with list (l)]](#Listing_packages_with_list_.28l.29)
        -   [[2.9.1] [Listing all installed packages]](#Listing_all_installed_packages)
        -   [[2.9.2] [Listing packages available in ebuild repositories]](#Listing_packages_available_in_ebuild_repositories)
    -   [[2.10] [Viewing package metadata with meta (m)]](#Viewing_package_metadata_with_meta_.28m.29)
    -   [[2.11] [Finding package sizes with size (s)]](#Finding_package_sizes_with_size_.28s.29)
    -   [[2.12] [Listing per-package USE flags with uses (u)]](#Listing_per-package_USE_flags_with_uses_.28u.29)
    -   [[2.13] [Finding the ebuild path with which (w)]](#Finding_the_ebuild_path_with_which_.28w.29)
-   [[3] [Tips]](#Tips)
    -   [[3.1] [Use shell aliases for less typing]](#Use_shell_aliases_for_less_typing)
    -   [[3.2] [Module short name cheat-sheet]](#Module_short_name_cheat-sheet)
-   [[4] [See also]](#See_also)

## [Installation]

Equery is part of the [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] package, see the [Gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") article for installation instructions.

## [Usage]

[equery] is based on a system of modules, each of which has a [shorthand name](https://wiki.gentoo.org/wiki/Equery#Module_short_name_cheat-sheet "Equery").

### [Invocation]

To list all modules and display other basic-usage information, run:

`user `[`$`]`equery --help`

    Gentoo package query tool
    Usage: equery [global-options] module-name [module-options]

    global options
     -h, --help              display this help message
     -q, --quiet             minimal output
     -C, --no-color          turn off colors
     -N, --no-pipe           turn off pipe detection
     -V, --version           display version info

    modules (short name)
     (b)elongs               list what package FILES belong to
     chec(k)                 verify checksums and timestamps for PKG
     (d)epends               list all packages directly depending on ATOM
     dep(g)raph              display a tree of all dependencies for PKG
     (f)iles                 list all files installed by PKG
     h(a)s                   list all packages for matching ENVIRONMENT data stored in /var/db/pkg
     (h)asuse                list all packages that have USE flag
     ke(y)words              display keywords for specified PKG
     (l)ist                  list package matching PKG
     (m)eta                  display metadata about PKG
     (s)ize                  display total size of all files owned by PKG
     (u)ses                  display USE flags for PKG
     (w)hich                 print full path to ebuild for PKG

Include a module name to display information for that specific module: [equery \--help \<module\>].

** Warning**\
Do not forget to **quote input when using special shell characters** like asterisks or greater than/less than signs.

equery accepts [version specifiers](https://wiki.gentoo.org/wiki/Version_specifier "Version specifier") similarly to [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge"). Thus package categories can sometimes be omitted, such that [equery list gcc] can be used in place of [equery list sys-devel/gcc], and versions can be appended to package names: [equery list \'\>=sys-devel/gcc-4\']. [equery] does not understand partial package names:

`user `[`$`]`equery check zilla`

    !!! No package found matching zilla

Unlike [emerge], [equery] can accept shell-like globbing in the category and/or package name: [equery check \'\*zilla\*], [equery check \'www-c\*/\*\'].

Most equery modules will accept multiple inputs: [equery hasuse sse sse2].

A few modules also allow full regular expressions: [equery -q list \--portage-tree \--full-regex \'\[kr\]?flickr.\*\']

** Note**\
Globbing support replaced a number of older options in [equery]. For example, to act on all packages in a certain set, use a `'*'` (asterisk). To act on all packages in a category, use `'category-name/*'`.

### [][Finding the package that a file came from with belongs (b)]

`user `[`$`]`equery belongs -e /usr/bin/glxgears`

     * Searching for /usr/bin/glxgears ...
     x11-apps/mesa-progs-7.5.1 (/usr/bin/glxgears)

`belongs` can search for files matching a regular expression with the `-f` option. The `-e` option stops searching after it finds a match. Since no file on your system should be owned by two packages, this is a safe optimization.

A short version of `belongs` (`b`) can also be used. For example, to list what package [equery] belongs to:

`user `[`$`]`equery b equery`

     * Searching for equery ...
    app-portage/gentoolkit-0.3.0.8-r2 (/usr/lib/python-exec/python2.7/equery)
    app-portage/gentoolkit-0.3.0.8-r2 (/usr/lib64/python3.3/site-packages/gentoolkit/test/equery)
    app-portage/gentoolkit-0.3.0.8-r2 (/usr/bin/equery -> ../lib/python-exec/python-exec2)
    app-portage/gentoolkit-0.3.0.8-r2 (/usr/lib64/python2.7/site-packages/gentoolkit/equery)
    app-portage/gentoolkit-0.3.0.8-r2 (/usr/lib/python-exec/python3.3/equery)
    app-portage/gentoolkit-0.3.0.8-r2 (/usr/lib64/python2.7/site-packages/gentoolkit/test/equery)
    app-portage/gentoolkit-0.3.0.8-r2 (/usr/lib64/python3.3/site-packages/gentoolkit/equery)

### [][Verifying package integrity with check (k)]

Sometimes it is useful to check a package\'s integrity. [equery] can verify MD5 sums as well as timestamps to indicate when a package might have been corrupted, replaced, or removed.

`user `[`$`]`equery check gentoolkit`

     * Checking app-portage/gentoolkit-0.3.0_rc7 ...
       71 out of 71 files passed

### [][Listing all packages depending on a package with depends (d)]

Ever wonder why a certain package has been installed on the system? [equery] can tell which packages list it as a dependency with `depends`. Include indirect dependencies with the `-D` option.

`user `[`$`]`equery depends pygtk`

     * Searching for pygtk ...
    app-admin/pessulus-2.24.0 (>=dev-python/pygtk-2.6.0)
    app-editors/gedit-2.24.3 (python ? >=dev-python/pygtk-2.12)
    dev-libs/libgweather-2.24.3 (python ? >=dev-python/pygtk-2)
    dev-python/gnome-python-base-2.22.3 (>=dev-python/pygtk-2.10.3)
    dev-python/gnome-python-desktop-base-2.24.1 (>=dev-python/pygtk-2.10.3)
    [...]

A second example lists all packages directly depending on udev:

`user `[`$`]`equery d udev`

    sys-auth/consolekit-0.4.5_p20120320 (acl ? >=sys-fs/udev-146-r1)
    sys-fs/cryptsetup-1.4.1 (>=sys-fs/udev-124)
                            (>=sys-fs/udev-182[static-libs])
                            (<=sys-fs/udev-171-r6)
    sys-fs/lvm2-2.02.88 (>=sys-fs/udev-151-r4)
    virtual/dev-manager-0 (sys-fs/udev)
    x11-libs/cairo-1.10.2-r2 (drm ? >=sys-fs/udev-136)

** Note**\
This output will include optional dependencies governed by USE flags, i.e. `acl` USE in `(acl ? >=sys-fs/udev-146-r1)` above, even if that USE flag is not active. A package would only be a dependency if that USE flag is active.

### [][Getting dependency graphs with depgraph (g)]

`depgraph` is the opposite of `depends`. It will find all ebuilds that a given package depends on (not the ebuilds that depend on that package). When it finds a dependency, it will recursively search *that* package\'s dependencies. Control how deep the tree gets with the `--depth` option.

`user `[`$`]`equery depgraph mozilla-firefox`

     * Searching for mozilla-firefox ...
     * dependency graph for www-client/mozilla-firefox-2.0.0.19:
    `-- www-client/mozilla-firefox-2.0.0.19
     `-- virtual/jre-1.6.0 (virtual/jre) [java]
      `-- virtual/jdk-1.6.0 (virtual/jdk-1.6.0*)
      `-- dev-java/icedtea6-bin (unable to resolve: package masked or removed)
       `-- dev-java/sun-jdk-1.6.0.15
        `-- dev-java/java-sdk-docs-1.6.0.10 [doc]
         `-- app-arch/unzip-6.0-r1
          `-- app-arch/bzip2-1.0.5-r1 [bzip2]
        `-- sys-libs/glibc-2.9_p20081201-r2
         `-- sys-devel/gettext-0.17 [nls]
          `-- virtual/libiconv-0 (virtual/libiconv)
    [...]

Notice how `jre` is a *direct* dependency and `jdk` is an *indirect* dependency if the `java` USE is set?

### [][Listing files installed by a package with files (f)]

[equery] can list all the files installed by an ebuild with the `files` module. Try `--tree` to get an easy to read directory layout. Use `--filter` to only find a certain type of file. For example, to find where executables were installed use `--filter=cmd`, or to quickly find the configuration file location try `--filter=conf`.

`user `[`$`]`equery files --tree gentoolkit`

     * Searching for gentoolkit ...
     * Contents of app-portage/gentoolkit-0.3.0_rc7:
     /etc
       > /eclean
          + distfiles.exclude
          + packages.exclude
       > /env.d
          + 99gentoolkit-env
       > /revdep-rebuild
          + 99revdep-rebuild
     /usr
       > /bin
          + eclean
          + eclean-dist -> eclean
          + eclean-pkg -> eclean
          + epkginfo
          + equery
          + eread
          + euse
          + glsa-check
          + revdep-rebuild
       > /lib
          > /python2.6
             > /site-packages
                > /gentoolkit
                + gentoolkit-0.3.0_rc7-py2.6.egg-info
                   + __init__.py
                   > /equery
                      + __init__.py
                      + belongs.py
                      + changes.py
                      + check.py
                      + depends.py
                      + depgraph.py
                      + files.py
    [...]

Another example, to list all files installed by [[[media-sound/ncmpcpp]](https://packages.gentoo.org/packages/media-sound/ncmpcpp)[]]:

`user `[`$`]`equery f ncmpcpp`

     * Searching for ncmpcpp ...
     * Contents of media-sound/ncmpcpp-0.5.10:
    /usr
    /usr/bin
    /usr/bin/ncmpcpp
    /usr/share
    /usr/share/bash-completion
    /usr/share/bash-completion/ncmpcpp
    /usr/share/doc
    /usr/share/doc/ncmpcpp-0.5.10
    /usr/share/doc/ncmpcpp-0.5.10/AUTHORS.bz2
    /usr/share/doc/ncmpcpp-0.5.10/NEWS.bz2
    /usr/share/doc/ncmpcpp-0.5.10/config.bz2
    /usr/share/doc/ncmpcpp-0.5.10/keys.bz2
    /usr/share/man
    /usr/share/man/man1
    /usr/share/man/man1/ncmpcpp.1.bz2

Descriptions of other modules and additional command line flags can be found in the equery [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") ([man equery]).

### [][[] Looking for packages that have a specific USE flag with hasuse (h)]

`hasuse` can be used to find packages with a given USE flag. `hasuse` will not indicate if the flag has been enabled or not; it simply outputs a list of ebuilds that have the queried flag as an option. See the EXAMPLES section of `hasuse` in the [equery] man page for more tip on getting this kind of information.

`user `[`$`]`equery hasuse qt3 qt4`

     * Searching for USE flag qt3 ...
    [IP-] [  ] app-crypt/pinentry-0.7.5 (0)
    [IP-] [  ] net-dns/avahi-0.6.24-r2 (0)
    [IP-] [  ] net-wireless/wpa_supplicant-0.6.9 (0)

     * Searching for USE flag qt4 ...
    [IP-] [  ] net-dns/avahi-0.6.24-r2 (0)
    [IP-] [  ] net-wireless/wpa_supplicant-0.6.9 (0)

### [][Display keywords for specified package (y)]

** Note**\
As of 2023-01-27, the **keywords** module is not documented in the equery(1) man page - cf. [bug #565408](https://bugs.gentoo.org/565408). However, a description is provided below. The keywords module is documented in its alias command eshowkw(1) man page.

`keywords` can be used to display the keyword status of a package on various architectures.

`user `[`$`]`equery keywords coreutils`

    Keywords for sys-apps/coreutils:
              |                               |   u   |
              | a   a     p s     l r   a     |   n   |
              | m   r h   p p   i o i s l m m | e u s | r
              | d a m p p c a x a o s 3 p 6 i | a s l | e
              | 6 r 6 p p 6 r 8 6 n c 9 h 8 p | p e o | p
              | 4 m 4 a c 4 c 6 4 g v 0 a k s | i d t | o
    ----------+-------------------------------+-------+-------
      8.32-r1 | + + + + + + + + ~ o ~ ~ ~ ~ ~ | 7 # 0 | gentoo
       9.1-r1 | + + + + + + + + ~ ~ ~ ~ ~ ~ ~ | 7 #   | gentoo
    [I]9.1-r2 | + + + + + + + + ~ ~ ~ ~ ~ ~ ~ | 7 o   | gentoo

`+` indicates the package version is available on stable; `~` indicates its availability on testing; and `o` indicates the package version is unavailable. `[I]` indicates the package version currently installed; `[M]` indicates the package is masked. On the far right the section labeled eapi is for the version of the ebuild tools that were used. More information can be found [here](https://devmanual.gentoo.org/ebuild-writing/eapi/index.html)

### [][Listing packages with list (l)]

`list` is a simple, yet powerful module to list packages that are either installed, present in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") or present in another [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") configured with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage").

#### [Listing all installed packages]

The standard query will search installed packages for the given package name. Passing in `'*'` displays all packages in the set:

`user `[`$`]`equery list '*'`

     * Searching for * ...
    [IP-] [  ] app-admin/eselect-1.2.3 (0)
    [IP-] [  ] app-admin/eselect-ctags-1.10 (0)
    [IP-] [  ] app-admin/eselect-esd-20060719 (0)
    [IP-] [  ] app-admin/eselect-fontconfig-1.0 (0)
    [IP-] [  ] app-admin/eselect-opengl-1.0.8-r1 (0)
    [IP-] [  ] app-admin/eselect-python-20090824 (0)
    [IP-] [  ] app-admin/eselect-ruby-20081227 (0)
    [IP-] [  ] app-admin/eselect-vi-1.1.5 (0)
    [IP-] [  ] app-admin/perl-cleaner-1.05 (0)
    [IP-] [  ] app-admin/pessulus-2.24.0 (0)
    [IP-] [  ] app-admin/python-updater-0.7 (0)
    [IP-] [  ] app-admin/sudo-1.7.2_p1 (0)
    [...]

In the leftmost field it is possible to see all the above packages are `I`(nstalled) and from the `P`(ortage) tree. They are not masked (the second field is blank), and they are all installed in the default slot (0).

#### [Listing packages available in ebuild repositories]

Use local options to look for packages in the [Gentoo repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") and overlays: the `--portage-tree` (`-p`) option will include packages available from the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") in the search, the `--overlay-tree` (`-o`) option will include packages available in overlays (ebuild repositories) that are configured with Portage in the search:

`user `[`$`]`equery list -po vim`

     * Searching for vim ...
    [-P-] [  ] app-editors/vim-7.0.235 (0)
    [-P-] [ ~] app-editors/vim-7.0.243 (0)
    [-P-] [  ] app-editors/vim-7.1.123 (0)
    [-P-] [ ~] app-editors/vim-7.1.330 (0)
    [-P-] [  ] app-editors/vim-7.2 (0)
    [-P-] [ ~] app-editors/vim-7.2.108 (0)
    [IP-] [  ] app-editors/vim-7.2.182 (0)
    [-P-] [ ~] app-editors/vim-7.2.238 (0)
    [-P-] [ ~] app-editors/vim-7.2.264 (0)

It is possible to see that version 7.2.182 is installed and that there are no versions available from an overlay. Users can see which versions are keyword masked by the `~` in the second field.

** Tip**\
To only list available packages, excluding packages that are already installed, add the `--exclude-installed` (`-I`) option.

### [][Viewing package metadata with meta (m)]

Each package in the [Gentoo repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") provides at least some [metadata](https://devmanual.gentoo.org/ebuild-writing/misc-files/metadata/index.html) about its maintainer, etc. The amount of useful information depends on how much package maintainers decide to provide. With no options, `meta` returns some basic useful information.

`user `[`$`]`equery meta gnucash`

     * app-office/gnucash [gentoo]
     Maintainer:  tove@gentoo.org (Torsten Veller)
     Upstream:    None specified
     Location:    /var/db/repos/gentoo/app-office/gnucash
     Keywords:    2.2.9-r1:0: alpha amd64 ppc sparc x86
     Keywords:    2.2.9-r2:0:
     Keywords:    2.3.8:0:
     Keywords:    2.3.10:0: ~alpha ~amd64 ~ppc ~sparc ~x86

Some maintainers provide extra information about a package, which can be very useful:

`user `[`$`]`equery meta --description emacs`

     * app-editors/emacs
      GNU Emacs is an extensible, customizable text editor - and more. At its core
      is an interpreter for Emacs Lisp, a dialect of the Lisp programming language
      with extensions to support text editing. The features of GNU Emacs include:
       * Content-sensitive editing modes, including syntax coloring, for a wide
         variety of file types including plain text, source code, and HTML.
       * Complete built-in documentation, including a tutorial for new users.
       * Support for many languages and their scripts, including all the European
         "Latin" scripts, Russian, Greek, Japanese, Chinese, Korean, Thai,
         Vietnamese, Lao, Ethiopian, and some Indian scripts.
       * Highly customizable, using Emacs Lisp code or a graphical customization
         interface.
       * A large number of extensions that add other functionality, including a
         project planner, mail and news reader, debugger interface, calendar, and
         more. Many of these extensions are distributed with GNU Emacs; others are
         available separately.

### [][Finding package sizes with size (s)]

Ever been curious to find out how much space a specific package is occupying? Since a package could have its files over a number of directories, the usual [du -hc] command might not give the correct figure. Don\'t worry, [equery] to the rescue!

`user `[`$`]`equery size openoffice-bin`

     * app-office/openoffice-bin-3.1.1
             Total files : 4624
             Total size  : 361.38 MiB

Using `size` prints the total space used in human-readable units and lists the total number of files the package has. To get the total size in bytes use `--bytes`.

### [][[] Listing per-package USE flags with uses (u)]

[equery]\'s `uses` module can provide information about what USE flags are available for a specific package and which of those flags is currently enabled.

`user `[`$`]`equery uses gst-plugins-meta`

     * Searching for gst-plugins-meta ...
    [ Legend : U - flag is set in make.conf       ]
    [        : I - package is installed with flag ]
    [ Colors : set, unset                         ]
     * Found these USE flags for media-plugins/gst-plugins-meta-0.10-r2:
     U I
     + + X      : Adds support for X11
     - - a52    : Enables support for decoding ATSC A/52 streams used in DVD
     + + alsa   : Adds support for media-libs/alsa-lib (Advanced Linux Sound
                  Architecture)
     - - dvb    : Adds support for DVB (Digital Video Broadcasting)
     + + dvd    : Adds support for DVDs
     + + esd    : Adds support for media-sound/esound (Enlightened Sound Daemon)
     + + ffmpeg : Enable ffmpeg-based audio/video codec support
     + + flac   : Adds support for FLAC: Free Lossless Audio Codec
     - - mad    : Adds support for mad (high-quality mp3 decoder library and cli
                  frontend)
     + + mpeg   : Adds libmpeg3 support to various packages
     - - mythtv : Support for retrieval from media-tv/mythtv backend
     + + ogg    : Adds support for the Ogg container format (commonly used by
                  Vorbis, Theora and flac)
     - - oss    : Adds support for OSS (Open Sound System)
     + + theora : Adds support for the Theora Video Compression Codec
     + + vorbis : Adds support for the OggVorbis audio codec
     - - xv     : Adds in optional support for the Xvideo extension (an X API for
                  video playback)

Here a number of USE flags are enabled in gstreamer\'s plugin meta-package, but it can be seen that there are other USE flags available. For more information on USE flags, please refer to the [USE Flags](https://wiki.gentoo.org/wiki/Handbook:X86/Working/USE "Handbook:X86/Working/USE") chapter of the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page").

### [][Finding the ebuild path with which (w)]

`which` is a simple script to help users quickly find the file path to an ebuild. If an unversioned package name is passed using `which` it will return the path to the newest installable ebuild version. In other words, it would return the ebuild Portage would use if [emerge example/package] was typed. `which` also accepts a *versioned* package to get the path to that ebuild.

`user `[`$`]`equery which gnome`

    /var/db/repos/gentoo/gnome-base/gnome/gnome-2.26.3.ebuild

Lastly, if none of the above features of [equery] have provided an answer, try using `which` to manually search an ebuild with programs like [cat], [less] or [grep]:

`user `[`$`]`grep HOMEPAGE $(equery which gentoolkit)`

    HOMEPAGE="http://www.gentoo.org/proj/en/portage/tools/index.xml"

** Warning**\
Be aware that [equery] currently changes the format of the output if it is sent through a pipe. The piped format is intended to be easier to parse by tools, but it can be turned off by adding the `--no-pipe` option. When writing scripts that employ [equery] be aware of this behavior.

## [Tips]

### [Use shell aliases for less typing]

[Shell](https://wiki.gentoo.org/wiki/Shell "Shell") aliases can be created to access equery\'s modules directly at the command line.

When using [bash](https://wiki.gentoo.org/wiki/Bash "Bash"), [aliases](https://wiki.gentoo.org/wiki/Bash#alias "Bash") can usually be created in a given user\'s [\~/.bashrc](https://wiki.gentoo.org/wiki/Bash#.bashrc "Bash") file:

[FILE] **`~/.bashrc`**

    alias eqf='equery f'
    alias equ='equery u'
    alias eqh='equery h'
    alias eqa='equery a'
    alias eqb='equery b'
    alias eql='equery l'
    alias eqd='equery d'
    alias eqg='equery g'
    alias eqk='equery k'
    alias eqm='equery m'
    alias eqy='equery y'
    alias eqs='equery s'
    alias eqw='equery w'

### [Module short name cheat-sheet]

These short names can be used in place of the long module names when invoking equery. For example, running [equery l gcc] is the same as running [equery list gcc].

  ---------- ------------ -----------------------------------------------------------------------
  Module     Short name   Description
  belongs    b            list what package FILES belong to
  check      k            verify checksums and timestamps for PKG
  depends    d            list all packages directly depending on ATOM
  depgraph   g            display a tree of all dependencies for PKG
  files      f            list all files installed by PKG
  has        a            list all packages for matching ENVIRONMENT data stored in /var/db/pkg
  hasuse     h            list all packages that have USE flag
  keywords   y            display keywords for specified PKG
  list       l            list package matching PKG
  meta       m            display metadata about PKG
  size       s            display total size of all files owned by PKG
  uses       u            display USE flags for PKG
  which      w            print full path to ebuild for PKG
  ---------- ------------ -----------------------------------------------------------------------

## [See also]

-   [Q applets](https://wiki.gentoo.org/wiki/Q_applets "Q applets") --- a collection of small, fast [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") **q**uery utilities written in C.
-   [Eix](https://wiki.gentoo.org/wiki/Eix "Eix") --- a set of utilities for searching and diffing local [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") using a binary cache.
-   [Gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- a suite of tools to ease the administration of a Gentoo system, and [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") in particular.
-   [Useful Portage tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").