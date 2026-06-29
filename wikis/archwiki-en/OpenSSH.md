# OpenSSH

OpenSSH (OpenBSD Secure Shell) is a set of computer programs providing encrypted communication sessions over a computer network using the Secure Shell (SSH) protocol. It was created as an open source alternative to the proprietary Secure Shell software suite offered by SSH Communications Security. OpenSSH is developed as part of the OpenBSD project, which is led by Theo de Raadt.

OpenSSH is occasionally confused with the similarly-named OpenSSL; however, the projects have different purposes and are developed by different teams, the similar name is drawn only from similar goals.

## Installation
Install the  package.

## Client usage
To connect to a server, run:

 $ ssh -p port user@server-address

If the server only allows public-key authentication, follow SSH keys.

## Configuration
The client can be configured to store common options and hosts. All options can be declared globally or restricted to specific hosts. For example:

With such a configuration, the following commands are equivalent

 $ ssh -p port user2@server-address
 $ ssh myserver

See  for more information.

Some options do not have command line switch equivalents, but you can specify configuration options on the command line with . For example .

## Server usage
 is the OpenSSH server daemon, configured with  and managed by . Whenever changing the configuration, use  in test mode before restarting the service to ensure it will be able to start cleanly. Valid configurations produce no output.

 # sshd -t

## Configuration
To allow access only for some users, add this line:

 AllowUsers    user1 user2

To allow access only for some groups:

 AllowGroups   group1 group2

To add a nice welcome message (e.g. from the  file), configure the  option:

 Banner /etc/issue

Public and private host keys are automatically generated in  by the sshdgenkeys service and regenerated if missing even if  option in  allows only some. Three key pairs are provided based on the algorithms ed25519, ecdsa and rsa. To have sshd use a particular key, specify the following option:

 HostKey /etc/ssh/ssh_host_ed25519_key

If the server is to be exposed to the WAN, it is recommended to change the default port from 22 to a random higher one like this:
 Port 39901

## Daemon management
Start/enable . It will keep the SSH daemon permanently active and fork for each incoming connection.

## Socket activation
 8.0p1-3 removed  that used systemd's socket activation due to it being susceptible to denial of service. See  for details. If  is enabled when updating to  8.0p1-3, the  and  units will be copied to  and reenabled. This is only done to not break existing setups; users are still advised to migrate to .

Using  negates the  setting, so it will allow connections over any address. To achieve the effect of setting , you must specify the port and IP for  (e.g. ) by editing . You must also add  under  or else setting the IP address will have the same drawback as setting : the socket will fail to start if the network is not up in time.

When using socket activation, a transient instance of  will be started for each connection (with different instance names). Therefore, neither  nor the daemon's regular  allow to monitor connection attempts in the log. The logs of socket-activated instances of SSH can be seen by running  as root or by running  as root.

## Protection
Allowing remote log-on through SSH is good for administrative purposes, but can pose a threat to your server's security. Often the target of brute force attacks, SSH access needs to be limited properly to prevent third parties gaining access to your server.

 offers an automated analysis of server and client configuration.  Several other good guides and tools are available on the topic, for example:

* Article by Mozilla Infosec Team
* SSH Hardening Guides

## Force public key authentication
If a client cannot authenticate through a public key, by default, the SSH server falls back to password authentication, thus allowing a malicious user to attempt to gain access by brute-forcing the password. One of the most effective ways to protect against this attack is to disable password logins entirely, and force the use of SSH keys. This can be accomplished by setting the following options in the daemon configuration file:

## Two-factor authentication and public keys
SSH can be set up to require multiple ways of authentication; you can tell which authentication methods are required using the  option. This enables you to use public keys as well as a two-factor authorization.

## Authentication providers
See Google Authenticator to set up Google Authenticator.

For Duo, install  which will supply the  module. Read the Duo Unix documentation for instructions on how to setup the necessary Duo credentials (Integration Key, Secret Key, API Hostname).

## PAM setup
To use PAM with OpenSSH, edit the following files:

Then you can log in with either a publickey or the user authentication as required by your PAM setup.

If, on the other hand, you want to authenticate the user on both a publickey and the user authentication as required by your PAM setup, use a comma instead of a space to separate the AuthenticationMethods:

With required pubkey and pam authentication, you may wish to disable the password requirement:

## Protecting against brute force attacks
Brute forcing is a simple concept: one continuously tries to log in to a webpage or server log-in prompt like SSH with a high number of random username and password combinations.

See ufw#Rate limiting with ufw or Simple stateful firewall#Bruteforce attacks for iptables.

Since 9.8 a basic protection similar to fail2ban is implemented: the option  is set with reasonable default values. Penalties for various conditions are enforced against a client on its source address, resulting in a refused connection for a time period.

Alternatively, you can protect yourself from brute force attacks by using an automated script that blocks anybody trying to brute force their way in.
* Only allow incoming SSH connections from trusted locations
* Use fail2ban or sshguard to automatically block IP addresses that fail password authentication too many times.
* Use pam_shield to block IP addresses that perform too many login attempts within a certain period of time. In contrast to fail2ban or sshguard, this program does not take login success or failure into account.

## Limit root login
It is generally considered bad practice to allow the root user to log in without restraint over SSH. There are two methods by which SSH root access can be restricted for increased security.

## Deny
Sudo selectively provides root rights for actions requiring these without requiring authenticating against the root account. This allows locking the root account against access via SSH and potentially functions as a security measure against brute force attacks, since now an attacker must guess the account name in addition to the password.

SSH can be configured to deny remote logins with the root user by editing the "Authentication" section in the daemon configuration file. Simply set  to :

Next, restart the SSH daemon.

You will now be unable to log in through SSH under root, but will still be able to log in with your normal user and use su or sudo to do system administration.

## Restrict
Some automated tasks such as remote, full-system backup require full root access. To allow these in a secure way, instead of disabling root login via SSH, it is possible to only allow root logins for selected commands. This can be achieved by editing , by prefixing the desired key, e.g. as follows:

 command="rrsync -ro /" ssh-ed25519 ...

This will allow any login with this specific key only to execute the command specified between the quotes.

The increased attack surface created by exposing the root user name at login can be compensated by adding the following to :

 PermitRootLogin forced-commands-only

This setting will not only restrict the commands which root may execute via SSH, but it will also disable the use of passwords, forcing use of public key authentication for the root account.

A slightly less restrictive alternative will allow any command for root, but makes brute force attacks infeasible by enforcing public key authentication. For this option, set:

 PermitRootLogin prohibit-password

## Locking the authorized_keys file
If, for whatever reason, you think that the user in question should not be able to add or change existing keys, you can prevent them from manipulating the file.

On the server, make the  file read-only for the user and deny all other permissions:

 $ chmod 400 ~/.ssh/authorized_keys

To prevent the user from simply changing the permissions back, set the immutable bit on the  file. To prevent the user from renaming the  directory and creating a new  directory and  file, set the immutable bit on the  directory too. To add or remove keys, you will have to remove the immutable bit from  and make it writable temporarily.

## SSH certificates
While common SSH keys and manual fingerprint verification may be easy to use with a handful of hosts that are managed by a single administrator, this method of authentication does not scale at all. When a number of servers need to be accessed through SSH by several users, manually verifying ssh public key fingerprints of every host becomes nearly impossible to do securely and reliably.

The solution for this is to use SSH certificates that provide automatic verification of public key identities through a chain of trust that scales significantly better than the default trust-on-first-use approach of SSH. SSH certificates are basically nothing else than normal public SSH keys, but with an additional signature from a trusted certificate authority that verifies the key identity.

## Create a host certificate authority key for your infrastructure
 $ ssh-keygen -t ed25519 -f ~/.ssh/ca_host_key -C 'Host certificate authority for *.example.com'

The private certificate authority key should be stored securely, ideally on a smartcard or hardware token that prevents key extraction like the Nitrokey or YubiKey.

## Sign a server's public SSH host key
Copy the public server key to your local system containing the private certificate authority key to sign it:

 $ ssh-keygen -h -s ~/.ssh/ca_key -I certLabel -n server01.example.com ./ssh_host_ed25519_key.pub

## Move the new certificate and configure sshd to use it
The generated certificate  should be copied to the server at .

## Configure all clients to trust the certificate authority
## SSH user certificates
Depending on the number of users and method of deployment, SSH User keys can also be used with Certificates. For organizations with many ssh users, this is strongly advised to manage User key deployment securely.

The deployment of user certificates works basically the same as for server identities. More details and instructions can be found at Wikibooks:OpenSSH/Cookbook/Certificate-based Authentication.

## Certificate deployment automation
Automated deployment of SSH certificates can be provided by a number of open source tools. Popular examples are:

* Ansible - openssh_cert module
* privacyIDEA - authentication server
* Theo App - authorized keys manager

## SSHFP record
The Secure Shell fingerprint record (SSHFP) is an optional resource record in the domain name system that associates SSH keys to a host name. It can be used to verify the SSH fingerprint on public servers via DANE instead of deploying trusted CA certificates, which allows even unmanaged clients to verify the validity of key fingerprints.

## Generate record entry
To generate the required hexadecimal key fingerprint to be stored in the DNS record, create the hash on the target server.

 $ ssh-keygen -r host.example.com

This will read all available SSH keys for the specified domain and output valid SSHFP records that can then be stored in the DNS entries of the affected domain.

## Client configuration
In order to automatically retrieve and trust SSH key fingerprints stored as SSHFP records, add the following to your ssh client configuration file:

If the target host has a valid SSHFP record and this record is verified with a valid DNSSEC signature, the fingerprint is automatically accepted without prompting the user to verify the hosts identity. In case the DNS record is not verified by DNSSEC, the user will be prompted to verify the fingerprint instead as usual.

## Generate SSHFP records
To determine the SSH fingerprint of a specific domain, use ssh-keyscan to retrieve the ssh fingerprints in a valid DNS record format. (Note that by default fingerprints for every available key type is provided as both SHA1 and SHA256.)

Since the SSHFP record stores the key fingerprints as hexadecimal values while the common output for SSH fingerprints is the base64 encoded SHA256 hash of the public key, it is necessary to convert the record back to the base64 format in order to compare it with values in the known_hosts file or other documentation that commonly stores fingerprints as SHA256.

 $ echo "SSHFP-fingerprint" | xxd -r -p | base64

Example for github.com using the hex value for the sha256 fingerprint of the key type ed25519

Compare with known_hosts entries:

 $ ssh-keygen -l -f ~/.ssh/known_hosts

## Manually retrieve SSHFP records from DNS
 $ dig SSHFP targetdomain.tld +short

## Tips and tricks
## Encrypted SOCKS tunnel
This can be useful for laptop users connect to unsafe wireless connections. The only requirement is an SSH server running at a somewhat secure location, like your home or at work. It might be useful to use a dynamic DNS service like DynDNS so you do not have to remember your IP address.

## Start the connection
 $ ssh -TND 4711 user@host

The  flag disables the interactive prompt, and the  flag specifies the local port on which to listen on (you can choose any port number).  The  flag disables pseudo-tty allocation.

Perhaps add the verbose () flag, to verify the connection.

## Configure your browser (or other programs)
The above step is useful only in combination with a web browser or another program. Since SSH supports both SOCKS v4 and SOCKS v5, you can use either.

* For Firefox:
# Go to Preferences > General > Network Settings and click on Settings....
# In the new  window, check the Manual proxy configuration option and enter  in the SOCKS host text field, and the port number in the Port text field ( in the example above).
# Restart Firefox.
:
* For Chromium:
# You can set the SOCKS settings as environment variables or as command line options. For example, add one of the following functions to your : {{bc|
secure_chromium() {
    local port=4711
    export SOCKS_SERVER=localhost:$port
    export SOCKS_VERSION=5
    (chromium > /dev/null 2>&1 &)
}

secure_chromium() {
    local port=4711
    (chromium --proxy-server="socks://localhost:$port" > /dev/null 2>&1 &)
}
}}
# Open a terminal and run:

## Set up a local TUN interface
This is more complicated initially, but results in you not having to manually configure every application to use the SOCKS proxy. It requires setting up a local TUN interface and routing traffic through it.

See VPN over SSH#Set up badvpn and tunnel interface.

## X11 forwarding
X11 forwarding is a mechanism that allows graphical interfaces of X11 programs running on a remote system to be displayed on a local client machine. For X11 forwarding the remote host does not need to have a full X11 system installed; however, it needs at least to have xauth installed. xauth is a utility that maintains  configurations used by server and client for authentication of X11 session (source).

## Setup
## Remote
* install the  packages
* in :
** set  to yes
** verify that  and  options are set to yes, and that  is set to 10 (those are the default values if nothing has been changed, see )
* then restart the sshd daemon.

## Client
* install the  package
* enable the  option by either specifying the  switch on the command line for opportunistic connections, or by setting  to yes in the client's configuration.

## Usage
Log on to the remote machine normally, specifying the  switch if ForwardX11 was not enabled in the client's configuration file:

 $ ssh -X user@host

If you receive errors trying to run graphical applications, try ForwardX11Trusted instead:

 $ ssh -Y user@host

Given the output , redo the setup for your remote machine. Once the X11 forwarding request succeeds, you can start any X program on the remote server, and it will be forwarded to your local session:

 $ xclock

Error output containing  indicates that  is improperly set.

Be careful with some applications as they check for a running instance on the local machine. Firefox is an example: either close the running Firefox instance or use the following start parameter to start a remote instance on the local machine:

 $ firefox --no-remote

If you get "X11 forwarding request failed on channel 0" when you connect (and the server  shows "Failed to allocate internet-domain X11 display socket"), make sure package  is installed. If its installation is not working, try to either:

* enable the  option in  on the server, or
* set the  option in  on the server to inet.
Setting it to inet may fix problems with Ubuntu clients on IPv4.

For running X applications as another user on the SSH server, you need to  the authentication line taken from  of the SSH logged in user.

## Forwarding other ports
In addition to SSH's built-in support for X11, it can also be used to securely tunnel any TCP connection, by use of local forwarding or remote forwarding.

Local forwarding opens a port on the local machine, connections to which will be forwarded to the remote host and from there on to a given destination. Very often, the forwarding destination will be the same as the remote host, thus providing a secure shell and, e.g. a secure VNC connection, to the same machine. Local forwarding is accomplished by means of the  switch and it is accompanying forwarding specification in the form of .

Thus:

 $ ssh -L 1000:mail.google.com:25 192.168.0.100

will use SSH to login to and open a shell on , and will also create a tunnel from the local machine's TCP port 1000 to mail.google.com on port 25. Once established, connections to  will connect to the Gmail SMTP port. To Google, it will appear that any such connection (though not necessarily the data conveyed over the connection) originated from , and such data will be secure between the local machine and 192.168.0.100, but not between  and Google, unless other measures are taken.

Similarly:

 $ ssh -L 2000:192.168.0.100:6001 192.168.0.100

will allow connections to  which will be transparently sent to the remote host on port 6001. The preceding example is useful for VNC connections using the vncserver utility--part of the tightvnc package--which, though very useful, is explicit about its lack of security.

Remote forwarding allows the remote host to connect to an arbitrary host via the SSH tunnel and the local machine, providing a functional reversal of local forwarding, and is useful for situations where, e.g., the remote host has limited connectivity due to firewalling. It is enabled with the  switch and a forwarding specification in the form of .

Thus:

 $ ssh -R 3000:irc.libera.chat:6667 192.168.0.200

will bring up a shell on , and connections from  to itself on port 3000 (the remote host's ) will be sent over the tunnel to the local machine and then on to irc.libera.chat on port 6667, thus, in this example, allowing the use of IRC programs on the remote host to be used, even if port 6667 would normally be blocked to it.

Both local and remote forwarding can be used to provide a secure "gateway", allowing other computers to take advantage of an SSH tunnel, without actually running SSH or the SSH daemon by providing a bind-address for the start of the tunnel as part of the forwarding specification, e.g. . The  can be any address on the machine at the start of the tunnel. The address  allows connections via the  or loopback interface, and an empty address or  allow connections via any interface. By default, forwarding is limited to connections from the machine at the "beginning" of the tunnel, i.e. the  is set to . Local forwarding requires no additional configuration; however, remote forwarding is limited by the remote server's SSH daemon configuration. See the  option in  and  option in  for more information about remote forwarding and local forwarding, respectively.

## Jump hosts
In certain scenarios, there might not be a direct connection to your target SSH daemon, and the use of a jump server (or bastion server) is required. Thus, we attempt to connect together two or more SSH tunnels, and assuming your local keys are authorized against each server in the chain. This is possible using SSH agent forwarding () and pseudo-terminal allocation () which forwards your local key with the following syntax:

 $ ssh -A -t -l user1 bastion1 \
   ssh -A -t -l user2 intermediate2 \
   ssh -A -t -l user3 target

This can be automated with the ProxyCommand option:

 $ ssh -o ProxyCommand="ssh -W %h:%p bastion.example.org" targetserver.example.org

An easier and more secure way to do this is using the ProxyJump option with the  flag:

 $ ssh -J user1@bastion1,user2@intermediate2 user3@target

Multiple hosts in the  directive can be separated with a comma; they will be connected to in the order listed. The  part is not required, but can be used. The host specifications for  use the ssh configuration file, so specific per-host options can be set there, if needed.

The main difference between the ProxyCommand and ProxyJump options is that the later does not require a shell on the jumphost. Consequently, this also means that the jumpserver does not require access to the users login credentials or SSH agent forwarding. With the ProxyJump option, the ssh client connects through the jumpserver directly to the target server, establishing an end-to-end encrypted channel between client and target server.

An equivalent of the  flag in the configuration file is the  option; see  for details.

## Reverse SSH through a relay
The idea is that the client connects to the server via another relay while the server is connected to the same relay using a reverse SSH tunnel. This is useful when the server is behind a NAT, and the relay is a publicly accessible SSH server used as a proxy to which the user has access. Therefore, the prerequisite is that the client's keys are authorized against both the relay and the server, and the server needs to be authorized against the relay as well for the reverse SSH connection.

The following configuration example assumes that  is the user account used on client,  on relay and  on server. First, assuming we will use port 2222, the server needs to establish the reverse tunnel with:

 $ ssh -R 2222:localhost:22 -N user2@relay

Which can also be automated with a startup script, systemd service, autossh or .

At the client side, the connection is established with:

 $ ssh -t user2@relay ssh user3@localhost -p 2222

The remote command to establish the connection to reverse tunnel can also be defined in relay's  file by including the  field as follows:

In this case the connection is established with:

 $ ssh user2@relay

Alternatively, you can add an entry to your ssh configuration that specifies both  and :

Which will reduce connecting to:

 $ ssh jump-destination

## Multiplexing
The SSH daemon usually listens on port 22. However, it is common practice for many public internet hotspots to block all traffic that is not on the regular HTTP/S ports (80 and 443, respectively), thus effectively blocking SSH connections. The immediate solution for this is to have  listen additionally on one of the whitelisted ports:

However, it is likely that port 443 is already in use by a web server serving HTTPS content, in which case it is possible to use a multiplexer, such as , which listens on the multiplexed port and can intelligently forward packets to many services.

## Speeding up SSH
There are several client configuration options which can speed up connections either globally or for specific hosts. See  for full descriptions of these options.

* Use a faster cipher: on modern CPUs with AESNI instructions,  and  should offer significantly better performance over openssh's default preferred cipher, usually . Cipher can be selected with the  flag. For a permanent effect, put  option in your  with ciphers in new preferred order, e.g.:

* Enable or disable compression: compression can increase speed on slow connections; it is enabled with the  option or the  flag. However, the compression algorithm used is the relatively slow  which becomes the bottleneck on fast networks. In order to speed up the connection, one should use the  option on local or fast networks.

* Connection sharing: you can make all sessions to the same host share a single connection using these options:
: where  can be any directory not writable by other users.

*  specifies how long the master should wait in the background for new clients after the initial client connection has been closed. Possible values are either:
**  to close the connection immediately after the last client disconnects,
** a time in seconds,
**  to wait forever, the connection will never be closed automatically.

* Login time can be shortened by bypassing IPv6 lookup using the  option or  flag.

* Last, if you intend to use SSH for SFTP or SCP, High Performance SSH/SCP can significantly increase throughput by dynamically raising the SSH buffer sizes. Install the package  to use a patched version of OpenSSH with this enhancement.

## Mounting a remote filesystem with SSHFS
Please refer to the SSHFS article to mount a SSH-accessible remote system to a local directory, so you will be able to do any operation on the mounted files with any tool (copy, rename, edit with vim, etc.). sshfs is generally preferred over shfs, the latter has not been updated since 2004.

## Keep alive
By default, the SSH session automatically logs out if it has been idle for a certain time. To keep the session up, the client can send a keep-alive signal to the server if no data has been received for some time, or symmetrically the server can send messages at regular intervals if it has not heard from the client.

* On the server side,  sets the timeout in seconds after which if no data has been received from the client, sshd will send a request for response. The default is 0, no message is sent. For example to request a response every 60 seconds from the client, set the  option in your server configuration. See also the  and  options.
* On the client side,  controls the interval between the requests for response sent from the client to the server. For example to request a response every 120 seconds from the server, add the  option to your client configuration. See also the  and  options.

## Automatically restart SSH tunnels with systemd
systemd can automatically start SSH connections on boot/login and restart them when they fail. This makes it a useful tool for maintaining SSH tunnels.

The following service can start an SSH tunnel on login using the connection settings in your ssh configuration. If the connection closes for any reason, it waits 10 seconds before restarting it:

Then enable and start the user unit. See #Keep alive for how to prevent the tunnel from timing out. If you wish to start the tunnel on boot, you might want to rewrite the unit as a system service.

## Autossh - automatically restarts SSH sessions and tunnels
When a session or tunnel cannot be kept alive, for example due to bad network conditions causing client disconnections, you can use  to automatically restart them.

Usage examples:

 $ autossh -M 0 -o "ServerAliveInterval 45" -o "ServerAliveCountMax 2" username@example.com

Combined with SSHFS:

 $ sshfs -o reconnect,compression=yes,transform_symlinks,ServerAliveInterval=45,ServerAliveCountMax=2,ssh_command='autossh -M 0' username@example.com: /mnt/example

Connecting through a SOCKS-proxy set by Proxy settings:

 $ autossh -M 0 -o "ServerAliveInterval 45" -o "ServerAliveCountMax 2" -NCD 8080 username@example.com

With the  option autossh can be made to run as a background process. Running it this way however means the passphrase cannot be entered interactively.

The session will end once you type  in the session, or the autossh process receives a SIGTERM, SIGINT of SIGKILL signal.

## Run autossh automatically at boot via systemd
If you want to automatically start autossh, you can create a systemd unit file:

Here  is an environment variable specifying how long ssh must be up before autossh considers it a successful connection, setting it to 0 autossh also ignores the first run failure of ssh. This may be useful when running autossh at boot. Other environment variables are available at . Of course, you can make this unit more complex if necessary (see the systemd documentation for details), and obviously you can use your own options for autossh, but note that the  implying  does not work with systemd.

Remember to start and/or enable the service afterwards.

You may also need to disable :

 ExecStart=/usr/bin/autossh -M 0 -o ControlMaster=no -NL 2222:localhost:2222 -o TCPKeepAlive=yes foo@bar.com

## Alternative service should SSH daemon fail
For remote or headless servers which rely exclusively on SSH, a failure to start the SSH daemon (e.g., after a system upgrade) may prevent administration access. systemd offers a simple solution via  option.

Let us suppose the server runs  and telnet is the fail-safe alternative of choice. Create a file as follows. Do not enable !

That's it. Telnet is not available when  is running. Should  fail to start, a telnet session can be opened for recovery.

## Terminal background color based on host
To better distinguish when you are on different hosts, you can set a different background color based on the kind of host.

This solution works, but is not universal (ZSH only).

## Network specific configuration
You can use host configuration specific to the network you are connected to using a .

For example, when using , and the connection is configured (manually or through DHCP) to use a search-domain:

Another example for : Consider that connecting to  requires a bastion/proxy (via ) unless you are already connected via VPN. The fragment  applies only when  cannot be looked up via DNS. Various alternatives are discussed at === Private networks hostkeys verification ===

Because different servers on different networks are likely to share a common private IP address, you might want to handle them differently.

The best solution is to use the #Network specific configuration to use a different  depending on the network you are on. The second solution, best used as default when you are working on new/prototype networks, would be to simply ignore hostkeys for private networks:

## Run command at login
If you are using an interactive session, there are multiple ways to execute a command on login:

* use the  file on the remote host (see ).
* use  on the remote host if the server has enabled the  option.
* use your shell configuration file on the remote host.  and similar environment variables can be used for detecting a SSH session, see .

## Agent forwarding
SSH agent forwarding allows you to use your local keys when connected to a server. It is [https://security.stackexchange.com/questions/7480/risks-of-ssh-to-an-untrusted-host#7504 recommended to only enable agent forwarding for selected hosts.

Next, configure an SSH agent and add your local key with ssh-add.

If you now connect to a remote server you will be able to connect to other services using your local keys.

## Generating new keys
New server private keys can be generated by:

# Deleting all the keys, e.g.:
# Restarting  or running  as root.

A more graceful alternative is to transition. First, generate the new host keys:

Add both old and new keys to :

Restart .

Clients will learn the host's new key fingerprints and add them to  the next time they connect to the server.

After a while, the old keys can be removed from , leaving only the new keys:

Restart , then physically remove the old keys:

{{bc|
# rm /etc/ssh/ssh_host_{ecdsa,ed25519,rsa}_key
}}

Again, clients will automatically adjust  to remove fingerprints corresponded to the old keys.

## Run sshd as non-privileged user
You may want to run  as non-privileged user in containers, or for testing, etc.

Since non-privileged user cannot read host keys in , new host keys must be generated:

 $ ssh-keygen -q -N "" -t rsa -b 4096 -f /path/to/host/keys/ssh_host_rsa_key
 $ ssh-keygen -q -N "" -t ecdsa -f /path/to/host/keys/ssh_host_ecdsa_key
 $ ssh-keygen -q -N "" -t ed25519 -f /path/to/host/keys/ssh_host_ed25519_key

Create an  file. The example below uses a port higher than 1024, provides a new path to the host keys and disables PAM:

Run sshd with the created config. The  flag disables daemon mode and  redirects output to stderr to allow easy monitoring.

 $ sshd -f /path/to/sshd_config -D -e

## Troubleshooting
## Checklist
Check these simple issues before you look any further.

# The configuration directory , its contents should be accessible only by the user (check this on both the client and the server), and the user's home directory should only be writable by the user:
# Check that the client's public key (e.g. ) is in  on the server.
# Check that you did not limit SSH access with  or  in the server config.
# Check if the user has set a password. Sometimes new users who have not yet logged in to the server do not have a password.
# Append  to .
# Run  as root for possible (error) messages.
# Restart  and logout/login on both client and server.

## Connection refused or timeout problem
## Port forwarding
If you are behind a NAT mode/router (which is likely unless you are on a VPS or publicly addressed host), make sure that your router is forwarding incoming ssh connections to your machine. Find the server's internal IP address with  and set up your router to forward TCP on your SSH port to that IP. portforward.com can help with that.

## Is SSH running and listening?
The ss utility shows all the processes listening to a TCP port with the following command line:

 $ ss --tcp --listening

If the above command do not show the system is listening to the port , then SSH is not running: check the journal for errors etc.

## Are there firewall rules blocking the connection?
Iptables may be blocking connections on port . Check this with:

and look for rules that might be dropping packets on the  chain. Then, if necessary, unblock the port with a command like:

For more help configuring firewalls, see firewalls.

## Is the traffic even getting to your computer?
Start a traffic dump on the computer you are having problems with:

 # tcpdump -lnn -i any port ssh and tcp-syn

This should show some basic information, then wait for any matching traffic to happen before displaying it. Try your connection now. If you do not see any output when you attempt to connect, then something outside of your computer is blocking the traffic (e. g., hardware firewall, NAT router etc.).

## Your ISP or a third party blocking default port?
In some cases, your ISP might block the default port (SSH port 22) so whatever you try (opening ports, hardening the stack, defending against flood attacks, et al) ends up useless. To confirm this, create a server on all interfaces (0.0.0.0) and connect remotely.

If you get an error message comparable to this:

 ssh: connect to host www.inet.hr port 22: Connection refused

That means the port is not being blocked by the ISP, but the server does not run SSH on that port (See security through obscurity).

However, if you get an error message comparable to this:

 ssh: connect to host 111.222.333.444 port 22: Operation timed out

That means that something is rejecting your TCP traffic on port 22. Basically that port is stealth, either by your firewall or 3rd party intervention (like an ISP blocking and/or rejecting incoming traffic on port 22). If you know you are not running any firewall on your computer, and you know that Gremlins are not growing in your routers and switches, then your ISP is blocking the traffic.

To double check, you can run Wireshark on your server and listen to traffic on port 22. Since Wireshark is a Layer 2 Packet Sniffing utility, and TCP/UDP are Layer 3 and above (see IP Network stack), if you do not receive anything while connecting remotely, a third party is most likely to be blocking the traffic on that port to your server.

## Diagnosis
Install either  or Wireshark with the  package.

For tcpdump:

 # tcpdump -ni interface "port 22"

For Wireshark:

 $ tshark -f "tcp port 22" -i interface

where  is the network interface for a WAN connection (see  to check). If you are not receiving any packets while trying to connect remotely, you can be very sure that your ISP is blocking the incoming traffic on port 22.

## Possible solution
The solution is just to use some other port that the ISP is not blocking. Open the  and configure the file to use different ports. For example, add:

 Port 22
 Port 1234

Also make sure that other "Port" configuration lines in the file are commented out. Just commenting "Port 22" and putting "Port 1234" will not solve the issue because then sshd will only listen on port 1234. Use both lines to run the SSH server on both ports.

Restart the server  and you are almost done. You still have to configure your client(s) to use the other port instead of the default port. There are numerous solutions to that problem, but let us cover two of them here.

## Read from socket failed: connection reset by peer
Recent versions of OpenSSH sometimes fail with the above error message when connecting to older ssh servers. This can be worked around by setting various client options for that host. See  for more information about the following options.

The problem could be the  elliptical host key algorithms. These can be disabled by setting  to a list excluding those algorithms. On the client side, the  that the client wants to use can also be set by preceding the  list with a  to remove the specified algorithms (including wildcards) from the default set (see ).
You can check the actually used host key algorithm with  in the line that contains .

If that does not work, it could be that the list of ciphers is too long. Set the  option to a shorter list (fewer than 80 characters should be enough). Similarly, you can also try shortening the list of .

See also the discussion on the OpenSSH bug forum.

## "shell: No such file or directory" / ssh_exchange_identification problem
One possible cause for this is the need of certain SSH clients to find an absolute path (one returned by , for instance) in , even if the shell's binary is located in one of the  entries.

## "Terminal unknown" or  "Error opening terminal" error message
If you receive the above errors upon logging in, this means the server does not recognize your terminal. ncurses applications like nano may fail with the message .

The correct solution is to install the client terminal's terminfo file on the server. This tells console programs on the server how to correctly interact with your terminal. You can get info about current terminfo using  and then find out which package owns it.

If you cannot install it normally, you can copy your terminfo to your home directory on the server:

 $ ssh myserver mkdir -p  ~/.terminfo/${TERM:0:1}
 $ scp /usr/share/terminfo/${TERM:0:1}/$TERM myserver:~/.terminfo/${TERM:0:1}/

After logging in and out from the server the problem should be fixed.

## TERM hack
Alternatively, you can simply set  in your environment on the server (e.g. in ). This will silence the error and allow ncurses applications to run again, but you may experience strange behavior and graphical glitches unless your terminal's control sequences exactly match xterm's.

## Connection closed by x.x.x.x
If you are seeing this error in your sshd logs, make sure you have set a valid :

## subsystem request failed
Since OpenSSH 8.8, scp uses SFTP as the default protocol for data transfers by requesting the subsystem named . If you run scp in verbose mode, , you can determine which subsystem your client is using (e.g. ). Errors such as  may be fixed by configuring the server's Subsystem settings: . The server configuration should resemble the example below.

## id_dsa refused
OpenSSH 7.0 deprecated DSA public keys for security reasons and OpenSSH 9.8 is built without support for DSA keys by default. The first OpenSSH release of 2025 will remove DSA support entirely. For now, if you absolutely must use them, you will need to rebuild  while passing  to .[https://marc.info/?l=openssh-unix-dev&m=171982945528949&w=2

## No matching key exchange method found by OpenSSH 7.0
OpenSSH 7.0 deprecated the diffie-hellman-group1-sha1 key algorithm because it is weak and within theoretical range of the so-called Logjam attack (see https://www.openssh.com/legacy.html). If the key algorithm is needed for a particular host, ssh will produce an error message like this:

 Unable to negotiate with 127.0.0.1: no matching key exchange method found.
 Their offer: diffie-hellman-group1-sha1

The best resolution for these failures is to upgrade/configure the server to not use deprecated algorithms. If that is not possible, you can force the client to reenable the algorithm with the client option .

## tmux/screen session killed when disconnecting from SSH
Paraphrased from a unix stackexchange answer:

If your processes are killed at the end of the ssh session, it is possible that you are using socket activation. Your process is killed by  when it notices that the SSH session process exited. In that case there are two solutions:

* Avoid using socket activation by migrating to  (recommended, see #Socket activation), or
* Set  in the  section of .

Though not necessary, setting  in  may also be useful as it avoids killing the SSH session process and its  or  process when the server is stopped or restarted.

Note the caveat that this may not work with .

## SSH session stops responding
SSH responds to flow control commands  and . It will freeze/hang/stop responding when you hit . Use  to resume your session.

## Broken pipe
If you attempt to create a connection which results in a  response for , you should reattempt the connection in debug mode and see if the output ends in error:

The  line above indicates that the reply packet was never received. So, it follows that this is a QoS issue. To decrease the likely-hood of a packet being dropped, set :

The  () type-of-service should resolve the issue, as well as  and  ().

## Terminate unresponsive SSH connection
If a client session is no longer responding and cannot be terminated by instructing the running program (e.g. shell), you can still terminate the session by pressing ,  and  one after another in that order.

The  is a pseudo-terminal escape character (see ), which can be added multiple times depending on the client session to terminate. For example, if you connected from A to B and then from B to C and the session from B to C freezes, you can terminate it by pressing  and typing , which will leave you in a working session on B.

## WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
If the client warns that the key of an ssh server has changed, you should verify that the newly offered key really belongs to the server operator via an authenticated (not necessarily encrypted) channel. Then remove the old key from the  file with  and accept the new key as if it was a new server.

## Connecting to a remote without the appropriate terminfo entry
When connecting to hosts that do not have a terminfo entry for your terminal, for example, when using a terminal emulator whose terminfo entry is not shipped with  (e.g. kitty and rxvt-unicode), or when connecting to hosts with a limited terminfo database (e.g. systems running OpenWrt), various issues will occur with software that relies on .

A proper solution is to place the appropriate terminfo entry on the host. If that is not feasible, an alternative is to set  to a value that is both supported by the remote host and compatible with the terminal.

Since OpenSSH 8.7, a custom  environment variable can be passed to remote hosts with a simple configuration snippet:

## Connection through jump host fails with "bash: No such file or directory"
If you do not have the  environment variable set to a full valid path (on the jump server), connection will fail with an error message simmilar to this one:

 bash: No such file or directory
 kex_exchange_identification: Connection closed by remote host
 Connection closed by UNKNOWN port 65535

You can simply solve this by setting your  to a full path name of a shell that will also be valid on the jump server or by setting a specific  variable for each server in your  file.
