# One Time PassWord

One Time PassWord (OTPW) is a PAM module allowing single-use passwords to login to a system. This is especially useful in the context of Secure Shell, allowing a user to login from a public or shared computer using a single-use password which will never work again.

Instructions for installing OTPW and configuring SSH to allow OTPW logins are below.

## Installation
Install the  package.

## Configuration for SSH logins
## PAM configuration
Create a PAM configuration file for otpw:

Next, modify sshd's PAM configuration to include otpw. If you are disabling static password authentication (), comment out the second bold line. Here is the modified  for reference:

## sshd configuration
OTPW uses Keyboard-Interactive logins for SSH sessions, which are enabled by adding these lines:

If you wish to allow static password logins as well, ensure  contains a line like this:

Otherwise, set it to . See the above info on editing  to fully disable static password auth, as PAM will otherwise allow a static password if OTPW fails (e.g. when a user runs out of passwords).

If you allow password authentication, then after failing one authentication method, ssh clients will fall back to the other. Note that by default, ssh allows you three attempts at a password per login method.

## OTPW configuration
OTPW is configured independently for each user account. If a given account does not have OTPW configured, that account will simply use a static password as usual. To configure OTPW for an account, run as that user:

 $ otpw-gen > ~/otpw_passwords

 will ask for a password prefix, which must be typed at the beginning of all otpw passwords. This is to ensure that if someone else gets your OTPW list, they cannot use it to login to your account without knowing your prefix.

After running the above command, there should be a file in the user's home directory called  which contains all of the user's OTPW passwords. There will also be a file  which contains the password hashes.  can be printed and referenced when logging in.

## Usage
After completing the configuration above, ssh should use OTPW automatically for users who have it configured. An OTPW login prompt looks like so:

 Password 041:

To log in, simply look up password 41 in your  list, for example:

 041 lYr0 g7QR

And type in your prefix followed by both halves of the password. The space is provided for readability and may or may not be included in the typed password. Do not enter a space between the prefix and the single-use password.

To specify to the ssh client which login method you would like to use, add  to use OTPW, or  for static passwords. These options can also be specified in  per-server.

To prevent someone from shoulder-surfing your OTPW and quickly using it to login to your account before you login, OTPW requires a concurrent login to enter three passwords instead of just one. This will usually not be an issue, but if OTPW should give a prompt like this:

 Password 072/251/152:

Then simply enter your prefix, and the three requested passwords in the order they are requested in. When a login is initiated, OTPW creates a file  to detect concurrent logins. If a second login is initiated when this file exists, OTPW will request the three passwords.
