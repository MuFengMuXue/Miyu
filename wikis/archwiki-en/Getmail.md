# Getmail

getmail is a mail retriever designed to allow you to get your mail from one or more mail accounts on various mail servers to your local machine for reading with a minimum of fuss. getmail is designed to be secure, flexible, reliable, and easy-to-use. getmail is designed to replace other mail retrievers such as fetchmail.

## Installation
Install the  package (uses python 2) or  package (uses python 3).

## Configuration
* Create a configuration directory, and set the right permissions by executing: . The main configuration file often contains sensitive information, namely passwords in plain text.
* Create a configuration file, the default being: . A separate configuration file is needed for each mailserver to pick up mail from. Configuration files other than the default, will have to be explicitly passed as arguments to the getmail command.

## Retrieving mail
Here is an example  used with a gmail account.

You can tweak this to your POP3 service's specification.

## Password management
It is possible, rather than storing your password in the config, to call an external program to read the password. In which case, you would use the  parameter:

   password_command = ("/path/to/password-retriever", "-p", "myaccount@example.org")

Note that the password parameter (in the example configuration above) overrides this parameter; specify one or the other, not both.

## Other options
Most people will like to add the following section to their  to prevent all the mail on the server being downloaded every time getmail is ran.

For this guide we will be storing our mail in the  format. The two main mailbox formats are  and . The main difference between the two is that  is one file, with all of your mails and their headers stored in it, whereas a  is a directory tree. Each mail is its own file, which will often speed things up.

A  is just a folder with the folders ,  and  in it.

 $ mkdir -p ~/mail/{cur,new,tmp}

Now, run getmail. If it works fine, you can create a cronjob for getmail to run every n hours/minutes. Type  to edit cronjobs, and enter the following:

  */10 * * * * /usr/bin/getmail

That will run  every 10 minutes.

Also, to quiet getmail down, we can reduce its verbosity to zero by adding the following to .

## More than one Email account with getmail
By default, when you run  the program searches for the file getmailrc created as seen above. If you have more than one mail account you would like to get mail from, then you can create such a file for each email address, and then tell getmail to run using both of them.  Obviously if you have two accounts and two files you cannot have both of them called getmailrc. What you do is give them two different names, using myself as an example: I call one personal, and one university. These two files contain content relevant to my personal mail, and my university work mail respectively. Then to get getmail to work on these two files, instead of searching for getmailrc(default), I use the --rcfile switch like so:  This can work with more files if you have more email accounts, just make sure each file is in the .getmail directory and make sure to  alter the cronjob to run the command with the --rcfile switches. E.g.
  */30 * * * * /usr/bin/getmail --rcfile university --rcfile personal

Obviously you can call your files whatever you want, providing you include them in the cronjob or shell command, and they are in the .getmail/ directory, getmail will fetch mail from those two accounts.

## Sorting mail with procmail
Edit your getmailrc to pass retrieved mail to procmail:

Then configure procmail to filter your mail.

## Fetching mail automatically with systemd
You can run  every n hours/minutes with Systemd/Timers. Create a unit file for the timer:

Now create the service file:

Enable/start the user unit .
