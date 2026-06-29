# Sieve filters

Sieve is a programming language that can be used to create filters for email on mail server.

## Servers
 can be used with Dovecot. It implements the ManageSieve protocol (specifically RFC 5804).

## Client tools
To manage sieve filters remotely, clients exist for servers implementing the ManageSieve protocol (RFC 5804).

*
*

## sieve-connect
To connect:

 $ sieve-connect -s mail.example.com -u user@example.com

Then the help is short and explicit:

 > help
