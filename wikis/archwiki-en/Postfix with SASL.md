# Postfix with SASL

SMTP protocol specifications include a possibility for user authentication, but do not provide the exact details of protocol message exchange, deferring instead to the SASL (Simple Authentication and Security Layer) standard (see RFC 4954 and RFC 4422). SASL is a generic authentication framework for authentication mechanisms, of which there are many, and each of them has its own particular procedure that prescribes the necessary cryptographic steps to perform with the authentication data and messages to exchange over the connection. Therefore, in order to avoid imposing artificial limits on what authentication mechanisms can be used with it, Postfix, by itself, does not authenticate SMTP users with usernames and passwords, or via any other means. It offloads this task to a SASL implementation, which has to be installed separately. SASL authentication daemon is responsible both for the policy (i.e. where valid usernames and secrets such as passwords are kept) and mechanism (how exactly clients supply credentials). This is in contrast with e.g. OpenSMTPD, which supports only PLAIN and LOGIN SASL mechanisms, but does not rely on any external library or daemon.

## Introduction
In this article you will learn how to setup SASL authentication for Postfix.

Once Postfix is up and running you can add SASL authentication to avoid relaying from unauthenticated anonymous users.  SASL authentication will prevent anonymous users from email spamming and only allow authenticated and trusted users to send emails.

Since  package in is already compiled with SASL support, to enable SASL authentication you have two choices:
* Use  package.
* Or enable your already configured Dovecot to handle Postfix authentication (as well as its own).

From [https://www.postfix.org/SASL_README.html Postfix's site:
:People who go to the trouble of installing Postfix may have the expectation that Postfix is more secure than some other mailers. The Cyrus SASL library contains a lot of code. With this, Postfix becomes as secure as other mail systems that use the Cyrus SASL library. Dovecot provides an alternative that may be worth considering.

## Configuration with cyrus-sasl package
Install the  package.

To enable SASL for accepting mail from other users, open the "Message submission" port (TCP 587) in , by uncommenting these lines (which are there by default, just commented):

Note that this also enables SSL, so if you do not have a SSL certificate, keep the "smtpd_tls_security_level" option commented out.

The three restriction options (client, helo, sender) can also be left commented out, since smtpd_recipient_restrictions already handles SASL users.

SASL can use different authentication methods. The default one is PAM (as configured in ), but to set it up properly you have to create :

Since pambase 20190105.1-1 and newer uses restrictive fallback for "other" PAM service, a pam configuration file is now required.Create .

If using PAM in conjunction with  for authentication, an alternative pam configuration file () could be constructed similar to: LDAP authentication#PAM configuration

Start/enable the .

Restart the .

If wanting to validate the SASL-PAM authentication process, the following command can be run to determine if SASL can authenticate via PAM:

Hopefully you should be able to telnet to your Postfix server with:

You should then type:

This is roughly what you should see:

## Configuration with Dovecot
If you are using Dovecot as your IMAP or POP mail server and your users already authenticate (with PAM maybe), then there is no need to configure another package.

Simply edit  and add the following lines under the  or  section (depending on what you are using):

Using this configuration implies that only authenticated users can send mails. You can see this from  option.

Now add the following to Dovecot configuration file in :

{{bc|1=
service auth {
  unix_listener /var/spool/postfix/private/auth {
    group = postfix
    mode = 0660
    user = postfix
  }
  user = root
}
}}

As you can see a unix socket is created in , the same specified in  option of

Finally restart both postfix and dovecot services.
