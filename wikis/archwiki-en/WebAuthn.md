# WebAuthn

Web Authentication (WebAuthn) is a web standard published by the World Wide Web Consortium (W3C). WebAuthn is a core component of the FIDO2 Project under the guidance of the FIDO Alliance. The goal of the project is to standardize an interface for authenticating users to web-based applications and services using public-key cryptography.

Similar to legacy U2F, Web Authentication is resilient to verifier impersonation, that is, it is resistant to active man-in-the-middle-attacks, but unlike U2F, WebAuthn does not require a traditional password. Moreover, a roaming hardware authenticator is resistant to malware since the private key material is at no time accessible to software running on the host machine. Passkey is another term used by some vendors to refer to WebAuthn or FIDO credentials.

## FIDO2 vs U2F
FIDO2 is the successor of the FIDO Universal 2nd Factor U2F legacy protocol. FIDO2 authentication has all the advantages of U2F—the primary difference is that a FIDO2 authenticator can also be a single-factor (passwordless) authenticator. The U2F protocol is designed to act as a second factor to strengthen existing username/password-based login flows.

## Authentication for websites
WebAuthn/FIDO2 is supported by major sites like Google, Facebook, Twitter, or GitHub. See https://www.dongleauth.com/ to find other websites and links to setup documentation. Major sites offer different WebAuthn variants but may first offer Passkeys authentication, since that allows to transiently synchronize credentials to a cloud-based account instead of relying on a separate hardware authenticator or password manager.

Modern browsers like Firefox and Chromium support WebAuthn authentication standalone, additional dependencies are not required.

For a demo site to test the WebAuthn authentication process, see https://webauthn.io/.

## Local Linux authentication (PAM)
For using U2F authentication see U2F.

## Using a FIDO2 authenticator for local login
The FIDO2 specification includes an extension called HMAC Secret Extension (hmac-secret), which allows the secure use of a shared secret stored on the authenticator for local authentication.

One of the easiest ways to setup the local authentication process with FIDO2 is through the use of
systemd-homed and the setup options of homectl.

## Authenticators and tools
## Using TPM as a FIDO device
To use TPM as a FIDO device, install . This is useful for testing or if you do not have a FIDO key. Alternatives include , a fork of the original tpm-fido, and .

## Software-based authenticators (without TPM)
For software based authenticator,  and  are available.

## Support
* Chromium: supported since v70
* Firefox: supported since v60
* : the web extension ,  enables saving passkeys directly in the vault without the need for a security key.
* KeePassXC
* pass with
