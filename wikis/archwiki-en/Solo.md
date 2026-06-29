# Solo

The Solo (or SoloKey) is a small USB security token supporting Universal 2nd Factor (U2F) requests, thus acting as a second factor for authentication. It also supports the newer FIDO2 standard allowing for passwordless logins.

Compared to a YubiKey it offers less features, but supports firmware upgrades to extend the functionality in the future. The key-hardware and software are released as open source. The keys are distributed in different form factors and two versions: Solo V1 (STM32L432 chip) and Solo V2 (LPC55S69 chip).

## Installation
Special drivers are not required for the key to work. It is recommended to install the Solo software and upgrade the firmware of your Solo.

## Upgrading the firmware
Managing your Solo V1, e.g. upgrading the firmware or setting a PIN, can be performed with the  package. After installing the package, first check if your key is detected:

Then you can use  to perform a firmware upgrade,  to set a PIN, and  to change your pin.

## Test the Solo in your browser
Visit the Webauthn demo, type in a username and click on "Register". Your Solo's LED will flash until you click it. After that, you can login to the page only using your Solo, no need for username or password.
