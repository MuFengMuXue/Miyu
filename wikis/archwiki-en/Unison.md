# Unison

Unison is a bidirectional file synchronization tool that runs on Unix-like operating systems (including Linux, macOS, and Solaris) and Windows. It allows two replicas of a collection of files and directories to be stored on different hosts (or different disks on the same host), modified separately, and then brought up to date by propagating the changes in each replica to the other.

## Installation
Install the  package, which provides CLI and GTK interfaces.

## Configuration
In order to use Unison, you need to create a profile.

## GUI
To configure Unison with the GUI run .

## Manual
Alternatively, manually create a profile in  and add the following lines to the default configuration file, .

Define the root directory to be synchronized.
 root=/home/user/

Define the remote directory where the files should be sychronized to.
 root=ssh://example.com//path/to/server/storage

Optionally, provide arguments to SSH.
 sshargs=-p 4000

Define which directories and files should be synchronized:
 # dirs
 path=Documents
 path=Photos
 path=Study
 # files
 path=.bashrc
 path=.vimrc

You can also define which files to ignore:
 ignore=Name temp.*
 ignore=Name .*~
 ignore=Name *.tmp

## Usage
Once your profile is set up, you can start syncing:
 $ unison profilename
or using the GUI tool:
 $ unison-gui
and select the profile. Unison has a nice interface where you can view the progress and changes.

## Version incompatibility
Since 2.52, Unison has implemented limited support for cross-version syncing. See the migration documentation for details.

For versions prior to 2.52 to function properly, both ends must have installed the same Unison version compiled with the same version of OCaml.

When synchronizing with another distribution you will most likely have to manually compile OCaml and Unison on one end.

## Tips and tricks
## Save human time and keystrokes
If one runs unison within a terminal emulator capable of maintaining a suitable scrollback buffer, there is no purpose in having to confirm every non-conflicting change; set the  option to true to avoid these prompts.

## More helpful diff output
The unison default diff command is . When looking at the output of this command, it can be difficult to remember which changes will be kept when propagating from left to right ('>'), versus right to left ('' keeps lines which start with '>':

 diff = diff -u CURRENT2 CURRENT1 | perl -pe 's/^\+/>/; s/^\-/ emacs -q --eval '(ediff-merge-files-with-ancestor "CURRENT1" "CURRENT2" "CURRENTARCH" nil "NEW")'

This assumes that you are running Unison in X, because the merge command cannot be run in the terminal (Emacs: "standard input is not a tty"). Note also that Unison replaces the CURRENT1, etc., variables with single-quoted filenames. Thus, the above works, but using double quotes throughout, as in "(ediff-merge-files... \"CURRENT1\" ...)", would not work.

Using the variable CURRENTARCH tells Unison that you expect to do 3-way merges with a common ancestor, which is only possible if the "backupcurrent" preference has been set previously to the last sync. To perform an ordinary 2-way merge in a terminal, one could use the following configuration instead. This also uses emerge.el, which some find preferable to ediff.el:

 merge = Name {*,.*} -> urxvt -e emacs -nw -q --eval '(emerge-files nil "CURRENT1" "CURRENT2" "NEW")'

If the variable CURRENTARCHOPT is used instead of CURRENTARCH, then Unison will provide a common ancestor when it is available, and otherwise fall back to requesting a 2-way merge (by setting the variable to the empty string). This can be detected in a shell script. For example:

 merge = Name {*,.*} -> unison-merge-files CURRENT1 CURRENT2 NEW CURRENTARCHOPT

with  defined as follows:

 #!/bin/sh
 CURRENT1=$1
 CURRENT2=$2
 NEW=$3
 CURRENTARCHOPT=$4
 EMACS="urxvt -e emacs -nw"
 if [ x$CURRENTARCHOPT = x ]; then
     $EMACS --eval "(emerge-files nil \"$CURRENT1\" \"$CURRENT2\" \"$NEW\")";
 else
     $EMACS --eval "(emerge-files-with-ancestor nil \"$CURRENT1\" \"$CURRENT2\" \"$CURRENTARCHOPT\" \"$NEW\")";
 fi

## Common configuration synchronization
When syncing configuration files which would vary (e.g., due to endemic applications, security-sensitive configuration) among systems (servers, workstations, laptops, smartphones, etc.) but nevertheless contain common constructs (e.g., key bindings, basic shell aliases), it would be apt to separate such content into separate configuration files (e.g., ), and sync only these.

## Using different data directory
Default unison data directory is . This directory will contain profiles, but also logs and raw data. If you want to change it, you can set an environment variable (in your shell config or before using  command):
 export UNISON="my-unison-data-folder"
