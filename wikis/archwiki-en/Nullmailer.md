# Nullmailer

Nullmailer is a small mail program that allows you (or your system) to send mails through an existing email account (using an SMTP server). Technically, this is a MTA. Nullmailer is particularly useful on systems that are not always online (like a travelling laptop).

## Installation
Install the package .

## Configuration
Configuration files are located in . Each file contains one option and the possible configurations are not particularly well documented. Below we give an example of a configuration to use gmail as a relay host.

After setting the configurations, start/enable the .

## Example: gmail
In the file  you need to set the connection to the relay host. For gmail:

You can also use starttls.

In the file , you need to encode the hostname of your computer.

In the file , you need to set the gmail domain:

## Other configurations
In the file  you can set the minimum time to pause between  successive  queue  runs  when there  are  messages  in  the  queue, in seconds. This defaults to 60, which for a travelling laptop is way too soon. You can set this to one hour for example:

 3600

In the file  you can set how long nullmailer tries to send a particular message before giving up. The default is one hour, 3 minutes might be a more reasonable cutoff:

 180

## Testing
You can test the configuration by sending a test email:

 $ echo "Subject: sendmail test" | sendmail -v recipient_address
