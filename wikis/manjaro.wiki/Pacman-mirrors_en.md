[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Pacman-mirrors&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Pacman-mirrors "Pacman-mirrors (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Pacman-mirrors/fr "Les miroirs Pacman (70% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Pacman-mirrors/ru "Pacman-mirrors (100% translated)") • ‎[中文](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Pacman-mirrors&language=zh&task=view "Start translation for this language") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Pacman-mirrors/zh-cn "Pacman-mirrors (16% translated)")

## Contents

-   [[1] [Pacman-Mirrors]](#Pacman-Mirrors)
    -   [[1.1] [Purpose]](#Purpose)
    -   [[1.2] [Use]](#Use)
    -   [[1.3] [**IMPORTANT**]](#IMPORTANT)
        -   [[1.3.1] [When to use a forced metadata refresh]](#When_to_use_a_forced_metadata_refresh)
-   [[2] [TL:DR - Samples please]](#TL:DR_-_Samples_please)
    -   [[2.1] [Commands giving information]](#Commands_giving_information)
        -   [[2.1.1] [Man page]](#Man_page)
        -   [[2.1.2] [Help on usage]](#Help_on_usage)
        -   [[2.1.3] [Version]](#Version)
        -   [[2.1.4] [Mirror status]](#Mirror_status)
        -   [[2.1.5] [List available countries]](#List_available_countries)
        -   [[2.1.6] [What branch am I on]](#What_branch_am_I_on)
    -   [[2.2] [Commands using defaults]](#Commands_using_defaults)
        -   [[2.2.1] [Update mirrorlist with the fastest mirrors]](#Update_mirrorlist_with_the_fastest_mirrors)
        -   [[2.2.2] [Limit to 5 mirrors]](#Limit_to_5_mirrors)
        -   [[2.2.3] [Mirrors for your country only]](#Mirrors_for_your_country_only)
    -   [[2.3] [Commands customizing the mirror pool]](#Commands_customizing_the_mirror_pool)
        -   [[2.3.1] [Customize mirror pool by continent]](#Customize_mirror_pool_by_continent)
        -   [[2.3.2] [Customize mirror pool by countries]](#Customize_mirror_pool_by_countries)
        -   [[2.3.3] [Customize mirror pool by interactive selection]](#Customize_mirror_pool_by_interactive_selection)
        -   [[2.3.4] [Use specific protocols (prioritized)]](#Use_specific_protocols_.28prioritized.29)
        -   [[2.3.5] [Switch branch to unstable and use German mirrors]](#Switch_branch_to_unstable_and_use_German_mirrors)
        -   [[2.3.6] [Switch branch and use German mirrors with https]](#Switch_branch_and_use_German_mirrors_with_https)
    -   [[2.4] [Reset]](#Reset)
-   [[3] [Overview]](#Overview)
    -   [[3.1] [Available arguments]](#Available_arguments)
    -   [[3.2] [Files used by pacman-mirrors]](#Files_used_by_pacman-mirrors)
        -   [[3.2.1] [File: /etc/pacman-mirrors.conf (sample - can be changed by pacman-mirrors api commands)]](#File:_.2Fetc.2Fpacman-mirrors.conf_.28sample_-_can_be_changed_by_pacman-mirrors_api_commands.29)
        -   [[3.2.2] [File: /usr/share/pacman-mirrors/mirrors.json (sample - self updating)]](#File:_.2Fusr.2Fshare.2Fpacman-mirrors.2Fmirrors.json_.28sample_-_self_updating.29)
        -   [[3.2.3] [File: /var/lib/pacman-mirrors/status.json (sample - self updating)]](#File:_.2Fvar.2Flib.2Fpacman-mirrors.2Fstatus.json_.28sample_-_self_updating.29)
        -   [[3.2.4] [Sample command to customize mirror pool]](#Sample_command_to_customize_mirror_pool)
        -   [[3.2.5] [File: /etc/pacman.d/mirrorlist (sample)]](#File:_.2Fetc.2Fpacman.d.2Fmirrorlist_.28sample.29)
        -   [[3.2.6] [File: /var/lib/pacman-mirrors/custom-mirrors.json (sample)]](#File:_.2Fvar.2Flib.2Fpacman-mirrors.2Fcustom-mirrors.json_.28sample.29)
    -   [[3.3] [Defaults]](#Defaults)
    -   [[3.4] [Continent]](#Continent)
    -   [[3.5] [Country]](#Country)
    -   [[3.6] [Customizing the mirror pool]](#Customizing_the_mirror_pool)
        -   [[3.6.1] [A word of caution]](#A_word_of_caution)
    -   [[3.7] [Customizing pool]](#Customizing_pool)
        -   [[3.7.1] [Syncronization status]](#Syncronization_status)
    -   [[3.8] [Resetting and changing the custom mirror pool]](#Resetting_and_changing_the_custom_mirror_pool)
    -   [[3.9] [Apply pacman-mirrors defaults]](#Apply_pacman-mirrors_defaults)
-   [[4] [manpage]](#manpage)
-   [[5] [FAQ]](#FAQ)
    -   [[5.1] [pacman-mirrors.conf]](#pacman-mirrors.conf)
-   [[6] [Forum posts]](#Forum_posts)

## [Pacman-Mirrors]

Pacman-mirrors is a Manjaro specific utility for generating and maintaining the system mirrorlist. This article covers current version 4.x. Pacman-mirrors uses the information available on the [Mirrorservice](http://repo.manjaro.org)

### [Purpose]

Manjaro uses pacman for system maintenance, updates and new installs. For pacman to function, a list of servers, or more commonly known as mirrors, with Manjaro software packages is required. As Manjaro has many mirrors all over the world it is feasible to use the mirrors closest to your location and preferably also up-to-date.

### [Use]

For most functions, a working internet connection is required. From v4, Pacman-Mirrors will check if network is online. It is doing so by querying some generic websites. The sites are chosen due to their general availability. pacman-mirrors will selfupdate by downloading mirrors.json and status.json from repo.manjaro.org.

1.  repo.manjaro.org
2.  wikipedia.org
3.  bitbucket.org

Should you get certificates error and pacman-mirrors throws a message of missing internet connection - you must verify your computers firmware date and time as this is probably completely off either because of configuration or a malfunctioning CMOS battery.

The app is run by an ordinary user with superuser rights from the console and when no arguments are given it will display pacman-mirrors version followed by status of the mirrors currently listed in your mirrorlist.

[user \$ ][ sudo pacman-mirrors [COPY TO CLIPBOARD]]

\

Exactly how the app generates the mirrorlist is controlled by supplying arguments on the commandline.

### [**IMPORTANT**]

#### [When to use a forced metadata refresh]

When pacman requests the metadata from the mirror then - to avoid unnecessary download - pacman asks for **Last-Modified** header for the metadata on the server.

Only in the event that **Last-Modifed** on the mirror is newer - pacman requests the complete file.

This can present an awkward scenario where the local metadata is newer than the mirror but it contains older content.

This inconsistency may then generate **HTTP 404 Not Found** errors because the local metadata could contain references to package versions which no longer exist.

The doubled **yy** is to mitigate such possible issues - especially when you switch branch or mirror.

It is bad practise to indiscrimately use **-Syyu** for update scenarios, but - pamac mirrorlist timer rewrites the mirrorlist on a weekly or bi-weekly basis - thus increasing the possibility of having inconsistent metadata - in which case the doubled **yy** makes sense - which is also why it is used in the pacman-mirrors man page.

To further the inconsistency - pamac uses copies of the pacman database - which has caused confusion before - pamac and pacman being in disagreement over available updates.

The commands presented in this document uses the syntax **-Syu** thus leaving it to the user to add the extra **-Syyu** only in case where it is strictly necessary.

\

**Tip**

------------------------------------------------------------------------

Every run of pacman-mirrors requires you to syncronize your database and update your system.

[user \$ ][ sudo pacman -Syu [COPY TO CLIPBOARD]]

\

If you fail to do so, the issue/s which had you make change might not be solved. Furthermore you might run into [*partial-updated*](//wiki.manjaro.org/index.php?title=System_Maintenance "System Maintenance") scenario which can cause havoc in your system. For more detailed information on how pacman works you can read up on the [Archlinux Wiki](https://wiki.archlinux.org/index.php/System_maintenance)

## [TL:DR - Samples please]

All commands uses the available mirror pool.\
The mirror pool can be the default full mirror pool or a customized mirror pool.\
Commands for info do not require superuser - changing systemfiles do.\
All samples are using the long name version of the argument. For short versions have a look at the [man page](https://gitlab.manjaro.org/applications/pacman-mirrors/-/blob/master/data/docs/index.md%7C) or the usage command

### [Commands giving information]

#### [Man page]

[user \$ ][ man pacman-mirrors [COPY TO CLIPBOARD]]

\

#### [Help on usage]

[user \$ ][ pacman-mirrors \--help [COPY TO CLIPBOARD]]

\

#### [Version]

[user \$ ][ pacman-mirrors \--version [COPY TO CLIPBOARD]]

\

#### [Mirror status]

[user \$ ][ pacman-mirrors \--status [COPY TO CLIPBOARD]]

\

#### [List available countries]

In default mirror pool

[user \$ ][ pacman-mirrors \--country-list [COPY TO CLIPBOARD]]

\

In custom mirror pool

[user \$ ][ pacman-mirrors \--country-config [COPY TO CLIPBOARD]]

\

#### [What branch am I on]

[user \$ ][ pacman-mirrors \--get-branch [COPY TO CLIPBOARD]]

\

### [Commands using defaults]

#### [Update mirrorlist with the fastest mirrors]

[user \$ ][ sudo pacman-mirrors \--fasttrack && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

#### [Limit to 5 mirrors]

An optional number can be supplied to limit the number of mirrors in the mirrorlist

[user \$ ][ sudo pacman-mirrors \--fasttrack 5 && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

#### [Mirrors for your country only]

Not all countries have mirrors, if geoip returns a country not in the pool all mirrors will be used.

[user \$ ][ sudo pacman-mirrors \--geoip && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

### [Commands customizing the mirror pool]

You can customize the mirror pool to your preference. BUT Don\'t limit yourself too much as pacman-mirrors **only** writes up-to-date mirrors to your mirrorlist.

#### [Customize mirror pool by continent]

Create a custom mirror pool using mirrors from the continent determined by querying a geolocation service

[user \$ ][ sudo pacman-mirrors \--continent && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

#### [Customize mirror pool by countries]

Create a custom mirror pool using mirrors from Germany, France and Austria

[user \$ ][ sudo pacman-mirrors \--country Germany,France,Austria && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

#### [Customize mirror pool by interactive selection]

Create a custom mirror pool using the **\--default** mirror pool **\--interactive** will list all available mirrors and procotols in a gui windows allowing to sort the columns and interactively select according to your preferences.

[user \$ ][ sudo pacman-mirrors \--interactive \--default && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

#### [][Use specific protocols (prioritized)]

Rank the current mirror pool using only https and http protocol

[user \$ ][ sudo pacman-mirrors \--api \--protocol https,http && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

#### [Switch branch to unstable and use German mirrors]

Change the system branch to unstable and create a custom mirror pool using mirrors from Germany

[user \$ ][ sudo pacman-mirrors \--country Germany \--api \--set-branch unstable && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

#### [Switch branch and use German mirrors with https]

Change the system branch to unstable, set configuration to use https only and create a custom mirror pool using mirrors from Germany

[user \$ ][ sudo pacman-mirrors \--country Germany \--api \--set-branch unstable \--protocol https && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

### [Reset]

You will come to a point where you want to reset to defaults

[user \$ ][ sudo pacman-mirrors \--country all \--api \--protocols all \--set-branch stable && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

## [Overview]

### [Available arguments]

All available arguments can be viewed by unfolding this block

    ➜  ~ pacman-mirrors -h
    Version 4.16.4
    USAGE:
     pacman-mirrors [-h] [-f [NUMBER]] [-i [-d]] [-m METHOD] [--status]
            [-c COUNTRY [COUNTRY...] | [--geoip] | [--continent]]
            [-l] [-lc] [-q] [-t SECONDS] [-v] [-n]
            [--api] [-S/-B BRANCH] [-p PREFIX]
                [-P PROTO [PROTO...]] [-R] [-U URL]

    METHODS:
      -i, --interactive     Generate custom mirrorlist
      -f, --fasttrack [NUMBER]
                            Generate mirrorlist with a number of up-to-date
                            mirrors. Overrides : --geoip, --method
      -c, --country COUNTRY [COUNTRY ...]
                            Comma separated list of countries, from which mirrors
                            will be used
      --geoip               Get current country using geolocation
      --continent           Use continent from geolocation

    API:
      -a, --api             [-p PREFIX][-R][-S/-B|-G BRANCH][-P PROTO [PROTO ...]]
      -S, -B, --set-branch
                            API: Replace branch in configuration
      -p, --prefix PREFIX   API: Set prefix to : $mnt | /mnt/install
      -P, --proto, --protocols  [ ...]
                            API: Replace protocols in configuration
      -R, --re-branch       API: Replace branch in mirrorlist
      -U, --url URL         API: Replace mirror url in mirrorlist

    MISC:
      -G, --get-branch      Return branch from configuration
      -d, --default         INTERACTIVE: Load default mirror file
      -h, --help
      -l, --list, --country-list
                            List all available countries
      -lc, --country-config
                            lists configured mirror countries
      -m, --method
                            Generation method
      -n, --no-mirrorlist   Use to skip generation of mirrorlist
      -q, --quiet           Quiet mode - less verbose output
      -s, --no-status       Ignore mirror branch status
      -t, --timeout SECONDS
                            Maximum waiting time for server response
      -v, --version         Print the pacman-mirrors version
      --no-color
      --interval INTERVAL   Max. number of hours since last sync
      -g                    Create mirror list from active pool.
      --status              Status for the current mirror list.
      --use-async           Experimental async mirror test.

### [Files used by pacman-mirrors]

#### [][File: `/etc/pacman-mirrors.conf` [(sample - can be changed by pacman-mirrors api commands)]]

To view the content of a default configuration - click the link to the right \-\--\>

     $ cat /etc/pacman-mirrors.conf
    ##
    ## /etc/pacman-mirrors.conf
    ##

    ## Branch Pacman should use (stable, testing, unstable)
    Branch = unstable

    ## Generation method
    ## 1) rank   - rank mirrors depending on their access time
    ## 2) random - randomly generate the output mirrorlist
    # Method = rank

    ## Filename to use when ranking mirrors
    ## The file must be present in core repo
    # TestFile = core.db.tar.gz

    ## Define protocols and priority
    ##   separated by comma 'https,http' or 'http,https'
    ## ATM available protocols are: http, https, ftp
    ## Not specifying a protocol will ban the protocol from being used
    ## If a mirror has more than one protocol defined only the first is written to the mirrorlist
    ## Empty means all in reversed alphabetic order
    # Protocols =

    ## When set to False - all certificates are accepted.
    ## Use only if you fully trust all ssl-enabled mirrors.
    # SSLVerify = True

    ## Static configuration
    ## Add a comma separated list of urls to use
    ## e.g. Static = https://mirror1.tld/manjaro/,https://mirror2.tld/manjaro/
    # Static =

#### [][File: `/usr/share/pacman-mirrors/mirrors.json` [(sample - self updating)]]

To view the content of a default mirror pool - click the link to the right \-\--\>

    ~ >>> cat /usr/share/pacman-mirrors/mirrors.json
    [
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,

    ]

#### [][File: `/var/lib/pacman-mirrors/status.json` [(sample - self updating)]]

To view the content of a default mirror pool including mirror status - click the link to the right \-\--\>

    ~/Desktop >>> cat /var/lib/pacman-mirrors/status.json
    [
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,

    ]




    ====File: <code>/etc/pacman-mirrors.conf</code> <small>(sample of default config)</small>====


    To view the content of a default pacman-mirrors.conf - click the link to the right --->


    ~ >>> cat /etc/pacman-mirrors.conf
    ##
    ## /etc/pacman-mirrors.conf
    ##

    ## Branch Pacman should use (stable, testing, unstable)
    # Branch = stable

    ## Generation method
    ## 1) rank   - rank mirrors depending on their access time
    ## 2) random - randomly generate the output mirrorlist
    # Method = rank

    ## Define protocols and priority
    ##   separated by comma 'https,http' or 'http,https'
    ## ATM available protocols are: http, https, ftp
    ## Not specifying a protocol will ban the protocol from being used
    ## If a mirror has more than one protocol defined only the first is written to the mirrorlist
    ## Empty means all in reversed alphabetic order
    # Protocols =

    ## Get a list of all available counties with 'pacman-mirrors -l'
    ## Value can be 'Custom' or nothing which means all
    # OnlyCountry =

    ## When set to False - all certificates are accepted.
    ## Use only if you fully trust all ssl-enabled mirrors.
    # SSLVerify = True

#### [Sample command to customize mirror pool]

To view the content of the sample command - click the link to the right \-\--\>

    ~ >>> sudo pacman-mirrors --country Denmark && sudo pacman -Syyu
    .: INFO Downloading mirrors from repo.manjaro.org

    .: INFO User generated mirror list
    --------------------------
    .: INFO Custom mirror file saved: /var/lib/pacman-mirrors/custom-mirrors.json
    .: INFO Using custom mirror file
    .: INFO Querying mirrors - This may take some time
       0.091 Denmark        : https://mirrors.dotsrc.org/manjaro/
       0.075 Denmark        : https://www.uex.dk/public/manjaro/
    .: INFO Writing mirror list
       Denmark         : https://www.uex.dk/public/manjaro/unstable/$repo/$arch
       Denmark         : https://mirrors.dotsrc.org/manjaro/unstable/$repo/$arch
    .: INFO Mirror list generated and saved to: /etc/pacman.d/mirrorlist
    .: INFO To remove custom config run  'sudo pacman-mirrors -c all'
    :: Synkroniserer pakkedatabaser...
     core                          143,1 KiB  10,7M/s 00:00 [##############################] 100%
     extra                        1719,8 KiB  10,3M/s 00:00 [##############################] 100%
     community                       4,5 MiB  11,0M/s 00:00 [##############################] 100%
     multilib                      177,7 KiB  13,3M/s 00:00 [##############################] 100%
    :: Starter fuld systemopgradering...
     der er intet at udføre

#### [][File: `/etc/pacman.d/mirrorlist` [(sample)]]

To view the content of the sample mirrorlist - click the link to the right \-\--\>

    ~ >>> cat /etc/pacman.d/mirrorlist
    ##
    ## Manjaro Linux custom mirrorlist
    ## Generated on 2017-11-08 10:59
    ##
    ## Please use 'pacman-mirrors -id' to reset custom mirrorlist
    ## Please use 'pacman-mirrors -c all' to reset custom mirrorlist
    ## To remove custom config run  'pacman-mirrors -c all'
    ##

    ## Country : Denmark
    Server = https://www.uex.dk/public/manjaro/unstable/$repo/$arch

    ## Country : Denmark
    Server = https://mirrors.dotsrc.org/manjaro/unstable/$repo/$arch

#### [][File: `/var/lib/pacman-mirrors/custom-mirrors.json` [(sample)]]

To view the content of a custom mirror pool - click the link to the right \-\--\>

    ~ >>> cat /var/lib/pacman-mirrors/custom-mirrors.json
    [
      ,

    ]

### [Defaults]

PacmanMirrors has some reasonable defaults

    - Ranking mirrors with the fastest mirrors on top
    - Using stable branch
    - Using all mirrors

The **-f** or **\--fasttrack** argument uses mirrors which are up-to-date for your branch. Optionally you can supply a number e.g. 10

### [Continent]

The \--continent argument is using a geolocation function to create a custom mirror pool from countries within the geolocated continent.

### [Country]

Instead of pacman-mirrors probing all mirrors in all countries it is possible to supply a list of countries from which to use the mirrors. This creates a custom mirror pool. The countries is an example - check the country list if in doubt.

[user \$ ][ sudo pacman-mirrors \--country Germany,France,Austria && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

If a supplied country does not offer a mirrorserver the app quits with an error explaining why.

[user \$ ][ sudo pacman-mirrors \--country Antarctica && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

    .: Info Downloading mirrors from repo.manjaro.org
    .: Warning Option '-c/--country' : unknown country: 'Antarctica'
    .: Info Available countries are:
    Australia, Austria, Belarus, Belgium, Brasil, Bulgaria, Canada, Chile, China, Colombia,
    Costa_Rica, Czech, Denmark, Ecuador, France, Germany, Greece, Hungary, Indonesia,
    Ireland, Italy, Japan, Netherlands, Philippines, Poland, Portugal, Romania, Russia,
    Singapore, South_Africa, Sweden, Spain, Taiwan, Turkey, United_Kingdom, United_States,
    Vietnam

\
Another option for the mirrors closest to your location is **\--geoip**

    $ sudo pacman-mirrors --geoip --quiet && sudo pacman -Syu
    :: Querying servers, this may take some time
    => Testing mirrors in France
    :: Writing mirror list
    :: Mirrorlist generated and saved to: /etc/pacman.d/mirrorlist

### [Customizing the mirror pool]

If you, for various reasons, have a preference for specific mirrors, it is possible to create a personal mirror pool. This is done by supplying *\--interactive \[\--default\]*, *\--continent\-- or* \--country *argument.*

#### [A word of caution]

Don\'t limit yourself too much. Pacman-mirrors will only use up-to-date mirrors in the final mirrorlist. Also observe this: Your custom mirror pool will not be changed - even if a mirror leaves service or becomes unmaintained. It is your reponsibility to maintain your custom mirror pool in the event the official mirrorpool is changed.

### [Customizing pool]

The customized pool is saved as `/var/lib/pacman-mirrors/custom-mirrors.json`

**First option** is using *\--interactive*. It uses your current mirror pool(whether default or custom)

[user \$ ][ sudo pacman-mirrors \--interactive && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

**Second option** is using *\--interactive \--default*. This force the use of the official mirror pool

[user \$ ][ sudo pacman-mirrors \--interactive \--default && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

**Third option** is supplying a list of countries with *\--country*. The countries is an example - check the country list if in doubt.

[user \$ ][ sudo pacman-mirrors \--country Germany,France,Austria && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

**Fourth option** is *\--continent*. The countries used is determined by the continent they are assigned to and can optionally be combined with **\--interactive**.

[user \$ ][ sudo pacman-mirrors \--continent \[\--interactive\] [COPY TO CLIPBOARD]]

\

Using *\--interactive* option, pacman-mirrors will process the available mirrors and present you with a list in which you will select your desired mirrors. In any case the pool is saved and used to generate a mirrorlist.

#### [Syncronization status]

Pacman-mirrors downloads pool status for the default mirror pool. When you want to regenerate your mirrorlist, your custom pool is updated with the info from the downloaded pool status.

This ensures you will **always** use up-to-date mirrors.

### [Resetting and changing the custom mirror pool]

**First option** to reset is to default mirror pool

[user \$ ][ sudo pacman-mirrors \--country all && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

**Second option** to is to use *\--default* with *\--interactive* and creating a new custom mirror pool

[user \$ ][ sudo pacman-mirrors \--interactive \--default && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

-   You will be presented with a list with all and every mirror and you can pick your selection.

**Third option** is to supply a list of countries and use those for a custom mirror pool. The countries is an example - check the country list if in doubt.

[user \$ ][ sudo pacman-mirrors \--country Germany,France,Austria && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

-   If you supply the same preferred countries on every reset you will get your mirror pool updated with added or removed mirrors.

The **\--continent** option has a behavior similar to **\--country**

### [Apply pacman-mirrors defaults]

[user \$ ][ sudo pacman-mirrors \--country all \--api \--protocol all -set-branch stable && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

The system will throw messages about newer packages on the system. These messages can safely be ignored and they dissappear when the installed package(s) equals the system branch.

## [manpage]

-   The manpage is in section 8 (System administration commands)
-   [man page](https://gitlab.manjaro.org/applications/pacman-mirrors/tree/master/docs)

\

## [FAQ]

### [pacman-mirrors.conf]

If pacman-mirrors is updated and has a new **pacman-mirrors.conf**, it will inform you that a new conf is saved as **pacman-mirrors.conf.pacnew**.

*You must manually merge changes/additions into your pacman-mirrors.conf.*

## [Forum posts]

-   [Pacman-mirrors in the forum](https://forum.manjaro.org/search?q=pacman-mirrors%20order%3Alatest)