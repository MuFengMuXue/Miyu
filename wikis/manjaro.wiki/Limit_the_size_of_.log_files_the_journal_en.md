[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Limit+the+size+of+.log+files+%26+the+journal&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Limit_the_size_of_.log_files_%26_the_journal "Limit the size of .log files & the journal (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Limit_the_size_of_.log_files_%26_the_journal/tr ".log dosyalarının ve günlüğün boyutunu sınırlayın (1% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Limit_the_size_of_.log_files_%26_the_journal/ru "Ограничение размера файлов .log и журнала (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [The first topic on this page will briefly cover the **systemd journal**]](#The_first_topic_on_this_page_will_briefly_cover_the_systemd_journal)
    -   [[1.2] [The second topic will cover handling log files]](#The_second_topic_will_cover_handling_log_files)
-   [[2] [The journal & the logs duplicate the same information]](#The_journal_.26_the_logs_duplicate_the_same_information)
-   [[3] [Read this its important]](#Read_this_its_important)
    -   [[3.1] [How to set a maximum size limit for the journal]](#How_to_set_a_maximum_size_limit_for_the_journal)
-   [[4] [The Journalctl command - a quick reference \[1\]]](#The_Journalctl_command_-_a_quick_reference_.5B1.5D)
    -   [[4.1] [You don\'t have to use \"sudo\" with journalctl]](#You_don.27t_have_to_use_.22sudo.22_with_journalctl)
    -   [[4.2] [See the whole line of the journalctl output text]](#See_the_whole_line_of_the_journalctl_output_text)
        -   [[4.2.1] [Use a \~/.bashrc alias to make this easy]](#Use_a_.7E.2F.bashrc_alias_to_make_this_easy)
        -   [[4.2.2] [Access to full journal containing info from the system & users:]](#Access_to_full_journal_containing_info_from_the_system_.26_users:)
        -   [[4.2.3] [Live view, shows the last 10 lines of the journal & all content as it happens:]](#Live_view.2C_shows_the_last_10_lines_of_the_journal_.26_all_content_as_it_happens:)
    -   [[4.3] [Basic filtering:]](#Basic_filtering:)
        -   [[4.3.1] [Shows all output to the journal since the last boot:]](#Shows_all_output_to_the_journal_since_the_last_boot:)
        -   [[4.3.2] [Shows all output with priority level ERROR & worse, since last boot:]](#Shows_all_output_with_priority_level_ERROR_.26_worse.2C_since_last_boot:)
    -   [[4.4] [Filtering based on time:]](#Filtering_based_on_time:)
        -   [[4.4.1] [Since yesterday:]](#Since_yesterday:)
        -   [[4.4.2] [Give a specific time period:]](#Give_a_specific_time_period:)
        -   [[4.4.3] [Pick a specific service & time period:]](#Pick_a_specific_service_.26_time_period:)
    -   [[4.5] [Point journalctl at specific devices, services, binaries]](#Point_journalctl_at_specific_devices.2C_services.2C_binaries)
        -   [[4.5.1] [Look at a specific device:]](#Look_at_a_specific_device:)
        -   [[4.5.2] [Check on a binary:]](#Check_on_a_binary:)
        -   [[4.5.3] [Check on the interlieved output from two specifics:]](#Check_on_the_interlieved_output_from_two_specifics:)
        -   [[4.5.4] [Show all systemd units that have been started in your journal:]](#Show_all_systemd_units_that_have_been_started_in_your_journal:)
    -   [[4.6] [A summation]](#A_summation)
-   [[5] [Managing /var/log/\* files]](#Managing_.2Fvar.2Flog.2F.2A_files)
    -   [[5.1] [Introducing Logrotate & friends]](#Introducing_Logrotate_.26_friends)
        -   [[5.1.1] [The scope of this article]](#The_scope_of_this_article)
    -   [[5.2] [/etc/logrotate.conf & /etc/logrotate.d]](#.2Fetc.2Flogrotate.conf_.26_.2Fetc.2Flogrotate.d)
        -   [[5.2.1] [Can I store & run my script files elsewhere?]](#Can_I_store_.26_run_my_script_files_elsewhere.3F)
        -   [[5.2.2] [My settings in logrotate.conf don\'t effect all of the .log files?]](#My_settings_in_logrotate.conf_don.27t_effect_all_of_the_.log_files.3F)
        -   [[5.2.3] [Can I store my scripts where I want?]](#Can_I_store_my_scripts_where_I_want.3F)
    -   [[5.3] [Some uses for Logrotate]](#Some_uses_for_Logrotate)
    -   [[5.4] [An Example that you can modify to suit]](#An_Example_that_you_can_modify_to_suit)
        -   [[5.4.1] [Firstly - Be sure this file is here /etc/cron.daily/logrotate]](#Firstly_-_Be_sure_this_file_is_here_.2Fetc.2Fcron.daily.2Flogrotate)
        -   [[5.4.2] [Secondly - Create /etc/logrotate.d/rotate.logs using the following]](#Secondly_-_Create_.2Fetc.2Flogrotate.d.2Frotate.logs_using_the_following)
        -   [[5.4.3] [A Summary of the above example thus far]](#A_Summary_of_the_above_example_thus_far)
        -   [[5.4.4] [The effect of running /etc/logrotate.d/rotate.logs everyday]](#The_effect_of_running_.2Fetc.2Flogrotate.d.2Frotate.logs_everyday)

# [Introduction]

    Note: 18-Feb-17: Updated the Journal section
          & created a Support page in the forum.
          12-Feb-14: Improved Journal section.
          24-Mar-14: Tidied content of page &
          added content to the next section.

Log files & the systemd journal do the same thing in different ways. They keep a record of everything that happens on your computer system. This makes it possible to understand what is going right & what is going wrong. As an example, if your system had been infiltrated by an ssh attack, this could be verified in the log/journal. So these log files are good for more than tracking troublesome hardware, or driver problems, badly written network manager code or the plethora of other problems that the complex & dynamic GNU/Linux system has to deal with.

These logs are an absolute blessing, as not all systems have them, & those server administrators who do have them sould be very grateful, as they can be the bread & butter of what they do.

Generally, only server administrators have use for logs that go back any length of time. Few users who run distros on their desktop, notebook, netbook and such machines, have need to keep such huge log files or histories going back for many months or even years on their system. They are a waste of space & also makes viewing your log files more cumbersome.

\

#### [The first topic on this page will briefly cover the **systemd journal**]

The systemd journal has taken the place of log files though it will happily run in parallel with the standard type log files. These are still created & maintained by default in Arch & Manjaro. If you delete syslog-ng & all of the /var/log/\*log files on reboot you will find that some log files will be automatically created again. On my machine after having deleted syslog-ng & all of the /var/log/\*.log files (except for the Xorg.0.log files), my machine now has the following (wtmp & btmp are created on boot by the /etc/logrotate.conf file) contents in my /var/log/ :

    journal/
    squid/
    Xorg.0.log
    Xorg.0.log.old
    btmp
    faillog
    lastlog
    pacman.log
    wtmp

\

#### [The second topic will cover handling log files]

This topic will go into far more depth, covering the use of the **logrotate** command, **logrotate.conf**, the **/etc/cron.daily cron.weekly cron.monthly cron.yearly**, and some ways to run created scripts, plus a mention of the **crontab** method of running a script also. I\'ll try to make this section accessible to as many people as possible, which means this will be a long page.

\

# [][The journal & the logs duplicate the same information]

You can read the text of the log files in a text editor, or using the **cat**, **more**, **less** & such commands as you would on any other text file. The journal on the other hand requires the **journalctl** command to be able to access its contents. The following is a good way to read the journal:

    sudo journalctl

\

# [Read this its important]

    Note: etc/systemd/journald.conf.d/*.conf
    overrides the file journald.conf

**man journald.conf**

When packages need to customize the configuration, they can install configuration snippets in /usr/lib/systemd/\*.conf.d/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. The main configuration file is read before any of the configuration directories, and has the lowest precedence; entries in a file in any configuration directory override entries in the single configuration file. Files in the \*.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of which of the subdirectories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name takes precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering of the files.

What that means is that you can create configuration files **.conf** in the **/etc/systemd/journald.conf.d/** directory, with suitable names of your choice. The content of these files take precedence over any other settings or configurations in systemd. Please bear that in mind when you read the following? In my cumbersome way I\'ve tried to make it all too obvious\...

\

## [How to set a maximum size limit for the journal]

There is usually no need to interfere with the maximum size of the journal, as it has been built to monitor the amount of free space on the partition where it exists & will shrink itself by deleting the oldest entries when a shortage of space demands it.

Use your favorite text editor with root privileges, (starting it with **sudo** will do the job).

    Note: the name size.conf is user created.

With your text editor create a file called **size.conf** in the following location **/etc/systemd/journald.conf.d/size.conf** The following sets the maximum file size to a 50 MB limit for the **/var/log/journal** . *(The SystemMaxUse=250M is for use with logrotate, which is looked at in the 2nd section of this page. Talk to papajoke on the forum if you need help with logrotate & systemd.)*

    [Journal]
    SystemMaxUse=250M
    SystemMaxFileSize=50M

You can also limit the content of the journal by specifying the level of the data to be added to the journal. This is done by creating & editing the file **/etc/systemd/journald.conf.d/level.conf**

    Note: the name level.conf is user created.

    [Journal]
    # not save all levels but only 0 to 4
    MaxLevelStore=warning

\

# [][The Journalctl command - a quick reference [\[1\]](http://www.freedesktop.org/software/systemd/man/journalctl.html)]

    Note: Following are few pointers on things
    you can do to make using journalctl quicker,
    easier & more effective, on your system.

## [][You don\'t have to use \"sudo\" with journalctl]

Add your **user** to **adm** group. This gives your \<user\> full use of the **journalctl** command. No more need to use sudo. Swap \"handy\" for your username in the following:

    # usermod -a -G adm handy

## [See the whole line of the journalctl output text]

You can pipe the output of journalctl to a file or to a text display tool like \"More\" or \"Less\", as follows:

    $ journalctl -b -p err|less

Doing so, gives you a means of avoiding the truncation of output which some system displays configurations may experience.

### [][Use a \~/.bashrc alias to make this easy]

I use the following \~/.bashrc alias:

    alias errors="journalctl -b -p err|less"

On entering **errors** in the Terminal, all errors or worse since the last boot are sent to (piped) to the Terminal based text display tool called **Less** which wraps the text output of the journalctl command. Apart from anything else, it makes the errors more useful for anyone reading them in the forum!

Type **Q** (upper or lower case) to close \"Less\".

\

### [][Access to full journal containing info from the system & users:]

    $ journalctl

### [][Live view, shows the last 10 lines of the journal & all content as it happens:]

    $ journalctl -f

## [Basic filtering:]

### [Shows all output to the journal since the last boot:]

    $ journalctl -b

### [][Shows all output with priority level ERROR & worse, since last boot:]

    $ journalctl -b -p err

Following is the above command with its output sent to a file called **-ERRORS** in your */home/\<user\>* directory. Having the **-** at the beginning of the name should cause the file to be shown at the top of the list of files when viewing the contents of your **\~/** (*/home/\<user\>*) directory. This command makes it easy to copy the contents of the -ERRORS file, & then paste it to the forum. Doing so allows us to display ALL of the command\'s output instead of only being able to cut & paste the truncated lines from our terminal:

    $ Journalctl -b -p err > -ERRORS

## [Filtering based on time:]

### [Since yesterday:]

    $ journalctl --since=yesterday

### [Give a specific time period:]

    $ journalctl --since=2012-10-15 --until="2011-10-16 23:59:59"

### [][Pick a specific service & time period:]

    $ journalctl -u httpd --since=00:00 --until=9:30

## [][Point journalctl at specific devices, services, binaries]

### [Look at a specific device:]

    $ journalctl /dev/sdc

### [Check on a binary:]

    $ journalctl /usr/sbin/vpnc

### [Check on the interlieved output from two specifics:]

    $ journalctl /usr/sbin/vpnc /usr/sbin/dhclient

### [Show all systemd units that have been started in your journal:]

    $ journalctl -F _SYSTEMD_UNIT

You can then interrogate the journal specifying any of those units.

## [A summation]

The Systemd Journal is capable of advanced functions beyond what has been mentioned here. The above is very good food for thought for people that are wondering if they need to be running **syslog-ng** or the like that creates most of the **/var/log/\*log** files on their systems.

By experimenting with the above commands one can make an informed decision for themselves, though as mentioned at the beginning of the Journal section, Arch & therefore Manjaro still run both the new systemd journal & the old style log file system in parallel. So if you find the /var/log/\*log files to be redundant & you want to be rid of them, various methods would be effective.

As of this writing I\'m running my system with **syslog-ng** (& its dependency) deleted. I deleted all of the log files from the /var/log directory (leaving any that are in their own sub-directories), except for Xorg.0.log , Xorg.0.old , lastlog , btmp & wtmp, (pacman.log turned up when pacman was used, depending on what you have installed on your system, you may have applications that create their own logs - which can be turned off - too). (Note: These days I\'m systemd free as I\'ve been very happily using the OpenRC init system instead.)

\

# [][Managing /var/log/\* files]

## [][Introducing Logrotate & friends]

What is this Logrotate? [\[2\]](http://linux.die.net/man/8/logrotate) logrotate is a powerful tool used to manage the log files created by system processes. It can be instructed to automatically compress, rename in a variety of ways, remove logs, to do all of this & more in a way that maximizes the convenience of logs & conserves your system\'s resources. An enormous amount of control is available to users including running scripts on your rotated files.

A problem I face in trying to make this article about logrotate as simple as possible is that logrotate can be called in so many ways, & these ways are not mutually exclusive.

For example, logrotate can be called to run on a file, or multiple files in any combination or multiple of **hourly, daily, weekly, monthly & yearly**, via scripts placed in the /etc/ in the already existing directories **hourly daily weekly monthly** the **yearly** directory can be added if required. **crontab** [\[3\]](http://www.adminschoice.com/crontab-quick-reference/) can be used to run logrotate or scripts as complex as a person needs. logrotate can be combined with other tools in anyway that a user can come up with to process these rotated files at any time & frequency.

\

#### [The scope of this article]

That said, much of the power of logrotate is for the benefit of those administering servers & will not be dealt with in the following. Though what we will deal with can be used on more than just our log files. We can use logrotate to backup any other files that we choose. I will expand on this at a later date.

\

## [][/etc/logrotate.conf & /etc/logrotate.d]

The logrotate.conf configuration file largely dictates logrotate\'s behaviour, it holds global settings, but most of the work that logrotate does is via script files stored in the **/etc/logrotate.d** directory, which take precedence over the global settings held in logrotate.conf.

Applications such as Apache, MySQL, Cups & others, put scripts into the /etc/logrotate.d directory to manage their log files.

If you manually run the command **sudo logrotate**, you will be presented with its usage template. logrotate needs you to specify the path to the script that you want it to use, including the logrotate.conf file which one may think due to its name would be automatically read, it is not.

To run logrotate & the logrotate.conf file you use the following command line:

    logrotate /etc/logrotate.conf

\

### [][Can I store & run my script files elsewhere?]

A line exists in logrotate.conf that tells logrotate to run all of the scripts that exist in /etc/logrotate.d

    include /etc/logrotate.d

We can use the **include** command in logrotate.conf to add other directories or use another directory instead of logrotate.d if we have reason to. Be careful what you do as there are files placed into the logrotate.d directory by other programs.

\

### [][My settings in logrotate.conf don\'t effect all of the .log files?]

Script files that are called via the logrotate.conf file take precedence over the global settings in logrotate.conf . That means that if you call a script from logrotate.conf that is located in the /etc/logrotate.d directory, then that script is more powerful than any of the global setting in logrotate.conf .

I use a script **/etc/logrotate.d/rotate.logs** that is set to work on all \*.log files, & it does. The two that don\'t get rotated are called **faillog** & **lastlog** , apart from not having the **.log** file extension, these two files are not normal log files, they are accessed via terminal commands of the same name.

\

### [][Can I store my scripts where I want?]

Some applications such as Apache cups, drop scripts into /etc/logrotate.d to aid in their own self maintenance. We can use a location of our choosing for these or other scripts if we want. We just have to call its path in the /etc/logrotate.conf file, the same way, as shown in the following example:

    include /home/handy/.config/mylogrotate

Apart from adding our own scripts to /etc/logrotate.d (or any other path that we have chosen to include), we can also add scripts into any of the previously mentioned **/etc/ cron.hourly cron.daily cron.weekly cron.monthly** folders. OR we can add a script into any of these folders that suit our needs that runs the logrotate /etc/logrotate.conf command which will have the logrotate.conf file, direct logrotate to the default /etc/logrotate.d directory where we have our script(s). OR to another directory where we have our script & have included the path in logrotate.conf . whew!

So you can see there are a variety of ways to call logrotate (let alone use it).

\

## [Some uses for Logrotate]

For example, script block below does the following, listed line by line:

-   **/var/log/\*.log ** this curly bracket closes the block of commands.

<!-- -->

    /var/log/*.log

The above script can be used as is, it does not need to be made executable, it just needs to be put somewhere that logrotate will see (in this example) every day.

We can use the above script block as a template, easily removing parts & modifying its relatively simple settings. It can be duplicated in a script with each script block specifying custom settings tailored for individual files.

\

## [An Example that you can modify to suit]

I\'ll show how I have my system set (at the time of this writing), you can use the information already given on this page & other available on the web to fine tune your set up to suit your needs (if you have the need anyway).

### [][Firstly - Be sure this file is here /etc/cron.daily/logrotate]

    #!/bin/sh

    # nicenesses range from -20 (most favorable scheduling) to 19 (least favorable)
    NICE=19

    # 0 for none, 1 for real time, 2 for best-effort, 3 for idle
    IONICE_CLASS=2

    # 0-7 (for IONICE_CLASS 1 and 2 only), 0=highest, 7=lowest
    IONICE_PRIORITY=7

    CMD_LOGROTATE="/usr/bin/logrotate /etc/logrotate.conf"

    if [ -x /usr/bin/nice ]; then
      CMD_LOGROTATE="/usr/bin/nice -n $ $"
    fi

    if [ -x /usr/bin/ionice ]; then
      CMD_LOGROTATE="/usr/bin/ionice -c $ -n $ $"
    fi

    $

    exit 0

\

### [][Secondly - Create /etc/logrotate.d/rotate.logs using the following]

    ## rotate all /var/log files with names ending in log
    /var/log/*log

\

### [A Summary of the above example thus far]

The First step puts a file into **/etc/cron.daily** which is an easy way to add the script to a daily cron job. Which means that script will be run everyday.

It basically runs this command:

    logrotate /etc/logrotate.conf

As logrotate.conf goes through its list of commands it calls this one:

    include /etc/logrotate.d

Which means that any scripts that are inside of **/etc/logrotate.d** are also run.

This brings us to the second step (above), where we created **/etc/logrotate.d/rotate.logs** . This script will be run everyday. The comments I added to the rotate.logs file above give a general idea of what it does. You can delete, modify & add to that script, but do it carefully.

### [][The effect of running /etc/logrotate.d/rotate.logs everyday]

Is that any file in /var/log that had **log** at the end of its name will be processed by the commands in the **rotate.logs** script. This will back up these files to a new file **\<name\>.log.1** & empty the original file to size 0. Any previous copies with **\<name\>.log.\<number\>** will have their numbers bumped up one, until the day when they would have been given an 8, that is the day that they are deleted.

As well as this rotating (copying) & renaming of files, all files will be compressed in gzip format on the next rotation. Which means that you always have the current file & yesterdays file in /var/log in uncompressed format.

No files that are empty will be processed, & a file being missing will throw no errors.

\