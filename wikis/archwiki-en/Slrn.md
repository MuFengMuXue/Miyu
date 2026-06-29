# Slrn

slrn is a text-based news client. It runs through a textual user interface and is highly customizable. It uses the S-Lang library.

## Installation
Install the  package.

## Configuration
To run slrn, you will have to set up an environment variable with the newsgroups server you wish to use:

 NNTPSERVER='my.news.server' && export NNTPSERVER

Two important slrn configuration files are .slrnrc for basic configuration and .jnewsrc that contains the list of newsgroups.

To create .slrnrc from a sample startup file for slrn:

 # cp /usr/share/doc/slrn/examples/slrn.rc.gz ~/.
 # gunzip -c ~/.slrn >~/.slrn.rc

After creating .slrnrc you should configure the user account and then create .jnewsrc:

 # slrn -f ~/.jnewsrc --create

## User account
To set up your newsgroup account, you have to set up the following parameters in .slrnrc

 set username "desired_username"
 set hostname "desired_hostname"
 set replyto "some_name "

## Signature
To set up a signature uncomment the following line in .slrnrc:

 set signature ".signature"

Also, you have to create .signature file in your home folder and put your signature in it.

## Encoding
To set up encoding (i.e. utf8) uncomment the following lines in .slrnrc:

 charset display utf8
 charset outgoing utf8

## Displaying all posts
By default slrn will only shows unread posts. If you are used to having all posts listed in a certain newsgroup, this will be a big change for you. To have all posts listed add the following to your .slrnrc:

 setkey group "set_prefix_argument(4); () = select_group();" " "

## Managing usergroups
You can manage usergroups directly through slrn or by editing .jnewsrc file. If you decide to manage them using .jnewsrc file, you can do it by changing the ! and : at the end of each newsgroup.

Unsubscribed group example:
 misc.test! 1-210917

Subscribed group example:
 misc.test: 1-210917
