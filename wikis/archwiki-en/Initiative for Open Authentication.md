# Initiative for Open Authentication

The Initiative for Open Authentication (OATH) is an industry-wide collaboration to develop an open reference architecture using open standards to promote the adoption of strong authentication. They publish the standard which Google Authenticator and other common 2-factor applications use.

## Installation
The following packages can be used to generate, transfer, and validate OATH credentials:

*  - Takes credentials and generates codes. Includes a PAM module for user authentication. See pam_oath.
*  - Offers a client program  for generating new credentials and a PAM module for user authentication. See Google Authenticator.
*  - Adds OATH support to
*  - Decodes QR codes
*  - Encodes QR codes

## Preliminary Setup
Some OATH methods rely on a correct time synchronization. Diagnose by  and ensure . If not, enable Systemd-timesyncd.

 $ systemctl enable systemd-timesyncd

## Standards
OATH has created two standards of significance to an Arch user, both based on a Base32-encoded shared secret of arbitrary length:

; HOTP: HMAC (Hash-based message authentication code) One-time Password (HOTP). Every time a password is generated, a counter is incremented. This value is concatenated with a secret key, and then hashed to generate a 6-10 digit code. The authenticating party does the same, except it increments a counter when a code is successfully authenticated. To handle desynchronization of the counter, the authenticating party can also check several (30-100) additional values beyond its current counter state.
; TOTP: Time-based one-time-password (TOTP), which works much like HOTP except it uses the current time instead of a counter. This solves the desynchronization problem, and eliminates the possibility of an adversary recording OTPs for use later.

## URI credential format
Credentials are usually shared in a QR-encoded URI format. All fields must be URI-encoded strings:

 otpauth://TYPE/LABEL?PARAMETERS

; TYPE:  or
; LABEL: Identifies which account a key is associated with, optionally prefixed with an issuer string. Example:
; PARAMETERS: Take the standard URI parameter format -

*  - required; this is the Base32 shared secret.
*  - Indicates the provider or service the account is associated with. If this is absent, the issuer prefix of the label will be used. If both are present, they should be equal.
*  -  by default. Can also be  or .
*  - How long passcodes should be. Default is 6, can be 8.
*  - Required if using HOTP. Initial counter value.
*  - Optional if using TOTP. Sets how long a code is valid, 30 seconds by default.

Here is an example:

 otpauth://totp/Example%20Company:archie@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example%20Company
          |type|  issuer prefix  |     account     |         secret        |     issuer            |
               |               label               |                  parameters                   |

## Tips and tricks
## Decode QR codes
This can be accomplished with tools from . Decode a PNG file:

 $ zbarimg my_qr_code.png --quiet --raw

Decode images from a camera:

 $ zbarcam /dev/video0

Take a screenshot with  and decode it to the clipboard:
 $ import -silent -window root png:- | zbarimg --quiet --raw - | xclip -selection clipboard

## Create QR codes
The  package is useful here.

Encode a URI, save it as a PNG:

 $ qrencode -o my_code.png 'MY_URI'

Encode a URI, print a QR code to the terminal:

 $ qrencode -t ansiutf8 'MY_URI'

Encode a URI, copy it to the clipboard as a PNG:

 $ qrencode -o - 'MY_URI' | xclip -selection clipboard -t image/png

## Generate keys
To generate your own key in the proper format, you can use something like the following:

 $ head -c 16 /dev/urandom | base32 --wrap 0

## Generate OTPs from the command line
Use  from :

 $ oathtool --base32 --totp KEY

Many password managers, including pass and KeePass also offer support for generating these codes.

## Linux User authentication with PAM
See either pam_oath or Google Authenticator.
