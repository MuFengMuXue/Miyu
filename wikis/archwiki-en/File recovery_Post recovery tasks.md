# File recovery/Post recovery tasks

## List only unique files by checksum
When files are restored it might be that many of them have the same hash sum and by making a list of the unique files including only one of the found duplicate files you will speed up gathering extra information about files with other utilities by using stored file names and path in it.

{{bc|find -type f -print0 | \
 xargs -0  md5sum | \
 awk '// {Countif( Count[$1 == 1 ){C=substr($0,index($0,"./"));A=$0;sub(/^.*\//,"",A);B=substr(A,index(A,"_")+1);HASHsum=$1;
 print A"|"B"|"C"|"HASHsum}}'
}}

This will print out result on screen with pattern: filename|restored_filename|full_path_to_filename|check_sum

 f851733136_WindowMaker_Dockapps.pdf|WindowMaker_Dockapps.pdf|./f851733136_WindowMaker_Dockapps.pdf|272cc4fcdc8027e3b8b53318f08f3f01

## Clean up and sort file names
To make destination file names more bash friendly you can remove special symbols, spaces and sort by second column for a better overview of duplicate names with different checksums. To the duplicate file names will be added a number with  as a separator in front of the restored_filename. The script will use file created by script from above and print result to stdout.

{{hc|clean_and_sort.sh|
if [ ! -z "$1" ];then
  awk -F"|" '{B=$2;
   gsub(/\(/,"",B);gsub(/\)/,"",B);
   gsub(/!/,"",B); gsub(/?/,"",B);
   gsub(/\gsub(/{/,"",B); gsub(/}/,"",B);
   gsub(/&/,"",B); gsub(/=/,"",B);
   gsub(/\^/,"",B);gsub(/~/,"",B);
   gsub(" ","",B) ;gsub(/#/,"",B);
   gsub(/\"/,"",B);gsub(/;/,"",B);
   gsub(/\\/,"",B);gsub(/\//,"",B);
   sub(/-*/,"",B); sub(/+*/,"",B);
   print $1" | "B" | "$3}' "$1" | \
  sort --field-separator=\| -s -d -k 2  \
awk -F'|' '{B=$2;Count[B++;sub(/ */,"",B);if( Count== 1 ){print $1"|"B"|"$3}else{print $1"|"Count[$2-1"¤"B"|"$3"|"$4} }'
else echo 'Path to file is missing!'
fi
}}

File names with special symbols especially if file names begins with them are harder to manage with commands like  or  without using quotes or backslash  but if you want to keep information about them then they can be replaced with HTML hex codes instead of removing all of them.

## Photorec
## Creation of a file with data for arrays
In this example the xdg-mime is used to gather information about the mime types but the  and  commands does the same output as the  command, with more or less details. This script will collect a lot of more additional information about the files into the info-mime-size-db.txt. Put the script in the destination directory that you used in photorec, make it executable and use path to files from the list with unique checksums described from above. e.g. {{ic|awk -F" | " '{system("start-collect-file-info.sh "$3" "$1" "$2)}' file_list-unique_checksums}}.

{{hc|start-collect-file-info.sh|#!/bin/bash
if [ ! -z "$1" ] && [ ! -z "$2" ] && [ ! -z "$3" ]; then
if [ -f "$1"  ]; then
echo "$1"
echo "$(file "$1" -F"|"  )'|'$(xdg-mime query filetype "$1")'|'$(du -h "$1" |awk '{print $1}' )|$2|$3" >> info-mime-size-db.txt
else
echo The « "$1" » is not a valid file name.
fi
fi}}
The script will build a file with pattern path to file/file name | info about the file | mime type | size | filename | restored_filename, here is an example:

## Post recovery tasks
This will help you more to understand the script and make your own scripts base on it. You can also put all necessary parts together into a script, modify patterns for files to search and run it. You need to create a database file with name  with information about files.

## Head of the script
Here is a simple check if the  exists in the current directory to prevent possible errors with rest of the script.

## Start variables
{{bc|1=CountAll="0"
CountToLimit="0"
BaseSubDirName="MyRestoredFiles"
Destination="$HOME/NameOfBaseFolder/${BaseSubDirName}-MoreDetailsInFolderName/"
NewDirNumber="0"
CountToLimit="0"}}

## Populate an array
## With a while loop
Here will be a short examples about how to speed up population of the array from a file with patterns by using bash standard expressions instead of awk, grep and sed. The  array will contain full path to the file and the  will contain original names restored by photorec but without random generated part.

{{bc|
WhileArray=0;
while read i; do
if  "$i" =~ "gif" || "$i" =~ "jpeg" ;then
ArrayOfFilesArrayOfsorted[WhileArray=${i/WhileArray=$((WhileArray+1));
fi;
done <  info-mime-size-db.txt
echo done, the array is full
}}

## Loops for restoration
This is a finale part of a script that manages restoration of files. When limit of files in a destination sub-directory reached then it creates and new one numbered sub-directory in the destination folder and continuing to copy files there.

{{bc|SizeOfArray=${#ArrayOfFiles[@}
while [  "${SizeOfArray}" != "${CountAll}" ]; do

IfExist="${Destination}${BaseSubDirName}${NewDirNumber}"
if [ ! -d "${IfExist}" ]; then echo mkdir -v "${IfExist}" -p;fi

CountToLimit=$((CountToLimit+1 ))
FileName=${ArrayOfsortedif [ $CountToLimit -gt 25 ; then
CountToLimit="0"
NewDirNumber=$((NewDirNumber+1))
fi;
NewDestination="$IfExist"

echo cp -fv "$PWD/${ArrayOfFiles"${IfExist}${FileName}"
CountAll=$((CountAll+1))
done}}
{{Note|In order to add more specific details about files in their names or names of the destination directories you will need to gather information about them with external programs, e.g. for image resolution:  {{ic|feh -l "${ArrayOfFiles[$CountAll}"  | tail -1 | awk '{print $3"x"$4}'}},  {{ic|identify ${ArrayOfFiles$CountAll} | awk '{print $3}'}}. }}

## Enough if files are few
If it is not so many files with the same extension then it will be enough to use something like {{ic|find -name *.xcf -exec copy "{}" $HOME/Desktop \;}} to avoid the overload of a destination folder you can calculate how many files are found .
