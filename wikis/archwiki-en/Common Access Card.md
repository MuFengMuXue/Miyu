# Common Access Card

This page explains how to setup Arch to use a US Department of Defense Common Access Card (CAC).

## Installation
Install  and .

## Configuration
If your card reader does not have a pin pad, append  to .

Sometimes  can struggle to identify the proper driver for CAC, instead it may choose PIV or something else. You can force the CAC driver by editing  for  and

## Enable pcscd
Start/enable .

## Configure browser
# Go to: https://www.cyber.mil/pki-pke/document-library
# Download certs: "PKI CA Certificate Bundles: PKCS#7 For DoD PKI Only - Version 5.14" (ZIP Download)
# Unzip the DoD PKI zip
# Follow browser-specific instructions

## Firefox
## Load security device
Navigate to Edit > Settings > Privacy & Security > Certificates > Security Devices and click "Load" to load a module using  or .

## Import the DoD Certificates
Install the certificates from the mentioned zip-file in this order, by going to Edit > Settings > Privacy & Security > Certificates > Manage Certificates > Authorities > Import (make sure to at-least check the box for "Trust this CA to identify websites"):

# Certificates_PKCS7_v5_14_DoD_der.p7b
# Certificates_PKCS7_v5_14_DoD_DoD_Root_CA_3_der.p7b
# Certificates_PKCS7_v5_14_DoD_DoD_Root_CA_4_der.p7b
# Certificates_PKCS7_v5_14_DoD_DoD_Root_CA_5_der.p7b
# Certificates_PKCS7_v5_14_DoD_DoD_Root_CA_6_der.p7b
# DOD_PKE_Chain.pem

## Chromium/Google Chrome
1. Add the CAC Module to the NSS DB.

Ensure that your CAC is connected, that Chromium is closed and enter the following in a terminal:

Upon success you will see "Module "CAC Module" added to database."

2. Check if the CAC Module was successfully added with

3. Navigate (in a shell) to the location of the unzipped DoD PKI files and install via:

  for n in *der.p7b; do certutil -d sql:$HOME/.pki/nssdb -A -t TC -n $n -i $n; done

or

Re-open Chrome, Navigate to Settings > Show Advanced Settings > Manage Certificates > Authorities to load CA bundle from the  PEM-formatted file from above.

4. Verify the authority is in Chrome under Settings > Show Advanced Settings > Manage Certificates > Authorities then expand "org-U.S. Government" and you should see a number of "DoD" certificates listed.

## VMware/Omnissa Horizon Client
Please note that Omnissa purchased the horizon-view solution from VMware.

## Omnissa
Install , and . To integrate CAC authentication with the VMware Horizon Client, create the directory  and link the pkcs11 library:

 # ln -s /usr/lib/pkcs11/opensc-pkcs11.so /usr/lib/omnissa/horizon/pkcs11/libopenscpkcs11.so

Also create the following symlinks to enable ssl_3.4.0.

 # ln -sf /usr/lib/libcrypto.so.3 /usr/lib/omnissa/libcrypto.so.3
 # ln -sf /usr/lib/libssl.so.3 /usr/lib/omnissa/libssl.so.3

If utilizing an external CAC reader, enable and start .

## VMware
Install , , and . Start and enable .

To integrate CAC authentication with the VMware Horizon Client, create the directory  and link the pkcs11 library:

 # ln -s /usr/lib/pkcs11/opensc-pkcs11.so /usr/lib/vmware/view/pkcs11/libopenscpkcs11.so

Also create the following symlinks to enable ssl_3.4.0

 # ln -sf /usr/lib/libcrypto.so.3 /usr/lib/vmware/libcrypto.so.3
 # ln -sf /usr/lib/libssl.so.3 /usr/lib/vmware/libssl.so.3

## Testing
Visit your favorite CAC secured web page and you should be asked for the Master Password for your certificate.  Enter it and if you get in, you know it is working.

If some sites/pages seem to have a problem working correctly (e.g. outlook web access will not authenticate the session for DoD webmail) try using a private/incognito session to test validity of the cert chain and remove some variables.

If you would like to manually query the certificates on a PIN enabled CAC/SmartCard, use the following command:

 $ p11tool --login --provider=/usr/lib/pkcs11/opensc-pkcs11.so --list-all-certs -d 100

## Debugging
## opensc-tool
Most of this information was found in a blog post by Firas Kraïem

Verify  can see your reader:

List plugged in card:

List plugged in card and drive in use:

## pcsc-tools
An other option is . The program  may be helpful
