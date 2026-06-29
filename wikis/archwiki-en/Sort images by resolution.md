# Sort images by resolution

When recovery of files done and you restored images with help of a post recovery tasks script then it could be wise to sort images by the resolution. This will help to sort the photos you made, webcam images or any other images into the folders by the resolutions, most of them are often using the same related image resolutions.

## Collect info about images
{{hc|collect-info-about-images.sh|#!/bin/bash
if [ 'XX' != 'XX'"$1" ]; then
 if [ -f "$1"  ]; then
# mime part start
  IsIt=$(file "$1" --mime-type -b);
  NeedImageOnly="ItIs_"${IsIt/'/'*/}
   if [ "$NeedImageOnly" == "ItIs_image" ] ; then
# mime part end
ImageInfoFEH=($(feh -l "$1"))
IfDamaged=${?}
ImageType=${ImageInfoFEHHeight=${ImageInfoFEH[11}
    Width=${ImageInfoFEHif [ "$IfDamaged" != '0'  ; then
    echo "$1" "Damaged" "${IfDamaged}";
   fi;
    echo "$1"'|'W'|'$Width'|'H'|'$Height'|'Format'|'$ImageType'|'Errors'|'$IfDamaged'|' >> collect-info-about-images.txt
# mime part start
  fi
# mime part end
   else
    echo The « "$1" » is not a valid file name.
  fi
 else
  ScriptsName=${0##*/}
   find -type f -exec sh -e "./$ScriptsName" "{}" \;
  #find -type f  -name "*.jpg" -o -name "*.gif" -o -name "*.png" -exec sh -e "./$ScriptsName" "{}" \;
fi
}}
The $IfDamaged variable contains an exit status code returned by .

You can also install  to check integrity of "PNG, JNG or MNG" and/or  and use output of errors in the $IfDamaged variable or modify script to skip adding of damaged files into a  file.

Example of  check resuslt:

Example of  check result:

To extract necessary data from a string in a script is better to use an expression instead of an extern program as  or  to make a script work a little faster, e.g.
{{bc|1=AA="$(jpeginfo -c f62152912.jpg)";
ZZ="${AA/*' if [ 'XX'"$ZZ" == 'XX' ; then
  echo File is good'!!!';
fi
}}

The collect-info-about-images.sh script generates data about images by pattern:
 full path to image|Width|size|Height|size|Format|type of image|Errors|exit code by feh|
Example:

## Sort images by resolution
This script creates folders based on the resolution. You can set your limitations about how many files should be in each folder and how many sub-directories in a base file type named folder. When limit is reached a new number in the order will be added to a directory name for creation. If you have a really huge amount of files and do not want to overload a single folder with all of them then you can also add your own counters for a new sub-folders after the base destination variable {{ic|1=IfExist="${Destination}/}}, just look out for quotes " to be in the begin and end of a whole destination path. It use to be much more easier to browse folders with a limited amount of images, thumbnails loads much faster and to remember or add to favorite a folder number/name instead of trying to find once more same image in an overloaded folder out of probably thousand images there.

{{bc|#!/bin/bash

NumberOfBaseDir="0"
SubDirNumber="0"
CountAll="0"
NumDir="0"

echo Creating destination.
Destination="./SortedImages"
echo mkdir -v "${Destination}" -p
echo Created destination with status: $?

echo Your set of limitations.
SDN=50; echo Limit files in a subdir: $SDN
NBD=50; echo Limit subdirs in a file type named destination: $NBD

SourceDataFile="collect-info-about-images.txt"
echo Source file with a necessery data: $SourceDataFile

if [ 'XX' == 'XX'"$SourceDataFile" ] ; then
 echo The '$SourceDataFile' variable is empty
 exit 1
else
 if [ ! -f "$SourceDataFile" ]; then
  echo The "$SourceDataFile" file doesn"'"t exist
  exit 2
 fi;
fi;

echo Populating an array from a file
ArrayFillCount=0;
while read line ; do
  tmpWb="${line/|H|*/}";
W="${tmpWb/*W|/}";
  tmpHb="${line/|Format|*/}";
H="${tmpHb/*|/}";

#if (( "$W" >= "800" )) && (( "$W" = "800" )) && (( "$H" <=  "1000" )); then
  ArrayOfFilesArrayFillCount=$((ArrayFillCount+1))
DupLimitKeeper[$W,$H="0";
#fi;fi;

done < $SourceDataFile;
echo Done with extracting of necessary data about resolutions.

echo Starting loop of restoration
XX=${#ArrayOfFileswhile [  "${XX}" != "${CountAl}l"  ; do
  preType=${ArrayOfFilesImageType=${preType/|*/}
  preW=${ArrayOfFiles[$CountAll/*"|W|"/};Width=${preW/|*/};preH=${ArrayOfFilesHeight=${preH/|*/};
PathToFile=${ArrayOfFiles[$CountAll/"|"*/}

DupLimitKeeperIfExist="${Destination}/${ImageType}${NumberOfBaseDir}/Resolution_${Width}x${Height}_DirN${SubDirNumber}"

if [ ! -d "$IfExist"  ;then
  echo mkdir -vp "$IfExist"
NumDir=$((NumDir+1));
fi

## Creating a new numbered file type folders
if [ "${DupLimitKeeper-gt $SDN ; then
  SubDirNumber=$((SubDirNumber+1));
  DupLimitKeeperfi

## Adding a file number
FileNameOnly="${PathToFile##*/}"
NewFileName="N${CountAll}C${FileNameOnly}"
#NewFileName="${FileNameOnly}"

## Creating a new sub-dir when limit of files in a sub-folder is reached
if [ $NumDir -gt $NBD ;then
  NumberOfBaseDir=$((NumberOfBaseDir+1));
  NumDir="0";
fi
##
if [ -f "${PathToFile}" ];then
  echo mv -v "${PathToFile}" "$IfExist/$NewFileName";
# echo cp -v "${PathToFile}" "$IfExist/$NewFileName";
fi

CountAll=$((CountAll+1))
done
echo Total processed files: $CountAll
}}
