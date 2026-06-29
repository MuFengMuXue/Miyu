[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Viewing+and+editing+configuration+files&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files "Viewing and editing configuration files (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files/tr "Yapılandırma dosyalarını görüntüleme ve düzenleme (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files/fr "Affichage et modification des fichiers de configuration (77% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files/ru "Просмотр и редактирование файлов конфигурации (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Terminal]](#Terminal)
    -   [[2.1] [Viewing configuration files from the terminal/tty]](#Viewing_configuration_files_from_the_terminal.2Ftty)
    -   [[2.2] [Editing files from the terminal]](#Editing_files_from_the_terminal)
-   [[3] [Desktop Environment]](#Desktop_Environment)
    -   [[3.1] [List of graphical text editors for each edition]](#List_of_graphical_text_editors_for_each_edition)
    -   [[3.2] [Editing files requiring privilege escalation]](#Editing_files_requiring_privilege_escalation)

# [Overview]

In Manjaro, it is common for configuration for the system and applications to reside inside plain text configuration files. These files can be viewed and edited from both the terminal/tty and from a desktop environment.

# [Terminal]

## [][Viewing configuration files from the terminal/tty]

There are two primary ways to view files from the command line.

You can use the command cat to dump the contents of a file to the screen by typing cat \<filename\>. For example to view the contents of your fstab you could use:

[user \$ ][ cat /etc/fstab [COPY TO CLIPBOARD]]

\

For larger files where it would be better to navigate around you can use less. For example, to view the contents of your pacman.conf you could type:

[user \$ ][ less /etc/pacman.conf [COPY TO CLIPBOARD]]

\

## [Editing files from the terminal]

There are many editors available to edit files from the command line but the one that is included with every edition of Manjaro is nano.

To open a configuration file with nano simply type nano \<filename\>. For example, to edit your .profile file you could type:

[user \$ ][ nano \~/.profile [COPY TO CLIPBOARD]]

\

The keybindings for nano can be seen at the bottom of the screen. The \^ indicates the ctrl key. For example to exit nano you could hold ctrl and press \'x\'.

Sometimes, escalated privileges are required to edit a file such as most of the files in the /etc directory. In these cases there are two ways to acquire rights to edit these files.

The first is to use sudo to run the text editor. For example, to edit your fstab file you could type:

[user \$ ][ sudo nano /etc/fstab [COPY TO CLIPBOARD]]

\

An alternative, and arguably safer method, would be to save a copy of the file somewhere you can write and then use sudo to move it. For example, if you used nano to edit your fstab and then saved a copy to your home folder, you could then move it to the proper location with sudo:

[user \$ ][ sudo mv \~/fstab /etc/fstab [COPY TO CLIPBOARD]]

\

# [Desktop Environment]

Each Desktop Environment includes a different graphical text editor. These can be started from the menu/launcher or from the command line.

To edit or view a file you can open it directly from the command line. Reference the list below to find the appropriate editor installed with your edition. For example to open your pacman.conf from the XFCE edition you could type:

[user \$ ][ mousepad /etc/pacman.conf [COPY TO CLIPBOARD]]

\

Alternatively, you could launch mousepad from the whisker menu and open the file by browsing to it. Sometimes, the menu item will have the name as found below but it can also simply read \'Text Editor\'

## [List of graphical text editors for each edition]

-   XFCE: mousepad
-   Gnome: gedit
-   KDE/plasma: kate
-   Awesome: mousepad
-   bspwn: gedit
-   Budgie: gedit
-   Cinnamon: xed
-   Deepin: gedit
-   i3: mousepad
-   LXDE: leafpad
-   LXQT: juffed-qt5
-   MATE: pluma
-   Openbox: xed

## [Editing files requiring privilege escalation]

**Warning**

------------------------------------------------------------------------

Never use sudo to run a graphical text editor. This can have unintended consequences or break the permission to configuration files that should not be owned by root.

Many of the graphical text editors will automatically ask for privilege escalation when they detect that you cannot write to a file.

If they don\'t, you can save a copy of the file to your home folder and move it into place using sudo. For example, if you edit your fstab and then saved a copy to your home folder, you could then move it to the proper location with sudo:

[user \$ ][ sudo mv \~/fstab /etc/fstab [COPY TO CLIPBOARD]]

\