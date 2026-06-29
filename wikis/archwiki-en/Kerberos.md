# Kerberos

Kerberos is a network authentication system. See krb5 documentation.

## Installation
Install the  package on your clients and server.

It is highly recommended to use a time synchronization daemon to keep client/server clocks in sync.

If hostname resolution has not been configured, you can manually add your clients and server to the  file of each machine. Note that the FQDN (myclient.example.com) must be the first hostname after the IP address in the hosts file.

## Server configuration
## Domain creation
Edit  to configure your domain:

{{hc|/etc/krb5.conf|
default_realm = EXAMPLE.COM

[realms
    EXAMPLE.COM = {
        admin_server = $ADDRESS
        # use "kdc = ..." if the kerberos SRV records aren't in DNS (see Advanced section)
        kdc = $ADDRESS
        # This breaks krb4 compatibility but increases security
        default_principal_flags = +preauth
    }

example.com  = EXAMPLE.COM
    .example.com = EXAMPLE.COM

[logging
    kdc          = SYSLOG:NOTICE
    admin_server = SYSLOG:NOTICE
    default      = SYSLOG:NOTICE
}}
Where  is IP address or domain name, where kerberos lives, like  or .

This file's format is described in the MIT Kerberos documentation

Create the database:

Finally, start/enable  and .

## Add principals
Start the Kerberos administration tool, using local authentication

Add a user principal to the Kerberos database:

Add the KDC principal to the Kerberos database:

Finally, Add the KDC principal to the server's keytab:

Quit the Kerberos administration tool:

 kadmin.local: quit

You should now be able to get a Kerberos ticket:

## Firewall
Add ALLOW rules to your firewall for any applicable ports/protocols:
* 88, TCP and UDP for Kerberos v5
* 749, TCP and UDP for kadmin if you plan to configure it
* 750, TCP and UDP for Kerberos v4 if you need backwards compatibility

## DNS records
This is not necessary if you specify the kerberos and kadmin server in each machine's krb5.conf

Do not forget reverse DNS.

## Client configuration
Edit the client's  to match your server's configuration. You can copy this file from the server, or just set the required realm information.

## Testing
You should now be able to get a Kerberos ticket on the client:

## Configuring kadmin
You will need /etc/krb5.conf configured on the kadmin client, and the server's firewall configured for kadmin.

## Configuring kadmin ACL
Create a principal for administration:

Add the user to the kadmin ACL file:

This file's format is described in the MIT Kerberos documentation

Configure kdc.conf:
{{hc|/var/lib/krb5kdc/kdc.conf|
kdc_ports = 750,88

[realms
    EXAMPLE.COM = {
        database_name = /var/lib/krb5kdc/principal
        acl_file = /var/lib/krb5kdc/kadm5.acl
        key_stash_file = /var/lib/krb5kdc/.k5.EXAMPLE.COM
        kdc_ports = 750,88
        max_life = 10h 0m 0s
        max_renewable_life = 7d 0h 0m 0s
    }
}}
This file's format is described in the MIT Kerberos documentation

Restart  and .

You can now use kadmin as your own user, authenticating with kerberos:

## Service principals and keytabs
First, ensure you have configured krb5.conf on all involved machines.

A kerberos principal has three components, formatted as `primary/instance@REALM`. For user principals, the primary is your username and the instance is omitted or is a role (eg. "admin"): `myuser@EXAMPLE.COM` or `myuser/admin@EXAMPLE.COM`. For hosts, the primary is "host" and the instance is the server FQDN: `host/myserver.example.com@EXAMPLE.COM`. For services, the primary is the service abbreviation and the instance is the FQDN: `nfs/myserver.example.com@EXAMPLE.COM`.
The realm can often be omitted, the local computer's default realm is usually assumed.

## With remote kadmin
This is the easier method, but requires you to have configured kadmin.

Open kadmin as root (so we can write the keytab) on the client, authenticating with your admin principal:

Add a principal for any services you will be using, eg. "host" for SSH authentication or "nfs" for NFS:

Save each key to the local keytab:

## Without remote kadmin
Start kadmin on the Kerberos server, using either unix or kerberos authentication:

Add a principal for any services you will be using, eg. "host" for SSH authentication or "nfs" for NFS:

Save each key to a new keytab to be transferred to the client:

Finally, copy  from the server to the client using SCP or similar, then put it in place with correct permissions:

Finally, delete kbclient.keytab from the server and client.

## Cross-Realm Trust
Set up a second server as shown above, then create the cross-realm principal on both KDCs. Cross-realm principals must be created with strong passwords, not , and the same password must be used on both KDCs. The principal must have the same key version number (kvno) in both KDCs.

To grant EXAMPLE.COM principals access to EXAMPLE.ORG resources, you would use the following principal:
 kadmin# addprinc krbtgt/EXAMPLE.ORG@EXAMPLE.COM
The  section of  can be used to further control cross-realm trust relationships.

## SSH authentication
Use the instructions in Service principals and keytabs to create a principal for the "host" service for both client and server, then put the client's keys in the client's keytab and the server's keys in the server's keytab.

Modify your SSH server configuration to enable GSSAPI authentication:

And modify your client configuration to send GSSAPI requests:

Get a ticket-granting ticket on the client before using ssh:

Pass the -v option to ssh to watch what's happening:

And you should now see a host ticket on the client:

## Authorize other principals
To allow a different kerberos principal to authenticate to a user account, add the principal name to the target account's  file. For example, to allow  to SSH to alice's account:

## NFS security
First, configure your NFS server. Also see NFS/Troubleshooting. Configuring a time synchronization daemon on both the clients and the server is strongly recommended. Clock drift will cause this to break, and the error message will not be helpful.

Use the instructions in #Service principals and keytabs to create a principal for the "nfs" service for both client and server, then put the client's keys in the client's keytab and the server's keys in the server's keytab.

## NFS server
Add a Kerberos export option. If necessary, multiple options can be specified using a colon as a delimiter with the preferred setting first, e.g. .

*  uses kerberos for authentication, integrity, and encryption.
*  uses kerberos for authentication and integrity checking, but still transmits data unencrypted.
*  uses kerberos for authentication only, and transmits the data unauthenticated and unencrypted.
*  is the default and does not provide any cryptographic security.

And reload the exports:

 # exportfs -arv

## NFS client
Mount the exported directory:

 # mount nfsserver:/srv/export /mnt/

You can add  for verbose information, and may need  and  or your chosen security option.

Check that it worked with the  command:

## Browsers
Some browsers have support for Kerberos protocol but disable it by default. Here are the instructions how to enable it:

## Chromium
Chromium needs to be run with a command line parameter that specifies a list of sites where Kerberos authentication is allowed. The easiest way is to add persistent flag to the configuration file:

{{hc|/etc/chromium/policies/managed/test_policy.json|
{
  "AuthServerAllowlist": "*.mycompany.com",
  "DisableAuthNegotiateCnameLookup": true
}
}}

## Firefox
To configure Firefox with trusted sites visit  and set  property to FOO.COM (Note: for Firefox there is no "*."; for Chrome, there is).

## Troubleshooting
## Cannot set GSSAPI authentication names
 Cannot set GSSAPI authentication names, aborting

Your realm is missing either the  or  principal.

For clients, invalid arguments/options may happen on first setup if rpc-gssd is not loaded. Loading it is usually acomplished by enabling and starting , but after first setup this target will need a restart.

## SSH authentication fails while connecting to a server requiring GSSAPI with KeyExchange
If any of the following errors are encountered:

 $ ssh -v -o GSSAPIDelegateCredentials=yes -o GSSAPIAuthentication=yes @
 Unable to negotiate with  port 22: no matching key exchange method found. Their offer: gss-group14-sha1-...

 $ ssh -v -o GSSAPIDelegateCredentials=yes -o GSSAPIKeyExchange=yes -o GSSAPIAuthentication=yes @
 command-line: line 0: Bad configuration option: gssapikeyexchange

it means that package  is not configured with GSSAPI patch for OpenSSH. You can install  or follow this example.
