**Resources**

[[]][Home](https://newsboat.org)

[[]][Package information](https://packages.gentoo.org/packages/net-news/newsboat)

[[]][GitHub](https://github.com/Newsboat)

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Newsboat&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Newsboat is an RSS/Atom feed reader for the text console. It is an actively maintained fork of Newsbeuter.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Feeds management]](#Feeds_management)
    -   [[2.2] [Formatting / Naming links]](#Formatting_.2F_Naming_links)
    -   [[2.3] [Tags]](#Tags)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Displaying rss feeds as a timeline]](#Displaying_rss_feeds_as_a_timeline)

## [Installation]

### [USE flags]

### [USE flags for] [net-news/newsboat](https://packages.gentoo.org/packages/net-news/newsboat) [[]] [An RSS/Atom feed reader for text terminals]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-02 07:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-news/newsboat`

## [Configuration]

### [Feeds management]

Add feed URLs to the [\~/.newsboat/urls] file with any text editor one per line. This example uses the gentoo.org news feed XML:

[FILE] **`~/.newsboat/urls`urls**

    https://www.gentoo.org/feeds/news.xml

### [][Formatting / Naming links]

To have names appear instead of the long URL configure the links like this:

[FILE] **`~/.newsboat/urls`urls**

    _your_link_here_ "~_better_name_for_url_here_"

This statement will show \_better_name_for_url_here\_ instead of the URL link address in newsboat.

### [Tags]

It is possible to have various feeds under the same \"tag\". These can later be filtered by pressing the `t` key inside Newsboat. This example will add the gentoo home page to the `gentoo` tag and the linux kernel homepage to the `kernel` tag:

[FILE] **`~/.newsboat/urls`urls**

    https://www.gentoo.org/feeds/news.xml gentoo
    https://www.kernel.org/feeds/all.atom.xml kernel

## [Usage]

### [Invocation]

`user `[`$`]`newsboat --help`

    Newsboat 2.23
    usage: newsboat [-i <file>|-e] [-u <urlfile>] [-c <cachefile>] [-x <command> ...] [-h]
        -e, --export-to-opml            export OPML feed to stdout
        -r, --refresh-on-start          refresh feeds on start
        -i, --import-from-opml=<file>   import OPML file
        -u, --url-file=<urlfile>        read RSS feed URLs from <urlfile>
        -c, --cache-file=<cachefile>    use <cachefile> as cache file
        -C, --config-file=<configfile>  read configuration from <configfile>
        -X, --vacuum                    compact the cache
        -x, --execute=<command>...      execute list of commands
        -q, --quiet                     quiet startup
        -v, --version                   get version information
        -l, --log-level=<loglevel>      write a log with a certain loglevel (valid values: 1 to 6)
        -d, --log-file=<logfile>        use <logfile> as output log file
        -E, --export-to-file=<file>     export list of read articles to <file>
        -I, --import-from-file=<file>   import list of read articles from <file>
        -h, --help                      this help
            --cleanup                   remove unreferenced items from cache

## [Tips]

### [Displaying rss feeds as a timeline]

It is possible to use Newsboat\'s [queries](https://newsboat.org/releases/2.21/docs/newsboat.html#_query_feeds) to replicate a timeline-like view of rss feeds. This could be used to replicate YouTube\'s Subscription feed. This example uses two YouTube channel rss feeds and planet gentoo\'s.

[FILE] **`~/.newsboat/urls`urls**

    "query:Subscriptions:tags # \"timeline\""
    https://www.youtube.com/feeds/videos.xml?channel_id=&lt;SomeYTChannel&gt; timeline
    https://www.youtube.com/feeds/videos.xml?channel_id=&lt;SomeOtherYTChannel&gt; timeline
    https://planet.gentoo.org/rss20.xml timeline

This will create a feed named \"Subscriptions\" that will display all the entries from feeds belonging to the `timeline` tag (in this example 2 YouTube channels and the planet gentoo entries).