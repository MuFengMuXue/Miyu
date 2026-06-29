# Amarok

Amarok is a music player and organizer for Linux with an intuitive Qt interface that integrates very well with KDE.

## Installation
Install the  package.

Amarok now depends on  directly. See GStreamer#Installation for information on codec support through plugins.

## Customization
## Integration with GNOME
See Uniform look for Qt and GTK applications for visual integration of the main GUI.

## Scripts and applets
New scripts and applets can be found either directly from within Amarok (Tools > Script Manager > Get More Scripts) or at store.kde.org.

## Moodbar
The moodbar is a feature which turns your standard progress slider bar into a progress slider bar coloured depending on the mood of your track.

Install .

Then go to Settings > Configure Amarok and check "Show moodbar in progress slider".

Since Amarok 2 does not generate moodfiles, you can follow this tutorial to create them yourself.

## SHOUTcast
To get SHOUTcast use the "SHOUTcast service" script. Start Amarok, go Tools > Script Manager > Get More Scripts, search for SHOUTcast install Shoutcast Service, restart Amarok. Then you have it in "Internet" context.

See also: How can I use Amarok to stream to my own radio station?, which recommends Internet DJ Console, available as .

## Ampache/MP3 streaming
If you are streaming MP3s directly or with the Ampache plugin, you are not able to seek in tracks if you are not using the GStreamer backend. Install the needed packages:   .
Then go inside Amarok to Settings > Configure Amarok > Playback > Configure Phonon > tab Backend. Here make GStreamer the prefered backend.

## Collection database
Amarok 2.x can use Sqlite (default) or MySQL to store the collection database. Users with large collections and more demanding performance requirements might prefer to use MySQL.

## MySQL
For basic MySQL configuration refer to the MariaDB page.

When using Amarok with MySQL you need to create a MySQL user that can access the database. To do use, enter the following:

This creates a database called 'amarokdb' and a user with name 'amarokuser' with the password password who can access said database from localhost. If you want to connect to your database computer from a different computer, change the line to

 GRANT ALL ON amarok.* TO amarokuser@'%' IDENTIFIED BY "password";

To configure Amarok to use MySQL, enter the Configure Amarok screen, choose Database and mark "use external MySQL database". Enter the server (usually "localhost" if on your local box, else the name of the remote box), the username ("amarokuser" in this example) and your chosen password-user. Do not forget to select the path to your music collection.

## Audio CD playback
If you are not using KDE as your Desktop Environment, Amarok may not have the utilities it needs to play back Audio CDs. Install  to obtain this functionality.

## Firefly/Daap share
To make Daap shares visible in Amarok enable the "DAAP Collection" plugin in the Amarok settings.

Install  and complete the hosts line in  to look like:

After that, start .
