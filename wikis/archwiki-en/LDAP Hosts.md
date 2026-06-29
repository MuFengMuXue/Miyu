# LDAP Hosts

This document will allow you to put your /etc/hosts into your LDAP server. At first make sure you have an LDAP server up and running (take LDAP authentication as an introduction). Next you need to create a proper ldif file from /etc/hosts. Actually mine is like:

Where 127.0.0.1 is localhost (of course), 192.168.1.1 is the LDAP server, followed by at least 3 workstation (gamera, iris & zedan). For a ldif file you need to create a ou for your hosts and each host (I will call the next file hosts.ldif):

Next put the file into your LDAP server with your credentials (output truncated):

If everything filled up then edit your /etc/nss_ldap.conf and change the line beginning with nss_base_hosts to the following:

Now change the /etc/hosts in that way that only localhost, the LDAP server and the own name of the workstation exist. An example how it could look on the workstation gamera:

On the LDAP server you can ignore every workstation. Finally you need to edit the hosts entry in your /etc/nsswitch.conf:

Now test your configuration:

The first 3 lines are from /etc/hosts, the last 4 lines are from your LDAP server. Finally to get ping working with LDAP you need to start nscd:
