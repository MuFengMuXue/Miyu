[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Change+to+a+Different+Download+Server&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Change_to_a_Different_Download_Server "Change to a Different Download Server (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Change_to_a_Different_Download_Server/tr "Farklı Bir İndirme Sunucusuna Geçin (3% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Change_to_a_Different_Download_Server/ru "Переход на другой сервер загрузки (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Updating the mirrorlist the easy way]](#Updating_the_mirrorlist_the_easy_way)
-   [[3] [Updating the mirrorlist manually]](#Updating_the_mirrorlist_manually)
    -   [[3.1] [Edit the Mirrorlist]](#Edit_the_Mirrorlist)
        -   [[3.1.1] [Terminal]](#Terminal)
        -   [[3.1.2] [Editing the mirrorlist]](#Editing_the_mirrorlist)
-   [[4] [Step 2: Synchronising with the Newly Enabled Server(s)]](#Step_2:_Synchronising_with_the_Newly_Enabled_Server.28s.29)
-   [[5] [See Also]](#See_Also)

# [Overview]

The official Manjaro repositories are hosted on *Software Servers*(also known as *mirrors*) . Physically located throughout the world, these mirrors are responsible for receiving requests for software packages and delivering them to your system. There are therefore three primary factors that will determine how fast your downloads are:

-   Your internet connection
-   The speed of the mirror itself, and
-   The proximity of the mirror to you, that is, how close or how far away it is from a network perspective.

Other than upgrading your internet package or switching providers, it is therefore, potentially possible to improve the speed of downloads from the Manjaro repositories by selecting a different mirror to use.

To get a list of countries currently serving mirrors use the command

[user \$ ][ sudo pacman-mirrors \--country-list [COPY TO CLIPBOARD]]

\

\

**note**

------------------------------------------------------------------------

The geographically closest server may not always necessarily be the fastest!

\

# [Updating the mirrorlist the easy way]

The easiest method is to use **pacman-mirrors** which automates the process of determining the fastest mirrors and updating the mirrrorlist accordingly.\
A full description of how to use **pacman-mirrors** can be found one the [Pacman-mirrors](//wiki.manjaro.org/index.php?title=Pacman-mirrors "Pacman-mirrors") page.

# [Updating the mirrorlist manually]

This is undertaken by amending the **mirrorlist** file, which is read by Manjaro\'s package managers, for the internet addresses of the Manjaro servers to download updates and software applications from.

\

## [Edit the Mirrorlist]

**tip**

------------------------------------------------------------------------

More than one server can be enabled. However, they will be selected in the order they are listed, and the package manager will only select another server if there is a problem with the one before it.

You have a multitude of options for editing text file. Every system and every user has a preferred GUI text editor. However due to security concerns, it is difficult to launch a GUI editor to correctly edit a protected system configuration file.

Therefore you need to be familiar with basic terminal usage. **nano** is a terminal based text editor available with all Manjaro editions that we will use as an example.

\

### [Terminal]

You will need to first open your terminal in order to edit the mirrorlist file. The syntax of the command to edit the mirrorlist is:

[user \$ ][ sudo \[terminal text editor\] /etc/pacman.d/mirrorlist [COPY TO CLIPBOARD]]

\

For example, if you wish to edit the file within the terminal using *nano* (a standard terminal-based text editor) then enter:

[user \$ ][ sudo nano /etc/pacman.d/mirrorlist [COPY TO CLIPBOARD]]

\

\

### [Editing the mirrorlist]

**Lines beginning with a hash \'#\' will be ignored by pacman**. Hence to disable a mirror, a comment can be put in the beginning of a line starting with *Server*.

The mirrorlist can be long generally and only a part of it is displayed below:

    ~ >>> cat /etc/pacman.d/mirrorlist
    ##
    ## Manjaro Linux default mirrorlist
    ## Generated on 2018-02-17 13:32
    ##
    ## Please use 'pacman-mirrors -f [NUMBER]' to modify mirrorlist
    ##

    ## Country : Germany
    Server = https://mirror.philpot.de/manjaro/unstable/$repo/$arch

    ## Country : Denmark
    Server = https://www.uex.dk/public/manjaro/unstable/$repo/$arch

    ## Country : United_Kingdom
    Server = http://manjaro.mirrors.uk2.net/unstable/$repo/$arch

    ## Country : Poland
    Server = https://mirror.tuchola-dc.pl/manjaro/unstable/$repo/$arch

    ## Country : Germany
    Server = http://mirror.ragenetwork.de/manjaro/unstable/$repo/$arch

    ## Country : Netherlands
    Server = https://mirror.koddos.net/manjaro/unstable/$repo/$arch

    ## Country : Netherlands
    Server = https://manjaro.mirror.wearetriple.com/unstable/$repo/$arch

    ## Country : Germany
    Server = https://mirror.alpix.eu/manjaro/unstable/$repo/$arch

    ## Country : Netherlands
    Server = https://mirror.neostrada.nl/manjaro/unstable/$repo/$arch

    ## Country : United_Kingdom
    Server = https://www.mirrorservice.org/sites/repo.manjaro.org/repos/unstable/$repo/$arch

    #----->snipped

**note**

------------------------------------------------------------------------

Do not remove hashes from the lines that contain the names of the server countries.

\
Once you have disabled and/or enabled the desired server(s), save the changes and close the mirrorlist.

\

# [][Step 2: Synchronising with the Newly Enabled Server(s)]

**warning**

------------------------------------------------------------------------

Always synchronise with **-Syyu** after changing mirrors. Failure to do so may result in a broken system after updates

Your Manjaro system has a database of all the software packages that are available from the official repositories. These are used by pacman to locate and download them for installation. Synchronising your database after changing servers will therefore ensure that it is up to date, and avoid any potential problems when subsequently downloading software packages.

To synchronise your database with the Manjaro repositories, enter the following command in the terminal:

[user \$ ][ sudo pacman -Syyu [COPY TO CLIPBOARD]]

\

Once the Mirrorlist has been amended and the database synchronised, the change will be immediate. There will be no need to reboot your system for the change to take effect.

\

# [See Also]

-   [Reference Guide to pacman-mirrrors](//wiki.manjaro.org/index.php?title=Pacman-mirrors "Pacman-mirrors")