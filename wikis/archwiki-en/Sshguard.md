# Sshguard

sshguard is a daemon that protects SSH and other services against brute-force attacks, similar to fail2ban.

sshguard is different from the latter in that it is written in C, is lighter and simpler to use with fewer features while performing its core function equally well.

sshguard is not vulnerable to most (or maybe any) of the log analysis vulnerabilities that have caused problems for similar tools.

## Installation
Install the  package.

## Configuration
sshguard works by monitoring , syslog-ng or the systemd journal for failed login attempts. For each failed attempt, the offending host is banned from further communication for a limited amount of time. The default amount of time the offender is banned starts at 120 seconds, and is increases by a factor of 1.5 every time it fails another login. sshguard can be configured to permanently ban a host with too many failed attempts.

Both temporary and permanent bans are done by adding an entry into the "sshguard" chain in iptables that drops all packets from the offender. The ban is then logged to syslog and ends up in , or the systemd journal if the latter is being used.

You must configure one of the following firewalls to be used with sshguard in order for blocking to work.

## firewalld
sshguard can work with firewalld. Make sure you have firewalld enabled, configured and setup first. To make sshguard write to your zone of preference, issue the following commands:

 # firewall-cmd --permanent --zone=public --add-rich-rule="rule source ipset=sshguard4 drop"

If you use ipv6, you can issue the same command but substitute sshguard4 with sshguard6. Finish with

 # firewall-cmd --reload

You can verify the above with

 # firewall-cmd --info-ipset=sshguard4

Finally, in /etc/sshguard.conf, find the line for BACKEND and change it as follows

## UFW
If UFW is installed and enabled, it must be given the ability to pass along DROP control to sshguard.  This is accomplished by modifying  and  to contain the following lines which should be inserted just after the section for loopback devices.

Restart ufw after making this modification.

## iptables
The main configuration required is creating a chain named , where sshguard automatically inserts rules to drop packets coming from bad hosts:

 # iptables -N sshguard

Then add a rule to jump to the  chain from the  chain. This rule must be added before any other rules processing the ports that sshguard is protecting. Use the following line to protect FTP and SSH or see for more examples.

 # iptables -A INPUT -m multiport -p tcp --destination-ports 21,22 -j sshguard

To save the rules:

 # iptables-save > /etc/iptables/iptables.rules

## nftables
Change the value of  to the following:

When you start/enable the , two new tables named  in the  and  address families are added which filter incoming traffic through sshguard's list of IP addresses. The chains in the  table have a priority of -10 and will be processed before other rules of lower priority. See  and nftables for more information.

## Usage
## systemd
Enable and start .

## syslog-ng
If you have  installed, you may start sshguard directly from the command line instead.

 /usr/sbin/sshguard -l /var/log/auth.log -b /var/db/sshguard/blacklist.db

## Configuration
Configuration is done in  which is required for sshguard to start. A commented example is located at  or can also be found on [https://bitbucket.org/sshguard/sshguard/src/master/examples/sshguard.conf.sample Bitbucket sshguard.conf.sample.

## Blacklisting threshold
By default in the Arch-provided configuration file, offenders become permanently banned once they reach a "danger" level of 120 (or 12 failed logins; see attack dangerousness for more details). This behavior can be modified by prepending a danger level to the blacklist file.

The  in this example tells sshguard to permanently ban a host after achieving a danger level of 200.

Finally, restart .

## Moderate banning example
A slightly more aggressive banning rule than the default one is proposed here to illustrate various options:
* It monitors sshd and vsftpd via logs from the systemd/Journal
* It blocks attackers after 2 attempts (each having a cost of 10, explaining the  value of the  parameter) for 180 seconds with subsequent block time longer by a factor of 1.5. Note that this 1.5 multiplicative delay is internal and not controlled in the settings
* Attackers are permanently blacklisted after 10 attempts (10 attempts having each a cost of 10, explaining the  value in the  parameter)
* It blocks not only the attacker's IP but all the IPv4 subnet 24 (CIDR notation)

## Aggressive banning
For some users under constant attack, a more aggressive banning policy can be adopted. If you are confident that accidental failed logins are unlikely, you can instruct SSHGuard to permanently ban hosts after a single failed login. Modify the parameters in the configuration file in the following way:

Finally restart .

Also, to prevent multiple authentication attempts during a single connection, you may want to change  by defining:

Restart  for this change to take effect.

## Tips and tricks
## Unbanning
If you ban yourself, you can wait to get unbanned automatically or use iptables or nftables to unban yourself.

You will also need to remove the IP address from  in order to make unbanning persistent.

## iptables
First check if your IP is banned by sshguard:

 # iptables --list sshguard --line-numbers --numeric

Then use the following command to unban, with the line-number as identified in the former command:

 # iptables --delete sshguard line-number

## nftables
Remove your IP address from the  set:

 # nft delete element family sshguard attackers { ip_address }

where  is either  or .

## Logging
To see what is being passed to sshguard, examine the script in  and the systemd service . An equivalent command to view the logs in the terminal:

 # journalctl -afb -p info SYSLOG_FACILITY=4 SYSLOG_FACILITY=10
