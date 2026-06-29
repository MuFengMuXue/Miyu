# DSL SpeedTouch modem

This howto shows one way to get a working speedtouch USB modem. It uses the kernel driver, not the userspace driver. This howto assumes that your ISP uses PPPoA and not PPPoE.

## Kernel modules and ppp
Make sure you have a kernel with the proper support (at least the modules , , , ,  and ). The default Arch kernel should work.

Otherwise make sure that your kernel supports firmware loading:

 $ zgrep FW_LOADER /proc/config.gz

Then install the  package.

## The manual way
## Configuring pppd
The last entry depends on your country/ISP and is created from the VPI and VCI setting in the format . This page has a VPI / VCI Setting List.

You also need to configure /etc/ppp/pap-secrets or chap-secrets, depending on your ISP.  pap-secrets files are of the format:

See The PAP/CHAP secrets file for more details.

If you want to use the DNS servers provided by your ISP (you probably do!) then make a symlink /etc/resolv.conf pointing to /etc/ppp/resolv.conf:
 cd etc
 rm resolv.conf
 ln -s ppp/resolv.conf resolv.conf

## Configure udev
Make a file  and put something like the following in it:
 ACTION=="add", SUBSYSTEM=="atm", KERNEL=="speedtch*", RUN="/usr/bin/pppd call speedtch"

With this Udev will start pppd automatically, if you do not want this you can simply bring up your modem using
 pppd call speedtch

## Firmware
Now you have everything except the firmware loading. The easiest way is to let udev do it.  Download rev4fw.zip (note disclaimer here) and  unzip it. It contains two files, a small one and a big one. Copy the small file to  and the big one to

 # mkdir -p /usr/lib/firmware
 # cp small_file /usr/lib/firmware/speedtch-1.bin
 # cp large_file /usr/lib/firmware/speedtch-2.bin

If you cannot download this file then follow the instructions of the second link above and use the firmware extractor (or download another firmware which has the two files).

## Troubleshooting
If the modem is being detected correctly and the firmware is loading, you should see something like the following from dmesg:

The pppd output in the journal should look something like:

If you are having problems you can check pppd debug messages by adding debug to .  This can help identify authentication problems (e.g. pap vs chap auth), etc.  Otherwise make sure you check your VPI/VCI settings!
