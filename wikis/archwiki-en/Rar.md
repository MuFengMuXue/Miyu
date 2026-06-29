# Rar

WinRAR is an archive manager. It can backup your data and reduce the size of email attachments, open and unpack RAR, ZIP and other files downloaded from Internet, create new archives in RAR and ZIP file format. A trial version is available, so you can try WinRAR before buying.

## Key features
* Variable amounts of redundancy ("recovery record" or "recovery volumes" both of which are demonstrated below) can be added to an archive, making it more resistant to corruption. Even if parts of an archive are damaged, it is possible to fully recover the stored data if a large enough recovery record exists. On its own, Tar does not have this ability.
* RAR is able to efficiently handle split volumes. Built-in support for multi-volume files enables the unpacking program to simply prompt the user for the next .partXXX RAR file, without the need to manually copy and then rejoin the pieces, or for extracting a file from a single piece without needing all pieces. RAR does not support tapes, as it uses seek and rename operations on its files.
* RAR archives can be of a solid format, in which all of the compressed files are treated as a single data block. Most currently used compression formats (with the exception of the older ZIP) allow solid structuring.
* Strong encryption capabilities. Older versions of the file format used a proprietary algorithm; newer versions use the AES encryption algorithm, a block cipher adopted as an encryption standard by the U.S. government. The only known ways to recover an encrypted file are via dictionary or brute force attacks. In newer versions, password protection can optionally protect filenames too, so that the filenames contained within the archive will not be displayed without the right password.

## Installation
Install the  package for both RAR and UnRAR,  for just UnRAR, or  for a FOSS implementation of unrar.

## Configuration file
RAR for Linux reads configuration information from the file  (i.e. in the user's home directory) or if you wish to define a global set of options for all users, in the  directory.

The syntax of the file is simply the following string:

 switches=any_RAR_switches_separated_by_spaces

For example:

 switches=-m5 -rr5p -ol -s -md64 -msmp3;mp4;avi;mkv;zip;7z;rar;tar;gz;bzip2;zst;jpg;jpeg;gif

For a complete listing and explanation of rars switches, see .

## RAR compression examples
## General syntax
 $ rar command -switch 1 -switch N archive files.rar @listfiles...

For a complete listing of commands and switches, see the last section of this article or simply run .

## Recursively compress an entire directory structure
* Task: backup  to  using 10 % recovery records:

 $ rar a -r -rr10p /media/data/darkhorse-backup.rar /home/darkhorse

* Explained:
{| class="wikitable"
| Switch || Action
|-
| a || adds files to archives.
|-
| -r || recurse subdirectories (includes all dirs/files under the parent directory).
|-
| -rr10p || adds recovery records to the archive.  This way up to 10% of the compressed archive can become corrupt or unusable, and it will be able to recover the data through parity.
|}

## Mixed-mode archives
You can also use mixed-mode archives which means that file types you specifiy do not get compressed - they simply get stored.

* Task: backup  to :

 $ rar a -r -rr10p -s -m5 -msjpg;mp3;tar /media/data/darkhorse-backup.rar /home/darkhorse

* Explained:
{| class="wikitable"
| Switch || Action
|-
| a || adds files to archives.
|-
| -r || recurse subdirectories (includes all dirs/files under the parent directory).
|-
| -rr10p || adds recovery records to the archive.  This way up to 10% of the compressed archive can become corrupt or unusable, and it will be able to recover the data through parity.
|-
| -m5 || Use the highest level of compression (m0 = store ... m3 = default ... m5 = maximal level of compression.
|-
| -msjpg;mp3;tar || ignore the compression option and store all .jpg and .mp3 and .tar files.
|-
|}

## Recursively compress many directory structures using a list
* Task: backup  and  and  to .

First create a list (simple text file) containing the various targets.  In this example, the list will be three lines long.  I named it 'home-list' in this example but you can call it anything you want:

 /home/darkhorse
 /home/palomino
 /home/seabiscuit

 $ rar a -r -rr10p -s /media/data/homes-backup.rar @/path/to/home-list

## UnRAR examples
## General syntax
 $ unrar command -switch 1 -switch N archive files... @listfiles... path_to_extract\

For a complete listing of commands and switches simply run:
 $ unrar h

To extract into a new folder:

 $ unrar x /media/data/homes-backup.rar homes-backup/

For multi-part rar files, run:

 $ unrar x homes-backup.part1.rar homes-backup/
