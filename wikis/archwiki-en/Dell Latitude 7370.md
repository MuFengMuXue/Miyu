# Dell Latitude 7370

These laptops are a part of the Latitude 13 7000 Series featuring Intel Skylake This series does have some relation to the Dell XPS 13 (2016) for general reference.

## Dock
The TB15 Thunderbolt dock is no longer supported by DELL, and is no longer being sold [http://www.itcentralpoint.com/dell-recalls-tb15-docking-station. The TB15 thunderbolt dock is still a work-in-progress for support, but the use of it is anecdotal It seems to currently work best when plugged in before booting and avoiding any form of hot-plugging [https://github.com/01org/thunderbolt-software/issues/2.

The TB15 has been replaced by the TB16 Alternative, the WD15 seems to work as an alternative docking station [https://www.dell.com/en-us/shop/dell-dock-wd15-with-180w-adapter/apd/450-aeuo/pc-accessories.

## Updating BIOS
Download the BIOS update from the DELL website and place it either at the root of a FAT-formatted USB disk, or within  on the hard drive (if using EFI). Reboot and hit  during startup, selecting "BIOS Flash Update". The simple file browser should see the executable, select it and allow the update to occur.

## Card reader
The Broadcom reader "should work" via  and , but requires an firmware/BIOS update that must be run in Windows Supporting documentation regarding the card reader: [https://ludovicrousseau.blogspot.fr/2016/08/broadcom-ccid-readers.html == Touchpad ==

There is a known issue where the touchpad is detected as "ImPS/2 BYD TouchPad", a patch is in the works [https://patchwork.kernel.org/patch/9204273/.

## Display
Due to being HiDPI it is also common to notice latency when using desktop environments like GNOME. Installing  appears to alleviate some of these issues.

## DisplayLink
In order to connect to external projectors using an external dongle, you will need to configure DisplayLink.

## Known issues
## Suspend
It appears the system can get into a state in which suspend will stop working (system will suspend but upon attempt to resume will cold boot)https://bbs.archlinux.org/viewtopic.php?id=207543. Current resolution appears to be to perform a shutdown within the system and suspend should start working again. Newer BIOS versions also have improved this issue, though it can still occur.

## No keyboard
It appears that on  the system will boot without a keyboard. This can be resolved by adding  to the  array in mkinitcpio.conf.
