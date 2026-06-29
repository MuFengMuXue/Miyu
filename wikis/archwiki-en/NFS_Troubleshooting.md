# NFS/Troubleshooting

Dedicated article for common problems and solutions.

## Server-side issues
## exportfs: /etc/exports:2: syntax error: bad option list
Make sure to delete all space from the option list in .

## exportfs: requires fsid= for NFS export
As not all filesystems are stored on devices and not all filesystems have UUIDs (e.g. FUSE), it is sometimes necessary to explicitly tell NFS how to identify a filesystem. This is done with the  option:

## Group/GID permissions issues
If NFS shares mount fine, and are fully accessible to the owner, but not to group members; check the number of groups that user belongs to. NFS has a limit of 16 on the number of groups a user can belong to. If you have users with more than this, you need to enable the  start-up flag on the NFS server:

## "Permission denied" when trying to write files as root
* If you need to mount shares as root, and have full r/w access from the client, add the no_root_squash option to the export in :
 /var/cache/pacman/pkg 192.168.1.0/24(rw,no_subtree_check,no_root_squash)

* You must also add no_root_squash to the first line in :
 / 192.168.1.0/24(rw,fsid=root,no_root_squash,no_subtree_check)

## "RPC: Program not registered" when showmount -e command issued
Make sure that  and  are running on the server site, see systemd. If they are not, start and enable them.

Also make sure NFSv3 is enabled. showmount does not work with NFSv4-only servers.

## UDP mounts not working
nfs-utils disabled serving NFS over UDP in version 2.2.1. Arch core updated to 2.3.1 on 21 Dec 2017 (skipping over 2.2.1.) If UDP stopped working then, add  under  in . Then restart .

## Timeout with big directories
Since nfs-utils version 1.0.x, every subdirectory is checked for permissions. This can lead to timeout on directories with a "large" number of subdirectories, even a few hundreds.

To disable this behaviour, add the option  to  to the share directory.

## Client-side issues
## mount.nfs4: No such device
Make sure the  kernel module has been loaded.

## mount.nfs4: Invalid argument
Enable and start  and make sure the appropriate daemons (nfs-idmapd, rpc-gssd, etc) are running on the server.

## mount.nfs4: Network is unreachable
Users making use of systemd-networkd or NetworkManager might notice NFS mounts are not mounted when booting.

Force the network to be completely configured by enabling  or .   This may slow down the boot-process because fewer services run in parallel.

## mount.nfs4: an incorrect mount option was specified
This can happen if using the  option without  and/or  running. Starting and enabling those services should resolve the issue.

## Unable to connect from OS X clients
When trying to connect from an OS X client, you will see that everything is ok in the server logs, but OS X will refuse to mount your NFS share. You can do one of two things to fix this:

* On the NFS server, add the  option to the share in  and re-run .

... OR ...

* On the OS X client, add the  option to the  command line. You can also set  as a default client mount option in :

Using the default client mount option should also affect mounting the share from Finder via "Connect to Server...".

## Unreliable connection from OS X clients
OS X's NFS client is optimized for OS X Servers and might present some issues with Linux servers. If you are experiencing slow performance, frequent disconnects and problems with international characters edit the default mount options by adding the line  to  on your Mac client. More information about the mount options can be found in the OS X .

## Intermittent client freezes when copying large files
If you copy large files from your client machine to the NFS server, the transfer speed is very fast, but after some seconds the speed drops and your client machine intermittently locks up completely for some time until the transfer is finished.

Try adding  as a mount option on the client (e.g. in ) to fix this problem.

## mount.nfs: Operation not permitted
## NFSv4
If you use Kerberos (), make sure the client and server clocks are correct. Using ntpd or systemd-timesyncd is recommended. Also, check that the canonical name for the server as resolved on the client (see Domain name resolution) matches the name in the server's NFS principal.

## NFSv3 and earlier
nfs-utils versions 1.2.1-2 or higher use NFSv4 by default, resulting in NFSv3 shares failing on upgrade. The problem can be solved by using either mount option  or  on the command line:
 # mount.nfs remote target directory -o ...,vers=3,...
 # mount.nfs remote target directory -o ...,nfsvers=3,...
or in :
 remote target directory nfs ...,vers=3,... 0 0
 remote target directory nfs ...,nfsvers=3,... 0 0

## mount.nfs: Protocol not supported
This error occurs when you include the export root in the path of the NFS source.
For example:
 # mount SERVER:/srv/nfs4/media /mnt
 mount.nfs4: Protocol not supported
Use the relative path instead:
 # mount SERVER:/media /mnt

## Permissions issues
If you find that you cannot set the permissions on files properly, make sure the user/user group are both on the client and server.

If all your files are owned by , and you are using NFSv4, on both the client and server, you should ensure that the  has been started.

On some systems detecting the domain from FQDN minus hostname does not seem to work reliably. If files are still showing as  after the above changes, edit , ensure that  is set to . For example:

## Problems with Vagrant and synced_folders
If you get an error about unuspported protocol, you need to enable NFS over UDP on your host (or make Vagrant use NFS over TCP.) See #UDP mounts not working.

If Vagrant scripts are unable to mount folders over NFS, installing the net-tools package may solve the issue.

## fstab entry not mounted on boot
If you have an NFS filesystem mount entry in  but the filesystem is not mounted after the system is booted up, verify the status of : it should be enabled.

## Performance issues
This NFS Howto page has some useful information regarding performance.  Here are some further tips:

## Diagnose the problem
* Htop should be your first port of call.  The most obvious symptom will be a maxed-out CPU.
* Press F2, and under "Display options", enable "Detailed CPU time".  Press F1 for an explanation of the colours used in the CPU bars.  In particular, is the CPU spending most of its time responding to IRQs, or in Wait-IO (wio)?

## Close-to-open/flush-on-close
Symptoms: Your clients are writing many small files.  The server CPU is not maxed out, but there is very high wait-IO, and the server disk seems to be churning more than you might expect.

In order to ensure data consistency across clients, the NFS protocol requires that the client's cache is flushed (all data is pushed to the server) whenever a file is closed after writing.  Because the server is not allowed to buffer disk writes (if it crashes, the client will not realise the data was not written properly), the data is written to disk immediately before the client's request is completed.  When you are writing lots of small files from the client, this means that the server spends most of its time waiting for small files to be written to its disk, which can cause a significant reduction in throughput.

See this excellent article or the nfs manpage for more details on the close-to-open policy.  There are several approaches to solving this problem:

## The nocto mount option
If all of the following conditions are satisfied:

* The export you have mounted on the client is only going to be used by the one client.
* It does not matter too much if a file written on one client does not immediately appear on other clients.
* It does not matter if after a client has written a file, and the client thinks the file has been saved, and then the client crashes, the file may be lost.

Use the nocto mount option, which will disable the close-to-open behavior.

## The async export option
Does your situation match these conditions?

* It is important that when a file is closed after writing on one client, it is:
** Immediately visible on all the other clients.
** Safely stored on the server, even if the client crashes immediately after closing the file.
* It is not important to you that if the server crashes:
** You may lose the files that were most recently written by clients.
** When the server is restarted, the clients will believe their recent files exist, even though they were actually lost.

In this situation, you can use  instead of  in the server's  file for those specific exports.  See the exports manual page for details.  In this case, it does not make sense to use the  mount option on the client.

## Buffer cache size and MTU
Symptoms: High kernel or IRQ CPU usage, a very high packet count through the network card.

This is a trickier optimisation. Make sure this is definitely the problem before spending too much time on this. The default values are usually fine for most situations.

See this article for information about I/O buffering in NFS. Essentially, data is accumulated into buffers before being sent. The size of the buffer will affect the way data is transmitted over the network. The Maximum Transmission Unit (MTU) of the network equipment will also affect throughput, as the buffers need to be split into MTU-sized chunks before they are sent over the network. If your buffer size is too big, the kernel or hardware may spend too much time splitting it into MTU-sized chunks. If the buffer size is too small, there will be overhead involved in sending a very large number of small packets. You can use the rsize and wsize mount options on the client to alter the buffer cache size. To achieve the best throughput, you need to experiment and discover the best values for your setup.

It is possible to change the MTU of many network cards. If your clients are on a separate subnet (e.g. for a Beowulf cluster), it may be safe to configure all of the network cards to use a high MTU. This should be done in very-high-bandwidth environments.

See NFS#Performance tuning for more information.

## Debugging
## Using rpcdebug
Using  is the easiest way to manipulate the kernel interfaces in place of echoing bitmasks to /proc.

{| class="wikitable"
|-
! Option !! Description
|-
| -c || Clear the given debug flags
|-
| -s || Set the given debug flags
|-
| -m module || Specify which module's flags to set or clear.
|-
| -v || Increase the verbosity of rpcdebug's output
|-
| -h || Print a help message and exit. When combined with the -v option, also prints the available debug flags.
|}

For the -m option, the available modules are:

{| class="wikitable"
|-
! Module !! Description
|-
| nfsd || The NFS server
|-
| nfs || The NFS client
|-
| nlm || The Network Lock Manager, in either an NFS client or server
|-
| rpc || The Remote Procedure Call module, in either an NFS client or server
|}

Examples:

Once the flags are set you can tail the journal for the debug output, usually by running  as root or similar.

## Using mountstats
The  package contains the  tool, which can retrieve a lot of statistics about NFS mounts, including average timings and packet size.

## Kernel Interfaces
A bitmask of the debug flags can be echoed into the interface to enable output to syslog; 0 is the default:

Sysctl controls are registered for these interfaces, so they can be used instead of echo:

At runtime the server holds information that can be examined:

A rundown of  (the userspace tool  pretty-prints this info):

## NFSD debug flags
## NFS debug flags
## NLM debug flags
## RPC debug flags
