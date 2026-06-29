# Idesk

Idesk is a simple program for adding icons to your X desktop. It can also manage your wallpaper with a built in changer similar to that found in Windows 7.

## Installation
Install the  package and create the  directory.

## Configuration
At the first run idesk will create the  configuration file. If  is empty, it will also create the  icon, which just runs  to display a welcome message. It can be used as a template for other icons.

The  package does not come with a man page, but it does come with a readme file: . There is also documentation on SourceForge.net, however most of the configuration options should be self-explanatory.

## Background options
If you are using another wallpaper setter such as Feh or Nitrogen, Idesk's background settings do not need to be modified.

If you are using Idesk's own background setter, supported wallpaper formats include JPEG, PNG, GIF, and XPM. Using either  or , specify the path to the image file you wish to use as a wallpaper.

## Icons
Idesk looks in  for files which names end with  for icons. Each file should define one icon. If you attempt to define a second icon, it will be silently ignored. Aside from ending with , the files' names are not important.

Example for Chromium:

 and  should match the actual dimensions of the icon.  and  will be modified by idesk to reflect the icon's actual position.

## Idesktool
The  package provides a graphical configuration tool for Idesk. It can be started by running the  command. Users can use Idesktool to create and remove icons, modify settings and restart Idesk.
