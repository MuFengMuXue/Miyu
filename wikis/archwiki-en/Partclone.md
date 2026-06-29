# Partclone

Partclone, like the well-known Partimage, can be used to back up and restore a partition while considering only used blocks.

## Installation
Install the  package.

## Using Partclone with an ext4-formatted partition
## Without compression
To backup without compression:

 # partclone.ext4 -c -s /dev/sda1 -o ~/image_sda1.pcl

To restore it:

 # partclone.ext4 -r -s ~/image_sda1.pcl -o /dev/sda1

## With compression
To backup with compression:

 # partclone.ext4 -c -s /dev/sda1 | lz4 -z > ~/image_sda1.pcl.lz4

To restore it:

 # lz4 -d -c ~/image_sda1.pcl.lz4 | partclone.ext4 -r -o /dev/sda1
