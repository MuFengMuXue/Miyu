This page contains [[changes](https://wiki.gentoo.org/index.php?title=Info&oldid=1220047&diff=1411639)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Info/de "Info (28% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Info/es "Info (36% translated)")
-   [français](https://wiki.gentoo.org/wiki/Info/fr "Info (20% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Info/hu "Az info parancs (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Info/ru "Info (70% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Info/ja "Info (88% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Info/ko "Info (20% translated)")

**Resources**

[[]][Home](https://www.gnu.org/software/texinfo/)

[[]][Official documentation](https://www.gnu.org/software/texinfo/manual/info-stnd/info-stnd.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/texinfo)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Info_(Unix) "wikipedia:Info (Unix)")

[[]][GitWeb](http://git.savannah.gnu.org/cgit/texinfo.git)

[[]]This article has some todo items:\

-   Rework to be less verbose.
-   etc.

[![](/images/thumb/a/ab/Pinfo.png/300px-Pinfo.png)](https://wiki.gentoo.org/wiki/File:Pinfo.png)

[](https://wiki.gentoo.org/wiki/File:Pinfo.png "Enlarge")

Pinfo showing directory node.

The **[info]** command is used to view and navigate info pages that contain computer program documentation. It is part of the [Texinfo](https://www.gnu.org/software/texinfo/) documentation system.

Most users will be familiar with the **[man](https://wiki.gentoo.org/wiki/Man_page "Man page")** documentation system. While man is good for quickly looking up items, it lacks structure in linking man pages together. Info pages can link with other pages, create menus and ease navigation in general. The contents of the man pages is sometimes complimentary to the info system, sometimes they will be different, sometimes only one system will contain anything at all.

Info pages are available even when a system is not connected to the Internet. The files are usually stored in [/usr/share/info] but are viewed with a dedicated program, such as the [info] command.

It is a real advantage to have documentation present on a system in a standardized and accessible way. Getting into the habit of looking for answers in the info and man pages is very good practice, they often contain the most complete documentation available.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Pinfo]](#Pinfo)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Browsing info pages]](#Browsing_info_pages)
        -   [[2.2.1] [Navigating to other info pages]](#Navigating_to_other_info_pages)
    -   [[2.3] [Searching through info]](#Searching_through_info)
        -   [[2.3.1] [Searching using an index]](#Searching_using_an_index)
        -   [[2.3.2] [Searching using the search command]](#Searching_using_the_search_command)
-   [[3] [Info pages stored on disk]](#Info_pages_stored_on_disk)
-   [[4] [Additional tools]](#Additional_tools)
-   [[5] [Additional documentation]](#Additional_documentation)
-   [[6] [See also]](#See_also)

## [Installation]

Info may already be present on some systems, in which case this section can be skipped. Type [whereis info] (belongs to [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]], which is usually part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)")) to determine if [info] is already installed.

### [Emerge]

Install [[[sys-apps/texinfo]](https://packages.gentoo.org/packages/sys-apps/texinfo)[]] package:

`root `[`#`]`emerge --ask sys-apps/texinfo`

### [Pinfo]

[pinfo] ([[[app-text/pinfo]](https://packages.gentoo.org/packages/app-text/pinfo)[]]) is a colorized alternative to the [info] viewer, with enhanced browsing facilities. If desired, this could be installed instead of or in parallel to [[[sys-apps/texinfo]](https://packages.gentoo.org/packages/sys-apps/texinfo)[]] (in which case substitute [pinfo] for [info] when following the rest of this document):

`root `[`#`]`emerge --ask sys-apps/pinfo`

See the pinfo [documentation](http://pinfo.sourceforge.net/doc/pinfo.html), [website](http://pinfo.sourceforge.net/), and [github](https://github.com/baszoetekouw/pinfo) for more information.

## [Usage]

### [Invocation]

To begin viewing - and navigating through - the info pages, invoke [info] with no arguments. The user will be presented with an overview of the documentation stored on their system:

`user `[`$`]`info`

Options:

`user `[`$`]`info --help`

    Usage: info [OPTION]... [MENU-ITEM...]

    Read documentation in Info format.

    Frequently-used options:
      -a, --all                    use all matching manuals
      -k, --apropos=STRING         look up STRING in all indices of all manuals
      -d, --directory=DIR          add DIR to INFOPATH
      -f, --file=MANUAL            specify Info manual to visit
      -h, --help                   display this help and exit
          --index-search=STRING    go to node pointed by index entry STRING
      -n, --node=NODENAME          specify nodes in first visited Info file
      -o, --output=FILE            output selected nodes to FILE
      -O, --show-options, --usage  go to command-line options node
          --subnodes               recursively output menu items
      -v, --variable VAR=VALUE     assign VALUE to Info variable VAR
          --version                display version information and exit
      -w, --where, --location      print physical location of Info file

    The first non-option argument, if present, is the menu entry to start from;
    it is searched for in all 'dir' files along INFOPATH.
    If it is not present, info merges all 'dir' files and shows the result.
    Any remaining arguments are treated as the names of menu
    items relative to the initial node visited.

    For a summary of key bindings, type H within Info.

    Examples:
      info                         show top-level dir menu
      info info-stnd               show the manual for this Info program
      info emacs                   start at emacs node from top-level dir
      info emacs buffers           select buffers menu entry in emacs manual
      info emacs -n Files          start at Files node within emacs manual
      info '(emacs)Files'          alternative way to start at Files node
      info --show-options emacs    start at node with emacs' command line options
      info --subnodes -o out.txt emacs
                                   dump entire emacs manual to out.txt
      info -f ./foo.info           show file ./foo.info, not searching dir

    Email bug reports to bug-texinfo@gnu.org,
    general questions and discussion to help-texinfo@gnu.org.
    Texinfo home page: http://www.gnu.org/software/texinfo/

### [Browsing info pages]

Now that info is started, the screen will be similar to this:

[CODE] **Sample info screen**

    File: dir,      Node: Top       This is the top of the INFO tree

      This (the Directory node) gives a menu of major topics.
      Typing "q" exits, "?" lists all Info commands, "d" returns here,
      "h" gives a primer for first-timers,
      "mEmacs<Return>" visits the Emacs manual, etc.

      In Emacs, you can click mouse button 2 on a menu item or cross reference
      to select it.

    * Menu:

    User Interface Toolkit
    * GDK: (gdk).           The General Drawing Kit
    * GTK: (gtk).           The GIMP Toolkit

    GNU programming tools
    * Autoconf v2.1: (autoconf).         Create source code configuration scripts.

Right now there are a bunch of entries with an asterisk before them. These are menu items for navigating through different node levels.

There are two ways of selecting menus, either with arrows or by number. In order to look at the wget info page, navigating with the arrow keys, use the [↓] key until reaching the line for wget:

[CODE] **Navigating to the wget info menu entry**

    Network Applications
    * GnuTLS: (gnutls).                     Package for Transport Layer Security.
    * Wget: (wget).         The non-interactive network downloader.
    * certtool: (gnutls)Invoking certtool.  Manipulate certificates and keys.
    * gnutls-cli: (gnutls)Invoking gnutls-cli.      GNU TLS test client.
    * gnutls-cli-debug: (gnutls)Invoking gnutls-cli-debug.  GNU TLS debug client.
    * gnutls-serv: (gnutls)Invoking gnutls-serv.    GNU TLS test server.
    * srptool: (gnutls)Invoking srptool.    Simple SRP password tool.

Once on this line, hit the [Enter] key to select the menu item. This will bring up the info page for wget:

[CODE] **The wget info page**

    File: wget.info,  Node: Top,  Next: Overview,  Up: (dir)

    Wget 1.10.2
    ***********

    This manual documents version 1.10.2 of GNU Wget, the freely available
    utility for network downloads.

       Copyright (C) 1996-2005 Free Software Foundation, Inc.

    * Menu:

    * Overview::            Features of Wget.
    * Invoking::            Wget command-line arguments.
    * Recursive Download::  Downloading interlinked pages.
    * Following Links::     The available methods of chasing links.
    * Time-Stamping::       Mirroring according to time-stamps.
    * Startup File::        Wget's initialization file.

In terms of nodes, this is considered the `Top` node for the wget page. Consider the `Top` node to be the same as the table of contents for that particular info page.

To navigate the page itself, users have a couple of different methods. First off is the standard info method. This is using the [Space] key to move forward a page and the [Backspace]/[Delete] keys to move back a page. This is the recommended method as it automatically advances/retreats to the appropriate node in the document. In order to skip entire nodes without using [Space]/[Backspace]/[Delete], users can also use the [\[] (advance backwards) and [\]] (advance forwards) keys.

Another way to navigate is through the [Page up]/[Page down] keys. These work, but they will not advance/retreat like [Space]/[Backspace]/[Delete] will.

As mentioned earlier, there are two ways of selecting menus. The second way will now be described here. The numbers `1-9` can be used to reference to the first-ninth menu entries in a document. This can be used to quickly peruse through documents. For example, users can press [3] to reach the `Recursive Download` menu entry. So press [3] and it will bring up the `Recursive Download` screen:

[CODE] **Resulting Recursive Download screen**

    File: wget.info,  Node: Recursive Download,  Next: Following Links,  Prev: Invoking,  Up: Top

    3 Recursive Download
    ********************

    GNU Wget is capable of traversing parts of the Web (or a single HTTP or
    FTP server), following links and directory structure.  We refer to this
    as to "recursive retrieval", or "recursion".

Here is a good time to note a few things. First off the top header section. This header shows the navigation capable from this particular screen. The page indicated by `Next:` can be accessed by pressing the [n] key, and the page indicated by `Prev:` can be accessed by pressing the [p] key. Please note that this will only work for the same level. If overused users could round up in totally unrelated content. It\'s better to use [Space]/[Backspace]/[Delete]/[\[]/[\]] to navigate in a linear fashion.

If for some reason users get lost, there are a few ways to get out. First is the [t] key. This will take the user straight to the toplevel (table of contents) for the particular info page being browsed. If users want to return to the last page looked out, they can do so with the [l] key. If users want to go to the above level, they can do so with the [u] key. The next chapter will look at searching for content.

#### [Navigating to other info pages]

Now that users can navigate an individual info page, it\'s important to look at accessing other info pages. The first obvious way is to go to the info page through the dir index listing of info pages. To get to the dir index from deep within a document, simply press the [d] key. From there users can search for the appropriate page they want. However, if they know the actual page, there is an easier way through the `Goto node (`[`g`]` key)` command. To go to an info page by name, type [g] to bring up the prompt and enter the name of the page in parentheses:

[CODE] **Going to an info page by name**

    * Startup File::        Wget's initialization file.
    * Examples::            Examples of usage.
    * Various::             The stuff that doesn't fit anywhere else.
    * Appendices::          Some useful references.
    * Copying::             You may give out copies of Wget and of this manual.
    --zz-Info: (wget.info.gz)Top, 24 lines --Top-------------------------------
    Goto node: (libc)

This will bring up the libc page as shown here:

[CODE] **Result of the Goto node command**

    File: libc.info,  Node: Top,  Next: Introduction,  Prev: (dir),  Up: (dir)

    Main Menu
    *********

    This is Edition 0.10, last updated 2001-07-06, of `The GNU C Library
    Reference Manual', for Version 2.3.x of the GNU C Library.

    * Menu:

    * Introduction::                 Purpose of the GNU C Library.

Now that users know how to go to info pages by name, the next section will look at searching for pieces of information using the info page\'s index.

### [Searching through info]

#### [Searching using an index]

The following example will describe how to lookup the `printf` function of the C library using the libc info page\'s index. Users should still be at the libc info page from the last section, and if not, they can use the Goto node command to do so. To utilize the index search, hit the [i] key to bring up the prompt, then enter the search term:

[CODE] **Entering an index search query**

    * Character Set Handling::       Support for extended character sets.
    * Locales::                      The country and language can affect the
                                       behavior of library functions.
    * Message Translation::          How to make the program speak the user's
                                       language.
    --zz-Info: (libc.info.gz)Top, 1291 lines --Top-- Subfile: libc.info-1.gz-----
    Index entry: printf

After pressing [Enter] upon completion of our query, users are brought to the libc definition for `printf`:

[CODE] **Result of the index search query**

    File: libc.info,  Node: Formatted Output Functions,  Next: Dynamic Output,  Prev: Other Output Conversions,  Up: Formatted Output

    12.12.7 Formatted Output Functions
    ----------------------------------

    This section describes how to call `printf' and related functions.
    Prototypes for these functions are in the header file `stdio.h'.
    Because these functions take a variable number of arguments, you _must_
    declare prototypes for them before using them.  Of course, the easiest
    way to make sure you have all the right prototypes is to just include

Users have successfully performed a search using the `libc` info page index. However, sometimes what users want is in the page itself. The next section will look at performing searches within the page.

#### [Searching using the search command]

Starting from the previous location at the `Formatted Output Functions` node, users will look at searching for the `sprintf` variation of the `printf` function. To perform a search, press the [s] key to bring up the search prompt, and then enter the query (sprintf in this case):

[CODE] **Entering a search query**

    -- Function: int wprintf (const wchar_t *TEMPLATE, ...)
         The `wprintf' function prints the optional arguments under the
         control of the wide template string TEMPLATE to the stream
         `stdout'.  It returns the number of wide characters printed, or a
    --zz-Info: (libc.info.gz)Formatted Output Functions, 127 lines --Top-- Subfile: libc.info-3.gz--
    Search for string []: sprintf

Hit [Enter] and it will show the result of the query:

[CODE] **Result of the search query**

    -- Function: int sprintf (char *S, const char *TEMPLATE, ...)
         This is like `printf', except that the output is stored in the
         character array S instead of written to a stream.  A null
         character is written to mark the end of the string.

         The `sprintf' function returns the number of characters stored in
         the array S, not including the terminating null character.

This is the needed function.

## [Info pages stored on disk]

The main info pages are held in [/usr/share/info]. Unlike the man style directory layout, [/usr/share/info] contains what is largely a rather extensive collection of files. These files have the following format:

[CODE] **info file format**

    pagename.info[-node].gz

`pagename` is the actual name of the page (example: `wget`). `[-node]` is an optional construct that designates another node level (generally these are referenced to by the toplevel of the info document in question).

In order to save space these info pages are compressed using the gzip compression scheme by default. Configure the `PORTAGE_COMPRESS` variable in [/etc/portage/make.conf] to choose different compression algorithms.

Additional info pages can be listed with the `INFOPATH` environment variable (usually set through the various [/etc/env.d/] files).

The [/usr/share/info/dir] file is used when info is run with no parameters. It contains a listing of all info pages available for users to browse.

## [Additional tools]

In order to make things easier for those that wish to browse info pages through a more friendly graphical interface, the following tools are available:

-   [[[app-text/info2html]](https://packages.gentoo.org/packages/app-text/info2html)[]] - Convert info pages to a browse-able HTML format
-   [[[app-text/pinfo]](https://packages.gentoo.org/packages/app-text/pinfo)[]] - [ncurses] based info viewer
-   [[[app-text/tkinfo]](https://packages.gentoo.org/packages/app-text/tkinfo)[]] - A tcl/tk based info browser
-   [[[app-vim/info]](https://packages.gentoo.org/packages/app-vim/info)[]] - A [vim] based info browser

The KDE browser Konqueror also allows users to browse info pages through the `info:` URI.

## [Additional documentation]

-   The [info] command can be used to view its own documentation:

`user `[`$`]`info info`

-   There is also documentation available in the man pages:

`user `[`$`]`man info`

## [See also]

-   [Man page](https://wiki.gentoo.org/wiki/Man_page "Man page") --- contains system reference documentation. It is found on most Unix-like systems.
-   [tldr pages](https://wiki.gentoo.org/wiki/Tldr_pages "Tldr pages") --- a project to provide brief documentation for [CLI](https://wiki.gentoo.org/wiki/Shell "Shell") commands.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Chris White**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*