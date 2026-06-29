# Aria2

From the project home page:
:aria2 is a lightweight multi-protocol & multi-source command-line download utility. It supports HTTP/HTTPS, FTP, BitTorrent and Metalink. aria2 can be manipulated via built-in JSON-RPC and XML-RPC interfaces.

## Installation
Install the  package.

To use aria2 as a daemon, you can write a systemd user unit.

## Configuration
## aria2.conf
aria2 looks at  for a set of global configuration options by default. This behavior can be modified with the  switch:

The following example downloads  using the options specified in the configuration file

 $ aria2c --conf-path=/file/aria2.rapidshare http://rapidshare.com/files/12345678/aria2.example.rar

If  exists and the options specified in  are desired, the  switch must be appended to the command:

The following example does not use the default configuration file and downloads  using the options specified in the configuration file

 $ aria2c --no-conf --conf-path=/file/aria2.rapidshare http://rapidshare.com/files/12345678/aria2.example.rar

If  does not yet exist and you wish to simplify the management of configuration options:

 $ touch $XDG_CONFIG_HOME/aria2/aria2.conf

## Example aria2.conf
{{bc|1=
continue
dir=${HOME}/Desktop
file-allocation=none
input-file=${HOME}/.aria2/input.conf
log-level=warn
max-connection-per-server=4
min-split-size=5M
on-download-complete=exit
}}

This is essentially the same as if running the following:

 $ aria2c --dir=${HOME}/Desktop --file-allocation=none --input-file=${HOME}/.aria2/input.conf --on-download-complete=exit --log-level=warn FILE

{{Note|The example aria2.conf above may incorrectly use the $HOME variable. Some users have reported the curly brace syntax to explicitly create a separate ${HOME} subdirectory in the aria2 working directory. Such a directory may be difficult to traverse as bash will consider it to be the $HOME environment variable. For now, it is recommended to use absolute path names in aria2.conf.}}

## Option details
*: Continue downloading a partially downloaded file if a corresponding control file exists.
*{{ic|1=dir=${HOME}/Desktop}}: Store the downloaded file(s) in .
*: Do not pre-allocate disk space before downloading begins. (Default: prealloc) 1
*{{ic|1=input-file=${HOME}/.aria2/input.conf}}: Download a list of line, or TAB separated URIs found in
*: Set log level to output warnings and errors only. (Default: debug)
*: Set a maximum of four (4) connections to each server per file. (Default: 1)
*: Only split the file if the size is larger than 2*5MB = 10MB. (Default: 20M)
*: Run the  command and exit the shell once the download session is complete.

## Example input file #1
Download  from two separate sources to  before merging as
 http://aria2.net/files/stable/aria2-1.10.0/aria2-1.10.0.tar.bz2    http://sourceforge.net/projects/aria2/files/stable/aria2-1.10.0/aria2-1.10.0.tar.bz2

## Example input file #2
Download  and save to  as

 http://aria2.net/files/stable/aria2-1.9.5/aria2-1.9.5.tar.bz2
   dir=/file/old
   out=aria2.old.tar.bz2

Download  and save to  as

 http://aria2.net/files/stable/aria2-1.10.0/aria2-1.10.0.tar.bz2
   out=aria2.new.tar.bz2

## Additional notes
1 : Recommended for newer file systems such as ext4 (with extents support), btrfs or XFS as it allocates large files (GB) almost instantly. Do not use falloc with legacy file systems such as ext3 as prealloc consumes approximately the same amount of time as standard allocation would while locking the aria2 process from proceeding to download.

## Example aria2.rapidshare
## Option details
*: Set HTTP username as USER_NAME for password-protected logins. This affects all URIs.
*: Set HTTP password as PASSWORD for password-protected logins. This affects all URIs.
*: Restart download if a corresponding control file does not exist. (Default: false)
*: Store the downloaded file(s) in .
*: Call  to allocate disk space before downloading begins. (Default: prealloc)
*: Enable HTTP/1.1 pipelining to overcome network latency and to reduce network load. (Default: false)
*: Download a list of single line of TAB separated URIs found in
*: Set log level to output errors only. (Default: debug)
*: Set a maximum of two (2) connections to each server per file. (Default: 1)
*: Output download progress summary every 120 seconds. (Default: 60) 2

## Additional notes
* Because the  contains a username and password, it is advisable to set permissions on the file to 600, or similar.

 $ cd /file
 $ chmod 600 /file/aria2.rapidshare
 $ ls -l
 total 128M
 -rw------- 1 arch users  167 Aug 20 00:00 aria2.rapidshare

2 : Suppresses download progress summary output and may improve overall performance. Logs will continue to be output according to the value specified in the  option.

## Example aria2.bittorrent
## Option details
*: Do not check the hash of the file(s) before seeding. (Default: true)
*: Set maximum overall upload speed to 1MB/sec. (Default: 0)
*:  Set maximum upload speed per torrent to 128K/sec. (Default: 0)
*: Seed completed torrents until share ratio reaches 5.0. (Default: 1.0)
*: Seed completed torrents for 240 minutes.

## Example aria2.daemon
This configuration can be used to start aria2 as a service. It can be used in conjunction with several of the frontends listed below. Note that rpc-user and rpc-pass are deprecated, but most frontends have not been ported to the new authentication yet. Do not forget to change user, password and Download directory.

## Frontends
## Web UIs
*
*
*

## Other UIs
*
*
*
*

## Tips and tricks
## Download the packages without installing them
Just use the command below:

 # pacman -Sp packages | aria2c -i -

 lists the URLs of the packages on stdout, instead of downloading them, then  pipes it to the next command. Finally, the  in  switch to aria2c means that the URLs for files to be downloaded should be read from the file specified, but if  is passed, then read the URLs from stdin.

## pacman XferCommand
See pacman/Tips and tricks#aria2.

## Changing the User Agent
Some sites may filter the requests based on your User Agent, since aria2 is not a well known downloader, it may be good to use a most known downloader or browser as the Aria's User Agent. Just use the  option like this:

 $ aria2c -UWget http://some-url-to-download/file.xyz

You can use whatever you want, like -UMozilla/5.0 and so on.

## Using aria2 with makepkg
You can use aria2 instead of  to download source files, just change the  variable as follows:

## Using aria2 as a Daemon
To use aria2 as a daemon, you should write a systemd user unit. For example:

#Example aria2.daemon shows an example configuration file.

## Seed a torrent with aria2
To seed an already downloaded torrent, use the  option:

 $ aria2c --check-integrity=true --seed-ratio=0.0 --dir="/path/to/iso" "/path/to/torrent"

Specifying  will seed the file forever.

## Using aria2 with torsocks
Aria2 can be used with torsocks for downloading over Tor; keep in mind that this is limited to TCP-based protocols, so torrents will not work.

By default, aria2 will try to use its own implementation of a DNS resolver, which does not work under torsocks. This problem can be fixed by passing the  option:

 $ torsocks aria2c --async-dns=false 'https://fastly.mirror.pkgbuild.com/iso/latest/archlinux-x86_64.iso'
