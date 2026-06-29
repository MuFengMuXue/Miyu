[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Basic+Tips+for+conky&language=en&action=page&filter= "Special:Translate")

Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky/de "Grundlegende Tipps für conky (9% translated)") • ‎[English](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky "Basic Tips for conky (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky/tr "Conky için Temel İpuçları (9% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky/es "Consejos básicos para Conky (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky/fr "Conseils pratiques pour Conky (83% translated)") • ‎[português do Brasil](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky/pt-br "Dicas Básicas para o Conky (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky/ru "Основные советы для conky (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky/fa "نکات اساسی برای کانکی (22% translated)")

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Configuration]](#Configuration)
        -   [[1.1.1] [Configuration file]](#Configuration_file)
    -   [[1.2] [Conky configuration]](#Conky_configuration)
    -   [[1.3] [Examples]](#Examples)
    -   [[1.4] [Conky text]](#Conky_text)
    -   [[1.5] [Examples]](#Examples_2)
    -   [[1.6] [execi]](#execi)
    -   [[1.7] [Running conky]](#Running_conky)
    -   [[1.8] [Troubleshooting & Tips]](#Troubleshooting_.26_Tips)
        -   [[1.8.1] [Missing rings]](#Missing_rings)
        -   [[1.8.2] [Missing network information]](#Missing_network_information)
    -   [[1.9] [Conky Manager]](#Conky_Manager)
-   [[2] [See Also]](#See_Also)

## [Installation]

Conky can be installed using the package manager

[user \$ ][ pamac install conky [COPY TO CLIPBOARD]]

\

### [Configuration]

All file names starting with a dot `.` are hidden files. If you want to see hidden files in your file manager, you need to make them visible. In most file managers this will be available in the options.

#### [Configuration file]

The default configuration file is located in `/usr/share/doc/conky-1.11.5_pre/conky.conf` where version are subject to change. Conky do not create a local conky folder so you will have to create beforehand

[user \$ ][ mkdir -p \~/.config/conky [COPY TO CLIPBOARD]]

\

Then copy the default to home

[user \$ ][ cp /usr/share/doc/conky-1.11.5_pre/conky.conf \~/.config/conky/conky.conf [COPY TO CLIPBOARD]]

\

The configuration file is a simple text file and the content written using \[[\|LUA syntax](https://www.lua.org/)\] and is split into two parts

-   Configuration
-   Text

### [Conky configuration]

The first/upper part contains all the configuration settings for the entire conky. Things like the position of the conky on your screen, transparency settings, border settings, the default font and it\'s size, and how often your conky gets updated. The whole configuration belong between brackets like this

\~/.config/conky/conky.conf

    conky.config = ;

Some rules apply

-   Every line end with `,`
-   Non-boolean/numerical value should be placed between `'`
-   Comment start with `--`

### [Examples]

**1.** This will set the default font color of your conky to white. Additionally, a `color1` gets set using a [Html Color Code](http://html-color-codes.info/)to a light blue:

\~/.config/conky/conky.conf

    conky.config = ;

**2.** This enables Xft, set the default font (LiberationMono), make it bold and set it\'s size (8):

\~/.config/conky/conky.conf

    conky.config = ;

**3.** In order to position your conky on your screen, modify these settings:

\~/.config/conky/conky.conf

    conky.config = ;

**4.** In some case you can have multiple values for one setting, they will be separated by a coma:

\~/.config/conky/conky.conf

    conky.config = ;

Use the command: `man conky`, and look into the **CONFIGURATION SETTINGS** section to see every settings available.

### [Conky text]

The second part contains the displayed conky code. Every code line corresponds to one displayed line on your desktop. There are a lot of available for displaying and modifying all kinds of information. Use the command: `man conky`, and look into the **OBJECTS/VARIABLES** section to see every objects/variables available.

**Info**

------------------------------------------------------------------------

The lines in the **conky.text** section is printed exactly as is. E.g. if you create an empty line between sections - conky will display an empty line.

The whole code belong between these two double bracket:

\~/.config/conky/conky.conf

    conky.text = [[
    ]];

### [Examples]

**1.** You can choose the color of your font using one of the following variables:

\~/.config/conky/conky.conf

    conky.text = [[
    ...
    $
    $
    ...
    ]];

Every variable is marked with a `$` sign and by `` brackets (only needed, if the variable contains more than one word).

**2.** You can call the default font (and it\'s size) with this command:

\~/.config/conky/conky.conf

    conky.text = [[
    ...
    $font
    ...
    ]];

If you want a different font (DejaVuSerif) and font size (9) in your conky, use this command in your `.conf` code:

\~/.config/conky/conky.conf

    conky.text = [[
    ...
    $
    ...
    ]];

**3.** This code line displays the text \"Kernel: \" and the kernel you are using (using `$alignr` just yields a nicer formatting, it is not necessary: `$alignr` aligns all following text on the right of your conky):

\~/.config/conky/conky.conf

    conky.text = [[
    Kernel: $$
    ]];

**4.** This variable gives you the latest 3 manjaro blog entry titles (using rss). It checks for updates every 60 minutes.

\~/.config/conky/conky.conf

    conky.text = [[
    $
    ]];

**5.** Information about the root partition `/` of your manjaro installation is displayed using

\~/.config/conky/conky.conf

    conky.text = [[
    Root: $$ of $
    ]];

**6.** Instead of example 3, you can use the following code to display the exact same information:

\~/.config/conky/conky.conf

    conky.text = [[
    Kernel: $$
    ]];

### [execi]

The variable `$` runs the `XXXX` bash code in your terminal every 3600 seconds and displays the result in your conky. The result of the `uname -r` bash command is your currently used kernel name.

Use any bash command instead of `XXXX` you can think of. The bash commands can be as long and complicated as you want.

\

**Warning**

------------------------------------------------------------------------

Using complicated bash commands (e.g. which call other programs or use large files) with low intervals (e.g. `$` runs the `XXXX` code once every 2 seconds and displays it\'s result in your conky) can use a lot of hardware resources and/or make your computer unresponsive.

### [Running conky]

If you want to display a conky on your desktop a `~/.config/conky/conky.conf` file with code in it is required. Next, open a terminal and run conky pointing to the file

[user \$ ][ conky -c \~/.config/conky/conky.conf [COPY TO CLIPBOARD]]

\

or to run as background daemon

[user \$ ][ conky -d -c \~/.config/conky/conky.conf [COPY TO CLIPBOARD]]

\

If you want to run conky automatically after each boot of your computer, you need to find out how to autostart a program. This depends on the Desktop Manager you are using. The next is examples of how to run conky from your system autostart folder/file/script/command. `sleep 20` and `-p 20` delay the start of conky by 20 seconds after your Desktop Environment has started. Adjust this value to your liking.

[user \$ ][ conky -c \~/.config/conky/conky.conf & [COPY TO CLIPBOARD]]

\

[user \$ ][ sleep 20 && conky -c \~/.config/conky/conky.conf & [COPY TO CLIPBOARD]]

\

When you change the running conky configuration file - conky will reload. But if you changed one of your dependency scripts (e.g. because you changed a variable and want to see the consequences) you will have to reload conky

[user \$ ][ killall conky && conky -c \~/.config/config/conky.conf [COPY TO CLIPBOARD]]

\

### [][Troubleshooting & Tips]

#### [Missing rings]

To be able to use LUA scripts to execute drawing functions like clock rings - you will a conky package compiled with LUA support. Either build the package the package `conky-lua` from [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") or install the `conky-lua-nv` from the official repo.

#### [Missing network information]

If network information is missing like download speed or network name (SSID), you need to replace the network interfaces in the configuration file with your network interface name. To get the names of your interfaces - open a terminal and execute

[user \$ ][ ip a [COPY TO CLIPBOARD]]

\

Use the output from the command. Interface names starting with `en` is ethernet interface and names starting with `wl` is wireless interfaces. Replace all network interfaces names with (e.g. `wlan0`, `eth0`) in your `.conf` text section with the interface name(s) you retrieved from the above command.

### [Conky Manager]

An application named Conky manager exist but has not been updated for years and the configurations found in the package may work or they may not. You may install it - it can be a used as an inspiration but you should not rely on it. If you still think you it is a must have - you can build the package `conky-manager` using [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository")

[user \$ ][ pamac build conky-manager [COPY TO CLIPBOARD]]

\

## [See Also]

-   The [Conky website](https://github.com/brndnmtthws/conky/wiki)
-   The [Arch Wiki](https://wiki.archlinux.org/index.php/conky) page for Conky