# Playerctl Manual

```text
PLAYERCTL(1)		     General Commands Manual		    PLAYERCTL(1)

NAME
     playerctl —— control media players via MPRIS

SYNOPSIS
     playerctl [-aFhlV] [-f FORMAT] [-i NAME] [-p NAME] command

DESCRIPTION
     The playerctl utility controls MPRIS-enabled media players.  In addition to
     offering  play,  pause and stop control, playerctl also offers previous and
     next track support, the ability to seek backwards and forwards in a  track,
     and  volume  control.   playerctl	also supports displaying metadata (e.g.,
     artist, title, album) for the current track, and showing the status of  the
     player.

     Players  that  can	 be  controlled	 using	playerctl  include audacious(1),
     cmus(1),  mopidy(1),  mpd(1),  quodlibet(1),   rhythmbox(1),   vlc(1)   and
     xmms2(1).	However, any player that implements the MPRIS interface specifi‐
     cation can be controlled using playerctl including web browsers.

     Playerctl	also  comes with a daemon called playerctld which keeps track of
     media player activity. When playerctld is running, playerctl commands  will
     act  on  the  media  player with the most recent activity.	 Run the command
     playerctld daemon to start the daemon.

     The options are as follows:

     -a, --all-players
	     Apply command to all available players.

     -F, --follow
	     Block and output the updated query when it changes.

     -f FORMAT, --format FORMAT
	     Set the output of the  current  command  to  FORMAT.   See	 “Format
	     Strings”.

     -h, --help
	     Print this help, then exit.

     -i NAME, --ignore-player NAME
	     Ignore the specific player NAME.  Multiple players can be specified
	     in a comma-separated list.

     -l, --list-all
	     List the names of running players that can be controlled.

     -p NAME, --player NAME
	     Control  the  specific player NAME.  Multiple players can be speci‐
	     fied in a comma-separated list.  Defaults to  the	first  available
	     player.  The name "name" matches both "name" and "name.{INSTANCE}".
	     Additionally, the name "%any" matches any player.

     -s, --no-messages
	     Silence some diagnostic and error messages.

     -V, --version
	     Print version number, then exit.

     The commands are as follows:

     status  Get the current status of the player.

     play    Command the player to play.

     pause   Command the player to pause.

     play-pause
	     Command the player to toggle between play and pause.

     stop    Command the player to stop.

     next    Command the player to skip to the next track.

     previous
	     Command the player to skip to the previous track.

     position [OFFSET[+|-]]
	     Print  the	 position  of the current track in seconds.  With OFFSET
	     specified, seek to OFFSET seconds from the	 start	of  the	 current
	     track.   With the optional [+|-] appended, seek forward or backward
	     OFFSET seconds from the current position.

     volume [LEVEL[+|-]]
	     Print the player's volume scaled from 0.0 (0%) to 1.0 (100%).  With
	     LEVEL specified, set the player's volume to LEVEL.	  With	the  op‐
	     tional  [+|-] appended, increase or decrease the player's volume by
	     LEVEL.

     metadata [KEY]
	     Print all metadata properties for the current track set by the cur‐
	     rent player.  If KEY is specified only the value of KEY is printed.

     open URI
	     Open URI in the player.  URI may be the name of a file or an exter‐
	     nal URL.

     shuffle [On | Off | Toggle]
	     Print the shuffle status of the player.  With  the	 shuffle  status
	     specified, set the shuffle status to either On , Off , or Toggle

     loop [None | Track | Playlist]
	     Print  the	 loop status of the player.  With the loop status speci‐
	     fied, set the loop status to None (disable	 looping),  Track  (loop
	     the current track), or Playlist (loop the current playlist).

   Format Strings
     The  output  of  the  position, metadata, status and volume commands can be
     controlled using a format string.	Variables set by these commands	 can  be
     included in the format string by enclosing them in curly braces: ‘{{var}}’.
     These will then be expanded on output.

     Each command has access to the following variables:

     playerName
	     The name of the current player.

     position
	     The time position of the current track, in microseconds.

     status  The status of the current player.

     volume  The player's volume scaled from 0.0 (0%) to 1.0 (100%).

     Each property listed in the metadata command are also set as variables.  It
     is recommended to check this list for each player, as different players may
     not  set  the  same properties.  See the MPRIS v2 metadata guidelines for a
     list of all properties in the MPRIS specification.	 The most common proper‐
     ties are as follows:

     album, xesam:album
	     The album of the current track.

     artist, xesam:artist
	     The artist of the current track.

     title, xesam:title
	     The title of the current track.

     Helper functions are also available to transform  expanded	 variables  into
     other  representations.   They are called in the form ‘{{func(var)}}’.  The
     helper functions are as follows:

     lc(str)
	     Convert string str to lowercase.

     uc(str)
	     Convert string str to uppercase.

     markup_escape(str)
	     Escape XML characters in string str.

     default(str1, str2)
	     Print str1 if set, else print str2.

     duration(time)
	     Reformat the microsecond timestamp time  in  the  form  ‘hh:mm:ss’.
	     Can only be called with position or mpris:length.

     emoji(key)
	     Try  to  convert the value for key to an emoji representation. Cur‐
	     rently implemented for status and volume.

     trunc(str, len)
	     Truncate str to a maximum of len  characters,  adding  an	ellipsis
	     (â¦) if necessary.

     The template language is also able to perform basic math operations.

     References to unknown functions will cause playerctl to exit with an error.
     References	 to  unknown  variables will be expanded to empty strings.  Text
     not enclosed in braces will be printed verbatim.

EXIT STATUS
     The playerctl utility exits 0 on success, and >0 if an error occurs.

EXAMPLES
     Print the player name, playback  status  in  lowercase,  and  position  and
     length in human readable form:

	   $ playerctl metadata --format '{{playerName}}: {{lc(status)}} '\
	   '{{duration(position)}}|{{duration(mpris:length)}}'

SEE ALSO
     MPRIS    v2   metadata   guidelines,   freedesktop.org,   https://freedesk‐
     top.org/wiki/Specifications/mpris-spec/metadata/, September 18, 2013.

     playerctl homepage, playerctl API documentation, GObject introspection lan‐
     guage bindings

AUTHORS
     The playerctl utility is maintained by Tony  Crisci  <tony@dubstepdish.com>
     and is made available under the GNU Lesser General Public License 3.0.

     This  reference was written by Nick Morrott <knowledgejunkie@gmail.com> for
     the Debian GNU/Linux project.  It was later updated and expanded by Stephen
     Gregoratto <dev@sgregoratto.me>.

GNU				     UNDATED			    PLAYERCTL(1)
```
