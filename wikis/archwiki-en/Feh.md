# Feh

From Wikipedia:

:feh is a lightweight image viewer aimed mainly at users of command line interfaces. Unlike most graphical image viewers, feh does not have any graphical control elements (apart from an optional file name display) which enables it to also be used to display background images on systems running the X window system.

## Installation
Install the  package.

## Usage
feh is highly configurable. For a full list of options, run  or see the  man page.

## Browse images
To quickly browse images in a specific directory, you can launch feh with the following arguments:

 $ feh -g 640x480 -d -S filename /path/to/directory

* The  flag forces the images to appear no larger than 640x480
* The  flag draws the file name
* The  flag sorts the images by file name

This is just one example; there are many more options available should you desire more flexibility.

## Set the wallpaper
 can be used to set the desktop wallpaper, for example for window managers without this feature such as Openbox, Fluxbox, and xmonad.

The following command is an example of how to set the initial background:

 $ feh --bg-scale /path/to/image.file

Other scaling options include:

To restore the background on the next session, add the following to your startup file (e.g. , , etc.):

 ~/.fehbg &

To change the background image, edit the file  which gets created after running the command  mentioned above.

One can explicitly disable the creation of the , by passing the  flag as well.

To setup different wallpapers for different monitors one should pass as many file paths as many monitors are available. For example, for a dual monitor setup it would be:

 $ feh --bg-center path/to/file/for/first/monitor path/to/file/for/second/monitor

## Open SVG images
 $ feh --conversion-timeout 1 file.svg

Note that this requires the  package.

## Random background image
You can have feh set a random wallpaper using the  option with one of the  options, for example:

 $ feh --bg-fill --randomize ~/.wallpaper/*

The above command tells feh to randomize the list of files in the  directory and set the backgrounds for all available desktops to whichever images are at the front of the randomized list (one unique image for each desktop). You can also do this recursively, if you have your wallpapers divided into subfolders:

 $ feh --recursive --bg-fill --randomize ~/.wallpaper

To set a different random wallpaper from  each session, add the following to your :

 $ feh --bg-max --randomize ~/.wallpaper/* &

Another way to set a random wallpaper on each xorg session is to edit your  as following.

## Troubleshooting
## Using in cron job
To use feh in a cron job for randomizing your wallpapers, you must specify the DISPLAY environment variable:

 DISPLAY=:0 feh --bg-max --randomize ~/.wallpaper/*

Note that some display managers like sddm might not save of XAUTHORITY file in  where feh
expects it to be, which causes the cronjob to complain about: "Authorization required, but no authorization protocol specified".
