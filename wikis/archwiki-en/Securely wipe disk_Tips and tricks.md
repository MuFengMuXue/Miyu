# Securely wipe disk/Tips and tricks

See Securely wipe disk for the main article.

This article describes alternative wiping methods to the specialized utilities that can speed up wiping.

## Wipe a single file
Wiping of a single file consists of two basic and one advanced anti-forensic time consumed method that can be done only with specialized tools, the last one method will not be covered in this article.

* Overwrite with random data before deletion or replace content with another one without changing file size.
* Wipe file and meta-data stored by the filesystem with specialized tools
** Search the whole disk for the deleted left-over parts of the file and wipe them too without making any changes to other files and their traces.

Overwriting of the file without changing its size can be done with common Linux utilities:

* Invoking  will replace content of file with pseudo-random data without changing the filesize (). Using the  option will remove file after overwriting it.
* With  you can convert file into the filesystem that will alter everything in it, mount and fill in with any other content for a better overwriting.
* The  will create a file with preset size and content of your choice, if destination file name exist then it will become overwritten. With  command you can replace the whole file or only a part in it with another content by combining  and  options. You need to know size of the file to avoid expand of the file, to do it can use  or . It is mandatory to use  option, see dd#Partial read: copied data is smaller than requested.
* Replace content in a file with a single symbol to avoid size changing you can do with  utility.

To wipe meta-data you can fill in partition with files that makes file system replace old entries about files with new or use specialized utilities for that, see wipe free space section below.

It is up to you how to combine all of Linux file creation and conversion tools to prevent recovery of files and/or mislead recovery tools and them who uses it by rewriting with random or replace with predefined content.

Examples:

Perl command that will replace everything in the file with :

 $ perl -p -i -e 's\file_name

dd:

 $ source_content | dd bs=size_in_bytes count=1 iflag=fullblock of=destination_file seek=0

Or by using stdout redirection that works a slightly faster for creation but you will not be able to use  option for skipping some parts in the destination:

 $ source_content | dd bs=size_in_bytes count=1 iflag=fullblock > destination_file

See also:

* [https://stackoverflow.com/questions/64860/best-way-to-convert-text-files-between-character-sets convert charset in text files
* Advanced Bash-Scripting Guide - describes more advanced ways about how to create files from a bash script
* sed alternatives - a perl example that works better than sed for replacing content in a file

## Overwrite the target
## Prevent wiping mounted partitions
Choosing the device to be wiped needs extra care; a simple typo can be enough to damage the system. To minimize these risks, you can use a simple script to wrap your favourite wipe tool. For example:

{{bc|if  -e "$1" && -b "$1" ;then
NOT_safe="$(lsblk -o "NAME,MOUNTPOINT" ${1//| grep -e / -e '\')";
 if  -z "$NOT_safe" ;then
# Here you can use any of your favourite wiping tools
# to wipe destination passed on command line and stored in variable "$1"
#
  else
  echo 'Not allowed to destroy if any of the partitions is mounted: '"$NOT_safe"
 fi
fi }}

## dd - advanced example
An alternative is to randomize the drive/partition using a randomly-seeded AES cipher from OpenSSL. For example:

 # DEVICE="/dev/sdX"
 # PASS=$(tr -cd '/dev/sd"XY"

With dd you can safely wipe repetitively without out-of-space-errors, if size to be wiped is set up correctly with options. By using dd inside the while loop for stdout you will be able to choose which part of the file you want to restore by combining the  and  options with random or fixed values e.g. restore only partition start or end from a file, related are  and  commands for output of the file parts to stdout.

See also:

* [https://flashdba.com/4k-sector-size/ sector size - file creation and sector sizes

## Wipe free space
You can wipe free space by several ways:

* Redirect output into a file instead of partition or device.
* Create multiple file copies by using e.g.  command in loops with random file names or destination directories until no free space will be left.
* Use an utility that creates encrypted files with random password and file names. Some of the file compression utilities have options for compression methods, file types and can even split file into volumes of the preset size upon creation. By using some options randomly into a loop you will be able to fill the whole free space up with encrypted data and overwrite previous data.
* Use a specialized program for the free space wiping such as:

## Using dd
One can create a file that fills the empty space using dd:

 dd if=source of=junk
 sync
 rm junk

The  can be the  or  stream.
The file is removed after making sure data has synchronized on disk.

## Using 7-Zip
{{bc|1=Password="$(dd if=/dev/random bs=128 count=1 iflag=fullblock)"
DestinationFile="$((${RANDOM/0/1}$(date "+%s")/${RANDOM/0/1}))"
7z a -t7z -mhe=on -p"${Password}" -mx=0 -v1m ${DestinationFile} source}}

See also  for description of used options.

The  can be a predefined file with random data or a device, e.g.  or another block device or partition on it, e.g. , with data you are not afraid to be found then even deleted files on it will be compressed to the destination.

## Create multiple files with help of the timeout command
The  command with randomized waiting time used it in a loop will break the command that will leave a file with random size. This is a slow method but is one of the possible alternatives. You can also use an array with predefined file names before the random part of it.

{{bc|AA=${RANDOM/0/1};
timeout $((AA/100)) cat /dev/urandom > filename${RANDOM}.tmp;
}}
