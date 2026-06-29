# Wim

WIM (Microsoft Windows Imaging Format) is a file-based disk image format for Windows. It is often used in Windows installers.

## Installation
On Linux, install  to work on these files.

## View information
To view information about the WIM file (including but not limited to: name, index, etc…), use:

 $ wiminfo image_file

## Mount
WIM as an image file can be mounted with the following command

## Read-only mount
 # wimmount image_file index directory

## Mount as read/write
 # wimmountrw image_file index directory

## Unmount
 # wimunmount directory --commit

to apply the changes in the read-write mount.

## Directory structure
To view the directory structure of a WIM image, use:

 # wimdir image_file index

## Extract the image
To extract the full image, do:

 # wimapply image_file index target_directory

If you only need a few files from the image, use .

## Compression
The Windows ISO is larger than 4GiB, so it cannot be copied to a boot disk formatted with the FAT32 file system, you will need to compress  to do this:

 # wimlib-imagex optimize install.wim --solid
