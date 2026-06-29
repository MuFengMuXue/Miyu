**Resources**

[[]][Home](https://www.nongnu.org/man-db/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/man-db)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Man_page "wikipedia:Man page")

[[]][GitWeb](https://git.savannah.nongnu.org/cgit/man-db.git)

[[]]This article has some todo items:\

-   Indicate how \"man\", \"doc\" etc. USE flags influence man page installation.
-   Add links to info on setting system wide, or user specific, envars & (&for different shells).
-   Integrate information from very verbose article Man_page/Navigate that is not yet here.
-   Test [custom page](https://wiki.gentoo.org/wiki/Man_page#Install_custom_man_pages_for_local_user "Man page") section.
-   Add link to info about dangers of depclean (and virtual packages) to \"sh: /usr/bin/less: No such file or directory\" section

[![](/images/thumb/c/ca/Manpage-example.png/300px-Manpage-example.png)](https://wiki.gentoo.org/wiki/File:Manpage-example.png)

[](https://wiki.gentoo.org/wiki/File:Manpage-example.png "Enlarge")

Example of what a man page can look like when viewed with the [man] command (with the bat pager for colorization).

The [man] page system (short for **man**ual **page**) contains system reference documentation. It is found on most Unix-like systems. Man pages contain documentation about programs (executable files), libraries, system calls, configuration files, etc.

***For many pieces of software, the man pages will contain the canonical documentation***, *as set out by the projects authors, maintainers, and documentation writers.* Many software projects provide documentation in other ways, sometimes in addition to man pages, sometimes in place of them. These documentation sources will be referenced, where appropriate.

Man pages are available even when a system is not connected to the Internet. The files are usually stored in [/usr/share/man] but are viewed with a dedicated program, such as the [man] command. Man pages are traditionally written in a special markup language called [troff](https://en.wikipedia.org/wiki/troff "wikipedia:troff"), but can be generated from other markup languages.

In parallel to man pages, the [info](https://wiki.gentoo.org/wiki/Info "Info") system also provides reference documentation. The contents of the info system is sometimes the same as the man pages, sometimes it will be complimentary, sometimes only one system will contain anything at all. Man pages tend to be monolithic documents whereas info pages are hyperlinked.

It is a real asset to have documentation present on a system in a standardized and accessible way. **Getting into the habit of looking for answers in the man and info pages is very good practice, they often contain the most complete documentation available.**

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Localization]](#Localization)
    -   [[2.2] [Pager]](#Pager)
    -   [[2.3] [Color for man pages]](#Color_for_man_pages)
    -   [[2.4] [Install custom man pages for local user]](#Install_custom_man_pages_for_local_user)
    -   [[2.5] [Man pages on constrained systems]](#Man_pages_on_constrained_systems)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Viewing a man page]](#Viewing_a_man_page)
    -   [[3.3] [Sections]](#Sections)
    -   [[3.4] [Command descriptions]](#Command_descriptions)
    -   [[3.5] [Search]](#Search)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [sh: /usr/bin/less: No such file or directory]](#sh:_.2Fusr.2Fbin.2Fless:_No_such_file_or_directory)
    -   [[4.2] [No manual entry for \[\...\]]](#No_manual_entry_for_.5B....5D)
-   [[5] [Additional tools]](#Additional_tools)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Installation]

Man pages should be available by default on most Gentoo installations. The [[[sys-apps/man-db]](https://packages.gentoo.org/packages/sys-apps/man-db)[]] package is part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") and should be installed by default; an alternative is the [Mandoc](https://wiki.gentoo.org/wiki/Mandoc "Mandoc") package. The [[[sys-apps/man-pages]](https://packages.gentoo.org/packages/sys-apps/man-pages)[]] package provides many basic man pages and is also part of the system set.

## [Configuration]

### [Localization]

If [localized](https://wiki.gentoo.org/wiki/Localization "Localization") man pages are desired, set the `LINGUAS` variable in [/etc/portage/make.conf], e.g. for Italian:

[FILE] **`/etc/portage/make.conf`Locale example**

    LINGUAS="it"

Several complimentary man page packs and related packages [are available](https://packages.gentoo.org/packages/search?q=man-pages).

### [Pager]

The [man] command uses an external program, called a [pager](https://en.wikipedia.org/wiki/Terminal_pager "wikipedia:Terminal pager"), to display the man pages. [man] will first use the `PAGER` [environment variable](https://wiki.gentoo.org/wiki/Handbook:Parts/Working/EnvVar "Handbook:Parts/Working/EnvVar") (default [/usr/bin/less], from [[[sys-apps/less]](https://packages.gentoo.org/packages/sys-apps/less)[]]) to determine what pager to use. To use a different pager, the `MANPAGER` environment variable can be set. See [man man] for details on how [man] chooses the pager. See [recommended tools](https://wiki.gentoo.org/wiki/Recommended_tools#Pagers "Recommended tools") for suggestions of pagers available on Gentoo. See the Handbook on how to [set environment variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar#Defining_variables_globally "Handbook:AMD64/Working/EnvVar").

The default pager can be modified using the [[eselect]](https://wiki.gentoo.org/wiki/Eselect "Eselect") command. See [eselect pager help] for details.

Being able to choose the program that will display man pages gives quite some flexibility to the man system. In addition to pagers in general, even vim can be used to display man pages^[\[1\]](#cite_note-1)^ - for example, for a user running bash:

[FILE] **`~/.bashrc`Set MANPAGER variable**

    MANPAGER="sh -c \"col -b | nvim -c 'set ft=man ts=8 nomod nolist nonu' -c 'nnoremap i <nop>' -\""

### [Color for man pages]

Man pages can be viewed in color by setting up the pager to use color.

To use [less] to color the display or man pages, set the `MANPAGER` environment variable accordingly. For example, for a user running bash:

[FILE] **`~/.bashrc`Set MANPAGER variable**

    MANPAGER="less -R --use-color -Dd+r -Du+b"

The [bat] pager ([[[sys-apps/bat]](https://packages.gentoo.org/packages/sys-apps/bat)[]]) can also be used for a pleasing color output^[\[2\]](#cite_note-2)^. For example:

[FILE] **`~/.bashrc`Set MANPAGER variable**

    # sh is used because MANPAGER cannot use pipes by itself.
    export MANPAGER="sh -c 'col -bx | bat -l man -p'"

See the Handbook on how to [set environment variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar#Defining_variables_globally "Handbook:AMD64/Working/EnvVar").

### [Install custom man pages for local user]

If user-specific man pages are required, they can be simply copied to an appropriate path, and referenced in the configuration.

Consider for example pages in [\~/.local/share/man] (respecting the section hierarchy). Adjust the `MANPATH` environment variable (for bash):

[FILE] **`~/.bash_profile`Adding the full local path to `MANPATH` environment variable.**

    MANPATH="$/.local/share/man:$"

Reference [\~/.local/share/man] for [mandb] to manage the database index cache:

[FILE] **`~/.manpath`Instructing [mandb] where to look.**

    MANDATORY_PATH /home/user/.local/share/man

Recreate the database:

`user `[`$`]`mandb --create --user-db`

The custom pages should now be available with the [man] command.

### [Man pages on constrained systems]

Most packages install additional man pages. This can be avoided to save small amounts of disk space, for creating embedded systems, for example. **This saves very little space, and is meant for extremely constrained environments only.**

It is useful to have the man pages installed, they should be omitted **only if absolutely necessary**.

To negate man page installation, add the following feature to [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`No man page example**

    FEATURES="noman"

## [Usage]

### [Invocation]

Man pages can be viewed using the [man] command, typed in a terminal. For example, to view the man page on [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") for the [emerge] command:

`user `[`$`]`man emerge`

Options:

`user `[`$`]`man --help`

    Usage: man [OPTION...] [SECTION] PAGE...

      -C, --config-file=FILE     use this user configuration file
      -d, --debug                emit debugging messages
      -D, --default              reset all options to their default values
          --warnings[=WARNINGS]  enable warnings from groff

     Main modes of operation:
      -f, --whatis               equivalent to whatis
      -k, --apropos              equivalent to apropos
      -K, --global-apropos       search for text in all pages
      -l, --local-file           interpret PAGE argument(s) as local filename(s)
      -w, --where, --path, --location
                                 print physical location of man page(s)
      -W, --where-cat, --location-cat
                                 print physical location of cat file(s)

      -c, --catman               used by catman to reformat out of date cat pages
      -R, --recode=ENCODING      output source page encoded in ENCODING

     Finding manual pages:
      -L, --locale=LOCALE        define the locale for this particular man search
      -m, --systems=SYSTEM       use manual pages from other systems
      -M, --manpath=PATH         set search path for manual pages to PATH

      -S, -s, --sections=LIST    use colon separated section list

      -e, --extension=EXTENSION  limit search to extension type EXTENSION

      -i, --ignore-case          look for pages case-insensitively (default)
      -I, --match-case           look for pages case-sensitively

          --regex                show all pages matching regex
          --wildcard             show all pages matching wildcard

          --names-only           make --regex and --wildcard match page names only,
                                 not descriptions

      -a, --all                  find all matching manual pages
      -u, --update               force a cache consistency check

          --no-subpages          don't try subpages, e.g. 'man foo bar' => 'man
                                 foo-bar'

     Controlling formatted output:
      -P, --pager=PAGER          use program PAGER to display output
      -r, --prompt=STRING        provide the `less' pager with a prompt

      -7, --ascii                display ASCII translation of certain latin1 chars
      -E, --encoding=ENCODING    use selected output encoding
          --no-hyphenation, --nh turn off hyphenation
          --no-justification,                              --nj   turn off justification
      -p, --preprocessor=STRING  STRING indicates which preprocessors to run:
                                 e - [n]eqn, p - pic, t - tbl,
    g - grap, r - refer, v - vgrind

      -t, --troff                use groff to format pages
      -T, --troff-device[=DEVICE]   use groff with selected device

      -H, --html[=BROWSER]       use lynx or BROWSER to display HTML output
      -X, --gxditview[=RESOLUTION]   use groff and display through gxditview
                                 (X11):
                                 -X = -TX75, -X100 = -TX100, -X100-12 = -TX100-12
      -Z, --ditroff              use groff and force it to produce ditroff

      -?, --help                 give this help list
          --usage                give a short usage message
      -V, --version              print program version

    Mandatory or optional arguments to long options are also mandatory or optional
    for any corresponding short options.

    Report bugs to cjwatson@debian.org.

A more thorough explanation of the [man] command can be found in the [Navigate](https://wiki.gentoo.org/wiki/Man_page/Navigate "Man page/Navigate") sub article.

### [Viewing a man page]

Presuming [less], or similar, is used as the pager, navigation of a man page can be performed using the [↑] and [↓] arrow keys (or the [j] and [k] keys if Vim navigation is preferred). Scroll page wise with the [Page Up] and [Page Down] keys.

Search using the [/] key followed by the search term, then [Enter]. After finding the first term, type [n] for the next occurrence.

Press [h] for more help on viewing man pages.

**Press [q] to quit.**

** Tip**\
If the less pager gets into a mode in which pressing [q] does not quit immediately, pressing [ESC] several times before pressing [q] may help, or even [Ctrl]+[c].

### [Sections]

Manuals have different *sections*, for when the same term is used in different domains. The sections are numbered : 1 *general commands*, 2 *system calls*, 3 *library functions*, 4 *special files and drivers*, 5 *file formats and conventions*, 6 *games and screensavers*, 7 *miscellaneous*, 8 *system administration commands and daemons*.

When there are pages in more than one section, the sections are searched following a pre-defined order, and the first page found will be shown. For example, to show the first available page for the *ebuild* manual, which happens to be section 1, type:

`user `[`$`]`man ebuild`

A page from a specific section can be requested. For example, to show the *ebuild* page from section 5:

`user `[`$`]`man 5 ebuild`

To list available sections for a given page, use the `-f` option:

`user `[`$`]`man -f ebuild`

### [Command descriptions]

If all that is wanted is to know what a command *is*, a one line description can be shown with the [whatis] command (part of [[[sys-apps/man-db]](https://packages.gentoo.org/packages/sys-apps/man-db)[]]):

`user `[`$`]`whatis emerge`

    emerge (1)           - Command-line interface to the Portage system

See [man whatis] for more information.

### [Search]

To search the man page descriptions for a keyword, use:

`user `[`$`]`man -k <keyword>`

[apropos] (part of [[[sys-apps/man-db]](https://packages.gentoo.org/packages/sys-apps/man-db)[]]) can also search the whatis database, for example to search for pages with \"portage\" in their descriptions:

`user `[`$`]`apropos portage`

    color.map [color]    (5)  - custom color settings for Portage
    ebuild               (1)  - a low level interface to the Portage system
    ...

Type [man apropos] in a terminal for more information.

## [Troubleshooting]

### [][sh: /usr/bin/less: No such file or directory]

If the pager required by [man] is inaccessible, a \"No such file or directory\" error is printed. For example, if the [less] command is missing:

`user `[`$`]`man emerge`

    sh: /usr/bin/less: No such file or directory
    Error executing formatting or display command.
    System command (cd "/usr/share/man" && (echo ".ll 9.9i"; echo ".nr LL 9.9i"; echo ".pl 1100i"; /bin/bzip2 -c -d '/usr/share/man/man1/emerge.1.bz2'; echo ".\\\""; echo ".pl \n(nlu+10") | /usr/bin/gtbl | /usr/bin/nroff -mandoc | /usr/bin/less) exited with status 127.
    No manual entry for emerge

One cause of this can be [[[sys-apps/less]](https://packages.gentoo.org/packages/sys-apps/less)[]] being removed by [emerge \--depclean]. When [using the `--depclean` option](https://wiki.gentoo.org/wiki/Knowledge_Base:Remove_orphaned_packages "Knowledge Base:Remove orphaned packages"), the `--ask` option should always be used, and the list of packages to be removed carefully reviewed.

One fix could be renstalling [[[sys-apps/less]](https://packages.gentoo.org/packages/sys-apps/less)[]]:

`root `[`#`]`emerge --ask sys-apps/less`

Alternatively, the `PAGER` or `MANPAGER` environment variables may be set to appropriate values. See [pager](https://wiki.gentoo.org/wiki/Man_page#Pager "Man page") section.

### [][No manual entry for \[\...\]]

If the [man] command reports an error beginning *\"No manual entry for\"*, running [mandb] as root to initialize and manually update the index database caches may help^[\[3\]](#cite_note-3)^. Gentoo performs this action daily via a [cron](https://wiki.gentoo.org/wiki/Cron "Cron") job, this should not be impeded.

## [Additional tools]

-   [emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs") should be able to be [set up to view man pages](https://emacs.stackexchange.com/questions/59462/can-i-set-manpager-to-open-a-man-page-with-emacs).
-   [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") Konqueror ([[[kde-apps/konqueror]](https://packages.gentoo.org/packages/kde-apps/konqueror)[]]) can render man pages. Enter in the address bar *`man:/`* followed by the man page name, e.g.: *`man:/ebuild`*. To view a specific section, add the section in parentheses, e.g.: *`man:/ebuild(5)`*.
-   KHelpCenter ([[[kde-apps/khelpcenter]](https://packages.gentoo.org/packages/kde-apps/khelpcenter)[]]) KDE documentation viewer.
-   Yelp ([[[gnome-extra/yelp]](https://packages.gentoo.org/packages/gnome-extra/yelp)[]]) GNOME documentation viewer. Man pages can be viewed in Yelp by launching from the command line and specifying the man page. For example, to view the [bash](https://wiki.gentoo.org/wiki/Bash "Bash") man page, enter [yelp man:bash].

## [See also]

-   [Info](https://wiki.gentoo.org/wiki/Info "Info") --- used to view and navigate info pages that contain computer program documentation. It is part of the [Texinfo](https://www.gnu.org/software/texinfo/) documentation system.
-   [Man page/Navigate](https://wiki.gentoo.org/wiki/Man_page/Navigate "Man page/Navigate") --- shows how to navigate man pages using the [man] command.
-   [tldr pages](https://wiki.gentoo.org/wiki/Tldr_pages "Tldr pages") --- a project to provide brief documentation for [CLI](https://wiki.gentoo.org/wiki/Shell "Shell") commands.
-   [Full manpages](https://wiki.gentoo.org/wiki/Full_manpages "Full manpages") --- Full **[man pages]** for important Gentoo commands or concepts.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://zameermanji.com/blog/2012/12/30/using-vim-as-manpager/](https://zameermanji.com/blog/2012/12/30/using-vim-as-manpager/)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/sharkdp/bat#how-to-use](https://github.com/sharkdp/bat#how-to-use)]]
3.  [[[↑](#cite_ref-3)] [[https://forums.gentoo.org/viewtopic-t-1109122.html](https://forums.gentoo.org/viewtopic-t-1109122.html)]]