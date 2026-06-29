# Very Secure FTP Daemon

vsftpd (Very Secure FTP Daemon) is a lightweight, stable and secure FTP server for UNIX-like systems.

## Installation
Install  and start/enable the  daemon.

To use xinetd for monitoring and controlling vsftpd connections, see #Using xinetd.

## Configuration
Most of the settings in vsftpd are done by editing the file . The file itself is well-documented, so this section only highlights some important changes you may want to modify. For all available options and documentation, see the  man page. Files are served by default from .

Enable connections :

 # Allow all connections
 vsftpd: ALL
 # IP address range
 vsftpd: 10.0.0.0/255.255.255.0

## Enabling uploading
The  flag must be set to YES in  in order to allow changes to the filesystem, such as uploading:

 write_enable=YES

## Local user login
One must set the line  in  to  in order to allow users in  to login:

 local_enable=YES

## Anonymous login
These lines controls whether anonymous users can login. By default, anonymous logins are enabled for download only from :

You may also add e.g. the following options (see  for more):

## Chroot jail
A chroot environment that prevents the user from leaving its home directory can be set up. To enable this, add the following lines to :

 chroot_list_enable=YES
 chroot_list_file=/etc/vsftpd.chroot_list

The  variable specifies the file which contains users that are jailed.

For a more restricted environment, specify the line:

 chroot_local_user=YES

This will make local users jailed by default. In this case, the file specified by  lists users that are not in a chroot jail.

## Limiting user login
It is possible to prevent users from logging into the FTP server by adding two lines to :

 userlist_enable=YES
 userlist_file=/etc/vsftpd.user_list

 now specifies the file which lists users that are not able to login.

If you only want to allow certain users to login, add the line:

 userlist_deny=NO

The file specified by  will now contain users that are able to login.

## Limiting connections
The data transfer rate, i.e. number of clients and connections per IP for local users can be limited by adding the information in :

 local_max_rate=1000000 # Maximum data transfer rate in bytes per second
 max_clients=50         # Maximum number of clients that may be connected
 max_per_ip=2           # Maximum connections per IP

## Using xinetd
Xinetd provides enhanced capabilities for monitoring and controlling connections. It is not necessary though for a basic good working vsftpd-server.

Installation of vsftpd will add a necessary service file, . By default services are disabled. Enable the ftp service:

{{bc|1=
service ftp
{
        socket_type             = stream
        wait                    = no
        user                    = root
        server                  = /usr/bin/vsftpd
        log_on_success  += HOST DURATION
        log_on_failure  += HOST
        disable                 = no
}
}}

If you have set the vsftpd daemon to run in standalone mode make the following change in :

 listen=NO

Otherwise connection will fail:

 500 OOPS: could not bind listening IPv4 socket

Instead of starting the vsftpd daemon start and enable .

## Using SSL/TLS to secure FTP
First, you need a X.509 SSL/TLS certificate to use TLS. If you do not have one, you can easily generate a self-signed certificate as follows:

 # cd /etc/ssl/certs
 # openssl req -x509 -nodes -days 7300 -newkey rsa:2048 -keyout vsftpd.pem -out vsftpd.pem
 # chmod 600 vsftpd.pem

You will be asked questions about your company, etc. As your certificate is not a trusted one, it does not really matter what is filled in, it will just be used for encryption. To use a trusted certificate, you can get one from a certificate authority like Let's Encrypt.

Then, edit the configuration file:

## Resolve hostname in passive mode
To override the IP address vsftpd advertises in passive mode by the hostname of your server and have it DNS resolved at startup, add the following two lines in :

 pasv_addr_resolve=YES
 pasv_address=yourdomain.org

## Port configurations
It may be necessary to adjust the default FTP listening port and the passive mode data ports.  This is a way to resolve traffic when the server is behind a NAT:

* For FTP servers exposed to the web, to reduce the likelihood of the server being attacked, the listening port can be changed to something other than the standard port 21.
* To limit the passive mode ports to open ports, a range can be provided.
The ports can be defined in the configuration file as illustrated below:

## Configuring iptables
Often the server running the FTP daemon is protected by an iptables firewall. To allow access to the FTP server the corresponding port needs to be opened using something like

 # iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 21 -j ACCEPT

This article will not provide any instruction on how to set up iptables but here is an example: Simple stateful firewall.

There are some kernel modules needed for proper FTP connection handling by iptables that should be referenced here. Among those especially nf_conntrack_ftp. It is needed as FTP uses the given listen_port (21 by default) for commands only; all the data transfer is done over different ports. These ports are chosen by the FTP daemon at random and for each session (also depending on whether active or passive mode is used). To tell iptables that packets on ports should be accepted, nf_conntrack_ftp is required. You can explicitly load the module at boot.

If the kernel >= 4.7 you either need to set net.netfilter.nf_conntrack_helper=1 via sysctl e.g.

 # echo net.netfilter.nf_conntrack_helper=1 > /etc/sysctl.d/70-conntrack.conf

or use

 # iptables -A PREROUTING -t raw -p tcp --dport 21 -j CT --helper ftp

## Tips and tricks
## PAM with virtual users
Since PAM no longer provides  another easy method is to use .  This section is however limited to explain how to configure a chroot environment and authentication by .

In this example we create the directory :

 # mkdir /etc/vsftpd

One option to create and store user names and passwords is to use the Apache generator htpasswd:

 # htpasswd -c /etc/vsftpd/.passwd

Replace the  with the user you want to create.

A problem with the above command is that vsftpd might not be able to read the generated MD5 hashed password. If running the same command with the -d switch, crypt() encryption, password become readable by vsftpd, but the downside of this is less security and a password limited to 8 characters. Openssl could be used to produce a MD5 based BSD password with algorithm 1:

 # openssl passwd -1

Whatever solution the produced  should look like this:

 username1:hashed_password1
 username2:hashed_password2
 ...

Next you need to create a PAM service using  and the generated  file. In this example we create a PAM policy for vsftpd with the following content:

Now it is time to create a home for the virtual users. In the example  is decided to host data for virtual users, which also reflects the default directory structure of Arch. First create the general user virtual and make  its home:

 # useradd -d /srv/ftp virtual

Make virtual the owner:

 # chown virtual:virtual /srv/ftp

A basic  with no private folders configured, which will default to the home folder of the virtual user:

 listen=YES
 listen 21
 connect_from_port_20=YES    # sample config file enables it, ftp data
 dirmessage_enable=YES       # sample config data enables it
 xferlog_enable=YES          # sample config data enables it
 pam_service_name=vsftpd     # pointing to the correct PAM service file `/etc/pam.d/vsftpd` rather than `/etc/pam.d/ftp`

 anonymous_enable=NO         # we does not use anonymous mode
 local_enable=YES            # we config virtual user use local privileges, virtual_use_local_privs=YES

 write_enable=YES            # global config, write to filesystem
 hide_ids=YES                # in ftp client interactive console, ls -la: uid=1001 -> ftp

 chroot_local_user=YES       # we do not want user to get the real root(/) directory
 guest_enable=YES            # for virtual user
 guest_username=virtual      # virtual user name: virtual
 virtual_use_local_privs=YES # permission of virtual user=local user

For more detailed meaning of above options, see the  man page.

Some parameters might not be necessary for your own setup. If you want the chroot environment to be writable you will need to add the following to the configuration file:

 allow_writeable_chroot=YES

Otherwise vsftpd because of default security settings will complain if it detects that chroot is writable.

Start .

You should now be able to login from a ftp-client with any of the users and passwords stored in .

## Adding private folders for the virtual users
First create directories for users:

 # mkdir /srv/ftp/user1
 # mkdir /srv/ftp/user2
 # chown virtual:virtual /srv/ftp/user?/

Then, add the following lines to :

 local_root=/srv/ftp/$USER
 user_sub_token=$USER

## Anonymous login as virtual users
We can modify the PAM policy for vsftpd to the following contents, to allow password-free login as virtual user:

## Troubleshooting
## vsftpd: refusing to run with writable root inside chroot()
As of vsftpd 2.3.5, the chroot directory that users are locked to must not be writable. This is in order to prevent a security vulnerabilty.

The safe way to allow upload is to keep chroot enabled, and configure your FTP directories.

 local_root=/srv/ftp/user

 # mkdir -p /srv/ftp/user/upload
 # chmod 550 /srv/ftp/user
 # chmod 750 /srv/ftp/user/upload

If you must:

You can put this into your  to workaround this security enhancement (since vsftpd 3.0.0; from Fixing 500 OOPS: vsftpd: refusing to run with writable root inside chroot ()):

 allow_writeable_chroot=YES

## FileZilla Client: GnuTLS error -8 -15 -110 when connecting via SSL
vsftpd tries to display plain-text error messages in the SSL session. In order to debug this, temporarily disable encryption and you will see the correct error message.Often these errors can be solved by adding[https://bugzilla.redhat.com/show_bug.cgi?id=845980:

## vsftpd.service fails to run on boot
If you have enabled  and it fails to run on boot, edit it and make sure it is set to load after  in the service file:

## Passive mode replies with the local IP address to a remote connection
If vsftpd returns a local address to a remote connection, like:

 227 Entering Passive Mode (192,168,0,19,192,27).

It may be that the FTP server is behind a NAT router and while some devices monitor FTP connections and dynamically replace the local IP address specification by the external IP address for packets containing the PASV response, some do not.

Indicate the external IP address in the vsftpd configuration using:

  pasv_address=externalIPaddress

or alternatively:

 pasv_addr_resolve=YES
 pasv_address=my.domain.name

In case internal connection is not possible after this change, one may need to run 2 vsftpd, one for internal and one for external connections.

## ipv6 only fails with: 500 OOPS: run two copies of vsftpd for IPv4 and IPv6
you most likely have commented out the line

 # When "listen" directive is enabled, vsftpd runs in standalone mode and
 # listens on IPv4 sockets. This directive cannot be used in conjunction
 # with the listen_ipv6 directive.
 #listen=YES
 #
 # This directive enables listening on IPv6 sockets. To listen on IPv4 and IPv6
 # sockets, you must run two copies of vsftpd with two configuration files.
 # Make sure, that one of the listen options is commented !!
 listen_ipv6=YES

instead of setting

 # When "listen" directive is enabled, vsftpd runs in standalone mode and
 # listens on IPv4 sockets. This directive cannot be used in conjunction
 # with the listen_ipv6 directive.
 listen=NO

## vsftpd connections fail on a machine using nis with: yp_bind_client_create_v2: RPC: Unable to send
as mentioned on the vsftpd faq page, "...built-in sandboxing uses network isolation on Linux. This
may be interfering with any module that needs to use the network to perform operations or lookups"

add this undocumented line to your

 isolate_network=NO

## LIST command resets connection
Adding
 seccomp_sandbox=NO
in the  file fixes this issue.

## Hardening
Just like any other service, VSFTPD can be hardened by modifying its systemd unit.
Hardening is also called sandboxing in the literature.
The following sandboxing options are an effective way to limit the exposure of the system towards the unit's processes.

Below is an example of a hardened drop-in file. Adjust the following file to your liking:

This will allow VSFTPD to only write to ,  and to its own log file, and will restrict writing to the rest of the file system. It will also deny access to the entire .
This also restrict any access to . Multiple paths can be specified for this option.

More details on the systemd sandboxing options can be found at .
