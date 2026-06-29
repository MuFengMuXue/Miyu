# SpamAssassin

SpamAssassin is a mail filter to identify spam.

## Installation
Install the  package.

Create a sa-update-keys directory in  and change the owner and group:

 # mkdir -p /etc/mail/spamassassin/sa-update-keys /etc/mail/sa-update-keys
 # chown -R spamd:spamd /etc/mail/spamassassin /etc/mail/sa-update-keys
 # chmod 755 /etc/mail/spamassassin
 # chmod 700 /etc/mail/spamassassin/sa-update-keys

Next start/enable .

## Usage
Go over  and configure it to your needs.

## Updating rules
Update the SpamAssassin matching patterns and compile them:

 /usr/bin/vendor_perl/sa-update && /usr/bin/vendor_perl/sa-compile

You will want to run this periodically, the best way to do so is by setting up a systemd timer.

Create the following service, which will run these commands:

Then create the timer, which will execute the previous service daily:

Now you can start and enable .

## Set maximum size for scanning
The default maximum size for scanning is 500 KB (see ). You can modify it: create the spamc configuration file. For example :

## Using a SQL database
SpamAssassin can load user preferences, Bayesian filter data and auto-whitelist from a SQL database. This is specially helpful for a virtual user mail setup, where users do not have a  directory with their SpamAssassin data.

## MySQL
Install . Then, create the database:

Git-clone [https://github.com/apache/spamassassin SpamAssassin's source. Under the  directory you will find the required files to create the database tables. Note that  has been replaced by  in recent MySQL versions, so replace it accordingly in the used  files if needed.

Create the tables for user preferences, Bayesian filter data and TxRep, respectively:

 $ mysql -u root -p    :localhost
user_scores_sql_username
user_scores_sql_password

# Bayesian filter
bayes_store_module          Mail::SpamAssassin::BayesStore::MySQL
bayes_sql_dsn               DBI:mysql::localhost
bayes_sql_username
bayes_sql_password

# TxRep plugin
txrep_factory               Mail::SpamAssassin::SQLBasedAddrList
user_awl_dsn                DBI:mysql::localhost
user_awl_sql_username
user_awl_sql_password
}}

Finally, restart .

## Plugins
## ClamAV
Install and setup clamd as described in ClamAV.

Follow one of the above instructions to call SpamAssassin from within your mail system.

Install the  package. Then install the ClamAV perl library as follows:

 # /usr/bin/vendor_perl/cpanp -i File::Scan::ClamAV

Add the 2 files from https://wiki.apache.org/spamassassin/ClamAVPlugin into .
Edit  and update  to point to your Clamd socket location (default is ).

Finally, restart .

## Razor
Vipul's Razor is a distributed, collaborative, spam detection and filtering network.

Make sure you have installed SpamAssassin first, then:

Install the  package.

Register with Razor.

 # mkdir /etc/mail/spamassassin/razor
 # chown spamd:spamd /etc/mail/spamassassin/razor
 cd /etc/mail/spamassassin/razor
 [spamd$ /usr/bin/vendor_perl/razor-admin -home=/etc/mail/spamassassin/razor -register
 /usr/bin/vendor_perl/razor-admin -home=/etc/mail/spamassassin/razor -create
 [spamd$ /usr/bin/vendor_perl/razor-admin -home=/etc/mail/spamassassin/razor -discover

To tell SpamAssassin about Razor, add the following line to :

 razor_config /etc/mail/spamassassin/razor/razor-agent.conf

To tell Razor about itself, add the following line to :

 razorhome = /etc/mail/spamassassin/razor/

Finally, restart .

## Tips and tricks
## Maintaining TxRep SQL table
It is recommended to keep TxRep SQL table clear of stale data, for performance and storage reasons. Here is a sample query that can be run on a regular schedule:

 DELETE FROM txrep WHERE last_hit <= (now() - INTERVAL 120 day);
