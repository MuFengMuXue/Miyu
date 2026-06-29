# Electronic identification

An electronic identification ("eID") is an electronic identification solution of citizens or organizations, for example in view to access benefits or services provided by government authorities, banks or other companies. Apart from online authentication many eICs also give users the option to sign electronic documents with a digital signature.

## Installation
Install the  package, all electronic identification requires this package. Then see #Hardware specific packages.

For pinentry support, install .

## Hardware specific packages
## ACS smart cards
Install the  package.

For more information about ACS smart cards, see ==== Cr-75 card reader ====

Install the  package for the device with the  ID.

## Belgium
## Installing the eID middleware
Import the (continuous build) keys from [https://files.eid.belgium.be/. See makepkg#Signature checking. Install the  package, then run:

 $ about-eid-mw

In the window that opens, the PCSC daemon status should be listed as "running". If it is not the case, start . Even if the service reports that it's socket activated or automatically started instead of "running", the service may need to be started manually.

## Installing the card reader's driver
Look at the brand of the card reader; there is a high chance it is ACS (Advanced Card System Ltd).
If it is ACS, go to https://belgeid.be/en/product/acr38 and download the Linux driver.
Follow the described install driver process.

## Installing the browser integration
## Chrome/Chromium
Chrome does not need a plugin. Chromium require  and  as well. This article provides some instructions.

## Firefox/Librewolf
A browser extension will need to be installed.
Additionally, the eID module will need to manually be added to the Firefox security devices configuration. The steps are:

# Open Firefox' settings.
# Search for 'security devices'. Click the corresponding button.
# In the popup, select 'Load'.
# The second popup will ask for a file location. You can find this file by running  and looking for the "64-bit PKCS#11 location" value.

For Librewolf, also symlink the directories created by the middleware to , to avoid an error notification when starting Librewolf:
 # ln -s /usr/lib/mozilla/managed-storage /usr/lib/librewolf/managed-storage
 # ln -s /usr/lib/mozilla/pkcs11-modules /usr/lib/librewolf/pkcs11-modules

## General troubleshooting
A test page is available from the government to check if eID is configured correctly. Troubleshooting hints may be available in the official documentation, although Arch Linux is not officially supported.

Also note that using Flatpak or Snap is/was not supported, as those do not allow PKCS#11 modules such as eID to be loaded. Fixed for snap for all opensc readers: closed launchpad bug.

## Signing documents
Signing emails with Thunderbird and documents with LibreOffice is explained in a blog post by Luc Stroobant.

Depending on system configuration, it may be possible to run Adobe Reader DC under wine. The Belgium government has a relevant FAQ item on digital signatures.

If using Adobe Reader is not possible, the Belgian Federal Public Services' Signing Box offers an upload tool to sign PDFs. The website prompts to install two dependencies: an extra eID middleware  and a browser extension.

Although  and  provide native support for digital PDF signing, signatures are not reported as valid by Signing Box. An open bug ticket exists for okular.

## Brazil (ICP-Brasil)
## SSL
Install  as the Brazilian root CAs are not part of Mozilla's NSS due to a long standing issue.

The above package should be enough. If you have any issue, check installation instructions https://www.gov.br/iti/pt-br/assuntos/navegadores for Chromium, Firefox and other popular web browsers, and for Java.

## Smart Cards (A3 certificates)
1. Install  and .

2. Start/enable

## Firefox
Navigate to Edit -> Preference -> Advanced -> Certificates -> Security Devices and click "Load" to load a module using  and name it .

Test it by going to Receita Federal's e-CAC.

## Chrome
Ensure Chrome is closed and run:

 $ modutil -dbdir sql:$HOME/.pki/nssdb/ -add "ICP-Brasil A3 - Safe Sign Identity Client" -libfile /usr/lib/libaetpkss.so

## Croatia
# Start/enable
# Install .
# Launch the client. It is used for activating the card or changing the PINs or the PUK.

## Firefox
Navigate to Edit > Preference > Advanced > Certificates > Security Devices and click Load to load a module using . You can assign any name to it, i.e. .

## Estonia
See https://www.id.ee/en/.

## DigiDoc
Once  and  is installed and  is started, install . One of the dependency  is verified with a signature that you have to import to your GnuPG keyring.

 $ gpg --keyserver keys.openpgp.org --recv-keys DCAA15007BED9DE690CD9523378B845402277962

If you have an ACS card reader,  is required.

DigiDoc4 has an optional GNOME/Files right click menu integration that requires  to be installed.

## Browser Configuration
Current browser ID-Card stack is based on Web eID.
It provides consistent user experience on all supported platforms for both PIN 1 authentication and PIN 2 document signing.

Web eID consists of two components. Both need to be installed.

*  - Native component used by all browsers
*  and  - Browser extension that talks to the native component

 is verified with a signature and you need to import developer PGP keys to your GnuPG keyring.

 $ wget -q -O- https://github.com/metsma.gpg | gpg --import -
 $ wget -q -O- https://github.com/mrts.gpg | gpg --import -

Not all sites have migrated to the new Web eID PIN 1 JavaScript API and use the older Mutual TLS (also some times called TLS-CCA. You still need to configure  PKCS #11 provider in the browsers by running this command:

 $ pkcs11-register

You will also need to restart the browser afterwards.

## Testing
* Make sure that Web eID extension is installed and enabled
* Go to https://web-eid.eu/ and follow Authenticate -> Sign flow
* Test Mutal TLS (TLS-CCA) using https://test-eid.eesti.ee/

## Finland
Atostek ID is the official client of the Finnish Digital and Population Data Services Agency. Atostek ID was released at the end of 2024. Atostek ID replaces the previous card reader software DigiSign Client. However, DigiSign Client still receives updates until the end of 2025. These updates will focus on bug fixes and security updates. No new features are planned for the old client.

Having both clients installed at the same time is not recommended.

Official information on the card reader software is available at: https://dvv.fi/en/download-card-reader-software.

## Atostek ID
Atostek ID is the current official card reader software.

## Installation
Install . Since Atostek ID is a GUI application that relies heavily on the system tray, pay attention that relevant optional dependencies are installed for your desktop environment.

Make sure to enable and start the . Otherwise the client might not start, or applications that rely on the client might crash.

## Activation
New government issued ID cards need to be activated before usage. This needs to be done only once.

Connect the card reader to your computer and insert your smart card. Launch the application. If the card has not been activated previously, the client will automatically display the activation window. Activation is required only once per card. If the activation window does not appear, choose "Activate card" from the application menu. When the activation window opens, enter the activation code (PUK) provided in the code letter that came with your card. Next, set a PIN for the authentication certificate (PIN1) and another PIN for the signing certificate (PIN2). It is highly recommended that PIN1 and PIN2 are different. Once you have entered the required information, click OK.

## Usage
Atostek ID supports digital authentication and signing. It also utilizes the PKCS #11 interface. The card reader software can be used, for example, to authenticate with a web browser, to sign PDF documents, and logging in to the system. See the official instructions at: https://dvv.fi/en/download-card-reader-software

## Firefox
Navigate to Security Devices page (Search it via Preferences), then click Load and set Module Name to p11-kit-proxy and module filename to . Finally restart Firefox. The card can be tested at: https://dvv.fi/en/test-the-use-of-a-certificate.

## Signature Creation Service (SCS)
Signature Creation Service (SCS) is a specification of the Digital and Population
Data Services Agency. It is used, for example, in patient information systems. SCS utilizes self-signed certificates, which can be generated by running:

 $ atostekid -installSCSCA

This will create a certificate () and a private key () in . The certificate will need to be installed manually to your web browser.

## Atostek ERA Smartcard
Atostek ERA Smartcard is a feature intended for social and healthcare users who are registered to use the ERA system. It utilizes self-signed certificates, which can be generated by running:

 $ atostekid -installCA

This will create a certificate () and a private key () in . The certificate will need to be installed manually to your web browser.

## Known issues
When authenticating and signing with Firefox, the PIN dialogs are not delegated to the Atostek ID client. Instead, the native PIN dialogs of Firefox are shown. It is possible that Firefox will ask PINs multiple times.

## DigiSign Client
DigiSign Client is the old card reader software. It will be supported until the end of 2025. The Finnish Digital and Population Data Services Agency recommends using the new #Atostek ID client instead.

## Installation
First install the prerequisites as described in #Installation. Then install . Launch the client, connect your reader and put in your card. Click the icon in your status bar once it turns yellow. This should trigger the card activation process if you have not activated it before.

## Usage
## Firefox
Navigate to Security Devices page (Search it via Preferences), then click Load and set Module Name to DigiSign PKCS#11-moduuli and module filename to . Finally restart Firefox. The card can be tested at: https://dvv.fi/en/test-the-use-of-a-certificate.

## Germany
## ReinerSCT devices
For some devices, you need to install  and copy the default configuration file  to the same folder, without the .default suffix. Restart  and applications like  should recognize the scanner. The ReinerSCT RFID will blink its LED, which it does not when the driver is not installed correctly.

You can also use a smartphone as the card reader, if both your computer and the smartphone are in the same network. You must install and run AusweisApp on the phone (available for Android / iPhone).

## Latvia
## eParaksts
For document signing install the  package. No additional software is necessary to use it with eParaksts mobile or eID Scan.

To use the eID card, install  and the prerequisite packages listed in #Installation, and make sure to enable and start . To use it in a browser, additionally install the browser extension .

## Smart-ID
To use the eID card with Smart-ID, install the following packages:
* - Native component communicating with all browsers
* or  - Browser extensions that communicate with the native component

## Romania
# Start/enable
# Install .
# Launch the client from

Refer to the Romanian eID wiki page for further installation tips and troubleshooting.

## Firefox
Navigate to Edit > Preference > Advanced > Certificates > Security Devices and click Load to load a module using . You can assign any name to it, i.e. .

## Issues with performance
Refer to the Romanian eID wiki page.

## Spain
## DNI electrónico (DNIe)
Install . To sign documents using your identity card, install the autofirma package ().

## Sweden
BankID is the leading electronic identification in Sweden.
