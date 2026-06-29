# Romanian eID

This page refers to the Romanian eID (electronic identity card) colloquially known as "CEI" (Cartea Electronica de Identitate), specifically its applications on Arch Linux systems, as well as installation guidelines and troubleshooting tips.

For general information referring to electronic identification on Arch Linux, specifically through government-issued cards, visit Electronic identification.

As of today, the only driver interface known to work with CEI is a proprietary solution issued freely by the Romanian government and available at https://hub.mai.gov.ro/aplicatie-cei. Sources (namely Andrei Nicoara on behalf of OrchestrateID) claim to have developed an interface for CEI using only open ISO standards citation - linkedin post, but no proof has been made to back this claim, and it is unlikely the specific ISO standards will be disclosed by the developers of OrchestrateID.

The app bundled with the drivers, available at  is used to display on-chip information, i.e. a set of all visible information printed on the polycarbonate card itself, alongside domicile and residence information, which can only be seen on chip. The app also facilitates changing the PIN numbers, seeing and exporting information on the cryptographic certificates public keys, and loading other certificates when used in combination with write-friendly smartcard readers. The PUK codes for the onboard certificates are not made known to the user, instead the user has to show up in person to any SPCEP office or Romanian embassy/consulate to be identified pending a PIN code reset.

The card is equipped with 2 certificates, bearing Advanced Electronic Signature status in the EU, as well as full equivalence to a handwritten signature under Romanian jurisdiction, under Law 214/2024. The certificates are used for TLS Authentication and respectively PAdES/PKCS#7/XAdES/etcetera file signature protocols. The resulting signatures are used to authenticate the signer as well as guarantee file integrity. Files signed with such a signature bear full legal obligations similar to a handwritten signature, under Romanian and EU jurisdictions. Romanian citizens can also use the authentication certificate to log into governmental and private digital platforms, for secure and legally binding operations. We strongly recommend unplugging the smartcard from your system immediately after use, to stop potential bad actors from legally acting on your behalf using the CEI certificates by interfacing with it.

## Installation
# Start/enable
# Install .

Depending on the smartcard reader, specific drivers relating to it might also be needed for proper functioning. Use the idplugclassic GUI application to test for smartcard access. Most USB readers are plug-and-play on Arch Linux, given that  is installed a priori.

## Software Integration
## NSS database
Append the following lines, to the  file located at the root of the NSS databse folder:

## Firefox
CEI can be used in Firefox for TLS authentication in government platforms.

Navigate to Edit > Preference > Advanced > Certificates > Security Devices and click Load to load a module using . You can assign any name to it, i.e. .

## Chromium-based browsers
CEI can be used in Chromium-based for TLS authentication in government platforms.

Chromium-based browsers utilize (usually) the built-in NSS database located at , where CEI can be added as described above.

## Okular
CEI can be used in Okular for document signing, commonly for PDF format files using PAdES type signatures.

Start by adding CEI to any valid NSS database of choice as described above, then, inside the Okular graphic user interface, navigate to Settings > Configure Backends > PDF and ensure the following settings are set correctly on this page:

* Check revocation of digital signatures' certificates using 3rd-party servers: ON
* Signature Backend: NSS
* Certificate Database: Custom: {absolute file path to your preferred NSS database}

## Troubleshooting
## Freezes and Crashes on PIN input
Some reputable users have been able to replicate an issue in which programs utilizing the card for cryptographic operations freeze or take several seconds before prompting for a pin, leading to crashes or annoyances. As the interface is momentarily closed-source, we cannot intervene to fix the issue from its origin, but a common fix is creating a new, empty NSS database using  and then appending the proper lines to the file  as described in the NSS database integration instructions above. Subsequently cleaning your Firefox profile's  file may help with this issue, as reported by some users.
