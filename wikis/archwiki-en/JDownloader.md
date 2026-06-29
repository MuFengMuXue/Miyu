# JDownloader

JDownloader is a download manager written in Java. JDownloader can download normal files, but also files from online file hosting services.

## Installation
Install .

## Running
Use the command jdownloader to start JDownloader. When you have just installed JDownloader, this will run the update tool to download some required files for JDownloader, else this will start JDownloader directly.

## Configuration
When you first start JDownloader you can choose your preferred language and also your download directory. On the next window, JDownloader will ask you if you want to install FlashGot, a Firefox extension, which is entirely optional.

If you enable the Light(GTK) theme and the fonts appear to lack anti-aliasing, follow the directions at Java Runtime Environment fonts#Anti-aliasing.

## Tips and tricks
## Downloading files without creating a subdirectory
By default jdownloader will create a subdirectory for each file you download in your destination folder. To stop this behaviour go to Settings > Packagiser and untick the predefined rules as desired.

## Changing preferences for individual sites
Preferences for individual sites can be found by going to Settings > Plugins. For example, by changing settings on the youtube.com plugin you could tell jdownloader to only download the audio from YouTube links.

## Changing font scale
If font is too small, it can be enlarged by increasing scale factor:
settings > advanced settings > LAFSettings.fontscalefactor jd forum.

## Cleaning up the UI
The graphical user interface can be adjusted to a bigger extent:
* Flashing of the update button can be disabled: change  in the advanced preferences.
* The banner at the top can be disabled by changing .
* Some warning icons can be removed when looking for .
* The Donate Tab can be disabled by setting  to .
* Entries in the menu can be changed when visiting Settings > User Interface > Main Menu, same goes for the Right Click Menu

## Troubleshooting
## Application not resizing with WM, menus immediately closing
see Java#Gray window, applications not resizing with WM, menus immediately closing

## Using the system tray icon
Minimize to tray is broken on Linux. You will run in problems like a little stray window appearing. Disable the feature altogether just to not accidentally run into it. For that, just unplug the checkbox in the settings.

To use the tray, applications which put JDownloader into the tray can be used, namely  or .

Both of them have a launcher, which would send an active application into the tray. The other way to start use them is to launch JDownloader (or any other programm) like that:

 $ kdocker -q -i /usr/share/icons/hicolor/22x22/apps/jdownloader.png -d 15 JDownloader

or

 $ alltray JDownloader

To use the command, you could:

* copy the desktop file to  and edit it.
* copy the desktop file to  and edit it.
* or create

It should be noted though, that when the application restarts, which JDownloader does to install updates, it will not be managed anymore by kdocker / alltray.
