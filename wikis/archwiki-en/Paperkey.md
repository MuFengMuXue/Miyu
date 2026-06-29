# Paperkey

Paperkey is a command line tool to export OpenPGP keys on paper. It reduces the size of the exported key, by removing the public key parts from the private key. Paperkey also includes CRC-24 checksums in the key to allow the user to check whether their private key has been restored correctly.

## Installation
Install the  package.

## Usage
## Backup
To create a backup of your GnuPG key, pipe the private key to paperkey:
 $ gpg --export-secret-key key-id | paperkey --output secret-key-paper.asc

## Restore secret key
To restore the secret key you need to have a file with the paperkey data and the public key. Then run the following command to import the private key to :
 $ paperkey --pubring public-key.gpg --secrets secret-key-paper.asc | gpg --import
Alternatively, restore the private key to a file:
 $ paperkey --pubring public-key.gpg --secrets secret-key-paper.asc --output secret-key.gpg

## Error: unable to parse OpenPGP packets (is this armored data?)
If you receive this error while restoring your key, you need to dearmor your public key first:
 $ gpg --dearmor public-key.asc

## Tips and tricks
## Print secret key directly
If no  argument is given, paperkey will print its output to . It is possible to print the key directly without intermediate file, which might have security implications. To do so, install CUPS, and pipe to :

 $ gpg --export-secret-key key-id | paperkey | lpr

## Encode the secret key as QR Code
By default, paperkey will output the secret key as human readable text. While this format guarantees the ability to read and restore the printed information, it is not very convenient. The  option tells paperkey to output the raw secret key data instead. This enables the use of other encodings, including machine-readable ones such as the QR code.

The  program can be used for this:

 $ gpg --export-secret-key key-id | paperkey --output-type raw | qrencode --8bit --output secret-key.qr.png

It is possible to increase the error correction level to maximum with the  option. This provides a lost data restoration rate of about 30% at the cost of reduced capacity. Should the secret key not fit in the QR code, the lower  and  error correction levels are also available and give restoration rates of about 25% and 15% respectively. The default error correction level is  which allows restoration of about 7% of lost data.

## Restore the secret key from QR code
With  it is possible to restore the key using a camera:

 $ zbarcam -1 --raw -Sbinary | paperkey --pubring public-key.gpg | gpg --import

The same options can also be applied to :

 $ zbarimg -1 --raw -q -Sbinary secret-key.qr.png | paperkey --pubring public-key.gpg | gpg --import

If you are using a scanned image, you might have to blur it by

 $ convert secret-key.qr.png -blur 0 secret-key-blurred.qr.png
