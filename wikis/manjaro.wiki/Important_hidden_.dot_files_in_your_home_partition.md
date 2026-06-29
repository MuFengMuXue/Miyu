Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Important_hidden_.dot_files_in_your_home_partition/tr "Ana bölümünüzdeki önemli gizli .dot dosyaları (24% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Important_hidden_.dot_files_in_your_home_partition/fr "Fichiers importants .dot cachés dans votre partition personnelle (78% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Important_hidden_.dot_files_in_your_home_partition/ru "Важные скрытые .dot-файлы в домашнем разделе (100% translated)")

## Contents

-   [[1] [What\'s a hidden \<.dot\> file?]](#What.27s_a_hidden_.3C.dot.3E_file.3F)
-   [[2] [Why is it worth knowing about these \<.dot\> files?]](#Why_is_it_worth_knowing_about_these_.3C.dot.3E_files.3F)
-   [[3] [So, what do these \<.dot\> files in my /home do?]](#So.2C_what_do_these_.3C.dot.3E_files_in_my_.2Fhome_do.3F)
-   [[4] [A reference to key \<.dot\> files]](#A_reference_to_key_.3C.dot.3E_files)
    -   [[4.1] [Directories]](#Directories)
    -   [[4.2] [Files]](#Files)
-   [[5] [Re-using /home]](#Re-using_.2Fhome)

# [][What\'s a hidden \<.dot\> file?]

They are files & directories with a \"**.**\" dot in front of them. Placing a \"**.**\" dot in front of a file or directory tells the operating system that such files & directories are to be hidden from view in file managers, file requesters & such. File managers & other applications can usually be set to view these normally hidden files. These hidden files & directories usually contain configuration files of some sort.

These hidden files will be referred to as *\<.dot\>* files in this article.

\

# [][Why is it worth knowing about these \<.dot\> files?]

-   These files contain settings/configuration information that will often need to be modified

<!-- -->

-   It is well worthwhile knowing which \<.dot\> directories & files in your \~/ directory are valuable in saving you time & effort if you have to reinstall Manjaro due to a hardware failure, corrupt data, user error\...

<!-- -->

-   If you are coming from, or going to another distro, this can be extremely valuable knowledge. As again, these \<.dot\> files can save you an enormous amount of time & effort in configuring your system to be just the way you like it. More on this to come.

<!-- -->

-   This knowledge can also be used to backup important config files, some of which can have had many, many hours of work in them.

\

# [][So, what do these \<.dot\> files in my /home do?]

**Note**

------------------------------------------------------------------------

\<.dot\> files are hidden by default. You usually need to enable them in your file manager or by using **ls -A**

Looking in your **\~** directory can identify any folders that have configuration or other customised data for our system, including the DE/WM and applications.

Some examples of these are; panels, trays, clocks, text editors, image viewers, pdf viewers & other applications. A quick look in your **\~/.config** directory will make this clear.

# [][A reference to key \<.dot\> files]

The following represent some of the most common types of \<.dot\> files that are found directly in your home folder. This is not an extensive list but represents some of the most common items.

Whether the files are important or not cannot be judged in this article - it depends on how much time you have spent on customizing your configuration files. Some window managers can only be configured using these files - in that case they become important. Or you have a collection of scripts in \~/.local/bin - they have become important as they - often - represent a great amount of work.

## [Directories]

**.cache** - Contains cached application files. Keep an eye on this folder as sometimes application caches can grow over time.

**.config** - This is where most modern applications keep user specific configuartion. This is the first place you should look for application related configuration files. Also, it is worth noting that any config files in this directory will have absolutely no effect if the program that they belong to is not installed on your machine. *So orphan config files pose absolutely no danger*.

**.local** - Holds a user specific version of **/usr/local**. Most notably application launchers can be found in **.local/share/applications**

**.local/bin** - Folder for your own scripts - included in your PATH

**.mozilla** - Configuration data for Firefox

**.thunderbird** - Configuration and mailboxes for Thunderbird

**.ssh** - ssh keys, known hosts and other per user ssh configuration

**.steam** - Data, config and game files for Valve\'s Steam platform

\
**.gnupg** - database for encrypting and signing using GnuPG - your private keys are here as well

## [Files]

**.bash_profile & .bashrc** - Per user configuration for **bash**

**.xinitrc** - If it is present in a user\'s home directory, startx and xinit execute it. Otherwise startx will run the default /etc/X11/xinit/xinitrc.

**.zshrc** - Per user configuration for **zsh**

\
**.netrc** - Configurations for accessing e.g. ftp servers

# [][Re-using /home]

People often get into trouble due to their keeping their old /home partition for a couple of prime reasons:

\

**1.** Permission problems (if they are using a different user name for example).

**2.** They have a mixture of hidden \<.dot\> files from multiple distros in **/home**

\
Before trying to re-use an existing **/home** be sure to review this section of the [Partioning Wiki Page](//wiki.manjaro.org/index.php?title=Partitioning_Overview_and_Existing_Partition_Tables#Where_Using_an_Existing_Linux_Partition_Table "Partitioning Overview and Existing Partition Tables")

\

**Note**

------------------------------------------------------------------------

If you happen to have any important hidden \<.dot\> files before you use the above linked to Manjaro method; know that they will be overwritten.

When coping \<.dot\> files from one **/home** to another, it is important to be selective, especially when doing so between different distros or different versions of the same distro. For example, it is unwise to copy an entire **\~/.config** over but perfectly safe to bring over many of the files within it on an application by application basis.