[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Alternative+way+to+install+ManjaroISO&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Alternative_way_to_install_ManjaroISO "Alternative way to install ManjaroISO (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Alternative_way_to_install_ManjaroISO/tr "ManjaroISO'yu kurmanın alternatif yolu (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Alternative_way_to_install_ManjaroISO/ru "Альтернативный способ установки ManjaroISO (100% translated)")

## Contents

-   [[1] [1. Create a work directory]](#1._Create_a_work_directory)
-   [[2] [2. Update your system]](#2._Update_your_system)
-   [[3] [3. Install ManjaroISO]](#3._Install_ManjaroISO)
-   [[4] [4. Clone from Github]](#4._Clone_from_Github)
-   [[5] [Updates]](#Updates)
-   [[6] [Differences]](#Differences)

\

**Warning**

------------------------------------------------------------------------

As of March 2015 manjaroiso is deprecated , [Manjaro-tools](//wiki.manjaro.org/index.php?title=Manjaro-tools "Manjaro-tools") is the way!

\
There is an alternative way to install and use [ManjaroISO](//wiki.manjaro.org/index.php?title=ManjaroISO "ManjaroISO").

This method is more flexible and is perfect for everybody, who wants to build a RC or pre release version of the next Manjaro version. It can also help with incompatibilities of ManjaroISO profiles.

This is the preferred method of all developers, who want to maintain their own spin of Manjaro and commit changes in their ManjaroISO profile folders to the ManjaroISO Github.

\

## [1. Create a work directory]

The first thing you should probably do is create a directory to work in, and cd to it. This\'ll help keep things organized.

[user \$ ][ mkdir -p \~/work/ [COPY TO CLIPBOARD]]

\

\

## [2. Update your system]

To update your system

[user \$ ][ sudo pacman -Syu [COPY TO CLIPBOARD]]

\

\

## [3. Install ManjaroISO]

Next, install manjaroiso without its profiles:

[user \$ ][ sudo pacman -S manjaroiso [COPY TO CLIPBOARD]]

\

\

## [4. Clone from Github]

The latest code for ManjaroISO is available on [Github](https://github.com/manjaro/manjaroiso/). There is the \"master\" branch and the \"development\" branch available.

The \"**master**\" branch is meant for creation of install-medias based on the latest **stable** Manjaro release. Clone ManjaroISO directly from Github to your work directory:

[user \$ ][ git clone [https://github.com/manjaro/manjaroiso.git](https://github.com/manjaro/manjaroiso.git) \~/work/manjaroiso [COPY TO CLIPBOARD]]

\

\
The \"**development**\" branch contains code for *buildiso* to build a **RC** or **pre** release install-media. Additionally, it contains more ManjaroISO profiles.

Attention: Not all ManjaroISO profiles in the \"development\" branch work and it can contain more bugs. Usually, it is updated more often, too.

Clone ManjaroISO from the \"development\" branch on Github:

[user \$ ][ git clone -b development [https://github.com/manjaro/manjaroiso.git](https://github.com/manjaro/manjaroiso.git) \~/work/manjaroiso [COPY TO CLIPBOARD]]

\

\

## [Updates]

Immediately after you have cloned the code from Github - as described in the last chapter - your ManjaroISO is up-to-date. When you wait a couple of days or longer, it is recommended to update.

An update pulls the latest changes from Github and puts them in your `~/work/manjaroiso` directory. Therefore, the following commands make sense.

First, you have to make sure you are in the directory you cloned the code from Github:

[user \$ ][ cd \~/work/manjaroiso [COPY TO CLIPBOARD]]

\

\
Use this \"update\" command, if you cloned from the master branch:

[user \$ ][ git pull origin master [COPY TO CLIPBOARD]]

\

Use this \"update\" command, if you cloned from the development branch:

[user \$ ][ git pull origin development [COPY TO CLIPBOARD]]

\

\
These \"update\" commands do **not** overwrite any changes you have made to files.

\

## [Differences]

In comparison to the other way to install [ManjaroISO](//wiki.manjaro.org/index.php?title=ManjaroISO "ManjaroISO"), there are a couple more files and directories in your `~/work/manjaroiso/` folder. But other than that, everything works the same.

Now, you can modify your ManjaroISO profile and use *buildiso* to build your own install-media as described [here](//wiki.manjaro.org/index.php?title=ManjaroISO#Modifying_a_ManjaroISO_Profile "ManjaroISO").