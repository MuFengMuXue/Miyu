[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Manjaro+Mirrors&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Manjaro_Mirrors "Manjaro Mirrors (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Manjaro_Mirrors/ru "Зеркала Manjaro (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Manjaro_Mirrors/zh-cn "Manjaro 镜像 (7% translated)")

## Contents

-   [[1] [What\'s a Mirror?]](#What.27s_a_Mirror.3F)
-   [[2] [Why do we need more mirrors?]](#Why_do_we_need_more_mirrors.3F)
-   [[3] [How does Manjaro know what mirror(s) to use?]](#How_does_Manjaro_know_what_mirror.28s.29_to_use.3F)
-   [[4] [How do we get more mirrors?]](#How_do_we_get_more_mirrors.3F)
-   [[5] [What is the size of the Manjaro database?]](#What_is_the_size_of_the_Manjaro_database.3F)
-   [[6] [How is the mirror synchronized?]](#How_is_the_mirror_synchronized.3F)
-   [[7] [How do you ask an organisation with servers to create a Manjaro mirror?]](#How_do_you_ask_an_organisation_with_servers_to_create_a_Manjaro_mirror.3F)
-   [[8] [Current Size Required for a Manjaro Mirror]](#Current_Size_Required_for_a_Manjaro_Mirror)
-   [[9] [Check here before you send a request for mirror hosting]](#Check_here_before_you_send_a_request_for_mirror_hosting)
-   [[10] [Do You Manage a Potential Manjaro Mirror Server?]](#Do_You_Manage_a_Potential_Manjaro_Mirror_Server.3F)
-   [[11] [See Also]](#See_Also)

# [][What\'s a Mirror?]

In the GNU/Linux distro world (& other systems too) a mirror is a server that hosts an up to date copy of a distro\'s software packages, stored in repositories (repos). There exist repos that are maintained by the distro administration - official - & other\'s. The Arch User Repository (AUR) being a good example of a non-official user maintained repo.

There are usually multiple repos in a mirror, holding software packages in categories, such as Manjaro\'s - core, extra, community & multilib repos. These repos will be duplicated with package content to suit both 32bit & 64bit installations, as well as for any & all the variety of releases that a distro may support. In Manjaro\'s case that is quite a number when all of the different Desktop & Window Manager titled front ends are considered.

The distro has package maintainers in its administration. They manage the contents of the repos, keeping it up to date, patching packages if required. Some distros, like Manjaro, have certain packages that are unique to it only - like mhwd for example.

\

# [][Why do we need more mirrors?]

The more mirrors we have the faster Manjaro\'s users can upgrade their systems. Some parts of the world have much faster internet speeds than others. In some circumstances, having a server in your country, or better yet, in your city, can make a world of difference to your download speeds.

\

# [][How does Manjaro know what mirror(s) to use?]

There is a file /etc/pacman.d/mirrorlist which lists all of the available mirrors.

There is another file called /etc/pacman-mirrors.conf that by default is configured to re-write your mirrorlist in a list with the fastest at the top, descending to the slowest, when the system is given the terminal command:

    sudo pacman-mirrors --fasttrack && sudo pacman -Syyu

This is a remarkably streamlined system compared to the ways that it has been in the past for the pacman rolling release system to manage its mirrors, let alone to rank their speed.

\

# [][How do we get more mirrors?]

I\'m glad you asked that question. This is the advice of **Philip Muller**, Lead developer of Manjaro Linux:

> \'Some people still ask me how I got 5 mirrors in one week before 0.8.0 came out. It is simple. Just write 100 mails to universities and companies supporting Linux. Go to Arch linux and grab their mirrorlist. Crawl through their servers and get their contact data. Write an email and see what response you get. Here is some more info about it.\'

\

# [][What is the size of the Manjaro database?]

We are at around 90 GB. Minimum of 120 GB is recommended, since we might have bigger rebuilds, which might double our space need temporally. 200 GB or higher would be better. As an example see also [this](https://lists.manjaro.org/pipermail/manjaro-mirrors/Week-of-Mon-20151207/000013.html).

\

# [][How is the mirror synchronized?]

**Via the following Rsync-Services:**

\

    Asia / Japan:
    rsync://ftp.tsukuba.wide.ad.jp/manjaro

    Europe / Germany:
    rsync://ftp.halifax.rwth-aachen.de/manjaro/

    Europe / Sweden:
    rsync://ftp.lysator.liu.se/pub/manjaro/

    Europe / Italy:
    rsync://manjaro.mirror.garr.it/manjaro/

    Europe / United Kingdom:
    rsync://mirrorservice.org/repo.manjaro.org/repos/

    RU / Russian Federation:
    rsync://mirror.yandex.ru/mirrors/manjaro/

*It is always recommend to sync from the nearest location. To sync from our own manjaro.org server we need the IP of your server so it can be white-listed at our end. Please mail [Philip Mueller directly](https://manjaro.org/terms-of-use/). There is a recommended script for use with our server, so please contact the Manjaro administration in this regard.*

# [][How do you ask an organisation with servers to create a Manjaro mirror?]

**Write them an email like this (in your native language):**

\
Dear Sir or Madam,

My name is \[Your Name\], I wish to ask you to please spare me a few minutes to read this letter & consider its contents.

I\'d like to introduce you to a relative new comer to the world of Linux distributions - Manjaro Linux. Manjaro is a new user-friendly Linux distribution based on the highly regarded Arch Linux. We are currently searching for mirrors to host our packages.

Although new, we are already one of the top 10 most popular Linux Distributions in the world, as listed in the DistroWatch.com top 100.

Manjaro Linux is based on well tested snapshots of the Arch Linux repositories, and is 100% compatible with Arch itself. We manage our repositories with our own in-house tool called BoxIt, which is designed like git.

Our aim is to create a light Linux distribution which is simple, up to date, fast, user friendly and which follows the K.I.S.S (Keep It Simple, Stupid) principle. As such, Manjaro Linux provides a more user friendly installation process, utilities for managing graphic drivers, and pre-configured desktop environments.

Our repository is at the size of around 40 GB. We have between 50 GB and 100 GB granted on other mirrors hosting our packages. Currently it is possible to sync from the following rsync services:

    Asia / Japan:
    rsync://ftp.tsukuba.wide.ad.jp/manjaro

    Europe / Germany:
    rsync://ftp.halifax.rwth-aachen.de/manjaro/

    Europe / Sweden:
    rsync://ftp.lysator.liu.se/pub/manjaro/

    Europe / Italy:
    rsync://manjaro.mirror.garr.it/manjaro/

    Europe / United Kingdom:
    rsync://mirrorservice.org/repo.manjaro.org/repos/

    RU / Russian Federation:
    rsync://mirror.yandex.ru/mirrors/manjaro/

If possible, please sync from the nearest rsync-service to your location. Also, it is recommended to use a similar script as that we provide for our Tier1-Servers, to sync from our server:

[https://gitlab.manjaro.org/tools/maintenance-tools/boxit/blob/master/manjaroreposync](https://gitlab.manjaro.org/tools/maintenance-tools/boxit/blob/master/manjaroreposync)

Thank you for your time and consideration,

\[Your Name\]

# [Current Size Required for a Manjaro Mirror]

*(last checked 2018-05-25 20:14 CEST)*\

    48K    ./tmp/core/i686
    52K ./tmp/core
    4.0K    ./tmp/extra/i686
    8.0K    ./tmp/extra
    4.0K    ./tmp/community/i686
    8.0K    ./tmp/community
    72K ./tmp
    2.0M    ./x32-stable/core/i686
    2.0M    ./x32-stable/core
    28M ./x32-stable/extra/i686
    28M ./x32-stable/extra
    65M ./x32-stable/community/i686
    65M ./x32-stable/community
    95M ./x32-stable
    2.0M    ./x32-testing/core/i686
    2.0M    ./x32-testing/core
    28M ./x32-testing/extra/i686
    28M ./x32-testing/extra
    64M ./x32-testing/community/i686
    64M ./x32-testing/community
    94M ./x32-testing
    2.1M    ./testing/multilib/x86_64
    2.1M    ./testing/multilib
    48K ./testing/core/i686
    2.3M    ./testing/core/x86_64
    2.3M    ./testing/core
    4.0K    ./testing/extra/i686
    23M ./testing/extra/x86_64
    23M ./testing/extra
    4.0K    ./testing/community/i686
    55M ./testing/community/x86_64
    55M ./testing/community
    82M ./testing
    2.1M    ./stable/multilib/x86_64
    2.1M    ./stable/multilib
    48K ./stable/core/i686
    2.3M    ./stable/core/x86_64
    2.3M    ./stable/core
    4.0K    ./stable/extra/i686
    23M ./stable/extra/x86_64
    23M ./stable/extra
    4.0K    ./stable/community/i686
    55M ./stable/community/x86_64
    55M ./stable/community
    82M ./stable
    2.0M    ./x32-unstable/core/i686
    2.0M    ./x32-unstable/core
    28M ./x32-unstable/extra/i686
    28M ./x32-unstable/extra
    65M ./x32-unstable/community/i686
    65M ./x32-unstable/community
    95M ./x32-unstable
    2.1M    ./unstable/multilib/x86_64
    2.1M    ./unstable/multilib
    48K ./unstable/core/i686
    2.3M    ./unstable/core/x86_64
    2.3M    ./unstable/core
    4.0K    ./unstable/extra/i686
    23M ./unstable/extra/x86_64
    23M ./unstable/extra
    4.0K    ./unstable/community/i686
    55M ./unstable/community/x86_64
    56M ./unstable/community
    82M ./unstable
    3.3G    ./pool/overlay-32
    37G ./pool/sync
    39G ./pool/sync-32
    4.6G    ./pool/overlay
    84G ./pool
    84G .

\

# [Check here before you send a request for mirror hosting]

Following is a list that will be updated when required.

It is very important that we don\'t send requests to anyone on this list, as they will consider it spam & could have Manjaro\'s IP addresses blocked by organisations who\'s business is to attempt to control spam.

So when you are trying to organise new mirrors DO NOT bother hosters who have already denied us support:

\

\
It is a good idea to check [repo.manjaro.org](http://repo.manjaro.org) to be sure that the wiki is up to date & also if you have been denied a request to post it in the same thread for obvious reasons.

# [][Do You Manage a Potential Manjaro Mirror Server?]

If so, here are some guidelines for you to think about, as putting up such a Mirror requires a certain commitment & perseverance.

The Manjaro community is better off not having a mirror, if it isn\'t kept functioning & up to date. So if you aren\'t in it for the long run, don\'t do it. You will only create disappointment.

Do you have enough bandwidth for the job? Do you pay for traffic? Your traffic may increase a lot. If you don\'t have enough bandwidth, you will end up offering at best a slow mirror, at worst an unreachable mirror.

Do you have enough disk space? You will need 100GB for the repos alone, though being able to offer 200GB would be great for the future. If your drive fills up you will not be able to rsync your mirror, it will become out of date & cause problems.

Sync every six hours. Being a rolling release system Manjaro\'s repos are very dynamic. So mirrors need to be updated multiple times per day.

Keep an eye on your sync scripts. Make sure that your mirror updates are functioning correctly. Users depend on your data to be all there & current.

Watch the Manjaro forum for announcements re. changes that may effect the mirror/repo system. The Manjaro administration will send you an email for any important changes. Though it often helps to be primed & ready for a change.

\

# [See Also]

-   [How to setup a Manjaro mirror server from scratch](https://forum.manjaro.org/t/root-tip-how-to-create-manjaro-mirror-server/21264)
-   [pacman-mirrors](//wiki.manjaro.org/index.php?title=Pacman-mirrors "Pacman-mirrors")
-   [Switching Mirrors](//wiki.manjaro.org/index.php?title=Change_to_a_Different_Download_Server "Change to a Different Download Server")