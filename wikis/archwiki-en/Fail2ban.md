# Fail2ban

Fail2ban scans log files (e.g. ) and bans IPs that show the malicious signs like too many authentication attempts, scanning for vulnerabilities, etc. Generally Fail2ban is then used to update firewall rules to reject the IP addresses for a specified amount of time, although any other arbitrary action (e.g. sending an email) could also be configured.

## Installation
Install the  package.

## Usage
Configure Fail2ban and enable/start .

## fail2ban-client
The fail2ban-client allows monitoring jails (reload, restart, status, etc.), to view all available commands:

 $ fail2ban-client

To view all enabled jails:

 # fail2ban-client status

To check the status of a jail, e.g. for sshd:

For a compact version for all jails, including banned IPs:

{{hc|# fail2ban-client banned|
['192.168.100.50'}, {'apache-auth': }}

## Configuration
Due to the possibility of Pacnew and Pacsave files being created for  during an upgrade,  recommends that users create a  file to "ease upgrades".

For example, to change the default ban time to 1 day:

Or create separate  files under the  directory, e.g. .

Reload  to apply the configuration changes.

## Enabling jails
By default all jails are disabled. Append  to the jail you want to use, e.g. to enable the OpenSSH jail:

See #Custom SSH jail.

## Receive an alert e-mail
If you want to receive an e-mail when someone has been banned, you have to configure an SMTP client (e.g. msmtp) and change default action, as given below.

## Firewall and services
By default, Fail2ban uses iptables. However, configuration of most firewalls and services is straightforward. For example, to use nftables:

See  for other examples, e.g. [https://github.com/fail2ban/fail2ban/blob/master/config/action.d/ufw.conf ufw.conf.

## Tips and tricks
## Custom SSH jail
Edit , add this section and update the list of trusted IP addresses in :

## systemd backend: journald filtering
When using the systemd backend to improve performance, configure a filter with . For example, to parse only kernel-level log messages:

See also .

## Service hardening
Currently, Fail2ban must be run as root. Therefore, you may wish to consider hardening the process with systemd.

Create a drop-in file for :

The  parameters  will allow Fail2ban full read access to every directory and file.  and  allow Fail2ban to operate on any firewall that has command-line shell interface. See  for more info.

By using  the filesystem hierarchy will only be read-only,  allows Fail2ban to have write access on required paths.

Finally, do a daemon-reload to apply the changes of the unit and restart .
