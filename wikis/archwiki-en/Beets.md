# Beets

Beets is a music tagger and library organizer using the MusicBrainz database. It has been initially released in 2010 and is regularly updated since.

## Installation
Install the  package.

The audio file decoding backend of Beets is audioread, a project developed by the same team.
This backend works itself by using, among others, FFmpeg and/or GStreamer (including its  and  packages) as backends.

Additionally, see the #Plugins for plugin specific dependencies.

## Configuration
User configuration is done using YAML syntax. For example:

## Usage
See the Getting Started guide to start with Beets. In this section, we assume that the reader already know the basics. The following operations are organized by their goal and are more advanced examples than the basics.

## Get help and generalities
The  command and its subcommands (e.g., , , etc.) supports a  flag to print the help. You can list enabled/loaded plugins using . You can enable a verbose output for debugging using the  flag. Finally, you can ensure the default behavior without any loaded plugin only for one command using the  flag.

## Add music
See Beets importing music.

By default, Beets will copy or move imported files as well as writing tags to the file. Beets support a read-only importation mode, where imported files will not be modified nor moved:

 $ beet import -A -C -W path

Additionally, one may enable the  plugin using  such that Beets will look for album arts in the same directory as the imported file.

## List music
See Beets seeing your music.

Beets support custom format for listing the music. The fields name can be either a default/standard field ( in the following example) or a custom/flexible field ( in the following example) as long as it is used in the Beets SQLite database:

 $ beet ls -f 'Mood: ${mood} Genre: ${genre}' query

Here are some corner cases when listing music:
* List files without titles in their tags:
 $ beet list -p "title::^$"
* List missing files in the library:
 $ beet --plugin="badfiles" bad 2>/dev/null | grep "file does not exist"
* Delete missing files from the library automatically:
 $ beet --plugin="badfiles" bad 2>/dev/null | grep "file does not exist" | cut -d ":" -f 1 | xargs -I% beet remove -f path::%

## Remove music
See Beets remove.

## Tag music
To run the Beets auto-tagger on already imported music, the way to go is to re-import the files directly from the music library:
# ...using a path:
# ...using a query (see #Querying)]:

To manually tag music, one may use the  command or the  command from the   plugin (see #Plugins). Beware that the  command will use the  configuration regarding moving ( option) and copying ( option) for moving files after the command completion. For example, you can add two genre tags to the music using:

 $ beet modify query genre="genre1;genre2"

Tagging modifications will be written to the database. To reflect the modifications into the file tags, use the following command:

 $ beet write query

## Querying
Nearly all Beets commands operate on matching items (music files imported into the library) based on a query. You can list the fields available using the  command. The query format is the following:
; : Match songs with  contained in tags , , , , , .
; : Match songs with the  plugin, searching the library using simple ASCII character matching (ignoring special characters).
; : Match sings with the  plugin, searching the library using fuzzy matching algorithms.
; : Match songs with  containing .
; : Match songs with  matching the Python regular expression's .
; : Match songs with  matching numbers between the range  and .
;  / : Match songs with  matching  in a case-sensitive or case-insensitive way, respectively.
; : Logical AND between queries.
; : Logical OR between queries (the  character after the comma is mandatory to separate the keywords).
;  / : Logical NOT.

## ReplayGain
ReplayGain support is accessible via an included plugin (see #Plugins). One can compute ReplayGain information for files matching the query using:

 $ beet --plugin="replaygain" replaygain query

## Album art
Album art is automatically fetched during the import, if the  included plugin is enabled (see #Plugins). After importing, one can:

* Manually add an image as an album art inside a file metadata:
 $ beet --plugin="embedart" embedart -f /path/to/image.jpg query
Ensure that the  plugin is not loaded, otherwise it will delete our album art after saving it, therefore canceling our command.

* Import an album art into the library:
 $ beet --plugin="fetchart" fetchart -q query
It will search in priority for images on the filesystem, i.e., where the music is stored in the library.

* Remove album art from files:
** First, include  in the  parameter of the  plugin inside the configuration file.
** Second, run:
 $ beet --plugin="zero" zero query

## Plugins
Beets supports official plugins and community plugins. Here is a curated list of plugins that add major features that may be available in other music library organizer tools:
; : Support computing and adding ReplayGain information during music import (relies on the FFmpeg or GStreamer backend through the  package).
; : Compute audio fingerprint using the Chromaprint technology and identify songs using the AcoustID online database. Requires the  command-line tool provided by  package for fingerprint computation, and  package for fetching the online database. The fingerprint will be written inside the  tag of files.
; : Search and download lyrics from web databases during music import (relies on the backend  package).
; : Search the local filesystem and/or download album art from web databases during the music import.
; : Transcode a library into another directory (e.g., from lossless to lossy transcoding for nomad devices) (relies on backends like FFmpeg).
; : External plugin supporting multiple versions (e.g., a lossless and lossy version) or locations for the library.
; : Read playlists in  format.
; : Create and automatically update playlists in  format based on predefined queries.
; : Search the library using fuzzy pattern matching.
; : Modify music metadata inside external editors (e.g., configuring the  variable for Vim, Emacs, etc.).
; : Check for corrupted files using checksum. Requires  for FLAC files  for MP3 files.

## Tips and tricks
## Enabling tab autocompletion
Autocompletion is supported for Bash and Zsh.

## Bash
Beets includes support for Bash shell command completion. To enable completion, put the following line into your :

You will also need to install the package  for this to work.

## Zsh
The official Arch package install the Zsh completion on the system.
If using another installation method, to install the completions, make the  (from the upstream repository) file available in one of the Zsh's  directories (either by a copy or symlink).
Using the Zsh's Bash completion compatibility as suggested by the documentation does only work partially.

## Setup the library directory (external drive, network)
Once imported, Beets hard code the path of each item of the library inside the SQLite's  database file.
Therefore, it is recommended to use a fixed path on the filesystem using a link redirecting to the actual directory storing the Beets library.

It has the following advantages:
# Having the link of the library pointing to different paths across machines, when the library is synced but not available on the same path.
# Allowing to dynamically change the path of the library by updating the symbolic link, for example, when switching to a synced external hard drive.
# Not having to deal with SQLite's database items path when the library is moved. Indeed, if you change the library location on the filesystem without any  command, it will be cumbersome to change the path of already imported items inside the database file (see #Updating the library directory).

As an example, to use a symlink with a fixed path of  pointing to a library mounted over network at , execute:

 $ ln -sfT /srv/beets /mnt/network/beets

You can rexecute the same command to update the symlink to another location later.
In the configuration file, one should have:

## Updating the library directory
According to Beets' FAQ, two regular options are offered to modify the path to the library directory (containing music files) after the files have been imported:
# Make the modification in  and use . This solution has the disadvantage that the library should be moved by Beets itself, and not before by an external program.
# Delete the SQLite database ( file) and re-create it from the new path using . This solution has the disadvantage that the custom tags that are stored inside the SQLite database itself (instead of inside the music files' metadata/header) would be lost.

The last solution suggested by Beets developers are to manually modifying the SQLite database without further indication.
This can be achieved by the following, assuming that SQLite is installed, and that the old and new paths of the library was  and , respectively.

1. Make a backup of the library database and open it:

 $ cp /path/to/library.db /path/to/library.db.bak"
 $ sqlite /path/to/library.db

2. List the tables to check that the scheme corresponds to the following  requests, and update it (in-place):

 sqlite> .schema
 sqlite> UPDATE items  SET path    = REPLACE(path,    '/old/library/path', '/new/library/path');
 sqlite> UPDATE albums SET artpath = REPLACE(artpath, '/old/library/path', '/new/library/path');

3. Exit SQLite:

 sqlite> .exit

4. Check that Beets correctly list the files of the library under the new path:

 $ beet ls -p === Synchronization across computers and external drives ===

Beets does not implement any syncing mechanisms on its own. However, its architecture makes it well suited to be used with other FOSS syncing software (as reported in its [https://github.com/beetbox/beets/issues/271 GitHub Issue #271):
; Syncthing: For syncing the SQLite database and the library across devices.
; git-annex: For syncing the library with a more advanced and fine-grained configuration across devices and external drives.
