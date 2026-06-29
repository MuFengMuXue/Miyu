As with any other piece of software, it is important to occasionally **update the firmware on an SSD** to ensure that the device is protected from any known firmware bugs; for example the [issues with 980 Pro devices failing into read-only mode unexpectedly](https://www.guru3d.com/news-story/samsung-issues-new-firmware-to-prevent-dying-980-pro-ssds.html).

Unfortunately Samsung have elected not to provide their firmware binaries to the [LVFS](https://wiki.gentoo.org/wiki/LVFS "LVFS") at this time, and as such there is no mechanism for updating this firmware without the use of the proprietary [Samsung Magician](https://semiconductor.samsung.com/consumer-storage/magician/) tool.

As Samsung do not provide a consolidated firmware update tool each model of SSD will need to be updated separately.

## [Updating the device]

There are two methods of updating the firmware on an Samsung SSD from Linux. Both methods begin by sourcing the appropriate firmware update `.iso` file for the device in question from the [Samsung website](https://www.samsung.com/semiconductor/minisite/ssd/download/tools/).

Once the appropriate ISO has been identified, download the file to a staging location. This example will be sourcing the Samsung 980 Pro firmware that contains fixes for the read-only issue.

`user `[`$`]`curl `[`https://semiconductor.samsung.com/resources/software-resources/Samsung_SSD_980_PRO_5B2QGXA7.iso`](https://semiconductor.samsung.com/resources/software-resources/Samsung_SSD_980_PRO_5B2QGXA7.iso)` -O`

At this point the two methods diverge. To update the firmware using the \'Official\' mechanism simply `dd` the `.iso` to an appropriate removable device and boot from that.

** Warning**\
The following instructions are not approved by Samsung and, though it is unlikely, may result in data loss. It is always safest to use the vendor\'s official update mechanism; in cases where this is not possible (or for the adventurous) the following instructions enable the use of the Samsung firmware updater tool on a Gentoo Linux system.

1.  Mount the `.iso` and extract the initrd to an appropriate location.

`user `[`$`]`mkdir /tmp/iso`

`user `[`$`]`sudo mount -o loop ./Samsung_SSD_980_PRO_5B2QGXA7.iso /tmp/iso/`

`user `[`$`]`mkdir /tmp/fwupdate`

`user `[`$`]`cd /tmp/fwupdate`

`user `[`$`]`gzip -dc /tmp/iso/initrd | cpio -idv --no-absolute-filenames`

`user `[`$`]`cd root/fumagician/`

1.  Run the `fumagician` binary as root. If possible (though this is not strictly required) unmount any file systems on the SSD(s) in question first.

`root `[`#`]`./fumagician`

The tool will report if any SSD in the system is eligible for the firmware included in the package and offer to perform the update if so.

Do not power off the device while the firmware update is in progress. Once the update is complete the system should be manually rebooted as soon as is practical.