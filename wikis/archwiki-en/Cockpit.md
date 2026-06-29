# Cockpit

Cockpit is a browser-based administration tool for Linux, sponsored by Red Hat.

## Installation
Install the  package. Check the optional dependencies to see what packages are required to manage network connections, packages and hard disks.

For additional features, install one of the following packages:

*  for managing virtual machines using libvirt
*  for managing Podman containers (replaces the deprecated cockpit-docker)
*  for configuring and monitoring storage, disks and mounts on the system.
*  for managing system packages.
*  for managing Networking.
*  for managing the Firewall using the Cockpit in Networking.
*  for managing Storage.
*  for reading PCP metrics and loading PCP archives.

## Usage
Start/enable the  unit to start Cockpit Visit https://localhost:9090/ in a web browser to use Cockpit. Log in with your Linux account and password.

## Configuration
## TLS certificate
By default, Cockpit uses a self-signed TLS certificate. To use a proper certificate, put a certificate with suffix  and a corresponding key with suffix  in the  directory. Cockpit will use the last  file in that folder, in alphabetical order, falling back on . The cert and key have to be readable by the cockpit-ws user. Restart  to apply. See [https://cockpit-project.org/guide/latest/https.html the page in the official docs for more information.

## Limit network access to the interface to local address only
By default, Cockpit listen on all network interfaces () on port 9090, for security reasons, one may want to limit the exposition of the interface to a specific one only or change the default port.

For example, for the interface to listen only on the local address, create a drop-in file:

Alternatively, you can use a unix domain socket instead of IP:Port binding, by setting the ListenStream to a path of your choice like , to be then used in a web server with reverse proxy capabilities.

Be aware, the Cockpit login MOTD should be disabled in this case, as the presented text will no longer be relevant to you.

See the page in the official docs for more information.

## Hide login MOTD
By default, Cockpit shows a MOTD on either TTY login or SSH.  recommends creating a symbolic link to hide these messages, but simply removing the files will also work:

 # rm /etc/motd.d/cockpit /etc/issue.d/cockpit.issue

To avoid pacman re-creating the original files when  is upgraded, create a NoExtract rule.

To avoid cockpit re-creating cockpit.issue on reboot, override ExecStart of cockpit-issue.service with /usr/bin/true.
