# ClamAV

Clam AntiVirus is an open source (GPL) anti-virus toolkit for UNIX.  It provides a number of utilities including a flexible and scalable multi-threaded daemon, a command line scanner and advanced tool for automatic database updates. Because ClamAV's main use is on file/mail servers, it primarily detects malware with its built-in signatures and is not a traditional endpoint security suite.

The current situation of anti-malware products on Linux is inadequate due to several factors:
#Limited Variety: Compared to Windows, there are fewer users/clients resulting in limited interest for companies to develop products for Linux.
#Complacency: Many believe Linux is inherently secure, leading to a lack of awareness and focus on malware protection. This creates a gap in proactive defense mechanisms.
#Lack of Features: Existing tools often lack advanced features which are common in Windows anti-malware products, making them less effective on Linux.
This is especially bad because the amount of malware on Linux is increasing just as the possible attack surface due to the increasing number of Linux-based servers and IoT devices.

Currently on Linux one of the few existing and actively developed anti-malware solutions is ClamAV.

## Installation
Install the  package.

This will install the following tools:

 clamd: ClamAV Daemon
 clamonacc: On-Access real-time protection
 clamdscan: A simple scanning client
 clamdtop: A resource monitoring interface for clamd
 freshclam: Daemon for virus signature updates
 clamconf: Tool to create and check configuration files

All ClamAV related tools, services and daemons communicate with clamd via a socket.

By default this is done via a local socket, "LocalSocket."

ClamAV also provides the possibility to enable communication via remote locations by using a network socket which is configured and names as "TCPSocket".

Another important thing to note is that when using LocalSocket, then clamd will need to be run under a user with the right permissions to scan the files you plan on including in your monitoring.

## Configuration
Default configuration files should already exist. Otherwise, you can manually create them by using clamconf:

 # clamconf -g freshclam.conf > freshclam.conf
 # clamconf -g clamd.conf > clamd.conf
 # clamconf -g clamav-milter.conf > clamav-milter.conf

The following files contain the relevant configuration options.

* freshclam:
* clamd:
* clamd mail filtering:

Last but not least you can check your config files by running

The default installation will create "sane" default configurations such as: a clamav system user, a clamav group, and the required clamd configuration files.

Additional recommended configurations can be set:

## Enabling real-time protection OnAccessScan
On-access scanning is the real-time protection daemon which will scan the file while reading, writing or executing it. It can be configured to either notify on detection or prevent/block on detection.

Configuration OnAccessScan is done via editing the  configuration file.

The following changes are required for OnAccessScan to work:

The following additional changes are recommended and will put the On-Access Scanner into notify-only mode:

## Creating desktop notifications for alerts
So far ClamAV will silently log any detection but not alert the user. A pop-up to alert the user on any detection can be added.

First add the following line to your clamd configuration:

Next, allow the clamav user to run notify-send as any user with custom environment variables via sudo:

Next, create the file , make it executable and add the following:

{{hc|/etc/clamav/virus-event.bash|2=
#!/bin/bash
PATH=/usr/bin
ALERT="Signature detected by clamav: $CLAM_VIRUSEVENT_VIRUSNAME in $CLAM_VIRUSEVENT_FILENAME"

# Send an alert to all graphical users.
for ADDRESS in /run/user/*; do
    USERID=${ADDRESS#/run/user/}
    /usr/bin/sudo -u "#$USERID" DBUS_SESSION_BUS_ADDRESS="unix:path=$ADDRESS/bus" PATH=${PATH} \
        /usr/bin/notify-send -u critical -i dialog-warning "Virus found!" "$ALERT"
done
}}

This allows you to change/specify the message when a virus has been detected by clamd's on-access scanning service.

By default, clamonacc passes clamav the names of just-accessed files for scanning. This is a problem, because files inaccessible to the clamav user cannot be scanned this way. Instead, it is possible to instruct clamonacc (which always runs as root) to use file descriptor passing. Edit  with the following:

 ExecStart=
 ExecStart=/usr/sbin/clamonacc -F --fdpass --log=/var/log/clamav/clamonacc.log

Lastly, you will need to start/enable or restart the  as well as the

See: #Starting the ClamAV + OnAccessScanning daemon

If you get AppArmor denials about clamd, set the profile to a complain-only mode:

 # aa-complain clamd

## Updating database
Update the virus definitions with:

 # freshclam

If you are behind a proxy, edit  and update HTTPProxyServer, HTTPProxyPort, HTTPProxyUsername and HTTPProxyPassword.

The database files are saved in:

 /var/lib/clamav/daily.cvd
 /var/lib/clamav/main.cvd
 /var/lib/clamav/bytecode.cvd

For automatic updates first create and set the required freshclam.log file:

 touch /var/log/clamav/freshclam.log
 chmod 600 /var/log/clamav/freshclam.log
 chown clamav /var/log/clamav/freshclam.log

Start/enable  or  so that the virus definitions are kept recent.

The  launches  in daemon mode, defaulting to 12 checks per day (every 2 hours). The frequency can be changed in .

The  launches the  check once per day. The frequency can be changed in .

## Starting the ClamAV + OnAccessScanning daemon
This will load all virus signatures in RAM. As of February 2024 these signatures require at least 1.6GB of free RAM. Twice that amount of RAM is used shortly, during the periodic update of the signatures.

The service is called . Start it and enable it to start at boot.

Additionally start and enable  for real-time on access protection.

## Testing the software
In order to make sure ClamAV and the definitions are installed correctly, scan the [https://www.eicar.org/download-anti-malware-testfile/ EICAR test file (a harmless signature with no virus code) with clamscan.

 $ curl https://secure.eicar.org/eicar.com.txt | clamscan -

The output must include:

 stdin: Eicar-Test-Signature FOUND

## Real-time protection
You can download and save the eicar file in one of the directories you configured clamonacc to monitor. For example:

 $ cd /home/user/Downloads/
 $ wget https://secure.eicar.org/eicar.com.txt
 $ cat eicar.com.txt

## Adding more databases/signatures repositories
ClamAV can use databases/signature from other repositories or security vendors.

To add the most important ones in a single step, install  (see online documentation). It will add signatures/databases from popular providers, e.g. MalwarePatrol, SecuriteInfo, Yara, Linux Malware Detect, etc.

## Set up Fangfrisch
As a replacement for the now abandoned , Fangfrisch is more secure, flexible and convenient and requires very little configuration ().

Most importantly,  never needs to be run with root permissions, unlike .

Create database structure by running:

 clamav$ /usr/bin/fangfrisch --conf /etc/fangfrisch/fangfrisch.conf initdb

Enable the  (system-level).

## Scan for viruses
There are two options for on-demand scanning:

## using the stand-alone scanner
 can be used to scan certain files, home directories, or an entire system:

 $ clamscan myfile
 $ clamscan --recursive --infected /home/$USER
 # clamscan --recursive --infected --exclude-dir='^/sys|^/dev' /

If you would like  to remove the infected file add to the command the  option, or you can use  to quarantine them.

You may also want  to scan larger files. In this case, append the options  and  to the command. '4000M' is the largest possible value, and may be lowered as necessary.

Using the  option will print the  logs to a text file for locating reported infections.

## using the daemon
 is similar to the above but utilizes the daemon, which must be running for the command to work. Most options are ignored since the daemon reads the settings specified in .

## Using the milter
Milter will scan your mail server for email containing virus. Adjust  to your needs. For example:

Create :

Your system may require a different  directive. It is needed, for example, when an automatism like logrotate stops the service.

Enable and start .

For Postfix, add the following lines to :

 user must be added to the  group in order to access the  unix socket:
 # usermod -aG clamav postfix

## Tips and tricks
## Run in multiple threads
## Using clamscan
When scanning a file or directory from the command line with , only a single CPU thread is used. Though this results in a lower resource load ― which is sometimes useful when running a scan in the background ― it also results in longer scan times, especially when scanning a large directory or an external drive. As such, you may wish to speed up this process by utilizing as many CPU threads as possible.

 is designed to be single-threaded, so  can be used to run the scan in parallel:

 $ find /home/$USER -type f -print0 | xargs -0 -P $(nproc) clamscan

In this example, the  parameter for  runs  in as many processes as there are CPUs (reported by ) at the same time.  and  options will allow even finer control of batching the workload across the threads.

This will consume loads of RAM as all processes are individual and will load the signature files. A single thread will consume around 1G (or more) of RAM, and may hang your computer unless OOM is clever enough. You may want to consider using clamdscan instead.

## Using clamdscan
If you already have  daemon running  can be used instead (see #Starting the ClamAV + OnAccessScanning daemon):

 $ clamdscan --multiscan --fdpass /home/$USER

Here the  parameter enables  to scan the contents of the directory in parallel using available threads.  parameter is required to pass the file descriptor permissions to  as the daemon is running under  user and group.

The number of available threads for  is determined in  via  parameter . Even though you may see that the number of  specified is more than one (current default is 10), when you start the scan using  from command line and do not specify  option, only one effective CPU thread will be used for scanning.

## TCPSocket — Enabling Network Access for clamd
By default  communicates via a Unix domain socket (), which is sufficient for local clients on the same host. Enabling a TCP socket allows remote clients on a local network to submit files for scanning — useful for centralised scanning infrastructures.

## Architecture
The recommended approach is to let  bind TCP itself via , rather than relying on systemd socket activation for the TCP socket. Socket activation for TCP introduces ordering problems when binding to a non-loopback address: systemd  starts before the network is available, causing the socket unit to fail with . Any attempt to add  to the socket unit creates an ordering cycle through systemd .

The Unix domain socket continues to use socket activation as before. Only TCP is handled differently.

## Configuration
Step 1 — Add TCP binding to :

For loopback (same host only):

For a specific local network interface (e.g. a trusted LAN or management network):

Replace  with the IP address of the interface you want clamd to listen on. Never use  unless all interfaces are protected by a firewall.

Step 2 — Create a systemd service drop-in:

The three directives serve distinct purposes:

*  /   ensures  starts only after the network interface is fully up and the IP address is available.
*   clears the hard dependency on , allowing  to start independently.
*   suppresses systemd's socket passing protocol. Without this,  detects the environment variables , , and  set by systemd and enters socket-activation mode, silently ignoring / from  and logging:

Step 3 — Reload and restart:

 $ sudo systemctl daemon-reload
 $ sudo systemctl restart clamav-daemon.service

Step 4 — Verify:

 $ ss -tlnp | grep 3310

Expected output ( owns the socket, systemd is not listed):
 tcp   LISTEN 0   200   192.168.0.199:3310   0.0.0.0:*   users:(("clamd",...))

## Firewall
When binding to a non-loopback address, restrict access at the firewall level. Example using iptables:

 # Allow only a specific trusted host or subnet
 $ iptables -A INPUT -p tcp --dport 3310 -s 192.168.0.0/24 -j ACCEPT
 $ iptables -A INPUT -p tcp --dport 3310 -j DROP

## Troubleshooting
## Error: Clamd was NOT notified
If you get the following messages after running freshclam:

Add a sock file for ClamAV:

 # touch /run/clamav/clamd.ctl
 # chown clamav:clamav /run/clamav/clamd.ctl

Then, edit  - uncomment this line:

 LocalSocket /run/clamav/clamd.ctl

Save the file and restart .

## Error: No supported database files found
If you get the next error when starting the daemon:

This happens because of mismatch between  setting  and  setting .  pointing to , but  (default directory) pointing to , or other directory. Edit in  and replace with the same  as in . After that clamav will start up successfully.

## Error: Can't create temporary directory
If you get the following error, along with a 'HINT' containing a UID and a GID number:

 # can't create temporary directory

Correct permissions:

 # chown UID:GID /var/lib/clamav && chmod 755 /var/lib/clamav

## ClamOnAcc logfile bloating up to insane sizes and filling up completely with access denied errors
This is happening because of a issue with the stock clamav-clamonacc systemd unit. Modify /lib/modules/systemd/system/clamav-clamonacc.service to read

 ExecStart=/usr/sbin/clamonacc --fdpass -F --log=/var/log/clamav/clamonacc.log --move=/root/quarantine

This instructs clamonacc to pass the file descriptior to clamd who will then do the scan on it's behalf.
