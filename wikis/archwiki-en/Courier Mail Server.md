# Courier Mail Server

Courier MTA is a mail transfer agent and POP3/IMAP4 server with Courier. This article builds upon Mail server.

The advantages of Courier-MTA are:
* Authentication for MTA and POP3/IMAP happens against one data source
* This data source can be a MySQL, PgSQL or LDAP, but also can be simpler like PAM or a compiled plaintextfile (BerkeleyDB)
* Easy support of virtual users
* SMTP-auth out of the box
* Comes with webmail
* Web based administration possible
* Also has a separate mail delivery agent (MDA), if it is needed

## Preamble
The following text describes a setup for two local domains on one physical machine, which is not so uncommon for single users or small companies. We authenticate against a BerkeleyDB-based ".dat" file which is created from a text or multiple textfiles automatically by tools that come with courier. This method is described in the Courier documentation as authuserdb, so do not get confused about names. The authentication against other providers happens in an adequate way and is covered in courier-authlibs documentation. There are differences in the handling of SASL methods (such as PLAIN or CRAM-MD5) depending on which authentication backend (authuserd, authpam, authmysql ...) you like to use. Just do not expect that this setup can be painlessly converted from the described authuserdb to authmysql.

## Installation
Install the  package.

Any other mail transfer agents (like Cyrus) or SMTP servers (Sendmail, Postfix, etc.) must be uninstalled for this, so answer 'yes' when prompted to do so.

## TLS
You need to obtain a certificate.

## Authuserdb authentication
Let Courier know that we want to authenticate against authuserdb.

In the file  find  then remove all listed modules except for authuserdb:

## Creating the vmail user
We want to deliver our mail primarily to virtual users, so we can easily create e-mail accounts without creating real users. Granny may want to read her e-mail but she does not need ssh access to that box, does she? To make that possible we need one "physical" user, that owns all of our mails physically on the drive. Note, that this is not the courier user which is primarily there to make sure that the actual server process does not run as root. Many people save this stuff in  since it is primarily thought for these things. You can create the users "home" just anywhere you want! The decision will be influenced by the partition layout of your drive(s).

Add a user "vmail", who is the lord of all of the mail files:

 # useradd -u 7200 -m vmail
 # passwd vmail

## Creating the email accounts
There is a place where the virtual users and their attributes will be stored. This can be either a plain textfile or a directory where several textfiles are contained. See courier-authlib's documentation for details. The directory-based approach makes maintenance a bit easier since we can separate the users of domains and subdomains, so we will go with this approach. The name of the directory is not negotiable.

 # mkdir /etc/authlib/userdb

The attributes of the "vmail"-system user need to be stored here, too, since we allowed only authuserdb in  . Fortunately, courier comes with a handy script that converts all local users into a file in courier-syntax. This file can be named freely, we call it "system". Later we also create a file for "domain1" and "domain2". Got the idea?

 # pw2userdb > /etc/authlib/userdb/system

Keep only the "vmail" user (this means that no local user can receive emails!):

 # sed -n -i "/vmail/p" /etc/authlib/userdb/system

Now we create the virtual users in the authentication database. The actual Maildir folders have to be created manually later. This creates a user "user1@domain1" and a "user2@domain2". For details about these commands check the man pages for the command itself and the man pages that are linked to.

* user1:

 # userdb -f /etc/authlib/userdb/domain1 user1@domain1 \
   set home=/home/vmail/domain1/user1 uid=7200 gid=7200

Let us set a password for the user (used for PLAIN and LOGIN and APOP):

 # userdbpw -md5 | userdb -f /etc/authlib/userdb/domain1 user1@domain1 set systempw

The following is used for CRAM-MD5 and friends (SASL-methods). Also note that this construct pipes the password directly into the command and thus can be read as cleartext, but can be handy for shell scripts that create new users:

 # echo 'pwuser1' | userdbpw -hmac-md5 | \
   userdb -f /etc/authlib/userdb/domain1 user1@domain1 set hmac-md5pw

* user2 (repeat for user2@domain2):

 # userdb -f /etc/authlib/userdb/domain2 user2@domain2 \
   set home=/home/vmail/domain2/user2 uid=7200 gid=7200

 # userdbpw | userdb -f /etc/authlib/userdb/domain2 user2@domain2 set systempw

 # echo 'pwuser2' | userdbpw -hmac-md5 | \
   userdb -f /etc/authlib/userdb/domain2 user2@domain2 set hmac-md5pw

## Setting up Maildirs
We need to create the virtual users "Maildir" as a physical place on the hard-drive in the "vmail"-system user home directory. Note that the "vmail" user needs write rights and also will own the files. It is easiest to create that stuff as the "vmail" user:

Become "vmail":

 # su vmail
 $ mkdir -p /home/vmail/domain1/user1 && maildirmake /home/vmail/domain1/user1/Maildir
 $ mkdir -p /home/vmail/domain2/user2 && maildirmake /home/vmail/domain2/user2/Maildir

Leave "vmail" account and become root:

 $ exit

Make sure you become root again by leaving the "vmail" account by typing  as shown above.

## Creating the user database
Now it is time to create the BerkeleyDB from the plain text files. It is important that the files in  are visible for root only. If they have any world or group rights, courier will not allow the creation of the db-files from the information.

 # chmod 700 /etc/authlib/userdb && chmod 600 /etc/authlib/userdb/*
 # makeuserdb

Now we can check if the authentication works. Courier comes with a little tool that checks if users can be authenticated. Before using this tool, we must make sure the authentication daemon is running by enabling . Then:

 # authtest user1@domain1
 # authtest user2@domain2

If you encounter any errors while testing the authentication, please consult these instructions, which detail how to use debugging features to pinpoint the problem.

## Configuring courier
Now we are now done with authentication stuff. It gave us a flexible layout which can be easily extended. Time to move on to courier's configuration itself. First, we will try to give some aliases for the server. The aliases follow the userdb's scheme very closely. Unlike in other servers, there is no need to handle with all aliases in just one file. Again, you can create several plain text files in one folder, where you can handle the aliases by domains or even finer structured if you like. The folder's location is again not negotiable, you must use . There is already a "system" file which deals with root, postmaster and the usual suspects. Just add a "user1@domain1" behind the existing "postmaster: " to have all system relevant mails delivered to "user1@domain1". We just assume that this user is your primary account.

 # cat > /etc/courier/aliases/domain1  /etc/courier/locals
 # echo server237.blahfarm.com >> /etc/courier/locals

 # mkdir /etc/courier/hosteddomains
 # cat > /etc/courier/hosteddomains/domain1  /etc/courier/hosteddomains/domain2  /etc/courier/esmtpacceptmailfor.dir/domain1

Repeat for domain2:

 # echo domain2 > /etc/courier/esmtpacceptmailfor.dir/domain2

Finally, convert into a BerkeleyDB:

 # makeacceptmailfor

...and you are done here.

## Testing your setup
Now the server is ready. Let us run several tests on the SMTP server and see if it is working nicely at least for sending and receiving mails.

Let us test some more stuff, which can be useful.

Send an ordinary mail (as root or ordinary user):

 $ echo "To: user2@domain2
 From: user1@domain1" | sendmail

Send a mail to an alias:

 $ echo "To: userer2@domain2
 From: user1@domain1" | sendmail

Send a mail to an external email address:

 $ echo "To: me_freak@gmail.com
 From: user1@domain1" | sendmail

## Configuring IMAP and POP3
So far, our operations have been focused on the box which runs the server itself. Now we need to setup some interaction related configuration. Since security is important we will setup some nice authentication modes, which does not send cleartext passwords. Courier supports CRAM-MD5 among others. You will have to make sure that your clients support that too. So far I tested sylpheed-claws > 1.0.4, esmtp and Thunderbird with these settings.

Now it comes in, that we will have to configure the several server daemons. Courier is already running (from the perftest above) but it does not provide services to the network. So we have to configure esmtpd, pop3d and imapd with their respective configuration files in  .

Since we like to use SMTPAuth instead if a IP/Domain based SMTP authentication we need to activate the AUTHREQUIRED option in esmtpd. Also we activate the CRAM-MD5 challenge method for authorization. NOTE: this setup definitely keeps Outlook losers out. For these buggy and old fashioned clients you will need to use way less restrictive settings!

In :

In :

The imapd setting is a bit different. In  there is a long line starting with IMAP_CAPABILITY. Just add a "AUTH=CRAM-MD5" at the end of the arguments and you should be done:

## Remarks
Because of our very small test case with just two boxes and no domain control we have to take a look at Courier's intrinsics and work around a little issue. Courier is nitpicking about RFC compliance, which does mean you have to make sure that you understand how to configure your e-mail clients for testing.
This will fail in our testing:

Why? Because you send from a non-valid domain name. I assume here, that we use our "domain1" and "domain2" testpark. Now, when you create an account in Sylpheed which looks like this:
Name:     user numberone
Address:  user1@domain1
Sylpheed consequently sends the mail as "user numberone ". This is wrong, since it violates the RFC. You get a Error: 517 - Syntax Error. For the testing you can simply fool Courier-MTA by setting the domain in sylpheed's dialog to:
Address:  user1@domain1.xx

Something similar (you just get Error 513 - Syntax Error) happens in this case:

because domain2 is not valid. You can send to mail.domain2 which will work around that. For boxes at the internet and properly configured domains this is absolutely no problem, since you are always part of a domain and thus have one dot (.) behind the @.
