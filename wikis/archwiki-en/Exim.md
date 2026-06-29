# Exim

Exim is a versatile mail transfer agent. This article builds upon Mail server. While the Exim wiki provides some helpful how-tos on certain specific use cases, a detailed description of all configuration options is available as well.

## Installation
Install the  package.

## Basic configuration
Exim comes with a bulky default configuration file which is located in . Many options in there are not necessary in a regular use case.

Configuration can be done in a single file containing several chapters. Exim’s configuration is divided into a number of different parts. General option settings must always appear before any other part. The other parts are all optional, and may appear in any order. Each part, other than the one for the general options, is introduced by the word “begin” followed by at least one literal space, and the name of the part. Other general comments about exim runtime configuration are given by this link to the official documentation.

Below is a very basic configuration, which provides: local delivers to system users, Mbox (also referred as traditional BSD mailbox) format, and authorized relaying to MX hosts. The description is based on a domain "mydomain.tld" served on a host "hostname.mydomain.tld". It is highly recommended to consult the official documentation before using the given documentation below.

## Main parameters
The required general options chapter contains some basic options. Using solely those options would open ports for connections but still no mail would be accepted nor relayed anywhere.

## TLS, security & authentication
To obtain a certificate, see OpenSSL#Usage.

The first part of the following options are still part of the first configuration section in Exim. Starting with "begin authenticators", the first special section of the suggested configuration here  begins. There will be other sections later.
Below some very basic security related options are defined, TLS is set up & a plain text authenticator using a user password lookup is introduced.

{{bc|
# actually not required: it's hard coded - anyway: no mail delivery to root
never_users = root

# don't show the exim version to everyone. Actually not even show the name.
smtp_banner = $smtp_active_hostname ESMTP $tod_full

# STARTTLS is offered to everyone
tls_advertise_hosts	= *
tls_certificate = /path/to/exim/only/fullchain.pem
tls_privatekey = /path/to/exim/only/privkey.pem

# use all ciphers on port 25, use only good ciphers on port 587
tls_require_ciphers = ${if =={$received_port}{25} \
				{DEFAULT} {HIGH:!MD5:!SHA1:!SHA2}}

# traffic on port 465 always uses TLS
tls_on_connect_ports = 465

# special sections always start with a "begin"
begin authenticators

	PLAIN:
		# authentication protocol is plain text
		driver = plaintext
		# authentication is offered as plain text
		public_name = PLAIN
		server_prompts = :
		# authentication is successful, if the password provided ($auth3)
		# equals the password found in a lookup file for user ($auth2)
		server_condition = ${if eq{$auth3}{${lookup{$auth2}dbm{/etc/authpwd}}}}
		server_set_id = $auth2
		# only offer plain text authentication after TLS is been negotiated
		server_advertise_condition = ${if def:tls_in_cipher}
}}

## Routing, transport & retry
For each recipient of a message routing is performed as follows: routers are tested in their order given in the routing section. For each router, conditions may apply (e.g. ). Only if all conditions apply, the message will be handed over to the defined transport (e.g. ). If transport fails or not all conditions of a router are fulfilled, the next router is tested.

{{bc|
begin routers

	# that's the relay router
	dnslookup:
		# the router type
		driver = dnslookup
		# the domains served on this router: not the local domain
		domains = ! +local_domains
		# the transport to be used (see transport section below)
		transport = remote_delivery
		# localhost is to be ignored if dns gives such result
		ignore_target_hosts =  (authentication >) ACL > routing > transport

With this it is important to note that messages coming from authenticated clients are treated (by default) by the same ACL as messages coming from other mail servers.
Exim know a full set of different ACL. Good knowledge of the SMTP protocol is required to choose the correct set of ACL.

 acl_smtp_connect > acl_smtp_helo > ... > acl_smtp_rcpt > ... > acl_smtp_data > ...

For a basic setup two ACL are mandatory: acl_smtp_rcpt and acl_smtp_data. These are default to deny while all other default to accept.
The example below just prevents being an open relay. This setup has multiple security flaws (e.g. all authenticated users may use any mail address). If added to an existing configuration, it must be added before any other special section (i.e. before any existing "begin").

## Hide machine name
If you have a laptop, or a machine in a smarthost configuration, where you do not want the name of the machine to appear in the outgoing email then you must enable exim's rewriting facilities.

In the Rewriting section you should have something like:

 *@machine.mydomain $1@mydomain

where  is the hostname of your laptop or PC and  is the domain name of the machine and the outgoing mail. To rewrite only sender domain, add special flag (F) in the line end. See upstream document for detail

## Startup
Start/enable the .

## Dovecot LMTP delivery & SASL authentication
In this section the integration of Dovecot is described. It is assumed that Dovecot & Exim are already setup and configured. Dovecot will serve as SASL authenticator and local transport mechanism. For this purpose the Dovecot services will be setup as follows.

{{hc|/etc/dovecot/conf.d/10-master.conf|2=
service auth {
	unix_listener exim-auth {
		mode = 0600
		user = exim
		group = exim
	}
	# Auth process is run as this user.
	user = $default_internal_user
}

service lmtp {
	# a unix socket is preferred of a local port communication
	unix_listener exim-lmtp {
		mode = 0600
		group = exim
		user = exim
	}
}
}}

To use the Dovecot SASL in a TLS protected environment, add the following authenticator to Exim.

{{hc|/etc/mail/exim.conf - authenticators section|
	PLAIN:
		driver = dovecot
		public_name = PLAIN
		server_socket = /var/run/dovecot/exim-auth
		server_set_id = $auth1
		server_advertise_condition = ${if def:tls_in_cipher}
}}

The existing router for local delivery can be reused. You may want to consider add a  to the router definition. If DSN is used, Exim will assume final delivery of the message at this point. In the transport section the transport for local delivery must be replaced by the following transport definition.

Since Dovecot is configured to provide a unix socket for the exim user, you may harden your security by adding the following line to the main configuration section.

## Using Gmail as smarthost
In the beginning of the exim conf file, you must enable TLS using

 tls_advertise_hosts = +local_network : *.gmail.com

or to advertise tls to all hosts

 tls_advertise_hosts = *

More information about TLS can be found in the exim documentation.

Add a router before or instead of the dnslookup router:

Add a transport:

Because of host verification, your exim log might contain

But this has no effect on mail-delivery and can be ignored.
Add an authenticator (replacing myaccount@gmail.com and mypassword with your own account details):

 is used for  and  instead of smtp.gmail.com to avoid occasional 530 5.5.1 Authentication Required errors. These are caused by the changing IP addresses in DNS queries for smtp.gmail.com.  will expand to the particular IP address that was resolved by the  router.

For added security, use a per-application password. This works with Google Apps accounts as well.

## Hardening
## Rate limits
Security breaches happen. In case you do not have any service that submits local mail (receiving mail from localhost on a port is not considered local submission), completely disable local submission. Do so by adding  to the main section and add the following simple ACL to the acl section.

If local submission is required, consider imposing a rate limit to it. Do so by adding  to the main section and adding the following ACL to the acl section. It imposes 2 rate limits: 20 mails in a single minute and 30 mails in 10 minutes. With this a burst of local submitted alerts are possible while

## Troubleshooting
## 451 Temporary local problem
If you are getting a "451 Temporary Local Problem" when testing SMTP, you are probably sending as root. By default Exim will not allow you to send as root.
