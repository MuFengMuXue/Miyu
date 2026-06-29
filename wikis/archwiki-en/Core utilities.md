# Core utilities

Core utilities are the basic, fundamental tools of a GNU/Linux system. This article provides an incomplete overview of them, links their documentation and describes useful alternatives. The scope of this article includes, but is not limited to, the GNU Core Utilities. Most core utilities are traditional Unix tools and many were standardized by POSIX but have been developed further to provide more features.

Most command-line interfaces are documented in man pages, utilities by the GNU Project are documented primarily in Info manuals, some shells provide a help command for shell builtin commands. Additionally most utilities print their usage when run with the  flag.

## Essentials
The following table lists some important utilities which Arch Linux users should be familiar with. See also .

{| class=wikitable
! Package !! Utility !! Description !! Documentation !! Alternatives
|-
| shell built-ins || cd || change directory ||  || #cd alternatives
|-
|rowspan=13| GNU
| ls || list directory || , info || , #ls alternatives
|-
| cat || concatenate files to stdout || , info || , #cat alternatives
|-
| mkdir || make directory || , info
|-
| rmdir || remove empty directory || , info
|-
| rm || remove files or directories || , info || shred
|-
| cp || copy files or directories || , info || #cp alternatives
|-
| mv || move files or directories || , info
|-
| ln || make hard or symbolic links || , info ||  (soname recovery)
|-
| chown || change file owner and group || , info ||
|-
| chmod || change file permissions || , info
|-
| dd || convert and copy a file || , info || #dd alternatives
|-
| df || report file system disk space usage || , info || #df alternatives
|-
| du || estimate disk space used by files and directories || , info || #du alternatives
|-
| GNU  || tar || tar archiver || , info || archivers
|-
| GNU  || less || terminal pager ||  || terminal pagers
|-
| GNU  || find || search files or directories || , info, GregsWiki || #find alternatives
|-
| GNU  || diff || compare files line by line || , info || #diff alternatives
|-
| GNU  || grep || print lines matching a pattern || , info || #grep alternatives
|-
| GNU  || sed || stream editor || , info, one-liners || ,
|-
| GNU AWK () || AWK || pattern scanning and processing language || , info, one-liners || AWK#Alternative implementations
|-
|rowspan=6|
| dmesg || print or control the kernel ring buffer ||  || systemd journal
|-
| lsblk || list block devices ||
|-
| mount || mount a filesystem ||
|-
| umount || unmount a filesystem ||
|-
| su || substitute user ||  || sudo, doas
|-
| kill || terminate a process ||  || ,
|-
|rowspan=3|
| pgrep || look up processes by name or attributes ||  ||
|-
| ps || show information about processes ||  ||rowspan=2| , system monitors
|-
| free || display amount of free and used memory ||
|}

## Preventing data loss
, ,  and shell redirections happily delete or overwrite files without asking. , , and  all support the  flag to prompt the user before every removal / overwrite. Some users like to enable the  flag by default using aliases. Relying upon these shell options can be dangerous, because you get used to them, resulting in potential data loss when you use another system or user that does not have them. The best way to prevent data loss is to create backups.

## Nonessentials
This table lists core utilities that often come in handy.

{| class=wikitable
! Package !! Utility !! Description !! Documentation !! Alternatives
|-
|rowspan=3| shell built-ins
| alias || define or display aliases ||
|-
| type || print the type of a command ||  || , ,
|-
| time || time a command ||
|-
|rowspan=16| GNU
| tee || read stdin and write to stdout and files || , info ||
|-
| mktemp || make a temporary file or directory || , info
|-
| mknod || create named pipe or device node || , , info
|-
| truncate || shrink or extend the size of a file || , info ||
|-
| basenc || encoding input and output it || , , info
|-
| cut || print selected parts of lines || , info || , ,
|-
| tr || translate or delete characters || , info ||
|-
| od || dump files in octal and other formats || , info || , vim's
|-
| sort || sort lines || , info
|-
| uniq || report or omit repeated lines || , info || , ,
|-
| comm || compare two sorted files line by line || , info ||
|-
| head || output the first part of files || , info
|-
| join || join lines of two inputs on a common field || , info ||
|-
| md5sum || calculate cryptography hash functions of inputs and output || , , info || ,
|-
| tail || output the last part of files, or follow files || , info
|-
| wc || print newline, word and byte count || , info
|-
| GNU  || strings || print printable characters in binary files || , info ||
|-
|  || column || columnate file, optionally pretty-printing in table with grid ||  || ,
|-
| GNU  || xargs || combine or template arguments from stdin to invoke external command ||  ||  ()
|-
| GNU  || iconv || convert character encodings ||  || ,
|-
| GNU  || uudecode || encode file into email friendly text || , , info ||
|-
|  || file || guess file type ||
|}

The  package provides useful tools like  that are missing from the GNU coreutils.

## Alternatives
Alternative core utilities are provided by the following packages:

*
*
*
*
*
*
*

## cat alternatives
*

## cd alternatives
*
*

See also Bash#Auto "cd" when entering just a path and Zsh#Remembering recent directories.

## date alternatives
*
*

## cp alternatives
Using rsync#As cp/mv alternative allows you to resume a failed transfer, to show the transfer status, to skip already existing files and to make sure of the destination files integrity using checksums.

## ls alternatives
*
*
*
*

## find alternatives
*
*
*
*
*

For graphical file searchers, see List of applications/Utilities#File searching.

## diff alternatives
*

While  does not provide a word-wise diff, several other programs do:

*
*
* git diff can do a word diff with , using  it can also be used for files outside of Git working trees.
*
*
*

See also List of applications/Utilities#Comparison, diff, merge.

## grep alternatives
*
*
*

## Code searchers
These tools aim to replace grep for code search. They do recursive search by default, skip binary files and respect .

*
*
*
*
*

See also: .

## Interactive filters
*
*
*
*
*
*

## dd alternatives
See also: dd and ddrescue

## Alternative dd implementations
This subsection lists dd implementations whose interface and default behaviour is mostly compliant with the POSIX specification of .

*
*

## Spin-offs of GNU dd
The GNU implementation of dd found in  also conforms to POSIX. This subsection lists its forks.

*
*

## Modernised dd analogues
This subsection lists dd alternatives that do not conform to POSIX (in terms of the JCL-resembling command-line syntax and default behaviour).

*
*

## buffer spin-offs
This subsection lists forks of , a general-purpose I/O buffering utility similar to dd but has a dynamic-sized buffer. It supports blockwise I/O and can be used when dumping from/to an LTO-tape to avoid shoe shining.

*

## df alternatives
*

## du alternatives
*
*
*
*
*

See also List of applications/Utilities#Disk usage display.

## POSIX shell utilities
Many common packages already install most popular POSIX utilities as dependencies, but the  metapackage can be installed to ensure all of them being always present.

Beside mandatory utilities, there are also metapackages for some of the optional categories:

*
*
*
*

## Tips and tricks
## Override or add missing coreutils
Some commands (, , etc.) are missing from  or taken from other packages. To complete them for compatibility, install  and do:

 # ln -sf /usr/bin/uu-coreutils /usr/local/bin/arch
 # echo -e "#compdef arch=uu-arch\n_uu-arch" > /usr/local/share/zsh/site-functions/_arch
 # echo "complete -c arch -w uu-arch" > /usr/local/share/fish/vendor_completions.d/arch.fish
