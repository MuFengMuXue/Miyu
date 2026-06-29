# FreeIPA

FreeIPA is an open-source Identity, Policy and Audit (IPA) suite, sponsored by Red Hat, which provides services similar to Microsoft's Active Directory

## Manual configuration as IPA client
Make sure your clocks are synchronized. Kerberos will not work otherwise. NTP is recommended.

Instead of using  script for automated client configuration and enrollment, the following sections describe a manual procedure for enrolling the client  to the FreeIPA server  in the  domain.

## Configure SSSD and Kerberos
Follow the LDAP auth instructions to setup SSSD. Use a SSSD configuration similar to the following, substituting the requisite fields:

Configure pam in similar way to LDAP, replacing  with .

Create an  file for your domain:

{{hc|/etc/krb5.conf|2=
default_realm = EXAMPLE.COM
        dns_lookup_realm = false
        dns_lookup_kdc = false
        rdns = false
        ticket_lifetime = 24h
        forwardable = yes
        #allow_weak_crypto = yes  # Only if absolutely necessary. Currently FreeIPA supports strong crypto.

[realms
        EXAMPLE.COM = {
                admin_server = freeipaserver.example.com
                kdc = freeipaserver.example.com:749
                default_admin = example.com
        }

example.com = EXAMPLE.COM
        .example.com = EXAMPLE.COM

[logging
        default = FILE:/var/log/krb5libs.log
        kdc = FILE:/var/log/krb5kdc.log
        admin_server = FILE:/var/log/kadmin.log
}}

## Enroll the client
On FreeIPA server, add the client to the IPA server (From Fedora documentation):
# Login and request and admin session
# Create a host entry  if the host does not have a static IP, use
# Set the client to be managed by IPA
# Generate keytab for the client

Install the keytab on the client:
 $ scp user@ipaserver.example.com:/tmp/client1.keytab krb5.keytab
 # mv krb5.keytab /etc/krb5.keytab

## SSH integration
## authorized_keys
You can configure SSHD to fetch users SSH public key from the LDAP directory by uncommenting those lines in :

 AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys
 AuthorizedKeysCommandUser nobody

Then restart .

You can add your ssh key to your FreeIPA user account through the web interface or use the  argument to the  or  commands.

Test it:

 $ sudo -u nobody sss_ssh_authorizedkeys

You should see your ssh public key on standard output and no error message on standard error.

## known_hosts
You can configure SSH to fetch hosts public key information from their directory entries in FreeIPA by adding those lines in :

 GlobalKnownHostsFile /var/lib/sss/pubconf/known_hosts
 ProxyCommand /usr/bin/sss_ssh_knownhostsproxy -p %p %h

## Kerberos/GSS API Authentication
You can enabled Kerberos / GSS API Authentication for the SSH Client to FreeIPA member hosts by uncommenting and changing the following lines in :

 GSSAPIAuthentication yes
 GSSAPIDelegateCredentials yes
