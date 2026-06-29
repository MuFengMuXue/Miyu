# CrashPlan

CrashPlan is a backup program that backs up data to remote servers, other computers, or hard drives. Backing up to the cloud servers requires a monthly subscription.

## Installation
Install .

## Usage
Before accessing CrashPlan's graphical user interface, you should start the  unit.

CrashPlan can be configured entirely through its graphical user interface. To start the graphical interface:

 $ CrashPlanDesktop

To make CrashPlan automatically start upon system startup, enable the systemd unit.

## On a headless server
Running CrashPlan on a headless server is not officially supported. However, it is possible to do so.

The CrashPlan daemon's configuration files (in ) are in an obscure XML format, and they are meant to be edited programmatically by the CrashPlan client.

CrashPlan 5 introduced a new client which unfortunately dropped support for configuring a remote server with a local client, so you will need to use X11 forwarding.

## X11 forwarding over SSH
Ensure that  is set to  in the headless server's  and from another machine running X11, SSH to the headless machine with , and from the remote shell run . The headless machine's windows will appear on the local X11 server. If you have problems, check .

## Local client
On CrashPlan v4.x and below, the client and daemon communicate on port 4243 by default. Thus, an easy way of configuring the CrashPlan daemon on a headless server is to create an SSH tunnel:

# Start the CrashPlan daemon on the server.
# Create an SSH tunnel. On the client: .
# Start the CrashPlan client. (Again, the executable is named .)

Note that the authentication token (located in ) on the local and remote servers must match. More ideas can be found on these websites:

* The CrashPlan support site details a slightly more complicated method of tunneling traffic from the client (CrashPlan Desktop) to the daemon (CrashPlan Engine) through an SSH tunnel.
* A post by Bryan Ross details how to make CrashPlan Desktop connect directly to CrashPlan Engine. Note that this method can be less secure than tunneling traffic through an SSH tunnel.

## Troubleshooting
## Waiting for Backup
If the backup is stuck on «Waiting for Backup» even after you engage it manually, it might be that CrashPlan cannot access the tempdir or it is mounted as . It uses the default Java tmp dir which is normally . You can either remove the  mount option (not recommended) or change the tmpdir CrashPlan is using.

To change the tmpdir CrashPlan uses, open  and insert  to , for example:

 SRV_JAVA_OPTS="-Djava.io.tmpdir=/var/tmp/crashplan -Dfile.encoding=UTF-8 …

Make sure to create the new tmpdir and verify CrashPlan's user has access to it.
 # mkdir /var/tmp/crashplan

Restart CrashPlan.

## Restore stuck preparing
If a restore gets stuck at «Preparing», it may be due to a permission restriction on  that causes communication between the restore tool and backup engine to fail. This can be caused by the sysctl variable  restricting the engine (running as ) from connecting to a named pipe owned by the desktop user contained in  (similar to tmpfs#Opening symlinks in tmpfs as root fails).

The protection can be disabled to permit the restore to occur with

 # sysctl fs.protected_fifos=0

systemd since version 241 sets this option to 1 by default; refer to  the systemd documentation for how to correctly change it, and see Sysctl for more information.

## Out of Memory
For backup sets containing large numbers of files, the default maximum heap size may not be large enough because the memory required scales with the number of files to back up. If the server runs out of memory it will silently restart, and usually get stuck restarting as it continually reaches the memory limit. To increase the heap size limit, adjust the  option in  to a reasonable value for your system.

## Real time protection
If you use real time protection for your backup set and have a lot of files to backup, the default system configuration might not be able to allocate all required handles to follow all files in real time. This issue can manifest itself with logs like "inotify_add_watch: No space left on device" in the syslog journal.
CrashPlan Support has instructions here describing how to modify inotify max_user_watches to a bigger value to fix the issue. You cannot follow their instructions directly though, you need to create a new file in /etc/sysctl.d as /etc/sysctl.conf is now ignored by systemd. See sysctl#Configuration for more information.

## JRE Version Update
If, during upgrade, CrashPlan is attempting to upgrade the self-installed JRE version and the upgrade never gets passed downloading the JRE from CrashPlan (checking in logs/upgrade.log, the last message is a curl/wget for the "latest" JRE tgz), it is possible to stop CrashPlan, download the JRE (from the ugprade log) manually and replace the jre folder in the CrashPlan install with the upgrade version. This should allow CrashPlan to get past being stuck trying to upgrade the JRE.

 $ cd
 $ ./bin/CrashPlanEngine stop
 $ rm -rf jre
 $ curl
 $ tar xzvf
 $ ./bin/CrashPlanEngine start
