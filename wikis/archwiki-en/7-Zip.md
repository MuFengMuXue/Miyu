# 7-Zip

7-Zip is a file archiver with a high compression ratio. It was previously provided by the p7zip package.

## Installation
Install the  package.

The command to run the program is the following:

 $ 7z

Alternatively,  provides 7z archive support and is included within the  package.

## Examples
Add file/directory to the archive (or create a new one):

 $ 7z a archive_name file_name

Also it is possible to set password with flag  and hide structure of the archive with flag :

 $ 7z a archive_name file_name -p -mhe=on

Update existing files in the archive or add new ones:

 $ 7z u archive_name file_name

List the content of an archive:

 $ 7z l archive_name

Extract all files from an archive to the current directory:

 $ 7z x archive_name

Extract into a new directory:

 $ 7z x -odirectory_name archive_name

Check integrity of the archive:

 $ 7z t archive_name

## Differences between 7z, 7za and 7zr binaries
The package includes three binaries:

*  uses plugins to handle archives.
*  is a stand-alone executable that handles fewer archive formats than 7z.
*  is a stand-alone executable. It is a "light-version" of 7za that only handles 7z archives. In contrast to 7za, it cannot handle encrypted archives.
