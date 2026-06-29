# GRUB/Tips and tricks

## Alternative installation methods
## Install to external USB stick
## BIOS
Assume your USB stick's first partition is FAT32 and its partition is /dev/sdy1

 # mount --mkdir /dev/sdy1 /mnt/usb
 # grub-install --target=i386-pc --debug --boot-directory=/mnt/usb/boot /dev/sdy
 # grub-mkconfig -o /mnt/usb/boot/grub/grub.cfg

Optionally backup configuration files of :

 # mkdir -p /mnt/usb/etc/default
 # cp /etc/default/grub /mnt/usb/etc/default
 # cp -a /etc/grub.d /mnt/usb/etc

 # sync; umount /mnt/usb

## EFI
For removable installations you have to use  and specify both  and . # grub-install --target=x86_64-efi --bootloader-id=GRUB --efi-directory=/mnt/usb --boot-directory=/mnt/usb/boot --removable

## Install to partition or partitionless disk
To set up grub to a partition boot sector, to a partitionless disk (also called superfloppy) or to a floppy disk, run (using for example  as the  partition):

 # chattr -i /boot/grub/i386-pc/core.img
 # grub-install --target=i386-pc --debug --force /dev/sdaX
 # chattr +i /boot/grub/i386-pc/core.img

You need to use the  option to allow usage of blocklists and should not use  (which is similar to simply generating ).

 will give out warnings like which should give you the idea of what might go wrong with this approach:

 /sbin/grub-setup: warn: Attempting to install GRUB to a partitionless disk or to a partition. This is a BAD idea.
 /sbin/grub-setup: warn: Embedding is not possible. GRUB can only be installed in this setup by using blocklists.
                         However, blocklists are UNRELIABLE and their use is discouraged.

Without  you may get the below error and  will not setup its boot code in the partition boot sector:

 /sbin/grub-setup: error: will not proceed with blocklists

With  you should get:

 Installation finished. No error reported.

The reason why  does not by default allow this is because in case of partition or a partitionless disk is that GRUB relies on embedded blocklists in the partition bootsector to locate the  file and the prefix directory . The sector locations of  may change whenever the file system in the partition is being altered (files copied, deleted etc.). For more info, see https://bugzilla.redhat.com/show_bug.cgi?id=728742 and https://bugzilla.redhat.com/show_bug.cgi?id=730915.

The workaround for this is to set the immutable flag on  (using  command as mentioned above) so that the sector locations of the  file in the disk is not altered. The immutable flag on  needs to be set only if GRUB is installed to a partition boot sector or a partitionless disk, not in case of installation to MBR or simple generation of  without embedding any bootsector (mentioned above).

Unfortunately, the  file that is created will not contain the proper UUID in order to boot, even if it reports no errors. see https://bbs.archlinux.org/viewtopic.php?pid=1294604#p1294604.
In order to fix this issue the following commands:

 # mount /dev/sdxY /mnt        #Your root partition.
 # mount /dev/sdxZ /mnt/boot   #Your boot partition (if you have one).
 # arch-chroot /mnt

Now, install , then:

 # grub-mkconfig -o /boot/grub/grub.cfg

## Generate core.img alone
To populate the  directory and generate a  file without embedding any GRUB bootsector code in the MBR, post-MBR region, or the partition bootsector, add  to :

 # grub-install --target=i386-pc --grub-setup=/bin/true --debug /dev/sda

You can then chainload GRUB's  from GRUB Legacy or syslinux as a Linux kernel or as a multiboot kernel (see also Syslinux#Chainloading).

## GUI configuration tools
*

## Drop-in configuration
Since [https://gitlab.archlinux.org/archlinux/packaging/packages/grub/-/commit/beee9df4ae2e3b2150d4e54b3825064e77661cb4 GRUB 2.12-1, in addition to the main configuration file , drop-in configuration snippets are, if any, read by  from , and naturally, they have higher precedence than and override the main  configuration file, are sourced lexicographically, and so on.  This is an alternative to editing  directly, and every mention of editing  can be made to drop-ins located in this folder.

## Visual configuration
In GRUB it is possible, by default, to change the look of the menu. Make sure to initialize the GRUB graphical terminal, gfxterm, in :

 GRUB_TERMINAL_OUTPUT="gfxterm"

## Setting the framebuffer resolution
GRUB can set the framebuffer for both GRUB itself () and the kernel (). The old  way is deprecated. The preferred method is editing  to set width (pixels) x height (pixels) x color depth:

 GRUB_GFXMODE=1024x768x32
 GRUB_GFXPAYLOAD_LINUX=keep

Multiple resolutions can be specified, including the default , so it is recommended that you edit the line to resemble . For more information, refer to the GRUB gfxmode documentation. The gfxpayload property will make sure the kernel keeps the resolution.

If this method does not work for you, the deprecated  method will still work. Just add it next to the  line in  for example:  will give you a  resolution.

## Background image and bitmap fonts
GRUB comes with support for background images and bitmap fonts in  format. The GNU Unifont font is included in the  package under the filename , or, as only ASCII characters under the name . Run  to get the file paths.

Image formats supported include JPEG, PNG and TGA, providing the correct modules are loaded. The maximum supported resolution depends on your hardware.

Make sure you have set up the proper framebuffer resolution.

Edit  like this:

 GRUB_BACKGROUND="/boot/grub/myimage"
 #GRUB_THEME="/path/to/gfxtheme"
 GRUB_FONT="/path/to/font.pf2"

Re-generate  to apply the changes. If adding the splash image was successful, the user will see  in the terminal as the command is executed. If this phrase is not seen, the image information was probably not incorporated into the  file.

If the image is not displayed, check:

* The path and the filename in  are correct
* The image is of the proper size and format (tga, png, 8-bit jpg)
* The image was saved in the RGB mode, and is not indexed
* The console mode is not enabled in
* The command  must be executed to place the background image information into the  file
* The  scripts will not quote the file name in  so make sure it does not contain spaces

## Theme
Here is an example for configuring Starfield theme which was included in GRUB package.

Edit :

 GRUB_THEME="/usr/share/grub/themes/starfield/theme.txt"

Re-generate  to apply the changes. If configuring the theme was successful, you will see  in the terminal.

Your splash image will usually not be displayed when using a theme.

## Menu colors
You can set the menu colors in GRUB. The available colors for GRUB can be found in the GRUB Manual.
Here is an example:

Edit :

 GRUB_COLOR_NORMAL="light-blue/black"
 GRUB_COLOR_HIGHLIGHT="light-cyan/blue"

## Hidden menu
One of the unique features of GRUB is hiding/skipping the menu and showing it by holding  when needed. You can also adjust whether you want to see the timeout counter.

Edit  as you wish. Here are the lines you need to add to enable this feature, the timeout has been set to five seconds and to be shown to the user:

 GRUB_TIMEOUT=5
 GRUB_TIMEOUT_STYLE='countdown'

 is how many seconds before displaying menu.

## Disable framebuffer
Users who use NVIDIA proprietary driver might wish to disable GRUB's framebuffer as it can cause problems with the binary driver.

To disable framebuffer, edit  and uncomment the following line:

 GRUB_TERMINAL_OUTPUT=console

Another option if you want to keep the framebuffer in GRUB is to revert to text mode just before starting the kernel. To do that modify the variable in :

 GRUB_GFXPAYLOAD_LINUX=text

## Language
 utilizes   for translations. The language used is determined by the Locale#Variables.

You can temporarily override the Locale when running  to generate config in a specific language, for example English (C locale):

 # LC_ALL=C grub-mkconfig -o /boot/grub/grub.cfg

## Booting ISO9660 image file directly via GRUB
GRUB supports booting from ISO images directly via loopback devices, see Multiboot USB drive#Using GRUB and loopback devices for examples.

## Password protection of GRUB menu
If you want to secure GRUB so it is not possible for anyone to change boot parameters or use the command line, you can add a username and password to GRUB's configuration files. To do this, run the command , then enter a password and confirm it:

Then, adjust permissions on  such that only root can read it by running . Then modify the file as following:

where  is the string starting with grub.pbkdf2 generated by .

Regenerate your configuration file with . Accessing the GRUB command line, boot parameters and also booting an entry now require the specified username and password. The latter can be prevented by following #Password protection of GRUB edit and console options only.

This can be relaxed and further customized with configuring more users as described in the "Security" part of the GRUB manual.

## Password protection of GRUB edit and console options only
Adding  to a menu entry will allow any user to boot the OS while preventing the user from editing the entry and preventing access to the grub command console.
Only a superuser or users specified with the  switch will be able to edit the menu entry.

In order to make Linux entries , the  variable in the beginning of  can be modified.

## Hide GRUB unless the Shift key is held down
In order to achieve the fastest possible boot, instead of having GRUB wait for a timeout, it is possible for GRUB to hide the menu unless the  key is held down or the  or  key is pressed during GRUB's start-up.

In order to achieve this, you should add the following lines to :

 GRUB_TIMEOUT=0
 GRUB_TIMEOUT_STYLE=hidden

Then regenerate the grub configuration:

 # grub-mkconfig -o /boot/grub/grub.cfg

## Combining the use of UUIDs and basic scripting
If you like the idea of using UUIDs to avoid unreliable BIOS mappings or are struggling with GRUB's syntax, here is an example boot menu item that uses UUIDs and a small script to direct GRUB to the proper disk partitions for your system. All you need to do is replace the UUIDs in the sample with the correct UUIDs for your system. The example applies to a system with a boot and root partition. You will obviously need to modify the GRUB configuration if you have additional partitions:

{{bc|
menuentry "Arch Linux 64" {
    # Set the UUIDs for your boot and root partition respectively
    set the_boot_uuid=ece0448f-bb08-486d-9864-ac3271bd8d07
    set the_root_uuid=c55da16f-e2af-4603-9e0b-03f5f565ec4a

    # (Note: This may be the same as your boot partition)

    # Get the boot/root devices and set them in the root and grub_boot variables
    search --fs-uuid $the_root_uuid --set=root
    search --fs-uuid $the_boot_uuid --set=grub_boot

    # Check to see if boot and root are equal.
    # If they are, then append /boot to $grub_boot (Since $grub_boot is actually the root partition)
    if [ $the_boot_uuid == $the_root_uuid ] ; then
        set grub_boot=($grub_boot)/boot
    else
        set grub_boot=($grub_boot)
    fi

    # $grub_boot now points to the correct location, so the following will properly find the kernel and initramfs
    linux $grub_boot/vmlinuz-linux root=/dev/disk/by-uuid/$the_root_uuid ro
    initrd $grub_boot/initramfs-linux.img
}
}}

## Multiple entries
## Disable submenu
If you have multiple kernels installed, say linux and linux-lts, by default  groups them in a submenu. If you do not like this behaviour you can go back to one single menu by adding the following line to :

 GRUB_DISABLE_SUBMENU=y

## Recall previous entry
GRUB can remember the last entry you booted from and use this as the default entry to boot from next time. This is useful if you have multiple kernels (i.e., the current Arch one and the LTS kernel as a fallback option) or operating systems. To do this, edit  and change the value of :

 GRUB_DEFAULT=saved

This ensures that GRUB will default to the saved entry. To enable saving the selected entry, add the following line to :

 GRUB_SAVEDEFAULT=true

This will only work if /boot is not a btrfs, because grub cannot write to btrfs.  But it will generate a misleading error message: "sparse file not allowed. Press any key to continue.".

## Changing the default menu entry
To change the default selected entry, edit  and change the value of :

Using menu titles:

 GRUB_DEFAULT='Advanced options for Arch Linux>Arch Linux, with Linux linux'

Using numbers:

 GRUB_DEFAULT="1>2"

Grub identifies entries in the generated menu (i.e. ) counted from zero. That means  for the first entry which is the default value,  for the second and so on. Main and submenu entries are separated
by a  and are both identified by a number, title, or ID.

The example above boots the third entry from the main menu 'Advanced options for Arch Linux'.

Using IDs (see value after --id or $menuentry_id_option in grub.cfg if generating your grub.cfg):

 GRUB_DEFAULT="gnulinux-advanced-39c666d6-c7fc-4fa6-8287-9540056f5a02>gnulinux-linux-zen-advanced-39c666d6-c7fc-4fa6-8287-9540056f5a02"

Documentation of all three identifier methods: https://www.gnu.org/software/grub/manual/grub/html_node/default.html

## Boot non-default entry only once
The command  is very helpful to boot another entry than the default only once. GRUB loads the entry passed in the first command line argument, when the system is rebooted the next time. Most importantly GRUB returns to loading the default entry for all future booting. Changing the configuration file or selecting an entry in the GRUB menu is not necessary.

{{Note|This requires  in  (and then regenerating ) or, in case of hand-made , the line {{ic|1=set default="${saved_entry}"}}.}}

## Play a tune
You can play a tune through the PC-speaker while booting (right before the menu appears) by modifying the variable :

 GRUB_INIT_TUNE="tempo note_duration second_note_duration ..."

You can add a menu entry to play each of these common  samples by creating the linked  and then re-running .

For information on this, you can look at , while some collections exist.

## Manual configuration of core image for early boot
If you require a special keymap or other complex steps that GRUB is not able to configure automatically in order to make  available to the GRUB environment, you can generate a core image yourself. On UEFI systems, the core image is the  file that is loaded by the firmware on boot. Building your own core image will allow you to embed any modules required for very early boot, as well as a configuration script to bootstrap GRUB.

Firstly, taking as an example a requirement for the  keymap embedded in early-boot in order to enter a password for an encrypted  on a UEFI system:

Determine from the generated  file what modules are required in order to mount the crypted . For instance, under your  you should see lines similar to:

Take note of all of those modules: they will need to be included in the core image. Now, create a tarball containing your keymap. This will be bundled in the core image as a memdisk:

 # grub-kbdcomp -o dvorak.gkb dvorak
 # tar cf memdisk.tar dvorak.gkb

Now create a configuration file to be used in the GRUB core image. This is in the same format as your regular grub config, but need contain only a few lines to find and load the main configuration file on the  partition:

Finally, generate the core image, listing all of the modules determined to be required in the generated , along with any modules used in the  script. The example above needs , , ,  and .

 # grub-mkimage -c early-grub.cfg -o grubx64.efi -O x86_64-efi -m memdisk.tar diskfilter cryptodisk luks gcry_rijndael gcry_sha256 ext2 memdisk tar at_keyboard keylayouts configfile

The generated EFI core image can now be used in the same way as the image that is generated automatically by : place it in your EFI system partition and enable it with , or configure as appropriate for your system firmware.

See also Debian cryptsetup docs.

## UEFI further reading
Below is other relevant information regarding installing Arch via UEFI.

## Alternative install method
Usually, GRUB keeps all files, including configuration files, in , regardless of where the EFI system partition is mounted.

If you want to keep these files inside the EFI system partition itself, add  to the grub-install command:

 # grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id=grub --boot-directory=esp --debug

This puts all GRUB files in , instead of in . When using this method, make sure you have grub-mkconfig put the configuration file in the same place:

 # grub-mkconfig -o esp/grub/grub.cfg

Configuration is otherwise the same.

## UEFI firmware workaround
See GRUB#Default/fallback boot path.

## GRUB standalone
This section assumes you are creating a standalone GRUB for x86_64 systems (x86_64-efi). For 32-bit (IA32) EFI systems, replace  with  where appropriate.

It is possible to create a  application which has all the modules embedded in a tar archive within the UEFI application, thus removing the need to have a separate directory populated with all of the GRUB UEFI modules and other related files. This is done using the  command (included in ) as follows:

 # echo 'configfile ${cmdpath}/grub.cfg' > /tmp/grub.cfg
 # grub-mkstandalone -d /usr/lib/grub/x86_64-efi/ -O x86_64-efi --modules="part_gpt part_msdos" --locales="en@quot" --themes="" -o "esp/EFI/grub/grubx64_standalone.efi" "boot/grub/grub.cfg=/tmp/grub.cfg" -v

Then copy the GRUB configuration file to  and create a UEFI Boot Manager entry for  using efibootmgr.

{{Note|The option  (with the quotes) is necessary for the {{ic|${cmdpath} }} feature to work properly.}}

{{Warning|
* You may find that the  file is not loaded due to {{ic|${cmdpath} }} missing a slash (i.e.  instead of ) and so you are dropped into a GRUB shell. If this happens determine what {{ic|${cmdpath} }} is set to ({{ic|echo ${cmdpath} }}) and then load the configuration file manually (e.g. ).
* If Secure Boot with shim is used, remember to add the SBAT section using .
}}

## Technical information
The GRUB EFI file always expects its configuration file to be at {{ic|${prefix}/grub.cfg}}. However in the standalone GRUB EFI file, the {{ic|${prefix} }} is located inside a tar archive and embedded inside the standalone GRUB EFI file itself (inside the GRUB environment, it is denoted by , without quotes). This tar archive contains all the files that would be stored normally at  in case of a normal GRUB EFI install.

Due to this embedding of  contents inside the standalone image itself, it does not rely on actual (external)  for anything. Thus in case of standalone GRUB EFI file {{ic|1=${prefix}==(memdisk)/boot/grub}} and the standalone GRUB EFI file reads expects the configuration file to be at {{ic|1=${prefix}/grub.cfg==(memdisk)/boot/grub/grub.cfg}}.

Hence to make sure the standalone GRUB EFI file reads the external  located in the same directory as the EFI file (inside the GRUB environment, it is denoted by {{ic|${cmdpath} }}), we create a simple  which instructs GRUB to use {{ic|${cmdpath}/grub.cfg}} as its configuration ({{ic|configfile ${cmdpath}/grub.cfg}} command in ). We then instruct grub-mkstandalone to copy this  file to {{ic|${prefix}/grub.cfg}} (which is actually ) using the option .

This way, the standalone GRUB EFI file and actual  can be stored in any directory inside the EFI system partition (as long as they are in the same directory), thus making them portable.

## UEFI and BIOS installation
If your arch installation should be bootable on both UEFI and BIOS systems, install GRUB using both methods. Partition the disk as GPT, create an EFI system partition and a BIOS boot partition as well, mount the ESP at  and run the GRUB install commands for both ways.

 # grub-install --target=i386-pc --recheck /dev/sdx
 # grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB --recheck

In a BIOS system the EFI variables are not present, thus the UEFI NVRAM boot entries cannot be set and the 2nd command will report an error. By using the  and  option the system will have a good chance to be bootable in UEFI mode too:

 # grub-install --target=i386-pc --recheck /dev/sdx
 # grub-install --target=x86_64-efi --efi-directory=/efi --recheck --removable --no-nvram

For some BIOS implementations it may be necessary to set the PMBR’s boot flag, e.g. with parted

 (parted) disk_set pmbr_boot on

## Speeding up LUKS decryption in GRUB
Upon boot GRUB may in some cases take a long time to verify the password. This can be due to a high cost parameters of the key derivation function, which you can check as follows:

 # cryptsetup luksDump /dev/sda3

The problem is that the cost parameters for a given keyslot are generated when the key is added to ensure a balance between being high enough to protect against brute force attacks and low enough to allow for fast key derivation by estimating the capabilities of your computer. However, when GRUB is started, it might not have the same computational resources at hand, thus being vastly slower.

If your password provides enough entropy to counter common attacks by itself, you can lower the parameters. For example to lower the iteration count of PBKDF2, use:

 # cryptsetup luksChangeKey --pbkdf-force-iterations 1000 /dev/sda3

A minimum of 1000 iterations is recommended as per RFC 2898, but you should aim for higher values if you can (The cost for an attacker as well as the time for key derivation scale linearly).

Recommended parameters for Argon2 are discussed in RFC 9106.

## Decrypt LUKS protected disk with the TPM
In recent version of GRUB (since ), it is possible to use the TPM to unlock an encrypted disk. It is useful if  partition is encrypted as it avoids the need to enter the passphrase at boot and makes unattended boot possible.

The first step consists in creating a random LUKS key and adding it to the store. This is achieved as follows (ajust the  UUID to match the encrypted disk on your system):

 # dd if=/dev/urandom of=luks-key bs=1 count=32
 # cryptsetup luksAddKey /dev/disk/by-uuid/0228eb43-a7cc-4737-a0d3-cf784154feea luks-key --pbkdf=pbkdf2 --hash=sha512

The key can be sealed with the TPM and stored on the unencrypted esp partition as follows:

 # grub-protect --action=add --protector=tpm2 --tpm2-pcrs=7 --tpm2key --tpm2-keyfile=luks-key --tpm2-outfile=esp/EFI/GRUB/sealed.tpm

Note that the tpm2-pcrs parameter can be adjusted to your needs. See Trusted_Platform_Module#Accessing_PCR_registers for more information.

Create a early grub boot script in  with the following content:

In the above script, you need to adjust the UUID of the disk and the prefix to the  directory. In this example, the  directory is located in the  subvolume of a Btrfs filesystem.

Regenerate the GRUB efi binary and make sure to include all the modules you need.

 # grub-mkimage -p /boot/grub --disable-shim-lock -c /boot/grub/early-grub.cfg -o esp/EFI/GRUB/grubx64.efi -O x86_64-efi part_gpt cryptodisk luks2 gcry_rijndael gcry_sha256 gcry_sha512 btrfs tpm2_key_protector fat configfile tpm echo

If secure boot is enabled, don't forget to sign the grub efi binary. For instance with :

 # sbctl sign

See Unified_Extensible_Firmware_Interface/Secure_Boot for more information.
