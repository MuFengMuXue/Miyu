# Gerbera

Gerbera is an open source UPnP media server with a web interface. It allows you to stream your digital media through your home network and listen to/watch it on a variety of UPnP compatible devices. It is a fork of the now-defunct MediaTomb.

## Installation
Install the  package.

By default, Gerbera sets up its own sqlite database. Alternatively, to use it with an external MariaDB server, uncomment the line containing  prior to building and see the official documentation for more information.

## Configuration
Gerbera may be configured and run per-user or as a system-wide daemon.

## Per-user
To create the configuration file for the current user:

 $ mkdir -p ~/.config/gerbera
 $ gerbera --create-config > ~/.config/gerbera/config.xml

Then run gerbera to start it.

## System-wide
The system-wide configuration file should be created by the gerbera user:

 gerbera --create-config > /etc/gerbera/config.xml

Then start/enable  to start the daemon.

## Usage
The daemon listens on port  by default. To access the web interface and begin importing media, navigate to http://localhost:50500/ in your favorite browser.

If running a per-user instance, the default port is . However, it is possible that the port will change upon server restart. The URL for the web interface is output during startup. Users may also specify the port manually:

 $ gerbera -p 50500

## Hiding full paths from media players
By default, full directory paths will be shown on devices when they are browsing through folders.

For example, if you add the directory , anyone connecting will have to navigate to the 'movies' directory from the root.

To hide all of that and only show the directory added, you can change the import script.

For example, this script will automatically truncate the whole directory structure specified in the variable video_root. Any directories added directly under the video root path will show up on UPnP devices starting from the that folder rather than .

 function addVideo(obj)
 {
    var video_root = "/media/main_core/Server_Core_Folder/FTP_Services/Media/";

    var absolute_path = obj.location;

    var relative_path = absolute_path;

    if(absolute_path.indexOf(video_root) == 0)
       relative_path = absolute_path.replace(video_root, "")

   var chain = new Array();

   var pathSplit = relative_path.split("/");

   for(var i = 0; i

## Playstation 3 Support
The following notes assume MediaTomb is running as a system-wide daemon. For a per-user install, the locations of the configuration file will be different (see above).

For PlayStation 3 support, users must set . An "avi" mimetype mapping should also be uncommented for DivX support.

When importing media to the database, MediaTomb will create a virtual container layout as defined by the  option. That is, media will be organized according to metadata (album, artist, etc.) through creation of virtual database objects. If your media is already organized on the file system, you may disable this feature to significantly improve import performance:

Users may customize the import script to fine-tune the virtual layout. The [http://mediatomb.cc/dokuwiki/scripting:scripting Scripting section of the MediaTomb wiki provides several examples. Starting with the built-in script available at :

 $ cp /usr/share/mediatomb/js/import.js /var/lib/mediatomb/.mediatomb/

... and edit  as desired. To utilize the customized script, users must set  and specify the script's location.

You may have to specify a network interface before MediaTomb will be recognized:

After configuring MediaTomb to your liking, restart .

## Troubleshooting
## Gerbera does not provide content even though it is added in the webfrontend
Be aware of the fact that the user Gerbera runs under, has to have read rights on the files that are added to be able to provide them.

So if Gerbera runs under the user 'gerbera' the (video-)files either have to be owned by the user 'gerbera' and need to be readable or the files and the user 'gerbera' have to belong to the same group with the file being readable ('gerbera' has to be in the group to which the file belongs (the file then needs the read rights for the group to be set)).

## The Client loses connection after 30 Minutes
Apparently this is related to SSNP message only being sent once which results in the Client dropping its connection in 30 minutes since it thinks the server is gone.

In the  add the alive tag:

 180

Default is . See https://docs.gerbera.io/en/stable/config-server.html#alive.
