# Nitrokey

Nitrokey is an open-source USB key series used to enable the secure encryption and signing of data. The secret keys are always stored inside the Nitrokey which protects against malware (such as computer viruses) and attackers. A user-chosen PIN and a tamper-proof smart card protect the Nitrokey in case of loss and theft. The hardware and software of Nitrokey are open-source. The free software and open hardware enables independent parties to verify the security of the device. Nitrokey is supported on Microsoft Windows, macOS, Linux, and BSD. Nitrokey is developed and produced in Germany.

## Software
Packages designed to help configure Nitrokey products are  (Nitrokey Pro and Nitrokey Storage),  (Nitrokey Pro and Nitrokey Storage),  (Nitrokey 3) and  (providing the  command).

For hardware encryption devices in general, it is important to have  installed. Secure login to a shell and various websites are also supported by the Nitrokey 3 and Nitrokey FIDO2. For this to work,  is required, see Universal 2nd Factor.

## Setup
Device nodes for a Nitrokey will be created by the udev rules which are part of the  package, previously they were part of the  package. The rules rely on the  tag to allow regular users to use the devices. For use by GnuPG, the newly created  device (as determined by ) must be accessible by an unprivileged user. For WebAuthn, the  device must also be. If they are only accessible by root, you can change the default by adding  to the appropriate lines in . Instead of 41, one might need to symlink to a higher number if  interferes.

To setup the udev rules manually (without the  package), please refer to https://docs.nitrokey.com/software/nitropy/linux/udev.

Nitrokeys are empty when they first arrive. The official instructions explain how to create a new secret key and transfer it to the device. Backing up the key must be done before the transfer but only do this if you have a secure place to store the backup. The official site also has instructions for how to interface with  and such using .

## Tips and tricks
## KeePassXC
To get Nitrokey 3 working with KeePassXC you need to install  and start and/or enable .
Open  and create new HMAC key.

Now you should be able to select your Nitrokey 3 after restarting KeePassXC.
