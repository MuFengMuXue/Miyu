# SSMTP

sSMTP is a program which delivers email from a local computer to a configured mailhost (mailhub). It is not a mail server (like feature-rich mail server sendmail) and does not receive mail, expand aliases or manage a queue. One of its primary uses is for forwarding automated email (like system alerts) off your machine and to an external email address.

## Installation
Install the package .

## Forward to a Gmail mail server
To configure sSMTP, you will have to edit its configuration file () and enter your account settings.

* If your Gmail account is secured with two-factor authentication, you need to generate a unique App Password to use in . You can do so on your App Passwords page. Use you Gmail username (not the App Name) in the  line and use the generated 16-character password in the  line, spaces in the password can be omitted.
* If you do not use two-factor authentication, you need to allow access to unsecure apps. You can do so on your Less Secure Apps page.

You can then pipe messages into mail instead of into sendmail.
 $ echo -e "Hey archuser." | mail archuser
