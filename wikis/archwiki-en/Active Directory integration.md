# Active Directory integration

From Wikipedia:
:Active Directory (AD) is a directory service that Microsoft developed for Windows domain networks.

This article describes how to integrate an Arch Linux system with an existing Windows domain network using Samba.

Before continuing, you must have an existing Active Directory domain, and have a user with the appropriate rights within the domain to: query users and add computer accounts (Domain Join).

This document is not an intended as a complete guide to Active Directory nor Samba. Refer to the resources section for additional information.

## Introduction
This article explains how to configure an Arch Linux system to participate in an Active Directory domain. This article was written and tested on a fresh installation, and it is assumed that all configuration files are in their unmodified, post-installation state. For the duration of the article, the example Active Directory domain will use the following configuration:

* NetBIOS domain name: INTERNAL
* DNS domain name: internal.domain.tld
* Kerberos realm: INTERNAL.DOMAIN.TLD
* First DC: server1.internal.domain.tld with IP address 192.168.1.1
* Second DC: server2.internal.domain.tld with IP address 192.168.1.2

In most small networks, the DCs (domain controllers) also hold the DNS server role. This may not be true in larger networks. Generally, DCs also hold the NTP role, but not always. Consult your network administrator to verify correct values for DNS and NTP servers.

## Needed software
In order to use samba effectively, you will need to install the following packages: , , and . (timedatectl can be used as an alternative to ntp.)

Additionally, while not required, the following packages will be useful for testing and troubleshooting: , , and if a printing is desired (whether you want to share printers, or use printers on another Samba/Windows host), .

## Initial configuration of services
## DNS configuration
Active Directory depends entirely on DNS for name resolution. It is imperative that the  file is configured with both the correct DNS servers and a domain search suffix. Whether configured via DHCP or static configuration, ensure that these values are correct for your domain. For the example domain configuration, the following contents are appropriate (be sure to replace 192.168.1.1, 192.168.1.2, and internal.domain.tld with appropriate values for your network):

If you elected to install the  package, you can test DNS configuration with the following commands (be sure to replace server1 and internal.domain.tld with appropriate values for your network):

 $ nslookup -type=SRV _kerberos._tcp.internal.domain.tld.
 $ nslookup -type=SRV _ldap._tcp.internal.domain.tld.
 $ nslookup server1.internal.domain.tld.

You should get output similar to the following (adjust appropriately for only one DC, or more than two):

 Server:        192.168.1.1
 Address:       192.168.1.1#53

 _kerberos._tcp.internal.domain.tld service = 0 100 88 server1.internal.domain.tld.
 _kerberos._tcp.internal.domain.tld service = 0 100 88 server2.internal.domain.tld.
 ...
 _ldap._tcp.internal.domain.tld     service = 0 100 389 server1.internal.domain.tld.
 _ldap._tcp.internal.domain.tld     service = 0 100 389 server2.internal.domain.tld.
 ...
 Name:   server1.internal.domain.tld
 Address: 192.168.1.1

## NTP configuration
In an Active Directory domain, more specifically for Kerberos ticketing, it is imperative that time is synchronized with all other hosts on the network. A margin of error no more than five minutes is required. For the example domain configuration, an appropriate  file should have the following contents (be sure to replace server1, server2, and internal.domain.tld with appropriate values for your network):

Enable and start the  unit.

## Kerberos configuration
The Samba documentation recommends a minimal Kerberos configuration, with just enough information in the section to hand off the work of discovering domain details to DNS. Unfortunately, this does not work well in practice. Continuing with the example domain configuration, modify the  file with the following contents (be sure to replace instances of INTERNAL, internal.domain.tld, SERVER1, and INTERNAL.DOMAIN.TLD''' with appropriate values for your network):

{{hc|/etc/krb5.conf|
[libdefaults
   default_realm = INTERNAL.DOMAIN.TLD
   dns_lookup_realm = false
   dns_lookup_kdc = true

INTERNAL.DOMAIN.TLD = {
      kdc = SERVER1.INTERNAL.DOMAIN.TLD
      default_domain = INTERNAL.DOMAIN.TLD
      admin_server = SERVER1.INTERNAL.DOMAIN.TLD
   }
   INTERNAL = {
      kdc = SERVER1.INTERNAL.DOMAIN.TLD
      default_domain = INTERNAL.DOMAIN.TLD
      admin_server = SERVER1.INTERNAL.DOMAIN.TLD
   }

[domain_realm
    .internal.domain.tld = INTERNAL.DOMAIN.TLD

pam = {
        ticket_lifetime = 1d
        renew_lifetime = 1d
        forwardable = true
        proxiable = false
        minimum_uid = 1
    }

}}

## Samba configuration
## Base Samba configuration file
A default installation of  does not ship with an example  file. For our example domain configuration, use the following base settings (replace instances of INTERNAL and INTERNAL.DOMAIN.TLD with appropriate values for your network):

If you do not wish to share local printers configured in , then add the following to the [Global section of the  file:

The remainder of the configuration depends on whether your domain supports RFC2307 Unix/NFS Attributes. Consult with your domain administrator if unsure.

## Adding the idmap configuration for domains with RFC2307 extensions
Be certain that the values below do not overlap with system values, and that all users have at least the uidNubmer attribute, and that those users' PrimaryGroup has a gid attribute. Append to the following to the section of the  file (replace INTERNAL with the NetBIOS domain name):

Additionally, if user accounts in AD have a gidNumber attribute, you can use it instead of the RID for the user's Primary Group by appending the following setting (again in the [Global section):

## Adding the idmap configuration for domains without RFC2307 extensions
If your administrator has not extended the AD schema to include the RFC2307 attributes, use the following idmap configuration in the section of the  file (replace INTERNAL with the NetBIOS domain name):

## Joining the domain
To join the AD domain, simply issue the following command (be sure to replace Administrator with a user that has privileges to join the AD domain).

 # net ads join -U Administrator

## Start the individual Samba services
Enable and start the , , and  services.

## Configure NSS
Modify the  file to allow Samba to map names to uid and gid:

## Testing NSS
Verify connectivity by listing the AD domain users and groups that system is aware of:

 # wbinfo -u
 # wbinfo -g

You should get a list of AD users followed by AD groups.

## Configuring PAM authentication
Rather than configuring options directly in the Linux-PAM configuration files, set defaults for the pam_winbind module in :

For most services, it will be sufficient to modify only the  file. Any configuration for programs that do not include this file will also need to be modified directly. Create a backup of the  file and use the following configuration:

If you have other services that do not include the  file, modify the configuration to mirror all pam_unix.so entries for pam_winbind.so and  change all required to sufficient. A good example is the su configuration. Create a backup of the  file and use the following in its place:

The above pam_winbind configuration will not use the default location of the Kerberos ticket (), which is at . Instead, it stores the automatically refreshed Kerberos ticket to . Append the following to your krb5.conf to let Kerberos know your new location:
{{hc|/etc/krb5.conf|
[libdefaults
   ...
   default_ccache_name = /run/user/%{uid}/krb5cc
   ...}}

To test your changes, start a new console or ssh session (do not exit your existing session until you have tested thoroughly) and try to login using the AD credentials. The domain name is optional, as this was set in the Winbind configuration as 'default realm'.  Please note that in the case of ssh, you will need to modify the  file to allow kerberos authentication (see below).

Run klist to verify that you have received a kerberos ticket. You should see something similar to:

Finally, you should test login as both the root user and a local unprivileged user before logging out of your existing (working) session.

## Old Wiki Article
Active Directory serves as a central location for network administration and security. It is responsible for authenticating and authorizing all users and computers within a Windows domain network, assigning and enforcing security policies for all computers in a network and installing or updating software on network computers. For example, when a user logs into a computer that is part of a Windows domain, it is Active Directory that verifies their password and specifies whether they are a system administrator or normal user. Server computers on which Active Directory is running are called domain controllers.

Active Directory uses Lightweight Directory Access Protocol (LDAP) versions 2 and 3, Microsoft's version of Kerberos and DNS.

## Terminology
If you are not familiar with Active Directory, there are a few keywords that are helpful to know.

* Domain : The name used to group computers and accounts.
* SID : Each computer that joins the domain as a member must have a unique SID or System Identifier.
* SMB : Server Message Block.
* NETBIOS: Network naming protocol used as an alternative to DNS. Mostly legacy, but still used in Windows Networking.
* WINS: Windows Information Naming Service. Used for resolving Netbios names to windows hosts.
* Winbind: Protocol for windows authentication.

## Active Directory configuration
This section works with the default configuration of Windows Server 2012 R2.

## GPO considerations
Digital signing is enabled by default in Windows Server, and must be enabled at both the client and server level. For certain versions of Samba, Linux clients may experience issues connecting to the domain and/or shares. It is recommended you add the following parameters to your  file:

 client signing = auto
 server signing = auto

If that is not successful, you can disable Digital Sign Communication (Always) in the AD group policies. In your AD Group Policy editor, locate:

Under Local policies > Security policies > Microsoft Network Server > Digital sign communication (Always) activate define this policy and use the disable radio button.

If you use Windows Server 2008 R2, you need to modify that in GPO for Default Domain Controller Policy > Computer Setting > Policies > Windows Setting > Security Setting > Local Policies > Security Option > Microsoft network client: Digitally sign communications (always).

Please note that disabling this GPO affects the security of all members of the domain.

## Linux host configuration
The next few steps will begin the process of configuring the Host. You will need root or sudo access to complete these steps.

## Installation
Install the following packages:
* , see also Samba
*
*  or , see also NTPd or OpenNTPD

## Updating DNS
Active Directory is heavily dependent upon DNS. You will need to update  to use one or more of the Active Directory domain controllers:

Replacing  and  with valid IP addresses for the AD servers. If your AD domains do not permit DNS forwarding or recursion, you may need to add additional resolvers.

## Configuring NTP
Read System time#Time synchronization to configure an NTP service.

On the NTP servers configuration, use the IP addresses for the AD servers, as they typically run NTP as a service. Alternatively, you can use other known NTP servers provided the Active directory servers sync to the same stratum.

Ensure that the service is configured to sync the time automatically very early on startup.

## Kerberos
Let us assume that your AD is named example.com. Let us further assume your AD is ruled by two domain controllers, the primary and secondary one, which are named PDC and BDC, pdc.example.com and bdc.example.com respectively. Their IP adresses will be 192.168.1.2 and 192.168.1.3 in this example.  Take care to watch your syntax; upper-case is very important here.

{{hc|/etc/krb5.conf|
default_realm 	= 	EXAMPLE.COM
	clockskew 	= 	300
	ticket_lifetime	=	1d
        forwardable     =       true
        proxiable       =       true
        dns_lookup_realm =      true
        dns_lookup_kdc  =       true

[realms
	EXAMPLE.COM = {
		kdc 	= 	PDC.EXAMPLE.COM
        kdc     =   PDC2.EXAMPLE.COM
        admin_server = PDC.EXAMPLE.COM
		admin_server = PDC2.EXAMPLE.COM
        default_domain = EXAMPLE.COM
	}

.kerberos.server = EXAMPLE.COM
	.example.com = EXAMPLE.COM
	example.com = EXAMPLE.COM
	example	= EXAMPLE.COM

[appdefaults
	pam = {
	ticket_lifetime 	= 1d
	renew_lifetime 		= 1d
	forwardable 		= true
	proxiable 		= false
	retain_after_close 	= false
	minimum_uid 		= 0
	debug 			= false
	}

default 		= FILE:/var/log/krb5libs.log
	kdc 			= FILE:/var/log/kdc.log
        admin_server            = FILE:/var/log/kadmind.log
}}

## Creating a Kerberos ticket
Now you can query the AD domain controllers and request a kerberos ticket (uppercase is necessary):

 kinit administrator@EXAMPLE.COM

You can use any username that has rights as a Domain Administrator.

## Validating the Ticket
Run klist to verify you did receive the token. You should see something similar to:

## pam_winbind.conf
If you get errors stating that /etc/security/pam_winbind.conf was not found, create the file and add the following:

With this setup, winbind will create user keytabs on the fly (krb5_ccache_type = FILE) at login and maintain them.  You can verify this by simply running klist in a shell after logging in as an AD user but without needing to run kinit.  You may need to set additional permissions on /etc/krb5.keytab eg 640 instead of 600 to get this to work (see  for example)

## Samba
Samba is a free software re-implementation of the SMB/CIFS networking protocol. It also includes tools for Linux machines to act as Windows networking servers and clients.

In this section, we will focus on getting Authentication to work first by editing the 'Global' section first. Later, we will go back and add shares.

## Join the domain
You need an AD Administrator account to do this. Let us assume this is named Administrator. The command is 'net ads join'

## Starting and testing services
## Starting Samba
Hopefully, you have not rebooted yet! Fine. If you are in an X-session, quit it, so you can test login into another console, while you are still logged in.

Enable and start the individual Samba daemons , , and .

Next we will need to modify the NSSwitch configuration, which tells the Linux host how to retrieve information from various sources and in which order to do so. In this case, we are appending Active Directory as additional sources for Users, Groups, and Hosts.

## Testing Winbind
Let us check if winbind is able to query the AD. The following command should return a list of AD users:

* Note we created an Active Directory user called 'test.user' on the domain controller

We can do the same for AD groups:

## Testing nsswitch
To ensure that our host is able to query the domain for users and groups, we test nsswitch settings by issuing the 'getent' command.

The following output shows what a stock Arch Linux install looks like:

And for groups:

## Testing Samba commands
Try out some net commands to see if Samba can communicate with  AD:

## Configuring PAM
Now we will change various rules in PAM to allow Active Directory users to use the system for things like login and sudo access.  When changing the rules, note the order of these items and whether they are marked as required or sufficient is critical to things working as expected. You should not deviate from these rules unless you know how to write PAM rules.

In case of logins, PAM should first ask for AD accounts, and for local accounts if no matching AD account was found. Therefore, we add entries to include  into the authentication process.

The Arch Linux PAM configuration keeps the central auth process in . Starting with the stock configuration from , change it like this:

## system-auth
## "auth" section
Find the line:

 auth required pam_unix.so ...

Delete it, and replace with:

 auth [success=1 default=ignore pam_localuser.so
 auth default=die pam_winbind.so
 auth default=die pam_unix.so nullok
 auth requisite pam_deny.so

## "account" section
Find the line:

 account required pam_unix.so

Keep it, and add this below:

 account default=ignore pam_localuser.so
 account required pam_winbind.so

## "password" section
Find the line:

 password required pam_unix.so ...

Delete it, and replace with:

 password default=ignore pam_localuser.so
 password default=die pam_winbind.so
 password default=die pam_unix.so sha512 shadow
 password requisite pam_deny.so

## "session" section
Find the line:

 session required pam_unix.so

Keep it, and add this line immediately above it:

 session required pam_mkhomedir.so skel=/etc/skel/ umask=0022

Below the pam_unix line, add these:

 session default=ignore pam_localuser.so
 session required pam_winbind.so

## passwd
## "password" section
In order for logged-in Active Directory users to be able to change their passwords with the  'passwd' command, the file  must include the information from system-auth.

Find the line:

 password required pam_unix.so sha512 shadow nullok

Delete it, and replace with:

 password include system-auth

## Testing login
Now, start a new console session (or ssh) and try to login using the AD credentials. The domain name is optional, as this was set in the Winbind configuration as 'default realm'.  Please note that in the case of ssh, you will need to modify the  file to allow kerberos authentication .

Both should work. You should notice that  will be automatically created.
Log into another session using an linux account. Check that you still be able to log in as root - but keep in mind to be logged in as root in at least one session!

## Configuring Shares
Earlier we skipped configuration of the shares. Now that things are working, go back to , and add the exports for the host that you want available on the windows network.

In the above example, the keyword NETWORK is to be used. Do not mistakenly substitute this with your domain name. For adding groups, prepend the '@' symbol to the group. Note that  is encapsulated in quotes so Samba correctly parses it when reading the configuration file.

## Adding a machine keytab file and activating password-free kerberized ssh to the machine
This explains how to generate a machine keytab file which you will need e.g. to enable password-free kerberized ssh to your machine from other machines in the domain. The scenario in mind is that you have a bunch of systems in your domain and you just added a server/workstation using the above description to your domain onto which a lot of users need to ssh in order to work - e.g. GPU workstation or an OpenMP compute node, etc. In this case you might not want to type your password every time you log in. On the other hand the key authentication used by many users in this case can not give you the necessary credentials to e.g. mount kerberized NFSv4 shares. So this will help you to enable password-free logins from your clients to the machine in question using kerberos ticket forwarding.

## Creating a machine key tab file
run 'net ads keytab create -U administrator' as root to create a machine keytab file in /etc/krb5.keytab. It will prompt you with a warning that we need to enable keytab authentication in our configuration file, so we will do that in the next step. In my case it had problems when a key tab file is already in place - the command just did not come back it hang ... In that case you should rename the existing /etc/krb5.keytab and run the command again - it should work now.

verify the content of your keytab by running:

## Enabling keytab authentication
Now you need to tell winbind to use the file by adding these lines to the /etc/samba/smb.conf:

  kerberos method = secrets and keytab
  dedicated keytab file = /etc/krb5.keytab

It should look something like this:

Restart the

Check if everything works by getting a machine ticket for your system by running

This should not give you any feedback but running 'klist' should show you sth like:

Some common mistakes here are a) forgetting the trailing $ or b) ignoring case sensitivity - it needs to look exactly like the entry in the keytab (usually you cannot to much wrong with all capital)

## Preparing sshd on server
Add these options to the  and restart  after making the changes.

## Adding necessary options on client
First we need to make sure that the tickets on our client are forwardable. This is usually standard but we better check anyways. You have to look for the  option and set it to 'true' in the Kerberos configuration file:

Secondly we need to add the following options to the user-specific SSH client configuration file to tell  to use these options - alternatively they can be invoked using the  options directly.

## Testing the setup
On Client:

make sure you have a valid ticket - if in doubt run 'kinit'

then use ssh to connect to you machine

 $ ssh myarchlinux.example.com

you should get connected without needing to enter your password.

if you have key authentication additionally activated then you should perform

 $ ssh -v myarchlinux.example.com

to see which authentication method it actually uses.

For debugging you can enable DEBUG3 on the server and look into the journal using journalctl.

## Nifty fine-tuning for complete password-free kerberos handling.
In case your clients are not using domain accounts on their local machines (for whatever reason) it can be hard to actually teach them to kinit before ssh to the workstation. Therefore I came up with a nice workaround:

## Generating user Keytabs which are accepted by AD
On a system let the user run:

Now test the file by invoking:

 $ kinit username@EXAMPLE.COM -kt username.keytab

It should not prompt you to give your password nor should it give any other feedback. If it worked you are basically done - just put the line above into e.g your shell configuration file - you can now get kerberos tickets without typing a password and with that you can connect to your workstation without typing a password while being completely kerberized and able to authenticate against NFSv4 and CIFS via tickets.

## Nice to know
The file 'username.keytab' is not machinespecific and can therefore be copied around. E.g. we created the files on a linux machine and copied them to our Mac clients as the commands on Macs are different ...

## Using SSSD
 can be used instead of Samba to integrate with AD. See SSSD documentation.

## Commercial solutions
* Centrify
* Likewise

## OpenSource version
* PowerBroker Identity Services Open: formerly Likewise acquired by BeyondTrust
* Centrify Express for Linux
