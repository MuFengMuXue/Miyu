# Thunar

From the project home page:
:Thunar is a modern file manager for the Xfce Desktop Environment. Thunar has been designed from the ground up to be fast and easy-to-use. Its user interface is clean and intuitive, and does not include any confusing or useless options by default. Thunar is fast and responsive with a good start up time and folder load time.

## Installation
Install the  package. Thunar is part of the  group and the default file manager of the Xfce desktop environment.

## Plugins and addons
*
*
*
*
*
*
:*
:*
:*
:*
:*
:*

## Configuration
## Configuring keybindings
To configure the keybindings, edit the file . To configure Thunar's hidden variables, use .

## Change the default sorting behavior
In Thunar it is possible to change the default sorting order. The  file has to be edited, most likely even created. This is what the contents should be like for sort by name, ascending:

## Thunar Volume Manager
If both  and  are installed, Thunar can be configured to run commands automatically when media are connected. For mobile devices, which generally follow MTP, an additional  package is required.

## Configuration
It can also be configured to execute certain actions when cameras and audio players are connected.
After installing the plugin:

# Launch Thunar and go to Edit > Preferences
# Under the 'Advanced' tab, check 'Enable Volume Management'
# Click configure and check the following items:
#* Mount removable drives when hot-plugged.
#* Mount removable media when inserted.
# Also make desired changes (see the example below)

Here is an example setting for making Amarok play an audio CD.

 Multimedia - Audio CDs:

## Custom actions
This section covers useful custom actions which can be accessed through  and which are stored in . More examples are listed in the Thunar wiki. Furthermore, this blog post provides a comprehensive collection of custom actions.

## Open Terminal Here
Open Terminal Here is the sole action on installation. Tell  which terminal to use:

{| class="wikitable"
! Name !! Command !! File patterns !! Appears if selection contains
|-
! Open Terminal Here
|  || * || Directories
|}

## Search for files and folders
To use this action, you need to have  installed. The  and  dependencies are optional for users that want to use a prebuilt index database.

{| class="wikitable"
! Name !! Command !! File patterns !! Appears if selection contains
|-
! Search
|  || * || Directories
|}

## Scan for viruses
To use this action, you need to have  and  installed.

{| class="wikitable"
! Name !! Command !! File patterns !! Appears if selection contains
|-
! Scan for virus
|  || * || Select all
|}

## Link to Dropbox
{| class="wikitable"
! Name !! Command !! File patterns !! Appears if selection contains
|-
! Link to Dropbox
|  || * || Directories, other files
|}

Please note that when using many custom actions to symlink files and folder to a particular place, it might be useful to put them into the  folder of the context menu to avoid that the menu itself gets bloated. This is fairly easy to achieve and requires a .desktop file in  for each action to perform. Say we want to put the above Dropbox symlink action into Send To, we create a  with the following content. The new applied action will be active after restarting Thunar.

## Tips and tricks
## Using Thunar to browse remote locations
Since Xfce 4.8 (Thunar 1.2) it is possible to browse remote locations (such as FTP servers or Samba shares) directly in Thunar. To enable this functionality, ensure that  and  (as well as  if you need SMB/CIFS support) are installed. A 'Network' entry is visible in Thunar's side bar and remote locations can be opened by using the following URI schemes in the location dialog (opened with ): smb://, ftp://, ssh://, sftp://, davs:// & followed by the server hostname or IP address.

There is no URI scheme for NFS shares, but Thunar can issue a  command if you setup your fstab properly.

What is important here is the  which prevents the share from being mounted until you click on it,  which allows any user to mount (and unmount) the share,  which makes network connectivity a pre-requisite, and finally,  which puts the mounting operation in the background so if your server requires some spin-up time, you will not have to deal with time out messages and re-clicking until it works.

## Starting in daemon mode
Thunar may be run in daemon mode. This has several advantages, including a faster startup for Thunar, Thunar running in the background and only opening a window when necessary (for instance, when a flash drive is inserted), and letting Thunar handle automatic mounting of removable media.

Make sure the command  is autostarted on login. See Xfce and Autostarting for more details.

## Solving problem with slow cold start
Some people still have problems with Thunar taking a long time to start for the first time. This is due to gvfs checking the network, preventing Thunar from starting until gvfs finishes its operations. To change this behaviour, edit  and change  to .

## Hide Shortcuts in Side Pane
There is a hidden menu to hide Shortcuts in the Side Pane.

Right click in the Side Pane where there are no shortcuts, like on the DEVICES section label. Then you will get a pop-up menu where you can uncheck items you do not want displayed.

## Assign keyboard shortcuts in Thunar
See GTK#Keyboard shortcuts,

## Showing partitions defined in fstab
By default, Thunar will not show in devices any partitions defined in  besides the root partition.

We can change that by adding the option  to fstab for the partition we wish to show.

## Troubleshooting
## Tumblerd hangs up, uses too much CPU
Tumblerd, the service that watches the file system and notifies the system when a thumbnail needs to be made, may get stuck in a loop, using 100% of the system's CPU; see the bug report. The following script is a temporary workaround to stop this from happening. Copy, and paste this into a .sh file, save it somewhere in your home directory, mark the file as executable and then set up the system to autostart it at system startup.

{{bc|
#!/bin/bash
period=20
tumblerpath="/usr/lib/*/tumbler-1/tumblerd" # The * here should find the right one, whether 32 and 64-bit
cpu_threshold=50
mem_threshold=20
max_strikes=2                               # max number of above cpu/mem-threshold's in a row
log="/tmp/tumblerd-watcher.log"

if  -n "${log}" ; then
    cat /dev/null > "${log}"
    exec >"${log}" 2>&1
fi

strikes=0
while sleep "${period}"; do
    while read pid; do
	cpu_usage=$(ps --no-headers -o pcpu -f "${pid}"|cut -f1 -d.)
	mem_usage=$(ps --no-headers -o pmem -f "${pid}"|cut -f1 -d.)

	if  $cpu_usage -gt $cpu_threshold  ||  $mem_usage -gt $mem_threshold ; then
	    echo "$(date +"%F %T") PID: $pid CPU: $cpu_usage/$cpu_threshold %cpu MEM: $mem_usage/$mem_threshold STRIKES: ${strikes} NPROCS: $(pgrep -c -f ${tumblerpath})"
	    (( strikes++ ))
	    if  ${strikes} -ge ${max_strikes} ; then
		kill "${pid}"
		echo "$(date +"%F %T") PID: $pid KILLED; NPROCS: $(pgrep -c -f ${tumblerpath})"
		strikes=0
	    fi
	else
	    strikes=0
	fi
    done /dev/null; do
    sleep 1
  done
  exec /usr/bin/Thunar "$@"
else
  exec /usr/bin/Thunar "$@"
fi
}}

## Not authenticated to mount filesystems
See File manager functionality#Troubleshooting.

## Thunar new window or tab being too slow to open
It might be the case that you have many files under the folder that you have set to be the . See XDG user directories.

The solution is to move files from whatever folder is the  to another one, or set the  to another folder.
