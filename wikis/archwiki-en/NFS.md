# NFS

From Wikipedia:
:Network File System (NFS) is a distributed file system protocol originally developed by Sun Microsystems in 1984, allowing a user on a client computer to access files over a network in a manner similar to how local storage is accessed.

The NFS FAQ lists file systems well tested and details limitations regarding FAT32.

## Installation
Both client and server only require the installation of the  package.

## Server configuration
Global configuration options are set in . Users of simple configurations should not need to edit this file.

The NFS server needs a list of directories to share, in the form of exports (see  for details) which one must define in  or . By default, the directories are exported with their paths as-is; for example:

The above will make the directory  mountable as  for both NFSv3 and NFSv4.

## Custom export root
Shares may be relative to the so-called NFS root. A good security practice is to define a NFS root in a discrete directory tree which will keep users limited to that mount point. Bind mounts are used to link the share mount point to the actual directory elsewhere on the filesystem.

Consider this following example wherein:

# The NFS root is .
# The export is  via a bind mount to the actual target .

 # mkdir -p /srv/nfs/music /mnt/music
 # mount --bind /mnt/music /srv/nfs/music

To make the bind mount persistent across reboots, add it to fstab:

Add directories to be shared and limit them to a range of addresses via a CIDR or hostname(s) of client machines that will be allowed to mount them in , e.g.:

When using NFSv4, the option  or  denotes the "root" export; if such an export is present, then all other directories must be below it. The  option in the  file has no effect on this. The default behavior, when there is no  export, is to behave the same way as in NFSv3.

In the above example, because  is designated as the root, the export  is now mountable as  via NFSv4 – note that the root prefix is omitted.

It should be noted that modifying  while the server is running will require a re-export for changes to take effect:

 # exportfs -arv

To view the current loaded exports state in more detail, use:

 # exportfs -v

For more information about all available options see .

## Starting the server
* To provide both NFSv3 and NFSv4 service, start and enable .
* To provide NFSv4 service exclusively, start and enable .

Users of protocol version 4 exports will probably want to mask at a minimum both  and  to prevent superfluous services from running.  See .  Additionally, consider masking  which is pulled in for some reason as well.

## Restricting NFS to interfaces/IPs
By default, starting  will listen for connections on all network interfaces, regardless of . This can be changed by defining which IPs and/or hostnames to listen on.

Restart  to apply the changes immediately.

## Firewall configuration
To enable access of NFSv4-servers through a firewall, TCP port  must be opened for incoming connections. (NFSv4 uses a static port number; it does not use any auxiliary services such as mountd or portmapper.)

To enable access of NFSv3 servers, you will additionally need to open TCP/UDP port  for the portmapper (rpcbind), as well as the MOUNT (rpc.mountd) port. By default, rpc.mountd selects a port dynamically, so if you're behind a firewall you will want to edit  to set a static port instead. Use  to examine the exact ports in use on the NFSv3 server:

## Client configuration
Users intending to use NFS4 with Kerberos need to start and enable .

## Manual mounting
For NFSv3 use this command to show the server's exported file systems:

 $ showmount -e servername

For NFSv4 mount the root NFS directory and look around for available mounts:

 # mount servername:/ /mountpoint/on/client

Then mount omitting the server's NFS export root:

 # mount -t nfs -o vers=4 servername:/music /mountpoint/on/client

If mount fails try including the server's export root (required for Debian/RHEL/SLES, some distributions need  instead of ):

 # mount -t nfs -o vers=4 servername:/srv/nfs/music /mountpoint/on/client

## Mount using /etc/fstab
Using fstab is useful for a server which is always on, and the NFS shares are available whenever the client boots up. Edit  file, and add an appropriate line reflecting the setup. Again, the server's NFS export root is omitted.

Some additional mount options to consider:

; rsize and wsize: The  value is the number of bytes used when reading from the server. The  value is the number of bytes used when writing to the server. By default, if these options are not specified, the client and server negotiate the largest values they can both support (see  for details). After changing these values, it is recommended to test the performance (see #Performance tuning).
; soft or hard: Determines the recovery behaviour of the NFS client after an NFS request times out. If neither option is specified (or if the  option is specified), NFS requests are retried indefinitely. If the  option is specified, then the NFS client fails an NFS request after retrans retransmissions have been sent, causing the NFS client to return an error to the calling application.

; timeo: The  value is the amount of time, in tenths of a second, to wait before resending a transmission after an RPC timeout. The default value for NFS over TCP is 600 (60 seconds). After the first timeout, the timeout value is doubled for each retry for a maximum of 60 seconds or until a major timeout occurs. If connecting to a slow server or over a busy network, better stability can be achieved by increasing this timeout value.
; retrans: The number of times the NFS client retries a request before it attempts further recovery action. If the  option is not specified, the NFS client tries each request three times. The NFS client generates a "server not responding" message after retrans retries, then attempts further recovery (depending on whether the hard mount option is in effect).
; _netdev: The  option tells the system to wait until the network is up before trying to mount the share - systemd assumes this for NFS.

## Mount using /etc/fstab with systemd
Another method is using the x-systemd.automount option which mounts the filesystem upon access:

To make systemd aware of the changes to fstab, reload systemd and restart  === As systemd unit ===

Create a new  file inside , e.g. . See  for details.

 path to share

 path to mount the share

 share mounting options

To use , start the unit and enable it to run on system boot.

## automount
To automatically mount a share, one may use the following automount unit:

Disable/stop the  unit, and enable/start  to automount the share when the mount path is being accessed.

## Mount using autofs
Using autofs is useful when multiple machines want to connect via NFS; they could both be clients as well as servers. The reason this method is preferable over the earlier one is that if the server is switched off, the client will not throw errors about being unable to find NFS shares. See autofs#NFS network mounts for details.

## Tips and tricks
## NFSv4 idmapping
The NFSv4 protocol represents the local system's UID and GID values on the wire as strings of the form . The process of translating from UID to string and string to UID is referred to as ID mapping.

## Domain
Display the system's effective NFSv4 domain name on stdout.

Edit to match up the Domain on the server and/or client:

## static mapping
These steps are only needed if the server and client have different user/group names.
Changes are only done in the clients config file.

## fallback mapping
Only in the client configuration. Local user/group name to be used when a mapping cannot be completed:

## Performance tuning
When using NFS on a network with a significant number of clients one may increase the default NFS threads from 8 to 16 or even a higher, depending on the server/network requirements:

It may be necessary to tune the  and  mount options to meet the requirements of the network configuration.

In recent linux kernels (>2.6.18) the size of I/O operations allowed by the NFS server (default max block size) varies depending on RAM size, with a maximum of 1M (1048576 bytes), the max block size of the server will be used even if nfs clients requires bigger  and . 	See https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/5.8_technical_notes/known_issues-kernel
It is possible to change the default max block size allowed by the server by writing to the  before starting nfsd. For example, the following command restores the previous default iosize of 32k:

 # echo 32768 > /proc/fs/nfsd/max_block_size

To make the change permanent, create a systemd-tmpfile:

To mount with the increased  and  mount options:

 # mount -t nfs -o rsize=32768,wsize=32768,vers=4 servername:/srv/nfs/music /mountpoint/on/client

Furthermore, despite the violation of NFS protocol, setting  instead of  or  may potentially achieve a significant performance gain especially on spinning disks. Configure exports with this option and then execute  to apply.

## Automatic mount handling
This trick is useful for NFS-shares on a wireless network and/or on a network that may be unreliable. If the NFS host becomes unreachable, the NFS share will be unmounted to hopefully prevent system hangs when using the  mount option [https://bbs.archlinux.org/viewtopic.php?pid=1260240#p1260240.

Make sure that the NFS mount points are correctly indicated in fstab:

Create the  script that will be used by cron or systemd/Timers to use ICMP ping to check if the NFS host is reachable:

{{hc|/usr/local/bin/auto_share|
#!/bin/bash

function net_umount {
  umount -l -f $1 &>/dev/null
}

function net_mount {
  mountpoint -q $1 || mount $1
}

NET_MOUNTS=$(sed -e '/^.*#/d' -e '/^.*:/!d' -e 's/\t/ /g' /etc/fstab | tr -s " ")$'\n'b

printf %s "$NET_MOUNTS" | while IFS= read -r line
do
  SERVER=$(echo $line | cut -f1 -d":")
  MOUNT_POINT=$(echo $line | cut -f2 -d" ")

  # Check if server already tested
  if "${server_ok[@}" =~ "${SERVER}" ]]; then
    # The server is up, make sure the share are mounted
    net_mount $MOUNT_POINT
  elif "${server_notok[@}" =~ "${SERVER}" ]]; then
    # The server could not be reached, unmount the share
    net_umount $MOUNT_POINT
  else
    # Check if the server is reachable
    ping -c 1 "${SERVER}" &>/dev/null

    if [ $? -ne 0 ]; then
      server_notok# The server could not be reached, unmount the share
      net_umount $MOUNT_POINT
    else
      server_ok${#server_ok[@}=$SERVER
      # The server is up, make sure the share are mounted
      net_mount $MOUNT_POINT
    fi
  fi
done
}}

{{Note|Test using a TCP probe instead of ICMP ping (default is tcp port 2049 in NFS4) then replace the line:

 # Check if the server is reachable
 ping -c 1 "${SERVER}" &>/dev/null

with:

 # Check if the server is reachable
 timeout 1 bash -c ": /dev/null
            ;;
    esac
fi
}}

Create a symlink inside  to catch the  events:

 # ln -s /etc/NetworkManager/dispatcher.d/30-nfs.sh /etc/NetworkManager/dispatcher.d/pre-down.d/30-nfs.sh

## TLS encryption
NFS traffic can be encrypted using TLS as of Linux 6.5 using the  mount option. To begin, install the  package on the client and server, and follow the below configuration steps for each.

## Server
Create a private key and obtain a certificate containing your server's DNS name (see Transport Layer Security#Obtaining a certificate for more detail). These files do not need to be added to the system's trust store.

Edit  to use these files, using your own values for  and :

Now start and enable .

## Client
Add the server's TLS certificate generated in the previous step to the system's trust store (see Transport Layer Security#Add a certificate to a trust store for more detail).

Start and enable .

Now you should be able to mount the server using the server's DNS name:

 # mount -o xprtsec=tls servername.domain:/ /mountpoint/on/client

Checking journalctl on the client should show that the TLS handshake was successful:

## Troubleshooting
There is a dedicated article NFS/Troubleshooting.
