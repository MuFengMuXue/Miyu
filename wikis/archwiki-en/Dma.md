# Dma

dma (Dragonfly Mail Agent) is a tiny Mail Transport Agent (MTA). It is able to accept mails and deliver it to local or remote destinations; however, if you want to send and receive mails with your domain name, then you will need a full-featured mail server.

## Installation
Install the  package.

## Configuration
dma has two main configuration files:  contains main setup directives and  is necessary for authentication on SMTP servers. dma provides sane defaults so you may be able to use it without special configuration for local mail delivery.

## SMTP transport
If you want to route mail through external SMTP server you must set  address (also known as relay host) in :

Also do not forget to set authentication credentials in  in the following format:

To have dma actually use the credentials file, set :

To change default port set  directive ( is default):

## Encryption
 directive enables encryption during mail transfers. Depending on your needs uncomment  to enable STARTTLS support and activate  to permit unencrypted fallback in case of error.

For whatever reason you may want to perform plain text SMTP authentication. In such case uncomment  directive and change it to  explicitly.

## Masquerading
If you want to substitute original From: field in envelope you can use  feature:

## Testing
To send test mail execute the following from command line:

 $ mail -s "Just a dma test" foo@bar.example.com
 This is just a small test message

Run  as root to see if all went good. Also you can check dma queue with:

 $ dma -bp

 directory also holds undelivered/unprocessed mails.

## Examples
## Send mails through Google's SMTP servers
## Prerequisites
If you use 2-Step Verification (also known as two-factor authentication) procedure then you should create so-called App Password.

To do that login into your Google Account, choose Security entry on the left panel and click on App Passwords in Signing in to Google panel. If you do not see this item please consult corresponding thread on Google.

Click on Select app and choose desired application (usual called as Mail). Then click on Select device and choose the device, but it is better to add custom device and call it appropriately for easy future management. Then click on Generate and write down your App Password (16-character code in the yellow bar).

## Configuration
The MASQUERADE line ensures that mails sent by DMA appear to come from the specified user. Google will reject emails that do not come from the correct Google account.

## Minimalistic configuration with "null client"
If your use case is "all emails to be send to external mailbox(es) without any local delivery", the following configuration:

* Uses port 465 (TLS by default, always encrypted, no STARTTLS negotiation needed)
* Sends everything to Google SMTP server, bypassing any local mboxes.
