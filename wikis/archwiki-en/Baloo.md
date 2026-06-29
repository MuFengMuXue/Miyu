# Baloo

Baloo is a file indexing and searching framework for KDE Plasma.

## Installation
Install the  package.

## Usage and configuration
In order to search using Baloo on the Plasma desktop, start KRunner (default keyboard shortcut ) and type in your query. Within Dolphin press .

By default the Desktop Search KCM exposes only two options: A panel to blacklist folders and a way to disable it with one click. Alternatively you can edit your  file (info).

Additionally the  process can also be used to control Baloo, e.g. in order to stop/start Baloo use  or  to resume.

Once you added additional folders to the blacklist or disabled Baloo entirely, a process named  removes all unneeded index files automatically. These are stored under .

## Command-line usage
 $ baloosearch6 query

Support for range queries:

 $ baloosearch6 "width>=6000 width=6000 width File search''.

To permanently delete the index database, run:

 $ balooctl6 purge

This will also resolve the following error message in file dialogs and other applications (KDE bug 437176):

 kf.kio.core: "Could not enter folder tags:/."

## Troubleshooting
## Inotify folder watch limit error
If you get the following error:

 KDE Baloo Filewatch service reached the inotify folder watch limit. File changes may be ignored.

Then you will need to increase the inotify folder watch limit:

 # sysctl -w fs.inotify.max_user_watches=524288

To make changes permanent, create a sysctl configuration file:

## Plasma Vault Files are indexed and available even when vault is closed
This is a major security bug not yet fixed. Any file inside vault is by default indexed and available through file manager search, Krunner and Kickoff.

One workaround is to stop folder(s) from being indexed by Baloo. The relevant options are available in System Settings > Search > File Search > Folder specific configuration > Add folder configuration > Stop indexing a folder. After adding the desired folder, the existing Baloo data  needs to be removed and freshly indexed again:

 $ balooctl6 disable
 $ balooctl6 purge
 $ balooctl6 enable
 $ balooctl6 check

## Baloo keeps running and slowing down the system, even when given the command to stop
Sometimes the daemon might be indexing a large amount of files (e.g. when looking through all the dotfiles in your  directory), leading to a big consumption of the machine's resources and, potentially, to an unresponsive system.

If  does not work, you can kill the process directly with  $ pkill -9 baloo_process

Afterwards, you can disable the indexer.

Alternatively, since nowadays the daemon is run via systemd, if you wish to keep the indexer running but without saturating the I/O bandwidth, you can adjust the daemon's user unit to e.g. give it a higher memory limit, prevent it from using swap, etc. [https://bugs.kde.org/show_bug.cgi?id=487916#c10
