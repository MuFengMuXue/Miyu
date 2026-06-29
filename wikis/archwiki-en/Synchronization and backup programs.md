# Synchronization and backup programs

This page lists and compares applications that synchronize data between two or more locations, and those that build on top of such functionality to make incremental copies of important data for backup purposes. Because of their relationship, the two groups share several traits that justify describing them in the same article.

## Important considerations
In order to choose the best program for one's own needs, the following aspects should be considered:

* The type of backup medium that is going to store the data, e.g. CD, DVD, remote server, external hard drive, etc.
* The planned frequency of backups, e.g. daily, weekly, monthly, etc.
* The features expected from the backup solution, e.g. compression, encryption, handles renames, etc.
* The planned method to restore backups if needed.

## Data synchronization
These applications simply keep directories synchronized between multiple locations/machines, in a "mirror" fashion. Nonetheless, most of them still allow storing and reverting to old revisions of modified or deleted files.

See also:

* List of applications/Utilities#File synchronization and backup
* List of applications/Internet#Cloud synchronization clients
* Wikipedia:Comparison of file synchronization software

## Legend
;Name: The application name, linking to the ArchWiki article or the official website.
;Package: A link to the package.
;Implementation: The programming language, library, or utility that the application is based on.
;Delta transfer: Only the modified parts of files are transferred.
;Encrypted transfer: Data is encrypted by default when transferred over the network.
;FS metadata: File system permissions and attributes are synchronized.
;Resumable: The synchronization can be resumed if interrupted.
;Handles renames: Moved/renamed files are detected and not stored or transferred twice. It typically means that a checksum of files or its chunks is computed. Applications missing this functionality can be supplemented by combining with , which only synchronizes renames.
;Version control: The old version of files are backed up (reverse incremental backup).
;Change propagation: Specifies in how many directions changes can be propagated.
:* unidirectional means one-way synchronization of two locations,
:* bidirectional means two-way synchronization of two locations and
:* multidirectional means full synchronization of more than two locations.
;Conflict resolution: The application handles file conflicts, either automatically or interactively, i.e. it does not silently discard conflicting files. This attribute does not apply to applications that only propagate changes in one direction.
;FS monitoring: The application listens to file system events to trigger the synchronization.
;CLI: The application provides a command-line interface.
;Other interfaces: The application has the specified user interfaces, e.g. GUI, TUI, or web-based.
;License: The license of the server and client applications.
;Other platforms: Supported operating systems other than Linux.
;Maintained: The project is maintained.
;Specificity: Brief notes about special features that notably set the application apart from the others.

## Table
{| class="wikitable sortable" style="text-align: center"
! Name
! Package
! Implementation
! Delta transfer
! Encrypted transfer
! FS metadata
! Resumable
! Handles renames
! Version control
! Change propagation
! Conflict resolution
! FS monitoring
! CLI
! Other interfaces
! License
! Other platforms
! Maintained
! Specificity
|-
! FreeFileSync
|
| C++
|
|
|
| ?
|
|
|unidirectional / multidirectional
|
|
|
|
|
| Windows, macOS
|
|
|-
! git-annex
|
| Haskell, git
|
|
|
|
|
|
| multidirectional; with git remotes |
|
|
|
|
| FreeBSD, macOS, Android (via Termux), Windows (beta)
|
|
|-
! [https://github.com/deajan/osync osync.sh
|
| Bash, based on rsync
|
|
|
|
|
|
| bidirectional
|
|
|
|
|
| FreeBSD, Windows (via WSL, MSYS, Cygwin), macOS, Android (via Termux), QTS, pfSense
|
|
|-
! rclone
|
| Go
|  |
|
|
|
|
| unidirectional / bidirectional [https://rclone.org/faq/#can-rclone-do-bi-directional-sync
|  |  [https://github.com/rclone/rclone/issues/249
|
|
|
| FreeBSD, Windows, macOS, Plan9, Solaris
|
|
|-
! rdiff-backup
|
| Python, librsync
|
|
|
|
|
|
|colspan="2"| unidirectional
|
|
|
|
| FreeBSD, Windows, macOS
|
|
|-
! Resilio Sync
|
| C++
|
|
|  |
|  [https://help.resilio.com/hc/en-us/articles/209606526-What-happens-when-file-is-renamed
|
| multidirectional
|  |  [https://platform.resilio.com/hc/en-us/articles/360015609859-How-agents-detect-file-changes
|
|
|
| As for v3: Windows, macOS, Android, iOS
|
|
|-
! rsync
|
| C
|
|
|
|
|
|
|colspan="2"| unidirectional
|
|
|
|
| FreeBSD, Windows (via WSL, MSYS, Cygwin), macOS, Android (via Termux)
|
|
|-
! SparkleShare
|
| C#, git
|
|  | ?
| ?
|
|
| ?
| ?
| ?
|
|
|
| Windows, macOS
|  [https://github.com/hbons/SparkleShare/issues/2006
| It can sync with any Git server over SSH.
|-
! Syncany
|
| Java
| ?
| ?
| ?
| ?
| ?
| ?
| ?
| ?
| ?
|
|
|
| Windows, macOS, Docker
|  |
|-
! Syncthing
|
| Go
|
|
|
|
|
| , previous versions moved to archive folder
| multidirectional
|
|
|
|
|
| BSD, Windows, macOS, Android (fork), Dragonfly, Illumos, Solaris
|
|
|-
! [https://synkron.sourceforge.net/ Synkron
|
| C++
| ?
| ?
| ?
| ?
| ?
| ?
| multidirectional
| ?
| ?
|
|
|
| BSD, Windows, macOS, ChromeOS
|  |
|-
! taskd
|
| C++, Python
|
|
| ?
|
| ?
| ?
| multidirectional
| ?
|
|
|
|
| Android
|
|
|-
! Unison
|
| OCaml
|
|
|
|
|
|
| bidirectional
|
|
|
|
|
| FreeBSD, Windows, macOS
|
|
|-
! [https://github.com/ynikitenko/yarsync yarsync
|
| Python, based on rsync
|
|
|
|
|
|
| unidirectional / multidirectional
|
|
|
|
|
| Windows (via WSL, MSYS, Cygwin), macOS, Android (via Termux)
|
| UNIX-like systems or backup drives, CLI like git.
|-
! Zaloha2.sh
|
| bash
|
|
|
|
|
|
| bidirectional
|
|
|
|
|
| BSD, Windows (via WSL, MSYS, Cygwin), macOS, Android (via Termux)
|
| Small and simple
|}

## Incremental backups
Applications that can do incremental backups remember and take into account what data has been backed up during the last run (so-called "diffs") and eliminate the need to have duplicates of unchanged data. Restoring the data to a certain point in time would require locating the last full backup and all the incremental backups from then to the moment when it is supposed to be restored. This sort of backup is useful for those who do it very often.

See also:
* Wikipedia:List of backup software
* Wikipedia:Comparison of backup software
* Wikipedia:Comparison of online backup services

Legend:

* Name: the application name, linking to the ArchWiki article or the official website.
* Package: a link to the package.
* Implementation: the programming language, library, or utility that the application is based on.
* Compressed storage: compression is used for storage.
* Encrypted storage: encryption is used for storage.
* Delta transfer: only the modified parts of files are transferred.
* Encrypted transfer: data is encrypted by default when transferred over a network.
* FS metadata: file system permissions and attributes are backed up.
* Easy access: the backup is stored plainly in the file system, or is mountable as such.
* Resumable: the backup can be resumed without restarting it if interrupted.
* Multithreading: the backup can be done in multiple threads of execution concurrently.
* Handles renames: moved/renamed files are detected and not stored or transferred twice; it typically means that a checksum is computed for files or chunks thereof.
* CLI: the application is command-line driven, i.e. it is scriptable.
* Other interfaces: the application has the specified user interfaces, e.g. GUI, TUI, or web-based.
* Licence: the licence of the server and client applications.
* Other platforms: supported operating systems other than Linux.
* Maintained: whether the project is maintained.
* Deduplication: whether the program supports deduplicating saved files
* Specificity: brief notes about special features that notably set the application apart from the others.

## Single machine
These applications are aimed at backing up data from the machine they are installed on, although the backup destination can be located on an external machine or storage media.

## Chunk-based increments
If a file is modified, these applications store only its changed parts at the next snapshot. Compared to #File-based increments applications, these are more space-efficient, especially when large files receive small modifications; on the other hand, the archived snapshots have to be opened with the backup application that created them, since the files have to be reconstructed from the stored binary diffs.

{| class="wikitable sortable" style="text-align:center"
! Name
! Package
! Implementation
! Compressed storage
! Encrypted storage
! Delta transfer
! Encrypted transfer
! FS metadata
! Easy access
! Resumable
! Multithreading
! Handles renames
! CLI
! Other interfaces
! Licence
! Other platforms
! Maintained
! Deduplication
! Specificity
|-
! Areca Backup
|
| Java
|
|
|
|
|
|
|
|  |
|
|
| GPLv2
| Windows
|
|
|
|-
! Borg backup
|
| Python, C (Cython)
|
|
|
|
|  [https://borgbackup.readthedocs.org/en/stable/faq.html#which-file-types-attributes-etc-are-preserved
|  |  [https://borgbackup.readthedocs.org/en/stable/faq.html#if-a-backup-stops-mid-way-does-the-already-backed-up-data-stay-there
|  |
|
|
| BSD
| *BSD, macOS, Windows (Cygwin / WSL)[https://borgbackup.readthedocs.io/en/stable/#main-features
|
|
|
|-
! bup
|
| C, Python, git
|
|
|
|
|
|  |
|
|
|
|
| GPLv2
| NetBSD, Windows, macOS
|
|
|
|-
! [https://duplicacy.com/ Duplicacy
|
| Go
|
|
|
|
|
|  |  [https://forum.duplicacy.com/t/is-backup-pause-resume-supported/351/3
|  |  [https://github.com/gilbertchen/duplicacy/wiki/Lock-Free-Deduplication#two-step-fossil-collection
|
|
| Custom (non-free)
| FreeBSD, macOS, Windows
|
|
|-
! Duplicati
|
| C#
|
|
|
|
|
|
|
|  |
|
|
| MIT
| Windows, macOS
|
|
|
|-
! Duplicity
|
| librsync
|
|
|
|
| ?
|
|
|
|
|
|
| GPLv2
|
|
|
|
|-
! [https://kopia.io Kopia
|
| Go, Javascript front-end
|
|
|
|
|
|
|
|
|
|
|
| Apache 2.0
| Windows, macOS, OpenBSD
|
|
|
|-
! Kup Backup System
|
| rsync, bup front-end
|
|
|
|
|
|
|
| ?
|
|
|
| GPLv2
|
|
|
|
|-
! Restic
|
| Go
|
|
|
|
|  |  [https://restic.readthedocs.io/en/stable/050_restore.html#restore-using-mount
|  |  [https://forum.restic.net/t/multithreaded-backup/3062/3
|
|
|  | BSD
| OpenBSD, Windows, macOS
|
|  [https://restic.readthedocs.io/en/v0.3.3/Design/#backups-and-deduplication
|
|-
! ZBackup
|
| C++
|
|
|
|
| ?
|
|
| ?
|
|
|
| GPLv2
|
|
|
|
|}

## File-based increments
If a file is modified, these applications store its new version entirely at the next snapshot. Compared to #Chunk-based increments applications, these are less space-efficient, especially when large files receive small modifications; on the other hand, often the archived snapshots can be opened without the need to have the backup application installed.

Specific legend:

* Hard links: whether unmodified files are stored as hard links to previous versions.

{| class="wikitable sortable" style="text-align:center"
! Name
! Package
! Implementation
! Compressed storage
! Encrypted storage
! Delta transfer
! Encrypted transfer
! FS metadata
! Easy access
! Resumable
! Handles renames
! Hard links
! CLI
! Other interfaces
! Licence
! Other platforms
! Maintained
! Specificity
|-
! Back In Time
|
| Python, rsync, diff
|
|
|
|
|
|
|
|
|
|
|
| GPLv2
|
|
|
|-
! DAR (Disk ARchive)
|
| C++
|
|
|
|
| ?
| ?
| ?
| ?
|
|
|
| GPLv2
| FreeBSD, NetBSD, Windows, macOS
|
|
|-
! rdup
|
| C
|
|
| ?
| ?
| ?
|
| ?
|
|
|
|
| GPLv3
|
|
|
|-
! rsnapshot
|
| rsync
|
|
|
|
| ?
| ?
| ?
| ?
|
|
|
| GPLv2
| Win32
|
|
|-
! Timeshift
|
| rsync
|
|
|
|
| ?
| ?
| ?
| ?
|
|
|
| GPLv3
| Designed for full-system backups to dedicated devices.
|
|
|}

## Network oriented
These applications have been designed to centralize the backup of several machines connected to a network, through a server-client model. In general they are more complicated to deploy, compared to #Single machine solutions.

Specific legend:

* Control direction: Pull: server logs into client. Push: client initiates backup session.
* Increment type: the strategy used to reduce used space by deduplicating data (i.e., besides compression).
** file-based: if a file is modified, the entire new version is stored at each snapshot.
*** hard-links: whether unmodified files are stored as hard links to previous versions.
** chunk-based: only the modified parts of files are stored at each snapshot.

{| class="wikitable sortable" style="text-align:center"
! Name
! Package
! Implementation
! Control direction
! Compressed storage
! Encrypted storage
! Delta transfer
! Encrypted transfer
! FS metadata
! Easy access
! Resumable
! Handles renames
! Increment type
! CLI
! Other interfaces
! Licence
! Other platforms
! Maintained
! Specificity
|-
! BackupPC
|
| Perl
| Pull
|
|
|
|
|
|
|
| ?
| file-based, hard links |
|
| GPLv2
| Any (no client needed)
|
|
|-
! [https://www.bacula.org Bacula
| bacula*
| C++
| Pull
|
|
| ?
|
| ?
| ?
|
| ?
| file-based |
|
| AGPLv3
| Windows, macOS
|
|
|-
! Bareos
| [https://aur.archlinux.org/packages/?K=bareos bareos*
| C++ (Bacula fork)
| ?
| ?
| ?
| ?
| ?
| ?
| ?
| ?
| ?
| ?
| ?
| ?
| AGPLv3
|
|
|
|-
! burp
|
| librsync
| Push
|
|
|
|
|
| ?
|
| ?
| chunk-based |
|
| AGPLv3
| Windows, macOS
|
|
|-
! [https://safekeep.sourceforge.net/ SafeKeep
|
| rdiff-backup
| Pull
|
|
| ?
|
| ?
| ?
| ?
| ?
| chunk-based |
|
| GPLv2
|
|
|
|-
! [https://github.com/ugoviti/synbak Synbak
|
| Multitool wrapper
| ?
|
|
|
|
|
| ?
| ?
| ?
| ?
|
|
| GPLv3
|
|
|
|-
! UrBackup
| urbackup*
| C++
| Pull
|
|
|
|
|
|
|
|
| file-based,hard-links and symlinksCoW-Snapshots[https://blog.urbackup.org/83/file-backup-storage-with-btrfs-snapshots
|  (client)
|
| AGPLv3+
| Windows, macOS
|
|
|}

## Version control systems
While version control systems are mostly used for source code, they can track any files in a directory.

See List of applications/Utilities#Version control systems and dotfiles.
