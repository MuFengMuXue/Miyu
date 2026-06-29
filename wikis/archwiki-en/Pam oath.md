# Pam oath

The OATH Toolkit provides one-time password (OTP) components for authentication systems. It contains a PAM authentication module that supports technologies include the event-based HOTP algorithm (RFC 4226) and the time-based TOTP algorithm (RFC 6238). The OTP generator applications are available for Android, iOS, Blackberry and other devices. Similar to Google Authenticator the authentication mechanism integrates into the Linux PAM system. This guide shows the installation and configuration of this mechanism.

## Installation
Install the  package.

## Setting up the OATH
The OATH seed is an hexadecimal number that should be unique per user. To generate a new seed for a user, you could use the following command line:

There needs to be one OATH per user and link to it in a configuration file . A specification of the file format can be found here. While being Root user create the file and insert the user seed:

If you need HOTP, use this configuration:

Make sure that the file can only be accessed by Root user:

 # chmod 600 /etc/users.oath
 # chown root /etc/users.oath

## Setting up the PAM
To enable OATH for a specific service only, like OpenSSH, you can edit the file  and add at the beginning of the file the following line:

 auth	  sufficient pam_oath.so usersfile=/etc/users.oath window=30 digits=6

This will allow authentication if you just enter the right OATH code. You can make OATH as a requirement and let the rest of the PAM stack be processed if you use the following line instead:

 auth	  required pam_oath.so usersfile=/etc/users.oath window=30 digits=6

For SSH login to work, make sure these options are enabled in the file :

 ChallengeResponseAuthentication yes
 UsePAM yes

Restart  to enable the changes.

If you want to force OATH request-response even if there is a working public key authentication and password authentication also add the following in :

 AuthenticationMethods publickey,keyboard-interactive:pam
 KbdInteractiveAuthentication yes
 PasswordAuthentication yes

## Logging with an OATH password
For logging in with TOTP:

 $ oathtool -v --totp -d 6 12345678909876543210

If you are logging in with HOTP:

 $ oathtool -v -d 6 12345678909876543210

Replace  by the seed corresponding to your user. It will output something like the following:

 Hex secret: 1ab4321412aebc
 Base32 secret: DK2DEFASV26A====
 Digits: 6
 Window size: 0
 Start counter: 0x0 (0)

 820170

The last string of numbers can be used as a code for login right now, but more interestingly the Base32 secret, because it can be converted to QR code for easily transferring keys. Install the package  to run the following command to convert:

 $ qrencode -o user.png 'otpauth://totp/user@machine?secret=DK2DEFASV26A====

Change user, machine and  accordingly. Once done, you can visualize your QR code with your preferred image visualizer application. Alternatively you may generate the QR code directly onto terminal with:

 $ qrencode -t UTF8 'otpauth://totp/user@machine?secret=DK2DEFASV26A====

It is pretty straight forward to use Aegis Authenticator or FreeOTP+ to then take a screenshot of that  (or ASCII-art like image) and get it to display OTP password when needed.
