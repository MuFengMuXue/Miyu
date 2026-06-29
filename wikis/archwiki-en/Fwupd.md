# Fwupd

fwupd is a simple daemon to allow session software to update device firmware on your local machine. It's designed for desktops, but also usable on phones and headless servers.

Supported devices are listed here and more are to come.

## Installation
Install the  package.

Most peripherals can be updated directly in the OS. However, BIOS/UEFI updates generally require UEFI mode (UpdateCapsule), where the firmware applies the update safely on reboot. See #Setup for UEFI upgrade if you intend such use.

## Graphical front-ends
Certain desktop environments front-end solutions have built-in fwupd support:

*
*
*

## Usage
The package provides a  which will automatically start the fwupd daemon when the first query is received. To display all devices detected by fwupd:

 $ fwupdmgr get-devices

To download the latest metadata from the [https://fwupd.org/ Linux Vendor firmware Service (LVFS):

 $ fwupdmgr refresh

To list updates available for any devices on the system:

 $ fwupdmgr get-updates

To install updates:

 $ fwupdmgr update

## Configuration
## Disable local cache server (passim)
fwupd v1.9.5 from September 2023 introduced a dependency on , a local cache server intended to help reduce LVFS bandwidth usage by making each machine able to serve the metadata file it downloads everyday to otherspassimd is a daemon which listens for connections on port  from any IP addresses (i.e. it listens on ). This has led to some criticism regarding the security implications[https://github.com/fwupd/fwupd/issues/6721and indeed several vulnerabilities were reported just a few weeks later[https://security.opensuse.org/2023/10/27/passim-local-caching-server.htmlOn Arch the request from  to make the dependency optional at compile-time was denied because it would require creating a split-package for a library.

As a consequence, if you wish to disable passimd you should follow the advice given by the author[https://people.freedesktop.org/~hughsient/temp/Passim.pdf: add  to  under the  section and mask .

## Setup for UEFI upgrade
The following requirements should be met:

# Make sure you are booted in UEFI mode, because it will not work in legacy boot mode.
# Verify your EFI variables are accessible.
# Mount your EFI system partition (ESP) properly.  is used to denote the mountpoint in this section.
# Make sure the optional dependency  is installed and the associated systemd unit is started before fwupd unit; it will provide UEFI firmware upgrade support.

## Prepare ESP
fwupd will copy all the necessary files over to the , but for this to work, a basic folder layout must be present on your ;
this constitutes the creation of an  directory on your :

 # mkdir esp/EFI/

Restart the  unit afterwards. You can now  and . You will be prompted to reboot (into the firmware updater).

## Secure Boot
Currently, fwupd relies on shim to chainload the fwupd EFI binary on systems with Secure Boot enabled; for this to work, shim has to be installed correctly.

## Using your own keys
## Assisted process with sbctl
You can sign the UEFI executable with . For an explanation of how to setup sbctl, see Unified Extensible Firmware Interface/Secure Boot with sbctl.

 # sbctl sign -s -o /usr/lib/fwupd/efi/fwupdx64.efi.signed /usr/lib/fwupd/efi/fwupdx64.efi

Then after each update of , the UEFI executable will be automatically signed, thanks to the sbctl pacman hook ().

Finally, you have to set  in  and restart :

## Manual process
Alternatively, you can manually sign the UEFI executable used to perform upgrades, which is located in . The signed UEFI executable is expected in . Using , this can be achieved by running:

 # sbsign --key keyfile --cert certfile /usr/lib/fwupd/efi/fwupdx64.efi

To automatically sign this file when installed or upgraded, a Pacman hook can be used:

Make sure to replace  and  with the corresponding paths of your keys.

Instead of a pacman hook, you can also create a symlink from  to , and add the file to the  list in .

Finally, you have to set  in  and restart :

See https://github.com/fwupd/fwupd/issues/669 for more information.

## Troubleshooting
## Stuck when rebooting
 reports no error, but the reboot it prompts stuck and holding the power button has no response. Try switching off the power, or press the reset button (on a laptop, it might be a hole on the back) to force-reboot.

## No error but no upgrade on reboot
Symptom:  reports no error and prompts for reboot (e.g., on BIOS update). However, the system reboots normally (or stuck) and the firmware update does NOT happen.

Possible cause: In BIOS settings changing the boot order must be allowed.

Possible other solution if there are multiple updates pending: Try updating packages one at a time. Use the following to select packages:

 $ fwupdmgr update update_ID

(Where  is something like .)

## read-only filesystem error
At least  1.5.2 deduces the wrong mount point if bind is used to mount the EFI system partition to /boot. Consequently it fails to write the UEFI update file to  ( while it should be written to .) This results in a (misleading)  error message. In case the update was performed by  (or any other fwupd-capable Update GUI), no error or misleading errors may be shown.

As a workaround, run  first if it was bind-mounted to  before, then run  to write the UEFI update file to ,  and reboot the system to perform the UEFI update.

## UEFI ESP partition not detected or configured
If the EFI system partition (ESP) is still not detected after all requirements in #Setup for UEFI upgrade are met, the mount point can be specified manually:

See the relevant article in the fwupd wiki for additional reasons that this might occur.

Setting the ESP location prevents  from being installed in unwanted EFI system partitions located on other disks.

## MSR plugin is failing to load
The MSR plugin allows querying the state of DCI, a debugging interface available for Intel CPUs that should be disabled on production machines according to fwupd's documentation.

This plugin needs the  kernel module loaded.  is a built-in kernel module in all the official Arch Linux kernel packages, but unofficial kernel packages might have it as a loadable kernel module. In the latter case, we need to explicitly load the module at boot.
