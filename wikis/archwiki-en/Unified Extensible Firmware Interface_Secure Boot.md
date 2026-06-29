# Unified Extensible Firmware Interface/Secure Boot

Secure Boot is a security feature found in the UEFI standard, designed to add a layer of protection to the pre-boot process: by maintaining a cryptographically signed list of binaries authorized or forbidden to run at boot, it helps in improving the confidence that the machine core boot components (boot manager, kernel, initramfs) have not been tampered with.

As such it can be seen as a continuation or complement to the efforts in securing one's computing environment, reducing the attack surface that other software security solutions such as system encryption cannot easily cover, while being totally distinct and not dependent on them. Secure Boot just stands on its own as a component of current security practices, with its own set of pros and cons.

## Checking Secure Boot status
## Before booting the OS
At this point, one has to look at the firmware setup. If the machine was booted and is running, in most cases it will have to be rebooted.

You may access the firmware configuration by pressing a special key during the boot process. The key to use depends on the firmware. It is usually one of , ,  or possibly another  key. Sometimes the right key is displayed for a short while at the beginning of the boot process. The motherboard manual usually records it. You might want to press the key, and keep pressing it, immediately following powering on the machine, even before the screen actually displays anything.

After entering the firmware setup, be careful not to change any settings without prior intention. Usually there are navigation instructions, and short help for the settings, at the bottom of each setup screen. The setup itself might be composed of several pages. You will have to navigate to the correct place. The interesting setting might be simply denoted by secure boot, which can be set on or off.

## After booting the OS
An easy way to check Secure Boot status on systems using systemd is to use :

Here we see that Secure Boot is enabled and enforced (in user mode); other values are  for Setup Mode,  if Secure Boot is disabled and  if the firmware does not feature Secure Boot.

Another way to check whether the machine was booted with Secure Boot is to use this command:

 $ od --address-radix=n --format=u1 /sys/firmware/efi/efivars/SecureBoot-8be4df61-93ca-11d2-aa0d-00e098032b8c

If Secure Boot is enabled, this command returns  as the final integer in a list of five, for example:

 6  0  0  0  1

Note, however, that the kernel may be unaware of Secure Boot (even if it is enabled in the firmware) if an insufficiently capable boot loader is used. This can be verified by checking the kernel messages shortly after the system starts up:

The kernel messages will otherwise read .

## Booting an installation medium
The official installation image does not support Secure Boot (). Secure Boot support was initially added in  and later removed in . At that time prebootloader was replaced with , even though the latter uses unsigned EFI binaries. There has been no support for Secure Boot in the official installation medium ever since.

In order to boot an installation medium in a Secure Boot system, you will need to either disable Secure Boot or modify the image in order to add a signed boot loader.

Archboot images provide a way to use secure boot on installation media.

## Disabling Secure Boot
The Secure Boot feature can be disabled via the UEFI firmware interface. How to access the firmware configuration is described in #Before booting the OS.

If using a hotkey did not work and you can boot Windows, you can force a reboot into the firmware configuration in the following way (for Windows 10): Settings > Update & Security > Recovery > Advanced startup (Restart now) > Troubleshoot > Advanced options > UEFI Firmware settings > restart.

Note that some motherboards (this is the case in a Packard Bell laptop and recent Xiaomi laptops) only allow to disable secure boot if you have set an administrator password (that can be removed afterwards). See also Rod Smith's Disabling Secure Boot.

## Repacking the installation image
See #ISO repacking.

## Editing the installation medium
If you are using a USB flash installation medium, then it is possible to manually edit the EFI system partition on the medium to add support for Secure Boot.

Plug in the USB drive, then mount the partition:

 # mount /dev/disk/by-label/ARCHISO_EFI /mnt

Then follow the instructions in #Using a signed boot loader to install any signed boot loader. For example, to install #PreLoader:

## Implementing Secure Boot
There are certain conditions making for an ideal setup of Secure boot:

# UEFI considered mostly trusted (despite having some well known criticisms and vulnerabilitiesand necessarily protected by a strong password
# Default manufacturer/third party keys are not in use, as they have been shown to weaken the security model of Secure Boot by a great margin[https://habr.com/ru/post/446238/
# UEFI directly loads a user-signed EFI boot stub-compatible unified kernel image (no boot manager), including microcode (if applicable) and initramfs so as to maintain throughout the boot process the chain of trust established by Secure Boot and reduce the attack surface
# Use of full drive encryption, so that the tools and files involved in the kernel image creation and signing process cannot be accessed and tampered with by someone having physical access to the machine.
# Some further improvements may be obtained by using a TPM.

A simple and fully self-reliant setup is described in #Using your own keys, while #Using a signed boot loader makes use of intermediate tools signed by a third-party.

Using the GRUB boot loader requires extra steps before enabling secure boot, see GRUB#Secure Boot support for details.

## Using your own keys
Secure Boot implementations use these keys:

; Platform Key (PK): Top-level key.
; Key Exchange Key (KEK): Keys used to sign Signatures Database and Forbidden Signatures Database updates.
; Signature Database (db): Contains keys and/or hashes of allowed EFI binaries.
; Forbidden Signatures Database (dbx): Contains keys and/or hashes of denylisted EFI binaries.

See The Meaning of all the UEFI Keys for a more detailed explanation.

To use Secure Boot you need at least PK, KEK and db keys. While you can add multiple KEK, db and dbx certificates, only one Platform Key is allowed.

Once Secure Boot is in "User Mode" keys can only be updated by signing the update (using sign-efi-sig-list) with a higher level key. Platform key can be signed by itself.

## Determine OpROM signature
Use the following steps to check if you have any signed OpROM.

List all of your devices with OpROM:

This shows an example of Intel DC SSD with signed EFI ROM. Repeat the following steps for each device.

Dump the ROM:

 # echo 1 > /sys/devices/pci0000:80/0000:80:01.0/0000:81:00.0/rom
 # cat /sys/devices/pci0000:80/0000:80:01.0/0000:81:00.0/rom > ~/intel_ssd.rom
 # echo 0 > /sys/devices/pci0000:80/0000:80:01.0/0000:81:00.0/rom

Retrieve and compile TianoCore's EDK II Tools:

 $ make -C BaseTools

Parse ROM file:

It indicates that the OpROM has a compressed EFI image at offset 0x0038 of Image 1 at Offset 0x0.

Get the EFI section:

 $ dd if=intel_ssd.rom ibs=1 skip=$(( 0x00 + 0x38 )) of=intel_ssd.rom.efi.compressed

Decompress the image:

 $ ./BaseTools/Source/C/bin/TianoCompress -d --uefi -v ~/intel_ssd.rom.efi.compressed -o ~/intel_ssd.rom.efi

Examine the signatures with  and you can see it is signed with Microsoft's DB certs:

## Backing up current variables
Before creating new keys and modifying EFI variables, it is advisable to backup the current variables, so that they may be restored in case of error.

Install the  package, then run the following commands to backup all four of the principal Secure Boot variables:

 $ for var in PK KEK db dbx ; do efi-readvar -v $var -o old_${var}.esl ; done

If you perform this command on a new computer or motherboard, the variables you extract will most likely be the ones provided by Microsoft.

## Putting firmware in "Setup Mode"
Secure Boot is in Setup Mode when the Platform Key is removed. To put firmware in Setup Mode, enter firmware setup utility and find an option to delete or clear certificates. How to enter the setup utility is described in #Before booting the OS.

## Assisted process with systemd
As of v257, you can easily set up Secure Boot with systemd and systemd-boot. Install .

First set up your desired configuration as in Unified kernel image#ukify (you can use the template from ), then generate your signing keys:

 # ukify genkey --config /etc/kernel/uki.conf
 Using config file: /etc/kernel/uki.conf
 Writing SecureBoot private key to /etc/kernel/secure-boot-private-key.pem
 Writing SecureBoot certificate to /etc/kernel/secure-boot-certificate.pem

Sign the boot loader with the newly created keys (see systemd-boot#Signing for Secure Boot for automation):

 # /usr/lib/systemd/systemd-sbsign sign \
 --private-key /etc/kernel/secure-boot-private-key.pem \
 --certificate /etc/kernel/secure-boot-certificate.pem \
 --output /usr/lib/systemd/boot/efi/systemd-bootx64.efi.signed \
 /usr/lib/systemd/boot/efi/systemd-bootx64.efi

Next, configure the ESP for auto-enrollment:

 # bootctl install --secure-boot-auto-enroll yes \
 --certificate /etc/kernel/secure-boot-certificate.pem \
 --private-key /etc/kernel/secure-boot-private-key.pem

This installs (or updates) the signed systemd-boot boot loader to the ESP, and creates three files ,  and  in . No separate platform or key exchange keys are generated, instead the signing key is enrolled at all three levels.

Finally, set  in , and reboot to enroll the keys in the firmware. See .

## Assisted process with sbctl
sbctl is a user-friendly way of setting up secure boot and signing files.

To use it, install . See also the upstream README and .

## Using sbctl with GRUB
See GRUB#Secure Boot support for instructions.

## Creating and enrolling keys
Before starting, go to your firmware settings and set secure boot mode to Setup mode. This is different for each device: see .

Once you log back in, check the secure boot status:

 $ sbctl status

You should see that sbctl is not installed and secure boot is disabled.

Then create your custom secure boot keys:

 # sbctl create-keys

Enroll your keys, with Microsoft's keys, to the UEFI:

 # sbctl enroll-keys -m

Check the secure boot status again:

 $ sbctl status

sbctl should be installed now, but secure boot will not work until the boot files have been signed with the keys you just created.

## Signing
Check what files need to be signed for secure boot to work:

 # sbctl verify

Now sign all the unsigned files. Usually the kernel and the boot loader need to be signed. For example:

 # sbctl sign -s /boot/vmlinuz-linux
 # sbctl sign -s /boot/EFI/BOOT/BOOTX64.EFI

The files that need to be signed will depend on your system's layout, kernel and boot loader.

Now you are done! Reboot your system and turn secure boot back on in the firmware settings. If the boot loader and OS load, secure boot should be working. Check with:

 $ sbctl status

## Automatic signing with the pacman hook
sbctl comes with a pacman hook that automatically signs all new files whenever the Linux kernel, systemd or the boot loader is updated.

## Manual process
## Install efitools
Nearly all of the following sections require you to install the  package.

## Creating keys
You will need private keys and certificates in various formats:

* PEM format private keys (.key) for EFI binary and EFI signature list signing.
* PEM format certificates (.crt) for ,  and .
* DER format certificates (.cer) for firmware.
* Certificates in an EFI Signature List (.esl) for , , KeyTool and firmware.
* Certificates in an EFI Signature List with an authentication header (.auth) (i.e. a signed certificate update file) for , sbkeysync, KeyTool and firmware.

Create a GUID for owner identification:

 $ uuidgen --random > GUID.txt

Platform key:

 $ openssl req -newkey rsa:4096 -noenc -keyout PK.key -new -x509 -sha256 -days 3650 -subj "/CN=my Platform Key/" -out PK.crt
 $ openssl x509 -outform DER -in PK.crt -out PK.cer
 $ cert-to-efi-sig-list -g "$(
* If  returns write errors, first run {{ic|1=chattr -i /sys/firmware/efi/efivars/{PK,KEK,db}*}} prior to issuing commands with  to temporarily change file attributes, enabling writing of the EFI keys within the  directory. See .
* If you get a  error for , you can enroll it with command .
* If this fails, it might be due to the firmware locking BIOS settings. On Dell or Lenovo systems, you may need to reset the BIOS password. See the sysfs firmware authentication documentation.

On Lenovo systems:

 # cat > /sys/class/firmware-attributes/thinklmi/authentication/Admin/current_password
 my-super-secret-password
 ^D

On Dell systems:

 # cat > /sys/class/firmware-attributes/dell-wmi-sysman/authentication/Admin/current_password
 my-super-secret-password
 ^D

and try again.
}}

On next boot the UEFI should be back in User Mode and enforcing Secure Boot policy.

## Using firmware setup utility
Copy all , ,  files (except the  file!) to a FAT formatted file system (you can use EFI system partition).

Launch firmware setup utility and enroll db, KEK and PK certificates.
Firmwares have various different interfaces, see Replacing Keys Using Your Firmware's Setup Utility for example how to enroll keys.

If the used tool supports it prefer using .auth and .esl over .cer.

## Using KeyTool
 is in  package, copy it to ESP. To use it after enrolling keys, sign it with .

 # sbsign --key db.key --cert db.crt --output esp/KeyTool-signed.efi /usr/share/efitools/efi/KeyTool.efi

Launch  using firmware setup utility, boot loader or UEFI Shell and enroll keys.

See Replacing Keys Using KeyTool for explanation of KeyTool menu options.

## Using systemd-boot
Since systemd version 252, systemd-boot can be used to enroll keys. To enroll keys, copy the ,  and  to the special folder on the ESP:

 # cp db.auth KEK.auth PK.auth esp/loader/keys/NAME/

Where NAME can be any unique name you assign, such as .

After copying the keys and enabling the secure boot setup mode a new entry would appear in the boot menu that would read . Activating this entry would enroll the secure boot keys.

## Signing EFI binaries
When Secure Boot is active (i.e. in "User Mode"), only signed EFI binaries (e.g. applications, drivers, unified kernel images) can be launched.

## With sbsigntools
Install  to sign EFI binaries with .

To sign your kernel and boot manager use sbsign, e.g.:

 # sbsign --key db.key --cert db.crt --output /boot/vmlinuz-linux /boot/vmlinuz-linux
 # sbsign --key db.key --cert db.crt --output esp/EFI/BOOT/BOOTx64.EFI esp/EFI/BOOT/BOOTx64.EFI

## Signing the kernel with a mkinitcpio post hook
You can also use a mkinitcpio post hook to sign the kernel when the initramfs gets generated.

Create the following file an make it executable:

Replace  and  with the paths to the key pair you want to use for signing the kernel.

If you are using systemd-boot, there is a dedicated pacman hook doing this task semi-automatically.

## Signing unified kernel images with a mkinitcpio post hook
See Unified kernel image#Signing the UKIs for Secure Boot.

## Fully automated unified kernel generation and signing with sbupdate
sbupdate is a tool made specifically to automate unified kernel image generation and signing on Arch Linux. It handles installation, removal and updates of kernels through pacman hooks.

Install  and configure it following the instructions given on the project's homepage.Once configured, simply run  as root for first-time image generation.

## Updating keys
Once Secure Boot is in "User Mode" any changes to KEK, db and dbx need to be signed with a higher level key.

For example, if you wanted to replace your db key with a new one:

# Create the new key,
# Convert it to EFI Signature List,
# Sign the EFI Signature List,
# Enroll the signed certificate update file.

 $ cert-to-efi-sig-list -g "$( MS_db.esl

Optional (for strict conformity with Microsoft UEFI Secure Boot requirements): Create an EFI Signature List from Microsoft's DER format  certificates using Microsoft's GUID ():

 $ sbsiglist --owner 77fa9abd-0359-4d32-bd60-28f4e78f784b --type x509 --output MS_Win_KEK_2011.esl MicCorKEKCA2011_2011-06-24.crt
 $ sbsiglist --owner 77fa9abd-0359-4d32-bd60-28f4e78f784b --type x509 --output MS_Win_KEK_2023.esl 'microsoft corporation kek 2k ca 2023.crt'
 $ cat MS_Win_KEK_2011.esl MS_Win_KEK_2023.esl > MS_Win_KEK.esl

Sign a  variable update with your . Use  with option  to add not replace a  certificate:

 $ sign-efi-sig-list -a -g 77fa9abd-0359-4d32-bd60-28f4e78f784b -k KEK.key -c KEK.crt db MS_db.esl add_MS_db.auth

Optional (for strict conformity with Microsoft UEFI Secure Boot requirements): Sign a  variable update with your . Use  with option  to add not replace a  certificate:

 $ sign-efi-sig-list -a -g 77fa9abd-0359-4d32-bd60-28f4e78f784b -k PK.key -c PK.crt KEK MS_Win_KEK.esl add_MS_Win_KEK.auth

Follow #Enrolling keys in firmware to enroll  and for strict conformity with Microsoft UEFI Secure Boot requirements  into the UEFI Secure Boot Database variables.

## Using a signed boot loader
Using a signed boot loader means using a boot loader signed with Microsoft's key. There are two known signed boot loaders: PreLoader and shim. Their purpose is to chainload other EFI binaries (usually boot loaders). Since Microsoft would never sign a boot loader that automatically launches any unsigned binary, PreLoader and shim use an allowlist called Machine Owner Key list, abbreviated MokList. If the SHA256 hash of the binary (Preloader and shim) or key the binary is signed with (shim) is in the MokList they execute it, if not they launch a key management utility which allows enrolling the hash or key.

## PreLoader
When run, PreLoader tries to launch . If the hash of  is not in MokList, PreLoader will launch . In HashTool you must enroll the hash of the EFI binaries you want to launch, that means your boot loader () and kernel.

## Set up PreLoader
Install  and copy  and  to the boot loader directory; for systemd-boot use:

 # cp /usr/share/preloader-signed/{PreLoader,HashTool}.efi esp/EFI/systemd

Now copy over the boot loader binary and rename it to ; for systemd-boot use:

 # cp esp/EFI/systemd/systemd-bootx64.efi esp/EFI/systemd/loader.efi

Finally, create a new NVRAM entry to boot :

 # efibootmgr --unicode --disk /dev/sd''X --part Y'' --create --label "PreLoader" --loader /EFI/systemd/PreLoader.efi

Replace  with the drive letter and replace  with the partition number of the EFI system partition.

This entry should be added to the list as the first to boot; check with the  command and adjust the boot-order if necessary.

## Fallback
If there are problems booting the custom NVRAM entry, copy  and  to the default loader location booted automatically by UEFI systems:

 # cp /usr/share/preloader-signed/HashTool.efi esp/EFI/BOOT/
 # cp esp/EFI/systemd/systemd-bootx64.efi esp/EFI/BOOT/loader.efi

Copy over  and rename it:

 # cp /usr/share/preloader-signed/PreLoader.efi esp/EFI/BOOT/BOOTx64.EFI

For particularly intransigent UEFI implementations, copy  to the default loader location used by Windows systems:

 # mkdir -p esp/EFI/Microsoft/Boot
 # cp /usr/share/preloader-signed/PreLoader.efi esp/EFI/Microsoft/Boot/bootmgfw.efi

As before, copy  and  to .

When the system starts with Secure Boot enabled, follow the steps above to enroll  and  (or whichever kernel image is being used).

## How to use while booting?
A message will show up that says  To use HashTool for enrolling the hash of  and , follow these steps. These steps assume titles for a remastered archiso installation media. The exact titles you will get depends on your boot loader setup.

* Select OK
* In the HashTool main menu, select Enroll Hash, choose  and confirm with Yes. Again, select Enroll Hash and  to enter the archiso directory, then select  and confirm with Yes. Then choose Exit to return to the boot device selection menu.
* In the boot device selection menu choose Arch Linux archiso x86_64 UEFI CD

## Delete enrolled hash
Every entry of hashes enrolled in the MOK database eats up a little piece of space of NVRAM. You may want to delete useless hashes to free the space and to prevent outdated programs from booting.

Install  and copy :

 # cp /usr/share/efitools/efi/KeyTool.efi esp/EFI/systemd/KeyTool.efi

Manage to boot to Preloader and you will see the KeyTool entry. You can then edit hashes in the MOK database.

## Remove PreLoader
Uninstall  and simply remove the copied files and revert configuration; for systemd-boot use:

 # rm esp/EFI/systemd/{PreLoader,HashTool}.efi
 # rm esp/EFI/systemd/loader.efi
 # efibootmgr --unicode --bootnum N --delete-bootnum
 # bootctl update

Where  is the NVRAM boot entry created for booting .
Check with the efibootmgr command and adjust the boot-order if necessary.

## shim
When run, shim tries to launch . If MokList does not contain the hash of  or the key it is signed with, shim will launch MokManager (). In MokManager you must enroll the hash of the EFI binaries you want to launch (your boot loader () and kernel) or enroll the key they are signed with.

## Set up shim
Install .

Rename your current boot loader to , because, by default, Shim will try load and run a file named . While this default can be overridden by passing a file path to a different EFI binary as a command line argument to shim, since some firmware have issues with UEFI boot entries that have command line arguments, it is more foolproof to rely on the default.

 # mv esp/EFI/BOOT/BOOTx64.EFI esp/EFI/BOOT/grubx64.efi

Copy shim and MokManager to your boot loader directory on ESP; use previous filename of your boot loader as as the filename for :

 # cp /usr/share/shim-signed/shimx64.efi esp/EFI/BOOT/BOOTx64.EFI
 # cp /usr/share/shim-signed/mmx64.efi esp/EFI/BOOT/

Finally, create a new NVRAM entry to boot :

 # efibootmgr --unicode --disk /dev/sd''X --part Y'' --create --label "Shim" --loader /EFI/BOOT/BOOTx64.EFI

shim can authenticate binaries by Machine Owner Key or hash stored in MokList.

; Machine Owner Key (MOK): A key that a user generates and uses to sign EFI binaries.
; hash: A SHA256 hash of an EFI binary.

Using hash is simpler, but each time you update your boot loader or kernel you will need to add their hashes in MokManager. With MOK you only need to add the key once, but you will have to sign the boot loader and kernel each time it updates.

## shim with hash
If shim does not find the SHA256 hash of  in MokList it will launch MokManager ().

In MokManager select Enroll hash from disk, find  and add it to MokList. Repeat the steps and add your kernel . When done select Continue boot and your boot loader will launch and it will be capable launching the kernel.

## shim with key
Install .

You will need:

; .key: PEM format private key for EFI binary signing.
; .crt: PEM format certificate for sbsign.
; .cer: DER format certificate for MokManager.

Create a Machine Owner Key:

 $ openssl req -newkey rsa:2048 -nodes -keyout MOK.key -new -x509 -sha256 -days 3650 -subj "/CN=my Machine Owner Key/" -out MOK.crt
 $ openssl x509 -outform DER -in MOK.crt -out MOK.cer

Sign your boot loader (named ) and kernel:

 # sbsign --key MOK.key --cert MOK.crt --output /boot/vmlinuz-linux /boot/vmlinuz-linux
 # sbsign --key MOK.key --cert MOK.crt --output esp/EFI/BOOT/grubx64.efi esp/EFI/BOOT/grubx64.efi

You will need to do this each time they are updated. You can automate the kernel signing with a mkinitcpio post hook. Create the following script and make it executable:

If you are using a unified kernel image, it must also be signed. Create a mkinitcpio post hook that will sign it.

Copy  to a FAT formatted file system (you can use the EFI system partition).

Reboot and enable Secure Boot. If shim does not find the certificate  is signed with in MokList it will launch MokManager ().

In MokManager select Enroll key from disk, find  and add it to MokList. When done select Continue boot and your boot loader will launch and it will be capable launching any binary signed with your Machine Owner Key.

## shim with key and GRUB
See GRUB#Shim-lock for instructions.

## Delete enrolled hash/key
Every entry of hash/key enrolled in the MOK database eats up a little piece of space of NVRAM. You may want to delete useless hash/key to free the space and to prevent outdated programs from booting.

MOK database can be managed with .

List enrolled keys and hashes:

 # mokutil --list-enrolled

Remove hash from database. The password entered here will be asked for confirmation to delete in MOK manager.

Remove key from database:

 # mokutil --delete MOK.cer

List hashes/keys to be deleted on next reboot:

 # mokutil --list-delete

On next reboot, MOK manager will be initiated with option to Enroll/Delete hashes/keys. See  for more details.

## Remove shim
Uninstall , remove the copied shim and MokManager files and rename back your boot loader.

## Protecting Secure Boot
The only way to prevent anyone with physical access from disabling Secure Boot is to protect the firmware settings with a password. Most UEFI firmwares provide such a feature, usually listed under the "Security" section in the firmware settings.

Consider enabling kernel lockdown mode. See [https://stackoverflow.com/a/60104165.

## Tips and tricks
## ISO repacking
It is possible to unpack and repack the official installation image using  and . This way, you can create an image that supports Secure Boot, either with custom keys or with a signed boot loader.

## Sign the official ISO with custom keys
Support for Secure Boot using custom keys can be added to the official ISO by simply extracting the boot loader ( and ), kernel, UEFI shell, signing them and then repacking the ISO with the signed files. Follow the steps below, or use  for an automated alternative.

First extract the relevant files and El Torito boot images:

 option  as used by mkarchiso makes the files on ISO 9660 read-only which persists after extracting them. Make the files writable so that they can be modified:

 $ chmod +w BOOTx64.EFI BOOTIA32.EFI shellx64.efi vmlinuz-linux

Sign the files. To do so with , for example:

 $ sbsign --key db.key --cert db.crt --output BOOTx64.EFI BOOTx64.EFI
 $ sbsign --key db.key --cert db.crt --output BOOTIA32.EFI BOOTIA32.EFI
 $ sbsign --key db.key --cert db.crt --output shellx64.efi shellx64.efi
 $ sbsign --key db.key --cert db.crt --output vmlinuz-linux vmlinuz-linux

Copy the signed EFI binaries to . It will be used as the EFI system partition and will be listed as an El Torito UEFI boot image. The size of  is fixed, but there are 8 MiB free space added by mkarchiso (for the purposes of rounding/alignment, to account for reserved sectors, etc.), so the size increase from the signatures should not be an issue.

 $ mcopy -D oO -i eltorito_img2_uefi.img vmlinuz-linux ::/arch/boot/x86_64/vmlinuz-linux
 $ mcopy -D oO -i eltorito_img2_uefi.img BOOTx64.EFI BOOTIA32.EFI ::/EFI/BOOT/
 $ mcopy -D oO -i eltorito_img2_uefi.img shellx64.efi ::/

Repack the ISO using the modified El Torito UEFI boot image and add the signed EFI binaries to ISO 9660:

Boot the resulting .

## Replacing the boot loader with PreLoader
Another way to add Secure Boot support to the official ISO is by extracting the boot loader and replacing it with #PreLoader.

First, extract the boot loader and the El Torito boot image:

Replace the  file with PreLoader:

Add the new files to the boot image:

 $ mcopy -D oO -i eltorito_img2_uefi.img BOOTx64.EFI loader.efi HashTool.efi ::/EFI/BOOT/

Finally, repack the ISO using the modified boot image and the new boot loader files:

## Sign the official ISO with a Machine Owner Key for shim
Support for Secure Boot using shim with a Machine Owner Key (MOK) can be added to the official ISO by extracting the boot loader, kernel and UEFI shell, signing them and then repacking the ISO with the signed files and shim.

First extract the relevant files and El Torito boot images. The boot loader file name will need to be  so that shim can find it.

 option  as used by mkarchiso makes the files on ISO 9660 read-only which persists after extracting them. Make the files writable so that they can be modified:

 $ chmod +w grubx64.efi shellx64.efi vmlinuz-linux

Sign the files with your MOK:

 $ sbsign --key MOK.key --cert MOK.crt --output grubx64.efi grubx64.efi
 $ sbsign --key MOK.key --cert MOK.crt --output shellx64.efi shellx64.efi
 $ sbsign --key MOK.key --cert MOK.crt --output vmlinuz-linux vmlinuz-linux

Acquire pre-signed shim EFI binaries, e.g. by installing . Place shim and MokManager in the current directory and change the shim EFI binary's file name to :

 $ cp /usr/share/shim-signed/shimx64.efi BOOTx64.EFI
 $ cp /usr/share/shim-signed/mmx64.efi ./

Copy shim, MokManager, the signed EFI binaries and the DER format MOK to . It will be used as the EFI system partition and will be listed as an El Torito UEFI boot image. The size of  is fixed, but there are 8 MiB free space added by mkarchiso (for the purposes of rounding/alignment, to account for reserved sectors, etc.), so the size increase from the added files should not be an issue.

 $ mcopy -D oO -i eltorito_img2_uefi.img vmlinuz-linux ::/arch/boot/x86_64/vmlinuz-linux
 $ mcopy -D oO -i eltorito_img2_uefi.img MOK.cer shellx64.efi ::/
 $ mcopy -D oO -i eltorito_img2_uefi.img BOOTx64.EFI grubx64.efi mmx64.efi ::/EFI/BOOT/

Repack the ISO using the modified El Torito UEFI boot image and add shim, MokManager, the signed EFI binaries and the DER format MOK to ISO 9660:

Boot the resulting . When MokManager launches, select Enroll key from disk > ARCHISO_EFI > MOK.cer. After enrolling the key, reboot and at the next boot, the live environment will successfully boot.

## Enrolling Option ROM digests
Option ROMs (OpROMs), i.e. device firmware that is executed during boot, must be signed for Secure Boot otherwise the devices will not be initialized. Typically OpROMs are signed with the Microsoft 3rd Party UEFI CA certificate which may prevent implementing Secure Boot with only your own keys. To solve this, the SHA256 digests of OpROMs can be enrolled instead.

On systems with a TPM, it is possible to acquire Option ROM SHA256 digests from the TPM event log.

Install  and .

Use  to read  and look for the digests of .For example:

This will print an easy to parse list of digests:

 # tpm2_eventlog /sys/kernel/security/tpm0/binary_bios_measurements | grep -o 'Digest: "[a-f0-9\{64\}"' | sed 's/Digest: "//;s/"$//'

Use  to create an EFI signature list for each OpROM digest you find:

 $ digest-to-efi-sig-list 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef OpROM1.esl
 $ digest-to-efi-sig-list fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210 OpROM2.esl

In case you have multiple OpROMs, combine their EFI signature lists into one so that it could be signed as a single file:

 $ cat OpROM1.esl OpROM2.esl > OpROM.esl

You could use a bash script like this if you have a lot of digests.

Sign the EFI signature list for appending to the Signature Database:

 $ sign-efi-sig-list -a -g "$(< GUID.txt)" -k KEK.key -c KEK.crt db OpROM.esl OpROM.auth

Enroll it.

The final and most dangerous step is to remove Microsoft 3rd Party UEFI CA certificate from the Signature Database and see if the system still boots and all devices still work.
