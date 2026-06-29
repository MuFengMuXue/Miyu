# Google Authenticator

Google Authenticator provides a two-step authentication procedure using one-time passcodes (OTP), initially standardized by the Initiative for Open Authentication (OATH). The authentication mechanism integrates into the Linux PAM system. This guide shows the installation and configuration of this mechanism.

For the reverse operation (generating codes compatible with Google Authenticator under Linux) see #Code generation below.

## Installation
Install the  package, which provides the client program  and the PAM module . The development version is available with .

## Configuration
This section covers configuring the system's PAM to require Google Authenticator OTP authentication for SSH and, optionally, desktop login.

## SSH
Usually one demands two-pass authentication only for remote login. The corresponding PAM configuration file is . In case you want to use Google Authenticator globally you would need to change , however, in this case proceed with extreme caution to not lock yourself out.
In this guide we proceed with editing  which is most safely (but not necessarily) done in a local session.

To enter both, your unix password and your OTP, add  above the system-remote-login lines to :

 auth            required        pam_google_authenticator.so
 auth            include         system-remote-login
 account         include         system-remote-login
 password        include         system-remote-login
 session         include         system-remote-login

This will ask for the OTP before prompting for your Unix password. Changing the order of the two modules will reverse this order.

To allow login with either the OTP or your Unix password use:

 auth            sufficient      pam_google_authenticator.so

Enable keyboard interactive authentication in :

 KbdInteractiveAuthentication yes

Finally, reload .

## Request OTP only when connecting from outside your local network
Sometimes, we just want to enable the 2FA capability just when we connect from outside our local network.
To achieve this, create a file (e.g. ) and add the networks where you want to be able to bypass the 2FA from:

 # only allow from local IP range
 + : ALL : 192.168.20.0/24
 # Additional network: VPN tunnel ip range (in case you have one)
 + : ALL : 10.8.0.0/24
 + : ALL : LOCAL
 - : ALL : ALL

Then edit your  and add the line:

 #%PAM-1.0
 auth default=ignore pam_access.so accessfile=/etc/security/access-local.conf
 auth      required  pam_google_authenticator.so
 auth      include   system-remote-login
 account   include   system-remote-login
 password  include   system-remote-login
 session   include   system-remote-login

## Desktop logins
The Google Authenticator PAM plugin can also be used for console logins and with GDM. Just add the following to  or the  file:

 auth required pam_google_authenticator.so

## Usage
Every user who wants to use two-pass authentication needs to
* generate a secret key file in their home folder, and
* setup their OTP generators accordingly

## Generating a secret key file
The google-authenticator generates a TOTP secret key file as follows:

It is recommended to store the emergency scratch codes safely (print them out and keep them in a safe location) as they are your only way to log in (via SSH) when you lost your mobile phone (i.e. your OTP-generator). They are also stored in , so you can look them up any time as long as you are logged in.

## Storage location
If you want to change the secret key files' storage path, you can use the flag :

 $ google-authenticator --secret="/path_folder/username"

Then, do not forget to change the location path for PAM, in :

{{hc|/etc/pam.d/sshd|2=
auth required pam_google_authenticator.so user=root secret=/path_folder/${USER}
}}

 is used to force PAM to search the file using root user.

Also, take care with the permissions of the secret key file. Indeed, the file must be only-readable by the owner (chmod: ). Here, the owner is root.

 $ chown root:root /path_file/secret_key_files
 $ chmod 400 /path_file/secret_key_files

## Code generation
In the final setup step, each user has to associate the secret key file generated in their home directory with their choice of OTP-generators to serve the authentication codes. A user may set up generators on different devices for redundancy, for example  in an OTP application on a mobile phone and a separate password manager, or decide to rely on the emergency scratch codes generated earlier as backup.

## Mobile phone generators
Install a generator application on your mobile phone (e.g.):

* FreeOTP for Android (F-Droid, Google Play) or iOS (App Store).
* FreeOTP+ for Android (F-Droid, Google Play).
* Aegis for Android (F-Droid, Google Play).
* Bitwarden for Android (F-Droid, Google Play) or iOS (App Store).
* Google Authenticator for Android (Google Play) or iOS (App Store).

In the mobile application, create a new account and either scan the QR code from the URL you were told when generating the secret key file, or enter the secret key (in the example above 'ZVZG5UZU4D7MY4DH') manually.

Now you should see a new passcode token being generated every 30 seconds on your phone.

If you have Google Authenticator configured with other systems, then losing your device can prevent you from being able to log in to those systems. Having additional ways to generate the codes can be helpful.

## Code managers
A script that enables the display, generation, storage and management of Google Authenticator codes is provided by . An alternative option is .

## KeePassXC
GUI password manager  allows associating Google Authenticator codes to its entries, and then it can generate OTP codes and export its keys via QR code.

## Command line
The easiest way to generate codes is with . It is available in the  package, and can be used as follows:

 $ oathtool --totp --base32 secret_key

On most Android systems with sufficient user access, the Google Authenticator database can be copied off the device and accessed directly, as it is an sqlite3 database. However, at some point in July 2022, the secret column on the accounts table started using encryption. If your database backup does not use this encryption, this shell script will read a Google Authenticator database and generate live codes for each key found:

## Testing
SSH to your host from another machine and/or from another terminal window:

 $ ssh hostname
 login as: username
 Verification code: generated/backup_code
 Password: password
 $
